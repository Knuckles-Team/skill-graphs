`default_response_class` |  The default response class to be used. Read more in the [FastAPI docs for Custom Response - HTML, Stream, File, others](https://fastapi.tiangolo.com/advanced/custom-response/#default-response-class). **TYPE:** `type[Response[](https://fastapi.tiangolo.com/reference/response/#fastapi.Response "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">fastapi.Response</span> \(<code>starlette.responses.Response</code>\)")]` **DEFAULT:** `Default(JSONResponse[](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.JSONResponse "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">fastapi.responses.JSONResponse</span> \(<code>starlette.responses.JSONResponse</code>\)"))`
`responses` |  Additional responses to be shown in OpenAPI. It will be added to the generated OpenAPI (e.g. visible at `/docs`). Read more about it in the [FastAPI docs for Additional Responses in OpenAPI](https://fastapi.tiangolo.com/advanced/additional-responses/). And in the [FastAPI docs for Bigger Applications](https://fastapi.tiangolo.com/tutorial/bigger-applications/#include-an-apirouter-with-a-custom-prefix-tags-responses-and-dependencies). **TYPE:** `dict[int | str, dict[str, Any]] | None` **DEFAULT:** `None`
`callbacks` |  OpenAPI callbacks that should apply to all _path operations_ in this router. It will be added to the generated OpenAPI (e.g. visible at `/docs`). Read more about it in the [FastAPI docs for OpenAPI Callbacks](https://fastapi.tiangolo.com/advanced/openapi-callbacks/). **TYPE:** `list[BaseRoute] | None` **DEFAULT:** `None`
`deprecated` |  Mark all _path operations_ in this router as deprecated. It will be added to the generated OpenAPI (e.g. visible at `/docs`). Read more about it in the [FastAPI docs for Path Operation Configuration](https://fastapi.tiangolo.com/tutorial/path-operation-configuration/). **TYPE:** `bool | None` **DEFAULT:** `None`
`include_in_schema` |  Include (or not) all the _path operations_ in this router in the generated OpenAPI schema. This affects the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `bool` **DEFAULT:** `True`
`generate_unique_id_function` |  Customize the function used to generate unique IDs for the _path operations_ shown in the generated OpenAPI. This is particularly useful when automatically generating clients or SDKs for your API. Read more about it in the [FastAPI docs about how to Generate Clients](https://fastapi.tiangolo.com/advanced/generate-clients/#custom-generate-unique-id-function). **TYPE:** `Callable[[APIRoute], str]` **DEFAULT:** `Default(generate_unique_id)`
Source code in `fastapi/routing.py`
```
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
```
| ```
def include_router(
    self,
    router: Annotated["APIRouter", Doc("The `APIRouter` to include.")],
    *,
    prefix: Annotated[str, Doc("An optional path prefix for the router.")] = "",
    tags: Annotated[
        list[str | Enum] | None,
        Doc(
            """
            A list of tags to be applied to all the *path operations* in this
            router.

            It will be added to the generated OpenAPI (e.g. visible at `/docs`).

            Read more about it in the
            [FastAPI docs for Path Operation Configuration](https://fastapi.tiangolo.com/tutorial/path-operation-configuration/).
            """
        ),
    ] = None,
    dependencies: Annotated[
        Sequence[params.Depends] | None,
        Doc(
            """
            A list of dependencies (using `Depends()`) to be applied to all the
            *path operations* in this router.

            Read more about it in the
            [FastAPI docs for Bigger Applications - Multiple Files](https://fastapi.tiangolo.com/tutorial/bigger-applications/#include-an-apirouter-with-a-custom-prefix-tags-responses-and-dependencies).
            """
        ),
    ] = None,
    default_response_class: Annotated[
        type[Response],
        Doc(
            """
            The default response class to be used.

            Read more in the
            [FastAPI docs for Custom Response - HTML, Stream, File, others](https://fastapi.tiangolo.com/advanced/custom-response/#default-response-class).
            """
        ),
    ] = Default(JSONResponse),
    responses: Annotated[
        dict[int | str, dict[str, Any]] | None,
        Doc(
            """
            Additional responses to be shown in OpenAPI.

            It will be added to the generated OpenAPI (e.g. visible at `/docs`).

            Read more about it in the
            [FastAPI docs for Additional Responses in OpenAPI](https://fastapi.tiangolo.com/advanced/additional-responses/).

            And in the
            [FastAPI docs for Bigger Applications](https://fastapi.tiangolo.com/tutorial/bigger-applications/#include-an-apirouter-with-a-custom-prefix-tags-responses-and-dependencies).
            """
        ),
    ] = None,
    callbacks: Annotated[
        list[BaseRoute] | None,
        Doc(
            """
            OpenAPI callbacks that should apply to all *path operations* in this
            router.

            It will be added to the generated OpenAPI (e.g. visible at `/docs`).

            Read more about it in the
            [FastAPI docs for OpenAPI Callbacks](https://fastapi.tiangolo.com/advanced/openapi-callbacks/).
            """
        ),
    ] = None,
    deprecated: Annotated[
        bool | None,
        Doc(
            """
            Mark all *path operations* in this router as deprecated.

            It will be added to the generated OpenAPI (e.g. visible at `/docs`).

            Read more about it in the
            [FastAPI docs for Path Operation Configuration](https://fastapi.tiangolo.com/tutorial/path-operation-configuration/).
            """
        ),
    ] = None,
    include_in_schema: Annotated[
        bool,
        Doc(
            """
            Include (or not) all the *path operations* in this router in the
            generated OpenAPI schema.

            This affects the generated OpenAPI (e.g. visible at `/docs`).
            """
        ),
    ] = True,
    generate_unique_id_function: Annotated[
        Callable[[APIRoute], str],
        Doc(
            """
            Customize the function used to generate unique IDs for the *path
            operations* shown in the generated OpenAPI.

            This is particularly useful when automatically generating clients or
            SDKs for your API.

            Read more about it in the
            [FastAPI docs about how to Generate Clients](https://fastapi.tiangolo.com/advanced/generate-clients/#custom-generate-unique-id-function).
            """
        ),
    ] = Default(generate_unique_id),
) -> None:
    """
    Include another `APIRouter` in the same current `APIRouter`.

    Read more about it in the
    [FastAPI docs for Bigger Applications](https://fastapi.tiangolo.com/tutorial/bigger-applications/).

    ## Example

```python
    from fastapi import APIRouter, FastAPI

    app = FastAPI()
    internal_router = APIRouter()
    users_router = APIRouter()

    @users_router.get("/users/")
    def read_users():
        return [{"name": "Rick"}, {"name": "Morty"}]

    internal_router.include_router(users_router)
    app.include_router(internal_router)
```
    """
    assert self is not router, (
        "Cannot include the same APIRouter instance into itself. "
        "Did you mean to include a different router?"
    )
    if prefix:
        assert prefix.startswith("/"), "A path prefix must start with '/'"
        assert not prefix.endswith("/"), (
            "A path prefix must not end with '/', as the routes will start with '/'"
        )
    else:
        for r in router.routes:
            path = getattr(r, "path")  # noqa: B009
            name = getattr(r, "name", "unknown")
            if path is not None and not path:
                raise FastAPIError(
                    f"Prefix and path cannot be both empty (path operation: {name})"
                )
    if responses is None:
        responses = {}
    for route in router.routes:
        if isinstance(route, APIRoute):
            combined_responses = {**responses, **route.responses}
            use_response_class = get_value_or_default(
                route.response_class,
                router.default_response_class,
                default_response_class,
                self.default_response_class,
            )
            current_tags = []
            if tags:
                current_tags.extend(tags)
            if route.tags:
                current_tags.extend(route.tags)
            current_dependencies: list[params.Depends] = []
            if dependencies:
                current_dependencies.extend(dependencies)
            if route.dependencies:
                current_dependencies.extend(route.dependencies)
            current_callbacks = []
            if callbacks:
                current_callbacks.extend(callbacks)
            if route.callbacks:
                current_callbacks.extend(route.callbacks)
            current_generate_unique_id = get_value_or_default(
                route.generate_unique_id_function,
                router.generate_unique_id_function,
                generate_unique_id_function,
                self.generate_unique_id_function,
            )
            self.add_api_route(
                prefix + route.path,
                route.endpoint,
                response_model=route.response_model,
                status_code=route.status_code,
                tags=current_tags,
                dependencies=current_dependencies,
                summary=route.summary,
                description=route.description,
                response_description=route.response_description,
                responses=combined_responses,
                deprecated=route.deprecated or deprecated or self.deprecated,
                methods=route.methods,
                operation_id=route.operation_id,
                response_model_include=route.response_model_include,
                response_model_exclude=route.response_model_exclude,
                response_model_by_alias=route.response_model_by_alias,
                response_model_exclude_unset=route.response_model_exclude_unset,
                response_model_exclude_defaults=route.response_model_exclude_defaults,
                response_model_exclude_none=route.response_model_exclude_none,
                include_in_schema=route.include_in_schema
                and self.include_in_schema
                and include_in_schema,
                response_class=use_response_class,
                name=route.name,
                route_class_override=type(route),
                callbacks=current_callbacks,
                openapi_extra=route.openapi_extra,
                generate_unique_id_function=current_generate_unique_id,
                strict_content_type=get_value_or_default(
                    route.strict_content_type,
                    router.strict_content_type,
                    self.strict_content_type,
                ),
            )
        elif isinstance(route, routing.Route):
            methods = list(route.methods or [])
            self.add_route(
                prefix + route.path,
                route.endpoint,
                methods=methods,
                include_in_schema=route.include_in_schema,
                name=route.name,
            )
        elif isinstance(route, APIWebSocketRoute):
            current_dependencies = []
            if dependencies:
                current_dependencies.extend(dependencies)
            if route.dependencies:
                current_dependencies.extend(route.dependencies)
            self.add_api_websocket_route(
                prefix + route.path,
                route.endpoint,
                dependencies=current_dependencies,
                name=route.name,
            )
        elif isinstance(route, routing.WebSocketRoute):
            self.add_websocket_route(
                prefix + route.path, route.endpoint, name=route.name
            )
    for handler in router.on_startup:
        self.add_event_handler("startup", handler)
    for handler in router.on_shutdown:
        self.add_event_handler("shutdown", handler)
    self.lifespan_context = _merge_lifespan_context(
        self.lifespan_context,
        router.lifespan_context,
    )

```

---|---
###  get [¶](https://fastapi.tiangolo.com/reference/apirouter/#fastapi.APIRouter.get "Permanent link")
```
get(
    path,
    *,
    response_model=Default(None),
    status_code=None,
    tags=None,
    dependencies=None,
    summary=None,
    description=None,
    response_description="Successful Response",
    responses=None,
    deprecated=None,
    operation_id=None,
    response_model_include=None,
    response_model_exclude=None,
    response_model_by_alias=True,
    response_model_exclude_unset=False,
    response_model_exclude_defaults=False,
    response_model_exclude_none=False,
    include_in_schema=True,
    response_class=Default(JSONResponse[](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.JSONResponse "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">fastapi.responses.JSONResponse</span> \(<code>starlette.responses.JSONResponse</code>\)")),
    name=None,
    callbacks=None,
    openapi_extra=None,
    generate_unique_id_function=Default(generate_unique_id)
)

```

Add a _path operation_ using an HTTP GET operation.
##### Example[¶](https://fastapi.tiangolo.com/reference/apirouter/#fastapi.APIRouter.get--example)
```
from fastapi import APIRouter, FastAPI

app = FastAPI()
router = APIRouter()

@router.get("/items/")
def read_items():
    return [{"name": "Empanada"}, {"name": "Arepa"}]

app.include_router(router)

```

PARAMETER | DESCRIPTION
---|---
`path` |  The URL path to be used for this _path operation_. For example, in `http://example.com/items`, the path is `/items`. **TYPE:** `str`
`response_model` |  The type to use for the response. It could be any valid Pydantic _field_ type. So, it doesn't have to be a Pydantic model, it could be other things, like a `list`, `dict`, etc. It will be used for:
  * Documentation: the generated OpenAPI (and the UI at `/docs`) will show it as the response (JSON Schema).
  * Serialization: you could return an arbitrary object and the `response_model` would be used to serialize that object into the corresponding JSON.
  * Filtering: the JSON sent to the client will only contain the data (fields) defined in the `response_model`. If you returned an object that contains an attribute `password` but the `response_model` does not include that field, the JSON sent to the client would not have that `password`.
  * Validation: whatever you return will be serialized with the `response_model`, converting any data as necessary to generate the corresponding JSON. But if the data in the object returned is not valid, that would mean a violation of the contract with the client, so it's an error from the API developer. So, FastAPI will raise an error and return a 500 error code (Internal Server Error).

Read more about it in the [FastAPI docs for Response Model](https://fastapi.tiangolo.com/tutorial/response-model/). **TYPE:** `Any` **DEFAULT:** `Default(None)`
`status_code` |  The default status code to be used for the response. You could override the status code by returning a response directly. Read more about it in the [FastAPI docs for Response Status Code](https://fastapi.tiangolo.com/tutorial/response-status-code/). **TYPE:** `int | None` **DEFAULT:** `None`
`tags` |  A list of tags to be applied to the _path operation_. It will be added to the generated OpenAPI (e.g. visible at `/docs`). Read more about it in the [FastAPI docs for Path Operation Configuration](https://fastapi.tiangolo.com/tutorial/path-operation-configuration/#tags). **TYPE:** `list[str | Enum] | None` **DEFAULT:** `None`
`dependencies` |  A list of dependencies (using `Depends()`) to be applied to the _path operation_. Read more about it in the [FastAPI docs for Dependencies in path operation decorators](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-in-path-operation-decorators/). **TYPE:** `Sequence[Depends] | None` **DEFAULT:** `None`
`summary` |  A summary for the _path operation_. It will be added to the generated OpenAPI (e.g. visible at `/docs`). Read more about it in the [FastAPI docs for Path Operation Configuration](https://fastapi.tiangolo.com/tutorial/path-operation-configuration/). **TYPE:** `str | None` **DEFAULT:** `None`
`description` |  A description for the _path operation_. If not provided, it will be extracted automatically from the docstring of the _path operation function_. It can contain Markdown. It will be added to the generated OpenAPI (e.g. visible at `/docs`). Read more about it in the [FastAPI docs for Path Operation Configuration](https://fastapi.tiangolo.com/tutorial/path-operation-configuration/). **TYPE:** `str | None` **DEFAULT:** `None`
`response_description` |  The description for the default response. It will be added to the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `str` **DEFAULT:** `'Successful Response'`
`responses` |  Additional responses that could be returned by this _path operation_. It will be added to the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `dict[int | str, dict[str, Any]] | None` **DEFAULT:** `None`
`deprecated` |  Mark this _path operation_ as deprecated. It will be added to the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `bool | None` **DEFAULT:** `None`
`operation_id` |  Custom operation ID to be used by this _path operation_. By default, it is generated automatically. If you provide a custom operation ID, you need to make sure it is unique for the whole API. You can customize the operation ID generation with the parameter `generate_unique_id_function` in the `FastAPI` class. Read more about it in the [FastAPI docs about how to Generate Clients](https://fastapi.tiangolo.com/advanced/generate-clients/#custom-generate-unique-id-function). **TYPE:** `str | None` **DEFAULT:** `None`
`response_model_include` |  Configuration passed to Pydantic to include only certain fields in the response data. Read more about it in the [FastAPI docs for Response Model - Return Type](https://fastapi.tiangolo.com/tutorial/response-model/#response_model_include-and-response_model_exclude). **TYPE:** `IncEx | None` **DEFAULT:** `None`
`response_model_exclude` |  Configuration passed to Pydantic to exclude certain fields in the response data. Read more about it in the [FastAPI docs for Response Model - Return Type](https://fastapi.tiangolo.com/tutorial/response-model/#response_model_include-and-response_model_exclude). **TYPE:** `IncEx | None` **DEFAULT:** `None`
`response_model_by_alias` |  Configuration passed to Pydantic to define if the response model should be serialized by alias when an alias is used. Read more about it in the [FastAPI docs for Response Model - Return Type](https://fastapi.tiangolo.com/tutorial/response-model/#response_model_include-and-response_model_exclude). **TYPE:** `bool` **DEFAULT:** `True`
`response_model_exclude_unset` |  Configuration passed to Pydantic to define if the response data should have all the fields, including the ones that were not set and have their default values. This is different from `response_model_exclude_defaults` in that if the fields are set, they will be included in the response, even if the value is the same as the default. When `True`, default values are omitted from the response. Read more about it in the [FastAPI docs for Response Model - Return Type](https://fastapi.tiangolo.com/tutorial/response-model/#use-the-response_model_exclude_unset-parameter). **TYPE:** `bool` **DEFAULT:** `False`
`response_model_exclude_defaults` |  Configuration passed to Pydantic to define if the response data should have all the fields, including the ones that have the same value as the default. This is different from `response_model_exclude_unset` in that if the fields are set but contain the same default values, they will be excluded from the response. When `True`, default values are omitted from the response. Read more about it in the [FastAPI docs for Response Model - Return Type](https://fastapi.tiangolo.com/tutorial/response-model/#use-the-response_model_exclude_unset-parameter). **TYPE:** `bool` **DEFAULT:** `False`
`response_model_exclude_none` |  Configuration passed to Pydantic to define if the response data should exclude fields set to `None`. This is much simpler (less smart) than `response_model_exclude_unset` and `response_model_exclude_defaults`. You probably want to use one of those two instead of this one, as those allow returning `None` values when it makes sense. Read more about it in the [FastAPI docs for Response Model - Return Type](https://fastapi.tiangolo.com/tutorial/response-model/#response_model_exclude_none). **TYPE:** `bool` **DEFAULT:** `False`
`include_in_schema` |  Include this _path operation_ in the generated OpenAPI schema. This affects the generated OpenAPI (e.g. visible at `/docs`). Read more about it in the [FastAPI docs for Query Parameters and String Validations](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#exclude-parameters-from-openapi). **TYPE:** `bool` **DEFAULT:** `True`
`response_class` |  Response class to be used for this _path operation_. This will not be used if you return a response directly. Read more about it in the [FastAPI docs for Custom Response - HTML, Stream, File, others](https://fastapi.tiangolo.com/advanced/custom-response/#redirectresponse). **TYPE:** `type[Response[](https://fastapi.tiangolo.com/reference/response/#fastapi.Response "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">fastapi.Response</span> \(<code>starlette.responses.Response</code>\)")]` **DEFAULT:** `Default(JSONResponse[](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.JSONResponse "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">fastapi.responses.JSONResponse</span> \(<code>starlette.responses.JSONResponse</code>\)"))`
`name` |  Name for this _path operation_. Only used internally. **TYPE:** `str | None` **DEFAULT:** `None`
`callbacks` |  List of _path operations_ that will be used as OpenAPI callbacks. This is only for OpenAPI documentation, the callbacks won't be used directly. It will be added to the generated OpenAPI (e.g. visible at `/docs`). Read more about it in the [FastAPI docs for OpenAPI Callbacks](https://fastapi.tiangolo.com/advanced/openapi-callbacks/). **TYPE:** `list[BaseRoute] | None` **DEFAULT:** `None`
`openapi_extra` |  Extra metadata to be included in the OpenAPI schema for this _path operation_. Read more about it in the [FastAPI docs for Path Operation Advanced Configuration](https://fastapi.tiangolo.com/advanced/path-operation-advanced-configuration/#custom-openapi-path-operation-schema). **TYPE:** `dict[str, Any] | None` **DEFAULT:** `None`
`generate_unique_id_function` |  Customize the function used to generate unique IDs for the _path operations_ shown in the generated OpenAPI. This is particularly useful when automatically generating clients or SDKs for your API. Read more about it in the [FastAPI docs about how to Generate Clients](https://fastapi.tiangolo.com/advanced/generate-clients/#custom-generate-unique-id-function). **TYPE:** `Callable[[APIRoute], str]` **DEFAULT:** `Default(generate_unique_id)`
Source code in `fastapi/routing.py`
```
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
