# pydantic_ai.models.instrumented
###  instrument_model
```
instrument_model(
    model: Model[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.Model "Model \(pydantic_ai.models.Model\)"), instrument: InstrumentationSettings[](https://ai.pydantic.dev/api/models/instrumented/#pydantic_ai.models.instrumented.InstrumentationSettings "InstrumentationSettings



      dataclass
   \(pydantic_ai.models.instrumented.InstrumentationSettings\)") |
) -> Model[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.Model "Model \(pydantic_ai.models.Model\)")

```

Instrument a model with OpenTelemetry/logfire.
Source code in `pydantic_ai_slim/pydantic_ai/models/instrumented.py`
```
66
67
68
69
70
71
72
73
74
```
| ```
def instrument_model(model: Model, instrument: InstrumentationSettings | bool) -> Model:
    """Instrument a model with OpenTelemetry/logfire."""
    if instrument and not isinstance(model, InstrumentedModel):
        if instrument is True:
            instrument = InstrumentationSettings()

        model = InstrumentedModel(model, instrument)

    return model

```

---|---
###  InstrumentationSettings `dataclass`
Options for instrumenting models and agents with OpenTelemetry.
Used in:
  * `Agent(instrument=...)`
  * [`Agent.instrument_all()`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.instrument_all "instrument_all



      staticmethod
  ")
  * [`InstrumentedModel`](https://ai.pydantic.dev/api/models/instrumented/#pydantic_ai.models.instrumented.InstrumentedModel "InstrumentedModel



      dataclass
  ")


See the [Debugging and Monitoring guide](https://ai.pydantic.dev/logfire/) for more info.
Source code in `pydantic_ai_slim/pydantic_ai/models/instrumented.py`
```
 77
 78
 79
 80
 81
 82
 83
 84
 85
 86
 87
 88
 89
 90
 91
 92
 93
 94
 95
 96
 97
 98
 99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
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
235
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
262
263
264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
295
296
297
298
299
300
301
302
303
304
305
306
307
308
309
310
311
312
313
314
315
316
317
318
319
320
321
322
323
324
325
326
327
328
329
330
331
332
333
334
335
336
337
338
339
340
341
342
343
344
345
346
347
348
349
350
351
352
353
```
| ```
@dataclass(init=False)
class InstrumentationSettings:
    """Options for instrumenting models and agents with OpenTelemetry.

    Used in:

    - `Agent(instrument=...)`
    - [`Agent.instrument_all()`][pydantic_ai.agent.Agent.instrument_all]
    - [`InstrumentedModel`][pydantic_ai.models.instrumented.InstrumentedModel]

    See the [Debugging and Monitoring guide](https://ai.pydantic.dev/logfire/) for more info.
    """

    tracer: Tracer = field(repr=False)
    logger: Logger = field(repr=False)
    event_mode: Literal['attributes', 'logs'] = 'attributes'
    include_binary_content: bool = True
    include_content: bool = True
    version: Literal[1, 2, 3, 4] = DEFAULT_INSTRUMENTATION_VERSION
    use_aggregated_usage_attribute_names: bool = False

    def __init__(
        self,
        *,
        tracer_provider: TracerProvider | None = None,
        meter_provider: MeterProvider | None = None,
        include_binary_content: bool = True,
        include_content: bool = True,
        version: Literal[1, 2, 3, 4] = DEFAULT_INSTRUMENTATION_VERSION,
        event_mode: Literal['attributes', 'logs'] = 'attributes',
        logger_provider: LoggerProvider | None = None,
        use_aggregated_usage_attribute_names: bool = False,
    ):
        """Create instrumentation options.

        Args:
            tracer_provider: The OpenTelemetry tracer provider to use.
                If not provided, the global tracer provider is used.
                Calling `logfire.configure()` sets the global tracer provider, so most users don't need this.
            meter_provider: The OpenTelemetry meter provider to use.
                If not provided, the global meter provider is used.
                Calling `logfire.configure()` sets the global meter provider, so most users don't need this.
            include_binary_content: Whether to include binary content in the instrumentation events.
            include_content: Whether to include prompts, completions, and tool call arguments and responses
                in the instrumentation events.
            version: Version of the data format. This is unrelated to the Pydantic AI package version.
                Version 1 is based on the legacy event-based OpenTelemetry GenAI spec
                    and will be removed in a future release.
                    The parameters `event_mode` and `logger_provider` are only relevant for version 1.
                Version 2 uses the newer OpenTelemetry GenAI spec and stores messages in the following attributes:
                    - `gen_ai.system_instructions` for instructions passed to the agent.
                    - `gen_ai.input.messages` and `gen_ai.output.messages` on model request spans.
                    - `pydantic_ai.all_messages` on agent run spans.
                Version 3 is the same as version 2, with additional support for thinking tokens.
                Version 4 is the same as version 3, with GenAI semantic conventions for multimodal content:
                    URL-based media uses type='uri' with uri and mime_type fields (and modality for image/audio/video).
                    Inline binary content uses type='blob' with mime_type and content fields (and modality for image/audio/video).
                    https://opentelemetry.io/docs/specs/semconv/gen-ai/non-normative/examples-llm-calls/#multimodal-inputs-example
            event_mode: The mode for emitting events in version 1.
                If `'attributes'`, events are attached to the span as attributes.
                If `'logs'`, events are emitted as OpenTelemetry log-based events.
            logger_provider: The OpenTelemetry logger provider to use.
                If not provided, the global logger provider is used.
                Calling `logfire.configure()` sets the global logger provider, so most users don't need this.
                This is only used if `event_mode='logs'` and `version=1`.
            use_aggregated_usage_attribute_names: Whether to use `gen_ai.aggregated_usage.*` attribute names
                for token usage on agent run spans instead of the standard `gen_ai.usage.*` names.
                Enable this to prevent double-counting in observability backends that aggregate span
                attributes across parent and child spans. Defaults to False.
                Note: `gen_ai.aggregated_usage.*` is a custom namespace, not part of the OpenTelemetry
                Semantic Conventions. It may be updated if OTel introduces an official convention.
        """
        from pydantic_ai import __version__

        tracer_provider = tracer_provider or get_tracer_provider()
        meter_provider = meter_provider or get_meter_provider()
        logger_provider = logger_provider or get_logger_provider()
        scope_name = 'pydantic-ai'
        self.tracer = tracer_provider.get_tracer(scope_name, __version__)
        self.meter = meter_provider.get_meter(scope_name, __version__)
        self.logger = logger_provider.get_logger(scope_name, __version__)
        self.event_mode = event_mode
        self.include_binary_content = include_binary_content
        self.include_content = include_content

        if event_mode == 'logs' and version != 1:
            warnings.warn(
                'event_mode is only relevant for version=1 which is deprecated and will be removed in a future release.',
                stacklevel=2,
            )
            version = 1

        self.version = version
        self.use_aggregated_usage_attribute_names = use_aggregated_usage_attribute_names

        # As specified in the OpenTelemetry GenAI metrics spec:
        # https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-metrics/#metric-gen_aiclienttokenusage
        tokens_histogram_kwargs = dict(
            name='gen_ai.client.token.usage',
            unit='{token}',
            description='Measures number of input and output tokens used',
        )
        try:
            self.tokens_histogram = self.meter.create_histogram(
                **tokens_histogram_kwargs,
                explicit_bucket_boundaries_advisory=TOKEN_HISTOGRAM_BOUNDARIES,
            )
        except TypeError:  # pragma: lax no cover
            # Older OTel/logfire versions don't support explicit_bucket_boundaries_advisory
            self.tokens_histogram = self.meter.create_histogram(
                **tokens_histogram_kwargs,  # pyright: ignore
            )
        self.cost_histogram = self.meter.create_histogram(
            'operation.cost',
            unit='{USD}',
            description='Monetary cost',
        )

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

    def messages_to_otel_messages(self, messages: list[ModelMessage]) -> list[_otel_messages.ChatMessage]:
        result: list[_otel_messages.ChatMessage] = []
        for message in messages:
            if isinstance(message, ModelRequest):
                for is_system, group in itertools.groupby(message.parts, key=lambda p: isinstance(p, SystemPromptPart)):
                    message_parts: list[_otel_messages.MessagePart] = []
                    for part in group:
                        if hasattr(part, 'otel_message_parts'):
                            message_parts.extend(part.otel_message_parts(self))

                    result.append(
                        _otel_messages.ChatMessage(role='system' if is_system else 'user', parts=message_parts)
                    )
            elif isinstance(message, ModelResponse):  # pragma: no branch
                otel_message = _otel_messages.OutputMessage(role='assistant', parts=message.otel_message_parts(self))
                if message.finish_reason is not None:
                    otel_message['finish_reason'] = message.finish_reason
                result.append(otel_message)
        return result

    def handle_messages(
        self,
        input_messages: list[ModelMessage],
        response: ModelResponse,
        system: str,
        span: Span,
        parameters: ModelRequestParameters | None = None,
    ):
        if self.version == 1:
            events = self.messages_to_otel_events(input_messages, parameters)
            for event in self.messages_to_otel_events([response], parameters):
                events.append(
                    LogRecord(
                        attributes={'event.name': 'gen_ai.choice'},
                        body={
                            'index': 0,
                            'message': event.body,
                        },
                    )
                )
            for event in events:
                event.attributes = {
                    GEN_AI_SYSTEM_ATTRIBUTE: system,
                    **(event.attributes or {}),
                }
            self._emit_events(span, events)
        else:
            output_messages = self.messages_to_otel_messages([response])
            assert len(output_messages) == 1
            output_message = output_messages[0]

            instructions = InstrumentedModel._get_instructions(input_messages, parameters)  # pyright: ignore [reportPrivateUsage]
            system_instructions_attributes = self.system_instructions_attributes(instructions)

            attributes: dict[str, AttributeValue] = {
                'gen_ai.input.messages': json.dumps(self.messages_to_otel_messages(input_messages)),
                'gen_ai.output.messages': json.dumps([output_message]),
                **system_instructions_attributes,
                'logfire.json_schema': json.dumps(
                    {
                        'type': 'object',
                        'properties': {
                            'gen_ai.input.messages': {'type': 'array'},
                            'gen_ai.output.messages': {'type': 'array'},
                            **(
                                {'gen_ai.system_instructions': {'type': 'array'}}
                                if system_instructions_attributes
                                else {}
                            ),
                            'model_request_parameters': {'type': 'object'},
                        },
                    }
                ),
            }
            span.set_attributes(attributes)

    def system_instructions_attributes(self, instructions: str | None) -> dict[str, str]:
        if instructions and self.include_content:
            return {
                'gen_ai.system_instructions': json.dumps([_otel_messages.TextPart(type='text', content=instructions)]),
            }
        return {}

    def _emit_events(self, span: Span, events: list[LogRecord]) -> None:
        if self.event_mode == 'logs':
            for event in events:
                self.logger.emit(event)
        else:
            attr_name = 'events'
            span.set_attributes(
                {
                    attr_name: json.dumps([InstrumentedModel.event_to_dict(event) for event in events]),
                    'logfire.json_schema': json.dumps(
                        {
                            'type': 'object',
                            'properties': {
                                attr_name: {'type': 'array'},
                                'model_request_parameters': {'type': 'object'},
                            },
                        }
                    ),
                }
            )

    def record_metrics(
        self,
        response: ModelResponse,
        price_calculation: PriceCalculation | None,
        attributes: dict[str, AttributeValue],
    ):
        for typ in ['input', 'output']:
            if not (tokens := getattr(response.usage, f'{typ}_tokens', 0)):  # pragma: no cover
                continue
            token_attributes = {**attributes, 'gen_ai.token.type': typ}
            self.tokens_histogram.record(tokens, token_attributes)
            if price_calculation:
                cost = float(getattr(price_calculation, f'{typ}_price'))
                self.cost_histogram.record(cost, token_attributes)

```

---|---
####  __init__
```
__init__(
    *,
    tracer_provider: TracerProvider | None = None,
    meter_provider: MeterProvider | None = None,
    include_binary_content:  = True,
    include_content:  = True,
    version: [
        1, 2, 3, 4
    ] = DEFAULT_INSTRUMENTATION_VERSION,
    event_mode: [
        "attributes", "logs"
    ] = "attributes",
    logger_provider: LoggerProvider | None = None,
    use_aggregated_usage_attribute_names:  = False
)

```

Create instrumentation options.
Parameters:
Name | Type | Description | Default
---|---|---|---
`tracer_provider` |  `TracerProvider | None` |  The OpenTelemetry tracer provider to use. If not provided, the global tracer provider is used. Calling `logfire.configure()` sets the global tracer provider, so most users don't need this. |  `None`
`meter_provider` |  `MeterProvider | None` |  The OpenTelemetry meter provider to use. If not provided, the global meter provider is used. Calling `logfire.configure()` sets the global meter provider, so most users don't need this. |  `None`
`include_binary_content` |  |  Whether to include binary content in the instrumentation events. |  `True`
`include_content` |  |  Whether to include prompts, completions, and tool call arguments and responses in the instrumentation events. |  `True`
`version` |  |  Version of the data format. This is unrelated to the Pydantic AI package version. Version 1 is based on the legacy event-based OpenTelemetry GenAI spec and will be removed in a future release. The parameters `event_mode` and `logger_provider` are only relevant for version 1. Version 2 uses the newer OpenTelemetry GenAI spec and stores messages in the following attributes: - `gen_ai.system_instructions` for instructions passed to the agent. - `gen_ai.input.messages` and `gen_ai.output.messages` on model request spans. - `pydantic_ai.all_messages` on agent run spans. Version 3 is the same as version 2, with additional support for thinking tokens. Version 4 is the same as version 3, with GenAI semantic conventions for multimodal content: URL-based media uses type='uri' with uri and mime_type fields (and modality for image/audio/video). Inline binary content uses type='blob' with mime_type and content fields (and modality for image/audio/video). https://opentelemetry.io/docs/specs/semconv/gen-ai/non-normative/examples-llm-calls/#multimodal-inputs-example |  `DEFAULT_INSTRUMENTATION_VERSION`
`event_mode` |  |  The mode for emitting events in version 1. If `'attributes'`, events are attached to the span as attributes. If `'logs'`, events are emitted as OpenTelemetry log-based events. |  `'attributes'`
`logger_provider` |  `LoggerProvider | None` |  The OpenTelemetry logger provider to use. If not provided, the global logger provider is used. Calling `logfire.configure()` sets the global logger provider, so most users don't need this. This is only used if `event_mode='logs'` and `version=1`. |  `None`
`use_aggregated_usage_attribute_names` |  |  Whether to use `gen_ai.aggregated_usage.*` attribute names for token usage on agent run spans instead of the standard `gen_ai.usage.*` names. Enable this to prevent double-counting in observability backends that aggregate span attributes across parent and child spans. Defaults to False. Note: `gen_ai.aggregated_usage.*` is a custom namespace, not part of the OpenTelemetry Semantic Conventions. It may be updated if OTel introduces an official convention. |  `False`
Source code in `pydantic_ai_slim/pydantic_ai/models/instrumented.py`
```
 98
 99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
```
| ```
def __init__(
    self,
    *,
    tracer_provider: TracerProvider | None = None,
    meter_provider: MeterProvider | None = None,
    include_binary_content: bool = True,
    include_content: bool = True,
    version: Literal[1, 2, 3, 4] = DEFAULT_INSTRUMENTATION_VERSION,
    event_mode: Literal['attributes', 'logs'] = 'attributes',
    logger_provider: LoggerProvider | None = None,
    use_aggregated_usage_attribute_names: bool = False,
):
    """Create instrumentation options.

    Args:
        tracer_provider: The OpenTelemetry tracer provider to use.
            If not provided, the global tracer provider is used.
            Calling `logfire.configure()` sets the global tracer provider, so most users don't need this.
        meter_provider: The OpenTelemetry meter provider to use.
            If not provided, the global meter provider is used.
            Calling `logfire.configure()` sets the global meter provider, so most users don't need this.
        include_binary_content: Whether to include binary content in the instrumentation events.
        include_content: Whether to include prompts, completions, and tool call arguments and responses
            in the instrumentation events.
        version: Version of the data format. This is unrelated to the Pydantic AI package version.
            Version 1 is based on the legacy event-based OpenTelemetry GenAI spec
                and will be removed in a future release.
                The parameters `event_mode` and `logger_provider` are only relevant for version 1.
            Version 2 uses the newer OpenTelemetry GenAI spec and stores messages in the following attributes:
                - `gen_ai.system_instructions` for instructions passed to the agent.
                - `gen_ai.input.messages` and `gen_ai.output.messages` on model request spans.
                - `pydantic_ai.all_messages` on agent run spans.
            Version 3 is the same as version 2, with additional support for thinking tokens.
            Version 4 is the same as version 3, with GenAI semantic conventions for multimodal content:
                URL-based media uses type='uri' with uri and mime_type fields (and modality for image/audio/video).
                Inline binary content uses type='blob' with mime_type and content fields (and modality for image/audio/video).
                https://opentelemetry.io/docs/specs/semconv/gen-ai/non-normative/examples-llm-calls/#multimodal-inputs-example
        event_mode: The mode for emitting events in version 1.
            If `'attributes'`, events are attached to the span as attributes.
            If `'logs'`, events are emitted as OpenTelemetry log-based events.
        logger_provider: The OpenTelemetry logger provider to use.
            If not provided, the global logger provider is used.
            Calling `logfire.configure()` sets the global logger provider, so most users don't need this.
            This is only used if `event_mode='logs'` and `version=1`.
        use_aggregated_usage_attribute_names: Whether to use `gen_ai.aggregated_usage.*` attribute names
            for token usage on agent run spans instead of the standard `gen_ai.usage.*` names.
            Enable this to prevent double-counting in observability backends that aggregate span
            attributes across parent and child spans. Defaults to False.
            Note: `gen_ai.aggregated_usage.*` is a custom namespace, not part of the OpenTelemetry
            Semantic Conventions. It may be updated if OTel introduces an official convention.
    """
    from pydantic_ai import __version__

    tracer_provider = tracer_provider or get_tracer_provider()
    meter_provider = meter_provider or get_meter_provider()
    logger_provider = logger_provider or get_logger_provider()
    scope_name = 'pydantic-ai'
    self.tracer = tracer_provider.get_tracer(scope_name, __version__)
    self.meter = meter_provider.get_meter(scope_name, __version__)
    self.logger = logger_provider.get_logger(scope_name, __version__)
    self.event_mode = event_mode
    self.include_binary_content = include_binary_content
    self.include_content = include_content

    if event_mode == 'logs' and version != 1:
        warnings.warn(
            'event_mode is only relevant for version=1 which is deprecated and will be removed in a future release.',
            stacklevel=2,
        )
        version = 1

    self.version = version
    self.use_aggregated_usage_attribute_names = use_aggregated_usage_attribute_names

    # As specified in the OpenTelemetry GenAI metrics spec:
    # https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-metrics/#metric-gen_aiclienttokenusage
    tokens_histogram_kwargs = dict(
        name='gen_ai.client.token.usage',
        unit='{token}',
        description='Measures number of input and output tokens used',
    )
    try:
        self.tokens_histogram = self.meter.create_histogram(
            **tokens_histogram_kwargs,
            explicit_bucket_boundaries_advisory=TOKEN_HISTOGRAM_BOUNDARIES,
        )
    except TypeError:  # pragma: lax no cover
        # Older OTel/logfire versions don't support explicit_bucket_boundaries_advisory
        self.tokens_histogram = self.meter.create_histogram(
            **tokens_histogram_kwargs,  # pyright: ignore
        )
    self.cost_histogram = self.meter.create_histogram(
        'operation.cost',
        unit='{USD}',
        description='Monetary cost',
    )

```

---|---
####  messages_to_otel_events
```
messages_to_otel_events(
    messages: [ModelMessage[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage "ModelMessage



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
###  InstrumentedModel `dataclass`
Bases: `WrapperModel[](https://ai.pydantic.dev/api/models/wrapper/#pydantic_ai.models.wrapper.WrapperModel "WrapperModel



      dataclass
   \(pydantic_ai.models.wrapper.WrapperModel\)")`
Model which wraps another model so that requests are instrumented with OpenTelemetry.
See the [Debugging and Monitoring guide](https://ai.pydantic.dev/logfire/) for more info.
Source code in `pydantic_ai_slim/pydantic_ai/models/instrumented.py`
```
384
385
386
387
388
389
390
391
392
393
394
395
396
397
398
399
400
401
402
403
404
405
406
407
408
409
410
411
412
413
414
415
416
417
418
419
420
421
422
423
424
425
426
427
428
429
430
431
432
433
434
435
436
437
438
439
440
441
442
443
444
445
446
447
448
449
450
451
452
453
454
455
456
457
458
459
460
461
462
463
464
465
466
467
468
469
470
471
472
473
474
475
476
477
478
479
480
481
482
483
484
485
486
487
488
489
490
491
492
493
494
495
496
497
498
499
500
501
502
503
504
505
506
507
508
509
510
511
512
513
514
515
516
517
518
519
520
521
522
523
524
525
526
527
528
529
530
531
532
533
534
535
536
537
538
539
540
541
542
543
544
545
546
547
548
549
550
551
552
553
554
555
556
557
558
559
560
561
562
563
564
565
566
567
568
569
570
571
572
573
574
575
576
577
578
579
580
```
| ```
@dataclass(init=False)
class InstrumentedModel(WrapperModel):
    """Model which wraps another model so that requests are instrumented with OpenTelemetry.

    See the [Debugging and Monitoring guide](https://ai.pydantic.dev/logfire/) for more info.
    """

    instrumentation_settings: InstrumentationSettings
    """Instrumentation settings for this model."""

    def __init__(
        self,
        wrapped: Model | KnownModelName,
        options: InstrumentationSettings | None = None,
    ) -> None:
        super().__init__(wrapped)
        self.instrumentation_settings = options or InstrumentationSettings()

    async def request(
        self,
        messages: list[ModelMessage],
        model_settings: ModelSettings | None,
        model_request_parameters: ModelRequestParameters,
    ) -> ModelResponse:
        prepared_settings, prepared_parameters = self.wrapped.prepare_request(
            model_settings,
            model_request_parameters,
        )
        with self._instrument(messages, prepared_settings, prepared_parameters) as finish:
            response = await self.wrapped.request(messages, model_settings, model_request_parameters)
            finish(response, prepared_parameters)
            return response

    @asynccontextmanager
    async def request_stream(
        self,
        messages: list[ModelMessage],
        model_settings: ModelSettings | None,
        model_request_parameters: ModelRequestParameters,
        run_context: RunContext[Any] | None = None,
    ) -> AsyncIterator[StreamedResponse]:
        prepared_settings, prepared_parameters = self.wrapped.prepare_request(
            model_settings,
            model_request_parameters,
        )
        with self._instrument(messages, prepared_settings, prepared_parameters) as finish:
            response_stream: StreamedResponse | None = None
            try:
                async with self.wrapped.request_stream(
                    messages, model_settings, model_request_parameters, run_context
                ) as response_stream:
                    yield response_stream
            finally:
                if response_stream:  # pragma: no branch
                    finish(response_stream.get(), prepared_parameters)

    @contextmanager
    def _instrument(
        self,
        messages: list[ModelMessage],
        model_settings: ModelSettings | None,
        model_request_parameters: ModelRequestParameters,
    ) -> Iterator[Callable[[ModelResponse, ModelRequestParameters], None]]:
        operation = 'chat'
        span_name = f'{operation} {self.model_name}'
        # TODO Missing attributes:
        #  - error.type: unclear if we should do something here or just always rely on span exceptions
        #  - gen_ai.request.stop_sequences/top_k: model_settings doesn't include these
        attributes: dict[str, AttributeValue] = {
            'gen_ai.operation.name': operation,
            **self.model_attributes(self.wrapped),
            **self.model_request_parameters_attributes(model_request_parameters),
            'logfire.json_schema': json.dumps(
                {
                    'type': 'object',
                    'properties': {'model_request_parameters': {'type': 'object'}},
                }
            ),
        }

        tool_definitions = _build_tool_definitions(model_request_parameters)
        if tool_definitions:
            attributes['gen_ai.tool.definitions'] = json.dumps(tool_definitions)

        if model_settings:
            for key in MODEL_SETTING_ATTRIBUTES:
                if isinstance(value := model_settings.get(key), float | int):
                    attributes[f'gen_ai.request.{key}'] = value

        record_metrics: Callable[[], None] | None = None
        try:
            with self.instrumentation_settings.tracer.start_as_current_span(
                span_name, attributes=attributes, kind=SpanKind.CLIENT
            ) as span:

                def finish(response: ModelResponse, parameters: ModelRequestParameters):
                    # FallbackModel updates these span attributes.
                    attributes.update(getattr(span, 'attributes', {}))
                    request_model = attributes[GEN_AI_REQUEST_MODEL_ATTRIBUTE]
                    system = cast(str, attributes[GEN_AI_SYSTEM_ATTRIBUTE])

                    response_model = response.model_name or request_model
                    price_calculation = None

                    def _record_metrics():
                        metric_attributes = {
                            GEN_AI_PROVIDER_NAME_ATTRIBUTE: system,  # New OTel standard attribute
                            GEN_AI_SYSTEM_ATTRIBUTE: system,  # Preserved for backward compatibility (deprecated)
                            'gen_ai.operation.name': operation,
                            'gen_ai.request.model': request_model,
                            'gen_ai.response.model': response_model,
                        }
                        self.instrumentation_settings.record_metrics(response, price_calculation, metric_attributes)

                    nonlocal record_metrics
                    record_metrics = _record_metrics

                    if not span.is_recording():
                        return

                    self.instrumentation_settings.handle_messages(messages, response, system, span, parameters)

                    attributes_to_set = {
                        **response.usage.opentelemetry_attributes(),
                        'gen_ai.response.model': response_model,
                    }
                    try:
                        price_calculation = response.cost()
                    except LookupError:
                        # The cost of this provider/model is unknown, which is common.
                        pass
                    except Exception as e:
                        warnings.warn(
                            f'Failed to get cost from response: {type(e).__name__}: {e}', CostCalculationFailedWarning
                        )
                    else:
                        attributes_to_set['operation.cost'] = float(price_calculation.total_price)

                    if response.provider_response_id is not None:
                        attributes_to_set['gen_ai.response.id'] = response.provider_response_id
                    if response.finish_reason is not None:
                        attributes_to_set['gen_ai.response.finish_reasons'] = [response.finish_reason]
                    span.set_attributes(attributes_to_set)
                    span.update_name(f'{operation} {request_model}')

                yield finish
        finally:
            if record_metrics:
                # We only want to record metrics after the span is finished,
                # to prevent them from being redundantly recorded in the span itself by logfire.
                record_metrics()

    @staticmethod
    def model_attributes(model: Model) -> dict[str, AttributeValue]:
        attributes: dict[str, AttributeValue] = {
            GEN_AI_PROVIDER_NAME_ATTRIBUTE: model.system,  # New OTel standard attribute
            GEN_AI_SYSTEM_ATTRIBUTE: model.system,  # Preserved for backward compatibility (deprecated)
            GEN_AI_REQUEST_MODEL_ATTRIBUTE: model.model_name,
        }
        if base_url := model.base_url:
            try:
                parsed = urlparse(base_url)
            except Exception:  # pragma: no cover
                pass
            else:
                if parsed.hostname:  # pragma: no branch
                    attributes['server.address'] = parsed.hostname
                if parsed.port:  # pragma: no branch
                    attributes['server.port'] = parsed.port

        return attributes

    @staticmethod
    def model_request_parameters_attributes(
        model_request_parameters: ModelRequestParameters,
    ) -> dict[str, AttributeValue]:
        return {'model_request_parameters': json.dumps(InstrumentedModel.serialize_any(model_request_parameters))}

    @staticmethod
    def event_to_dict(event: LogRecord) -> dict[str, Any]:
        if not event.body:
            body = {}  # pragma: no cover
        elif isinstance(event.body, Mapping):
            body = event.body
        else:
            body = {'body': event.body}
        return {**body, **(event.attributes or {})}

    @staticmethod
    def serialize_any(value: Any) -> str:
        try:
            return ANY_ADAPTER.dump_python(value, mode='json')
        except Exception:
            try:
                return str(value)
            except Exception as e:
                return f'Unable to serialize: {e}'

```

---|---
####  instrumentation_settings `instance-attribute`
```
instrumentation_settings: InstrumentationSettings[](https://ai.pydantic.dev/api/models/instrumented/#pydantic_ai.models.instrumented.InstrumentationSettings "InstrumentationSettings



      dataclass
   \(pydantic_ai.models.instrumented.InstrumentationSettings\)") = (
    options or InstrumentationSettings[](https://ai.pydantic.dev/api/models/instrumented/#pydantic_ai.models.instrumented.InstrumentationSettings "InstrumentationSettings



      dataclass
   \(pydantic_ai.models.instrumented.InstrumentationSettings\)")()
)

```

Instrumentation settings for this model.
###  CostCalculationFailedWarning
Bases:
Warning raised when cost calculation fails.
Source code in `pydantic_ai_slim/pydantic_ai/models/instrumented.py`
```
583
584
```
| ```
class CostCalculationFailedWarning(Warning):
    """Warning raised when cost calculation fails."""

```

---|---
© Pydantic Services Inc. 2024 to present
