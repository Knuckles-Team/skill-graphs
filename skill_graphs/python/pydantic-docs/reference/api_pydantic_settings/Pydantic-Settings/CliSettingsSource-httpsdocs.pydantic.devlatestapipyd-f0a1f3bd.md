##  CliSettingsSource [¶](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.CliSettingsSource)
```
CliSettingsSource(
    settings_cls: [BaseSettings[](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.BaseSettings)],
    cli_prog_name:  | None = None,
    cli_parse_args: (
         | [] | [, ...] | None
    ) = None,
    cli_parse_none_str:  | None = None,
    cli_hide_none_type:  | None = None,
    cli_avoid_json:  | None = None,
    cli_enforce_required:  | None = None,
    cli_use_class_docs_for_groups:  | None = None,
    cli_exit_on_error:  | None = None,
    cli_prefix:  | None = None,
    cli_flag_prefix_char:  | None = None,
    cli_implicit_flags:  | None = None,
    cli_ignore_unknown_args:  | None = None,
    cli_kebab_case:  | None = None,
    case_sensitive:  | None = True,
    root_parser:  = None,
    parse_args_method: [..., ] | None = None,
    add_argument_method: (
        [..., ] | None
    ) = ,
    add_argument_group_method: (
        [..., ] | None
    ) = ,
    add_parser_method: (
        [..., ] | None
    ) = add_parser,
    add_subparsers_method: (
        [..., ] | None
    ) = ,
    formatter_class:  = ,
)

```

Bases: `EnvSettingsSource[](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.EnvSettingsSource)`, `T]`
Source class for loading settings values from CLI.
Note
A `CliSettingsSource` connects with a `root_parser` object by using the parser methods to add `settings_cls` fields as command line arguments. The `CliSettingsSource` internal parser representation is based upon the `argparse` parsing library, and therefore, requires the parser methods to support the same attributes as their `argparse` library counterparts.
Parameters:
Name | Type | Description | Default
---|---|---|---
`cli_prog_name` |  |  The CLI program name to display in help text. Defaults to `None` if cli_parse_args is `None`. Otherwise, defaults to sys.argv[0]. |  `None`
`cli_parse_args` |  |  The list of CLI arguments to parse. Defaults to None. If set to `True`, defaults to sys.argv[1:]. |  `None`
`cli_parse_none_str` |  |  The CLI string value that should be parsed (e.g. "null", "void", "None", etc.) into `None` type(None). Defaults to "null" if cli_avoid_json is `False`, and "None" if cli_avoid_json is `True`. |  `None`
`cli_hide_none_type` |  |  Hide `None` values in CLI help text. Defaults to `False`. |  `None`
`cli_avoid_json` |  |  Avoid complex JSON objects in CLI help text. Defaults to `False`. |  `None`
`cli_enforce_required` |  |  Enforce required fields at the CLI. Defaults to `False`. |  `None`
`cli_use_class_docs_for_groups` |  |  Use class docstrings in CLI group help text instead of field descriptions. Defaults to `False`. |  `None`
`cli_exit_on_error` |  |  Determines whether or not the internal parser exits with error info when an error occurs. Defaults to `True`. |  `None`
`cli_prefix` |  |  Prefix for command line arguments added under the root parser. Defaults to "". |  `None`
`cli_flag_prefix_char` |  |  The flag prefix character to use for CLI optional arguments. Defaults to '-'. |  `None`
`cli_implicit_flags` |  |  Whether `bool` fields should be implicitly converted into CLI boolean flags. (e.g. --flag, --no-flag). Defaults to `False`. |  `None`
`cli_ignore_unknown_args` |  |  Whether to ignore unknown CLI args and parse only known ones. Defaults to `False`. |  `None`
`cli_kebab_case` |  |  CLI args use kebab case. Defaults to `False`. |  `None`
`case_sensitive` |  |  Whether CLI "--arg" names should be read with case-sensitivity. Defaults to `True`. Note: Case-insensitive matching is only supported on the internal root parser and does not apply to CLI subcommands. |  `True`
`root_parser` |  |  The root parser object. |  `None`
`parse_args_method` |  |  The root parser parse args method. Defaults to `argparse.ArgumentParser.parse_args`. |  `None`
`add_argument_method` |  |  The root parser add argument method. Defaults to `argparse.ArgumentParser.add_argument`. |
`add_argument_group_method` |  |  The root parser add argument group method. Defaults to `argparse.ArgumentParser.add_argument_group`. |
`add_parser_method` |  |  The root parser add new parser (sub-command) method. Defaults to `argparse._SubParsersAction.add_parser`. |  `add_parser`
`add_subparsers_method` |  |  The root parser add subparsers (sub-commands) method. Defaults to `argparse.ArgumentParser.add_subparsers`. |
`formatter_class` |  |  A class for customizing the root parser help text. Defaults to `argparse.RawDescriptionHelpFormatter`. |
Source code in `pydantic_settings/sources.py`
```
1115
1116
1117
1118
1119
1120
1121
1122
1123
1124
1125
1126
1127
1128
1129
1130
1131
1132
1133
1134
1135
1136
1137
1138
1139
1140
1141
1142
1143
1144
1145
1146
1147
1148
1149
1150
1151
1152
1153
1154
1155
1156
1157
1158
1159
1160
1161
1162
1163
1164
1165
1166
1167
1168
1169
1170
1171
1172
1173
1174
1175
1176
1177
1178
1179
1180
1181
1182
1183
1184
1185
1186
1187
1188
1189
1190
1191
1192
1193
1194
1195
1196
1197
1198
1199
1200
1201
1202
1203
1204
1205
1206
1207
1208
1209
1210
1211
1212
1213
1214
1215
1216
1217
1218
1219
1220
1221
1222
1223
1224
1225
1226
1227
1228
1229
1230
1231
1232
1233
1234
1235
1236
```
| ```
def __init__(
    self,
    settings_cls: type[BaseSettings],
    cli_prog_name: str | None = None,
    cli_parse_args: bool | list[str] | tuple[str, ...] | None = None,
    cli_parse_none_str: str | None = None,
    cli_hide_none_type: bool | None = None,
    cli_avoid_json: bool | None = None,
    cli_enforce_required: bool | None = None,
    cli_use_class_docs_for_groups: bool | None = None,
    cli_exit_on_error: bool | None = None,
    cli_prefix: str | None = None,
    cli_flag_prefix_char: str | None = None,
    cli_implicit_flags: bool | None = None,
    cli_ignore_unknown_args: bool | None = None,
    cli_kebab_case: bool | None = None,
    case_sensitive: bool | None = True,
    root_parser: Any = None,
    parse_args_method: Callable[..., Any] | None = None,
    add_argument_method: Callable[..., Any] | None = ArgumentParser.add_argument,
    add_argument_group_method: Callable[..., Any] | None = ArgumentParser.add_argument_group,
    add_parser_method: Callable[..., Any] | None = _SubParsersAction.add_parser,
    add_subparsers_method: Callable[..., Any] | None = ArgumentParser.add_subparsers,
    formatter_class: Any = RawDescriptionHelpFormatter,
) -> None:
    self.cli_prog_name = (
        cli_prog_name if cli_prog_name is not None else settings_cls.model_config.get('cli_prog_name', sys.argv[0])
    )
    self.cli_hide_none_type = (
        cli_hide_none_type
        if cli_hide_none_type is not None
        else settings_cls.model_config.get('cli_hide_none_type', False)
    )
    self.cli_avoid_json = (
        cli_avoid_json if cli_avoid_json is not None else settings_cls.model_config.get('cli_avoid_json', False)
    )
    if not cli_parse_none_str:
        cli_parse_none_str = 'None' if self.cli_avoid_json is True else 'null'
    self.cli_parse_none_str = cli_parse_none_str
    self.cli_enforce_required = (
        cli_enforce_required
        if cli_enforce_required is not None
        else settings_cls.model_config.get('cli_enforce_required', False)
    )
    self.cli_use_class_docs_for_groups = (
        cli_use_class_docs_for_groups
        if cli_use_class_docs_for_groups is not None
        else settings_cls.model_config.get('cli_use_class_docs_for_groups', False)
    )
    self.cli_exit_on_error = (
        cli_exit_on_error
        if cli_exit_on_error is not None
        else settings_cls.model_config.get('cli_exit_on_error', True)
    )
    self.cli_prefix = cli_prefix if cli_prefix is not None else settings_cls.model_config.get('cli_prefix', '')
    self.cli_flag_prefix_char = (
        cli_flag_prefix_char
        if cli_flag_prefix_char is not None
        else settings_cls.model_config.get('cli_flag_prefix_char', '-')
    )
    self._cli_flag_prefix = self.cli_flag_prefix_char * 2
    if self.cli_prefix:
        if cli_prefix.startswith('.') or cli_prefix.endswith('.') or not cli_prefix.replace('.', '').isidentifier():  # type: ignore
            raise SettingsError(f'CLI settings source prefix is invalid: {cli_prefix}')
        self.cli_prefix += '.'
    self.cli_implicit_flags = (
        cli_implicit_flags
        if cli_implicit_flags is not None
        else settings_cls.model_config.get('cli_implicit_flags', False)
    )
    self.cli_ignore_unknown_args = (
        cli_ignore_unknown_args
        if cli_ignore_unknown_args is not None
        else settings_cls.model_config.get('cli_ignore_unknown_args', False)
    )
    self.cli_kebab_case = (
        cli_kebab_case if cli_kebab_case is not None else settings_cls.model_config.get('cli_kebab_case', False)
    )

    case_sensitive = case_sensitive if case_sensitive is not None else True
    if not case_sensitive and root_parser is not None:
        raise SettingsError('Case-insensitive matching is only supported on the internal root parser')

    super().__init__(
        settings_cls,
        env_nested_delimiter='.',
        env_parse_none_str=self.cli_parse_none_str,
        env_parse_enums=True,
        env_prefix=self.cli_prefix,
        case_sensitive=case_sensitive,
    )

    root_parser = (
        _CliInternalArgParser(
            cli_exit_on_error=self.cli_exit_on_error,
            prog=self.cli_prog_name,
            description=None if settings_cls.__doc__ is None else dedent(settings_cls.__doc__),
            formatter_class=formatter_class,
            prefix_chars=self.cli_flag_prefix_char,
            allow_abbrev=False,
        )
        if root_parser is None
        else root_parser
    )
    self._connect_root_parser(
        root_parser=root_parser,
        parse_args_method=parse_args_method,
        add_argument_method=add_argument_method,
        add_argument_group_method=add_argument_group_method,
        add_parser_method=add_parser_method,
        add_subparsers_method=add_subparsers_method,
        formatter_class=formatter_class,
    )

    if cli_parse_args not in (None, False):
        if cli_parse_args is True:
            cli_parse_args = sys.argv[1:]
        elif not isinstance(cli_parse_args, (list, tuple)):
            raise SettingsError(
                f'cli_parse_args must be List[str] or Tuple[str, ...], received {type(cli_parse_args)}'
            )
        self._load_env_vars(parsed_args=self._parse_args(self.root_parser, cli_parse_args))

```

---|---
###  root_parser `property` [¶](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.CliSettingsSource.root_parser)
```
root_parser: T

```

The connected root parser instance.
##  DotEnvSettingsSource [¶](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.DotEnvSettingsSource)
```
DotEnvSettingsSource(
    settings_cls: [BaseSettings[](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.BaseSettings)],
    env_file: DotenvType | None = ENV_FILE_SENTINEL,
    env_file_encoding:  | None = None,
    case_sensitive:  | None = None,
    env_prefix:  | None = None,
    env_nested_delimiter:  | None = None,
    env_ignore_empty:  | None = None,
    env_parse_none_str:  | None = None,
    env_parse_enums:  | None = None,
)

```

Bases: `EnvSettingsSource[](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.EnvSettingsSource)`
Source class for loading settings values from env files.
Source code in `pydantic_settings/sources.py`
```
959
960
961
962
963
964
965
966
967
968
969
970
971
972
973
974
975
976
977
978
979
980
981
982
983
```
| ```
def __init__(
    self,
    settings_cls: type[BaseSettings],
    env_file: DotenvType | None = ENV_FILE_SENTINEL,
    env_file_encoding: str | None = None,
    case_sensitive: bool | None = None,
    env_prefix: str | None = None,
    env_nested_delimiter: str | None = None,
    env_ignore_empty: bool | None = None,
    env_parse_none_str: str | None = None,
    env_parse_enums: bool | None = None,
) -> None:
    self.env_file = env_file if env_file != ENV_FILE_SENTINEL else settings_cls.model_config.get('env_file')
    self.env_file_encoding = (
        env_file_encoding if env_file_encoding is not None else settings_cls.model_config.get('env_file_encoding')
    )
    super().__init__(
        settings_cls,
        case_sensitive,
        env_prefix,
        env_nested_delimiter,
        env_ignore_empty,
        env_parse_none_str,
        env_parse_enums,
    )

```

---|---
