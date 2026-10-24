##  get_subcommand [¶](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.get_subcommand)
```
get_subcommand(
    model: PydanticModel,
    is_required:  = True,
    cli_exit_on_error:  | None = None,
) -> [PydanticModel]

```

Get the subcommand from a model.
Parameters:
Name | Type | Description | Default
---|---|---|---
`model` |  `PydanticModel` |  The model to get the subcommand from. |  _required_
`is_required` |  |  Determines whether a model must have subcommand set and raises error if not found. Defaults to `True`. |  `True`
`cli_exit_on_error` |  |  Determines whether this function exits with error if no subcommand is found. Defaults to model_config `cli_exit_on_error` value if set. Otherwise, defaults to `True`. |  `None`
Returns:
Type | Description
---|---
`PydanticModel]` |  The subcommand model if found, otherwise `None`.
Raises:
Type | Description
---|---
|  When no subcommand is found and is_required=`True` and cli_exit_on_error=`True` (the default).
`SettingsError` |  When no subcommand is found and is_required=`True` and cli_exit_on_error=`False`.
Source code in `pydantic_settings/sources.py`
```
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
```
| ```
def get_subcommand(
    model: PydanticModel, is_required: bool = True, cli_exit_on_error: bool | None = None
) -> Optional[PydanticModel]:
    """
    Get the subcommand from a model.

    Args:
        model: The model to get the subcommand from.
        is_required: Determines whether a model must have subcommand set and raises error if not
            found. Defaults to `True`.
        cli_exit_on_error: Determines whether this function exits with error if no subcommand is found.
            Defaults to model_config `cli_exit_on_error` value if set. Otherwise, defaults to `True`.

    Returns:
        The subcommand model if found, otherwise `None`.

    Raises:
        SystemExit: When no subcommand is found and is_required=`True` and cli_exit_on_error=`True`
            (the default).
        SettingsError: When no subcommand is found and is_required=`True` and
            cli_exit_on_error=`False`.
    """

    model_cls = type(model)
    if cli_exit_on_error is None and is_model_class(model_cls):
        model_default = model_cls.model_config.get('cli_exit_on_error')
        if isinstance(model_default, bool):
            cli_exit_on_error = model_default
    if cli_exit_on_error is None:
        cli_exit_on_error = True

    subcommands: list[str] = []
    for field_name, field_info in _get_model_fields(model_cls).items():
        if _CliSubCommand in field_info.metadata:
            if getattr(model, field_name) is not None:
                return getattr(model, field_name)
            subcommands.append(field_name)

    if is_required:
        error_message = (
            f'Error: CLI subcommand is required {{{", ".join(subcommands)}}}'
            if subcommands
            else 'Error: CLI subcommand is required but no subcommands were found.'
        )
        raise SystemExit(error_message) if cli_exit_on_error else SettingsError(error_message)

    return None

```

---|---
Was this page helpful?
Thanks for your feedback!
Thanks for your feedback!
Made with
