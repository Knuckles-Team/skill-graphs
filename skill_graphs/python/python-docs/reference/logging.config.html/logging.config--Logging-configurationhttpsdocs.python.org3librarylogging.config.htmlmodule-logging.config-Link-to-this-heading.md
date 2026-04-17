#  `logging.config` — Logging configuration[¶](https://docs.python.org/3/library/logging.config.html#module-logging.config "Link to this heading")
**Source code:**
Important
This page contains only reference information. For tutorials, please see
  * [Basic Tutorial](https://docs.python.org/3/howto/logging.html#logging-basic-tutorial)
  * [Advanced Tutorial](https://docs.python.org/3/howto/logging.html#logging-advanced-tutorial)
  * [Logging Cookbook](https://docs.python.org/3/howto/logging-cookbook.html#logging-cookbook)


* * *
This section describes the API for configuring the logging module.
## Configuration functions[¶](https://docs.python.org/3/library/logging.config.html#configuration-functions "Link to this heading")
The following functions configure the logging module. They are located in the `logging.config` module. Their use is optional — you can configure the logging module using these functions or by making calls to the main API (defined in [`logging`](https://docs.python.org/3/library/logging.html#module-logging "logging: Flexible event logging system for applications.") itself) and defining handlers which are declared either in `logging` or [`logging.handlers`](https://docs.python.org/3/library/logging.handlers.html#module-logging.handlers "logging.handlers: Handlers for the logging module.").

logging.config.dictConfig(_config_)[¶](https://docs.python.org/3/library/logging.config.html#logging.config.dictConfig "Link to this definition")

Takes the logging configuration from a dictionary. The contents of this dictionary are described in [Configuration dictionary schema](https://docs.python.org/3/library/logging.config.html#logging-config-dictschema) below.
If an error is encountered during configuration, this function will raise a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError"), [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError"), [`AttributeError`](https://docs.python.org/3/library/exceptions.html#AttributeError "AttributeError") or [`ImportError`](https://docs.python.org/3/library/exceptions.html#ImportError "ImportError") with a suitably descriptive message. The following is a (possibly incomplete) list of conditions which will raise an error:
  * A `level` which is not a string or which is a string not corresponding to an actual logging level.
  * A `propagate` value which is not a boolean.
  * An id which does not have a corresponding destination.
  * A non-existent handler id found during an incremental call.
  * An invalid logger name.
  * Inability to resolve to an internal or external object.


Parsing is performed by the `DictConfigurator` class, whose constructor is passed the dictionary used for configuration, and has a `configure()` method. The `logging.config` module has a callable attribute `dictConfigClass` which is initially set to `DictConfigurator`. You can replace the value of `dictConfigClass` with a suitable implementation of your own.
`dictConfig()` calls `dictConfigClass` passing the specified dictionary, and then calls the `configure()` method on the returned object to put the configuration into effect:
Copy```
def dictConfig(config):
    dictConfigClass(config).configure()

```

For example, a subclass of `DictConfigurator` could call `DictConfigurator.__init__()` in its own `__init__()`, then set up custom prefixes which would be usable in the subsequent `configure()` call. `dictConfigClass` would be bound to this new subclass, and then `dictConfig()` could be called exactly as in the default, uncustomized state.
Added in version 3.2.

logging.config.fileConfig(_fname_ , _defaults =None_, _disable_existing_loggers =True_, _encoding =None_)[¶](https://docs.python.org/3/library/logging.config.html#logging.config.fileConfig "Link to this definition")

Reads the logging configuration from a [`configparser`](https://docs.python.org/3/library/configparser.html#module-configparser "configparser: Configuration file parser.")-format file. The format of the file should be as described in [Configuration file format](https://docs.python.org/3/library/logging.config.html#logging-config-fileformat). This function can be called several times from an application, allowing an end user to select from various pre-canned configurations (if the developer provides a mechanism to present the choices and load the chosen configuration).
It will raise [`FileNotFoundError`](https://docs.python.org/3/library/exceptions.html#FileNotFoundError "FileNotFoundError") if the file doesn’t exist and [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError") if the file is invalid or empty.

Parameters:

  * **fname** – A filename, or a file-like object, or an instance derived from [`RawConfigParser`](https://docs.python.org/3/library/configparser.html#configparser.RawConfigParser "configparser.RawConfigParser"). If a `RawConfigParser`-derived instance is passed, it is used as is. Otherwise, a [`ConfigParser`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser "configparser.ConfigParser") is instantiated, and the configuration read by it from the object passed in `fname`. If that has a [`readline()`](https://docs.python.org/3/library/readline.html#module-readline "readline: GNU readline support for Python.") method, it is assumed to be a file-like object and read using [`read_file()`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.read_file "configparser.ConfigParser.read_file"); otherwise, it is assumed to be a filename and passed to [`read()`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.read "configparser.ConfigParser.read").
  * **defaults** – Defaults to be passed to the `ConfigParser` can be specified in this argument.
  * **disable_existing_loggers** – If specified as `False`, loggers which exist when this call is made are left enabled. The default is `True` because this enables old behaviour in a backward-compatible way. This behaviour is to disable any existing non-root loggers unless they or their ancestors are explicitly named in the logging configuration.
  * **encoding** – The encoding used to open file when _fname_ is filename.


Changed in version 3.4: An instance of a subclass of [`RawConfigParser`](https://docs.python.org/3/library/configparser.html#configparser.RawConfigParser "configparser.RawConfigParser") is now accepted as a value for `fname`. This facilitates:
>   * Use of a configuration file where logging configuration is just part of the overall application configuration.
>   * Use of a configuration read from a file, and then modified by the using application (e.g. based on command-line parameters or other aspects of the runtime environment) before being passed to `fileConfig`.
>

Changed in version 3.10: Added the _encoding_ parameter.
Changed in version 3.12: An exception will be thrown if the provided file doesn’t exist or is invalid or empty.

logging.config.listen(_port =DEFAULT_LOGGING_CONFIG_PORT_, _verify =None_)[¶](https://docs.python.org/3/library/logging.config.html#logging.config.listen "Link to this definition")

Starts up a socket server on the specified port, and listens for new configurations. If no port is specified, the module’s default `DEFAULT_LOGGING_CONFIG_PORT` is used. Logging configurations will be sent as a file suitable for processing by [`dictConfig()`](https://docs.python.org/3/library/logging.config.html#logging.config.dictConfig "logging.config.dictConfig") or [`fileConfig()`](https://docs.python.org/3/library/logging.config.html#logging.config.fileConfig "logging.config.fileConfig"). Returns a [`Thread`](https://docs.python.org/3/library/threading.html#threading.Thread "threading.Thread") instance on which you can call [`start()`](https://docs.python.org/3/library/threading.html#threading.Thread.start "threading.Thread.start") to start the server, and which you can [`join()`](https://docs.python.org/3/library/threading.html#threading.Thread.join "threading.Thread.join") when appropriate. To stop the server, call [`stopListening()`](https://docs.python.org/3/library/logging.config.html#logging.config.stopListening "logging.config.stopListening").
The `verify` argument, if specified, should be a callable which should verify whether bytes received across the socket are valid and should be processed. This could be done by encrypting and/or signing what is sent across the socket, such that the `verify` callable can perform signature verification and/or decryption. The `verify` callable is called with a single argument - the bytes received across the socket - and should return the bytes to be processed, or `None` to indicate that the bytes should be discarded. The returned bytes could be the same as the passed in bytes (e.g. when only verification is done), or they could be completely different (perhaps if decryption were performed).
To send a configuration to the socket, read in the configuration file and send it to the socket as a sequence of bytes preceded by a four-byte length string packed in binary using `struct.pack('>L', n)`.
Note
Because portions of the configuration are passed through [`eval()`](https://docs.python.org/3/library/functions.html#eval "eval"), use of this function may open its users to a security risk. While the function only binds to a socket on `localhost`, and so does not accept connections from remote machines, there are scenarios where untrusted code could be run under the account of the process which calls `listen()`. Specifically, if the process calling `listen()` runs on a multi-user machine where users cannot trust each other, then a malicious user could arrange to run essentially arbitrary code in a victim user’s process, simply by connecting to the victim’s `listen()` socket and sending a configuration which runs whatever code the attacker wants to have executed in the victim’s process. This is especially easy to do if the default port is used, but not hard even if a different port is used. To avoid the risk of this happening, use the `verify` argument to `listen()` to prevent unrecognised configurations from being applied.
Changed in version 3.4: The `verify` argument was added.
Note
If you want to send configurations to the listener which don’t disable existing loggers, you will need to use a JSON format for the configuration, which will use [`dictConfig()`](https://docs.python.org/3/library/logging.config.html#logging.config.dictConfig "logging.config.dictConfig") for configuration. This method allows you to specify `disable_existing_loggers` as `False` in the configuration you send.

logging.config.stopListening()[¶](https://docs.python.org/3/library/logging.config.html#logging.config.stopListening "Link to this definition")

Stops the listening server which was created with a call to [`listen()`](https://docs.python.org/3/library/logging.config.html#logging.config.listen "logging.config.listen"). This is typically called before calling `join()` on the return value from `listen()`.
## Security considerations[¶](https://docs.python.org/3/library/logging.config.html#security-considerations "Link to this heading")
The logging configuration functionality tries to offer convenience, and in part this is done by offering the ability to convert text in configuration files into Python objects used in logging configuration - for example, as described in [User-defined objects](https://docs.python.org/3/library/logging.config.html#logging-config-dict-userdef). However, these same mechanisms (importing callables from user-defined modules and calling them with parameters from the configuration) could be used to invoke any code you like, and for this reason you should treat configuration files from untrusted sources with _extreme caution_ and satisfy yourself that nothing bad can happen if you load them, before actually loading them.
## Configuration dictionary schema[¶](https://docs.python.org/3/library/logging.config.html#configuration-dictionary-schema "Link to this heading")
Describing a logging configuration requires listing the various objects to create and the connections between them; for example, you may create a handler named ‘console’ and then say that the logger named ‘startup’ will send its messages to the ‘console’ handler. These objects aren’t limited to those provided by the [`logging`](https://docs.python.org/3/library/logging.html#module-logging "logging: Flexible event logging system for applications.") module because you might write your own formatter or handler class. The parameters to these classes may also need to include external objects such as `sys.stderr`. The syntax for describing these objects and connections is defined in [Object connections](https://docs.python.org/3/library/logging.config.html#logging-config-dict-connections) below.
### Dictionary Schema Details[¶](https://docs.python.org/3/library/logging.config.html#dictionary-schema-details "Link to this heading")
The dictionary passed to [`dictConfig()`](https://docs.python.org/3/library/logging.config.html#logging.config.dictConfig "logging.config.dictConfig") must contain the following keys:
  * _version_ - to be set to an integer value representing the schema version. The only valid value at present is 1, but having this key allows the schema to evolve while still preserving backwards compatibility.


All other keys are optional, but if present they will be interpreted as described below. In all cases below where a ‘configuring dict’ is mentioned, it will be checked for the special `'()'` key to see if a custom instantiation is required. If so, the mechanism described in [User-defined objects](https://docs.python.org/3/library/logging.config.html#logging-config-dict-userdef) below is used to create an instance; otherwise, the context is used to determine what to instantiate.
  * _formatters_ - the corresponding value will be a dict in which each key is a formatter id and each value is a dict describing how to configure the corresponding [`Formatter`](https://docs.python.org/3/library/logging.html#logging.Formatter "logging.Formatter") instance.
The configuring dict is searched for the following optional keys which correspond to the arguments passed to create a [`Formatter`](https://docs.python.org/3/library/logging.html#logging.Formatter "logging.Formatter") object:
    * `format`
    * `datefmt`
    * `style`
    * `validate` (since version >=3.8)
    * `defaults` (since version >=3.12)
An optional `class` key indicates the name of the formatter’s class (as a dotted module and class name). The instantiation arguments are as for [`Formatter`](https://docs.python.org/3/library/logging.html#logging.Formatter "logging.Formatter"), thus this key is most useful for instantiating a customised subclass of `Formatter`. For example, the alternative class might present exception tracebacks in an expanded or condensed format. If your formatter requires different or extra configuration keys, you should use [User-defined objects](https://docs.python.org/3/library/logging.config.html#logging-config-dict-userdef).
  * _filters_ - the corresponding value will be a dict in which each key is a filter id and each value is a dict describing how to configure the corresponding Filter instance.
The configuring dict is searched for the key `name` (defaulting to the empty string) and this is used to construct a [`logging.Filter`](https://docs.python.org/3/library/logging.html#logging.Filter "logging.Filter") instance.
  * _handlers_ - the corresponding value will be a dict in which each key is a handler id and each value is a dict describing how to configure the corresponding Handler instance.
The configuring dict is searched for the following keys:
    * `class` (mandatory). This is the fully qualified name of the handler class.
    * `level` (optional). The level of the handler.
    * `formatter` (optional). The id of the formatter for this handler.
    * `filters` (optional). A list of ids of the filters for this handler.
Changed in version 3.11: `filters` can take filter instances in addition to ids.
All _other_ keys are passed through as keyword arguments to the handler’s constructor. For example, given the snippet:
```
handlers:
  console:
    class : logging.StreamHandler
    formatter: brief
    level   : INFO
    filters: [allow_foo]
    stream  : ext://sys.stdout
  file:
    class : logging.handlers.RotatingFileHandler
    formatter: precise
    filename: logconfig.log
    maxBytes: 1024
    backupCount: 3

```

the handler with id `console` is instantiated as a [`logging.StreamHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.StreamHandler "logging.StreamHandler"), using `sys.stdout` as the underlying stream. The handler with id `file` is instantiated as a [`logging.handlers.RotatingFileHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.RotatingFileHandler "logging.handlers.RotatingFileHandler") with the keyword arguments `filename='logconfig.log', maxBytes=1024, backupCount=3`.
  * _loggers_ - the corresponding value will be a dict in which each key is a logger name and each value is a dict describing how to configure the corresponding Logger instance.
The configuring dict is searched for the following keys:
    * `level` (optional). The level of the logger.
    * `propagate` (optional). The propagation setting of the logger.
    * `filters` (optional). A list of ids of the filters for this logger.
Changed in version 3.11: `filters` can take filter instances in addition to ids.
    * `handlers` (optional). A list of ids of the handlers for this logger.
The specified loggers will be configured according to the level, propagation, filters and handlers specified.
  * _root_ - this will be the configuration for the root logger. Processing of the configuration will be as for any logger, except that the `propagate` setting will not be applicable.
  * _incremental_ - whether the configuration is to be interpreted as incremental to the existing configuration. This value defaults to `False`, which means that the specified configuration replaces the existing configuration with the same semantics as used by the existing [`fileConfig()`](https://docs.python.org/3/library/logging.config.html#logging.config.fileConfig "logging.config.fileConfig") API.
If the specified value is `True`, the configuration is processed as described in the section on [Incremental Configuration](https://docs.python.org/3/library/logging.config.html#logging-config-dict-incremental).
  * _disable_existing_loggers_ - whether any existing non-root loggers are to be disabled. This setting mirrors the parameter of the same name in [`fileConfig()`](https://docs.python.org/3/library/logging.config.html#logging.config.fileConfig "logging.config.fileConfig"). If absent, this parameter defaults to `True`. This value is ignored if _incremental_ is `True`.


### Incremental Configuration[¶](https://docs.python.org/3/library/logging.config.html#incremental-configuration "Link to this heading")
It is difficult to provide complete flexibility for incremental configuration. For example, because objects such as filters and formatters are anonymous, once a configuration is set up, it is not possible to refer to such anonymous objects when augmenting a configuration.
Furthermore, there is not a compelling case for arbitrarily altering the object graph of loggers, handlers, filters, formatters at run-time, once a configuration is set up; the verbosity of loggers and handlers can be controlled just by setting levels (and, in the case of loggers, propagation flags). Changing the object graph arbitrarily in a safe way is problematic in a multi-threaded environment; while not impossible, the benefits are not worth the complexity it adds to the implementation.
Thus, when the `incremental` key of a configuration dict is present and is `True`, the system will completely ignore any `formatters` and `filters` entries, and process only the `level` settings in the `handlers` entries, and the `level` and `propagate` settings in the `loggers` and `root` entries.
Using a value in the configuration dict lets configurations to be sent over the wire as pickled dicts to a socket listener. Thus, the logging verbosity of a long-running application can be altered over time with no need to stop and restart the application.
### Object connections[¶](https://docs.python.org/3/library/logging.config.html#object-connections "Link to this heading")
The schema describes a set of logging objects - loggers, handlers, formatters, filters - which are connected to each other in an object graph. Thus, the schema needs to represent connections between the objects. For example, say that, once configured, a particular logger has attached to it a particular handler. For the purposes of this discussion, we can say that the logger represents the source, and the handler the destination, of a connection between the two. Of course in the configured objects this is represented by the logger holding a reference to the handler. In the configuration dict, this is done by giving each destination object an id which identifies it unambiguously, and then using the id in the source object’s configuration to indicate that a connection exists between the source and the destination object with that id.
So, for example, consider the following YAML snippet:
```
formatters:
  brief:
    # configuration for formatter with id 'brief' goes here
  precise:
    # configuration for formatter with id 'precise' goes here
handlers:
  h1: #This is an id
