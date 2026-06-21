## FileHandler[¶](https://docs.python.org/3/library/logging.handlers.html#filehandler "Link to this heading")
The [`FileHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.FileHandler "logging.FileHandler") class, located in the core [`logging`](https://docs.python.org/3/library/logging.html#module-logging "logging: Flexible event logging system for applications.") package, sends logging output to a disk file. It inherits the output functionality from [`StreamHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.StreamHandler "logging.StreamHandler").

_class_ logging.FileHandler(_filename_ , _mode ='a'_, _encoding =None_, _delay =False_, _errors =None_)[¶](https://docs.python.org/3/library/logging.handlers.html#logging.FileHandler "Link to this definition")

Returns a new instance of the `FileHandler` class. The specified file is opened and used as the stream for logging. If _mode_ is not specified, `'a'` is used. If _encoding_ is not `None`, it is used to open the file with that encoding. If _delay_ is true, then file opening is deferred until the first call to [`emit()`](https://docs.python.org/3/library/logging.handlers.html#logging.FileHandler.emit "logging.FileHandler.emit"). By default, the file grows indefinitely. If _errors_ is specified, it’s used to determine how encoding errors are handled.
Changed in version 3.6: As well as string values, [`Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path") objects are also accepted for the _filename_ argument.
Changed in version 3.9: The _errors_ parameter was added.

close()[¶](https://docs.python.org/3/library/logging.handlers.html#logging.FileHandler.close "Link to this definition")

Closes the file.

emit(_record_)[¶](https://docs.python.org/3/library/logging.handlers.html#logging.FileHandler.emit "Link to this definition")

Outputs the record to the file.
Note that if the file was closed due to logging shutdown at exit and the file mode is ‘w’, the record will not be emitted (see [bpo-42378](https://bugs.python.org/issue?@action=redirect&bpo=42378)).
