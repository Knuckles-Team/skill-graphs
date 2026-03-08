##  Custom [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Custom "Permanent link")
Bases: `BaseModel`
Custom component that allows for special data to be rendered.
###  data `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Custom.data "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)data: JsonData

```

The data to render in the custom component.
###  sub_type `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Custom.sub_type "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)sub_type: str

```

The sub-type of the custom component.
###  library `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Custom.library "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)library: str | None = None

```

Optional library to use for the custom component.
###  class_name `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Custom.class_name "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)class_name: ClassNameField = None

```

Optional class name to apply to the custom component's HTML component.
###  type `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Custom.type "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)type: Literal['Custom'] = 'Custom'

```

The type of the component. Always 'Custom'.
Made with
