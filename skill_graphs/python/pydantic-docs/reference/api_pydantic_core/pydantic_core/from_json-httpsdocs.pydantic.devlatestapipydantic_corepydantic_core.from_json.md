##  from_json [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.from_json)
```
from_json(
    data:  |  | ,
    *,
    allow_inf_nan:  = True,
    cache_strings: (
         | ["all", "keys", "none"]
    ) = True,
    allow_partial: (
         | ["off", "on", "trailing-strings"]
    ) = False
) ->

```

Deserialize JSON data to a Python object.
This is effectively a faster version of `json.loads()`, with some extra functionality.
Parameters:
Name | Type | Description | Default
---|---|---|---
`data` |  |  The JSON data to deserialize. |  _required_
`allow_inf_nan` |  |  Whether to allow `Infinity`, `-Infinity` and `NaN` values as `json.loads()` does by default. |  `True`
`cache_strings` |  |  Whether to cache strings to avoid constructing new Python objects, this should have a significant impact on performance while increasing memory usage slightly, `all/True` means cache all strings, `keys` means cache only dict keys, `none/False` means no caching. |  `True`
`allow_partial` |  |  Whether to allow partial deserialization, if `True` JSON data is returned if the end of the input is reached before the full object is deserialized, e.g. `["aa", "bb", "c` would return `['aa', 'bb']`. `'trailing-strings'` means any final unfinished JSON string is included in the result. |  `False`
Raises:
Type | Description
---|---
|  If deserialization fails.
Returns:
Type | Description
---|---
|  The deserialized Python object.
