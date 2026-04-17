[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`readline` — GNU readline interface](https://docs.python.org/3/library/readline.html)
    * [Init file](https://docs.python.org/3/library/readline.html#init-file)
    * [Line buffer](https://docs.python.org/3/library/readline.html#line-buffer)
    * [History file](https://docs.python.org/3/library/readline.html#history-file)
    * [History list](https://docs.python.org/3/library/readline.html#history-list)
    * [Startup hooks](https://docs.python.org/3/library/readline.html#startup-hooks)
    * [Completion](https://docs.python.org/3/library/readline.html#completion)
    * [Example](https://docs.python.org/3/library/readline.html#example)


#### Previous topic
[`stringprep` — Internet String Preparation](https://docs.python.org/3/library/stringprep.html "previous chapter")
#### Next topic
[`rlcompleter` — Completion function for GNU readline](https://docs.python.org/3/library/rlcompleter.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=readline+%E2%80%94+GNU+readline+interface&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Freadline.html&pagesource=library%2Freadline.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/rlcompleter.html "rlcompleter — Completion function for GNU readline") |
  * [previous](https://docs.python.org/3/library/stringprep.html "stringprep — Internet String Preparation") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Text Processing Services](https://docs.python.org/3/library/text.html) »
  * [`readline` — GNU readline interface](https://docs.python.org/3/library/readline.html)
  * |
  * Theme  Auto Light Dark |


#  `readline` — GNU readline interface[¶](https://docs.python.org/3/library/readline.html#module-readline "Link to this heading")
* * *
The `readline` module defines a number of functions to facilitate completion and reading/writing of history files from the Python interpreter. This module can be used directly, or via the [`rlcompleter`](https://docs.python.org/3/library/rlcompleter.html#module-rlcompleter "rlcompleter: Python identifier completion, suitable for the GNU readline library.") module, which supports completion of Python identifiers at the interactive prompt. Settings made using this module affect the behaviour of both the interpreter’s interactive prompt and the prompts offered by the built-in [`input()`](https://docs.python.org/3/library/functions.html#input "input") function.
Readline keybindings may be configured via an initialization file, typically `.inputrc` in your home directory. See
[Availability](https://docs.python.org/3/library/intro.html#availability): not Android, not iOS, not WASI.
This module is not supported on [mobile platforms](https://docs.python.org/3/library/intro.html#mobile-availability) or [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability).
This is an [optional module](https://docs.python.org/3/glossary.html#term-optional-module). If it is missing from your copy of CPython, look for documentation from your distributor (that is, whoever provided Python to you). If you are the distributor, see [Requirements for optional modules](https://docs.python.org/3/using/configure.html#optional-module-requirements).
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.
Note
The underlying Readline library API may be implemented by the `editline` (`libedit`) library instead of GNU readline. On macOS the `readline` module detects which library is being used at run time.
The configuration file for `editline` is different from that of GNU readline. If you programmatically load configuration strings you can use [`backend`](https://docs.python.org/3/library/readline.html#readline.backend "readline.backend") to determine which library is being used.
If you use `editline`/`libedit` readline emulation on macOS, the initialization file located in your home directory is named `.editrc`. For example, the following content in `~/.editrc` will turn ON _vi_ keybindings and TAB completion:
Copy```
python:bind -v
python:bind ^I rl_complete

```

Also note that different libraries may use different history file formats. When switching the underlying library, existing history files may become unusable.

readline.backend[¶](https://docs.python.org/3/library/readline.html#readline.backend "Link to this definition")

The name of the underlying Readline library being used, either `"readline"` or `"editline"`.
Added in version 3.13.
## Init file[¶](https://docs.python.org/3/library/readline.html#init-file "Link to this heading")
The following functions relate to the init file and user configuration:

readline.parse_and_bind(_string_)[¶](https://docs.python.org/3/library/readline.html#readline.parse_and_bind "Link to this definition")

Execute the init line provided in the _string_ argument. This calls `rl_parse_and_bind()` in the underlying library.

readline.read_init_file([_filename_])[¶](https://docs.python.org/3/library/readline.html#readline.read_init_file "Link to this definition")

Execute a readline initialization file. The default filename is the last filename used. This calls `rl_read_init_file()` in the underlying library. It raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `open` with the file name if given, and `"<readline_init_file>"` otherwise, regardless of which file the library resolves.
Changed in version 3.14: The auditing event was added.
## Line buffer[¶](https://docs.python.org/3/library/readline.html#line-buffer "Link to this heading")
The following functions operate on the line buffer:

readline.get_line_buffer()[¶](https://docs.python.org/3/library/readline.html#readline.get_line_buffer "Link to this definition")

Return the current contents of the line buffer (`rl_line_buffer` in the underlying library).

readline.insert_text(_string_)[¶](https://docs.python.org/3/library/readline.html#readline.insert_text "Link to this definition")

Insert text into the line buffer at the cursor position. This calls `rl_insert_text()` in the underlying library, but ignores the return value.

readline.redisplay()[¶](https://docs.python.org/3/library/readline.html#readline.redisplay "Link to this definition")

Change what’s displayed on the screen to reflect the current contents of the line buffer. This calls `rl_redisplay()` in the underlying library.
## History file[¶](https://docs.python.org/3/library/readline.html#history-file "Link to this heading")
The following functions operate on a history file:

readline.read_history_file([_filename_])[¶](https://docs.python.org/3/library/readline.html#readline.read_history_file "Link to this definition")

Load a readline history file, and append it to the history list. The default filename is `~/.history`. This calls `read_history()` in the underlying library and raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `open` with the file name if given and `"~/.history"` otherwise.
Changed in version 3.14: The auditing event was added.

readline.write_history_file([_filename_])[¶](https://docs.python.org/3/library/readline.html#readline.write_history_file "Link to this definition")

Save the history list to a readline history file, overwriting any existing file. The default filename is `~/.history`. This calls `write_history()` in the underlying library and raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `open` with the file name if given and `"~/.history"` otherwise.
Changed in version 3.14: The auditing event was added.

readline.append_history_file(_nelements_[, _filename_])[¶](https://docs.python.org/3/library/readline.html#readline.append_history_file "Link to this definition")

Append the last _nelements_ items of history to a file. The default filename is `~/.history`. The file must already exist. This calls `append_history()` in the underlying library. This function only exists if Python was compiled for a version of the library that supports it. It raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `open` with the file name if given and `"~/.history"` otherwise.
Added in version 3.5.
Changed in version 3.14: The auditing event was added.

readline.get_history_length()[¶](https://docs.python.org/3/library/readline.html#readline.get_history_length "Link to this definition")


readline.set_history_length(_length_)[¶](https://docs.python.org/3/library/readline.html#readline.set_history_length "Link to this definition")

Set or return the desired number of lines to save in the history file. The [`write_history_file()`](https://docs.python.org/3/library/readline.html#readline.write_history_file "readline.write_history_file") function uses this value to truncate the history file, by calling `history_truncate_file()` in the underlying library. Negative values imply unlimited history file size.
## History list[¶](https://docs.python.org/3/library/readline.html#history-list "Link to this heading")
The following functions operate on a global history list:

readline.clear_history()[¶](https://docs.python.org/3/library/readline.html#readline.clear_history "Link to this definition")

Clear the current history. This calls `clear_history()` in the underlying library. The Python function only exists if Python was compiled for a version of the library that supports it.

readline.get_current_history_length()[¶](https://docs.python.org/3/library/readline.html#readline.get_current_history_length "Link to this definition")

Return the number of items currently in the history. (This is different from [`get_history_length()`](https://docs.python.org/3/library/readline.html#readline.get_history_length "readline.get_history_length"), which returns the maximum number of lines that will be written to a history file.)

readline.get_history_item(_index_)[¶](https://docs.python.org/3/library/readline.html#readline.get_history_item "Link to this definition")

Return the current contents of history item at _index_. The item index is one-based. This calls `history_get()` in the underlying library.

readline.remove_history_item(_pos_)[¶](https://docs.python.org/3/library/readline.html#readline.remove_history_item "Link to this definition")

Remove history item specified by its position from the history. The position is zero-based. This calls `remove_history()` in the underlying library.

readline.replace_history_item(_pos_ , _line_)[¶](https://docs.python.org/3/library/readline.html#readline.replace_history_item "Link to this definition")

Replace history item specified by its position with _line_. The position is zero-based. This calls `replace_history_entry()` in the underlying library.

readline.add_history(_line_)[¶](https://docs.python.org/3/library/readline.html#readline.add_history "Link to this definition")

Append _line_ to the history buffer, as if it was the last line typed. This calls `add_history()` in the underlying library.

readline.set_auto_history(_enabled_)[¶](https://docs.python.org/3/library/readline.html#readline.set_auto_history "Link to this definition")

Enable or disable automatic calls to `add_history()` when reading input via readline. The _enabled_ argument should be a Boolean value that when true, enables auto history, and that when false, disables auto history.
Added in version 3.6.
**CPython implementation detail:** Auto history is enabled by default, and changes to this do not persist across multiple sessions.
## Startup hooks[¶](https://docs.python.org/3/library/readline.html#startup-hooks "Link to this heading")

readline.set_startup_hook([_function_])[¶](https://docs.python.org/3/library/readline.html#readline.set_startup_hook "Link to this definition")

Set or remove the function invoked by the `rl_startup_hook` callback of the underlying library. If _function_ is specified, it will be used as the new hook function; if omitted or `None`, any function already installed is removed. The hook is called with no arguments just before readline prints the first prompt.

readline.set_pre_input_hook([_function_])[¶](https://docs.python.org/3/library/readline.html#readline.set_pre_input_hook "Link to this definition")

Set or remove the function invoked by the `rl_pre_input_hook` callback of the underlying library. If _function_ is specified, it will be used as the new hook function; if omitted or `None`, any function already installed is removed. The hook is called with no arguments after the first prompt has been printed and just before readline starts reading input characters. This function only exists if Python was compiled for a version of the library that supports it.
## Completion[¶](https://docs.python.org/3/library/readline.html#completion "Link to this heading")
The following functions relate to implementing a custom word completion function. This is typically operated by the Tab key, and can suggest and automatically complete a word being typed. By default, Readline is set up to be used by [`rlcompleter`](https://docs.python.org/3/library/rlcompleter.html#module-rlcompleter "rlcompleter: Python identifier completion, suitable for the GNU readline library.") to complete Python identifiers for the interactive interpreter. If the `readline` module is to be used with a custom completer, a different set of word delimiters should be set.

readline.set_completer([_function_])[¶](https://docs.python.org/3/library/readline.html#readline.set_completer "Link to this definition")

Set or remove the completer function. If _function_ is specified, it will be used as the new completer function; if omitted or `None`, any completer function already installed is removed. The completer function is called as `function(text, state)`, for _state_ in `0`, `1`, `2`, …, until it returns a non-string value. It should return the next possible completion starting with _text_.
The installed completer function is invoked by the _entry_func_ callback passed to `rl_completion_matches()` in the underlying library. The _text_ string comes from the first parameter to the `rl_attempted_completion_function` callback of the underlying library.

readline.get_completer()[¶](https://docs.python.org/3/library/readline.html#readline.get_completer "Link to this definition")

Get the completer function, or `None` if no completer function has been set.

readline.get_completion_type()[¶](https://docs.python.org/3/library/readline.html#readline.get_completion_type "Link to this definition")

Get the type of completion being attempted. This returns the `rl_completion_type` variable in the underlying library as an integer.

readline.get_begidx()[¶](https://docs.python.org/3/library/readline.html#readline.get_begidx "Link to this definition")


readline.get_endidx()[¶](https://docs.python.org/3/library/readline.html#readline.get_endidx "Link to this definition")

Get the beginning or ending index of the completion scope. These indexes are the _start_ and _end_ arguments passed to the `rl_attempted_completion_function` callback of the underlying library. The values may be different in the same input editing scenario based on the underlying C readline implementation. Ex: libedit is known to behave differently than libreadline.

readline.set_completer_delims(_string_)[¶](https://docs.python.org/3/library/readline.html#readline.set_completer_delims "Link to this definition")


readline.get_completer_delims()[¶](https://docs.python.org/3/library/readline.html#readline.get_completer_delims "Link to this definition")

Set or get the word delimiters for completion. These determine the start of the word to be considered for completion (the completion scope). These functions access the `rl_completer_word_break_characters` variable in the underlying library.

readline.set_completion_display_matches_hook([_function_])[¶](https://docs.python.org/3/library/readline.html#readline.set_completion_display_matches_hook "Link to this definition")

Set or remove the completion display function. If _function_ is specified, it will be used as the new completion display function; if omitted or `None`, any completion display function already installed is removed. This sets or clears the `rl_completion_display_matches_hook` callback in the underlying library. The completion display function is called as `function(substitution, [matches], longest_match_length)` once each time matches need to be displayed.
## Example[¶](https://docs.python.org/3/library/readline.html#example "Link to this heading")
The following example demonstrates how to use the `readline` module’s history reading and writing functions to automatically load and save a history file named `.python_history` from the user’s home directory. The code below would normally be executed automatically during interactive sessions from the user’s [`PYTHONSTARTUP`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONSTARTUP) file.
Copy```
import atexit
import os
import readline

histfile = os.path.join(os.path.expanduser("~"), ".python_history")
try:
    readline.read_history_file(histfile)
    # default history len is -1 (infinite), which may grow unruly
    readline.set_history_length(1000)
except FileNotFoundError:
    pass

atexit.register(readline.write_history_file, histfile)

```

This code is actually automatically run when Python is run in [interactive mode](https://docs.python.org/3/tutorial/interpreter.html#tut-interactive) (see [Readline configuration](https://docs.python.org/3/library/site.html#rlcompleter-config)).
The following example achieves the same goal but supports concurrent interactive sessions, by only appending the new history.
Copy```
import atexit
import os
import readline
histfile = os.path.join(os.path.expanduser("~"), ".python_history")

try:
    readline.read_history_file(histfile)
    h_len = readline.get_current_history_length()
except FileNotFoundError:
    open(histfile, 'wb').close()
    h_len = 0

def save(prev_h_len, histfile):
    new_h_len = readline.get_current_history_length()
    readline.set_history_length(1000)
    readline.append_history_file(new_h_len - prev_h_len, histfile)
atexit.register(save, h_len, histfile)

```

The following example extends the [`code.InteractiveConsole`](https://docs.python.org/3/library/code.html#code.InteractiveConsole "code.InteractiveConsole") class to support history save/restore.
Copy```
import atexit
import code
import os
import readline

class HistoryConsole(code.InteractiveConsole):
    def __init__(self, locals=None, filename="<console>",
                 histfile=os.path.expanduser("~/.console-history")):
        code.InteractiveConsole.__init__(self, locals, filename)
        self.init_history(histfile)

    def init_history(self, histfile):
        readline.parse_and_bind("tab: complete")
        if hasattr(readline, "read_history_file"):
            try:
                readline.read_history_file(histfile)
            except FileNotFoundError:
                pass
            atexit.register(self.save_history, histfile)

    def save_history(self, histfile):
        readline.set_history_length(1000)
        readline.write_history_file(histfile)

```

Note
The new [REPL](https://docs.python.org/3/glossary.html#term-REPL) introduced in version 3.13 doesn’t support readline. However, readline can still be used by setting the [`PYTHON_BASIC_REPL`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_BASIC_REPL) environment variable.
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`readline` — GNU readline interface](https://docs.python.org/3/library/readline.html)
    * [Init file](https://docs.python.org/3/library/readline.html#init-file)
    * [Line buffer](https://docs.python.org/3/library/readline.html#line-buffer)
    * [History file](https://docs.python.org/3/library/readline.html#history-file)
    * [History list](https://docs.python.org/3/library/readline.html#history-list)
    * [Startup hooks](https://docs.python.org/3/library/readline.html#startup-hooks)
    * [Completion](https://docs.python.org/3/library/readline.html#completion)
    * [Example](https://docs.python.org/3/library/readline.html#example)


#### Previous topic
[`stringprep` — Internet String Preparation](https://docs.python.org/3/library/stringprep.html "previous chapter")
#### Next topic
[`rlcompleter` — Completion function for GNU readline](https://docs.python.org/3/library/rlcompleter.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=readline+%E2%80%94+GNU+readline+interface&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Freadline.html&pagesource=library%2Freadline.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/rlcompleter.html "rlcompleter — Completion function for GNU readline") |
  * [previous](https://docs.python.org/3/library/stringprep.html "stringprep — Internet String Preparation") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Text Processing Services](https://docs.python.org/3/library/text.html) »
  * [`readline` — GNU readline interface](https://docs.python.org/3/library/readline.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
