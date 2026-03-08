##  FormFieldBoolean [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldBoolean "Permanent link")
Bases: `BaseFormField`
Form field for boolean input.
###  name `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldBoolean.name "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)name: str

```

Name of the field.
###  title `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldBoolean.title "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)title: list[str] | str

```

Title of the field to display. Can be a list of strings for multi-line titles.
###  required `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldBoolean.required "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)required: bool = False

```

Whether the field is required. Defaults to False.
###  error `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldBoolean.error "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)error: str | None = None

```

Error message to display if the field is invalid.
###  locked `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldBoolean.locked "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)locked: bool = False

```

Whether the field is locked. Defaults to False.
###  description `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldBoolean.description "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)description: str | None = None

```

Description of the field.
###  display_mode `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldBoolean.display_mode "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)display_mode: Literal['default', 'inline'] | None = None

```

Display mode for the field.
###  class_name `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldBoolean.class_name "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)class_name: ClassNameField = None

```

Optional class name to apply to the field's HTML component.
###  initial `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldBoolean.initial "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)initial: bool | None = None

```

Initial value for the field.
###  mode `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldBoolean.mode "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)mode: Literal['checkbox', 'switch'] = 'checkbox'

```

Mode for the boolean field.
###  type `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldBoolean.type "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)type: Literal['FormFieldBoolean'] = 'FormFieldBoolean'

```

The type of the component. Always 'FormFieldBoolean'.
