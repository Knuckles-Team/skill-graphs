## Version 1.0.4[¶](https://flask.palletsprojects.com/en/stable/changes/#version-1-0-4 "Link to this heading")
Released 2019-07-04
  * The key information for `BadRequestKeyError` is no longer cleared outside debug mode, so error handlers can still access it. This requires upgrading to Werkzeug 0.15.5.
  * `send_file` url quotes the “:” and “/” characters for more compatible UTF-8 filename support in some browsers.
  * Fixes for
  * Show message about dotenv on stderr instead of stdout.
