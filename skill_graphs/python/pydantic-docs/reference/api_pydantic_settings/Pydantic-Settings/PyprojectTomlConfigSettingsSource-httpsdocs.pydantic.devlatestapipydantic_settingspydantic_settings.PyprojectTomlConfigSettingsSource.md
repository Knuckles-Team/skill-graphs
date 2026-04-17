##  PyprojectTomlConfigSettingsSource [¶](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.PyprojectTomlConfigSettingsSource)
```
PyprojectTomlConfigSettingsSource(
    settings_cls: [BaseSettings[](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.BaseSettings)],
    toml_file:  | None = None,
)

```

Bases: `TomlConfigSettingsSource[](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.TomlConfigSettingsSource)`
A source class that loads variables from a `pyproject.toml` file.
Source code in `pydantic_settings/sources.py`
```
2068
2069
2070
2071
2072
2073
2074
2075
2076
2077
2078
2079
2080
2081
2082
```
| ```
def __init__(
    self,
    settings_cls: type[BaseSettings],
    toml_file: Path | None = None,
) -> None:
    self.toml_file_path = self._pick_pyproject_toml_file(
        toml_file, settings_cls.model_config.get('pyproject_toml_depth', 0)
    )
    self.toml_table_header: tuple[str, ...] = settings_cls.model_config.get(
        'pyproject_toml_table_header', ('tool', 'pydantic-settings')
    )
    self.toml_data = self._read_files(self.toml_file_path)
    for key in self.toml_table_header:
        self.toml_data = self.toml_data.get(key, {})
    super(TomlConfigSettingsSource, self).__init__(settings_cls, self.toml_data)

```

---|---
##  SecretsSettingsSource [¶](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.SecretsSettingsSource)
```
SecretsSettingsSource(
    settings_cls: [BaseSettings[](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.BaseSettings)],
    secrets_dir: PathType | None = None,
    case_sensitive:  | None = None,
    env_prefix:  | None = None,
    env_ignore_empty:  | None = None,
    env_parse_none_str:  | None = None,
    env_parse_enums:  | None = None,
)

```

Bases: `PydanticBaseEnvSettingsSource`
Source class for loading settings values from secret files.
Source code in `pydantic_settings/sources.py`
```
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
```
| ```
def __init__(
    self,
    settings_cls: type[BaseSettings],
    secrets_dir: PathType | None = None,
    case_sensitive: bool | None = None,
    env_prefix: str | None = None,
    env_ignore_empty: bool | None = None,
    env_parse_none_str: str | None = None,
    env_parse_enums: bool | None = None,
) -> None:
    super().__init__(
        settings_cls, case_sensitive, env_prefix, env_ignore_empty, env_parse_none_str, env_parse_enums
    )
    self.secrets_dir = secrets_dir if secrets_dir is not None else self.config.get('secrets_dir')

```

---|---
###  find_case_path `classmethod` [¶](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.SecretsSettingsSource.find_case_path)
```
find_case_path(
    dir_path: , file_name: , case_sensitive:
) ->  | None

```

Find a file within path's directory matching filename, optionally ignoring case.
Parameters:
Name | Type | Description | Default
---|---|---|---
`dir_path` |  |  Directory path. |  _required_
`file_name` |  |  File name. |  _required_
`case_sensitive` |  |  Whether to search for file name case sensitively. |  _required_
Returns:
Type | Description
---|---
|  Whether file path or `None` if file does not exist in directory.
Source code in `pydantic_settings/sources.py`
```
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
```
| ```
@classmethod
def find_case_path(cls, dir_path: Path, file_name: str, case_sensitive: bool) -> Path | None:
    """
    Find a file within path's directory matching filename, optionally ignoring case.

    Args:
        dir_path: Directory path.
        file_name: File name.
        case_sensitive: Whether to search for file name case sensitively.

    Returns:
        Whether file path or `None` if file does not exist in directory.
    """
    for f in dir_path.iterdir():
        if f.name == file_name:
            return f
        elif not case_sensitive and f.name.lower() == file_name.lower():
            return f
    return None

```

---|---
###  get_field_value [¶](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.SecretsSettingsSource.get_field_value)
```
get_field_value(
    field: FieldInfo[](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.FieldInfo), field_name:
) -> [, , ]

```

Gets the value for field from secret file and a flag to determine whether value is complex.
Parameters:
Name | Type | Description | Default
---|---|---|---
`field` |  `FieldInfo[](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.FieldInfo)` |  The field. |  _required_
`field_name` |  |  The field name. |  _required_
Returns:
Type | Description
---|---
|  A tuple that contains the value (`None` if the file does not exist), key, and a flag to determine whether value is complex.
Source code in `pydantic_settings/sources.py`
```
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
```
| ```
def get_field_value(self, field: FieldInfo, field_name: str) -> tuple[Any, str, bool]:
    """
    Gets the value for field from secret file and a flag to determine whether value is complex.

    Args:
        field: The field.
        field_name: The field name.

    Returns:
        A tuple that contains the value (`None` if the file does not exist), key, and
            a flag to determine whether value is complex.
    """

    for field_key, env_name, value_is_complex in self._extract_field_info(field, field_name):
        # paths reversed to match the last-wins behaviour of `env_file`
        for secrets_path in reversed(self.secrets_paths):
            path = self.find_case_path(secrets_path, env_name, self.case_sensitive)
            if not path:
                # path does not exist, we currently don't return a warning for this
                continue

            if path.is_file():
                return path.read_text().strip(), field_key, value_is_complex
            else:
                warnings.warn(
                    f'attempted to load secret file "{path}" but found a {path_type_label(path)} instead.',
                    stacklevel=4,
                )

    return None, field_key, value_is_complex

```

---|---
