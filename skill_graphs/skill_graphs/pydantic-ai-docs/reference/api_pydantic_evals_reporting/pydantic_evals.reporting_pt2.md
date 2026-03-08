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

```

---|---
####  average_from_aggregates `staticmethod`
```
average_from_aggregates(
    aggregates: [ReportCaseAggregate[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.ReportCaseAggregate "ReportCaseAggregate \(pydantic_evals.reporting.ReportCaseAggregate\)")],
) -> ReportCaseAggregate[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.ReportCaseAggregate "ReportCaseAggregate \(pydantic_evals.reporting.ReportCaseAggregate\)")

```

Average across multiple aggregates (used for multi-run experiment summaries).
Source code in `pydantic_evals/pydantic_evals/reporting/__init__.py`
```
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
###  EvaluationReport `dataclass`
Bases: `InputsT, OutputT, MetadataT]`
A report of the results of evaluating a model on a set of cases.
Source code in `pydantic_evals/pydantic_evals/reporting/__init__.py`
```
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
581
582
583
584
585
586
587
588
589
590
591
592
593
594
595
596
597
598
599
600
601
602
603
604
605
606
607
608
609
610
611
612
613
614
615
616
617
618
619
620
621
622
623
624
625
626
627
628
629
630
631
632
633
634
635
636
637
638
639
640
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
675
676
677
678
```
| ```
@dataclass(kw_only=True)
class EvaluationReport(Generic[InputsT, OutputT, MetadataT]):
    """A report of the results of evaluating a model on a set of cases."""

    name: str
    """The name of the report."""

    cases: list[ReportCase[InputsT, OutputT, MetadataT]]
    """The cases in the report."""
    failures: list[ReportCaseFailure[InputsT, OutputT, MetadataT]] = field(
        default_factory=list[ReportCaseFailure[InputsT, OutputT, MetadataT]]
    )
    """The failures in the report. These are cases where task execution raised an exception."""

    analyses: list[ReportAnalysis] = field(default_factory=list[ReportAnalysis])
    """Experiment-wide analyses produced by report evaluators."""

    report_evaluator_failures: list[EvaluatorFailure] = field(default_factory=list[EvaluatorFailure])
    """Failures from report evaluators that raised exceptions."""

    experiment_metadata: dict[str, Any] | None = None
    """Metadata associated with the specific experiment represented by this report."""
    trace_id: str | None = None
    """The trace ID of the evaluation."""
    span_id: str | None = None
    """The span ID of the evaluation."""

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

    def averages(self) -> ReportCaseAggregate | None:
        groups = self.case_groups()
        if groups is not None:
            non_empty_summaries = [g.summary for g in groups if g.runs]
            return ReportCaseAggregate.average_from_aggregates(non_empty_summaries) if non_empty_summaries else None
        elif self.cases:
            return ReportCaseAggregate.average(self.cases)
        return None

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

    # TODO(DavidM): in v2, change the return type here to RenderableType
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

    def _metadata_panel(
        self, baseline: EvaluationReport[InputsT, OutputT, MetadataT] | None = None
    ) -> RenderableType | None:
        """Wrap a table with an experiment metadata panel if metadata exists.

        Args:
            table: The table to wrap
            baseline: Optional baseline report for diff metadata

        Returns:
            Either the table unchanged or a Group with Panel and Table
        """
        if baseline is None:
            # Single report - show metadata if present
            if self.experiment_metadata:
                metadata_text = Text()
                items = list(self.experiment_metadata.items())
                for i, (key, value) in enumerate(items):
                    metadata_text.append(f'{key}: {value}', style='dim')
                    if i < len(items) - 1:
                        metadata_text.append('\n')
                return Panel(
                    metadata_text,
                    title=f'Evaluation Summary: {self.name}',
                    title_align='left',
                    border_style='dim',
                    padding=(0, 1),
                    expand=False,
                )
        else:
            # Diff report - show metadata diff if either has metadata
            if self.experiment_metadata or baseline.experiment_metadata:
                diff_name = baseline.name if baseline.name == self.name else f'{baseline.name} → {self.name}'
                metadata_text = Text()
                lines_styles: list[tuple[str, str]] = []
                if baseline.experiment_metadata and self.experiment_metadata:
                    # Collect all keys from both
                    all_keys = sorted(set(baseline.experiment_metadata.keys()) | set(self.experiment_metadata.keys()))
                    for key in all_keys:
                        baseline_val = baseline.experiment_metadata.get(key)
                        report_val = self.experiment_metadata.get(key)
                        if baseline_val == report_val:
                            lines_styles.append((f'{key}: {report_val}', 'dim'))
                        elif baseline_val is None:
                            lines_styles.append((f'+ {key}: {report_val}', 'green'))
                        elif report_val is None:
                            lines_styles.append((f'- {key}: {baseline_val}', 'red'))
                        else:
                            lines_styles.append((f'{key}: {baseline_val} → {report_val}', 'yellow'))
                elif self.experiment_metadata:
                    lines_styles = [(f'+ {k}: {v}', 'green') for k, v in self.experiment_metadata.items()]
                else:  # baseline.experiment_metadata only
                    assert baseline.experiment_metadata is not None
                    lines_styles = [(f'- {k}: {v}', 'red') for k, v in baseline.experiment_metadata.items()]

                for i, (line, style) in enumerate(lines_styles):
                    metadata_text.append(line, style=style)
                    if i < len(lines_styles) - 1:
                        metadata_text.append('\n')

                return Panel(
                    metadata_text,
                    title=f'Evaluation Diff: {diff_name}',
                    title_align='left',
                    border_style='dim',
                    padding=(0, 1),
                    expand=False,
                )

        return None

    # TODO(DavidM): in v2, change the return type here to RenderableType
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

    def __str__(self) -> str:  # pragma: lax no cover
        """Return a string representation of the report."""
        return self.render()

```

---|---
####  name `instance-attribute`
```
name:

```

The name of the report.
####  cases `instance-attribute`
```
cases: [ReportCase[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.ReportCase "ReportCase



      dataclass
   \(pydantic_evals.reporting.ReportCase\)")[InputsT, OutputT, MetadataT]]

```

The cases in the report.
####  failures `class-attribute` `instance-attribute`
```
failures: [
    ReportCaseFailure[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.ReportCaseFailure "ReportCaseFailure



      dataclass
   \(pydantic_evals.reporting.ReportCaseFailure\)")[InputsT, OutputT, MetadataT]
] = (
    default_factory=[
        ReportCaseFailure[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.ReportCaseFailure "ReportCaseFailure



      dataclass
   \(pydantic_evals.reporting.ReportCaseFailure\)")[InputsT, OutputT, MetadataT]
    ]
)

```

The failures in the report. These are cases where task execution raised an exception.
####  analyses `class-attribute` `instance-attribute`
```
analyses: [ReportAnalysis[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.ReportAnalysis "ReportAnalysis



      module-attribute
   \(pydantic_evals.reporting.analyses.ReportAnalysis\)")] = (
    default_factory=[ReportAnalysis[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.ReportAnalysis "ReportAnalysis



      module-attribute
   \(pydantic_evals.reporting.analyses.ReportAnalysis\)")]
)

```

Experiment-wide analyses produced by report evaluators.
####  report_evaluator_failures `class-attribute` `instance-attribute`
```
report_evaluator_failures: [EvaluatorFailure[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.EvaluatorFailure "EvaluatorFailure
