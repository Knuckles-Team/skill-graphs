## Version 2.0.0[¶](https://flask.palletsprojects.com/en/stable/changes/#version-2-0-0 "Link to this heading")
Released 2021-05-11
  * Drop support for Python 2 and 3.5.
  * Bump minimum versions of other Pallets projects: Werkzeug >= 2, Jinja2 >= 3, MarkupSafe >= 2, ItsDangerous >= 2, Click >= 8. Be sure to check the change logs for each project. For better compatibility with other applications (e.g. Celery) that still require Click 7, there is no hard dependency on Click 8 yet, but using Click 7 will trigger a DeprecationWarning and Flask 2.1 will depend on Click 8.
  * JSON support no longer uses simplejson. To use another JSON module, override `app.json_encoder` and `json_decoder`.
  * The `encoding` option to JSON functions is deprecated.
  * Passing `script_info` to app factory functions is deprecated. This was not portable outside the `flask` command. Use `click.get_current_context().obj` if it’s needed.
  * The CLI shows better error messages when the app failed to load when looking up commands.
  * Add `SessionInterface.get_cookie_name` to allow setting the session cookie name dynamically.
  * Add `Config.from_file` to load config using arbitrary file loaders, such as `toml.load` or `json.load`. `Config.from_json` is deprecated in favor of this.
  * The `flask run` command will only defer errors on reload. Errors present during the initial call will cause the server to exit with the traceback immediately.
  * `send_file` raises a `ValueError` when passed an `io` object in text mode. Previously, it would respond with 200 OK and an empty file.
  * When using ad-hoc certificates, check for the cryptography library instead of PyOpenSSL.
  * When specifying a factory function with `FLASK_APP`, keyword argument can be passed.
  * When loading a `.env` or `.flaskenv` file, the current working directory is no longer changed to the location of the file.
  * When returning a `(response, headers)` tuple from a view, the headers replace rather than extend existing headers on the response. For example, this allows setting the `Content-Type` for `jsonify()`. Use `response.headers.extend()` if extending is desired.
  * The `Scaffold` class provides a common API for the `Flask` and `Blueprint` classes. `Blueprint` information is stored in attributes just like `Flask`, rather than opaque lambda functions. This is intended to improve consistency and maintainability.
  * Include `samesite` and `secure` options when removing the session cookie.
  * Support passing a `pathlib.Path` to `static_folder`.
  * `send_file` and `send_from_directory` are wrappers around the implementations in `werkzeug.utils`.
  * Some `send_file` parameters have been renamed, the old names are deprecated. `attachment_filename` is renamed to `download_name`. `cache_timeout` is renamed to `max_age`. `add_etags` is renamed to `etag`.
  * `send_file` passes `download_name` even if `as_attachment=False` by using `Content-Disposition: inline`.
  * `send_file` sets `conditional=True` and `max_age=None` by default. `Cache-Control` is set to `no-cache` if `max_age` is not set, otherwise `public`. This tells browsers to validate conditional requests instead of using a timed cache.
  * `helpers.safe_join` is deprecated. Use `werkzeug.utils.safe_join` instead.
  * The request context does route matching before opening the session. This could allow a session interface to change behavior based on `request.endpoint`.
  * Use Jinja’s implementation of the `|tojson` filter.
  * Add route decorators for common HTTP methods. For example, `@app.post("/login")` is a shortcut for `@app.route("/login", methods=["POST"])`.
  * Support async views, error handlers, before and after request, and teardown functions.
  * Support nesting blueprints.
  * Set the default encoding to “UTF-8” when loading `.env` and `.flaskenv` files to allow to use non-ASCII characters.
  * `flask shell` sets up tab and history completion like the default `python` shell if `readline` is installed.
  * `helpers.total_seconds()` is deprecated. Use `timedelta.total_seconds()` instead.
  * Add type hinting.
