## Version 0.6[¶](https://flask.palletsprojects.com/en/stable/changes/#version-0-6 "Link to this heading")
Released 2010-07-27, codename Whisky
  * After request functions are now called in reverse order of registration.
  * OPTIONS is now automatically implemented by Flask unless the application explicitly adds ‘OPTIONS’ as method to the URL rule. In this case no automatic OPTIONS handling kicks in.
  * Static rules are now even in place if there is no static folder for the module. This was implemented to aid GAE which will remove the static folder if it’s part of a mapping in the .yml file.
  * `Flask.config` is now available in the templates as `config`.
  * Context processors will no longer override values passed directly to the render function.
  * Added the ability to limit the incoming request data with the new `MAX_CONTENT_LENGTH` configuration value.
  * The endpoint for the `Module.add_url_rule` method is now optional to be consistent with the function of the same name on the application object.
  * Added a `make_response` function that simplifies creating response object instances in views.
  * Added signalling support based on blinker. This feature is currently optional and supposed to be used by extensions and applications. If you want to use it, make sure to have `blinker` installed.
  * Refactored the way URL adapters are created. This process is now fully customizable with the `Flask.create_url_adapter` method.
  * Modules can now register for a subdomain instead of just an URL prefix. This makes it possible to bind a whole module to a configurable subdomain.
