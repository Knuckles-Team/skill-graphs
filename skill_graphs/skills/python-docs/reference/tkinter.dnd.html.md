[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`tkinter.scrolledtext` — Scrolled Text Widget](https://docs.python.org/3/library/tkinter.scrolledtext.html "previous chapter")
#### Next topic
[`tkinter.ttk` — Tk themed widgets](https://docs.python.org/3/library/tkinter.ttk.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=tkinter.dnd+%E2%80%94+Drag+and+drop+support&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ftkinter.dnd.html&pagesource=library%2Ftkinter.dnd.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/tkinter.ttk.html "tkinter.ttk — Tk themed widgets") |
  * [previous](https://docs.python.org/3/library/tkinter.scrolledtext.html "tkinter.scrolledtext — Scrolled Text Widget") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Graphical user interfaces with Tk](https://docs.python.org/3/library/tk.html) »
  * [`tkinter.dnd` — Drag and drop support](https://docs.python.org/3/library/tkinter.dnd.html)
  * |
  * Theme  Auto Light Dark |


#  `tkinter.dnd` — Drag and drop support[¶](https://docs.python.org/3/library/tkinter.dnd.html#module-tkinter.dnd "Link to this heading")
**Source code:**
* * *
Note
This is experimental and due to be deprecated when it is replaced with the Tk DND.
The `tkinter.dnd` module provides drag-and-drop support for objects within a single application, within the same window or between windows. To enable an object to be dragged, you must create an event binding for it that starts the drag-and-drop process. Typically, you bind a ButtonPress event to a callback function that you write (see [Bindings and Events](https://docs.python.org/3/library/tkinter.html#bindings-and-events)). The function should call [`dnd_start()`](https://docs.python.org/3/library/tkinter.dnd.html#tkinter.dnd.dnd_start "tkinter.dnd.dnd_start"), where ‘source’ is the object to be dragged, and ‘event’ is the event that invoked the call (the argument to your callback function).
Selection of a target object occurs as follows:
  1. Top-down search of area under mouse for target widget


>   * Target widget should have a callable _dnd_accept_ attribute
>   * If _dnd_accept_ is not present or returns `None`, search moves to parent widget
>   * If no target widget is found, then the target object is `None`
>

  1. Call to _< old_target>.dnd_leave(source, event)_
  2. Call to _< new_target>.dnd_enter(source, event)_
  3. Call to _< target>.dnd_commit(source, event)_ to notify of drop
  4. Call to _< source>.dnd_end(target, event)_ to signal end of drag-and-drop



_class_ tkinter.dnd.DndHandler(_source_ , _event_)[¶](https://docs.python.org/3/library/tkinter.dnd.html#tkinter.dnd.DndHandler "Link to this definition")

The _DndHandler_ class handles drag-and-drop events tracking Motion and ButtonRelease events on the root of the event widget.

cancel(_event =None_)[¶](https://docs.python.org/3/library/tkinter.dnd.html#tkinter.dnd.DndHandler.cancel "Link to this definition")

Cancel the drag-and-drop process.

finish(_event_ , _commit =0_)[¶](https://docs.python.org/3/library/tkinter.dnd.html#tkinter.dnd.DndHandler.finish "Link to this definition")

Execute end of drag-and-drop functions.

on_motion(_event_)[¶](https://docs.python.org/3/library/tkinter.dnd.html#tkinter.dnd.DndHandler.on_motion "Link to this definition")

Inspect area below mouse for target objects while drag is performed.

on_release(_event_)[¶](https://docs.python.org/3/library/tkinter.dnd.html#tkinter.dnd.DndHandler.on_release "Link to this definition")

Signal end of drag when the release pattern is triggered.

tkinter.dnd.dnd_start(_source_ , _event_)[¶](https://docs.python.org/3/library/tkinter.dnd.html#tkinter.dnd.dnd_start "Link to this definition")

Factory function for drag-and-drop process.
See also
[Bindings and Events](https://docs.python.org/3/library/tkinter.html#bindings-and-events)
#### Previous topic
[`tkinter.scrolledtext` — Scrolled Text Widget](https://docs.python.org/3/library/tkinter.scrolledtext.html "previous chapter")
#### Next topic
[`tkinter.ttk` — Tk themed widgets](https://docs.python.org/3/library/tkinter.ttk.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=tkinter.dnd+%E2%80%94+Drag+and+drop+support&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ftkinter.dnd.html&pagesource=library%2Ftkinter.dnd.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/tkinter.ttk.html "tkinter.ttk — Tk themed widgets") |
  * [previous](https://docs.python.org/3/library/tkinter.scrolledtext.html "tkinter.scrolledtext — Scrolled Text Widget") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Graphical user interfaces with Tk](https://docs.python.org/3/library/tk.html) »
  * [`tkinter.dnd` — Drag and drop support](https://docs.python.org/3/library/tkinter.dnd.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
