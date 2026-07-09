# `pydantic_evals.reporting`
###  ConfusionMatrix
Bases: `BaseModel[](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel "pydantic.BaseModel")`
A confusion matrix comparing expected vs predicted labels across cases.
Source code in `pydantic_evals/pydantic_evals/reporting/analyses.py`
```
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
```
| ```
class ConfusionMatrix(BaseModel):
    """A confusion matrix comparing expected vs predicted labels across cases."""

    type: Literal['confusion_matrix'] = 'confusion_matrix'
    title: str = 'Confusion Matrix'
    description: str | None = None
    class_labels: list[str]
    """Ordered list of class labels (used for both axes)."""
    matrix: list[list[int]]
    """matrix[expected_idx][predicted_idx] = count of cases."""

```

---|---
####  class_labels `instance-attribute`
```
class_labels: []

```

Ordered list of class labels (used for both axes).
####  matrix `instance-attribute`
```
matrix: [[]]

```

matrix[expected_idx][predicted_idx] = count of cases.
###  LinePlot
Bases: `BaseModel[](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel "pydantic.BaseModel")`
A generic XY line plot with labeled axes, supporting multiple curves.
Use this for ROC curves, KS plots, calibration curves, or any custom line chart that doesn't fit the specific PrecisionRecall type.
Source code in `pydantic_evals/pydantic_evals/reporting/analyses.py`
```
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
```
| ```
class LinePlot(BaseModel):
    """A generic XY line plot with labeled axes, supporting multiple curves.

    Use this for ROC curves, KS plots, calibration curves, or any custom
    line chart that doesn't fit the specific PrecisionRecall type.
    """

    type: Literal['line_plot'] = 'line_plot'
    title: str
    description: str | None = None
    x_label: str
    """Label for the x-axis."""
    y_label: str
    """Label for the y-axis."""
    x_range: tuple[float, float] | None = None
    """Optional fixed range for x-axis (min, max)."""
    y_range: tuple[float, float] | None = None
    """Optional fixed range for y-axis (min, max)."""
    curves: list[LinePlotCurve]
    """One or more curves to plot."""

```

---|---
####  x_label `instance-attribute`
```
x_label:

```

Label for the x-axis.
####  y_label `instance-attribute`
```
y_label:

```

Label for the y-axis.
####  x_range `class-attribute` `instance-attribute`
```
x_range: [, ] | None = None

```

Optional fixed range for x-axis (min, max).
####  y_range `class-attribute` `instance-attribute`
```
y_range: [, ] | None = None

```

Optional fixed range for y-axis (min, max).
####  curves `instance-attribute`
```
curves: [LinePlotCurve]

```

One or more curves to plot.
###  PrecisionRecall
Bases: `BaseModel[](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel "pydantic.BaseModel")`
Precision-recall curve data across cases.
Source code in `pydantic_evals/pydantic_evals/reporting/analyses.py`
```
52
53
54
55
56
57
58
59
```
| ```
class PrecisionRecall(BaseModel):
    """Precision-recall curve data across cases."""

    type: Literal['precision_recall'] = 'precision_recall'
    title: str = 'Precision-Recall Curve'
    description: str | None = None
    curves: list[PrecisionRecallCurve]
    """One or more curves."""

```

---|---
####  curves `instance-attribute`
```
curves: [PrecisionRecallCurve[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.PrecisionRecallCurve "PrecisionRecallCurve \(pydantic_evals.reporting.analyses.PrecisionRecallCurve\)")]

```

One or more curves.
###  PrecisionRecallCurve
Bases: `BaseModel[](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel "pydantic.BaseModel")`
A single precision-recall curve.
Source code in `pydantic_evals/pydantic_evals/reporting/analyses.py`
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
```
| ```
class PrecisionRecallCurve(BaseModel):
    """A single precision-recall curve."""

    name: str
    """Name of this curve (e.g., experiment name or evaluator name)."""
    points: list[PrecisionRecallPoint]
    """Points on the curve, ordered by threshold."""
    auc: float | None = None
    """Area under the precision-recall curve."""

```

---|---
####  name `instance-attribute`
```
name:

```

Name of this curve (e.g., experiment name or evaluator name).
####  points `instance-attribute`
```
points: [PrecisionRecallPoint[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.PrecisionRecallPoint "PrecisionRecallPoint \(pydantic_evals.reporting.analyses.PrecisionRecallPoint\)")]

```

Points on the curve, ordered by threshold.
####  auc `class-attribute` `instance-attribute`
```
auc:  | None = None

```

Area under the precision-recall curve.
###  PrecisionRecallPoint
Bases: `BaseModel[](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel "pydantic.BaseModel")`
A single point on a precision-recall curve.
Source code in `pydantic_evals/pydantic_evals/reporting/analyses.py`
```
33
34
35
36
37
38
```
| ```
class PrecisionRecallPoint(BaseModel):
    """A single point on a precision-recall curve."""

    threshold: float
    precision: float
    recall: float

```

---|---
###  ReportAnalysis `module-attribute`
```
ReportAnalysis = [
    ConfusionMatrix[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.ConfusionMatrix "ConfusionMatrix \(pydantic_evals.reporting.analyses.ConfusionMatrix\)")
    | PrecisionRecall[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.PrecisionRecall "PrecisionRecall \(pydantic_evals.reporting.analyses.PrecisionRecall\)")
    | ScalarResult[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.ScalarResult "ScalarResult \(pydantic_evals.reporting.analyses.ScalarResult\)")
    | TableResult[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.TableResult "TableResult \(pydantic_evals.reporting.analyses.TableResult\)")
    | LinePlot[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.LinePlot "LinePlot \(pydantic_evals.reporting.analyses.LinePlot\)"),
    Discriminator[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Discriminator "pydantic.Discriminator")("type"),
]

```

Discriminated union of all report-level analysis types.
###  ScalarResult
Bases: `BaseModel[](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel "pydantic.BaseModel")`
A single scalar statistic (e.g., F1 score, accuracy, BLEU).
Source code in `pydantic_evals/pydantic_evals/reporting/analyses.py`
```
62
63
64
65
66
67
68
69
70
```
| ```
class ScalarResult(BaseModel):
    """A single scalar statistic (e.g., F1 score, accuracy, BLEU)."""

    type: Literal['scalar'] = 'scalar'
    title: str
    description: str | None = None
    value: float | int
    unit: str | None = None
    """Optional unit label (e.g., '%', 'ms')."""

```

---|---
####  unit `class-attribute` `instance-attribute`
```
unit:  | None = None

```

Optional unit label (e.g., '%', 'ms').
###  TableResult
Bases: `BaseModel[](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel "pydantic.BaseModel")`
A generic table of data (fallback for custom analyses).
Source code in `pydantic_evals/pydantic_evals/reporting/analyses.py`
```
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
```
| ```
class TableResult(BaseModel):
    """A generic table of data (fallback for custom analyses)."""

    type: Literal['table'] = 'table'
    title: str
    description: str | None = None
    columns: list[str]
    """Column headers."""
    rows: list[list[str | int | float | bool | None]]
    """Row data, one list per row."""

```

---|---
####  columns `instance-attribute`
```
columns: []

```

Column headers.
####  rows `instance-attribute`
```
rows: [[ |  |  |  | None]]

```

Row data, one list per row.
###  ReportCase `dataclass`
Bases: `InputsT, OutputT, MetadataT]`
A single case in an evaluation report.
Source code in `pydantic_evals/pydantic_evals/reporting/__init__.py`
```
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
```
| ```
@dataclass(kw_only=True)
class ReportCase(Generic[InputsT, OutputT, MetadataT]):
    """A single case in an evaluation report."""

    name: str
    """The name of the [case][pydantic_evals.Case]."""
    inputs: InputsT
    """The inputs to the task, from [`Case.inputs`][pydantic_evals.dataset.Case.inputs]."""
    metadata: MetadataT | None
    """Any metadata associated with the case, from [`Case.metadata`][pydantic_evals.dataset.Case.metadata]."""
    expected_output: OutputT | None
    """The expected output of the task, from [`Case.expected_output`][pydantic_evals.dataset.Case.expected_output]."""
    output: OutputT
    """The output of the task execution."""

    metrics: dict[str, float | int]
    attributes: dict[str, Any]

    scores: dict[str, EvaluationResult[int | float]]
    labels: dict[str, EvaluationResult[str]]
    assertions: dict[str, EvaluationResult[bool]]

    task_duration: float
    total_duration: float  # includes evaluator execution time

    source_case_name: str | None = None
    """The original case name before run-indexing. Serves as the aggregation key
    for multi-run experiments. None when repeat == 1."""

    trace_id: str | None = None
    """The trace ID of the case span."""
    span_id: str | None = None
    """The span ID of the case span."""

    evaluator_failures: list[EvaluatorFailure] = field(default_factory=list[EvaluatorFailure])

```

---|---
####  name `instance-attribute`
```
name:

```

The name of the [case](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.Case "Case



      dataclass
  ").
####  inputs `instance-attribute`
```
inputs: InputsT

```

The inputs to the task, from [`Case.inputs`](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.Case.inputs "inputs



      instance-attribute
  ").
####  metadata `instance-attribute`
```
metadata: MetadataT | None

```

Any metadata associated with the case, from [`Case.metadata`](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.Case.metadata "metadata



      class-attribute
      instance-attribute
  ").
####  expected_output `instance-attribute`
```
expected_output: OutputT | None

```

The expected output of the task, from [`Case.expected_output`](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.Case.expected_output "expected_output



      class-attribute
      instance-attribute
  ").
####  output `instance-attribute`
```
output: OutputT

```

The output of the task execution.
####  source_case_name `class-attribute` `instance-attribute`
```
source_case_name:  | None = None

```

The original case name before run-indexing. Serves as the aggregation key for multi-run experiments. None when repeat == 1.
####  trace_id `class-attribute` `instance-attribute`
```
trace_id:  | None = None

```

The trace ID of the case span.
####  span_id `class-attribute` `instance-attribute`
```
span_id:  | None = None

```

The span ID of the case span.
###  ReportCaseFailure `dataclass`
Bases: `InputsT, OutputT, MetadataT]`
A single case in an evaluation report that failed due to an error during task execution.
Source code in `pydantic_evals/pydantic_evals/reporting/__init__.py`
```
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
```
| ```
@dataclass(kw_only=True)
class ReportCaseFailure(Generic[InputsT, OutputT, MetadataT]):
    """A single case in an evaluation report that failed due to an error during task execution."""

    name: str
    """The name of the [case][pydantic_evals.Case]."""
    inputs: InputsT
    """The inputs to the task, from [`Case.inputs`][pydantic_evals.dataset.Case.inputs]."""
    metadata: MetadataT | None
    """Any metadata associated with the case, from [`Case.metadata`][pydantic_evals.dataset.Case.metadata]."""
    expected_output: OutputT | None
    """The expected output of the task, from [`Case.expected_output`][pydantic_evals.dataset.Case.expected_output]."""

    error_message: str
    """The message of the exception that caused the failure."""
    error_stacktrace: str
    """The stacktrace of the exception that caused the failure."""

    source_case_name: str | None = None
    """The original case name before run-indexing. Serves as the aggregation key
    for multi-run experiments. None when repeat == 1."""

    trace_id: str | None = None
    """The trace ID of the case span."""
    span_id: str | None = None
    """The span ID of the case span."""

```

---|---
####  name `instance-attribute`
```
name:

```

The name of the [case](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.Case "Case



      dataclass
  ").
####  inputs `instance-attribute`
```
inputs: InputsT

```

The inputs to the task, from [`Case.inputs`](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.Case.inputs "inputs



      instance-attribute
  ").
####  metadata `instance-attribute`
```
metadata: MetadataT | None

```

Any metadata associated with the case, from [`Case.metadata`](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.Case.metadata "metadata



      class-attribute
      instance-attribute
  ").
####  expected_output `instance-attribute`
```
expected_output: OutputT | None

```

The expected output of the task, from [`Case.expected_output`](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.Case.expected_output "expected_output



      class-attribute
      instance-attribute
  ").
####  error_message `instance-attribute`
```
error_message:

```

The message of the exception that caused the failure.
####  error_stacktrace `instance-attribute`
```
error_stacktrace:

```

The stacktrace of the exception that caused the failure.
####  source_case_name `class-attribute` `instance-attribute`
```
source_case_name:  | None = None

```

The original case name before run-indexing. Serves as the aggregation key for multi-run experiments. None when repeat == 1.
####  trace_id `class-attribute` `instance-attribute`
```
trace_id:  | None = None

```

The trace ID of the case span.
####  span_id `class-attribute` `instance-attribute`
```
span_id:  | None = None

```

The span ID of the case span.
###  ReportCaseGroup `dataclass`
Bases: `InputsT, OutputT, MetadataT]`
Grouped results from running the same case multiple times.
This is a computed view, not stored data. Obtain via `EvaluationReport.case_groups()`.
Source code in `pydantic_evals/pydantic_evals/reporting/__init__.py`
```
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
```
| ```
@dataclass(kw_only=True)
class ReportCaseGroup(Generic[InputsT, OutputT, MetadataT]):
    """Grouped results from running the same case multiple times.

    This is a computed view, not stored data. Obtain via
    `EvaluationReport.case_groups()`.
    """

    name: str
    """The original case name (shared across all runs)."""
    inputs: InputsT
    """The inputs (same for all runs)."""
    metadata: MetadataT | None
    """The metadata (same for all runs)."""
    expected_output: OutputT | None
    """The expected output (same for all runs)."""

    runs: Sequence[ReportCase[InputsT, OutputT, MetadataT]]
    """Individual run results."""
    failures: Sequence[ReportCaseFailure[InputsT, OutputT, MetadataT]]
    """Runs that failed with exceptions."""

    summary: ReportCaseAggregate
    """Aggregated statistics across runs."""

```

---|---
####  name `instance-attribute`
```
name:

```

The original case name (shared across all runs).
####  inputs `instance-attribute`
```
inputs: InputsT

```

The inputs (same for all runs).
####  metadata `instance-attribute`
```
metadata: MetadataT | None

```

The metadata (same for all runs).
####  expected_output `instance-attribute`
```
expected_output: OutputT | None

```

The expected output (same for all runs).
####  runs `instance-attribute`
```
runs: [ReportCase[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.ReportCase "ReportCase



      dataclass
   \(pydantic_evals.reporting.ReportCase\)")[InputsT, OutputT, MetadataT]]

```

Individual run results.
####  failures `instance-attribute`
```
failures: [
    ReportCaseFailure[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.ReportCaseFailure "ReportCaseFailure



      dataclass
   \(pydantic_evals.reporting.ReportCaseFailure\)")[InputsT, OutputT, MetadataT]
]

```

Runs that failed with exceptions.
####  summary `instance-attribute`
```
summary: ReportCaseAggregate[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.ReportCaseAggregate "ReportCaseAggregate \(pydantic_evals.reporting.ReportCaseAggregate\)")

```

Aggregated statistics across runs.
###  ReportCaseAggregate
Bases: `BaseModel[](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel "pydantic.BaseModel")`
A synthetic case that summarizes a set of cases.
Source code in `pydantic_evals/pydantic_evals/reporting/__init__.py`
```
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
```
| ```
class ReportCaseAggregate(BaseModel):
    """A synthetic case that summarizes a set of cases."""

    name: str

    scores: dict[str, float | int]
    labels: dict[str, dict[str, float]]
    metrics: dict[str, float | int]
    assertions: float | None
    task_duration: float
    total_duration: float

    @staticmethod
    def average(cases: list[ReportCase]) -> ReportCaseAggregate:
        """Produce a synthetic "summary" case by averaging quantitative attributes."""
        num_cases = len(cases)
        if num_cases == 0:
            return ReportCaseAggregate(
                name='Averages',
                scores={},
                labels={},
                metrics={},
                assertions=None,
                task_duration=0.0,
                total_duration=0.0,
            )

        def _scores_averages(scores_by_name: list[dict[str, int | float | bool]]) -> dict[str, float]:
            counts_by_name: dict[str, int] = defaultdict(int)
            sums_by_name: dict[str, float] = defaultdict(float)
            for sbn in scores_by_name:
                for name, score in sbn.items():
                    counts_by_name[name] += 1
                    sums_by_name[name] += score
            return {name: sums_by_name[name] / counts_by_name[name] for name in sums_by_name}

        def _labels_averages(labels_by_name: list[dict[str, str]]) -> dict[str, dict[str, float]]:
            counts_by_name: dict[str, int] = defaultdict(int)
            sums_by_name: dict[str, dict[str, float]] = defaultdict(lambda: defaultdict(float))
            for lbn in labels_by_name:
                for name, label in lbn.items():
                    counts_by_name[name] += 1
                    sums_by_name[name][label] += 1
            return {
                name: {value: count / counts_by_name[name] for value, count in sums_by_name[name].items()}
                for name in sums_by_name
            }

        average_task_duration = sum(case.task_duration for case in cases) / num_cases
        average_total_duration = sum(case.total_duration for case in cases) / num_cases

        # average_assertions: dict[str, float] = _scores_averages([{k: v.value for k, v in case.scores.items()} for case in cases])
        average_scores: dict[str, float] = _scores_averages(
            [{k: v.value for k, v in case.scores.items()} for case in cases]
        )
        average_labels: dict[str, dict[str, float]] = _labels_averages(
            [{k: v.value for k, v in case.labels.items()} for case in cases]
        )
        average_metrics: dict[str, float] = _scores_averages([case.metrics for case in cases])

        average_assertions: float | None = None
        n_assertions = sum(len(case.assertions) for case in cases)
        if n_assertions > 0:
            n_passing = sum(1 for case in cases for assertion in case.assertions.values() if assertion.value)
            average_assertions = n_passing / n_assertions

        return ReportCaseAggregate(
            name='Averages',
            scores=average_scores,
            labels=average_labels,
            metrics=average_metrics,
            assertions=average_assertions,
            task_duration=average_task_duration,
            total_duration=average_total_duration,
        )

    @staticmethod
    def average_from_aggregates(aggregates: list[ReportCaseAggregate]) -> ReportCaseAggregate:
        """Average across multiple aggregates (used for multi-run experiment summaries)."""
        if not aggregates:
            return ReportCaseAggregate(
                name='Averages',
                scores={},
                labels={},
                metrics={},
                assertions=None,
                task_duration=0.0,
                total_duration=0.0,
            )

        def _avg_numeric_dicts(dicts: list[dict[str, float | int]]) -> dict[str, float | int]:
            all_keys: set[str] = set()
            for d in dicts:
                all_keys.update(d)
            return {key: sum(vals) / len(vals) for key in all_keys if (vals := [d[key] for d in dicts if key in d])}

        avg_scores = _avg_numeric_dicts([a.scores for a in aggregates])
        avg_metrics = _avg_numeric_dicts([a.metrics for a in aggregates])

        # Average labels (average the distribution dicts)
        all_label_keys: set[str] = set()
        for a in aggregates:
            all_label_keys.update(a.labels)
        avg_labels: dict[str, dict[str, float]] = {}
        for key in all_label_keys:
            combined: dict[str, float] = {}
            count = 0
            for a in aggregates:
                if key in a.labels:
                    count += 1
                    for label_val, freq in a.labels[key].items():
                        combined[label_val] = combined.get(label_val, 0.0) + freq
            avg_labels[key] = {k: v / count for k, v in combined.items()}

        # Average assertions
        assertion_values = [a.assertions for a in aggregates if a.assertions is not None]
        avg_assertions: float | None = None
        if assertion_values:
            avg_assertions = sum(assertion_values) / len(assertion_values)

        # Average durations
        task_durs = [a.task_duration for a in aggregates]
        total_durs = [a.total_duration for a in aggregates]

        return ReportCaseAggregate(
            name='Averages',
            scores=avg_scores,
            labels=avg_labels,
            metrics=avg_metrics,
            assertions=avg_assertions,
            task_duration=sum(task_durs) / len(task_durs),
            total_duration=sum(total_durs) / len(total_durs),
        )

```

---|---
####  average `staticmethod`
```
average(cases: [ReportCase[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.ReportCase "ReportCase



      dataclass
   \(pydantic_evals.reporting.ReportCase\)")]) -> ReportCaseAggregate[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.ReportCaseAggregate "ReportCaseAggregate \(pydantic_evals.reporting.ReportCaseAggregate\)")

```

Produce a synthetic "summary" case by averaging quantitative attributes.
Source code in `pydantic_evals/pydantic_evals/reporting/__init__.py`
```
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
```
| ```
@staticmethod
def average(cases: list[ReportCase]) -> ReportCaseAggregate:
    """Produce a synthetic "summary" case by averaging quantitative attributes."""
    num_cases = len(cases)
    if num_cases == 0:
        return ReportCaseAggregate(
            name='Averages',
            scores={},
            labels={},
            metrics={},
            assertions=None,
            task_duration=0.0,
            total_duration=0.0,
        )

    def _scores_averages(scores_by_name: list[dict[str, int | float | bool]]) -> dict[str, float]:
        counts_by_name: dict[str, int] = defaultdict(int)
        sums_by_name: dict[str, float] = defaultdict(float)
        for sbn in scores_by_name:
            for name, score in sbn.items():
                counts_by_name[name] += 1
                sums_by_name[name] += score
        return {name: sums_by_name[name] / counts_by_name[name] for name in sums_by_name}

    def _labels_averages(labels_by_name: list[dict[str, str]]) -> dict[str, dict[str, float]]:
        counts_by_name: dict[str, int] = defaultdict(int)
        sums_by_name: dict[str, dict[str, float]] = defaultdict(lambda: defaultdict(float))
