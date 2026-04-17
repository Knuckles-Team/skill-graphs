#  `argparse` — Parser for command-line options, arguments and subcommands[¶](https://docs.python.org/3/library/argparse.html#module-argparse "Link to this heading")
Added in version 3.2.
**Source code:**
Note
While `argparse` is the default recommended standard library module for implementing basic command line applications, authors with more exacting requirements for exactly how their command line applications behave may find it doesn’t provide the necessary level of control. Refer to [Choosing an argument parsing library](https://docs.python.org/3/library/optparse.html#choosing-an-argument-parser) for alternatives to consider when `argparse` doesn’t support behaviors that the application requires (such as entirely disabling support for interspersed options and positional arguments, or accepting option parameter values that start with `-` even when they correspond to another defined option).
* * *
Tutorial
This page contains the API reference information. For a more gentle introduction to Python command-line parsing, have a look at the [argparse tutorial](https://docs.python.org/3/howto/argparse.html#argparse-tutorial).
The `argparse` module makes it easy to write user-friendly command-line interfaces. The program defines what arguments it requires, and `argparse` will figure out how to parse those out of [`sys.argv`](https://docs.python.org/3/library/sys.html#sys.argv "sys.argv"). The `argparse` module also automatically generates help and usage messages. The module will also issue errors when users give the program invalid arguments.
The `argparse` module’s support for command-line interfaces is built around an instance of [`argparse.ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser"). It is a container for argument specifications and has options that apply to the parser as whole:
Copy```
parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')

```

The [`ArgumentParser.add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument") method attaches individual argument specifications to the parser. It supports positional arguments, options that accept values, and on/off flags:
Copy```
parser.add_argument('filename')           # positional argument
parser.add_argument('-c', '--count')      # option that takes a value
parser.add_argument('-v', '--verbose',
                    action='store_true')  # on/off flag

```

The [`ArgumentParser.parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args") method runs the parser and places the extracted data in a [`argparse.Namespace`](https://docs.python.org/3/library/argparse.html#argparse.Namespace "argparse.Namespace") object:
Copy```
args = parser.parse_args()
print(args.filename, args.count, args.verbose)

```

Note
If you’re looking for a guide about how to upgrade [`optparse`](https://docs.python.org/3/library/optparse.html#module-optparse "optparse: Command-line option parsing library.") code to `argparse`, see [Upgrading Optparse Code](https://docs.python.org/3/howto/argparse-optparse.html#upgrading-optparse-code).
## ArgumentParser objects[¶](https://docs.python.org/3/library/argparse.html#argumentparser-objects "Link to this heading")

_class_ argparse.ArgumentParser(_prog =None_, _usage =None_, _description =None_, _epilog =None_, _parents =[]_, _formatter_class =argparse.HelpFormatter_, _prefix_chars ='-'_, _fromfile_prefix_chars =None_, _argument_default =None_, _conflict_handler ='error'_, _add_help =True_, _allow_abbrev =True_, _exit_on_error =True_, _*_ , _suggest_on_error =False_, _color =True_)[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "Link to this definition")

Create a new `ArgumentParser` object. All parameters should be passed as keyword arguments. Each parameter has its own more detailed description below, but in short they are:
  * [prog](https://docs.python.org/3/library/argparse.html#prog) - The name of the program (default: generated from the `__main__` module attributes and `sys.argv[0]`)
  * [usage](https://docs.python.org/3/library/argparse.html#usage) - The string describing the program usage (default: generated from arguments added to parser)
  * [description](https://docs.python.org/3/library/argparse.html#description) - Text to display before the argument help (by default, no text)
  * [epilog](https://docs.python.org/3/library/argparse.html#epilog) - Text to display after the argument help (by default, no text)
  * [parents](https://docs.python.org/3/library/argparse.html#parents) - A list of `ArgumentParser` objects whose arguments should also be included
  * [formatter_class](https://docs.python.org/3/library/argparse.html#formatter-class) - A class for customizing the help output
  * [prefix_chars](https://docs.python.org/3/library/argparse.html#prefix-chars) - The set of characters that prefix optional arguments (default: ‘-‘)
  * [fromfile_prefix_chars](https://docs.python.org/3/library/argparse.html#fromfile-prefix-chars) - The set of characters that prefix files from which additional arguments should be read (default: `None`)
  * [argument_default](https://docs.python.org/3/library/argparse.html#argument-default) - The global default value for arguments (default: `None`)
  * [conflict_handler](https://docs.python.org/3/library/argparse.html#conflict-handler) - The strategy for resolving conflicting optionals (usually unnecessary)
  * [add_help](https://docs.python.org/3/library/argparse.html#add-help) - Add a `-h/--help` option to the parser (default: `True`)
  * [allow_abbrev](https://docs.python.org/3/library/argparse.html#allow-abbrev) - Allows long options to be abbreviated if the abbreviation is unambiguous (default: `True`)
  * [exit_on_error](https://docs.python.org/3/library/argparse.html#exit-on-error) - Determines whether or not `ArgumentParser` exits with error info when an error occurs. (default: `True`)
  * [suggest_on_error](https://docs.python.org/3/library/argparse.html#suggest-on-error) - Enables suggestions for mistyped argument choices and subparser names (default: `False`)
  * [color](https://docs.python.org/3/library/argparse.html#color) - Allow color output (default: `True`)


Changed in version 3.5: _allow_abbrev_ parameter was added.
Changed in version 3.8: In previous versions, _allow_abbrev_ also disabled grouping of short flags such as `-vv` to mean `-v -v`.
Changed in version 3.9: _exit_on_error_ parameter was added.
Changed in version 3.14: _suggest_on_error_ and _color_ parameters were added.
The following sections describe how each of these are used.
### prog[¶](https://docs.python.org/3/library/argparse.html#prog "Link to this heading")
By default, [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") calculates the name of the program to display in help messages depending on the way the Python interpreter was run:
  * The [`base name`](https://docs.python.org/3/library/os.path.html#os.path.basename "os.path.basename") of `sys.argv[0]` if a file was passed as argument.
  * The Python interpreter name followed by `sys.argv[0]` if a directory or a zipfile was passed as argument.
  * The Python interpreter name followed by `-m` followed by the module or package name if the [`-m`](https://docs.python.org/3/using/cmdline.html#cmdoption-m) option was used.


This default is almost always desirable because it will make the help messages match the string that was used to invoke the program on the command line. However, to change this default behavior, another value can be supplied using the `prog=` argument to [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser"):
Copy```
>>> parser = argparse.ArgumentParser(prog='myprogram')
>>> parser.print_help()
usage: myprogram [-h]

options:
 -h, --help  show this help message and exit

```

Note that the program name, whether determined from `sys.argv[0]`, from the `__main__` module attributes or from the `prog=` argument, is available to help messages using the `%(prog)s` format specifier.
Copy```
>>> parser = argparse.ArgumentParser(prog='myprogram')
>>> parser.add_argument('--foo', help='foo of the %(prog)s program')
>>> parser.print_help()
usage: myprogram [-h] [--foo FOO]

options:
 -h, --help  show this help message and exit
 --foo FOO   foo of the myprogram program

```

Changed in version 3.14: The default `prog` value now reflects how `__main__` was actually executed, rather than always being `os.path.basename(sys.argv[0])`.
### usage[¶](https://docs.python.org/3/library/argparse.html#usage "Link to this heading")
By default, [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") calculates the usage message from the arguments it contains. The default message can be overridden with the `usage=` keyword argument:
Copy```
>>> parser = argparse.ArgumentParser(prog='PROG', usage='%(prog)s [options]')
>>> parser.add_argument('--foo', nargs='?', help='foo help')
>>> parser.add_argument('bar', nargs='+', help='bar help')
>>> parser.print_help()
usage: PROG [options]

positional arguments:
 bar          bar help

options:
 -h, --help   show this help message and exit
 --foo [FOO]  foo help

```

The `%(prog)s` format specifier is available to fill in the program name in your usage messages.
When a custom usage message is specified for the main parser, you may also want to consider passing the `prog` argument to [`add_subparsers()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_subparsers "argparse.ArgumentParser.add_subparsers") or the `prog` and the `usage` arguments to `add_parser()`, to ensure consistent command prefixes and usage information across subparsers.
### description[¶](https://docs.python.org/3/library/argparse.html#description "Link to this heading")
Most calls to the [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") constructor will use the `description=` keyword argument. This argument gives a brief description of what the program does and how it works. In help messages, the description is displayed between the command-line usage string and the help messages for the various arguments.
By default, the description will be line-wrapped so that it fits within the given space. To change this behavior, see the [formatter_class](https://docs.python.org/3/library/argparse.html#formatter-class) argument.
### epilog[¶](https://docs.python.org/3/library/argparse.html#epilog "Link to this heading")
Some programs like to display additional description of the program after the description of the arguments. Such text can be specified using the `epilog=` argument to [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser"):
Copy```
>>> parser = argparse.ArgumentParser(
...     description='A foo that bars',
...     epilog="And that's how you'd foo a bar")
>>> parser.print_help()
usage: argparse.py [-h]

A foo that bars

options:
 -h, --help  show this help message and exit

And that's how you'd foo a bar

```

As with the [description](https://docs.python.org/3/library/argparse.html#description) argument, the `epilog=` text is by default line-wrapped, but this behavior can be adjusted with the [formatter_class](https://docs.python.org/3/library/argparse.html#formatter-class) argument to [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser").
### parents[¶](https://docs.python.org/3/library/argparse.html#parents "Link to this heading")
Sometimes, several parsers share a common set of arguments. Rather than repeating the definitions of these arguments, a single parser with all the shared arguments and passed to `parents=` argument to [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") can be used. The `parents=` argument takes a list of `ArgumentParser` objects, collects all the positional and optional actions from them, and adds these actions to the `ArgumentParser` object being constructed:
Copy```
>>> parent_parser = argparse.ArgumentParser(add_help=False)
>>> parent_parser.add_argument('--parent', type=int)

>>> foo_parser = argparse.ArgumentParser(parents=[parent_parser])
>>> foo_parser.add_argument('foo')
>>> foo_parser.parse_args(['--parent', '2', 'XXX'])
Namespace(foo='XXX', parent=2)

>>> bar_parser = argparse.ArgumentParser(parents=[parent_parser])
>>> bar_parser.add_argument('--bar')
>>> bar_parser.parse_args(['--bar', 'YYY'])
Namespace(bar='YYY', parent=None)

```

Note that most parent parsers will specify `add_help=False`. Otherwise, the [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") will see two `-h/--help` options (one in the parent and one in the child) and raise an error.
Note
You must fully initialize the parsers before passing them via `parents=`. If you change the parent parsers after the child parser, those changes will not be reflected in the child.
### formatter_class[¶](https://docs.python.org/3/library/argparse.html#formatter-class "Link to this heading")
[`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") objects allow the help formatting to be customized by specifying an alternate formatting class. Currently, there are four such classes:

_class_ argparse.RawDescriptionHelpFormatter[¶](https://docs.python.org/3/library/argparse.html#argparse.RawDescriptionHelpFormatter "Link to this definition")


_class_ argparse.RawTextHelpFormatter[¶](https://docs.python.org/3/library/argparse.html#argparse.RawTextHelpFormatter "Link to this definition")


_class_ argparse.ArgumentDefaultsHelpFormatter[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentDefaultsHelpFormatter "Link to this definition")


_class_ argparse.MetavarTypeHelpFormatter[¶](https://docs.python.org/3/library/argparse.html#argparse.MetavarTypeHelpFormatter "Link to this definition")

[`RawDescriptionHelpFormatter`](https://docs.python.org/3/library/argparse.html#argparse.RawDescriptionHelpFormatter "argparse.RawDescriptionHelpFormatter") and [`RawTextHelpFormatter`](https://docs.python.org/3/library/argparse.html#argparse.RawTextHelpFormatter "argparse.RawTextHelpFormatter") give more control over how textual descriptions are displayed. By default, [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") objects line-wrap the [description](https://docs.python.org/3/library/argparse.html#description) and [epilog](https://docs.python.org/3/library/argparse.html#epilog) texts in command-line help messages:
Copy```
>>> parser = argparse.ArgumentParser(
...     prog='PROG',
...     description='''this description
...         was indented weird
...             but that is okay''',
...     epilog='''
...             likewise for this epilog whose whitespace will
...         be cleaned up and whose words will be wrapped
...         across a couple lines''')
>>> parser.print_help()
usage: PROG [-h]

this description was indented weird but that is okay

options:
 -h, --help  show this help message and exit

likewise for this epilog whose whitespace will be cleaned up and whose words
will be wrapped across a couple lines

```

Passing [`RawDescriptionHelpFormatter`](https://docs.python.org/3/library/argparse.html#argparse.RawDescriptionHelpFormatter "argparse.RawDescriptionHelpFormatter") as `formatter_class=` indicates that [description](https://docs.python.org/3/library/argparse.html#description) and [epilog](https://docs.python.org/3/library/argparse.html#epilog) are already correctly formatted and should not be line-wrapped:
Copy```
>>> parser = argparse.ArgumentParser(
...     prog='PROG',
...     formatter_class=argparse.RawDescriptionHelpFormatter,
...     description=textwrap.dedent('''\
...         Please do not mess up this text!
...         --------------------------------
...             I have indented it
...             exactly the way
...             I want it
...         '''))
>>> parser.print_help()
usage: PROG [-h]

Please do not mess up this text!
--------------------------------
   I have indented it
   exactly the way
   I want it

options:
 -h, --help  show this help message and exit

```

[`RawTextHelpFormatter`](https://docs.python.org/3/library/argparse.html#argparse.RawTextHelpFormatter "argparse.RawTextHelpFormatter") maintains whitespace for all sorts of help text, including argument descriptions. However, multiple newlines are replaced with one. If you wish to preserve multiple blank lines, add spaces between the newlines.
[`ArgumentDefaultsHelpFormatter`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentDefaultsHelpFormatter "argparse.ArgumentDefaultsHelpFormatter") automatically adds information about default values to each of the argument help messages:
Copy```
>>> parser = argparse.ArgumentParser(
...     prog='PROG',
...     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
>>> parser.add_argument('--foo', type=int, default=42, help='FOO!')
>>> parser.add_argument('bar', nargs='*', default=[1, 2, 3], help='BAR!')
>>> parser.print_help()
usage: PROG [-h] [--foo FOO] [bar ...]

positional arguments:
 bar         BAR! (default: [1, 2, 3])

options:
 -h, --help  show this help message and exit
 --foo FOO   FOO! (default: 42)

```

[`MetavarTypeHelpFormatter`](https://docs.python.org/3/library/argparse.html#argparse.MetavarTypeHelpFormatter "argparse.MetavarTypeHelpFormatter") uses the name of the [type](https://docs.python.org/3/library/argparse.html#type) argument for each argument as the display name for its values (rather than using the [dest](https://docs.python.org/3/library/argparse.html#dest) as the regular formatter does):
Copy```
>>> parser = argparse.ArgumentParser(
...     prog='PROG',
...     formatter_class=argparse.MetavarTypeHelpFormatter)
>>> parser.add_argument('--foo', type=int)
>>> parser.add_argument('bar', type=float)
>>> parser.print_help()
usage: PROG [-h] [--foo int] float

positional arguments:
  float

options:
  -h, --help  show this help message and exit
  --foo int

```

### prefix_chars[¶](https://docs.python.org/3/library/argparse.html#prefix-chars "Link to this heading")
Most command-line options will use `-` as the prefix, e.g. `-f/--foo`. Parsers that need to support different or additional prefix characters, e.g. for options like `+f` or `/foo`, may specify them using the `prefix_chars=` argument to the [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") constructor:
Copy```
>>> parser = argparse.ArgumentParser(prog='PROG', prefix_chars='-+')
>>> parser.add_argument('+f')
>>> parser.add_argument('++bar')
>>> parser.parse_args('+f X ++bar Y'.split())
Namespace(bar='Y', f='X')

```

The `prefix_chars=` argument defaults to `'-'`. Supplying a set of characters that does not include `-` will cause `-f/--foo` options to be disallowed.
### fromfile_prefix_chars[¶](https://docs.python.org/3/library/argparse.html#fromfile-prefix-chars "Link to this heading")
Sometimes, when dealing with a particularly long argument list, it may make sense to keep the list of arguments in a file rather than typing it out at the command line. If the `fromfile_prefix_chars=` argument is given to the [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") constructor, then arguments that start with any of the specified characters will be treated as files, and will be replaced by the arguments they contain. For example:
Copy```
>>> with open('args.txt', 'w', encoding=sys.getfilesystemencoding()) as fp:
...     fp.write('-f\nbar')
...
>>> parser = argparse.ArgumentParser(fromfile_prefix_chars='@')
>>> parser.add_argument('-f')
>>> parser.parse_args(['-f', 'foo', '@args.txt'])
Namespace(f='bar')

```

Arguments read from a file must be one per line by default (but see also [`convert_arg_line_to_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.convert_arg_line_to_args "argparse.ArgumentParser.convert_arg_line_to_args")) and are treated as if they were in the same place as the original file referencing argument on the command line. So in the example above, the expression `['-f', 'foo', '@args.txt']` is considered equivalent to the expression `['-f', 'foo', '-f', 'bar']`.
Note
Empty lines are treated as empty strings (`''`), which are allowed as values but not as arguments. Empty lines that are read as arguments will result in an “unrecognized arguments” error.
[`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") uses [filesystem encoding and error handler](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler) to read the file containing arguments.
The `fromfile_prefix_chars=` argument defaults to `None`, meaning that arguments will never be treated as file references.
Changed in version 3.12: [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") changed encoding and errors to read arguments files from default (e.g. [`locale.getpreferredencoding(False)`](https://docs.python.org/3/library/locale.html#locale.getpreferredencoding "locale.getpreferredencoding") and `"strict"`) to the [filesystem encoding and error handler](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler). Arguments file should be encoded in UTF-8 instead of ANSI Codepage on Windows.
### argument_default[¶](https://docs.python.org/3/library/argparse.html#argument-default "Link to this heading")
Generally, argument defaults are specified either by passing a default to [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument") or by calling the [`set_defaults()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.set_defaults "argparse.ArgumentParser.set_defaults") methods with a specific set of name-value pairs. Sometimes however, it may be useful to specify a single parser-wide default for arguments. This can be accomplished by passing the `argument_default=` keyword argument to [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser"). For example, to globally suppress attribute creation on [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args") calls, we supply `argument_default=SUPPRESS`:
Copy```
>>> parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
>>> parser.add_argument('--foo')
>>> parser.add_argument('bar', nargs='?')
>>> parser.parse_args(['--foo', '1', 'BAR'])
Namespace(bar='BAR', foo='1')
>>> parser.parse_args([])
Namespace()

```

### allow_abbrev[¶](https://docs.python.org/3/library/argparse.html#allow-abbrev "Link to this heading")
Normally, when you pass an argument list to the [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args") method of an [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser"), it [recognizes abbreviations](https://docs.python.org/3/library/argparse.html#prefix-matching) of long options.
This feature can be disabled by setting `allow_abbrev` to `False`:
Copy```
>>> parser = argparse.ArgumentParser(prog='PROG', allow_abbrev=False)
>>> parser.add_argument('--foobar', action='store_true')
>>> parser.add_argument('--foonley', action='store_false')
>>> parser.parse_args(['--foon'])
usage: PROG [-h] [--foobar] [--foonley]
PROG: error: unrecognized arguments: --foon

```

Added in version 3.5.
### conflict_handler[¶](https://docs.python.org/3/library/argparse.html#conflict-handler "Link to this heading")
[`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") objects do not allow two actions with the same option string. By default, `ArgumentParser` objects raise an exception if an attempt is made to create an argument with an option string that is already in use:
Copy```
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('-f', '--foo', help='old foo help')
>>> parser.add_argument('--foo', help='new foo help')
Traceback (most recent call last):
 ..
ArgumentError: argument --foo: conflicting option string(s): --foo

```

Sometimes (e.g. when using [parents](https://docs.python.org/3/library/argparse.html#parents)) it may be useful to simply override any older arguments with the same option string. To get this behavior, the value `'resolve'` can be supplied to the `conflict_handler=` argument of [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser"):
Copy```
>>> parser = argparse.ArgumentParser(prog='PROG', conflict_handler='resolve')
>>> parser.add_argument('-f', '--foo', help='old foo help')
>>> parser.add_argument('--foo', help='new foo help')
>>> parser.print_help()
usage: PROG [-h] [-f FOO] [--foo FOO]

options:
 -h, --help  show this help message and exit
 -f FOO      old foo help
 --foo FOO   new foo help

```

Note that [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") objects only remove an action if all of its option strings are overridden. So, in the example above, the old `-f/--foo` action is retained as the `-f` action, because only the `--foo` option string was overridden.
### add_help[¶](https://docs.python.org/3/library/argparse.html#add-help "Link to this heading")
By default, [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") objects add an option which simply displays the parser’s help message. If `-h` or `--help` is supplied at the command line, the `ArgumentParser` help will be printed.
Occasionally, it may be useful to disable the addition of this help option. This can be achieved by passing `False` as the `add_help=` argument to [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser"):
Copy```
>>> parser = argparse.ArgumentParser(prog='PROG', add_help=False)
>>> parser.add_argument('--foo', help='foo help')
>>> parser.print_help()
usage: PROG [--foo FOO]

options:
 --foo FOO  foo help

```

The help option is typically `-h/--help`. The exception to this is if the `prefix_chars=` is specified and does not include `-`, in which case `-h` and `--help` are not valid options. In this case, the first character in `prefix_chars` is used to prefix the help options:
Copy```
>>> parser = argparse.ArgumentParser(prog='PROG', prefix_chars='+/')
>>> parser.print_help()
usage: PROG [+h]

options:
  +h, ++help  show this help message and exit

```

### exit_on_error[¶](https://docs.python.org/3/library/argparse.html#exit-on-error "Link to this heading")
Normally, when you pass an invalid argument list to the [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args") method of an [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser"), it will print a _message_ to [`sys.stderr`](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr") and exit with a status code of 2.
If the user would like to catch errors manually, the feature can be enabled by setting `exit_on_error` to `False`:
Copy```
>>> parser = argparse.ArgumentParser(exit_on_error=False)
>>> parser.add_argument('--integers', type=int)
_StoreAction(option_strings=['--integers'], dest='integers', nargs=None, const=None, default=None, type=<class 'int'>, choices=None, help=None, metavar=None)
>>> try:
...     parser.parse_args('--integers a'.split())
... except argparse.ArgumentError:
...     print('Catching an argumentError')
...
Catching an argumentError

```

Added in version 3.9.
### suggest_on_error[¶](https://docs.python.org/3/library/argparse.html#suggest-on-error "Link to this heading")
By default, when a user passes an invalid argument choice or subparser name, [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") will exit with error info and list the permissible argument choices (if specified) or subparser names as part of the error message.
If the user would like to enable suggestions for mistyped argument choices and subparser names, the feature can be enabled by setting `suggest_on_error` to `True`. Note that this only applies for arguments when the choices specified are strings:
Copy```
>>> parser = argparse.ArgumentParser(suggest_on_error=True)
>>> parser.add_argument('--action', choices=['debug', 'dryrun'])
>>> parser.parse_args(['--action', 'debugg'])
usage: tester.py [-h] [--action {debug,dryrun}]
tester.py: error: argument --action: invalid choice: 'debugg', maybe you meant 'debug'? (choose from debug, dryrun)

```

If you’re writing code that needs to be compatible with older Python versions and want to opportunistically use `suggest_on_error` when it’s available, you can set it as an attribute after initializing the parser instead of using the keyword argument:
Copy```
>>> parser = argparse.ArgumentParser(description='Process some integers.')
>>> parser.suggest_on_error = True

```

Added in version 3.14.
### color[¶](https://docs.python.org/3/library/argparse.html#color "Link to this heading")
By default, the help message is printed in color using [in your local environment](https://docs.python.org/3/using/cmdline.html#using-on-controlling-color), or in the argument parser itself by setting `color` to `False`:
Copy```
>>> parser = argparse.ArgumentParser(description='Process some integers.',
...                                  color=False)
>>> parser.add_argument('--action', choices=['sum', 'max'])
>>> parser.add_argument('integers', metavar='N', type=int, nargs='+',
...                     help='an integer for the accumulator')
>>> parser.parse_args(['--help'])

```

Note that when `color=True`, colored output depends on both environment variables and terminal capabilities. However, if `color=False`, colored output is always disabled, even if environment variables like `FORCE_COLOR` are set.
Note
Error messages will include color codes when redirecting stderr to a file. To avoid this, set the [`PYTHON_COLORS`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_COLORS) environment variable (for example, `NO_COLOR=1 python script.py 2> errors.txt`).
Added in version 3.14.
