[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`pdb` — The Python Debugger](https://docs.python.org/3/library/pdb.html)
    * [Command-line interface](https://docs.python.org/3/library/pdb.html#command-line-interface)
    * [Debugger commands](https://docs.python.org/3/library/pdb.html#debugger-commands)


#### Previous topic
[`faulthandler` — Dump the Python traceback](https://docs.python.org/3/library/faulthandler.html "previous chapter")
#### Next topic
[The Python Profilers](https://docs.python.org/3/library/profile.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=pdb+%E2%80%94+The+Python+Debugger&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fpdb.html&pagesource=library%2Fpdb.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/profile.html "The Python Profilers") |
  * [previous](https://docs.python.org/3/library/faulthandler.html "faulthandler — Dump the Python traceback") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Debugging and Profiling](https://docs.python.org/3/library/debug.html) »
  * [`pdb` — The Python Debugger](https://docs.python.org/3/library/pdb.html)
  * |
  * Theme  Auto Light Dark |


#  `pdb` — The Python Debugger[¶](https://docs.python.org/3/library/pdb.html#module-pdb "Link to this heading")
**Source code:**
* * *
The module `pdb` defines an interactive source code debugger for Python programs. It supports setting (conditional) breakpoints and single stepping at the source line level, inspection of stack frames, source code listing, and evaluation of arbitrary Python code in the context of any stack frame. It also supports post-mortem debugging and can be called under program control.
The debugger is extensible – it is actually defined as the class [`Pdb`](https://docs.python.org/3/library/pdb.html#pdb.Pdb "pdb.Pdb"). This is currently undocumented but easily understood by reading the source. The extension interface uses the modules [`bdb`](https://docs.python.org/3/library/bdb.html#module-bdb "bdb: Debugger framework.") and [`cmd`](https://docs.python.org/3/library/cmd.html#module-cmd "cmd: Build line-oriented command interpreters.").
See also

Module [`faulthandler`](https://docs.python.org/3/library/faulthandler.html#module-faulthandler "faulthandler: Dump the Python traceback.")

Used to dump Python tracebacks explicitly, on a fault, after a timeout, or on a user signal.

Module [`traceback`](https://docs.python.org/3/library/traceback.html#module-traceback "traceback: Print or retrieve a stack traceback.")

Standard interface to extract, format and print stack traces of Python programs.
The typical usage to break into the debugger is to insert:
Copy```
import pdb; pdb.set_trace()

```

Or:
Copy```
breakpoint()

```

at the location you want to break into the debugger, and then run the program. You can then step through the code following this statement, and continue running without the debugger using the [`continue`](https://docs.python.org/3/library/pdb.html#pdbcommand-continue) command.
Changed in version 3.7: The built-in [`breakpoint()`](https://docs.python.org/3/library/functions.html#breakpoint "breakpoint"), when called with defaults, can be used instead of `import pdb; pdb.set_trace()`.
Copy```
def double(x):
   breakpoint()
   return x * 2
val = 3
print(f"{val} * 2 is {double(val)}")

```

The debugger’s prompt is `(Pdb)`, which is the indicator that you are in debug mode:
Copy```
> ...(2)double()
-> breakpoint()
(Pdb) p x
3
(Pdb) continue
3 * 2 is 6

```

Changed in version 3.3: Tab-completion via the [`readline`](https://docs.python.org/3/library/readline.html#module-readline "readline: GNU readline support for Python.") module is available for commands and command arguments, e.g. the current global and local names are offered as arguments of the `p` command.
## Command-line interface[¶](https://docs.python.org/3/library/pdb.html#command-line-interface "Link to this heading")
You can also invoke `pdb` from the command line to debug other scripts. For example:
Copy```
python -m pdb [-c command] (-m module | -p pid | pyfile) [args ...]

```

When invoked as a module, pdb will automatically enter post-mortem debugging if the program being debugged exits abnormally. After post-mortem debugging (or after normal exit of the program), pdb will restart the program. Automatic restarting preserves pdb’s state (such as breakpoints) and in most cases is more useful than quitting the debugger upon program’s exit.

-c, --command <command>[¶](https://docs.python.org/3/library/pdb.html#cmdoption-pdb-c "Link to this definition")

To execute commands as if given in a `.pdbrc` file; see [Debugger commands](https://docs.python.org/3/library/pdb.html#debugger-commands).
Changed in version 3.2: Added the `-c` option.

-m <module>[¶](https://docs.python.org/3/library/pdb.html#cmdoption-pdb-m "Link to this definition")

To execute modules similar to the way `python -m` does. As with a script, the debugger will pause execution just before the first line of the module.
Changed in version 3.7: Added the `-m` option.

-p, --pid <pid>[¶](https://docs.python.org/3/library/pdb.html#cmdoption-pdb-p "Link to this definition")

Attach to the process with the specified PID.
Added in version 3.14.
To attach to a running Python process for remote debugging, use the `-p` or `--pid` option with the target process’s PID:
Copy```
python -m pdb -p 1234

```

Note
Attaching to a process that is blocked in a system call or waiting for I/O will only work once the next bytecode instruction is executed or when the process receives a signal.
Typical usage to execute a statement under control of the debugger is:
Copy```
>>> import pdb
>>> def f(x):
...     print(1 / x)
>>> pdb.run("f(2)")
> <string>(1)<module>()
(Pdb) continue
0.5
>>>

```

The typical usage to inspect a crashed program is:
Copy```
>>> import pdb
>>> def f(x):
...     print(1 / x)
...
>>> f(0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in f
ZeroDivisionError: division by zero
>>> pdb.pm()
> <stdin>(2)f()
(Pdb) p x
0
(Pdb)

```

Changed in version 3.13: The implementation of [**PEP 667**](https://peps.python.org/pep-0667/) means that name assignments made via `pdb` will immediately affect the active scope, even when running inside an [optimized scope](https://docs.python.org/3/glossary.html#term-optimized-scope).
The module defines the following functions; each enters the debugger in a slightly different way:

pdb.run(_statement_ , _globals =None_, _locals =None_)[¶](https://docs.python.org/3/library/pdb.html#pdb.run "Link to this definition")

Execute the _statement_ (given as a string or a code object) under debugger control. The debugger prompt appears before any code is executed; you can set breakpoints and type [`continue`](https://docs.python.org/3/library/pdb.html#pdbcommand-continue), or you can step through the statement using [`step`](https://docs.python.org/3/library/pdb.html#pdbcommand-step) or [`next`](https://docs.python.org/3/library/pdb.html#pdbcommand-next) (all these commands are explained below). The optional _globals_ and _locals_ arguments specify the environment in which the code is executed; by default the dictionary of the module [`__main__`](https://docs.python.org/3/library/__main__.html#module-__main__ "__main__: The environment where top-level code is run. Covers command-line interfaces, import-time behavior, and ``__name__ == '__main__'``.") is used. (See the explanation of the built-in [`exec()`](https://docs.python.org/3/library/functions.html#exec "exec") or [`eval()`](https://docs.python.org/3/library/functions.html#eval "eval") functions.)

pdb.runeval(_expression_ , _globals =None_, _locals =None_)[¶](https://docs.python.org/3/library/pdb.html#pdb.runeval "Link to this definition")

Evaluate the _expression_ (given as a string or a code object) under debugger control. When `runeval()` returns, it returns the value of the _expression_. Otherwise this function is similar to [`run()`](https://docs.python.org/3/library/pdb.html#pdb.run "pdb.run").

pdb.runcall(_function_ , _* args_, _** kwds_)[¶](https://docs.python.org/3/library/pdb.html#pdb.runcall "Link to this definition")

Call the _function_ (a function or method object, not a string) with the given arguments. When `runcall()` returns, it returns whatever the function call returned. The debugger prompt appears as soon as the function is entered.

pdb.set_trace(_*_ , _header =None_, _commands =None_)[¶](https://docs.python.org/3/library/pdb.html#pdb.set_trace "Link to this definition")

Enter the debugger at the calling stack frame. This is useful to hard-code a breakpoint at a given point in a program, even if the code is not otherwise being debugged (e.g. when an assertion fails). If given, _header_ is printed to the console just before debugging begins. The _commands_ argument, if given, is a list of commands to execute when the debugger starts.
Changed in version 3.7: The keyword-only argument _header_.
Changed in version 3.13: `set_trace()` will enter the debugger immediately, rather than on the next line of code to be executed.
Added in version 3.14: The _commands_ argument.

_awaitable _pdb.set_trace_async(_*_ , _header =None_, _commands =None_)[¶](https://docs.python.org/3/library/pdb.html#pdb.set_trace_async "Link to this definition")

async version of [`set_trace()`](https://docs.python.org/3/library/pdb.html#pdb.set_trace "pdb.set_trace"). This function should be used inside an async function with [`await`](https://docs.python.org/3/reference/expressions.html#await).
Copy```
async def f():
    await pdb.set_trace_async()

```

[`await`](https://docs.python.org/3/reference/expressions.html#await) statements are supported if the debugger is invoked by this function.
Added in version 3.14.

pdb.post_mortem(_t =None_)[¶](https://docs.python.org/3/library/pdb.html#pdb.post_mortem "Link to this definition")

Enter post-mortem debugging of the given exception or [traceback object](https://docs.python.org/3/reference/datamodel.html#traceback-objects). If no value is given, it uses the exception that is currently being handled, or raises `ValueError` if there isn’t one.
Changed in version 3.13: Support for exception objects was added.

pdb.pm()[¶](https://docs.python.org/3/library/pdb.html#pdb.pm "Link to this definition")

Enter post-mortem debugging of the exception found in [`sys.last_exc`](https://docs.python.org/3/library/sys.html#sys.last_exc "sys.last_exc").

pdb.set_default_backend(_backend_)[¶](https://docs.python.org/3/library/pdb.html#pdb.set_default_backend "Link to this definition")

There are two supported backends for pdb: `'settrace'` and `'monitoring'`. See [`bdb.Bdb`](https://docs.python.org/3/library/bdb.html#bdb.Bdb "bdb.Bdb") for details. The user can set the default backend to use if none is specified when instantiating [`Pdb`](https://docs.python.org/3/library/pdb.html#pdb.Pdb "pdb.Pdb"). If no backend is specified, the default is `'settrace'`.
Note
[`breakpoint()`](https://docs.python.org/3/library/functions.html#breakpoint "breakpoint") and [`set_trace()`](https://docs.python.org/3/library/pdb.html#pdb.set_trace "pdb.set_trace") will not be affected by this function. They always use `'monitoring'` backend.
Added in version 3.14.

pdb.get_default_backend()[¶](https://docs.python.org/3/library/pdb.html#pdb.get_default_backend "Link to this definition")

Returns the default backend for pdb.
Added in version 3.14.
The `run*` functions and [`set_trace()`](https://docs.python.org/3/library/pdb.html#pdb.set_trace "pdb.set_trace") are aliases for instantiating the [`Pdb`](https://docs.python.org/3/library/pdb.html#pdb.Pdb "pdb.Pdb") class and calling the method of the same name. If you want to access further features, you have to do this yourself:

_class_ pdb.Pdb(_completekey ='tab'_, _stdin =None_, _stdout =None_, _skip =None_, _nosigint =False_, _readrc =True_, _mode =None_, _backend =None_, _colorize =False_)[¶](https://docs.python.org/3/library/pdb.html#pdb.Pdb "Link to this definition")

`Pdb` is the debugger class.
The _completekey_ , _stdin_ and _stdout_ arguments are passed to the underlying [`cmd.Cmd`](https://docs.python.org/3/library/cmd.html#cmd.Cmd "cmd.Cmd") class; see the description there.
The _skip_ argument, if given, must be an iterable of glob-style module name patterns. The debugger will not step into frames that originate in a module that matches one of these patterns. [[1]](https://docs.python.org/3/library/pdb.html#id3)
By default, Pdb sets a handler for the SIGINT signal (which is sent when the user presses `Ctrl`-`C` on the console) when you give a [`continue`](https://docs.python.org/3/library/pdb.html#pdbcommand-continue) command. This allows you to break into the debugger again by pressing `Ctrl`-`C`. If you want Pdb not to touch the SIGINT handler, set _nosigint_ to true.
The _readrc_ argument defaults to true and controls whether Pdb will load .pdbrc files from the filesystem.
The _mode_ argument specifies how the debugger was invoked. It impacts the workings of some debugger commands. Valid values are `'inline'` (used by the breakpoint() builtin), `'cli'` (used by the command line invocation) or `None` (for backwards compatible behaviour, as before the _mode_ argument was added).
The _backend_ argument specifies the backend to use for the debugger. If `None` is passed, the default backend will be used. See [`set_default_backend()`](https://docs.python.org/3/library/pdb.html#pdb.set_default_backend "pdb.set_default_backend"). Otherwise the supported backends are `'settrace'` and `'monitoring'`.
The _colorize_ argument, if set to `True`, will enable colorized output in the debugger, if color is supported. This will highlight source code displayed in pdb.
Example call to enable tracing with _skip_ :
Copy```
import pdb; pdb.Pdb(skip=['django.*']).set_trace()

```

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `pdb.Pdb` with no arguments.
Changed in version 3.1: Added the _skip_ parameter.
Changed in version 3.2: Added the _nosigint_ parameter. Previously, a SIGINT handler was never set by Pdb.
Changed in version 3.6: The _readrc_ argument.
Added in version 3.14: Added the _mode_ argument.
Added in version 3.14: Added the _backend_ argument.
Added in version 3.14: Added the _colorize_ argument.
Changed in version 3.14: Inline breakpoints like [`breakpoint()`](https://docs.python.org/3/library/functions.html#breakpoint "breakpoint") or [`pdb.set_trace()`](https://docs.python.org/3/library/pdb.html#pdb.set_trace "pdb.set_trace") will always stop the program at calling frame, ignoring the _skip_ pattern (if any).

run(_statement_ , _globals =None_, _locals =None_)[¶](https://docs.python.org/3/library/pdb.html#pdb.Pdb.run "Link to this definition")


runeval(_expression_ , _globals =None_, _locals =None_)[¶](https://docs.python.org/3/library/pdb.html#pdb.Pdb.runeval "Link to this definition")


runcall(_function_ , _* args_, _** kwds_)[¶](https://docs.python.org/3/library/pdb.html#pdb.Pdb.runcall "Link to this definition")


set_trace()[¶](https://docs.python.org/3/library/pdb.html#pdb.Pdb.set_trace "Link to this definition")

See the documentation for the functions explained above.
## Debugger commands[¶](https://docs.python.org/3/library/pdb.html#debugger-commands "Link to this heading")
The commands recognized by the debugger are listed below. Most commands can be abbreviated to one or two letters as indicated; e.g. `h(elp)` means that either `h` or `help` can be used to enter the help command (but not `he` or `hel`, nor `H` or `Help` or `HELP`). Arguments to commands must be separated by whitespace (spaces or tabs). Optional arguments are enclosed in square brackets (`[]`) in the command syntax; the square brackets must not be typed. Alternatives in the command syntax are separated by a vertical bar (`|`).
Entering a blank line repeats the last command entered. Exception: if the last command was a [`list`](https://docs.python.org/3/library/pdb.html#pdbcommand-list) command, the next 11 lines are listed.
Commands that the debugger doesn’t recognize are assumed to be Python statements and are executed in the context of the program being debugged. Python statements can also be prefixed with an exclamation point (`!`). This is a powerful way to inspect the program being debugged; it is even possible to change a variable or call a function. When an exception occurs in such a statement, the exception name is printed but the debugger’s state is not changed.
Changed in version 3.13: Expressions/Statements whose prefix is a pdb command are now correctly identified and executed.
The debugger supports [aliases](https://docs.python.org/3/library/pdb.html#debugger-aliases). Aliases can have parameters which allows one a certain level of adaptability to the context under examination.
Multiple commands may be entered on a single line, separated by `;;`. (A single `;` is not used as it is the separator for multiple commands in a line that is passed to the Python parser.) No intelligence is applied to separating the commands; the input is split at the first `;;` pair, even if it is in the middle of a quoted string. A workaround for strings with double semicolons is to use implicit string concatenation `';'';'` or `";"";"`.
To set a temporary global variable, use a _convenience variable_. A _convenience variable_ is a variable whose name starts with `$`. For example, `$foo = 1` sets a global variable `$foo` which you can use in the debugger session. The _convenience variables_ are cleared when the program resumes execution so it’s less likely to interfere with your program compared to using normal variables like `foo = 1`.
There are four preset _convenience variables_ :
  * `$_frame`: the current frame you are debugging
  * `$_retval`: the return value if the frame is returning
  * `$_exception`: the exception if the frame is raising an exception
  * `$_asynctask`: the asyncio task if pdb stops in an async function


Added in version 3.12: Added the _convenience variable_ feature.
Added in version 3.14: Added the `$_asynctask` convenience variable.
If a file `.pdbrc` exists in the user’s home directory or in the current directory, it is read with `'utf-8'` encoding and executed as if it had been typed at the debugger prompt, with the exception that empty lines and lines starting with `#` are ignored. This is particularly useful for aliases. If both files exist, the one in the home directory is read first and aliases defined there can be overridden by the local file.
Changed in version 3.2: `.pdbrc` can now contain commands that continue debugging, such as [`continue`](https://docs.python.org/3/library/pdb.html#pdbcommand-continue) or [`next`](https://docs.python.org/3/library/pdb.html#pdbcommand-next). Previously, these commands had no effect.
Changed in version 3.11: `.pdbrc` is now read with `'utf-8'` encoding. Previously, it was read with the system locale encoding.

h(elp) [command][¶](https://docs.python.org/3/library/pdb.html#pdbcommand-help "Link to this definition")

Without argument, print the list of available commands. With a _command_ as argument, print help about that command. `help pdb` displays the full documentation (the docstring of the `pdb` module). Since the _command_ argument must be an identifier, `help exec` must be entered to get help on the `!` command.

w(here) [count][¶](https://docs.python.org/3/library/pdb.html#pdbcommand-where "Link to this definition")

Print a stack trace, with the most recent frame at the bottom. if _count_ is 0, print the current frame entry. If _count_ is negative, print the least recent - _count_ frames. If _count_ is positive, print the most recent _count_ frames. An arrow (`>`) indicates the current frame, which determines the context of most commands.
Changed in version 3.14: _count_ argument is added.

d(own) [count][¶](https://docs.python.org/3/library/pdb.html#pdbcommand-down "Link to this definition")

Move the current frame _count_ (default one) levels down in the stack trace (to a newer frame).

u(p) [count][¶](https://docs.python.org/3/library/pdb.html#pdbcommand-up "Link to this definition")

Move the current frame _count_ (default one) levels up in the stack trace (to an older frame).

b(reak) [([filename:]lineno | function) [, condition]][¶](https://docs.python.org/3/library/pdb.html#pdbcommand-break "Link to this definition")

With a _lineno_ argument, set a break at line _lineno_ in the current file. The line number may be prefixed with a _filename_ and a colon, to specify a breakpoint in another file (possibly one that hasn’t been loaded yet). The file is searched on [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path"). Acceptable forms of _filename_ are `/abspath/to/file.py`, `relpath/file.py`, `module` and `package.module`.
With a _function_ argument, set a break at the first executable statement within that function. _function_ can be any expression that evaluates to a function in the current namespace.
If a second argument is present, it is an expression which must evaluate to true before the breakpoint is honored.
Without argument, list all breaks, including for each breakpoint, the number of times that breakpoint has been hit, the current ignore count, and the associated condition if any.
Each breakpoint is assigned a number to which all the other breakpoint commands refer.

tbreak [([filename:]lineno | function) [, condition]][¶](https://docs.python.org/3/library/pdb.html#pdbcommand-tbreak "Link to this definition")

Temporary breakpoint, which is removed automatically when it is first hit. The arguments are the same as for [`break`](https://docs.python.org/3/library/pdb.html#pdbcommand-break).

cl(ear) [filename:lineno | bpnumber ...][¶](https://docs.python.org/3/library/pdb.html#pdbcommand-clear "Link to this definition")

With a _filename:lineno_ argument, clear all the breakpoints at this line. With a space separated list of breakpoint numbers, clear those breakpoints. Without argument, clear all breaks (but first ask confirmation).

disable bpnumber [bpnumber ...][¶](https://docs.python.org/3/library/pdb.html#pdbcommand-disable "Link to this definition")

Disable the breakpoints given as a space separated list of breakpoint numbers. Disabling a breakpoint means it cannot cause the program to stop execution, but unlike clearing a breakpoint, it remains in the list of breakpoints and can be (re-)enabled.

enable bpnumber [bpnumber ...][¶](https://docs.python.org/3/library/pdb.html#pdbcommand-enable "Link to this definition")

Enable the breakpoints specified.

ignore bpnumber [count][¶](https://docs.python.org/3/library/pdb.html#pdbcommand-ignore "Link to this definition")

Set the ignore count for the given breakpoint number. If _count_ is omitted, the ignore count is set to 0. A breakpoint becomes active when the ignore count is zero. When non-zero, the _count_ is decremented each time the breakpoint is reached and the breakpoint is not disabled and any associated condition evaluates to true.

condition bpnumber [condition][¶](https://docs.python.org/3/library/pdb.html#pdbcommand-condition "Link to this definition")

Set a new _condition_ for the breakpoint, an expression which must evaluate to true before the breakpoint is honored. If _condition_ is absent, any existing condition is removed; i.e., the breakpoint is made unconditional.

commands [bpnumber][¶](https://docs.python.org/3/library/pdb.html#pdbcommand-commands "Link to this definition")

Specify a list of commands for breakpoint number _bpnumber_. The commands themselves appear on the following lines. Type a line containing just `end` to terminate the commands. An example:
Copy```
(Pdb) commands 1
(com) p some_variable
(com) end
(Pdb)

```

To remove all commands from a breakpoint, type `commands` and follow it immediately with `end`; that is, give no commands.
With no _bpnumber_ argument, `commands` refers to the last breakpoint set.
You can use breakpoint commands to start your program up again. Simply use the [`continue`](https://docs.python.org/3/library/pdb.html#pdbcommand-continue) command, or [`step`](https://docs.python.org/3/library/pdb.html#pdbcommand-step), or any other command that resumes execution.
Specifying any command resuming execution (currently [`continue`](https://docs.python.org/3/library/pdb.html#pdbcommand-continue), [`step`](https://docs.python.org/3/library/pdb.html#pdbcommand-step), [`next`](https://docs.python.org/3/library/pdb.html#pdbcommand-next), [`return`](https://docs.python.org/3/library/pdb.html#pdbcommand-return), [`until`](https://docs.python.org/3/library/pdb.html#pdbcommand-until), [`jump`](https://docs.python.org/3/library/pdb.html#pdbcommand-jump), [`quit`](https://docs.python.org/3/library/pdb.html#pdbcommand-quit) and their abbreviations) terminates the command list (as if that command was immediately followed by end). This is because any time you resume execution (even with a simple next or step), you may encounter another breakpoint—which could have its own command list, leading to ambiguities about which list to execute.
If the list of commands contains the `silent` command, or a command that resumes execution, then the breakpoint message containing information about the frame is not displayed.
Changed in version 3.14: Frame information will not be displayed if a command that resumes execution is present in the command list.

s(tep)[¶](https://docs.python.org/3/library/pdb.html#pdbcommand-step "Link to this definition")

Execute the current line, stop at the first possible occasion (either in a function that is called or on the next line in the current function).

n(ext)[¶](https://docs.python.org/3/library/pdb.html#pdbcommand-next "Link to this definition")

Continue execution until the next line in the current function is reached or it returns. (The difference between [`next`](https://docs.python.org/3/library/pdb.html#pdbcommand-next) and [`step`](https://docs.python.org/3/library/pdb.html#pdbcommand-step) is that `step` stops inside a called function, while `next` executes called functions at (nearly) full speed, only stopping at the next line in the current function.)

unt(il) [lineno][¶](https://docs.python.org/3/library/pdb.html#pdbcommand-until "Link to this definition")

Without argument, continue execution until the line with a number greater than the current one is reached.
With _lineno_ , continue execution until a line with a number greater or equal to _lineno_ is reached. In both cases, also stop when the current frame returns.
Changed in version 3.2: Allow giving an explicit line number.

r(eturn)[¶](https://docs.python.org/3/library/pdb.html#pdbcommand-return "Link to this definition")

Continue execution until the current function returns.

c(ont(inue))[¶](https://docs.python.org/3/library/pdb.html#pdbcommand-continue "Link to this definition")

Continue execution, only stop when a breakpoint is encountered.

j(ump) lineno[¶](https://docs.python.org/3/library/pdb.html#pdbcommand-jump "Link to this definition")

Set the next line that will be executed. Only available in the bottom-most frame. This lets you jump back and execute code again, or jump forward to skip code that you don’t want to run.
It should be noted that not all jumps are allowed – for instance it is not possible to jump into the middle of a [`for`](https://docs.python.org/3/reference/compound_stmts.html#for) loop or out of a [`finally`](https://docs.python.org/3/reference/compound_stmts.html#finally) clause.

l(ist) [first[, last]][¶](https://docs.python.org/3/library/pdb.html#pdbcommand-list "Link to this definition")

List source code for the current file. Without arguments, list 11 lines around the current line or continue the previous listing. With `.` as argument, list 11 lines around the current line. With one argument, list 11 lines around at that line. With two arguments, list the given range; if the second argument is less than the first, it is interpreted as a count.
The current line in the current frame is indicated by `->`. If an exception is being debugged, the line where the exception was originally raised or propagated is indicated by `>>`, if it differs from the current line.
Changed in version 3.2: Added the `>>` marker.

ll | longlist[¶](https://docs.python.org/3/library/pdb.html#pdbcommand-ll "Link to this definition")

List all source code for the current function or frame. Interesting lines are marked as for [`list`](https://docs.python.org/3/library/pdb.html#pdbcommand-list).
Added in version 3.2.

a(rgs)[¶](https://docs.python.org/3/library/pdb.html#pdbcommand-args "Link to this definition")

Print the arguments of the current function and their current values.

p expression[¶](https://docs.python.org/3/library/pdb.html#pdbcommand-p "Link to this definition")

Evaluate _expression_ in the current context and print its value.
Note
`print()` can also be used, but is not a debugger command — this executes the Python [`print()`](https://docs.python.org/3/library/functions.html#print "print") function.

pp expression[¶](https://docs.python.org/3/library/pdb.html#pdbcommand-pp "Link to this definition")

Like the [`p`](https://docs.python.org/3/library/pdb.html#pdbcommand-p) command, except the value of _expression_ is pretty-printed using the [`pprint`](https://docs.python.org/3/library/pprint.html#module-pprint "pprint: Data pretty printer.") module.

whatis expression[¶](https://docs.python.org/3/library/pdb.html#pdbcommand-whatis "Link to this definition")

Print the type of _expression_.

source expression[¶](https://docs.python.org/3/library/pdb.html#pdbcommand-source "Link to this definition")

Try to get source code of _expression_ and display it.
Added in version 3.2.

display [expression][¶](https://docs.python.org/3/library/pdb.html#pdbcommand-display "Link to this definition")

Display the value of _expression_ if it changed, each time execution stops in the current frame.
Without _expression_ , list all display expressions for the current frame.
Note
Display evaluates _expression_ and compares to the result of the previous evaluation of _expression_ , so when the result is mutable, display may not be able to pick up the changes.
Example:
Copy```
lst = []
breakpoint()
pass
lst.append(1)
print(lst)

```

Display won’t realize `lst` has been changed because the result of evaluation is modified in place by `lst.append(1)` before being compared:
Copy```
> example.py(3)<module>()
-> pass
(Pdb) display lst
display lst: []
(Pdb) n
> example.py(4)<module>()
-> lst.append(1)
(Pdb) n
> example.py(5)<module>()
-> print(lst)
(Pdb)

```

You can do some tricks with copy mechanism to make it work:
Copy```
> example.py(3)<module>()
-> pass
(Pdb) display lst[:]
display lst[:]: []
(Pdb) n
> example.py(4)<module>()
-> lst.append(1)
(Pdb) n
> example.py(5)<module>()
-> print(lst)
display lst[:]: [1]  [old: []]
(Pdb)

```

Added in version 3.2.

undisplay [expression][¶](https://docs.python.org/3/library/pdb.html#pdbcommand-undisplay "Link to this definition")

Do not display _expression_ anymore in the current frame. Without _expression_ , clear all display expressions for the current frame.
Added in version 3.2.

interact[¶](https://docs.python.org/3/library/pdb.html#pdbcommand-interact "Link to this definition")

Start an interactive interpreter (using the [`code`](https://docs.python.org/3/library/code.html#module-code "code: Facilities to implement read-eval-print loops.") module) in a new global namespace initialised from the local and global namespaces for the current scope. Use `exit()` or `quit()` to exit the interpreter and return to the debugger.
Note
As `interact` creates a new dedicated namespace for code execution, assignments to variables will not affect the original namespaces. However, modifications to any referenced mutable objects will be reflected in the original namespaces as usual.
Added in version 3.2.
Changed in version 3.13: `exit()` and `quit()` can be used to exit the [`interact`](https://docs.python.org/3/library/pdb.html#pdbcommand-interact) command.
Changed in version 3.13: [`interact`](https://docs.python.org/3/library/pdb.html#pdbcommand-interact) directs its output to the debugger’s output channel rather than [`sys.stderr`](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr").

alias [name [command]][¶](https://docs.python.org/3/library/pdb.html#pdbcommand-alias "Link to this definition")

Create an alias called _name_ that executes _command_. The _command_ must _not_ be enclosed in quotes. Replaceable parameters can be indicated by `%1`, `%2`, … and `%9`, while `%*` is replaced by all the parameters. If _command_ is omitted, the current alias for _name_ is shown. If no arguments are given, all aliases are listed.
Aliases may be nested and can contain anything that can be legally typed at the pdb prompt. Note that internal pdb commands _can_ be overridden by aliases. Such a command is then hidden until the alias is removed. Aliasing is recursively applied to the first word of the command line; all other words in the line are left alone.
As an example, here are two useful aliases (especially when placed in the `.pdbrc` file):
Copy```
# Print instance variables (usage "pi classInst")
alias pi for k in %1.__dict__.keys(): print(f"%1.{k} = {%1.__dict__[k]}")
# Print instance variables in self
alias ps pi self

```


unalias name[¶](https://docs.python.org/3/library/pdb.html#pdbcommand-unalias "Link to this definition")

Delete the specified alias _name_.

! statement[¶](https://docs.python.org/3/library/pdb.html#pdbcommand-0 "Link to this definition")

Execute the (one-line) _statement_ in the context of the current stack frame. The exclamation point can be omitted unless the first word of the statement resembles a debugger command, e.g.:
```
(Pdb) ! n=42
(Pdb)

```

To set a global variable, you can prefix the assignment command with a [`global`](https://docs.python.org/3/reference/simple_stmts.html#global) statement on the same line, e.g.:
```
(Pdb) global list_options; list_options = ['-l']
(Pdb)

```


run [args ...][¶](https://docs.python.org/3/library/pdb.html#pdbcommand-run "Link to this definition")


restart [args ...][¶](https://docs.python.org/3/library/pdb.html#pdbcommand-restart "Link to this definition")

Restart the debugged Python program. If _args_ is supplied, it is split with [`shlex`](https://docs.python.org/3/library/shlex.html#module-shlex "shlex: Simple lexical analysis for Unix shell-like languages.") and the result is used as the new [`sys.argv`](https://docs.python.org/3/library/sys.html#sys.argv "sys.argv"). History, breakpoints, actions and debugger options are preserved. [`restart`](https://docs.python.org/3/library/pdb.html#pdbcommand-restart) is an alias for [`run`](https://docs.python.org/3/library/pdb.html#pdbcommand-run).
Changed in version 3.14: [`run`](https://docs.python.org/3/library/pdb.html#pdbcommand-run) and [`restart`](https://docs.python.org/3/library/pdb.html#pdbcommand-restart) commands are disabled when the debugger is invoked in `'inline'` mode.

q(uit)[¶](https://docs.python.org/3/library/pdb.html#pdbcommand-quit "Link to this definition")

Quit from the debugger. The program being executed is aborted. An end-of-file input is equivalent to [`quit`](https://docs.python.org/3/library/pdb.html#pdbcommand-quit).
A confirmation prompt will be shown if the debugger is invoked in `'inline'` mode. Either `y`, `Y`, `<Enter>` or `EOF` will confirm the quit.
Changed in version 3.14: A confirmation prompt will be shown if the debugger is invoked in `'inline'` mode. After the confirmation, the debugger will call [`sys.exit()`](https://docs.python.org/3/library/sys.html#sys.exit "sys.exit") immediately, instead of raising [`bdb.BdbQuit`](https://docs.python.org/3/library/bdb.html#bdb.BdbQuit "bdb.BdbQuit") in the next trace event.

debug code[¶](https://docs.python.org/3/library/pdb.html#pdbcommand-debug "Link to this definition")

Enter a recursive debugger that steps through _code_ (which is an arbitrary expression or statement to be executed in the current environment).

retval[¶](https://docs.python.org/3/library/pdb.html#pdbcommand-retval "Link to this definition")

Print the return value for the last return of the current function.

exceptions [excnumber][¶](https://docs.python.org/3/library/pdb.html#pdbcommand-exceptions "Link to this definition")

List or jump between chained exceptions.
When using `pdb.pm()` or `Pdb.post_mortem(...)` with a chained exception instead of a traceback, it allows the user to move between the chained exceptions using `exceptions` command to list exceptions, and `exceptions <number>` to switch to that exception.
Example:
Copy```
def out():
    try:
        middle()
    except Exception as e:
        raise ValueError("reraise middle() error") from e

def middle():
    try:
        return inner(0)
    except Exception as e:
        raise ValueError("Middle fail")

def inner(x):
    1 / x

 out()

```

calling `pdb.pm()` will allow to move between exceptions:
Copy```
> example.py(5)out()
-> raise ValueError("reraise middle() error") from e

(Pdb) exceptions
  0 ZeroDivisionError('division by zero')
  1 ValueError('Middle fail')
> 2 ValueError('reraise middle() error')

(Pdb) exceptions 0
> example.py(16)inner()
-> 1 / x

(Pdb) up
> example.py(10)middle()
-> return inner(0)

```

Added in version 3.13.
Footnotes
[[1](https://docs.python.org/3/library/pdb.html#id1)]
Whether a frame is considered to originate in a certain module is determined by the `__name__` in the frame globals.
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`pdb` — The Python Debugger](https://docs.python.org/3/library/pdb.html)
    * [Command-line interface](https://docs.python.org/3/library/pdb.html#command-line-interface)
    * [Debugger commands](https://docs.python.org/3/library/pdb.html#debugger-commands)


#### Previous topic
[`faulthandler` — Dump the Python traceback](https://docs.python.org/3/library/faulthandler.html "previous chapter")
#### Next topic
[The Python Profilers](https://docs.python.org/3/library/profile.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=pdb+%E2%80%94+The+Python+Debugger&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fpdb.html&pagesource=library%2Fpdb.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/profile.html "The Python Profilers") |
  * [previous](https://docs.python.org/3/library/faulthandler.html "faulthandler — Dump the Python traceback") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Debugging and Profiling](https://docs.python.org/3/library/debug.html) »
  * [`pdb` — The Python Debugger](https://docs.python.org/3/library/pdb.html)
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
