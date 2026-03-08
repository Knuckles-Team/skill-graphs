## Version 1.0.3[¶](https://flask.palletsprojects.com/en/stable/changes/#version-1-0-3 "Link to this heading")
Released 2019-05-17
  * `send_file` encodes filenames as ASCII instead of Latin-1 (ISO-8859-1). This fixes compatibility with Gunicorn, which is stricter about header encodings than
  * Allow custom CLIs using `FlaskGroup` to set the debug flag without it always being overwritten based on environment variables.
  * `flask --version` outputs Werkzeug’s version and simplifies the Python version.
  * `send_file` handles an `attachment_filename` that is a native Python 2 string (bytes) with UTF-8 coded bytes.
  * A catch-all error handler registered for `HTTPException` will not handle `RoutingException`, which is used internally during routing. This fixes the unexpected behavior that had been introduced in 1.0.
  * Passing the `json` argument to `app.test_client` does not push/pop an extra app context.
