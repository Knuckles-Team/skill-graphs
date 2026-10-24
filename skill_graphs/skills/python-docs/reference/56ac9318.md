[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`tkinter.ttk` — Tk themed widgets](https://docs.python.org/3/library/tkinter.ttk.html)
    * [Using Ttk](https://docs.python.org/3/library/tkinter.ttk.html#using-ttk)
    * [Ttk Widgets](https://docs.python.org/3/library/tkinter.ttk.html#ttk-widgets)
    * [Widget](https://docs.python.org/3/library/tkinter.ttk.html#widget)
      * [Standard Options](https://docs.python.org/3/library/tkinter.ttk.html#standard-options)
      * [Scrollable Widget Options](https://docs.python.org/3/library/tkinter.ttk.html#scrollable-widget-options)
      * [Label Options](https://docs.python.org/3/library/tkinter.ttk.html#label-options)
      * [Compatibility Options](https://docs.python.org/3/library/tkinter.ttk.html#compatibility-options)
      * [Widget States](https://docs.python.org/3/library/tkinter.ttk.html#widget-states)
      * [ttk.Widget](https://docs.python.org/3/library/tkinter.ttk.html#ttk-widget)
    * [Combobox](https://docs.python.org/3/library/tkinter.ttk.html#combobox)
      * [Options](https://docs.python.org/3/library/tkinter.ttk.html#options)
      * [Virtual events](https://docs.python.org/3/library/tkinter.ttk.html#virtual-events)
      * [ttk.Combobox](https://docs.python.org/3/library/tkinter.ttk.html#ttk-combobox)
    * [Spinbox](https://docs.python.org/3/library/tkinter.ttk.html#spinbox)
      * [Options](https://docs.python.org/3/library/tkinter.ttk.html#id1)
      * [Virtual events](https://docs.python.org/3/library/tkinter.ttk.html#id2)
      * [ttk.Spinbox](https://docs.python.org/3/library/tkinter.ttk.html#ttk-spinbox)
    * [Notebook](https://docs.python.org/3/library/tkinter.ttk.html#notebook)
      * [Options](https://docs.python.org/3/library/tkinter.ttk.html#id3)
      * [Tab Options](https://docs.python.org/3/library/tkinter.ttk.html#tab-options)
      * [Tab Identifiers](https://docs.python.org/3/library/tkinter.ttk.html#tab-identifiers)
      * [Virtual Events](https://docs.python.org/3/library/tkinter.ttk.html#id4)
      * [ttk.Notebook](https://docs.python.org/3/library/tkinter.ttk.html#ttk-notebook)
    * [Progressbar](https://docs.python.org/3/library/tkinter.ttk.html#progressbar)
      * [Options](https://docs.python.org/3/library/tkinter.ttk.html#id5)
      * [ttk.Progressbar](https://docs.python.org/3/library/tkinter.ttk.html#ttk-progressbar)
    * [Separator](https://docs.python.org/3/library/tkinter.ttk.html#separator)
      * [Options](https://docs.python.org/3/library/tkinter.ttk.html#id6)
    * [Sizegrip](https://docs.python.org/3/library/tkinter.ttk.html#sizegrip)
      * [Platform-specific notes](https://docs.python.org/3/library/tkinter.ttk.html#platform-specific-notes)
      * [Bugs](https://docs.python.org/3/library/tkinter.ttk.html#bugs)
    * [Treeview](https://docs.python.org/3/library/tkinter.ttk.html#treeview)
      * [Options](https://docs.python.org/3/library/tkinter.ttk.html#id7)
      * [Item Options](https://docs.python.org/3/library/tkinter.ttk.html#item-options)
      * [Tag Options](https://docs.python.org/3/library/tkinter.ttk.html#tag-options)
      * [Column Identifiers](https://docs.python.org/3/library/tkinter.ttk.html#column-identifiers)
      * [Virtual Events](https://docs.python.org/3/library/tkinter.ttk.html#id8)
      * [ttk.Treeview](https://docs.python.org/3/library/tkinter.ttk.html#ttk-treeview)
    * [Ttk Styling](https://docs.python.org/3/library/tkinter.ttk.html#ttk-styling)
      * [Layouts](https://docs.python.org/3/library/tkinter.ttk.html#layouts)


#### Previous topic
[`tkinter.dnd` — Drag and drop support](https://docs.python.org/3/library/tkinter.dnd.html "previous chapter")
#### Next topic
[IDLE — Python editor and shell](https://docs.python.org/3/library/idle.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=tkinter.ttk+%E2%80%94+Tk+themed+widgets&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ftkinter.ttk.html&pagesource=library%2Ftkinter.ttk.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/idle.html "IDLE — Python editor and shell") |
  * [previous](https://docs.python.org/3/library/tkinter.dnd.html "tkinter.dnd — Drag and drop support") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Graphical user interfaces with Tk](https://docs.python.org/3/library/tk.html) »
  * [`tkinter.ttk` — Tk themed widgets](https://docs.python.org/3/library/tkinter.ttk.html)
  * |
  * Theme  Auto Light Dark |
