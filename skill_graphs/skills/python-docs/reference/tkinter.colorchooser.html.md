[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`tkinter` — Python interface to Tcl/Tk](https://docs.python.org/3/library/tkinter.html "previous chapter")
#### Next topic
[`tkinter.font` — Tkinter font wrapper](https://docs.python.org/3/library/tkinter.font.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=tkinter.colorchooser+%E2%80%94+Color+choosing+dialog&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ftkinter.colorchooser.html&pagesource=library%2Ftkinter.colorchooser.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/tkinter.font.html "tkinter.font — Tkinter font wrapper") |
  * [previous](https://docs.python.org/3/library/tkinter.html "tkinter — Python interface to Tcl/Tk") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Graphical user interfaces with Tk](https://docs.python.org/3/library/tk.html) »
  * [`tkinter.colorchooser` — Color choosing dialog](https://docs.python.org/3/library/tkinter.colorchooser.html)
  * |
  * Theme  Auto Light Dark |


#  `tkinter.colorchooser` — Color choosing dialog[¶](https://docs.python.org/3/library/tkinter.colorchooser.html#module-tkinter.colorchooser "Link to this heading")
**Source code:**
* * *
The `tkinter.colorchooser` module provides the [`Chooser`](https://docs.python.org/3/library/tkinter.colorchooser.html#tkinter.colorchooser.Chooser "tkinter.colorchooser.Chooser") class as an interface to the native color picker dialog. `Chooser` implements a modal color choosing dialog window. The `Chooser` class inherits from the [`Dialog`](https://docs.python.org/3/library/dialog.html#tkinter.commondialog.Dialog "tkinter.commondialog.Dialog") class.

_class_ tkinter.colorchooser.Chooser(_master =None_, _** options_)[¶](https://docs.python.org/3/library/tkinter.colorchooser.html#tkinter.colorchooser.Chooser "Link to this definition")


tkinter.colorchooser.askcolor(_color =None_, _** options_)[¶](https://docs.python.org/3/library/tkinter.colorchooser.html#tkinter.colorchooser.askcolor "Link to this definition")

Create a color choosing dialog. A call to this method will show the window, wait for the user to make a selection, and return the selected color (or `None`) to the caller.
See also

Module [`tkinter.commondialog`](https://docs.python.org/3/library/dialog.html#module-tkinter.commondialog "tkinter.commondialog: Tkinter base class for dialogs")

Tkinter standard dialog module
#### Previous topic
[`tkinter` — Python interface to Tcl/Tk](https://docs.python.org/3/library/tkinter.html "previous chapter")
#### Next topic
[`tkinter.font` — Tkinter font wrapper](https://docs.python.org/3/library/tkinter.font.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=tkinter.colorchooser+%E2%80%94+Color+choosing+dialog&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ftkinter.colorchooser.html&pagesource=library%2Ftkinter.colorchooser.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/tkinter.font.html "tkinter.font — Tkinter font wrapper") |
  * [previous](https://docs.python.org/3/library/tkinter.html "tkinter — Python interface to Tcl/Tk") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Graphical user interfaces with Tk](https://docs.python.org/3/library/tk.html) »
  * [`tkinter.colorchooser` — Color choosing dialog](https://docs.python.org/3/library/tkinter.colorchooser.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
