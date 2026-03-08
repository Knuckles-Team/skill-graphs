## Configuration[¶](https://flask.palletsprojects.com/en/stable/api/#configuration "Link to this heading")

_class_ flask.Config(_root_path_ , _defaults =None_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Config "Link to this definition")

Works exactly like a dict but provides ways to fill it from files or special dictionaries. There are two common patterns to populate the config.
Either you can fill the config from a config file:
```
app.config.from_pyfile('yourconfig.cfg')

```

Or alternatively you can define the configuration options in the module that calls [`from_object()`](https://flask.palletsprojects.com/en/stable/api/#flask.Config.from_object "flask.Config.from_object") or provide an import path to a module that should be loaded. It is also possible to tell it to use the same module and with that provide the configuration values just before the call:
```
DEBUG = True
SECRET_KEY = 'development key'
app.config.from_object(__name__)

```

In both cases (loading from any Python file or loading from modules), only uppercase keys are added to the config. This makes it possible to use lowercase values in the config file for temporary values that are not added to the config or to define the config keys in the same file that implements the application.
Probably the most interesting way to load configurations is from an environment variable pointing to a file:
```
app.config.from_envvar('YOURAPPLICATION_SETTINGS')

```

In this case before launching the application you have to set this environment variable to the file you want to use. On Linux and OS X use the export statement:
```
export YOURAPPLICATION_SETTINGS='/path/to/config/file'

```

On windows use `set` instead.

Parameters:

  * **root_path** (_|__[__]_) – path to which files are read relative from. When the config object is created by the application, this is the application’s [`root_path`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.root_path "flask.Flask.root_path").
  * **defaults** (_[__,__t.Any_ _]__|__None_) – an optional dictionary of default values



from_envvar(_variable_name_ , _silent =False_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Config.from_envvar "Link to this definition")

Loads a configuration from an environment variable pointing to a configuration file. This is basically just a shortcut with nicer error messages for this line of code:
```
app.config.from_pyfile(os.environ['YOURAPPLICATION_SETTINGS'])

```


Parameters:

  * **variable_name** (
  * **silent** (`True` if you want silent failure for missing files.



Returns:

`True` if the file was loaded successfully.

Return type:


from_prefixed_env(_prefix ='FLASK'_, _*_ , _loads =json.loads_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Config.from_prefixed_env "Link to this definition")

Load any environment variables that start with `FLASK_`, dropping the prefix from the env key for the config key. Values are passed through a loading function to attempt to convert them to more specific types than strings.
Keys are loaded in
The default loading function attempts to parse values as any valid JSON type, including dicts and lists.
Specific items in nested dicts can be set by separating the keys with double underscores (`__`). If an intermediate key doesn’t exist, it will be initialized to an empty dict.

Parameters:

  * **prefix** (`_`).
  * **loads** (_[__[__]__,__]_) – Pass each string value to this function and use the returned value as the config value. If any error is raised it is ignored and the value remains a string. The default is [`json.loads()`](https://flask.palletsprojects.com/en/stable/api/#flask.json.loads "flask.json.loads").



Return type:
Changelog
Added in version 2.1.

from_pyfile(_filename_ , _silent =False_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Config.from_pyfile "Link to this definition")

Updates the values in the config from a Python file. This function behaves as if the file was imported as module with the [`from_object()`](https://flask.palletsprojects.com/en/stable/api/#flask.Config.from_object "flask.Config.from_object") function.

Parameters:

  * **filename** (_|__[__]_) – the filename of the config. This can either be an absolute filename or a filename relative to the root path.
  * **silent** (`True` if you want silent failure for missing files.



Returns:

`True` if the file was loaded successfully.

Return type:
Changelog
Added in version 0.7: `silent` parameter.

from_object(_obj_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Config.from_object "Link to this definition")

Updates the values from the given object. An object can be of one of the following two types:
  * a string: in this case the object with that name will be imported
  * an actual object reference: that object is used directly


Objects are usually either modules or classes. [`from_object()`](https://flask.palletsprojects.com/en/stable/api/#flask.Config.from_object "flask.Config.from_object") loads only the uppercase attributes of the module/class. A `dict` object will not work with [`from_object()`](https://flask.palletsprojects.com/en/stable/api/#flask.Config.from_object "flask.Config.from_object") because the keys of a `dict` are not attributes of the `dict` class.
Example of module-based configuration:
```
app.config.from_object('yourapplication.default_config')
from yourapplication import default_config
app.config.from_object(default_config)

```

Nothing is done to the object before loading. If the object is a class and has `@property` attributes, it needs to be instantiated before being passed to this method.
You should not use this function to load the actual configuration but rather configuration defaults. The actual config should be loaded with [`from_pyfile()`](https://flask.palletsprojects.com/en/stable/api/#flask.Config.from_pyfile "flask.Config.from_pyfile") and ideally from a location not within the package because the package might be installed system wide.
See [Development / Production](https://flask.palletsprojects.com/en/stable/config/#config-dev-prod) for an example of class-based configuration using [`from_object()`](https://flask.palletsprojects.com/en/stable/api/#flask.Config.from_object "flask.Config.from_object").

Parameters:

**obj** (_|_

Return type:

None

from_file(_filename_ , _load_ , _silent =False_, _text =True_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Config.from_file "Link to this definition")

Update the values in the config from a file that is loaded using the `load` parameter. The loaded data is passed to the [`from_mapping()`](https://flask.palletsprojects.com/en/stable/api/#flask.Config.from_mapping "flask.Config.from_mapping") method.
```
import json
app.config.from_file("config.json", load=json.load)

import tomllib
app.config.from_file("config.toml", load=tomllib.load, text=False)

```


Parameters:

  * **filename** (_|__[__]_) – The path to the data file. This can be an absolute path or relative to the config root path.
  * **load** (`Callable[[Reader], Mapping]` where `Reader` implements a `read` method.) – A callable that takes a file handle and returns a mapping of loaded data from the file.
  * **silent** (
  * **text** (



Returns:

`True` if the file was loaded successfully.

Return type:
Changelog
Changed in version 2.3: The `text` parameter was added.
Added in version 2.0.

from_mapping(_mapping =None_, _** kwargs_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Config.from_mapping "Link to this definition")

Updates the config like `update()` ignoring items with non-upper keys.

Returns:

Always returns `True`.

Parameters:

  * **mapping** (_[__,__]__|__None_)
  * **kwargs** (



Return type:
Changelog
Added in version 0.11.

get_namespace(_namespace_ , _lowercase =True_, _trim_namespace =True_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Config.get_namespace "Link to this definition")

Returns a dictionary containing a subset of configuration options that match the specified namespace/prefix. Example usage:
```
app.config['IMAGE_STORE_TYPE'] = 'fs'
app.config['IMAGE_STORE_PATH'] = '/var/app/images'
app.config['IMAGE_STORE_BASE_URL'] = 'http://img.website.com'
image_store_config = app.config.get_namespace('IMAGE_STORE_')

```

The resulting dictionary `image_store_config` would look like:
```
{
    'type': 'fs',
    'path': '/var/app/images',
    'base_url': 'http://img.website.com'
}

```

This is often useful when configuration options map directly to keyword arguments in functions or class constructors.

Parameters:

  * **namespace** (
  * **lowercase** (
  * **trim_namespace** (



Return type:
Changelog
Added in version 0.11.
