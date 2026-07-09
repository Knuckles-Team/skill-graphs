    """

    def decorator(func: DecoratedCallable) -> DecoratedCallable:
        self.add_event_handler(event_type, func)
        return func

    return decorator

```

---|---
[ Previous  Dependencies - Depends() and Security()  ](https://fastapi.tiangolo.com/reference/dependencies/) [ Next  Background Tasks - BackgroundTasks  ](https://fastapi.tiangolo.com/reference/background/)
The FastAPI trademark is owned by [@tiangolo](https://tiangolo.com) and is registered in the US and across other regions
Made with
[ ](https://tiangolo.com "tiangolo.com")
