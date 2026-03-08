        repeat: Number of times to run each case. When > 1, each case is run multiple times and
            results are grouped by the original case name for aggregation. Defaults to 1.

    Returns:
        A report containing the results of the evaluation.
    """
    return get_event_loop().run_until_complete(
        self.evaluate(
            task,
            name=name,
            max_concurrency=max_concurrency,
            progress=progress,
            retry_task=retry_task,
            retry_evaluators=retry_evaluators,
            task_name=task_name,
            metadata=metadata,
            repeat=repeat,
        )
    )

```

---|---
####  add_case
```
add_case(
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
) -> None

```

Adds a case to the dataset.
This is a convenience method for creating a [`Case`](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.Case "Case



      dataclass
  ") and adding it to the dataset.
Parameters:
Name | Type | Description | Default
---|---|---|---
`name` |  |  Optional name for the case. If not provided, a generic name will be assigned. |  `None`
`inputs` |  `InputsT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.InputsT "InputsT



      module-attribute
   \(pydantic_evals.dataset.InputsT\)")` |  The inputs to the task being evaluated. |  _required_
`metadata` |  `MetadataT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.MetadataT "MetadataT



      module-attribute
   \(pydantic_evals.dataset.MetadataT\)") | None` |  Optional metadata for the case, which can be used by evaluators. |  `None`
`expected_output` |  `OutputT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.OutputT "OutputT



      module-attribute
   \(pydantic_evals.dataset.OutputT\)") | None` |  The expected output of the task, used for comparison in evaluators. |  `None`
`evaluators` |  `Evaluator[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.Evaluator "Evaluator



      dataclass
   \(pydantic_evals.evaluators.Evaluator\)")[InputsT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.InputsT "InputsT



      module-attribute
   \(pydantic_evals.dataset.InputsT\)"), OutputT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.OutputT "OutputT



      module-attribute
   \(pydantic_evals.dataset.OutputT\)"), MetadataT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.MetadataT "MetadataT



      module-attribute
   \(pydantic_evals.dataset.MetadataT\)")], ...]` |  Tuple of evaluators specific to this case, in addition to dataset-level evaluators. |  `()`
Source code in `pydantic_evals/pydantic_evals/dataset.py`
```
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
```
| ```
def add_case(
    self,
    *,
    name: str | None = None,
    inputs: InputsT,
    metadata: MetadataT | None = None,
    expected_output: OutputT | None = None,
    evaluators: tuple[Evaluator[InputsT, OutputT, MetadataT], ...] = (),
) -> None:
    """Adds a case to the dataset.

    This is a convenience method for creating a [`Case`][pydantic_evals.Case] and adding it to the dataset.

    Args:
        name: Optional name for the case. If not provided, a generic name will be assigned.
        inputs: The inputs to the task being evaluated.
        metadata: Optional metadata for the case, which can be used by evaluators.
        expected_output: The expected output of the task, used for comparison in evaluators.
        evaluators: Tuple of evaluators specific to this case, in addition to dataset-level evaluators.
    """
    if name in {case.name for case in self.cases}:
        raise ValueError(f'Duplicate case name: {name!r}')

    case = Case[InputsT, OutputT, MetadataT](
        name=name,
        inputs=inputs,
        metadata=metadata,
        expected_output=expected_output,
        evaluators=evaluators,
    )
    self.cases.append(case)

```

---|---
####  add_evaluator
```
add_evaluator(
    evaluator: Evaluator[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.Evaluator "Evaluator



      dataclass
   \(pydantic_evals.evaluators.Evaluator\)")[InputsT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.InputsT "InputsT



      module-attribute
   \(pydantic_evals.dataset.InputsT\)"), OutputT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.OutputT "OutputT



      module-attribute
   \(pydantic_evals.dataset.OutputT\)"), MetadataT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.MetadataT "MetadataT



      module-attribute
   \(pydantic_evals.dataset.MetadataT\)")],
    specific_case:  | None = None,
) -> None

```

Adds an evaluator to the dataset or a specific case.
Parameters:
Name | Type | Description | Default
---|---|---|---
`evaluator` |  `Evaluator[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.Evaluator "Evaluator



      dataclass
   \(pydantic_evals.evaluators.Evaluator\)")[InputsT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.InputsT "InputsT



      module-attribute
   \(pydantic_evals.dataset.InputsT\)"), OutputT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.OutputT "OutputT



      module-attribute
   \(pydantic_evals.dataset.OutputT\)"), MetadataT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.MetadataT "MetadataT



      module-attribute
   \(pydantic_evals.dataset.MetadataT\)")]` |  The evaluator to add. |  _required_
`specific_case` |  |  If provided, the evaluator will only be added to the case with this name. If None, the evaluator will be added to all cases in the dataset. |  `None`
Raises:
Type | Description
---|---
|  If `specific_case` is provided but no case with that name exists in the dataset.
Source code in `pydantic_evals/pydantic_evals/dataset.py`
```
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
```
| ```
def add_evaluator(
    self,
    evaluator: Evaluator[InputsT, OutputT, MetadataT],
    specific_case: str | None = None,
) -> None:
    """Adds an evaluator to the dataset or a specific case.

    Args:
        evaluator: The evaluator to add.
        specific_case: If provided, the evaluator will only be added to the case with this name.
            If None, the evaluator will be added to all cases in the dataset.

    Raises:
        ValueError: If `specific_case` is provided but no case with that name exists in the dataset.
    """
    if specific_case is None:
        self.evaluators.append(evaluator)
    else:
        # If this is too slow, we could try to add a case lookup dict.
        # Note that if we do that, we'd need to make the cases list private to prevent modification.
        added = False
        for case in self.cases:
            if case.name == specific_case:
                case.evaluators.append(evaluator)
                added = True
        if not added:
            raise ValueError(f'Case {specific_case!r} not found in the dataset')

```

---|---
####  from_file `classmethod`
```
from_file(
    path:  | ,
    fmt: ["yaml", "json"] | None = None,
    custom_evaluator_types: [
        [Evaluator[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.Evaluator "Evaluator



      dataclass
   \(pydantic_evals.evaluators.Evaluator\)")[InputsT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.InputsT "InputsT



      module-attribute
   \(pydantic_evals.dataset.InputsT\)"), OutputT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.OutputT "OutputT



      module-attribute
   \(pydantic_evals.dataset.OutputT\)"), MetadataT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.MetadataT "MetadataT



      module-attribute
   \(pydantic_evals.dataset.MetadataT\)")]]
    ] = (),
    custom_report_evaluator_types: [
        [ReportEvaluator[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.ReportEvaluator "ReportEvaluator



      dataclass
   \(pydantic_evals.evaluators.report_evaluator.ReportEvaluator\)")[InputsT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.InputsT "InputsT



      module-attribute
   \(pydantic_evals.dataset.InputsT\)"), OutputT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.OutputT "OutputT



      module-attribute
   \(pydantic_evals.dataset.OutputT\)"), MetadataT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.MetadataT "MetadataT



      module-attribute
   \(pydantic_evals.dataset.MetadataT\)")]]
    ] = (),
) ->

```

Load a dataset from a file.
Parameters:
Name | Type | Description | Default
---|---|---|---
`path` |  |  Path to the file to load. |  _required_
`fmt` |  |  Format of the file. If None, the format will be inferred from the file extension. Must be either 'yaml' or 'json'. |  `None`
`custom_evaluator_types` |  `Evaluator[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.Evaluator "Evaluator



      dataclass
   \(pydantic_evals.evaluators.Evaluator\)")[InputsT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.InputsT "InputsT



      module-attribute
   \(pydantic_evals.dataset.InputsT\)"), OutputT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.OutputT "OutputT



      module-attribute
   \(pydantic_evals.dataset.OutputT\)"), MetadataT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.MetadataT "MetadataT



      module-attribute
   \(pydantic_evals.dataset.MetadataT\)")]]]` |  Custom evaluator classes to use when deserializing the dataset. These are additional evaluators beyond the default ones. |  `()`
`custom_report_evaluator_types` |  `ReportEvaluator[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.ReportEvaluator "ReportEvaluator



      dataclass
   \(pydantic_evals.evaluators.report_evaluator.ReportEvaluator\)")[InputsT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.InputsT "InputsT



      module-attribute
   \(pydantic_evals.dataset.InputsT\)"), OutputT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.OutputT "OutputT



      module-attribute
   \(pydantic_evals.dataset.OutputT\)"), MetadataT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.MetadataT "MetadataT



      module-attribute
   \(pydantic_evals.dataset.MetadataT\)")]]]` |  Custom report evaluator classes to use when deserializing the dataset. These are additional report evaluators beyond the default ones. |  `()`
Returns:
Type | Description
---|---
|  A new Dataset instance loaded from the file.
Raises:
Type | Description
---|---
`ValidationError` |  If the file cannot be parsed as a valid dataset.
|  If the format cannot be inferred from the file extension.
Source code in `pydantic_evals/pydantic_evals/dataset.py`
```
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
```
| ```
@classmethod
def from_file(
    cls,
    path: Path | str,
    fmt: Literal['yaml', 'json'] | None = None,
    custom_evaluator_types: Sequence[type[Evaluator[InputsT, OutputT, MetadataT]]] = (),
    custom_report_evaluator_types: Sequence[type[ReportEvaluator[InputsT, OutputT, MetadataT]]] = (),
) -> Self:
    """Load a dataset from a file.

    Args:
        path: Path to the file to load.
        fmt: Format of the file. If None, the format will be inferred from the file extension.
            Must be either 'yaml' or 'json'.
        custom_evaluator_types: Custom evaluator classes to use when deserializing the dataset.
            These are additional evaluators beyond the default ones.
        custom_report_evaluator_types: Custom report evaluator classes to use when deserializing the dataset.
            These are additional report evaluators beyond the default ones.

    Returns:
        A new Dataset instance loaded from the file.

    Raises:
        ValidationError: If the file cannot be parsed as a valid dataset.
        ValueError: If the format cannot be inferred from the file extension.
    """
    path = Path(path)
    fmt = cls._infer_fmt(path, fmt)

    raw = Path(path).read_text(encoding='utf-8')
    try:
        return cls.from_text(
            raw,
            fmt=fmt,
            custom_evaluator_types=custom_evaluator_types,
            custom_report_evaluator_types=custom_report_evaluator_types,
            default_name=path.stem,
        )
    except ValidationError as e:  # pragma: no cover
        raise ValueError(f'{path} contains data that does not match the schema for {cls.__name__}:\n{e}.') from e

```

---|---
####  from_text `classmethod`
```
from_text(
    contents: ,
    fmt: ["yaml", "json"] = "yaml",
    custom_evaluator_types: [
        [Evaluator[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.Evaluator "Evaluator



      dataclass
   \(pydantic_evals.evaluators.Evaluator\)")[InputsT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.InputsT "InputsT



      module-attribute
   \(pydantic_evals.dataset.InputsT\)"), OutputT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.OutputT "OutputT



      module-attribute
   \(pydantic_evals.dataset.OutputT\)"), MetadataT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.MetadataT "MetadataT



      module-attribute
   \(pydantic_evals.dataset.MetadataT\)")]]
    ] = (),
    custom_report_evaluator_types: [
        [ReportEvaluator[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.ReportEvaluator "ReportEvaluator



      dataclass
   \(pydantic_evals.evaluators.report_evaluator.ReportEvaluator\)")[InputsT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.InputsT "InputsT



      module-attribute
   \(pydantic_evals.dataset.InputsT\)"), OutputT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.OutputT "OutputT



      module-attribute
   \(pydantic_evals.dataset.OutputT\)"), MetadataT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.MetadataT "MetadataT



      module-attribute
   \(pydantic_evals.dataset.MetadataT\)")]]
    ] = (),
    *,
    default_name:  | None = None
) ->

```

Load a dataset from a string.
Parameters:
Name | Type | Description | Default
---|---|---|---
`contents` |  |  The string content to parse. |  _required_
`fmt` |  |  Format of the content. Must be either 'yaml' or 'json'. |  `'yaml'`
`custom_evaluator_types` |  `Evaluator[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.Evaluator "Evaluator



      dataclass
   \(pydantic_evals.evaluators.Evaluator\)")[InputsT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.InputsT "InputsT



      module-attribute
   \(pydantic_evals.dataset.InputsT\)"), OutputT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.OutputT "OutputT



      module-attribute
   \(pydantic_evals.dataset.OutputT\)"), MetadataT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.MetadataT "MetadataT



      module-attribute
   \(pydantic_evals.dataset.MetadataT\)")]]]` |  Custom evaluator classes to use when deserializing the dataset. These are additional evaluators beyond the default ones. |  `()`
`custom_report_evaluator_types` |  `ReportEvaluator[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.ReportEvaluator "ReportEvaluator



      dataclass
   \(pydantic_evals.evaluators.report_evaluator.ReportEvaluator\)")[InputsT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.InputsT "InputsT



      module-attribute
   \(pydantic_evals.dataset.InputsT\)"), OutputT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.OutputT "OutputT



      module-attribute
   \(pydantic_evals.dataset.OutputT\)"), MetadataT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.MetadataT "MetadataT



      module-attribute
   \(pydantic_evals.dataset.MetadataT\)")]]]` |  Custom report evaluator classes to use when deserializing the dataset. These are additional report evaluators beyond the default ones. |  `()`
`default_name` |  |  Default name of the dataset, to be used if not specified in the serialized contents. |  `None`
Returns:
Type | Description
---|---
|  A new Dataset instance parsed from the string.
Raises:
Type | Description
---|---
`ValidationError` |  If the content cannot be parsed as a valid dataset.
Source code in `pydantic_evals/pydantic_evals/dataset.py`
```
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
```
| ```
@classmethod
def from_text(
    cls,
    contents: str,
    fmt: Literal['yaml', 'json'] = 'yaml',
    custom_evaluator_types: Sequence[type[Evaluator[InputsT, OutputT, MetadataT]]] = (),
    custom_report_evaluator_types: Sequence[type[ReportEvaluator[InputsT, OutputT, MetadataT]]] = (),
    *,
    default_name: str | None = None,
) -> Self:
    """Load a dataset from a string.

    Args:
        contents: The string content to parse.
        fmt: Format of the content. Must be either 'yaml' or 'json'.
        custom_evaluator_types: Custom evaluator classes to use when deserializing the dataset.
            These are additional evaluators beyond the default ones.
        custom_report_evaluator_types: Custom report evaluator classes to use when deserializing the dataset.
            These are additional report evaluators beyond the default ones.
        default_name: Default name of the dataset, to be used if not specified in the serialized contents.

    Returns:
        A new Dataset instance parsed from the string.

    Raises:
        ValidationError: If the content cannot be parsed as a valid dataset.
    """
    if fmt == 'yaml':
        loaded = yaml.safe_load(contents)
        return cls.from_dict(
            loaded, custom_evaluator_types, custom_report_evaluator_types, default_name=default_name
        )
    else:
        dataset_model_type = cls._serialization_type()
        dataset_model = dataset_model_type.model_validate_json(contents)
        return cls._from_dataset_model(
            dataset_model, custom_evaluator_types, custom_report_evaluator_types, default_name
        )

```

---|---
####  from_dict `classmethod`
```
from_dict(
    data: [, ],
    custom_evaluator_types: [
        [Evaluator[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.Evaluator "Evaluator



      dataclass
   \(pydantic_evals.evaluators.Evaluator\)")[InputsT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.InputsT "InputsT



      module-attribute
   \(pydantic_evals.dataset.InputsT\)"), OutputT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.OutputT "OutputT



      module-attribute
   \(pydantic_evals.dataset.OutputT\)"), MetadataT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.MetadataT "MetadataT



      module-attribute
   \(pydantic_evals.dataset.MetadataT\)")]]
    ] = (),
    custom_report_evaluator_types: [
        [ReportEvaluator[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.ReportEvaluator "ReportEvaluator



      dataclass
   \(pydantic_evals.evaluators.report_evaluator.ReportEvaluator\)")[InputsT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.InputsT "InputsT



      module-attribute
   \(pydantic_evals.dataset.InputsT\)"), OutputT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.OutputT "OutputT



      module-attribute
   \(pydantic_evals.dataset.OutputT\)"), MetadataT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.MetadataT "MetadataT



      module-attribute
   \(pydantic_evals.dataset.MetadataT\)")]]
    ] = (),
    *,
    default_name:  | None = None
) ->

```

Load a dataset from a dictionary.
Parameters:
Name | Type | Description | Default
---|---|---|---
`data` |  |  Dictionary representation of the dataset. |  _required_
`custom_evaluator_types` |  `Evaluator[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.Evaluator "Evaluator



      dataclass
   \(pydantic_evals.evaluators.Evaluator\)")[InputsT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.InputsT "InputsT



      module-attribute
   \(pydantic_evals.dataset.InputsT\)"), OutputT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.OutputT "OutputT



      module-attribute
   \(pydantic_evals.dataset.OutputT\)"), MetadataT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.MetadataT "MetadataT



      module-attribute
   \(pydantic_evals.dataset.MetadataT\)")]]]` |  Custom evaluator classes to use when deserializing the dataset. These are additional evaluators beyond the default ones. |  `()`
`custom_report_evaluator_types` |  `ReportEvaluator[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.ReportEvaluator "ReportEvaluator



      dataclass
   \(pydantic_evals.evaluators.report_evaluator.ReportEvaluator\)")[InputsT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.InputsT "InputsT



      module-attribute
   \(pydantic_evals.dataset.InputsT\)"), OutputT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.OutputT "OutputT



      module-attribute
   \(pydantic_evals.dataset.OutputT\)"), MetadataT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.MetadataT "MetadataT



      module-attribute
   \(pydantic_evals.dataset.MetadataT\)")]]]` |  Custom report evaluator classes to use when deserializing the dataset. These are additional report evaluators beyond the default ones. |  `()`
`default_name` |  |  Default name of the dataset, to be used if not specified in the data. |  `None`
Returns:
Type | Description
---|---
|  A new Dataset instance created from the dictionary.
Raises:
Type | Description
---|---
`ValidationError` |  If the dictionary cannot be converted to a valid dataset.
Source code in `pydantic_evals/pydantic_evals/dataset.py`
```
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
```
| ```
@classmethod
def from_dict(
    cls,
    data: dict[str, Any],
    custom_evaluator_types: Sequence[type[Evaluator[InputsT, OutputT, MetadataT]]] = (),
    custom_report_evaluator_types: Sequence[type[ReportEvaluator[InputsT, OutputT, MetadataT]]] = (),
    *,
    default_name: str | None = None,
) -> Self:
    """Load a dataset from a dictionary.

    Args:
        data: Dictionary representation of the dataset.
        custom_evaluator_types: Custom evaluator classes to use when deserializing the dataset.
            These are additional evaluators beyond the default ones.
        custom_report_evaluator_types: Custom report evaluator classes to use when deserializing the dataset.
            These are additional report evaluators beyond the default ones.
        default_name: Default name of the dataset, to be used if not specified in the data.
