


      module-attribute
   \(pydantic_evals.dataset.OutputT\)"), MetadataT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.MetadataT "MetadataT



      module-attribute
   \(pydantic_evals.dataset.MetadataT\)")]] = (
    []
)

```

List of evaluators to be used on all cases in the dataset.
####  report_evaluators `class-attribute` `instance-attribute`
```
report_evaluators: [
    ReportEvaluator[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.ReportEvaluator "ReportEvaluator



      dataclass
   \(pydantic_evals.evaluators.report_evaluator.ReportEvaluator\)")[InputsT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.InputsT "InputsT



      module-attribute
   \(pydantic_evals.dataset.InputsT\)"), OutputT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.OutputT "OutputT



      module-attribute
   \(pydantic_evals.dataset.OutputT\)"), MetadataT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.MetadataT "MetadataT



      module-attribute
   \(pydantic_evals.dataset.MetadataT\)")]
] = []

```

Evaluators that operate on the full report to produce experiment-wide analyses.
####  __init__
```
__init__(
    *,
    name:  | None = None,
    cases: [Case[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.Case "Case



      dataclass
   \(pydantic_evals.dataset.Case\)")[InputsT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.InputsT "InputsT



      module-attribute
   \(pydantic_evals.dataset.InputsT\)"), OutputT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.OutputT "OutputT



      module-attribute
   \(pydantic_evals.dataset.OutputT\)"), MetadataT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.MetadataT "MetadataT



      module-attribute
   \(pydantic_evals.dataset.MetadataT\)")]],
    evaluators: [
        Evaluator[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.Evaluator "Evaluator



      dataclass
   \(pydantic_evals.evaluators.Evaluator\)")[InputsT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.InputsT "InputsT



      module-attribute
   \(pydantic_evals.dataset.InputsT\)"), OutputT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.OutputT "OutputT



      module-attribute
   \(pydantic_evals.dataset.OutputT\)"), MetadataT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.MetadataT "MetadataT



      module-attribute
   \(pydantic_evals.dataset.MetadataT\)")]
    ] = (),
    report_evaluators: [
        ReportEvaluator[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.ReportEvaluator "ReportEvaluator



      dataclass
   \(pydantic_evals.evaluators.report_evaluator.ReportEvaluator\)")[InputsT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.InputsT "InputsT



      module-attribute
   \(pydantic_evals.dataset.InputsT\)"), OutputT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.OutputT "OutputT



      module-attribute
   \(pydantic_evals.dataset.OutputT\)"), MetadataT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.MetadataT "MetadataT



      module-attribute
   \(pydantic_evals.dataset.MetadataT\)")]
    ] = ()
)

```

Initialize a new dataset with test cases and optional evaluators.
Parameters:
Name | Type | Description | Default
---|---|---|---
`name` |  |  Optional name for the dataset. |  `None`
`cases` |  `Case[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.Case "Case



      dataclass
   \(pydantic_evals.dataset.Case\)")[InputsT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.InputsT "InputsT



      module-attribute
   \(pydantic_evals.dataset.InputsT\)"), OutputT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.OutputT "OutputT



      module-attribute
   \(pydantic_evals.dataset.OutputT\)"), MetadataT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.MetadataT "MetadataT



      module-attribute
   \(pydantic_evals.dataset.MetadataT\)")]]` |  Sequence of test cases to include in the dataset. |  _required_
`evaluators` |  `Evaluator[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.Evaluator "Evaluator



      dataclass
   \(pydantic_evals.evaluators.Evaluator\)")[InputsT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.InputsT "InputsT



      module-attribute
   \(pydantic_evals.dataset.InputsT\)"), OutputT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.OutputT "OutputT



      module-attribute
   \(pydantic_evals.dataset.OutputT\)"), MetadataT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.MetadataT "MetadataT



      module-attribute
   \(pydantic_evals.dataset.MetadataT\)")]]` |  Optional sequence of evaluators to apply to all cases in the dataset. |  `()`
`report_evaluators` |  `ReportEvaluator[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.ReportEvaluator "ReportEvaluator



      dataclass
   \(pydantic_evals.evaluators.report_evaluator.ReportEvaluator\)")[InputsT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.InputsT "InputsT



      module-attribute
   \(pydantic_evals.dataset.InputsT\)"), OutputT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.OutputT "OutputT



      module-attribute
   \(pydantic_evals.dataset.OutputT\)"), MetadataT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.MetadataT "MetadataT



      module-attribute
   \(pydantic_evals.dataset.MetadataT\)")]]` |  Optional sequence of report evaluators that run on the full evaluation report. |  `()`
Source code in `pydantic_evals/pydantic_evals/dataset.py`
```
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
def __init__(
    self,
    *,
    name: str | None = None,
    cases: Sequence[Case[InputsT, OutputT, MetadataT]],
    evaluators: Sequence[Evaluator[InputsT, OutputT, MetadataT]] = (),
    report_evaluators: Sequence[ReportEvaluator[InputsT, OutputT, MetadataT]] = (),
):
    """Initialize a new dataset with test cases and optional evaluators.

    Args:
        name: Optional name for the dataset.
        cases: Sequence of test cases to include in the dataset.
        evaluators: Optional sequence of evaluators to apply to all cases in the dataset.
        report_evaluators: Optional sequence of report evaluators that run on the full evaluation report.
    """
    case_names = set[str]()
    for case in cases:
        if case.name is None:
            continue
        if case.name in case_names:
            raise ValueError(f'Duplicate case name: {case.name!r}')
        case_names.add(case.name)

    super().__init__(
        name=name,
        cases=cases,
        evaluators=list(evaluators),
        report_evaluators=list(report_evaluators),
    )

```

---|---
####  evaluate `async`
```
evaluate(
    task: (
        [[InputsT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.InputsT "InputsT



      module-attribute
   \(pydantic_evals.dataset.InputsT\)")], [OutputT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.OutputT "OutputT



      module-attribute
   \(pydantic_evals.dataset.OutputT\)")]]
        | [[InputsT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.InputsT "InputsT



      module-attribute
   \(pydantic_evals.dataset.InputsT\)")], OutputT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.OutputT "OutputT



      module-attribute
   \(pydantic_evals.dataset.OutputT\)")]
    ),
    name:  | None = None,
    max_concurrency:  | None = None,
    progress:  = True,
    retry_task: RetryConfig[](https://ai.pydantic.dev/api/retries/#pydantic_ai.retries.RetryConfig "RetryConfig \(pydantic_ai.retries.RetryConfig\)") | None = None,
    retry_evaluators: RetryConfig[](https://ai.pydantic.dev/api/retries/#pydantic_ai.retries.RetryConfig "RetryConfig \(pydantic_ai.retries.RetryConfig\)") | None = None,
    *,
    task_name:  | None = None,
    metadata: [, ] | None = None,
    repeat:  = 1
) -> EvaluationReport[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.EvaluationReport "EvaluationReport



      dataclass
   \(pydantic_evals.reporting.EvaluationReport\)")[InputsT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.InputsT "InputsT



      module-attribute
   \(pydantic_evals.dataset.InputsT\)"), OutputT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.OutputT "OutputT



      module-attribute
   \(pydantic_evals.dataset.OutputT\)"), MetadataT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.MetadataT "MetadataT



      module-attribute
   \(pydantic_evals.dataset.MetadataT\)")]

```

Evaluates the test cases in the dataset using the given task.
This method runs the task on each case in the dataset, applies evaluators, and collects results into a report. Cases are run concurrently, limited by `max_concurrency` if specified.
Parameters:
Name | Type | Description | Default
---|---|---|---
`task` |  `InputsT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.InputsT "InputsT



      module-attribute
   \(pydantic_evals.dataset.InputsT\)")], OutputT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.OutputT "OutputT



      module-attribute
   \(pydantic_evals.dataset.OutputT\)")]] | InputsT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.InputsT "InputsT



      module-attribute
   \(pydantic_evals.dataset.InputsT\)")], OutputT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.OutputT "OutputT



      module-attribute
   \(pydantic_evals.dataset.OutputT\)")]` |  The task to evaluate. This should be a callable that takes the inputs of the case and returns the output. |  _required_
`name` |  |  The name of the experiment being run, this is used to identify the experiment in the report. If omitted, the task_name will be used; if that is not specified, the name of the task function is used. |  `None`
`max_concurrency` |  |  The maximum number of concurrent evaluations of the task to allow. If None, all cases will be evaluated concurrently. |  `None`
`progress` |  |  Whether to show a progress bar for the evaluation. Defaults to `True`. |  `True`
`retry_task` |  `RetryConfig[](https://ai.pydantic.dev/api/retries/#pydantic_ai.retries.RetryConfig "RetryConfig \(pydantic_ai.retries.RetryConfig\)") | None` |  Optional retry configuration for the task execution. |  `None`
`retry_evaluators` |  `RetryConfig[](https://ai.pydantic.dev/api/retries/#pydantic_ai.retries.RetryConfig "RetryConfig \(pydantic_ai.retries.RetryConfig\)") | None` |  Optional retry configuration for evaluator execution. |  `None`
`task_name` |  |  Optional override to the name of the task being executed, otherwise the name of the task function will be used. |  `None`
`metadata` |  |  Optional dict of experiment metadata. |  `None`
`repeat` |  |  Number of times to run each case. When > 1, each case is run multiple times and results are grouped by the original case name for aggregation. Defaults to 1. |  `1`
Returns:
Type | Description
---|---
`EvaluationReport[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.EvaluationReport "EvaluationReport



      dataclass
   \(pydantic_evals.reporting.EvaluationReport\)")[InputsT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.InputsT "InputsT



      module-attribute
   \(pydantic_evals.dataset.InputsT\)"), OutputT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.OutputT "OutputT



      module-attribute
   \(pydantic_evals.dataset.OutputT\)"), MetadataT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.MetadataT "MetadataT



      module-attribute
   \(pydantic_evals.dataset.MetadataT\)")]` |  A report containing the results of the evaluation.
Source code in `pydantic_evals/pydantic_evals/dataset.py`
```
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
```
| ```
async def evaluate(
    self,
    task: Callable[[InputsT], Awaitable[OutputT]] | Callable[[InputsT], OutputT],
    name: str | None = None,
    max_concurrency: int | None = None,
    progress: bool = True,
    retry_task: RetryConfig | None = None,
    retry_evaluators: RetryConfig | None = None,
    *,
    task_name: str | None = None,
    metadata: dict[str, Any] | None = None,
    repeat: int = 1,
) -> EvaluationReport[InputsT, OutputT, MetadataT]:
    """Evaluates the test cases in the dataset using the given task.

    This method runs the task on each case in the dataset, applies evaluators,
    and collects results into a report. Cases are run concurrently, limited by `max_concurrency` if specified.

    Args:
        task: The task to evaluate. This should be a callable that takes the inputs of the case
            and returns the output.
        name: The name of the experiment being run, this is used to identify the experiment in the report.
            If omitted, the task_name will be used; if that is not specified, the name of the task function is used.
        max_concurrency: The maximum number of concurrent evaluations of the task to allow.
            If None, all cases will be evaluated concurrently.
        progress: Whether to show a progress bar for the evaluation. Defaults to `True`.
        retry_task: Optional retry configuration for the task execution.
        retry_evaluators: Optional retry configuration for evaluator execution.
        task_name: Optional override to the name of the task being executed, otherwise the name of the task
            function will be used.
        metadata: Optional dict of experiment metadata.
        repeat: Number of times to run each case. When > 1, each case is run multiple times and
            results are grouped by the original case name for aggregation. Defaults to 1.

    Returns:
        A report containing the results of the evaluation.
    """
    if repeat < 1:
        raise ValueError(f'repeat must be >= 1, got {repeat}')

    task_name = task_name or get_unwrapped_function_name(task)
    name = name or task_name

    tasks_to_run = self._build_tasks_to_run(repeat)
    total_tasks = len(tasks_to_run)
    progress_bar = Progress() if progress else None

    limiter = anyio.Semaphore(max_concurrency) if max_concurrency is not None else AsyncExitStack()

    extra_attributes: dict[str, Any] = {'gen_ai.operation.name': 'experiment'}
    if metadata is not None:
        extra_attributes['metadata'] = metadata
    if repeat > 1:
        extra_attributes['logfire.experiment.repeat'] = repeat
    with (
        logfire_span(
            'evaluate {name}',
            name=name,
            task_name=task_name,
            dataset_name=self.name,
            n_cases=len(self.cases),
            **extra_attributes,
        ) as eval_span,
        progress_bar or nullcontext(),
    ):
        task_id = progress_bar.add_task(f'Evaluating {task_name}', total=total_tasks) if progress_bar else None

        async def _handle_case(
            case: Case[InputsT, OutputT, MetadataT],
            report_case_name: str,
            source_case_name: str | None,
        ):
            async with limiter:
                result = await _run_task_and_evaluators(
                    task,
                    case,
                    report_case_name,
                    self.evaluators,
                    retry_task,
                    retry_evaluators,
                    source_case_name=source_case_name,
                )
                if progress_bar and task_id is not None:  # pragma: no branch
                    progress_bar.update(task_id, advance=1)
                return result

        if (context := eval_span.context) is None:  # pragma: no cover
            trace_id = None
            span_id = None
        else:
            trace_id = f'{context.trace_id:032x}'
            span_id = f'{context.span_id:016x}'
        cases_and_failures = await task_group_gather(
            [
                lambda case=case, rn=report_name, scn=source_name: _handle_case(case, rn, scn)
                for case, report_name, source_name in tasks_to_run
            ]
        )
        cases: list[ReportCase] = []
        failures: list[ReportCaseFailure] = []
        for item in cases_and_failures:
            if isinstance(item, ReportCase):
                cases.append(item)
            else:
                failures.append(item)
        report = EvaluationReport(
            name=name,
            cases=cases,
            failures=failures,
            experiment_metadata=metadata,
            span_id=span_id,
            trace_id=trace_id,
        )

        # Run report evaluators
        if self.report_evaluators:
            report_ctx = ReportEvaluatorContext(
                name=name,
                report=report,
                experiment_metadata=metadata,
            )
            await _run_report_evaluators(self.report_evaluators, report_ctx)

        _set_experiment_span_attributes(eval_span, report, metadata, len(self.cases), repeat)
    return report

```

---|---
####  evaluate_sync
```
evaluate_sync(
    task: (
        [[InputsT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.InputsT "InputsT



      module-attribute
   \(pydantic_evals.dataset.InputsT\)")], [OutputT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.OutputT "OutputT



      module-attribute
   \(pydantic_evals.dataset.OutputT\)")]]
        | [[InputsT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.InputsT "InputsT



      module-attribute
   \(pydantic_evals.dataset.InputsT\)")], OutputT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.OutputT "OutputT



      module-attribute
   \(pydantic_evals.dataset.OutputT\)")]
    ),
    name:  | None = None,
    max_concurrency:  | None = None,
    progress:  = True,
    retry_task: RetryConfig[](https://ai.pydantic.dev/api/retries/#pydantic_ai.retries.RetryConfig "RetryConfig \(pydantic_ai.retries.RetryConfig\)") | None = None,
    retry_evaluators: RetryConfig[](https://ai.pydantic.dev/api/retries/#pydantic_ai.retries.RetryConfig "RetryConfig \(pydantic_ai.retries.RetryConfig\)") | None = None,
    *,
    task_name:  | None = None,
    metadata: [, ] | None = None,
    repeat:  = 1
) -> EvaluationReport[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.EvaluationReport "EvaluationReport



      dataclass
   \(pydantic_evals.reporting.EvaluationReport\)")[InputsT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.InputsT "InputsT



      module-attribute
   \(pydantic_evals.dataset.InputsT\)"), OutputT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.OutputT "OutputT



      module-attribute
   \(pydantic_evals.dataset.OutputT\)"), MetadataT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.MetadataT "MetadataT



      module-attribute
   \(pydantic_evals.dataset.MetadataT\)")]

```

Evaluates the test cases in the dataset using the given task.
This is a synchronous wrapper around [`evaluate`](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.Dataset.evaluate "evaluate



      async
  ") provided for convenience.
Parameters:
Name | Type | Description | Default
---|---|---|---
`task` |  `InputsT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.InputsT "InputsT



      module-attribute
   \(pydantic_evals.dataset.InputsT\)")], OutputT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.OutputT "OutputT



      module-attribute
   \(pydantic_evals.dataset.OutputT\)")]] | InputsT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.InputsT "InputsT



      module-attribute
   \(pydantic_evals.dataset.InputsT\)")], OutputT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.OutputT "OutputT



      module-attribute
   \(pydantic_evals.dataset.OutputT\)")]` |  The task to evaluate. This should be a callable that takes the inputs of the case and returns the output. |  _required_
`name` |  |  The name of the experiment being run, this is used to identify the experiment in the report. If omitted, the task_name will be used; if that is not specified, the name of the task function is used. |  `None`
`max_concurrency` |  |  The maximum number of concurrent evaluations of the task to allow. If None, all cases will be evaluated concurrently. |  `None`
`progress` |  |  Whether to show a progress bar for the evaluation. Defaults to `True`. |  `True`
`retry_task` |  `RetryConfig[](https://ai.pydantic.dev/api/retries/#pydantic_ai.retries.RetryConfig "RetryConfig \(pydantic_ai.retries.RetryConfig\)") | None` |  Optional retry configuration for the task execution. |  `None`
`retry_evaluators` |  `RetryConfig[](https://ai.pydantic.dev/api/retries/#pydantic_ai.retries.RetryConfig "RetryConfig \(pydantic_ai.retries.RetryConfig\)") | None` |  Optional retry configuration for evaluator execution. |  `None`
`task_name` |  |  Optional override to the name of the task being executed, otherwise the name of the task function will be used. |  `None`
`metadata` |  |  Optional dict of experiment metadata. |  `None`
`repeat` |  |  Number of times to run each case. When > 1, each case is run multiple times and results are grouped by the original case name for aggregation. Defaults to 1. |  `1`
Returns:
Type | Description
---|---
`EvaluationReport[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.EvaluationReport "EvaluationReport



      dataclass
   \(pydantic_evals.reporting.EvaluationReport\)")[InputsT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.InputsT "InputsT



      module-attribute
   \(pydantic_evals.dataset.InputsT\)"), OutputT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.OutputT "OutputT



      module-attribute
   \(pydantic_evals.dataset.OutputT\)"), MetadataT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.MetadataT "MetadataT



      module-attribute
   \(pydantic_evals.dataset.MetadataT\)")]` |  A report containing the results of the evaluation.
Source code in `pydantic_evals/pydantic_evals/dataset.py`
```
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
```
| ```
def evaluate_sync(
    self,
    task: Callable[[InputsT], Awaitable[OutputT]] | Callable[[InputsT], OutputT],
    name: str | None = None,
    max_concurrency: int | None = None,
    progress: bool = True,
    retry_task: RetryConfig | None = None,
    retry_evaluators: RetryConfig | None = None,
    *,
    task_name: str | None = None,
    metadata: dict[str, Any] | None = None,
    repeat: int = 1,
) -> EvaluationReport[InputsT, OutputT, MetadataT]:
    """Evaluates the test cases in the dataset using the given task.

    This is a synchronous wrapper around [`evaluate`][pydantic_evals.dataset.Dataset.evaluate] provided for convenience.

    Args:
        task: The task to evaluate. This should be a callable that takes the inputs of the case
            and returns the output.
        name: The name of the experiment being run, this is used to identify the experiment in the report.
            If omitted, the task_name will be used; if that is not specified, the name of the task function is used.
        max_concurrency: The maximum number of concurrent evaluations of the task to allow.
            If None, all cases will be evaluated concurrently.
        progress: Whether to show a progress bar for the evaluation. Defaults to `True`.
        retry_task: Optional retry configuration for the task execution.
        retry_evaluators: Optional retry configuration for evaluator execution.
        task_name: Optional override to the name of the task being executed, otherwise the name of the task
            function will be used.
        metadata: Optional dict of experiment metadata.
