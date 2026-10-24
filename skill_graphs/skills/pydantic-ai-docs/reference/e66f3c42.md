            response_modalities=modalities,
            image_config=image_config,
        )

        # Validate logprobs settings
        logprobs_requested = model_settings.get('google_logprobs')
        if logprobs_requested:
            config['response_logprobs'] = True

            if 'google_top_logprobs' in model_settings:
                config['logprobs'] = model_settings.get('google_top_logprobs')

        return contents, config

    def _process_response(self, response: GenerateContentResponse) -> ModelResponse:
        candidate = response.candidates[0] if response.candidates else None

        vendor_id = response.response_id
        finish_reason: FinishReason | None = None
        vendor_details: dict[str, Any] = {}

        raw_finish_reason = candidate.finish_reason if candidate else None
        if raw_finish_reason and candidate:  # pragma: no branch
            vendor_details = {'finish_reason': raw_finish_reason.value}
            # Add safety ratings to provider details
            if candidate.safety_ratings:
                vendor_details['safety_ratings'] = [r.model_dump(by_alias=True) for r in candidate.safety_ratings]
            finish_reason = _FINISH_REASON_MAP.get(raw_finish_reason)
        elif candidate is None and response.prompt_feedback and response.prompt_feedback.block_reason:
            block_reason = response.prompt_feedback.block_reason
            vendor_details['block_reason'] = block_reason.value
            if response.prompt_feedback.block_reason_message:
                vendor_details['block_reason_message'] = response.prompt_feedback.block_reason_message
            if response.prompt_feedback.safety_ratings:
                vendor_details['safety_ratings'] = [
                    r.model_dump(by_alias=True) for r in response.prompt_feedback.safety_ratings
                ]
            finish_reason = 'content_filter'

        if response.create_time is not None:  # pragma: no branch
            vendor_details['timestamp'] = response.create_time

        if candidate is None or candidate.content is None or candidate.content.parts is None:
            parts = []
        else:
            parts = candidate.content.parts or []

        if candidate and (logprob_results := candidate.logprobs_result):
            vendor_details['logprobs'] = logprob_results.model_dump(mode='json')
            vendor_details['avg_logprobs'] = candidate.avg_logprobs

        usage = _metadata_as_usage(response, provider=self._provider.name, provider_url=self._provider.base_url)
        grounding_metadata = candidate.grounding_metadata if candidate else None
        url_context_metadata = candidate.url_context_metadata if candidate else None

        return _process_response_from_parts(
            parts,
            grounding_metadata,
            response.model_version or self._model_name,
            self._provider.name,
            self._provider.base_url,
            usage,
            vendor_id=vendor_id,
            vendor_details=vendor_details or None,
            finish_reason=finish_reason,
            url_context_metadata=url_context_metadata,
        )

    async def _process_streamed_response(
        self, response: AsyncIterator[GenerateContentResponse], model_request_parameters: ModelRequestParameters
    ) -> StreamedResponse:
        """Process a streamed response, and prepare a streaming response to return."""
        peekable_response = _utils.PeekableAsyncStream(response)
        first_chunk = await peekable_response.peek()
        if isinstance(first_chunk, _utils.Unset):
            raise UnexpectedModelBehavior('Streamed response ended without content or tool calls')  # pragma: no cover

        return GeminiStreamedResponse(
            model_request_parameters=model_request_parameters,
            _model_name=first_chunk.model_version or self._model_name,
            _response=peekable_response,
            _provider_name=self._provider.name,
            _provider_url=self._provider.base_url,
            _provider_timestamp=first_chunk.create_time,
        )

    async def _map_messages(  # noqa: C901
        self, messages: list[ModelMessage], model_request_parameters: ModelRequestParameters
    ) -> tuple[ContentDict | None, list[ContentUnionDict]]:
        contents: list[ContentUnionDict] = []
        system_parts: list[PartDict] = []

        for m in messages:
            if isinstance(m, ModelRequest):
                message_parts: list[PartDict] = []

                for part in m.parts:
                    if isinstance(part, SystemPromptPart):
                        system_parts.append({'text': part.content})
                    elif isinstance(part, UserPromptPart):
                        message_parts.extend(await self._map_user_prompt(part))
                    elif isinstance(part, ToolReturnPart):
                        message_parts.append(
                            {
                                'function_response': {
                                    'name': part.tool_name,
                                    'response': part.model_response_object(),
                                    'id': part.tool_call_id,
                                }
                            }
                        )
                    elif isinstance(part, RetryPromptPart):
                        if part.tool_name is None:
                            message_parts.append({'text': part.model_response()})
                        else:
                            message_parts.append(
                                {
                                    'function_response': {
                                        'name': part.tool_name,
                                        'response': {'error': part.model_response()},
                                        'id': part.tool_call_id,
                                    }
                                }
                            )
                    else:
                        assert_never(part)

                # Work around a Gemini bug where content objects containing functionResponse parts are treated as
                # role=model even when role=user is explicitly specified.
                #
                # We build `message_parts` first, then split into multiple content objects whenever we transition
                # between function_response and non-function_response parts.
                #
                # TODO: Remove workaround when https://github.com/pydantic/pydantic-ai/issues/4210 is resolved
                if message_parts:
                    content_parts: list[PartDict] = []

                    for part in message_parts:
                        if (
                            content_parts
                            and 'function_response' in content_parts[-1]
                            and 'function_response' not in part
                        ):
                            contents.append({'role': 'user', 'parts': content_parts})
                            content_parts = []

                        content_parts.append(part)

                    contents.append({'role': 'user', 'parts': content_parts})
            elif isinstance(m, ModelResponse):
                maybe_content = _content_model_response(m, self.system)
                if maybe_content:
                    contents.append(maybe_content)
            else:
                assert_never(m)

        # Google GenAI requires at least one user part in the message, and that function call turns
        # come immediately after a user turn or after a function response turn.
        if not contents or contents[0].get('role') == 'model':  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
            contents.insert(0, {'role': 'user', 'parts': [{'text': ''}]})

        if instructions := self._get_instructions(messages, model_request_parameters):
            system_parts.append({'text': instructions})
        system_instruction = ContentDict(role='user', parts=system_parts) if system_parts else None

        return system_instruction, contents

    async def _map_user_prompt(self, part: UserPromptPart) -> list[PartDict]:  # noqa: C901
        if isinstance(part.content, str):
            return [{'text': part.content}]
        else:
            content: list[PartDict] = []
            for item in part.content:
                if isinstance(item, str):
                    content.append({'text': item})
                elif isinstance(item, BinaryContent):
                    inline_data_dict: BlobDict = {'data': item.data, 'mime_type': item.media_type}
                    part_dict: PartDict = {'inline_data': inline_data_dict}
                    if item.vendor_metadata:
                        part_dict['video_metadata'] = cast(VideoMetadataDict, item.vendor_metadata)
                    content.append(part_dict)
                elif isinstance(item, VideoUrl) and (
                    item.is_youtube or (item.url.startswith('gs://') and self.system == 'google-vertex')
                ):
                    # YouTube URLs work on both google-gla and google-vertex
                    # GCS URIs (gs://...) only work on google-vertex (Vertex AI can access GCS buckets)
                    # GCS on google-gla falls through to FileUrl which raises clear error on download attempt
                    # Other URLs fall through to FileUrl handling (download for google-gla)
                    # Note: force_download is not checked here, mirroring the original YouTube behavior.
                    # GCS URIs cannot be downloaded anyway ("gs://" protocol not supported for download).
                    file_data_dict: FileDataDict = {'file_uri': item.url, 'mime_type': item.media_type}
                    part_dict: PartDict = {'file_data': file_data_dict}
                    if item.vendor_metadata:
                        part_dict['video_metadata'] = cast(VideoMetadataDict, item.vendor_metadata)
                    content.append(part_dict)
                elif isinstance(item, FileUrl):
                    if item.force_download or (
                        # google-gla does not support passing file urls directly, except for youtube videos
                        # (see above) and files uploaded to the file API (which cannot be downloaded anyway)
                        self.system == 'google-gla'
                        and not item.url.startswith(r'https://generativelanguage.googleapis.com/v1beta/files')
                    ):
                        downloaded_item = await download_item(item, data_format='bytes')
                        inline_data: BlobDict = {
                            'data': downloaded_item['data'],
                            'mime_type': downloaded_item['data_type'],
                        }
                        part_dict: PartDict = {'inline_data': inline_data}
                        # VideoUrl is a subclass of FileUrl - include video_metadata if present
                        if isinstance(item, VideoUrl) and item.vendor_metadata:
                            part_dict['video_metadata'] = cast(VideoMetadataDict, item.vendor_metadata)
                        content.append(part_dict)
                    else:
                        file_data_dict: FileDataDict = {'file_uri': item.url, 'mime_type': item.media_type}
                        part_dict: PartDict = {'file_data': file_data_dict}
                        # VideoUrl is a subclass of FileUrl - include video_metadata if present
                        if isinstance(item, VideoUrl) and item.vendor_metadata:
                            part_dict['video_metadata'] = cast(VideoMetadataDict, item.vendor_metadata)
                        content.append(part_dict)  # pragma: lax no cover
                elif isinstance(item, UploadedFile):
                    # Verify provider matches
                    if item.provider_name != self.system:
                        raise UserError(
                            f'UploadedFile with `provider_name={item.provider_name!r}` cannot be used with GoogleModel. '
                            f'Expected `provider_name` to be `{self.system!r}`.'
                        )
                    # UploadedFile.file_id should be a URI from the Google Files API
                    if not item.file_id.startswith('https://'):
                        raise UserError(
                            f'UploadedFile for GoogleModel must use a file URI from the Google Files API, got: {item.file_id}'
                        )
                    file_data_dict: FileDataDict = {'file_uri': item.file_id, 'mime_type': item.media_type}
                    part_dict: PartDict = {'file_data': file_data_dict}
                    # Include video_metadata if present in vendor_metadata
                    if item.vendor_metadata:
                        part_dict['video_metadata'] = cast(VideoMetadataDict, item.vendor_metadata)
                    content.append(part_dict)
                elif isinstance(item, CachePoint):
                    # Google doesn't support inline CachePoint markers. Google's caching requires
                    # pre-creating cache objects via the API, then referencing them by name using
                    # `GoogleModelSettings.google_cached_content`. See https://ai.google.dev/gemini-api/docs/caching
                    pass
                else:
                    assert_never(item)
        return content

    def _map_response_schema(self, o: OutputObjectDefinition) -> dict[str, Any]:
        response_schema = o.json_schema.copy()
        if o.name:
            response_schema['title'] = o.name
        if o.description:
            response_schema['description'] = o.description

        return response_schema

```

---|---
####  __init__
```
__init__(
    model_name: GoogleModelName[](https://ai.pydantic.dev/api/models/google/#pydantic_ai.models.google.GoogleModelName "GoogleModelName



      module-attribute
   \(pydantic_ai.models.google.GoogleModelName\)"),
    *,
    provider: (
        ["google-gla", "google-vertex", "gateway"]
        | Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[Client]
    ) = "google-gla",
    profile: ModelProfileSpec | None = None,
    settings: ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None = None
)

```

Initialize a Gemini model.
Parameters:
Name | Type | Description | Default
---|---|---|---
`model_name` |  `GoogleModelName[](https://ai.pydantic.dev/api/models/google/#pydantic_ai.models.google.GoogleModelName "GoogleModelName



      module-attribute
   \(pydantic_ai.models.google.GoogleModelName\)")` |  The name of the model to use. |  _required_
`provider` |  `Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[Client]` |  The provider to use for authentication and API access. Can be either the string 'google-gla' or 'google-vertex' or an instance of `Provider[google.genai.AsyncClient]`. Defaults to 'google-gla'. |  `'google-gla'`
`profile` |  `ModelProfileSpec | None` |  The model profile to use. Defaults to a profile picked by the provider based on the model name. |  `None`
`settings` |  `ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None` |  The model settings to use. Defaults to None. |  `None`
Source code in `pydantic_ai_slim/pydantic_ai/models/google.py`
```
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
259
260
261
```
| ```
def __init__(
    self,
    model_name: GoogleModelName,
    *,
    provider: Literal['google-gla', 'google-vertex', 'gateway'] | Provider[Client] = 'google-gla',
    profile: ModelProfileSpec | None = None,
    settings: ModelSettings | None = None,
):
    """Initialize a Gemini model.

    Args:
        model_name: The name of the model to use.
        provider: The provider to use for authentication and API access. Can be either the string
            'google-gla' or 'google-vertex' or an instance of `Provider[google.genai.AsyncClient]`.
            Defaults to 'google-gla'.
        profile: The model profile to use. Defaults to a profile picked by the provider based on the model name.
        settings: The model settings to use. Defaults to None.
    """
    self._model_name = model_name

    if isinstance(provider, str):
        provider = infer_provider('gateway/google-vertex' if provider == 'gateway' else provider)
    self._provider = provider
    self.client = provider.client

    super().__init__(settings=settings, profile=profile or provider.model_profile)

```

---|---
####  model_name `property`
```
model_name: GoogleModelName[](https://ai.pydantic.dev/api/models/google/#pydantic_ai.models.google.GoogleModelName "GoogleModelName



      module-attribute
   \(pydantic_ai.models.google.GoogleModelName\)")

```

The model name.
####  system `property`
```
system:

```

The model provider.
####  supported_builtin_tools `classmethod`
```
supported_builtin_tools() -> (
    [[AbstractBuiltinTool[](https://ai.pydantic.dev/api/builtin_tools/#pydantic_ai.builtin_tools.AbstractBuiltinTool "AbstractBuiltinTool



      dataclass
   \(pydantic_ai.builtin_tools.AbstractBuiltinTool\)")]]
)

```

Return the set of builtin tool types this model can handle.
Source code in `pydantic_ai_slim/pydantic_ai/models/google.py`
```
277
278
279
280
```
| ```
@classmethod
def supported_builtin_tools(cls) -> frozenset[type[AbstractBuiltinTool]]:
    """Return the set of builtin tool types this model can handle."""
    return frozenset({WebSearchTool, CodeExecutionTool, FileSearchTool, WebFetchTool, ImageGenerationTool})

```

---|---
###  GeminiStreamedResponse `dataclass`
Bases: `StreamedResponse[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.StreamedResponse "StreamedResponse



      dataclass
   \(pydantic_ai.models.StreamedResponse\)")`
Implementation of `StreamedResponse` for the Gemini model.
Source code in `pydantic_ai_slim/pydantic_ai/models/google.py`
```
 839
 840
 841
 842
 843
 844
 845
 846
 847
 848
 849
 850
 851
 852
 853
 854
 855
 856
 857
 858
 859
 860
 861
 862
 863
 864
 865
 866
 867
 868
 869
 870
 871
 872
 873
 874
 875
 876
 877
 878
 879
 880
 881
 882
 883
 884
 885
 886
 887
 888
 889
 890
 891
 892
 893
 894
 895
 896
 897
 898
 899
 900
 901
 902
 903
 904
 905
 906
 907
 908
 909
 910
 911
 912
 913
 914
 915
 916
 917
 918
 919
 920
 921
 922
 923
 924
 925
 926
 927
 928
 929
 930
 931
 932
 933
 934
 935
 936
 937
 938
 939
 940
 941
 942
 943
 944
 945
 946
 947
 948
 949
 950
 951
 952
 953
 954
 955
 956
 957
 958
 959
 960
 961
 962
 963
 964
 965
 966
 967
 968
 969
 970
 971
 972
 973
 974
 975
 976
 977
 978
 979
 980
 981
 982
 983
 984
 985
 986
 987
 988
 989
 990
 991
 992
 993
 994
 995
 996
 997
 998
 999
1000
1001
1002
1003
1004
1005
1006
1007
1008
1009
1010
1011
1012
1013
1014
1015
1016
1017
1018
1019
1020
1021
1022
1023
1024
1025
1026
1027
1028
1029
1030
1031
1032
1033
1034
1035
1036
1037
1038
1039
1040
1041
1042
1043
1044
1045
1046
1047
1048
1049
1050
1051
1052
1053
1054
1055
1056
1057
1058
1059
1060
1061
1062
1063
1064
1065
1066
1067
1068
1069
1070
1071
1072
1073
1074
1075
1076
1077
1078
1079
1080
1081
1082
1083
1084
1085
1086
1087
1088
1089
1090
1091
1092
```
| ```
@dataclass
class GeminiStreamedResponse(StreamedResponse):
    """Implementation of `StreamedResponse` for the Gemini model."""

    _model_name: GoogleModelName
    _response: AsyncIterator[GenerateContentResponse]
    _provider_name: str
    _provider_url: str
    _provider_timestamp: datetime | None = None
    _timestamp: datetime = field(default_factory=_utils.now_utc)
    _file_search_tool_call_id: str | None = field(default=None, init=False)
    _code_execution_tool_call_id: str | None = field(default=None, init=False)
    _has_content_filter: bool = field(default=False, init=False)

    async def _get_event_iterator(self) -> AsyncIterator[ModelResponseStreamEvent]:  # noqa: C901
        if self._provider_timestamp is not None:
            self.provider_details = {'timestamp': self._provider_timestamp}
        try:
            async for chunk in self._response:
                self._usage = _metadata_as_usage(chunk, self._provider_name, self._provider_url)

                if not chunk.candidates:
                    if chunk.prompt_feedback and chunk.prompt_feedback.block_reason:
                        self._has_content_filter = True
                        block_reason = chunk.prompt_feedback.block_reason
                        self.provider_details = {
                            **(self.provider_details or {}),
                            'block_reason': block_reason.value,
                        }
                        if chunk.prompt_feedback.block_reason_message:
                            self.provider_details['block_reason_message'] = chunk.prompt_feedback.block_reason_message
                        if chunk.prompt_feedback.safety_ratings:
                            self.provider_details['safety_ratings'] = [
                                r.model_dump(by_alias=True) for r in chunk.prompt_feedback.safety_ratings
                            ]
                        self.finish_reason = 'content_filter'
                        if chunk.response_id:  # pragma: no branch
                            self.provider_response_id = chunk.response_id
                    continue

                candidate = chunk.candidates[0]

                if chunk.response_id:  # pragma: no branch
                    self.provider_response_id = chunk.response_id

                raw_finish_reason = candidate.finish_reason
                if raw_finish_reason and not self._has_content_filter:
                    self.provider_details = {**(self.provider_details or {}), 'finish_reason': raw_finish_reason.value}

                    if candidate.safety_ratings:
                        self.provider_details['safety_ratings'] = [
                            r.model_dump(by_alias=True) for r in candidate.safety_ratings
                        ]

                    self.finish_reason = _FINISH_REASON_MAP.get(raw_finish_reason)

                # Google streams the grounding metadata (including the web search queries and results)
                # _after_ the text that was generated using it, so it would show up out of order in the stream,
                # and cause issues with the logic that doesn't consider text ahead of built-in tool calls as output.
                # If that gets fixed (or we have a workaround), we can uncomment this:
                # web_search_call, web_search_return = _map_grounding_metadata(
                #     candidate.grounding_metadata, self.provider_name
                # )
                # if web_search_call and web_search_return:
                #     yield self._parts_manager.handle_part(vendor_part_id=uuid4(), part=web_search_call)
                #     yield self._parts_manager.handle_part(
                #         vendor_part_id=uuid4(), part=web_search_return
                #     )

                # URL context metadata (for WebFetchTool) is streamed in the first chunk, before the text,
                # so we can safely yield it here
                web_fetch_call, web_fetch_return = _map_url_context_metadata(
                    candidate.url_context_metadata, self.provider_name
                )
                if web_fetch_call and web_fetch_return:
                    yield self._parts_manager.handle_part(vendor_part_id=uuid4(), part=web_fetch_call)
                    yield self._parts_manager.handle_part(vendor_part_id=uuid4(), part=web_fetch_return)

                if candidate.content is None or candidate.content.parts is None:
                    continue

                parts = candidate.content.parts
                if not parts:
                    continue  # pragma: no cover

                for part in parts:
                    provider_details: dict[str, Any] | None = None
                    if part.thought_signature:
                        # Per https://ai.google.dev/gemini-api/docs/function-calling?example=meeting#thought-signatures:
                        # - Always send the thought_signature back to the model inside its original Part.
                        # - Don't merge a Part containing a signature with one that does not. This breaks the positional context of the thought.
                        # - Don't combine two Parts that both contain signatures, as the signature strings cannot be merged.
                        thought_signature = base64.b64encode(part.thought_signature).decode('utf-8')
                        provider_details = {'thought_signature': thought_signature}

                    if part.text is not None:
                        if len(part.text) == 0 and not provider_details:
                            continue
                        if part.thought:
                            for event in self._parts_manager.handle_thinking_delta(
                                vendor_part_id=None,
                                content=part.text,
                                provider_name=self.provider_name if provider_details else None,
                                provider_details=provider_details,
