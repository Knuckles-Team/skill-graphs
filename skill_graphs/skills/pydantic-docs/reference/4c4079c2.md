##  SettingsConfigDict [¶](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.SettingsConfigDict)
Bases: `ConfigDict[](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict)`
###  pyproject_toml_depth `instance-attribute` [¶](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.SettingsConfigDict.pyproject_toml_depth)
```
pyproject_toml_depth:

```

Number of levels **up** from the current working directory to attempt to find a pyproject.toml file.
This is only used when a pyproject.toml file is not found in the current working directory.
###  pyproject_toml_table_header `instance-attribute` [¶](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.SettingsConfigDict.pyproject_toml_table_header)
```
pyproject_toml_table_header: [, ...]

```

Header of the TOML table within a pyproject.toml file to use when filling variables. This is supplied as a `tuple[str, ...]` instead of a `str` to accommodate for headers containing a `.`.
For example, `toml_table_header = ("tool", "my.tool", "foo")` can be used to fill variable values from a table with header `[tool."my.tool".foo]`.
To use the root table, exclude this config setting or provide an empty tuple.
