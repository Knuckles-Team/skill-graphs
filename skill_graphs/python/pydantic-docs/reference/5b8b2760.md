##  Details [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Details "Permanent link")
Bases: `BaseModel`
Details associated with displaying a data model.
###  data `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Details.data "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)data: SerializeAsAny[DataModel]

```

Data model to display.
###  fields `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Details.fields "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)fields: list[DisplayLookup | Display[](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Display "fastui.components.display.Display")] | None = None

```

Fields to display.
###  class_name `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Details.class_name "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)class_name: ClassNameField = None

```

Optional class name to apply to the details component.
###  type `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Details.type "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)type: Literal['Details'] = 'Details'

```

The type of the component. Always 'Details'.
