## Version 0.7[¶](https://flask.palletsprojects.com/en/stable/changes/#version-0-7 "Link to this heading")
Released 2011-06-28, codename Grappa
  * Added `Flask.make_default_options_response` which can be used by subclasses to alter the default behavior for `OPTIONS` responses.
  * Unbound locals now raise a proper `RuntimeError` instead of an `AttributeError`.
  * Mimetype guessing and etag support based on file objects is now deprecated for `send_file` because it was unreliable. Pass filenames instead or attach your own etags and provide a proper mimetype by hand.
  * Static file handling for modules now requires the name of the static folder to be supplied explicitly. The previous autodetection was not reliable and caused issues on Google’s App Engine. Until 1.0 the old behavior will continue to work but issue dependency warnings.
  * Fixed a problem for Flask to run on jython.
  * Added a `PROPAGATE_EXCEPTIONS` configuration variable that can be used to flip the setting of exception propagation which previously was linked to `DEBUG` alone and is now linked to either `DEBUG` or `TESTING`.
  * Flask no longer internally depends on rules being added through the `add_url_rule` function and can now also accept regular werkzeug rules added to the url map.
  * Added an `endpoint` method to the flask application object which allows one to register a callback to an arbitrary endpoint with a decorator.
  * Use Last-Modified for static file sending instead of Date which was incorrectly introduced in 0.6.
  * Added `create_jinja_loader` to override the loader creation process.
  * Implemented a silent flag for `config.from_pyfile`.
  * Added `teardown_request` decorator, for functions that should run at the end of a request regardless of whether an exception occurred. Also the behavior for `after_request` was changed. It’s now no longer executed when an exception is raised.
  * Implemented `has_request_context`.
  * Deprecated `init_jinja_globals`. Override the `Flask.create_jinja_environment` method instead to achieve the same functionality.
  * Added `safe_join`.
  * The automatic JSON request data unpacking now looks at the charset mimetype parameter.
  * Don’t modify the session on `get_flashed_messages` if there are no messages in the session.
  * `before_request` handlers are now able to abort requests with errors.
  * It is not possible to define user exception handlers. That way you can provide custom error messages from a central hub for certain errors that might occur during request processing (for instance database connection errors, timeouts from remote resources etc.).
  * Blueprints can provide blueprint specific error handlers.
  * Implemented generic class-based views.
