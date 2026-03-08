## Version 3.1.1[¶](https://flask.palletsprojects.com/en/stable/changes/#version-3-1-1 "Link to this heading")
Released 2025-05-13
  * Fix signing key selection order when key rotation is enabled via `SECRET_KEY_FALLBACKS`.
  * Fix type hint for `cli_runner.invoke`.
  * `flask --help` loads the app and plugins first to make sure all commands are shown.
  * Mark sans-io base class as being able to handle views that return `AsyncIterable`. This is not accurate for Flask, but makes typing easier for Quart.
