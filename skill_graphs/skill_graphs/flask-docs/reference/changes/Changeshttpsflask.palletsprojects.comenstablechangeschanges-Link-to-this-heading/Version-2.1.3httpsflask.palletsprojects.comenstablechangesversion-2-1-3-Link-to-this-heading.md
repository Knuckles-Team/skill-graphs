## Version 2.1.3[¶](https://flask.palletsprojects.com/en/stable/changes/#version-2-1-3 "Link to this heading")
Released 2022-07-13
  * Inline some optional imports that are only used for certain CLI commands.
  * Relax type annotation for `after_request` functions.
  * `instance_path` for namespace packages uses the path closest to the imported submodule.
  * Clearer error message when `render_template` and `render_template_string` are used outside an application context.
