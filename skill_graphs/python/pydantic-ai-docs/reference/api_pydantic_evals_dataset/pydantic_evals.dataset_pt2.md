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

    @classmethod
    @functools.cache
    def _params(cls) -> tuple[type[InputsT], type[OutputT], type[MetadataT]]:
        """Get the type parameters for the Dataset class.

        Returns:
            A tuple of (InputsT, OutputT, MetadataT) types.
        """
        for c in cls.__mro__:
            metadata = getattr(c, '__pydantic_generic_metadata__', {})
            if len(args := (metadata.get('args', ()) or getattr(c, '__args__', ()))) == 3:  # pragma: no branch
                return args
        else:  # pragma: no cover
            warnings.warn(
                f'Could not determine the generic parameters for {cls}; using `Any` for each.'
                f' You should explicitly set the generic parameters via `Dataset[MyInputs, MyOutput, MyMetadata]`'
                f' when serializing or deserializing.',
                UserWarning,
            )
            return Any, Any, Any  # type: ignore

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

    @classmethod
    def _from_dataset_model(
        cls,
        dataset_model: _DatasetModel[InputsT, OutputT, MetadataT],
        custom_evaluator_types: Sequence[type[Evaluator[InputsT, OutputT, MetadataT]]] = (),
        custom_report_evaluator_types: Sequence[type[ReportEvaluator[InputsT, OutputT, MetadataT]]] = (),
        default_name: str | None = None,
    ) -> Self:
        """Create a Dataset from a _DatasetModel.

        Args:
            dataset_model: The _DatasetModel to convert.
            custom_evaluator_types: Custom evaluator classes to register for deserialization.
            custom_report_evaluator_types: Custom report evaluator classes to register for deserialization.
            default_name: Default name of the dataset, to be used if the value is `None` in the provided model.

        Returns:
            A new Dataset instance created from the _DatasetModel.
        """
        registry = _get_evaluator_registry(custom_evaluator_types, Evaluator, DEFAULT_EVALUATORS, 'evaluator')
        report_evaluator_registry = _get_evaluator_registry(
            custom_report_evaluator_types, ReportEvaluator, DEFAULT_REPORT_EVALUATORS, 'report evaluator'
        )

        cases: list[Case[InputsT, OutputT, MetadataT]] = []
        errors: list[ValueError] = []
        dataset_evaluators: list[Evaluator] = []
        for spec in dataset_model.evaluators:
            try:
                dataset_evaluator = _load_evaluator_from_registry(
                    registry, spec, 'evaluator', 'custom_evaluator_types', context='dataset'
                )
            except ValueError as e:
                errors.append(e)
                continue
            dataset_evaluators.append(dataset_evaluator)

        report_evaluators: list[ReportEvaluator] = []
        for spec in dataset_model.report_evaluators:
            try:
                report_evaluator = _load_evaluator_from_registry(
                    report_evaluator_registry,
                    spec,
                    'report evaluator',
                    'custom_report_evaluator_types',
                    context='dataset',
                )
            except ValueError as e:
                errors.append(e)
                continue
            report_evaluators.append(report_evaluator)

        for row in dataset_model.cases:
            evaluators: list[Evaluator] = []
            for spec in row.evaluators:
                try:
                    evaluator = _load_evaluator_from_registry(
                        registry, spec, 'evaluator', 'custom_evaluator_types', context=f'case {row.name!r}'
                    )
                except ValueError as e:
                    errors.append(e)
                    continue
                evaluators.append(evaluator)
            row = Case[InputsT, OutputT, MetadataT](
                name=row.name,
                inputs=row.inputs,
                metadata=row.metadata,
                expected_output=row.expected_output,
            )
            row.evaluators = evaluators
            cases.append(row)
        if errors:
            raise ExceptionGroup(f'{len(errors)} error(s) loading evaluators from registry', errors[:3])
        result = cls(name=dataset_model.name, cases=cases, report_evaluators=report_evaluators)
        if result.name is None:
            result.name = default_name
        result.evaluators = dataset_evaluators
        return result

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

    @classmethod
    def _save_schema(
        cls,
        path: Path | str,
        custom_evaluator_types: Sequence[type[Evaluator[InputsT, OutputT, MetadataT]]] = (),
        custom_report_evaluator_types: Sequence[type[ReportEvaluator[InputsT, OutputT, MetadataT]]] = (),
    ):
        """Save the JSON schema for this dataset type to a file.

        Args:
            path: Path to save the schema to.
            custom_evaluator_types: Custom evaluator classes to include in the schema.
            custom_report_evaluator_types: Custom report evaluator classes to include in the schema.
        """
        path = Path(path)
        json_schema = cls.model_json_schema_with_evaluators(custom_evaluator_types, custom_report_evaluator_types)
        schema_content = to_json(json_schema, indent=2).decode() + '\n'
        if not path.exists() or path.read_text(encoding='utf-8') != schema_content:  # pragma: no branch
            path.write_text(schema_content, encoding='utf-8')

    @classmethod
    @functools.cache
    def _serialization_type(cls) -> type[_DatasetModel[InputsT, OutputT, MetadataT]]:
        """Get the serialization type for this dataset class.

        Returns:
            A _DatasetModel type with the same generic parameters as this Dataset class.
        """
        input_type, output_type, metadata_type = cls._params()
        return _DatasetModel[input_type, output_type, metadata_type]

    @classmethod
    def _infer_fmt(cls, path: Path, fmt: Literal['yaml', 'json'] | None) -> Literal['yaml', 'json']:
        """Infer the format to use for a file based on its extension.

        Args:
            path: The path to infer the format for.
            fmt: The explicitly provided format, if any.

        Returns:
            The inferred format ('yaml' or 'json').

        Raises:
            ValueError: If the format cannot be inferred from the file extension.
        """
        if fmt is not None:
            return fmt
        suffix = path.suffix.lower()
        if suffix in {'.yaml', '.yml'}:
            return 'yaml'
        elif suffix == '.json':
            return 'json'
        raise ValueError(
            f'Could not infer format for filename {path.name!r}. Use the `fmt` argument to specify the format.'
        )

    @model_serializer(mode='wrap')
    def _add_json_schema(self, nxt: SerializerFunctionWrapHandler, info: SerializationInfo) -> dict[str, Any]:
        """Add the JSON schema path to the serialized output.

        See <https://github.com/json-schema-org/json-schema-spec/issues/828> for context, that seems to be the nearest
        there is to a spec for this.
        """
        context = cast(dict[str, Any] | None, info.context)
        if isinstance(context, dict) and (schema := context.get('$schema')):
            return {'$schema': schema} | nxt(self)
        else:
            return nxt(self)

```

---|---
####  name `class-attribute` `instance-attribute`
```
name:  | None = None

```

Optional name of the dataset.
####  cases `instance-attribute`
```
cases: [Case[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.Case "Case



      dataclass
   \(pydantic_evals.dataset.Case\)")[InputsT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.InputsT "InputsT



      module-attribute
   \(pydantic_evals.dataset.InputsT\)"), OutputT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.OutputT "OutputT



      module-attribute
   \(pydantic_evals.dataset.OutputT\)"), MetadataT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.MetadataT "MetadataT



      module-attribute
   \(pydantic_evals.dataset.MetadataT\)")]]

```

List of test cases in the dataset.
####  evaluators `class-attribute` `instance-attribute`
```
evaluators: [Evaluator[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.Evaluator "Evaluator



      dataclass
   \(pydantic_evals.evaluators.Evaluator\)")[InputsT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.InputsT "InputsT



      module-attribute
   \(pydantic_evals.dataset.InputsT\)"), OutputT[](https://ai.pydantic.dev/api/pydantic_evals/dataset/#pydantic_evals.dataset.OutputT "OutputT
