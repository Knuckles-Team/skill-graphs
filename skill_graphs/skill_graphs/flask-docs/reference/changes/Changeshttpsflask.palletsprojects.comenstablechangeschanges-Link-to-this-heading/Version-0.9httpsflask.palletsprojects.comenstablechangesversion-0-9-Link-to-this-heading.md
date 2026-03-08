## Version 0.9[¶](https://flask.palletsprojects.com/en/stable/changes/#version-0-9 "Link to this heading")
Released 2012-07-01, codename Campari
  * The `Request.on_json_loading_failed` now returns a JSON formatted response by default.
  * The `url_for` function now can generate anchors to the generated links.
  * The `url_for` function now can also explicitly generate URL rules specific to a given HTTP method.
  * Logger now only returns the debug log setting if it was not set explicitly.
  * Unregister a circular dependency between the WSGI environment and the request object when shutting down the request. This means that environ `werkzeug.request` will be `None` after the response was returned to the WSGI server but has the advantage that the garbage collector is not needed on CPython to tear down the request unless the user created circular dependencies themselves.
  * Session is now stored after callbacks so that if the session payload is stored in the session you can still modify it in an after request callback.
  * The `Flask` class will avoid importing the provided import name if it can (the required first parameter), to benefit tools which build Flask instances programmatically. The Flask class will fall back to using import on systems with custom module hooks, e.g. Google App Engine, or when the import name is inside a zip archive (usually an egg) prior to Python 2.7.
  * Blueprints now have a decorator to add custom template filters application wide, `Blueprint.app_template_filter`.
  * The Flask and Blueprint classes now have a non-decorator method for adding custom template filters application wide, `Flask.add_template_filter` and `Blueprint.add_app_template_filter`.
  * The `get_flashed_messages` function now allows rendering flashed message categories in separate blocks, through a `category_filter` argument.
  * The `Flask.run` method now accepts `None` for `host` and `port` arguments, using default values when `None`. This allows for calling run using configuration values, e.g. `app.run(app.config.get('MYHOST'), app.config.get('MYPORT'))`, with proper behavior whether or not a config file is provided.
  * The `render_template` method now accepts a either an iterable of template names or a single template name. Previously, it only accepted a single template name. On an iterable, the first template found is rendered.
  * Added `Flask.app_context` which works very similar to the request context but only provides access to the current application. This also adds support for URL generation without an active request context.
  * View functions can now return a tuple with the first instance being an instance of `Response`. This allows for returning `jsonify(error="error msg"), 400` from a view function.
  * `Flask` and `Blueprint` now provide a `get_send_file_max_age` hook for subclasses to override behavior of serving static files from Flask when using `Flask.send_static_file` (used for the default static file handler) and `helpers.send_file`. This hook is provided a filename, which for example allows changing cache controls by file extension. The default max-age for `send_file` and static files can be configured through a new `SEND_FILE_MAX_AGE_DEFAULT` configuration variable, which is used in the default `get_send_file_max_age` implementation.
  * Fixed an assumption in sessions implementation which could break message flashing on sessions implementations which use external storage.
  * Changed the behavior of tuple return values from functions. They are no longer arguments to the response object, they now have a defined meaning.
  * Added `Flask.request_globals_class` to allow a specific class to be used on creation of the `g` instance of each request.
  * Added `required_methods` attribute to view functions to force-add methods on registration.
  * Added `flask.after_this_request`.
  * Added `flask.stream_with_context` and the ability to push contexts multiple times without producing unexpected behavior.
