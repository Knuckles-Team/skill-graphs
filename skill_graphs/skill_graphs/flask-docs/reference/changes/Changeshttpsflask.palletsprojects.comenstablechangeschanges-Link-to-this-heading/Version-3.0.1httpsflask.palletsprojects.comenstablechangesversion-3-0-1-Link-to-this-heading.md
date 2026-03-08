## Version 3.0.1[¶](https://flask.palletsprojects.com/en/stable/changes/#version-3-0-1 "Link to this heading")
Released 2024-01-18
  * Correct type for `path` argument to `send_file`.
  * Fix a typo in an error message for the `flask run --key` option.
  * Session data is untagged without relying on the built-in `json.loads` `object_hook`. This allows other JSON providers that don’t implement that.
  * Address more type findings when using mypy strict mode.
