
**func** (_[__[__...__]__,__]_)

Return type:


async_to_sync(_func_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.async_to_sync "Link to this definition")

Return a sync function that will run the coroutine function.
```
result = app.async_to_sync(func)(*args, **kwargs)

```

Override this method to change how the app converts async code to be synchronously callable.
Changelog
Added in version 2.0.

Parameters:

**func** (_[__[__...__]__,__[__,__,__]__]_)

Return type:


url_for(_endpoint_ , _*_ , __anchor =None_, __method =None_, __scheme =None_, __external =None_, _** values_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.url_for "Link to this definition")

Generate a URL to the given endpoint with the given values.
This is called by [`flask.url_for()`](https://flask.palletsprojects.com/en/stable/api/#flask.url_for "flask.url_for"), and can be called directly as well.
An _endpoint_ is the name of a URL rule, usually added with [`@app.route()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.route "flask.Flask.route"), and usually the same name as the view function. A route defined in a [`Blueprint`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint "flask.Blueprint") will prepend the blueprint’s name separated by a `.` to the endpoint.
In some cases, such as email messages, you want URLs to include the scheme and domain, like `https://example.com/hello`. When not in an active request, URLs will be external by default, but this requires setting [`SERVER_NAME`](https://flask.palletsprojects.com/en/stable/config/#SERVER_NAME "SERVER_NAME") so Flask knows what domain to use. [`APPLICATION_ROOT`](https://flask.palletsprojects.com/en/stable/config/#APPLICATION_ROOT "APPLICATION_ROOT") and [`PREFERRED_URL_SCHEME`](https://flask.palletsprojects.com/en/stable/config/#PREFERRED_URL_SCHEME "PREFERRED_URL_SCHEME") should also be configured as needed. This config is only used when not in an active request.
Functions can be decorated with [`url_defaults()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.url_defaults "flask.Flask.url_defaults") to modify keyword arguments before the URL is built.
If building fails for some reason, such as an unknown endpoint or incorrect values, the app’s [`handle_url_build_error()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.handle_url_build_error "flask.Flask.handle_url_build_error") method is called. If that returns a string, that is returned, otherwise a `BuildError` is raised.

Parameters:

  * **endpoint** (`.`, the current blueprint name (if any) will be used.
  * **_anchor** (_|__None_) – If given, append this as `#anchor` to the URL.
  * **_method** (_|__None_) – If given, generate the URL associated with this method for the endpoint.
  * **_scheme** (_|__None_) – If given, the URL will have this scheme if it is external.
  * **_external** (_|__None_) – If given, prefer the URL to be internal (False) or require it to be external (True). External URLs include the scheme and domain. When not in an active request, URLs are external by default.
  * **values** (`?a=b&c=d`.



Return type:
Changelog
Added in version 2.2: Moved from `flask.url_for`, which calls this method.

make_response(_rv_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.make_response "Link to this definition")

Convert the return value from a view function to an instance of [`response_class`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.response_class "flask.Flask.response_class").

Parameters:

**rv** (_ft.ResponseReturnValue_) –
the return value from the view function. The view function must return a response. Returning `None`, or the view ending without returning, is not allowed. The following types are allowed for `view_rv`:

`str`

A response object is created with the string encoded to UTF-8 as the body.

`bytes`

A response object is created with the bytes as the body.

`dict`

A dictionary that will be jsonify’d before being returned.

`list`

A list that will be jsonify’d before being returned.

`generator` or `iterator`

A generator that returns `str` or `bytes` to be streamed as the response.

`tuple`

Either `(body, status, headers)`, `(body, status)`, or `(body, headers)`, where `body` is any of the other types allowed here, `status` is a string or an integer, and `headers` is a dictionary or a list of `(key, value)` tuples. If `body` is a [`response_class`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.response_class "flask.Flask.response_class") instance, `status` overwrites the exiting value and `headers` are extended.

[`response_class`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.response_class "flask.Flask.response_class")

The object is returned unchanged.

other [`Response`](https://werkzeug.palletsprojects.com/en/stable/wrappers/#werkzeug.wrappers.Response "\(in Werkzeug v3.1.x\)") class

The object is coerced to [`response_class`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.response_class "flask.Flask.response_class").
The function is called as a WSGI application. The result is used to create a response object.

Return type:

[Response](https://flask.palletsprojects.com/en/stable/api/#flask.Response "flask.Response") Changelog
Changed in version 2.2: A generator will be converted to a streaming response. A list will be converted to a JSON response.
Changed in version 1.1: A dict will be converted to a JSON response.
Changed in version 0.9: Previously a tuple was interpreted as the arguments for the response object.

preprocess_request()[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.preprocess_request "Link to this definition")

Called before the request is dispatched. Calls [`url_value_preprocessors`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.url_value_preprocessors "flask.Flask.url_value_preprocessors") registered with the app and the current blueprint (if any). Then calls [`before_request_funcs`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.before_request_funcs "flask.Flask.before_request_funcs") registered with the app and the blueprint.
If any [`before_request()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.before_request "flask.Flask.before_request") handler returns a non-None value, the value is handled as if it was the return value from the view, and further request handling is stopped.

Return type:

ft.ResponseReturnValue | None

process_response(_response_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.process_response "Link to this definition")

Can be overridden in order to modify the response object before it’s sent to the WSGI server. By default this will call all the [`after_request()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.after_request "flask.Flask.after_request") decorated functions.
Changelog
Changed in version 0.5: As of Flask 0.5 the functions registered for after request execution are called in reverse order of registration.

Parameters:

**response** ([_Response_](https://flask.palletsprojects.com/en/stable/api/#flask.Response "flask.wrappers.Response")) – a [`response_class`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.response_class "flask.Flask.response_class") object.

Returns:

a new response object or the same, has to be an instance of [`response_class`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.response_class "flask.Flask.response_class").

Return type:

[_Response_](https://flask.palletsprojects.com/en/stable/api/#flask.Response "flask.wrappers.Response")

do_teardown_request(_exc =_sentinel_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.do_teardown_request "Link to this definition")

Called after the request is dispatched and the response is returned, right before the request context is popped.
This calls all functions decorated with [`teardown_request()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.teardown_request "flask.Flask.teardown_request"), and [`Blueprint.teardown_request()`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.teardown_request "flask.Blueprint.teardown_request") if a blueprint handled the request. Finally, the [`request_tearing_down`](https://flask.palletsprojects.com/en/stable/api/#flask.request_tearing_down "flask.request_tearing_down") signal is sent.
This is called by [`RequestContext.pop()`](https://flask.palletsprojects.com/en/stable/api/#flask.ctx.RequestContext.pop "flask.ctx.RequestContext.pop"), which may be delayed during testing to maintain access to resources.

Parameters:

**exc** (_|__None_) – An unhandled exception raised while dispatching the request. Detected from the current exception information if not passed. Passed to each teardown function.

Return type:

None Changelog
Changed in version 0.9: Added the `exc` argument.

do_teardown_appcontext(_exc =_sentinel_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.do_teardown_appcontext "Link to this definition")

Called right before the application context is popped.
When handling a request, the application context is popped after the request context. See [`do_teardown_request()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.do_teardown_request "flask.Flask.do_teardown_request").
This calls all functions decorated with [`teardown_appcontext()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.teardown_appcontext "flask.Flask.teardown_appcontext"). Then the [`appcontext_tearing_down`](https://flask.palletsprojects.com/en/stable/api/#flask.appcontext_tearing_down "flask.appcontext_tearing_down") signal is sent.
This is called by [`AppContext.pop()`](https://flask.palletsprojects.com/en/stable/api/#flask.ctx.AppContext.pop "flask.ctx.AppContext.pop").
Changelog
Added in version 0.9.

Parameters:

**exc** (_|__None_)

Return type:

None

app_context()[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.app_context "Link to this definition")

Create an [`AppContext`](https://flask.palletsprojects.com/en/stable/api/#flask.ctx.AppContext "flask.ctx.AppContext"). Use as a `with` block to push the context, which will make [`current_app`](https://flask.palletsprojects.com/en/stable/api/#flask.current_app "flask.current_app") point at this application.
An application context is automatically pushed by `RequestContext.push()` when handling a request, and when running a CLI command. Use this to manually create a context outside of these situations.
```
with app.app_context():
    init_db()

```

See [The Application Context](https://flask.palletsprojects.com/en/stable/appcontext/).
Changelog
Added in version 0.9.

Return type:

[_AppContext_](https://flask.palletsprojects.com/en/stable/api/#flask.ctx.AppContext "flask.ctx.AppContext")

request_context(_environ_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.request_context "Link to this definition")

Create a [`RequestContext`](https://flask.palletsprojects.com/en/stable/api/#flask.ctx.RequestContext "flask.ctx.RequestContext") representing a WSGI environment. Use a `with` block to push the context, which will make [`request`](https://flask.palletsprojects.com/en/stable/api/#flask.request "flask.request") point at this request.
See [The Request Context](https://flask.palletsprojects.com/en/stable/reqcontext/).
Typically you should not call this from your own code. A request context is automatically pushed by the [`wsgi_app()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.wsgi_app "flask.Flask.wsgi_app") when handling a request. Use [`test_request_context()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.test_request_context "flask.Flask.test_request_context") to create an environment and context instead of this method.

Parameters:

**environ** (_WSGIEnvironment_) – a WSGI environment

Return type:

[RequestContext](https://flask.palletsprojects.com/en/stable/api/#flask.ctx.RequestContext "flask.ctx.RequestContext")

test_request_context(_* args_, _** kwargs_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.test_request_context "Link to this definition")

Create a [`RequestContext`](https://flask.palletsprojects.com/en/stable/api/#flask.ctx.RequestContext "flask.ctx.RequestContext") for a WSGI environment created from the given values. This is mostly useful during testing, where you may want to run a function that uses request data without dispatching a full request.
See [The Request Context](https://flask.palletsprojects.com/en/stable/reqcontext/).
Use a `with` block to push the context, which will make [`request`](https://flask.palletsprojects.com/en/stable/api/#flask.request "flask.request") point at the request for the created environment.
```
with app.test_request_context(...):
    generate_report()

```

When using the shell, it may be easier to push and pop the context manually to avoid indentation.
```
ctx = app.test_request_context(...)
ctx.push()
...
ctx.pop()

```

Takes the same arguments as Werkzeug’s [`EnvironBuilder`](https://werkzeug.palletsprojects.com/en/stable/test/#werkzeug.test.EnvironBuilder "\(in Werkzeug v3.1.x\)"), with some defaults from the application. See the linked Werkzeug docs for most of the available arguments. Flask-specific behavior is listed here.

Parameters:

  * **path** – URL path being requested.
  * **base_url** – Base URL where the app is being served, which `path` is relative to. If not given, built from [`PREFERRED_URL_SCHEME`](https://flask.palletsprojects.com/en/stable/config/#PREFERRED_URL_SCHEME "PREFERRED_URL_SCHEME"), `subdomain`, [`SERVER_NAME`](https://flask.palletsprojects.com/en/stable/config/#SERVER_NAME "SERVER_NAME"), and [`APPLICATION_ROOT`](https://flask.palletsprojects.com/en/stable/config/#APPLICATION_ROOT "APPLICATION_ROOT").
  * **subdomain** – Subdomain name to append to [`SERVER_NAME`](https://flask.palletsprojects.com/en/stable/config/#SERVER_NAME "SERVER_NAME").
  * **url_scheme** – Scheme to use instead of [`PREFERRED_URL_SCHEME`](https://flask.palletsprojects.com/en/stable/config/#PREFERRED_URL_SCHEME "PREFERRED_URL_SCHEME").
  * **data** – The request body, either as a string or a dict of form keys and values.
  * **json** – If given, this is serialized as JSON and passed as `data`. Also defaults `content_type` to `application/json`.
  * **args** ([`EnvironBuilder`](https://werkzeug.palletsprojects.com/en/stable/test/#werkzeug.test.EnvironBuilder "\(in Werkzeug v3.1.x\)").
  * **kwargs** ([`EnvironBuilder`](https://werkzeug.palletsprojects.com/en/stable/test/#werkzeug.test.EnvironBuilder "\(in Werkzeug v3.1.x\)").



Return type:

[_RequestContext_](https://flask.palletsprojects.com/en/stable/api/#flask.ctx.RequestContext "flask.ctx.RequestContext")

wsgi_app(_environ_ , _start_response_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.wsgi_app "Link to this definition")

The actual WSGI application. This is not implemented in `__call__()` so that middlewares can be applied without losing a reference to the app object. Instead of doing this:
```
app = MyMiddleware(app)

```

It’s a better idea to do this instead:
```
app.wsgi_app = MyMiddleware(app.wsgi_app)

```

Then you still have the original application object around and can continue to call methods on it.
Changelog
Changed in version 0.7: Teardown events for the request and app contexts are called even if an unhandled error occurs. Other events may not be called depending on when an error occurs during dispatch. See [Callbacks and Errors](https://flask.palletsprojects.com/en/stable/reqcontext/#callbacks-and-errors).

Parameters:

  * **environ** (_WSGIEnvironment_) – A WSGI environment.
  * **start_response** (_StartResponse_) – A callable accepting a status code, a list of headers, and an optional exception context to start the response.



Return type:

cabc.Iterable[

aborter_class[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.aborter_class "Link to this definition")

alias of [`Aborter`](https://werkzeug.palletsprojects.com/en/stable/exceptions/#werkzeug.exceptions.Aborter "\(in Werkzeug v3.1.x\)")

add_template_filter(_f_ , _name =None_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.add_template_filter "Link to this definition")

Register a custom template filter. Works exactly like the [`template_filter()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.template_filter "flask.Flask.template_filter") decorator.

Parameters:

  * **name** (_|__None_) – the optional name of the filter, otherwise the function name will be used.
  * **f** (_[__[__...__]__,__]_)



Return type:

None

add_template_global(_f_ , _name =None_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.add_template_global "Link to this definition")

Register a custom template global function. Works exactly like the [`template_global()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.template_global "flask.Flask.template_global") decorator.
Changelog
Added in version 0.10.

Parameters:

  * **name** (_|__None_) – the optional name of the global function, otherwise the function name will be used.
  * **f** (_[__[__...__]__,__]_)



Return type:

None

add_template_test(_f_ , _name =None_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.add_template_test "Link to this definition")

Register a custom template test. Works exactly like the [`template_test()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.template_test "flask.Flask.template_test") decorator.
Changelog
Added in version 0.10.

Parameters:

  * **name** (_|__None_) – the optional name of the test, otherwise the function name will be used.
  * **f** (_[__[__...__]__,__]_)



Return type:

None

add_url_rule(_rule_ , _endpoint =None_, _view_func =None_, _provide_automatic_options =None_, _** options_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.add_url_rule "Link to this definition")

Register a rule for routing incoming requests and building URLs. The [`route()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.route "flask.Flask.route") decorator is a shortcut to call this with the `view_func` argument. These are equivalent:
```
@app.route("/")
def index():
    ...

```

```
def index():
    ...

app.add_url_rule("/", view_func=index)

```

See [URL Route Registrations](https://flask.palletsprojects.com/en/stable/api/#url-route-registrations).
The endpoint name for the route defaults to the name of the view function if the `endpoint` parameter isn’t passed. An error will be raised if a function has already been registered for the endpoint.
The `methods` parameter defaults to `["GET"]`. `HEAD` is always added automatically, and `OPTIONS` is added automatically by default.
`view_func` does not necessarily need to be passed, but if the rule should participate in routing an endpoint name must be associated with a view function at some point with the [`endpoint()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.endpoint "flask.Flask.endpoint") decorator.
```
app.add_url_rule("/", endpoint="index")

@app.endpoint("index")
def index():
    ...

```

If `view_func` has a `required_methods` attribute, those methods are added to the passed and automatic methods. If it has a `provide_automatic_methods` attribute, it is used as the default if the parameter is not passed.

Parameters:

  * **rule** (
  * **endpoint** (_|__None_) – The endpoint name to associate with the rule and view function. Used when routing and building URLs. Defaults to `view_func.__name__`.
  * **view_func** (_ft.RouteCallable_ _|__None_) – The view function to associate with the endpoint name.
  * **provide_automatic_options** (_|__None_) – Add the `OPTIONS` method and respond to `OPTIONS` requests automatically.
  * **options** (_t.Any_) – Extra options passed to the [`Rule`](https://werkzeug.palletsprojects.com/en/stable/routing/#werkzeug.routing.Rule "\(in Werkzeug v3.1.x\)") object.



Return type:

None

after_request(_f_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.after_request "Link to this definition")

Register a function to run after each request to this object.
The function is called with the response object, and must return a response object. This allows the functions to modify or replace the response before it is sent.
If a function raises an exception, any remaining `after_request` functions will not be called. Therefore, this should not be used for actions that must execute, such as to close resources. Use [`teardown_request()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.teardown_request "flask.Flask.teardown_request") for that.
This is available on both app and blueprint objects. When used on an app, this executes after every request. When used on a blueprint, this executes after every request that the blueprint handles. To register with a blueprint and execute after every request, use [`Blueprint.after_app_request()`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.after_app_request "flask.Blueprint.after_app_request").

Parameters:

**f** (_T_after_request_)

Return type:

_T_after_request_

app_ctx_globals_class[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.app_ctx_globals_class "Link to this definition")

alias of [`_AppCtxGlobals`](https://flask.palletsprojects.com/en/stable/api/#flask.ctx._AppCtxGlobals "flask.ctx._AppCtxGlobals")

auto_find_instance_path()[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.auto_find_instance_path "Link to this definition")

Tries to locate the instance path if it was not provided to the constructor of the application class. It will basically calculate the path to a folder named `instance` next to your main file or the package.
Changelog
Added in version 0.8.

Return type:


before_request(_f_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.before_request "Link to this definition")

Register a function to run before each request.
For example, this can be used to open a database connection, or to load the logged in user from the session.
```
@app.before_request
def load_user():
    if "user_id" in session:
        g.user = db.session.get(session["user_id"])

```

The function will be called without any arguments. If it returns a non-`None` value, the value is handled as if it was the return value from the view, and further request handling is stopped.
This is available on both app and blueprint objects. When used on an app, this executes before every request. When used on a blueprint, this executes before every request that the blueprint handles. To register with a blueprint and execute before every request, use [`Blueprint.before_app_request()`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.before_app_request "flask.Blueprint.before_app_request").

Parameters:

**f** (_T_before_request_)

Return type:

_T_before_request_

config_class[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.config_class "Link to this definition")

alias of [`Config`](https://flask.palletsprojects.com/en/stable/api/#flask.Config "flask.config.Config")

context_processor(_f_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.context_processor "Link to this definition")

Registers a template context processor function. These functions run before rendering a template. The keys of the returned dict are added as variables available in the template.
This is available on both app and blueprint objects. When used on an app, this is called for every rendered template. When used on a blueprint, this is called for templates rendered from the blueprint’s views. To register with a blueprint and affect every template, use [`Blueprint.app_context_processor()`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.app_context_processor "flask.Blueprint.app_context_processor").

Parameters:

**f** (_T_template_context_processor_)

Return type:

_T_template_context_processor_

create_global_jinja_loader()[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.create_global_jinja_loader "Link to this definition")

Creates the loader for the Jinja environment. Can be used to override just the loader and keeping the rest unchanged. It’s discouraged to override this function. Instead one should override the [`jinja_loader()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.jinja_loader "flask.Flask.jinja_loader") function instead.
The global loader dispatches between the loaders of the application and the individual blueprints.
Changelog
Added in version 0.7.

Return type:

_DispatchingJinjaLoader_

_property_ debug _:_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.debug "Link to this definition")

Whether debug mode is enabled. When using `flask run` to start the development server, an interactive debugger will be shown for unhandled exceptions, and the server will be reloaded when code changes. This maps to the [`DEBUG`](https://flask.palletsprojects.com/en/stable/config/#DEBUG "DEBUG") config key. It may not behave as expected if set late.
