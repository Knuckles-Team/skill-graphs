# `pydantic_evals.dataset`
Dataset management for pydantic evals.
This module provides functionality for creating, loading, saving, and evaluating datasets of test cases. Each case must have inputs, and can optionally have a name, expected output, metadata, and case-specific evaluators.
Datasets can be loaded from and saved to YAML or JSON files, and can be evaluated against a task function to produce an evaluation report.
###  InputsT `module-attribute`
```
InputsT = TypeVar('InputsT', default=)

```

Generic type for the inputs to the task being evaluated.
###  OutputT `module-attribute`
```
OutputT = TypeVar('OutputT', default=)

```

Generic type for the expected output of the task being evaluated.
###  MetadataT `module-attribute`
```
MetadataT = TypeVar('MetadataT', default=)

```

Generic type for the metadata associated with the task being evaluated.
###  DEFAULT_DATASET_PATH `module-attribute`
```
DEFAULT_DATASET_PATH = './test_cases.yaml'

```

Default path for saving/loading datasets.
###  DEFAULT_SCHEMA_PATH_TEMPLATE `module-attribute`
```
DEFAULT_SCHEMA_PATH_TEMPLATE = './{stem}_schema.json'

```

Default template for schema file paths, where {stem} is replaced with the dataset filename stem.
###  Case `dataclass`
Bases: `InputsT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.InputsT "InputsT



      module-attribute
   \(pydantic_evals.dataset.InputsT\)"), OutputT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.OutputT "OutputT



      module-attribute
   \(pydantic_evals.dataset.OutputT\)"), MetadataT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.MetadataT "MetadataT



      module-attribute
   \(pydantic_evals.dataset.MetadataT\)")]`
A single row of a [`Dataset`](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.Dataset "Dataset").
Each case represents a single test scenario with inputs to test. A case may optionally specify a name, expected outputs to compare against, and arbitrary metadata.
Cases can also have their own specific evaluators which are run in addition to dataset-level evaluators.
Example:
```
from pydantic_evals import Case

case = Case(
    name='Simple addition',
    inputs={'a': 1, 'b': 2},
    expected_output=3,
    metadata={'description': 'Tests basic addition'},
)

```

Source code in `pydantic_evals/pydantic_evals/dataset.py`
```
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
```
| ```
@dataclass(init=False)
class Case(Generic[InputsT, OutputT, MetadataT]):
    """A single row of a [`Dataset`][pydantic_evals.Dataset].

    Each case represents a single test scenario with inputs to test. A case may optionally specify a name, expected
    outputs to compare against, and arbitrary metadata.

    Cases can also have their own specific evaluators which are run in addition to dataset-level evaluators.

    Example:
```python
    from pydantic_evals import Case

    case = Case(
        name='Simple addition',
        inputs={'a': 1, 'b': 2},
        expected_output=3,
        metadata={'description': 'Tests basic addition'},
    )
```
    """

    name: str | None
    """Name of the case. This is used to identify the case in the report and can be used to filter cases."""
    inputs: InputsT
    """Inputs to the task. This is the input to the task that will be evaluated."""
    metadata: MetadataT | None = None
    """Metadata to be used in the evaluation.

    This can be used to provide additional information about the case to the evaluators.
    """
    expected_output: OutputT | None = None
    """Expected output of the task. This is the expected output of the task that will be evaluated."""
    evaluators: list[Evaluator[InputsT, OutputT, MetadataT]] = field(
        default_factory=list[Evaluator[InputsT, OutputT, MetadataT]]
    )
    """Evaluators to be used just on this case."""

    def __init__(
        self,
        *,
        name: str | None = None,
        inputs: InputsT,
        metadata: MetadataT | None = None,
        expected_output: OutputT | None = None,
        evaluators: tuple[Evaluator[InputsT, OutputT, MetadataT], ...] = (),
    ):
        """Initialize a new test case.

        Args:
            name: Optional name for the case. If not provided, a generic name will be assigned when added to a dataset.
            inputs: The inputs to the task being evaluated.
            metadata: Optional metadata for the case, which can be used by evaluators.
            expected_output: Optional expected output of the task, used for comparison in evaluators.
            evaluators: Tuple of evaluators specific to this case. These are in addition to any
                dataset-level evaluators.

        """
        # Note: `evaluators` must be a tuple instead of Sequence due to misbehavior with pyright's generic parameter
        # inference if it has type `Sequence`
        self.name = name
        self.inputs = inputs
        self.metadata = metadata
        self.expected_output = expected_output
        self.evaluators = list(evaluators)

```

---|---
####  __init__
```
__init__(
    *,
    name:  | None = None,
    inputs: InputsT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.InputsT "InputsT



      module-attribute
   \(pydantic_evals.dataset.InputsT\)"),
    metadata: MetadataT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.MetadataT "MetadataT



      module-attribute
   \(pydantic_evals.dataset.MetadataT\)") | None = None,
    expected_output: OutputT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.OutputT "OutputT



      module-attribute
   \(pydantic_evals.dataset.OutputT\)") | None = None,
    evaluators: [
        Evaluator[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.Evaluator "Evaluator



      dataclass
   \(pydantic_evals.evaluators.Evaluator\)")[InputsT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.InputsT "InputsT



      module-attribute
   \(pydantic_evals.dataset.InputsT\)"), OutputT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.OutputT "OutputT



      module-attribute
   \(pydantic_evals.dataset.OutputT\)"), MetadataT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.MetadataT "MetadataT



      module-attribute
   \(pydantic_evals.dataset.MetadataT\)")], ...
    ] = ()
)

```

Initialize a new test case.
Parameters:
Name | Type | Description | Default
---|---|---|---
`name` |  |  Optional name for the case. If not provided, a generic name will be assigned when added to a dataset. |  `None`
`inputs` |  `InputsT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.InputsT "InputsT



      module-attribute
   \(pydantic_evals.dataset.InputsT\)")` |  The inputs to the task being evaluated. |  _required_
`metadata` |  `MetadataT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.MetadataT "MetadataT



      module-attribute
   \(pydantic_evals.dataset.MetadataT\)") | None` |  Optional metadata for the case, which can be used by evaluators. |  `None`
`expected_output` |  `OutputT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.OutputT "OutputT



      module-attribute
   \(pydantic_evals.dataset.OutputT\)") | None` |  Optional expected output of the task, used for comparison in evaluators. |  `None`
`evaluators` |  `Evaluator[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.Evaluator "Evaluator



      dataclass
   \(pydantic_evals.evaluators.Evaluator\)")[InputsT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.InputsT "InputsT



      module-attribute
   \(pydantic_evals.dataset.InputsT\)"), OutputT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.OutputT "OutputT



      module-attribute
   \(pydantic_evals.dataset.OutputT\)"), MetadataT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.MetadataT "MetadataT



      module-attribute
   \(pydantic_evals.dataset.MetadataT\)")], ...]` |  Tuple of evaluators specific to this case. These are in addition to any dataset-level evaluators. |  `()`
Source code in `pydantic_evals/pydantic_evals/dataset.py`
```
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
```
| ```
def __init__(
    self,
    *,
    name: str | None = None,
    inputs: InputsT,
    metadata: MetadataT | None = None,
    expected_output: OutputT | None = None,
    evaluators: tuple[Evaluator[InputsT, OutputT, MetadataT], ...] = (),
):
    """Initialize a new test case.

    Args:
        name: Optional name for the case. If not provided, a generic name will be assigned when added to a dataset.
        inputs: The inputs to the task being evaluated.
        metadata: Optional metadata for the case, which can be used by evaluators.
        expected_output: Optional expected output of the task, used for comparison in evaluators.
        evaluators: Tuple of evaluators specific to this case. These are in addition to any
            dataset-level evaluators.

    """
    # Note: `evaluators` must be a tuple instead of Sequence due to misbehavior with pyright's generic parameter
    # inference if it has type `Sequence`
    self.name = name
    self.inputs = inputs
    self.metadata = metadata
    self.expected_output = expected_output
    self.evaluators = list(evaluators)

```

---|---
####  name `instance-attribute`
```
name:  | None = name

```

Name of the case. This is used to identify the case in the report and can be used to filter cases.
####  inputs `instance-attribute`
```
inputs: InputsT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.InputsT "InputsT



      module-attribute
   \(pydantic_evals.dataset.InputsT\)") = inputs

```

Inputs to the task. This is the input to the task that will be evaluated.
####  metadata `class-attribute` `instance-attribute`
```
metadata: MetadataT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.MetadataT "MetadataT



      module-attribute
   \(pydantic_evals.dataset.MetadataT\)") | None = metadata

```

Metadata to be used in the evaluation.
This can be used to provide additional information about the case to the evaluators.
####  expected_output `class-attribute` `instance-attribute`
```
expected_output: OutputT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.OutputT "OutputT



      module-attribute
   \(pydantic_evals.dataset.OutputT\)") | None = expected_output

```

Expected output of the task. This is the expected output of the task that will be evaluated.
####  evaluators `class-attribute` `instance-attribute`
```
evaluators: [Evaluator[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.Evaluator "Evaluator



      dataclass
   \(pydantic_evals.evaluators.Evaluator\)")[InputsT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.InputsT "InputsT



      module-attribute
   \(pydantic_evals.dataset.InputsT\)"), OutputT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.OutputT "OutputT



      module-attribute
   \(pydantic_evals.dataset.OutputT\)"), MetadataT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.MetadataT "MetadataT



      module-attribute
   \(pydantic_evals.dataset.MetadataT\)")]] = (
    (evaluators)
)

```

Evaluators to be used just on this case.
###  Dataset
Bases: `BaseModel[](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel "pydantic.BaseModel")`, `InputsT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.InputsT "InputsT



      module-attribute
   \(pydantic_evals.dataset.InputsT\)"), OutputT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.OutputT "OutputT



      module-attribute
   \(pydantic_evals.dataset.OutputT\)"), MetadataT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.MetadataT "MetadataT



      module-attribute
   \(pydantic_evals.dataset.MetadataT\)")]`
A dataset of test [cases](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.Case "Case



      dataclass
  ").
Datasets allow you to organize a collection of test cases and evaluate them against a task function. They can be loaded from and saved to YAML or JSON files, and can have dataset-level evaluators that apply to all cases.
Example:
```
# Create a dataset with two test cases
from dataclasses import dataclass

from pydantic_evals import Case, Dataset
from pydantic_evals.evaluators import Evaluator, EvaluatorContext


@dataclass
class ExactMatch(Evaluator):
    def evaluate(self, ctx: EvaluatorContext) -> bool:
        return ctx.output == ctx.expected_output

dataset = Dataset(
    cases=[
        Case(name='test1', inputs={'text': 'Hello'}, expected_output='HELLO'),
        Case(name='test2', inputs={'text': 'World'}, expected_output='WORLD'),
    ],
    evaluators=[ExactMatch()],
)

# Evaluate the dataset against a task function
async def uppercase(inputs: dict) -> str:
    return inputs['text'].upper()

async def main():
    report = await dataset.evaluate(uppercase)
    report.print()
'''
   Evaluation Summary: uppercase
┏━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━┓
┃ Case ID  ┃ Assertions ┃ Duration ┃
┡━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━┩
│ test1    │ ✔          │     10ms │
├──────────┼────────────┼──────────┤
│ test2    │ ✔          │     10ms │
├──────────┼────────────┼──────────┤
│ Averages │ 100.0% ✔   │     10ms │
└──────────┴────────────┴──────────┘
'''

```

Source code in `pydantic_evals/pydantic_evals/dataset.py`
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
679
680
681
682
683
684
685
686
687
688
689
690
691
692
693
694
695
696
697
698
699
700
701
702
703
704
705
706
707
708
709
710
711
712
713
714
715
716
717
718
719
720
721
722
723
724
725
726
727
728
729
730
731
732
733
734
735
736
737
738
739
740
741
742
743
744
745
746
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
806
807
808
809
810
811
812
813
814
815
816
817
818
819
820
821
822
823
824
825
826
827
828
829
830
831
832
833
834
835
836
837
838
839
840
841
842
843
844
845
846
847
848
849
850
851
852
853
854
855
856
857
858
859
860
861
862
863
864
865
866
867
868
869
870
871
872
873
874
875
876
877
878
879
880
881
882
883
884
885
886
887
888
889
890
891
892
893
894
```
| ```
class Dataset(BaseModel, Generic[InputsT, OutputT, MetadataT], extra='forbid', arbitrary_types_allowed=True):
    """A dataset of test [cases][pydantic_evals.Case].

    Datasets allow you to organize a collection of test cases and evaluate them against a task function.
    They can be loaded from and saved to YAML or JSON files, and can have dataset-level evaluators that
    apply to all cases.

    Example:
```python
    # Create a dataset with two test cases
    from dataclasses import dataclass

    from pydantic_evals import Case, Dataset
    from pydantic_evals.evaluators import Evaluator, EvaluatorContext


    @dataclass
    class ExactMatch(Evaluator):
        def evaluate(self, ctx: EvaluatorContext) -> bool:
            return ctx.output == ctx.expected_output

    dataset = Dataset(
        cases=[
            Case(name='test1', inputs={'text': 'Hello'}, expected_output='HELLO'),
            Case(name='test2', inputs={'text': 'World'}, expected_output='WORLD'),
        ],
        evaluators=[ExactMatch()],
    )

    # Evaluate the dataset against a task function
    async def uppercase(inputs: dict) -> str:
        return inputs['text'].upper()

    async def main():
        report = await dataset.evaluate(uppercase)
        report.print()
    '''
       Evaluation Summary: uppercase
    ┏━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━┓
    ┃ Case ID  ┃ Assertions ┃ Duration ┃
    ┡━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━┩
    │ test1    │ ✔          │     10ms │
    ├──────────┼────────────┼──────────┤
    │ test2    │ ✔          │     10ms │
    ├──────────┼────────────┼──────────┤
    │ Averages │ 100.0% ✔   │     10ms │
    └──────────┴────────────┴──────────┘
    '''
```
    """

    name: str | None = None
    """Optional name of the dataset."""
    cases: list[Case[InputsT, OutputT, MetadataT]]
    """List of test cases in the dataset."""
    evaluators: list[Evaluator[InputsT, OutputT, MetadataT]] = []
    """List of evaluators to be used on all cases in the dataset."""
    report_evaluators: list[ReportEvaluator[InputsT, OutputT, MetadataT]] = []
    """Evaluators that operate on the full report to produce experiment-wide analyses."""

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

    def _build_tasks_to_run(self, repeat: int) -> list[tuple[Case[InputsT, OutputT, MetadataT], str, str | None]]:
        """Build the list of (case, report_case_name, source_case_name) tuples for evaluation."""
        if repeat > 1:
            return [
                (case, f'{case_name} [{run_idx}/{repeat}]', case_name)
                for i, case in enumerate(self.cases, 1)
                for run_idx in range(1, repeat + 1)
                if (case_name := case.name or f'Case {i}')
            ]
        else:
            return [(case, case.name or f'Case {i}', None) for i, case in enumerate(self.cases, 1)]

    # TODO in v2: Make everything not required keyword-only
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
