## LoggerAdapter Objects[¶](https://docs.python.org/3/library/logging.html#loggeradapter-objects "Link to this heading")
[`LoggerAdapter`](https://docs.python.org/3/library/logging.html#logging.LoggerAdapter "logging.LoggerAdapter") instances are used to conveniently pass contextual information into logging calls. For a usage example, see the section on [adding contextual information to your logging output](https://docs.python.org/3/howto/logging-cookbook.html#context-info).

_class_ logging.LoggerAdapter(_logger_ , _extra =None_, _merge_extra =False_)[¶](https://docs.python.org/3/library/logging.html#logging.LoggerAdapter "Link to this definition")

Returns an instance of `LoggerAdapter` initialized with an underlying [`Logger`](https://docs.python.org/3/library/logging.html#logging.Logger "logging.Logger") instance, an optional dict-like object (_extra_), and an optional boolean (_merge_extra_) indicating whether or not the _extra_ argument of individual log calls should be merged with the `LoggerAdapter` extra. The default behavior is to ignore the _extra_ argument of individual log calls and only use the one of the `LoggerAdapter` instance

process(_msg_ , _kwargs_)[¶](https://docs.python.org/3/library/logging.html#logging.LoggerAdapter.process "Link to this definition")

Modifies the message and/or keyword arguments passed to a logging call in order to insert contextual information. This implementation takes the object passed as _extra_ to the constructor and adds it to _kwargs_ using key ‘extra’. The return value is a (_msg_ , _kwargs_) tuple which has the (possibly modified) versions of the arguments passed in.

manager[¶](https://docs.python.org/3/library/logging.html#logging.LoggerAdapter.manager "Link to this definition")

Delegates to the underlying `manager` on _logger_.

_log[¶](https://docs.python.org/3/library/logging.html#logging.LoggerAdapter._log "Link to this definition")

Delegates to the underlying `_log()` method on _logger_.
In addition to the above, `LoggerAdapter` supports the following methods of [`Logger`](https://docs.python.org/3/library/logging.html#logging.Logger "logging.Logger"): [`debug()`](https://docs.python.org/3/library/logging.html#logging.Logger.debug "logging.Logger.debug"), [`info()`](https://docs.python.org/3/library/logging.html#logging.Logger.info "logging.Logger.info"), [`warning()`](https://docs.python.org/3/library/logging.html#logging.Logger.warning "logging.Logger.warning"), [`error()`](https://docs.python.org/3/library/logging.html#logging.Logger.error "logging.Logger.error"), [`exception()`](https://docs.python.org/3/library/logging.html#logging.Logger.exception "logging.Logger.exception"), [`critical()`](https://docs.python.org/3/library/logging.html#logging.Logger.critical "logging.Logger.critical"), [`log()`](https://docs.python.org/3/library/logging.html#logging.Logger.log "logging.Logger.log"), [`isEnabledFor()`](https://docs.python.org/3/library/logging.html#logging.Logger.isEnabledFor "logging.Logger.isEnabledFor"), [`getEffectiveLevel()`](https://docs.python.org/3/library/logging.html#logging.Logger.getEffectiveLevel "logging.Logger.getEffectiveLevel"), [`setLevel()`](https://docs.python.org/3/library/logging.html#logging.Logger.setLevel "logging.Logger.setLevel") and [`hasHandlers()`](https://docs.python.org/3/library/logging.html#logging.Logger.hasHandlers "logging.Logger.hasHandlers"). These methods have the same signatures as their counterparts in `Logger`, so you can use the two types of instances interchangeably.
Changed in version 3.2: The [`isEnabledFor()`](https://docs.python.org/3/library/logging.html#logging.Logger.isEnabledFor "logging.Logger.isEnabledFor"), [`getEffectiveLevel()`](https://docs.python.org/3/library/logging.html#logging.Logger.getEffectiveLevel "logging.Logger.getEffectiveLevel"), [`setLevel()`](https://docs.python.org/3/library/logging.html#logging.Logger.setLevel "logging.Logger.setLevel") and [`hasHandlers()`](https://docs.python.org/3/library/logging.html#logging.Logger.hasHandlers "logging.Logger.hasHandlers") methods were added to `LoggerAdapter`. These methods delegate to the underlying logger.
Changed in version 3.6: Attribute `manager` and method `_log()` were added, which delegate to the underlying logger and allow adapters to be nested.
Changed in version 3.10: The _extra_ argument is now optional.
Changed in version 3.13: The _merge_extra_ parameter was added.
