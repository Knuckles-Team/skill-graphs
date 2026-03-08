## Version 0.10[¶](https://flask.palletsprojects.com/en/stable/changes/#version-0-10 "Link to this heading")
Released 2013-06-13, codename Limoncello
  * Changed default cookie serialization format from pickle to JSON to limit the impact an attacker can do if the secret key leaks.
  * Added `template_test` methods in addition to the already existing `template_filter` method family.
  * Added `template_global` methods in addition to the already existing `template_filter` method family.
  * Set the content-length header for x-sendfile.
  * `tojson` filter now does not escape script blocks in HTML5 parsers.
  * `tojson` used in templates is now safe by default. This was allowed due to the different escaping behavior.
  * Flask will now raise an error if you attempt to register a new function on an already used endpoint.
  * Added wrapper module around simplejson and added default serialization of datetime objects. This allows much easier customization of how JSON is handled by Flask or any Flask extension.
  * Removed deprecated internal `flask.session` module alias. Use `flask.sessions` instead to get the session module. This is not to be confused with `flask.session` the session proxy.
  * Templates can now be rendered without request context. The behavior is slightly different as the `request`, `session` and `g` objects will not be available and blueprint’s context processors are not called.
  * The config object is now available to the template as a real global and not through a context processor which makes it available even in imported templates by default.
  * Added an option to generate non-ascii encoded JSON which should result in less bytes being transmitted over the network. It’s disabled by default to not cause confusion with existing libraries that might expect `flask.json.dumps` to return bytes by default.
  * `flask.g` is now stored on the app context instead of the request context.
  * `flask.g` now gained a `get()` method for not erroring out on non existing items.
  * `flask.g` now can be used with the `in` operator to see what’s defined and it now is iterable and will yield all attributes stored.
  * `flask.Flask.request_globals_class` got renamed to `flask.Flask.app_ctx_globals_class` which is a better name to what it does since 0.10.
  * `request`, `session` and `g` are now also added as proxies to the template context which makes them available in imported templates. One has to be very careful with those though because usage outside of macros might cause caching.
  * Flask will no longer invoke the wrong error handlers if a proxy exception is passed through.
  * Added a workaround for chrome’s cookies in localhost not working as intended with domain names.
  * Changed logic for picking defaults for cookie values from sessions to work better with Google Chrome.
  * Added `message_flashed` signal that simplifies flashing testing.
  * Added support for copying of request contexts for better working with greenlets.
  * Removed custom JSON HTTP exception subclasses. If you were relying on them you can reintroduce them again yourself trivially. Using them however is strongly discouraged as the interface was flawed.
  * Python requirements changed: requiring Python 2.6 or 2.7 now to prepare for Python 3.3 port.
  * Changed how the teardown system is informed about exceptions. This is now more reliable in case something handles an exception halfway through the error handling process.
  * Request context preservation in debug mode now keeps the exception information around which means that teardown handlers are able to distinguish error from success cases.
  * Added the `JSONIFY_PRETTYPRINT_REGULAR` configuration variable.
  * Flask now orders JSON keys by default to not trash HTTP caches due to different hash seeds between different workers.
  * Added `appcontext_pushed` and `appcontext_popped` signals.
  * The builtin run method now takes the `SERVER_NAME` into account when picking the default port to run on.
  * Added `flask.request.get_json()` as a replacement for the old `flask.request.json` property.
