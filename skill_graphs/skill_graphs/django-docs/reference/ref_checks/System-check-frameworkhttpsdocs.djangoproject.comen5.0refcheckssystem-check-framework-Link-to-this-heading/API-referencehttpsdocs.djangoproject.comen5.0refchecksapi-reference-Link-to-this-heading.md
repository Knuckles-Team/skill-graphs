## API reference[¶](https://docs.djangoproject.com/en/5.0/ref/checks/#api-reference "Link to this heading")
###  `CheckMessage`[¶](https://docs.djangoproject.com/en/5.0/ref/checks/#checkmessage "Link to this heading")

_class_ CheckMessage(_level_ , _msg_ , _hint =None_, _obj =None_, _id =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/checks/messages/#CheckMessage)[¶](https://docs.djangoproject.com/en/5.0/ref/checks/#django.core.checks.CheckMessage "Link to this definition")

The warnings and errors raised by system checks must be instances of `CheckMessage`. An instance encapsulates a single reportable error or warning. It also provides context and hints applicable to the message, and a unique identifier that is used for filtering purposes.
Constructor arguments are:

`level`

The severity of the message. Use one of the predefined values: `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`. If the level is greater or equal to `ERROR`, then Django will prevent management commands from executing. Messages with level lower than `ERROR` (i.e. warnings) are reported to the console, but can be silenced.

`msg`

A short (less than 80 characters) string describing the problem. The string should _not_ contain newlines.

`hint`

A single-line string providing a hint for fixing the problem. If no hint can be provided, or the hint is self-evident from the error message, the hint can be omitted, or a value of `None` can be used.

`obj`

Optional. An object providing context for the message (for example, the model where the problem was discovered). The object should be a model, field, or manager or any other object that defines a `__str__()` method. The method is used while reporting all messages and its result precedes the message.

`id`

Optional string. A unique identifier for the issue. Identifiers should follow the pattern `applabel.X001`, where `X` is one of the letters `CEWID`, indicating the message severity (`C` for criticals, `E` for errors and so). The number can be allocated by the application, but should be unique within that application.
There are subclasses to make creating messages with common levels easier. When using them you can omit the `level` argument because it is implied by the class name.

_class_ Debug(_msg_ , _hint =None_, _obj =None_, _id =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/checks/messages/#Debug)[¶](https://docs.djangoproject.com/en/5.0/ref/checks/#django.core.checks.Debug "Link to this definition")


_class_ Info(_msg_ , _hint =None_, _obj =None_, _id =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/checks/messages/#Info)[¶](https://docs.djangoproject.com/en/5.0/ref/checks/#django.core.checks.Info "Link to this definition")


_class_ Warning(_msg_ , _hint=None obj=None_, _id=None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/checks/messages/#Warning)[¶](https://docs.djangoproject.com/en/5.0/ref/checks/#django.core.checks.Warning "Link to this definition")


_class_ Error(_msg_ , _hint =None_, _obj =None_, _id =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/checks/messages/#Error)[¶](https://docs.djangoproject.com/en/5.0/ref/checks/#django.core.checks.Error "Link to this definition")


_class_ Critical(_msg_ , _hint =None_, _obj =None_, _id =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/checks/messages/#Critical)[¶](https://docs.djangoproject.com/en/5.0/ref/checks/#django.core.checks.Critical "Link to this definition")
