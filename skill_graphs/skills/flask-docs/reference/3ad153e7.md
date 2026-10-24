## Application Object[¶](https://flask.palletsprojects.com/en/stable/api/#application-object "Link to this heading")

_class_ flask.Flask(_import_name_ , _static_url_path =None_, _static_folder ='static'_, _static_host =None_, _host_matching =False_, _subdomain_matching =False_, _template_folder ='templates'_, _instance_path =None_, _instance_relative_config =False_, _root_path =None_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask "Link to this definition")

The flask object implements a WSGI application and acts as the central object. It is passed the name of the module or package of the application. Once it is created it will act as a central registry for the view functions, the URL rules, template configuration and much more.
The name of the package is used to resolve resources from inside the package or the folder the module is contained in depending on if the package parameter resolves to an actual python package (a folder with an `__init__.py` file inside) or a standard module (just a `.py` file).
For more information about resource loading, see [`open_resource()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.open_resource "flask.Flask.open_resource").
Usually you create a [`Flask`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask "flask.Flask") instance in your main module or in the `__init__.py` file of your package like this:
```
from flask import Flask
app = Flask(__name__)

```

About the First Parameter
The idea of the first parameter is to give Flask an idea of what belongs to your application. This name is used to find resources on the filesystem, can be used by extensions to improve debugging information and a lot more.
So it’s important what you provide there. If you are using a single module, `__name__` is always the correct value. If you however are using a package, it’s usually recommended to hardcode the name of your package there.
For example if your application is defined in `yourapplication/app.py` you should create it with one of the two versions below:
```
app = Flask('yourapplication')
app = Flask(__name__.split('.')[0])

```

Why is that? The application will work even with `__name__`, thanks to how resources are looked up. However it will make debugging more painful. Certain extensions can make assumptions based on the import name of your application. For example the Flask-SQLAlchemy extension will look for the code in your application that triggered an SQL query in debug mode. If the import name is not properly set up, that debugging information is lost. (For example it would only pick up SQL queries in `yourapplication.app` and not `yourapplication.views.frontend`)
Changelog
Added in version 1.0: The `host_matching` and `static_host` parameters were added.
Added in version 1.0: The `subdomain_matching` parameter was added. Subdomain matching needs to be enabled manually now. Setting [`SERVER_NAME`](https://flask.palletsprojects.com/en/stable/config/#SERVER_NAME "SERVER_NAME") does not implicitly enable it.
Added in version 0.11: The `root_path` parameter was added.
Added in version 0.8: The `instance_path` and `instance_relative_config` parameters were added.
Added in version 0.7: The `static_url_path`, `static_folder`, and `template_folder` parameters were added.

Parameters:

  * **import_name** (
  * **static_url_path** (_|__None_) – can be used to specify a different path for the static files on the web. Defaults to the name of the `static_folder` folder.
  * **static_folder** (_|__[__]__|__None_) – The folder with static files that is served at `static_url_path`. Relative to the application `root_path` or an absolute path. Defaults to `'static'`.
  * **static_host** (_|__None_) – the host to use when adding the static route. Defaults to None. Required when using `host_matching=True` with a `static_folder` configured.
  * **host_matching** (`url_map.host_matching` attribute. Defaults to False.
  * **subdomain_matching** ([`SERVER_NAME`](https://flask.palletsprojects.com/en/stable/config/#SERVER_NAME "SERVER_NAME") when matching routes. Defaults to False.
  * **template_folder** (_|__[__]__|__None_) – the folder that contains the templates that should be used by the application. Defaults to `'templates'` folder in the root path of the application.
  * **instance_path** (_|__None_) – An alternative instance path for the application. By default the folder `'instance'` next to the package or module is assumed to be the instance path.
  * **instance_relative_config** (`True` relative filenames for loading the config are assumed to be relative to the instance path instead of the application root.
  * **root_path** (_|__None_) – The path to the root of the application files. This should only be set manually when it can’t be detected automatically, such as for namespace packages.



request_class[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.request_class "Link to this definition")

alias of [`Request`](https://flask.palletsprojects.com/en/stable/api/#flask.Request "flask.wrappers.Request")

response_class[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.response_class "Link to this definition")

alias of [`Response`](https://flask.palletsprojects.com/en/stable/api/#flask.Response "flask.wrappers.Response")

session_interface _:[ SessionInterface](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SessionInterface "flask.sessions.SessionInterface")_ _= <flask.sessions.SecureCookieSessionInterface object>_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.session_interface "Link to this definition")

the session interface to use. By default an instance of [`SecureCookieSessionInterface`](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SecureCookieSessionInterface "flask.sessions.SecureCookieSessionInterface") is used here.
Changelog
Added in version 0.8.

cli _: Group_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.cli "Link to this definition")

The Click command group for registering CLI commands for this object. The commands are available from the `flask` command once the application has been discovered and blueprints have been registered.

get_send_file_max_age(_filename_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.get_send_file_max_age "Link to this definition")

Used by [`send_file()`](https://flask.palletsprojects.com/en/stable/api/#flask.send_file "flask.send_file") to determine the `max_age` cache value for a given file path if it wasn’t passed.
By default, this returns [`SEND_FILE_MAX_AGE_DEFAULT`](https://flask.palletsprojects.com/en/stable/config/#SEND_FILE_MAX_AGE_DEFAULT "SEND_FILE_MAX_AGE_DEFAULT") from the configuration of [`current_app`](https://flask.palletsprojects.com/en/stable/api/#flask.current_app "flask.current_app"). This defaults to `None`, which tells the browser to use conditional requests instead of a timed cache, which is usually preferable.
Note this is a duplicate of the same method in the Flask class.
Changelog
Changed in version 2.0: The default configuration is `None` instead of 12 hours.
Added in version 0.9.

Parameters:

**filename** (_|__None_)

Return type:


send_static_file(_filename_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.send_static_file "Link to this definition")

The view function used to serve files from [`static_folder`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.static_folder "flask.Flask.static_folder"). A route is automatically registered for this view at [`static_url_path`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.static_url_path "flask.Flask.static_url_path") if [`static_folder`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.static_folder "flask.Flask.static_folder") is set.
Note this is a duplicate of the same method in the Flask class.
Changelog
Added in version 0.5.

Parameters:

**filename** (

Return type:

[_Response_](https://flask.palletsprojects.com/en/stable/api/#flask.Response "flask.wrappers.Response")

open_resource(_resource_ , _mode ='rb'_, _encoding =None_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.open_resource "Link to this definition")

Open a resource file relative to [`root_path`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.root_path "flask.Flask.root_path") for reading.
For example, if the file `schema.sql` is next to the file `app.py` where the `Flask` app is defined, it can be opened with:
```
with app.open_resource("schema.sql") as f:
    conn.executescript(f.read())

```


Parameters:

  * **resource** ([`root_path`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.root_path "flask.Flask.root_path").
  * **mode** (`"r"` (or `"rt"`) and `"rb"`.
  * **encoding** (_|__None_) – Open the file with this encoding when opening in text mode. This is ignored when opening in binary mode.



Return type:

Changed in version 3.1: Added the `encoding` parameter.

open_instance_resource(_resource_ , _mode ='rb'_, _encoding ='utf-8'_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.open_instance_resource "Link to this definition")

Open a resource file relative to the application’s instance folder [`instance_path`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.instance_path "flask.Flask.instance_path"). Unlike [`open_resource()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.open_resource "flask.Flask.open_resource"), files in the instance folder can be opened for writing.

Parameters:

  * **resource** ([`instance_path`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.instance_path "flask.Flask.instance_path").
  * **mode** (
  * **encoding** (_|__None_) – Open the file with this encoding when opening in text mode. This is ignored when opening in binary mode.



Return type:

Changed in version 3.1: Added the `encoding` parameter.

create_jinja_environment()[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.create_jinja_environment "Link to this definition")

Create the Jinja environment based on [`jinja_options`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.jinja_options "flask.Flask.jinja_options") and the various Jinja-related methods of the app. Changing [`jinja_options`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.jinja_options "flask.Flask.jinja_options") after this will have no effect. Also adds Flask-related globals and filters to the environment.
Changelog
Changed in version 0.11: `Environment.auto_reload` set in accordance with `TEMPLATES_AUTO_RELOAD` configuration option.
Added in version 0.5.

Return type:

_Environment_

create_url_adapter(_request_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.create_url_adapter "Link to this definition")

Creates a URL adapter for the given request. The URL adapter is created at a point where the request context is not yet set up so the request is passed explicitly.
Changed in version 3.1: If [`SERVER_NAME`](https://flask.palletsprojects.com/en/stable/config/#SERVER_NAME "SERVER_NAME") is set, it does not restrict requests to only that domain, for both `subdomain_matching` and `host_matching`.
Changelog
Changed in version 1.0: [`SERVER_NAME`](https://flask.palletsprojects.com/en/stable/config/#SERVER_NAME "SERVER_NAME") no longer implicitly enables subdomain matching. Use `subdomain_matching` instead.
Changed in version 0.9: This can be called outside a request when the URL adapter is created for an application context.
Added in version 0.6.

Parameters:

**request** ([_Request_](https://flask.palletsprojects.com/en/stable/api/#flask.Request "flask.wrappers.Request") _|__None_)

Return type:

[_MapAdapter_](https://werkzeug.palletsprojects.com/en/stable/routing/#werkzeug.routing.MapAdapter "\(in Werkzeug v3.1.x\)") | None

update_template_context(_context_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.update_template_context "Link to this definition")

Update the template context with some commonly used variables. This injects request, session, config and g into the template context as well as everything template context processors want to inject. Note that the as of Flask 0.6, the original values in the context will not be overridden if a context processor decides to return a value with the same key.

Parameters:

**context** (_[__,__]_) – the context as a dictionary that is updated in place to add extra variables.

Return type:

None

make_shell_context()[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.make_shell_context "Link to this definition")

Returns the shell context for an interactive shell for this application. This runs all the registered shell context processors.
Changelog
Added in version 0.11.

Return type:


run(_host =None_, _port =None_, _debug =None_, _load_dotenv =True_, _** options_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.run "Link to this definition")

Runs the application on a local development server.
Do not use `run()` in a production setting. It is not intended to meet security and performance requirements for a production server. Instead, see [Deploying to Production](https://flask.palletsprojects.com/en/stable/deploying/) for WSGI server recommendations.
If the [`debug`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.debug "flask.Flask.debug") flag is set the server will automatically reload for code changes and show a debugger in case an exception happened.
If you want to run the application in debug mode, but disable the code execution on the interactive debugger, you can pass `use_evalex=False` as parameter. This will keep the debugger’s traceback screen active, but disable code execution.
It is not recommended to use this function for development with automatic reloading as this is badly supported. Instead you should be using the **flask** command line script’s `run` support.
Keep in Mind
Flask will suppress any server error with a generic error page unless it is in debug mode. As such to enable just the interactive debugger without the code reloading, you have to invoke [`run()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.run "flask.Flask.run") with `debug=True` and `use_reloader=False`. Setting `use_debugger` to `True` without being in debug mode won’t catch any exceptions because there won’t be any to catch.

Parameters:

  * **host** (_|__None_) – the hostname to listen on. Set this to `'0.0.0.0'` to have the server available externally as well. Defaults to `'127.0.0.1'` or the host in the `SERVER_NAME` config variable if present.
  * **port** (_|__None_) – the port of the webserver. Defaults to `5000` or the port defined in the `SERVER_NAME` config variable if present.
  * **debug** (_|__None_) – if given, enable or disable debug mode. See [`debug`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.debug "flask.Flask.debug").
  * **load_dotenv** (`.env` and `.flaskenv` files to set environment variables. Will also change the working directory to the directory containing the first file found.
  * **options** ([`werkzeug.serving.run_simple()`](https://werkzeug.palletsprojects.com/en/stable/serving/#werkzeug.serving.run_simple "\(in Werkzeug v3.1.x\)") for more information.



Return type:

None Changelog
Changed in version 1.0: If installed, python-dotenv will be used to load environment variables from `.env` and `.flaskenv` files.
The `FLASK_DEBUG` environment variable will override [`debug`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.debug "flask.Flask.debug").
Threaded mode is enabled by default.
Changed in version 0.10: The default port is now picked from the `SERVER_NAME` variable.

test_client(_use_cookies =True_, _** kwargs_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.test_client "Link to this definition")

Creates a test client for this application. For information about unit testing head over to [Testing Flask Applications](https://flask.palletsprojects.com/en/stable/testing/).
Note that if you are testing for assertions or exceptions in your application code, you must set `app.testing = True` in order for the exceptions to propagate to the test client. Otherwise, the exception will be handled by the application (not visible to the test client) and the only indication of an AssertionError or other exception will be a 500 status code response to the test client. See the [`testing`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.testing "flask.Flask.testing") attribute. For example:
```
app.testing = True
client = app.test_client()

```

The test client can be used in a `with` block to defer the closing down of the context until the end of the `with` block. This is useful if you want to access the context locals for testing:
```
with app.test_client() as c:
    rv = c.get('/?vodka=42')
    assert request.args['vodka'] == '42'

```

Additionally, you may pass optional keyword arguments that will then be passed to the application’s [`test_client_class`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.test_client_class "flask.Flask.test_client_class") constructor. For example:
```
from flask.testing import FlaskClient

class CustomClient(FlaskClient):
    def __init__(self, *args, **kwargs):
        self._authentication = kwargs.pop("authentication")
        super(CustomClient,self).__init__( *args, **kwargs)

app.test_client_class = CustomClient
client = app.test_client(authentication='Basic ....')

```

See [`FlaskClient`](https://flask.palletsprojects.com/en/stable/api/#flask.testing.FlaskClient "flask.testing.FlaskClient") for more information.
Changelog
Changed in version 0.11: Added `**kwargs` to support passing additional keyword arguments to the constructor of [`test_client_class`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.test_client_class "flask.Flask.test_client_class").
Added in version 0.7: The `use_cookies` parameter was added as well as the ability to override the client to be used by setting the [`test_client_class`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.test_client_class "flask.Flask.test_client_class") attribute.
Changed in version 0.4: added support for `with` block usage for the client.

Parameters:

  * **use_cookies** (
  * **kwargs** (_t.Any_)



Return type:

[FlaskClient](https://flask.palletsprojects.com/en/stable/api/#flask.testing.FlaskClient "flask.testing.FlaskClient")

test_cli_runner(_** kwargs_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.test_cli_runner "Link to this definition")

Create a CLI runner for testing CLI commands. See [Running Commands with the CLI Runner](https://flask.palletsprojects.com/en/stable/testing/#testing-cli).
Returns an instance of [`test_cli_runner_class`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.test_cli_runner_class "flask.Flask.test_cli_runner_class"), by default [`FlaskCliRunner`](https://flask.palletsprojects.com/en/stable/api/#flask.testing.FlaskCliRunner "flask.testing.FlaskCliRunner"). The Flask app object is passed as the first argument.
Changelog
Added in version 1.0.

Parameters:

**kwargs** (_t.Any_)

Return type:

[FlaskCliRunner](https://flask.palletsprojects.com/en/stable/api/#flask.testing.FlaskCliRunner "flask.testing.FlaskCliRunner")

handle_http_exception(_e_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.handle_http_exception "Link to this definition")

Handles an HTTP exception. By default this will invoke the registered error handlers and fall back to returning the exception as response.
Changelog
Changed in version 1.0.3: `RoutingException`, used internally for actions such as slash redirects during routing, is not passed to error handlers.
Changed in version 1.0: Exceptions are looked up by code _and_ by MRO, so `HTTPException` subclasses can be handled with a catch-all handler for the base `HTTPException`.
Added in version 0.3.

Parameters:

**e** (_HTTPException_)

Return type:

HTTPException | ft.ResponseReturnValue

handle_user_exception(_e_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.handle_user_exception "Link to this definition")

This method is called whenever an exception occurs that should be handled. A special case is `HTTPException` which is forwarded to the [`handle_http_exception()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.handle_http_exception "flask.Flask.handle_http_exception") method. This function will either return a response value or reraise the exception with the same traceback.
Changelog
Changed in version 1.0: Key errors raised from request data like `form` show the bad key in debug mode rather than a generic bad request message.
Added in version 0.7.

Parameters:

**e** (

Return type:

HTTPException | ft.ResponseReturnValue

handle_exception(_e_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.handle_exception "Link to this definition")

Handle an exception that did not have an error handler associated with it, or that was raised from an error handler. This always causes a 500 `InternalServerError`.
Always sends the [`got_request_exception`](https://flask.palletsprojects.com/en/stable/api/#flask.got_request_exception "flask.got_request_exception") signal.
If [`PROPAGATE_EXCEPTIONS`](https://flask.palletsprojects.com/en/stable/config/#PROPAGATE_EXCEPTIONS "PROPAGATE_EXCEPTIONS") is `True`, such as in debug mode, the error will be re-raised so that the debugger can display it. Otherwise, the original exception is logged, and an [`InternalServerError`](https://werkzeug.palletsprojects.com/en/stable/exceptions/#werkzeug.exceptions.InternalServerError "\(in Werkzeug v3.1.x\)") is returned.
If an error handler is registered for `InternalServerError` or `500`, it will be used. For consistency, the handler will always receive the `InternalServerError`. The original unhandled exception is available as `e.original_exception`.
Changelog
Changed in version 1.1.0: Always passes the `InternalServerError` instance to the handler, setting `original_exception` to the unhandled error.
Changed in version 1.1.0: `after_request` functions and other finalization is done even for the default 500 response when there is no handler.
Added in version 0.3.

Parameters:

**e** (

Return type:

[_Response_](https://flask.palletsprojects.com/en/stable/api/#flask.Response "flask.wrappers.Response")

log_exception(_exc_info_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.log_exception "Link to this definition")

Logs an exception. This is called by [`handle_exception()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.handle_exception "flask.Flask.handle_exception") if debugging is disabled and right before the handler is called. The default implementation logs the exception as error on the [`logger`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.logger "flask.Flask.logger").
Changelog
Added in version 0.8.

Parameters:

**exc_info** (_[__,__,__]__|__[__None_ _,__None_ _,__None_ _]_)

Return type:

None

dispatch_request()[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.dispatch_request "Link to this definition")

Does the request dispatching. Matches the URL and returns the return value of the view or error handler. This does not have to be a response object. In order to convert the return value to a proper response object, call [`make_response()`](https://flask.palletsprojects.com/en/stable/api/#flask.make_response "flask.make_response").
Changelog
Changed in version 0.7: This no longer does the exception handling, this code was moved to the new [`full_dispatch_request()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.full_dispatch_request "flask.Flask.full_dispatch_request").

Return type:

ft.ResponseReturnValue

full_dispatch_request()[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.full_dispatch_request "Link to this definition")

Dispatches the request and on top of that performs request pre and postprocessing as well as HTTP exception catching and error handling.
Changelog
Added in version 0.7.

Return type:

[_Response_](https://flask.palletsprojects.com/en/stable/api/#flask.Response "flask.wrappers.Response")

make_default_options_response()[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.make_default_options_response "Link to this definition")

This method is called to create the default `OPTIONS` response. This can be changed through subclassing to change the default behavior of `OPTIONS` responses.
Changelog
Added in version 0.7.

Return type:

[_Response_](https://flask.palletsprojects.com/en/stable/api/#flask.Response "flask.wrappers.Response")

ensure_sync(_func_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.ensure_sync "Link to this definition")

Ensure that the function is synchronous for WSGI workers. Plain `def` functions are returned as-is. `async def` functions are wrapped to run and wait for the response.
Override this method to change how the app runs async views.
Changelog
Added in version 2.0.

Parameters:
