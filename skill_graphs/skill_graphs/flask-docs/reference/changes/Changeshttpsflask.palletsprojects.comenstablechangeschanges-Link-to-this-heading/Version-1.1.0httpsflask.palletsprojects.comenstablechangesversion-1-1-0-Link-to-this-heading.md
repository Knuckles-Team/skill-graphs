## Version 1.1.0[¶](https://flask.palletsprojects.com/en/stable/changes/#version-1-1-0 "Link to this heading")
Released 2019-07-04
  * Bump minimum Werkzeug version to >= 0.15.
  * Drop support for Python 3.4.
  * Error handlers for `InternalServerError` or `500` will always be passed an instance of `InternalServerError`. If they are invoked due to an unhandled exception, that original exception is now available as `e.original_exception` rather than being passed directly to the handler. The same is true if the handler is for the base `HTTPException`. This makes error handler behavior more consistent.
    * `Flask.finalize_request` is called for all unhandled exceptions even if there is no `500` error handler.
  * `Flask.logger` takes the same name as `Flask.name` (the value passed as `Flask(import_name)`. This reverts 1.0’s behavior of always logging to `"flask.app"`, in order to support multiple apps in the same process. A warning will be shown if old configuration is detected that needs to be moved.
  * `RequestContext.copy` includes the current session object in the request context copy. This prevents `session` pointing to an out-of-date object.
  * Using built-in RequestContext, unprintable Unicode characters in Host header will result in a HTTP 400 response and not HTTP 500 as previously.
  * `send_file` supports `PathLike` objects as described in `pathlib` in Python 3.
  * `send_file` supports `BytesIO` partial content.
  * `open_resource` accepts the “rt” file mode. This still does the same thing as “r”.
  * The `MethodView.methods` attribute set in a base class is used by subclasses.
  * `Flask.jinja_options` is a `dict` instead of an `ImmutableDict` to allow easier configuration. Changes must still be made before creating the environment.
  * Flask’s `JSONMixin` for the request and response wrappers was moved into Werkzeug. Use Werkzeug’s version with Flask-specific support. This bumps the Werkzeug dependency to >= 0.15.
  * The `flask` command entry point is simplified to take advantage of Werkzeug 0.15’s better reloader support. This bumps the Werkzeug dependency to >= 0.15.
  * Support `static_url_path` that ends with a forward slash.
  * Support empty `static_folder` without requiring setting an empty `static_url_path` as well.
  * `jsonify` supports `dataclass` objects.
  * Allow customizing the `Flask.url_map_class` used for routing.
  * The development server port can be set to 0, which tells the OS to pick an available port.
  * The return value from `cli.load_dotenv` is more consistent with the documentation. It will return `False` if python-dotenv is not installed, or if the given path isn’t a file.
  * Signaling support has a stub for the `connect_via` method when the Blinker library is not installed.
  * Add an `--extra-files` option to the `flask run` CLI command to specify extra files that will trigger the reloader on change.
  * Allow returning a dictionary from a view function. Similar to how returning a string will produce a `text/html` response, returning a dict will call `jsonify` to produce a `application/json` response.
  * Blueprints have a `cli` Click group like `app.cli`. CLI commands registered with a blueprint will be available as a group under the `flask` command.
  * When using the test client as a context manager (`with client:`), all preserved request contexts are popped when the block exits, ensuring nested contexts are cleaned up correctly.
  * Show a better error message when the view return type is not supported.
  * `flask.testing.make_test_environ_builder()` has been deprecated in favour of a new class `flask.testing.EnvironBuilder`.
  * The `flask run` command no longer fails if Python is not built with SSL support. Using the `--cert` option will show an appropriate error message.
  * URL matching now occurs after the request context is pushed, rather than when it’s created. This allows custom URL converters to access the app and request contexts, such as to query a database for an id.
