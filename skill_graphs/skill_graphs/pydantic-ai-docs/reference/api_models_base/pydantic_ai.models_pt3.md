            params,
            builtin_tools=list({tool.unique_id: tool for tool in builtin_tools}.values()),
        )

    if params.output_mode == 'auto':
        output_mode = self.profile.default_structured_output_mode
        params = replace(
            params,
            output_mode=output_mode,
            allow_text_output=output_mode in ('native', 'prompted'),
        )

    # Reset irrelevant fields
    if params.output_tools and params.output_mode != 'tool':
        params = replace(params, output_tools=[])
    if params.output_object and params.output_mode not in ('native', 'prompted'):
        params = replace(params, output_object=None)
    if params.prompted_output_template and params.output_mode not in ('prompted', 'native'):
        params = replace(params, prompted_output_template=None)  # pragma: no cover

    # Set default prompted output template
    if (
        params.output_mode == 'prompted'
        or (params.output_mode == 'native' and self.profile.native_output_requires_schema_in_instructions)
    ) and params.prompted_output_template is None:
        params = replace(params, prompted_output_template=self.profile.prompted_output_template)

    # Check if output mode is supported
    if params.output_mode == 'native' and not self.profile.supports_json_schema_output:
        raise UserError('Native structured output is not supported by this model.')
    if params.output_mode == 'tool' and not self.profile.supports_tools:
        raise UserError('Tool output is not supported by this model.')
    if params.allow_image_output and not self.profile.supports_image_output:
        raise UserError('Image output is not supported by this model.')

    # Check if builtin tools are supported
    if params.builtin_tools:
        supported_types = self.profile.supported_builtin_tools
        unsupported = [tool for tool in params.builtin_tools if not isinstance(tool, tuple(supported_types))]
        if unsupported:
            unsupported_names = [type(tool).__name__ for tool in unsupported]
            supported_names = [t.__name__ for t in supported_types]
            raise UserError(
                f'Builtin tool(s) {unsupported_names} not supported by this model. Supported: {supported_names}'
            )

    return model_settings, params

```

---|---
####  model_name `abstractmethod` `property`
```
model_name:

```

The model name.
####  model_id `property`
```
model_id:

```

The fully qualified model name in `'provider:model_name'` format.
####  label `property`
```
label:

```

Human-friendly display label for the model.
Handles common patterns: - gpt-5 -> GPT 5 - claude-sonnet-4-5 -> Claude Sonnet 4.5 - gemini-2.5-pro -> Gemini 2.5 Pro - meta-llama/llama-3-70b -> Llama 3 70b (OpenRouter style)
####  supported_builtin_tools `classmethod`
```
supported_builtin_tools() -> (
    [[AbstractBuiltinTool[](https://ai.pydantic.dev/api/builtin_tools/#pydantic_ai.builtin_tools.AbstractBuiltinTool "AbstractBuiltinTool



      dataclass
   \(pydantic_ai.builtin_tools.AbstractBuiltinTool\)")]]
)

```

Return the set of builtin tool types this model class can handle.
Subclasses should override this to reflect their actual capabilities. Default is empty set - subclasses must explicitly declare support.
Source code in `pydantic_ai_slim/pydantic_ai/models/__init__.py`
```
841
842
843
844
845
846
847
848
```
| ```
@classmethod
def supported_builtin_tools(cls) -> frozenset[type[AbstractBuiltinTool]]:
    """Return the set of builtin tool types this model class can handle.

    Subclasses should override this to reflect their actual capabilities.
    Default is empty set - subclasses must explicitly declare support.
    """
    return frozenset()

```

---|---
####  profile `cached` `property`
```
profile: ModelProfile[](https://ai.pydantic.dev/api/profiles/#pydantic_ai.profiles.ModelProfile "pydantic_ai.profiles.ModelProfile")

```

The model profile.
We use this to compute the intersection of the profile's supported_builtin_tools and the model's implemented tools, ensuring model.profile.supported_builtin_tools is the single source of truth for what builtin tools are actually usable.
####  system `abstractmethod` `property`
```
system:

```

The model provider, ex: openai.
Use to populate the `gen_ai.system` OpenTelemetry semantic convention attribute, so should use well-known values listed in https://opentelemetry.io/docs/specs/semconv/attributes-registry/gen-ai/#gen-ai-system when applicable.
####  base_url `property`
```
base_url:  | None

```

The base URL for the provider API, if available.
###  StreamedResponse `dataclass`
Bases:
Streamed response from an LLM when calling a tool.
Source code in `pydantic_ai_slim/pydantic_ai/models/__init__.py`
```
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
```
| ```
@dataclass
class StreamedResponse(ABC):
    """Streamed response from an LLM when calling a tool."""

    model_request_parameters: ModelRequestParameters

    final_result_event: FinalResultEvent | None = field(default=None, init=False)

    provider_response_id: str | None = field(default=None, init=False)
    provider_details: dict[str, Any] | None = field(default=None, init=False)
    finish_reason: FinishReason | None = field(default=None, init=False)

    _parts_manager: ModelResponsePartsManager = field(default_factory=ModelResponsePartsManager, init=False)
    _event_iterator: AsyncIterator[ModelResponseStreamEvent] | None = field(default=None, init=False)
    _usage: RequestUsage = field(default_factory=RequestUsage, init=False)

    def __aiter__(self) -> AsyncIterator[ModelResponseStreamEvent]:
        """Stream the response as an async iterable of [`ModelResponseStreamEvent`][pydantic_ai.messages.ModelResponseStreamEvent]s.

        This proxies the `_event_iterator()` and emits all events, while also checking for matches
        on the result schema and emitting a [`FinalResultEvent`][pydantic_ai.messages.FinalResultEvent] if/when the
        first match is found.
        """
        if self._event_iterator is None:

            async def iterator_with_final_event(
                iterator: AsyncIterator[ModelResponseStreamEvent],
            ) -> AsyncIterator[ModelResponseStreamEvent]:
                async for event in iterator:
                    yield event
                    if (
                        final_result_event := _get_final_result_event(event, self.model_request_parameters)
                    ) is not None:
                        self.final_result_event = final_result_event
                        yield final_result_event
                        break

                # If we broke out of the above loop, we need to yield the rest of the events
                # If we didn't, this will just be a no-op
                async for event in iterator:
                    yield event

            async def iterator_with_part_end(
                iterator: AsyncIterator[ModelResponseStreamEvent],
            ) -> AsyncIterator[ModelResponseStreamEvent]:
                last_start_event: PartStartEvent | None = None

                def part_end_event(next_part: ModelResponsePart | None = None) -> PartEndEvent | None:
                    if not last_start_event:
                        return None

                    index = last_start_event.index
                    part = self._parts_manager.get_parts()[index]
                    if not isinstance(part, TextPart | ThinkingPart | BaseToolCallPart):
                        # Parts other than these 3 don't have deltas, so don't need an end part.
                        return None

                    return PartEndEvent(
                        index=index,
                        part=part,
                        next_part_kind=next_part.part_kind if next_part else None,
                    )

                async for event in iterator:
                    if isinstance(event, PartStartEvent):
                        if last_start_event:
                            end_event = part_end_event(event.part)
                            if end_event:
                                yield end_event

                            event.previous_part_kind = last_start_event.part.part_kind
                        last_start_event = event

                    yield event

                end_event = part_end_event()
                if end_event:
                    yield end_event

            self._event_iterator = iterator_with_part_end(iterator_with_final_event(self._get_event_iterator()))
        return self._event_iterator

    @abstractmethod
    async def _get_event_iterator(self) -> AsyncIterator[ModelResponseStreamEvent]:
        """Return an async iterator of [`ModelResponseStreamEvent`][pydantic_ai.messages.ModelResponseStreamEvent]s.

        This method should be implemented by subclasses to translate the vendor-specific stream of events into
        pydantic_ai-format events.

        It should use the `_parts_manager` to handle deltas, and should update the `_usage` attributes as it goes.
        """
        raise NotImplementedError()
        # noinspection PyUnreachableCode
        yield

    def get(self) -> ModelResponse:
        """Build a [`ModelResponse`][pydantic_ai.messages.ModelResponse] from the data received from the stream so far."""
        return ModelResponse(
            parts=self._parts_manager.get_parts(),
            model_name=self.model_name,
            timestamp=self.timestamp,
            usage=self.usage(),
            provider_name=self.provider_name,
            provider_url=self.provider_url,
            provider_response_id=self.provider_response_id,
            provider_details=self.provider_details,
            finish_reason=self.finish_reason,
        )

    # TODO (v2): Make this a property
    def usage(self) -> RequestUsage:
        """Get the usage of the response so far. This will not be the final usage until the stream is exhausted."""
        return self._usage

    @property
    @abstractmethod
    def model_name(self) -> str:
        """Get the model name of the response."""
        raise NotImplementedError()

    @property
    @abstractmethod
    def provider_name(self) -> str | None:
        """Get the provider name."""
        raise NotImplementedError()

    @property
    @abstractmethod
    def provider_url(self) -> str | None:
        """Get the provider base URL."""
        raise NotImplementedError()

    @property
    @abstractmethod
    def timestamp(self) -> datetime:
        """Get the timestamp of the response."""
        raise NotImplementedError()

```

---|---
####  __aiter__
```
__aiter__() -> [ModelResponseStreamEvent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponseStreamEvent "ModelResponseStreamEvent



      module-attribute
   \(pydantic_ai.messages.ModelResponseStreamEvent\)")]

```

Stream the response as an async iterable of [`ModelResponseStreamEvent`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponseStreamEvent "ModelResponseStreamEvent



      module-attribute
  ")s.
This proxies the `_event_iterator()` and emits all events, while also checking for matches on the result schema and emitting a [`FinalResultEvent`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FinalResultEvent "FinalResultEvent



      dataclass
  ") if/when the first match is found.
Source code in `pydantic_ai_slim/pydantic_ai/models/__init__.py`
```
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
```
| ```
def __aiter__(self) -> AsyncIterator[ModelResponseStreamEvent]:
    """Stream the response as an async iterable of [`ModelResponseStreamEvent`][pydantic_ai.messages.ModelResponseStreamEvent]s.

    This proxies the `_event_iterator()` and emits all events, while also checking for matches
    on the result schema and emitting a [`FinalResultEvent`][pydantic_ai.messages.FinalResultEvent] if/when the
    first match is found.
    """
    if self._event_iterator is None:

        async def iterator_with_final_event(
            iterator: AsyncIterator[ModelResponseStreamEvent],
        ) -> AsyncIterator[ModelResponseStreamEvent]:
            async for event in iterator:
                yield event
                if (
                    final_result_event := _get_final_result_event(event, self.model_request_parameters)
                ) is not None:
                    self.final_result_event = final_result_event
                    yield final_result_event
                    break

            # If we broke out of the above loop, we need to yield the rest of the events
            # If we didn't, this will just be a no-op
            async for event in iterator:
                yield event

        async def iterator_with_part_end(
            iterator: AsyncIterator[ModelResponseStreamEvent],
        ) -> AsyncIterator[ModelResponseStreamEvent]:
            last_start_event: PartStartEvent | None = None

            def part_end_event(next_part: ModelResponsePart | None = None) -> PartEndEvent | None:
                if not last_start_event:
                    return None

                index = last_start_event.index
                part = self._parts_manager.get_parts()[index]
                if not isinstance(part, TextPart | ThinkingPart | BaseToolCallPart):
                    # Parts other than these 3 don't have deltas, so don't need an end part.
                    return None

                return PartEndEvent(
                    index=index,
                    part=part,
                    next_part_kind=next_part.part_kind if next_part else None,
                )

            async for event in iterator:
                if isinstance(event, PartStartEvent):
                    if last_start_event:
                        end_event = part_end_event(event.part)
                        if end_event:
                            yield end_event

                        event.previous_part_kind = last_start_event.part.part_kind
                    last_start_event = event

                yield event

            end_event = part_end_event()
            if end_event:
                yield end_event

        self._event_iterator = iterator_with_part_end(iterator_with_final_event(self._get_event_iterator()))
    return self._event_iterator

```

---|---
####  get
```
get() -> ModelResponse[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse "ModelResponse



      dataclass
   \(pydantic_ai.messages.ModelResponse\)")

```

Build a [`ModelResponse`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse "ModelResponse



      dataclass
  ") from the data received from the stream so far.
Source code in `pydantic_ai_slim/pydantic_ai/models/__init__.py`
```
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
```
| ```
def get(self) -> ModelResponse:
    """Build a [`ModelResponse`][pydantic_ai.messages.ModelResponse] from the data received from the stream so far."""
    return ModelResponse(
        parts=self._parts_manager.get_parts(),
        model_name=self.model_name,
        timestamp=self.timestamp,
        usage=self.usage(),
        provider_name=self.provider_name,
        provider_url=self.provider_url,
        provider_response_id=self.provider_response_id,
        provider_details=self.provider_details,
        finish_reason=self.finish_reason,
    )

```

---|---
####  usage
```
usage() -> RequestUsage[](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.RequestUsage "RequestUsage



      dataclass
   \(pydantic_ai.usage.RequestUsage\)")

```

Get the usage of the response so far. This will not be the final usage until the stream is exhausted.
Source code in `pydantic_ai_slim/pydantic_ai/models/__init__.py`
```
1055
1056
1057
```
| ```
def usage(self) -> RequestUsage:
    """Get the usage of the response so far. This will not be the final usage until the stream is exhausted."""
    return self._usage

```

---|---
####  model_name `abstractmethod` `property`
```
model_name:

```

Get the model name of the response.
####  provider_name `abstractmethod` `property`
```
provider_name:  | None

```

Get the provider name.
####  provider_url `abstractmethod` `property`
```
provider_url:  | None

```

Get the provider base URL.
####  timestamp `abstractmethod` `property`
```
timestamp:

```

Get the timestamp of the response.
###  ALLOW_MODEL_REQUESTS `module-attribute`
```
ALLOW_MODEL_REQUESTS = True

```

Whether to allow requests to models.
This global setting allows you to disable request to most models, e.g. to make sure you don't accidentally make costly requests to a model during tests.
The testing models [`TestModel`](https://ai.pydantic.dev/api/models/test/#pydantic_ai.models.test.TestModel "TestModel



      dataclass
  ") and [`FunctionModel`](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.FunctionModel "FunctionModel



      dataclass
  ") are no affected by this setting.
###  check_allow_model_requests
```
check_allow_model_requests() -> None

```

Check if model requests are allowed.
If you're defining your own models that have costs or latency associated with their use, you should call this in [`Model.request`](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.Model.request "request



      abstractmethod
      async
  ") and [`Model.request_stream`](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.Model.request_stream "request_stream



      async
  ").
Raises:
Type | Description
---|---
|  If model requests are not allowed.
Source code in `pydantic_ai_slim/pydantic_ai/models/__init__.py`
```
1095
1096
1097
1098
1099
1100
1101
1102
1103
1104
1105
```
| ```
def check_allow_model_requests() -> None:
    """Check if model requests are allowed.

    If you're defining your own models that have costs or latency associated with their use, you should call this in
    [`Model.request`][pydantic_ai.models.Model.request] and [`Model.request_stream`][pydantic_ai.models.Model.request_stream].

    Raises:
        RuntimeError: If model requests are not allowed.
    """
    if not ALLOW_MODEL_REQUESTS:
        raise RuntimeError('Model requests are not allowed, since ALLOW_MODEL_REQUESTS is False')

```

---|---
###  override_allow_model_requests
```
override_allow_model_requests(
    allow_model_requests: ,
) -> [None]

```

Context manager to temporarily override [`ALLOW_MODEL_REQUESTS`](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.ALLOW_MODEL_REQUESTS "ALLOW_MODEL_REQUESTS



      module-attribute
  ").
Parameters:
Name | Type | Description | Default
---|---|---|---
`allow_model_requests` |  |  Whether to allow model requests within the context. |  _required_
Source code in `pydantic_ai_slim/pydantic_ai/models/__init__.py`
```
1108
1109
1110
1111
1112
1113
1114
1115
1116
1117
1118
1119
1120
1121
```
| ```
@contextmanager
def override_allow_model_requests(allow_model_requests: bool) -> Iterator[None]:
    """Context manager to temporarily override [`ALLOW_MODEL_REQUESTS`][pydantic_ai.models.ALLOW_MODEL_REQUESTS].

    Args:
        allow_model_requests: Whether to allow model requests within the context.
    """
    global ALLOW_MODEL_REQUESTS
    old_value = ALLOW_MODEL_REQUESTS
    ALLOW_MODEL_REQUESTS = allow_model_requests  # pyright: ignore[reportConstantRedefinition]
    try:
        yield
    finally:
        ALLOW_MODEL_REQUESTS = old_value  # pyright: ignore[reportConstantRedefinition]

```

---|---
© Pydantic Services Inc. 2024 to present
