### Navigation
  * [index](https://flask.palletsprojects.com/en/stable/genindex/ "General Index")
  * [modules](https://flask.palletsprojects.com/en/stable/py-modindex/ "Python Module Index") |
  * [next](https://flask.palletsprojects.com/en/stable/async-await/ "Using async and await") |
  * [previous](https://flask.palletsprojects.com/en/stable/deploying/apache-httpd/ "Apache httpd") |
  * [Flask Documentation (3.1.x)](https://flask.palletsprojects.com/en/stable/) »
  * [Async with Gevent](https://flask.palletsprojects.com/en/stable/gevent/)


# Async with Gevent[¶](https://flask.palletsprojects.com/en/stable/gevent/#async-with-gevent "Link to this heading")
Gevent is a reliable way to handle numerous, long lived, concurrent connections, and to achieve similar capabilities to ASGI and asyncio. This works without needing to write `async def` or `await` anywhere, but relies on gevent and greenlet’s low level manipulation of the Python interpreter.
Deciding whether you should use gevent with Flask, or [Quart](https://quart.palletsprojects.com), or something else, is ultimately up to understanding the specific needs of your project.
## Enabling gevent[¶](https://flask.palletsprojects.com/en/stable/gevent/#enabling-gevent "Link to this heading")
You need to apply gevent’s patching as early as possible in your code. This enables gevent’s underlying event loop and converts many Python internals to run inside it. Add the following at the top of your project’s module or top `__init__.py`:
```
import gevent.monkey
gevent.monkey.patch_all()

```

When deploying in production, use [Gunicorn](https://flask.palletsprojects.com/en/stable/deploying/gunicorn/) or [uWSGI](https://flask.palletsprojects.com/en/stable/deploying/uwsgi/) with a gevent worker, as described on those pages.
To run concurrent tasks within your own code, such as views, use
```
@app.post("/send")
def send_email():
    gevent.spawn(email.send, to="example@example.example", text="example")
    return "Email is being sent."

```

If you need to access `request` or other Flask context globals within the spawned function, decorate the function with [`stream_with_context()`](https://flask.palletsprojects.com/en/stable/api/#flask.stream_with_context "flask.stream_with_context") or [`copy_current_request_context()`](https://flask.palletsprojects.com/en/stable/api/#flask.copy_current_request_context "flask.copy_current_request_context"). Prefer passing the exact data you need when spawning the function, rather than using the decorators.
Note
When using gevent, greenlet>=1.0 is required. When using PyPy, PyPy>=7.3.7 is required.
## Combining with `async`/`await`[¶](https://flask.palletsprojects.com/en/stable/gevent/#combining-with-async-await "Link to this heading")
Gevent’s patching does not interact well with Flask’s built-in asyncio support. If you want to use Gevent and asyncio in the same app, you’ll need to override [`flask.Flask.async_to_sync()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.async_to_sync "flask.Flask.async_to_sync") to run async functions inside gevent.
```
import gevent.monkey
gevent.monkey.patch_all()

import asyncio
from flask import Flask, request

loop = asyncio.EventLoop()
gevent.spawn(loop.run_forever)

class GeventFlask(Flask):
    def async_to_sync(self, func):
        def run(*args, **kwargs):
            coro = func(*args, **kwargs)
            future = asyncio.run_coroutine_threadsafe(coro, loop)
            return future.result()

        return run

app = GeventFlask(__name__)

@app.get("/")
async def greet():
    await asyncio.sleep(1)
    return f"Hello, {request.args.get("name", "World")}!"

```

This starts an asyncio event loop in a gevent worker. Async functions are scheduled on that event loop. This may still have limitations, and may need to be modified further when using other asyncio implementations.
### libuv[¶](https://flask.palletsprojects.com/en/stable/gevent/#libuv "Link to this heading")
`async_to_sync` code from the previous section to work with uvloop, but that’s not currently known.
To enable gevent’s libuv support, add the following at the _very_ top of your code, before `gevent.monkey.patch_all()`:
```
import gevent
gevent.config.loop = "libuv"

import gevent.monkey
gevent.monkey.patch_all()

```

[ ![Logo of Flask](https://flask.palletsprojects.com/en/stable/_static/flask-logo.svg) ](https://flask.palletsprojects.com/en/stable/)
### Contents
  * [Async with Gevent](https://flask.palletsprojects.com/en/stable/gevent/)
    * [Enabling gevent](https://flask.palletsprojects.com/en/stable/gevent/#enabling-gevent)
    * [Combining with `async`/`await`](https://flask.palletsprojects.com/en/stable/gevent/#combining-with-async-await)
      * [libuv](https://flask.palletsprojects.com/en/stable/gevent/#libuv)


### Navigation
  * [Overview](https://flask.palletsprojects.com/en/stable/)
    * Previous: [Apache httpd](https://flask.palletsprojects.com/en/stable/deploying/apache-httpd/ "previous chapter")
    * Next: [Using `async` and `await`](https://flask.palletsprojects.com/en/stable/async-await/ "next chapter")


### Quick search
·
![](https://server.ethicalads.io/proxy/view/10198/019ccc19-fbbb-73e1-ae2b-ca6fbf16d95b/)
