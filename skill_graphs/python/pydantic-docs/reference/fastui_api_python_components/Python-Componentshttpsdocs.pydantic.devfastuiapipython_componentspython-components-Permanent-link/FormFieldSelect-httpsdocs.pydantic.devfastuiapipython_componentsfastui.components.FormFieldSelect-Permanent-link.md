##  FormFieldSelect [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldSelect "Permanent link")
Bases: `BaseFormField`
Form field for select input.
###  name `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldSelect.name "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)name: str

```

Name of the field.
###  title `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldSelect.title "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)title: list[str] | str

```

Title of the field to display. Can be a list of strings for multi-line titles.
###  required `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldSelect.required "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)required: bool = False

```

Whether the field is required. Defaults to False.
###  error `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldSelect.error "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)error: str | None = None

```

Error message to display if the field is invalid.
###  locked `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldSelect.locked "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)locked: bool = False

```

Whether the field is locked. Defaults to False.
###  description `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldSelect.description "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)description: str | None = None

```

Description of the field.
###  display_mode `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldSelect.display_mode "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)display_mode: Literal['default', 'inline'] | None = None

```

Display mode for the field.
###  class_name `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldSelect.class_name "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)class_name: ClassNameField = None

```

Optional class name to apply to the field's HTML component.
###  options `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldSelect.options "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)options: SelectOptions

```

Options for the select field.
###  multiple `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldSelect.multiple "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)multiple: bool | None = None

```

Whether multiple options can be selected.
###  initial `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldSelect.initial "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)initial: list[str] | str | None = None

```

Initial value for the field.
###  vanilla `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldSelect.vanilla "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)vanilla: bool | None = None

```

Whether to use a vanilla (plain) select element.
###  placeholder `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldSelect.placeholder "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)placeholder: str | None = None

```

Placeholder text for the field.
###  autocomplete `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldSelect.autocomplete "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)autocomplete: str | None = None

```

Autocomplete value for the field.
###  type `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldSelect.type "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)type: Literal['FormFieldSelect'] = 'FormFieldSelect'

```

The type of the component. Always 'FormFieldSelect'.
