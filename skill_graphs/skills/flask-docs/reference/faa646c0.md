## Blueprint Objects[¶](https://flask.palletsprojects.com/en/stable/api/#blueprint-objects "Link to this heading")

_class_ flask.Blueprint(_name_ , _import_name_ , _static_folder =None_, _static_url_path =None_, _template_folder =None_, _url_prefix =None_, _subdomain =None_, _url_defaults =None_, _root_path =None_, _cli_group =_sentinel_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint "Link to this definition")


Parameters:

  * **name** (
  * **import_name** (
  * **static_folder** (_|__[__]__|__None_)
  * **static_url_path** (_|__None_)
  * **template_folder** (_|__[__]__|__None_)
  * **url_prefix** (_|__None_)
  * **subdomain** (_|__None_)
  * **url_defaults** (_[__,__t.Any_ _]__|__None_)
  * **root_path** (_|__None_)
  * **cli_group** (_|__None_)



cli _: Group_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.cli "Link to this definition")

The Click command group for registering CLI commands for this object. The commands are available from the `flask` command once the application has been discovered and blueprints have been registered.

get_send_file_max_age(_filename_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.get_send_file_max_age "Link to this definition")

Used by [`send_file()`](https://flask.palletsprojects.com/en/stable/api/#flask.send_file "flask.send_file") to determine the `max_age` cache value for a given file path if it wasn’t passed.
By default, this returns [`SEND_FILE_MAX_AGE_DEFAULT`](https://flask.palletsprojects.com/en/stable/config/#SEND_FILE_MAX_AGE_DEFAULT "SEND_FILE_MAX_AGE_DEFAULT") from the configuration of [`current_app`](https://flask.palletsprojects.com/en/stable/api/#flask.current_app "flask.current_app"). This defaults to `None`, which tells the browser to use conditional requests instead of a timed cache, which is usually preferable.
Note this is a duplicate of the same method in the Flask class.
Changelog
Changed in version 2.0: The default configuration is `None` instead of 12 hours.
Added in version 0.9.

Parameters:

**filename** (_|__None_)

Return type:


send_static_file(_filename_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.send_static_file "Link to this definition")

The view function used to serve files from [`static_folder`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.static_folder "flask.Blueprint.static_folder"). A route is automatically registered for this view at [`static_url_path`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.static_url_path "flask.Blueprint.static_url_path") if [`static_folder`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.static_folder "flask.Blueprint.static_folder") is set.
Note this is a duplicate of the same method in the Flask class.
Changelog
Added in version 0.5.

Parameters:

**filename** (

Return type:

[Response](https://flask.palletsprojects.com/en/stable/api/#flask.Response "flask.Response")

open_resource(_resource_ , _mode ='rb'_, _encoding ='utf-8'_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.open_resource "Link to this definition")

Open a resource file relative to [`root_path`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.root_path "flask.Blueprint.root_path") for reading. The blueprint-relative equivalent of the app’s [`open_resource()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.open_resource "flask.Flask.open_resource") method.

Parameters:

  * **resource** ([`root_path`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.root_path "flask.Blueprint.root_path").
  * **mode** (`"r"` (or `"rt"`) and `"rb"`.
  * **encoding** (_|__None_) – Open the file with this encoding when opening in text mode. This is ignored when opening in binary mode.



Return type:

Changed in version 3.1: Added the `encoding` parameter.

add_app_template_filter(_f_ , _name =None_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.add_app_template_filter "Link to this definition")

Register a template filter, available in any template rendered by the application. Works like the [`app_template_filter()`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.app_template_filter "flask.Blueprint.app_template_filter") decorator. Equivalent to [`Flask.add_template_filter()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.add_template_filter "flask.Flask.add_template_filter").

Parameters:

  * **name** (_|__None_) – the optional name of the filter, otherwise the function name will be used.
  * **f** (_[__[__...__]__,__]_)



Return type:

None

add_app_template_global(_f_ , _name =None_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.add_app_template_global "Link to this definition")

Register a template global, available in any template rendered by the application. Works like the [`app_template_global()`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.app_template_global "flask.Blueprint.app_template_global") decorator. Equivalent to [`Flask.add_template_global()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.add_template_global "flask.Flask.add_template_global").
Changelog
Added in version 0.10.

Parameters:

  * **name** (_|__None_) – the optional name of the global, otherwise the function name will be used.
  * **f** (_[__[__...__]__,__]_)



Return type:

None

add_app_template_test(_f_ , _name =None_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.add_app_template_test "Link to this definition")

Register a template test, available in any template rendered by the application. Works like the [`app_template_test()`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.app_template_test "flask.Blueprint.app_template_test") decorator. Equivalent to [`Flask.add_template_test()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.add_template_test "flask.Flask.add_template_test").
Changelog
Added in version 0.10.

Parameters:

  * **name** (_|__None_) – the optional name of the test, otherwise the function name will be used.
  * **f** (_[__[__...__]__,__]_)



Return type:

None

add_url_rule(_rule_ , _endpoint =None_, _view_func =None_, _provide_automatic_options =None_, _** options_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.add_url_rule "Link to this definition")

Register a URL rule with the blueprint. See [`Flask.add_url_rule()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.add_url_rule "flask.Flask.add_url_rule") for full documentation.
The URL rule is prefixed with the blueprint’s URL prefix. The endpoint name, used with [`url_for()`](https://flask.palletsprojects.com/en/stable/api/#flask.url_for "flask.url_for"), is prefixed with the blueprint’s name.

Parameters:

  * **rule** (
  * **endpoint** (_|__None_)
  * **view_func** (_ft.RouteCallable_ _|__None_)
  * **provide_automatic_options** (_|__None_)
  * **options** (_t.Any_)



Return type:

None

after_app_request(_f_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.after_app_request "Link to this definition")

Like [`after_request()`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.after_request "flask.Blueprint.after_request"), but after every request, not only those handled by the blueprint. Equivalent to [`Flask.after_request()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.after_request "flask.Flask.after_request").

Parameters:

**f** (_T_after_request_)

Return type:

_T_after_request_

after_request(_f_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.after_request "Link to this definition")

Register a function to run after each request to this object.
The function is called with the response object, and must return a response object. This allows the functions to modify or replace the response before it is sent.
If a function raises an exception, any remaining `after_request` functions will not be called. Therefore, this should not be used for actions that must execute, such as to close resources. Use [`teardown_request()`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.teardown_request "flask.Blueprint.teardown_request") for that.
This is available on both app and blueprint objects. When used on an app, this executes after every request. When used on a blueprint, this executes after every request that the blueprint handles. To register with a blueprint and execute after every request, use [`Blueprint.after_app_request()`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.after_app_request "flask.Blueprint.after_app_request").

Parameters:

**f** (_T_after_request_)

Return type:

_T_after_request_

app_context_processor(_f_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.app_context_processor "Link to this definition")

Like [`context_processor()`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.context_processor "flask.Blueprint.context_processor"), but for templates rendered by every view, not only by the blueprint. Equivalent to [`Flask.context_processor()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.context_processor "flask.Flask.context_processor").

Parameters:

**f** (_T_template_context_processor_)

Return type:

_T_template_context_processor_

app_errorhandler(_code_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.app_errorhandler "Link to this definition")

Like [`errorhandler()`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.errorhandler "flask.Blueprint.errorhandler"), but for every request, not only those handled by the blueprint. Equivalent to [`Flask.errorhandler()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.errorhandler "flask.Flask.errorhandler").

Parameters:

**code** (_[__]__|_

Return type:

_T_error_handler_], _T_error_handler_]

app_template_filter(_name =None_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.app_template_filter "Link to this definition")

Register a template filter, available in any template rendered by the application. Equivalent to [`Flask.template_filter()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.template_filter "flask.Flask.template_filter").

Parameters:

**name** (_|__None_) – the optional name of the filter, otherwise the function name will be used.

Return type:

_T_template_filter_], _T_template_filter_]

app_template_global(_name =None_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.app_template_global "Link to this definition")

Register a template global, available in any template rendered by the application. Equivalent to [`Flask.template_global()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.template_global "flask.Flask.template_global").
Changelog
Added in version 0.10.

Parameters:

**name** (_|__None_) – the optional name of the global, otherwise the function name will be used.

Return type:

_T_template_global_], _T_template_global_]

app_template_test(_name =None_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.app_template_test "Link to this definition")

Register a template test, available in any template rendered by the application. Equivalent to [`Flask.template_test()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.template_test "flask.Flask.template_test").
Changelog
Added in version 0.10.

Parameters:

**name** (_|__None_) – the optional name of the test, otherwise the function name will be used.

Return type:

_T_template_test_], _T_template_test_]

app_url_defaults(_f_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.app_url_defaults "Link to this definition")

Like [`url_defaults()`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.url_defaults "flask.Blueprint.url_defaults"), but for every request, not only those handled by the blueprint. Equivalent to [`Flask.url_defaults()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.url_defaults "flask.Flask.url_defaults").

Parameters:

**f** (_T_url_defaults_)

Return type:

_T_url_defaults_

app_url_value_preprocessor(_f_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.app_url_value_preprocessor "Link to this definition")

Like [`url_value_preprocessor()`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.url_value_preprocessor "flask.Blueprint.url_value_preprocessor"), but for every request, not only those handled by the blueprint. Equivalent to [`Flask.url_value_preprocessor()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.url_value_preprocessor "flask.Flask.url_value_preprocessor").

Parameters:

**f** (_T_url_value_preprocessor_)

Return type:

_T_url_value_preprocessor_

before_app_request(_f_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.before_app_request "Link to this definition")

Like [`before_request()`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.before_request "flask.Blueprint.before_request"), but before every request, not only those handled by the blueprint. Equivalent to [`Flask.before_request()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.before_request "flask.Flask.before_request").

Parameters:

**f** (_T_before_request_)

Return type:

_T_before_request_

before_request(_f_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.before_request "Link to this definition")

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

context_processor(_f_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.context_processor "Link to this definition")

Registers a template context processor function. These functions run before rendering a template. The keys of the returned dict are added as variables available in the template.
This is available on both app and blueprint objects. When used on an app, this is called for every rendered template. When used on a blueprint, this is called for templates rendered from the blueprint’s views. To register with a blueprint and affect every template, use [`Blueprint.app_context_processor()`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.app_context_processor "flask.Blueprint.app_context_processor").

Parameters:

**f** (_T_template_context_processor_)

Return type:

_T_template_context_processor_

delete(_rule_ , _** options_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.delete "Link to this definition")

Shortcut for [`route()`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.route "flask.Blueprint.route") with `methods=["DELETE"]`.
Changelog
Added in version 2.0.

Parameters:

  * **rule** (
  * **options** (



Return type:

_T_route_], _T_route_]

endpoint(_endpoint_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.endpoint "Link to this definition")

Decorate a view function to register it for the given endpoint. Used if a rule is added without a `view_func` with [`add_url_rule()`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.add_url_rule "flask.Blueprint.add_url_rule").
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

errorhandler(_code_or_exception_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.errorhandler "Link to this definition")

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
Added in version 0.7: Use [`register_error_handler()`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.register_error_handler "flask.Blueprint.register_error_handler") instead of modifying [`error_handler_spec`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.error_handler_spec "flask.Blueprint.error_handler_spec") directly, for application wide error handlers.
Added in version 0.7: One can now additionally also register custom exception types that do not necessarily have to be a subclass of the [`HTTPException`](https://werkzeug.palletsprojects.com/en/stable/exceptions/#werkzeug.exceptions.HTTPException "\(in Werkzeug v3.1.x\)") class.

Parameters:

**code_or_exception** (_[__]__|_

Return type:

_T_error_handler_], _T_error_handler_]

get(_rule_ , _** options_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.get "Link to this definition")

Shortcut for [`route()`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.route "flask.Blueprint.route") with `methods=["GET"]`.
Changelog
Added in version 2.0.

Parameters:

  * **rule** (
  * **options** (



Return type:

_T_route_], _T_route_]

_property_ has_static_folder _:_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.has_static_folder "Link to this definition")

`True` if [`static_folder`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.static_folder "flask.Blueprint.static_folder") is set.
Changelog
Added in version 0.5.

_property_ jinja_loader _:[ BaseLoader](https://jinja.palletsprojects.com/en/stable/api/#jinja2.BaseLoader "\(in Jinja v3.1.x\)")|_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.jinja_loader "Link to this definition")

The Jinja loader for this object’s templates. By default this is a class [`jinja2.loaders.FileSystemLoader`](https://jinja.palletsprojects.com/en/stable/api/#jinja2.FileSystemLoader "\(in Jinja v3.1.x\)") to [`template_folder`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.template_folder "flask.Blueprint.template_folder") if it is set.
Changelog
Added in version 0.5.

make_setup_state(_app_ , _options_ , _first_registration =False_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.make_setup_state "Link to this definition")

Creates an instance of [`BlueprintSetupState()`](https://flask.palletsprojects.com/en/stable/api/#flask.blueprints.BlueprintSetupState "flask.blueprints.BlueprintSetupState") object that is later passed to the register callback functions. Subclasses can override this to return a subclass of the setup state.

Parameters:

  * **app** (_App_)
  * **options** (_[__,__t.Any_ _]_)
  * **first_registration** (



Return type:

[BlueprintSetupState](https://flask.palletsprojects.com/en/stable/api/#flask.blueprints.BlueprintSetupState "flask.blueprints.BlueprintSetupState")

patch(_rule_ , _** options_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.patch "Link to this definition")

Shortcut for [`route()`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.route "flask.Blueprint.route") with `methods=["PATCH"]`.
Changelog
Added in version 2.0.

Parameters:

  * **rule** (
  * **options** (



Return type:

_T_route_], _T_route_]

post(_rule_ , _** options_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.post "Link to this definition")

Shortcut for [`route()`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.route "flask.Blueprint.route") with `methods=["POST"]`.
Changelog
Added in version 2.0.

Parameters:

  * **rule** (
  * **options** (



Return type:

_T_route_], _T_route_]

put(_rule_ , _** options_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.put "Link to this definition")

Shortcut for [`route()`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.route "flask.Blueprint.route") with `methods=["PUT"]`.
Changelog
Added in version 2.0.

Parameters:

  * **rule** (
  * **options** (



Return type:

_T_route_], _T_route_]

record(_func_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.record "Link to this definition")

Registers a function that is called when the blueprint is registered on the application. This function is called with the state as argument as returned by the [`make_setup_state()`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.make_setup_state "flask.Blueprint.make_setup_state") method.

Parameters:

**func** (_[__[_[_BlueprintSetupState_](https://flask.palletsprojects.com/en/stable/api/#flask.blueprints.BlueprintSetupState "flask.sansio.blueprints.BlueprintSetupState") _]__,__None_ _]_)

Return type:

None

record_once(_func_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.record_once "Link to this definition")

Works like [`record()`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.record "flask.Blueprint.record") but wraps the function in another function that will ensure the function is only called once. If the blueprint is registered a second time on the application, the function passed is not called.

Parameters:

**func** (_[__[_[_BlueprintSetupState_](https://flask.palletsprojects.com/en/stable/api/#flask.blueprints.BlueprintSetupState "flask.sansio.blueprints.BlueprintSetupState") _]__,__None_ _]_)

Return type:

None

register(_app_ , _options_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.register "Link to this definition")

Called by [`Flask.register_blueprint()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.register_blueprint "flask.Flask.register_blueprint") to register all views and callbacks registered on the blueprint with the application. Creates a [`BlueprintSetupState`](https://flask.palletsprojects.com/en/stable/api/#flask.blueprints.BlueprintSetupState "flask.blueprints.BlueprintSetupState") and calls each [`record()`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.record "flask.Blueprint.record") callback with it.

Parameters:

  * **app** (_App_) – The application this blueprint is being registered with.
  * **options** (_[__,__t.Any_ _]_) – Keyword arguments forwarded from [`register_blueprint()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.register_blueprint "flask.Flask.register_blueprint").



Return type:

None Changelog
Changed in version 2.3: Nested blueprints now correctly apply subdomains.
Changed in version 2.1: Registering the same blueprint with the same name multiple times is an error.
Changed in version 2.0.1: Nested blueprints are registered with their dotted name. This allows different blueprints with the same name to be nested at different locations.
Changed in version 2.0.1: The `name` option can be used to change the (pre-dotted) name the blueprint is registered with. This allows the same blueprint to be registered multiple times with unique names for `url_for`.

register_blueprint(_blueprint_ , _** options_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.register_blueprint "Link to this definition")

Register a [`Blueprint`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint "flask.Blueprint") on this blueprint. Keyword arguments passed to this method will override the defaults set on the blueprint.
Changelog
Changed in version 2.0.1: The `name` option can be used to change the (pre-dotted) name the blueprint is registered with. This allows the same blueprint to be registered multiple times with unique names for `url_for`.
Added in version 2.0.

Parameters:

  * **blueprint** (_Blueprint_)
  * **options** (



Return type:

None

register_error_handler(_code_or_exception_ , _f_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.register_error_handler "Link to this definition")

Alternative error attach function to the [`errorhandler()`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.errorhandler "flask.Blueprint.errorhandler") decorator that is more straightforward to use for non decorator usage.
Changelog
Added in version 0.7.

Parameters:

  * **code_or_exception** (_[__]__|_
  * **f** (_ft.ErrorHandlerCallable_)



Return type:

None

route(_rule_ , _** options_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.route "Link to this definition")

Decorate a view function to register it with the given URL rule and options. Calls [`add_url_rule()`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.add_url_rule "flask.Blueprint.add_url_rule"), which has more details about the implementation.
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

_property_ static_folder _: |_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.static_folder "Link to this definition")

The absolute path to the configured static folder. `None` if no static folder is set.

_property_ static_url_path _: |_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.static_url_path "Link to this definition")

The URL prefix that the static route will be accessible from.
If it was not configured during init, it is derived from [`static_folder`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.static_folder "flask.Blueprint.static_folder").

teardown_app_request(_f_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.teardown_app_request "Link to this definition")

Like [`teardown_request()`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.teardown_request "flask.Blueprint.teardown_request"), but after every request, not only those handled by the blueprint. Equivalent to [`Flask.teardown_request()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.teardown_request "flask.Flask.teardown_request").

Parameters:

**f** (_T_teardown_)

Return type:

_T_teardown_

teardown_request(_f_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.teardown_request "Link to this definition")

Register a function to be called when the request context is popped. Typically this happens at the end of each request, but contexts may be pushed manually as well during testing.
```
with app.test_request_context():
    ...

```

When the `with` block exits (or `ctx.pop()` is called), the teardown functions are called just before the request context is made inactive.
When a teardown function was called because of an unhandled exception it will be passed an error object. If an [`errorhandler()`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.errorhandler "flask.Blueprint.errorhandler") is registered, it will handle the exception and the teardown will not receive it.
Teardown functions must avoid raising exceptions. If they execute code that might fail they must surround that code with a `try`/`except` block and log any errors.
The return values of teardown functions are ignored.
This is available on both app and blueprint objects. When used on an app, this executes after every request. When used on a blueprint, this executes after every request that the blueprint handles. To register with a blueprint and execute after every request, use [`Blueprint.teardown_app_request()`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.teardown_app_request "flask.Blueprint.teardown_app_request").

Parameters:

**f** (_T_teardown_)

Return type:

_T_teardown_

url_defaults(_f_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.url_defaults "Link to this definition")

Callback function for URL defaults for all view functions of the application. It’s called with the endpoint and values and should update the values passed in place.
This is available on both app and blueprint objects. When used on an app, this is called for every request. When used on a blueprint, this is called for requests that the blueprint handles. To register with a blueprint and affect every request, use [`Blueprint.app_url_defaults()`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.app_url_defaults "flask.Blueprint.app_url_defaults").

Parameters:

**f** (_T_url_defaults_)

Return type:

_T_url_defaults_

url_value_preprocessor(_f_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.url_value_preprocessor "Link to this definition")

Register a URL value preprocessor function for all view functions in the application. These functions will be called before the [`before_request()`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.before_request "flask.Blueprint.before_request") functions.
The function can modify the values captured from the matched url before they are passed to the view. For example, this can be used to pop a common language code value and place it in `g` rather than pass it to every view.
The function is passed the endpoint name and values dict. The return value is ignored.
This is available on both app and blueprint objects. When used on an app, this is called for every request. When used on a blueprint, this is called for requests that the blueprint handles. To register with a blueprint and affect every request, use [`Blueprint.app_url_value_preprocessor()`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.app_url_value_preprocessor "flask.Blueprint.app_url_value_preprocessor").

Parameters:

**f** (_T_url_value_preprocessor_)

Return type:

_T_url_value_preprocessor_

import_name[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.import_name "Link to this definition")

The name of the package or module that this object belongs to. Do not change this once it is set by the constructor.

template_folder[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.template_folder "Link to this definition")

The path to the templates folder, relative to [`root_path`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.root_path "flask.Blueprint.root_path"), to add to the template loader. `None` if templates should not be added.

root_path[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.root_path "Link to this definition")

Absolute path to the package on the filesystem. Used to look up resources contained in the package.

view_functions _:[,ft.RouteCallable]_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.view_functions "Link to this definition")

A dictionary mapping endpoint names to view functions.
To register a view function, use the [`route()`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.route "flask.Blueprint.route") decorator.
This data structure is internal. It should not be modified directly and its format may change at any time.

error_handler_spec _:[ft.AppOrBlueprintKey,[|,[[],ft.ErrorHandlerCallable]]]_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.error_handler_spec "Link to this definition")

A data structure of registered error handlers, in the format `{scope: {code: {class: handler}}}`. The `scope` key is the name of a blueprint the handlers are active for, or `None` for all requests. The `code` key is the HTTP status code for `HTTPException`, or `None` for other exceptions. The innermost dictionary maps exception classes to handler functions.
To register an error handler, use the [`errorhandler()`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.errorhandler "flask.Blueprint.errorhandler") decorator.
This data structure is internal. It should not be modified directly and its format may change at any time.

before_request_funcs _:[ft.AppOrBlueprintKey,[ft.BeforeRequestCallable]]_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.before_request_funcs "Link to this definition")

A data structure of functions to call at the beginning of each request, in the format `{scope: [functions]}`. The `scope` key is the name of a blueprint the functions are active for, or `None` for all requests.
To register a function, use the [`before_request()`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.before_request "flask.Blueprint.before_request") decorator.
This data structure is internal. It should not be modified directly and its format may change at any time.

after_request_funcs _:[ft.AppOrBlueprintKey,[ft.AfterRequestCallable[t.Any]]]_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.after_request_funcs "Link to this definition")

A data structure of functions to call at the end of each request, in the format `{scope: [functions]}`. The `scope` key is the name of a blueprint the functions are active for, or `None` for all requests.
To register a function, use the [`after_request()`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.after_request "flask.Blueprint.after_request") decorator.
This data structure is internal. It should not be modified directly and its format may change at any time.

teardown_request_funcs _:[ft.AppOrBlueprintKey,[ft.TeardownCallable]]_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.teardown_request_funcs "Link to this definition")

A data structure of functions to call at the end of each request even if an exception is raised, in the format `{scope: [functions]}`. The `scope` key is the name of a blueprint the functions are active for, or `None` for all requests.
To register a function, use the [`teardown_request()`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.teardown_request "flask.Blueprint.teardown_request") decorator.
This data structure is internal. It should not be modified directly and its format may change at any time.

template_context_processors _:[ft.AppOrBlueprintKey,[ft.TemplateContextProcessorCallable]]_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.template_context_processors "Link to this definition")

A data structure of functions to call to pass extra context values when rendering templates, in the format `{scope: [functions]}`. The `scope` key is the name of a blueprint the functions are active for, or `None` for all requests.
To register a function, use the [`context_processor()`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.context_processor "flask.Blueprint.context_processor") decorator.
This data structure is internal. It should not be modified directly and its format may change at any time.

url_value_preprocessors _:[ft.AppOrBlueprintKey,[ft.URLValuePreprocessorCallable]]_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.url_value_preprocessors "Link to this definition")

A data structure of functions to call to modify the keyword arguments passed to the view function, in the format `{scope: [functions]}`. The `scope` key is the name of a blueprint the functions are active for, or `None` for all requests.
To register a function, use the [`url_value_preprocessor()`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.url_value_preprocessor "flask.Blueprint.url_value_preprocessor") decorator.
This data structure is internal. It should not be modified directly and its format may change at any time.

url_default_functions _:[ft.AppOrBlueprintKey,[ft.URLDefaultCallable]]_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.url_default_functions "Link to this definition")

A data structure of functions to call to modify the keyword arguments when generating URLs, in the format `{scope: [functions]}`. The `scope` key is the name of a blueprint the functions are active for, or `None` for all requests.
To register a function, use the [`url_defaults()`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.url_defaults "flask.Blueprint.url_defaults") decorator.
This data structure is internal. It should not be modified directly and its format may change at any time.
