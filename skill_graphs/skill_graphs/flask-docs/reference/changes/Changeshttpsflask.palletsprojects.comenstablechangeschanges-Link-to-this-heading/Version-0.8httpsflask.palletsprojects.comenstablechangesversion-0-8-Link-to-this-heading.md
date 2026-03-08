## Version 0.8[¶](https://flask.palletsprojects.com/en/stable/changes/#version-0-8 "Link to this heading")
Released 2011-09-29, codename Rakija
  * Refactored session support into a session interface so that the implementation of the sessions can be changed without having to override the Flask class.
  * Empty session cookies are now deleted properly automatically.
  * View functions can now opt out of getting the automatic OPTIONS implementation.
  * HTTP exceptions and Bad Request errors can now be trapped so that they show up normally in the traceback.
  * Flask in debug mode is now detecting some common problems and tries to warn you about them.
  * Flask in debug mode will now complain with an assertion error if a view was attached after the first request was handled. This gives earlier feedback when users forget to import view code ahead of time.
  * Added the ability to register callbacks that are only triggered once at the beginning of the first request with `Flask.before_first_request`.
  * Malformed JSON data will now trigger a bad request HTTP exception instead of a value error which usually would result in a 500 internal server error if not handled. This is a backwards incompatible change.
  * Applications now not only have a root path where the resources and modules are located but also an instance path which is the designated place to drop files that are modified at runtime (uploads etc.). Also this is conceptually only instance depending and outside version control so it’s the perfect place to put configuration files etc.
  * Added the `APPLICATION_ROOT` configuration variable.
  * Implemented `TestClient.session_transaction` to easily modify sessions from the test environment.
  * Refactored test client internally. The `APPLICATION_ROOT` configuration variable as well as `SERVER_NAME` are now properly used by the test client as defaults.
  * Added `View.decorators` to support simpler decorating of pluggable (class-based) views.
  * Fixed an issue where the test client if used with the “with” statement did not trigger the execution of the teardown handlers.
  * Added finer control over the session cookie parameters.
  * HEAD requests to a method view now automatically dispatch to the `get` method if no handler was implemented.
  * Implemented the virtual `flask.ext` package to import extensions from.
  * The context preservation on exceptions is now an integral component of Flask itself and no longer of the test client. This cleaned up some internal logic and lowers the odds of runaway request contexts in unittests.
  * Fixed the Jinja environment’s `list_templates` method not returning the correct names when blueprints or modules were involved.
