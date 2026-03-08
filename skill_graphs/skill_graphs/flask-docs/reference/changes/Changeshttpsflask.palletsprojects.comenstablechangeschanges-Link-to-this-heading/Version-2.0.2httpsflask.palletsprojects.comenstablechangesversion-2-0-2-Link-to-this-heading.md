## Version 2.0.2[¶](https://flask.palletsprojects.com/en/stable/changes/#version-2-0-2 "Link to this heading")
Released 2021-10-04
  * Fix type annotation for `teardown_*` methods.
  * Fix type annotation for `before_request` and `before_app_request` decorators.
  * Fixed the issue where typing requires template global decorators to accept functions with no arguments.
  * Support View and MethodView instances with async handlers.
  * Enhance typing of `app.errorhandler` decorator.
  * Fix registering a blueprint twice with differing names.
  * Fix the type of `static_folder` to accept `pathlib.Path`.
  * `jsonify` handles `decimal.Decimal` by encoding to `str`.
  * Correctly handle raising deferred errors in CLI lazy loading.
  * The CLI loader handles `**kwargs` in a `create_app` function.
  * Fix the order of `before_request` and other callbacks that trigger before the view returns. They are called from the app down to the closest nested blueprint.
