##  ServerLoad [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.ServerLoad "Permanent link")
Bases: `BaseModel`
A component that will be replaced by the server with the component returned by the given URL.
###  path `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.ServerLoad.path "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)path: str

```

The URL to load the component from.
###  load_trigger `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.ServerLoad.load_trigger "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)load_trigger: PageEvent | None = None

```

Optional event to trigger when the component is loaded.
###  components `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.ServerLoad.components "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)components: list[AnyComponent[](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.AnyComponent "fastui.components.AnyComponent")] | None = None

```

Optional list of components to render while the server is loading the new component(s).
###  sse `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.ServerLoad.sse "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)sse: bool | None = None

```

Optional flag to enable server-sent events (SSE) for the server load.
###  sse_retry `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.ServerLoad.sse_retry "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)sse_retry: int | None = None

```

Optional time in milliseconds to retry the SSE connection.
###  method `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.ServerLoad.method "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)method: Literal['GET', 'POST', 'PATCH', 'PUT', 'DELETE'] | None = None

```

Optional HTTP method to use when loading the component.
###  type `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.ServerLoad.type "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)type: Literal['ServerLoad'] = 'ServerLoad'

```

The type of the component. Always 'ServerLoad'.
