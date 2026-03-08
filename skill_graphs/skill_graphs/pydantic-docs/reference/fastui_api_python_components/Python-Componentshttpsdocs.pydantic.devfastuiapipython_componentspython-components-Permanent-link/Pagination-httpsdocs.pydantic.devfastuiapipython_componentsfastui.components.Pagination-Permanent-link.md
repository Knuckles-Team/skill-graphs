##  Pagination [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Pagination "Permanent link")
Bases: `BaseModel`
Pagination component to use with tables.
###  page `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Pagination.page "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)page: int

```

The current page number.
###  page_size `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Pagination.page_size "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)page_size: int

```

The number of items per page.
###  total `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Pagination.total "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)total: int

```

The total number of items.
###  page_query_param `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Pagination.page_query_param "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)page_query_param: str = 'page'

```

The query parameter to use for the page number.
###  class_name `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Pagination.class_name "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)class_name: ClassNameField = None

```

Optional class name to apply to the pagination's HTML component.
###  type `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Pagination.type "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)type: Literal['Pagination'] = 'Pagination'

```

The type of the component. Always 'Pagination'.
