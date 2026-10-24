##  Code [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Code "Permanent link")
Bases: `BaseModel`
Code component that renders code with syntax highlighting.
###  text `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Code.text "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)text: str

```

The code to render.
###  language `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Code.language "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)language: str | None = None

```

Optional language of the code. If None, no syntax highlighting is applied.
###  code_style `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Code.code_style "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)code_style: CodeStyle[](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.CodeStyle "fastui.components.CodeStyle") = None

```

Optional code style to apply to the code.
###  class_name `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Code.class_name "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)class_name: ClassNameField = None

```

Optional class name to apply to the page's HTML component.
###  type `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Code.type "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)type: Literal['Code'] = 'Code'

```

The type of the component. Always 'Code'.
