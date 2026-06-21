##  Iframe [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Iframe "Permanent link")
Bases: `BaseModel`
Iframe component that displays content from a URL.
###  src `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Iframe.src "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)src: HttpUrl

```

The URL of the content to display.
###  title `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Iframe.title "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)title: str | None = None

```

Optional title for the iframe.
###  width `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Iframe.width "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)width: str | int | None = None

```

Optional width used to display the iframe.
###  height `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Iframe.height "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)height: str | int | None = None

```

Optional height used to display the iframe.
###  class_name `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Iframe.class_name "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)class_name: ClassNameField = None

```

Optional class name to apply to the iframe's HTML component.
###  srcdoc `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Iframe.srcdoc "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)srcdoc: str | None = None

```

Optional HTML content to display in the iframe.
###  sandbox `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Iframe.sandbox "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)sandbox: str | None = None

```

Optional sandbox policy for the iframe. Specifies restrictions on the HTML content in the iframe.
###  type `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Iframe.type "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)type: Literal['Iframe'] = 'Iframe'

```

The type of the component. Always 'Iframe'.
