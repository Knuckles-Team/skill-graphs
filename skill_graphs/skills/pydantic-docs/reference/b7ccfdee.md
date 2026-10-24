##  Toast [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Toast "Permanent link")
Bases: `BaseModel`
Toast component that displays a toast message (small temporary message).
###  title `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Toast.title "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)title: str

```

The title of the toast.
###  body `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Toast.body "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)body: list[AnyComponent[](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.AnyComponent "fastui.components.AnyComponent")]

```

List of components to render in the toast body.
###  position `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Toast.position "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)position: Literal['top-start', 'top-center', 'top-end', 'middle-start', 'middle-center', 'middle-end', 'bottom-start', 'bottom-center', 'bottom-end'] | None = None

```

Optional position of the toast.
###  open_trigger `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Toast.open_trigger "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)open_trigger: PageEvent | None = None

```

Optional event to trigger when the toast is opened.
###  open_context `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Toast.open_context "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)open_context: ContextType | None = None

```

Optional context to pass to the open trigger event.
###  class_name `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Toast.class_name "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)class_name: ClassNameField = None

```

Optional class name to apply to the toast's HTML component.
###  type `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Toast.type "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)type: Literal['Toast'] = 'Toast'

```

The type of the component. Always 'Toast'.
