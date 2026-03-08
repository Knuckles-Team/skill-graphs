[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`curses.panel` — A panel stack extension for curses](https://docs.python.org/3/library/curses.panel.html)
    * [Functions](https://docs.python.org/3/library/curses.panel.html#functions)
    * [Panel Objects](https://docs.python.org/3/library/curses.panel.html#panel-objects)


#### Previous topic
[`curses.ascii` — Utilities for ASCII characters](https://docs.python.org/3/library/curses.ascii.html "previous chapter")
#### Next topic
[`cmd` — Support for line-oriented command interpreters](https://docs.python.org/3/library/cmd.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=curses.panel+%E2%80%94+A+panel+stack+extension+for+curses&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fcurses.panel.html&pagesource=library%2Fcurses.panel.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/cmd.html "cmd — Support for line-oriented command interpreters") |
  * [previous](https://docs.python.org/3/library/curses.ascii.html "curses.ascii — Utilities for ASCII characters") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Command-line interface libraries](https://docs.python.org/3/library/cmdlinelibs.html) »
  * [`curses.panel` — A panel stack extension for curses](https://docs.python.org/3/library/curses.panel.html)
  * |
  * Theme  Auto Light Dark |


#  `curses.panel` — A panel stack extension for curses[¶](https://docs.python.org/3/library/curses.panel.html#module-curses.panel "Link to this heading")
* * *
Panels are windows with the added feature of depth, so they can be stacked on top of each other, and only the visible portions of each window will be displayed. Panels can be added, moved up or down in the stack, and removed.
## Functions[¶](https://docs.python.org/3/library/curses.panel.html#functions "Link to this heading")
The module `curses.panel` defines the following functions:

curses.panel.bottom_panel()[¶](https://docs.python.org/3/library/curses.panel.html#curses.panel.bottom_panel "Link to this definition")

Returns the bottom panel in the panel stack.

curses.panel.new_panel(_win_)[¶](https://docs.python.org/3/library/curses.panel.html#curses.panel.new_panel "Link to this definition")

Returns a panel object, associating it with the given window _win_. Be aware that you need to keep the returned panel object referenced explicitly. If you don’t, the panel object is garbage collected and removed from the panel stack.

curses.panel.top_panel()[¶](https://docs.python.org/3/library/curses.panel.html#curses.panel.top_panel "Link to this definition")

Returns the top panel in the panel stack.

curses.panel.update_panels()[¶](https://docs.python.org/3/library/curses.panel.html#curses.panel.update_panels "Link to this definition")

Updates the virtual screen after changes in the panel stack. This does not call [`curses.doupdate()`](https://docs.python.org/3/library/curses.html#curses.doupdate "curses.doupdate"), so you’ll have to do this yourself.
## Panel Objects[¶](https://docs.python.org/3/library/curses.panel.html#panel-objects "Link to this heading")
Panel objects, as returned by [`new_panel()`](https://docs.python.org/3/library/curses.panel.html#curses.panel.new_panel "curses.panel.new_panel") above, are windows with a stacking order. There’s always a window associated with a panel which determines the content, while the panel methods are responsible for the window’s depth in the panel stack.
Panel objects have the following methods:

Panel.above()[¶](https://docs.python.org/3/library/curses.panel.html#curses.panel.Panel.above "Link to this definition")

Returns the panel above the current panel.

Panel.below()[¶](https://docs.python.org/3/library/curses.panel.html#curses.panel.Panel.below "Link to this definition")

Returns the panel below the current panel.

Panel.bottom()[¶](https://docs.python.org/3/library/curses.panel.html#curses.panel.Panel.bottom "Link to this definition")

Push the panel to the bottom of the stack.

Panel.hidden()[¶](https://docs.python.org/3/library/curses.panel.html#curses.panel.Panel.hidden "Link to this definition")

Returns `True` if the panel is hidden (not visible), `False` otherwise.

Panel.hide()[¶](https://docs.python.org/3/library/curses.panel.html#curses.panel.Panel.hide "Link to this definition")

Hide the panel. This does not delete the object, it just makes the window on screen invisible.

Panel.move(_y_ , _x_)[¶](https://docs.python.org/3/library/curses.panel.html#curses.panel.Panel.move "Link to this definition")

Move the panel to the screen coordinates `(y, x)`.

Panel.replace(_win_)[¶](https://docs.python.org/3/library/curses.panel.html#curses.panel.Panel.replace "Link to this definition")

Change the window associated with the panel to the window _win_.

Panel.set_userptr(_obj_)[¶](https://docs.python.org/3/library/curses.panel.html#curses.panel.Panel.set_userptr "Link to this definition")

Set the panel’s user pointer to _obj_. This is used to associate an arbitrary piece of data with the panel, and can be any Python object.

Panel.show()[¶](https://docs.python.org/3/library/curses.panel.html#curses.panel.Panel.show "Link to this definition")

Display the panel (which might have been hidden).

Panel.top()[¶](https://docs.python.org/3/library/curses.panel.html#curses.panel.Panel.top "Link to this definition")

Push panel to the top of the stack.

Panel.userptr()[¶](https://docs.python.org/3/library/curses.panel.html#curses.panel.Panel.userptr "Link to this definition")

Returns the user pointer for the panel. This might be any Python object.

Panel.window()[¶](https://docs.python.org/3/library/curses.panel.html#curses.panel.Panel.window "Link to this definition")

Returns the window object associated with the panel.
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`curses.panel` — A panel stack extension for curses](https://docs.python.org/3/library/curses.panel.html)
    * [Functions](https://docs.python.org/3/library/curses.panel.html#functions)
    * [Panel Objects](https://docs.python.org/3/library/curses.panel.html#panel-objects)


#### Previous topic
[`curses.ascii` — Utilities for ASCII characters](https://docs.python.org/3/library/curses.ascii.html "previous chapter")
#### Next topic
[`cmd` — Support for line-oriented command interpreters](https://docs.python.org/3/library/cmd.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=curses.panel+%E2%80%94+A+panel+stack+extension+for+curses&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fcurses.panel.html&pagesource=library%2Fcurses.panel.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/cmd.html "cmd — Support for line-oriented command interpreters") |
  * [previous](https://docs.python.org/3/library/curses.ascii.html "curses.ascii — Utilities for ASCII characters") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Command-line interface libraries](https://docs.python.org/3/library/cmdlinelibs.html) »
  * [`curses.panel` — A panel stack extension for curses](https://docs.python.org/3/library/curses.panel.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
