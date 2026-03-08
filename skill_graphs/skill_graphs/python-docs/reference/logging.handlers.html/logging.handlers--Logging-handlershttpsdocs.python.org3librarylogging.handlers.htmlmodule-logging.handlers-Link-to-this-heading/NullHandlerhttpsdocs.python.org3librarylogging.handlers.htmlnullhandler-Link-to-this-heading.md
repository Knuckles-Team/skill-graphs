## NullHandler[¶](https://docs.python.org/3/library/logging.handlers.html#nullhandler "Link to this heading")
Added in version 3.1.
The [`NullHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.NullHandler "logging.NullHandler") class, located in the core [`logging`](https://docs.python.org/3/library/logging.html#module-logging "logging: Flexible event logging system for applications.") package, does not do any formatting or output. It is essentially a ‘no-op’ handler for use by library developers.

_class_ logging.NullHandler[¶](https://docs.python.org/3/library/logging.handlers.html#logging.NullHandler "Link to this definition")

Returns a new instance of the `NullHandler` class.

emit(_record_)[¶](https://docs.python.org/3/library/logging.handlers.html#logging.NullHandler.emit "Link to this definition")

This method does nothing.

handle(_record_)[¶](https://docs.python.org/3/library/logging.handlers.html#logging.NullHandler.handle "Link to this definition")

This method does nothing.

createLock()[¶](https://docs.python.org/3/library/logging.handlers.html#logging.NullHandler.createLock "Link to this definition")

This method returns `None` for the lock, since there is no underlying I/O to which access needs to be serialized.
See [Configuring Logging for a Library](https://docs.python.org/3/howto/logging.html#library-config) for more information on how to use [`NullHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.NullHandler "logging.NullHandler").
