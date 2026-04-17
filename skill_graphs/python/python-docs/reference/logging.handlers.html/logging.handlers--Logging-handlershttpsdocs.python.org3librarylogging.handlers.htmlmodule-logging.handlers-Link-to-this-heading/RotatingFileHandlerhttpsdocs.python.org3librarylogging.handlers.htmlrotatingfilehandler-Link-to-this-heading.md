## RotatingFileHandler[¶](https://docs.python.org/3/library/logging.handlers.html#rotatingfilehandler "Link to this heading")
The [`RotatingFileHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.RotatingFileHandler "logging.handlers.RotatingFileHandler") class, located in the `logging.handlers` module, supports rotation of disk log files.

_class_ logging.handlers.RotatingFileHandler(_filename_ , _mode ='a'_, _maxBytes =0_, _backupCount =0_, _encoding =None_, _delay =False_, _errors =None_)[¶](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.RotatingFileHandler "Link to this definition")

Returns a new instance of the `RotatingFileHandler` class. The specified file is opened and used as the stream for logging. If _mode_ is not specified, `'a'` is used. If _encoding_ is not `None`, it is used to open the file with that encoding. If _delay_ is true, then file opening is deferred until the first call to [`emit()`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.RotatingFileHandler.emit "logging.handlers.RotatingFileHandler.emit"). By default, the file grows indefinitely. If _errors_ is provided, it determines how encoding errors are handled.
You can use the _maxBytes_ and _backupCount_ values to allow the file to _rollover_ at a predetermined size. When the size is about to be exceeded, the file is closed and a new file is silently opened for output. Rollover occurs whenever the current log file is nearly _maxBytes_ in length; but if either of _maxBytes_ or _backupCount_ is zero, rollover never occurs, so you generally want to set _backupCount_ to at least 1, and have a non-zero _maxBytes_. When _backupCount_ is non-zero, the system will save old log files by appending the extensions ‘.1’, ‘.2’ etc., to the filename. For example, with a _backupCount_ of 5 and a base file name of `app.log`, you would get `app.log`, `app.log.1`, `app.log.2`, up to `app.log.5`. The file being written to is always `app.log`. When this file is filled, it is closed and renamed to `app.log.1`, and if files `app.log.1`, `app.log.2`, etc. exist, then they are renamed to `app.log.2`, `app.log.3` etc. respectively.
Changed in version 3.6: As well as string values, [`Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path") objects are also accepted for the _filename_ argument.
Changed in version 3.9: The _errors_ parameter was added.

doRollover()[¶](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.RotatingFileHandler.doRollover "Link to this definition")

Does a rollover, as described above.

emit(_record_)[¶](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.RotatingFileHandler.emit "Link to this definition")

Outputs the record to the file, catering for rollover as described previously.

shouldRollover(_record_)[¶](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.RotatingFileHandler.shouldRollover "Link to this definition")

See if the supplied record would cause the file to exceed the configured size limit.
