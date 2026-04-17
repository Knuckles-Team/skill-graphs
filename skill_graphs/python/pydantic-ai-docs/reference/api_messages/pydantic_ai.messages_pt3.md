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
```
| ```
@dataclass(repr=False)
class UserPromptPart:
    """A user prompt, generally written by the end user.

    Content comes from the `user_prompt` parameter of [`Agent.run`][pydantic_ai.agent.AbstractAgent.run],
    [`Agent.run_sync`][pydantic_ai.agent.AbstractAgent.run_sync], and [`Agent.run_stream`][pydantic_ai.agent.AbstractAgent.run_stream].
    """

    content: str | Sequence[UserContent]
    """The content of the prompt."""

    _: KW_ONLY

    timestamp: datetime = field(default_factory=_now_utc)
    """The timestamp of the prompt."""

    part_kind: Literal['user-prompt'] = 'user-prompt'
    """Part type identifier, this is available on all parts as a discriminator."""

    def otel_event(self, settings: InstrumentationSettings) -> LogRecord:
        content: Any = [{'kind': part.pop('type'), **part} for part in self.otel_message_parts(settings)]
        for part in content:
            if part['kind'] == 'binary' and 'content' in part:
                part['binary_content'] = part.pop('content')
        content = [
            part['content'] if part == {'kind': 'text', 'content': part.get('content')} else part for part in content
        ]
        if content in ([{'kind': 'text'}], [self.content]):
            content = content[0]
        return LogRecord(attributes={'event.name': 'gen_ai.user.message'}, body={'content': content, 'role': 'user'})

    def otel_message_parts(self, settings: InstrumentationSettings) -> list[_otel_messages.MessagePart]:
        parts: list[_otel_messages.MessagePart] = []
        content: Sequence[UserContent] = [self.content] if isinstance(self.content, str) else self.content
        for part in content:
            if isinstance(part, str):
                parts.append(
                    _otel_messages.TextPart(type='text', **({'content': part} if settings.include_content else {}))
                )
            elif isinstance(part, ImageUrl | AudioUrl | DocumentUrl | VideoUrl):
                if settings.version >= 4:
                    uri_part = _otel_messages.UriPart(type='uri')
                    modality = _kind_to_modality_lookup.get(part.kind)
                    if modality is not None:
                        uri_part['modality'] = modality
                    try:  # don't fail the whole message if media type can't be inferred for some reason, just omit it
                        uri_part['mime_type'] = part.media_type
                    except ValueError:
                        pass
                    if settings.include_content:
                        uri_part['uri'] = part.url
                    parts.append(uri_part)
                else:
                    parts.append(
                        _otel_messages.MediaUrlPart(
                            type=part.kind,
                            **{'url': part.url} if settings.include_content else {},
                        )
                    )
            elif isinstance(part, BinaryContent):
                parts.append(_convert_binary_to_otel_part(part.media_type, lambda p=part: p.base64, settings))
            elif isinstance(part, UploadedFile):
                # UploadedFile references provider-hosted files by file_id (OTel GenAI spec FilePart)
                # Infer modality from media_type - OTel spec defines: image, video, audio (or any string)
                category = part.media_type.split('/', 1)[0]
                if category in ('image', 'audio', 'video'):
                    modality = category
                else:
                    modality = 'document'  # default for PDFs, text, etc.
                file_part = _otel_messages.FilePart(type='file', modality=modality, mime_type=part.media_type)
                if settings.include_content:
                    file_part['file_id'] = part.file_id
                parts.append(file_part)
            elif isinstance(part, CachePoint):
                # CachePoint is a marker, not actual content - skip it for otel
                pass
            else:
                parts.append({'type': part.kind})  # pragma: no cover
        return parts

    __repr__ = _utils.dataclasses_no_defaults_repr

```

---|---
####  content `instance-attribute`
```
content:  | [UserContent]

```

The content of the prompt.
####  timestamp `class-attribute` `instance-attribute`
```
timestamp:  = (default_factory=now_utc)

```

The timestamp of the prompt.
####  part_kind `class-attribute` `instance-attribute`
```
part_kind: ['user-prompt'] = 'user-prompt'

```

Part type identifier, this is available on all parts as a discriminator.
###  BaseToolReturnPart `dataclass`
Base class for tool return parts.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
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
```
| ```
@dataclass(repr=False)
class BaseToolReturnPart:
    """Base class for tool return parts."""

    tool_name: str
    """The name of the "tool" was called."""

    content: ToolReturnContent
    """The return value."""

    tool_call_id: str = field(default_factory=_generate_tool_call_id)
    """The tool call identifier, this is used by some models including OpenAI.

    In case the tool call id is not provided by the model, Pydantic AI will generate a random one.
    """

    _: KW_ONLY

    metadata: Any = None
    """Additional data that can be accessed programmatically by the application but is not sent to the LLM."""

    timestamp: datetime = field(default_factory=_now_utc)
    """The timestamp, when the tool returned."""

    outcome: Literal['success', 'failed', 'denied'] = 'success'
    """The outcome of the tool call.

    - `'success'`: The tool executed successfully.
    - `'failed'`: The tool raised an error during execution.
    - `'denied'`: The tool call was denied by the approval mechanism.
    """

    def model_response_str(self) -> str:
        """Return a string representation of the content for the model."""
        if isinstance(self.content, str):
            return self.content
        else:
            return tool_return_ta.dump_json(self.content).decode()

    def model_response_object(self) -> dict[str, Any]:
        """Return a dictionary representation of the content, wrapping non-dict types appropriately."""
        # gemini supports JSON dict return values, but no other JSON types, hence we wrap anything else in a dict
        json_content = tool_return_ta.dump_python(self.content, mode='json')
        if isinstance(json_content, dict):
            return json_content  # type: ignore[reportUnknownReturn]
        else:
            return {'return_value': json_content}

    def otel_event(self, settings: InstrumentationSettings) -> LogRecord:
        body: AnyValue = {
            'role': 'tool',
            'id': self.tool_call_id,
            'name': self.tool_name,
        }
        if settings.include_content:
            body['content'] = self.content  # pyright: ignore[reportArgumentType]

        return LogRecord(
            body=body,
            attributes={'event.name': 'gen_ai.tool.message'},
        )

    def otel_message_parts(self, settings: InstrumentationSettings) -> list[_otel_messages.MessagePart]:
        from .models.instrumented import InstrumentedModel

        part = _otel_messages.ToolCallResponsePart(
            type='tool_call_response',
            id=self.tool_call_id,
            name=self.tool_name,
        )

        if settings.include_content and self.content is not None:
            part['result'] = InstrumentedModel.serialize_any(self.content)

        return [part]

    def has_content(self) -> bool:
        """Return `True` if the tool return has content."""
        return self.content is not None  # pragma: no cover

    __repr__ = _utils.dataclasses_no_defaults_repr

```

---|---
####  tool_name `instance-attribute`
```
tool_name:

```

The name of the "tool" was called.
####  content `instance-attribute`
```
content: ToolReturnContent

```

The return value.
####  tool_call_id `class-attribute` `instance-attribute`
```
tool_call_id:  = (
    default_factory=generate_tool_call_id
)

```

The tool call identifier, this is used by some models including OpenAI.
In case the tool call id is not provided by the model, Pydantic AI will generate a random one.
####  metadata `class-attribute` `instance-attribute`
```
metadata:  = None

```

Additional data that can be accessed programmatically by the application but is not sent to the LLM.
####  timestamp `class-attribute` `instance-attribute`
```
timestamp:  = (default_factory=now_utc)

```

The timestamp, when the tool returned.
####  outcome `class-attribute` `instance-attribute`
```
outcome: ['success', 'failed', 'denied'] = 'success'

```

The outcome of the tool call.
  * `'success'`: The tool executed successfully.
  * `'failed'`: The tool raised an error during execution.
  * `'denied'`: The tool call was denied by the approval mechanism.


####  model_response_str
```
model_response_str() ->

```

Return a string representation of the content for the model.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1035
1036
1037
1038
1039
1040
```
| ```
def model_response_str(self) -> str:
    """Return a string representation of the content for the model."""
    if isinstance(self.content, str):
        return self.content
    else:
        return tool_return_ta.dump_json(self.content).decode()

```

---|---
####  model_response_object
```
model_response_object() -> [, ]

```

Return a dictionary representation of the content, wrapping non-dict types appropriately.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1042
1043
1044
1045
1046
1047
1048
1049
```
| ```
def model_response_object(self) -> dict[str, Any]:
    """Return a dictionary representation of the content, wrapping non-dict types appropriately."""
    # gemini supports JSON dict return values, but no other JSON types, hence we wrap anything else in a dict
    json_content = tool_return_ta.dump_python(self.content, mode='json')
    if isinstance(json_content, dict):
        return json_content  # type: ignore[reportUnknownReturn]
    else:
        return {'return_value': json_content}

```

---|---
####  has_content
```
has_content() ->

```

Return `True` if the tool return has content.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1079
1080
1081
```
| ```
def has_content(self) -> bool:
    """Return `True` if the tool return has content."""
    return self.content is not None  # pragma: no cover

```

---|---
###  ToolReturnPart `dataclass`
Bases: `BaseToolReturnPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BaseToolReturnPart "BaseToolReturnPart



      dataclass
   \(pydantic_ai.messages.BaseToolReturnPart\)")`
A tool return message, this encodes the result of running a tool.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1086
1087
1088
1089
1090
1091
1092
1093
```
| ```
@dataclass(repr=False)
class ToolReturnPart(BaseToolReturnPart):
    """A tool return message, this encodes the result of running a tool."""

    _: KW_ONLY

    part_kind: Literal['tool-return'] = 'tool-return'
    """Part type identifier, this is available on all parts as a discriminator."""

```

---|---
####  part_kind `class-attribute` `instance-attribute`
```
part_kind: ['tool-return'] = 'tool-return'

```

Part type identifier, this is available on all parts as a discriminator.
###  BuiltinToolReturnPart `dataclass`
Bases: `BaseToolReturnPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BaseToolReturnPart "BaseToolReturnPart



      dataclass
   \(pydantic_ai.messages.BaseToolReturnPart\)")`
A tool return message from a built-in tool.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
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
1106
1107
1108
1109
1110
1111
1112
1113
1114
1115
```
| ```
@dataclass(repr=False)
class BuiltinToolReturnPart(BaseToolReturnPart):
    """A tool return message from a built-in tool."""

    _: KW_ONLY

    provider_name: str | None = None
    """The name of the provider that generated the response.

    Required to be set when `provider_details` is set.
    """

    provider_details: dict[str, Any] | None = None
    """Additional data returned by the provider that can't be mapped to standard fields.

    This is used for data that is required to be sent back to APIs, as well as data users may want to access programmatically.
    When this field is set, `provider_name` is required to identify the provider that generated this data."""

    part_kind: Literal['builtin-tool-return'] = 'builtin-tool-return'
    """Part type identifier, this is available on all parts as a discriminator."""

```

---|---
####  provider_name `class-attribute` `instance-attribute`
```
provider_name:  | None = None

```

The name of the provider that generated the response.
Required to be set when `provider_details` is set.
####  provider_details `class-attribute` `instance-attribute`
```
provider_details: [, ] | None = None

```

Additional data returned by the provider that can't be mapped to standard fields.
This is used for data that is required to be sent back to APIs, as well as data users may want to access programmatically. When this field is set, `provider_name` is required to identify the provider that generated this data.
####  part_kind `class-attribute` `instance-attribute`
```
part_kind: ["builtin-tool-return"] = (
    "builtin-tool-return"
)

```

Part type identifier, this is available on all parts as a discriminator.
###  RetryPromptPart `dataclass`
A message back to a model asking it to try again.
This can be sent for a number of reasons:
  * Pydantic validation of tool arguments failed, here content is derived from a Pydantic [`ValidationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError)
  * a tool raised a [`ModelRetry`](https://ai.pydantic.dev/api/exceptions/#pydantic_ai.exceptions.ModelRetry "ModelRetry") exception
  * no tool was found for the tool name
  * the model returned plain text when a structured response was expected
  * Pydantic validation of a structured response failed, here content is derived from a Pydantic [`ValidationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError)
  * an output validator raised a [`ModelRetry`](https://ai.pydantic.dev/api/exceptions/#pydantic_ai.exceptions.ModelRetry "ModelRetry") exception

Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1121
1122
1123
1124
1125
1126
1127
1128
1129
1130
1131
1132
1133
1134
1135
1136
1137
1138
1139
1140
1141
1142
1143
1144
1145
1146
1147
1148
1149
1150
1151
1152
1153
1154
1155
1156
1157
1158
1159
1160
1161
1162
1163
1164
1165
1166
1167
1168
1169
1170
1171
1172
1173
1174
1175
1176
1177
1178
1179
1180
1181
1182
1183
1184
1185
1186
1187
1188
1189
1190
1191
1192
1193
1194
1195
1196
1197
1198
1199
1200
1201
1202
1203
1204
1205
1206
1207
1208
```
| ```
@dataclass(repr=False)
class RetryPromptPart:
    """A message back to a model asking it to try again.

    This can be sent for a number of reasons:

    * Pydantic validation of tool arguments failed, here content is derived from a Pydantic
      [`ValidationError`][pydantic_core.ValidationError]
    * a tool raised a [`ModelRetry`][pydantic_ai.exceptions.ModelRetry] exception
    * no tool was found for the tool name
    * the model returned plain text when a structured response was expected
    * Pydantic validation of a structured response failed, here content is derived from a Pydantic
      [`ValidationError`][pydantic_core.ValidationError]
    * an output validator raised a [`ModelRetry`][pydantic_ai.exceptions.ModelRetry] exception
    """

    content: list[pydantic_core.ErrorDetails] | str
    """Details of why and how the model should retry.

    If the retry was triggered by a [`ValidationError`][pydantic_core.ValidationError], this will be a list of
    error details.
    """

    _: KW_ONLY

    tool_name: str | None = None
    """The name of the tool that was called, if any."""

    tool_call_id: str = field(default_factory=_generate_tool_call_id)
    """The tool call identifier, this is used by some models including OpenAI.

    In case the tool call id is not provided by the model, Pydantic AI will generate a random one.
    """

    timestamp: datetime = field(default_factory=_now_utc)
    """The timestamp, when the retry was triggered."""

    part_kind: Literal['retry-prompt'] = 'retry-prompt'
    """Part type identifier, this is available on all parts as a discriminator."""

    def model_response(self) -> str:
        """Return a string message describing why the retry is requested."""
        if isinstance(self.content, str):
            if self.tool_name is None:
                description = f'Validation feedback:\n{self.content}'
            else:
                description = self.content
        else:
            json_errors = error_details_ta.dump_json(self.content, exclude={'__all__': {'ctx'}}, indent=2)
            plural = isinstance(self.content, list) and len(self.content) != 1
            description = (
                f'{len(self.content)} validation error{"s" if plural else ""}:\n```json\n{json_errors.decode()}\n```'
            )
        return f'{description}\n\nFix the errors and try again.'

    def otel_event(self, settings: InstrumentationSettings) -> LogRecord:
        if self.tool_name is None:
            return LogRecord(
                attributes={'event.name': 'gen_ai.user.message'},
                body={'content': self.model_response(), 'role': 'user'},
            )
        else:
            return LogRecord(
                attributes={'event.name': 'gen_ai.tool.message'},
                body={
                    **({'content': self.model_response()} if settings.include_content else {}),
                    'role': 'tool',
                    'id': self.tool_call_id,
                    'name': self.tool_name,
                },
            )

    def otel_message_parts(self, settings: InstrumentationSettings) -> list[_otel_messages.MessagePart]:
        if self.tool_name is None:
            return [_otel_messages.TextPart(type='text', content=self.model_response())]
        else:
            part = _otel_messages.ToolCallResponsePart(
                type='tool_call_response',
                id=self.tool_call_id,
                name=self.tool_name,
            )

            if settings.include_content:
                part['result'] = self.model_response()

            return [part]

    __repr__ = _utils.dataclasses_no_defaults_repr

```

---|---
####  content `instance-attribute`
```
content: [ErrorDetails[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ErrorDetails "pydantic_core.ErrorDetails")] |

```

Details of why and how the model should retry.
If the retry was triggered by a [`ValidationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError), this will be a list of error details.
####  tool_name `class-attribute` `instance-attribute`
```
tool_name:  | None = None

```

The name of the tool that was called, if any.
####  tool_call_id `class-attribute` `instance-attribute`
```
tool_call_id:  = (
    default_factory=generate_tool_call_id
)

```

The tool call identifier, this is used by some models including OpenAI.
In case the tool call id is not provided by the model, Pydantic AI will generate a random one.
####  timestamp `class-attribute` `instance-attribute`
```
timestamp:  = (default_factory=now_utc)

```

The timestamp, when the retry was triggered.
####  part_kind `class-attribute` `instance-attribute`
```
part_kind: ['retry-prompt'] = 'retry-prompt'

```

Part type identifier, this is available on all parts as a discriminator.
####  model_response
```
model_response() ->

```

Return a string message describing why the retry is requested.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1161
1162
1163
1164
1165
1166
1167
1168
1169
1170
1171
1172
1173
1174
```
| ```
def model_response(self) -> str:
    """Return a string message describing why the retry is requested."""
    if isinstance(self.content, str):
        if self.tool_name is None:
            description = f'Validation feedback:\n{self.content}'
        else:
            description = self.content
    else:
        json_errors = error_details_ta.dump_json(self.content, exclude={'__all__': {'ctx'}}, indent=2)
        plural = isinstance(self.content, list) and len(self.content) != 1
        description = (
            f'{len(self.content)} validation error{"s" if plural else ""}:\n```json\n{json_errors.decode()}\n```'
        )
    return f'{description}\n\nFix the errors and try again.'

```

---|---
###  ModelRequestPart `module-attribute`
```
ModelRequestPart = [
    SystemPromptPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.SystemPromptPart "SystemPromptPart



      dataclass
   \(pydantic_ai.messages.SystemPromptPart\)")
    | UserPromptPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.UserPromptPart "UserPromptPart



      dataclass
   \(pydantic_ai.messages.UserPromptPart\)")
    | ToolReturnPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolReturnPart "ToolReturnPart



      dataclass
   \(pydantic_ai.messages.ToolReturnPart\)")
    | RetryPromptPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.RetryPromptPart "RetryPromptPart



      dataclass
   \(pydantic_ai.messages.RetryPromptPart\)"),
    Discriminator[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Discriminator "pydantic.Discriminator")("part_kind"),
]

```

A message part sent by Pydantic AI to a model.
###  ModelRequest `dataclass`
A request generated by Pydantic AI and sent to a model, e.g. a message from the Pydantic AI app to the model.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1217
1218
1219
1220
1221
1222
1223
1224
1225
1226
1227
1228
1229
1230
1231
1232
1233
1234
1235
1236
1237
1238
1239
1240
1241
1242
1243
1244
1245
1246
1247
1248
```
| ```
@dataclass(repr=False)
class ModelRequest:
    """A request generated by Pydantic AI and sent to a model, e.g. a message from the Pydantic AI app to the model."""

    parts: Sequence[ModelRequestPart]
    """The parts of the user message."""

    _: KW_ONLY

    # Default is None for backwards compatibility with old serialized messages that don't have this field.
    # Using a default_factory would incorrectly fill in the current time for deserialized historical messages.
    timestamp: datetime | None = None
    """The timestamp when the request was sent to the model."""

    instructions: str | None = None
    """The instructions for the model."""

    kind: Literal['request'] = 'request'
    """Message type identifier, this is available on all parts as a discriminator."""

    run_id: str | None = None
    """The unique identifier of the agent run in which this message originated."""

    metadata: dict[str, Any] | None = None
    """Additional data that can be accessed programmatically by the application but is not sent to the LLM."""

    @classmethod
    def user_text_prompt(cls, user_prompt: str, *, instructions: str | None = None) -> ModelRequest:
        """Create a `ModelRequest` with a single user prompt as text."""
        return cls(parts=[UserPromptPart(user_prompt)], instructions=instructions)

    __repr__ = _utils.dataclasses_no_defaults_repr

```

---|---
####  parts `instance-attribute`
```
parts: [ModelRequestPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelRequestPart "ModelRequestPart



      module-attribute
   \(pydantic_ai.messages.ModelRequestPart\)")]

```

The parts of the user message.
####  timestamp `class-attribute` `instance-attribute`
```
timestamp:  | None = None

```

The timestamp when the request was sent to the model.
####  instructions `class-attribute` `instance-attribute`
```
instructions:  | None = None

```

The instructions for the model.
####  kind `class-attribute` `instance-attribute`
```
kind: ['request'] = 'request'

```

Message type identifier, this is available on all parts as a discriminator.
####  run_id `class-attribute` `instance-attribute`
```
run_id:  | None = None

```

The unique identifier of the agent run in which this message originated.
####  metadata `class-attribute` `instance-attribute`
```
metadata: [, ] | None = None

```

Additional data that can be accessed programmatically by the application but is not sent to the LLM.
####  user_text_prompt `classmethod`
```
user_text_prompt(
    user_prompt: , *, instructions:  | None = None
) -> ModelRequest[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelRequest "ModelRequest



      dataclass
   \(pydantic_ai.messages.ModelRequest\)")

```

Create a `ModelRequest` with a single user prompt as text.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1243
1244
1245
