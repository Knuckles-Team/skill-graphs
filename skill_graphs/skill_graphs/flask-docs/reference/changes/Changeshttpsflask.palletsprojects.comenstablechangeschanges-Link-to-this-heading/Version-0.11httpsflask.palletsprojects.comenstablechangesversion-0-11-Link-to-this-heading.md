## Version 0.11[¶](https://flask.palletsprojects.com/en/stable/changes/#version-0-11 "Link to this heading")
Released 2016-05-29, codename Absinthe
  * Added support to serializing top-level arrays to `jsonify`. This introduces a security risk in ancient browsers.
  * Added before_render_template signal.
  * Added `**kwargs` to `Flask.test_client` to support passing additional keyword arguments to the constructor of `Flask.test_client_class`.
  * Added `SESSION_REFRESH_EACH_REQUEST` config key that controls the set-cookie behavior. If set to `True` a permanent session will be refreshed each request and get their lifetime extended, if set to `False` it will only be modified if the session actually modifies. Non permanent sessions are not affected by this and will always expire if the browser window closes.
  * Made Flask support custom JSON mimetypes for incoming data.
  * Added support for returning tuples in the form `(response, headers)` from a view function.
  * Added `Config.from_json`.
  * Added `Flask.config_class`.
  * Added `Config.get_namespace`.
  * Templates are no longer automatically reloaded outside of debug mode. This can be configured with the new `TEMPLATES_AUTO_RELOAD` config key.
  * Added a workaround for a limitation in Python 3.3’s namespace loader.
  * Added support for explicit root paths when using Python 3.3’s namespace packages.
  * Added `flask` and the `flask.cli` module to start the local debug server through the click CLI system. This is recommended over the old `flask.run()` method as it works faster and more reliable due to a different design and also replaces `Flask-Script`.
  * Error handlers that match specific classes are now checked first, thereby allowing catching exceptions that are subclasses of HTTP exceptions (in `werkzeug.exceptions`). This makes it possible for an extension author to create exceptions that will by default result in the HTTP error of their choosing, but may be caught with a custom error handler if desired.
  * Added `Config.from_mapping`.
  * Flask will now log by default even if debug is disabled. The log format is now hardcoded but the default log handling can be disabled through the `LOGGER_HANDLER_POLICY` configuration key.
  * Removed deprecated module functionality.
  * Added the `EXPLAIN_TEMPLATE_LOADING` config flag which when enabled will instruct Flask to explain how it locates templates. This should help users debug when the wrong templates are loaded.
  * Enforce blueprint handling in the order they were registered for template loading.
  * Ported test suite to py.test.
  * Deprecated `request.json` in favour of `request.get_json()`.
  * Add “pretty” and “compressed” separators definitions in jsonify() method. Reduces JSON response size when `JSONIFY_PRETTYPRINT_REGULAR=False` by removing unnecessary white space included by default after separators.
  * JSON responses are now terminated with a newline character, because it is a convention that UNIX text files end with a newline and some clients don’t deal well when this newline is missing.
  * The automatically provided `OPTIONS` method is now correctly disabled if the user registered an overriding rule with the lowercase-version `options`.
  * `flask.json.jsonify` now supports the `datetime.date` type.
  * Don’t leak exception info of already caught exceptions to context teardown handlers.
  * Allow custom Jinja environment subclasses.
  * Updated extension dev guidelines.
  * `flask.g` now has `pop()` and `setdefault` methods.
  * Turn on autoescape for `flask.templating.render_template_string` by default.
  * `flask.ext` is now deprecated.
  * `send_from_directory` now raises BadRequest if the filename is invalid on the server OS.
  * Added the `JSONIFY_MIMETYPE` configuration variable.
  * Exceptions during teardown handling will no longer leave bad application contexts lingering around.
  * Fixed broken `test_appcontext_signals()` test case.
  * Raise an `AttributeError` in `helpers.find_package` with a useful message explaining why it is raised when a `is_package()` method.
  * Fixed an issue causing exceptions raised before entering a request or app context to be passed to teardown handlers.
  * Fixed an issue with query parameters getting removed from requests in the test client when absolute URLs were requested.
  * Made `@before_first_request` into a decorator as intended.
  * Fixed an etags bug when sending a file streams with a name.
  * Fixed `send_from_directory` not expanding to the application root path correctly.
  * Changed logic of before first request handlers to flip the flag after invoking. This will allow some uses that are potentially dangerous but should probably be permitted.
  * Fixed Python 3 bug when a handler from `app.url_build_error_handlers` reraises the `BuildError`.
