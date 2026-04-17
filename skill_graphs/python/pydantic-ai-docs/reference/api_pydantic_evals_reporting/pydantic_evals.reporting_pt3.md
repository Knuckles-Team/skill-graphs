


      dataclass
   \(pydantic_evals.evaluators.evaluator.EvaluatorFailure\)")] = (
    default_factory=[EvaluatorFailure[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.EvaluatorFailure "EvaluatorFailure



      dataclass
   \(pydantic_evals.evaluators.evaluator.EvaluatorFailure\)")]
)

```

Failures from report evaluators that raised exceptions.
####  experiment_metadata `class-attribute` `instance-attribute`
```
experiment_metadata: [, ] | None = None

```

Metadata associated with the specific experiment represented by this report.
####  trace_id `class-attribute` `instance-attribute`
```
trace_id:  | None = None

```

The trace ID of the evaluation.
####  span_id `class-attribute` `instance-attribute`
```
span_id:  | None = None

```

The span ID of the evaluation.
####  case_groups
```
case_groups() -> (
    [ReportCaseGroup[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.ReportCaseGroup "ReportCaseGroup



      dataclass
   \(pydantic_evals.reporting.ReportCaseGroup\)")[InputsT, OutputT, MetadataT]]
    | None
)

```

Group cases by source_case_name and compute per-group aggregates.
Returns None if no cases have source_case_name set (i.e., single-run experiment).
Source code in `pydantic_evals/pydantic_evals/reporting/__init__.py`
```
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
```
| ```
def case_groups(self) -> list[ReportCaseGroup[InputsT, OutputT, MetadataT]] | None:
    """Group cases by source_case_name and compute per-group aggregates.

    Returns None if no cases have source_case_name set (i.e., single-run experiment).
    """
    if not any(c.source_case_name for c in self.cases) and not any(f.source_case_name for f in self.failures):
        return None

    groups: dict[
        str,
        tuple[list[ReportCase[InputsT, OutputT, MetadataT]], list[ReportCaseFailure[InputsT, OutputT, MetadataT]]],
    ] = {}
    for case in self.cases:
        key = case.source_case_name or case.name
        groups.setdefault(key, ([], []))[0].append(case)
    for failure in self.failures:
        key = failure.source_case_name or failure.name
        groups.setdefault(key, ([], []))[1].append(failure)

    result: list[ReportCaseGroup[InputsT, OutputT, MetadataT]] = []
    for group_name, (runs, failures) in groups.items():
        first: ReportCase[InputsT, OutputT, MetadataT] | ReportCaseFailure[InputsT, OutputT, MetadataT] = (
            runs[0] if runs else failures[0]
        )
        result.append(
            ReportCaseGroup(
                name=group_name,
                inputs=first.inputs,
                metadata=first.metadata,
                expected_output=first.expected_output,
                runs=runs,
                failures=failures,
                summary=ReportCaseAggregate.average(list(runs)),
            )
        )
    return result

```

---|---
####  render
```
render(
    width:  | None = None,
    baseline: (
        EvaluationReport[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.EvaluationReport "EvaluationReport



      dataclass
   \(pydantic_evals.reporting.EvaluationReport\)")[InputsT, OutputT, MetadataT] | None
    ) = None,
    *,
    include_input:  = False,
    include_metadata:  = False,
    include_expected_output:  = False,
    include_output:  = False,
    include_durations:  = True,
    include_total_duration:  = False,
    include_removed_cases:  = False,
    include_averages:  = True,
    include_errors:  = True,
    include_error_stacktrace:  = False,
    include_evaluator_failures:  = True,
    include_analyses:  = True,
    input_config: RenderValueConfig[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.RenderValueConfig "RenderValueConfig \(pydantic_evals.reporting.RenderValueConfig\)") | None = None,
    metadata_config: RenderValueConfig[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.RenderValueConfig "RenderValueConfig \(pydantic_evals.reporting.RenderValueConfig\)") | None = None,
    output_config: RenderValueConfig[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.RenderValueConfig "RenderValueConfig \(pydantic_evals.reporting.RenderValueConfig\)") | None = None,
    score_configs: (
        [, RenderNumberConfig[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.RenderNumberConfig "RenderNumberConfig \(pydantic_evals.reporting.RenderNumberConfig\)")] | None
    ) = None,
    label_configs: (
        [, RenderValueConfig[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.RenderValueConfig "RenderValueConfig \(pydantic_evals.reporting.RenderValueConfig\)")] | None
    ) = None,
    metric_configs: (
        [, RenderNumberConfig[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.RenderNumberConfig "RenderNumberConfig \(pydantic_evals.reporting.RenderNumberConfig\)")] | None
    ) = None,
    duration_config: RenderNumberConfig[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.RenderNumberConfig "RenderNumberConfig \(pydantic_evals.reporting.RenderNumberConfig\)") | None = None,
    include_reasons:  = False
) ->

```

Render this report to a nicely-formatted string, optionally comparing it to a baseline report.
If you want more control over the output, use `console_table` instead and pass it to `rich.Console.print`.
Source code in `pydantic_evals/pydantic_evals/reporting/__init__.py`
```
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
```
| ```
def render(
    self,
    width: int | None = None,
    baseline: EvaluationReport[InputsT, OutputT, MetadataT] | None = None,
    *,
    include_input: bool = False,
    include_metadata: bool = False,
    include_expected_output: bool = False,
    include_output: bool = False,
    include_durations: bool = True,
    include_total_duration: bool = False,
    include_removed_cases: bool = False,
    include_averages: bool = True,
    include_errors: bool = True,
    include_error_stacktrace: bool = False,
    include_evaluator_failures: bool = True,
    include_analyses: bool = True,
    input_config: RenderValueConfig | None = None,
    metadata_config: RenderValueConfig | None = None,
    output_config: RenderValueConfig | None = None,
    score_configs: dict[str, RenderNumberConfig] | None = None,
    label_configs: dict[str, RenderValueConfig] | None = None,
    metric_configs: dict[str, RenderNumberConfig] | None = None,
    duration_config: RenderNumberConfig | None = None,
    include_reasons: bool = False,
) -> str:
    """Render this report to a nicely-formatted string, optionally comparing it to a baseline report.

    If you want more control over the output, use `console_table` instead and pass it to `rich.Console.print`.
    """
    io_file = StringIO()
    console = Console(width=width, file=io_file)
    self.print(
        width=width,
        baseline=baseline,
        console=console,
        include_input=include_input,
        include_metadata=include_metadata,
        include_expected_output=include_expected_output,
        include_output=include_output,
        include_durations=include_durations,
        include_total_duration=include_total_duration,
        include_removed_cases=include_removed_cases,
        include_averages=include_averages,
        include_errors=include_errors,
        include_error_stacktrace=include_error_stacktrace,
        include_evaluator_failures=include_evaluator_failures,
        include_analyses=include_analyses,
        input_config=input_config,
        metadata_config=metadata_config,
        output_config=output_config,
        score_configs=score_configs,
        label_configs=label_configs,
        metric_configs=metric_configs,
        duration_config=duration_config,
        include_reasons=include_reasons,
    )
    return io_file.getvalue()

```

---|---
####  print
```
print(
    width:  | None = None,
    baseline: (
        EvaluationReport[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.EvaluationReport "EvaluationReport



      dataclass
   \(pydantic_evals.reporting.EvaluationReport\)")[InputsT, OutputT, MetadataT] | None
    ) = None,
    *,
    console:  | None = None,
    include_input:  = False,
    include_metadata:  = False,
    include_expected_output:  = False,
    include_output:  = False,
    include_durations:  = True,
    include_total_duration:  = False,
    include_removed_cases:  = False,
    include_averages:  = True,
    include_errors:  = True,
    include_error_stacktrace:  = False,
    include_evaluator_failures:  = True,
    include_analyses:  = True,
    input_config: RenderValueConfig[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.RenderValueConfig "RenderValueConfig \(pydantic_evals.reporting.RenderValueConfig\)") | None = None,
    metadata_config: RenderValueConfig[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.RenderValueConfig "RenderValueConfig \(pydantic_evals.reporting.RenderValueConfig\)") | None = None,
    output_config: RenderValueConfig[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.RenderValueConfig "RenderValueConfig \(pydantic_evals.reporting.RenderValueConfig\)") | None = None,
    score_configs: (
        [, RenderNumberConfig[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.RenderNumberConfig "RenderNumberConfig \(pydantic_evals.reporting.RenderNumberConfig\)")] | None
    ) = None,
    label_configs: (
        [, RenderValueConfig[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.RenderValueConfig "RenderValueConfig \(pydantic_evals.reporting.RenderValueConfig\)")] | None
    ) = None,
    metric_configs: (
        [, RenderNumberConfig[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.RenderNumberConfig "RenderNumberConfig \(pydantic_evals.reporting.RenderNumberConfig\)")] | None
    ) = None,
    duration_config: RenderNumberConfig[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.RenderNumberConfig "RenderNumberConfig \(pydantic_evals.reporting.RenderNumberConfig\)") | None = None,
    include_reasons:  = False
) -> None

```

Print this report to the console, optionally comparing it to a baseline report.
If you want more control over the output, use `console_table` instead and pass it to `rich.Console.print`.
Source code in `pydantic_evals/pydantic_evals/reporting/__init__.py`
```
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
```
| ```
def print(
    self,
    width: int | None = None,
    baseline: EvaluationReport[InputsT, OutputT, MetadataT] | None = None,
    *,
    console: Console | None = None,
    include_input: bool = False,
    include_metadata: bool = False,
    include_expected_output: bool = False,
    include_output: bool = False,
    include_durations: bool = True,
    include_total_duration: bool = False,
    include_removed_cases: bool = False,
    include_averages: bool = True,
    include_errors: bool = True,
    include_error_stacktrace: bool = False,
    include_evaluator_failures: bool = True,
    include_analyses: bool = True,
    input_config: RenderValueConfig | None = None,
    metadata_config: RenderValueConfig | None = None,
    output_config: RenderValueConfig | None = None,
    score_configs: dict[str, RenderNumberConfig] | None = None,
    label_configs: dict[str, RenderValueConfig] | None = None,
    metric_configs: dict[str, RenderNumberConfig] | None = None,
    duration_config: RenderNumberConfig | None = None,
    include_reasons: bool = False,
) -> None:
    """Print this report to the console, optionally comparing it to a baseline report.

    If you want more control over the output, use `console_table` instead and pass it to `rich.Console.print`.
    """
    if console is None:  # pragma: no branch
        console = Console(width=width)

    metadata_panel = self._metadata_panel(baseline=baseline)
    renderable: RenderableType = self.console_table(
        baseline=baseline,
        include_input=include_input,
        include_metadata=include_metadata,
        include_expected_output=include_expected_output,
        include_output=include_output,
        include_durations=include_durations,
        include_total_duration=include_total_duration,
        include_removed_cases=include_removed_cases,
        include_averages=include_averages,
        include_evaluator_failures=include_evaluator_failures,
        input_config=input_config,
        metadata_config=metadata_config,
        output_config=output_config,
        score_configs=score_configs,
        label_configs=label_configs,
        metric_configs=metric_configs,
        duration_config=duration_config,
        include_reasons=include_reasons,
        with_title=not metadata_panel,
    )
    # Wrap table with experiment metadata panel if present
    if metadata_panel:
        renderable = Group(metadata_panel, renderable)
    console.print(renderable)
    if include_analyses and self.analyses:
        for analysis in self.analyses:
            console.print(_render_analysis(analysis))
    if include_evaluator_failures and self.report_evaluator_failures:
        console.print(
            Text('\nReport Evaluator Failures:', style='bold red'),
        )
        for failure in self.report_evaluator_failures:
            msg = f'  {failure.name}: {failure.error_message}'
            console.print(Text(msg, style='red'))
    if include_errors and self.failures:  # pragma: no cover
        failures_table = self.failures_table(
            include_input=include_input,
            include_metadata=include_metadata,
            include_expected_output=include_expected_output,
            include_error_message=True,
            include_error_stacktrace=include_error_stacktrace,
            input_config=input_config,
            metadata_config=metadata_config,
        )
        console.print(failures_table, style='red')

```

---|---
####  console_table
```
console_table(
    baseline: (
        EvaluationReport[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.EvaluationReport "EvaluationReport



      dataclass
   \(pydantic_evals.reporting.EvaluationReport\)")[InputsT, OutputT, MetadataT] | None
    ) = None,
    *,
    include_input:  = False,
    include_metadata:  = False,
    include_expected_output:  = False,
    include_output:  = False,
    include_durations:  = True,
    include_total_duration:  = False,
    include_removed_cases:  = False,
    include_averages:  = True,
    include_evaluator_failures:  = True,
    input_config: RenderValueConfig[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.RenderValueConfig "RenderValueConfig \(pydantic_evals.reporting.RenderValueConfig\)") | None = None,
    metadata_config: RenderValueConfig[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.RenderValueConfig "RenderValueConfig \(pydantic_evals.reporting.RenderValueConfig\)") | None = None,
    output_config: RenderValueConfig[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.RenderValueConfig "RenderValueConfig \(pydantic_evals.reporting.RenderValueConfig\)") | None = None,
    score_configs: (
        [, RenderNumberConfig[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.RenderNumberConfig "RenderNumberConfig \(pydantic_evals.reporting.RenderNumberConfig\)")] | None
    ) = None,
    label_configs: (
        [, RenderValueConfig[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.RenderValueConfig "RenderValueConfig \(pydantic_evals.reporting.RenderValueConfig\)")] | None
    ) = None,
    metric_configs: (
        [, RenderNumberConfig[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.RenderNumberConfig "RenderNumberConfig \(pydantic_evals.reporting.RenderNumberConfig\)")] | None
    ) = None,
    duration_config: RenderNumberConfig[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.RenderNumberConfig "RenderNumberConfig \(pydantic_evals.reporting.RenderNumberConfig\)") | None = None,
    include_reasons:  = False,
    with_title:  = True
) ->

```

Return a table containing the data from this report.
If a baseline is provided, returns a diff between this report and the baseline report. Optionally include input and output details.
Source code in `pydantic_evals/pydantic_evals/reporting/__init__.py`
```
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
```
| ```
def console_table(
    self,
    baseline: EvaluationReport[InputsT, OutputT, MetadataT] | None = None,
    *,
    include_input: bool = False,
    include_metadata: bool = False,
    include_expected_output: bool = False,
    include_output: bool = False,
    include_durations: bool = True,
    include_total_duration: bool = False,
    include_removed_cases: bool = False,
    include_averages: bool = True,
    include_evaluator_failures: bool = True,
    input_config: RenderValueConfig | None = None,
    metadata_config: RenderValueConfig | None = None,
    output_config: RenderValueConfig | None = None,
    score_configs: dict[str, RenderNumberConfig] | None = None,
    label_configs: dict[str, RenderValueConfig] | None = None,
    metric_configs: dict[str, RenderNumberConfig] | None = None,
    duration_config: RenderNumberConfig | None = None,
    include_reasons: bool = False,
    with_title: bool = True,
) -> Table:
    """Return a table containing the data from this report.

    If a baseline is provided, returns a diff between this report and the baseline report.
    Optionally include input and output details.
    """
    renderer = EvaluationRenderer(
        include_input=include_input,
        include_metadata=include_metadata,
        include_expected_output=include_expected_output,
        include_output=include_output,
        include_durations=include_durations,
        include_total_duration=include_total_duration,
        include_removed_cases=include_removed_cases,
        include_averages=include_averages,
        include_error_message=False,
        include_error_stacktrace=False,
        include_evaluator_failures=include_evaluator_failures,
        input_config={**_DEFAULT_VALUE_CONFIG, **(input_config or {})},
        metadata_config={**_DEFAULT_VALUE_CONFIG, **(metadata_config or {})},
        output_config=output_config or _DEFAULT_VALUE_CONFIG,
        score_configs=score_configs or {},
        label_configs=label_configs or {},
        metric_configs=metric_configs or {},
        duration_config=duration_config or _DEFAULT_DURATION_CONFIG,
        include_reasons=include_reasons,
    )
    if baseline is None:
        return renderer.build_table(self, with_title=with_title)
    else:
        return renderer.build_diff_table(self, baseline, with_title=with_title)

```

---|---
####  failures_table
```
failures_table(
    *,
    include_input:  = False,
    include_metadata:  = False,
    include_expected_output:  = False,
    include_error_message:  = True,
    include_error_stacktrace:  = True,
    input_config: RenderValueConfig[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.RenderValueConfig "RenderValueConfig \(pydantic_evals.reporting.RenderValueConfig\)") | None = None,
    metadata_config: RenderValueConfig[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.RenderValueConfig "RenderValueConfig \(pydantic_evals.reporting.RenderValueConfig\)") | None = None
) ->

```

Return a table containing the failures in this report.
Source code in `pydantic_evals/pydantic_evals/reporting/__init__.py`
```
641
642
643
644
645
646
647
648
649
650
651
652
653
654
655
656
657
658
659
660
661
662
663
664
665
666
667
668
669
670
671
672
673
674
```
| ```
def failures_table(
    self,
    *,
    include_input: bool = False,
    include_metadata: bool = False,
    include_expected_output: bool = False,
    include_error_message: bool = True,
    include_error_stacktrace: bool = True,
    input_config: RenderValueConfig | None = None,
    metadata_config: RenderValueConfig | None = None,
) -> Table:
    """Return a table containing the failures in this report."""
    renderer = EvaluationRenderer(
        include_input=include_input,
        include_metadata=include_metadata,
        include_expected_output=include_expected_output,
        include_output=False,
        include_durations=False,
        include_total_duration=False,
        include_removed_cases=False,
        include_averages=False,
        input_config={**_DEFAULT_VALUE_CONFIG, **(input_config or {})},
        metadata_config={**_DEFAULT_VALUE_CONFIG, **(metadata_config or {})},
        output_config=_DEFAULT_VALUE_CONFIG,
        score_configs={},
        label_configs={},
        metric_configs={},
        duration_config=_DEFAULT_DURATION_CONFIG,
        include_reasons=False,
        include_error_message=include_error_message,
        include_error_stacktrace=include_error_stacktrace,
        include_evaluator_failures=False,  # Not applicable for failures table
    )
    return renderer.build_failures_table(self)

```

---|---
####  __str__
```
__str__() ->

```

Return a string representation of the report.
Source code in `pydantic_evals/pydantic_evals/reporting/__init__.py`
```
676
677
678
```
| ```
def __str__(self) -> str:  # pragma: lax no cover
    """Return a string representation of the report."""
    return self.render()

```

---|---
###  RenderValueConfig
Bases:
A configuration for rendering a values in an Evaluation report.
Source code in `pydantic_evals/pydantic_evals/reporting/__init__.py`
```
684
685
686
687
688
689
690
```
| ```
class RenderValueConfig(TypedDict, total=False):
    """A configuration for rendering a values in an Evaluation report."""

    value_formatter: str | Callable[[Any], str]
    diff_checker: Callable[[Any, Any], bool] | None
    diff_formatter: Callable[[Any, Any], str | None] | None
    diff_style: str

```

---|---
###  RenderNumberConfig
Bases:
A configuration for rendering a particular score or metric in an Evaluation report.
See the implementation of `_RenderNumber` for more clarity on how these parameters affect the rendering.
Source code in `pydantic_evals/pydantic_evals/reporting/__init__.py`
```
747
748
749
750
751
752
753
754
755
756
757
758
759
760
761
762
763
764
765
766
767
768
769
770
771
772
773
774
775
776
777
778
779
780
781
782
783
784
785
786
787
788
789
790
791
792
793
794
795
796
797
798
799
800
801
802
803
804
805
```
| ```
class RenderNumberConfig(TypedDict, total=False):
    """A configuration for rendering a particular score or metric in an Evaluation report.

    See the implementation of `_RenderNumber` for more clarity on how these parameters affect the rendering.
    """

    value_formatter: str | Callable[[float | int], str]
    """The logic to use for formatting values.

    * If not provided, format as ints if all values are ints, otherwise at least one decimal place and at least four significant figures.
    * You can also use a custom string format spec, e.g. '{:.3f}'
    * You can also use a custom function, e.g. lambda x: f'{x:.3f}'
    """
    diff_formatter: str | Callable[[float | int, float | int], str | None] | None
    """The logic to use for formatting details about the diff.

    The strings produced by the value_formatter will always be included in the reports, but the diff_formatter is
    used to produce additional text about the difference between the old and new values, such as the absolute or
    relative difference.

    * If not provided, format as ints if all values are ints, otherwise at least one decimal place and at least four
        significant figures, and will include the percentage change.
    * You can also use a custom string format spec, e.g. '{:+.3f}'
    * You can also use a custom function, e.g. lambda x: f'{x:+.3f}'.
        If this function returns None, no extra diff text will be added.
    * You can also use None to never generate extra diff text.
    """
    diff_atol: float
    """The absolute tolerance for considering a difference "significant".

    A difference is "significant" if `abs(new - old) < self.diff_atol + self.diff_rtol * abs(old)`.

    If a difference is not significant, it will not have the diff styles applied. Note that we still show
    both the rendered before and after values in the diff any time they differ, even if the difference is not
    significant. (If the rendered values are exactly the same, we only show the value once.)
