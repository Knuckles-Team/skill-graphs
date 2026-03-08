## Version 2.3.0[¶](https://flask.palletsprojects.com/en/stable/changes/#version-2-3-0 "Link to this heading")
Released 2023-04-25
  * Drop support for Python 3.7.
  * Update minimum requirements to the latest versions: Werkzeug>=2.3.0, Jinja2>3.1.2, itsdangerous>=2.1.2, click>=8.1.3.
  * Remove previously deprecated code.
    * The `push` and `pop` methods of the deprecated `_app_ctx_stack` and `_request_ctx_stack` objects are removed. `top` still exists to give extensions more time to update, but it will be removed.
    * The `FLASK_ENV` environment variable, `ENV` config key, and `app.env` property are removed.
    * The `session_cookie_name`, `send_file_max_age_default`, `use_x_sendfile`, `propagate_exceptions`, and `templates_auto_reload` properties on `app` are removed.
    * The `JSON_AS_ASCII`, `JSON_SORT_KEYS`, `JSONIFY_MIMETYPE`, and `JSONIFY_PRETTYPRINT_REGULAR` config keys are removed.
    * The `app.before_first_request` and `bp.before_app_first_request` decorators are removed.
    * `json_encoder` and `json_decoder` attributes on app and blueprint, and the corresponding `json.JSONEncoder` and `JSONDecoder` classes, are removed.
    * The `json.htmlsafe_dumps` and `htmlsafe_dump` functions are removed.
    * Calling setup methods on blueprints after registration is an error instead of a warning.
  * Importing `escape` and `Markup` from `flask` is deprecated. Import them directly from `markupsafe` instead.
  * The `app.got_first_request` property is deprecated.
  * The `locked_cached_property` decorator is deprecated. Use a lock inside the decorated function if locking is needed.
  * Signals are always available. `blinker>=1.6.2` is a required dependency. The `signals_available` attribute is deprecated.
  * Signals support `async` subscriber functions.
  * Remove uses of locks that could cause requests to block each other very briefly.
  * Use modern packaging metadata with `pyproject.toml` instead of `setup.cfg`.
  * Ensure subdomains are applied with nested blueprints.
  * `config.from_file` can use `text=False` to indicate that the parser wants a binary file instead.
  * If a blueprint is created with an empty name it raises a `ValueError`.
  * `SESSION_COOKIE_DOMAIN` does not fall back to `SERVER_NAME`. The default is not to set the domain, which modern browsers interpret as an exact match rather than a subdomain match. Warnings about `localhost` and IP addresses are also removed.
  * The `routes` command shows each rule’s `subdomain` or `host` when domain matching is in use.
  * Use postponed evaluation of annotations.
