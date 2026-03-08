            new_provider_name = self.provider_name if self.provider_name is not None else part.provider_name
            # Resolve callable provider_details if needed
            resolved_details = (
                self.provider_details(part.provider_details)
                if callable(self.provider_details)
                else self.provider_details
            )
            new_provider_details = {**(part.provider_details or {}), **(resolved_details or {})} or None
            return replace(
                part,
                content=new_content,
                signature=new_signature,
                provider_name=new_provider_name,
                provider_details=new_provider_details,
            )
        elif isinstance(part, ThinkingPartDelta):
            if self.content_delta is None and self.signature_delta is None:
                raise ValueError('Cannot apply ThinkingPartDelta with no content or signature')
            if self.content_delta is not None:
                part = replace(part, content_delta=(part.content_delta or '') + self.content_delta)
            if self.signature_delta is not None:
                part = replace(part, signature_delta=self.signature_delta)
            if self.provider_name is not None:
                part = replace(part, provider_name=self.provider_name)
            if self.provider_details is not None:
                if callable(self.provider_details):
                    if callable(part.provider_details):
                        existing_fn = part.provider_details
                        new_fn = self.provider_details

                        def chained_both(d: dict[str, Any] | None) -> dict[str, Any]:
                            return new_fn(existing_fn(d))

                        part = replace(part, provider_details=chained_both)
                    else:
                        part = replace(part, provider_details=self.provider_details)  # pragma: no cover
                elif callable(part.provider_details):
                    existing_fn = part.provider_details
                    new_dict = self.provider_details

                    def chained_dict(d: dict[str, Any] | None) -> dict[str, Any]:
                        return {**existing_fn(d), **new_dict}

                    part = replace(part, provider_details=chained_dict)
                else:
                    existing = part.provider_details if isinstance(part.provider_details, dict) else {}
                    part = replace(part, provider_details={**existing, **self.provider_details})
            return part
        raise ValueError(  # pragma: no cover
            f'Cannot apply ThinkingPartDeltas to non-ThinkingParts or non-ThinkingPartDeltas ({part=}, {self=})'
        )

    __repr__ = _utils.dataclasses_no_defaults_repr

```

---|---
####  content_delta `class-attribute` `instance-attribute`
```
content_delta:  | None = None

```

The incremental thinking content to add to the existing `ThinkingPart` content.
####  signature_delta `class-attribute` `instance-attribute`
```
signature_delta:  | None = None

```

Optional signature delta.
Note this is never treated as a delta — it can replace None.
####  provider_name `class-attribute` `instance-attribute`
```
provider_name:  | None = None

```

Optional provider name for the thinking part.
Signatures are only sent back to the same provider. Required to be set when `provider_details` is set and the initial ThinkingPart does not have a `provider_name` or it has changed.
####  provider_details `class-attribute` `instance-attribute`
```
provider_details: ProviderDetailsDelta[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ProviderDetailsDelta "ProviderDetailsDelta



      module-attribute
   \(pydantic_ai.messages.ProviderDetailsDelta\)") = None

```

Additional data returned by the provider that can't be mapped to standard fields.
Can be a dict to merge with existing details, or a callable that takes the existing details and returns updated details.
This is used for data that is required to be sent back to APIs, as well as data users may want to access programmatically.
When this field is set, `provider_name` is required to identify the provider that generated this data.
####  part_delta_kind `class-attribute` `instance-attribute`
```
part_delta_kind: ['thinking'] = 'thinking'

```

Part delta type identifier, used as a discriminator.
####  apply
```
apply(part: ModelResponsePart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponsePart "ModelResponsePart



      module-attribute
   \(pydantic_ai.messages.ModelResponsePart\)")) -> ThinkingPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPart "ThinkingPart



      dataclass
   \(pydantic_ai.messages.ThinkingPart\)")

```

```
apply(
    part: ModelResponsePart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponsePart "ModelResponsePart



      module-attribute
   \(pydantic_ai.messages.ModelResponsePart\)") | ThinkingPartDelta[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPartDelta "ThinkingPartDelta



      dataclass
   \(pydantic_ai.messages.ThinkingPartDelta\)"),
) -> ThinkingPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPart "ThinkingPart



      dataclass
   \(pydantic_ai.messages.ThinkingPart\)") | ThinkingPartDelta[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPartDelta "ThinkingPartDelta



      dataclass
   \(pydantic_ai.messages.ThinkingPartDelta\)")

```

```
apply(
    part: ModelResponsePart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponsePart "ModelResponsePart



      module-attribute
   \(pydantic_ai.messages.ModelResponsePart\)") | ThinkingPartDelta[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPartDelta "ThinkingPartDelta



      dataclass
   \(pydantic_ai.messages.ThinkingPartDelta\)"),
) -> ThinkingPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPart "ThinkingPart



      dataclass
   \(pydantic_ai.messages.ThinkingPart\)") | ThinkingPartDelta[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPartDelta "ThinkingPartDelta



      dataclass
   \(pydantic_ai.messages.ThinkingPartDelta\)")

```

Apply this thinking delta to an existing `ThinkingPart`.
Parameters:
Name | Type | Description | Default
---|---|---|---
`part` |  `ModelResponsePart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponsePart "ModelResponsePart



      module-attribute
   \(pydantic_ai.messages.ModelResponsePart\)") | ThinkingPartDelta[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPartDelta "ThinkingPartDelta



      dataclass
   \(pydantic_ai.messages.ThinkingPartDelta\)")` |  The existing model response part, which must be a `ThinkingPart`. |  _required_
Returns:
Type | Description
---|---
`ThinkingPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPart "ThinkingPart



      dataclass
   \(pydantic_ai.messages.ThinkingPart\)") | ThinkingPartDelta[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPartDelta "ThinkingPartDelta



      dataclass
   \(pydantic_ai.messages.ThinkingPartDelta\)")` |  A new `ThinkingPart` with updated thinking content.
Raises:
Type | Description
---|---
|  If `part` is not a `ThinkingPart`.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1832
1833
1834
1835
1836
1837
1838
1839
1840
1841
1842
1843
1844
1845
1846
1847
1848
1849
1850
1851
1852
1853
1854
1855
1856
1857
1858
1859
1860
1861
1862
1863
1864
1865
1866
1867
1868
1869
1870
1871
1872
1873
1874
1875
1876
1877
1878
1879
1880
1881
1882
1883
1884
1885
1886
1887
1888
1889
1890
1891
1892
1893
1894
1895
1896
1897
```
| ```
def apply(self, part: ModelResponsePart | ThinkingPartDelta) -> ThinkingPart | ThinkingPartDelta:
    """Apply this thinking delta to an existing `ThinkingPart`.

    Args:
        part: The existing model response part, which must be a `ThinkingPart`.

    Returns:
        A new `ThinkingPart` with updated thinking content.

    Raises:
        ValueError: If `part` is not a `ThinkingPart`.
    """
    if isinstance(part, ThinkingPart):
        new_content = part.content + self.content_delta if self.content_delta else part.content
        new_signature = self.signature_delta if self.signature_delta is not None else part.signature
        new_provider_name = self.provider_name if self.provider_name is not None else part.provider_name
        # Resolve callable provider_details if needed
        resolved_details = (
            self.provider_details(part.provider_details)
            if callable(self.provider_details)
            else self.provider_details
        )
        new_provider_details = {**(part.provider_details or {}), **(resolved_details or {})} or None
        return replace(
            part,
            content=new_content,
            signature=new_signature,
            provider_name=new_provider_name,
            provider_details=new_provider_details,
        )
    elif isinstance(part, ThinkingPartDelta):
        if self.content_delta is None and self.signature_delta is None:
            raise ValueError('Cannot apply ThinkingPartDelta with no content or signature')
        if self.content_delta is not None:
            part = replace(part, content_delta=(part.content_delta or '') + self.content_delta)
        if self.signature_delta is not None:
            part = replace(part, signature_delta=self.signature_delta)
        if self.provider_name is not None:
            part = replace(part, provider_name=self.provider_name)
        if self.provider_details is not None:
            if callable(self.provider_details):
                if callable(part.provider_details):
                    existing_fn = part.provider_details
                    new_fn = self.provider_details

                    def chained_both(d: dict[str, Any] | None) -> dict[str, Any]:
                        return new_fn(existing_fn(d))

                    part = replace(part, provider_details=chained_both)
                else:
                    part = replace(part, provider_details=self.provider_details)  # pragma: no cover
            elif callable(part.provider_details):
                existing_fn = part.provider_details
                new_dict = self.provider_details

                def chained_dict(d: dict[str, Any] | None) -> dict[str, Any]:
                    return {**existing_fn(d), **new_dict}

                part = replace(part, provider_details=chained_dict)
            else:
                existing = part.provider_details if isinstance(part.provider_details, dict) else {}
                part = replace(part, provider_details={**existing, **self.provider_details})
        return part
    raise ValueError(  # pragma: no cover
        f'Cannot apply ThinkingPartDeltas to non-ThinkingParts or non-ThinkingPartDeltas ({part=}, {self=})'
    )

```

---|---
###  ToolCallPartDelta `dataclass`
A partial update (delta) for a `ToolCallPart` to modify tool name, arguments, or tool call ID.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1902
1903
1904
1905
1906
1907
1908
1909
1910
1911
1912
1913
1914
1915
1916
1917
1918
1919
1920
1921
1922
1923
1924
1925
1926
1927
1928
1929
1930
1931
1932
1933
1934
1935
1936
1937
1938
1939
1940
1941
1942
1943
1944
1945
1946
1947
1948
1949
1950
1951
1952
1953
1954
1955
1956
1957
1958
1959
1960
1961
1962
1963
1964
1965
1966
1967
1968
1969
1970
1971
1972
1973
1974
1975
1976
1977
1978
1979
1980
1981
1982
1983
1984
1985
1986
1987
1988
1989
1990
1991
1992
1993
1994
1995
1996
1997
1998
1999
2000
2001
2002
2003
2004
2005
2006
2007
2008
2009
2010
2011
2012
2013
2014
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
2029
2030
2031
2032
2033
2034
2035
2036
2037
2038
2039
2040
2041
2042
2043
2044
2045
2046
2047
2048
2049
2050
2051
2052
2053
2054
2055
2056
2057
2058
2059
2060
2061
2062
2063
```
| ```
@dataclass(repr=False, kw_only=True)
class ToolCallPartDelta:
    """A partial update (delta) for a `ToolCallPart` to modify tool name, arguments, or tool call ID."""

    tool_name_delta: str | None = None
    """Incremental text to add to the existing tool name, if any."""

    args_delta: str | dict[str, Any] | None = None
    """Incremental data to add to the tool arguments.

    If this is a string, it will be appended to existing JSON arguments.
    If this is a dict, it will be merged with existing dict arguments.
    """

    tool_call_id: str | None = None
    """Optional tool call identifier, this is used by some models including OpenAI.

    Note this is never treated as a delta — it can replace None, but otherwise if a
    non-matching value is provided an error will be raised."""

    provider_name: str | None = None
    """The name of the provider that generated the response.

    This is required to be set when `provider_details` is set and the initial ToolCallPart does not have a `provider_name` or it has changed.
    """

    provider_details: dict[str, Any] | None = None
    """Additional data returned by the provider that can't be mapped to standard fields.

    This is used for data that is required to be sent back to APIs, as well as data users may want to access programmatically.

    When this field is set, `provider_name` is required to identify the provider that generated this data.
    """

    part_delta_kind: Literal['tool_call'] = 'tool_call'
    """Part delta type identifier, used as a discriminator. Note that this is different from `ToolCallPart.part_kind`."""

    def as_part(self) -> ToolCallPart | None:
        """Convert this delta to a fully formed `ToolCallPart` if possible, otherwise return `None`.

        Returns:
            A `ToolCallPart` if `tool_name_delta` is set, otherwise `None`.
        """
        if self.tool_name_delta is None:
            return None

        return ToolCallPart(
            self.tool_name_delta,
            self.args_delta,
            self.tool_call_id or _generate_tool_call_id(),
            provider_name=self.provider_name,
            provider_details=self.provider_details,
        )

    @overload
    def apply(self, part: ModelResponsePart) -> ToolCallPart | BuiltinToolCallPart: ...

    @overload
    def apply(
        self, part: ModelResponsePart | ToolCallPartDelta
    ) -> ToolCallPart | BuiltinToolCallPart | ToolCallPartDelta: ...

    def apply(
        self, part: ModelResponsePart | ToolCallPartDelta
    ) -> ToolCallPart | BuiltinToolCallPart | ToolCallPartDelta:
        """Apply this delta to a part or delta, returning a new part or delta with the changes applied.

        Args:
            part: The existing model response part or delta to update.

        Returns:
            Either a new `ToolCallPart` or `BuiltinToolCallPart`, or an updated `ToolCallPartDelta`.

        Raises:
            ValueError: If `part` is neither a `ToolCallPart`, `BuiltinToolCallPart`, nor a `ToolCallPartDelta`.
            UnexpectedModelBehavior: If applying JSON deltas to dict arguments or vice versa.
        """
        if isinstance(part, ToolCallPart | BuiltinToolCallPart):
            return self._apply_to_part(part)

        if isinstance(part, ToolCallPartDelta):
            return self._apply_to_delta(part)

        raise ValueError(  # pragma: no cover
            f'Can only apply ToolCallPartDeltas to ToolCallParts, BuiltinToolCallParts, or ToolCallPartDeltas, not {part}'
        )

    def _apply_to_delta(self, delta: ToolCallPartDelta) -> ToolCallPart | BuiltinToolCallPart | ToolCallPartDelta:
        """Internal helper to apply this delta to another delta."""
        if self.tool_name_delta:
            # Append incremental text to the existing tool_name_delta
            updated_tool_name_delta = (delta.tool_name_delta or '') + self.tool_name_delta
            delta = replace(delta, tool_name_delta=updated_tool_name_delta)

        if isinstance(self.args_delta, str):
            if isinstance(delta.args_delta, dict):
                raise UnexpectedModelBehavior(
                    f'Cannot apply JSON deltas to non-JSON tool arguments ({delta=}, {self=})'
                )
            updated_args_delta = (delta.args_delta or '') + self.args_delta
            delta = replace(delta, args_delta=updated_args_delta)
        elif isinstance(self.args_delta, dict):
            if isinstance(delta.args_delta, str):
                raise UnexpectedModelBehavior(
                    f'Cannot apply dict deltas to non-dict tool arguments ({delta=}, {self=})'
                )
            updated_args_delta = {**(delta.args_delta or {}), **self.args_delta}
            delta = replace(delta, args_delta=updated_args_delta)

        if self.tool_call_id:
            delta = replace(delta, tool_call_id=self.tool_call_id)

        if self.provider_name:
            delta = replace(delta, provider_name=self.provider_name)

        if self.provider_details:
            merged_provider_details = {**(delta.provider_details or {}), **self.provider_details}
            delta = replace(delta, provider_details=merged_provider_details)

        # If we now have enough data to create a full ToolCallPart, do so
        if delta.tool_name_delta is not None:
            return ToolCallPart(
                delta.tool_name_delta,
                delta.args_delta,
                delta.tool_call_id or _generate_tool_call_id(),
                provider_name=delta.provider_name,
                provider_details=delta.provider_details,
            )

        return delta

    def _apply_to_part(self, part: ToolCallPart | BuiltinToolCallPart) -> ToolCallPart | BuiltinToolCallPart:
        """Internal helper to apply this delta directly to a `ToolCallPart` or `BuiltinToolCallPart`."""
        if self.tool_name_delta:
            # Append incremental text to the existing tool_name
            tool_name = part.tool_name + self.tool_name_delta
            part = replace(part, tool_name=tool_name)

        if isinstance(self.args_delta, str):
            if isinstance(part.args, dict):
                raise UnexpectedModelBehavior(f'Cannot apply JSON deltas to non-JSON tool arguments ({part=}, {self=})')
            updated_json = (part.args or '') + self.args_delta
            part = replace(part, args=updated_json)
        elif isinstance(self.args_delta, dict):
            if isinstance(part.args, str):
                raise UnexpectedModelBehavior(f'Cannot apply dict deltas to non-dict tool arguments ({part=}, {self=})')
            updated_dict = {**(part.args or {}), **self.args_delta}
            part = replace(part, args=updated_dict)

        if self.tool_call_id:
            part = replace(part, tool_call_id=self.tool_call_id)

        if self.provider_name:
            part = replace(part, provider_name=self.provider_name)

        if self.provider_details:
            merged_provider_details = {**(part.provider_details or {}), **self.provider_details}
            part = replace(part, provider_details=merged_provider_details)

        return part

    __repr__ = _utils.dataclasses_no_defaults_repr

```

---|---
####  tool_name_delta `class-attribute` `instance-attribute`
```
tool_name_delta:  | None = None

```

Incremental text to add to the existing tool name, if any.
####  args_delta `class-attribute` `instance-attribute`
```
args_delta:  | [, ] | None = None

```

Incremental data to add to the tool arguments.
If this is a string, it will be appended to existing JSON arguments. If this is a dict, it will be merged with existing dict arguments.
####  tool_call_id `class-attribute` `instance-attribute`
```
tool_call_id:  | None = None

```

Optional tool call identifier, this is used by some models including OpenAI.
Note this is never treated as a delta — it can replace None, but otherwise if a non-matching value is provided an error will be raised.
####  provider_name `class-attribute` `instance-attribute`
```
provider_name:  | None = None

```

The name of the provider that generated the response.
This is required to be set when `provider_details` is set and the initial ToolCallPart does not have a `provider_name` or it has changed.
####  provider_details `class-attribute` `instance-attribute`
```
provider_details: [, ] | None = None

```

Additional data returned by the provider that can't be mapped to standard fields.
This is used for data that is required to be sent back to APIs, as well as data users may want to access programmatically.
When this field is set, `provider_name` is required to identify the provider that generated this data.
####  part_delta_kind `class-attribute` `instance-attribute`
```
part_delta_kind: ['tool_call'] = 'tool_call'

```

Part delta type identifier, used as a discriminator. Note that this is different from `ToolCallPart.part_kind`.
####  as_part
```
as_part() -> ToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart "ToolCallPart



      dataclass
   \(pydantic_ai.messages.ToolCallPart\)") | None

```

Convert this delta to a fully formed `ToolCallPart` if possible, otherwise return `None`.
Returns:
Type | Description
---|---
`ToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart "ToolCallPart



      dataclass
   \(pydantic_ai.messages.ToolCallPart\)") | None` |  A `ToolCallPart` if `tool_name_delta` is set, otherwise `None`.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1939
1940
1941
1942
1943
1944
1945
1946
1947
1948
1949
1950
1951
1952
1953
1954
```
| ```
def as_part(self) -> ToolCallPart | None:
    """Convert this delta to a fully formed `ToolCallPart` if possible, otherwise return `None`.

    Returns:
        A `ToolCallPart` if `tool_name_delta` is set, otherwise `None`.
    """
    if self.tool_name_delta is None:
        return None

    return ToolCallPart(
        self.tool_name_delta,
        self.args_delta,
        self.tool_call_id or _generate_tool_call_id(),
        provider_name=self.provider_name,
        provider_details=self.provider_details,
    )

```

---|---
####  apply
```
apply(
    part: ModelResponsePart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponsePart "ModelResponsePart



      module-attribute
   \(pydantic_ai.messages.ModelResponsePart\)"),
) -> ToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart "ToolCallPart



      dataclass
   \(pydantic_ai.messages.ToolCallPart\)") | BuiltinToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolCallPart "BuiltinToolCallPart



      dataclass
   \(pydantic_ai.messages.BuiltinToolCallPart\)")

```

```
apply(
    part: ModelResponsePart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponsePart "ModelResponsePart



      module-attribute
   \(pydantic_ai.messages.ModelResponsePart\)") | ToolCallPartDelta[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta "ToolCallPartDelta



      dataclass
   \(pydantic_ai.messages.ToolCallPartDelta\)"),
) -> ToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart "ToolCallPart



      dataclass
   \(pydantic_ai.messages.ToolCallPart\)") | BuiltinToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolCallPart "BuiltinToolCallPart



      dataclass
   \(pydantic_ai.messages.BuiltinToolCallPart\)") | ToolCallPartDelta[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta "ToolCallPartDelta



      dataclass
   \(pydantic_ai.messages.ToolCallPartDelta\)")

```

```
apply(
    part: ModelResponsePart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponsePart "ModelResponsePart



      module-attribute
   \(pydantic_ai.messages.ModelResponsePart\)") | ToolCallPartDelta[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta "ToolCallPartDelta



      dataclass
   \(pydantic_ai.messages.ToolCallPartDelta\)"),
) -> ToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart "ToolCallPart



      dataclass
   \(pydantic_ai.messages.ToolCallPart\)") | BuiltinToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolCallPart "BuiltinToolCallPart



      dataclass
   \(pydantic_ai.messages.BuiltinToolCallPart\)") | ToolCallPartDelta[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta "ToolCallPartDelta



      dataclass
   \(pydantic_ai.messages.ToolCallPartDelta\)")

```

Apply this delta to a part or delta, returning a new part or delta with the changes applied.
Parameters:
Name | Type | Description | Default
---|---|---|---
`part` |  `ModelResponsePart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponsePart "ModelResponsePart



      module-attribute
   \(pydantic_ai.messages.ModelResponsePart\)") | ToolCallPartDelta[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta "ToolCallPartDelta



      dataclass
   \(pydantic_ai.messages.ToolCallPartDelta\)")` |  The existing model response part or delta to update. |  _required_
Returns:
Type | Description
---|---
`ToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart "ToolCallPart



      dataclass
   \(pydantic_ai.messages.ToolCallPart\)") | BuiltinToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolCallPart "BuiltinToolCallPart
