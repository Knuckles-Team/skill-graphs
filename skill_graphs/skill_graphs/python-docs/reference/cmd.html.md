[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`cmd` — Support for line-oriented command interpreters](https://docs.python.org/3/library/cmd.html)
    * [Cmd Objects](https://docs.python.org/3/library/cmd.html#cmd-objects)
    * [Cmd Example](https://docs.python.org/3/library/cmd.html#cmd-example)


#### Previous topic
[`curses.panel` — A panel stack extension for curses](https://docs.python.org/3/library/curses.panel.html "previous chapter")
#### Next topic
[Concurrent Execution](https://docs.python.org/3/library/concurrency.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=cmd+%E2%80%94+Support+for+line-oriented+command+interpreters&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fcmd.html&pagesource=library%2Fcmd.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/concurrency.html "Concurrent Execution") |
  * [previous](https://docs.python.org/3/library/curses.panel.html "curses.panel — A panel stack extension for curses") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Command-line interface libraries](https://docs.python.org/3/library/cmdlinelibs.html) »
  * [`cmd` — Support for line-oriented command interpreters](https://docs.python.org/3/library/cmd.html)
  * |
  * Theme  Auto Light Dark |


#  `cmd` — Support for line-oriented command interpreters[¶](https://docs.python.org/3/library/cmd.html#module-cmd "Link to this heading")
**Source code:**
* * *
The [`Cmd`](https://docs.python.org/3/library/cmd.html#cmd.Cmd "cmd.Cmd") class provides a simple framework for writing line-oriented command interpreters. These are often useful for test harnesses, administrative tools, and prototypes that will later be wrapped in a more sophisticated interface.

_class_ cmd.Cmd(_completekey ='tab'_, _stdin =None_, _stdout =None_)[¶](https://docs.python.org/3/library/cmd.html#cmd.Cmd "Link to this definition")

A `Cmd` instance or subclass instance is a line-oriented interpreter framework. There is no good reason to instantiate `Cmd` itself; rather, it’s useful as a superclass of an interpreter class you define yourself in order to inherit `Cmd`’s methods and encapsulate action methods.
The optional argument _completekey_ is the [`readline`](https://docs.python.org/3/library/readline.html#module-readline "readline: GNU readline support for Python.") name of a completion key; it defaults to `Tab`. If _completekey_ is not [`None`](https://docs.python.org/3/library/constants.html#None "None") and `readline` is available, command completion is done automatically.
The default, `'tab'`, is treated specially, so that it refers to the `Tab` key on every [`readline.backend`](https://docs.python.org/3/library/readline.html#readline.backend "readline.backend"). Specifically, if `readline.backend` is `editline`, `Cmd` will use `'^I'` instead of `'tab'`. Note that other values are not treated this way, and might only work with a specific backend.
The optional arguments _stdin_ and _stdout_ specify the input and output file objects that the Cmd instance or subclass instance will use for input and output. If not specified, they will default to [`sys.stdin`](https://docs.python.org/3/library/sys.html#sys.stdin "sys.stdin") and [`sys.stdout`](https://docs.python.org/3/library/sys.html#sys.stdout "sys.stdout").
If you want a given _stdin_ to be used, make sure to set the instance’s [`use_rawinput`](https://docs.python.org/3/library/cmd.html#cmd.Cmd.use_rawinput "cmd.Cmd.use_rawinput") attribute to `False`, otherwise _stdin_ will be ignored.
Changed in version 3.13: `completekey='tab'` is replaced by `'^I'` for `editline`.
## Cmd Objects[¶](https://docs.python.org/3/library/cmd.html#cmd-objects "Link to this heading")
A [`Cmd`](https://docs.python.org/3/library/cmd.html#cmd.Cmd "cmd.Cmd") instance has the following methods:

Cmd.cmdloop(_intro =None_)[¶](https://docs.python.org/3/library/cmd.html#cmd.Cmd.cmdloop "Link to this definition")

Repeatedly issue a prompt, accept input, parse an initial prefix off the received input, and dispatch to action methods, passing them the remainder of the line as argument.
The optional argument is a banner or intro string to be issued before the first prompt (this overrides the [`intro`](https://docs.python.org/3/library/cmd.html#cmd.Cmd.intro "cmd.Cmd.intro") class attribute).
If the [`readline`](https://docs.python.org/3/library/readline.html#module-readline "readline: GNU readline support for Python.") module is loaded, input will automatically inherit **bash** -like history-list editing (e.g. `Control`-`P` scrolls back to the last command, `Control`-`N` forward to the next one, `Control`-`F` moves the cursor to the right non-destructively, `Control`-`B` moves the cursor to the left non-destructively, etc.).
An end-of-file on input is passed back as the string `'EOF'`.
An interpreter instance will recognize a command name `foo` if and only if it has a method `do_foo()`. As a special case, a line beginning with the character `'?'` is dispatched to the method [`do_help()`](https://docs.python.org/3/library/cmd.html#cmd.Cmd.do_help "cmd.Cmd.do_help"). As another special case, a line beginning with the character `'!'` is dispatched to the method `do_shell()` (if such a method is defined).
This method will return when the [`postcmd()`](https://docs.python.org/3/library/cmd.html#cmd.Cmd.postcmd "cmd.Cmd.postcmd") method returns a true value. The _stop_ argument to `postcmd()` is the return value from the command’s corresponding `do_*()` method.
If completion is enabled, completing commands will be done automatically, and completing of commands args is done by calling `complete_foo()` with arguments _text_ , _line_ , _begidx_ , and _endidx_. _text_ is the string prefix we are attempting to match: all returned matches must begin with it. _line_ is the current input line with leading whitespace removed, _begidx_ and _endidx_ are the beginning and ending indexes of the prefix text, which could be used to provide different completion depending upon which position the argument is in.

Cmd.do_help(_arg_)[¶](https://docs.python.org/3/library/cmd.html#cmd.Cmd.do_help "Link to this definition")

All subclasses of [`Cmd`](https://docs.python.org/3/library/cmd.html#cmd.Cmd "cmd.Cmd") inherit a predefined `do_help()`. This method, called with an argument `'bar'`, invokes the corresponding method `help_bar()`, and if that is not present, prints the docstring of `do_bar()`, if available. With no argument, `do_help()` lists all available help topics (that is, all commands with corresponding `help_*()` methods or commands that have docstrings), and also lists any undocumented commands.

Cmd.onecmd(_str_)[¶](https://docs.python.org/3/library/cmd.html#cmd.Cmd.onecmd "Link to this definition")

Interpret the argument as though it had been typed in response to the prompt. This may be overridden, but should not normally need to be; see the [`precmd()`](https://docs.python.org/3/library/cmd.html#cmd.Cmd.precmd "cmd.Cmd.precmd") and [`postcmd()`](https://docs.python.org/3/library/cmd.html#cmd.Cmd.postcmd "cmd.Cmd.postcmd") methods for useful execution hooks. The return value is a flag indicating whether interpretation of commands by the interpreter should stop. If there is a `do_*()` method for the command _str_ , the return value of that method is returned, otherwise the return value from the [`default()`](https://docs.python.org/3/library/cmd.html#cmd.Cmd.default "cmd.Cmd.default") method is returned.

Cmd.emptyline()[¶](https://docs.python.org/3/library/cmd.html#cmd.Cmd.emptyline "Link to this definition")

Method called when an empty line is entered in response to the prompt. If this method is not overridden, it repeats the last nonempty command entered.

Cmd.default(_line_)[¶](https://docs.python.org/3/library/cmd.html#cmd.Cmd.default "Link to this definition")

Method called on an input line when the command prefix is not recognized. If this method is not overridden, it prints an error message and returns.

Cmd.completedefault(_text_ , _line_ , _begidx_ , _endidx_)[¶](https://docs.python.org/3/library/cmd.html#cmd.Cmd.completedefault "Link to this definition")

Method called to complete an input line when no command-specific `complete_*()` method is available. By default, it returns an empty list.

Cmd.columnize(_list_ , _displaywidth =80_)[¶](https://docs.python.org/3/library/cmd.html#cmd.Cmd.columnize "Link to this definition")

Method called to display a list of strings as a compact set of columns. Each column is only as wide as necessary. Columns are separated by two spaces for readability.

Cmd.precmd(_line_)[¶](https://docs.python.org/3/library/cmd.html#cmd.Cmd.precmd "Link to this definition")

Hook method executed just before the command line _line_ is interpreted, but after the input prompt is generated and issued. This method is a stub in [`Cmd`](https://docs.python.org/3/library/cmd.html#cmd.Cmd "cmd.Cmd"); it exists to be overridden by subclasses. The return value is used as the command which will be executed by the [`onecmd()`](https://docs.python.org/3/library/cmd.html#cmd.Cmd.onecmd "cmd.Cmd.onecmd") method; the `precmd()` implementation may re-write the command or simply return _line_ unchanged.

Cmd.postcmd(_stop_ , _line_)[¶](https://docs.python.org/3/library/cmd.html#cmd.Cmd.postcmd "Link to this definition")

Hook method executed just after a command dispatch is finished. This method is a stub in [`Cmd`](https://docs.python.org/3/library/cmd.html#cmd.Cmd "cmd.Cmd"); it exists to be overridden by subclasses. _line_ is the command line which was executed, and _stop_ is a flag which indicates whether execution will be terminated after the call to `postcmd()`; this will be the return value of the [`onecmd()`](https://docs.python.org/3/library/cmd.html#cmd.Cmd.onecmd "cmd.Cmd.onecmd") method. The return value of this method will be used as the new value for the internal flag which corresponds to _stop_ ; returning false will cause interpretation to continue.

Cmd.preloop()[¶](https://docs.python.org/3/library/cmd.html#cmd.Cmd.preloop "Link to this definition")

Hook method executed once when [`cmdloop()`](https://docs.python.org/3/library/cmd.html#cmd.Cmd.cmdloop "cmd.Cmd.cmdloop") is called. This method is a stub in [`Cmd`](https://docs.python.org/3/library/cmd.html#cmd.Cmd "cmd.Cmd"); it exists to be overridden by subclasses.

Cmd.postloop()[¶](https://docs.python.org/3/library/cmd.html#cmd.Cmd.postloop "Link to this definition")

Hook method executed once when [`cmdloop()`](https://docs.python.org/3/library/cmd.html#cmd.Cmd.cmdloop "cmd.Cmd.cmdloop") is about to return. This method is a stub in [`Cmd`](https://docs.python.org/3/library/cmd.html#cmd.Cmd "cmd.Cmd"); it exists to be overridden by subclasses.
Instances of [`Cmd`](https://docs.python.org/3/library/cmd.html#cmd.Cmd "cmd.Cmd") subclasses have some public instance variables:

Cmd.prompt[¶](https://docs.python.org/3/library/cmd.html#cmd.Cmd.prompt "Link to this definition")

The prompt issued to solicit input.

Cmd.identchars[¶](https://docs.python.org/3/library/cmd.html#cmd.Cmd.identchars "Link to this definition")

The string of characters accepted for the command prefix.

Cmd.lastcmd[¶](https://docs.python.org/3/library/cmd.html#cmd.Cmd.lastcmd "Link to this definition")

The last nonempty command prefix seen.

Cmd.cmdqueue[¶](https://docs.python.org/3/library/cmd.html#cmd.Cmd.cmdqueue "Link to this definition")

A list of queued input lines. The cmdqueue list is checked in [`cmdloop()`](https://docs.python.org/3/library/cmd.html#cmd.Cmd.cmdloop "cmd.Cmd.cmdloop") when new input is needed; if it is nonempty, its elements will be processed in order, as if entered at the prompt.

Cmd.intro[¶](https://docs.python.org/3/library/cmd.html#cmd.Cmd.intro "Link to this definition")

A string to issue as an intro or banner. May be overridden by giving the [`cmdloop()`](https://docs.python.org/3/library/cmd.html#cmd.Cmd.cmdloop "cmd.Cmd.cmdloop") method an argument.

Cmd.doc_header[¶](https://docs.python.org/3/library/cmd.html#cmd.Cmd.doc_header "Link to this definition")

The header to issue if the help output has a section for documented commands.

Cmd.misc_header[¶](https://docs.python.org/3/library/cmd.html#cmd.Cmd.misc_header "Link to this definition")

The header to issue if the help output has a section for miscellaneous help topics (that is, there are `help_*()` methods without corresponding `do_*()` methods).

Cmd.undoc_header[¶](https://docs.python.org/3/library/cmd.html#cmd.Cmd.undoc_header "Link to this definition")

The header to issue if the help output has a section for undocumented commands (that is, there are `do_*()` methods without corresponding `help_*()` methods).

Cmd.ruler[¶](https://docs.python.org/3/library/cmd.html#cmd.Cmd.ruler "Link to this definition")

The character used to draw separator lines under the help-message headers. If empty, no ruler line is drawn. It defaults to `'='`.

Cmd.use_rawinput[¶](https://docs.python.org/3/library/cmd.html#cmd.Cmd.use_rawinput "Link to this definition")

A flag, defaulting to true. If true, [`cmdloop()`](https://docs.python.org/3/library/cmd.html#cmd.Cmd.cmdloop "cmd.Cmd.cmdloop") uses [`input()`](https://docs.python.org/3/library/functions.html#input "input") to display a prompt and read the next command; if false, [`sys.stdout.write()`](https://docs.python.org/3/library/sys.html#sys.stdout "sys.stdout") and [`sys.stdin.readline()`](https://docs.python.org/3/library/sys.html#sys.stdin "sys.stdin") are used. (This means that by importing [`readline`](https://docs.python.org/3/library/readline.html#module-readline "readline: GNU readline support for Python."), on systems that support it, the interpreter will automatically support **Emacs** -like line editing and command-history keystrokes.)
## Cmd Example[¶](https://docs.python.org/3/library/cmd.html#cmd-example "Link to this heading")
The `cmd` module is mainly useful for building custom shells that let a user work with a program interactively.
This section presents a simple example of how to build a shell around a few of the commands in the [`turtle`](https://docs.python.org/3/library/turtle.html#module-turtle "turtle: An educational framework for simple graphics applications") module.
Basic turtle commands such as [`forward()`](https://docs.python.org/3/library/turtle.html#turtle.forward "turtle.forward") are added to a [`Cmd`](https://docs.python.org/3/library/cmd.html#cmd.Cmd "cmd.Cmd") subclass with method named `do_forward()`. The argument is converted to a number and dispatched to the turtle module. The docstring is used in the help utility provided by the shell.
The example also includes a basic record and playback facility implemented with the [`precmd()`](https://docs.python.org/3/library/cmd.html#cmd.Cmd.precmd "cmd.Cmd.precmd") method which is responsible for converting the input to lowercase and writing the commands to a file. The `do_playback()` method reads the file and adds the recorded commands to the [`cmdqueue`](https://docs.python.org/3/library/cmd.html#cmd.Cmd.cmdqueue "cmd.Cmd.cmdqueue") for immediate playback:
Copy```
import cmd, sys
from turtle import *

class TurtleShell(cmd.Cmd):
    intro = 'Welcome to the turtle shell.   Type help or ? to list commands.\n'
    prompt = '(turtle) '
    file = None

    # ----- basic turtle commands -----
    def do_forward(self, arg):
        'Move the turtle forward by the specified distance:  FORWARD 10'
        forward(*parse(arg))
    def do_right(self, arg):
        'Turn turtle right by given number of degrees:  RIGHT 20'
        right(*parse(arg))
    def do_left(self, arg):
        'Turn turtle left by given number of degrees:  LEFT 90'
        left(*parse(arg))
    def do_goto(self, arg):
        'Move turtle to an absolute position with changing orientation.  GOTO 100 200'
        goto(*parse(arg))
    def do_home(self, arg):
        'Return turtle to the home position:  HOME'
        home()
    def do_circle(self, arg):
        'Draw circle with given radius an options extent and steps:  CIRCLE 50'
        circle(*parse(arg))
    def do_position(self, arg):
        'Print the current turtle position:  POSITION'
        print('Current position is %d %d\n' % position())
    def do_heading(self, arg):
        'Print the current turtle heading in degrees:  HEADING'
        print('Current heading is %d\n' % (heading(),))
    def do_color(self, arg):
        'Set the color:  COLOR BLUE'
        color(arg.lower())
    def do_undo(self, arg):
        'Undo (repeatedly) the last turtle action(s):  UNDO'
    def do_reset(self, arg):
        'Clear the screen and return turtle to center:  RESET'
        reset()
    def do_bye(self, arg):
        'Stop recording, close the turtle window, and exit:  BYE'
        print('Thank you for using Turtle')
        self.close()
        bye()
        return True

    # ----- record and playback -----
    def do_record(self, arg):
        'Save future commands to filename:  RECORD rose.cmd'
        self.file = open(arg, 'w')
    def do_playback(self, arg):
        'Playback commands from a file:  PLAYBACK rose.cmd'
        self.close()
        with open(arg) as f:
            self.cmdqueue.extend(f.read().splitlines())
    def precmd(self, line):
        line = line.lower()
        if self.file and 'playback' not in line:
            print(line, file=self.file)
        return line
    def close(self):
        if self.file:
            self.file.close()
            self.file = None

def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(int, arg.split()))

if __name__ == '__main__':
    TurtleShell().cmdloop()

```

Here is a sample session with the turtle shell showing the help functions, using blank lines to repeat commands, and the simple record and playback facility:
```
Welcome to the turtle shell.   Type help or ? to list commands.

(turtle) ?

Documented commands (type help <topic>):
========================================
bye     color    goto     home  playback  record  right
circle  forward  heading  left  position  reset   undo

(turtle) help forward
Move the turtle forward by the specified distance:  FORWARD 10
(turtle) record spiral.cmd
(turtle) position
Current position is 0 0

(turtle) heading
Current heading is 0

(turtle) reset
(turtle) circle 20
(turtle) right 30
(turtle) circle 40
(turtle) right 30
(turtle) circle 60
(turtle) right 30
(turtle) circle 80
(turtle) right 30
(turtle) circle 100
(turtle) right 30
(turtle) circle 120
(turtle) right 30
(turtle) circle 120
(turtle) heading
Current heading is 180

(turtle) forward 100
(turtle)
(turtle) right 90
(turtle) forward 100
(turtle)
(turtle) right 90
(turtle) forward 400
(turtle) right 90
(turtle) forward 500
(turtle) right 90
(turtle) forward 400
(turtle) right 90
(turtle) forward 300
(turtle) playback spiral.cmd
Current position is 0 0

Current heading is 0

Current heading is 180

(turtle) bye
Thank you for using Turtle

```

### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`cmd` — Support for line-oriented command interpreters](https://docs.python.org/3/library/cmd.html)
    * [Cmd Objects](https://docs.python.org/3/library/cmd.html#cmd-objects)
    * [Cmd Example](https://docs.python.org/3/library/cmd.html#cmd-example)


#### Previous topic
[`curses.panel` — A panel stack extension for curses](https://docs.python.org/3/library/curses.panel.html "previous chapter")
#### Next topic
[Concurrent Execution](https://docs.python.org/3/library/concurrency.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=cmd+%E2%80%94+Support+for+line-oriented+command+interpreters&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fcmd.html&pagesource=library%2Fcmd.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/concurrency.html "Concurrent Execution") |
  * [previous](https://docs.python.org/3/library/curses.panel.html "curses.panel — A panel stack extension for curses") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Command-line interface libraries](https://docs.python.org/3/library/cmdlinelibs.html) »
  * [`cmd` — Support for line-oriented command interpreters](https://docs.python.org/3/library/cmd.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
