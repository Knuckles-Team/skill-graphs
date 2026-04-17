##  Link [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Link "Permanent link")
Bases: `BaseModel`
Link component.
###  components `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Link.components "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)components: list[AnyComponent[](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.AnyComponent "fastui.components.AnyComponent")]

```

List of components to render attached to the link.
###  on_click `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Link.on_click "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)on_click: AnyEvent | None = None

```

Optional event to trigger when the link is clicked.
###  mode `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Link.mode "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)mode: Literal['navbar', 'footer', 'tabs', 'vertical', 'pagination'] | None = None

```

Optional mode of the link.
###  active `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Link.active "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)active: str | bool | None = None

```

Optional active state of the link.
###  locked `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Link.locked "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)locked: bool | None = None

```

Optional locked state of the link.
###  class_name `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Link.class_name "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)class_name: ClassNameField = None

```

Optional class name to apply to the link's HTML component.
###  type `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Link.type "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)type: Literal['Link'] = 'Link'

```

The type of the component. Always 'Link'.
