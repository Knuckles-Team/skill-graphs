##  Table [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Table "Permanent link")
Bases: `BaseModel`
Table component.
###  data `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Table.data "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)data: Sequence[SerializeAsAny[DataModel]]

```

Sequence of data models to display in the table.
###  columns `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Table.columns "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)columns: list[DisplayLookup] | None = None

```

List of columns to display in the table. If not provided, columns will be inferred from the data model.
###  data_model `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Table.data_model "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)data_model: type_[BaseModel] | None = Field(default=None, exclude=True)

```

Data model to use for the table. If not provided, the model will be inferred from the first data item.
###  no_data_message `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Table.no_data_message "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)no_data_message: str | None = None

```

Message to display when there is no data.
###  class_name `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Table.class_name "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)class_name: ClassNameField = None

```

Optional class name to apply to the paragraph's HTML component.
###  type `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Table.type "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)type: Literal['Table'] = 'Table'

```

The type of the component. Always 'Table'.
