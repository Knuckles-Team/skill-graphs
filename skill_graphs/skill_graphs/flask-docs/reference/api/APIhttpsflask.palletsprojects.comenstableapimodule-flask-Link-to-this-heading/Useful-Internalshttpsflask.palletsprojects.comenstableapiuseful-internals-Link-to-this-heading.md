## Useful Internals[¶](https://flask.palletsprojects.com/en/stable/api/#useful-internals "Link to this heading")

_class_ flask.ctx.RequestContext(_app_ , _environ_ , _request =None_, _session =None_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.ctx.RequestContext "Link to this definition")

The request context contains per-request information. The Flask app creates and pushes it at the beginning of the request, then pops it at the end of the request. It will create the URL adapter and request object for the WSGI environment provided.
Do not attempt to use this class directly, instead use [`test_request_context()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.test_request_context "flask.Flask.test_request_context") and [`request_context()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.request_context "flask.Flask.request_context") to create this object.
When the request context is popped, it will evaluate all the functions registered on the application for teardown execution ([`teardown_request()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.teardown_request "flask.Flask.teardown_request")).
The request context is automatically popped at the end of the request. When using the interactive debugger, the context will be restored so `request` is still accessible. Similarly, the test client can preserve the context after the request ends. However, teardown functions may already have closed some resources such as database connections.

Parameters:

  * **app** ([_Flask_](https://flask.palletsprojects.com/en/stable/api/#flask.Flask "flask.Flask"))
  * **environ** (_WSGIEnvironment_)
  * **request** ([_Request_](https://flask.palletsprojects.com/en/stable/api/#flask.Request "flask.Request") _|__None_)
  * **session** ([_SessionMixin_](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SessionMixin "flask.sessions.SessionMixin") _|__None_)



copy()[¶](https://flask.palletsprojects.com/en/stable/api/#flask.ctx.RequestContext.copy "Link to this definition")

Creates a copy of this request context with the same request object. This can be used to move a request context to a different greenlet. Because the actual request object is the same this cannot be used to move a request context to a different thread unless access to the request object is locked.
Changelog
Changed in version 1.1: The current session object is used instead of reloading the original data. This prevents `flask.session` pointing to an out-of-date object.
Added in version 0.10.

Return type:

[_RequestContext_](https://flask.palletsprojects.com/en/stable/api/#flask.ctx.RequestContext "flask.ctx.RequestContext")

match_request()[¶](https://flask.palletsprojects.com/en/stable/api/#flask.ctx.RequestContext.match_request "Link to this definition")

Can be overridden by a subclass to hook into the matching of the request.

Return type:

None

_property_ session _:[ SessionMixin](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SessionMixin "flask.sessions.SessionMixin")_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.ctx.RequestContext.session "Link to this definition")

The session data associated with this request. Not available until this context has been pushed. Accessing this property, also accessed by the [`session`](https://flask.palletsprojects.com/en/stable/api/#flask.session "flask.session") proxy, sets [`SessionMixin.accessed`](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SessionMixin.accessed "flask.sessions.SessionMixin.accessed").

pop(_exc =_sentinel_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.ctx.RequestContext.pop "Link to this definition")

Pops the request context and unbinds it by doing that. This will also trigger the execution of functions registered by the [`teardown_request()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.teardown_request "flask.Flask.teardown_request") decorator.
Changelog
Changed in version 0.9: Added the `exc` argument.

Parameters:

**exc** (_|__None_)

Return type:

None

flask.globals.request_ctx[¶](https://flask.palletsprojects.com/en/stable/api/#flask.flask.globals.request_ctx "Link to this definition")

The current [`RequestContext`](https://flask.palletsprojects.com/en/stable/api/#flask.ctx.RequestContext "flask.ctx.RequestContext"). If a request context is not active, accessing attributes on this proxy will raise a `RuntimeError`.
This is an internal object that is essential to how Flask handles requests. Accessing this should not be needed in most cases. Most likely you want [`request`](https://flask.palletsprojects.com/en/stable/api/#flask.request "flask.request") and [`session`](https://flask.palletsprojects.com/en/stable/api/#flask.session "flask.session") instead.

_class_ flask.ctx.AppContext(_app_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.ctx.AppContext "Link to this definition")

The app context contains application-specific information. An app context is created and pushed at the beginning of each request if one is not already active. An app context is also pushed when running CLI commands.

Parameters:

**app** ([_Flask_](https://flask.palletsprojects.com/en/stable/api/#flask.Flask "flask.Flask"))

push()[¶](https://flask.palletsprojects.com/en/stable/api/#flask.ctx.AppContext.push "Link to this definition")

Binds the app context to the current context.

Return type:

None

pop(_exc =_sentinel_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.ctx.AppContext.pop "Link to this definition")

Pops the app context.

Parameters:

**exc** (_|__None_)

Return type:

None

flask.globals.app_ctx[¶](https://flask.palletsprojects.com/en/stable/api/#flask.flask.globals.app_ctx "Link to this definition")

The current [`AppContext`](https://flask.palletsprojects.com/en/stable/api/#flask.ctx.AppContext "flask.ctx.AppContext"). If an app context is not active, accessing attributes on this proxy will raise a `RuntimeError`.
This is an internal object that is essential to how Flask handles requests. Accessing this should not be needed in most cases. Most likely you want [`current_app`](https://flask.palletsprojects.com/en/stable/api/#flask.current_app "flask.current_app") and [`g`](https://flask.palletsprojects.com/en/stable/api/#flask.g "flask.g") instead.

_class_ flask.blueprints.BlueprintSetupState(_blueprint_ , _app_ , _options_ , _first_registration_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.blueprints.BlueprintSetupState "Link to this definition")

Temporary holder object for registering a blueprint with the application. An instance of this class is created by the [`make_setup_state()`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.make_setup_state "flask.Blueprint.make_setup_state") method and later passed to all register callback functions.

Parameters:

  * **blueprint** ([_Blueprint_](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint "flask.blueprints.Blueprint"))
  * **app** (_App_)
  * **options** (_t.Any_)
  * **first_registration** (



app[¶](https://flask.palletsprojects.com/en/stable/api/#flask.blueprints.BlueprintSetupState.app "Link to this definition")

a reference to the current application

blueprint[¶](https://flask.palletsprojects.com/en/stable/api/#flask.blueprints.BlueprintSetupState.blueprint "Link to this definition")

a reference to the blueprint that created this setup state.

options[¶](https://flask.palletsprojects.com/en/stable/api/#flask.blueprints.BlueprintSetupState.options "Link to this definition")

a dictionary with all options that were passed to the [`register_blueprint()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.register_blueprint "flask.Flask.register_blueprint") method.

first_registration[¶](https://flask.palletsprojects.com/en/stable/api/#flask.blueprints.BlueprintSetupState.first_registration "Link to this definition")

as blueprints can be registered multiple times with the application and not everything wants to be registered multiple times on it, this attribute can be used to figure out if the blueprint was registered in the past already.

subdomain[¶](https://flask.palletsprojects.com/en/stable/api/#flask.blueprints.BlueprintSetupState.subdomain "Link to this definition")

The subdomain that the blueprint should be active for, `None` otherwise.

url_prefix[¶](https://flask.palletsprojects.com/en/stable/api/#flask.blueprints.BlueprintSetupState.url_prefix "Link to this definition")

The prefix that should be used for all URLs defined on the blueprint.

url_defaults[¶](https://flask.palletsprojects.com/en/stable/api/#flask.blueprints.BlueprintSetupState.url_defaults "Link to this definition")

A dictionary with URL defaults that is added to each and every URL that was defined with the blueprint.

add_url_rule(_rule_ , _endpoint =None_, _view_func =None_, _** options_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.blueprints.BlueprintSetupState.add_url_rule "Link to this definition")

A helper method to register a rule (and optionally a view function) to the application. The endpoint is automatically prefixed with the blueprint’s name.

Parameters:

  * **rule** (
  * **endpoint** (_|__None_)
  * **view_func** (_ft.RouteCallable_ _|__None_)
  * **options** (_t.Any_)



Return type:

None
