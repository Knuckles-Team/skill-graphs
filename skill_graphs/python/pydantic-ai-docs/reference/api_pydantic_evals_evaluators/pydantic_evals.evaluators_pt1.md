# `pydantic_evals.evaluators`
###  Contains `dataclass`
Bases: `Evaluator[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.Evaluator "Evaluator



      dataclass
   \(pydantic_evals.evaluators.evaluator.Evaluator\)")[`
Check if the output contains the expected output.
For strings, checks if expected_output is a substring of output. For lists/tuples, checks if expected_output is in output. For dicts, checks if all key-value pairs in expected_output are in output. For model-like types (BaseModel, dataclasses), converts to a dict and checks key-value pairs.
Note: case_sensitive only applies when both the value and output are strings.
Source code in `pydantic_evals/pydantic_evals/evaluators/common.py`
```
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
```
| ```
@dataclass(repr=False)
class Contains(Evaluator[object, object, object]):
    """Check if the output contains the expected output.

    For strings, checks if expected_output is a substring of output.
    For lists/tuples, checks if expected_output is in output.
    For dicts, checks if all key-value pairs in expected_output are in output.
    For model-like types (BaseModel, dataclasses), converts to a dict and checks key-value pairs.

    Note: case_sensitive only applies when both the value and output are strings.
    """

    value: Any
    case_sensitive: bool = True
    as_strings: bool = False
    evaluation_name: str | None = field(default=None)

    def evaluate(
        self,
        ctx: EvaluatorContext[object, object, object],
    ) -> EvaluationReason:
        # Convert objects to strings if requested
        failure_reason: str | None = None
        as_strings = self.as_strings or (isinstance(self.value, str) and isinstance(ctx.output, str))
        if as_strings:
            output_str = str(ctx.output)
            expected_str = str(self.value)

            if not self.case_sensitive:
                output_str = output_str.lower()
                expected_str = expected_str.lower()

            failure_reason: str | None = None
            if expected_str not in output_str:
                output_trunc = _truncated_repr(output_str, max_length=100)
                expected_trunc = _truncated_repr(expected_str, max_length=100)
                failure_reason = f'Output string {output_trunc} does not contain expected string {expected_trunc}'
            return EvaluationReason(value=failure_reason is None, reason=failure_reason)

        try:
            # Handle different collection types
            output_type = type(ctx.output)
            output_is_model_like = is_model_like(output_type)
            if isinstance(ctx.output, dict) or output_is_model_like:
                if output_is_model_like:
                    adapter: TypeAdapter[Any] = TypeAdapter(output_type)
                    output_dict = adapter.dump_python(ctx.output)  # pyright: ignore[reportUnknownMemberType]
                else:
                    # Cast to Any to avoid type checking issues
                    output_dict = cast(dict[Any, Any], ctx.output)  # pyright: ignore[reportUnknownMemberType]

                if isinstance(self.value, dict):
                    # Cast to Any to avoid type checking issues
                    expected_dict = cast(dict[Any, Any], self.value)  # pyright: ignore[reportUnknownMemberType]
                    for k in expected_dict:
                        if k not in output_dict:
                            k_trunc = _truncated_repr(k, max_length=30)
                            failure_reason = f'Output does not contain expected key {k_trunc}'
                            break
                        elif output_dict[k] != expected_dict[k]:
                            k_trunc = _truncated_repr(k, max_length=30)
                            output_v_trunc = _truncated_repr(output_dict[k], max_length=100)
                            expected_v_trunc = _truncated_repr(expected_dict[k], max_length=100)
                            failure_reason = (
                                f'Output has different value for key {k_trunc}: {output_v_trunc} != {expected_v_trunc}'
                            )
                            break
                else:
                    if self.value not in output_dict:
                        output_trunc = _truncated_repr(output_dict, max_length=200)
                        failure_reason = f'Output {output_trunc} does not contain provided value as a key'
            elif self.value not in ctx.output:  # pyright: ignore[reportOperatorIssue]  # will be handled by except block
                output_trunc = _truncated_repr(ctx.output, max_length=200)
                failure_reason = f'Output {output_trunc} does not contain provided value'
        except (TypeError, ValueError) as e:
            failure_reason = f'Containment check failed: {e}'

        return EvaluationReason(value=failure_reason is None, reason=failure_reason)

```

---|---
###  Equals `dataclass`
Bases: `Evaluator[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.Evaluator "Evaluator



      dataclass
   \(pydantic_evals.evaluators.evaluator.Evaluator\)")[`
Check if the output exactly equals the provided value.
Source code in `pydantic_evals/pydantic_evals/evaluators/common.py`
```
30
31
32
33
34
35
36
37
38
```
| ```
@dataclass(repr=False)
class Equals(Evaluator[object, object, object]):
    """Check if the output exactly equals the provided value."""

    value: Any
    evaluation_name: str | None = field(default=None)

    def evaluate(self, ctx: EvaluatorContext[object, object, object]) -> bool:
        return ctx.output == self.value

```

---|---
###  EqualsExpected `dataclass`
Bases: `Evaluator[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.Evaluator "Evaluator



      dataclass
   \(pydantic_evals.evaluators.evaluator.Evaluator\)")[`
Check if the output exactly equals the expected output.
Source code in `pydantic_evals/pydantic_evals/evaluators/common.py`
```
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
```
| ```
@dataclass(repr=False)
class EqualsExpected(Evaluator[object, object, object]):
    """Check if the output exactly equals the expected output."""

    evaluation_name: str | None = field(default=None)

    def evaluate(self, ctx: EvaluatorContext[object, object, object]) -> bool | dict[str, bool]:
        if ctx.expected_output is None:
            return {}  # Only compare if expected output is provided
        return ctx.output == ctx.expected_output

```

---|---
###  HasMatchingSpan `dataclass`
Bases: `Evaluator[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.Evaluator "Evaluator



      dataclass
   \(pydantic_evals.evaluators.evaluator.Evaluator\)")[`
Check if the span tree contains a span that matches the specified query.
Source code in `pydantic_evals/pydantic_evals/evaluators/common.py`
```
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
```
| ```
@dataclass(repr=False)
class HasMatchingSpan(Evaluator[object, object, object]):
    """Check if the span tree contains a span that matches the specified query."""

    query: SpanQuery
    evaluation_name: str | None = field(default=None)

    def evaluate(
        self,
        ctx: EvaluatorContext[object, object, object],
    ) -> bool:
        return ctx.span_tree.any(self.query)

```

---|---
###  IsInstance `dataclass`
Bases: `Evaluator[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.Evaluator "Evaluator



      dataclass
   \(pydantic_evals.evaluators.evaluator.Evaluator\)")[`
Check if the output is an instance of a type with the given name.
Source code in `pydantic_evals/pydantic_evals/evaluators/common.py`
```
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
```
| ```
@dataclass(repr=False)
class IsInstance(Evaluator[object, object, object]):
    """Check if the output is an instance of a type with the given name."""

    type_name: str
    evaluation_name: str | None = field(default=None)

    def evaluate(self, ctx: EvaluatorContext[object, object, object]) -> EvaluationReason:
        output = ctx.output
        for cls in type(output).__mro__:
            if cls.__name__ == self.type_name or cls.__qualname__ == self.type_name:
                return EvaluationReason(value=True)

        reason = f'output is of type {type(output).__name__}'
        if type(output).__qualname__ != type(output).__name__:
            reason += f' (qualname: {type(output).__qualname__})'
        return EvaluationReason(value=False, reason=reason)

```

---|---
###  LLMJudge `dataclass`
Bases: `Evaluator[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.Evaluator "Evaluator



      dataclass
   \(pydantic_evals.evaluators.evaluator.Evaluator\)")[`
Judge whether the output of a language model meets the criteria of a provided rubric.
If you do not specify a model, it uses the default model for judging. This starts as 'openai:gpt-5.2', but can be overridden by calling [`set_default_judge_model`](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.llm_as_a_judge.set_default_judge_model "set_default_judge_model").
Source code in `pydantic_evals/pydantic_evals/evaluators/common.py`
```
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
```
| ```
@dataclass(repr=False)
class LLMJudge(Evaluator[object, object, object]):
    """Judge whether the output of a language model meets the criteria of a provided rubric.

    If you do not specify a model, it uses the default model for judging. This starts as 'openai:gpt-5.2', but can be
    overridden by calling [`set_default_judge_model`][pydantic_evals.evaluators.llm_as_a_judge.set_default_judge_model].
    """

    rubric: str
    model: models.Model | models.KnownModelName | str | None = None
    include_input: bool = False
    include_expected_output: bool = False
    model_settings: ModelSettings | None = None
    score: OutputConfig | Literal[False] = False
    assertion: OutputConfig | Literal[False] = field(default_factory=lambda: OutputConfig(include_reason=True))

    async def evaluate(
        self,
        ctx: EvaluatorContext[object, object, object],
    ) -> EvaluatorOutput:
        if self.include_input:
            if self.include_expected_output:
                from .llm_as_a_judge import judge_input_output_expected

                grading_output = await judge_input_output_expected(
                    ctx.inputs, ctx.output, ctx.expected_output, self.rubric, self.model, self.model_settings
                )
            else:
                from .llm_as_a_judge import judge_input_output

                grading_output = await judge_input_output(
                    ctx.inputs, ctx.output, self.rubric, self.model, self.model_settings
                )
        else:
            if self.include_expected_output:
                from .llm_as_a_judge import judge_output_expected

                grading_output = await judge_output_expected(
                    ctx.output, ctx.expected_output, self.rubric, self.model, self.model_settings
                )
            else:
                from .llm_as_a_judge import judge_output

                grading_output = await judge_output(ctx.output, self.rubric, self.model, self.model_settings)

        output: dict[str, EvaluationScalar | EvaluationReason] = {}
        include_both = self.score is not False and self.assertion is not False
        evaluation_name = self.get_default_evaluation_name()

        if self.score is not False:
            default_name = f'{evaluation_name}_score' if include_both else evaluation_name
            _update_combined_output(output, grading_output.score, grading_output.reason, self.score, default_name)

        if self.assertion is not False:
            default_name = f'{evaluation_name}_pass' if include_both else evaluation_name
            _update_combined_output(output, grading_output.pass_, grading_output.reason, self.assertion, default_name)

        return output

    def build_serialization_arguments(self):
        result = super().build_serialization_arguments()
        # always serialize the model as a string when present; use its name if it's a KnownModelName
        if (model := result.get('model')) and isinstance(model, models.Model):  # pragma: no branch
            result['model'] = model.model_id

        # Note: this may lead to confusion if you try to serialize-then-deserialize with a custom model.
        # I expect that is rare enough to be worth not solving yet, but common enough that we probably will want to
        # solve it eventually. I'm imagining some kind of model registry, but don't want to work out the details yet.
        return result

```

---|---
###  MaxDuration `dataclass`
Bases: `Evaluator[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.Evaluator "Evaluator



      dataclass
   \(pydantic_evals.evaluators.evaluator.Evaluator\)")[`
Check if the execution time is under the specified maximum.
Source code in `pydantic_evals/pydantic_evals/evaluators/common.py`
```
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
```
| ```
@dataclass(repr=False)
class MaxDuration(Evaluator[object, object, object]):
    """Check if the execution time is under the specified maximum."""

    seconds: float | timedelta

    def evaluate(self, ctx: EvaluatorContext[object, object, object]) -> bool:
        duration = timedelta(seconds=ctx.duration)
        seconds = self.seconds
        if not isinstance(seconds, timedelta):
            seconds = timedelta(seconds=seconds)
        return duration <= seconds

```

---|---
###  OutputConfig
Bases:
Configuration for the score and assertion outputs of the LLMJudge evaluator.
Source code in `pydantic_evals/pydantic_evals/evaluators/common.py`
```
177
178
179
180
181
```
| ```
class OutputConfig(TypedDict, total=False):
    """Configuration for the score and assertion outputs of the LLMJudge evaluator."""

    evaluation_name: str
    include_reason: bool

```

---|---
###  EvaluatorContext `dataclass`
Bases: `InputsT, OutputT, MetadataT]`
Context for evaluating a task execution.
An instance of this class is the sole input to all Evaluators. It contains all the information needed to evaluate the task execution, including inputs, outputs, metadata, and telemetry data.
Evaluators use this context to access the task inputs, actual output, expected output, and other information when evaluating the result of the task execution.
Example:
```
from dataclasses import dataclass

from pydantic_evals.evaluators import Evaluator, EvaluatorContext


@dataclass
class ExactMatch(Evaluator):
    def evaluate(self, ctx: EvaluatorContext) -> bool:
        # Use the context to access task inputs, outputs, and expected outputs
        return ctx.output == ctx.expected_output

```

Source code in `pydantic_evals/pydantic_evals/evaluators/context.py`
```
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
102
```
| ```
@dataclass(kw_only=True)
class EvaluatorContext(Generic[InputsT, OutputT, MetadataT]):
    """Context for evaluating a task execution.

    An instance of this class is the sole input to all Evaluators. It contains all the information
    needed to evaluate the task execution, including inputs, outputs, metadata, and telemetry data.

    Evaluators use this context to access the task inputs, actual output, expected output, and other
    information when evaluating the result of the task execution.

    Example:
```python
    from dataclasses import dataclass

    from pydantic_evals.evaluators import Evaluator, EvaluatorContext


    @dataclass
    class ExactMatch(Evaluator):
        def evaluate(self, ctx: EvaluatorContext) -> bool:
            # Use the context to access task inputs, outputs, and expected outputs
            return ctx.output == ctx.expected_output
```
    """

    name: str | None
    """The name of the case."""
    inputs: InputsT
    """The inputs provided to the task for this case."""
    metadata: MetadataT | None
    """Metadata associated with the case, if provided. May be None if no metadata was specified."""
    expected_output: OutputT | None
    """The expected output for the case, if provided. May be None if no expected output was specified."""

    output: OutputT
    """The actual output produced by the task for this case."""
    duration: float
    """The duration of the task run for this case."""
    _span_tree: SpanTree | SpanTreeRecordingError = field(repr=False)
    """The span tree for the task run for this case.

    This will be `None` if `logfire.configure` has not been called.
    """

    attributes: dict[str, Any]
    """Attributes associated with the task run for this case.

    These can be set by calling `pydantic_evals.dataset.set_eval_attribute` in any code executed
    during the evaluation task."""
    metrics: dict[str, int | float]
    """Metrics associated with the task run for this case.

    These can be set by calling `pydantic_evals.dataset.increment_eval_metric` in any code executed
    during the evaluation task."""

    @property
    def span_tree(self) -> SpanTree:
        """Get the `SpanTree` for this task execution.

        The span tree is a graph where each node corresponds to an OpenTelemetry span recorded during the task
        execution, including timing information and any custom spans created during execution.

        Returns:
            The span tree for the task execution.

        Raises:
            SpanTreeRecordingError: If spans were not captured during execution of the task, e.g. due to not having
                the necessary dependencies installed.
        """
        if isinstance(self._span_tree, SpanTreeRecordingError):
            # In this case, there was a reason we couldn't record the SpanTree. We raise that now
            raise self._span_tree
        return self._span_tree

```

---|---
####  name `instance-attribute`
```
name:  | None

```

The name of the case.
####  inputs `instance-attribute`
```
inputs: InputsT

```

The inputs provided to the task for this case.
####  metadata `instance-attribute`
```
metadata: MetadataT | None

```

Metadata associated with the case, if provided. May be None if no metadata was specified.
####  expected_output `instance-attribute`
```
expected_output: OutputT | None

```

The expected output for the case, if provided. May be None if no expected output was specified.
####  output `instance-attribute`
```
output: OutputT

```

The actual output produced by the task for this case.
####  duration `instance-attribute`
```
duration:

```

The duration of the task run for this case.
####  attributes `instance-attribute`
```
attributes: [, ]

```

Attributes associated with the task run for this case.
These can be set by calling `pydantic_evals.dataset.set_eval_attribute` in any code executed during the evaluation task.
####  metrics `instance-attribute`
```
metrics: [,  | ]

```

Metrics associated with the task run for this case.
These can be set by calling `pydantic_evals.dataset.increment_eval_metric` in any code executed during the evaluation task.
####  span_tree `property`
```
span_tree: SpanTree[](https://ai.pydantic.dev/api/pydantic_evals/otel/#pydantic_evals.otel.SpanTree "SpanTree



      dataclass
   \(pydantic_evals.otel.span_tree.SpanTree\)")

```

Get the `SpanTree` for this task execution.
The span tree is a graph where each node corresponds to an OpenTelemetry span recorded during the task execution, including timing information and any custom spans created during execution.
Returns:
Type | Description
---|---
`SpanTree[](https://ai.pydantic.dev/api/pydantic_evals/otel/#pydantic_evals.otel.SpanTree "SpanTree



      dataclass
   \(pydantic_evals.otel.span_tree.SpanTree\)")` |  The span tree for the task execution.
Raises:
Type | Description
---|---
`SpanTreeRecordingError` |  If spans were not captured during execution of the task, e.g. due to not having the necessary dependencies installed.
###  EvaluationReason `dataclass`
The result of running an evaluator with an optional explanation.
Contains a scalar value and an optional "reason" explaining the value.
Parameters:
Name | Type | Description | Default
---|---|---|---
`value` |  `EvaluationScalar` |  The scalar result of the evaluation (boolean, integer, float, or string). |  _required_
`reason` |  |  An optional explanation of the evaluation result. |  `None`
Source code in `pydantic_evals/pydantic_evals/evaluators/evaluator.py`
```
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
```
| ```
@dataclass
class EvaluationReason:
    """The result of running an evaluator with an optional explanation.

    Contains a scalar value and an optional "reason" explaining the value.

    Args:
        value: The scalar result of the evaluation (boolean, integer, float, or string).
        reason: An optional explanation of the evaluation result.
    """

    value: EvaluationScalar
    reason: str | None = None

```

---|---
###  EvaluationResult `dataclass`
Bases: `EvaluationScalarT]`
The details of an individual evaluation result.
Contains the name, value, reason, and source evaluator for a single evaluation.
Parameters:
Name | Type | Description | Default
---|---|---|---
`name` |  |  The name of the evaluation. |  _required_
`value` |  `EvaluationScalarT` |  The scalar result of the evaluation. |  _required_
`reason` |  |  An optional explanation of the evaluation result. |  _required_
`source` |  `EvaluatorSpec[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.EvaluatorSpec "EvaluatorSpec \(pydantic_evals.evaluators.spec.EvaluatorSpec\)")` |  The spec of the evaluator that produced this result. |  _required_
Source code in `pydantic_evals/pydantic_evals/evaluators/evaluator.py`
```
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
```
| ```
@dataclass
class EvaluationResult(Generic[EvaluationScalarT]):
    """The details of an individual evaluation result.

    Contains the name, value, reason, and source evaluator for a single evaluation.

    Args:
        name: The name of the evaluation.
        value: The scalar result of the evaluation.
        reason: An optional explanation of the evaluation result.
        source: The spec of the evaluator that produced this result.
    """

    name: str
    value: EvaluationScalarT
    reason: str | None
    source: EvaluatorSpec

    def downcast(self, *value_types: type[T]) -> EvaluationResult[T] | None:
        """Attempt to downcast this result to a more specific type.

        Args:
            *value_types: The types to check the value against.

        Returns:
            A downcast version of this result if the value is an instance of one of the given types,
            otherwise None.
        """
        # Check if value matches any of the target types, handling bool as a special case
        for value_type in value_types:
            if isinstance(self.value, value_type):
                # Only match bool with explicit bool type
                if isinstance(self.value, bool) and value_type is not bool:
                    continue
                return cast(EvaluationResult[T], self)
        return None

```

---|---
####  downcast
```
downcast(
    *value_types: [T],
) -> EvaluationResult[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.EvaluationResult "EvaluationResult



      dataclass
   \(pydantic_evals.evaluators.evaluator.EvaluationResult\)")[T] | None

```

Attempt to downcast this result to a more specific type.
Parameters:
Name | Type | Description | Default
---|---|---|---
`*value_types` |  `T]` |  The types to check the value against. |  `()`
Returns:
Type | Description
---|---
`EvaluationResult[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.EvaluationResult "EvaluationResult



      dataclass
   \(pydantic_evals.evaluators.evaluator.EvaluationResult\)")[T] | None` |  A downcast version of this result if the value is an instance of one of the given types,
`EvaluationResult[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.EvaluationResult "EvaluationResult



      dataclass
   \(pydantic_evals.evaluators.evaluator.EvaluationResult\)")[T] | None` |  otherwise None.
Source code in `pydantic_evals/pydantic_evals/evaluators/evaluator.py`
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
```
| ```
def downcast(self, *value_types: type[T]) -> EvaluationResult[T] | None:
    """Attempt to downcast this result to a more specific type.

    Args:
        *value_types: The types to check the value against.
