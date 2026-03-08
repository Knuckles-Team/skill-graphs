## Version 3.1.2[¶](https://flask.palletsprojects.com/en/stable/changes/#version-3-1-2 "Link to this heading")
Released 2025-08-19
  * `stream_with_context` does not fail inside async views.
  * When using `follow_redirects` in the test client, the final state of `session` is correct.
  * Relax type hint for passing bytes IO to `send_file`.
