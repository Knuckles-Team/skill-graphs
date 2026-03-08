## Version 2.0.3[¶](https://flask.palletsprojects.com/en/stable/changes/#version-2-0-3 "Link to this heading")
Released 2022-02-14
  * The test client’s `as_tuple` parameter is deprecated and will be removed in Werkzeug 2.1. It is now also deprecated in Flask, to be removed in Flask 2.1, while remaining compatible with both in 2.0.x. Use `response.request.environ` instead.
  * Fix type annotation for `errorhandler` decorator.
  * Revert a change to the CLI that caused it to hide `ImportError` tracebacks when importing the application.
  * `app.json_encoder` and `json_decoder` are only passed to `dumps` and `loads` if they have custom behavior. This improves performance, mainly on PyPy.
  * Clearer error message when `after_this_request` is used outside a request context.
