## Application Globals[¶](https://flask.palletsprojects.com/en/stable/api/#application-globals "Link to this heading")
To share data that is valid for one request only from one function to another, a global variable is not good enough because it would break in threaded environments. Flask provides you with a special object that ensures it is only valid for the active request and that will return different values for each request. In a nutshell: it does the right thing, like it does for [`request`](https://flask.palletsprojects.com/en/stable/api/#flask.request "flask.request") and [`session`](https://flask.palletsprojects.com/en/stable/api/#flask.session "flask.session").

flask.g[¶](https://flask.palletsprojects.com/en/stable/api/#flask.g "Link to this definition")

A namespace object that can store data during an [application context](https://flask.palletsprojects.com/en/stable/appcontext/). This is an instance of [`Flask.app_ctx_globals_class`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.app_ctx_globals_class "flask.Flask.app_ctx_globals_class"), which defaults to [`ctx._AppCtxGlobals`](https://flask.palletsprojects.com/en/stable/api/#flask.ctx._AppCtxGlobals "flask.ctx._AppCtxGlobals").
This is a good place to store resources during a request. For example, a `before_request` function could load a user object from a session id, then set `g.user` to be used in the view function.
This is a proxy. See [Notes On Proxies](https://flask.palletsprojects.com/en/stable/reqcontext/#notes-on-proxies) for more information.
Changelog
Changed in version 0.10: Bound to the application context instead of the request context.

_class_ flask.ctx._AppCtxGlobals[¶](https://flask.palletsprojects.com/en/stable/api/#flask.ctx._AppCtxGlobals "Link to this definition")

A plain object. Used as a namespace for storing data during an application context.
Creating an app context automatically creates this object, which is made available as the `g` proxy.

'key' in g

Check whether an attribute is present.
Changelog
Added in version 0.10.

iter(g)

Return an iterator over the attribute names.
Changelog
Added in version 0.10.

get(_name_ , _default =None_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.ctx._AppCtxGlobals.get "Link to this definition")

Get an attribute by name, or a default value. Like

Parameters:

  * **name** (
  * **default** (_|__None_) – Value to return if the attribute is not present.



Return type:
Changelog
Added in version 0.10.

pop(_name_ , _default =_sentinel_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.ctx._AppCtxGlobals.pop "Link to this definition")

Get and remove an attribute by name. Like

Parameters:

  * **name** (
  * **default** (`KeyError`.



Return type:
Changelog
Added in version 0.11.

setdefault(_name_ , _default =None_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.ctx._AppCtxGlobals.setdefault "Link to this definition")

Get the value of an attribute if it is present, otherwise set and return a default value. Like

Parameters:

  * **name** (
  * **default** (



Return type:
Changelog
Added in version 0.11.
