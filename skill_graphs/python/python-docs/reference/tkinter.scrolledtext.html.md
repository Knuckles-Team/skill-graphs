[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`tkinter.messagebox` — Tkinter message prompts](https://docs.python.org/3/library/tkinter.messagebox.html "previous chapter")
#### Next topic
[`tkinter.dnd` — Drag and drop support](https://docs.python.org/3/library/tkinter.dnd.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=tkinter.scrolledtext+%E2%80%94+Scrolled+Text+Widget&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ftkinter.scrolledtext.html&pagesource=library%2Ftkinter.scrolledtext.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/tkinter.dnd.html "tkinter.dnd — Drag and drop support") |
  * [previous](https://docs.python.org/3/library/tkinter.messagebox.html "tkinter.messagebox — Tkinter message prompts") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Graphical user interfaces with Tk](https://docs.python.org/3/library/tk.html) »
  * [`tkinter.scrolledtext` — Scrolled Text Widget](https://docs.python.org/3/library/tkinter.scrolledtext.html)
  * |
  * Theme  Auto Light Dark |


#  `tkinter.scrolledtext` — Scrolled Text Widget[¶](https://docs.python.org/3/library/tkinter.scrolledtext.html#module-tkinter.scrolledtext "Link to this heading")
**Source code:**
* * *
The `tkinter.scrolledtext` module provides a class of the same name which implements a basic text widget which has a vertical scroll bar configured to do the “right thing.” Using the [`ScrolledText`](https://docs.python.org/3/library/tkinter.scrolledtext.html#tkinter.scrolledtext.ScrolledText "tkinter.scrolledtext.ScrolledText") class is a lot easier than setting up a text widget and scroll bar directly.
The text widget and scrollbar are packed together in a `Frame`, and the methods of the `Grid` and `Pack` geometry managers are acquired from the `Frame` object. This allows the [`ScrolledText`](https://docs.python.org/3/library/tkinter.scrolledtext.html#tkinter.scrolledtext.ScrolledText "tkinter.scrolledtext.ScrolledText") widget to be used directly to achieve most normal geometry management behavior.
Should more specific control be necessary, the following attributes are available:

_class_ tkinter.scrolledtext.ScrolledText(_master =None_, _** kw_)[¶](https://docs.python.org/3/library/tkinter.scrolledtext.html#tkinter.scrolledtext.ScrolledText "Link to this definition")


frame[¶](https://docs.python.org/3/library/tkinter.scrolledtext.html#tkinter.scrolledtext.ScrolledText.frame "Link to this definition")

The frame which surrounds the text and scroll bar widgets.

vbar[¶](https://docs.python.org/3/library/tkinter.scrolledtext.html#tkinter.scrolledtext.ScrolledText.vbar "Link to this definition")

The scroll bar widget.
#### Previous topic
[`tkinter.messagebox` — Tkinter message prompts](https://docs.python.org/3/library/tkinter.messagebox.html "previous chapter")
#### Next topic
[`tkinter.dnd` — Drag and drop support](https://docs.python.org/3/library/tkinter.dnd.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=tkinter.scrolledtext+%E2%80%94+Scrolled+Text+Widget&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ftkinter.scrolledtext.html&pagesource=library%2Ftkinter.scrolledtext.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/tkinter.dnd.html "tkinter.dnd — Drag and drop support") |
  * [previous](https://docs.python.org/3/library/tkinter.messagebox.html "tkinter.messagebox — Tkinter message prompts") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Graphical user interfaces with Tk](https://docs.python.org/3/library/tk.html) »
  * [`tkinter.scrolledtext` — Scrolled Text Widget](https://docs.python.org/3/library/tkinter.scrolledtext.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
