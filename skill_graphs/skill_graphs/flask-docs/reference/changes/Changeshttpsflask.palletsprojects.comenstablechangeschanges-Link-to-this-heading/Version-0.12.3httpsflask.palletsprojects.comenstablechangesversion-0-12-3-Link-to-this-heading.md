## Version 0.12.3[¶](https://flask.palletsprojects.com/en/stable/changes/#version-0-12-3 "Link to this heading")
Released 2018-04-26
  * `Request.get_json` no longer accepts arbitrary encodings. Incoming JSON should be encoded using UTF-8 per
  * Fix a Python warning about imports when using `python -m flask`.
  * Fix a `ValueError` caused by invalid `Range` requests in some cases.
