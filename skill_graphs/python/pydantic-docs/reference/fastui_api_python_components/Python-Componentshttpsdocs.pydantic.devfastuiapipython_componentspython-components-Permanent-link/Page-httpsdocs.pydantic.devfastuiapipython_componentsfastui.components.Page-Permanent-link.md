##  Page [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Page "Permanent link")
Bases: `BaseModel`
Similar to `container` in many UI frameworks, this acts as a root component for most pages.
###  components `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Page.components "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)components: list[AnyComponent[](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.AnyComponent "fastui.components.AnyComponent")]

```

List of components to render on the page.
###  class_name `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Page.class_name "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)class_name: ClassNameField = None

```

Optional class name to apply to the page's HTML component.
###  type `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Page.type "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)type: Literal['Page'] = 'Page'

```

The type of the component. Always 'Page'.
