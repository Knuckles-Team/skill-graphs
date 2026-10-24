## Stream Helpers[¶](https://flask.palletsprojects.com/en/stable/api/#stream-helpers "Link to this heading")

flask.stream_with_context(_generator_or_function :_) → [¶](https://flask.palletsprojects.com/en/stable/api/#flask.stream_with_context "Link to this definition")


flask.stream_with_context(_generator_or_function :[[...],]_) → [[],]

Wrap a response generator function so that it runs inside the current request context. This keeps [`request`](https://flask.palletsprojects.com/en/stable/api/#flask.request "flask.request"), [`session`](https://flask.palletsprojects.com/en/stable/api/#flask.session "flask.session"), and [`g`](https://flask.palletsprojects.com/en/stable/api/#flask.g "flask.g") available, even though at the point the generator runs the request context will typically have ended.
Warning
Due to the following caveat, it is often safer to pass the data you need as arguments to the generator, rather than relying on the context objects.
More headers cannot be sent after the body has begun. Therefore, you must make sure all headers are set before starting the response. In particular, if the generator will access `session`, be sure to do so in the view as well so that the `Vary: cookie` header will be set. Do not modify the session in the generator, as the `Set-Cookie` header will already be sent.
Use it as a decorator on a generator function:
```
from flask import stream_with_context, request, Response

@app.get("/stream")
def streamed_response():
    @stream_with_context
    def generate():
        yield "Hello "
        yield request.args["name"]
        yield "!"

    return Response(generate())

```

Or use it as a wrapper around a created generator:
```
from flask import stream_with_context, request, Response

@app.get("/stream")
def streamed_response():
    def generate():
        yield "Hello "
        yield request.args["name"]
        yield "!"

    return Response(stream_with_context(generate()))

```

Changelog
Added in version 0.9.
