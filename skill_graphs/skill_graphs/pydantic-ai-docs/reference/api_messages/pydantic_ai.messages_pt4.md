1246
```
| ```
@classmethod
def user_text_prompt(cls, user_prompt: str, *, instructions: str | None = None) -> ModelRequest:
    """Create a `ModelRequest` with a single user prompt as text."""
    return cls(parts=[UserPromptPart(user_prompt)], instructions=instructions)

```

---|---
###  TextPart `dataclass`
A plain text response from a model.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1251
1252
1253
1254
1255
1256
1257
1258
1259
1260
1261
1262
1263
1264
1265
1266
1267
1268
1269
1270
1271
1272
1273
1274
1275
1276
1277
1278
1279
1280
1281
1282
1283
1284
1285
1286
```
| ```
@dataclass(repr=False)
class TextPart:
    """A plain text response from a model."""

    content: str
    """The text content of the response."""

    _: KW_ONLY

    id: str | None = None
    """An optional identifier of the text part.

    When this field is set, `provider_name` is required to identify the provider that generated this data.
    """

    provider_name: str | None = None
    """The name of the provider that generated the response.

    Required to be set when `provider_details` or `id` is set.
    """

    provider_details: dict[str, Any] | None = None
    """Additional data returned by the provider that can't be mapped to standard fields.

    This is used for data that is required to be sent back to APIs, as well as data users may want to access programmatically.
    When this field is set, `provider_name` is required to identify the provider that generated this data.
    """

    part_kind: Literal['text'] = 'text'
    """Part type identifier, this is available on all parts as a discriminator."""

    def has_content(self) -> bool:
        """Return `True` if the text content is non-empty."""
        return bool(self.content)

    __repr__ = _utils.dataclasses_no_defaults_repr

```

---|---
####  content `instance-attribute`
```
content:

```

The text content of the response.
####  id `class-attribute` `instance-attribute`
```
id:  | None = None

```

An optional identifier of the text part.
When this field is set, `provider_name` is required to identify the provider that generated this data.
####  provider_name `class-attribute` `instance-attribute`
```
provider_name:  | None = None

```

The name of the provider that generated the response.
Required to be set when `provider_details` or `id` is set.
####  provider_details `class-attribute` `instance-attribute`
```
provider_details: [, ] | None = None

```

Additional data returned by the provider that can't be mapped to standard fields.
This is used for data that is required to be sent back to APIs, as well as data users may want to access programmatically. When this field is set, `provider_name` is required to identify the provider that generated this data.
####  part_kind `class-attribute` `instance-attribute`
```
part_kind: ['text'] = 'text'

```

Part type identifier, this is available on all parts as a discriminator.
####  has_content
```
has_content() ->

```

Return `True` if the text content is non-empty.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1282
1283
1284
```
| ```
def has_content(self) -> bool:
    """Return `True` if the text content is non-empty."""
    return bool(self.content)

```

---|---
###  ThinkingPart `dataclass`
A thinking response from a model.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1289
1290
1291
1292
1293
1294
1295
1296
1297
1298
1299
1300
1301
1302
1303
1304
1305
1306
1307
1308
1309
1310
1311
1312
1313
1314
1315
1316
1317
1318
1319
1320
1321
1322
1323
1324
1325
1326
1327
1328
1329
1330
1331
1332
1333
1334
1335
1336
1337
1338
```
| ```
@dataclass(repr=False)
class ThinkingPart:
    """A thinking response from a model."""

    content: str
    """The thinking content of the response."""

    _: KW_ONLY

    id: str | None = None
    """The identifier of the thinking part.

    When this field is set, `provider_name` is required to identify the provider that generated this data.
    """

    signature: str | None = None
    """The signature of the thinking.

    Supported by:

    * Anthropic (corresponds to the `signature` field)
    * Bedrock (corresponds to the `signature` field)
    * Google (corresponds to the `thought_signature` field)
    * OpenAI (corresponds to the `encrypted_content` field)

    When this field is set, `provider_name` is required to identify the provider that generated this data.
    """

    provider_name: str | None = None
    """The name of the provider that generated the response.

    Signatures are only sent back to the same provider.
    Required to be set when `provider_details`, `id` or `signature` is set.
    """

    provider_details: dict[str, Any] | None = None
    """Additional data returned by the provider that can't be mapped to standard fields.

    This is used for data that is required to be sent back to APIs, as well as data users may want to access programmatically.
    When this field is set, `provider_name` is required to identify the provider that generated this data.
    """

    part_kind: Literal['thinking'] = 'thinking'
    """Part type identifier, this is available on all parts as a discriminator."""

    def has_content(self) -> bool:
        """Return `True` if the thinking content is non-empty."""
        return bool(self.content)

    __repr__ = _utils.dataclasses_no_defaults_repr

```

---|---
####  content `instance-attribute`
```
content:

```

The thinking content of the response.
####  id `class-attribute` `instance-attribute`
```
id:  | None = None

```

The identifier of the thinking part.
When this field is set, `provider_name` is required to identify the provider that generated this data.
####  signature `class-attribute` `instance-attribute`
```
signature:  | None = None

```

The signature of the thinking.
Supported by:
  * Anthropic (corresponds to the `signature` field)
  * Bedrock (corresponds to the `signature` field)
  * Google (corresponds to the `thought_signature` field)
  * OpenAI (corresponds to the `encrypted_content` field)


When this field is set, `provider_name` is required to identify the provider that generated this data.
####  provider_name `class-attribute` `instance-attribute`
```
provider_name:  | None = None

```

The name of the provider that generated the response.
Signatures are only sent back to the same provider. Required to be set when `provider_details`, `id` or `signature` is set.
####  provider_details `class-attribute` `instance-attribute`
```
provider_details: [, ] | None = None

```

Additional data returned by the provider that can't be mapped to standard fields.
This is used for data that is required to be sent back to APIs, as well as data users may want to access programmatically. When this field is set, `provider_name` is required to identify the provider that generated this data.
####  part_kind `class-attribute` `instance-attribute`
```
part_kind: ['thinking'] = 'thinking'

```

Part type identifier, this is available on all parts as a discriminator.
####  has_content
```
has_content() ->

```

Return `True` if the thinking content is non-empty.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1334
1335
1336
```
| ```
def has_content(self) -> bool:
    """Return `True` if the thinking content is non-empty."""
    return bool(self.content)

```

---|---
###  FilePart `dataclass`
A file response from a model.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1341
1342
1343
1344
1345
1346
1347
1348
1349
1350
1351
1352
1353
1354
1355
1356
1357
1358
1359
1360
1361
1362
1363
1364
1365
1366
1367
1368
1369
1370
1371
1372
1373
1374
1375
1376
```
| ```
@dataclass(repr=False)
class FilePart:
    """A file response from a model."""

    content: Annotated[BinaryContent, pydantic.AfterValidator(BinaryImage.narrow_type)]
    """The file content of the response."""

    _: KW_ONLY

    id: str | None = None
    """The identifier of the file part.

    When this field is set, `provider_name` is required to identify the provider that generated this data.
    """

    provider_name: str | None = None
    """The name of the provider that generated the response.

    Required to be set when `provider_details` or `id` is set.
    """

    provider_details: dict[str, Any] | None = None
    """Additional data returned by the provider that can't be mapped to standard fields.

    This is used for data that is required to be sent back to APIs, as well as data users may want to access programmatically.
    When this field is set, `provider_name` is required to identify the provider that generated this data.
    """

    part_kind: Literal['file'] = 'file'
    """Part type identifier, this is available on all parts as a discriminator."""

    def has_content(self) -> bool:
        """Return `True` if the file content is non-empty."""
        return bool(self.content.data)

    __repr__ = _utils.dataclasses_no_defaults_repr

```

---|---
####  content `instance-attribute`
```
content: [
    BinaryContent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent "BinaryContent \(pydantic_ai.messages.BinaryContent\)"), AfterValidator[](https://docs.pydantic.dev/latest/api/functional_validators/#pydantic.functional_validators.AfterValidator "pydantic.AfterValidator")(narrow_type[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent.narrow_type "narrow_type



      staticmethod
   \(pydantic_ai.messages.BinaryImage.narrow_type\)"))
]

```

The file content of the response.
####  id `class-attribute` `instance-attribute`
```
id:  | None = None

```

The identifier of the file part.
When this field is set, `provider_name` is required to identify the provider that generated this data.
####  provider_name `class-attribute` `instance-attribute`
```
provider_name:  | None = None

```

The name of the provider that generated the response.
Required to be set when `provider_details` or `id` is set.
####  provider_details `class-attribute` `instance-attribute`
```
provider_details: [, ] | None = None

```

Additional data returned by the provider that can't be mapped to standard fields.
This is used for data that is required to be sent back to APIs, as well as data users may want to access programmatically. When this field is set, `provider_name` is required to identify the provider that generated this data.
####  part_kind `class-attribute` `instance-attribute`
```
part_kind: ['file'] = 'file'

```

Part type identifier, this is available on all parts as a discriminator.
####  has_content
```
has_content() ->

```

Return `True` if the file content is non-empty.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1372
1373
1374
```
| ```
def has_content(self) -> bool:
    """Return `True` if the file content is non-empty."""
    return bool(self.content.data)

```

---|---
###  BaseToolCallPart `dataclass`
A tool call from a model.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1379
1380
1381
1382
1383
1384
1385
1386
1387
1388
1389
1390
1391
1392
1393
1394
1395
1396
1397
1398
1399
1400
1401
1402
1403
1404
1405
1406
1407
1408
1409
1410
1411
1412
1413
1414
1415
1416
1417
1418
1419
1420
1421
1422
1423
1424
1425
1426
1427
1428
1429
1430
1431
1432
1433
1434
1435
1436
1437
1438
1439
1440
1441
1442
1443
1444
1445
1446
1447
1448
1449
```
| ```
@dataclass(repr=False)
class BaseToolCallPart:
    """A tool call from a model."""

    tool_name: str
    """The name of the tool to call."""

    args: str | dict[str, Any] | None = None
    """The arguments to pass to the tool.

    This is stored either as a JSON string or a Python dictionary depending on how data was received.
    """

    tool_call_id: str = field(default_factory=_generate_tool_call_id)
    """The tool call identifier, this is used by some models including OpenAI.

    In case the tool call id is not provided by the model, Pydantic AI will generate a random one.
    """

    _: KW_ONLY

    id: str | None = None
    """An optional identifier of the tool call part, separate from the tool call ID.

    This is used by some APIs like OpenAI Responses.
    When this field is set, `provider_name` is required to identify the provider that generated this data.
    """

    provider_name: str | None = None
    """The name of the provider that generated the response.

    Builtin tool calls are only sent back to the same provider.
    Required to be set when `provider_details` or `id` is set.
    """

    provider_details: dict[str, Any] | None = None
    """Additional data returned by the provider that can't be mapped to standard fields.

    This is used for data that is required to be sent back to APIs, as well as data users may want to access programmatically.
    When this field is set, `provider_name` is required to identify the provider that generated this data.
    """

    def args_as_dict(self) -> dict[str, Any]:
        """Return the arguments as a Python dictionary.

        This is just for convenience with models that require dicts as input.
        """
        if not self.args:
            return {}
        if isinstance(self.args, dict):
            return self.args
        args = pydantic_core.from_json(self.args)
        assert isinstance(args, dict), 'args should be a dict'
        return cast(dict[str, Any], args)

    def args_as_json_str(self) -> str:
        """Return the arguments as a JSON string.

        This is just for convenience with models that require JSON strings as input.
        """
        if not self.args:
            return '{}'
        if isinstance(self.args, str):
            return self.args
        return pydantic_core.to_json(self.args).decode()

    def has_content(self) -> bool:
        """Return `True` if the tool call has content."""
        return self.args not in ('', {}, None)

    __repr__ = _utils.dataclasses_no_defaults_repr

```

---|---
####  tool_name `instance-attribute`
```
tool_name:

```

The name of the tool to call.
####  args `class-attribute` `instance-attribute`
```
args:  | [, ] | None = None

```

The arguments to pass to the tool.
This is stored either as a JSON string or a Python dictionary depending on how data was received.
####  tool_call_id `class-attribute` `instance-attribute`
```
tool_call_id:  = (
    default_factory=generate_tool_call_id
)

```

The tool call identifier, this is used by some models including OpenAI.
In case the tool call id is not provided by the model, Pydantic AI will generate a random one.
####  id `class-attribute` `instance-attribute`
```
id:  | None = None

```

An optional identifier of the tool call part, separate from the tool call ID.
This is used by some APIs like OpenAI Responses. When this field is set, `provider_name` is required to identify the provider that generated this data.
####  provider_name `class-attribute` `instance-attribute`
```
provider_name:  | None = None

```

The name of the provider that generated the response.
Builtin tool calls are only sent back to the same provider. Required to be set when `provider_details` or `id` is set.
####  provider_details `class-attribute` `instance-attribute`
```
provider_details: [, ] | None = None

```

Additional data returned by the provider that can't be mapped to standard fields.
This is used for data that is required to be sent back to APIs, as well as data users may want to access programmatically. When this field is set, `provider_name` is required to identify the provider that generated this data.
####  args_as_dict
```
args_as_dict() -> [, ]

```

Return the arguments as a Python dictionary.
This is just for convenience with models that require dicts as input.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1421
1422
1423
1424
1425
1426
1427
1428
1429
1430
1431
1432
```
| ```
def args_as_dict(self) -> dict[str, Any]:
    """Return the arguments as a Python dictionary.

    This is just for convenience with models that require dicts as input.
    """
    if not self.args:
        return {}
    if isinstance(self.args, dict):
        return self.args
    args = pydantic_core.from_json(self.args)
    assert isinstance(args, dict), 'args should be a dict'
    return cast(dict[str, Any], args)

```

---|---
####  args_as_json_str
```
args_as_json_str() ->

```

Return the arguments as a JSON string.
This is just for convenience with models that require JSON strings as input.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1434
1435
1436
1437
1438
1439
1440
1441
1442
1443
```
| ```
def args_as_json_str(self) -> str:
    """Return the arguments as a JSON string.

    This is just for convenience with models that require JSON strings as input.
    """
    if not self.args:
        return '{}'
    if isinstance(self.args, str):
        return self.args
    return pydantic_core.to_json(self.args).decode()

```

---|---
####  has_content
```
has_content() ->

```

Return `True` if the tool call has content.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1445
1446
1447
```
| ```
def has_content(self) -> bool:
    """Return `True` if the tool call has content."""
    return self.args not in ('', {}, None)

```

---|---
###  ToolCallPart `dataclass`
Bases: `BaseToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BaseToolCallPart "BaseToolCallPart



      dataclass
   \(pydantic_ai.messages.BaseToolCallPart\)")`
A tool call from a model.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1452
1453
1454
1455
1456
1457
1458
1459
```
| ```
@dataclass(repr=False)
class ToolCallPart(BaseToolCallPart):
    """A tool call from a model."""

    _: KW_ONLY

    part_kind: Literal['tool-call'] = 'tool-call'
    """Part type identifier, this is available on all parts as a discriminator. Note that this is different from `ToolCallPartDelta.part_delta_kind`."""

```

---|---
####  part_kind `class-attribute` `instance-attribute`
```
part_kind: ['tool-call'] = 'tool-call'

```

Part type identifier, this is available on all parts as a discriminator. Note that this is different from `ToolCallPartDelta.part_delta_kind`.
###  BuiltinToolCallPart `dataclass`
Bases: `BaseToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BaseToolCallPart "BaseToolCallPart



      dataclass
   \(pydantic_ai.messages.BaseToolCallPart\)")`
A tool call to a built-in tool.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1462
1463
1464
1465
1466
1467
1468
1469
```
| ```
@dataclass(repr=False)
class BuiltinToolCallPart(BaseToolCallPart):
    """A tool call to a built-in tool."""

    _: KW_ONLY

    part_kind: Literal['builtin-tool-call'] = 'builtin-tool-call'
    """Part type identifier, this is available on all parts as a discriminator."""

```

---|---
####  part_kind `class-attribute` `instance-attribute`
```
part_kind: ["builtin-tool-call"] = (
    "builtin-tool-call"
)

```

Part type identifier, this is available on all parts as a discriminator.
###  ModelResponsePart `module-attribute`
```
ModelResponsePart = [
    TextPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPart "TextPart



      dataclass
   \(pydantic_ai.messages.TextPart\)")
    | ToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart "ToolCallPart



      dataclass
   \(pydantic_ai.messages.ToolCallPart\)")
    | BuiltinToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolCallPart "BuiltinToolCallPart



      dataclass
   \(pydantic_ai.messages.BuiltinToolCallPart\)")
    | BuiltinToolReturnPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BuiltinToolReturnPart "BuiltinToolReturnPart



      dataclass
   \(pydantic_ai.messages.BuiltinToolReturnPart\)")
    | ThinkingPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ThinkingPart "ThinkingPart



      dataclass
   \(pydantic_ai.messages.ThinkingPart\)")
    | FilePart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FilePart "FilePart



      dataclass
   \(pydantic_ai.messages.FilePart\)"),
    Discriminator[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Discriminator "pydantic.Discriminator")("part_kind"),
]

```

A message part returned by a model.
###  ModelResponse `dataclass`
A response from a model, e.g. a message from the model to the Pydantic AI app.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
1479
1480
1481
1482
1483
1484
1485
1486
1487
1488
1489
1490
1491
1492
1493
1494
1495
1496
1497
1498
1499
1500
1501
1502
1503
1504
1505
1506
1507
1508
1509
1510
1511
1512
1513
1514
1515
1516
1517
1518
1519
1520
1521
1522
1523
1524
1525
1526
1527
1528
1529
1530
1531
1532
1533
1534
1535
1536
1537
1538
1539
1540
1541
1542
1543
1544
1545
1546
1547
1548
1549
1550
1551
1552
1553
1554
1555
1556
1557
1558
1559
1560
1561
1562
1563
1564
1565
1566
1567
1568
1569
1570
1571
1572
1573
1574
1575
1576
1577
1578
1579
1580
1581
1582
1583
1584
1585
1586
1587
1588
1589
1590
1591
1592
1593
1594
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
1618
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
1666
1667
1668
1669
1670
1671
1672
1673
1674
1675
1676
1677
1678
1679
1680
1681
1682
1683
1684
1685
1686
1687
1688
1689
1690
1691
1692
1693
1694
1695
1696
1697
1698
1699
1700
1701
1702
1703
1704
1705
1706
1707
1708
1709
1710
1711
1712
1713
1714
1715
1716
1717
1718
1719
1720
1721
1722
1723
1724
1725
1726
1727
1728
1729
1730
1731
```
| ```
@dataclass(repr=False)
class ModelResponse:
    """A response from a model, e.g. a message from the model to the Pydantic AI app."""

    parts: Sequence[ModelResponsePart]
    """The parts of the model message."""

    _: KW_ONLY

    usage: RequestUsage = field(default_factory=RequestUsage)
    """Usage information for the request.

    This has a default to make tests easier, and to support loading old messages where usage will be missing.
    """

    model_name: str | None = None
    """The name of the model that generated the response."""

    timestamp: datetime = field(default_factory=_now_utc)
    """The timestamp when the response was received locally.

    This is always a high-precision local datetime. Provider-specific timestamps
    (if available) are stored in `provider_details['timestamp']`.
    """

    kind: Literal['response'] = 'response'
    """Message type identifier, this is available on all parts as a discriminator."""

    provider_name: str | None = None
    """The name of the LLM provider that generated the response."""

    provider_url: str | None = None
    """The base URL of the LLM provider that generated the response."""

    provider_details: Annotated[
        dict[str, Any] | None,
        # `vendor_details` is deprecated, but we still want to support deserializing model responses stored in a DB before the name was changed
        pydantic.Field(validation_alias=pydantic.AliasChoices('provider_details', 'vendor_details')),
    ] = None
    """Additional data returned by the provider that can't be mapped to standard fields."""

    provider_response_id: Annotated[
        str | None,
        # `vendor_id` is deprecated, but we still want to support deserializing model responses stored in a DB before the name was changed
        pydantic.Field(validation_alias=pydantic.AliasChoices('provider_response_id', 'vendor_id')),
    ] = None
    """request ID as specified by the model provider. This can be used to track the specific request to the model."""

    finish_reason: FinishReason | None = None
    """Reason the model finished generating the response, normalized to OpenTelemetry values."""

    run_id: str | None = None
    """The unique identifier of the agent run in which this message originated."""

    metadata: dict[str, Any] | None = None
    """Additional data that can be accessed programmatically by the application but is not sent to the LLM."""

    @property
    def text(self) -> str | None:
        """Get the text in the response."""
        texts: list[str] = []
        last_part: ModelResponsePart | None = None
        for part in self.parts:
            if isinstance(part, TextPart):
                # Adjacent text parts should be joined together, but if there are parts in between
                # (like built-in tool calls) they should have newlines between them
                if isinstance(last_part, TextPart):
                    texts[-1] += part.content
                else:
                    texts.append(part.content)
            last_part = part
        if not texts:
            return None

        return '\n\n'.join(texts)

    @property
    def thinking(self) -> str | None:
        """Get the thinking in the response."""
        thinking_parts = [part.content for part in self.parts if isinstance(part, ThinkingPart)]
        if not thinking_parts:
            return None
        return '\n\n'.join(thinking_parts)

    @property
    def files(self) -> list[BinaryContent]:
        """Get the files in the response."""
        return [part.content for part in self.parts if isinstance(part, FilePart)]

    @property
    def images(self) -> list[BinaryImage]:
        """Get the images in the response."""
        return [file for file in self.files if isinstance(file, BinaryImage)]

    @property
