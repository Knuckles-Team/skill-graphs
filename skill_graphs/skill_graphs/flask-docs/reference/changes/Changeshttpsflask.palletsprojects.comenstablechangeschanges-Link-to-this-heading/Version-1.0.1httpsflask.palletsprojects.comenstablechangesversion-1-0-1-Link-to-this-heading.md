## Version 1.0.1[¶](https://flask.palletsprojects.com/en/stable/changes/#version-1-0-1 "Link to this heading")
Released 2018-04-29
  * Fix registering partials (with no `__name__`) as view functions.
  * Don’t treat lists returned from view functions the same as tuples. Only tuples are interpreted as response data.
  * Extra slashes between a blueprint’s `url_prefix` and a route URL are merged. This fixes some backwards compatibility issues with the change in 1.0.
  * Only trap `BadRequestKeyError` errors in debug mode, not all `BadRequest` errors. This allows `abort(400)` to continue working as expected.
  * The `FLASK_SKIP_DOTENV` environment variable can be set to `1` to skip automatically loading dotenv files.
