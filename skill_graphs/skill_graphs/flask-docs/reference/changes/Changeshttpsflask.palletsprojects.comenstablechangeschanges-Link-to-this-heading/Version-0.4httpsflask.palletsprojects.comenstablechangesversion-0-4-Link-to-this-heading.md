## Version 0.4[¶](https://flask.palletsprojects.com/en/stable/changes/#version-0-4 "Link to this heading")
Released 2010-06-18, codename Rakia
  * Added the ability to register application wide error handlers from modules.
  * `Flask.after_request` handlers are now also invoked if the request dies with an exception and an error handling page kicks in.
  * Test client has not the ability to preserve the request context for a little longer. This can also be used to trigger custom requests that do not pop the request stack for testing.
  * Because the Python standard library caches loggers, the name of the logger is configurable now to better support unittests.
  * Added `TESTING` switch that can activate unittesting helpers.
  * The logger switches to `DEBUG` mode now if debug is enabled.
