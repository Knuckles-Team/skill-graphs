##  Button [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Button "Permanent link")
Bases: `BaseModel`
Button component.
###  text `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Button.text "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)text: str

```

The text to display on the button.
###  on_click `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Button.on_click "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)on_click: AnyEvent | None = None

```

Optional event to trigger when the button is clicked.
###  html_type `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Button.html_type "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)html_type: Literal['button', 'reset', 'submit'] | None = None

```

Optional HTML type of the button. If None, defaults to 'button'.
###  named_style `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Button.named_style "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)named_style: NamedStyleField = None

```

Optional named style to apply to the button.
###  class_name `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Button.class_name "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)class_name: ClassNameField = None

```

Optional class name to apply to the button's HTML component.
###  type `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Button.type "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)type: Literal['Button'] = 'Button'

```

The type of the component. Always 'Button'.
