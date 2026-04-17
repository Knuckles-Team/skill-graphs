##  FormFieldSelectSearch [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldSelectSearch "Permanent link")
Bases: `BaseFormField`
Form field for searchable select input.
###  name `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldSelectSearch.name "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)name: str

```

Name of the field.
###  title `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldSelectSearch.title "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)title: list[str] | str

```

Title of the field to display. Can be a list of strings for multi-line titles.
###  required `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldSelectSearch.required "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)required: bool = False

```

Whether the field is required. Defaults to False.
###  error `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldSelectSearch.error "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)error: str | None = None

```

Error message to display if the field is invalid.
###  locked `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldSelectSearch.locked "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)locked: bool = False

```

Whether the field is locked. Defaults to False.
###  description `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldSelectSearch.description "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)description: str | None = None

```

Description of the field.
###  display_mode `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldSelectSearch.display_mode "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)display_mode: Literal['default', 'inline'] | None = None

```

Display mode for the field.
###  class_name `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldSelectSearch.class_name "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)class_name: ClassNameField = None

```

Optional class name to apply to the field's HTML component.
###  search_url `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldSelectSearch.search_url "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)search_url: str

```

URL to search for options.
###  multiple `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldSelectSearch.multiple "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)multiple: bool | None = None

```

Whether multiple options can be selected.
###  initial `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldSelectSearch.initial "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)initial: SelectOption | None = None

```

Initial value for the field.
###  debounce `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldSelectSearch.debounce "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)debounce: int | None = None

```

Time in milliseconds to debounce requests by. Defaults to 300ms.
###  placeholder `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldSelectSearch.placeholder "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)placeholder: str | None = None

```

Placeholder text for the field.
###  type `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldSelectSearch.type "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)type: Literal['FormFieldSelectSearch'] = 'FormFieldSelectSearch'

```

The type of the component. Always 'FormFieldSelectSearch'.
