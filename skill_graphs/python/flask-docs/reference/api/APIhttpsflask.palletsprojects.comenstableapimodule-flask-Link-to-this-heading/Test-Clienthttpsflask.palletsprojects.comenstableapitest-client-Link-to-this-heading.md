## Test Client[¶](https://flask.palletsprojects.com/en/stable/api/#test-client "Link to this heading")

_class_ flask.testing.FlaskClient(_* args_, _** kwargs_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.testing.FlaskClient "Link to this definition")

Works like a regular Werkzeug test client but has knowledge about Flask’s contexts to defer the cleanup of the request context until the end of a `with` block. For general information about how to use this class refer to [`werkzeug.test.Client`](https://werkzeug.palletsprojects.com/en/stable/test/#werkzeug.test.Client "\(in Werkzeug v3.1.x\)").
Changelog
Changed in version 0.12: `app.test_client()` includes preset default environment, which can be set after instantiation of the `app.test_client()` object in `client.environ_base`.
Basic usage is outlined in the [Testing Flask Applications](https://flask.palletsprojects.com/en/stable/testing/) chapter.

Parameters:

  * **args** (_t.Any_)
  * **kwargs** (_t.Any_)



session_transaction(_* args_, _** kwargs_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.testing.FlaskClient.session_transaction "Link to this definition")

When used in combination with a `with` statement this opens a session transaction. This can be used to modify the session that the test client uses. Once the `with` block is left the session is stored back.
```
with client.session_transaction() as session:
    session['value'] = 42

```

Internally this is implemented by going through a temporary test request context and since session handling could depend on request variables this function accepts the same arguments as [`test_request_context()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.test_request_context "flask.Flask.test_request_context") which are directly passed through.

Parameters:

  * **args** (
  * **kwargs** (



Return type:

[_SessionMixin_](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SessionMixin "flask.sessions.SessionMixin")]

open(_* args_, _buffered =False_, _follow_redirects =False_, _** kwargs_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.testing.FlaskClient.open "Link to this definition")

Generate an environ dict from the given arguments, make a request to the application using it, and return the response.

Parameters:

  * **args** (_t.Any_) – Passed to `EnvironBuilder` to create the environ for the request. If a single arg is passed, it can be an existing `EnvironBuilder` or an environ dict.
  * **buffered** (`close()` method, it is called automatically.
  * **follow_redirects** (`TestResponse.history` lists the intermediate responses.
  * **kwargs** (_t.Any_)



Return type:

TestResponse Changelog
Changed in version 2.1: Removed the `as_tuple` parameter.
Changed in version 2.0: The request input stream is closed when calling `response.close()`. Input streams for redirects are automatically closed.
Changed in version 0.5: If a dict is provided as file in the dict for the `data` parameter the content type has to be called `content_type` instead of `mimetype`. This change was made for consistency with `werkzeug.FileWrapper`.
Changed in version 0.5: Added the `follow_redirects` parameter.
