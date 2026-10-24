## Textbox objects[¶](https://docs.python.org/3/library/curses.html#textbox-objects "Link to this heading")
You can instantiate a [`Textbox`](https://docs.python.org/3/library/curses.html#curses.textpad.Textbox "curses.textpad.Textbox") object as follows:

_class_ curses.textpad.Textbox(_win_)[¶](https://docs.python.org/3/library/curses.html#curses.textpad.Textbox "Link to this definition")

Return a textbox widget object. The _win_ argument should be a curses [window](https://docs.python.org/3/library/curses.html#curses-window-objects) object in which the textbox is to be contained. The edit cursor of the textbox is initially located at the upper left hand corner of the containing window, with coordinates `(0, 0)`. The instance’s [`stripspaces`](https://docs.python.org/3/library/curses.html#curses.textpad.Textbox.stripspaces "curses.textpad.Textbox.stripspaces") flag is initially on.
`Textbox` objects have the following methods:

edit([_validator_])[¶](https://docs.python.org/3/library/curses.html#curses.textpad.Textbox.edit "Link to this definition")

This is the entry point you will normally use. It accepts editing keystrokes until one of the termination keystrokes is entered. If _validator_ is supplied, it must be a function. It will be called for each keystroke entered with the keystroke as a parameter; command dispatch is done on the result. This method returns the window contents as a string; whether blanks in the window are included is affected by the [`stripspaces`](https://docs.python.org/3/library/curses.html#curses.textpad.Textbox.stripspaces "curses.textpad.Textbox.stripspaces") attribute.

do_command(_ch_)[¶](https://docs.python.org/3/library/curses.html#curses.textpad.Textbox.do_command "Link to this definition")

Process a single command keystroke. Here are the supported special keystrokes:
Keystroke | Action
---|---
`Control`-`A` | Go to left edge of window.
`Control`-`B` | Cursor left, wrapping to previous line if appropriate.
`Control`-`D` | Delete character under cursor.
`Control`-`E` | Go to right edge (stripspaces off) or end of line (stripspaces on).
`Control`-`F` | Cursor right, wrapping to next line when appropriate.
`Control`-`G` | Terminate, returning the window contents.
`Control`-`H` | Delete character backward.
`Control`-`J` | Terminate if the window is 1 line, otherwise insert newline.
`Control`-`K` | If line is blank, delete it, otherwise clear to end of line.
`Control`-`L` | Refresh screen.
`Control`-`N` | Cursor down; move down one line.
`Control`-`O` | Insert a blank line at cursor location.
`Control`-`P` | Cursor up; move up one line.
Move operations do nothing if the cursor is at an edge where the movement is not possible. The following synonyms are supported where possible:
Constant | Keystroke
---|---
[`KEY_LEFT`](https://docs.python.org/3/library/curses.html#curses.KEY_LEFT "curses.KEY_LEFT") | `Control`-`B`
[`KEY_RIGHT`](https://docs.python.org/3/library/curses.html#curses.KEY_RIGHT "curses.KEY_RIGHT") | `Control`-`F`
[`KEY_UP`](https://docs.python.org/3/library/curses.html#curses.KEY_UP "curses.KEY_UP") | `Control`-`P`
[`KEY_DOWN`](https://docs.python.org/3/library/curses.html#curses.KEY_DOWN "curses.KEY_DOWN") | `Control`-`N`
[`KEY_BACKSPACE`](https://docs.python.org/3/library/curses.html#curses.KEY_BACKSPACE "curses.KEY_BACKSPACE") | `Control`-`h`
All other keystrokes are treated as a command to insert the given character and move right (with line wrapping).

gather()[¶](https://docs.python.org/3/library/curses.html#curses.textpad.Textbox.gather "Link to this definition")

Return the window contents as a string; whether blanks in the window are included is affected by the [`stripspaces`](https://docs.python.org/3/library/curses.html#curses.textpad.Textbox.stripspaces "curses.textpad.Textbox.stripspaces") member.

stripspaces[¶](https://docs.python.org/3/library/curses.html#curses.textpad.Textbox.stripspaces "Link to this definition")

This attribute is a flag which controls the interpretation of blanks in the window. When it is on, trailing blanks on each line are ignored; any cursor motion that would land the cursor on a trailing blank goes to the end of that line instead, and trailing blanks are stripped when the window contents are gathered.
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`curses` — Terminal handling for character-cell displays](https://docs.python.org/3/library/curses.html)
    * [Functions](https://docs.python.org/3/library/curses.html#functions)
    * [Window Objects](https://docs.python.org/3/library/curses.html#window-objects)
    * [Constants](https://docs.python.org/3/library/curses.html#constants)
  * [`curses.textpad` — Text input widget for curses programs](https://docs.python.org/3/library/curses.html#module-curses.textpad)
    * [Textbox objects](https://docs.python.org/3/library/curses.html#textbox-objects)


#### Previous topic
[`fileinput` — Iterate over lines from multiple input streams](https://docs.python.org/3/library/fileinput.html "previous chapter")
#### Next topic
[`curses.ascii` — Utilities for ASCII characters](https://docs.python.org/3/library/curses.ascii.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=curses+%E2%80%94+Terminal+handling+for+character-cell+displays&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fcurses.html&pagesource=library%2Fcurses.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/curses.ascii.html "curses.ascii — Utilities for ASCII characters") |
  * [previous](https://docs.python.org/3/library/fileinput.html "fileinput — Iterate over lines from multiple input streams") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Command-line interface libraries](https://docs.python.org/3/library/cmdlinelibs.html) »
  * [`curses` — Terminal handling for character-cell displays](https://docs.python.org/3/library/curses.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
  *[/]: Positional-only parameter separator (PEP 570)
