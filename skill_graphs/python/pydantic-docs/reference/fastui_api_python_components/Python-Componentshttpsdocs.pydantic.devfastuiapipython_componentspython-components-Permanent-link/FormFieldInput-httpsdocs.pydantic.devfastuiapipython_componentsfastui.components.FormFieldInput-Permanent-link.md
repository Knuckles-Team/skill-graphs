##  FormFieldInput [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldInput "Permanent link")
Bases: `BaseFormField`
Form field for basic input.
###  name `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldInput.name "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)name: str

```

Name of the field.
###  title `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldInput.title "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)title: list[str] | str

```

Title of the field to display. Can be a list of strings for multi-line titles.
###  required `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldInput.required "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)required: bool = False

```

Whether the field is required. Defaults to False.
###  error `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldInput.error "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)error: str | None = None

```

Error message to display if the field is invalid.
###  locked `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldInput.locked "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)locked: bool = False

```

Whether the field is locked. Defaults to False.
###  description `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldInput.description "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)description: str | None = None

```

Description of the field.
###  display_mode `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldInput.display_mode "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)display_mode: Literal['default', 'inline'] | None = None

```

Display mode for the field.
###  class_name `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldInput.class_name "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)class_name: ClassNameField = None

```

Optional class name to apply to the field's HTML component.
###  html_type `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldInput.html_type "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)html_type: InputHtmlType = 'text'

```

HTML input type for the field.
###  initial `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldInput.initial "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)initial: str | float | None = None

```

Initial value for the field.
###  placeholder `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldInput.placeholder "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)placeholder: str | None = None

```

Placeholder text for the field.
###  autocomplete `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldInput.autocomplete "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)autocomplete: str | None = None

```

Autocomplete value for the field.
###  type `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldInput.type "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)type: Literal['FormFieldInput'] = 'FormFieldInput'

```

The type of the component. Always 'FormFieldInput'.
