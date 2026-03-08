## Custom String Formatting[¶](https://docs.python.org/3/library/string.html#custom-string-formatting "Link to this heading")
The built-in string class provides the ability to do complex variable substitutions and value formatting via the [`format()`](https://docs.python.org/3/library/stdtypes.html#str.format "str.format") method described in [**PEP 3101**](https://peps.python.org/pep-3101/). The [`Formatter`](https://docs.python.org/3/library/string.html#string.Formatter "string.Formatter") class in the `string` module allows you to create and customize your own string formatting behaviors using the same implementation as the built-in `format()` method.

_class_ string.Formatter[¶](https://docs.python.org/3/library/string.html#string.Formatter "Link to this definition")

The `Formatter` class has the following public methods:

format(_format_string_ , _/_ , _* args_, _** kwargs_)[¶](https://docs.python.org/3/library/string.html#string.Formatter.format "Link to this definition")

The primary API method. It takes a format string and an arbitrary set of positional and keyword arguments. It is just a wrapper that calls [`vformat()`](https://docs.python.org/3/library/string.html#string.Formatter.vformat "string.Formatter.vformat").
Changed in version 3.7: A format string argument is now [positional-only](https://docs.python.org/3/glossary.html#positional-only-parameter).

vformat(_format_string_ , _args_ , _kwargs_)[¶](https://docs.python.org/3/library/string.html#string.Formatter.vformat "Link to this definition")

This function does the actual work of formatting. It is exposed as a separate function for cases where you want to pass in a predefined dictionary of arguments, rather than unpacking and repacking the dictionary as individual arguments using the `*args` and `**kwargs` syntax. `vformat()` does the work of breaking up the format string into character data and replacement fields. It calls the various methods described below.
In addition, the `Formatter` defines a number of methods that are intended to be replaced by subclasses:

parse(_format_string_)[¶](https://docs.python.org/3/library/string.html#string.Formatter.parse "Link to this definition")

Loop over the format_string and return an iterable of tuples (_literal_text_ , _field_name_ , _format_spec_ , _conversion_). This is used by [`vformat()`](https://docs.python.org/3/library/string.html#string.Formatter.vformat "string.Formatter.vformat") to break the string into either literal text, or replacement fields.
The values in the tuple conceptually represent a span of literal text followed by a single replacement field. If there is no literal text (which can happen if two replacement fields occur consecutively), then _literal_text_ will be a zero-length string. If there is no replacement field, then the values of _field_name_ , _format_spec_ and _conversion_ will be `None`. The value of _field_name_ is unmodified and auto-numbering of non-numbered positional fields is done by [`vformat()`](https://docs.python.org/3/library/string.html#string.Formatter.vformat "string.Formatter.vformat").

get_field(_field_name_ , _args_ , _kwargs_)[¶](https://docs.python.org/3/library/string.html#string.Formatter.get_field "Link to this definition")

Given _field_name_ , convert it to an object to be formatted. Auto-numbering of _field_name_ returned from [`parse()`](https://docs.python.org/3/library/string.html#string.Formatter.parse "string.Formatter.parse") is done by [`vformat()`](https://docs.python.org/3/library/string.html#string.Formatter.vformat "string.Formatter.vformat") before calling this method. Returns a tuple (obj, used_key). The default version takes strings of the form defined in [**PEP 3101**](https://peps.python.org/pep-3101/), such as “0[name]” or “label.title”. _args_ and _kwargs_ are as passed in to `vformat()`. The return value _used_key_ has the same meaning as the _key_ parameter to [`get_value()`](https://docs.python.org/3/library/string.html#string.Formatter.get_value "string.Formatter.get_value").

get_value(_key_ , _args_ , _kwargs_)[¶](https://docs.python.org/3/library/string.html#string.Formatter.get_value "Link to this definition")

Retrieve a given field value. The _key_ argument will be either an integer or a string. If it is an integer, it represents the index of the positional argument in _args_ ; if it is a string, then it represents a named argument in _kwargs_.
The _args_ parameter is set to the list of positional arguments to [`vformat()`](https://docs.python.org/3/library/string.html#string.Formatter.vformat "string.Formatter.vformat"), and the _kwargs_ parameter is set to the dictionary of keyword arguments.
For compound field names, these functions are only called for the first component of the field name; subsequent components are handled through normal attribute and indexing operations.
So for example, the field expression ‘0.name’ would cause `get_value()` to be called with a _key_ argument of 0. The `name` attribute will be looked up after `get_value()` returns by calling the built-in [`getattr()`](https://docs.python.org/3/library/functions.html#getattr "getattr") function.
If the index or keyword refers to an item that does not exist, then an [`IndexError`](https://docs.python.org/3/library/exceptions.html#IndexError "IndexError") or [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "KeyError") should be raised.

check_unused_args(_used_args_ , _args_ , _kwargs_)[¶](https://docs.python.org/3/library/string.html#string.Formatter.check_unused_args "Link to this definition")

Implement checking for unused arguments if desired. The arguments to this function is the set of all argument keys that were actually referred to in the format string (integers for positional arguments, and strings for named arguments), and a reference to the _args_ and _kwargs_ that was passed to vformat. The set of unused args can be calculated from these parameters. `check_unused_args()` is assumed to raise an exception if the check fails.

format_field(_value_ , _format_spec_)[¶](https://docs.python.org/3/library/string.html#string.Formatter.format_field "Link to this definition")

`format_field()` simply calls the global [`format()`](https://docs.python.org/3/library/functions.html#format "format") built-in. The method is provided so that subclasses can override it.

convert_field(_value_ , _conversion_)[¶](https://docs.python.org/3/library/string.html#string.Formatter.convert_field "Link to this definition")

Converts the value (returned by [`get_field()`](https://docs.python.org/3/library/string.html#string.Formatter.get_field "string.Formatter.get_field")) given a conversion type (as in the tuple returned by the [`parse()`](https://docs.python.org/3/library/string.html#string.Formatter.parse "string.Formatter.parse") method). The default version understands ‘s’ (str), ‘r’ (repr) and ‘a’ (ascii) conversion types.
