##  TomlConfigSettingsSource [¶](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.TomlConfigSettingsSource)
```
TomlConfigSettingsSource(
    settings_cls: [BaseSettings[](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.BaseSettings)],
    toml_file: PathType | None = DEFAULT_PATH,
)

```

Bases: `InitSettingsSource[](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.InitSettingsSource)`, `ConfigFileSourceMixin`
A source class that loads variables from a TOML file
Source code in `pydantic_settings/sources.py`
```
2043
2044
2045
2046
2047
2048
2049
2050
```
| ```
def __init__(
    self,
    settings_cls: type[BaseSettings],
    toml_file: PathType | None = DEFAULT_PATH,
):
    self.toml_file_path = toml_file if toml_file != DEFAULT_PATH else settings_cls.model_config.get('toml_file')
    self.toml_data = self._read_files(self.toml_file_path)
    super().__init__(settings_cls, self.toml_data)

```

---|---
##  YamlConfigSettingsSource [¶](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.YamlConfigSettingsSource)
```
YamlConfigSettingsSource(
    settings_cls: [BaseSettings[](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.BaseSettings)],
    yaml_file: PathType | None = DEFAULT_PATH,
    yaml_file_encoding:  | None = None,
)

```

Bases: `InitSettingsSource[](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.InitSettingsSource)`, `ConfigFileSourceMixin`
A source class that loads variables from a yaml file
Source code in `pydantic_settings/sources.py`
```
2114
2115
2116
2117
2118
2119
2120
2121
2122
2123
2124
2125
2126
2127
```
| ```
def __init__(
    self,
    settings_cls: type[BaseSettings],
    yaml_file: PathType | None = DEFAULT_PATH,
    yaml_file_encoding: str | None = None,
):
    self.yaml_file_path = yaml_file if yaml_file != DEFAULT_PATH else settings_cls.model_config.get('yaml_file')
    self.yaml_file_encoding = (
        yaml_file_encoding
        if yaml_file_encoding is not None
        else settings_cls.model_config.get('yaml_file_encoding')
    )
    self.yaml_data = self._read_files(self.yaml_file_path)
    super().__init__(settings_cls, self.yaml_data)

```

---|---
