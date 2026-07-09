##  Display [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Display "Permanent link")
Bases: `DisplayBase`
Description of how to display a value, either in a table or detail view.
###  mode `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Display.mode "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)mode: DisplayMode | None = None

```

Display mode for the value.
###  title `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Display.title "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)title: str | None = None

```

Title to display for the value.
###  on_click `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Display.on_click "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)on_click: AnyEvent | None = None

```

Event to trigger when the value is clicked.
###  value `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Display.value "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)value: JsonData

```

Value to display.
###  type `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Display.type "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)type: Literal['Display'] = 'Display'

```

The type of the component. Always 'Display'.
