## The parse_args() method[¶](https://docs.python.org/3/library/argparse.html#the-parse-args-method "Link to this heading")

ArgumentParser.parse_args(_args =None_, _namespace =None_)[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "Link to this definition")

Convert argument strings to objects and assign them as attributes of the namespace. Return the populated namespace.
Previous calls to [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument") determine exactly what objects are created and how they are assigned. See the documentation for `add_argument()` for details.
  * [args](https://docs.python.org/3/library/argparse.html#args) - List of strings to parse. The default is taken from [`sys.argv`](https://docs.python.org/3/library/sys.html#sys.argv "sys.argv").
  * [namespace](https://docs.python.org/3/library/argparse.html#namespace) - An object to take the attributes. The default is a new empty [`Namespace`](https://docs.python.org/3/library/argparse.html#argparse.Namespace "argparse.Namespace") object.


### Option value syntax[¶](https://docs.python.org/3/library/argparse.html#option-value-syntax "Link to this heading")
The [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args") method supports several ways of specifying the value of an option (if it takes one). In the simplest case, the option and its value are passed as two separate arguments:
Copy```
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('-x')
>>> parser.add_argument('--foo')
>>> parser.parse_args(['-x', 'X'])
Namespace(foo=None, x='X')
>>> parser.parse_args(['--foo', 'FOO'])
Namespace(foo='FOO', x=None)

```

For long options (options with names longer than a single character), the option and value can also be passed as a single command-line argument, using `=` to separate them:
Copy```
>>> parser.parse_args(['--foo=FOO'])
Namespace(foo='FOO', x=None)

```

For short options (options only one character long), the option and its value can be concatenated:
Copy```
>>> parser.parse_args(['-xX'])
Namespace(foo=None, x='X')

```

Several short options can be joined together, using only a single `-` prefix, as long as only the last option (or none of them) requires a value:
Copy```
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('-x', action='store_true')
>>> parser.add_argument('-y', action='store_true')
>>> parser.add_argument('-z')
>>> parser.parse_args(['-xyzZ'])
Namespace(x=True, y=True, z='Z')

```

### Invalid arguments[¶](https://docs.python.org/3/library/argparse.html#invalid-arguments "Link to this heading")
While parsing the command line, [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args") checks for a variety of errors, including ambiguous options, invalid types, invalid options, wrong number of positional arguments, etc. When it encounters such an error, it exits and prints the error along with a usage message:
Copy```
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('--foo', type=int)
>>> parser.add_argument('bar', nargs='?')

>>> # invalid type
>>> parser.parse_args(['--foo', 'spam'])
usage: PROG [-h] [--foo FOO] [bar]
PROG: error: argument --foo: invalid int value: 'spam'

>>> # invalid option
>>> parser.parse_args(['--bar'])
usage: PROG [-h] [--foo FOO] [bar]
PROG: error: no such option: --bar

>>> # wrong number of arguments
>>> parser.parse_args(['spam', 'badger'])
usage: PROG [-h] [--foo FOO] [bar]
PROG: error: extra arguments found: badger

```

### Arguments containing `-`[¶](https://docs.python.org/3/library/argparse.html#arguments-containing "Link to this heading")
The [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args") method attempts to give errors whenever the user has clearly made a mistake, but some situations are inherently ambiguous. For example, the command-line argument `-1` could either be an attempt to specify an option or an attempt to provide a positional argument. The `parse_args()` method is cautious here: positional arguments may only begin with `-` if they look like negative numbers and there are no options in the parser that look like negative numbers:
Copy```
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('-x')
>>> parser.add_argument('foo', nargs='?')

>>> # no negative number options, so -1 is a positional argument
>>> parser.parse_args(['-x', '-1'])
Namespace(foo=None, x='-1')

>>> # no negative number options, so -1 and -5 are positional arguments
>>> parser.parse_args(['-x', '-1', '-5'])
Namespace(foo='-5', x='-1')

>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('-1', dest='one')
>>> parser.add_argument('foo', nargs='?')

>>> # negative number options present, so -1 is an option
>>> parser.parse_args(['-1', 'X'])
Namespace(foo=None, one='X')

>>> # negative number options present, so -2 is an option
>>> parser.parse_args(['-2'])
usage: PROG [-h] [-1 ONE] [foo]
PROG: error: no such option: -2

>>> # negative number options present, so both -1s are options
>>> parser.parse_args(['-1', '-1'])
usage: PROG [-h] [-1 ONE] [foo]
PROG: error: argument -1: expected one argument

```

If you have positional arguments that must begin with `-` and don’t look like negative numbers, you can insert the pseudo-argument `'--'` which tells [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args") that everything after that is a positional argument:
Copy```
>>> parser.parse_args(['--', '-f'])
Namespace(foo='-f', one=None)

```

See also [the argparse howto on ambiguous arguments](https://docs.python.org/3/howto/argparse.html#specifying-ambiguous-arguments) for more details.
### Argument abbreviations (prefix matching)[¶](https://docs.python.org/3/library/argparse.html#argument-abbreviations-prefix-matching "Link to this heading")
The [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args") method [by default](https://docs.python.org/3/library/argparse.html#allow-abbrev) allows long options to be abbreviated to a prefix, if the abbreviation is unambiguous (the prefix matches a unique option):
Copy```
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('-bacon')
>>> parser.add_argument('-badger')
>>> parser.parse_args('-bac MMM'.split())
Namespace(bacon='MMM', badger=None)
>>> parser.parse_args('-bad WOOD'.split())
Namespace(bacon=None, badger='WOOD')
>>> parser.parse_args('-ba BA'.split())
usage: PROG [-h] [-bacon BACON] [-badger BADGER]
PROG: error: ambiguous option: -ba could match -badger, -bacon

```

An error is produced for arguments that could produce more than one options. This feature can be disabled by setting [allow_abbrev](https://docs.python.org/3/library/argparse.html#allow-abbrev) to `False`.
### Beyond `sys.argv`[¶](https://docs.python.org/3/library/argparse.html#beyond-sys-argv "Link to this heading")
Sometimes it may be useful to have an [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") parse arguments other than those of [`sys.argv`](https://docs.python.org/3/library/sys.html#sys.argv "sys.argv"). This can be accomplished by passing a list of strings to [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args"). This is useful for testing at the interactive prompt:
Copy```
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument(
...     'integers', metavar='int', type=int, choices=range(10),
...     nargs='+', help='an integer in the range 0..9')
>>> parser.add_argument(
...     '--sum', dest='accumulate', action='store_const', const=sum,
...     default=max, help='sum the integers (default: find the max)')
>>> parser.parse_args(['1', '2', '3', '4'])
Namespace(accumulate=<built-in function max>, integers=[1, 2, 3, 4])
>>> parser.parse_args(['1', '2', '3', '4', '--sum'])
Namespace(accumulate=<built-in function sum>, integers=[1, 2, 3, 4])

```

### The Namespace object[¶](https://docs.python.org/3/library/argparse.html#the-namespace-object "Link to this heading")

_class_ argparse.Namespace[¶](https://docs.python.org/3/library/argparse.html#argparse.Namespace "Link to this definition")

Simple class used by default by [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args") to create an object holding attributes and return it.
This class is deliberately simple, just an [`object`](https://docs.python.org/3/library/functions.html#object "object") subclass with a readable string representation. If you prefer to have dict-like view of the attributes, you can use the standard Python idiom, [`vars()`](https://docs.python.org/3/library/functions.html#vars "vars"):
Copy```
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo')
>>> args = parser.parse_args(['--foo', 'BAR'])
>>> vars(args)
{'foo': 'BAR'}

```

It may also be useful to have an [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") assign attributes to an already existing object, rather than a new `Namespace` object. This can be achieved by specifying the `namespace=` keyword argument:
Copy```
>>> class C:
...     pass
...
>>> c = C()
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo')
>>> parser.parse_args(args=['--foo', 'BAR'], namespace=c)
>>> c.foo
'BAR'

```

## Other utilities[¶](https://docs.python.org/3/library/argparse.html#other-utilities "Link to this heading")
### Subcommands[¶](https://docs.python.org/3/library/argparse.html#subcommands "Link to this heading")

ArgumentParser.add_subparsers(_*_[, _title_][, _description_][, _prog_][, _parser_class_][, _action_][, _dest_][, _required_][, _help_][, _metavar_])[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_subparsers "Link to this definition")

Many programs split up their functionality into a number of subcommands, for example, the `svn` program can invoke subcommands like `svn checkout`, `svn update`, and `svn commit`. Splitting up functionality this way can be a particularly good idea when a program performs several different functions which require different kinds of command-line arguments. [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") supports the creation of such subcommands with the `add_subparsers()` method. The `add_subparsers()` method is normally called with no arguments and returns a special action object. This object has a single method, `add_parser()`, which takes a command name and any `ArgumentParser` constructor arguments, and returns an `ArgumentParser` object that can be modified as usual.
Description of parameters:
  * _title_ - title for the sub-parser group in help output; by default “subcommands” if description is provided, otherwise uses title for positional arguments
  * _description_ - description for the sub-parser group in help output, by default `None`
  * _prog_ - usage information that will be displayed with subcommand help, by default the name of the program and any positional arguments before the subparser argument
  * _parser_class_ - class which will be used to create sub-parser instances, by default the class of the current parser (e.g. [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser"))
  * [action](https://docs.python.org/3/library/argparse.html#action) - the basic type of action to be taken when this argument is encountered at the command line
  * [dest](https://docs.python.org/3/library/argparse.html#dest) - name of the attribute under which subcommand name will be stored; by default `None` and no value is stored
  * [required](https://docs.python.org/3/library/argparse.html#required) - Whether or not a subcommand must be provided, by default `False` (added in 3.7)
  * [help](https://docs.python.org/3/library/argparse.html#help) - help for sub-parser group in help output, by default `None`
  * [metavar](https://docs.python.org/3/library/argparse.html#metavar) - string presenting available subcommands in help; by default it is `None` and presents subcommands in form {cmd1, cmd2, ..}


Some example usage:
Copy```
>>> # create the top-level parser
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('--foo', action='store_true', help='foo help')
>>> subparsers = parser.add_subparsers(help='subcommand help')
>>>
>>> # create the parser for the "a" command
>>> parser_a = subparsers.add_parser('a', help='a help')
>>> parser_a.add_argument('bar', type=int, help='bar help')
>>>
>>> # create the parser for the "b" command
>>> parser_b = subparsers.add_parser('b', help='b help')
>>> parser_b.add_argument('--baz', choices=('X', 'Y', 'Z'), help='baz help')
>>>
>>> # parse some argument lists
>>> parser.parse_args(['a', '12'])
Namespace(bar=12, foo=False)
>>> parser.parse_args(['--foo', 'b', '--baz', 'Z'])
Namespace(baz='Z', foo=True)

```

Note that the object returned by [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args") will only contain attributes for the main parser and the subparser that was selected by the command line (and not any other subparsers). So in the example above, when the `a` command is specified, only the `foo` and `bar` attributes are present, and when the `b` command is specified, only the `foo` and `baz` attributes are present.
Similarly, when a help message is requested from a subparser, only the help for that particular parser will be printed. The help message will not include parent parser or sibling parser messages. (A help message for each subparser command, however, can be given by supplying the `help=` argument to `add_parser()` as above.)
Copy```
>>> parser.parse_args(['--help'])
usage: PROG [-h] [--foo] {a,b} ...

positional arguments:
  {a,b}   subcommand help
    a     a help
    b     b help

options:
  -h, --help  show this help message and exit
  --foo   foo help

>>> parser.parse_args(['a', '--help'])
usage: PROG a [-h] bar

positional arguments:
  bar     bar help

options:
  -h, --help  show this help message and exit

>>> parser.parse_args(['b', '--help'])
usage: PROG b [-h] [--baz {X,Y,Z}]

options:
  -h, --help     show this help message and exit
  --baz {X,Y,Z}  baz help

```

The `add_subparsers()` method also supports `title` and `description` keyword arguments. When either is present, the subparser’s commands will appear in their own group in the help output. For example:
Copy```
>>> parser = argparse.ArgumentParser()
>>> subparsers = parser.add_subparsers(title='subcommands',
...                                    description='valid subcommands',
...                                    help='additional help')
>>> subparsers.add_parser('foo')
>>> subparsers.add_parser('bar')
>>> parser.parse_args(['-h'])
usage:  [-h] {foo,bar} ...

options:
  -h, --help  show this help message and exit

subcommands:
  valid subcommands

  {foo,bar}   additional help

```

Furthermore, `add_parser()` supports an additional _aliases_ argument, which allows multiple strings to refer to the same subparser. This example, like `svn`, aliases `co` as a shorthand for `checkout`:
Copy```
>>> parser = argparse.ArgumentParser()
>>> subparsers = parser.add_subparsers()
>>> checkout = subparsers.add_parser('checkout', aliases=['co'])
>>> checkout.add_argument('foo')
>>> parser.parse_args(['co', 'bar'])
Namespace(foo='bar')

```

`add_parser()` supports also an additional _deprecated_ argument, which allows to deprecate the subparser.
Copy```
>>> import argparse
>>> parser = argparse.ArgumentParser(prog='chicken.py')
>>> subparsers = parser.add_subparsers()
>>> run = subparsers.add_parser('run')
>>> fly = subparsers.add_parser('fly', deprecated=True)
>>> parser.parse_args(['fly'])
chicken.py: warning: command 'fly' is deprecated
Namespace()

```

Added in version 3.13.
One particularly effective way of handling subcommands is to combine the use of the `add_subparsers()` method with calls to [`set_defaults()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.set_defaults "argparse.ArgumentParser.set_defaults") so that each subparser knows which Python function it should execute. For example:
Copy```
>>> # subcommand functions
>>> def foo(args):
...     print(args.x * args.y)
...
>>> def bar(args):
...     print('((%s))' % args.z)
...
>>> # create the top-level parser
>>> parser = argparse.ArgumentParser()
>>> subparsers = parser.add_subparsers(required=True)
>>>
>>> # create the parser for the "foo" command
>>> parser_foo = subparsers.add_parser('foo')
>>> parser_foo.add_argument('-x', type=int, default=1)
>>> parser_foo.add_argument('y', type=float)
>>> parser_foo.set_defaults(func=foo)
>>>
>>> # create the parser for the "bar" command
>>> parser_bar = subparsers.add_parser('bar')
>>> parser_bar.add_argument('z')
>>> parser_bar.set_defaults(func=bar)
>>>
>>> # parse the args and call whatever function was selected
>>> args = parser.parse_args('foo 1 -x 2'.split())
>>> args.func(args)
2.0
>>>
>>> # parse the args and call whatever function was selected
>>> args = parser.parse_args('bar XYZYX'.split())
>>> args.func(args)
((XYZYX))

```

This way, you can let [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args") do the job of calling the appropriate function after argument parsing is complete. Associating functions with actions like this is typically the easiest way to handle the different actions for each of your subparsers. However, if it is necessary to check the name of the subparser that was invoked, the `dest` keyword argument to the `add_subparsers()` call will work:
Copy```
>>> parser = argparse.ArgumentParser()
>>> subparsers = parser.add_subparsers(dest='subparser_name')
>>> subparser1 = subparsers.add_parser('1')
>>> subparser1.add_argument('-x')
>>> subparser2 = subparsers.add_parser('2')
>>> subparser2.add_argument('y')
>>> parser.parse_args(['2', 'frobble'])
Namespace(subparser_name='2', y='frobble')

```

Changed in version 3.7: New _required_ keyword-only parameter.
Changed in version 3.14: Subparser’s _prog_ is no longer affected by a custom usage message in the main parser.
### FileType objects[¶](https://docs.python.org/3/library/argparse.html#filetype-objects "Link to this heading")

_class_ argparse.FileType(_mode ='r'_, _bufsize =-1_, _encoding =None_, _errors =None_)[¶](https://docs.python.org/3/library/argparse.html#argparse.FileType "Link to this definition")

The `FileType` factory creates objects that can be passed to the type argument of [`ArgumentParser.add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument"). Arguments that have `FileType` objects as their type will open command-line arguments as files with the requested modes, buffer sizes, encodings and error handling (see the [`open()`](https://docs.python.org/3/library/functions.html#open "open") function for more details):
Copy```
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--raw', type=argparse.FileType('wb', 0))
>>> parser.add_argument('out', type=argparse.FileType('w', encoding='UTF-8'))
>>> parser.parse_args(['--raw', 'raw.dat', 'file.txt'])
Namespace(out=<_io.TextIOWrapper name='file.txt' mode='w' encoding='UTF-8'>, raw=<_io.FileIO name='raw.dat' mode='wb'>)

```

FileType objects understand the pseudo-argument `'-'` and automatically convert this into [`sys.stdin`](https://docs.python.org/3/library/sys.html#sys.stdin "sys.stdin") for readable `FileType` objects and [`sys.stdout`](https://docs.python.org/3/library/sys.html#sys.stdout "sys.stdout") for writable `FileType` objects:
Copy```
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('infile', type=argparse.FileType('r'))
>>> parser.parse_args(['-'])
Namespace(infile=<_io.TextIOWrapper name='<stdin>' encoding='UTF-8'>)

```

Note
If one argument uses _FileType_ and then a subsequent argument fails, an error is reported but the file is not automatically closed. This can also clobber the output files. In this case, it would be better to wait until after the parser has run and then use the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)-statement to manage the files.
Changed in version 3.4: Added the _encodings_ and _errors_ parameters.
Deprecated since version 3.14.
### Argument groups[¶](https://docs.python.org/3/library/argparse.html#argument-groups "Link to this heading")

ArgumentParser.add_argument_group(_title=None_ , _description=None_ , _*_[, _argument_default_][, _conflict_handler_])[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument_group "Link to this definition")

By default, [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") groups command-line arguments into “positional arguments” and “options” when displaying help messages. When there is a better conceptual grouping of arguments than this default one, appropriate groups can be created using the `add_argument_group()` method:
Copy```
>>> parser = argparse.ArgumentParser(prog='PROG', add_help=False)
>>> group = parser.add_argument_group('group')
>>> group.add_argument('--foo', help='foo help')
>>> group.add_argument('bar', help='bar help')
>>> parser.print_help()
usage: PROG [--foo FOO] bar

group:
  bar    bar help
  --foo FOO  foo help

```

The `add_argument_group()` method returns an argument group object which has an [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument") method just like a regular [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser"). When an argument is added to the group, the parser treats it just like a normal argument, but displays the argument in a separate group for help messages. The `add_argument_group()` method accepts _title_ and _description_ arguments which can be used to customize this display:
Copy```
>>> parser = argparse.ArgumentParser(prog='PROG', add_help=False)
>>> group1 = parser.add_argument_group('group1', 'group1 description')
>>> group1.add_argument('foo', help='foo help')
>>> group2 = parser.add_argument_group('group2', 'group2 description')
>>> group2.add_argument('--bar', help='bar help')
>>> parser.print_help()
usage: PROG [--bar BAR] foo

group1:
  group1 description

  foo    foo help

group2:
  group2 description

  --bar BAR  bar help

```

The optional, keyword-only parameters [argument_default](https://docs.python.org/3/library/argparse.html#argument-default) and [conflict_handler](https://docs.python.org/3/library/argparse.html#conflict-handler) allow for finer-grained control of the behavior of the argument group. These parameters have the same meaning as in the [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") constructor, but apply specifically to the argument group rather than the entire parser.
Note that any arguments not in your user-defined groups will end up back in the usual “positional arguments” and “optional arguments” sections.
Deprecated since version 3.11, removed in version 3.14: Calling `add_argument_group()` on an argument group now raises an exception. This nesting was never supported, often failed to work correctly, and was unintentionally exposed through inheritance.
Deprecated since version 3.14: Passing [prefix_chars](https://docs.python.org/3/library/argparse.html#prefix-chars) to `add_argument_group()` is now deprecated.
### Mutual exclusion[¶](https://docs.python.org/3/library/argparse.html#mutual-exclusion "Link to this heading")

ArgumentParser.add_mutually_exclusive_group(_required =False_)[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_mutually_exclusive_group "Link to this definition")

Create a mutually exclusive group. `argparse` will make sure that only one of the arguments in the mutually exclusive group was present on the command line:
Copy```
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> group = parser.add_mutually_exclusive_group()
>>> group.add_argument('--foo', action='store_true')
>>> group.add_argument('--bar', action='store_false')
>>> parser.parse_args(['--foo'])
Namespace(bar=True, foo=True)
>>> parser.parse_args(['--bar'])
Namespace(bar=False, foo=False)
>>> parser.parse_args(['--foo', '--bar'])
usage: PROG [-h] [--foo | --bar]
PROG: error: argument --bar: not allowed with argument --foo

```

The `add_mutually_exclusive_group()` method also accepts a _required_ argument, to indicate that at least one of the mutually exclusive arguments is required:
Copy```
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> group = parser.add_mutually_exclusive_group(required=True)
>>> group.add_argument('--foo', action='store_true')
>>> group.add_argument('--bar', action='store_false')
>>> parser.parse_args([])
usage: PROG [-h] (--foo | --bar)
PROG: error: one of the arguments --foo --bar is required

```

Note that currently mutually exclusive argument groups do not support the _title_ and _description_ arguments of [`add_argument_group()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument_group "argparse.ArgumentParser.add_argument_group"). However, a mutually exclusive group can be added to an argument group that has a title and description. For example:
Copy```
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> group = parser.add_argument_group('Group title', 'Group description')
>>> exclusive_group = group.add_mutually_exclusive_group(required=True)
>>> exclusive_group.add_argument('--foo', help='foo help')
>>> exclusive_group.add_argument('--bar', help='bar help')
>>> parser.print_help()
usage: PROG [-h] (--foo FOO | --bar BAR)

options:
  -h, --help  show this help message and exit

Group title:
  Group description

  --foo FOO   foo help
  --bar BAR   bar help

```

Deprecated since version 3.11, removed in version 3.14: Calling [`add_argument_group()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument_group "argparse.ArgumentParser.add_argument_group") or `add_mutually_exclusive_group()` on a mutually exclusive group now raises an exception. This nesting was never supported, often failed to work correctly, and was unintentionally exposed through inheritance.
### Parser defaults[¶](https://docs.python.org/3/library/argparse.html#parser-defaults "Link to this heading")

ArgumentParser.set_defaults(_** kwargs_)[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.set_defaults "Link to this definition")

Most of the time, the attributes of the object returned by [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args") will be fully determined by inspecting the command-line arguments and the argument actions. `set_defaults()` allows some additional attributes that are determined without any inspection of the command line to be added:
Copy```
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('foo', type=int)
>>> parser.set_defaults(bar=42, baz='badger')
>>> parser.parse_args(['736'])
Namespace(bar=42, baz='badger', foo=736)

```

Note that defaults can be set at both the parser level using `set_defaults()` and at the argument level using [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument"). If both are called for the same argument, the last default set for an argument is used:
Copy```
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', default='bar')
>>> parser.set_defaults(foo='spam')
>>> parser.parse_args([])
Namespace(foo='spam')

```

Parser-level defaults can be particularly useful when working with multiple parsers. See the [`add_subparsers()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_subparsers "argparse.ArgumentParser.add_subparsers") method for an example of this type.

ArgumentParser.get_default(_dest_)[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.get_default "Link to this definition")

Get the default value for a namespace attribute, as set by either [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument") or by [`set_defaults()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.set_defaults "argparse.ArgumentParser.set_defaults"):
Copy```
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', default='badger')
>>> parser.get_default('foo')
'badger'

```

### Printing help[¶](https://docs.python.org/3/library/argparse.html#printing-help "Link to this heading")
In most typical applications, [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args") will take care of formatting and printing any usage or error messages. However, several formatting methods are available:

ArgumentParser.print_usage(_file =None_)[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.print_usage "Link to this definition")

Print a brief description of how the [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") should be invoked on the command line. If _file_ is `None`, [`sys.stdout`](https://docs.python.org/3/library/sys.html#sys.stdout "sys.stdout") is assumed.

ArgumentParser.print_help(_file =None_)[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.print_help "Link to this definition")

Print a help message, including the program usage and information about the arguments registered with the [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser"). If _file_ is `None`, [`sys.stdout`](https://docs.python.org/3/library/sys.html#sys.stdout "sys.stdout") is assumed.
There are also variants of these methods that simply return a string instead of printing it:

ArgumentParser.format_usage()[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.format_usage "Link to this definition")

Return a string containing a brief description of how the [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") should be invoked on the command line.

ArgumentParser.format_help()[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.format_help "Link to this definition")

Return a string containing a help message, including the program usage and information about the arguments registered with the [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser").
### Partial parsing[¶](https://docs.python.org/3/library/argparse.html#partial-parsing "Link to this heading")

ArgumentParser.parse_known_args(_args =None_, _namespace =None_)[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_known_args "Link to this definition")

Sometimes a script only needs to handle a specific set of command-line arguments, leaving any unrecognized arguments for another script or program. In these cases, the `parse_known_args()` method can be useful.
This method works similarly to [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args"), but it does not raise an error for extra, unrecognized arguments. Instead, it parses the known arguments and returns a two item tuple that contains the populated namespace and the list of any unrecognized arguments.
Copy```
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', action='store_true')
>>> parser.add_argument('bar')
>>> parser.parse_known_args(['--foo', '--badger', 'BAR', 'spam'])
(Namespace(bar='BAR', foo=True), ['--badger', 'spam'])

```

Warning
[Prefix matching](https://docs.python.org/3/library/argparse.html#prefix-matching) rules apply to [`parse_known_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_known_args "argparse.ArgumentParser.parse_known_args"). The parser may consume an option even if it’s just a prefix of one of its known options, instead of leaving it in the remaining arguments list.
### Customizing file parsing[¶](https://docs.python.org/3/library/argparse.html#customizing-file-parsing "Link to this heading")

ArgumentParser.convert_arg_line_to_args(_arg_line_)[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.convert_arg_line_to_args "Link to this definition")

Arguments that are read from a file (see the _fromfile_prefix_chars_ keyword argument to the [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") constructor) are read one argument per line. `convert_arg_line_to_args()` can be overridden for fancier reading.
This method takes a single argument _arg_line_ which is a string read from the argument file. It returns a list of arguments parsed from this string. The method is called once per line read from the argument file, in order.
A useful override of this method is one that treats each space-separated word as an argument. The following example demonstrates how to do this:
Copy```
class MyArgumentParser(argparse.ArgumentParser):
    def convert_arg_line_to_args(self, arg_line):
        return arg_line.split()

```

### Exiting methods[¶](https://docs.python.org/3/library/argparse.html#exiting-methods "Link to this heading")

ArgumentParser.exit(_status =0_, _message =None_)[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.exit "Link to this definition")

This method terminates the program, exiting with the specified _status_ and, if given, it prints a _message_ to [`sys.stderr`](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr") before that. The user can override this method to handle these steps differently:
Copy```
class ErrorCatchingArgumentParser(argparse.ArgumentParser):
    def exit(self, status=0, message=None):
        if status:
            raise Exception(f'Exiting because of an error: {message}')
        exit(status)

```


ArgumentParser.error(_message_)[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.error "Link to this definition")

This method prints a usage message, including the _message_ , to [`sys.stderr`](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr") and terminates the program with a status code of 2.
### Intermixed parsing[¶](https://docs.python.org/3/library/argparse.html#intermixed-parsing "Link to this heading")

ArgumentParser.parse_intermixed_args(_args =None_, _namespace =None_)[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_intermixed_args "Link to this definition")


ArgumentParser.parse_known_intermixed_args(_args =None_, _namespace =None_)[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_known_intermixed_args "Link to this definition")

A number of Unix commands allow the user to intermix optional arguments with positional arguments. The [`parse_intermixed_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_intermixed_args "argparse.ArgumentParser.parse_intermixed_args") and `parse_known_intermixed_args()` methods support this parsing style.
These parsers do not support all the `argparse` features, and will raise exceptions if unsupported features are used. In particular, subparsers, and mutually exclusive groups that include both optionals and positionals are not supported.
The following example shows the difference between [`parse_known_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_known_args "argparse.ArgumentParser.parse_known_args") and [`parse_intermixed_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_intermixed_args "argparse.ArgumentParser.parse_intermixed_args"): the former returns `['2', '3']` as unparsed arguments, while the latter collects all the positionals into `rest`.
Copy```
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo')
>>> parser.add_argument('cmd')
>>> parser.add_argument('rest', nargs='*', type=int)
>>> parser.parse_known_args('doit 1 --foo bar 2 3'.split())
(Namespace(cmd='doit', foo='bar', rest=[1]), ['2', '3'])
>>> parser.parse_intermixed_args('doit 1 --foo bar 2 3'.split())
Namespace(cmd='doit', foo='bar', rest=[1, 2, 3])

```

`parse_known_intermixed_args()` returns a two item tuple containing the populated namespace and the list of remaining argument strings. [`parse_intermixed_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_intermixed_args "argparse.ArgumentParser.parse_intermixed_args") raises an error if there are any remaining unparsed argument strings.
Added in version 3.7.
### Registering custom types or actions[¶](https://docs.python.org/3/library/argparse.html#registering-custom-types-or-actions "Link to this heading")

ArgumentParser.register(_registry_name_ , _value_ , _object_)[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.register "Link to this definition")

Sometimes it’s desirable to use a custom string in error messages to provide more user-friendly output. In these cases, `register()` can be used to register custom actions or types with a parser and allow you to reference the type by their registered name instead of their callable name.
The `register()` method accepts three arguments - a _registry_name_ , specifying the internal registry where the object will be stored (e.g., `action`, `type`), _value_ , which is the key under which the object will be registered, and object, the callable to be registered.
The following example shows how to register a custom type with a parser:
Copy```
>>> import argparse
>>> parser = argparse.ArgumentParser()
>>> parser.register('type', 'hexadecimal integer', lambda s: int(s, 16))
>>> parser.add_argument('--foo', type='hexadecimal integer')
_StoreAction(option_strings=['--foo'], dest='foo', nargs=None, const=None, default=None, type='hexadecimal integer', choices=None, required=False, help=None, metavar=None, deprecated=False)
>>> parser.parse_args(['--foo', '0xFA'])
Namespace(foo=250)
>>> parser.parse_args(['--foo', '1.2'])
usage: PROG [-h] [--foo FOO]
PROG: error: argument --foo: invalid 'hexadecimal integer' value: '1.2'

```

## Exceptions[¶](https://docs.python.org/3/library/argparse.html#exceptions "Link to this heading")

_exception_ argparse.ArgumentError[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentError "Link to this definition")

An error from creating or using an argument (optional or positional).
The string value of this exception is the message, augmented with information about the argument that caused it.

_exception_ argparse.ArgumentTypeError[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentTypeError "Link to this definition")

Raised when something goes wrong converting a command line string to a type.
Guides and Tutorials
  * [Argparse Tutorial](https://docs.python.org/3/howto/argparse.html)
  * [Migrating `optparse` code to `argparse`](https://docs.python.org/3/howto/argparse-optparse.html)


### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`argparse` — Parser for command-line options, arguments and subcommands](https://docs.python.org/3/library/argparse.html)
    * [ArgumentParser objects](https://docs.python.org/3/library/argparse.html#argumentparser-objects)
      * [prog](https://docs.python.org/3/library/argparse.html#prog)
      * [usage](https://docs.python.org/3/library/argparse.html#usage)
      * [description](https://docs.python.org/3/library/argparse.html#description)
      * [epilog](https://docs.python.org/3/library/argparse.html#epilog)
      * [parents](https://docs.python.org/3/library/argparse.html#parents)
      * [formatter_class](https://docs.python.org/3/library/argparse.html#formatter-class)
      * [prefix_chars](https://docs.python.org/3/library/argparse.html#prefix-chars)
      * [fromfile_prefix_chars](https://docs.python.org/3/library/argparse.html#fromfile-prefix-chars)
      * [argument_default](https://docs.python.org/3/library/argparse.html#argument-default)
      * [allow_abbrev](https://docs.python.org/3/library/argparse.html#allow-abbrev)
      * [conflict_handler](https://docs.python.org/3/library/argparse.html#conflict-handler)
      * [add_help](https://docs.python.org/3/library/argparse.html#add-help)
      * [exit_on_error](https://docs.python.org/3/library/argparse.html#exit-on-error)
      * [suggest_on_error](https://docs.python.org/3/library/argparse.html#suggest-on-error)
      * [color](https://docs.python.org/3/library/argparse.html#color)
    * [The add_argument() method](https://docs.python.org/3/library/argparse.html#the-add-argument-method)
      * [name or flags](https://docs.python.org/3/library/argparse.html#name-or-flags)
      * [action](https://docs.python.org/3/library/argparse.html#action)
      * [nargs](https://docs.python.org/3/library/argparse.html#nargs)
      * [const](https://docs.python.org/3/library/argparse.html#const)
      * [default](https://docs.python.org/3/library/argparse.html#default)
      * [type](https://docs.python.org/3/library/argparse.html#type)
      * [choices](https://docs.python.org/3/library/argparse.html#choices)
      * [required](https://docs.python.org/3/library/argparse.html#required)
      * [help](https://docs.python.org/3/library/argparse.html#help)
      * [metavar](https://docs.python.org/3/library/argparse.html#metavar)
      * [dest](https://docs.python.org/3/library/argparse.html#dest)
      * [deprecated](https://docs.python.org/3/library/argparse.html#deprecated)
      * [Action classes](https://docs.python.org/3/library/argparse.html#action-classes)
    * [The parse_args() method](https://docs.python.org/3/library/argparse.html#the-parse-args-method)
      * [Option value syntax](https://docs.python.org/3/library/argparse.html#option-value-syntax)
      * [Invalid arguments](https://docs.python.org/3/library/argparse.html#invalid-arguments)
      * [Arguments containing `-`](https://docs.python.org/3/library/argparse.html#arguments-containing)
      * [Argument abbreviations (prefix matching)](https://docs.python.org/3/library/argparse.html#argument-abbreviations-prefix-matching)
      * [Beyond `sys.argv`](https://docs.python.org/3/library/argparse.html#beyond-sys-argv)
      * [The Namespace object](https://docs.python.org/3/library/argparse.html#the-namespace-object)
    * [Other utilities](https://docs.python.org/3/library/argparse.html#other-utilities)
      * [Subcommands](https://docs.python.org/3/library/argparse.html#subcommands)
      * [FileType objects](https://docs.python.org/3/library/argparse.html#filetype-objects)
      * [Argument groups](https://docs.python.org/3/library/argparse.html#argument-groups)
      * [Mutual exclusion](https://docs.python.org/3/library/argparse.html#mutual-exclusion)
      * [Parser defaults](https://docs.python.org/3/library/argparse.html#parser-defaults)
      * [Printing help](https://docs.python.org/3/library/argparse.html#printing-help)
      * [Partial parsing](https://docs.python.org/3/library/argparse.html#partial-parsing)
      * [Customizing file parsing](https://docs.python.org/3/library/argparse.html#customizing-file-parsing)
      * [Exiting methods](https://docs.python.org/3/library/argparse.html#exiting-methods)
      * [Intermixed parsing](https://docs.python.org/3/library/argparse.html#intermixed-parsing)
      * [Registering custom types or actions](https://docs.python.org/3/library/argparse.html#registering-custom-types-or-actions)
    * [Exceptions](https://docs.python.org/3/library/argparse.html#exceptions)


#### Previous topic
[Command-line interface libraries](https://docs.python.org/3/library/cmdlinelibs.html "previous chapter")
#### Next topic
[Argparse Tutorial](https://docs.python.org/3/howto/argparse.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=argparse+%E2%80%94+Parser+for+command-line+options%2C+arguments+and+subcommands&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fargparse.html&pagesource=library%2Fargparse.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/howto/argparse.html "Argparse Tutorial") |
  * [previous](https://docs.python.org/3/library/cmdlinelibs.html "Command-line interface libraries") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Command-line interface libraries](https://docs.python.org/3/library/cmdlinelibs.html) »
  * [`argparse` — Parser for command-line options, arguments and subcommands](https://docs.python.org/3/library/argparse.html)
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
