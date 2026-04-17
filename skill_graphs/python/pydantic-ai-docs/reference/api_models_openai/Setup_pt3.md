                openai_messages.append(self._map_model_response(message))
            else:
                assert_never(message)
        if instructions := self._get_instructions(messages, model_request_parameters):
            system_prompt_count = sum(1 for m in openai_messages if m.get('role') == 'system')
            openai_messages.insert(
                system_prompt_count, chat.ChatCompletionSystemMessageParam(content=instructions, role='system')
            )
        return openai_messages

    @staticmethod
    def _map_tool_call(t: ToolCallPart) -> ChatCompletionMessageFunctionToolCallParam:
        return ChatCompletionMessageFunctionToolCallParam(
            id=_guard_tool_call_id(t=t),
            type='function',
            function={'name': t.tool_name, 'arguments': t.args_as_json_str()},
        )

    def _map_json_schema(self, o: OutputObjectDefinition) -> chat.completion_create_params.ResponseFormat:
        response_format_param: chat.completion_create_params.ResponseFormatJSONSchema = {  # pyright: ignore[reportPrivateImportUsage]
            'type': 'json_schema',
            'json_schema': {'name': o.name or DEFAULT_OUTPUT_TOOL_NAME, 'schema': o.json_schema},
        }
        if o.description:
            response_format_param['json_schema']['description'] = o.description
        if OpenAIModelProfile.from_profile(self.profile).openai_supports_strict_tool_definition:  # pragma: no branch
            response_format_param['json_schema']['strict'] = o.strict
        return response_format_param

    def _map_tool_definition(self, f: ToolDefinition) -> chat.ChatCompletionToolParam:
        tool_param: chat.ChatCompletionToolParam = {
            'type': 'function',
            'function': {
                'name': f.name,
                'description': f.description or '',
                'parameters': f.parameters_json_schema,
            },
        }
        if f.strict and OpenAIModelProfile.from_profile(self.profile).openai_supports_strict_tool_definition:
            tool_param['function']['strict'] = f.strict
        return tool_param

    async def _map_user_message(self, message: ModelRequest) -> AsyncIterable[chat.ChatCompletionMessageParam]:
        for part in message.parts:
            if isinstance(part, SystemPromptPart):
                system_prompt_role = OpenAIModelProfile.from_profile(self.profile).openai_system_prompt_role
                if system_prompt_role == 'developer':
                    yield chat.ChatCompletionDeveloperMessageParam(role='developer', content=part.content)
                elif system_prompt_role == 'user':
                    yield chat.ChatCompletionUserMessageParam(role='user', content=part.content)
                else:
                    yield chat.ChatCompletionSystemMessageParam(role='system', content=part.content)
            elif isinstance(part, UserPromptPart):
                yield await self._map_user_prompt(part)
            elif isinstance(part, ToolReturnPart):
                yield chat.ChatCompletionToolMessageParam(
                    role='tool',
                    tool_call_id=_guard_tool_call_id(t=part),
                    content=part.model_response_str(),
                )
            elif isinstance(part, RetryPromptPart):
                if part.tool_name is None:
                    yield chat.ChatCompletionUserMessageParam(role='user', content=part.model_response())
                else:
                    yield chat.ChatCompletionToolMessageParam(
                        role='tool',
                        tool_call_id=_guard_tool_call_id(t=part),
                        content=part.model_response(),
                    )
            else:
                assert_never(part)

    async def _map_image_url_item(self, item: ImageUrl) -> ChatCompletionContentPartImageParam:
        """Map an ImageUrl to a chat completion image content part."""
        image_url: ImageURL = {'url': item.url}
        if metadata := item.vendor_metadata:
            image_url['detail'] = metadata.get('detail', 'auto')
        if item.force_download:
            image_content = await download_item(item, data_format='base64_uri', type_format='extension')
            image_url['url'] = image_content['data']
        return ChatCompletionContentPartImageParam(image_url=image_url, type='image_url')

    async def _map_binary_content_item(self, item: BinaryContent) -> ChatCompletionContentPartParam:
        """Map a BinaryContent item to a chat completion content part."""
        profile = OpenAIModelProfile.from_profile(self.profile)
        if self._is_text_like_media_type(item.media_type):
            # Inline text-like binary content as a text block
            return self._inline_text_file_part(
                item.data.decode('utf-8'),
                media_type=item.media_type,
                identifier=item.identifier,
            )
        elif item.is_image:
            image_url = ImageURL(url=item.data_uri)
            if metadata := item.vendor_metadata:
                image_url['detail'] = metadata.get('detail', 'auto')
            return ChatCompletionContentPartImageParam(image_url=image_url, type='image_url')
        elif item.is_audio:
            assert item.format in ('wav', 'mp3')
            if profile.openai_chat_audio_input_encoding == 'uri':
                audio = InputAudio(data=item.data_uri, format=item.format)
            else:
                audio = InputAudio(data=item.base64, format=item.format)
            return ChatCompletionContentPartInputAudioParam(input_audio=audio, type='input_audio')
        elif item.is_document:
            return File(
                file=FileFile(
                    file_data=item.data_uri,
                    filename=f'filename.{item.format}',
                ),
                type='file',
            )
        else:  # pragma: no cover
            raise RuntimeError(f'Unsupported binary content type: {item.media_type}')

    async def _map_audio_url_item(self, item: AudioUrl) -> ChatCompletionContentPartInputAudioParam:
        """Map an AudioUrl to a chat completion audio content part."""
        profile = OpenAIModelProfile.from_profile(self.profile)
        data_format = 'base64_uri' if profile.openai_chat_audio_input_encoding == 'uri' else 'base64'
        downloaded_item = await download_item(item, data_format=data_format, type_format='extension')
        assert downloaded_item['data_type'] in (
            'wav',
            'mp3',
        ), f'Unsupported audio format: {downloaded_item["data_type"]}'
        audio = InputAudio(data=downloaded_item['data'], format=downloaded_item['data_type'])
        return ChatCompletionContentPartInputAudioParam(input_audio=audio, type='input_audio')

    async def _map_document_url_item(self, item: DocumentUrl) -> ChatCompletionContentPartParam:
        """Map a DocumentUrl to a chat completion content part."""
        profile = OpenAIModelProfile.from_profile(self.profile)
        # OpenAI Chat API's FileFile only supports base64-encoded data, not URLs.
        # Some providers (e.g., OpenRouter) support URLs via the profile flag.
        if not item.force_download and profile.openai_chat_supports_file_urls:
            return File(
                file=FileFile(
                    file_data=item.url,
                    filename=f'filename.{item.format}',
                ),
                type='file',
            )
        if self._is_text_like_media_type(item.media_type):
            downloaded_text = await download_item(item, data_format='text')
            return self._inline_text_file_part(
                downloaded_text['data'],
                media_type=item.media_type,
                identifier=item.identifier,
            )
        else:
            downloaded_item = await download_item(item, data_format='base64_uri', type_format='extension')
            return File(
                file=FileFile(
                    file_data=downloaded_item['data'],
                    filename=f'filename.{downloaded_item["data_type"]}',
                ),
                type='file',
            )

    async def _map_video_url_item(self, item: VideoUrl) -> ChatCompletionContentPartParam:  # pragma: no cover
        """Map a VideoUrl to a chat completion content part."""
        raise NotImplementedError('VideoUrl is not supported for OpenAI')

    async def _map_content_item(
        self, item: str | ImageUrl | BinaryContent | AudioUrl | DocumentUrl | VideoUrl | UploadedFile | CachePoint
    ) -> ChatCompletionContentPartParam | None:
        """Map a single content item to a chat completion content part, or None to filter it out."""
        if isinstance(item, str):
            return ChatCompletionContentPartTextParam(text=item, type='text')
        elif isinstance(item, ImageUrl):
            return await self._map_image_url_item(item)
        elif isinstance(item, BinaryContent):
            return await self._map_binary_content_item(item)
        elif isinstance(item, AudioUrl):
            return await self._map_audio_url_item(item)
        elif isinstance(item, DocumentUrl):
            return await self._map_document_url_item(item)
        elif isinstance(item, VideoUrl):
            return await self._map_video_url_item(item)
        elif isinstance(item, UploadedFile):
            # Verify provider matches
            if item.provider_name != self.system:
                raise UserError(
                    f'UploadedFile with `provider_name={item.provider_name!r}` cannot be used with OpenAIChatModel. '
                    f'Expected `provider_name` to be `{self.system!r}`.'
                )
            return File(
                file=FileFile(file_id=item.file_id),
                type='file',
            )
        elif isinstance(item, CachePoint):
            # OpenAI doesn't support prompt caching via CachePoint, so we filter it out
            return None
        else:
            assert_never(item)

    async def _map_user_prompt(self, part: UserPromptPart) -> chat.ChatCompletionUserMessageParam:
        content: str | list[ChatCompletionContentPartParam]
        if isinstance(part.content, str):
            content = part.content
        else:
            content = []
            for item in part.content:
                mapped_item = await self._map_content_item(item)
                if mapped_item is not None:
                    content.append(mapped_item)
        return chat.ChatCompletionUserMessageParam(role='user', content=content)

    @staticmethod
    def _is_text_like_media_type(media_type: str) -> bool:
        return (
            media_type.startswith('text/')
            or media_type == 'application/json'
            or media_type.endswith('+json')
            or media_type == 'application/xml'
            or media_type.endswith('+xml')
            or media_type in ('application/x-yaml', 'application/yaml')
        )

    @staticmethod
    def _inline_text_file_part(text: str, *, media_type: str, identifier: str) -> ChatCompletionContentPartTextParam:
        text = '\n'.join(
            [
                f'-----BEGIN FILE id="{identifier}" type="{media_type}"-----',
                text,
                f'-----END FILE id="{identifier}"-----',
            ]
        )
        return ChatCompletionContentPartTextParam(text=text, type='text')

```

---|---
####  __init__
```
__init__(
    model_name: OpenAIModelName[](https://ai.pydantic.dev/api/models/openai/#pydantic_ai.models.openai.OpenAIModelName "OpenAIModelName



      module-attribute
   \(pydantic_ai.models.openai.OpenAIModelName\)"),
    *,
    provider: (
        OpenAIChatCompatibleProvider
        | ["openai", "openai-chat", "gateway"]
        | Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[AsyncOpenAI]
    ) = "openai",
    profile: ModelProfileSpec | None = None,
    settings: ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None = None
) -> None

```

```
__init__(
    model_name: OpenAIModelName[](https://ai.pydantic.dev/api/models/openai/#pydantic_ai.models.openai.OpenAIModelName "OpenAIModelName



      module-attribute
   \(pydantic_ai.models.openai.OpenAIModelName\)"),
    *,
    provider: (
        OpenAIChatCompatibleProvider
        | ["openai", "openai-chat", "gateway"]
        | Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[AsyncOpenAI]
    ) = "openai",
    profile: ModelProfileSpec | None = None,
    system_prompt_role: (
        OpenAISystemPromptRole | None
    ) = None,
    settings: ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None = None
) -> None

```

```
__init__(
    model_name: OpenAIModelName[](https://ai.pydantic.dev/api/models/openai/#pydantic_ai.models.openai.OpenAIModelName "OpenAIModelName



      module-attribute
   \(pydantic_ai.models.openai.OpenAIModelName\)"),
    *,
    provider: (
        OpenAIChatCompatibleProvider
        | ["openai", "openai-chat", "gateway"]
        | Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[AsyncOpenAI]
    ) = "openai",
    profile: ModelProfileSpec | None = None,
    system_prompt_role: (
        OpenAISystemPromptRole | None
    ) = None,
    settings: ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None = None
)

```

Initialize an OpenAI model.
Parameters:
Name | Type | Description | Default
---|---|---|---
`model_name` |  `OpenAIModelName[](https://ai.pydantic.dev/api/models/openai/#pydantic_ai.models.openai.OpenAIModelName "OpenAIModelName



      module-attribute
   \(pydantic_ai.models.openai.OpenAIModelName\)")` |  The name of the OpenAI model to use. List of model names available `.inv` files for their API). |  _required_
`provider` |  `OpenAIChatCompatibleProvider | Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[AsyncOpenAI]` |  The provider to use. Defaults to `'openai'`. |  `'openai'`
`profile` |  `ModelProfileSpec | None` |  The model profile to use. Defaults to a profile picked by the provider based on the model name. |  `None`
`system_prompt_role` |  `OpenAISystemPromptRole | None` |  The role to use for the system prompt message. If not provided, defaults to `'system'`. In the future, this may be inferred from the model name. |  `None`
`settings` |  `ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None` |  Default model settings for this model instance. |  `None`
Source code in `pydantic_ai_slim/pydantic_ai/models/openai.py`
```
517
518
519
520
521
522
523
524
525
526
527
528
529
530
531
532
533
534
535
536
537
538
539
540
541
542
543
544
545
546
547
548
549
550
551
552
553
554
```
| ```
def __init__(
    self,
    model_name: OpenAIModelName,
    *,
    provider: OpenAIChatCompatibleProvider
    | Literal[
        'openai',
        'openai-chat',
        'gateway',
    ]
    | Provider[AsyncOpenAI] = 'openai',
    profile: ModelProfileSpec | None = None,
    system_prompt_role: OpenAISystemPromptRole | None = None,
    settings: ModelSettings | None = None,
):
    """Initialize an OpenAI model.

    Args:
        model_name: The name of the OpenAI model to use. List of model names available
            [here](https://github.com/openai/openai-python/blob/v1.54.3/src/openai/types/chat_model.py#L7)
            (Unfortunately, despite being ask to do so, OpenAI do not provide `.inv` files for their API).
        provider: The provider to use. Defaults to `'openai'`.
        profile: The model profile to use. Defaults to a profile picked by the provider based on the model name.
        system_prompt_role: The role to use for the system prompt message. If not provided, defaults to `'system'`.
            In the future, this may be inferred from the model name.
        settings: Default model settings for this model instance.
    """
    self._model_name = model_name

    if isinstance(provider, str):
        provider = infer_provider('gateway/openai' if provider == 'gateway' else provider)
    self._provider = provider
    self.client = provider.client

    super().__init__(settings=settings, profile=profile or provider.model_profile)

    if system_prompt_role is not None:
        self.profile = OpenAIModelProfile(openai_system_prompt_role=system_prompt_role).update(self.profile)

```

---|---
####  model_name `property`
```
model_name: OpenAIModelName[](https://ai.pydantic.dev/api/models/openai/#pydantic_ai.models.openai.OpenAIModelName "OpenAIModelName



      module-attribute
   \(pydantic_ai.models.openai.OpenAIModelName\)")

```

The model name.
####  system `property`
```
system:

```

The model provider.
####  supported_builtin_tools `classmethod`
```
supported_builtin_tools() -> (
    [[AbstractBuiltinTool[](https://ai.pydantic.dev/api/builtin_tools/#pydantic_ai.builtin_tools.AbstractBuiltinTool "AbstractBuiltinTool



      dataclass
   \(pydantic_ai.builtin_tools.AbstractBuiltinTool\)")]]
)

```

Return the set of builtin tool types this model can handle.
Source code in `pydantic_ai_slim/pydantic_ai/models/openai.py`
```
570
571
572
573
```
| ```
@classmethod
def supported_builtin_tools(cls) -> frozenset[type[AbstractBuiltinTool]]:
    """Return the set of builtin tool types this model can handle."""
    return frozenset({WebSearchTool})

```

---|---
####  profile `cached` `property`
```
profile: ModelProfile[](https://ai.pydantic.dev/api/profiles/#pydantic_ai.profiles.ModelProfile "pydantic_ai.profiles.ModelProfile")

```

The model profile.
WebSearchTool is only supported if openai_chat_supports_web_search is True.
###  OpenAIModel `dataclass` `deprecated`
Bases: `OpenAIChatModel[](https://ai.pydantic.dev/api/models/openai/#pydantic_ai.models.openai.OpenAIChatModel "OpenAIChatModel



      dataclass
   \(pydantic_ai.models.openai.OpenAIChatModel\)")`
Deprecated
`OpenAIModel` was renamed to `OpenAIChatModel` to clearly distinguish it from `OpenAIResponsesModel` which uses OpenAI's newer Responses API. Use that unless you're using an OpenAI Chat Completions-compatible API, or require a feature that the Responses API doesn't support yet like audio.
Deprecated alias for `OpenAIChatModel`.
Source code in `pydantic_ai_slim/pydantic_ai/models/openai.py`
```
1323
1324
1325
1326
1327
1328
1329
1330
```
| ```
@deprecated(
    '`OpenAIModel` was renamed to `OpenAIChatModel` to clearly distinguish it from `OpenAIResponsesModel` which '
    "uses OpenAI's newer Responses API. Use that unless you're using an OpenAI Chat Completions-compatible API, or "
    "require a feature that the Responses API doesn't support yet like audio."
)
@dataclass(init=False)
class OpenAIModel(OpenAIChatModel):
    """Deprecated alias for `OpenAIChatModel`."""

```

---|---
###  OpenAIResponsesModel `dataclass`
Bases: `Model[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.Model "Model \(pydantic_ai.models.Model\)")`
A model that uses the OpenAI Responses API.
The
If you are interested in the differences between the Responses API and the Chat Completions API, see the
Source code in `pydantic_ai_slim/pydantic_ai/models/openai.py`
```
1336
1337
1338
1339
1340
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
1377
1378
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
1450
1451
1452
1453
1454
1455
1456
1457
1458
1459
1460
1461
1462
1463
1464
1465
1466
1467
1468
1469
1470
1471
1472
1473
1474
1475
1476
1477
1478
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
1732
1733
1734
1735
1736
1737
1738
1739
1740
1741
1742
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
1791
1792
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
1900
1901
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
2064
2065
2066
2067
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
2083
2084
2085
2086
2087
2088
2089
2090
2091
2092
2093
2094
2095
2096
2097
2098
2099
2100
2101
2102
2103
2104
2105
2106
2107
2108
2109
2110
2111
2112
2113
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
2128
2129
2130
2131
2132
2133
2134
2135
2136
2137
2138
2139
2140
2141
2142
2143
2144
2145
2146
2147
2148
2149
2150
2151
2152
2153
2154
2155
2156
2157
2158
2159
2160
2161
2162
2163
2164
2165
2166
2167
2168
2169
2170
2171
2172
2173
2174
2175
2176
2177
2178
2179
2180
2181
2182
2183
2184
2185
2186
2187
2188
2189
2190
2191
2192
2193
2194
2195
2196
2197
2198
2199
2200
2201
2202
2203
2204
2205
2206
2207
2208
2209
2210
2211
2212
2213
2214
2215
2216
2217
2218
2219
2220
2221
2222
2223
2224
2225
2226
2227
2228
2229
2230
2231
2232
2233
2234
2235
2236
2237
2238
2239
2240
2241
2242
2243
2244
2245
2246
2247
2248
2249
2250
2251
2252
```
| ```
@dataclass(init=False)
class OpenAIResponsesModel(Model):
    """A model that uses the OpenAI Responses API.

    The [OpenAI Responses API](https://platform.openai.com/docs/api-reference/responses) is the
    new API for OpenAI models.

    If you are interested in the differences between the Responses API and the Chat Completions API,
    see the [OpenAI API docs](https://platform.openai.com/docs/guides/responses-vs-chat-completions).
    """

    client: AsyncOpenAI = field(repr=False)

    _model_name: OpenAIModelName = field(repr=False)
    _provider: Provider[AsyncOpenAI] = field(repr=False)

    def __init__(
        self,
        model_name: OpenAIModelName,
        *,
        provider: OpenAIResponsesCompatibleProvider
        | Literal[
            'openai',
            'gateway',
        ]
        | Provider[AsyncOpenAI] = 'openai',
        profile: ModelProfileSpec | None = None,
        settings: ModelSettings | None = None,
    ):
        """Initialize an OpenAI Responses model.

        Args:
            model_name: The name of the OpenAI model to use.
            provider: The provider to use. Defaults to `'openai'`.
            profile: The model profile to use. Defaults to a profile picked by the provider based on the model name.
            settings: Default model settings for this model instance.
