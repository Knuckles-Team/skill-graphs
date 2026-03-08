## Version 3.0.0[¶](https://flask.palletsprojects.com/en/stable/changes/#version-3-0-0 "Link to this heading")
Released 2023-09-30
  * Remove previously deprecated code.
  * Deprecate the `__version__` attribute. Use feature detection, or `importlib.metadata.version("flask")`, instead.
  * Restructure the code such that the Flask (app) and Blueprint classes have Sans-IO bases.
  * Allow self as an argument to url_for.
  * Require Werkzeug >= 3.0.0.
