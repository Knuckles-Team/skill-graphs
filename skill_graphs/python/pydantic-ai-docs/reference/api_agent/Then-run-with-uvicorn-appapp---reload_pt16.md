


      module-attribute
   \(pydantic_ai.messages.ModelMessage\)")],
    parameters: ModelRequestParameters[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.ModelRequestParameters "ModelRequestParameters



      dataclass
   \(pydantic_ai.models.ModelRequestParameters\)") | None = None,
) -> [LogRecord]

```

Convert a list of model messages to OpenTelemetry events.
Parameters:
Name | Type | Description | Default
---|---|---|---
`messages` |  `ModelMessage[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage "ModelMessage



      module-attribute
   \(pydantic_ai.messages.ModelMessage\)")]` |  The messages to convert. |  _required_
`parameters` |  `ModelRequestParameters[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.ModelRequestParameters "ModelRequestParameters



      dataclass
   \(pydantic_ai.models.ModelRequestParameters\)") | None` |  The model request parameters. |  `None`
Returns:
Type | Description
---|---
`LogRecord]` |  A list of OpenTelemetry events.
Source code in `pydantic_ai_slim/pydantic_ai/models/instrumented.py`
```
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
```
| ```
def messages_to_otel_events(
    self, messages: list[ModelMessage], parameters: ModelRequestParameters | None = None
) -> list[LogRecord]:
    """Convert a list of model messages to OpenTelemetry events.

    Args:
        messages: The messages to convert.
        parameters: The model request parameters.

    Returns:
        A list of OpenTelemetry events.
    """
    events: list[LogRecord] = []
    instructions = InstrumentedModel._get_instructions(messages, parameters)  # pyright: ignore [reportPrivateUsage]
    if instructions is not None:
        events.append(
            LogRecord(
                attributes={'event.name': 'gen_ai.system.message'},
                body={**({'content': instructions} if self.include_content else {}), 'role': 'system'},
            )
        )

    for message_index, message in enumerate(messages):
        message_events: list[LogRecord] = []
        if isinstance(message, ModelRequest):
            for part in message.parts:
                if hasattr(part, 'otel_event'):
                    message_events.append(part.otel_event(self))
        elif isinstance(message, ModelResponse):  # pragma: no branch
            message_events = message.otel_events(self)
        for event in message_events:
            event.attributes = {
                'gen_ai.message.index': message_index,
                **(event.attributes or {}),
            }
        events.extend(message_events)

    for event in events:
        event.body = InstrumentedModel.serialize_any(event.body)
    return events

```

---|---
###  EventStreamHandler `module-attribute`
```
EventStreamHandler:  = [
    [
        RunContext[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
   \(pydantic_ai.tools.RunContext\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")],
        [AgentStreamEvent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.AgentStreamEvent "AgentStreamEvent



      module-attribute
   \(pydantic_ai.messages.AgentStreamEvent\)")],
    ],
    [None],
]

```

A function that receives agent [`RunContext`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
  ") and an async iterable of events from the model's streaming response and the agent's execution of tools.
© Pydantic Services Inc. 2024 to present
