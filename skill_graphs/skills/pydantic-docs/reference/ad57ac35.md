##  CliApp [¶](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.CliApp)
A utility class for running Pydantic `BaseSettings`, `BaseModel`, or `pydantic.dataclasses.dataclass` as CLI applications.
###  run `staticmethod` [¶](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.CliApp.run)
```
run(
    model_cls: [T],
    cli_args: (
        []
        |
        |
        | [, ]
        | None
    ) = None,
    cli_settings_source: (
        CliSettingsSource[](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.CliSettingsSource)[] | None
    ) = None,
    cli_exit_on_error:  | None = None,
    cli_cmd_method_name:  = "cli_cmd",
    **model_init_data:
) -> T

```

Runs a Pydantic `BaseSettings`, `BaseModel`, or `pydantic.dataclasses.dataclass` as a CLI application. Running a model as a CLI application requires the `cli_cmd` method to be defined in the model class.
Parameters:
Name | Type | Description | Default
---|---|---|---
`model_cls` |  `T]` |  The model class to run as a CLI application. |  _required_
`cli_args` |  |  The list of CLI arguments to parse. If `cli_settings_source` is specified, this may also be a namespace or dictionary of pre-parsed CLI arguments. Defaults to `sys.argv[1:]`. |  `None`
`cli_settings_source` |  `CliSettingsSource[](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.CliSettingsSource)[` |  Override the default CLI settings source with a user defined instance. Defaults to `None`. |  `None`
`cli_exit_on_error` |  |  Determines whether this function exits on error. If model is subclass of `BaseSettings`, defaults to BaseSettings `cli_exit_on_error` value. Otherwise, defaults to `True`. |  `None`
`cli_cmd_method_name` |  |  The CLI command method name to run. Defaults to "cli_cmd". |  `'cli_cmd'`
`model_init_data` |  |  The model init data. |  `{}`
Returns:
Type | Description
---|---
`T` |  The ran instance of model.
Raises:
Type | Description
---|---
`SettingsError` |  If model_cls is not subclass of `BaseModel` or `pydantic.dataclasses.dataclass`.
`SettingsError` |  If model_cls does not have a `cli_cmd` entrypoint defined.
Source code in `pydantic_settings/main.py`
```
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
```
| ```
@staticmethod
def run(
    model_cls: type[T],
    cli_args: list[str] | Namespace | SimpleNamespace | dict[str, Any] | None = None,
    cli_settings_source: CliSettingsSource[Any] | None = None,
    cli_exit_on_error: bool | None = None,
    cli_cmd_method_name: str = 'cli_cmd',
    **model_init_data: Any,
) -> T:
    """
    Runs a Pydantic `BaseSettings`, `BaseModel`, or `pydantic.dataclasses.dataclass` as a CLI application.
    Running a model as a CLI application requires the `cli_cmd` method to be defined in the model class.

    Args:
        model_cls: The model class to run as a CLI application.
        cli_args: The list of CLI arguments to parse. If `cli_settings_source` is specified, this may
            also be a namespace or dictionary of pre-parsed CLI arguments. Defaults to `sys.argv[1:]`.
        cli_settings_source: Override the default CLI settings source with a user defined instance.
            Defaults to `None`.
        cli_exit_on_error: Determines whether this function exits on error. If model is subclass of
            `BaseSettings`, defaults to BaseSettings `cli_exit_on_error` value. Otherwise, defaults to
            `True`.
        cli_cmd_method_name: The CLI command method name to run. Defaults to "cli_cmd".
        model_init_data: The model init data.

    Returns:
        The ran instance of model.

    Raises:
        SettingsError: If model_cls is not subclass of `BaseModel` or `pydantic.dataclasses.dataclass`.
        SettingsError: If model_cls does not have a `cli_cmd` entrypoint defined.
    """

    if not (is_pydantic_dataclass(model_cls) or is_model_class(model_cls)):
        raise SettingsError(
            f'Error: {model_cls.__name__} is not subclass of BaseModel or pydantic.dataclasses.dataclass'
        )

    cli_settings = None
    cli_parse_args = True if cli_args is None else cli_args
    if cli_settings_source is not None:
        if isinstance(cli_parse_args, (Namespace, SimpleNamespace, dict)):
            cli_settings = cli_settings_source(parsed_args=cli_parse_args)
        else:
            cli_settings = cli_settings_source(args=cli_parse_args)
    elif isinstance(cli_parse_args, (Namespace, SimpleNamespace, dict)):
        raise SettingsError('Error: `cli_args` must be list[str] or None when `cli_settings_source` is not used')

    model_init_data['_cli_parse_args'] = cli_parse_args
    model_init_data['_cli_exit_on_error'] = cli_exit_on_error
    model_init_data['_cli_settings_source'] = cli_settings
    if not issubclass(model_cls, BaseSettings):

        class CliAppBaseSettings(BaseSettings, model_cls):  # type: ignore
            model_config = SettingsConfigDict(
                nested_model_default_partial_update=True,
                case_sensitive=True,
                cli_hide_none_type=True,
                cli_avoid_json=True,
                cli_enforce_required=True,
                cli_implicit_flags=True,
                cli_kebab_case=True,
            )

        model = CliAppBaseSettings(**model_init_data)
        model_init_data = {}
        for field_name, field_info in model.model_fields.items():
            model_init_data[_field_name_for_signature(field_name, field_info)] = getattr(model, field_name)

    return CliApp._run_cli_cmd(model_cls(**model_init_data), cli_cmd_method_name, is_required=False)

```

---|---
###  run_subcommand `staticmethod` [¶](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.CliApp.run_subcommand)
```
run_subcommand(
    model: PydanticModel,
    cli_exit_on_error:  | None = None,
    cli_cmd_method_name:  = "cli_cmd",
) -> PydanticModel

```

Runs the model subcommand. Running a model subcommand requires the `cli_cmd` method to be defined in the nested model subcommand class.
Parameters:
Name | Type | Description | Default
---|---|---|---
`model` |  `PydanticModel` |  The model to run the subcommand from. |  _required_
`cli_exit_on_error` |  |  Determines whether this function exits with error if no subcommand is found. Defaults to model_config `cli_exit_on_error` value if set. Otherwise, defaults to `True`. |  `None`
`cli_cmd_method_name` |  |  The CLI command method name to run. Defaults to "cli_cmd". |  `'cli_cmd'`
Returns:
Type | Description
---|---
`PydanticModel` |  The ran subcommand model.
Raises:
Type | Description
---|---
|  When no subcommand is found and cli_exit_on_error=`True` (the default).
`SettingsError` |  When no subcommand is found and cli_exit_on_error=`False`.
Source code in `pydantic_settings/main.py`
```
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
```
| ```
@staticmethod
def run_subcommand(
    model: PydanticModel, cli_exit_on_error: bool | None = None, cli_cmd_method_name: str = 'cli_cmd'
) -> PydanticModel:
    """
    Runs the model subcommand. Running a model subcommand requires the `cli_cmd` method to be defined in
    the nested model subcommand class.

    Args:
        model: The model to run the subcommand from.
        cli_exit_on_error: Determines whether this function exits with error if no subcommand is found.
            Defaults to model_config `cli_exit_on_error` value if set. Otherwise, defaults to `True`.
        cli_cmd_method_name: The CLI command method name to run. Defaults to "cli_cmd".

    Returns:
        The ran subcommand model.

    Raises:
        SystemExit: When no subcommand is found and cli_exit_on_error=`True` (the default).
        SettingsError: When no subcommand is found and cli_exit_on_error=`False`.
    """

    subcommand = get_subcommand(model, is_required=True, cli_exit_on_error=cli_exit_on_error)
    return CliApp._run_cli_cmd(subcommand, cli_cmd_method_name, is_required=True)

```

---|---
