## Version 2.2.0[¶](https://flask.palletsprojects.com/en/stable/changes/#version-2-2-0 "Link to this heading")
Released 2022-08-01
  * Remove previously deprecated code.
    * Old names for some `send_file` parameters have been removed. `download_name` replaces `attachment_filename`, `max_age` replaces `cache_timeout`, and `etag` replaces `add_etags`. Additionally, `path` replaces `filename` in `send_from_directory`.
    * The `RequestContext.g` property returning `AppContext.g` is removed.
  * Update Werkzeug dependency to >= 2.2.
  * The app and request contexts are managed using Python context vars directly rather than Werkzeug’s `LocalStack`. This should result in better performance and memory use.
    * Extension maintainers, be aware that `_app_ctx_stack.top` and `_request_ctx_stack.top` are deprecated. Store data on `g` instead using a unique prefix, like `g._extension_name_attr`.
  * The `FLASK_ENV` environment variable and `app.env` attribute are deprecated, removing the distinction between development and debug mode. Debug mode should be controlled directly using the `--debug` option or `app.run(debug=True)`.
  * Some attributes that proxied config keys on `app` are deprecated: `session_cookie_name`, `send_file_max_age_default`, `use_x_sendfile`, `propagate_exceptions`, and `templates_auto_reload`. Use the relevant config keys instead.
  * Add new customization points to the `Flask` app object for many previously global behaviors.
    * `flask.url_for` will call `app.url_for`.
    * `flask.abort` will call `app.aborter`. `Flask.aborter_class` and `Flask.make_aborter` can be used to customize this aborter.
    * `flask.redirect` will call `app.redirect`.
    * `flask.json` is an instance of `JSONProvider`. A different provider can be set to use a different JSON library. `flask.jsonify` will call `app.json.response`, other functions in `flask.json` will call corresponding functions in `app.json`.
  * JSON configuration is moved to attributes on the default `app.json` provider. `JSON_AS_ASCII`, `JSON_SORT_KEYS`, `JSONIFY_MIMETYPE`, and `JSONIFY_PRETTYPRINT_REGULAR` are deprecated.
  * Setting custom `json_encoder` and `json_decoder` classes on the app or a blueprint, and the corresponding `json.JSONEncoder` and `JSONDecoder` classes, are deprecated. JSON behavior can now be overridden using the `app.json` provider interface.
  * `json.htmlsafe_dumps` and `json.htmlsafe_dump` are deprecated, the function is built-in to Jinja now.
  * Refactor `register_error_handler` to consolidate error checking. Rewrite some error messages to be more consistent.
  * Use Blueprint decorators and functions intended for setup after registering the blueprint will show a warning. In the next version, this will become an error just like the application setup methods.
  * `before_first_request` is deprecated. Run setup code when creating the application instead.
  * Added the `View.init_every_request` class attribute. If a view subclass sets this to `False`, the view will not create a new instance on every request.
  * A `flask.cli.FlaskGroup` Click group can be nested as a sub-command in a custom CLI.
  * Add `--app` and `--debug` options to the `flask` CLI, instead of requiring that they are set through environment variables.
  * Add `--env-file` option to the `flask` CLI. This allows specifying a dotenv file to load in addition to `.env` and `.flaskenv`.
  * It is no longer required to decorate custom CLI commands on `app.cli` or `blueprint.cli` with `@with_appcontext`, an app context will already be active at that point.
  * `SessionInterface.get_expiration_time` uses a timezone-aware value.
  * View functions can return generators directly instead of wrapping them in a `Response`.
  * Add `stream_template` and `stream_template_string` functions to render a template as a stream of pieces.
  * A new implementation of context preservation during debugging and testing.
    * `request`, `g`, and other context-locals point to the correct data when running code in the interactive debugger console.
    * Teardown functions are always run at the end of the request, even if the context is preserved. They are also run after the preserved context is popped.
    * `stream_with_context` preserves context separately from a `with client` block. It will be cleaned up when `response.get_data()` or `response.close()` is called.
  * Allow returning a list from a view function, to convert it to a JSON response like a dict is.
  * When type checking, allow `TypedDict` to be returned from view functions.
  * Remove the `--eager-loading/--lazy-loading` options from the `flask run` command. The app is always eager loaded the first time, then lazily loaded in the reloader. The reloader always prints errors immediately but continues serving. Remove the internal `DispatchingApp` middleware used by the previous implementation.
