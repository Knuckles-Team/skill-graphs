## Session Interface[¶](https://flask.palletsprojects.com/en/stable/api/#session-interface "Link to this heading")
Changelog
Added in version 0.8.
The session interface provides a simple way to replace the session implementation that Flask is using.

_class_ flask.sessions.SessionInterface[¶](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SessionInterface "Link to this definition")

The basic interface you have to implement in order to replace the default session interface which uses werkzeug’s securecookie implementation. The only methods you have to implement are [`open_session()`](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SessionInterface.open_session "flask.sessions.SessionInterface.open_session") and [`save_session()`](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SessionInterface.save_session "flask.sessions.SessionInterface.save_session"), the others have useful defaults which you don’t need to change.
The session object returned by the [`open_session()`](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SessionInterface.open_session "flask.sessions.SessionInterface.open_session") method has to provide a dictionary like interface plus the properties and methods from the [`SessionMixin`](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SessionMixin "flask.sessions.SessionMixin"). We recommend just subclassing a dict and adding that mixin:
```
class Session(dict, SessionMixin):
    pass

```

If [`open_session()`](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SessionInterface.open_session "flask.sessions.SessionInterface.open_session") returns `None` Flask will call into [`make_null_session()`](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SessionInterface.make_null_session "flask.sessions.SessionInterface.make_null_session") to create a session that acts as replacement if the session support cannot work because some requirement is not fulfilled. The default [`NullSession`](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.NullSession "flask.sessions.NullSession") class that is created will complain that the secret key was not set.
To replace the session interface on an application all you have to do is to assign [`flask.Flask.session_interface`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.session_interface "flask.Flask.session_interface"):
```
app = Flask(__name__)
app.session_interface = MySessionInterface()

```

Multiple requests with the same session may be sent and handled concurrently. When implementing a new session interface, consider whether reads or writes to the backing store must be synchronized. There is no guarantee on the order in which the session for each request is opened or saved, it will occur in the order that requests begin and end processing.
Changelog
Added in version 0.8.

null_session_class[¶](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SessionInterface.null_session_class "Link to this definition")

[`make_null_session()`](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SessionInterface.make_null_session "flask.sessions.SessionInterface.make_null_session") will look here for the class that should be created when a null session is requested. Likewise the [`is_null_session()`](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SessionInterface.is_null_session "flask.sessions.SessionInterface.is_null_session") method will perform a typecheck against this type.
alias of [`NullSession`](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.NullSession "flask.sessions.NullSession")

pickle_based _= False_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SessionInterface.pickle_based "Link to this definition")

A flag that indicates if the session interface is pickle based. This can be used by Flask extensions to make a decision in regards to how to deal with the session object.
Changelog
Added in version 0.10.

make_null_session(_app_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SessionInterface.make_null_session "Link to this definition")

Creates a null session which acts as a replacement object if the real session support could not be loaded due to a configuration error. This mainly aids the user experience because the job of the null session is to still support lookup without complaining but modifications are answered with a helpful error message of what failed.
This creates an instance of [`null_session_class`](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SessionInterface.null_session_class "flask.sessions.SessionInterface.null_session_class") by default.

Parameters:

**app** ([_Flask_](https://flask.palletsprojects.com/en/stable/api/#flask.Flask "flask.Flask"))

Return type:

[NullSession](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.NullSession "flask.sessions.NullSession")

is_null_session(_obj_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SessionInterface.is_null_session "Link to this definition")

Checks if a given object is a null session. Null sessions are not asked to be saved.
This checks if the object is an instance of [`null_session_class`](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SessionInterface.null_session_class "flask.sessions.SessionInterface.null_session_class") by default.

Parameters:

**obj** (

Return type:


get_cookie_name(_app_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SessionInterface.get_cookie_name "Link to this definition")

The name of the session cookie. Uses``app.config[“SESSION_COOKIE_NAME”]``.

Parameters:

**app** ([_Flask_](https://flask.palletsprojects.com/en/stable/api/#flask.Flask "flask.Flask"))

Return type:


get_cookie_domain(_app_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SessionInterface.get_cookie_domain "Link to this definition")

The value of the `Domain` parameter on the session cookie. If not set, browsers will only send the cookie to the exact domain it was set from. Otherwise, they will send it to any subdomain of the given value as well.
Uses the [`SESSION_COOKIE_DOMAIN`](https://flask.palletsprojects.com/en/stable/config/#SESSION_COOKIE_DOMAIN "SESSION_COOKIE_DOMAIN") config.
Changelog
Changed in version 2.3: Not set by default, does not fall back to `SERVER_NAME`.

Parameters:

**app** ([_Flask_](https://flask.palletsprojects.com/en/stable/api/#flask.Flask "flask.Flask"))

Return type:


get_cookie_path(_app_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SessionInterface.get_cookie_path "Link to this definition")

Returns the path for which the cookie should be valid. The default implementation uses the value from the `SESSION_COOKIE_PATH` config var if it’s set, and falls back to `APPLICATION_ROOT` or uses `/` if it’s `None`.

Parameters:

**app** ([_Flask_](https://flask.palletsprojects.com/en/stable/api/#flask.Flask "flask.Flask"))

Return type:


get_cookie_httponly(_app_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SessionInterface.get_cookie_httponly "Link to this definition")

Returns True if the session cookie should be httponly. This currently just returns the value of the `SESSION_COOKIE_HTTPONLY` config var.

Parameters:

**app** ([_Flask_](https://flask.palletsprojects.com/en/stable/api/#flask.Flask "flask.Flask"))

Return type:


get_cookie_secure(_app_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SessionInterface.get_cookie_secure "Link to this definition")

Returns True if the cookie should be secure. This currently just returns the value of the `SESSION_COOKIE_SECURE` setting.

Parameters:

**app** ([_Flask_](https://flask.palletsprojects.com/en/stable/api/#flask.Flask "flask.Flask"))

Return type:


get_cookie_samesite(_app_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SessionInterface.get_cookie_samesite "Link to this definition")

Return `'Strict'` or `'Lax'` if the cookie should use the `SameSite` attribute. This currently just returns the value of the [`SESSION_COOKIE_SAMESITE`](https://flask.palletsprojects.com/en/stable/config/#SESSION_COOKIE_SAMESITE "SESSION_COOKIE_SAMESITE") setting.

Parameters:

**app** ([_Flask_](https://flask.palletsprojects.com/en/stable/api/#flask.Flask "flask.Flask"))

Return type:


get_cookie_partitioned(_app_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SessionInterface.get_cookie_partitioned "Link to this definition")

Returns True if the cookie should be partitioned. By default, uses the value of [`SESSION_COOKIE_PARTITIONED`](https://flask.palletsprojects.com/en/stable/config/#SESSION_COOKIE_PARTITIONED "SESSION_COOKIE_PARTITIONED").
Added in version 3.1.

Parameters:

**app** ([_Flask_](https://flask.palletsprojects.com/en/stable/api/#flask.Flask "flask.Flask"))

Return type:


get_expiration_time(_app_ , _session_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SessionInterface.get_expiration_time "Link to this definition")

A helper method that returns an expiration date for the session or `None` if the session is linked to the browser session. The default implementation returns now + the permanent session lifetime configured on the application.

Parameters:

  * **app** ([_Flask_](https://flask.palletsprojects.com/en/stable/api/#flask.Flask "flask.Flask"))
  * **session** ([_SessionMixin_](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SessionMixin "flask.sessions.SessionMixin"))



Return type:

datetime | None

should_set_cookie(_app_ , _session_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SessionInterface.should_set_cookie "Link to this definition")

Used by session backends to determine if a `Set-Cookie` header should be set for this session cookie for this response. If the session has been modified, the cookie is set. If the session is permanent and the `SESSION_REFRESH_EACH_REQUEST` config is true, the cookie is always set.
This check is usually skipped if the session was deleted.
Changelog
Added in version 0.11.

Parameters:

  * **app** ([_Flask_](https://flask.palletsprojects.com/en/stable/api/#flask.Flask "flask.Flask"))
  * **session** ([_SessionMixin_](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SessionMixin "flask.sessions.SessionMixin"))



Return type:


open_session(_app_ , _request_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SessionInterface.open_session "Link to this definition")

This is called at the beginning of each request, after pushing the request context, before matching the URL.
This must return an object which implements a dictionary-like interface as well as the [`SessionMixin`](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SessionMixin "flask.sessions.SessionMixin") interface.
This will return `None` to indicate that loading failed in some way that is not immediately an error. The request context will fall back to using [`make_null_session()`](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SessionInterface.make_null_session "flask.sessions.SessionInterface.make_null_session") in this case.

Parameters:

  * **app** ([_Flask_](https://flask.palletsprojects.com/en/stable/api/#flask.Flask "flask.Flask"))
  * **request** ([_Request_](https://flask.palletsprojects.com/en/stable/api/#flask.Request "flask.Request"))



Return type:

[SessionMixin](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SessionMixin "flask.sessions.SessionMixin") | None

save_session(_app_ , _session_ , _response_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SessionInterface.save_session "Link to this definition")

This is called at the end of each request, after generating a response, before removing the request context. It is skipped if [`is_null_session()`](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SessionInterface.is_null_session "flask.sessions.SessionInterface.is_null_session") returns `True`.

Parameters:

  * **app** ([_Flask_](https://flask.palletsprojects.com/en/stable/api/#flask.Flask "flask.Flask"))
  * **session** ([_SessionMixin_](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SessionMixin "flask.sessions.SessionMixin"))
  * **response** ([_Response_](https://flask.palletsprojects.com/en/stable/api/#flask.Response "flask.Response"))



Return type:

None

_class_ flask.sessions.SecureCookieSessionInterface[¶](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SecureCookieSessionInterface "Link to this definition")

The default session interface that stores sessions in signed cookies through the `itsdangerous` module.

salt _= 'cookie-session'_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SecureCookieSessionInterface.salt "Link to this definition")

the salt that should be applied on top of the secret key for the signing of cookie based sessions.

_static_ digest_method(_string =b''_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SecureCookieSessionInterface.digest_method "Link to this definition")

the hash function to use for the signature. The default is sha1

Parameters:

**string** (

Return type:


key_derivation _= 'hmac'_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SecureCookieSessionInterface.key_derivation "Link to this definition")

the name of the itsdangerous supported key derivation. The default is hmac.

serializer _= <flask.json.tag.TaggedJSONSerializer object>_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SecureCookieSessionInterface.serializer "Link to this definition")

A python serializer for the payload. The default is a compact JSON derived serializer with support for some extra Python types such as datetime objects or tuples.

session_class[¶](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SecureCookieSessionInterface.session_class "Link to this definition")

alias of [`SecureCookieSession`](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SecureCookieSession "flask.sessions.SecureCookieSession")

open_session(_app_ , _request_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SecureCookieSessionInterface.open_session "Link to this definition")

This is called at the beginning of each request, after pushing the request context, before matching the URL.
This must return an object which implements a dictionary-like interface as well as the [`SessionMixin`](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SessionMixin "flask.sessions.SessionMixin") interface.
This will return `None` to indicate that loading failed in some way that is not immediately an error. The request context will fall back to using `make_null_session()` in this case.

Parameters:

  * **app** ([_Flask_](https://flask.palletsprojects.com/en/stable/api/#flask.Flask "flask.Flask"))
  * **request** ([_Request_](https://flask.palletsprojects.com/en/stable/api/#flask.Request "flask.Request"))



Return type:

[SecureCookieSession](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SecureCookieSession "flask.sessions.SecureCookieSession") | None

save_session(_app_ , _session_ , _response_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SecureCookieSessionInterface.save_session "Link to this definition")

This is called at the end of each request, after generating a response, before removing the request context. It is skipped if `is_null_session()` returns `True`.

Parameters:

  * **app** ([_Flask_](https://flask.palletsprojects.com/en/stable/api/#flask.Flask "flask.Flask"))
  * **session** ([_SessionMixin_](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SessionMixin "flask.sessions.SessionMixin"))
  * **response** ([_Response_](https://flask.palletsprojects.com/en/stable/api/#flask.Response "flask.Response"))



Return type:

None

_class_ flask.sessions.SecureCookieSession(_initial =None_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SecureCookieSession "Link to this definition")

Base class for sessions based on signed cookies.
This session backend will set the [`modified`](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SecureCookieSession.modified "flask.sessions.SecureCookieSession.modified") and `accessed` attributes. It cannot reliably track whether a session is new (vs. empty), so `new` remains hard coded to `False`.

Parameters:

**initial** (_c.Mapping_ _[__,__t.Any_ _]__|__None_)

modified _= False_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SecureCookieSession.modified "Link to this definition")

When data is changed, this is set to `True`. Only the session dictionary itself is tracked; if the session contains mutable data (for example a nested dict) then this must be set to `True` manually when modifying that data. The session cookie will only be written to the response if this is `True`.

_class_ flask.sessions.NullSession(_initial =None_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.NullSession "Link to this definition")

Class used to generate nicer error messages if sessions are not available. Will still allow read-only access to the empty session but fail on setting.

Parameters:

**initial** (_c.Mapping_ _[__,__t.Any_ _]__|__None_)

clear(_* args_, _** kwargs_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.NullSession.clear "Link to this definition")

Remove all items from the dict.

Parameters:

  * **args** (
  * **kwargs** (



Return type:


pop(_k_[, _d_]) → v, remove specified key and return the corresponding value.[¶](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.NullSession.pop "Link to this definition")

If the key is not found, return the default if given; otherwise, raise a KeyError.

Parameters:

  * **args** (
  * **kwargs** (



Return type:


popitem(_* args_, _** kwargs_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.NullSession.popitem "Link to this definition")

Remove and return a (key, value) pair as a 2-tuple.
Pairs are returned in LIFO (last-in, first-out) order. Raises KeyError if the dict is empty.

Parameters:

  * **args** (
  * **kwargs** (



Return type:


update([_E_ , ]_**F_) → None. Update D from mapping/iterable E and F.[¶](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.NullSession.update "Link to this definition")

If E is present and has a .keys() method, then does: for k in E.keys(): D[k] = E[k] If E is present and lacks a .keys() method, then does: for k, v in E: D[k] = v In either case, this is followed by: for k in F: D[k] = F[k]

Parameters:

  * **args** (
  * **kwargs** (



Return type:


setdefault(_* args_, _** kwargs_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.NullSession.setdefault "Link to this definition")

Insert key with a value of default if key is not in the dictionary.
Return the value for key if key is in the dictionary, else default.

Parameters:

  * **args** (
  * **kwargs** (



Return type:


_class_ flask.sessions.SessionMixin[¶](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SessionMixin "Link to this definition")

Expands a basic dictionary with session attributes.

_property_ permanent _:_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SessionMixin.permanent "Link to this definition")

This reflects the `'_permanent'` key in the dict.

modified _= True_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SessionMixin.modified "Link to this definition")

Some implementations can detect changes to the session and set this when that happens. The mixin default is hard coded to `True`.

accessed _= False_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SessionMixin.accessed "Link to this definition")

Indicates if the session was accessed, even if it was not modified. This is set when the session object is accessed through the request context, including the global `session` proxy. A `Vary: cookie` header will be added if this is `True`.
Changed in version 3.1.3: This is tracked by the request context.
Notice
The [`PERMANENT_SESSION_LIFETIME`](https://flask.palletsprojects.com/en/stable/config/#PERMANENT_SESSION_LIFETIME "PERMANENT_SESSION_LIFETIME") config can be an integer or `timedelta`. The [`permanent_session_lifetime`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.permanent_session_lifetime "flask.Flask.permanent_session_lifetime") attribute is always a `timedelta`.
