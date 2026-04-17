
```

Deserialize an EvaluatorSpec from various formats.
This validator handles the various short forms of evaluator specifications, converting them to a consistent EvaluatorSpec instance.
Parameters:
Name | Type | Description | Default
---|---|---|---
`value` |  |  The value to deserialize. |  _required_
`handler` |  `ModelWrapValidatorHandler[](https://docs.pydantic.dev/latest/api/functional_validators/#pydantic.functional_validators.ModelWrapValidatorHandler "pydantic.ModelWrapValidatorHandler")[EvaluatorSpec[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.EvaluatorSpec "EvaluatorSpec \(pydantic_evals.evaluators.spec.EvaluatorSpec\)")]` |  The validator handler. |  _required_
Returns:
Type | Description
---|---
`EvaluatorSpec[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.EvaluatorSpec "EvaluatorSpec \(pydantic_evals.evaluators.spec.EvaluatorSpec\)")` |  The deserialized EvaluatorSpec.
Raises:
Type | Description
---|---
`ValidationError` |  If the value cannot be deserialized.
Source code in `pydantic_evals/pydantic_evals/evaluators/spec.py`
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
```
| ```
@model_validator(mode='wrap')
@classmethod
def deserialize(cls, value: Any, handler: ModelWrapValidatorHandler[EvaluatorSpec]) -> EvaluatorSpec:
    """Deserialize an EvaluatorSpec from various formats.

    This validator handles the various short forms of evaluator specifications,
    converting them to a consistent EvaluatorSpec instance.

    Args:
        value: The value to deserialize.
        handler: The validator handler.

    Returns:
        The deserialized EvaluatorSpec.

    Raises:
        ValidationError: If the value cannot be deserialized.
    """
    try:
        result = handler(value)
        return result
    except ValidationError as exc:
        try:
            deserialized = _SerializedEvaluatorSpec.model_validate(value)
        except ValidationError:
            raise exc  # raise the original error
        return deserialized.to_evaluator_spec()

```

---|---
####  serialize
```
serialize(
    handler: SerializerFunctionWrapHandler,
    info: SerializationInfo[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.SerializationInfo "pydantic_core.core_schema.SerializationInfo"),
) ->

```

Serialize using the appropriate short-form if possible.
Returns:
Type | Description
---|---
|  The serialized evaluator specification, using the shortest form possible:
|
  * Just the name if there are no arguments


|
  * {name: first_arg} if there's a single positional argument


|
  * {name: {kwargs}} if there are multiple (keyword) arguments


Source code in `pydantic_evals/pydantic_evals/evaluators/spec.py`
```
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
```
| ```
@model_serializer(mode='wrap')
def serialize(self, handler: SerializerFunctionWrapHandler, info: SerializationInfo) -> Any:
    """Serialize using the appropriate short-form if possible.

    Returns:
        The serialized evaluator specification, using the shortest form possible:
        - Just the name if there are no arguments
        - {name: first_arg} if there's a single positional argument
        - {name: {kwargs}} if there are multiple (keyword) arguments
    """
    if isinstance(info.context, dict) and info.context.get('use_short_form'):  # pyright: ignore[reportUnknownMemberType]
        if self.arguments is None:
            return self.name
        elif isinstance(self.arguments, tuple):
            return {self.name: self.arguments[0]}
        else:
            return {self.name: self.arguments}
    else:
        return handler(self)

```

---|---
###  ConfusionMatrixEvaluator `dataclass`
Bases: `ReportEvaluator[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.ReportEvaluator "ReportEvaluator



      dataclass
   \(pydantic_evals.evaluators.report_evaluator.ReportEvaluator\)")`
Computes a confusion matrix from case data.
Source code in `pydantic_evals/pydantic_evals/evaluators/report_common.py`
```
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
@dataclass(repr=False)
class ConfusionMatrixEvaluator(ReportEvaluator):
    """Computes a confusion matrix from case data."""

    predicted_from: Literal['expected_output', 'output', 'metadata', 'labels'] = 'output'
    predicted_key: str | None = None

    expected_from: Literal['expected_output', 'output', 'metadata', 'labels'] = 'expected_output'
    expected_key: str | None = None

    title: str = 'Confusion Matrix'

    def evaluate(self, ctx: ReportEvaluatorContext[Any, Any, Any]) -> ConfusionMatrix:
        predicted: list[str] = []
        expected: list[str] = []

        for case in ctx.report.cases:
            pred = self._extract(case, self.predicted_from, self.predicted_key)
            exp = self._extract(case, self.expected_from, self.expected_key)
            if pred is None or exp is None:
                continue
            predicted.append(pred)
            expected.append(exp)

        all_labels = sorted(set(predicted) | set(expected))
        label_to_idx = {label: i for i, label in enumerate(all_labels)}
        matrix = [[0] * len(all_labels) for _ in all_labels]

        for e, p in zip(expected, predicted):
            matrix[label_to_idx[e]][label_to_idx[p]] += 1

        return ConfusionMatrix(
            title=self.title,
            class_labels=all_labels,
            matrix=matrix,
        )

    @staticmethod
    def _extract(
        case: ReportCase[Any, Any, Any],
        from_: Literal['expected_output', 'output', 'metadata', 'labels'],
        key: str | None,
    ) -> str | None:
        if from_ == 'expected_output':
            return str(case.expected_output) if case.expected_output is not None else None
        elif from_ == 'output':
            return str(case.output) if case.output is not None else None
        elif from_ == 'metadata':
            if key is not None:
                if isinstance(case.metadata, dict):
                    metadata_dict = cast(dict[str, Any], case.metadata)  # pyright: ignore[reportUnknownMemberType]
                    val = metadata_dict.get(key)
                    return str(val) if val is not None else None
                return None  # key requested but metadata isn't a dict — skip this case
            return str(case.metadata) if case.metadata is not None else None
        elif from_ == 'labels':
            if key is None:
                raise ValueError("'key' is required when from_='labels'")
            label_result = case.labels.get(key)
            return label_result.value if label_result else None
        assert_never(from_)

```

---|---
###  KolmogorovSmirnovEvaluator `dataclass`
Bases: `ReportEvaluator[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.ReportEvaluator "ReportEvaluator



      dataclass
   \(pydantic_evals.evaluators.report_evaluator.ReportEvaluator\)")`
Computes a Kolmogorov-Smirnov plot and statistic from case data.
Plots the empirical CDFs of the score distribution for positive and negative cases, and computes the KS statistic (maximum vertical distance between the two CDFs).
Returns a `LinePlot` with the two CDF curves and a `ScalarResult` with the KS statistic.
Source code in `pydantic_evals/pydantic_evals/evaluators/report_common.py`
```
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
```
| ```
@dataclass(repr=False)
class KolmogorovSmirnovEvaluator(ReportEvaluator):
    """Computes a Kolmogorov-Smirnov plot and statistic from case data.

    Plots the empirical CDFs of the score distribution for positive and negative cases,
    and computes the KS statistic (maximum vertical distance between the two CDFs).

    Returns a `LinePlot` with the two CDF curves and a `ScalarResult` with the KS statistic.
    """

    score_key: str
    positive_from: Literal['expected_output', 'assertions', 'labels']
    positive_key: str | None = None

    score_from: Literal['scores', 'metrics'] = 'scores'

    title: str = 'KS Plot'
    n_thresholds: int = 100

    def evaluate(self, ctx: ReportEvaluatorContext[Any, Any, Any]) -> list[ReportAnalysis]:
        scored_cases = _extract_scored_cases(
            ctx.report.cases, self.score_key, self.score_from, self.positive_from, self.positive_key
        )

        empty_result: list[ReportAnalysis] = [
            LinePlot(
                title=self.title,
                x_label='Score',
                y_label='Cumulative Probability',
                y_range=(0, 1),
                curves=[],
            ),
            ScalarResult(title='KS Statistic', value=float('nan')),
        ]
        if not scored_cases:
            return empty_result

        pos_scores = sorted(s for s, p in scored_cases if p)
        neg_scores = sorted(s for s, p in scored_cases if not p)

        if not pos_scores or not neg_scores:
            return empty_result

        # Compute CDFs at all unique scores using binary search
        all_scores = sorted({s for s, _ in scored_cases})
        # Start both CDFs at y=0 at the minimum score
        pos_cdf: list[tuple[float, float]] = [(all_scores[0], 0.0)]
        neg_cdf: list[tuple[float, float]] = [(all_scores[0], 0.0)]
        ks_stat = 0.0

        for score in all_scores:
            pos_val = bisect_right(pos_scores, score) / len(pos_scores)
            neg_val = bisect_right(neg_scores, score) / len(neg_scores)
            pos_cdf.append((score, pos_val))
            neg_cdf.append((score, neg_val))
            ks_stat = max(ks_stat, abs(pos_val - neg_val))

        # Downsample for display
        display_pos = _downsample(pos_cdf, self.n_thresholds)
        display_neg = _downsample(neg_cdf, self.n_thresholds)

        pos_curve = LinePlotCurve(
            name='Positive',
            points=[LinePlotPoint(x=s, y=v) for s, v in display_pos],
            step='end',
        )
        neg_curve = LinePlotCurve(
            name='Negative',
            points=[LinePlotPoint(x=s, y=v) for s, v in display_neg],
            step='end',
        )

        return [
            LinePlot(
                title=self.title,
                x_label='Score',
                y_label='Cumulative Probability',
                y_range=(0, 1),
                curves=[pos_curve, neg_curve],
            ),
            ScalarResult(title='KS Statistic', value=ks_stat),
        ]

```

---|---
###  PrecisionRecallEvaluator `dataclass`
Bases: `ReportEvaluator[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.ReportEvaluator "ReportEvaluator



      dataclass
   \(pydantic_evals.evaluators.report_evaluator.ReportEvaluator\)")`
Computes a precision-recall curve from case data.
Returns both a `PrecisionRecall` chart and a `ScalarResult` with the AUC value. The AUC is computed at full resolution (every unique score threshold) for accuracy, while the chart points are downsampled to `n_thresholds` for display.
Source code in `pydantic_evals/pydantic_evals/evaluators/report_common.py`
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
222
223
224
225
226
227
228
229
230
```
| ```
@dataclass(repr=False)
class PrecisionRecallEvaluator(ReportEvaluator):
    """Computes a precision-recall curve from case data.

    Returns both a `PrecisionRecall` chart and a `ScalarResult` with the AUC value.
    The AUC is computed at full resolution (every unique score threshold) for accuracy,
    while the chart points are downsampled to `n_thresholds` for display.
    """

    score_key: str
    positive_from: Literal['expected_output', 'assertions', 'labels']
    positive_key: str | None = None

    score_from: Literal['scores', 'metrics'] = 'scores'

    title: str = 'Precision-Recall Curve'
    n_thresholds: int = 100

    def evaluate(self, ctx: ReportEvaluatorContext[Any, Any, Any]) -> list[ReportAnalysis]:
        scored_cases = _extract_scored_cases(
            ctx.report.cases, self.score_key, self.score_from, self.positive_from, self.positive_key
        )

        if not scored_cases:
            return [
                PrecisionRecall(title=self.title, curves=[]),
                ScalarResult(title=f'{self.title} AUC', value=float('nan')),
            ]

        total_positives = sum(1 for _, p in scored_cases if p)

        # Compute precision/recall at every unique score for exact AUC
        unique_thresholds = sorted({s for s, _ in scored_cases}, reverse=True)
        # Start with anchor at (recall=0, precision=1) — the "no predictions" point
        max_score = unique_thresholds[0]
        all_points: list[PrecisionRecallPoint] = [PrecisionRecallPoint(threshold=max_score, precision=1.0, recall=0.0)]
        for threshold in unique_thresholds:
            tp = sum(1 for s, p in scored_cases if s >= threshold and p)
            fp = sum(1 for s, p in scored_cases if s >= threshold and not p)
            fn = total_positives - tp
            precision = tp / (tp + fp) if (tp + fp) > 0 else 1.0
            recall = tp / (fn + tp) if (fn + tp) > 0 else 0.0
            all_points.append(PrecisionRecallPoint(threshold=threshold, precision=precision, recall=recall))

        # Exact AUC from the full-resolution points (anchor included)
        auc_points = [(p.recall, p.precision) for p in all_points]
        auc = _trapezoidal_auc(auc_points)

        # Downsample for display
        if len(all_points) <= self.n_thresholds or self.n_thresholds <= 1:
            display_points = all_points
        else:
            indices = sorted(
                {int(i * (len(all_points) - 1) / (self.n_thresholds - 1)) for i in range(self.n_thresholds)}
            )
            display_points = [all_points[i] for i in indices]

        curve = PrecisionRecallCurve(name=ctx.name, points=display_points, auc=auc)
        return [
            PrecisionRecall(title=self.title, curves=[curve]),
            ScalarResult(title=f'{self.title} AUC', value=auc),
        ]

```

---|---
###  ROCAUCEvaluator `dataclass`
Bases: `ReportEvaluator[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.ReportEvaluator "ReportEvaluator



      dataclass
   \(pydantic_evals.evaluators.report_evaluator.ReportEvaluator\)")`
Computes an ROC curve and AUC from case data.
Returns a `LinePlot` with the ROC curve (plus a dashed random-baseline diagonal) and a `ScalarResult` with the AUC value.
Source code in `pydantic_evals/pydantic_evals/evaluators/report_common.py`
```
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
```
| ```
@dataclass(repr=False)
class ROCAUCEvaluator(ReportEvaluator):
    """Computes an ROC curve and AUC from case data.

    Returns a `LinePlot` with the ROC curve (plus a dashed random-baseline diagonal)
    and a `ScalarResult` with the AUC value.
    """

    score_key: str
    positive_from: Literal['expected_output', 'assertions', 'labels']
    positive_key: str | None = None

    score_from: Literal['scores', 'metrics'] = 'scores'

    title: str = 'ROC Curve'
    n_thresholds: int = 100

    def evaluate(self, ctx: ReportEvaluatorContext[Any, Any, Any]) -> list[ReportAnalysis]:
        scored_cases = _extract_scored_cases(
            ctx.report.cases, self.score_key, self.score_from, self.positive_from, self.positive_key
        )

        empty_result: list[ReportAnalysis] = [
            LinePlot(
                title=self.title,
                x_label='False Positive Rate',
                y_label='True Positive Rate',
                x_range=(0, 1),
                y_range=(0, 1),
                curves=[],
            ),
            ScalarResult(title=f'{self.title} AUC', value=float('nan')),
        ]
        if not scored_cases:
            return empty_result

        total_positives = sum(1 for _, p in scored_cases if p)
        total_negatives = len(scored_cases) - total_positives

        if total_positives == 0 or total_negatives == 0:
            return empty_result

        # Compute TPR/FPR at every unique score for exact AUC
        unique_thresholds = sorted({s for s, _ in scored_cases}, reverse=True)
        all_fpr_tpr: list[tuple[float, float]] = [(0.0, 0.0)]
        for threshold in unique_thresholds:
            tp = sum(1 for s, p in scored_cases if s >= threshold and p)
            fp = sum(1 for s, p in scored_cases if s >= threshold and not p)
            tpr = tp / total_positives
            fpr = fp / total_negatives
            all_fpr_tpr.append((fpr, tpr))
        all_fpr_tpr.sort()

        # Exact AUC
        auc = _trapezoidal_auc(all_fpr_tpr)

        # Downsample for display
        downsampled = _downsample(all_fpr_tpr, self.n_thresholds)

        roc_curve = LinePlotCurve(
            name=f'{ctx.name} (AUC: {auc:.3f})',
            points=[LinePlotPoint(x=fpr, y=tpr) for fpr, tpr in downsampled],
        )
        baseline = LinePlotCurve(
            name='Random',
            points=[LinePlotPoint(x=0, y=0), LinePlotPoint(x=1, y=1)],
            style='dashed',
        )

        return [
            LinePlot(
                title=self.title,
                x_label='False Positive Rate',
                y_label='True Positive Rate',
                x_range=(0, 1),
                y_range=(0, 1),
                curves=[roc_curve, baseline],
            ),
            ScalarResult(title=f'{self.title} AUC', value=auc),
        ]

```

---|---
###  ReportEvaluator `dataclass`
Bases: `BaseEvaluator`, `InputsT, OutputT, MetadataT]`
Base class for experiment-wide evaluators that analyze full reports.
Unlike case-level Evaluators which assess individual task outputs, ReportEvaluators see all case results together and produce experiment-wide analyses like confusion matrices, precision-recall curves, or scalar statistics.
Source code in `pydantic_evals/pydantic_evals/evaluators/report_evaluator.py`
```
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
```
| ```
@dataclass(repr=False)
class ReportEvaluator(BaseEvaluator, Generic[InputsT, OutputT, MetadataT]):
    """Base class for experiment-wide evaluators that analyze full reports.

    Unlike case-level Evaluators which assess individual task outputs,
    ReportEvaluators see all case results together and produce
    experiment-wide analyses like confusion matrices, precision-recall curves,
    or scalar statistics.
    """

    @abstractmethod
    def evaluate(
        self, ctx: ReportEvaluatorContext[InputsT, OutputT, MetadataT]
    ) -> ReportAnalysis | list[ReportAnalysis] | Awaitable[ReportAnalysis | list[ReportAnalysis]]:
        """Evaluate the full report and return experiment-wide analysis/analyses."""
        ...

    async def evaluate_async(
        self, ctx: ReportEvaluatorContext[InputsT, OutputT, MetadataT]
    ) -> ReportAnalysis | list[ReportAnalysis]:
        """Evaluate, handling both sync and async implementations."""
        output = self.evaluate(ctx)
        if inspect.iscoroutine(output):
            return await output
        return cast('ReportAnalysis | list[ReportAnalysis]', output)

```

---|---
####  evaluate `abstractmethod`
```
evaluate(
    ctx: ReportEvaluatorContext[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.ReportEvaluatorContext "ReportEvaluatorContext



      dataclass
   \(pydantic_evals.evaluators.report_evaluator.ReportEvaluatorContext\)")[
        InputsT, OutputT, MetadataT
    ],
) -> (
    ReportAnalysis[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.ReportAnalysis "ReportAnalysis



      module-attribute
   \(pydantic_evals.reporting.analyses.ReportAnalysis\)")
    | [ReportAnalysis[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.ReportAnalysis "ReportAnalysis



      module-attribute
   \(pydantic_evals.reporting.analyses.ReportAnalysis\)")]
    | [ReportAnalysis[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.ReportAnalysis "ReportAnalysis



      module-attribute
   \(pydantic_evals.reporting.analyses.ReportAnalysis\)") | [ReportAnalysis[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.ReportAnalysis "ReportAnalysis



      module-attribute
   \(pydantic_evals.reporting.analyses.ReportAnalysis\)")]]
)

```

Evaluate the full report and return experiment-wide analysis/analyses.
Source code in `pydantic_evals/pydantic_evals/evaluators/report_evaluator.py`
```
49
50
51
52
53
54
```
| ```
@abstractmethod
def evaluate(
    self, ctx: ReportEvaluatorContext[InputsT, OutputT, MetadataT]
) -> ReportAnalysis | list[ReportAnalysis] | Awaitable[ReportAnalysis | list[ReportAnalysis]]:
    """Evaluate the full report and return experiment-wide analysis/analyses."""
    ...

```

---|---
####  evaluate_async `async`
```
evaluate_async(
    ctx: ReportEvaluatorContext[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.ReportEvaluatorContext "ReportEvaluatorContext



      dataclass
   \(pydantic_evals.evaluators.report_evaluator.ReportEvaluatorContext\)")[
        InputsT, OutputT, MetadataT
    ],
) -> ReportAnalysis[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.ReportAnalysis "ReportAnalysis



      module-attribute
   \(pydantic_evals.reporting.analyses.ReportAnalysis\)") | [ReportAnalysis[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.ReportAnalysis "ReportAnalysis



      module-attribute
   \(pydantic_evals.reporting.analyses.ReportAnalysis\)")]

```

Evaluate, handling both sync and async implementations.
Source code in `pydantic_evals/pydantic_evals/evaluators/report_evaluator.py`
```
56
57
58
59
60
61
62
63
```
| ```
async def evaluate_async(
    self, ctx: ReportEvaluatorContext[InputsT, OutputT, MetadataT]
) -> ReportAnalysis | list[ReportAnalysis]:
    """Evaluate, handling both sync and async implementations."""
    output = self.evaluate(ctx)
    if inspect.iscoroutine(output):
        return await output
    return cast('ReportAnalysis | list[ReportAnalysis]', output)

```

---|---
###  ReportEvaluatorContext `dataclass`
Bases: `InputsT, OutputT, MetadataT]`
Context for report-level evaluation, containing the full experiment results.
Source code in `pydantic_evals/pydantic_evals/evaluators/report_evaluator.py`
```
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
```
| ```
@dataclass(kw_only=True)
class ReportEvaluatorContext(Generic[InputsT, OutputT, MetadataT]):
    """Context for report-level evaluation, containing the full experiment results."""

    name: str
    """The experiment name."""
    report: EvaluationReport[InputsT, OutputT, MetadataT]
    """The full evaluation report."""
    experiment_metadata: dict[str, Any] | None
    """Experiment-level metadata."""

```

---|---
####  name `instance-attribute`
```
name:

```

The experiment name.
####  report `instance-attribute`
```
report: EvaluationReport[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.EvaluationReport "EvaluationReport



      dataclass
   \(pydantic_evals.reporting.EvaluationReport\)")[InputsT, OutputT, MetadataT]

```

The full evaluation report.
####  experiment_metadata `instance-attribute`
```
experiment_metadata: [, ] | None

```

Experiment-level metadata.
###  GradingOutput
Bases: `BaseModel[](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel "pydantic.BaseModel")`
The output of a grading operation.
Source code in `pydantic_evals/pydantic_evals/evaluators/llm_as_a_judge.py`
```
27
28
29
30
31
32
```
| ```
class GradingOutput(BaseModel, populate_by_name=True):
    """The output of a grading operation."""

    reason: str
    pass_: bool = Field(validation_alias='pass', serialization_alias='pass')
    score: float

```

---|---
###  judge_output `async`
```
judge_output(
    output: ,
    rubric: ,
    model: Model[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.Model "Model \(pydantic_ai.models.Model\)") | KnownModelName[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.KnownModelName "KnownModelName



      module-attribute
   \(pydantic_ai.models.KnownModelName\)") |  | None = None,
    model_settings: ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None = None,
) -> GradingOutput[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.llm_as_a_judge.GradingOutput "GradingOutput \(pydantic_evals.evaluators.llm_as_a_judge.GradingOutput\)")
