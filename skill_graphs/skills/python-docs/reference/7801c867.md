## WatchedFileHandler[¶](https://docs.python.org/3/library/logging.handlers.html#watchedfilehandler "Link to this heading")
The [`WatchedFileHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.WatchedFileHandler "logging.handlers.WatchedFileHandler") class, located in the `logging.handlers` module, is a `FileHandler` which watches the file it is logging to. If the file changes, it is closed and reopened using the file name.
A file change can happen because of usage of programs such as _newsyslog_ and _logrotate_ which perform log file rotation. This handler, intended for use under Unix/Linux, watches the file to see if it has changed since the last emit. (A file is deemed to have changed if its device or inode have changed.) If the file has changed, the old file stream is closed, and the file opened to get a new stream.
This handler is not appropriate for use under Windows, because under Windows open log files cannot be moved or renamed - logging opens the files with exclusive locks - and so there is no need for such a handler. Furthermore, _ST_INO_ is not supported under Windows; [`stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat") always returns zero for this value.

_class_ logging.handlers.WatchedFileHandler(_filename_ , _mode ='a'_, _encoding =None_, _delay =False_, _errors =None_)[¶](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.WatchedFileHandler "Link to this definition")

Returns a new instance of the `WatchedFileHandler` class. The specified file is opened and used as the stream for logging. If _mode_ is not specified, `'a'` is used. If _encoding_ is not `None`, it is used to open the file with that encoding. If _delay_ is true, then file opening is deferred until the first call to [`emit()`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.WatchedFileHandler.emit "logging.handlers.WatchedFileHandler.emit"). By default, the file grows indefinitely. If _errors_ is provided, it determines how encoding errors are handled.
Changed in version 3.6: As well as string values, [`Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path") objects are also accepted for the _filename_ argument.
Changed in version 3.9: The _errors_ parameter was added.

reopenIfNeeded()[¶](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.WatchedFileHandler.reopenIfNeeded "Link to this definition")

Checks to see if the file has changed. If it has, the existing stream is flushed and closed and the file opened again, typically as a precursor to outputting the record to the file.
Added in version 3.6.

emit(_record_)[¶](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.WatchedFileHandler.emit "Link to this definition")

Outputs the record to the file, but first calls [`reopenIfNeeded()`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.WatchedFileHandler.reopenIfNeeded "logging.handlers.WatchedFileHandler.reopenIfNeeded") to reopen the file if it has changed.
