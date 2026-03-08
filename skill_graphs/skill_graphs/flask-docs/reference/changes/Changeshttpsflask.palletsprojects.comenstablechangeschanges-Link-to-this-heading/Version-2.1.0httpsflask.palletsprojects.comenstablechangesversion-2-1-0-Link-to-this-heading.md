## Version 2.1.0[¶](https://flask.palletsprojects.com/en/stable/changes/#version-2-1-0 "Link to this heading")
Released 2022-03-28
  * Drop support for Python 3.6.
  * Update Click dependency to >= 8.0.
  * Remove previously deprecated code.
    * The CLI does not pass `script_info` to app factory functions.
    * `config.from_json` is replaced by `config.from_file(name, load=json.load)`.
    * `json` functions no longer take an `encoding` parameter.
    * `safe_join` is removed, use `werkzeug.utils.safe_join` instead.
    * `total_seconds` is removed, use `timedelta.total_seconds` instead.
    * The same blueprint cannot be registered with the same name. Use `name=` when registering to specify a unique name.
    * The test client’s `as_tuple` parameter is removed. Use `response.request.environ` instead.
  * Some parameters in `send_file` and `send_from_directory` were renamed in 2.0. The deprecation period for the old names is extended to 2.2. Be sure to test with deprecation warnings visible.
    * `attachment_filename` is renamed to `download_name`.
    * `cache_timeout` is renamed to `max_age`.
    * `add_etags` is renamed to `etag`.
    * `filename` is renamed to `path`.
  * The `RequestContext.g` property is deprecated. Use `g` directly or `AppContext.g` instead.
  * `copy_current_request_context` can decorate async functions.
  * The CLI uses `importlib.metadata` instead of `pkg_resources` to load command entry points.
  * Overriding `FlaskClient.open` will not cause an error on redirect.
  * Add an `--exclude-patterns` option to the `flask run` CLI command to specify patterns that will be ignored by the reloader.
  * When using lazy loading (the default with the debugger), the Click context from the `flask run` command remains available in the loader thread.
  * Deleting the session cookie uses the `httponly` flag.
  * Relax typing for `errorhandler` to allow the user to use more precise types and decorate the same function multiple times.
  * Fix typing for `__exit__` methods for better compatibility with `ExitStack`.
  * From Werkzeug, for redirect responses the `Location` header URL will remain relative, and exclude the scheme and domain, by default.
  * Add `Config.from_prefixed_env()` to load config values from environment variables that start with `FLASK_` or another prefix. This parses values as JSON by default, and allows setting keys in nested dicts.
