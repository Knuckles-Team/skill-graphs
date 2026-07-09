##  Modal [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Modal "Permanent link")
Bases: `BaseModel`
Modal component that displays a modal dialog.
###  title `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Modal.title "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)title: str

```

The text displayed on the modal trigger button.
###  body `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Modal.body "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)body: list[AnyComponent[](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.AnyComponent "fastui.components.AnyComponent")]

```

List of components to render in the modal body.
###  footer `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Modal.footer "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)footer: list[AnyComponent[](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.AnyComponent "fastui.components.AnyComponent")] | None = None

```

Optional list of components to render in the modal footer.
###  open_trigger `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Modal.open_trigger "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)open_trigger: PageEvent | None = None

```

Optional event to trigger when the modal is opened.
###  open_context `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Modal.open_context "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)open_context: ContextType | None = None

```

Optional context to pass to the open trigger event.
###  class_name `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Modal.class_name "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)class_name: ClassNameField = None

```

Optional class name to apply to the modal's HTML component.
###  type `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Modal.type "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)type: Literal['Modal'] = 'Modal'

```

The type of the component. Always 'Modal'.
