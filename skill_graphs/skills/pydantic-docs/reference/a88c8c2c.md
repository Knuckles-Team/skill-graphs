##  FormFieldFile [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldFile "Permanent link")
Bases: `BaseFormField`
Form field for file input.
###  name `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldFile.name "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)name: str

```

Name of the field.
###  title `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldFile.title "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)title: list[str] | str

```

Title of the field to display. Can be a list of strings for multi-line titles.
###  required `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldFile.required "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)required: bool = False

```

Whether the field is required. Defaults to False.
###  error `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldFile.error "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)error: str | None = None

```

Error message to display if the field is invalid.
###  locked `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldFile.locked "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)locked: bool = False

```

Whether the field is locked. Defaults to False.
###  description `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldFile.description "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)description: str | None = None

```

Description of the field.
###  display_mode `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldFile.display_mode "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)display_mode: Literal['default', 'inline'] | None = None

```

Display mode for the field.
###  class_name `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldFile.class_name "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)class_name: ClassNameField = None

```

Optional class name to apply to the field's HTML component.
###  multiple `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldFile.multiple "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)multiple: bool | None = None

```

Whether multiple files can be selected.
###  accept `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldFile.accept "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)accept: str | None = None

```

Accepted file types.
###  type `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FormFieldFile.type "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)type: Literal['FormFieldFile'] = 'FormFieldFile'

```

The type of the component. Always 'FormFieldFile'.
