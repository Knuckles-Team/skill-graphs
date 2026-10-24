##  EnvSettingsSource [¶](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.EnvSettingsSource)
```
EnvSettingsSource(
    settings_cls: [BaseSettings[](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.BaseSettings)],
    case_sensitive:  | None = None,
    env_prefix:  | None = None,
    env_nested_delimiter:  | None = None,
    env_ignore_empty:  | None = None,
    env_parse_none_str:  | None = None,
    env_parse_enums:  | None = None,
)

```

Bases: `PydanticBaseEnvSettingsSource`
Source class for loading settings values from environment variables.
Source code in `pydantic_settings/sources.py`
```
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
```
| ```
def __init__(
    self,
    settings_cls: type[BaseSettings],
    case_sensitive: bool | None = None,
    env_prefix: str | None = None,
    env_nested_delimiter: str | None = None,
    env_ignore_empty: bool | None = None,
    env_parse_none_str: str | None = None,
    env_parse_enums: bool | None = None,
) -> None:
    super().__init__(
        settings_cls, case_sensitive, env_prefix, env_ignore_empty, env_parse_none_str, env_parse_enums
    )
    self.env_nested_delimiter = (
        env_nested_delimiter if env_nested_delimiter is not None else self.config.get('env_nested_delimiter')
    )
    self.env_prefix_len = len(self.env_prefix)

    self.env_vars = self._load_env_vars()

```

---|---
###  get_field_value [¶](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.EnvSettingsSource.get_field_value)
```
get_field_value(
    field: FieldInfo[](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.FieldInfo), field_name:
) -> [, , ]

```

Gets the value for field from environment variables and a flag to determine whether value is complex.
Parameters:
Name | Type | Description | Default
---|---|---|---
`field` |  `FieldInfo[](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.FieldInfo)` |  The field. |  _required_
`field_name` |  |  The field name. |  _required_
Returns:
Type | Description
---|---
|  A tuple that contains the value (`None` if not found), key, and a flag to determine whether value is complex.
Source code in `pydantic_settings/sources.py`
```
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
```
| ```
def get_field_value(self, field: FieldInfo, field_name: str) -> tuple[Any, str, bool]:
    """
    Gets the value for field from environment variables and a flag to determine whether value is complex.

    Args:
        field: The field.
        field_name: The field name.

    Returns:
        A tuple that contains the value (`None` if not found), key, and
            a flag to determine whether value is complex.
    """

    env_val: str | None = None
    for field_key, env_name, value_is_complex in self._extract_field_info(field, field_name):
        env_val = self.env_vars.get(env_name)
        if env_val is not None:
            break

    return env_val, field_key, value_is_complex

```

---|---
###  prepare_field_value [¶](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.EnvSettingsSource.prepare_field_value)
```
prepare_field_value(
    field_name: ,
    field: FieldInfo[](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.FieldInfo),
    value: ,
    value_is_complex: ,
) ->

```

Prepare value for the field.
  * Extract value for nested field.
  * Deserialize value to python object for complex field.


Parameters:
Name | Type | Description | Default
---|---|---|---
`field` |  `FieldInfo[](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.FieldInfo)` |  The field. |  _required_
`field_name` |  |  The field name. |  _required_
Returns:
Type | Description
---|---
|  A tuple contains prepared value for the field.
Raises:
Type | Description
---|---
`ValuesError` |  When There is an error in deserializing value for complex field.
Source code in `pydantic_settings/sources.py`
```
776
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
```
| ```
def prepare_field_value(self, field_name: str, field: FieldInfo, value: Any, value_is_complex: bool) -> Any:
    """
    Prepare value for the field.

    * Extract value for nested field.
    * Deserialize value to python object for complex field.

    Args:
        field: The field.
        field_name: The field name.

    Returns:
        A tuple contains prepared value for the field.

    Raises:
        ValuesError: When There is an error in deserializing value for complex field.
    """
    is_complex, allow_parse_failure = self._field_is_complex(field)
    if self.env_parse_enums:
        enum_val = _annotation_enum_name_to_val(field.annotation, value)
        value = value if enum_val is None else enum_val

    if is_complex or value_is_complex:
        if isinstance(value, EnvNoneType):
            return value
        elif value is None:
            # field is complex but no value found so far, try explode_env_vars
            env_val_built = self.explode_env_vars(field_name, field, self.env_vars)
            if env_val_built:
                return env_val_built
        else:
            # field is complex and there's a value, decode that as JSON, then add explode_env_vars
            try:
                value = self.decode_complex_value(field_name, field, value)
            except ValueError as e:
                if not allow_parse_failure:
                    raise e

            if isinstance(value, dict):
                return deep_update(value, self.explode_env_vars(field_name, field, self.env_vars))
            else:
                return value
    elif value is not None:
        # simplest case, field is not complex, we only need to add the value if it was found
        return value

```

---|---
###  next_field [¶](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.EnvSettingsSource.next_field)
```
next_field(
    field: FieldInfo[](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.FieldInfo) |  | None,
    key: ,
    case_sensitive:  | None = None,
) -> FieldInfo[](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.FieldInfo) | None

```

Find the field in a sub model by key(env name)
By having the following models:
```
```py
class SubSubModel(BaseSettings):
    dvals: Dict

class SubModel(BaseSettings):
    vals: list[str]
    sub_sub_model: SubSubModel

class Cfg(BaseSettings):
    sub_model: SubModel
```

```

Then
next_field(sub_model, 'vals') Returns the `vals` field of `SubModel` class next_field(sub_model, 'sub_sub_model') Returns `sub_sub_model` field of `SubModel` class
Parameters:
Name | Type | Description | Default
---|---|---|---
`field` |  `FieldInfo[](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.FieldInfo) | ` |  The field. |  _required_
`key` |  |  The key (env name). |  _required_
`case_sensitive` |  |  Whether to search for key case sensitively. |  `None`
Returns:
Type | Description
---|---
`FieldInfo[](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.FieldInfo) | None` |  Field if it finds the next field otherwise `None`.
Source code in `pydantic_settings/sources.py`
```
838
839
840
841
842
843
844
845
846
847
848
849
850
851
852
853
854
855
856
857
858
859
860
861
862
863
864
865
866
867
868
869
870
871
872
873
874
875
876
877
878
879
880
881
882
883
884
885
886
887
888
889
890
```
| ```
def next_field(
    self, field: FieldInfo | Any | None, key: str, case_sensitive: bool | None = None
) -> FieldInfo | None:
    """
    Find the field in a sub model by key(env name)

    By having the following models:

    ```py
        class SubSubModel(BaseSettings):
            dvals: Dict

        class SubModel(BaseSettings):
            vals: list[str]
            sub_sub_model: SubSubModel

        class Cfg(BaseSettings):
            sub_model: SubModel
    ```

    Then:
        next_field(sub_model, 'vals') Returns the `vals` field of `SubModel` class
        next_field(sub_model, 'sub_sub_model') Returns `sub_sub_model` field of `SubModel` class

    Args:
        field: The field.
        key: The key (env name).
        case_sensitive: Whether to search for key case sensitively.

    Returns:
        Field if it finds the next field otherwise `None`.
    """
    if not field:
        return None

    annotation = field.annotation if isinstance(field, FieldInfo) else field
    if origin_is_union(get_origin(annotation)) or isinstance(annotation, WithArgsTypes):
        for type_ in get_args(annotation):
            type_has_key = self.next_field(type_, key, case_sensitive)
            if type_has_key:
                return type_has_key
    elif is_model_class(annotation) or is_pydantic_dataclass(annotation):
        fields = _get_model_fields(annotation)
        # `case_sensitive is None` is here to be compatible with the old behavior.
        # Has to be removed in V3.
        for field_name, f in fields.items():
            for _, env_name, _ in self._extract_field_info(f, field_name):
                if case_sensitive is None or case_sensitive:
                    if field_name == key or env_name == key:
                        return f
                elif field_name.lower() == key.lower() or env_name.lower() == key.lower():
                    return f
    return None

```

---|---
###  explode_env_vars [¶](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.EnvSettingsSource.explode_env_vars)
```
explode_env_vars(
    field_name: ,
    field: FieldInfo[](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.FieldInfo),
    env_vars: [,  | None],
) -> [, ]

```

Process env_vars and extract the values of keys containing env_nested_delimiter into nested dictionaries.
This is applied to a single field, hence filtering by env_var prefix.
Parameters:
Name | Type | Description | Default
---|---|---|---
`field_name` |  |  The field name. |  _required_
`field` |  `FieldInfo[](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.FieldInfo)` |  The field. |  _required_
`env_vars` |  |  Environment variables. |  _required_
Returns:
Type | Description
---|---
|  A dictionary contains extracted values from nested env values.
Source code in `pydantic_settings/sources.py`
```
892
893
894
895
896
897
898
899
900
901
902
903
904
905
906
907
908
909
910
911
912
913
914
915
916
917
918
919
920
921
922
923
924
925
926
927
928
929
930
931
932
933
934
935
936
937
938
939
940
941
942
943
944
945
```
| ```
def explode_env_vars(self, field_name: str, field: FieldInfo, env_vars: Mapping[str, str | None]) -> dict[str, Any]:
    """
    Process env_vars and extract the values of keys containing env_nested_delimiter into nested dictionaries.

    This is applied to a single field, hence filtering by env_var prefix.

    Args:
        field_name: The field name.
        field: The field.
        env_vars: Environment variables.

    Returns:
        A dictionary contains extracted values from nested env values.
    """
    is_dict = lenient_issubclass(get_origin(field.annotation), dict)

    prefixes = [
        f'{env_name}{self.env_nested_delimiter}' for _, env_name, _ in self._extract_field_info(field, field_name)
    ]
    result: dict[str, Any] = {}
    for env_name, env_val in env_vars.items():
        if not any(env_name.startswith(prefix) for prefix in prefixes):
            continue
        # we remove the prefix before splitting in case the prefix has characters in common with the delimiter
        env_name_without_prefix = env_name[self.env_prefix_len :]
        _, *keys, last_key = env_name_without_prefix.split(self.env_nested_delimiter)
        env_var = result
        target_field: FieldInfo | None = field
        for key in keys:
            target_field = self.next_field(target_field, key, self.case_sensitive)
            if isinstance(env_var, dict):
                env_var = env_var.setdefault(key, {})

        # get proper field with last_key
        target_field = self.next_field(target_field, last_key, self.case_sensitive)

        # check if env_val maps to a complex field and if so, parse the env_val
        if (target_field or is_dict) and env_val:
            if target_field:
                is_complex, allow_json_failure = self._field_is_complex(target_field)
            else:
                # nested field type is dict
                is_complex, allow_json_failure = True, True
            if is_complex:
                try:
                    env_val = self.decode_complex_value(last_key, target_field, env_val)  # type: ignore
                except ValueError as e:
                    if not allow_json_failure:
                        raise e
        if isinstance(env_var, dict):
            if last_key not in env_var or not isinstance(env_val, EnvNoneType) or env_var[last_key] == {}:
                env_var[last_key] = env_val

    return result

```

---|---
##  ForceDecode [¶](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.ForceDecode)
Annotation to force decoding of a field value.
##  InitSettingsSource [¶](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.InitSettingsSource)
```
InitSettingsSource(
    settings_cls: [BaseSettings[](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.BaseSettings)],
    init_kwargs: [, ],
    nested_model_default_partial_update:  | None = None,
)

```

Bases: `PydanticBaseSettingsSource[](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.PydanticBaseSettingsSource)`
Source class for loading values provided during settings class initialization.
Source code in `pydantic_settings/sources.py`
```
385
386
387
388
389
390
391
392
393
394
395
396
397
```
| ```
def __init__(
    self,
    settings_cls: type[BaseSettings],
    init_kwargs: dict[str, Any],
    nested_model_default_partial_update: bool | None = None,
):
    self.init_kwargs = init_kwargs
    super().__init__(settings_cls)
    self.nested_model_default_partial_update = (
        nested_model_default_partial_update
        if nested_model_default_partial_update is not None
        else self.config.get('nested_model_default_partial_update', False)
    )

```

---|---
