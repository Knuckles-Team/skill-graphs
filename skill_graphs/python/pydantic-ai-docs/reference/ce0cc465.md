# `pydantic_ai.usage`
###  UsageBase `dataclass`
Source code in `pydantic_ai_slim/pydantic_ai/usage.py`
```
 18
 19
 20
 21
 22
 23
 24
 25
 26
 27
 28
 29
 30
 31
 32
 33
 34
 35
 36
 37
 38
 39
 40
 41
 42
 43
 44
 45
 46
 47
 48
 49
 50
 51
 52
 53
 54
 55
 56
 57
 58
 59
 60
 61
 62
 63
 64
 65
 66
 67
 68
 69
 70
 71
 72
 73
 74
 75
 76
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
```
| ```
@dataclass(repr=False, kw_only=True)
class UsageBase:
    input_tokens: Annotated[
        int,
        # `request_tokens` is deprecated, but we still want to support deserializing model responses stored in a DB before the name was changed
        Field(validation_alias=AliasChoices('input_tokens', 'request_tokens')),
    ] = 0
    """Number of input/prompt tokens."""

    cache_write_tokens: int = 0
    """Number of tokens written to the cache."""
    cache_read_tokens: int = 0
    """Number of tokens read from the cache."""

    output_tokens: Annotated[
        int,
        # `response_tokens` is deprecated, but we still want to support deserializing model responses stored in a DB before the name was changed
        Field(validation_alias=AliasChoices('output_tokens', 'response_tokens')),
    ] = 0
    """Number of output/completion tokens."""

    input_audio_tokens: int = 0
    """Number of audio input tokens."""
    cache_audio_read_tokens: int = 0
    """Number of audio tokens read from the cache."""
    output_audio_tokens: int = 0
    """Number of audio output tokens."""

    details: Annotated[
        dict[str, int],
        # `details` can not be `None` any longer, but we still want to support deserializing model responses stored in a DB before this was changed
        BeforeValidator(lambda d: d or {}),
    ] = dataclasses.field(default_factory=dict[str, int])
    """Any extra details returned by the model."""

    @property
    @deprecated('`request_tokens` is deprecated, use `input_tokens` instead')
    def request_tokens(self) -> int:
        return self.input_tokens

    @property
    @deprecated('`response_tokens` is deprecated, use `output_tokens` instead')
    def response_tokens(self) -> int:
        return self.output_tokens

    @property
    def total_tokens(self) -> int:
        """Sum of `input_tokens + output_tokens`."""
        return self.input_tokens + self.output_tokens

    def opentelemetry_attributes(self) -> dict[str, int]:
        """Get the token usage values as OpenTelemetry attributes."""
        result: dict[str, int] = {}
        if self.input_tokens:
            result['gen_ai.usage.input_tokens'] = self.input_tokens
        if self.output_tokens:
            result['gen_ai.usage.output_tokens'] = self.output_tokens

        details = self.details.copy()
        if self.cache_write_tokens:
            details['cache_write_tokens'] = self.cache_write_tokens
        if self.cache_read_tokens:
            details['cache_read_tokens'] = self.cache_read_tokens
        if self.input_audio_tokens:
            details['input_audio_tokens'] = self.input_audio_tokens
        if self.cache_audio_read_tokens:
            details['cache_audio_read_tokens'] = self.cache_audio_read_tokens
        if self.output_audio_tokens:
            details['output_audio_tokens'] = self.output_audio_tokens
        if details:
            prefix = 'gen_ai.usage.details.'
            for key, value in details.items():
                # Skipping check for value since spec implies all detail values are relevant
                if value:
                    result[prefix + key] = value
        return result

    def __repr__(self):
        kv_pairs = (f'{f.name}={value!r}' for f in fields(self) if (value := getattr(self, f.name)))
        return f'{self.__class__.__qualname__}({", ".join(kv_pairs)})'

    def has_values(self) -> bool:
        """Whether any values are set and non-zero."""
        return any(dataclasses.asdict(self).values())

```

---|---
####  input_tokens `class-attribute` `instance-attribute`
```
input_tokens: [
    ,
    Field[](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field "pydantic.Field")(
        validation_alias=AliasChoices[](https://docs.pydantic.dev/latest/api/aliases/#pydantic.aliases.AliasChoices "pydantic.AliasChoices")(
            input_tokens[](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.UsageBase.input_tokens "input_tokens



      class-attribute
      instance-attribute
   \(pydantic_ai.usage.UsageBase.input_tokens\)"), request_tokens
        )
    ),
] = 0

```

Number of input/prompt tokens.
####  cache_write_tokens `class-attribute` `instance-attribute`
```
cache_write_tokens:  = 0

```

Number of tokens written to the cache.
####  cache_read_tokens `class-attribute` `instance-attribute`
```
cache_read_tokens:  = 0

```

Number of tokens read from the cache.
####  output_tokens `class-attribute` `instance-attribute`
```
output_tokens: [
    ,
    Field[](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field "pydantic.Field")(
        validation_alias=AliasChoices[](https://docs.pydantic.dev/latest/api/aliases/#pydantic.aliases.AliasChoices "pydantic.AliasChoices")(
            output_tokens[](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.UsageBase.output_tokens "output_tokens



      class-attribute
      instance-attribute
   \(pydantic_ai.usage.UsageBase.output_tokens\)"), response_tokens
        )
    ),
] = 0

```

Number of output/completion tokens.
####  input_audio_tokens `class-attribute` `instance-attribute`
```
input_audio_tokens:  = 0

```

Number of audio input tokens.
####  cache_audio_read_tokens `class-attribute` `instance-attribute`
```
cache_audio_read_tokens:  = 0

```

Number of audio tokens read from the cache.
####  output_audio_tokens `class-attribute` `instance-attribute`
```
output_audio_tokens:  = 0

```

Number of audio output tokens.
####  details `class-attribute` `instance-attribute`
```
details: [
    [, ], BeforeValidator[](https://docs.pydantic.dev/latest/api/functional_validators/#pydantic.functional_validators.BeforeValidator "pydantic.BeforeValidator")(lambda d: d or {})
] = (default_factory=[, ])

```

Any extra details returned by the model.
####  total_tokens `property`
```
total_tokens:

```

Sum of `input_tokens + output_tokens`.
####  opentelemetry_attributes
```
opentelemetry_attributes() -> [, ]

```

Get the token usage values as OpenTelemetry attributes.
Source code in `pydantic_ai_slim/pydantic_ai/usage.py`
```
68
69
70
71
72
73
74
75
76
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
```
| ```
def opentelemetry_attributes(self) -> dict[str, int]:
    """Get the token usage values as OpenTelemetry attributes."""
    result: dict[str, int] = {}
    if self.input_tokens:
        result['gen_ai.usage.input_tokens'] = self.input_tokens
    if self.output_tokens:
        result['gen_ai.usage.output_tokens'] = self.output_tokens

    details = self.details.copy()
    if self.cache_write_tokens:
        details['cache_write_tokens'] = self.cache_write_tokens
    if self.cache_read_tokens:
        details['cache_read_tokens'] = self.cache_read_tokens
    if self.input_audio_tokens:
        details['input_audio_tokens'] = self.input_audio_tokens
    if self.cache_audio_read_tokens:
        details['cache_audio_read_tokens'] = self.cache_audio_read_tokens
    if self.output_audio_tokens:
        details['output_audio_tokens'] = self.output_audio_tokens
    if details:
        prefix = 'gen_ai.usage.details.'
        for key, value in details.items():
            # Skipping check for value since spec implies all detail values are relevant
            if value:
                result[prefix + key] = value
    return result

```

---|---
####  has_values
```
has_values() ->

```

Whether any values are set and non-zero.
Source code in `pydantic_ai_slim/pydantic_ai/usage.py`
```
 99
100
101
```
| ```
def has_values(self) -> bool:
    """Whether any values are set and non-zero."""
    return any(dataclasses.asdict(self).values())

```

---|---
###  RequestUsage `dataclass`
Bases: `UsageBase[](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.UsageBase "UsageBase



      dataclass
   \(pydantic_ai.usage.UsageBase\)")`
LLM usage associated with a single request.
This is an implementation of `genai_prices.types.AbstractUsage` so it can be used to calculate the price of the request using
Source code in `pydantic_ai_slim/pydantic_ai/usage.py`
```
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
```
| ```
@dataclass(repr=False, kw_only=True)
class RequestUsage(UsageBase):
    """LLM usage associated with a single request.

    This is an implementation of `genai_prices.types.AbstractUsage` so it can be used to calculate the price of the
    request using [genai-prices](https://github.com/pydantic/genai-prices).
    """

    @property
    def requests(self):
        return 1

    def incr(self, incr_usage: RequestUsage) -> None:
        """Increment the usage in place.

        Args:
            incr_usage: The usage to increment by.
        """
        return _incr_usage_tokens(self, incr_usage)

    def __add__(self, other: RequestUsage) -> RequestUsage:
        """Add two RequestUsages together.

        This is provided so it's trivial to sum usage information from multiple parts of a response.

        **WARNING:** this CANNOT be used to sum multiple requests without breaking some pricing calculations.
        """
        new_usage = copy(self)
        new_usage.incr(other)
        return new_usage

    @classmethod
    def extract(
        cls,
        data: Any,
        *,
        provider: str,
        provider_url: str,
        provider_fallback: str,
        api_flavor: str = 'default',
        details: dict[str, Any] | None = None,
    ) -> RequestUsage:
        """Extract usage information from the response data using genai-prices.

        Args:
            data: The response data from the model API.
            provider: The actual provider ID
            provider_url: The provider base_url
            provider_fallback: The fallback provider ID to use if the actual provider is not found in genai-prices.
                For example, an OpenAI model should set this to "openai" in case it has an obscure provider ID.
            api_flavor: The API flavor to use when extracting usage information,
                e.g. 'chat' or 'responses' for OpenAI.
            details: Becomes the `details` field on the returned `RequestUsage` for convenience.
        """
        details = details or {}
        for provider_id, provider_api_url in [(None, provider_url), (provider, None), (provider_fallback, None)]:
            try:
                provider_obj = get_snapshot().find_provider(None, provider_id, provider_api_url)
                _model_ref, extracted_usage = provider_obj.extract_usage(data, api_flavor=api_flavor)
                return cls(**{k: v for k, v in extracted_usage.__dict__.items() if v is not None}, details=details)
            except Exception:
                pass
        return cls(details=details)

```

---|---
####  incr
```
incr(incr_usage: RequestUsage[](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.RequestUsage "RequestUsage



      dataclass
   \(pydantic_ai.usage.RequestUsage\)")) -> None

```

Increment the usage in place.
Parameters:
Name | Type | Description | Default
---|---|---|---
`incr_usage` |  `RequestUsage[](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.RequestUsage "RequestUsage



      dataclass
   \(pydantic_ai.usage.RequestUsage\)")` |  The usage to increment by. |  _required_
Source code in `pydantic_ai_slim/pydantic_ai/usage.py`
```
116
117
118
119
120
121
122
```
| ```
def incr(self, incr_usage: RequestUsage) -> None:
    """Increment the usage in place.

    Args:
        incr_usage: The usage to increment by.
    """
    return _incr_usage_tokens(self, incr_usage)

```

---|---
####  __add__
```
__add__(other: RequestUsage[](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.RequestUsage "RequestUsage



      dataclass
   \(pydantic_ai.usage.RequestUsage\)")) -> RequestUsage[](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.RequestUsage "RequestUsage



      dataclass
   \(pydantic_ai.usage.RequestUsage\)")

```

Add two RequestUsages together.
This is provided so it's trivial to sum usage information from multiple parts of a response.
**WARNING:** this CANNOT be used to sum multiple requests without breaking some pricing calculations.
Source code in `pydantic_ai_slim/pydantic_ai/usage.py`
```
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
```
| ```
def __add__(self, other: RequestUsage) -> RequestUsage:
    """Add two RequestUsages together.

    This is provided so it's trivial to sum usage information from multiple parts of a response.

    **WARNING:** this CANNOT be used to sum multiple requests without breaking some pricing calculations.
    """
    new_usage = copy(self)
    new_usage.incr(other)
    return new_usage

```

---|---
####  extract `classmethod`
```
extract(
    data: ,
    *,
    provider: ,
    provider_url: ,
    provider_fallback: ,
    api_flavor:  = "default",
    details: [, ] | None = None
) -> RequestUsage[](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.RequestUsage "RequestUsage



      dataclass
   \(pydantic_ai.usage.RequestUsage\)")

```

Extract usage information from the response data using genai-prices.
Parameters:
Name | Type | Description | Default
---|---|---|---
`data` |  |  The response data from the model API. |  _required_
`provider` |  |  The actual provider ID |  _required_
`provider_url` |  |  The provider base_url |  _required_
`provider_fallback` |  |  The fallback provider ID to use if the actual provider is not found in genai-prices. For example, an OpenAI model should set this to "openai" in case it has an obscure provider ID. |  _required_
`api_flavor` |  |  The API flavor to use when extracting usage information, e.g. 'chat' or 'responses' for OpenAI. |  `'default'`
`details` |  |  Becomes the `details` field on the returned `RequestUsage` for convenience. |  `None`
Source code in `pydantic_ai_slim/pydantic_ai/usage.py`
```
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
```
| ```
@classmethod
def extract(
    cls,
    data: Any,
    *,
    provider: str,
    provider_url: str,
    provider_fallback: str,
    api_flavor: str = 'default',
    details: dict[str, Any] | None = None,
) -> RequestUsage:
    """Extract usage information from the response data using genai-prices.

    Args:
        data: The response data from the model API.
        provider: The actual provider ID
        provider_url: The provider base_url
        provider_fallback: The fallback provider ID to use if the actual provider is not found in genai-prices.
            For example, an OpenAI model should set this to "openai" in case it has an obscure provider ID.
        api_flavor: The API flavor to use when extracting usage information,
            e.g. 'chat' or 'responses' for OpenAI.
        details: Becomes the `details` field on the returned `RequestUsage` for convenience.
    """
    details = details or {}
    for provider_id, provider_api_url in [(None, provider_url), (provider, None), (provider_fallback, None)]:
        try:
            provider_obj = get_snapshot().find_provider(None, provider_id, provider_api_url)
            _model_ref, extracted_usage = provider_obj.extract_usage(data, api_flavor=api_flavor)
            return cls(**{k: v for k, v in extracted_usage.__dict__.items() if v is not None}, details=details)
        except Exception:
            pass
    return cls(details=details)

```

---|---
###  RunUsage `dataclass`
Bases: `UsageBase[](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.UsageBase "UsageBase



      dataclass
   \(pydantic_ai.usage.UsageBase\)")`
LLM usage associated with an agent run.
Responsibility for calculating request usage is on the model; Pydantic AI simply sums the usage information across requests.
Source code in `pydantic_ai_slim/pydantic_ai/usage.py`
```
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
```
| ```
@dataclass(repr=False, kw_only=True)
class RunUsage(UsageBase):
    """LLM usage associated with an agent run.

    Responsibility for calculating request usage is on the model; Pydantic AI simply sums the usage information across requests.
    """

    requests: int = 0
    """Number of requests made to the LLM API."""

    tool_calls: int = 0
    """Number of successful tool calls executed during the run."""

    input_tokens: int = 0
    """Total number of input/prompt tokens."""

    cache_write_tokens: int = 0
    """Total number of tokens written to the cache."""

    cache_read_tokens: int = 0
    """Total number of tokens read from the cache."""

    input_audio_tokens: int = 0
    """Total number of audio input tokens."""

    cache_audio_read_tokens: int = 0
    """Total number of audio tokens read from the cache."""

    output_tokens: int = 0
    """Total number of output/completion tokens."""

    details: dict[str, int] = dataclasses.field(default_factory=dict[str, int])
    """Any extra details returned by the model."""

    def incr(self, incr_usage: RunUsage | RequestUsage) -> None:
        """Increment the usage in place.

        Args:
            incr_usage: The usage to increment by.
        """
        if isinstance(incr_usage, RunUsage):
            self.requests += incr_usage.requests
            self.tool_calls += incr_usage.tool_calls
        return _incr_usage_tokens(self, incr_usage)

    def __add__(self, other: RunUsage | RequestUsage) -> RunUsage:
        """Add two RunUsages together.

        This is provided so it's trivial to sum usage information from multiple runs.
        """
        new_usage = copy(self)
        new_usage.incr(other)
        return new_usage

```

---|---
####  requests `class-attribute` `instance-attribute`
```
requests:  = 0

```

Number of requests made to the LLM API.
####  tool_calls `class-attribute` `instance-attribute`
```
tool_calls:  = 0

```

Number of successful tool calls executed during the run.
####  input_tokens `class-attribute` `instance-attribute`
```
input_tokens:  = 0

```

Total number of input/prompt tokens.
####  cache_write_tokens `class-attribute` `instance-attribute`
```
cache_write_tokens:  = 0

```

Total number of tokens written to the cache.
####  cache_read_tokens `class-attribute` `instance-attribute`
```
cache_read_tokens:  = 0

```

Total number of tokens read from the cache.
####  input_audio_tokens `class-attribute` `instance-attribute`
```
input_audio_tokens:  = 0

```

Total number of audio input tokens.
####  cache_audio_read_tokens `class-attribute` `instance-attribute`
```
cache_audio_read_tokens:  = 0

```

Total number of audio tokens read from the cache.
####  output_tokens `class-attribute` `instance-attribute`
```
output_tokens:  = 0

```

Total number of output/completion tokens.
####  details `class-attribute` `instance-attribute`
```
details: [, ] = (
    default_factory=[, ]
)

```

Any extra details returned by the model.
####  incr
```
incr(incr_usage: RunUsage[](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.RunUsage "RunUsage



      dataclass
   \(pydantic_ai.usage.RunUsage\)") | RequestUsage[](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.RequestUsage "RequestUsage



      dataclass
   \(pydantic_ai.usage.RequestUsage\)")) -> None

```

Increment the usage in place.
Parameters:
Name | Type | Description | Default
---|---|---|---
`incr_usage` |  `RunUsage[](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.RunUsage "RunUsage



      dataclass
   \(pydantic_ai.usage.RunUsage\)") | RequestUsage[](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.RequestUsage "RequestUsage



      dataclass
   \(pydantic_ai.usage.RequestUsage\)")` |  The usage to increment by. |  _required_
Source code in `pydantic_ai_slim/pydantic_ai/usage.py`
```
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
```
| ```
def incr(self, incr_usage: RunUsage | RequestUsage) -> None:
    """Increment the usage in place.

    Args:
        incr_usage: The usage to increment by.
    """
    if isinstance(incr_usage, RunUsage):
        self.requests += incr_usage.requests
        self.tool_calls += incr_usage.tool_calls
    return _incr_usage_tokens(self, incr_usage)

```

---|---
####  __add__
```
__add__(other: RunUsage[](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.RunUsage "RunUsage



      dataclass
   \(pydantic_ai.usage.RunUsage\)") | RequestUsage[](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.RequestUsage "RequestUsage



      dataclass
   \(pydantic_ai.usage.RequestUsage\)")) -> RunUsage[](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.RunUsage "RunUsage



      dataclass
   \(pydantic_ai.usage.RunUsage\)")

```

Add two RunUsages together.
This is provided so it's trivial to sum usage information from multiple runs.
Source code in `pydantic_ai_slim/pydantic_ai/usage.py`
```
214
215
216
217
218
219
220
221
```
| ```
def __add__(self, other: RunUsage | RequestUsage) -> RunUsage:
    """Add two RunUsages together.

    This is provided so it's trivial to sum usage information from multiple runs.
    """
    new_usage = copy(self)
    new_usage.incr(other)
    return new_usage

```

---|---
###  Usage `dataclass` `deprecated`
Bases: `RunUsage[](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.RunUsage "RunUsage



      dataclass
   \(pydantic_ai.usage.RunUsage\)")`
Deprecated
`Usage` is deprecated, use `RunUsage` instead
Deprecated alias for `RunUsage`.
Source code in `pydantic_ai_slim/pydantic_ai/usage.py`
```
244
245
246
247
```
| ```
@dataclass(repr=False, kw_only=True)
@deprecated('`Usage` is deprecated, use `RunUsage` instead')
class Usage(RunUsage):
    """Deprecated alias for `RunUsage`."""

```

---|---
###  UsageLimits `dataclass`
Limits on model usage.
The request count is tracked by pydantic_ai, and the request limit is checked before each request to the model. Token counts are provided in responses from the model, and the token limits are checked after each response.
Each of the limits can be set to `None` to disable that limit.
Source code in `pydantic_ai_slim/pydantic_ai/usage.py`
```
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
354
355
356
357
358
359
360
361
362
363
364
365
366
367
368
369
370
371
372
373
374
375
376
377
378
379
380
381
382
383
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
```
| ```
@dataclass(repr=False, kw_only=True)
class UsageLimits:
    """Limits on model usage.

    The request count is tracked by pydantic_ai, and the request limit is checked before each request to the model.
    Token counts are provided in responses from the model, and the token limits are checked after each response.

    Each of the limits can be set to `None` to disable that limit.
    """

    request_limit: int | None = 50
    """The maximum number of requests allowed to the model."""
    tool_calls_limit: int | None = None
    """The maximum number of successful tool calls allowed to be executed."""
    input_tokens_limit: int | None = None
    """The maximum number of input/prompt tokens allowed."""
    output_tokens_limit: int | None = None
    """The maximum number of output/response tokens allowed."""
    total_tokens_limit: int | None = None
    """The maximum number of tokens allowed in requests and responses combined."""
    count_tokens_before_request: bool = False
    """If True, perform a token counting pass before sending the request to the model,
    to enforce `request_tokens_limit` ahead of time.

    This may incur additional overhead (from calling the model's `count_tokens` API before making the actual request) and is disabled by default.

    Supported by:

    - Anthropic
    - Google
    - Bedrock Converse

    Support for OpenAI is in development: https://github.com/pydantic/pydantic-ai/issues/3430
    """

    @property
    @deprecated('`request_tokens_limit` is deprecated, use `input_tokens_limit` instead')
    def request_tokens_limit(self) -> int | None:
        return self.input_tokens_limit

    @property
    @deprecated('`response_tokens_limit` is deprecated, use `output_tokens_limit` instead')
    def response_tokens_limit(self) -> int | None:
        return self.output_tokens_limit

    @overload
    def __init__(
        self,
        *,
        request_limit: int | None = 50,
        tool_calls_limit: int | None = None,
        input_tokens_limit: int | None = None,
        output_tokens_limit: int | None = None,
        total_tokens_limit: int | None = None,
        count_tokens_before_request: bool = False,
    ) -> None:
        self.request_limit = request_limit
        self.tool_calls_limit = tool_calls_limit
        self.input_tokens_limit = input_tokens_limit
        self.output_tokens_limit = output_tokens_limit
        self.total_tokens_limit = total_tokens_limit
        self.count_tokens_before_request = count_tokens_before_request

    @overload
    @deprecated(
        'Use `input_tokens_limit` instead of `request_tokens_limit` and `output_tokens_limit` and `total_tokens_limit`'
    )
    def __init__(
        self,
        *,
        request_limit: int | None = 50,
        tool_calls_limit: int | None = None,
        request_tokens_limit: int | None = None,
        response_tokens_limit: int | None = None,
        total_tokens_limit: int | None = None,
        count_tokens_before_request: bool = False,
    ) -> None:
        self.request_limit = request_limit
        self.tool_calls_limit = tool_calls_limit
        self.input_tokens_limit = request_tokens_limit
        self.output_tokens_limit = response_tokens_limit
        self.total_tokens_limit = total_tokens_limit
        self.count_tokens_before_request = count_tokens_before_request

    def __init__(
        self,
        *,
        request_limit: int | None = 50,
        tool_calls_limit: int | None = None,
        input_tokens_limit: int | None = None,
        output_tokens_limit: int | None = None,
        total_tokens_limit: int | None = None,
        count_tokens_before_request: bool = False,
        # deprecated:
        request_tokens_limit: int | None = None,
        response_tokens_limit: int | None = None,
    ):
        self.request_limit = request_limit
        self.tool_calls_limit = tool_calls_limit
        self.input_tokens_limit = input_tokens_limit if input_tokens_limit is not None else request_tokens_limit
        self.output_tokens_limit = output_tokens_limit if output_tokens_limit is not None else response_tokens_limit
        self.total_tokens_limit = total_tokens_limit
        self.count_tokens_before_request = count_tokens_before_request

    def has_token_limits(self) -> bool:
        """Returns `True` if this instance places any limits on token counts.

        If this returns `False`, the `check_tokens` method will never raise an error.

        This is useful because if we have token limits, we need to check them after receiving each streamed message.
        If there are no limits, we can skip that processing in the streaming response iterator.
        """
        return any(
            limit is not None for limit in (self.input_tokens_limit, self.output_tokens_limit, self.total_tokens_limit)
        )

    def check_before_request(self, usage: RunUsage) -> None:
        """Raises a `UsageLimitExceeded` exception if the next request would exceed any of the limits."""
        request_limit = self.request_limit
        if request_limit is not None and usage.requests >= request_limit:
            raise UsageLimitExceeded(f'The next request would exceed the request_limit of {request_limit}')

        input_tokens = usage.input_tokens
        if self.input_tokens_limit is not None and input_tokens > self.input_tokens_limit:
            raise UsageLimitExceeded(
                f'The next request would exceed the input_tokens_limit of {self.input_tokens_limit} ({input_tokens=})'
            )

        total_tokens = usage.total_tokens
        if self.total_tokens_limit is not None and total_tokens > self.total_tokens_limit:
            raise UsageLimitExceeded(  # pragma: lax no cover
                f'The next request would exceed the total_tokens_limit of {self.total_tokens_limit} ({total_tokens=})'
            )

    def check_tokens(self, usage: RunUsage) -> None:
        """Raises a `UsageLimitExceeded` exception if the usage exceeds any of the token limits."""
        input_tokens = usage.input_tokens
        if self.input_tokens_limit is not None and input_tokens > self.input_tokens_limit:
            raise UsageLimitExceeded(f'Exceeded the input_tokens_limit of {self.input_tokens_limit} ({input_tokens=})')

        output_tokens = usage.output_tokens
        if self.output_tokens_limit is not None and output_tokens > self.output_tokens_limit:
            raise UsageLimitExceeded(
                f'Exceeded the output_tokens_limit of {self.output_tokens_limit} ({output_tokens=})'
            )

        total_tokens = usage.total_tokens
        if self.total_tokens_limit is not None and total_tokens > self.total_tokens_limit:
            raise UsageLimitExceeded(f'Exceeded the total_tokens_limit of {self.total_tokens_limit} ({total_tokens=})')

    def check_before_tool_call(self, projected_usage: RunUsage) -> None:
        """Raises a `UsageLimitExceeded` exception if the next tool call(s) would exceed the tool call limit."""
        tool_calls_limit = self.tool_calls_limit
        tool_calls = projected_usage.tool_calls
        if tool_calls_limit is not None and tool_calls > tool_calls_limit:
            raise UsageLimitExceeded(
                f'The next tool call(s) would exceed the tool_calls_limit of {tool_calls_limit} ({tool_calls=}).'
            )

    __repr__ = _utils.dataclasses_no_defaults_repr

```

---|---
####  request_limit `class-attribute` `instance-attribute`
```
request_limit:  | None = request_limit

```

The maximum number of requests allowed to the model.
####  tool_calls_limit `class-attribute` `instance-attribute`
```
tool_calls_limit:  | None = tool_calls_limit

```

The maximum number of successful tool calls allowed to be executed.
####  input_tokens_limit `class-attribute` `instance-attribute`
```
input_tokens_limit:  | None = (
    input_tokens_limit
    if input_tokens_limit is not None
    else request_tokens_limit
)

```

The maximum number of input/prompt tokens allowed.
####  output_tokens_limit `class-attribute` `instance-attribute`
```
output_tokens_limit:  | None = (
    output_tokens_limit
    if output_tokens_limit is not None
    else response_tokens_limit
)

```

The maximum number of output/response tokens allowed.
####  total_tokens_limit `class-attribute` `instance-attribute`
```
total_tokens_limit:  | None = total_tokens_limit

```

The maximum number of tokens allowed in requests and responses combined.
####  count_tokens_before_request `class-attribute` `instance-attribute`
```
count_tokens_before_request:  = (
    count_tokens_before_request
)

```

If True, perform a token counting pass before sending the request to the model, to enforce `request_tokens_limit` ahead of time.
This may incur additional overhead (from calling the model's `count_tokens` API before making the actual request) and is disabled by default.
Supported by:
  * Anthropic
  * Google
  * Bedrock Converse


Support for OpenAI is in development: https://github.com/pydantic/pydantic-ai/issues/3430
####  has_token_limits
```
has_token_limits() ->

```

Returns `True` if this instance places any limits on token counts.
If this returns `False`, the `check_tokens` method will never raise an error.
This is useful because if we have token limits, we need to check them after receiving each streamed message. If there are no limits, we can skip that processing in the streaming response iterator.
Source code in `pydantic_ai_slim/pydantic_ai/usage.py`
```
354
355
356
357
358
359
360
361
362
363
364
```
| ```
def has_token_limits(self) -> bool:
    """Returns `True` if this instance places any limits on token counts.

    If this returns `False`, the `check_tokens` method will never raise an error.

    This is useful because if we have token limits, we need to check them after receiving each streamed message.
    If there are no limits, we can skip that processing in the streaming response iterator.
    """
    return any(
        limit is not None for limit in (self.input_tokens_limit, self.output_tokens_limit, self.total_tokens_limit)
    )

```

---|---
####  check_before_request
```
check_before_request(usage: RunUsage[](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.RunUsage "RunUsage



      dataclass
   \(pydantic_ai.usage.RunUsage\)")) -> None

```

Raises a `UsageLimitExceeded` exception if the next request would exceed any of the limits.
Source code in `pydantic_ai_slim/pydantic_ai/usage.py`
```
366
367
368
369
370
371
372
373
374
375
376
377
378
379
380
381
382
```
| ```
def check_before_request(self, usage: RunUsage) -> None:
    """Raises a `UsageLimitExceeded` exception if the next request would exceed any of the limits."""
    request_limit = self.request_limit
    if request_limit is not None and usage.requests >= request_limit:
        raise UsageLimitExceeded(f'The next request would exceed the request_limit of {request_limit}')

    input_tokens = usage.input_tokens
    if self.input_tokens_limit is not None and input_tokens > self.input_tokens_limit:
        raise UsageLimitExceeded(
            f'The next request would exceed the input_tokens_limit of {self.input_tokens_limit} ({input_tokens=})'
        )

    total_tokens = usage.total_tokens
    if self.total_tokens_limit is not None and total_tokens > self.total_tokens_limit:
        raise UsageLimitExceeded(  # pragma: lax no cover
            f'The next request would exceed the total_tokens_limit of {self.total_tokens_limit} ({total_tokens=})'
        )

```

---|---
####  check_tokens
```
check_tokens(usage: RunUsage[](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.RunUsage "RunUsage



      dataclass
   \(pydantic_ai.usage.RunUsage\)")) -> None

```

Raises a `UsageLimitExceeded` exception if the usage exceeds any of the token limits.
Source code in `pydantic_ai_slim/pydantic_ai/usage.py`
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
```
| ```
def check_tokens(self, usage: RunUsage) -> None:
    """Raises a `UsageLimitExceeded` exception if the usage exceeds any of the token limits."""
    input_tokens = usage.input_tokens
    if self.input_tokens_limit is not None and input_tokens > self.input_tokens_limit:
        raise UsageLimitExceeded(f'Exceeded the input_tokens_limit of {self.input_tokens_limit} ({input_tokens=})')

    output_tokens = usage.output_tokens
    if self.output_tokens_limit is not None and output_tokens > self.output_tokens_limit:
        raise UsageLimitExceeded(
            f'Exceeded the output_tokens_limit of {self.output_tokens_limit} ({output_tokens=})'
        )

    total_tokens = usage.total_tokens
    if self.total_tokens_limit is not None and total_tokens > self.total_tokens_limit:
        raise UsageLimitExceeded(f'Exceeded the total_tokens_limit of {self.total_tokens_limit} ({total_tokens=})')

```

---|---
####  check_before_tool_call
```
check_before_tool_call(projected_usage: RunUsage[](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.RunUsage "RunUsage



      dataclass
   \(pydantic_ai.usage.RunUsage\)")) -> None

```

Raises a `UsageLimitExceeded` exception if the next tool call(s) would exceed the tool call limit.
Source code in `pydantic_ai_slim/pydantic_ai/usage.py`
```
400
401
402
403
404
405
406
407
```
| ```
def check_before_tool_call(self, projected_usage: RunUsage) -> None:
    """Raises a `UsageLimitExceeded` exception if the next tool call(s) would exceed the tool call limit."""
    tool_calls_limit = self.tool_calls_limit
    tool_calls = projected_usage.tool_calls
    if tool_calls_limit is not None and tool_calls > tool_calls_limit:
        raise UsageLimitExceeded(
            f'The next tool call(s) would exceed the tool_calls_limit of {tool_calls_limit} ({tool_calls=}).'
        )

```

---|---
© Pydantic Services Inc. 2024 to present
