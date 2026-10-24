# be suppressed using the add_help_option argument
parser = OptionParser(add_help_option=False)

parser.add_option("-h", "--help", action="help")
parser.add_option("-v", action="store_true", dest="verbose",
                  help="Be moderately verbose")
parser.add_option("--file", dest="filename",
                  help="Input file to read data from")
parser.add_option("--secret", help=SUPPRESS_HELP)

```

If `optparse` sees either `-h` or `--help` on the command line, it will print something like the following help message to stdout (assuming `sys.argv[0]` is `"foo.py"`):
```
Usage: foo.py [options]

Options:
  -h, --help        Show this help message and exit
  -v                Be moderately verbose
  --file=FILENAME   Input file to read data from

```

After printing the help message, `optparse` terminates your process with `sys.exit(0)`.
  * `"version"`
Prints the version number supplied to the OptionParser to stdout and exits. The version number is actually formatted and printed by the `print_version()` method of OptionParser. Generally only relevant if the `version` argument is supplied to the OptionParser constructor. As with [`help`](https://docs.python.org/3/library/optparse.html#optparse.Option.help "optparse.Option.help") options, you will rarely create `version` options, since `optparse` automatically adds them when needed.


### Standard option types[¶](https://docs.python.org/3/library/optparse.html#standard-option-types "Link to this heading")
`optparse` has five built-in option types: `"string"`, `"int"`, `"choice"`, `"float"` and `"complex"`. If you need to add new option types, see section [Extending optparse](https://docs.python.org/3/library/optparse.html#optparse-extending-optparse).
Arguments to string options are not checked or converted in any way: the text on the command line is stored in the destination (or passed to the callback) as-is.
Integer arguments (type `"int"`) are parsed as follows:
  * if the number starts with `0x`, it is parsed as a hexadecimal number
  * if the number starts with `0`, it is parsed as an octal number
  * if the number starts with `0b`, it is parsed as a binary number
  * otherwise, the number is parsed as a decimal number


The conversion is done by calling [`int()`](https://docs.python.org/3/library/functions.html#int "int") with the appropriate base (2, 8, 10, or 16). If this fails, so will `optparse`, although with a more useful error message.
`"float"` and `"complex"` option arguments are converted directly with [`float()`](https://docs.python.org/3/library/functions.html#float "float") and [`complex()`](https://docs.python.org/3/library/functions.html#complex "complex"), with similar error-handling.
`"choice"` options are a subtype of `"string"` options. The [`choices`](https://docs.python.org/3/library/optparse.html#optparse.Option.choices "optparse.Option.choices") option attribute (a sequence of strings) defines the set of allowed option arguments. `optparse.check_choice()` compares user-supplied option arguments against this master list and raises [`OptionValueError`](https://docs.python.org/3/library/optparse.html#optparse.OptionValueError "optparse.OptionValueError") if an invalid string is given.
### Parsing arguments[¶](https://docs.python.org/3/library/optparse.html#parsing-arguments "Link to this heading")
The whole point of creating and populating an OptionParser is to call its [`parse_args()`](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.parse_args "optparse.OptionParser.parse_args") method.

OptionParser.parse_args(_args =None_, _values =None_)[¶](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.parse_args "Link to this definition")

Parse the command-line options found in _args_.
The input parameters are

`args`

the list of arguments to process (default: `sys.argv[1:]`)

`values`

a [`Values`](https://docs.python.org/3/library/optparse.html#optparse.Values "optparse.Values") object to store option arguments in (default: a new instance of `Values`) – if you give an existing object, the option defaults will not be initialized on it
and the return value is a pair `(options, args)` where

`options`

the same object that was passed in as _values_ , or the `optparse.Values` instance created by `optparse`

`args`

the leftover positional arguments after all options have been processed
The most common usage is to supply neither keyword argument. If you supply `values`, it will be modified with repeated [`setattr()`](https://docs.python.org/3/library/functions.html#setattr "setattr") calls (roughly one for every option argument stored to an option destination) and returned by [`parse_args()`](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.parse_args "optparse.OptionParser.parse_args").
If [`parse_args()`](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.parse_args "optparse.OptionParser.parse_args") encounters any errors in the argument list, it calls the OptionParser’s `error()` method with an appropriate end-user error message. This ultimately terminates your process with an exit status of 2 (the traditional Unix exit status for command-line errors).
### Querying and manipulating your option parser[¶](https://docs.python.org/3/library/optparse.html#querying-and-manipulating-your-option-parser "Link to this heading")
The default behavior of the option parser can be customized slightly, and you can also poke around your option parser and see what’s there. OptionParser provides several methods to help you out:

OptionParser.disable_interspersed_args()[¶](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.disable_interspersed_args "Link to this definition")

Set parsing to stop on the first non-option. For example, if `-a` and `-b` are both simple options that take no arguments, `optparse` normally accepts this syntax:
Copy```
prog -a arg1 -b arg2

```

and treats it as equivalent to
Copy```
prog -a -b arg1 arg2

```

To disable this feature, call `disable_interspersed_args()`. This restores traditional Unix syntax, where option parsing stops with the first non-option argument.
Use this if you have a command processor which runs another command which has options of its own and you want to make sure these options don’t get confused. For example, each command might have a different set of options.

OptionParser.enable_interspersed_args()[¶](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.enable_interspersed_args "Link to this definition")

Set parsing to not stop on the first non-option, allowing interspersing switches with command arguments. This is the default behavior.

OptionParser.get_option(_opt_str_)[¶](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.get_option "Link to this definition")

Returns the Option instance with the option string _opt_str_ , or `None` if no options have that option string.

OptionParser.has_option(_opt_str_)[¶](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.has_option "Link to this definition")

Return `True` if the OptionParser has an option with option string _opt_str_ (e.g., `-q` or `--verbose`).

OptionParser.remove_option(_opt_str_)[¶](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.remove_option "Link to this definition")

If the [`OptionParser`](https://docs.python.org/3/library/optparse.html#optparse.OptionParser "optparse.OptionParser") has an option corresponding to _opt_str_ , that option is removed. If that option provided any other option strings, all of those option strings become invalid. If _opt_str_ does not occur in any option belonging to this `OptionParser`, raises [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError").
### Conflicts between options[¶](https://docs.python.org/3/library/optparse.html#conflicts-between-options "Link to this heading")
If you’re not careful, it’s easy to define options with conflicting option strings:
Copy```
parser.add_option("-n", "--dry-run", ...)
...
parser.add_option("-n", "--noisy", ...)

```

(This is particularly true if you’ve defined your own OptionParser subclass with some standard options.)
Every time you add an option, `optparse` checks for conflicts with existing options. If it finds any, it invokes the current conflict-handling mechanism. You can set the conflict-handling mechanism either in the constructor:
Copy```
parser = OptionParser(..., conflict_handler=handler)

```

or with a separate call:
Copy```
parser.set_conflict_handler(handler)

```

The available conflict handlers are:
>

`"error"` (default)

> assume option conflicts are a programming error and raise [`OptionConflictError`](https://docs.python.org/3/library/optparse.html#optparse.OptionConflictError "optparse.OptionConflictError")

`"resolve"`

> resolve option conflicts intelligently (see below)
As an example, let’s define an [`OptionParser`](https://docs.python.org/3/library/optparse.html#optparse.OptionParser "optparse.OptionParser") that resolves conflicts intelligently and add conflicting options to it:
Copy```
parser = OptionParser(conflict_handler="resolve")
parser.add_option("-n", "--dry-run", ..., help="do no harm")
parser.add_option("-n", "--noisy", ..., help="be noisy")

```

At this point, `optparse` detects that a previously added option is already using the `-n` option string. Since `conflict_handler` is `"resolve"`, it resolves the situation by removing `-n` from the earlier option’s list of option strings. Now `--dry-run` is the only way for the user to activate that option. If the user asks for help, the help message will reflect that:
Copy```
Options:
  --dry-run     do no harm
  ...
  -n, --noisy   be noisy

```

It’s possible to whittle away the option strings for a previously added option until there are none left, and the user has no way of invoking that option from the command-line. In that case, `optparse` removes that option completely, so it doesn’t show up in help text or anywhere else. Carrying on with our existing OptionParser:
Copy```
parser.add_option("--dry-run", ..., help="new dry-run option")

```

At this point, the original `-n`/`--dry-run` option is no longer accessible, so `optparse` removes it, leaving this help text:
Copy```
Options:
  ...
  -n, --noisy   be noisy
  --dry-run     new dry-run option

```

### Cleanup[¶](https://docs.python.org/3/library/optparse.html#cleanup "Link to this heading")
OptionParser instances have several cyclic references. This should not be a problem for Python’s garbage collector, but you may wish to break the cyclic references explicitly by calling `destroy()` on your OptionParser once you are done with it. This is particularly useful in long-running applications where large object graphs are reachable from your OptionParser.
### Other methods[¶](https://docs.python.org/3/library/optparse.html#other-methods "Link to this heading")
OptionParser supports several other public methods:

OptionParser.set_usage(_usage_)[¶](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.set_usage "Link to this definition")

Set the usage string according to the rules described above for the `usage` constructor keyword argument. Passing `None` sets the default usage string; use `optparse.SUPPRESS_USAGE` to suppress a usage message.

OptionParser.print_usage(_file =None_)[¶](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.print_usage "Link to this definition")

Print the usage message for the current program (`self.usage`) to _file_ (default stdout). Any occurrence of the string `%prog` in `self.usage` is replaced with the name of the current program. Does nothing if `self.usage` is empty or not defined.

OptionParser.get_usage()[¶](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.get_usage "Link to this definition")

Same as [`print_usage()`](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.print_usage "optparse.OptionParser.print_usage") but returns the usage string instead of printing it.

OptionParser.set_defaults(_dest=value_ , _..._)[¶](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.set_defaults "Link to this definition")

Set default values for several option destinations at once. Using `set_defaults()` is the preferred way to set default values for options, since multiple options can share the same destination. For example, if several “mode” options all set the same destination, any one of them can set the default, and the last one wins:
Copy```
parser.add_option("--advanced", action="store_const",
                  dest="mode", const="advanced",
                  default="novice")    # overridden below
parser.add_option("--novice", action="store_const",
                  dest="mode", const="novice",
                  default="advanced")  # overrides above setting

```

To avoid this confusion, use `set_defaults()`:
Copy```
parser.set_defaults(mode="advanced")
parser.add_option("--advanced", action="store_const",
                  dest="mode", const="advanced")
parser.add_option("--novice", action="store_const",
                  dest="mode", const="novice")

```
