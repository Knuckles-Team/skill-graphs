


      dataclass
   \(pydantic_ai.messages.BuiltinToolCallPart\)") | ToolCallPartDelta[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta "ToolCallPartDelta



      dataclass
   \(pydantic_ai.messages.ToolCallPartDelta\)")` |  Either a new `ToolCallPart` or `BuiltinToolCallPart`, or an updated `ToolCallPartDelta`.
Raises:
Type | Description
---|---
|  If `part` is neither a `ToolCallPart`, `BuiltinToolCallPart`, nor a `ToolCallPartDelta`.
`UnexpectedModelBehavior[](https://ai.pydantic.dev/api/exceptions/#pydantic_ai.exceptions.UnexpectedModelBehavior "UnexpectedModelBehavior \(pydantic_ai.exceptions.UnexpectedModelBehavior\)")` |  If applying JSON deltas to dict arguments or vice versa.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1964
1965
1966
1967
1968
1969
1970
1971
1972
1973
1974
1975
1976
1977
1978
1979
1980
1981
1982
1983
1984
1985
1986
1987
```
| ```
def apply(
    self, part: ModelResponsePart | ToolCallPartDelta
) -> ToolCallPart | BuiltinToolCallPart | ToolCallPartDelta:
    """Apply this delta to a part or delta, returning a new part or delta with the changes applied.

    Args:
        part: The existing model response part or delta to update.

    Returns:
        Either a new `ToolCallPart` or `BuiltinToolCallPart`, or an updated `ToolCallPartDelta`.

    Raises:
        ValueError: If `part` is neither a `ToolCallPart`, `BuiltinToolCallPart`, nor a `ToolCallPartDelta`.
        UnexpectedModelBehavior: If applying JSON deltas to dict arguments or vice versa.
    """
    if isinstance(part, ToolCallPart | BuiltinToolCallPart):
        return self._apply_to_part(part)

    if isinstance(part, ToolCallPartDelta):
        return self._apply_to_delta(part)

    raise ValueError(  # pragma: no cover
        f'Can only apply ToolCallPartDeltas to ToolCallParts, BuiltinToolCallParts, or ToolCallPartDeltas, not {part}'
    )

```

---|---
###  ModelResponsePartDelta `module-attribute`
```
ModelResponsePartDelta = [
    TextPartDelta[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPartDelta "TextPartDelta



      dataclass
   \(pydantic_ai.messages.TextPartDelta\)") | ThinkingPartDelta[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPartDelta "ThinkingPartDelta



      dataclass
   \(pydantic_ai.messages.ThinkingPartDelta\)") | ToolCallPartDelta[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta "ToolCallPartDelta



      dataclass
   \(pydantic_ai.messages.ToolCallPartDelta\)"),
    Discriminator[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Discriminator "pydantic.Discriminator")("part_delta_kind"),
]

```

A partial update (delta) for any model response part.
###  PartStartEvent `dataclass`
An event indicating that a new part has started.
If multiple `PartStartEvent`s are received with the same index, the new one should fully replace the old one.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
2072
2073
2074
2075
2076
2077
2078
2079
2080
2081
2082
2083
2084
2085
2086
2087
2088
2089
2090
2091
2092
2093
2094
2095
2096
2097
```
| ```
@dataclass(repr=False, kw_only=True)
class PartStartEvent:
    """An event indicating that a new part has started.

    If multiple `PartStartEvent`s are received with the same index,
    the new one should fully replace the old one.
    """

    index: int
    """The index of the part within the overall response parts list."""

    part: ModelResponsePart
    """The newly started `ModelResponsePart`."""

    previous_part_kind: (
        Literal['text', 'thinking', 'tool-call', 'builtin-tool-call', 'builtin-tool-return', 'file'] | None
    ) = None
    """The kind of the previous part, if any.

    This is useful for UI event streams to know whether to group parts of the same kind together when emitting events.
    """

    event_kind: Literal['part_start'] = 'part_start'
    """Event type identifier, used as a discriminator."""

    __repr__ = _utils.dataclasses_no_defaults_repr

```

---|---
####  index `instance-attribute`
```
index:

```

The index of the part within the overall response parts list.
####  part `instance-attribute`
```
part: ModelResponsePart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponsePart "ModelResponsePart



      module-attribute
   \(pydantic_ai.messages.ModelResponsePart\)")

```

The newly started `ModelResponsePart`.
####  previous_part_kind `class-attribute` `instance-attribute`
```
previous_part_kind: (
    [
        "text",
        "thinking",
        "tool-call",
        "builtin-tool-call",
        "builtin-tool-return",
        "file",
    ]
    | None
) = None

```

The kind of the previous part, if any.
This is useful for UI event streams to know whether to group parts of the same kind together when emitting events.
####  event_kind `class-attribute` `instance-attribute`
```
event_kind: ['part_start'] = 'part_start'

```

Event type identifier, used as a discriminator.
###  PartDeltaEvent `dataclass`
An event indicating a delta update for an existing part.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
2100
2101
2102
2103
2104
2105
2106
2107
2108
2109
2110
2111
2112
2113
```
| ```
@dataclass(repr=False, kw_only=True)
class PartDeltaEvent:
    """An event indicating a delta update for an existing part."""

    index: int
    """The index of the part within the overall response parts list."""

    delta: ModelResponsePartDelta
    """The delta to apply to the specified part."""

    event_kind: Literal['part_delta'] = 'part_delta'
    """Event type identifier, used as a discriminator."""

    __repr__ = _utils.dataclasses_no_defaults_repr

```

---|---
####  index `instance-attribute`
```
index:

```

The index of the part within the overall response parts list.
####  delta `instance-attribute`
```
delta: ModelResponsePartDelta[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponsePartDelta "ModelResponsePartDelta



      module-attribute
   \(pydantic_ai.messages.ModelResponsePartDelta\)")

```

The delta to apply to the specified part.
####  event_kind `class-attribute` `instance-attribute`
```
event_kind: ['part_delta'] = 'part_delta'

```

Event type identifier, used as a discriminator.
###  PartEndEvent `dataclass`
An event indicating that a part is complete.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
2116
2117
2118
2119
2120
2121
2122
2123
2124
2125
2126
2127
2128
2129
2130
2131
2132
2133
2134
2135
2136
2137
```
| ```
@dataclass(repr=False, kw_only=True)
class PartEndEvent:
    """An event indicating that a part is complete."""

    index: int
    """The index of the part within the overall response parts list."""

    part: ModelResponsePart
    """The complete `ModelResponsePart`."""

    next_part_kind: (
        Literal['text', 'thinking', 'tool-call', 'builtin-tool-call', 'builtin-tool-return', 'file'] | None
    ) = None
    """The kind of the next part, if any.

    This is useful for UI event streams to know whether to group parts of the same kind together when emitting events.
    """

    event_kind: Literal['part_end'] = 'part_end'
    """Event type identifier, used as a discriminator."""

    __repr__ = _utils.dataclasses_no_defaults_repr

```

---|---
####  index `instance-attribute`
```
index:

```

The index of the part within the overall response parts list.
####  part `instance-attribute`
```
part: ModelResponsePart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponsePart "ModelResponsePart



      module-attribute
   \(pydantic_ai.messages.ModelResponsePart\)")

```

The complete `ModelResponsePart`.
####  next_part_kind `class-attribute` `instance-attribute`
```
next_part_kind: (
    [
        "text",
        "thinking",
        "tool-call",
        "builtin-tool-call",
        "builtin-tool-return",
        "file",
    ]
    | None
) = None

```

The kind of the next part, if any.
This is useful for UI event streams to know whether to group parts of the same kind together when emitting events.
####  event_kind `class-attribute` `instance-attribute`
```
event_kind: ['part_end'] = 'part_end'

```

Event type identifier, used as a discriminator.
###  FinalResultEvent `dataclass`
An event indicating the response to the current model request matches the output schema and will produce a result.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
2140
2141
2142
2143
2144
2145
2146
2147
2148
2149
2150
2151
```
| ```
@dataclass(repr=False, kw_only=True)
class FinalResultEvent:
    """An event indicating the response to the current model request matches the output schema and will produce a result."""

    tool_name: str | None
    """The name of the output tool that was called. `None` if the result is from text content and not from a tool."""
    tool_call_id: str | None
    """The tool call ID, if any, that this result is associated with."""
    event_kind: Literal['final_result'] = 'final_result'
    """Event type identifier, used as a discriminator."""

    __repr__ = _utils.dataclasses_no_defaults_repr

```

---|---
####  tool_name `instance-attribute`
```
tool_name:  | None

```

The name of the output tool that was called. `None` if the result is from text content and not from a tool.
####  tool_call_id `instance-attribute`
```
tool_call_id:  | None

```

The tool call ID, if any, that this result is associated with.
####  event_kind `class-attribute` `instance-attribute`
```
event_kind: ['final_result'] = 'final_result'

```

Event type identifier, used as a discriminator.
###  ModelResponseStreamEvent `module-attribute`
```
ModelResponseStreamEvent = [
    PartStartEvent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartStartEvent "PartStartEvent



      dataclass
   \(pydantic_ai.messages.PartStartEvent\)")
    | PartDeltaEvent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartDeltaEvent "PartDeltaEvent



      dataclass
   \(pydantic_ai.messages.PartDeltaEvent\)")
    | PartEndEvent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartEndEvent "PartEndEvent



      dataclass
   \(pydantic_ai.messages.PartEndEvent\)")
    | FinalResultEvent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FinalResultEvent "FinalResultEvent



      dataclass
   \(pydantic_ai.messages.FinalResultEvent\)"),
    Discriminator[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Discriminator "pydantic.Discriminator")("event_kind"),
]

```

An event in the model response stream, starting a new part, applying a delta to an existing one, indicating a part is complete, or indicating the final result.
###  FunctionToolCallEvent `dataclass`
An event indicating the start to a call to a function tool.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
2160
2161
2162
2163
2164
2165
2166
2167
2168
2169
2170
2171
2172
2173
2174
2175
2176
2177
2178
2179
2180
2181
2182
2183
2184
2185
2186
2187
2188
2189
2190
2191
2192
```
| ```
@dataclass(repr=False)
class FunctionToolCallEvent:
    """An event indicating the start to a call to a function tool."""

    part: ToolCallPart
    """The (function) tool call to make."""

    _: KW_ONLY

    args_valid: bool | None = None
    """Whether the tool arguments passed validation.
    See the [custom validation docs](https://ai.pydantic.dev/tools-advanced/#args-validator) for more info.

    - `True`: Schema validation and custom validation (if configured) both passed; args are guaranteed valid.
    - `False`: Validation was performed and failed.
    - `None`: Validation was not performed.
    """

    event_kind: Literal['function_tool_call'] = 'function_tool_call'
    """Event type identifier, used as a discriminator."""

    @property
    def tool_call_id(self) -> str:
        """An ID used for matching details about the call to its result."""
        return self.part.tool_call_id

    @property
    @deprecated('`call_id` is deprecated, use `tool_call_id` instead.')
    def call_id(self) -> str:
        """An ID used for matching details about the call to its result."""
        return self.part.tool_call_id  # pragma: no cover

    __repr__ = _utils.dataclasses_no_defaults_repr

```

---|---
####  part `instance-attribute`
```
part: ToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart "ToolCallPart



      dataclass
   \(pydantic_ai.messages.ToolCallPart\)")

```

The (function) tool call to make.
####  args_valid `class-attribute` `instance-attribute`
```
args_valid:  | None = None

```

Whether the tool arguments passed validation. See the [custom validation docs](https://ai.pydantic.dev/tools-advanced/#args-validator) for more info.
  * `True`: Schema validation and custom validation (if configured) both passed; args are guaranteed valid.
  * `False`: Validation was performed and failed.
  * `None`: Validation was not performed.


####  event_kind `class-attribute` `instance-attribute`
```
event_kind: ["function_tool_call"] = (
    "function_tool_call"
)

```

Event type identifier, used as a discriminator.
####  tool_call_id `property`
```
tool_call_id:

```

An ID used for matching details about the call to its result.
####  call_id `property`
```
call_id:

```

An ID used for matching details about the call to its result.
###  FunctionToolResultEvent `dataclass`
An event indicating the result of a function tool call.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
2195
2196
2197
2198
2199
2200
2201
2202
2203
2204
2205
2206
2207
2208
2209
2210
2211
2212
2213
2214
2215
```
| ```
@dataclass(repr=False)
class FunctionToolResultEvent:
    """An event indicating the result of a function tool call."""

    result: ToolReturnPart | RetryPromptPart
    """The result of the call to the function tool."""

    _: KW_ONLY

    content: str | Sequence[UserContent] | None = None
    """The content that will be sent to the model as a UserPromptPart following the result."""

    event_kind: Literal['function_tool_result'] = 'function_tool_result'
    """Event type identifier, used as a discriminator."""

    @property
    def tool_call_id(self) -> str:
        """An ID used to match the result to its original call."""
        return self.result.tool_call_id

    __repr__ = _utils.dataclasses_no_defaults_repr

```

---|---
####  result `instance-attribute`
```
result: ToolReturnPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolReturnPart "ToolReturnPart



      dataclass
   \(pydantic_ai.messages.ToolReturnPart\)") | RetryPromptPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.RetryPromptPart "RetryPromptPart



      dataclass
   \(pydantic_ai.messages.RetryPromptPart\)")

```

The result of the call to the function tool.
####  content `class-attribute` `instance-attribute`
```
content:  | [UserContent] | None = None

```

The content that will be sent to the model as a UserPromptPart following the result.
####  event_kind `class-attribute` `instance-attribute`
```
event_kind: ["function_tool_result"] = (
    "function_tool_result"
)

```

Event type identifier, used as a discriminator.
####  tool_call_id `property`
```
tool_call_id:

```

An ID used to match the result to its original call.
###  BuiltinToolCallEvent `dataclass` `deprecated`
Deprecated
`BuiltinToolCallEvent` is deprecated, look for `PartStartEvent` and `PartDeltaEvent` with `BuiltinToolCallPart` instead.
An event indicating the start to a call to a built-in tool.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
2218
2219
2220
2221
2222
2223
2224
2225
2226
2227
2228
2229
2230
2231
```
| ```
@deprecated(
    '`BuiltinToolCallEvent` is deprecated, look for `PartStartEvent` and `PartDeltaEvent` with `BuiltinToolCallPart` instead.'
)
@dataclass(repr=False)
class BuiltinToolCallEvent:
    """An event indicating the start to a call to a built-in tool."""

    part: BuiltinToolCallPart
    """The built-in tool call to make."""

    _: KW_ONLY

    event_kind: Literal['builtin_tool_call'] = 'builtin_tool_call'
    """Event type identifier, used as a discriminator."""

```

---|---
####  part `instance-attribute`
```
part: BuiltinToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolCallPart "BuiltinToolCallPart



      dataclass
   \(pydantic_ai.messages.BuiltinToolCallPart\)")

```

The built-in tool call to make.
####  event_kind `class-attribute` `instance-attribute`
```
event_kind: ["builtin_tool_call"] = (
    "builtin_tool_call"
)

```

Event type identifier, used as a discriminator.
###  BuiltinToolResultEvent `dataclass` `deprecated`
Deprecated
`BuiltinToolResultEvent` is deprecated, look for `PartStartEvent` and `PartDeltaEvent` with `BuiltinToolReturnPart` instead.
An event indicating the result of a built-in tool call.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
2234
2235
2236
2237
2238
2239
2240
2241
2242
2243
2244
2245
2246
2247
```
| ```
@deprecated(
    '`BuiltinToolResultEvent` is deprecated, look for `PartStartEvent` and `PartDeltaEvent` with `BuiltinToolReturnPart` instead.'
)
@dataclass(repr=False)
class BuiltinToolResultEvent:
    """An event indicating the result of a built-in tool call."""

    result: BuiltinToolReturnPart
    """The result of the call to the built-in tool."""

    _: KW_ONLY

    event_kind: Literal['builtin_tool_result'] = 'builtin_tool_result'
    """Event type identifier, used as a discriminator."""

```

---|---
####  result `instance-attribute`
```
result: BuiltinToolReturnPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolReturnPart "BuiltinToolReturnPart



      dataclass
   \(pydantic_ai.messages.BuiltinToolReturnPart\)")

```

The result of the call to the built-in tool.
####  event_kind `class-attribute` `instance-attribute`
```
event_kind: ["builtin_tool_result"] = (
    "builtin_tool_result"
)

```

Event type identifier, used as a discriminator.
###  HandleResponseEvent `module-attribute`
```
HandleResponseEvent = [
    FunctionToolCallEvent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FunctionToolCallEvent "FunctionToolCallEvent



      dataclass
   \(pydantic_ai.messages.FunctionToolCallEvent\)")
    | FunctionToolResultEvent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FunctionToolResultEvent "FunctionToolResultEvent



      dataclass
   \(pydantic_ai.messages.FunctionToolResultEvent\)")
    | BuiltinToolCallEvent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolCallEvent "BuiltinToolCallEvent



      dataclass
      deprecated
   \(pydantic_ai.messages.BuiltinToolCallEvent\)")
    | BuiltinToolResultEvent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolResultEvent "BuiltinToolResultEvent



      dataclass
      deprecated
   \(pydantic_ai.messages.BuiltinToolResultEvent\)"),
    Discriminator[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Discriminator "pydantic.Discriminator")("event_kind"),
]

```

An event yielded when handling a model response, indicating tool calls and results.
###  AgentStreamEvent `module-attribute`
```
AgentStreamEvent = [
    ModelResponseStreamEvent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponseStreamEvent "ModelResponseStreamEvent



      module-attribute
   \(pydantic_ai.messages.ModelResponseStreamEvent\)") | HandleResponseEvent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.HandleResponseEvent "HandleResponseEvent



      module-attribute
   \(pydantic_ai.messages.HandleResponseEvent\)"),
    Discriminator[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Discriminator "pydantic.Discriminator")("event_kind"),
]

```

An event in the agent stream: model response stream events and response-handling events.
© Pydantic Services Inc. 2024 to present
