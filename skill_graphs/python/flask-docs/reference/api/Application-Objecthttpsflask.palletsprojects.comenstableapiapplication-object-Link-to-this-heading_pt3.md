**Do not enable debug mode when deploying in production.**
Default: `False`

delete(_rule_ , _** options_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.delete "Link to this definition")

Shortcut for [`route()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.route "flask.Flask.route") with `methods=["DELETE"]`.
Changelog
Added in version 2.0.

Parameters:

  * **rule** (
  * **options** (



Return type:

_T_route_], _T_route_]

endpoint(_endpoint_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.endpoint "Link to this definition")

Decorate a view function to register it for the given endpoint. Used if a rule is added without a `view_func` with [`add_url_rule()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.add_url_rule "flask.Flask.add_url_rule").
```
app.add_url_rule("/ex", endpoint="example")

@app.endpoint("example")
def example():
    ...

```


Parameters:

**endpoint** (

Return type:

_F_], _F_]

errorhandler(_code_or_exception_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.errorhandler "Link to this definition")

Register a function to handle errors by code or exception class.
A decorator that is used to register a function given an error code. Example:
```
@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404

```

You can also register handlers for arbitrary exceptions:
```
@app.errorhandler(DatabaseError)
def special_exception_handler(error):
    return 'Database connection failed', 500

```

This is available on both app and blueprint objects. When used on an app, this can handle errors from every request. When used on a blueprint, this can handle errors from requests that the blueprint handles. To register with a blueprint and affect every request, use [`Blueprint.app_errorhandler()`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.app_errorhandler "flask.Blueprint.app_errorhandler").
Changelog
Added in version 0.7: Use [`register_error_handler()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.register_error_handler "flask.Flask.register_error_handler") instead of modifying [`error_handler_spec`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.error_handler_spec "flask.Flask.error_handler_spec") directly, for application wide error handlers.
Added in version 0.7: One can now additionally also register custom exception types that do not necessarily have to be a subclass of the [`HTTPException`](https://werkzeug.palletsprojects.com/en/stable/exceptions/#werkzeug.exceptions.HTTPException "\(in Werkzeug v3.1.x\)") class.

Parameters:

**code_or_exception** (_[__]__|_

Return type:

_T_error_handler_], _T_error_handler_]

get(_rule_ , _** options_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.get "Link to this definition")

Shortcut for [`route()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.route "flask.Flask.route") with `methods=["GET"]`.
Changelog
Added in version 2.0.

Parameters:

  * **rule** (
  * **options** (



Return type:

_T_route_], _T_route_]

handle_url_build_error(_error_ , _endpoint_ , _values_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.handle_url_build_error "Link to this definition")

Called by [`url_for()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.url_for "flask.Flask.url_for") if a `BuildError` was raised. If this returns a value, it will be returned by `url_for`, otherwise the error will be re-raised.
Each function in [`url_build_error_handlers`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.url_build_error_handlers "flask.Flask.url_build_error_handlers") is called with `error`, `endpoint` and `values`. If a function returns `None` or raises a `BuildError`, it is skipped. Otherwise, its return value is returned by `url_for`.

Parameters:

  * **error** (_BuildError_) – The active `BuildError` being handled.
  * **endpoint** (
  * **values** (_[__,__]_) – The keyword arguments passed to `url_for`.



Return type:


_property_ has_static_folder _:_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.has_static_folder "Link to this definition")

`True` if [`static_folder`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.static_folder "flask.Flask.static_folder") is set.
Changelog
Added in version 0.5.

inject_url_defaults(_endpoint_ , _values_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.inject_url_defaults "Link to this definition")

Injects the URL defaults for the given endpoint directly into the values dictionary passed. This is used internally and automatically called on URL building.
Changelog
Added in version 0.7.

Parameters:

  * **endpoint** (
  * **values** (_[__,__]_)



Return type:

None

iter_blueprints()[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.iter_blueprints "Link to this definition")

Iterates over all blueprints by the order they were registered.
Changelog
Added in version 0.11.

Return type:

t.ValuesView[[Blueprint](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint "flask.Blueprint")]

_property_ jinja_env _: Environment_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.jinja_env "Link to this definition")

The Jinja environment used to load templates.
The environment is created the first time this property is accessed. Changing [`jinja_options`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.jinja_options "flask.Flask.jinja_options") after that will have no effect.

jinja_environment[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.jinja_environment "Link to this definition")

alias of `Environment`

_property_ jinja_loader _:[ BaseLoader](https://jinja.palletsprojects.com/en/stable/api/#jinja2.BaseLoader "\(in Jinja v3.1.x\)")|_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.jinja_loader "Link to this definition")

The Jinja loader for this object’s templates. By default this is a class [`jinja2.loaders.FileSystemLoader`](https://jinja.palletsprojects.com/en/stable/api/#jinja2.FileSystemLoader "\(in Jinja v3.1.x\)") to [`template_folder`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.template_folder "flask.Flask.template_folder") if it is set.
Changelog
Added in version 0.5.

jinja_options _:[,t.Any]__={}_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.jinja_options "Link to this definition")

Options that are passed to the Jinja environment in [`create_jinja_environment()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.create_jinja_environment "flask.Flask.create_jinja_environment"). Changing these options after the environment is created (accessing [`jinja_env`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.jinja_env "flask.Flask.jinja_env")) will have no effect.
Changelog
Changed in version 1.1.0: This is a `dict` instead of an `ImmutableDict` to allow easier configuration.

json_provider_class[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.json_provider_class "Link to this definition")

alias of [`DefaultJSONProvider`](https://flask.palletsprojects.com/en/stable/api/#flask.json.provider.DefaultJSONProvider "flask.json.provider.DefaultJSONProvider")

_property_ logger _:_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.logger "Link to this definition")

A standard Python [`name`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.name "flask.Flask.name").
In debug mode, the logger’s
If there are no handlers configured, a default handler will be added. See [Logging](https://flask.palletsprojects.com/en/stable/logging/) for more information.
Changelog
Changed in version 1.1.0: The logger takes the same name as [`name`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.name "flask.Flask.name") rather than hard-coding `"flask.app"`.
Changed in version 1.0.0: Behavior was simplified. The logger is always named `"flask.app"`. The level is only set during configuration, it doesn’t check `app.debug` each time. Only one format is used, not different ones depending on `app.debug`. No handlers are removed, and a handler is only added if no handlers are already configured.
Added in version 0.3.

make_aborter()[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.make_aborter "Link to this definition")

Create the object to assign to [`aborter`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.aborter "flask.Flask.aborter"). That object is called by [`flask.abort()`](https://flask.palletsprojects.com/en/stable/api/#flask.abort "flask.abort") to raise HTTP errors, and can be called directly as well.
By default, this creates an instance of [`aborter_class`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.aborter_class "flask.Flask.aborter_class"), which defaults to [`werkzeug.exceptions.Aborter`](https://werkzeug.palletsprojects.com/en/stable/exceptions/#werkzeug.exceptions.Aborter "\(in Werkzeug v3.1.x\)").
Changelog
Added in version 2.2.

Return type:

[_Aborter_](https://werkzeug.palletsprojects.com/en/stable/exceptions/#werkzeug.exceptions.Aborter "\(in Werkzeug v3.1.x\)")

make_config(_instance_relative =False_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.make_config "Link to this definition")

Used to create the config attribute by the Flask constructor. The `instance_relative` parameter is passed in from the constructor of Flask (there named `instance_relative_config`) and indicates if the config should be relative to the instance path or the root path of the application.
Changelog
Added in version 0.8.

Parameters:

**instance_relative** (

Return type:

[_Config_](https://flask.palletsprojects.com/en/stable/api/#flask.Config "flask.config.Config")

_property_ name _:_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.name "Link to this definition")

The name of the application. This is usually the import name with the difference that it’s guessed from the run file if the import name is main. This name is used as a display name when Flask needs the name of the application. It can be set and overridden to change the value.
Changelog
Added in version 0.8.

patch(_rule_ , _** options_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.patch "Link to this definition")

Shortcut for [`route()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.route "flask.Flask.route") with `methods=["PATCH"]`.
Changelog
Added in version 2.0.

Parameters:

  * **rule** (
  * **options** (



Return type:

_T_route_], _T_route_]

permanent_session_lifetime[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.permanent_session_lifetime "Link to this definition")

A
This attribute can also be configured from the config with the `PERMANENT_SESSION_LIFETIME` configuration key. Defaults to `timedelta(days=31)`

post(_rule_ , _** options_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.post "Link to this definition")

Shortcut for [`route()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.route "flask.Flask.route") with `methods=["POST"]`.
Changelog
Added in version 2.0.

Parameters:

  * **rule** (
  * **options** (



Return type:

_T_route_], _T_route_]

put(_rule_ , _** options_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.put "Link to this definition")

Shortcut for [`route()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.route "flask.Flask.route") with `methods=["PUT"]`.
Changelog
Added in version 2.0.

Parameters:

  * **rule** (
  * **options** (



Return type:

_T_route_], _T_route_]

redirect(_location_ , _code =302_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.redirect "Link to this definition")

Create a redirect response object.
This is called by [`flask.redirect()`](https://flask.palletsprojects.com/en/stable/api/#flask.redirect "flask.redirect"), and can be called directly as well.

Parameters:

  * **location** (
  * **code** (



Return type:

BaseResponse Changelog
Added in version 2.2: Moved from `flask.redirect`, which calls this method.

register_blueprint(_blueprint_ , _** options_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.register_blueprint "Link to this definition")

Register a [`Blueprint`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint "flask.Blueprint") on the application. Keyword arguments passed to this method will override the defaults set on the blueprint.
Calls the blueprint’s [`register()`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.register "flask.Blueprint.register") method after recording the blueprint in the application’s [`blueprints`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.blueprints "flask.Flask.blueprints").

Parameters:

  * **blueprint** ([_Blueprint_](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint "flask.Blueprint")) – The blueprint to register.
  * **url_prefix** – Blueprint routes will be prefixed with this.
  * **subdomain** – Blueprint routes will match on this subdomain.
  * **url_defaults** – Blueprint routes will use these default values for view arguments.
  * **options** (_t.Any_) – Additional keyword arguments are passed to [`BlueprintSetupState`](https://flask.palletsprojects.com/en/stable/api/#flask.blueprints.BlueprintSetupState "flask.blueprints.BlueprintSetupState"). They can be accessed in [`record()`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.record "flask.Blueprint.record") callbacks.



Return type:

None Changelog
Changed in version 2.0.1: The `name` option can be used to change the (pre-dotted) name the blueprint is registered with. This allows the same blueprint to be registered multiple times with unique names for `url_for`.
Added in version 0.7.

register_error_handler(_code_or_exception_ , _f_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.register_error_handler "Link to this definition")

Alternative error attach function to the [`errorhandler()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.errorhandler "flask.Flask.errorhandler") decorator that is more straightforward to use for non decorator usage.
Changelog
Added in version 0.7.

Parameters:

  * **code_or_exception** (_[__]__|_
  * **f** (_ft.ErrorHandlerCallable_)



Return type:

None

route(_rule_ , _** options_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.route "Link to this definition")

Decorate a view function to register it with the given URL rule and options. Calls [`add_url_rule()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.add_url_rule "flask.Flask.add_url_rule"), which has more details about the implementation.
```
@app.route("/")
def index():
    return "Hello, World!"

```

See [URL Route Registrations](https://flask.palletsprojects.com/en/stable/api/#url-route-registrations).
The endpoint name for the route defaults to the name of the view function if the `endpoint` parameter isn’t passed.
The `methods` parameter defaults to `["GET"]`. `HEAD` and `OPTIONS` are added automatically.

Parameters:

  * **rule** (
  * **options** ([`Rule`](https://werkzeug.palletsprojects.com/en/stable/routing/#werkzeug.routing.Rule "\(in Werkzeug v3.1.x\)") object.



Return type:

_T_route_], _T_route_]

secret_key[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.secret_key "Link to this definition")

If a secret key is set, cryptographic components can use this to sign cookies and other things. Set this to a complex random value when you want to use the secure cookie for instance.
This attribute can also be configured from the config with the [`SECRET_KEY`](https://flask.palletsprojects.com/en/stable/config/#SECRET_KEY "SECRET_KEY") configuration key. Defaults to `None`.

select_jinja_autoescape(_filename_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.select_jinja_autoescape "Link to this definition")

Returns `True` if autoescaping should be active for the given template name. If no template name is given, returns `True`.
Changelog
Changed in version 2.2: Autoescaping is now enabled by default for `.svg` files.
Added in version 0.5.

Parameters:

**filename** (_|__None_)

Return type:


shell_context_processor(_f_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.shell_context_processor "Link to this definition")

Registers a shell context processor function.
Changelog
Added in version 0.11.

Parameters:

**f** (_T_shell_context_processor_)

Return type:

_T_shell_context_processor_

should_ignore_error(_error_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.should_ignore_error "Link to this definition")

This is called to figure out if an error should be ignored or not as far as the teardown system is concerned. If this function returns `True` then the teardown handlers will not be passed the error.
Changelog
Added in version 0.10.

Parameters:

**error** (_|__None_)

Return type:


_property_ static_folder _: |_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.static_folder "Link to this definition")

The absolute path to the configured static folder. `None` if no static folder is set.

_property_ static_url_path _: |_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.static_url_path "Link to this definition")

The URL prefix that the static route will be accessible from.
If it was not configured during init, it is derived from [`static_folder`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.static_folder "flask.Flask.static_folder").

teardown_appcontext(_f_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.teardown_appcontext "Link to this definition")

Registers a function to be called when the application context is popped. The application context is typically popped after the request context for each request, at the end of CLI commands, or after a manually pushed context ends.
```
with app.app_context():
    ...

```

When the `with` block exits (or `ctx.pop()` is called), the teardown functions are called just before the app context is made inactive. Since a request context typically also manages an application context it would also be called when you pop a request context.
When a teardown function was called because of an unhandled exception it will be passed an error object. If an [`errorhandler()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.errorhandler "flask.Flask.errorhandler") is registered, it will handle the exception and the teardown will not receive it.
Teardown functions must avoid raising exceptions. If they execute code that might fail they must surround that code with a `try`/`except` block and log any errors.
The return values of teardown functions are ignored.
Changelog
Added in version 0.9.

Parameters:

**f** (_T_teardown_)

Return type:

_T_teardown_

teardown_request(_f_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.teardown_request "Link to this definition")

Register a function to be called when the request context is popped. Typically this happens at the end of each request, but contexts may be pushed manually as well during testing.
```
with app.test_request_context():
    ...

```

When the `with` block exits (or `ctx.pop()` is called), the teardown functions are called just before the request context is made inactive.
When a teardown function was called because of an unhandled exception it will be passed an error object. If an [`errorhandler()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.errorhandler "flask.Flask.errorhandler") is registered, it will handle the exception and the teardown will not receive it.
Teardown functions must avoid raising exceptions. If they execute code that might fail they must surround that code with a `try`/`except` block and log any errors.
The return values of teardown functions are ignored.
This is available on both app and blueprint objects. When used on an app, this executes after every request. When used on a blueprint, this executes after every request that the blueprint handles. To register with a blueprint and execute after every request, use [`Blueprint.teardown_app_request()`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.teardown_app_request "flask.Blueprint.teardown_app_request").

Parameters:

**f** (_T_teardown_)

Return type:

_T_teardown_

template_filter(_name =None_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.template_filter "Link to this definition")

A decorator that is used to register custom template filter. You can specify a name for the filter, otherwise the function name will be used. Example:
```
@app.template_filter()
def reverse(s):
    return s[::-1]

```


Parameters:

**name** (_|__None_) – the optional name of the filter, otherwise the function name will be used.

Return type:

_T_template_filter_], _T_template_filter_]

template_global(_name =None_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.template_global "Link to this definition")

A decorator that is used to register a custom template global function. You can specify a name for the global function, otherwise the function name will be used. Example:
```
@app.template_global()
def double(n):
    return 2 * n

```

Changelog
Added in version 0.10.

Parameters:

**name** (_|__None_) – the optional name of the global function, otherwise the function name will be used.

Return type:

_T_template_global_], _T_template_global_]

template_test(_name =None_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.template_test "Link to this definition")

A decorator that is used to register custom template test. You can specify a name for the test, otherwise the function name will be used. Example:
```
@app.template_test()
def is_prime(n):
    if n == 2:
        return True
    for i in range(2, int(math.ceil(math.sqrt(n))) + 1):
        if n % i == 0:
            return False
    return True

```

Changelog
Added in version 0.10.

Parameters:

**name** (_|__None_) – the optional name of the test, otherwise the function name will be used.

Return type:

_T_template_test_], _T_template_test_]

test_cli_runner_class _:[[FlaskCliRunner](https://flask.palletsprojects.com/en/stable/api/#flask.testing.FlaskCliRunner "flask.testing.FlaskCliRunner")]|__= None_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.test_cli_runner_class "Link to this definition")

The [`CliRunner`](https://click.palletsprojects.com/en/stable/api/#click.testing.CliRunner "\(in Click v8.3.x\)") subclass, by default [`FlaskCliRunner`](https://flask.palletsprojects.com/en/stable/api/#flask.testing.FlaskCliRunner "flask.testing.FlaskCliRunner") that is used by [`test_cli_runner()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.test_cli_runner "flask.Flask.test_cli_runner"). Its `__init__` method should take a Flask app object as the first argument.
Changelog
Added in version 1.0.

test_client_class _:[[FlaskClient](https://flask.palletsprojects.com/en/stable/api/#flask.testing.FlaskClient "flask.testing.FlaskClient")]|__= None_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.test_client_class "Link to this definition")

The [`test_client()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.test_client "flask.Flask.test_client") method creates an instance of this test client class. Defaults to [`FlaskClient`](https://flask.palletsprojects.com/en/stable/api/#flask.testing.FlaskClient "flask.testing.FlaskClient").
Changelog
Added in version 0.7.

testing[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.testing "Link to this definition")

The testing flag. Set this to `True` to enable the test mode of Flask extensions (and in the future probably also Flask itself). For example this might activate test helpers that have an additional runtime cost which should not be enabled by default.
If this is enabled and PROPAGATE_EXCEPTIONS is not changed from the default it’s implicitly enabled.
This attribute can also be configured from the config with the `TESTING` configuration key. Defaults to `False`.

trap_http_exception(_e_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.trap_http_exception "Link to this definition")

Checks if an HTTP exception should be trapped or not. By default this will return `False` for all exceptions except for a bad request key error if `TRAP_BAD_REQUEST_ERRORS` is set to `True`. It also returns `True` if `TRAP_HTTP_EXCEPTIONS` is set to `True`.
This is called for all HTTP exceptions raised by a view function. If it returns `True` for any exception the error handler for this exception is not called and it shows up as regular exception in the traceback. This is helpful for debugging implicitly raised HTTP exceptions.
Changelog
Changed in version 1.0: Bad request errors are not trapped by default in debug mode.
