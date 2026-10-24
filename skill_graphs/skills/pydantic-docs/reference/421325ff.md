##  JsonConfigSettingsSource [¶](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.JsonConfigSettingsSource)
```
JsonConfigSettingsSource(
    settings_cls: [BaseSettings[](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.BaseSettings)],
    json_file: PathType | None = DEFAULT_PATH,
    json_file_encoding:  | None = None,
)

```

Bases: `InitSettingsSource[](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.InitSettingsSource)`, `ConfigFileSourceMixin`
A source class that loads variables from a JSON file
Source code in `pydantic_settings/sources.py`
```
2015
2016
2017
2018
2019
2020
2021
2022
2023
2024
2025
2026
2027
2028
```
| ```
def __init__(
    self,
    settings_cls: type[BaseSettings],
    json_file: PathType | None = DEFAULT_PATH,
    json_file_encoding: str | None = None,
):
    self.json_file_path = json_file if json_file != DEFAULT_PATH else settings_cls.model_config.get('json_file')
    self.json_file_encoding = (
        json_file_encoding
        if json_file_encoding is not None
        else settings_cls.model_config.get('json_file_encoding')
    )
    self.json_data = self._read_files(self.json_file_path)
    super().__init__(settings_cls, self.json_data)

```

---|---
##  NoDecode [¶](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.NoDecode)
Annotation to prevent decoding of a field value.
##  PydanticBaseSettingsSource [¶](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.PydanticBaseSettingsSource)
```
PydanticBaseSettingsSource(
    settings_cls: [BaseSettings[](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.BaseSettings)],
)

```

Bases:
Abstract base class for settings sources, every settings source classes should inherit from it.
Source code in `pydantic_settings/sources.py`
```
236
237
238
239
240
```
| ```
def __init__(self, settings_cls: type[BaseSettings]):
    self.settings_cls = settings_cls
    self.config = settings_cls.model_config
    self._current_state: dict[str, Any] = {}
    self._settings_sources_data: dict[str, dict[str, Any]] = {}

```

---|---
###  current_state `property` [¶](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.PydanticBaseSettingsSource.current_state)
```
current_state: [, ]

```

The current state of the settings, populated by the previous settings sources.
###  settings_sources_data `property` [¶](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.PydanticBaseSettingsSource.settings_sources_data)
```
settings_sources_data: [, [, ]]

```

The state of all previous settings sources.
###  get_field_value `abstractmethod` [¶](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.PydanticBaseSettingsSource.get_field_value)
```
get_field_value(
    field: FieldInfo[](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.FieldInfo), field_name:
) -> [, , ]

```

Gets the value, the key for model creation, and a flag to determine whether value is complex.
This is an abstract method that should be overridden in every settings source classes.
Parameters:
Name | Type | Description | Default
---|---|---|---
`field` |  `FieldInfo[](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.FieldInfo)` |  The field. |  _required_
`field_name` |  |  The field name. |  _required_
Returns:
Type | Description
---|---
|  A tuple that contains the value, key and a flag to determine whether value is complex.
Source code in `pydantic_settings/sources.py`
```
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
```
| ```
@abstractmethod
def get_field_value(self, field: FieldInfo, field_name: str) -> tuple[Any, str, bool]:
    """
    Gets the value, the key for model creation, and a flag to determine whether value is complex.

    This is an abstract method that should be overridden in every settings source classes.

    Args:
        field: The field.
        field_name: The field name.

    Returns:
        A tuple that contains the value, key and a flag to determine whether value is complex.
    """
    pass

```

---|---
###  field_is_complex [¶](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.PydanticBaseSettingsSource.field_is_complex)
```
field_is_complex(field: FieldInfo[](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.FieldInfo)) ->

```

Checks whether a field is complex, in which case it will attempt to be parsed as JSON.
Parameters:
Name | Type | Description | Default
---|---|---|---
`field` |  `FieldInfo[](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.FieldInfo)` |  The field. |  _required_
Returns:
Type | Description
---|---
|  Whether the field is complex.
Source code in `pydantic_settings/sources.py`
```
286
287
288
289
290
291
292
293
294
295
296
```
| ```
def field_is_complex(self, field: FieldInfo) -> bool:
    """
    Checks whether a field is complex, in which case it will attempt to be parsed as JSON.

    Args:
        field: The field.

    Returns:
        Whether the field is complex.
    """
    return _annotation_is_complex(field.annotation, field.metadata)

```

---|---
###  prepare_field_value [¶](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.PydanticBaseSettingsSource.prepare_field_value)
```
prepare_field_value(
    field_name: ,
    field: FieldInfo[](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.FieldInfo),
    value: ,
    value_is_complex: ,
) ->

```

Prepares the value of a field.
Parameters:
Name | Type | Description | Default
---|---|---|---
`field_name` |  |  The field name. |  _required_
`field` |  `FieldInfo[](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.FieldInfo)` |  The field. |  _required_
`value` |  |  The value of the field that has to be prepared. |  _required_
`value_is_complex` |  |  A flag to determine whether value is complex. |  _required_
Returns:
Type | Description
---|---
|  The prepared value.
Source code in `pydantic_settings/sources.py`
```
298
299
300
301
302
303
304
305
306
307
308
309
310
311
312
313
```
| ```
def prepare_field_value(self, field_name: str, field: FieldInfo, value: Any, value_is_complex: bool) -> Any:
    """
    Prepares the value of a field.

    Args:
        field_name: The field name.
        field: The field.
        value: The value of the field that has to be prepared.
        value_is_complex: A flag to determine whether value is complex.

    Returns:
        The prepared value.
    """
    if value is not None and (self.field_is_complex(field) or value_is_complex):
        return self.decode_complex_value(field_name, field, value)
    return value

```

---|---
###  decode_complex_value [¶](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.PydanticBaseSettingsSource.decode_complex_value)
```
decode_complex_value(
    field_name: , field: FieldInfo[](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.FieldInfo), value:
) ->

```

Decode the value for a complex field
Parameters:
Name | Type | Description | Default
---|---|---|---
`field_name` |  |  The field name. |  _required_
`field` |  `FieldInfo[](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.FieldInfo)` |  The field. |  _required_
`value` |  |  The value of the field that has to be prepared. |  _required_
Returns:
Type | Description
---|---
|  The decoded value for further preparation
Source code in `pydantic_settings/sources.py`
```
315
316
317
318
319
320
321
322
323
324
325
326
327
328
329
330
331
332
333
```
| ```
def decode_complex_value(self, field_name: str, field: FieldInfo, value: Any) -> Any:
    """
    Decode the value for a complex field

    Args:
        field_name: The field name.
        field: The field.
        value: The value of the field that has to be prepared.

    Returns:
        The decoded value for further preparation
    """
    if field and (
        NoDecode in field.metadata
        or (self.config.get('enable_decoding') is False and ForceDecode not in field.metadata)
    ):
        return value

    return json.loads(value)

```

---|---
