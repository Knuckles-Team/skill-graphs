## Version 1.0[¶](https://flask.palletsprojects.com/en/stable/changes/#version-1-0 "Link to this heading")
Released 2018-04-26
  * Python 2.6 and 3.3 are no longer supported.
  * Bump minimum dependency versions to the latest stable versions: Werkzeug >= 0.14, Jinja >= 2.10, itsdangerous >= 0.24, Click >= 5.1.
  * Skip `app.run` when a Flask application is run from the command line. This avoids some behavior that was confusing to debug.
  * Change the default for `JSONIFY_PRETTYPRINT_REGULAR` to `False`. `~json.jsonify` returns a compact format by default, and an indented format in debug mode.
  * `Flask.__init__` accepts the `host_matching` argument and sets it on `Flask.url_map`.
  * `Flask.__init__` accepts the `static_host` argument and passes it as the `host` argument when defining the static route.
  * `send_file` supports Unicode in `attachment_filename`.
  * Pass `_scheme` argument from `url_for` to `Flask.handle_url_build_error`.
  * `Flask.add_url_rule` accepts the `provide_automatic_options` argument to disable adding the `OPTIONS` method.
  * `MethodView` subclasses inherit method handlers from base classes.
  * Errors caused while opening the session at the beginning of the request are handled by the app’s error handlers.
  * Blueprints gained `Blueprint.json_encoder` and `Blueprint.json_decoder` attributes to override the app’s encoder and decoder.
  * `Flask.make_response` raises `TypeError` instead of `ValueError` for bad response types. The error messages have been improved to describe why the type is invalid.
  * Add `routes` CLI command to output routes registered on the application.
  * Show warning when session cookie domain is a bare hostname or an IP address, as these may not behave properly in some browsers, such as Chrome.
  * Allow IP address as exact session cookie domain.
  * `SESSION_COOKIE_DOMAIN` is set if it is detected through `SERVER_NAME`.
  * Auto-detect zero-argument app factory called `create_app` or `make_app` from `FLASK_APP`.
  * Factory functions are not required to take a `script_info` parameter to work with the `flask` command. If they take a single parameter or a parameter named `script_info`, the `ScriptInfo` object will be passed.
  * `FLASK_APP` can be set to an app factory, with arguments if needed, for example `FLASK_APP=myproject.app:create_app('dev')`.
  * `FLASK_APP` can point to local packages that are not installed in editable mode, although `pip install -e` is still preferred.
  * The `View` class attribute `View.provide_automatic_options` is set in `View.as_view`, to be detected by `Flask.add_url_rule`.
  * Error handling will try handlers registered for `blueprint, code`, `app, code`, `blueprint, exception`, `app, exception`.
  * `Cookie` is added to the response’s `Vary` header if the session is accessed at all during the request (and not deleted).
  * `Flask.test_request_context` accepts `subdomain` and `url_scheme` arguments for use when building the base URL.
  * Set `APPLICATION_ROOT` to `'/'` by default. This was already the implicit default when it was set to `None`.
  * `TRAP_BAD_REQUEST_ERRORS` is enabled by default in debug mode. `BadRequestKeyError` has a message with the bad key in debug mode instead of the generic bad request message.
  * Allow registering new tags with `TaggedJSONSerializer` to support storing other types in the session cookie.
  * Only open the session if the request has not been pushed onto the context stack yet. This allows `stream_with_context` generators to access the same session that the containing view uses.
  * Add `json` keyword argument for the test client request methods. This will dump the given object as JSON and set the appropriate content type.
  * Extract JSON handling to a mixin applied to both the `Request` and `Response` classes. This adds the `Response.is_json` and `Response.get_json` methods to the response to make testing JSON response much easier.
  * Removed error handler caching because it caused unexpected results for some exception inheritance hierarchies. Register handlers explicitly for each exception if you want to avoid traversing the MRO.
  * Fix incorrect JSON encoding of aware, non-UTC datetimes.
  * Template auto reloading will honor debug mode even if `Flask.jinja_env` was already accessed.
  * The following old deprecated code was removed.
    * `flask.ext` - import extensions directly by their name instead of through the `flask.ext` namespace. For example, `import flask.ext.sqlalchemy` becomes `import flask_sqlalchemy`.
    * `Flask.init_jinja_globals` - extend `Flask.create_jinja_environment` instead.
    * `Flask.error_handlers` - tracked by `Flask.error_handler_spec`, use `Flask.errorhandler` to register handlers.
    * `Flask.request_globals_class` - use `Flask.app_ctx_globals_class` instead.
    * `Flask.static_path` - use `Flask.static_url_path` instead.
    * `Request.module` - use `Request.blueprint` instead.
  * The `Request.json` property is no longer deprecated.
  * Support passing a `EnvironBuilder` or `dict` to `test_client.open`.
  * The `flask` command and `Flask.run` will load environment variables from `.env` and `.flaskenv` files if python-dotenv is installed.
  * When passing a full URL to the test client, the scheme in the URL is used instead of `PREFERRED_URL_SCHEME`.
  * `Flask.logger` has been simplified. `LOGGER_NAME` and `LOGGER_HANDLER_POLICY` config was removed. The logger is always named `flask.app`. The level is only set on first access, it doesn’t check `Flask.debug` each time. Only one format is used, not different ones depending on `Flask.debug`. No handlers are removed, and a handler is only added if no handlers are already configured.
  * Blueprint view function names may not contain dots.
  * Fix a `ValueError` caused by invalid `Range` requests in some cases.
  * The development server uses threads by default.
  * Loading config files with `silent=True` will ignore `ENOTDIR` errors.
  * Pass `--cert` and `--key` options to `flask run` to run the development server over HTTPS.
  * Added `SESSION_COOKIE_SAMESITE` to control the `SameSite` attribute on the session cookie.
  * Added `Flask.test_cli_runner` to create a Click runner that can invoke Flask CLI commands for testing.
  * Subdomain matching is disabled by default and setting `SERVER_NAME` does not implicitly enable it. It can be enabled by passing `subdomain_matching=True` to the `Flask` constructor.
  * A single trailing slash is stripped from the blueprint `url_prefix` when it is registered with the app.
  * `Request.get_json` doesn’t cache the result if parsing fails when `silent` is true.
  * `Request.get_json` no longer accepts arbitrary encodings. Incoming JSON should be encoded using UTF-8 per
  * Added `MAX_COOKIE_SIZE` and `Response.max_cookie_size` to control when Werkzeug warns about large cookies that browsers may ignore.
  * Updated documentation theme to make docs look better in small windows.
  * Rewrote the tutorial docs and example project to take a more structured approach to help new users avoid common pitfalls.
