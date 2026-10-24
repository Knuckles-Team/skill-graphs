## The add_argument() method[¶](https://docs.python.org/3/library/argparse.html#the-add-argument-method "Link to this heading")

ArgumentParser.add_argument(_name or flags..._, _*_[, _action_][, _nargs_][, _const_][, _default_][, _type_][, _choices_][, _required_][, _help_][, _metavar_][, _dest_][, _deprecated_])[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "Link to this definition")

Define how a single command-line argument should be parsed. Each parameter has its own more detailed description below, but in short they are:
  * [name or flags](https://docs.python.org/3/library/argparse.html#name-or-flags) - Either a name or a list of option strings, e.g. `'foo'` or `'-f', '--foo'`.
  * [action](https://docs.python.org/3/library/argparse.html#action) - The basic type of action to be taken when this argument is encountered at the command line.
  * [nargs](https://docs.python.org/3/library/argparse.html#nargs) - The number of command-line arguments that should be consumed.
  * [const](https://docs.python.org/3/library/argparse.html#const) - A constant value required by some [action](https://docs.python.org/3/library/argparse.html#action) and [nargs](https://docs.python.org/3/library/argparse.html#nargs) selections.
  * [default](https://docs.python.org/3/library/argparse.html#default) - The value produced if the argument is absent from the command line and if it is absent from the namespace object.
  * [type](https://docs.python.org/3/library/argparse.html#type) - The type to which the command-line argument should be converted.
  * [choices](https://docs.python.org/3/library/argparse.html#choices) - A sequence of the allowable values for the argument.
  * [required](https://docs.python.org/3/library/argparse.html#required) - Whether or not the command-line option may be omitted (optionals only).
  * [help](https://docs.python.org/3/library/argparse.html#help) - A brief description of what the argument does.
  * [metavar](https://docs.python.org/3/library/argparse.html#metavar) - A name for the argument in usage messages.
  * [dest](https://docs.python.org/3/library/argparse.html#dest) - The name of the attribute to be added to the object returned by [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args").
  * [deprecated](https://docs.python.org/3/library/argparse.html#deprecated) - Whether or not use of the argument is deprecated.


The following sections describe how each of these are used.
### name or flags[¶](https://docs.python.org/3/library/argparse.html#name-or-flags "Link to this heading")
The [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument") method must know whether an optional argument, like `-f` or `--foo`, or a positional argument, like a list of filenames, is expected. The first arguments passed to `add_argument()` must therefore be either a series of flags, or a simple argument name.
For example, an optional argument could be created like:
Copy```
>>> parser.add_argument('-f', '--foo')

```

while a positional argument could be created like:
Copy```
>>> parser.add_argument('bar')

```

When [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args") is called, optional arguments will be identified by the `-` prefix, and the remaining arguments will be assumed to be positional:
Copy```
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('-f', '--foo')
>>> parser.add_argument('bar')
>>> parser.parse_args(['BAR'])
Namespace(bar='BAR', foo=None)
>>> parser.parse_args(['BAR', '--foo', 'FOO'])
Namespace(bar='BAR', foo='FOO')
>>> parser.parse_args(['--foo', 'FOO'])
usage: PROG [-h] [-f FOO] bar
PROG: error: the following arguments are required: bar

```

By default, `argparse` automatically handles the internal naming and display names of arguments, simplifying the process without requiring additional configuration. As such, you do not need to specify the [dest](https://docs.python.org/3/library/argparse.html#dest) and [metavar](https://docs.python.org/3/library/argparse.html#metavar) parameters. For optional arguments, the [dest](https://docs.python.org/3/library/argparse.html#dest) parameter defaults to the argument name, with underscores `_` replacing hyphens `-`. The [metavar](https://docs.python.org/3/library/argparse.html#metavar) parameter defaults to the upper-cased name. For example:
Copy```
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('--foo-bar')
>>> parser.parse_args(['--foo-bar', 'FOO-BAR'])
Namespace(foo_bar='FOO-BAR')
>>> parser.print_help()
usage:  [-h] [--foo-bar FOO-BAR]

optional arguments:
 -h, --help  show this help message and exit
 --foo-bar FOO-BAR

```

### action[¶](https://docs.python.org/3/library/argparse.html#action "Link to this heading")
[`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") objects associate command-line arguments with actions. These actions can do just about anything with the command-line arguments associated with them, though most actions simply add an attribute to the object returned by [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args"). The `action` keyword argument specifies how the command-line arguments should be handled. The supplied actions are:
  * `'store'` - This just stores the argument’s value. This is the default action.
  * `'store_const'` - This stores the value specified by the [const](https://docs.python.org/3/library/argparse.html#const) keyword argument; note that the [const](https://docs.python.org/3/library/argparse.html#const) keyword argument defaults to `None`. The `'store_const'` action is most commonly used with optional arguments that specify some sort of flag. For example:
Copy```
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', action='store_const', const=42)
>>> parser.parse_args(['--foo'])
Namespace(foo=42)

```

  * `'store_true'` and `'store_false'` - These are special cases of `'store_const'` that respectively store the values `True` and `False` with default values of `False` and `True`:
Copy```
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', action='store_true')
>>> parser.add_argument('--bar', action='store_false')
>>> parser.add_argument('--baz', action='store_false')
>>> parser.parse_args('--foo --bar'.split())
Namespace(foo=True, bar=False, baz=True)

```

  * `'append'` - This appends each argument value to a list. It is useful for allowing an option to be specified multiple times. If the default value is a non-empty list, the parsed value will start with the default list’s elements and any values from the command line will be appended after those default values. Example usage:
Copy```
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', action='append', default=['0'])
>>> parser.parse_args('--foo 1 --foo 2'.split())
Namespace(foo=['0', '1', '2'])

```

  * `'append_const'` - This appends the value specified by the [const](https://docs.python.org/3/library/argparse.html#const) keyword argument to a list; note that the [const](https://docs.python.org/3/library/argparse.html#const) keyword argument defaults to `None`. The `'append_const'` action is typically useful when multiple arguments need to store constants to the same list. For example:
Copy```
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--str', dest='types', action='append_const', const=str)
>>> parser.add_argument('--int', dest='types', action='append_const', const=int)
>>> parser.parse_args('--str --int'.split())
Namespace(types=[<class 'str'>, <class 'int'>])

```

  * `'extend'` - This appends each item from a multi-value argument to a list. The `'extend'` action is typically used with the [nargs](https://docs.python.org/3/library/argparse.html#nargs) keyword argument value `'+'` or `'*'`. Note that when [nargs](https://docs.python.org/3/library/argparse.html#nargs) is `None` (the default) or `'?'`, each character of the argument string will be appended to the list. Example usage:
Copy```
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument("--foo", action="extend", nargs="+", type=str)
>>> parser.parse_args(["--foo", "f1", "--foo", "f2", "f3", "f4"])
Namespace(foo=['f1', 'f2', 'f3', 'f4'])

```

Added in version 3.8.
  * `'count'` - This counts the number of times an argument occurs. For example, this is useful for increasing verbosity levels:
Copy```
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--verbose', '-v', action='count', default=0)
>>> parser.parse_args(['-vvv'])
Namespace(verbose=3)

```

Note, the _default_ will be `None` unless explicitly set to _0_.
  * `'help'` - This prints a complete help message for all the options in the current parser and then exits. By default a help action is automatically added to the parser. See [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") for details of how the output is created.
  * `'version'` - This expects a `version=` keyword argument in the [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument") call, and prints version information and exits when invoked:
Copy```
>>> import argparse
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('--version', action='version', version='%(prog)s 2.0')
>>> parser.parse_args(['--version'])
PROG 2.0

```



You may also specify an arbitrary action by passing an [`Action`](https://docs.python.org/3/library/argparse.html#argparse.Action "argparse.Action") subclass (e.g. [`BooleanOptionalAction`](https://docs.python.org/3/library/argparse.html#argparse.BooleanOptionalAction "argparse.BooleanOptionalAction")) or other object that implements the same interface. Only actions that consume command-line arguments (e.g. `'store'`, `'append'`, `'extend'`, or custom actions with non-zero `nargs`) can be used with positional arguments.
The recommended way to create a custom action is to extend [`Action`](https://docs.python.org/3/library/argparse.html#argparse.Action "argparse.Action"), overriding the `__call__()` method and optionally the `__init__()` and `format_usage()` methods. You can also register custom actions using the [`register()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.register "argparse.ArgumentParser.register") method and reference them by their registered name.
An example of a custom action:
Copy```
>>> class FooAction(argparse.Action):
...     def __init__(self, option_strings, dest, nargs=None, **kwargs):
...         if nargs is not None:
...             raise ValueError("nargs not allowed")
...         super().__init__(option_strings, dest, **kwargs)
...     def __call__(self, parser, namespace, values, option_string=None):
...         print('%r %r %r' % (namespace, values, option_string))
...         setattr(namespace, self.dest, values)
...
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', action=FooAction)
>>> parser.add_argument('bar', action=FooAction)
>>> args = parser.parse_args('1 --foo 2'.split())
Namespace(bar=None, foo=None) '1' None
Namespace(bar='1', foo=None) '2' '--foo'
>>> args
Namespace(bar='1', foo='2')

```

For more details, see [`Action`](https://docs.python.org/3/library/argparse.html#argparse.Action "argparse.Action").
### nargs[¶](https://docs.python.org/3/library/argparse.html#nargs "Link to this heading")
[`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") objects usually associate a single command-line argument with a single action to be taken. The `nargs` keyword argument associates a different number of command-line arguments with a single action. See also [Specifying ambiguous arguments](https://docs.python.org/3/howto/argparse.html#specifying-ambiguous-arguments). The supported values are:
  * `N` (an integer). `N` arguments from the command line will be gathered together into a list. For example:
Copy```
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', nargs=2)
>>> parser.add_argument('bar', nargs=1)
>>> parser.parse_args('c --foo a b'.split())
Namespace(bar=['c'], foo=['a', 'b'])

```

Note that `nargs=1` produces a list of one item. This is different from the default, in which the item is produced by itself.


  * `'?'`. One argument will be consumed from the command line if possible, and produced as a single item. If no command-line argument is present, the value from [default](https://docs.python.org/3/library/argparse.html#default) will be produced. Note that for optional arguments, there is an additional case - the option string is present but not followed by a command-line argument. In this case the value from [const](https://docs.python.org/3/library/argparse.html#const) will be produced. Some examples to illustrate this:
Copy```
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', nargs='?', const='c', default='d')
>>> parser.add_argument('bar', nargs='?', default='d')
>>> parser.parse_args(['XX', '--foo', 'YY'])
Namespace(bar='XX', foo='YY')
>>> parser.parse_args(['XX', '--foo'])
Namespace(bar='XX', foo='c')
>>> parser.parse_args([])
Namespace(bar='d', foo='d')

```

One of the more common uses of `nargs='?'` is to allow optional input and output files:
Copy```
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('infile', nargs='?')
>>> parser.add_argument('outfile', nargs='?')
>>> parser.parse_args(['input.txt', 'output.txt'])
Namespace(infile='input.txt', outfile='output.txt')
>>> parser.parse_args(['input.txt'])
Namespace(infile='input.txt', outfile=None)
>>> parser.parse_args([])
Namespace(infile=None, outfile=None)

```



  * `'*'`. All command-line arguments present are gathered into a list. Note that it generally doesn’t make much sense to have more than one positional argument with `nargs='*'`, but multiple optional arguments with `nargs='*'` is possible. For example:
Copy```
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', nargs='*')
>>> parser.add_argument('--bar', nargs='*')
>>> parser.add_argument('baz', nargs='*')
>>> parser.parse_args('a b --foo x y --bar 1 2'.split())
Namespace(bar=['1', '2'], baz=['a', 'b'], foo=['x', 'y'])

```



  * `'+'`. Just like `'*'`, all command-line arguments present are gathered into a list. Additionally, an error message will be generated if there wasn’t at least one command-line argument present. For example:
Copy```
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('foo', nargs='+')
>>> parser.parse_args(['a', 'b'])
Namespace(foo=['a', 'b'])
>>> parser.parse_args([])
usage: PROG [-h] foo [foo ...]
PROG: error: the following arguments are required: foo

```



If the `nargs` keyword argument is not provided, the number of arguments consumed is determined by the [action](https://docs.python.org/3/library/argparse.html#action). Generally this means a single command-line argument will be consumed and a single item (not a list) will be produced. Actions that do not consume command-line arguments (e.g. `'store_const'`) set `nargs=0`.
### const[¶](https://docs.python.org/3/library/argparse.html#const "Link to this heading")
The `const` argument of [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument") is used to hold constant values that are not read from the command line but are required for the various [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") actions. The two most common uses of it are:
  * When [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument") is called with `action='store_const'` or `action='append_const'`. These actions add the `const` value to one of the attributes of the object returned by [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args"). See the [action](https://docs.python.org/3/library/argparse.html#action) description for examples. If `const` is not provided to `add_argument()`, it will receive a default value of `None`.
  * When [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument") is called with option strings (like `-f` or `--foo`) and `nargs='?'`. This creates an optional argument that can be followed by zero or one command-line arguments. When parsing the command line, if the option string is encountered with no command-line argument following it, the value from `const` will be used. See the [nargs](https://docs.python.org/3/library/argparse.html#nargs) description for examples.


Changed in version 3.11: `const=None` by default, including when `action='append_const'` or `action='store_const'`.
### default[¶](https://docs.python.org/3/library/argparse.html#default "Link to this heading")
All optional arguments and some positional arguments may be omitted at the command line. The `default` keyword argument of [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument"), whose value defaults to `None`, specifies what value should be used if the command-line argument is not present. For optional arguments, the `default` value is used when the option string was not present at the command line:
Copy```
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', default=42)
>>> parser.parse_args(['--foo', '2'])
Namespace(foo='2')
>>> parser.parse_args([])
Namespace(foo=42)

```

If the target namespace already has an attribute set, the action _default_ will not overwrite it:
Copy```
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', default=42)
>>> parser.parse_args([], namespace=argparse.Namespace(foo=101))
Namespace(foo=101)

```

If the `default` value is a string, the parser parses the value as if it were a command-line argument. In particular, the parser applies any [type](https://docs.python.org/3/library/argparse.html#type) conversion argument, if provided, before setting the attribute on the [`Namespace`](https://docs.python.org/3/library/argparse.html#argparse.Namespace "argparse.Namespace") return value. Otherwise, the parser uses the value as is:
Copy```
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--length', default='10', type=int)
>>> parser.add_argument('--width', default=10.5, type=int)
>>> parser.parse_args()
Namespace(length=10, width=10.5)

```

For positional arguments with [nargs](https://docs.python.org/3/library/argparse.html#nargs) equal to `?` or `*`, the `default` value is used when no command-line argument was present:
Copy```
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('foo', nargs='?', default=42)
>>> parser.parse_args(['a'])
Namespace(foo='a')
>>> parser.parse_args([])
Namespace(foo=42)

```

For [required](https://docs.python.org/3/library/argparse.html#required) arguments, the `default` value is ignored. For example, this applies to positional arguments with [nargs](https://docs.python.org/3/library/argparse.html#nargs) values other than `?` or `*`, or optional arguments marked as `required=True`.
Providing `default=argparse.SUPPRESS` causes no attribute to be added if the command-line argument was not present:
Copy```
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', default=argparse.SUPPRESS)
>>> parser.parse_args([])
Namespace()
>>> parser.parse_args(['--foo', '1'])
Namespace(foo='1')

```

### type[¶](https://docs.python.org/3/library/argparse.html#type "Link to this heading")
By default, the parser reads command-line arguments in as simple strings. However, quite often the command-line string should instead be interpreted as another type, such as a [`float`](https://docs.python.org/3/library/functions.html#float "float") or [`int`](https://docs.python.org/3/library/functions.html#int "int"). The `type` keyword for [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument") allows any necessary type-checking and type conversions to be performed.
If the [type](https://docs.python.org/3/library/argparse.html#type) keyword is used with the [default](https://docs.python.org/3/library/argparse.html#default) keyword, the type converter is only applied if the default is a string.
The argument to `type` can be a callable that accepts a single string or the name of a registered type (see [`register()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.register "argparse.ArgumentParser.register")) If the function raises [`ArgumentTypeError`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentTypeError "argparse.ArgumentTypeError"), [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError"), or [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError"), the exception is caught and a nicely formatted error message is displayed. Other exception types are not handled.
Common built-in types and functions can be used as type converters:
Copy```
import argparse
import pathlib

parser = argparse.ArgumentParser()
parser.add_argument('count', type=int)
parser.add_argument('distance', type=float)
parser.add_argument('street', type=ascii)
parser.add_argument('code_point', type=ord)
parser.add_argument('datapath', type=pathlib.Path)

```

User defined functions can be used as well:
Copy```
>>> def hyphenated(string):
...     return '-'.join([word[:4] for word in string.casefold().split()])
...
>>> parser = argparse.ArgumentParser()
>>> _ = parser.add_argument('short_title', type=hyphenated)
>>> parser.parse_args(['"The Tale of Two Cities"'])
Namespace(short_title='"the-tale-of-two-citi')

```

The [`bool()`](https://docs.python.org/3/library/functions.html#bool "bool") function is not recommended as a type converter. All it does is convert empty strings to `False` and non-empty strings to `True`. This is usually not what is desired.
In general, the `type` keyword is a convenience that should only be used for simple conversions that can only raise one of the three supported exceptions. Anything with more interesting error-handling or resource management should be done downstream after the arguments are parsed.
For example, JSON or YAML conversions have complex error cases that require better reporting than can be given by the `type` keyword. A [`JSONDecodeError`](https://docs.python.org/3/library/json.html#json.JSONDecodeError "json.JSONDecodeError") would not be well formatted and a [`FileNotFoundError`](https://docs.python.org/3/library/exceptions.html#FileNotFoundError "FileNotFoundError") exception would not be handled at all.
Even [`FileType`](https://docs.python.org/3/library/argparse.html#argparse.FileType "argparse.FileType") has its limitations for use with the `type` keyword. If one argument uses `FileType` and then a subsequent argument fails, an error is reported but the file is not automatically closed. In this case, it would be better to wait until after the parser has run and then use the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)-statement to manage the files.
For type checkers that simply check against a fixed set of values, consider using the [choices](https://docs.python.org/3/library/argparse.html#choices) keyword instead.
### choices[¶](https://docs.python.org/3/library/argparse.html#choices "Link to this heading")
Some command-line arguments should be selected from a restricted set of values. These can be handled by passing a sequence object as the _choices_ keyword argument to [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument"). When the command line is parsed, argument values will be checked, and an error message will be displayed if the argument was not one of the acceptable values:
Copy```
>>> parser = argparse.ArgumentParser(prog='game.py')
>>> parser.add_argument('move', choices=['rock', 'paper', 'scissors'])
>>> parser.parse_args(['rock'])
Namespace(move='rock')
>>> parser.parse_args(['fire'])
usage: game.py [-h] {rock,paper,scissors}
game.py: error: argument move: invalid choice: 'fire' (choose from 'rock',
'paper', 'scissors')

```

Any sequence can be passed as the _choices_ value, so [`list`](https://docs.python.org/3/library/stdtypes.html#list "list") objects, [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "tuple") objects, and custom sequences are all supported.
Use of [`enum.Enum`](https://docs.python.org/3/library/enum.html#enum.Enum "enum.Enum") is not recommended because it is difficult to control its appearance in usage, help, and error messages.
Note that _choices_ are checked after any [type](https://docs.python.org/3/library/argparse.html#type) conversions have been performed, so objects in _choices_ should match the [type](https://docs.python.org/3/library/argparse.html#type) specified. This can make _choices_ appear unfamiliar in usage, help, or error messages.
To keep _choices_ user-friendly, consider a custom type wrapper that converts and formats values, or omit [type](https://docs.python.org/3/library/argparse.html#type) and handle conversion in your application code.
Formatted choices override the default _metavar_ which is normally derived from _dest_. This is usually what you want because the user never sees the _dest_ parameter. If this display isn’t desirable (perhaps because there are many choices), just specify an explicit [metavar](https://docs.python.org/3/library/argparse.html#metavar).
### required[¶](https://docs.python.org/3/library/argparse.html#required "Link to this heading")
In general, the `argparse` module assumes that flags like `-f` and `--bar` indicate _optional_ arguments, which can always be omitted at the command line. To make an option _required_ , `True` can be specified for the `required=` keyword argument to [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument"):
Copy```
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', required=True)
>>> parser.parse_args(['--foo', 'BAR'])
Namespace(foo='BAR')
>>> parser.parse_args([])
usage: [-h] --foo FOO
: error: the following arguments are required: --foo

```

As the example shows, if an option is marked as `required`, [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args") will report an error if that option is not present at the command line.
Note
Required options are generally considered bad form because users expect _options_ to be _optional_ , and thus they should be avoided when possible.
### help[¶](https://docs.python.org/3/library/argparse.html#help "Link to this heading")
The `help` value is a string containing a brief description of the argument. When a user requests help (usually by using `-h` or `--help` at the command line), these `help` descriptions will be displayed with each argument.
The `help` strings can include various format specifiers to avoid repetition of things like the program name or the argument [default](https://docs.python.org/3/library/argparse.html#default). The available specifiers include the program name, `%(prog)s` and most keyword arguments to [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument"), e.g. `%(default)s`, `%(type)s`, etc.:
Copy```
>>> parser = argparse.ArgumentParser(prog='frobble')
>>> parser.add_argument('bar', nargs='?', type=int, default=42,
...                     help='the bar to %(prog)s (default: %(default)s)')
>>> parser.print_help()
usage: frobble [-h] [bar]

positional arguments:
 bar     the bar to frobble (default: 42)

options:
 -h, --help  show this help message and exit

```

As the help string supports %-formatting, if you want a literal `%` to appear in the help string, you must escape it as `%%`.
`argparse` supports silencing the help entry for certain options, by setting the `help` value to `argparse.SUPPRESS`:
Copy```
>>> parser = argparse.ArgumentParser(prog='frobble')
>>> parser.add_argument('--foo', help=argparse.SUPPRESS)
>>> parser.print_help()
usage: frobble [-h]

options:
  -h, --help  show this help message and exit

```

### metavar[¶](https://docs.python.org/3/library/argparse.html#metavar "Link to this heading")
When [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") generates help messages, it needs some way to refer to each expected argument. By default, `ArgumentParser` objects use the [dest](https://docs.python.org/3/library/argparse.html#dest) value as the “name” of each object. By default, for positional argument actions, the [dest](https://docs.python.org/3/library/argparse.html#dest) value is used directly, and for optional argument actions, the [dest](https://docs.python.org/3/library/argparse.html#dest) value is uppercased. So, a single positional argument with `dest='bar'` will be referred to as `bar`. A single optional argument `--foo` that should be followed by a single command-line argument will be referred to as `FOO`. An example:
Copy```
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo')
>>> parser.add_argument('bar')
>>> parser.parse_args('X --foo Y'.split())
Namespace(bar='X', foo='Y')
>>> parser.print_help()
usage:  [-h] [--foo FOO] bar

positional arguments:
 bar

options:
 -h, --help  show this help message and exit
 --foo FOO

```

An alternative name can be specified with `metavar`:
Copy```
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', metavar='YYY')
>>> parser.add_argument('bar', metavar='XXX')
>>> parser.parse_args('X --foo Y'.split())
Namespace(bar='X', foo='Y')
>>> parser.print_help()
usage:  [-h] [--foo YYY] XXX

positional arguments:
 XXX

options:
 -h, --help  show this help message and exit
 --foo YYY

```

Note that `metavar` only changes the _displayed_ name - the name of the attribute on the [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args") object is still determined by the [dest](https://docs.python.org/3/library/argparse.html#dest) value.
Different values of `nargs` may cause the metavar to be used multiple times. Providing a tuple to `metavar` specifies a different display for each of the arguments:
Copy```
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('-x', nargs=2)
>>> parser.add_argument('--foo', nargs=2, metavar=('bar', 'baz'))
>>> parser.print_help()
usage: PROG [-h] [-x X X] [--foo bar baz]

options:
 -h, --help     show this help message and exit
 -x X X
 --foo bar baz

```

### dest[¶](https://docs.python.org/3/library/argparse.html#dest "Link to this heading")
Most [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") actions add some value as an attribute of the object returned by [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args"). The name of this attribute is determined by the `dest` keyword argument of [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument"). For positional argument actions, `dest` is normally supplied as the first argument to `add_argument()`:
Copy```
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('bar')
>>> parser.parse_args(['XXX'])
Namespace(bar='XXX')

```

For optional argument actions, the value of `dest` is normally inferred from the option strings. [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") generates the value of `dest` by taking the first long option string and stripping away the initial `--` string. If no long option strings were supplied, `dest` will be derived from the first short option string by stripping the initial `-` character. Any internal `-` characters will be converted to `_` characters to make sure the string is a valid attribute name. The examples below illustrate this behavior:
Copy```
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('-f', '--foo-bar', '--foo')
>>> parser.add_argument('-x', '-y')
>>> parser.parse_args('-f 1 -x 2'.split())
Namespace(foo_bar='1', x='2')
>>> parser.parse_args('--foo 1 -y 2'.split())
Namespace(foo_bar='1', x='2')

```

`dest` allows a custom attribute name to be provided:
Copy```
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', dest='bar')
>>> parser.parse_args('--foo XXX'.split())
Namespace(bar='XXX')

```

### deprecated[¶](https://docs.python.org/3/library/argparse.html#deprecated "Link to this heading")
During a project’s lifetime, some arguments may need to be removed from the command line. Before removing them, you should inform your users that the arguments are deprecated and will be removed. The `deprecated` keyword argument of [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument"), which defaults to `False`, specifies if the argument is deprecated and will be removed in the future. For arguments, if `deprecated` is `True`, then a warning will be printed to [`sys.stderr`](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr") when the argument is used:
Copy```
>>> import argparse
>>> parser = argparse.ArgumentParser(prog='snake.py')
>>> parser.add_argument('--legs', default=0, type=int, deprecated=True)
>>> parser.parse_args([])
Namespace(legs=0)
>>> parser.parse_args(['--legs', '4'])
snake.py: warning: option '--legs' is deprecated
Namespace(legs=4)

```

Added in version 3.13.
### Action classes[¶](https://docs.python.org/3/library/argparse.html#action-classes "Link to this heading")
`Action` classes implement the Action API, a callable which returns a callable which processes arguments from the command-line. Any object which follows this API may be passed as the `action` parameter to [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument").

_class_ argparse.Action(_option_strings_ , _dest_ , _nargs =None_, _const =None_, _default =None_, _type =None_, _choices =None_, _required =False_, _help =None_, _metavar =None_)[¶](https://docs.python.org/3/library/argparse.html#argparse.Action "Link to this definition")

`Action` objects are used by an [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") to represent the information needed to parse a single argument from one or more strings from the command line. The `Action` class must accept the two positional arguments plus any keyword arguments passed to [`ArgumentParser.add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument") except for the `action` itself.
Instances of `Action` (or return value of any callable to the `action` parameter) should have attributes `dest`, `option_strings`, `default`, `type`, `required`, `help`, etc. defined. The easiest way to ensure these attributes are defined is to call `Action.__init__()`.

__call__(_parser_ , _namespace_ , _values_ , _option_string =None_)[¶](https://docs.python.org/3/library/argparse.html#argparse.Action.__call__ "Link to this definition")

`Action` instances should be callable, so subclasses must override the `__call__()` method, which should accept four parameters:
  * _parser_ - The [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") object which contains this action.
  * _namespace_ - The [`Namespace`](https://docs.python.org/3/library/argparse.html#argparse.Namespace "argparse.Namespace") object that will be returned by [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args"). Most actions add an attribute to this object using [`setattr()`](https://docs.python.org/3/library/functions.html#setattr "setattr").
  * _values_ - The associated command-line arguments, with any type conversions applied. Type conversions are specified with the [type](https://docs.python.org/3/library/argparse.html#type) keyword argument to [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument").
  * _option_string_ - The option string that was used to invoke this action. The `option_string` argument is optional, and will be absent if the action is associated with a positional argument.


The `__call__()` method may perform arbitrary actions, but will typically set attributes on the `namespace` based on `dest` and `values`.

format_usage()[¶](https://docs.python.org/3/library/argparse.html#argparse.Action.format_usage "Link to this definition")

`Action` subclasses can define a `format_usage()` method that takes no argument and return a string which will be used when printing the usage of the program. If such method is not provided, a sensible default will be used.

_class_ argparse.BooleanOptionalAction[¶](https://docs.python.org/3/library/argparse.html#argparse.BooleanOptionalAction "Link to this definition")

A subclass of [`Action`](https://docs.python.org/3/library/argparse.html#argparse.Action "argparse.Action") for handling boolean flags with positive and negative options. Adding a single argument such as `--foo` automatically creates both `--foo` and `--no-foo` options, storing `True` and `False` respectively:
Copy```
>>> import argparse
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', action=argparse.BooleanOptionalAction)
>>> parser.parse_args(['--no-foo'])
Namespace(foo=False)

```

Added in version 3.9.
