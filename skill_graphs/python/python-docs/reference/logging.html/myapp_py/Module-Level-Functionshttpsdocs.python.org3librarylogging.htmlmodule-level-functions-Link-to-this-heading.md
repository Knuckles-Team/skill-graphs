## Module-Level Functions[¶](https://docs.python.org/3/library/logging.html#module-level-functions "Link to this heading")
In addition to the classes described above, there are a number of module-level functions.

logging.getLogger(_name =None_)[¶](https://docs.python.org/3/library/logging.html#logging.getLogger "Link to this definition")

Return a logger with the specified name or, if name is `None`, return the root logger of the hierarchy. If specified, the name is typically a dot-separated hierarchical name like _‘a’_ , _‘a.b’_ or _‘a.b.c.d’_. Choice of these names is entirely up to the developer who is using logging, though it is recommended that `__name__` be used unless you have a specific reason for not doing that, as mentioned in [Logger Objects](https://docs.python.org/3/library/logging.html#logger).
All calls to this function with a given name return the same logger instance. This means that logger instances never need to be passed between different parts of an application.

logging.getLoggerClass()[¶](https://docs.python.org/3/library/logging.html#logging.getLoggerClass "Link to this definition")

Return either the standard [`Logger`](https://docs.python.org/3/library/logging.html#logging.Logger "logging.Logger") class, or the last class passed to [`setLoggerClass()`](https://docs.python.org/3/library/logging.html#logging.setLoggerClass "logging.setLoggerClass"). This function may be called from within a new class definition, to ensure that installing a customized `Logger` class will not undo customizations already applied by other code. For example:
Copy```
class MyLogger(logging.getLoggerClass()):
    # ... override behaviour here

```


logging.getLogRecordFactory()[¶](https://docs.python.org/3/library/logging.html#logging.getLogRecordFactory "Link to this definition")

Return a callable which is used to create a [`LogRecord`](https://docs.python.org/3/library/logging.html#logging.LogRecord "logging.LogRecord").
Added in version 3.2: This function has been provided, along with [`setLogRecordFactory()`](https://docs.python.org/3/library/logging.html#logging.setLogRecordFactory "logging.setLogRecordFactory"), to allow developers more control over how the [`LogRecord`](https://docs.python.org/3/library/logging.html#logging.LogRecord "logging.LogRecord") representing a logging event is constructed.
See [`setLogRecordFactory()`](https://docs.python.org/3/library/logging.html#logging.setLogRecordFactory "logging.setLogRecordFactory") for more information about the how the factory is called.

logging.debug(_msg_ , _* args_, _** kwargs_)[¶](https://docs.python.org/3/library/logging.html#logging.debug "Link to this definition")

This is a convenience function that calls [`Logger.debug()`](https://docs.python.org/3/library/logging.html#logging.Logger.debug "logging.Logger.debug"), on the root logger. The handling of the arguments is in every way identical to what is described in that method.
The only difference is that if the root logger has no handlers, then [`basicConfig()`](https://docs.python.org/3/library/logging.html#logging.basicConfig "logging.basicConfig") is called, prior to calling `debug` on the root logger.
For very short scripts or quick demonstrations of `logging` facilities, `debug` and the other module-level functions may be convenient. However, most programs will want to carefully and explicitly control the logging configuration, and should therefore prefer creating a module-level logger and calling [`Logger.debug()`](https://docs.python.org/3/library/logging.html#logging.Logger.debug "logging.Logger.debug") (or other level-specific methods) on it, as described at the beginning of this documentation.

logging.info(_msg_ , _* args_, _** kwargs_)[¶](https://docs.python.org/3/library/logging.html#logging.info "Link to this definition")

Logs a message with level [`INFO`](https://docs.python.org/3/library/logging.html#logging.INFO "logging.INFO") on the root logger. The arguments and behavior are otherwise the same as for [`debug()`](https://docs.python.org/3/library/logging.html#logging.debug "logging.debug").

logging.warning(_msg_ , _* args_, _** kwargs_)[¶](https://docs.python.org/3/library/logging.html#logging.warning "Link to this definition")

Logs a message with level [`WARNING`](https://docs.python.org/3/library/logging.html#logging.WARNING "logging.WARNING") on the root logger. The arguments and behavior are otherwise the same as for [`debug()`](https://docs.python.org/3/library/logging.html#logging.debug "logging.debug").
Note
There is an obsolete function `warn` which is functionally identical to `warning`. As `warn` is deprecated, please do not use it - use `warning` instead.

logging.error(_msg_ , _* args_, _** kwargs_)[¶](https://docs.python.org/3/library/logging.html#logging.error "Link to this definition")

Logs a message with level [`ERROR`](https://docs.python.org/3/library/logging.html#logging.ERROR "logging.ERROR") on the root logger. The arguments and behavior are otherwise the same as for [`debug()`](https://docs.python.org/3/library/logging.html#logging.debug "logging.debug").

logging.critical(_msg_ , _* args_, _** kwargs_)[¶](https://docs.python.org/3/library/logging.html#logging.critical "Link to this definition")

Logs a message with level [`CRITICAL`](https://docs.python.org/3/library/logging.html#logging.CRITICAL "logging.CRITICAL") on the root logger. The arguments and behavior are otherwise the same as for [`debug()`](https://docs.python.org/3/library/logging.html#logging.debug "logging.debug").

logging.exception(_msg_ , _* args_, _** kwargs_)[¶](https://docs.python.org/3/library/logging.html#logging.exception "Link to this definition")

Logs a message with level [`ERROR`](https://docs.python.org/3/library/logging.html#logging.ERROR "logging.ERROR") on the root logger. The arguments and behavior are otherwise the same as for [`debug()`](https://docs.python.org/3/library/logging.html#logging.debug "logging.debug"). Exception info is added to the logging message. This function should only be called from an exception handler.

logging.log(_level_ , _msg_ , _* args_, _** kwargs_)[¶](https://docs.python.org/3/library/logging.html#logging.log "Link to this definition")

Logs a message with level _level_ on the root logger. The arguments and behavior are otherwise the same as for [`debug()`](https://docs.python.org/3/library/logging.html#logging.debug "logging.debug").

logging.disable(_level =CRITICAL_)[¶](https://docs.python.org/3/library/logging.html#logging.disable "Link to this definition")

Provides an overriding level _level_ for all loggers which takes precedence over the logger’s own level. When the need arises to temporarily throttle logging output down across the whole application, this function can be useful. Its effect is to disable all logging calls of severity _level_ and below, so that if you call it with a value of INFO, then all INFO and DEBUG events would be discarded, whereas those of severity WARNING and above would be processed according to the logger’s effective level. If `logging.disable(logging.NOTSET)` is called, it effectively removes this overriding level, so that logging output again depends on the effective levels of individual loggers.
Note that if you have defined any custom logging level higher than `CRITICAL` (this is not recommended), you won’t be able to rely on the default value for the _level_ parameter, but will have to explicitly supply a suitable value.
Changed in version 3.7: The _level_ parameter was defaulted to level `CRITICAL`. See [bpo-28524](https://bugs.python.org/issue?@action=redirect&bpo=28524) for more information about this change.

logging.addLevelName(_level_ , _levelName_)[¶](https://docs.python.org/3/library/logging.html#logging.addLevelName "Link to this definition")

Associates level _level_ with text _levelName_ in an internal dictionary, which is used to map numeric levels to a textual representation, for example when a [`Formatter`](https://docs.python.org/3/library/logging.html#logging.Formatter "logging.Formatter") formats a message. This function can also be used to define your own levels. The only constraints are that all levels used must be registered using this function, levels should be positive integers and they should increase in increasing order of severity.
Note
If you are thinking of defining your own levels, please see the section on [Custom Levels](https://docs.python.org/3/howto/logging.html#custom-levels).

logging.getLevelNamesMapping()[¶](https://docs.python.org/3/library/logging.html#logging.getLevelNamesMapping "Link to this definition")

Returns a mapping from level names to their corresponding logging levels. For example, the string “CRITICAL” maps to [`CRITICAL`](https://docs.python.org/3/library/logging.html#logging.CRITICAL "logging.CRITICAL"). The returned mapping is copied from an internal mapping on each call to this function.
Added in version 3.11.

logging.getLevelName(_level_)[¶](https://docs.python.org/3/library/logging.html#logging.getLevelName "Link to this definition")

Returns the textual or numeric representation of logging level _level_.
If _level_ is one of the predefined levels [`CRITICAL`](https://docs.python.org/3/library/logging.html#logging.CRITICAL "logging.CRITICAL"), [`ERROR`](https://docs.python.org/3/library/logging.html#logging.ERROR "logging.ERROR"), [`WARNING`](https://docs.python.org/3/library/logging.html#logging.WARNING "logging.WARNING"), [`INFO`](https://docs.python.org/3/library/logging.html#logging.INFO "logging.INFO") or [`DEBUG`](https://docs.python.org/3/library/logging.html#logging.DEBUG "logging.DEBUG") then you get the corresponding string. If you have associated levels with names using [`addLevelName()`](https://docs.python.org/3/library/logging.html#logging.addLevelName "logging.addLevelName") then the name you have associated with _level_ is returned. If a numeric value corresponding to one of the defined levels is passed in, the corresponding string representation is returned.
The _level_ parameter also accepts a string representation of the level such as ‘INFO’. In such cases, this functions returns the corresponding numeric value of the level.
If no matching numeric or string value is passed in, the string ‘Level %s’ % level is returned.
Note
Levels are internally integers (as they need to be compared in the logging logic). This function is used to convert between an integer level and the level name displayed in the formatted log output by means of the `%(levelname)s` format specifier (see [LogRecord attributes](https://docs.python.org/3/library/logging.html#logrecord-attributes)), and vice versa.
Changed in version 3.4: In Python versions earlier than 3.4, this function could also be passed a text level, and would return the corresponding numeric value of the level. This undocumented behaviour was considered a mistake, and was removed in Python 3.4, but reinstated in 3.4.2 due to retain backward compatibility.

logging.getHandlerByName(_name_)[¶](https://docs.python.org/3/library/logging.html#logging.getHandlerByName "Link to this definition")

Returns a handler with the specified _name_ , or `None` if there is no handler with that name.
Added in version 3.12.

logging.getHandlerNames()[¶](https://docs.python.org/3/library/logging.html#logging.getHandlerNames "Link to this definition")

Returns an immutable set of all known handler names.
Added in version 3.12.

logging.makeLogRecord(_attrdict_)[¶](https://docs.python.org/3/library/logging.html#logging.makeLogRecord "Link to this definition")

Creates and returns a new [`LogRecord`](https://docs.python.org/3/library/logging.html#logging.LogRecord "logging.LogRecord") instance whose attributes are defined by _attrdict_. This function is useful for taking a pickled `LogRecord` attribute dictionary, sent over a socket, and reconstituting it as a `LogRecord` instance at the receiving end.

logging.basicConfig(_** kwargs_)[¶](https://docs.python.org/3/library/logging.html#logging.basicConfig "Link to this definition")

Does basic configuration for the logging system by creating a [`StreamHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.StreamHandler "logging.StreamHandler") with a default [`Formatter`](https://docs.python.org/3/library/logging.html#logging.Formatter "logging.Formatter") and adding it to the root logger. The functions [`debug()`](https://docs.python.org/3/library/logging.html#logging.debug "logging.debug"), [`info()`](https://docs.python.org/3/library/logging.html#logging.info "logging.info"), [`warning()`](https://docs.python.org/3/library/logging.html#logging.warning "logging.warning"), [`error()`](https://docs.python.org/3/library/logging.html#logging.error "logging.error") and [`critical()`](https://docs.python.org/3/library/logging.html#logging.critical "logging.critical") will call `basicConfig()` automatically if no handlers are defined for the root logger.
This function does nothing if the root logger already has handlers configured, unless the keyword argument _force_ is set to `True`.
Note
This function should be called from the main thread before other threads are started. In versions of Python prior to 2.7.1 and 3.2, if this function is called from multiple threads, it is possible (in rare circumstances) that a handler will be added to the root logger more than once, leading to unexpected results such as messages being duplicated in the log.
The following keyword arguments are supported.
Format | Description
---|---
_filename_ | Specifies that a [`FileHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.FileHandler "logging.FileHandler") be created, using the specified filename, rather than a [`StreamHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.StreamHandler "logging.StreamHandler").
_filemode_ | If _filename_ is specified, open the file in this [mode](https://docs.python.org/3/library/functions.html#filemodes). Defaults to `'a'`.
_format_ | Use the specified format string for the handler. Defaults to attributes `levelname`, `name` and `message` separated by colons.
_datefmt_ | Use the specified date/time format, as accepted by [`time.strftime()`](https://docs.python.org/3/library/time.html#time.strftime "time.strftime").
_style_ | If _format_ is specified, use this style for the format string. One of `'%'`, `'{'` or `'$'` for [printf-style](https://docs.python.org/3/library/stdtypes.html#old-string-formatting), [`str.format()`](https://docs.python.org/3/library/stdtypes.html#str.format "str.format") or [`string.Template`](https://docs.python.org/3/library/string.html#string.Template "string.Template") respectively. Defaults to `'%'`.
_level_ | Set the root logger level to the specified [level](https://docs.python.org/3/library/logging.html#levels).
_stream_ | Use the specified stream to initialize the [`StreamHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.StreamHandler "logging.StreamHandler"). Note that this argument is incompatible with _filename_ - if both are present, a `ValueError` is raised.
_handlers_ | If specified, this should be an iterable of already created handlers to add to the root logger. Any handlers which don’t already have a formatter set will be assigned the default formatter created in this function. Note that this argument is incompatible with _filename_ or _stream_ - if both are present, a `ValueError` is raised.
_force_ | If this keyword argument is specified as true, any existing handlers attached to the root logger are removed and closed, before carrying out the configuration as specified by the other arguments.
_encoding_ | If this keyword argument is specified along with _filename_ , its value is used when the [`FileHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.FileHandler "logging.FileHandler") is created, and thus used when opening the output file.
_errors_ | If this keyword argument is specified along with _filename_ , its value is used when the [`FileHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.FileHandler "logging.FileHandler") is created, and thus used when opening the output file. If not specified, the value ‘backslashreplace’ is used. Note that if `None` is specified, it will be passed as such to [`open()`](https://docs.python.org/3/library/functions.html#open "open"), which means that it will be treated the same as passing ‘errors’.
Changed in version 3.2: The _style_ argument was added.
Changed in version 3.3: The _handlers_ argument was added. Additional checks were added to catch situations where incompatible arguments are specified (e.g. _handlers_ together with _stream_ or _filename_ , or _stream_ together with _filename_).
Changed in version 3.8: The _force_ argument was added.
Changed in version 3.9: The _encoding_ and _errors_ arguments were added.

logging.shutdown()[¶](https://docs.python.org/3/library/logging.html#logging.shutdown "Link to this definition")

Informs the logging system to perform an orderly shutdown by flushing and closing all handlers. This should be called at application exit and no further use of the logging system should be made after this call.
When the logging module is imported, it registers this function as an exit handler (see [`atexit`](https://docs.python.org/3/library/atexit.html#module-atexit "atexit: Register and execute cleanup functions.")), so normally there’s no need to do that manually.

logging.setLoggerClass(_klass_)[¶](https://docs.python.org/3/library/logging.html#logging.setLoggerClass "Link to this definition")

Tells the logging system to use the class _klass_ when instantiating a logger. The class should define `__init__()` such that only a name argument is required, and the `__init__()` should call `Logger.__init__()`. This function is typically called before any loggers are instantiated by applications which need to use custom logger behavior. After this call, as at any other time, do not instantiate loggers directly using the subclass: continue to use the [`logging.getLogger()`](https://docs.python.org/3/library/logging.html#logging.getLogger "logging.getLogger") API to get your loggers.

logging.setLogRecordFactory(_factory_)[¶](https://docs.python.org/3/library/logging.html#logging.setLogRecordFactory "Link to this definition")

Set a callable which is used to create a [`LogRecord`](https://docs.python.org/3/library/logging.html#logging.LogRecord "logging.LogRecord").

Parameters:

**factory** – The factory callable to be used to instantiate a log record.
Added in version 3.2: This function has been provided, along with [`getLogRecordFactory()`](https://docs.python.org/3/library/logging.html#logging.getLogRecordFactory "logging.getLogRecordFactory"), to allow developers more control over how the [`LogRecord`](https://docs.python.org/3/library/logging.html#logging.LogRecord "logging.LogRecord") representing a logging event is constructed.
The factory has the following signature:
`factory(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs)`
>

name:

> The logger name.

level:

> The logging level (numeric).

fn:

> The full pathname of the file where the logging call was made.

lno:

> The line number in the file where the logging call was made.

msg:

> The logging message.

args:

> The arguments for the logging message.

exc_info:

> An exception tuple, or `None`.

func:

> The name of the function or method which invoked the logging call.

sinfo:

> A stack traceback such as is provided by [`traceback.print_stack()`](https://docs.python.org/3/library/traceback.html#traceback.print_stack "traceback.print_stack"), showing the call hierarchy.

kwargs:

> Additional keyword arguments.
## Module-Level Attributes[¶](https://docs.python.org/3/library/logging.html#module-level-attributes "Link to this heading")

logging.lastResort[¶](https://docs.python.org/3/library/logging.html#logging.lastResort "Link to this definition")

A “handler of last resort” is available through this attribute. This is a [`StreamHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.StreamHandler "logging.StreamHandler") writing to `sys.stderr` with a level of `WARNING`, and is used to handle logging events in the absence of any logging configuration. The end result is to just print the message to `sys.stderr`. This replaces the earlier error message saying that “no handlers could be found for logger XYZ”. If you need the earlier behaviour for some reason, `lastResort` can be set to `None`.
Added in version 3.2.

logging.raiseExceptions[¶](https://docs.python.org/3/library/logging.html#logging.raiseExceptions "Link to this definition")

Used to see if exceptions during handling should be propagated.
Default: `True`.
If `raiseExceptions` is `False`, exceptions get silently ignored. This is what is mostly wanted for a logging system - most users will not care about errors in the logging system, they are more interested in application errors.
## Integration with the warnings module[¶](https://docs.python.org/3/library/logging.html#integration-with-the-warnings-module "Link to this heading")
The [`captureWarnings()`](https://docs.python.org/3/library/logging.html#logging.captureWarnings "logging.captureWarnings") function can be used to integrate `logging` with the [`warnings`](https://docs.python.org/3/library/warnings.html#module-warnings "warnings: Issue warning messages and control their disposition.") module.

logging.captureWarnings(_capture_)[¶](https://docs.python.org/3/library/logging.html#logging.captureWarnings "Link to this definition")

This function is used to turn the capture of warnings by logging on and off.
If _capture_ is `True`, warnings issued by the [`warnings`](https://docs.python.org/3/library/warnings.html#module-warnings "warnings: Issue warning messages and control their disposition.") module will be redirected to the logging system. Specifically, a warning will be formatted using [`warnings.formatwarning()`](https://docs.python.org/3/library/warnings.html#warnings.formatwarning "warnings.formatwarning") and the resulting string logged to a logger named `'py.warnings'` with a severity of [`WARNING`](https://docs.python.org/3/library/logging.html#logging.WARNING "logging.WARNING").
If _capture_ is `False`, the redirection of warnings to the logging system will stop, and warnings will be redirected to their original destinations (i.e. those in effect before `captureWarnings(True)` was called).
See also

Module [`logging.config`](https://docs.python.org/3/library/logging.config.html#module-logging.config "logging.config: Configuration of the logging module.")

Configuration API for the logging module.

Module [`logging.handlers`](https://docs.python.org/3/library/logging.handlers.html#module-logging.handlers "logging.handlers: Handlers for the logging module.")

Useful handlers included with the logging module.

[**PEP 282**](https://peps.python.org/pep-0282/) - A Logging System

The proposal which described this feature for inclusion in the Python standard library.
This is the original source for the `logging` package. The version of the package available from this site is suitable for use with Python 1.5.2, 2.1.x and 2.2.x, which do not include the `logging` package in the standard library.
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`logging` — Logging facility for Python](https://docs.python.org/3/library/logging.html)
    * [Logger Objects](https://docs.python.org/3/library/logging.html#logger-objects)
    * [Logging Levels](https://docs.python.org/3/library/logging.html#logging-levels)
    * [Handler Objects](https://docs.python.org/3/library/logging.html#handler-objects)
    * [Formatter Objects](https://docs.python.org/3/library/logging.html#formatter-objects)
    * [Filter Objects](https://docs.python.org/3/library/logging.html#filter-objects)
    * [LogRecord Objects](https://docs.python.org/3/library/logging.html#logrecord-objects)
    * [LogRecord attributes](https://docs.python.org/3/library/logging.html#logrecord-attributes)
    * [LoggerAdapter Objects](https://docs.python.org/3/library/logging.html#loggeradapter-objects)
    * [Thread Safety](https://docs.python.org/3/library/logging.html#thread-safety)
    * [Module-Level Functions](https://docs.python.org/3/library/logging.html#module-level-functions)
    * [Module-Level Attributes](https://docs.python.org/3/library/logging.html#module-level-attributes)
    * [Integration with the warnings module](https://docs.python.org/3/library/logging.html#integration-with-the-warnings-module)


#### Previous topic
[`time` — Time access and conversions](https://docs.python.org/3/library/time.html "previous chapter")
#### Next topic
[`logging.config` — Logging configuration](https://docs.python.org/3/library/logging.config.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=logging+%E2%80%94+Logging+facility+for+Python&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Flogging.html&pagesource=library%2Flogging.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/logging.config.html "logging.config — Logging configuration") |
  * [previous](https://docs.python.org/3/library/time.html "time — Time access and conversions") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Generic Operating System Services](https://docs.python.org/3/library/allows.html) »
  * [`logging` — Logging facility for Python](https://docs.python.org/3/library/logging.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
  *[*]: Keyword-only parameters separator (PEP 3102)
