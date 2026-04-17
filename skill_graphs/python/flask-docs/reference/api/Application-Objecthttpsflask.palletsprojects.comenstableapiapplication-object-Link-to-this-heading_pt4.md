Added in version 0.8.

Parameters:

**e** (

Return type:


url_defaults(_f_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.url_defaults "Link to this definition")

Callback function for URL defaults for all view functions of the application. It’s called with the endpoint and values and should update the values passed in place.
This is available on both app and blueprint objects. When used on an app, this is called for every request. When used on a blueprint, this is called for requests that the blueprint handles. To register with a blueprint and affect every request, use [`Blueprint.app_url_defaults()`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.app_url_defaults "flask.Blueprint.app_url_defaults").

Parameters:

**f** (_T_url_defaults_)

Return type:

_T_url_defaults_

url_map_class[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.url_map_class "Link to this definition")

alias of [`Map`](https://werkzeug.palletsprojects.com/en/stable/routing/#werkzeug.routing.Map "\(in Werkzeug v3.1.x\)")

url_rule_class[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.url_rule_class "Link to this definition")

alias of [`Rule`](https://werkzeug.palletsprojects.com/en/stable/routing/#werkzeug.routing.Rule "\(in Werkzeug v3.1.x\)")

url_value_preprocessor(_f_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.url_value_preprocessor "Link to this definition")

Register a URL value preprocessor function for all view functions in the application. These functions will be called before the [`before_request()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.before_request "flask.Flask.before_request") functions.
The function can modify the values captured from the matched url before they are passed to the view. For example, this can be used to pop a common language code value and place it in `g` rather than pass it to every view.
The function is passed the endpoint name and values dict. The return value is ignored.
This is available on both app and blueprint objects. When used on an app, this is called for every request. When used on a blueprint, this is called for requests that the blueprint handles. To register with a blueprint and affect every request, use [`Blueprint.app_url_value_preprocessor()`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.app_url_value_preprocessor "flask.Blueprint.app_url_value_preprocessor").

Parameters:

**f** (_T_url_value_preprocessor_)

Return type:

_T_url_value_preprocessor_

instance_path[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.instance_path "Link to this definition")

Holds the path to the instance folder.
Changelog
Added in version 0.8.

config[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.config "Link to this definition")

The configuration dictionary as [`Config`](https://flask.palletsprojects.com/en/stable/api/#flask.Config "flask.Config"). This behaves exactly like a regular dictionary but supports additional methods to load a config from files.

aborter[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.aborter "Link to this definition")

An instance of [`aborter_class`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.aborter_class "flask.Flask.aborter_class") created by [`make_aborter()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.make_aborter "flask.Flask.make_aborter"). This is called by [`flask.abort()`](https://flask.palletsprojects.com/en/stable/api/#flask.abort "flask.abort") to raise HTTP errors, and can be called directly as well.
Changelog
Added in version 2.2: Moved from `flask.abort`, which calls this object.

json _:[ JSONProvider](https://flask.palletsprojects.com/en/stable/api/#flask.json.provider.JSONProvider "flask.json.provider.JSONProvider")_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.json "Link to this definition")

Provides access to JSON methods. Functions in `flask.json` will call methods on this provider when the application context is active. Used for handling JSON requests and responses.
An instance of [`json_provider_class`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.json_provider_class "flask.Flask.json_provider_class"). Can be customized by changing that attribute on a subclass, or by assigning to this attribute afterwards.
The default, [`DefaultJSONProvider`](https://flask.palletsprojects.com/en/stable/api/#flask.json.provider.DefaultJSONProvider "flask.json.provider.DefaultJSONProvider"), uses Python’s built-in
Changelog
Added in version 2.2.

url_build_error_handlers _:[t.Callable[[,,[,t.Any]],]]_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.url_build_error_handlers "Link to this definition")

A list of functions that are called by [`handle_url_build_error()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.handle_url_build_error "flask.Flask.handle_url_build_error") when [`url_for()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.url_for "flask.Flask.url_for") raises a `BuildError`. Each function is called with `error`, `endpoint` and `values`. If a function returns `None` or raises a `BuildError`, it is skipped. Otherwise, its return value is returned by `url_for`.
Changelog
Added in version 0.9.

teardown_appcontext_funcs _:[ft.TeardownCallable]_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.teardown_appcontext_funcs "Link to this definition")

A list of functions that are called when the application context is destroyed. Since the application context is also torn down if the request ends this is the place to store code that disconnects from databases.
Changelog
Added in version 0.9.

shell_context_processors _:[ft.ShellContextProcessorCallable]_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.shell_context_processors "Link to this definition")

A list of shell context processor functions that should be run when a shell context is created.
Changelog
Added in version 0.11.

blueprints _:[,[Blueprint](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint "flask.Blueprint")]_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.blueprints "Link to this definition")

Maps registered blueprint names to blueprint objects. The dict retains the order the blueprints were registered in. Blueprints can be registered multiple times, this dict does not track how often they were attached.
Changelog
Added in version 0.7.

extensions _:[,t.Any]_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.extensions "Link to this definition")

a place where extensions can store application specific state. For example this is where an extension could store database engines and similar things.
The key must match the name of the extension module. For example in case of a “Flask-Foo” extension in `flask_foo`, the key would be `'foo'`.
Changelog
Added in version 0.7.

url_map[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.url_map "Link to this definition")

The [`Map`](https://werkzeug.palletsprojects.com/en/stable/routing/#werkzeug.routing.Map "\(in Werkzeug v3.1.x\)") for this instance. You can use this to change the routing converters after the class was created but before any routes are connected. Example:
```
from werkzeug.routing import BaseConverter

class ListConverter(BaseConverter):
    def to_python(self, value):
        return value.split(',')
    def to_url(self, values):
        return ','.join(super(ListConverter, self).to_url(value)
                        for value in values)

app = Flask(__name__)
app.url_map.converters['list'] = ListConverter

```


import_name[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.import_name "Link to this definition")

The name of the package or module that this object belongs to. Do not change this once it is set by the constructor.

template_folder[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.template_folder "Link to this definition")

The path to the templates folder, relative to [`root_path`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.root_path "flask.Flask.root_path"), to add to the template loader. `None` if templates should not be added.

root_path[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.root_path "Link to this definition")

Absolute path to the package on the filesystem. Used to look up resources contained in the package.

view_functions _:[,ft.RouteCallable]_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.view_functions "Link to this definition")

A dictionary mapping endpoint names to view functions.
To register a view function, use the [`route()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.route "flask.Flask.route") decorator.
This data structure is internal. It should not be modified directly and its format may change at any time.

error_handler_spec _:[ft.AppOrBlueprintKey,[|,[[],ft.ErrorHandlerCallable]]]_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.error_handler_spec "Link to this definition")

A data structure of registered error handlers, in the format `{scope: {code: {class: handler}}}`. The `scope` key is the name of a blueprint the handlers are active for, or `None` for all requests. The `code` key is the HTTP status code for `HTTPException`, or `None` for other exceptions. The innermost dictionary maps exception classes to handler functions.
To register an error handler, use the [`errorhandler()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.errorhandler "flask.Flask.errorhandler") decorator.
This data structure is internal. It should not be modified directly and its format may change at any time.

before_request_funcs _:[ft.AppOrBlueprintKey,[ft.BeforeRequestCallable]]_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.before_request_funcs "Link to this definition")

A data structure of functions to call at the beginning of each request, in the format `{scope: [functions]}`. The `scope` key is the name of a blueprint the functions are active for, or `None` for all requests.
To register a function, use the [`before_request()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.before_request "flask.Flask.before_request") decorator.
This data structure is internal. It should not be modified directly and its format may change at any time.

after_request_funcs _:[ft.AppOrBlueprintKey,[ft.AfterRequestCallable[t.Any]]]_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.after_request_funcs "Link to this definition")

A data structure of functions to call at the end of each request, in the format `{scope: [functions]}`. The `scope` key is the name of a blueprint the functions are active for, or `None` for all requests.
To register a function, use the [`after_request()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.after_request "flask.Flask.after_request") decorator.
This data structure is internal. It should not be modified directly and its format may change at any time.

teardown_request_funcs _:[ft.AppOrBlueprintKey,[ft.TeardownCallable]]_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.teardown_request_funcs "Link to this definition")

A data structure of functions to call at the end of each request even if an exception is raised, in the format `{scope: [functions]}`. The `scope` key is the name of a blueprint the functions are active for, or `None` for all requests.
To register a function, use the [`teardown_request()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.teardown_request "flask.Flask.teardown_request") decorator.
This data structure is internal. It should not be modified directly and its format may change at any time.

template_context_processors _:[ft.AppOrBlueprintKey,[ft.TemplateContextProcessorCallable]]_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.template_context_processors "Link to this definition")

A data structure of functions to call to pass extra context values when rendering templates, in the format `{scope: [functions]}`. The `scope` key is the name of a blueprint the functions are active for, or `None` for all requests.
To register a function, use the [`context_processor()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.context_processor "flask.Flask.context_processor") decorator.
This data structure is internal. It should not be modified directly and its format may change at any time.

url_value_preprocessors _:[ft.AppOrBlueprintKey,[ft.URLValuePreprocessorCallable]]_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.url_value_preprocessors "Link to this definition")

A data structure of functions to call to modify the keyword arguments passed to the view function, in the format `{scope: [functions]}`. The `scope` key is the name of a blueprint the functions are active for, or `None` for all requests.
To register a function, use the [`url_value_preprocessor()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.url_value_preprocessor "flask.Flask.url_value_preprocessor") decorator.
This data structure is internal. It should not be modified directly and its format may change at any time.

url_default_functions _:[ft.AppOrBlueprintKey,[ft.URLDefaultCallable]]_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.url_default_functions "Link to this definition")

A data structure of functions to call to modify the keyword arguments when generating URLs, in the format `{scope: [functions]}`. The `scope` key is the name of a blueprint the functions are active for, or `None` for all requests.
To register a function, use the [`url_defaults()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.url_defaults "flask.Flask.url_defaults") decorator.
This data structure is internal. It should not be modified directly and its format may change at any time.
