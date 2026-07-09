
    Returns:
        A new Dataset instance created from the dictionary.

    Raises:
        ValidationError: If the dictionary cannot be converted to a valid dataset.
    """
    dataset_model_type = cls._serialization_type()
    dataset_model = dataset_model_type.model_validate(data)
    return cls._from_dataset_model(
        dataset_model, custom_evaluator_types, custom_report_evaluator_types, default_name
    )

```

---|---
####  to_file
```
to_file(
    path:  | ,
    fmt: ["yaml", "json"] | None = None,
    schema_path: (
         |  | None
    ) = DEFAULT_SCHEMA_PATH_TEMPLATE[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.DEFAULT_SCHEMA_PATH_TEMPLATE "DEFAULT_SCHEMA_PATH_TEMPLATE



      module-attribute
   \(pydantic_evals.dataset.DEFAULT_SCHEMA_PATH_TEMPLATE\)"),
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
)

```

Save the dataset to a file.
Parameters:
Name | Type | Description | Default
---|---|---|---
`path` |  |  Path to save the dataset to. |  _required_
`fmt` |  |  Format to use. If None, the format will be inferred from the file extension. Must be either 'yaml' or 'json'. |  `None`
`schema_path` |  |  Path to save the JSON schema to. If None, no schema will be saved. Can be a string template with {stem} which will be replaced with the dataset filename stem. |  `DEFAULT_SCHEMA_PATH_TEMPLATE[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.DEFAULT_SCHEMA_PATH_TEMPLATE "DEFAULT_SCHEMA_PATH_TEMPLATE



      module-attribute
   \(pydantic_evals.dataset.DEFAULT_SCHEMA_PATH_TEMPLATE\)")`
`custom_evaluator_types` |  `Evaluator[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.Evaluator "Evaluator



      dataclass
   \(pydantic_evals.evaluators.Evaluator\)")[InputsT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.InputsT "InputsT



      module-attribute
   \(pydantic_evals.dataset.InputsT\)"), OutputT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.OutputT "OutputT



      module-attribute
   \(pydantic_evals.dataset.OutputT\)"), MetadataT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.MetadataT "MetadataT



      module-attribute
   \(pydantic_evals.dataset.MetadataT\)")]]]` |  Custom evaluator classes to include in the schema. |  `()`
`custom_report_evaluator_types` |  `ReportEvaluator[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.ReportEvaluator "ReportEvaluator



      dataclass
   \(pydantic_evals.evaluators.report_evaluator.ReportEvaluator\)")[InputsT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.InputsT "InputsT



      module-attribute
   \(pydantic_evals.dataset.InputsT\)"), OutputT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.OutputT "OutputT



      module-attribute
   \(pydantic_evals.dataset.OutputT\)"), MetadataT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.MetadataT "MetadataT



      module-attribute
   \(pydantic_evals.dataset.MetadataT\)")]]]` |  Custom report evaluator classes to include in the schema. |  `()`
Source code in `pydantic_evals/pydantic_evals/dataset.py`
```
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
```
| ```
def to_file(
    self,
    path: Path | str,
    fmt: Literal['yaml', 'json'] | None = None,
    schema_path: Path | str | None = DEFAULT_SCHEMA_PATH_TEMPLATE,
    custom_evaluator_types: Sequence[type[Evaluator[InputsT, OutputT, MetadataT]]] = (),
    custom_report_evaluator_types: Sequence[type[ReportEvaluator[InputsT, OutputT, MetadataT]]] = (),
):
    """Save the dataset to a file.

    Args:
        path: Path to save the dataset to.
        fmt: Format to use. If None, the format will be inferred from the file extension.
            Must be either 'yaml' or 'json'.
        schema_path: Path to save the JSON schema to. If None, no schema will be saved.
            Can be a string template with {stem} which will be replaced with the dataset filename stem.
        custom_evaluator_types: Custom evaluator classes to include in the schema.
        custom_report_evaluator_types: Custom report evaluator classes to include in the schema.
    """
    path = Path(path)
    fmt = self._infer_fmt(path, fmt)

    schema_ref: str | None = None
    if schema_path is not None:  # pragma: no branch
        if isinstance(schema_path, str):  # pragma: no branch
            schema_path = Path(schema_path.format(stem=path.stem))

        if not schema_path.is_absolute():
            schema_ref = str(schema_path)
            schema_path = path.parent / schema_path
        elif schema_path.is_relative_to(path):  # pragma: no cover
            schema_ref = str(_get_relative_path_reference(schema_path, path))
        else:  # pragma: no cover
            schema_ref = str(schema_path)
        self._save_schema(schema_path, custom_evaluator_types, custom_report_evaluator_types)

    context: dict[str, Any] = {'use_short_form': True}
    if fmt == 'yaml':
        dumped_data = self.model_dump(mode='json', by_alias=True, context=context)
        content = yaml.dump(dumped_data, sort_keys=False)
        if schema_ref:  # pragma: no branch
            yaml_language_server_line = f'{_YAML_SCHEMA_LINE_PREFIX}{schema_ref}'
            content = f'{yaml_language_server_line}\n{content}'
        path.write_text(content, encoding='utf-8')
    else:
        context['$schema'] = schema_ref
        json_data = self.model_dump_json(indent=2, by_alias=True, context=context)
        path.write_text(json_data + '\n', encoding='utf-8')

```

---|---
####  model_json_schema_with_evaluators `classmethod`
```
model_json_schema_with_evaluators(
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
) -> [, ]

```

Generate a JSON schema for this dataset type, including evaluator details.
This is useful for generating a schema that can be used to validate YAML-format dataset files.
Parameters:
Name | Type | Description | Default
---|---|---|---
`custom_evaluator_types` |  `Evaluator[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.Evaluator "Evaluator



      dataclass
   \(pydantic_evals.evaluators.Evaluator\)")[InputsT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.InputsT "InputsT



      module-attribute
   \(pydantic_evals.dataset.InputsT\)"), OutputT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.OutputT "OutputT



      module-attribute
   \(pydantic_evals.dataset.OutputT\)"), MetadataT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.MetadataT "MetadataT



      module-attribute
   \(pydantic_evals.dataset.MetadataT\)")]]]` |  Custom evaluator classes to include in the schema. |  `()`
`custom_report_evaluator_types` |  `ReportEvaluator[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.ReportEvaluator "ReportEvaluator



      dataclass
   \(pydantic_evals.evaluators.report_evaluator.ReportEvaluator\)")[InputsT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.InputsT "InputsT



      module-attribute
   \(pydantic_evals.dataset.InputsT\)"), OutputT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.OutputT "OutputT



      module-attribute
   \(pydantic_evals.dataset.OutputT\)"), MetadataT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.MetadataT "MetadataT



      module-attribute
   \(pydantic_evals.dataset.MetadataT\)")]]]` |  Custom report evaluator classes to include in the schema. |  `()`
Returns:
Type | Description
---|---
|  A dictionary representing the JSON schema.
Source code in `pydantic_evals/pydantic_evals/dataset.py`
```
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
```
| ```
@classmethod
def model_json_schema_with_evaluators(
    cls,
    custom_evaluator_types: Sequence[type[Evaluator[InputsT, OutputT, MetadataT]]] = (),
    custom_report_evaluator_types: Sequence[type[ReportEvaluator[InputsT, OutputT, MetadataT]]] = (),
) -> dict[str, Any]:
    """Generate a JSON schema for this dataset type, including evaluator details.

    This is useful for generating a schema that can be used to validate YAML-format dataset files.

    Args:
        custom_evaluator_types: Custom evaluator classes to include in the schema.
        custom_report_evaluator_types: Custom report evaluator classes to include in the schema.

    Returns:
        A dictionary representing the JSON schema.
    """
    evaluator_schema_types = _build_evaluator_schema_types(
        _get_evaluator_registry(custom_evaluator_types, Evaluator, DEFAULT_EVALUATORS, 'evaluator')
    )
    report_evaluator_schema_types = _build_evaluator_schema_types(
        _get_evaluator_registry(
            custom_report_evaluator_types, ReportEvaluator, DEFAULT_REPORT_EVALUATORS, 'report evaluator'
        )
    )

    in_type, out_type, meta_type = cls._params()

    # Note: we shadow the `Case` and `Dataset` class names here to generate a clean JSON schema
    class Case(BaseModel, extra='forbid'):  # pyright: ignore[reportUnusedClass]  # this _is_ used below, but pyright doesn't seem to notice..
        name: str | None = None
        inputs: in_type  # pyright: ignore[reportInvalidTypeForm]
        metadata: meta_type | None = None  # pyright: ignore[reportInvalidTypeForm]
        expected_output: out_type | None = None  # pyright: ignore[reportInvalidTypeForm]
        if evaluator_schema_types:  # pragma: no branch
            evaluators: list[Union[tuple(evaluator_schema_types)]] = []  # pyright: ignore  # noqa: UP007

    class Dataset(BaseModel, extra='forbid'):
        name: str | None = None
        cases: list[Case]
        if evaluator_schema_types:  # pragma: no branch
            evaluators: list[Union[tuple(evaluator_schema_types)]] = []  # pyright: ignore  # noqa: UP007
        if report_evaluator_schema_types:  # pragma: no branch
            report_evaluators: list[Union[tuple(report_evaluator_schema_types)]] = []  # pyright: ignore  # noqa: UP007

    json_schema = Dataset.model_json_schema()
    # See `_add_json_schema` below, since `$schema` is added to the JSON, it has to be supported in the JSON
    json_schema['properties']['$schema'] = {'type': 'string'}
    return json_schema

```

---|---
###  set_eval_attribute
```
set_eval_attribute(name: , value: ) -> None

```

Set an attribute on the current task run.
Parameters:
Name | Type | Description | Default
---|---|---|---
`name` |  |  The name of the attribute. |  _required_
`value` |  |  The value of the attribute. |  _required_
Source code in `pydantic_evals/pydantic_evals/dataset.py`
```
1266
1267
1268
1269
1270
1271
1272
1273
1274
1275
```
| ```
def set_eval_attribute(name: str, value: Any) -> None:
    """Set an attribute on the current task run.

    Args:
        name: The name of the attribute.
        value: The value of the attribute.
    """
    current_case = _CURRENT_TASK_RUN.get()
    if current_case is not None:  # pragma: no branch
        current_case.record_attribute(name, value)

```

---|---
###  increment_eval_metric
```
increment_eval_metric(
    name: , amount:  |
) -> None

```

Increment a metric on the current task run.
Parameters:
Name | Type | Description | Default
---|---|---|---
`name` |  |  The name of the metric. |  _required_
`amount` |  |  The amount to increment by. |  _required_
Source code in `pydantic_evals/pydantic_evals/dataset.py`
```
1278
1279
1280
1281
1282
1283
1284
1285
1286
1287
```
| ```
def increment_eval_metric(name: str, amount: int | float) -> None:
    """Increment a metric on the current task run.

    Args:
        name: The name of the metric.
        amount: The amount to increment by.
    """
    current_case = _CURRENT_TASK_RUN.get()
    if current_case is not None:  # pragma: no branch
        current_case.increment_metric(name, amount)

```

---|---
© Pydantic Services Inc. 2024 to present
