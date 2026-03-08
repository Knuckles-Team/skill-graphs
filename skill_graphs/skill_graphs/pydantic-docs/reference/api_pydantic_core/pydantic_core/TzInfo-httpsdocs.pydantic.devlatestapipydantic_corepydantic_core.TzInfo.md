##  TzInfo [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.TzInfo)
```
TzInfo(seconds:  = 0.0)

```

Bases:
An `pydantic-core` implementation of the abstract
Parameters:
Name | Type | Description | Default
---|---|---|---
`seconds` |  |  The offset from UTC in seconds. Defaults to 0.0 (UTC). |  `0.0`
###  tzname [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.TzInfo.tzname)
```
tzname(dt:  | None) ->  | None

```

Return the time zone name corresponding to the _dt_ , as a string.
For more info, see
###  utcoffset [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.TzInfo.utcoffset)
```
utcoffset(dt:  | None) ->  | None

```

Return offset of local time from UTC, as a
More info can be found at
###  dst [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.TzInfo.dst)
```
dst(dt:  | None) ->  | None

```

Return the daylight saving time (DST) adjustment, as a `None` if DST information isn’t known.
More info can be found at
###  fromutc [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.TzInfo.fromutc)
```
fromutc(dt: ) ->

```

Adjust the date and time data associated datetime object _dt_ , returning an equivalent datetime in self’s local time.
More info can be found at
