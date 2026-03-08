## Version 2.0.1[¶](https://flask.palletsprojects.com/en/stable/changes/#version-2-0-1 "Link to this heading")
Released 2021-05-21
  * Re-add the `filename` parameter in `send_from_directory`. The `filename` parameter has been renamed to `path`, the old name is deprecated.
  * Mark top-level names as exported so type checking understands imports in user projects.
  * Fix type annotation for `g` and inform mypy that it is a namespace object that has arbitrary attributes.
  * Fix some types that weren’t available in Python 3.6.0.
  * Improve typing for `send_file`, `send_from_directory`, and `get_send_file_max_age`.
  * Show an error when a blueprint name contains a dot. The `.` has special meaning, it is used to separate (nested) blueprint names and the endpoint name.
  * Combine URL prefixes when nesting blueprints that were created with a `url_prefix` value.
  * Revert a change to the order that URL matching was done. The URL is again matched after the session is loaded, so the session is available in custom URL converters.
  * Re-add deprecated `Config.from_json`, which was accidentally removed early.
  * Improve typing for some functions using `Callable` in their type signatures, focusing on decorator factories.
  * Nested blueprints are registered with their dotted name. This allows different blueprints with the same name to be nested at different locations.
  * `register_blueprint` takes a `name` option to change the (pre-dotted) name the blueprint is registered with. This allows the same blueprint to be registered multiple times with unique names for `url_for`. Registering the same blueprint with the same name multiple times is deprecated.
  * Improve typing for `stream_with_context`.
