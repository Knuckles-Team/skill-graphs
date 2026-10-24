## Option Callbacks[¶](https://docs.python.org/3/library/optparse.html#option-callbacks "Link to this heading")
When `optparse`’s built-in actions and types aren’t quite enough for your needs, you have two choices: extend `optparse` or define a callback option. Extending `optparse` is more general, but overkill for a lot of simple cases. Quite often a simple callback is all you need.
There are two steps to defining a callback option:
  * define the option itself using the `"callback"` action
  * write the callback; this is a function (or method) that takes at least four arguments, as described below


### Defining a callback option[¶](https://docs.python.org/3/library/optparse.html#defining-a-callback-option "Link to this heading")
As always, the easiest way to define a callback option is by using the [`OptionParser.add_option()`](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.add_option "optparse.OptionParser.add_option") method. Apart from [`action`](https://docs.python.org/3/library/optparse.html#optparse.Option.action "optparse.Option.action"), the only option attribute you must specify is `callback`, the function to call:
Copy```
parser.add_option("-c", action="callback", callback=my_callback)

```

`callback` is a function (or other callable object), so you must have already defined `my_callback()` when you create this callback option. In this simple case, `optparse` doesn’t even know if `-c` takes any arguments, which usually means that the option takes no arguments—the mere presence of `-c` on the command-line is all it needs to know. In some circumstances, though, you might want your callback to consume an arbitrary number of command-line arguments. This is where writing callbacks gets tricky; it’s covered later in this section.
`optparse` always passes four particular arguments to your callback, and it will only pass additional arguments if you specify them via [`callback_args`](https://docs.python.org/3/library/optparse.html#optparse.Option.callback_args "optparse.Option.callback_args") and [`callback_kwargs`](https://docs.python.org/3/library/optparse.html#optparse.Option.callback_kwargs "optparse.Option.callback_kwargs"). Thus, the minimal callback function signature is:
Copy```
def my_callback(option, opt, value, parser):

```

The four arguments to a callback are described below.
There are several other option attributes that you can supply when you define a callback option:

[`type`](https://docs.python.org/3/library/optparse.html#optparse.Option.type "optparse.Option.type")

has its usual meaning: as with the `"store"` or `"append"` actions, it instructs `optparse` to consume one argument and convert it to [`type`](https://docs.python.org/3/library/optparse.html#optparse.Option.type "optparse.Option.type"). Rather than storing the converted value(s) anywhere, though, `optparse` passes it to your callback function.

[`nargs`](https://docs.python.org/3/library/optparse.html#optparse.Option.nargs "optparse.Option.nargs")

also has its usual meaning: if it is supplied and > 1, `optparse` will consume [`nargs`](https://docs.python.org/3/library/optparse.html#optparse.Option.nargs "optparse.Option.nargs") arguments, each of which must be convertible to [`type`](https://docs.python.org/3/library/optparse.html#optparse.Option.type "optparse.Option.type"). It then passes a tuple of converted values to your callback.

[`callback_args`](https://docs.python.org/3/library/optparse.html#optparse.Option.callback_args "optparse.Option.callback_args")

a tuple of extra positional arguments to pass to the callback

[`callback_kwargs`](https://docs.python.org/3/library/optparse.html#optparse.Option.callback_kwargs "optparse.Option.callback_kwargs")

a dictionary of extra keyword arguments to pass to the callback
### How callbacks are called[¶](https://docs.python.org/3/library/optparse.html#how-callbacks-are-called "Link to this heading")
All callbacks are called as follows:
Copy```
func(option, opt_str, value, parser, *args, **kwargs)

```

where

`option`

is the Option instance that’s calling the callback

`opt_str`

is the option string seen on the command-line that’s triggering the callback. (If an abbreviated long option was used, `opt_str` will be the full, canonical option string—e.g. if the user puts `--foo` on the command-line as an abbreviation for `--foobar`, then `opt_str` will be `"--foobar"`.)

`value`

is the argument to this option seen on the command-line. `optparse` will only expect an argument if [`type`](https://docs.python.org/3/library/optparse.html#optparse.Option.type "optparse.Option.type") is set; the type of `value` will be the type implied by the option’s type. If `type` for this option is `None` (no argument expected), then `value` will be `None`. If [`nargs`](https://docs.python.org/3/library/optparse.html#optparse.Option.nargs "optparse.Option.nargs") > 1, `value` will be a tuple of values of the appropriate type.

`parser`

is the OptionParser instance driving the whole thing, mainly useful because you can access some other interesting data through its instance attributes:

`parser.largs`

the current list of leftover arguments, ie. arguments that have been consumed but are neither options nor option arguments. Feel free to modify `parser.largs`, e.g. by adding more arguments to it. (This list will become `args`, the second return value of [`parse_args()`](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.parse_args "optparse.OptionParser.parse_args").)

`parser.rargs`

the current list of remaining arguments, ie. with `opt_str` and `value` (if applicable) removed, and only the arguments following them still there. Feel free to modify `parser.rargs`, e.g. by consuming more arguments.

`parser.values`

the object where option values are by default stored (an instance of optparse.OptionValues). This lets callbacks use the same mechanism as the rest of `optparse` for storing option values; you don’t need to mess around with globals or closures. You can also access or modify the value(s) of any options already encountered on the command-line.

`args`

is a tuple of arbitrary positional arguments supplied via the [`callback_args`](https://docs.python.org/3/library/optparse.html#optparse.Option.callback_args "optparse.Option.callback_args") option attribute.

`kwargs`

is a dictionary of arbitrary keyword arguments supplied via [`callback_kwargs`](https://docs.python.org/3/library/optparse.html#optparse.Option.callback_kwargs "optparse.Option.callback_kwargs").
### Raising errors in a callback[¶](https://docs.python.org/3/library/optparse.html#raising-errors-in-a-callback "Link to this heading")
The callback function should raise [`OptionValueError`](https://docs.python.org/3/library/optparse.html#optparse.OptionValueError "optparse.OptionValueError") if there are any problems with the option or its argument(s). `optparse` catches this and terminates the program, printing the error message you supply to stderr. Your message should be clear, concise, accurate, and mention the option at fault. Otherwise, the user will have a hard time figuring out what they did wrong.
### Callback example 1: trivial callback[¶](https://docs.python.org/3/library/optparse.html#callback-example-1-trivial-callback "Link to this heading")
Here’s an example of a callback option that takes no arguments, and simply records that the option was seen:
Copy```
def record_foo_seen(option, opt_str, value, parser):
    parser.values.saw_foo = True

parser.add_option("--foo", action="callback", callback=record_foo_seen)

```

Of course, you could do that with the `"store_true"` action.
### Callback example 2: check option order[¶](https://docs.python.org/3/library/optparse.html#callback-example-2-check-option-order "Link to this heading")
Here’s a slightly more interesting example: record the fact that `-a` is seen, but blow up if it comes after `-b` in the command-line.
Copy```
def check_order(option, opt_str, value, parser):
    if parser.values.b:
        raise OptionValueError("can't use -a after -b")
    parser.values.a = 1
...
parser.add_option("-a", action="callback", callback=check_order)
parser.add_option("-b", action="store_true", dest="b")

```

### Callback example 3: check option order (generalized)[¶](https://docs.python.org/3/library/optparse.html#callback-example-3-check-option-order-generalized "Link to this heading")
If you want to reuse this callback for several similar options (set a flag, but blow up if `-b` has already been seen), it needs a bit of work: the error message and the flag that it sets must be generalized.
Copy```
def check_order(option, opt_str, value, parser):
    if parser.values.b:
        raise OptionValueError("can't use %s after -b" % opt_str)
    setattr(parser.values, option.dest, 1)
...
parser.add_option("-a", action="callback", callback=check_order, dest='a')
parser.add_option("-b", action="store_true", dest="b")
parser.add_option("-c", action="callback", callback=check_order, dest='c')

```

### Callback example 4: check arbitrary condition[¶](https://docs.python.org/3/library/optparse.html#callback-example-4-check-arbitrary-condition "Link to this heading")
Of course, you could put any condition in there—you’re not limited to checking the values of already-defined options. For example, if you have options that should not be called when the moon is full, all you have to do is this:
Copy```
def check_moon(option, opt_str, value, parser):
    if is_moon_full():
        raise OptionValueError("%s option invalid when moon is full"
                               % opt_str)
    setattr(parser.values, option.dest, 1)
...
parser.add_option("--foo",
                  action="callback", callback=check_moon, dest="foo")

```

(The definition of `is_moon_full()` is left as an exercise for the reader.)
### Callback example 5: fixed arguments[¶](https://docs.python.org/3/library/optparse.html#callback-example-5-fixed-arguments "Link to this heading")
Things get slightly more interesting when you define callback options that take a fixed number of arguments. Specifying that a callback option takes arguments is similar to defining a `"store"` or `"append"` option: if you define [`type`](https://docs.python.org/3/library/optparse.html#optparse.Option.type "optparse.Option.type"), then the option takes one argument that must be convertible to that type; if you further define [`nargs`](https://docs.python.org/3/library/optparse.html#optparse.Option.nargs "optparse.Option.nargs"), then the option takes `nargs` arguments.
Here’s an example that just emulates the standard `"store"` action:
Copy```
def store_value(option, opt_str, value, parser):
    setattr(parser.values, option.dest, value)
...
parser.add_option("--foo",
                  action="callback", callback=store_value,
                  type="int", nargs=3, dest="foo")

```

Note that `optparse` takes care of consuming 3 arguments and converting them to integers for you; all you have to do is store them. (Or whatever; obviously you don’t need a callback for this example.)
### Callback example 6: variable arguments[¶](https://docs.python.org/3/library/optparse.html#callback-example-6-variable-arguments "Link to this heading")
Things get hairy when you want an option to take a variable number of arguments. For this case, you must write a callback, as `optparse` doesn’t provide any built-in capabilities for it. And you have to deal with certain intricacies of conventional Unix command-line parsing that `optparse` normally handles for you. In particular, callbacks should implement the conventional rules for bare `--` and `-` arguments:
  * either `--` or `-` can be option arguments
  * bare `--` (if not the argument to some option): halt command-line processing and discard the `--`
  * bare `-` (if not the argument to some option): halt command-line processing but keep the `-` (append it to `parser.largs`)


If you want an option that takes a variable number of arguments, there are several subtle, tricky issues to worry about. The exact implementation you choose will be based on which trade-offs you’re willing to make for your application (which is why `optparse` doesn’t support this sort of thing directly).
Nevertheless, here’s a stab at a callback for an option with variable arguments:
Copy```
def vararg_callback(option, opt_str, value, parser):
    assert value is None
    value = []

    def floatable(str):
        try:
            float(str)
            return True
        except ValueError:
            return False

    for arg in parser.rargs:
        # stop on --foo like options
        if arg[:2] == "--" and len(arg) > 2:
            break
        # stop on -a, but not on -3 or -3.0
        if arg[:1] == "-" and len(arg) > 1 and not floatable(arg):
            break
        value.append(arg)

    del parser.rargs[:len(value)]
    setattr(parser.values, option.dest, value)

...
parser.add_option("-c", "--callback", dest="vararg_attr",
                  action="callback", callback=vararg_callback)

```

## Extending `optparse`[¶](https://docs.python.org/3/library/optparse.html#extending-optparse "Link to this heading")
Since the two major controlling factors in how `optparse` interprets command-line options are the action and type of each option, the most likely direction of extension is to add new actions and new types.
### Adding new types[¶](https://docs.python.org/3/library/optparse.html#adding-new-types "Link to this heading")
To add new types, you need to define your own subclass of `optparse`’s [`Option`](https://docs.python.org/3/library/optparse.html#optparse.Option "optparse.Option") class. This class has a couple of attributes that define `optparse`’s types: [`TYPES`](https://docs.python.org/3/library/optparse.html#optparse.Option.TYPES "optparse.Option.TYPES") and [`TYPE_CHECKER`](https://docs.python.org/3/library/optparse.html#optparse.Option.TYPE_CHECKER "optparse.Option.TYPE_CHECKER").

Option.TYPES[¶](https://docs.python.org/3/library/optparse.html#optparse.Option.TYPES "Link to this definition")

A tuple of type names; in your subclass, simply define a new tuple [`TYPES`](https://docs.python.org/3/library/optparse.html#optparse.Option.TYPES "optparse.Option.TYPES") that builds on the standard one.

Option.TYPE_CHECKER[¶](https://docs.python.org/3/library/optparse.html#optparse.Option.TYPE_CHECKER "Link to this definition")

A dictionary mapping type names to type-checking functions. A type-checking function has the following signature:
Copy```
def check_mytype(option, opt, value)

```

where `option` is an [`Option`](https://docs.python.org/3/library/optparse.html#optparse.Option "optparse.Option") instance, `opt` is an option string (e.g., `-f`), and `value` is the string from the command line that must be checked and converted to your desired type. `check_mytype()` should return an object of the hypothetical type `mytype`. The value returned by a type-checking function will wind up in the OptionValues instance returned by [`OptionParser.parse_args()`](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.parse_args "optparse.OptionParser.parse_args"), or be passed to a callback as the `value` parameter.
Your type-checking function should raise [`OptionValueError`](https://docs.python.org/3/library/optparse.html#optparse.OptionValueError "optparse.OptionValueError") if it encounters any problems. `OptionValueError` takes a single string argument, which is passed as-is to [`OptionParser`](https://docs.python.org/3/library/optparse.html#optparse.OptionParser "optparse.OptionParser")’s `error()` method, which in turn prepends the program name and the string `"error:"` and prints everything to stderr before terminating the process.
Here’s a silly example that demonstrates adding a `"complex"` option type to parse Python-style complex numbers on the command line. (This is even sillier than it used to be, because `optparse` 1.3 added built-in support for complex numbers, but never mind.)
First, the necessary imports:
Copy```
from copy import copy
from optparse import Option, OptionValueError

```

You need to define your type-checker first, since it’s referred to later (in the [`TYPE_CHECKER`](https://docs.python.org/3/library/optparse.html#optparse.Option.TYPE_CHECKER "optparse.Option.TYPE_CHECKER") class attribute of your Option subclass):
Copy```
def check_complex(option, opt, value):
    try:
        return complex(value)
    except ValueError:
        raise OptionValueError(
            "option %s: invalid complex value: %r" % (opt, value))

```

Finally, the Option subclass:
Copy```
class MyOption (Option):
    TYPES = Option.TYPES + ("complex",)
    TYPE_CHECKER = copy(Option.TYPE_CHECKER)
    TYPE_CHECKER["complex"] = check_complex

```

(If we didn’t make a [`copy()`](https://docs.python.org/3/library/copy.html#module-copy "copy: Shallow and deep copy operations.") of [`Option.TYPE_CHECKER`](https://docs.python.org/3/library/optparse.html#optparse.Option.TYPE_CHECKER "optparse.Option.TYPE_CHECKER"), we would end up modifying the `TYPE_CHECKER` attribute of `optparse`’s Option class. This being Python, nothing stops you from doing that except good manners and common sense.)
That’s it! Now you can write a script that uses the new option type just like any other `optparse`-based script, except you have to instruct your OptionParser to use MyOption instead of Option:
Copy```
parser = OptionParser(option_class=MyOption)
parser.add_option("-c", type="complex")

```

Alternately, you can build your own option list and pass it to OptionParser; if you don’t use `add_option()` in the above way, you don’t need to tell OptionParser which option class to use:
Copy```
option_list = [MyOption("-c", action="store", type="complex", dest="c")]
parser = OptionParser(option_list=option_list)

```

### Adding new actions[¶](https://docs.python.org/3/library/optparse.html#adding-new-actions "Link to this heading")
Adding new actions is a bit trickier, because you have to understand that `optparse` has a couple of classifications for actions:

“store” actions

actions that result in `optparse` storing a value to an attribute of the current OptionValues instance; these options require a [`dest`](https://docs.python.org/3/library/optparse.html#optparse.Option.dest "optparse.Option.dest") attribute to be supplied to the Option constructor.

“typed” actions

actions that take a value from the command line and expect it to be of a certain type; or rather, a string that can be converted to a certain type. These options require a [`type`](https://docs.python.org/3/library/optparse.html#optparse.Option.type "optparse.Option.type") attribute to the Option constructor.
These are overlapping sets: some default “store” actions are `"store"`, `"store_const"`, `"append"`, and `"count"`, while the default “typed” actions are `"store"`, `"append"`, and `"callback"`.
When you add an action, you need to categorize it by listing it in at least one of the following class attributes of Option (all are lists of strings):

Option.ACTIONS[¶](https://docs.python.org/3/library/optparse.html#optparse.Option.ACTIONS "Link to this definition")

All actions must be listed in ACTIONS.

Option.STORE_ACTIONS[¶](https://docs.python.org/3/library/optparse.html#optparse.Option.STORE_ACTIONS "Link to this definition")

“store” actions are additionally listed here.

Option.TYPED_ACTIONS[¶](https://docs.python.org/3/library/optparse.html#optparse.Option.TYPED_ACTIONS "Link to this definition")

“typed” actions are additionally listed here.

Option.ALWAYS_TYPED_ACTIONS[¶](https://docs.python.org/3/library/optparse.html#optparse.Option.ALWAYS_TYPED_ACTIONS "Link to this definition")

Actions that always take a type (i.e. whose options always take a value) are additionally listed here. The only effect of this is that `optparse` assigns the default type, `"string"`, to options with no explicit type whose action is listed in [`ALWAYS_TYPED_ACTIONS`](https://docs.python.org/3/library/optparse.html#optparse.Option.ALWAYS_TYPED_ACTIONS "optparse.Option.ALWAYS_TYPED_ACTIONS").
In order to actually implement your new action, you must override Option’s `take_action()` method and add a case that recognizes your action.
For example, let’s add an `"extend"` action. This is similar to the standard `"append"` action, but instead of taking a single value from the command-line and appending it to an existing list, `"extend"` will take multiple values in a single comma-delimited string, and extend an existing list with them. That is, if `--names` is an `"extend"` option of type `"string"`, the command line
Copy```
--names=foo,bar --names blah --names ding,dong

```

would result in a list
Copy```
["foo", "bar", "blah", "ding", "dong"]

```

Again we define a subclass of Option:
Copy```
class MyOption(Option):

    ACTIONS = Option.ACTIONS + ("extend",)
    STORE_ACTIONS = Option.STORE_ACTIONS + ("extend",)
    TYPED_ACTIONS = Option.TYPED_ACTIONS + ("extend",)
    ALWAYS_TYPED_ACTIONS = Option.ALWAYS_TYPED_ACTIONS + ("extend",)

    def take_action(self, action, dest, opt, value, values, parser):
        if action == "extend":
            lvalue = value.split(",")
            values.ensure_value(dest, []).extend(lvalue)
        else:
            Option.take_action(
                self, action, dest, opt, value, values, parser)

```

Features of note:
  * `"extend"` both expects a value on the command-line and stores that value somewhere, so it goes in both [`STORE_ACTIONS`](https://docs.python.org/3/library/optparse.html#optparse.Option.STORE_ACTIONS "optparse.Option.STORE_ACTIONS") and [`TYPED_ACTIONS`](https://docs.python.org/3/library/optparse.html#optparse.Option.TYPED_ACTIONS "optparse.Option.TYPED_ACTIONS").
  * to ensure that `optparse` assigns the default type of `"string"` to `"extend"` actions, we put the `"extend"` action in [`ALWAYS_TYPED_ACTIONS`](https://docs.python.org/3/library/optparse.html#optparse.Option.ALWAYS_TYPED_ACTIONS "optparse.Option.ALWAYS_TYPED_ACTIONS") as well.
  * `MyOption.take_action()` implements just this one new action, and passes control back to `Option.take_action()` for the standard `optparse` actions.
  * `values` is an instance of the optparse_parser.Values class, which provides the very useful `ensure_value()` method. `ensure_value()` is essentially [`getattr()`](https://docs.python.org/3/library/functions.html#getattr "getattr") with a safety valve; it is called as
Copy```
values.ensure_value(attr, value)

```

If the `attr` attribute of `values` doesn’t exist or is `None`, then ensure_value() first sets it to `value`, and then returns `value`. This is very handy for actions like `"extend"`, `"append"`, and `"count"`, all of which accumulate data in a variable and expect that variable to be of a certain type (a list for the first two, an integer for the latter). Using `ensure_value()` means that scripts using your action don’t have to worry about setting a default value for the option destinations in question; they can just leave the default as `None` and `ensure_value()` will take care of getting it right when it’s needed.


## Exceptions[¶](https://docs.python.org/3/library/optparse.html#exceptions "Link to this heading")

_exception_ optparse.OptionError[¶](https://docs.python.org/3/library/optparse.html#optparse.OptionError "Link to this definition")

Raised if an [`Option`](https://docs.python.org/3/library/optparse.html#optparse.Option "optparse.Option") instance is created with invalid or inconsistent arguments.

_exception_ optparse.OptionConflictError[¶](https://docs.python.org/3/library/optparse.html#optparse.OptionConflictError "Link to this definition")

Raised if conflicting options are added to an [`OptionParser`](https://docs.python.org/3/library/optparse.html#optparse.OptionParser "optparse.OptionParser").

_exception_ optparse.OptionValueError[¶](https://docs.python.org/3/library/optparse.html#optparse.OptionValueError "Link to this definition")

Raised if an invalid option value is encountered on the command line.

_exception_ optparse.BadOptionError[¶](https://docs.python.org/3/library/optparse.html#optparse.BadOptionError "Link to this definition")

Raised if an invalid option is passed on the command line.

_exception_ optparse.AmbiguousOptionError[¶](https://docs.python.org/3/library/optparse.html#optparse.AmbiguousOptionError "Link to this definition")

Raised if an ambiguous option is passed on the command line.
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`optparse` — Parser for command line options](https://docs.python.org/3/library/optparse.html)
    * [Choosing an argument parsing library](https://docs.python.org/3/library/optparse.html#choosing-an-argument-parsing-library)
    * [Introduction](https://docs.python.org/3/library/optparse.html#introduction)
    * [Background](https://docs.python.org/3/library/optparse.html#background)
      * [Terminology](https://docs.python.org/3/library/optparse.html#terminology)
      * [What are options for?](https://docs.python.org/3/library/optparse.html#what-are-options-for)
      * [What are positional arguments for?](https://docs.python.org/3/library/optparse.html#what-are-positional-arguments-for)
    * [Tutorial](https://docs.python.org/3/library/optparse.html#tutorial)
      * [Understanding option actions](https://docs.python.org/3/library/optparse.html#understanding-option-actions)
      * [The store action](https://docs.python.org/3/library/optparse.html#the-store-action)
      * [Handling boolean (flag) options](https://docs.python.org/3/library/optparse.html#handling-boolean-flag-options)
      * [Other actions](https://docs.python.org/3/library/optparse.html#other-actions)
      * [Default values](https://docs.python.org/3/library/optparse.html#default-values)
      * [Generating help](https://docs.python.org/3/library/optparse.html#generating-help)
        * [Grouping Options](https://docs.python.org/3/library/optparse.html#grouping-options)
      * [Printing a version string](https://docs.python.org/3/library/optparse.html#printing-a-version-string)
      * [How `optparse` handles errors](https://docs.python.org/3/library/optparse.html#how-optparse-handles-errors)
      * [Putting it all together](https://docs.python.org/3/library/optparse.html#putting-it-all-together)
    * [Reference Guide](https://docs.python.org/3/library/optparse.html#reference-guide)
      * [Creating the parser](https://docs.python.org/3/library/optparse.html#creating-the-parser)
      * [Populating the parser](https://docs.python.org/3/library/optparse.html#populating-the-parser)
      * [Defining options](https://docs.python.org/3/library/optparse.html#defining-options)
      * [Option attributes](https://docs.python.org/3/library/optparse.html#option-attributes)
      * [Standard option actions](https://docs.python.org/3/library/optparse.html#standard-option-actions)
      * [Standard option types](https://docs.python.org/3/library/optparse.html#standard-option-types)
      * [Parsing arguments](https://docs.python.org/3/library/optparse.html#parsing-arguments)
      * [Querying and manipulating your option parser](https://docs.python.org/3/library/optparse.html#querying-and-manipulating-your-option-parser)
      * [Conflicts between options](https://docs.python.org/3/library/optparse.html#conflicts-between-options)
      * [Cleanup](https://docs.python.org/3/library/optparse.html#cleanup)
      * [Other methods](https://docs.python.org/3/library/optparse.html#other-methods)
    * [Option Callbacks](https://docs.python.org/3/library/optparse.html#option-callbacks)
      * [Defining a callback option](https://docs.python.org/3/library/optparse.html#defining-a-callback-option)
      * [How callbacks are called](https://docs.python.org/3/library/optparse.html#how-callbacks-are-called)
      * [Raising errors in a callback](https://docs.python.org/3/library/optparse.html#raising-errors-in-a-callback)
      * [Callback example 1: trivial callback](https://docs.python.org/3/library/optparse.html#callback-example-1-trivial-callback)
      * [Callback example 2: check option order](https://docs.python.org/3/library/optparse.html#callback-example-2-check-option-order)
      * [Callback example 3: check option order (generalized)](https://docs.python.org/3/library/optparse.html#callback-example-3-check-option-order-generalized)
      * [Callback example 4: check arbitrary condition](https://docs.python.org/3/library/optparse.html#callback-example-4-check-arbitrary-condition)
      * [Callback example 5: fixed arguments](https://docs.python.org/3/library/optparse.html#callback-example-5-fixed-arguments)
      * [Callback example 6: variable arguments](https://docs.python.org/3/library/optparse.html#callback-example-6-variable-arguments)
    * [Extending `optparse`](https://docs.python.org/3/library/optparse.html#extending-optparse)
      * [Adding new types](https://docs.python.org/3/library/optparse.html#adding-new-types)
      * [Adding new actions](https://docs.python.org/3/library/optparse.html#adding-new-actions)
    * [Exceptions](https://docs.python.org/3/library/optparse.html#exceptions)


#### Previous topic
[Migrating `optparse` code to `argparse`](https://docs.python.org/3/howto/argparse-optparse.html "previous chapter")
#### Next topic
[`getpass` — Portable password input](https://docs.python.org/3/library/getpass.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=optparse+%E2%80%94+Parser+for+command+line+options&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Foptparse.html&pagesource=library%2Foptparse.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/getpass.html "getpass — Portable password input") |
  * [previous](https://docs.python.org/3/howto/argparse-optparse.html "Migrating optparse code to argparse") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Command-line interface libraries](https://docs.python.org/3/library/cmdlinelibs.html) »
  * [`optparse` — Parser for command line options](https://docs.python.org/3/library/optparse.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
