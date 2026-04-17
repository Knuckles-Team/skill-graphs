## Reference Guide[¶](https://docs.python.org/3/library/optparse.html#reference-guide "Link to this heading")
### Creating the parser[¶](https://docs.python.org/3/library/optparse.html#creating-the-parser "Link to this heading")
The first step in using `optparse` is to create an OptionParser instance.

_class_ optparse.OptionParser(_..._)[¶](https://docs.python.org/3/library/optparse.html#optparse.OptionParser "Link to this definition")

The OptionParser constructor has no required arguments, but a number of optional keyword arguments. You should always pass them as keyword arguments, i.e. do not rely on the order in which the arguments are declared.

`usage` (default: `"%prog [options]"`)

The usage summary to print when your program is run incorrectly or with a help option. When `optparse` prints the usage string, it expands `%prog` to `os.path.basename(sys.argv[0])` (or to `prog` if you passed that keyword argument). To suppress a usage message, pass the special value `optparse.SUPPRESS_USAGE`.

`option_list` (default: `[]`)

A list of Option objects to populate the parser with. The options in `option_list` are added after any options in `standard_option_list` (a class attribute that may be set by OptionParser subclasses), but before any version or help options. Deprecated; use [`add_option()`](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.add_option "optparse.OptionParser.add_option") after creating the parser instead.

`option_class` (default: optparse.Option)

Class to use when adding options to the parser in [`add_option()`](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.add_option "optparse.OptionParser.add_option").

`version` (default: `None`)

A version string to print when the user supplies a version option. If you supply a true value for `version`, `optparse` automatically adds a version option with the single option string `--version`. The substring `%prog` is expanded the same as for `usage`.

`conflict_handler` (default: `"error"`)

Specifies what to do when options with conflicting option strings are added to the parser; see section [Conflicts between options](https://docs.python.org/3/library/optparse.html#optparse-conflicts-between-options).

`description` (default: `None`)

A paragraph of text giving a brief overview of your program. `optparse` reformats this paragraph to fit the current terminal width and prints it when the user requests help (after `usage`, but before the list of options).

`formatter` (default: a new `IndentedHelpFormatter`)

An instance of optparse.HelpFormatter that will be used for printing help text. `optparse` provides two concrete classes for this purpose: IndentedHelpFormatter and TitledHelpFormatter.

`add_help_option` (default: `True`)

If true, `optparse` will add a help option (with option strings `-h` and `--help`) to the parser.

`prog`

The string to use when expanding `%prog` in `usage` and `version` instead of `os.path.basename(sys.argv[0])`.

`epilog` (default: `None`)

A paragraph of help text to print after the option help.
### Populating the parser[¶](https://docs.python.org/3/library/optparse.html#populating-the-parser "Link to this heading")
There are several ways to populate the parser with options. The preferred way is by using [`OptionParser.add_option()`](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.add_option "optparse.OptionParser.add_option"), as shown in section [Tutorial](https://docs.python.org/3/library/optparse.html#optparse-tutorial). `add_option()` can be called in one of two ways:
  * pass it an Option instance (as returned by `make_option()`)
  * pass it any combination of positional and keyword arguments that are acceptable to `make_option()` (i.e., to the Option constructor), and it will create the Option instance for you


The other alternative is to pass a list of pre-constructed Option instances to the OptionParser constructor, as in:
Copy```
option_list = [
    make_option("-f", "--filename",
                action="store", type="string", dest="filename"),
    make_option("-q", "--quiet",
                action="store_false", dest="verbose"),
    ]
parser = OptionParser(option_list=option_list)

```

(`make_option()` is a factory function for creating Option instances; currently it is an alias for the Option constructor. A future version of `optparse` may split Option into several classes, and `make_option()` will pick the right class to instantiate. Do not instantiate Option directly.)
### Defining options[¶](https://docs.python.org/3/library/optparse.html#defining-options "Link to this heading")
Each Option instance represents a set of synonymous command-line option strings, e.g. `-f` and `--file`. You can specify any number of short or long option strings, but you must specify at least one overall option string.
The canonical way to create an [`Option`](https://docs.python.org/3/library/optparse.html#optparse.Option "optparse.Option") instance is with the `add_option()` method of [`OptionParser`](https://docs.python.org/3/library/optparse.html#optparse.OptionParser "optparse.OptionParser").

OptionParser.add_option(_option_)[¶](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.add_option "Link to this definition")


OptionParser.add_option(_*opt_str_ , _attr=value_ , _..._)

To define an option with only a short option string:
Copy```
parser.add_option("-f", attr=value, ...)

```

And to define an option with only a long option string:
Copy```
parser.add_option("--foo", attr=value, ...)

```

The keyword arguments define attributes of the new Option object. The most important option attribute is [`action`](https://docs.python.org/3/library/optparse.html#optparse.Option.action "optparse.Option.action"), and it largely determines which other attributes are relevant or required. If you pass irrelevant option attributes, or fail to pass required ones, `optparse` raises an [`OptionError`](https://docs.python.org/3/library/optparse.html#optparse.OptionError "optparse.OptionError") exception explaining your mistake.
An option’s _action_ determines what `optparse` does when it encounters this option on the command-line. The standard option actions hard-coded into `optparse` are:

`"store"`

store this option’s argument (default)

`"store_const"`

store a constant value, pre-set via [`Option.const`](https://docs.python.org/3/library/optparse.html#optparse.Option.const "optparse.Option.const")

`"store_true"`

store `True`

`"store_false"`

store `False`

`"append"`

append this option’s argument to a list

`"append_const"`

append a constant value to a list, pre-set via [`Option.const`](https://docs.python.org/3/library/optparse.html#optparse.Option.const "optparse.Option.const")

`"count"`

increment a counter by one

`"callback"`

call a specified function

`"help"`

print a usage message including all options and the documentation for them
(If you don’t supply an action, the default is `"store"`. For this action, you may also supply [`type`](https://docs.python.org/3/library/optparse.html#optparse.Option.type "optparse.Option.type") and [`dest`](https://docs.python.org/3/library/optparse.html#optparse.Option.dest "optparse.Option.dest") option attributes; see [Standard option actions](https://docs.python.org/3/library/optparse.html#optparse-standard-option-actions).)
As you can see, most actions involve storing or updating a value somewhere. `optparse` always creates a special object for this, conventionally called `options`, which is an instance of [`optparse.Values`](https://docs.python.org/3/library/optparse.html#optparse.Values "optparse.Values").

_class_ optparse.Values[¶](https://docs.python.org/3/library/optparse.html#optparse.Values "Link to this definition")

An object holding parsed argument names and values as attributes. Normally created by calling when calling [`OptionParser.parse_args()`](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.parse_args "optparse.OptionParser.parse_args"), and can be overridden by a custom subclass passed to the _values_ argument of `OptionParser.parse_args()` (as described in [Parsing arguments](https://docs.python.org/3/library/optparse.html#optparse-parsing-arguments)).
Option arguments (and various other values) are stored as attributes of this object, according to the [`dest`](https://docs.python.org/3/library/optparse.html#optparse.Option.dest "optparse.Option.dest") (destination) option attribute.
For example, when you call
Copy```
parser.parse_args()

```

one of the first things `optparse` does is create the `options` object:
Copy```
options = Values()

```

If one of the options in this parser is defined with
Copy```
parser.add_option("-f", "--file", action="store", type="string", dest="filename")

```

and the command-line being parsed includes any of the following:
Copy```
-ffoo
-f foo
--file=foo
--file foo

```

then `optparse`, on seeing this option, will do the equivalent of
Copy```
options.filename = "foo"

```

The [`type`](https://docs.python.org/3/library/optparse.html#optparse.Option.type "optparse.Option.type") and [`dest`](https://docs.python.org/3/library/optparse.html#optparse.Option.dest "optparse.Option.dest") option attributes are almost as important as [`action`](https://docs.python.org/3/library/optparse.html#optparse.Option.action "optparse.Option.action"), but `action` is the only one that makes sense for _all_ options.
### Option attributes[¶](https://docs.python.org/3/library/optparse.html#option-attributes "Link to this heading")

_class_ optparse.Option[¶](https://docs.python.org/3/library/optparse.html#optparse.Option "Link to this definition")

A single command line argument, with various attributes passed by keyword to the constructor. Normally created with [`OptionParser.add_option()`](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.add_option "optparse.OptionParser.add_option") rather than directly, and can be overridden by a custom class via the _option_class_ argument to [`OptionParser`](https://docs.python.org/3/library/optparse.html#optparse.OptionParser "optparse.OptionParser").
The following option attributes may be passed as keyword arguments to [`OptionParser.add_option()`](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.add_option "optparse.OptionParser.add_option"). If you pass an option attribute that is not relevant to a particular option, or fail to pass a required option attribute, `optparse` raises [`OptionError`](https://docs.python.org/3/library/optparse.html#optparse.OptionError "optparse.OptionError").

Option.action[¶](https://docs.python.org/3/library/optparse.html#optparse.Option.action "Link to this definition")

(default: `"store"`)
Determines `optparse`’s behaviour when this option is seen on the command line; the available options are documented [here](https://docs.python.org/3/library/optparse.html#optparse-standard-option-actions).

Option.type[¶](https://docs.python.org/3/library/optparse.html#optparse.Option.type "Link to this definition")

(default: `"string"`)
The argument type expected by this option (e.g., `"string"` or `"int"`); the available option types are documented [here](https://docs.python.org/3/library/optparse.html#optparse-standard-option-types).

Option.dest[¶](https://docs.python.org/3/library/optparse.html#optparse.Option.dest "Link to this definition")

(default: derived from option strings)
If the option’s action implies writing or modifying a value somewhere, this tells `optparse` where to write it: `dest` names an attribute of the `options` object that `optparse` builds as it parses the command line.

Option.default[¶](https://docs.python.org/3/library/optparse.html#optparse.Option.default "Link to this definition")

The value to use for this option’s destination if the option is not seen on the command line. See also [`OptionParser.set_defaults()`](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.set_defaults "optparse.OptionParser.set_defaults").

Option.nargs[¶](https://docs.python.org/3/library/optparse.html#optparse.Option.nargs "Link to this definition")

(default: 1)
How many arguments of type [`type`](https://docs.python.org/3/library/optparse.html#optparse.Option.type "optparse.Option.type") should be consumed when this option is seen. If > 1, `optparse` will store a tuple of values to [`dest`](https://docs.python.org/3/library/optparse.html#optparse.Option.dest "optparse.Option.dest").

Option.const[¶](https://docs.python.org/3/library/optparse.html#optparse.Option.const "Link to this definition")

For actions that store a constant value, the constant value to store.

Option.choices[¶](https://docs.python.org/3/library/optparse.html#optparse.Option.choices "Link to this definition")

For options of type `"choice"`, the list of strings the user may choose from.

Option.callback[¶](https://docs.python.org/3/library/optparse.html#optparse.Option.callback "Link to this definition")

For options with action `"callback"`, the callable to call when this option is seen. See section [Option Callbacks](https://docs.python.org/3/library/optparse.html#optparse-option-callbacks) for detail on the arguments passed to the callable.

Option.callback_args[¶](https://docs.python.org/3/library/optparse.html#optparse.Option.callback_args "Link to this definition")


Option.callback_kwargs[¶](https://docs.python.org/3/library/optparse.html#optparse.Option.callback_kwargs "Link to this definition")

Additional positional and keyword arguments to pass to `callback` after the four standard callback arguments.

Option.help[¶](https://docs.python.org/3/library/optparse.html#optparse.Option.help "Link to this definition")

Help text to print for this option when listing all available options after the user supplies a `help` option (such as `--help`). If no help text is supplied, the option will be listed without help text. To hide this option, use the special value `optparse.SUPPRESS_HELP`.

Option.metavar[¶](https://docs.python.org/3/library/optparse.html#optparse.Option.metavar "Link to this definition")

(default: derived from option strings)
Stand-in for the option argument(s) to use when printing help text. See section [Tutorial](https://docs.python.org/3/library/optparse.html#optparse-tutorial) for an example.
### Standard option actions[¶](https://docs.python.org/3/library/optparse.html#standard-option-actions "Link to this heading")
The various option actions all have slightly different requirements and effects. Most actions have several relevant option attributes which you may specify to guide `optparse`’s behaviour; a few have required attributes, which you must specify for any option using that action.
  * `"store"` [relevant: [`type`](https://docs.python.org/3/library/optparse.html#optparse.Option.type "optparse.Option.type"), [`dest`](https://docs.python.org/3/library/optparse.html#optparse.Option.dest "optparse.Option.dest"), [`nargs`](https://docs.python.org/3/library/optparse.html#optparse.Option.nargs "optparse.Option.nargs"), [`choices`](https://docs.python.org/3/library/optparse.html#optparse.Option.choices "optparse.Option.choices")]
The option must be followed by an argument, which is converted to a value according to [`type`](https://docs.python.org/3/library/optparse.html#optparse.Option.type "optparse.Option.type") and stored in [`dest`](https://docs.python.org/3/library/optparse.html#optparse.Option.dest "optparse.Option.dest"). If [`nargs`](https://docs.python.org/3/library/optparse.html#optparse.Option.nargs "optparse.Option.nargs") > 1, multiple arguments will be consumed from the command line; all will be converted according to `type` and stored to `dest` as a tuple. See the [Standard option types](https://docs.python.org/3/library/optparse.html#optparse-standard-option-types) section.
If [`choices`](https://docs.python.org/3/library/optparse.html#optparse.Option.choices "optparse.Option.choices") is supplied (a list or tuple of strings), the type defaults to `"choice"`.
If [`type`](https://docs.python.org/3/library/optparse.html#optparse.Option.type "optparse.Option.type") is not supplied, it defaults to `"string"`.
If [`dest`](https://docs.python.org/3/library/optparse.html#optparse.Option.dest "optparse.Option.dest") is not supplied, `optparse` derives a destination from the first long option string (e.g., `--foo-bar` implies `foo_bar`). If there are no long option strings, `optparse` derives a destination from the first short option string (e.g., `-f` implies `f`).
Example:
Copy```
parser.add_option("-f")
parser.add_option("-p", type="float", nargs=3, dest="point")

```

As it parses the command line
Copy```
-f foo.txt -p 1 -3.5 4 -fbar.txt

```

`optparse` will set
Copy```
options.f = "foo.txt"
options.point = (1.0, -3.5, 4.0)
options.f = "bar.txt"

```

  * `"store_const"` [required: [`const`](https://docs.python.org/3/library/optparse.html#optparse.Option.const "optparse.Option.const"); relevant: [`dest`](https://docs.python.org/3/library/optparse.html#optparse.Option.dest "optparse.Option.dest")]
The value [`const`](https://docs.python.org/3/library/optparse.html#optparse.Option.const "optparse.Option.const") is stored in [`dest`](https://docs.python.org/3/library/optparse.html#optparse.Option.dest "optparse.Option.dest").
Example:
Copy```
parser.add_option("-q", "--quiet",
                  action="store_const", const=0, dest="verbose")
parser.add_option("-v", "--verbose",
                  action="store_const", const=1, dest="verbose")
parser.add_option("--noisy",
                  action="store_const", const=2, dest="verbose")

```

If `--noisy` is seen, `optparse` will set
Copy```
options.verbose = 2

```

  * `"store_true"` [relevant: [`dest`](https://docs.python.org/3/library/optparse.html#optparse.Option.dest "optparse.Option.dest")]
A special case of `"store_const"` that stores `True` to [`dest`](https://docs.python.org/3/library/optparse.html#optparse.Option.dest "optparse.Option.dest").
  * `"store_false"` [relevant: [`dest`](https://docs.python.org/3/library/optparse.html#optparse.Option.dest "optparse.Option.dest")]
Like `"store_true"`, but stores `False`.
Example:
Copy```
parser.add_option("--clobber", action="store_true", dest="clobber")
parser.add_option("--no-clobber", action="store_false", dest="clobber")

```

  * `"append"` [relevant: [`type`](https://docs.python.org/3/library/optparse.html#optparse.Option.type "optparse.Option.type"), [`dest`](https://docs.python.org/3/library/optparse.html#optparse.Option.dest "optparse.Option.dest"), [`nargs`](https://docs.python.org/3/library/optparse.html#optparse.Option.nargs "optparse.Option.nargs"), [`choices`](https://docs.python.org/3/library/optparse.html#optparse.Option.choices "optparse.Option.choices")]
The option must be followed by an argument, which is appended to the list in [`dest`](https://docs.python.org/3/library/optparse.html#optparse.Option.dest "optparse.Option.dest"). If no default value for `dest` is supplied, an empty list is automatically created when `optparse` first encounters this option on the command-line. If [`nargs`](https://docs.python.org/3/library/optparse.html#optparse.Option.nargs "optparse.Option.nargs") > 1, multiple arguments are consumed, and a tuple of length `nargs` is appended to `dest`.
The defaults for [`type`](https://docs.python.org/3/library/optparse.html#optparse.Option.type "optparse.Option.type") and [`dest`](https://docs.python.org/3/library/optparse.html#optparse.Option.dest "optparse.Option.dest") are the same as for the `"store"` action.
Example:
Copy```
parser.add_option("-t", "--tracks", action="append", type="int")

```

If `-t3` is seen on the command-line, `optparse` does the equivalent of:
Copy```
options.tracks = []
options.tracks.append(int("3"))

```

If, a little later on, `--tracks=4` is seen, it does:
Copy```
options.tracks.append(int("4"))

```

The `append` action calls the `append` method on the current value of the option. This means that any default value specified must have an `append` method. It also means that if the default value is non-empty, the default elements will be present in the parsed value for the option, with any values from the command line appended after those default values:
Copy```
>>> parser.add_option("--files", action="append", default=['~/.mypkg/defaults'])
>>> opts, args = parser.parse_args(['--files', 'overrides.mypkg'])
>>> opts.files
['~/.mypkg/defaults', 'overrides.mypkg']

```

  * `"append_const"` [required: [`const`](https://docs.python.org/3/library/optparse.html#optparse.Option.const "optparse.Option.const"); relevant: [`dest`](https://docs.python.org/3/library/optparse.html#optparse.Option.dest "optparse.Option.dest")]
Like `"store_const"`, but the value [`const`](https://docs.python.org/3/library/optparse.html#optparse.Option.const "optparse.Option.const") is appended to [`dest`](https://docs.python.org/3/library/optparse.html#optparse.Option.dest "optparse.Option.dest"); as with `"append"`, `dest` defaults to `None`, and an empty list is automatically created the first time the option is encountered.
  * `"count"` [relevant: [`dest`](https://docs.python.org/3/library/optparse.html#optparse.Option.dest "optparse.Option.dest")]
Increment the integer stored at [`dest`](https://docs.python.org/3/library/optparse.html#optparse.Option.dest "optparse.Option.dest"). If no default value is supplied, `dest` is set to zero before being incremented the first time.
Example:
Copy```
parser.add_option("-v", action="count", dest="verbosity")

```

The first time `-v` is seen on the command line, `optparse` does the equivalent of:
Copy```
options.verbosity = 0
options.verbosity += 1

```

Every subsequent occurrence of `-v` results in
Copy```
options.verbosity += 1

```

  * `"callback"` [required: [`callback`](https://docs.python.org/3/library/optparse.html#optparse.Option.callback "optparse.Option.callback"); relevant: [`type`](https://docs.python.org/3/library/optparse.html#optparse.Option.type "optparse.Option.type"), [`nargs`](https://docs.python.org/3/library/optparse.html#optparse.Option.nargs "optparse.Option.nargs"), [`callback_args`](https://docs.python.org/3/library/optparse.html#optparse.Option.callback_args "optparse.Option.callback_args"), [`callback_kwargs`](https://docs.python.org/3/library/optparse.html#optparse.Option.callback_kwargs "optparse.Option.callback_kwargs")]
Call the function specified by [`callback`](https://docs.python.org/3/library/optparse.html#optparse.Option.callback "optparse.Option.callback"), which is called as
Copy```
func(option, opt_str, value, parser, *args, **kwargs)

```

See section [Option Callbacks](https://docs.python.org/3/library/optparse.html#optparse-option-callbacks) for more detail.
  * `"help"`
Prints a complete help message for all the options in the current option parser. The help message is constructed from the `usage` string passed to OptionParser’s constructor and the [`help`](https://docs.python.org/3/library/optparse.html#optparse.Option.help "optparse.Option.help") string passed to every option.
If no [`help`](https://docs.python.org/3/library/optparse.html#optparse.Option.help "optparse.Option.help") string is supplied for an option, it will still be listed in the help message. To omit an option entirely, use the special value `optparse.SUPPRESS_HELP`.
`optparse` automatically adds a [`help`](https://docs.python.org/3/library/optparse.html#optparse.Option.help "optparse.Option.help") option to all OptionParsers, so you do not normally need to create one.
Example:
Copy```
from optparse import OptionParser, SUPPRESS_HELP
