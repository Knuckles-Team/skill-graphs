### Navigation
  * [index](https://flask.palletsprojects.com/en/stable/genindex/ "General Index")
  * [modules](https://flask.palletsprojects.com/en/stable/py-modindex/ "Python Module Index") |
  * [next](https://flask.palletsprojects.com/en/stable/patterns/singlepageapplications/ "Single-Page Applications") |
  * [previous](https://flask.palletsprojects.com/en/stable/patterns/celery/ "Background Tasks with Celery") |
  * [Flask Documentation (3.1.x)](https://flask.palletsprojects.com/en/stable/) »
  * [Patterns for Flask](https://flask.palletsprojects.com/en/stable/patterns/) »
  * [Subclassing Flask](https://flask.palletsprojects.com/en/stable/patterns/subclassing/)


# Subclassing Flask[¶](https://flask.palletsprojects.com/en/stable/patterns/subclassing/#subclassing-flask "Link to this heading")
The [`Flask`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask "flask.Flask") class is designed for subclassing.
For example, you may want to override how request parameters are handled to preserve their order:
```
from flask import Flask, Request
from werkzeug.datastructures import ImmutableOrderedMultiDict
class MyRequest(Request):
    """Request subclass to override request parameter storage"""
    parameter_storage_class = ImmutableOrderedMultiDict
class MyFlask(Flask):
    """Flask subclass using the custom request class"""
    request_class = MyRequest

```

This is the recommended approach for overriding or augmenting Flask’s internal functionality.
[ ![Logo of Flask](https://flask.palletsprojects.com/en/stable/_static/flask-logo.svg) ](https://flask.palletsprojects.com/en/stable/)
### Navigation
  * [Overview](https://flask.palletsprojects.com/en/stable/)
    * [Patterns for Flask](https://flask.palletsprojects.com/en/stable/patterns/)
      * Previous: [Background Tasks with Celery](https://flask.palletsprojects.com/en/stable/patterns/celery/ "previous chapter")
      * Next: [Single-Page Applications](https://flask.palletsprojects.com/en/stable/patterns/singlepageapplications/ "next chapter")


### Quick search
·
![](https://server.ethicalads.io/proxy/view/10129/019ccc1c-0b55-76a1-b9a4-a9a7a7861bcc/)
