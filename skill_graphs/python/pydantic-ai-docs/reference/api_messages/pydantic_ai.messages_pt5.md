    def tool_calls(self) -> list[ToolCallPart]:
        """Get the tool calls in the response."""
        return [part for part in self.parts if isinstance(part, ToolCallPart)]

    @property
    def builtin_tool_calls(self) -> list[tuple[BuiltinToolCallPart, BuiltinToolReturnPart]]:
        """Get the builtin tool calls and results in the response."""
        calls = [part for part in self.parts if isinstance(part, BuiltinToolCallPart)]
        if not calls:
            return []
        returns_by_id = {part.tool_call_id: part for part in self.parts if isinstance(part, BuiltinToolReturnPart)}
        return [
            (call_part, returns_by_id[call_part.tool_call_id])
            for call_part in calls
            if call_part.tool_call_id in returns_by_id
        ]

    @deprecated('`price` is deprecated, use `cost` instead')
    def price(self) -> genai_types.PriceCalculation:  # pragma: no cover
        return self.cost()

    def cost(self) -> genai_types.PriceCalculation:
        """Calculate the cost of the usage.

        Uses [`genai-prices`](https://github.com/pydantic/genai-prices).
        """
        assert self.model_name, 'Model name is required to calculate price'
        # Try matching on provider_api_url first as this is more specific, then fall back to provider_id.
        if self.provider_url:
            try:
                return calc_price(
                    self.usage,
                    self.model_name,
                    provider_api_url=self.provider_url,
                    genai_request_timestamp=self.timestamp,
                )
            except LookupError:
                pass
        return calc_price(
            self.usage,
            self.model_name,
            provider_id=self.provider_name,
            genai_request_timestamp=self.timestamp,
        )

    def otel_events(self, settings: InstrumentationSettings) -> list[LogRecord]:
        """Return OpenTelemetry events for the response."""
        result: list[LogRecord] = []

        def new_event_body():
            new_body: dict[str, Any] = {'role': 'assistant'}
            ev = LogRecord(attributes={'event.name': 'gen_ai.assistant.message'}, body=new_body)
            result.append(ev)
            return new_body

        body = new_event_body()
        for part in self.parts:
            if isinstance(part, ToolCallPart):
                body.setdefault('tool_calls', []).append(
                    {
                        'id': part.tool_call_id,
                        'type': 'function',
                        'function': {
                            'name': part.tool_name,
                            **({'arguments': part.args} if settings.include_content else {}),
                        },
                    }
                )
            elif isinstance(part, TextPart | ThinkingPart):
                kind = part.part_kind
                body.setdefault('content', []).append(
                    {'kind': kind, **({'text': part.content} if settings.include_content else {})}
                )
            elif isinstance(part, FilePart):
                body.setdefault('content', []).append(
                    {
                        'kind': 'binary',
                        'media_type': part.content.media_type,
                        **(
                            {'binary_content': part.content.base64}
                            if settings.include_content and settings.include_binary_content
                            else {}
                        ),
                    }
                )

        if content := body.get('content'):
            text_content = content[0].get('text')
            if content == [{'kind': 'text', 'text': text_content}]:
                body['content'] = text_content

        return result

    def otel_message_parts(self, settings: InstrumentationSettings) -> list[_otel_messages.MessagePart]:
        parts: list[_otel_messages.MessagePart] = []
        for part in self.parts:
            if isinstance(part, TextPart):
                parts.append(
                    _otel_messages.TextPart(
                        type='text',
                        **({'content': part.content} if settings.include_content else {}),
                    )
                )
            elif isinstance(part, ThinkingPart):
                parts.append(
                    _otel_messages.ThinkingPart(
                        type='thinking',
                        **({'content': part.content} if settings.include_content else {}),
                    )
                )
            elif isinstance(part, FilePart):
                parts.append(
                    _convert_binary_to_otel_part(part.content.media_type, lambda p=part: p.content.base64, settings)
                )
            elif isinstance(part, BaseToolCallPart):
                call_part = _otel_messages.ToolCallPart(type='tool_call', id=part.tool_call_id, name=part.tool_name)
                if isinstance(part, BuiltinToolCallPart):
                    call_part['builtin'] = True
                if settings.include_content and part.args is not None:
                    from .models.instrumented import InstrumentedModel

                    if isinstance(part.args, str):
                        call_part['arguments'] = part.args
                    else:
                        call_part['arguments'] = {k: InstrumentedModel.serialize_any(v) for k, v in part.args.items()}

                parts.append(call_part)
            elif isinstance(part, BuiltinToolReturnPart):
                return_part = _otel_messages.ToolCallResponsePart(
                    type='tool_call_response',
                    id=part.tool_call_id,
                    name=part.tool_name,
                    builtin=True,
                )
                if settings.include_content and part.content is not None:  # pragma: no branch
                    from .models.instrumented import InstrumentedModel

                    return_part['result'] = InstrumentedModel.serialize_any(part.content)

                parts.append(return_part)
        return parts

    @property
    @deprecated('`vendor_details` is deprecated, use `provider_details` instead')
    def vendor_details(self) -> dict[str, Any] | None:
        return self.provider_details

    @property
    @deprecated('`vendor_id` is deprecated, use `provider_response_id` instead')
    def vendor_id(self) -> str | None:
        return self.provider_response_id

    @property
    @deprecated('`provider_request_id` is deprecated, use `provider_response_id` instead')
    def provider_request_id(self) -> str | None:
        return self.provider_response_id

    __repr__ = _utils.dataclasses_no_defaults_repr

```

---|---
####  parts `instance-attribute`
```
parts: [ModelResponsePart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponsePart "ModelResponsePart



      module-attribute
   \(pydantic_ai.messages.ModelResponsePart\)")]

```

The parts of the model message.
####  usage `class-attribute` `instance-attribute`
```
usage: RequestUsage[](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.RequestUsage "RequestUsage



      dataclass
   \(pydantic_ai.usage.RequestUsage\)") = (default_factory=RequestUsage[](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.RequestUsage "RequestUsage



      dataclass
   \(pydantic_ai.usage.RequestUsage\)"))

```

Usage information for the request.
This has a default to make tests easier, and to support loading old messages where usage will be missing.
####  model_name `class-attribute` `instance-attribute`
```
model_name:  | None = None

```

The name of the model that generated the response.
####  timestamp `class-attribute` `instance-attribute`
```
timestamp:  = (default_factory=now_utc)

```

The timestamp when the response was received locally.
This is always a high-precision local datetime. Provider-specific timestamps (if available) are stored in `provider_details['timestamp']`.
####  kind `class-attribute` `instance-attribute`
```
kind: ['response'] = 'response'

```

Message type identifier, this is available on all parts as a discriminator.
####  provider_name `class-attribute` `instance-attribute`
```
provider_name:  | None = None

```

The name of the LLM provider that generated the response.
####  provider_url `class-attribute` `instance-attribute`
```
provider_url:  | None = None

```

The base URL of the LLM provider that generated the response.
####  provider_details `class-attribute` `instance-attribute`
```
provider_details: [
    [, ] | None,
    Field[](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field "pydantic.Field")(
        validation_alias=AliasChoices[](https://docs.pydantic.dev/latest/api/aliases/#pydantic.aliases.AliasChoices "pydantic.AliasChoices")(
            provider_details[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.provider_details "provider_details



      class-attribute
      instance-attribute
   \(pydantic_ai.messages.ModelResponse.provider_details\)"), vendor_details
        )
    ),
] = None

```

Additional data returned by the provider that can't be mapped to standard fields.
####  provider_response_id `class-attribute` `instance-attribute`
```
provider_response_id: [
     | None,
    Field[](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field "pydantic.Field")(
        validation_alias=AliasChoices[](https://docs.pydantic.dev/latest/api/aliases/#pydantic.aliases.AliasChoices "pydantic.AliasChoices")(
            provider_response_id[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.provider_response_id "provider_response_id



      class-attribute
      instance-attribute
   \(pydantic_ai.messages.ModelResponse.provider_response_id\)"), vendor_id
        )
    ),
] = None

```

request ID as specified by the model provider. This can be used to track the specific request to the model.
####  finish_reason `class-attribute` `instance-attribute`
```
finish_reason: FinishReason[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FinishReason "FinishReason



      module-attribute
   \(pydantic_ai.messages.FinishReason\)") | None = None

```

Reason the model finished generating the response, normalized to OpenTelemetry values.
####  run_id `class-attribute` `instance-attribute`
```
run_id:  | None = None

```

The unique identifier of the agent run in which this message originated.
####  metadata `class-attribute` `instance-attribute`
```
metadata: [, ] | None = None

```

Additional data that can be accessed programmatically by the application but is not sent to the LLM.
####  text `property`
```
text:  | None

```

Get the text in the response.
####  thinking `property`
```
thinking:  | None

```

Get the thinking in the response.
####  files `property`
```
files: [BinaryContent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent "BinaryContent \(pydantic_ai.messages.BinaryContent\)")]

```

Get the files in the response.
####  images `property`
```
images: [BinaryImage[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryImage "BinaryImage \(pydantic_ai.messages.BinaryImage\)")]

```

Get the images in the response.
####  tool_calls `property`
```
tool_calls: [ToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart "ToolCallPart



      dataclass
   \(pydantic_ai.messages.ToolCallPart\)")]

```

Get the tool calls in the response.
####  builtin_tool_calls `property`
```
builtin_tool_calls: [
    [BuiltinToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolCallPart "BuiltinToolCallPart



      dataclass
   \(pydantic_ai.messages.BuiltinToolCallPart\)"), BuiltinToolReturnPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolReturnPart "BuiltinToolReturnPart



      dataclass
   \(pydantic_ai.messages.BuiltinToolReturnPart\)")]
]

```

Get the builtin tool calls and results in the response.
####  price `deprecated`
```
price() -> PriceCalculation

```

Deprecated
`price` is deprecated, use `cost` instead
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1591
1592
1593
```
| ```
@deprecated('`price` is deprecated, use `cost` instead')
def price(self) -> genai_types.PriceCalculation:  # pragma: no cover
    return self.cost()

```

---|---
####  cost
```
cost() -> PriceCalculation

```

Calculate the cost of the usage.
Uses
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1595
1596
1597
1598
1599
1600
1601
1602
1603
1604
1605
1606
1607
1608
1609
1610
1611
1612
1613
1614
1615
1616
1617
```
| ```
def cost(self) -> genai_types.PriceCalculation:
    """Calculate the cost of the usage.

    Uses [`genai-prices`](https://github.com/pydantic/genai-prices).
    """
    assert self.model_name, 'Model name is required to calculate price'
    # Try matching on provider_api_url first as this is more specific, then fall back to provider_id.
    if self.provider_url:
        try:
            return calc_price(
                self.usage,
                self.model_name,
                provider_api_url=self.provider_url,
                genai_request_timestamp=self.timestamp,
            )
        except LookupError:
            pass
    return calc_price(
        self.usage,
        self.model_name,
        provider_id=self.provider_name,
        genai_request_timestamp=self.timestamp,
    )

```

---|---
####  otel_events
```
otel_events(
    settings: InstrumentationSettings[](https://ai.pydantic.dev/api/models/instrumented/#pydantic_ai.models.instrumented.InstrumentationSettings "InstrumentationSettings



      dataclass
   \(pydantic_ai.models.instrumented.InstrumentationSettings\)"),
) -> [LogRecord]

```

Return OpenTelemetry events for the response.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1619
1620
1621
1622
1623
1624
1625
1626
1627
1628
1629
1630
1631
1632
1633
1634
1635
1636
1637
1638
1639
1640
1641
1642
1643
1644
1645
1646
1647
1648
1649
1650
1651
1652
1653
1654
1655
1656
1657
1658
1659
1660
1661
1662
1663
1664
1665
```
| ```
def otel_events(self, settings: InstrumentationSettings) -> list[LogRecord]:
    """Return OpenTelemetry events for the response."""
    result: list[LogRecord] = []

    def new_event_body():
        new_body: dict[str, Any] = {'role': 'assistant'}
        ev = LogRecord(attributes={'event.name': 'gen_ai.assistant.message'}, body=new_body)
        result.append(ev)
        return new_body

    body = new_event_body()
    for part in self.parts:
        if isinstance(part, ToolCallPart):
            body.setdefault('tool_calls', []).append(
                {
                    'id': part.tool_call_id,
                    'type': 'function',
                    'function': {
                        'name': part.tool_name,
                        **({'arguments': part.args} if settings.include_content else {}),
                    },
                }
            )
        elif isinstance(part, TextPart | ThinkingPart):
            kind = part.part_kind
            body.setdefault('content', []).append(
                {'kind': kind, **({'text': part.content} if settings.include_content else {})}
            )
        elif isinstance(part, FilePart):
            body.setdefault('content', []).append(
                {
                    'kind': 'binary',
                    'media_type': part.content.media_type,
                    **(
                        {'binary_content': part.content.base64}
                        if settings.include_content and settings.include_binary_content
                        else {}
                    ),
                }
            )

    if content := body.get('content'):
        text_content = content[0].get('text')
        if content == [{'kind': 'text', 'text': text_content}]:
            body['content'] = text_content

    return result

```

---|---
###  ModelMessage `module-attribute`
```
ModelMessage = [
    ModelRequest[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelRequest "ModelRequest



      dataclass
   \(pydantic_ai.messages.ModelRequest\)") | ModelResponse[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse "ModelResponse



      dataclass
   \(pydantic_ai.messages.ModelResponse\)"), Discriminator[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Discriminator "pydantic.Discriminator")("kind")
]

```

Any message sent to or returned by a model.
###  ModelMessagesTypeAdapter `module-attribute`
```
ModelMessagesTypeAdapter = TypeAdapter[](https://docs.pydantic.dev/latest/api/type_adapter/#pydantic.type_adapter.TypeAdapter "pydantic.TypeAdapter")(
    [ModelMessage[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage "ModelMessage



      module-attribute
   \(pydantic_ai.messages.ModelMessage\)")],
    config=ConfigDict[](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict "pydantic.ConfigDict")(
        defer_build=True,
        ser_json_bytes="base64",
        val_json_bytes="base64",
    ),
)

```

Pydantic [`TypeAdapter`](https://docs.pydantic.dev/latest/api/type_adapter/#pydantic.type_adapter.TypeAdapter) for (de)serializing messages.
###  TextPartDelta `dataclass`
A partial update (delta) for a `TextPart` to append new text content.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1743
1744
1745
1746
1747
1748
1749
1750
1751
1752
1753
1754
1755
1756
1757
1758
1759
1760
1761
1762
1763
1764
1765
1766
1767
1768
1769
1770
1771
1772
1773
1774
1775
1776
1777
1778
1779
1780
1781
1782
1783
1784
1785
1786
1787
1788
1789
1790
```
| ```
@dataclass(repr=False)
class TextPartDelta:
    """A partial update (delta) for a `TextPart` to append new text content."""

    content_delta: str
    """The incremental text content to add to the existing `TextPart` content."""

    _: KW_ONLY

    provider_name: str | None = None
    """The name of the provider that generated the response.

    This is required to be set when `provider_details` is set and the initial TextPart does not have a `provider_name` or it has changed.
    """

    provider_details: dict[str, Any] | None = None
    """Additional data returned by the provider that can't be mapped to standard fields.

    This is used for data that is required to be sent back to APIs, as well as data users may want to access programmatically.

    When this field is set, `provider_name` is required to identify the provider that generated this data.
    """

    part_delta_kind: Literal['text'] = 'text'
    """Part delta type identifier, used as a discriminator."""

    def apply(self, part: ModelResponsePart) -> TextPart:
        """Apply this text delta to an existing `TextPart`.

        Args:
            part: The existing model response part, which must be a `TextPart`.

        Returns:
            A new `TextPart` with updated text content.

        Raises:
            ValueError: If `part` is not a `TextPart`.
        """
        if not isinstance(part, TextPart):
            raise ValueError('Cannot apply TextPartDeltas to non-TextParts')  # pragma: no cover
        return replace(
            part,
            content=part.content + self.content_delta,
            provider_name=self.provider_name or part.provider_name,
            provider_details={**(part.provider_details or {}), **(self.provider_details or {})} or None,
        )

    __repr__ = _utils.dataclasses_no_defaults_repr

```

---|---
####  content_delta `instance-attribute`
```
content_delta:

```

The incremental text content to add to the existing `TextPart` content.
####  provider_name `class-attribute` `instance-attribute`
```
provider_name:  | None = None

```

The name of the provider that generated the response.
This is required to be set when `provider_details` is set and the initial TextPart does not have a `provider_name` or it has changed.
####  provider_details `class-attribute` `instance-attribute`
```
provider_details: [, ] | None = None

```

Additional data returned by the provider that can't be mapped to standard fields.
This is used for data that is required to be sent back to APIs, as well as data users may want to access programmatically.
When this field is set, `provider_name` is required to identify the provider that generated this data.
####  part_delta_kind `class-attribute` `instance-attribute`
```
part_delta_kind: ['text'] = 'text'

```

Part delta type identifier, used as a discriminator.
####  apply
```
apply(part: ModelResponsePart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponsePart "ModelResponsePart



      module-attribute
   \(pydantic_ai.messages.ModelResponsePart\)")) -> TextPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPart "TextPart



      dataclass
   \(pydantic_ai.messages.TextPart\)")

```

Apply this text delta to an existing `TextPart`.
Parameters:
Name | Type | Description | Default
---|---|---|---
`part` |  `ModelResponsePart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponsePart "ModelResponsePart



      module-attribute
   \(pydantic_ai.messages.ModelResponsePart\)")` |  The existing model response part, which must be a `TextPart`. |  _required_
Returns:
Type | Description
---|---
`TextPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPart "TextPart



      dataclass
   \(pydantic_ai.messages.TextPart\)")` |  A new `TextPart` with updated text content.
Raises:
Type | Description
---|---
|  If `part` is not a `TextPart`.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1769
1770
1771
1772
1773
1774
1775
1776
1777
1778
1779
1780
1781
1782
1783
1784
1785
1786
1787
1788
```
| ```
def apply(self, part: ModelResponsePart) -> TextPart:
    """Apply this text delta to an existing `TextPart`.

    Args:
        part: The existing model response part, which must be a `TextPart`.

    Returns:
        A new `TextPart` with updated text content.

    Raises:
        ValueError: If `part` is not a `TextPart`.
    """
    if not isinstance(part, TextPart):
        raise ValueError('Cannot apply TextPartDeltas to non-TextParts')  # pragma: no cover
    return replace(
        part,
        content=part.content + self.content_delta,
        provider_name=self.provider_name or part.provider_name,
        provider_details={**(part.provider_details or {}), **(self.provider_details or {})} or None,
    )

```

---|---
###  ThinkingPartDelta `dataclass`
A partial update (delta) for a `ThinkingPart` to append new thinking content.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1793
1794
1795
1796
1797
1798
1799
1800
1801
1802
1803
1804
1805
1806
1807
1808
1809
1810
1811
1812
1813
1814
1815
1816
1817
1818
1819
1820
1821
1822
1823
1824
1825
1826
1827
1828
1829
1830
1831
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
1898
1899
```
| ```
@dataclass(repr=False, kw_only=True)
class ThinkingPartDelta:
    """A partial update (delta) for a `ThinkingPart` to append new thinking content."""

    content_delta: str | None = None
    """The incremental thinking content to add to the existing `ThinkingPart` content."""

    signature_delta: str | None = None
    """Optional signature delta.

    Note this is never treated as a delta — it can replace None.
    """

    provider_name: str | None = None
    """Optional provider name for the thinking part.

    Signatures are only sent back to the same provider.
    Required to be set when `provider_details` is set and the initial ThinkingPart does not have a `provider_name` or it has changed.
    """

    provider_details: ProviderDetailsDelta = None
    """Additional data returned by the provider that can't be mapped to standard fields.

    Can be a dict to merge with existing details, or a callable that takes
    the existing details and returns updated details.

    This is used for data that is required to be sent back to APIs, as well as data users may want to access programmatically.

    When this field is set, `provider_name` is required to identify the provider that generated this data."""

    part_delta_kind: Literal['thinking'] = 'thinking'
    """Part delta type identifier, used as a discriminator."""

    @overload
    def apply(self, part: ModelResponsePart) -> ThinkingPart: ...

    @overload
    def apply(self, part: ModelResponsePart | ThinkingPartDelta) -> ThinkingPart | ThinkingPartDelta: ...

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
