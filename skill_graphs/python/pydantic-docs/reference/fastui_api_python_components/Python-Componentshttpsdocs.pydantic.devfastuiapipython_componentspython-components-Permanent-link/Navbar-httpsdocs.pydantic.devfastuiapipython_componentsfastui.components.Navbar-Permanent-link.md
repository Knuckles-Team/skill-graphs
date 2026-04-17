##  Navbar [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Navbar "Permanent link")
Bases: `BaseModel`
Navbar component used for moving between pages.
###  title `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Navbar.title "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)title: str | None = None

```

Optional title to display in the navbar.
###  title_event `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Navbar.title_event "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)title_event: AnyEvent | None = None

```

Optional event to trigger when the title is clicked. Often used to navigate to the home page.
###  start_links `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Navbar.start_links "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)start_links: list[Link[](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Link "fastui.components.Link")] = []

```

List of links to render at the start of the navbar.
###  end_links `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Navbar.end_links "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)end_links: list[Link[](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Link "fastui.components.Link")] = []

```

List of links to render at the end of the navbar.
###  class_name `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Navbar.class_name "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)class_name: ClassNameField = None

```

Optional class name to apply to the navbar's HTML component.
###  type `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.Navbar.type "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)type: Literal['Navbar'] = 'Navbar'

```

The type of the component. Always 'Navbar'.
