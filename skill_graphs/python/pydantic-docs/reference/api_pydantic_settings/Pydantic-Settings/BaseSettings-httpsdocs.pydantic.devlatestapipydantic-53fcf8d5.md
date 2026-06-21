##  BaseSettings [¶](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.BaseSettings)
```
BaseSettings(
    __pydantic_self__,
    _case_sensitive:  | None = None,
    _nested_model_default_partial_update: (
         | None
    ) = None,
    _env_prefix:  | None = None,
    _env_file: DotenvType | None = ENV_FILE_SENTINEL,
    _env_file_encoding:  | None = None,
    _env_ignore_empty:  | None = None,
    _env_nested_delimiter:  | None = None,
    _env_parse_none_str:  | None = None,
    _env_parse_enums:  | None = None,
    _cli_prog_name:  | None = None,
    _cli_parse_args: (
         | [] | [, ...] | None
    ) = None,
    _cli_settings_source: (
        CliSettingsSource[](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.CliSettingsSource)[] | None
    ) = None,
    _cli_parse_none_str:  | None = None,
    _cli_hide_none_type:  | None = None,
    _cli_avoid_json:  | None = None,
    _cli_enforce_required:  | None = None,
    _cli_use_class_docs_for_groups:  | None = None,
    _cli_exit_on_error:  | None = None,
    _cli_prefix:  | None = None,
    _cli_flag_prefix_char:  | None = None,
    _cli_implicit_flags:  | None = None,
    _cli_ignore_unknown_args:  | None = None,
    _cli_kebab_case:  | None = None,
    _secrets_dir: PathType | None = None,
    **values:
)

```

Bases: `BaseModel[](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel)`
Base class for settings, allowing values to be overridden by environment variables.
This is useful in production for secrets you do not wish to save in code, it plays nicely with docker(-compose), Heroku and any 12 factor app design.
All the below attributes can be set via `model_config`.
Parameters:
Name | Type | Description | Default
---|---|---|---
`_case_sensitive` |  |  Whether environment and CLI variable names should be read with case-sensitivity. Defaults to `None`. |  `None`
`_nested_model_default_partial_update` |  |  Whether to allow partial updates on nested model default object fields. Defaults to `False`. |  `None`
`_env_prefix` |  |  Prefix for all environment variables. Defaults to `None`. |  `None`
`_env_file` |  `DotenvType | None` |  The env file(s) to load settings values from. Defaults to `Path('')`, which means that the value from `model_config['env_file']` should be used. You can also pass `None` to indicate that environment variables should not be loaded from an env file. |  `ENV_FILE_SENTINEL`
`_env_file_encoding` |  |  The env file encoding, e.g. `'latin-1'`. Defaults to `None`. |  `None`
`_env_ignore_empty` |  |  Ignore environment variables where the value is an empty string. Default to `False`. |  `None`
`_env_nested_delimiter` |  |  The nested env values delimiter. Defaults to `None`. |  `None`
`_env_parse_none_str` |  |  The env string value that should be parsed (e.g. "null", "void", "None", etc.) into `None` type(None). Defaults to `None` type(None), which means no parsing should occur. |  `None`
`_env_parse_enums` |  |  Parse enum field names to values. Defaults to `None.`, which means no parsing should occur. |  `None`
`_cli_prog_name` |  |  The CLI program name to display in help text. Defaults to `None` if _cli_parse_args is `None`. Otherwise, defaults to sys.argv[0]. |  `None`
`_cli_parse_args` |  |  The list of CLI arguments to parse. Defaults to None. If set to `True`, defaults to sys.argv[1:]. |  `None`
`_cli_settings_source` |  `CliSettingsSource[](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.CliSettingsSource)[` |  Override the default CLI settings source with a user defined instance. Defaults to None. |  `None`
`_cli_parse_none_str` |  |  The CLI string value that should be parsed (e.g. "null", "void", "None", etc.) into `None` type(None). Defaults to _env_parse_none_str value if set. Otherwise, defaults to "null" if _cli_avoid_json is `False`, and "None" if _cli_avoid_json is `True`. |  `None`
`_cli_hide_none_type` |  |  Hide `None` values in CLI help text. Defaults to `False`. |  `None`
`_cli_avoid_json` |  |  Avoid complex JSON objects in CLI help text. Defaults to `False`. |  `None`
`_cli_enforce_required` |  |  Enforce required fields at the CLI. Defaults to `False`. |  `None`
`_cli_use_class_docs_for_groups` |  |  Use class docstrings in CLI group help text instead of field descriptions. Defaults to `False`. |  `None`
`_cli_exit_on_error` |  |  Determines whether or not the internal parser exits with error info when an error occurs. Defaults to `True`. |  `None`
`_cli_prefix` |  |  The root parser command line arguments prefix. Defaults to "". |  `None`
`_cli_flag_prefix_char` |  |  The flag prefix character to use for CLI optional arguments. Defaults to '-'. |  `None`
`_cli_implicit_flags` |  |  Whether `bool` fields should be implicitly converted into CLI boolean flags. (e.g. --flag, --no-flag). Defaults to `False`. |  `None`
`_cli_ignore_unknown_args` |  |  Whether to ignore unknown CLI args and parse only known ones. Defaults to `False`. |  `None`
`_cli_kebab_case` |  |  CLI args use kebab case. Defaults to `False`. |  `None`
`_secrets_dir` |  `PathType | None` |  The secret files directory or a sequence of directories. Defaults to `None`. |  `None`
Source code in `pydantic_settings/main.py`
```
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
```
| ```
def __init__(
    __pydantic_self__,
    _case_sensitive: bool | None = None,
    _nested_model_default_partial_update: bool | None = None,
    _env_prefix: str | None = None,
    _env_file: DotenvType | None = ENV_FILE_SENTINEL,
    _env_file_encoding: str | None = None,
    _env_ignore_empty: bool | None = None,
    _env_nested_delimiter: str | None = None,
    _env_parse_none_str: str | None = None,
    _env_parse_enums: bool | None = None,
    _cli_prog_name: str | None = None,
    _cli_parse_args: bool | list[str] | tuple[str, ...] | None = None,
    _cli_settings_source: CliSettingsSource[Any] | None = None,
    _cli_parse_none_str: str | None = None,
    _cli_hide_none_type: bool | None = None,
    _cli_avoid_json: bool | None = None,
    _cli_enforce_required: bool | None = None,
    _cli_use_class_docs_for_groups: bool | None = None,
    _cli_exit_on_error: bool | None = None,
    _cli_prefix: str | None = None,
    _cli_flag_prefix_char: str | None = None,
    _cli_implicit_flags: bool | None = None,
    _cli_ignore_unknown_args: bool | None = None,
    _cli_kebab_case: bool | None = None,
    _secrets_dir: PathType | None = None,
    **values: Any,
) -> None:
    # Uses something other than `self` the first arg to allow "self" as a settable attribute
    super().__init__(
        **__pydantic_self__._settings_build_values(
            values,
            _case_sensitive=_case_sensitive,
            _nested_model_default_partial_update=_nested_model_default_partial_update,
            _env_prefix=_env_prefix,
            _env_file=_env_file,
            _env_file_encoding=_env_file_encoding,
            _env_ignore_empty=_env_ignore_empty,
            _env_nested_delimiter=_env_nested_delimiter,
            _env_parse_none_str=_env_parse_none_str,
            _env_parse_enums=_env_parse_enums,
            _cli_prog_name=_cli_prog_name,
            _cli_parse_args=_cli_parse_args,
            _cli_settings_source=_cli_settings_source,
            _cli_parse_none_str=_cli_parse_none_str,
            _cli_hide_none_type=_cli_hide_none_type,
            _cli_avoid_json=_cli_avoid_json,
            _cli_enforce_required=_cli_enforce_required,
            _cli_use_class_docs_for_groups=_cli_use_class_docs_for_groups,
            _cli_exit_on_error=_cli_exit_on_error,
            _cli_prefix=_cli_prefix,
            _cli_flag_prefix_char=_cli_flag_prefix_char,
            _cli_implicit_flags=_cli_implicit_flags,
            _cli_ignore_unknown_args=_cli_ignore_unknown_args,
            _cli_kebab_case=_cli_kebab_case,
            _secrets_dir=_secrets_dir,
        )
    )

```

---|---
###  settings_customise_sources `classmethod` [¶](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.BaseSettings.settings_customise_sources)
```
settings_customise_sources(
    settings_cls: [BaseSettings[](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.BaseSettings)],
    init_settings: PydanticBaseSettingsSource[](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.PydanticBaseSettingsSource),
    env_settings: PydanticBaseSettingsSource[](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.PydanticBaseSettingsSource),
    dotenv_settings: PydanticBaseSettingsSource[](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.PydanticBaseSettingsSource),
    file_secret_settings: PydanticBaseSettingsSource[](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.PydanticBaseSettingsSource),
) -> [PydanticBaseSettingsSource[](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.PydanticBaseSettingsSource), ...]

```

Define the sources and their order for loading the settings values.
Parameters:
Name | Type | Description | Default
---|---|---|---
`settings_cls` |  `BaseSettings[](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.BaseSettings)]` |  The Settings class. |  _required_
`init_settings` |  `PydanticBaseSettingsSource[](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.PydanticBaseSettingsSource)` |  The `InitSettingsSource` instance. |  _required_
`env_settings` |  `PydanticBaseSettingsSource[](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.PydanticBaseSettingsSource)` |  The `EnvSettingsSource` instance. |  _required_
`dotenv_settings` |  `PydanticBaseSettingsSource[](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.PydanticBaseSettingsSource)` |  The `DotEnvSettingsSource` instance. |  _required_
`file_secret_settings` |  `PydanticBaseSettingsSource[](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.PydanticBaseSettingsSource)` |  The `SecretsSettingsSource` instance. |  _required_
Returns:
Type | Description
---|---
`PydanticBaseSettingsSource[](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.PydanticBaseSettingsSource), ...]` |  A tuple containing the sources and their order for loading the settings values.
Source code in `pydantic_settings/main.py`
```
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
```
| ```
@classmethod
def settings_customise_sources(
    cls,
    settings_cls: type[BaseSettings],
    init_settings: PydanticBaseSettingsSource,
    env_settings: PydanticBaseSettingsSource,
    dotenv_settings: PydanticBaseSettingsSource,
    file_secret_settings: PydanticBaseSettingsSource,
) -> tuple[PydanticBaseSettingsSource, ...]:
    """
    Define the sources and their order for loading the settings values.

    Args:
        settings_cls: The Settings class.
        init_settings: The `InitSettingsSource` instance.
        env_settings: The `EnvSettingsSource` instance.
        dotenv_settings: The `DotEnvSettingsSource` instance.
        file_secret_settings: The `SecretsSettingsSource` instance.

    Returns:
        A tuple containing the sources and their order for loading the settings values.
    """
    return init_settings, env_settings, dotenv_settings, file_secret_settings

```

---|---
