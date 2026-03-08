## Version 0.12[¶](https://flask.palletsprojects.com/en/stable/changes/#version-0-12 "Link to this heading")
Released 2016-12-21, codename Punsch
  * The cli command now responds to `--version`.
  * Mimetype guessing and ETag generation for file-like objects in `send_file` has been removed.
  * Mimetype guessing in `send_file` now fails loudly and doesn’t fall back to `application/octet-stream`.
  * Make `flask.safe_join` able to join multiple paths like `os.path.join`
  * Revert a behavior change that made the dev server crash instead of returning an Internal Server Error.
  * Correctly invoke response handlers for both regular request dispatching as well as error handlers.
  * Disable logger propagation by default for the app logger.
  * Add support for range requests in `send_file`.
  * `app.test_client` includes preset default environment, which can now be directly set, instead of per `client.get`.
  * Fix crash when running under PyPy3.
