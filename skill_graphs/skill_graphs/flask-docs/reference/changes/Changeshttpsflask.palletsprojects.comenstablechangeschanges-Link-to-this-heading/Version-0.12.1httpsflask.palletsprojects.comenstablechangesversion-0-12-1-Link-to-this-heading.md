## Version 0.12.1[¶](https://flask.palletsprojects.com/en/stable/changes/#version-0-12-1 "Link to this heading")
Released 2017-03-31
  * Prevent `flask run` from showing a `NoAppException` when an `ImportError` occurs within the imported application module.
  * Fix encoding behavior of `app.config.from_pyfile` for Python 3.
  * Use the `SERVER_NAME` config if it is present as default values for `app.run`.
  * Call `ctx.auto_pop` with the exception object instead of `None`, in the event that a `BaseException` such as `KeyboardInterrupt` is raised in a request handler.
