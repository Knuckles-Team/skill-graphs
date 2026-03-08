##  ModelForm [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.ModelForm "Permanent link")
Bases: `BaseForm`
Form component generated from a Pydantic model.
###  submit_url `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.ModelForm.submit_url "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)submit_url: str

```

URL to submit the form data to.
###  initial `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.ModelForm.initial "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)initial: dict[str, JsonData] | None = None

```

Initial values for the form fields, mapping field names to values.
###  method `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.ModelForm.method "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)method: Literal['POST', 'GOTO', 'GET'] = 'POST'

```

HTTP method to use for the form submission.
###  display_mode `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.ModelForm.display_mode "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)display_mode: Literal['default', 'page', 'inline'] | None = None

```

Display mode for the form.
###  submit_on_change `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.ModelForm.submit_on_change "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)submit_on_change: bool | None = None

```

Whether to submit the form on change.
###  submit_trigger `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.ModelForm.submit_trigger "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)submit_trigger: PageEvent | None = None

```

Event to trigger form submission.
###  loading `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.ModelForm.loading "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)loading: list[AnyComponent[](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.AnyComponent "fastui.components.AnyComponent")] | None = None

```

Components to display while the form is submitting.
###  footer `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.ModelForm.footer "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)footer: list[AnyComponent[](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.AnyComponent "fastui.components.AnyComponent")] | None = None

```

Components to display in the form footer.
###  class_name `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.ModelForm.class_name "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)class_name: ClassNameField = None

```

Optional class name to apply to the form's HTML component.
###  model `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.ModelForm.model "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)model: type_[BaseModel] = Field(exclude=True)

```

Pydantic model from which to generate the form.
###  type `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.ModelForm.type "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)type: Literal['ModelForm'] = 'ModelForm'

```

The type of the component. Always 'ModelForm'.
