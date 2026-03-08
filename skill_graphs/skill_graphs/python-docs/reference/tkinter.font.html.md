[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`tkinter.colorchooser` — Color choosing dialog](https://docs.python.org/3/library/tkinter.colorchooser.html "previous chapter")
#### Next topic
[Tkinter Dialogs](https://docs.python.org/3/library/dialog.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=tkinter.font+%E2%80%94+Tkinter+font+wrapper&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ftkinter.font.html&pagesource=library%2Ftkinter.font.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/dialog.html "Tkinter Dialogs") |
  * [previous](https://docs.python.org/3/library/tkinter.colorchooser.html "tkinter.colorchooser — Color choosing dialog") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Graphical user interfaces with Tk](https://docs.python.org/3/library/tk.html) »
  * [`tkinter.font` — Tkinter font wrapper](https://docs.python.org/3/library/tkinter.font.html)
  * |
  * Theme  Auto Light Dark |


#  `tkinter.font` — Tkinter font wrapper[¶](https://docs.python.org/3/library/tkinter.font.html#module-tkinter.font "Link to this heading")
**Source code:**
* * *
The `tkinter.font` module provides the [`Font`](https://docs.python.org/3/library/tkinter.font.html#tkinter.font.Font "tkinter.font.Font") class for creating and using named fonts.
The different font weights and slants are:

tkinter.font.NORMAL[¶](https://docs.python.org/3/library/tkinter.font.html#tkinter.font.NORMAL "Link to this definition")


tkinter.font.BOLD[¶](https://docs.python.org/3/library/tkinter.font.html#tkinter.font.BOLD "Link to this definition")


tkinter.font.ITALIC[¶](https://docs.python.org/3/library/tkinter.font.html#tkinter.font.ITALIC "Link to this definition")


tkinter.font.ROMAN[¶](https://docs.python.org/3/library/tkinter.font.html#tkinter.font.ROMAN "Link to this definition")


_class_ tkinter.font.Font(_root =None_, _font =None_, _name =None_, _exists =False_, _** options_)[¶](https://docs.python.org/3/library/tkinter.font.html#tkinter.font.Font "Link to this definition")

The `Font` class represents a named font. _Font_ instances are given unique names and can be specified by their family, size, and style configuration. Named fonts are Tk’s method of creating and identifying fonts as a single object, rather than specifying a font by its attributes with each occurrence.
> arguments:
>> _font_ - font specifier tuple (family, size, options)
>> _name_ - unique font name
>> _exists_ - self points to existing named font if true
> additional keyword options (ignored if _font_ is specified):
>> _family_ - font family i.e. Courier, Times
>> _size_ - font size
>> If _size_ is positive it is interpreted as size in points.
>> If _size_ is a negative number its absolute value is treated
>> as size in pixels.
>> _weight_ - font emphasis (NORMAL, BOLD)
>> _slant_ - ROMAN, ITALIC
>> _underline_ - font underlining (0 - none, 1 - underline)
>> _overstrike_ - font strikeout (0 - none, 1 - strikeout)

actual(_option =None_, _displayof =None_)[¶](https://docs.python.org/3/library/tkinter.font.html#tkinter.font.Font.actual "Link to this definition")

Return the attributes of the font.

cget(_option_)[¶](https://docs.python.org/3/library/tkinter.font.html#tkinter.font.Font.cget "Link to this definition")

Retrieve an attribute of the font.

config(_** options_)[¶](https://docs.python.org/3/library/tkinter.font.html#tkinter.font.Font.config "Link to this definition")

Modify attributes of the font.

copy()[¶](https://docs.python.org/3/library/tkinter.font.html#tkinter.font.Font.copy "Link to this definition")

Return new instance of the current font.

measure(_text_ , _displayof =None_)[¶](https://docs.python.org/3/library/tkinter.font.html#tkinter.font.Font.measure "Link to this definition")

Return amount of space the text would occupy on the specified display when formatted in the current font. If no display is specified then the main application window is assumed.

metrics(_* options_, _** kw_)[¶](https://docs.python.org/3/library/tkinter.font.html#tkinter.font.Font.metrics "Link to this definition")

Return font-specific data. Options include:

_ascent_ - distance between baseline and highest point that a

character of the font can occupy

_descent_ - distance between baseline and lowest point that a

character of the font can occupy

_linespace_ - minimum vertical separation necessary between any two

characters of the font that ensures no vertical overlap between lines.
_fixed_ - 1 if font is fixed-width else 0

tkinter.font.families(_root =None_, _displayof =None_)[¶](https://docs.python.org/3/library/tkinter.font.html#tkinter.font.families "Link to this definition")

Return the different font families.

tkinter.font.names(_root =None_)[¶](https://docs.python.org/3/library/tkinter.font.html#tkinter.font.names "Link to this definition")

Return the names of defined fonts.

tkinter.font.nametofont(_name_ , _root =None_)[¶](https://docs.python.org/3/library/tkinter.font.html#tkinter.font.nametofont "Link to this definition")

Return a [`Font`](https://docs.python.org/3/library/tkinter.font.html#tkinter.font.Font "tkinter.font.Font") representation of a tk named font.
Changed in version 3.10: The _root_ parameter was added.
#### Previous topic
[`tkinter.colorchooser` — Color choosing dialog](https://docs.python.org/3/library/tkinter.colorchooser.html "previous chapter")
#### Next topic
[Tkinter Dialogs](https://docs.python.org/3/library/dialog.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=tkinter.font+%E2%80%94+Tkinter+font+wrapper&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ftkinter.font.html&pagesource=library%2Ftkinter.font.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/dialog.html "Tkinter Dialogs") |
  * [previous](https://docs.python.org/3/library/tkinter.colorchooser.html "tkinter.colorchooser — Color choosing dialog") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Graphical user interfaces with Tk](https://docs.python.org/3/library/tk.html) »
  * [`tkinter.font` — Tkinter font wrapper](https://docs.python.org/3/library/tkinter.font.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
