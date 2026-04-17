## Command Line Interface[¶](https://flask.palletsprojects.com/en/stable/api/#command-line-interface "Link to this heading")

_class_ flask.cli.FlaskGroup(_add_default_commands =True_, _create_app =None_, _add_version_option =True_, _load_dotenv =True_, _set_debug_flag =True_, _** extra_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.cli.FlaskGroup "Link to this definition")

Special subclass of the [`AppGroup`](https://flask.palletsprojects.com/en/stable/api/#flask.cli.AppGroup "flask.cli.AppGroup") group that supports loading more commands from the configured Flask app. Normally a developer does not have to interface with this class but there are some very advanced use cases for which it makes sense to create an instance of this. see [Custom Scripts](https://flask.palletsprojects.com/en/stable/cli/#custom-scripts).

Parameters:

  * **add_default_commands** (
  * **add_version_option** (`--version` option.
  * **create_app** (_t.Callable_ _[__...__,_[_Flask_](https://flask.palletsprojects.com/en/stable/api/#flask.Flask "flask.Flask") _]__|__None_) – an optional callback that is passed the script info and returns the loaded app.
  * **load_dotenv** (`.env` and `.flaskenv` files to set environment variables. Will also change the working directory to the directory containing the first file found.
  * **set_debug_flag** (
  * **extra** (_t.Any_)


Changed in version 3.1: `-e path` takes precedence over default `.env` and `.flaskenv` files.
Changelog
Changed in version 2.2: Added the `-A/--app`, `--debug/--no-debug`, `-e/--env-file` options.
Changed in version 2.2: An app context is pushed when running `app.cli` commands, so `@with_appcontext` is no longer required for those commands.
Changed in version 1.0: If installed, python-dotenv will be used to load environment variables from `.env` and `.flaskenv` files.

get_command(_ctx_ , _name_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.cli.FlaskGroup.get_command "Link to this definition")

Given a context and a command name, this returns a `Command` object if it exists or returns `None`.

Parameters:

  * **ctx** ([_Context_](https://click.palletsprojects.com/en/stable/api/#click.Context "\(in Click v8.3.x\)"))
  * **name** (



Return type:

[_Command_](https://click.palletsprojects.com/en/stable/api/#click.Command "\(in Click v8.3.x\)") | None

list_commands(_ctx_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.cli.FlaskGroup.list_commands "Link to this definition")

Returns a list of subcommand names in the order they should appear.

Parameters:

**ctx** ([_Context_](https://click.palletsprojects.com/en/stable/api/#click.Context "\(in Click v8.3.x\)"))

Return type:


make_context(_info_name_ , _args_ , _parent =None_, _** extra_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.cli.FlaskGroup.make_context "Link to this definition")

This function when given an info name and arguments will kick off the parsing and create a new `Context`. It does not invoke the actual command callback though.
To quickly customize the context class used without overriding this method, set the `context_class` attribute.

Parameters:

  * **info_name** (_|__None_) – the info name for this invocation. Generally this is the most descriptive name for the script or command. For the toplevel script it’s usually the name of the script, for commands below it’s the name of the command.
  * **args** (_[__]_) – the arguments to parse as list of strings.
  * **parent** ([_Context_](https://click.palletsprojects.com/en/stable/api/#click.Context "\(in Click v8.3.x\)") _|__None_) – the parent context if available.
  * **extra** (



Return type:

[_Context_](https://click.palletsprojects.com/en/stable/api/#click.Context "\(in Click v8.3.x\)")
Changed in version 8.0: Added the `context_class` attribute.

_class_ flask.cli.AppGroup(_name =None_, _commands =None_, _invoke_without_command =False_, _no_args_is_help =None_, _subcommand_metavar =None_, _chain =False_, _result_callback =None_, _** kwargs_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.cli.AppGroup "Link to this definition")

This works similar to a regular click [`Group`](https://click.palletsprojects.com/en/stable/api/#click.Group "\(in Click v8.3.x\)") but it changes the behavior of the [`command()`](https://flask.palletsprojects.com/en/stable/api/#flask.cli.AppGroup.command "flask.cli.AppGroup.command") decorator so that it automatically wraps the functions in [`with_appcontext()`](https://flask.palletsprojects.com/en/stable/api/#flask.cli.with_appcontext "flask.cli.with_appcontext").
Not to be confused with [`FlaskGroup`](https://flask.palletsprojects.com/en/stable/api/#flask.cli.FlaskGroup "flask.cli.FlaskGroup").

Parameters:

  * **name** (_|__None_)
  * **commands** (_cabc.MutableMapping_ _[__,__Command_ _]__|__cabc.Sequence_ _[__Command_ _]__|__None_)
  * **invoke_without_command** (
  * **no_args_is_help** (_|__None_)
  * **subcommand_metavar** (_|__None_)
  * **chain** (
  * **result_callback** (_t.Callable_ _[__...__,__t.Any_ _]__|__None_)
  * **kwargs** (_t.Any_)



command(_* args_, _** kwargs_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.cli.AppGroup.command "Link to this definition")

This works exactly like the method of the same name on a regular [`click.Group`](https://click.palletsprojects.com/en/stable/api/#click.Group "\(in Click v8.3.x\)") but it wraps callbacks in [`with_appcontext()`](https://flask.palletsprojects.com/en/stable/api/#flask.cli.with_appcontext "flask.cli.with_appcontext") unless it’s disabled by passing `with_appcontext=False`.

Parameters:

  * **args** (
  * **kwargs** (



Return type:

[_Command_](https://click.palletsprojects.com/en/stable/api/#click.Command "\(in Click v8.3.x\)")]

group(_* args_, _** kwargs_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.cli.AppGroup.group "Link to this definition")

This works exactly like the method of the same name on a regular [`click.Group`](https://click.palletsprojects.com/en/stable/api/#click.Group "\(in Click v8.3.x\)") but it defaults the group class to [`AppGroup`](https://flask.palletsprojects.com/en/stable/api/#flask.cli.AppGroup "flask.cli.AppGroup").

Parameters:

  * **args** (
  * **kwargs** (



Return type:

[_Group_](https://click.palletsprojects.com/en/stable/api/#click.Group "\(in Click v8.3.x\)")]

_class_ flask.cli.ScriptInfo(_app_import_path =None_, _create_app =None_, _set_debug_flag =True_, _load_dotenv_defaults =True_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.cli.ScriptInfo "Link to this definition")

Helper object to deal with Flask applications. This is usually not necessary to interface with as it’s used internally in the dispatching to click. In future versions of Flask this object will most likely play a bigger role. Typically it’s created automatically by the [`FlaskGroup`](https://flask.palletsprojects.com/en/stable/api/#flask.cli.FlaskGroup "flask.cli.FlaskGroup") but you can also manually create it and pass it onwards as click object.
Changed in version 3.1: Added the `load_dotenv_defaults` parameter and attribute.

Parameters:

  * **app_import_path** (_|__None_)
  * **create_app** (_t.Callable_ _[__...__,_[_Flask_](https://flask.palletsprojects.com/en/stable/api/#flask.Flask "flask.Flask") _]__|__None_)
  * **set_debug_flag** (
  * **load_dotenv_defaults** (



app_import_path[¶](https://flask.palletsprojects.com/en/stable/api/#flask.cli.ScriptInfo.app_import_path "Link to this definition")

Optionally the import path for the Flask application.

create_app[¶](https://flask.palletsprojects.com/en/stable/api/#flask.cli.ScriptInfo.create_app "Link to this definition")

Optionally a function that is passed the script info to create the instance of the application.

data _:[t.Any,t.Any]_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.cli.ScriptInfo.data "Link to this definition")

A dictionary with arbitrary data that can be associated with this script info.

load_dotenv_defaults[¶](https://flask.palletsprojects.com/en/stable/api/#flask.cli.ScriptInfo.load_dotenv_defaults "Link to this definition")

Whether default `.flaskenv` and `.env` files should be loaded.
`ScriptInfo` doesn’t load anything, this is for reference when doing the load elsewhere during processing.
Added in version 3.1.

load_app()[¶](https://flask.palletsprojects.com/en/stable/api/#flask.cli.ScriptInfo.load_app "Link to this definition")

Loads the Flask app (if not yet loaded) and returns it. Calling this multiple times will just result in the already loaded app to be returned.

Return type:

[Flask](https://flask.palletsprojects.com/en/stable/api/#flask.Flask "flask.Flask")

flask.cli.load_dotenv(_path =None_, _load_defaults =True_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.cli.load_dotenv "Link to this definition")

Load “dotenv” files to set environment variables. A given path takes precedence over `.env`, which takes precedence over `.flaskenv`. After loading and combining these files, values are only set if the key is not already set in `os.environ`.
This is a no-op if

Parameters:

  * **path** (_|__[__]__|__None_) – Load the file at this location.
  * **load_defaults** (`.flaskenv` and `.env` files.



Returns:

`True` if at least one env var was loaded.

Return type:

Changed in version 3.1: Added the `load_defaults` parameter. A given path takes precedence over default files.
Changelog
Changed in version 2.0: The current directory is not changed to the location of the loaded file.
Changed in version 2.0: When loading the env files, set the default encoding to UTF-8.
Changed in version 1.1.0: Returns `False` when python-dotenv is not installed, or when the given path isn’t a file.
Added in version 1.0.

flask.cli.with_appcontext(_f_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.cli.with_appcontext "Link to this definition")

Wraps a callback so that it’s guaranteed to be executed with the script’s application context.
Custom commands (and their options) registered under `app.cli` or `blueprint.cli` will always have an app context available, this decorator is not required in that case.
Changelog
Changed in version 2.2: The app context is active for subcommands as well as the decorated callback. The app context is always available to `app.cli` command and parameter callbacks.

Parameters:

**f** (_F_)

Return type:

_F_

flask.cli.pass_script_info(_f_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.cli.pass_script_info "Link to this definition")

Marks a function so that an instance of [`ScriptInfo`](https://flask.palletsprojects.com/en/stable/api/#flask.cli.ScriptInfo "flask.cli.ScriptInfo") is passed as first argument to the click callback.

Parameters:

**f** (_t.Callable_ _[__te.Concatenate_ _[__T_ _,__P_ _]__,__R_ _]_)

Return type:

t.Callable[P, R]

flask.cli.run_command _= <Command run>_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.cli.run_command "Link to this definition")

Run a local development server.
This server is for development purposes only. It does not provide the stability, security, or performance of production WSGI servers.
The reloader and debugger are enabled by default with the ‘–debug’ option.

Parameters:

  * **args** (_t.Any_)
  * **kwargs** (_t.Any_)



Return type:

t.Any

flask.cli.shell_command _= <Command shell>_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.cli.shell_command "Link to this definition")

Run an interactive Python shell in the context of a given Flask application. The application will populate the default namespace of this shell according to its configuration.
This is useful for executing small snippets of management code without having to manually configure the application.

Parameters:

  * **args** (_t.Any_)
  * **kwargs** (_t.Any_)



Return type:

t.Any
[ ![Logo of Flask](https://flask.palletsprojects.com/en/stable/_static/flask-logo.svg) ](https://flask.palletsprojects.com/en/stable/)
### Contents
  * [API](https://flask.palletsprojects.com/en/stable/api/)
    * [Application Object](https://flask.palletsprojects.com/en/stable/api/#application-object)
      * [`Flask`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask)
        * [`Flask.request_class`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.request_class)
        * [`Flask.response_class`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.response_class)
        * [`Flask.session_interface`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.session_interface)
        * [`Flask.cli`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.cli)
        * [`Flask.get_send_file_max_age()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.get_send_file_max_age)
        * [`Flask.send_static_file()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.send_static_file)
        * [`Flask.open_resource()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.open_resource)
        * [`Flask.open_instance_resource()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.open_instance_resource)
        * [`Flask.create_jinja_environment()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.create_jinja_environment)
        * [`Flask.create_url_adapter()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.create_url_adapter)
        * [`Flask.update_template_context()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.update_template_context)
        * [`Flask.make_shell_context()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.make_shell_context)
        * [`Flask.run()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.run)
        * [`Flask.test_client()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.test_client)
        * [`Flask.test_cli_runner()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.test_cli_runner)
        * [`Flask.handle_http_exception()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.handle_http_exception)
        * [`Flask.handle_user_exception()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.handle_user_exception)
        * [`Flask.handle_exception()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.handle_exception)
        * [`Flask.log_exception()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.log_exception)
        * [`Flask.dispatch_request()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.dispatch_request)
        * [`Flask.full_dispatch_request()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.full_dispatch_request)
        * [`Flask.make_default_options_response()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.make_default_options_response)
        * [`Flask.ensure_sync()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.ensure_sync)
        * [`Flask.async_to_sync()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.async_to_sync)
        * [`Flask.url_for()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.url_for)
        * [`Flask.make_response()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.make_response)
        * [`Flask.preprocess_request()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.preprocess_request)
        * [`Flask.process_response()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.process_response)
        * [`Flask.do_teardown_request()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.do_teardown_request)
        * [`Flask.do_teardown_appcontext()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.do_teardown_appcontext)
        * [`Flask.app_context()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.app_context)
        * [`Flask.request_context()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.request_context)
        * [`Flask.test_request_context()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.test_request_context)
        * [`Flask.wsgi_app()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.wsgi_app)
        * [`Flask.aborter_class`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.aborter_class)
        * [`Flask.add_template_filter()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.add_template_filter)
        * [`Flask.add_template_global()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.add_template_global)
        * [`Flask.add_template_test()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.add_template_test)
        * [`Flask.add_url_rule()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.add_url_rule)
        * [`Flask.after_request()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.after_request)
        * [`Flask.app_ctx_globals_class`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.app_ctx_globals_class)
        * [`Flask.auto_find_instance_path()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.auto_find_instance_path)
        * [`Flask.before_request()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.before_request)
        * [`Flask.config_class`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.config_class)
        * [`Flask.context_processor()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.context_processor)
        * [`Flask.create_global_jinja_loader()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.create_global_jinja_loader)
        * [`Flask.debug`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.debug)
        * [`Flask.delete()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.delete)
        * [`Flask.endpoint()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.endpoint)
        * [`Flask.errorhandler()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.errorhandler)
        * [`Flask.get()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.get)
        * [`Flask.handle_url_build_error()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.handle_url_build_error)
        * [`Flask.has_static_folder`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.has_static_folder)
        * [`Flask.inject_url_defaults()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.inject_url_defaults)
        * [`Flask.iter_blueprints()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.iter_blueprints)
        * [`Flask.jinja_env`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.jinja_env)
        * [`Flask.jinja_environment`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.jinja_environment)
        * [`Flask.jinja_loader`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.jinja_loader)
        * [`Flask.jinja_options`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.jinja_options)
        * [`Flask.json_provider_class`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.json_provider_class)
        * [`Flask.logger`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.logger)
        * [`Flask.make_aborter()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.make_aborter)
        * [`Flask.make_config()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.make_config)
        * [`Flask.name`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.name)
        * [`Flask.patch()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.patch)
        * [`Flask.permanent_session_lifetime`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.permanent_session_lifetime)
        * [`Flask.post()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.post)
        * [`Flask.put()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.put)
        * [`Flask.redirect()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.redirect)
        * [`Flask.register_blueprint()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.register_blueprint)
        * [`Flask.register_error_handler()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.register_error_handler)
        * [`Flask.route()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.route)
        * [`Flask.secret_key`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.secret_key)
        * [`Flask.select_jinja_autoescape()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.select_jinja_autoescape)
        * [`Flask.shell_context_processor()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.shell_context_processor)
        * [`Flask.should_ignore_error()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.should_ignore_error)
        * [`Flask.static_folder`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.static_folder)
        * [`Flask.static_url_path`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.static_url_path)
        * [`Flask.teardown_appcontext()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.teardown_appcontext)
        * [`Flask.teardown_request()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.teardown_request)
        * [`Flask.template_filter()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.template_filter)
        * [`Flask.template_global()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.template_global)
        * [`Flask.template_test()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.template_test)
        * [`Flask.test_cli_runner_class`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.test_cli_runner_class)
        * [`Flask.test_client_class`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.test_client_class)
        * [`Flask.testing`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.testing)
        * [`Flask.trap_http_exception()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.trap_http_exception)
        * [`Flask.url_defaults()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.url_defaults)
        * [`Flask.url_map_class`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.url_map_class)
        * [`Flask.url_rule_class`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.url_rule_class)
        * [`Flask.url_value_preprocessor()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.url_value_preprocessor)
        * [`Flask.instance_path`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.instance_path)
        * [`Flask.config`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.config)
        * [`Flask.aborter`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.aborter)
        * [`Flask.json`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.json)
        * [`Flask.url_build_error_handlers`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.url_build_error_handlers)
        * [`Flask.teardown_appcontext_funcs`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.teardown_appcontext_funcs)
        * [`Flask.shell_context_processors`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.shell_context_processors)
        * [`Flask.blueprints`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.blueprints)
        * [`Flask.extensions`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.extensions)
        * [`Flask.url_map`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.url_map)
        * [`Flask.import_name`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.import_name)
        * [`Flask.template_folder`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.template_folder)
        * [`Flask.root_path`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.root_path)
        * [`Flask.view_functions`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.view_functions)
        * [`Flask.error_handler_spec`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.error_handler_spec)
        * [`Flask.before_request_funcs`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.before_request_funcs)
        * [`Flask.after_request_funcs`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.after_request_funcs)
        * [`Flask.teardown_request_funcs`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.teardown_request_funcs)
        * [`Flask.template_context_processors`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.template_context_processors)
        * [`Flask.url_value_preprocessors`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.url_value_preprocessors)
        * [`Flask.url_default_functions`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.url_default_functions)
    * [Blueprint Objects](https://flask.palletsprojects.com/en/stable/api/#blueprint-objects)
      * [`Blueprint`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint)
