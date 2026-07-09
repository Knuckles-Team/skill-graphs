##  FireEvent [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FireEvent "Permanent link")
Bases: `BaseModel`
Fire an event.
###  event `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FireEvent.event "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)event: AnyEvent

```

The event to fire.
###  message `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FireEvent.message "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)message: str | None = None

```

Optional message to display when the event is fired. Defaults to a blank message.
###  type `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/fastui/api/python_components/#fastui.components.FireEvent.type "Permanent link")
```
[](https://docs.pydantic.dev/fastui/api/python_components/#__codelineno-0-1)type: Literal['FireEvent'] = 'FireEvent'

```

The type of the component. Always 'FireEvent'.
