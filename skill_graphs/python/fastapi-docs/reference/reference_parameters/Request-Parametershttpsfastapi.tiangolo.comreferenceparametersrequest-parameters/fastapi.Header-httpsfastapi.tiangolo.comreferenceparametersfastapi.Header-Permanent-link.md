##  fastapi.Header [¶](https://fastapi.tiangolo.com/reference/parameters/#fastapi.Header "Permanent link")
```
Header(
    default=Undefined,
    *,
    default_factory=_Unset,
    alias=None,
    alias_priority=_Unset,
    validation_alias=None,
    serialization_alias=None,
    convert_underscores=True,
    title=None,
    description=None,
    gt=None,
    ge=None,
    lt=None,
    le=None,
    min_length=None,
    max_length=None,
    pattern=None,
    regex=None,
    discriminator=None,
    strict=_Unset,
    multiple_of=_Unset,
    allow_inf_nan=_Unset,
    max_digits=_Unset,
    decimal_places=_Unset,
    examples=None,
    example=_Unset,
    openapi_examples=None,
    deprecated=None,
    include_in_schema=True,
    json_schema_extra=None,
    **extra
)

```

PARAMETER | DESCRIPTION
---|---
`default` |  Default value if the parameter field is not set. **TYPE:** `Any` **DEFAULT:** `Undefined`
`default_factory` |  A callable to generate the default value. This doesn't affect `Path` parameters as the value is always required. The parameter is available only for compatibility. **TYPE:** `Callable[[], Any] | None` **DEFAULT:** `_Unset`
`alias` |  An alternative name for the parameter field. This will be used to extract the data and for the generated OpenAPI. It is particularly useful when you can't use the name you want because it is a Python reserved keyword or similar. **TYPE:** `str | None` **DEFAULT:** `None`
`alias_priority` |  Priority of the alias. This affects whether an alias generator is used. **TYPE:** `int | None` **DEFAULT:** `_Unset`
`validation_alias` |  'Whitelist' validation step. The parameter field will be the single one allowed by the alias or set of aliases defined. **TYPE:** `str | AliasPath | AliasChoices | None` **DEFAULT:** `None`
`serialization_alias` |  'Blacklist' validation step. The vanilla parameter field will be the single one of the alias' or set of aliases' fields and all the other fields will be ignored at serialization time. **TYPE:** `str | None` **DEFAULT:** `None`
`convert_underscores` |  Automatically convert underscores to hyphens in the parameter field name. Read more about it in the [FastAPI docs for Header Parameters](https://fastapi.tiangolo.com/tutorial/header-params/#automatic-conversion) **TYPE:** `bool` **DEFAULT:** `True`
`title` |  Human-readable title. **TYPE:** `str | None` **DEFAULT:** `None`
`description` |  Human-readable description. **TYPE:** `str | None` **DEFAULT:** `None`
`gt` |  Greater than. If set, value must be greater than this. Only applicable to numbers. **TYPE:** `float | None` **DEFAULT:** `None`
`ge` |  Greater than or equal. If set, value must be greater than or equal to this. Only applicable to numbers. **TYPE:** `float | None` **DEFAULT:** `None`
`lt` |  Less than. If set, value must be less than this. Only applicable to numbers. **TYPE:** `float | None` **DEFAULT:** `None`
`le` |  Less than or equal. If set, value must be less than or equal to this. Only applicable to numbers. **TYPE:** `float | None` **DEFAULT:** `None`
`min_length` |  Minimum length for strings. **TYPE:** `int | None` **DEFAULT:** `None`
`max_length` |  Maximum length for strings. **TYPE:** `int | None` **DEFAULT:** `None`
`pattern` |  RegEx pattern for strings. **TYPE:** `str | None` **DEFAULT:** `None`
`regex` |  Deprecated in FastAPI 0.100.0 and Pydantic v2, use `pattern` instead. RegEx pattern for strings. **TYPE:** `str | None` **DEFAULT:** `None`
`discriminator` |  Parameter field name for discriminating the type in a tagged union. **TYPE:** `str | None` **DEFAULT:** `None`
`strict` |  If `True`, strict validation is applied to the field. **TYPE:** `bool | None` **DEFAULT:** `_Unset`
`multiple_of` |  Value must be a multiple of this. Only applicable to numbers. **TYPE:** `float | None` **DEFAULT:** `_Unset`
`allow_inf_nan` |  Allow `inf`, `-inf`, `nan`. Only applicable to numbers. **TYPE:** `bool | None` **DEFAULT:** `_Unset`
`max_digits` |  Maximum number of digits allowed for decimal values. **TYPE:** `int | None` **DEFAULT:** `_Unset`
`decimal_places` |  Maximum number of decimal places allowed for decimal values. **TYPE:** `int | None` **DEFAULT:** `_Unset`
`examples` |  Example values for this field. Read more about it in the [FastAPI docs for Declare Request Example Data](https://fastapi.tiangolo.com/tutorial/schema-extra-example/) **TYPE:** `list[Any] | None` **DEFAULT:** `None`
`example` |  Deprecated in OpenAPI 3.1.0 that now uses JSON Schema 2020-12, although still supported. Use examples instead.  **TYPE:** `Any | None` **DEFAULT:** `_Unset`
`openapi_examples` |  OpenAPI-specific examples. It will be added to the generated OpenAPI (e.g. visible at `/docs`). Swagger UI (that provides the `/docs` interface) has better support for the OpenAPI-specific examples than the JSON Schema `examples`, that's the main use case for this. Read more about it in the [FastAPI docs for Declare Request Example Data](https://fastapi.tiangolo.com/tutorial/schema-extra-example/#using-the-openapi_examples-parameter). **TYPE:** `dict[str, Example[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Example "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">Example</span> \(<code>fastapi.openapi.models.Example</code>\)")] | None` **DEFAULT:** `None`
`deprecated` |  Mark this parameter field as deprecated. It will affect the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `deprecated | str | bool | None` **DEFAULT:** `None`
`include_in_schema` |  To include (or not) this parameter field in the generated OpenAPI. You probably don't need it, but it's available. This affects the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `bool` **DEFAULT:** `True`
`json_schema_extra` |  Any additional JSON schema data. **TYPE:** `dict[str, Any] | None` **DEFAULT:** `None`
`**extra` |  The `extra` kwargs is deprecated. Use `json_schema_extra` instead. Include extra fields used by the JSON Schema. **TYPE:** `Any` **DEFAULT:** `{}`
Source code in `fastapi/param_functions.py`
```
 702
 703
 704
 705
 706
 707
 708
 709
 710
 711
 712
 713
 714
 715
 716
 717
 718
 719
 720
 721
 722
 723
 724
 725
 726
 727
 728
 729
 730
 731
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
 751
 752
 753
 754
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
 775
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
 821
 822
 823
 824
 825
 826
 827
 828
 829
 830
 831
 832
 833
 834
 835
 836
 837
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
 891
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
 946
 947
 948
 949
 950
 951
 952
 953
 954
 955
 956
 957
 958
 959
 960
 961
 962
 963
 964
 965
 966
 967
 968
 969
 970
 971
 972
 973
 974
 975
 976
 977
 978
 979
 980
 981
 982
 983
 984
 985
 986
 987
 988
 989
 990
 991
 992
 993
 994
 995
 996
 997
 998
 999
1000
1001
1002
1003
1004
1005
1006
1007
1008
1009
1010
1011
1012
1013
1014
1015
1016
```
| ```
def Header(  # noqa: N802
    default: Annotated[
        Any,
        Doc(
            """
            Default value if the parameter field is not set.
            """
        ),
    ] = Undefined,
    *,
    default_factory: Annotated[
        Callable[[], Any] | None,
        Doc(
            """
            A callable to generate the default value.

            This doesn't affect `Path` parameters as the value is always required.
            The parameter is available only for compatibility.
            """
        ),
    ] = _Unset,
    alias: Annotated[
        str | None,
        Doc(
            """
            An alternative name for the parameter field.

            This will be used to extract the data and for the generated OpenAPI.
            It is particularly useful when you can't use the name you want because it
            is a Python reserved keyword or similar.
            """
        ),
    ] = None,
    alias_priority: Annotated[
        int | None,
        Doc(
            """
            Priority of the alias. This affects whether an alias generator is used.
            """
        ),
    ] = _Unset,
    validation_alias: Annotated[
        str | AliasPath | AliasChoices | None,
        Doc(
            """
            'Whitelist' validation step. The parameter field will be the single one
            allowed by the alias or set of aliases defined.
            """
        ),
    ] = None,
    serialization_alias: Annotated[
        str | None,
        Doc(
            """
            'Blacklist' validation step. The vanilla parameter field will be the
            single one of the alias' or set of aliases' fields and all the other
            fields will be ignored at serialization time.
            """
        ),
    ] = None,
    convert_underscores: Annotated[
        bool,
        Doc(
            """
            Automatically convert underscores to hyphens in the parameter field name.

            Read more about it in the
            [FastAPI docs for Header Parameters](https://fastapi.tiangolo.com/tutorial/header-params/#automatic-conversion)
            """
        ),
    ] = True,
    title: Annotated[
        str | None,
        Doc(
            """
            Human-readable title.
            """
        ),
    ] = None,
    description: Annotated[
        str | None,
        Doc(
            """
            Human-readable description.
            """
        ),
    ] = None,
    gt: Annotated[
        float | None,
        Doc(
            """
            Greater than. If set, value must be greater than this. Only applicable to
            numbers.
            """
        ),
    ] = None,
    ge: Annotated[
        float | None,
        Doc(
            """
            Greater than or equal. If set, value must be greater than or equal to
            this. Only applicable to numbers.
            """
        ),
    ] = None,
    lt: Annotated[
        float | None,
        Doc(
            """
            Less than. If set, value must be less than this. Only applicable to numbers.
            """
        ),
    ] = None,
    le: Annotated[
        float | None,
        Doc(
            """
            Less than or equal. If set, value must be less than or equal to this.
            Only applicable to numbers.
            """
        ),
    ] = None,
    min_length: Annotated[
        int | None,
        Doc(
            """
            Minimum length for strings.
            """
        ),
    ] = None,
    max_length: Annotated[
        int | None,
        Doc(
            """
            Maximum length for strings.
            """
        ),
    ] = None,
    pattern: Annotated[
        str | None,
        Doc(
            """
            RegEx pattern for strings.
            """
        ),
    ] = None,
    regex: Annotated[
        str | None,
        Doc(
            """
            RegEx pattern for strings.
            """
        ),
        deprecated(
            "Deprecated in FastAPI 0.100.0 and Pydantic v2, use `pattern` instead."
        ),
    ] = None,
    discriminator: Annotated[
        str | None,
        Doc(
            """
            Parameter field name for discriminating the type in a tagged union.
            """
        ),
    ] = None,
    strict: Annotated[
        bool | None,
        Doc(
            """
            If `True`, strict validation is applied to the field.
            """
        ),
    ] = _Unset,
    multiple_of: Annotated[
        float | None,
        Doc(
            """
            Value must be a multiple of this. Only applicable to numbers.
            """
        ),
    ] = _Unset,
    allow_inf_nan: Annotated[
        bool | None,
        Doc(
            """
            Allow `inf`, `-inf`, `nan`. Only applicable to numbers.
            """
        ),
    ] = _Unset,
    max_digits: Annotated[
        int | None,
        Doc(
            """
            Maximum number of digits allowed for decimal values.
            """
        ),
    ] = _Unset,
    decimal_places: Annotated[
        int | None,
        Doc(
            """
            Maximum number of decimal places allowed for decimal values.
            """
        ),
    ] = _Unset,
    examples: Annotated[
        list[Any] | None,
        Doc(
            """
            Example values for this field.

            Read more about it in the
            [FastAPI docs for Declare Request Example Data](https://fastapi.tiangolo.com/tutorial/schema-extra-example/)
            """
        ),
    ] = None,
    example: Annotated[
        Any | None,
        deprecated(
            "Deprecated in OpenAPI 3.1.0 that now uses JSON Schema 2020-12, "
            "although still supported. Use examples instead."
        ),
    ] = _Unset,
    openapi_examples: Annotated[
        dict[str, Example] | None,
        Doc(
            """
            OpenAPI-specific examples.

            It will be added to the generated OpenAPI (e.g. visible at `/docs`).

            Swagger UI (that provides the `/docs` interface) has better support for the
            OpenAPI-specific examples than the JSON Schema `examples`, that's the main
            use case for this.

            Read more about it in the
            [FastAPI docs for Declare Request Example Data](https://fastapi.tiangolo.com/tutorial/schema-extra-example/#using-the-openapi_examples-parameter).
            """
        ),
    ] = None,
    deprecated: Annotated[
        deprecated | str | bool | None,
        Doc(
            """
            Mark this parameter field as deprecated.

            It will affect the generated OpenAPI (e.g. visible at `/docs`).
            """
        ),
    ] = None,
    include_in_schema: Annotated[
        bool,
        Doc(
            """
            To include (or not) this parameter field in the generated OpenAPI.
            You probably don't need it, but it's available.

            This affects the generated OpenAPI (e.g. visible at `/docs`).
            """
        ),
    ] = True,
    json_schema_extra: Annotated[
        dict[str, Any] | None,
        Doc(
            """
            Any additional JSON schema data.
            """
        ),
    ] = None,
    **extra: Annotated[
        Any,
        Doc(
            """
            Include extra fields used by the JSON Schema.
            """
        ),
        deprecated(
            """
            The `extra` kwargs is deprecated. Use `json_schema_extra` instead.
            """
        ),
    ],
) -> Any:
    return params.Header(
        default=default,
        default_factory=default_factory,
        alias=alias,
        alias_priority=alias_priority,
        validation_alias=validation_alias,
        serialization_alias=serialization_alias,
        convert_underscores=convert_underscores,
        title=title,
        description=description,
        gt=gt,
        ge=ge,
        lt=lt,
        le=le,
        min_length=min_length,
        max_length=max_length,
        pattern=pattern,
        regex=regex,
        discriminator=discriminator,
        strict=strict,
        multiple_of=multiple_of,
        allow_inf_nan=allow_inf_nan,
        max_digits=max_digits,
        decimal_places=decimal_places,
        example=example,
        examples=examples,
        openapi_examples=openapi_examples,
        deprecated=deprecated,
        include_in_schema=include_in_schema,
        json_schema_extra=json_schema_extra,
        **extra,
    )

```

---|---
##  fastapi.Form [¶](https://fastapi.tiangolo.com/reference/parameters/#fastapi.Form "Permanent link")
```
Form(
    default=Undefined,
    *,
    default_factory=_Unset,
    media_type="application/x-www-form-urlencoded",
    alias=None,
    alias_priority=_Unset,
    validation_alias=None,
    serialization_alias=None,
    title=None,
    description=None,
    gt=None,
    ge=None,
    lt=None,
    le=None,
    min_length=None,
    max_length=None,
    pattern=None,
    regex=None,
    discriminator=None,
    strict=_Unset,
    multiple_of=_Unset,
    allow_inf_nan=_Unset,
    max_digits=_Unset,
    decimal_places=_Unset,
    examples=None,
    example=_Unset,
    openapi_examples=None,
    deprecated=None,
    include_in_schema=True,
    json_schema_extra=None,
    **extra
)

```

PARAMETER | DESCRIPTION
---|---
`default` |  Default value if the parameter field is not set. **TYPE:** `Any` **DEFAULT:** `Undefined`
`default_factory` |  A callable to generate the default value. This doesn't affect `Path` parameters as the value is always required. The parameter is available only for compatibility. **TYPE:** `Callable[[], Any] | None` **DEFAULT:** `_Unset`
`media_type` |  The media type of this parameter field. Changing it would affect the generated OpenAPI, but currently it doesn't affect the parsing of the data. **TYPE:** `str` **DEFAULT:** `'application/x-www-form-urlencoded'`
`alias` |  An alternative name for the parameter field. This will be used to extract the data and for the generated OpenAPI. It is particularly useful when you can't use the name you want because it is a Python reserved keyword or similar. **TYPE:** `str | None` **DEFAULT:** `None`
`alias_priority` |  Priority of the alias. This affects whether an alias generator is used. **TYPE:** `int | None` **DEFAULT:** `_Unset`
`validation_alias` |  'Whitelist' validation step. The parameter field will be the single one allowed by the alias or set of aliases defined. **TYPE:** `str | AliasPath | AliasChoices | None` **DEFAULT:** `None`
`serialization_alias` |  'Blacklist' validation step. The vanilla parameter field will be the single one of the alias' or set of aliases' fields and all the other fields will be ignored at serialization time. **TYPE:** `str | None` **DEFAULT:** `None`
`title` |  Human-readable title. **TYPE:** `str | None` **DEFAULT:** `None`
`description` |  Human-readable description. **TYPE:** `str | None` **DEFAULT:** `None`
`gt` |  Greater than. If set, value must be greater than this. Only applicable to numbers. **TYPE:** `float | None` **DEFAULT:** `None`
`ge` |  Greater than or equal. If set, value must be greater than or equal to this. Only applicable to numbers. **TYPE:** `float | None` **DEFAULT:** `None`
`lt` |  Less than. If set, value must be less than this. Only applicable to numbers. **TYPE:** `float | None` **DEFAULT:** `None`
`le` |  Less than or equal. If set, value must be less than or equal to this. Only applicable to numbers. **TYPE:** `float | None` **DEFAULT:** `None`
`min_length` |  Minimum length for strings. **TYPE:** `int | None` **DEFAULT:** `None`
`max_length` |  Maximum length for strings. **TYPE:** `int | None` **DEFAULT:** `None`
`pattern` |  RegEx pattern for strings. **TYPE:** `str | None` **DEFAULT:** `None`
`regex` |  Deprecated in FastAPI 0.100.0 and Pydantic v2, use `pattern` instead. RegEx pattern for strings. **TYPE:** `str | None` **DEFAULT:** `None`
`discriminator` |  Parameter field name for discriminating the type in a tagged union. **TYPE:** `str | None` **DEFAULT:** `None`
`strict` |  If `True`, strict validation is applied to the field. **TYPE:** `bool | None` **DEFAULT:** `_Unset`
`multiple_of` |  Value must be a multiple of this. Only applicable to numbers. **TYPE:** `float | None` **DEFAULT:** `_Unset`
`allow_inf_nan` |  Allow `inf`, `-inf`, `nan`. Only applicable to numbers. **TYPE:** `bool | None` **DEFAULT:** `_Unset`
`max_digits` |  Maximum number of digits allowed for decimal values. **TYPE:** `int | None` **DEFAULT:** `_Unset`
`decimal_places` |  Maximum number of decimal places allowed for decimal values. **TYPE:** `int | None` **DEFAULT:** `_Unset`
`examples` |  Example values for this field. Read more about it in the [FastAPI docs for Declare Request Example Data](https://fastapi.tiangolo.com/tutorial/schema-extra-example/) **TYPE:** `list[Any] | None` **DEFAULT:** `None`
`example` |  Deprecated in OpenAPI 3.1.0 that now uses JSON Schema 2020-12, although still supported. Use examples instead.  **TYPE:** `Any | None` **DEFAULT:** `_Unset`
`openapi_examples` |  OpenAPI-specific examples. It will be added to the generated OpenAPI (e.g. visible at `/docs`). Swagger UI (that provides the `/docs` interface) has better support for the OpenAPI-specific examples than the JSON Schema `examples`, that's the main use case for this. Read more about it in the [FastAPI docs for Declare Request Example Data](https://fastapi.tiangolo.com/tutorial/schema-extra-example/#using-the-openapi_examples-parameter). **TYPE:** `dict[str, Example[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Example "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">Example</span> \(<code>fastapi.openapi.models.Example</code>\)")] | None` **DEFAULT:** `None`
`deprecated` |  Mark this parameter field as deprecated. It will affect the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `deprecated | str | bool | None` **DEFAULT:** `None`
`include_in_schema` |  To include (or not) this parameter field in the generated OpenAPI. You probably don't need it, but it's available. This affects the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `bool` **DEFAULT:** `True`
`json_schema_extra` |  Any additional JSON schema data. **TYPE:** `dict[str, Any] | None` **DEFAULT:** `None`
`**extra` |  The `extra` kwargs is deprecated. Use `json_schema_extra` instead. Include extra fields used by the JSON Schema. **TYPE:** `Any` **DEFAULT:** `{}`
Source code in `fastapi/param_functions.py`
```
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
```
| ```
def Form(  # noqa: N802
    default: Annotated[
        Any,
        Doc(
            """
            Default value if the parameter field is not set.
            """
        ),
    ] = Undefined,
    *,
    default_factory: Annotated[
        Callable[[], Any] | None,
        Doc(
            """
            A callable to generate the default value.

            This doesn't affect `Path` parameters as the value is always required.
            The parameter is available only for compatibility.
            """
        ),
    ] = _Unset,
    media_type: Annotated[
        str,
        Doc(
            """
            The media type of this parameter field. Changing it would affect the
            generated OpenAPI, but currently it doesn't affect the parsing of the data.
            """
        ),
    ] = "application/x-www-form-urlencoded",
    alias: Annotated[
        str | None,
        Doc(
            """
            An alternative name for the parameter field.

            This will be used to extract the data and for the generated OpenAPI.
            It is particularly useful when you can't use the name you want because it
            is a Python reserved keyword or similar.
            """
        ),
    ] = None,
    alias_priority: Annotated[
        int | None,
        Doc(
            """
            Priority of the alias. This affects whether an alias generator is used.
            """
        ),
    ] = _Unset,
    validation_alias: Annotated[
        str | AliasPath | AliasChoices | None,
        Doc(
            """
            'Whitelist' validation step. The parameter field will be the single one
            allowed by the alias or set of aliases defined.
            """
        ),
    ] = None,
    serialization_alias: Annotated[
        str | None,
        Doc(
            """
            'Blacklist' validation step. The vanilla parameter field will be the
            single one of the alias' or set of aliases' fields and all the other
            fields will be ignored at serialization time.
            """
        ),
    ] = None,
    title: Annotated[
        str | None,
        Doc(
            """
            Human-readable title.
            """
        ),
    ] = None,
    description: Annotated[
        str | None,
        Doc(
            """
            Human-readable description.
            """
        ),
    ] = None,
    gt: Annotated[
        float | None,
        Doc(
            """
            Greater than. If set, value must be greater than this. Only applicable to
            numbers.
            """
        ),
    ] = None,
    ge: Annotated[
        float | None,
        Doc(
            """
            Greater than or equal. If set, value must be greater than or equal to
            this. Only applicable to numbers.
            """
        ),
    ] = None,
    lt: Annotated[
        float | None,
        Doc(
            """
            Less than. If set, value must be less than this. Only applicable to numbers.
            """
        ),
    ] = None,
    le: Annotated[
        float | None,
        Doc(
            """
            Less than or equal. If set, value must be less than or equal to this.
            Only applicable to numbers.
            """
        ),
    ] = None,
    min_length: Annotated[
        int | None,
        Doc(
            """
            Minimum length for strings.
            """
        ),
    ] = None,
    max_length: Annotated[
        int | None,
        Doc(
            """
            Maximum length for strings.
            """
        ),
    ] = None,
    pattern: Annotated[
        str | None,
        Doc(
            """
            RegEx pattern for strings.
            """
        ),
    ] = None,
    regex: Annotated[
        str | None,
        Doc(
            """
            RegEx pattern for strings.
            """
        ),
        deprecated(
            "Deprecated in FastAPI 0.100.0 and Pydantic v2, use `pattern` instead."
        ),
    ] = None,
    discriminator: Annotated[
        str | None,
        Doc(
            """
            Parameter field name for discriminating the type in a tagged union.
            """
        ),
    ] = None,
    strict: Annotated[
        bool | None,
        Doc(
            """
            If `True`, strict validation is applied to the field.
            """
        ),
    ] = _Unset,
    multiple_of: Annotated[
        float | None,
        Doc(
            """
            Value must be a multiple of this. Only applicable to numbers.
            """
        ),
    ] = _Unset,
    allow_inf_nan: Annotated[
        bool | None,
        Doc(
            """
            Allow `inf`, `-inf`, `nan`. Only applicable to numbers.
            """
        ),
    ] = _Unset,
    max_digits: Annotated[
        int | None,
        Doc(
            """
            Maximum number of digits allowed for decimal values.
            """
        ),
    ] = _Unset,
    decimal_places: Annotated[
        int | None,
        Doc(
            """
            Maximum number of decimal places allowed for decimal values.
            """
        ),
    ] = _Unset,
    examples: Annotated[
        list[Any] | None,
        Doc(
            """
            Example values for this field.

            Read more about it in the
            [FastAPI docs for Declare Request Example Data](https://fastapi.tiangolo.com/tutorial/schema-extra-example/)
            """
        ),
    ] = None,
    example: Annotated[
        Any | None,
        deprecated(
            "Deprecated in OpenAPI 3.1.0 that now uses JSON Schema 2020-12, "
            "although still supported. Use examples instead."
        ),
    ] = _Unset,
    openapi_examples: Annotated[
        dict[str, Example] | None,
        Doc(
            """
            OpenAPI-specific examples.

            It will be added to the generated OpenAPI (e.g. visible at `/docs`).

            Swagger UI (that provides the `/docs` interface) has better support for the
            OpenAPI-specific examples than the JSON Schema `examples`, that's the main
            use case for this.

            Read more about it in the
            [FastAPI docs for Declare Request Example Data](https://fastapi.tiangolo.com/tutorial/schema-extra-example/#using-the-openapi_examples-parameter).
            """
        ),
    ] = None,
    deprecated: Annotated[
        deprecated | str | bool | None,
        Doc(
            """
            Mark this parameter field as deprecated.

            It will affect the generated OpenAPI (e.g. visible at `/docs`).
            """
        ),
    ] = None,
    include_in_schema: Annotated[
        bool,
        Doc(
            """
            To include (or not) this parameter field in the generated OpenAPI.
            You probably don't need it, but it's available.

            This affects the generated OpenAPI (e.g. visible at `/docs`).
            """
        ),
    ] = True,
    json_schema_extra: Annotated[
        dict[str, Any] | None,
        Doc(
            """
            Any additional JSON schema data.
            """
        ),
    ] = None,
    **extra: Annotated[
        Any,
        Doc(
            """
            Include extra fields used by the JSON Schema.
            """
        ),
        deprecated(
            """
            The `extra` kwargs is deprecated. Use `json_schema_extra` instead.
            """
        ),
    ],
) -> Any:
    return params.Form(
        default=default,
        default_factory=default_factory,
        media_type=media_type,
        alias=alias,
        alias_priority=alias_priority,
        validation_alias=validation_alias,
        serialization_alias=serialization_alias,
        title=title,
        description=description,
        gt=gt,
        ge=ge,
        lt=lt,
        le=le,
        min_length=min_length,
        max_length=max_length,
        pattern=pattern,
        regex=regex,
        discriminator=discriminator,
        strict=strict,
        multiple_of=multiple_of,
        allow_inf_nan=allow_inf_nan,
        max_digits=max_digits,
        decimal_places=decimal_places,
        example=example,
        examples=examples,
        openapi_examples=openapi_examples,
        deprecated=deprecated,
        include_in_schema=include_in_schema,
        json_schema_extra=json_schema_extra,
        **extra,
    )

```

---|---
