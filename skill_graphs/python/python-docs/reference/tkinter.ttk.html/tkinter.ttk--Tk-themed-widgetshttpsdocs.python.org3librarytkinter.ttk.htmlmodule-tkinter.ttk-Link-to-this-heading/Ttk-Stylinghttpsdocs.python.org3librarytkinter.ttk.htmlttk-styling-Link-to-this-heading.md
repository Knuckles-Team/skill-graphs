## Ttk Styling[¶](https://docs.python.org/3/library/tkinter.ttk.html#ttk-styling "Link to this heading")
Each widget in `ttk` is assigned a style, which specifies the set of elements making up the widget and how they are arranged, along with dynamic and default settings for element options. By default the style name is the same as the widget’s class name, but it may be overridden by the widget’s style option. If you don’t know the class name of a widget, use the method `Misc.winfo_class()` (somewidget.winfo_class()).
See also
This document explains how the theme engine works

_class_ tkinter.ttk.Style[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Style "Link to this definition")

This class is used to manipulate the style database.

configure(_style_ , _query_opt =None_, _** kw_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Style.configure "Link to this definition")

Query or set the default value of the specified option(s) in _style_.
Each key in _kw_ is an option and each value is a string identifying the value for that option.
For example, to change every default button to be a flat button with some padding and a different background color:
Copy```
from tkinter import ttk
import tkinter

root = tkinter.Tk()

ttk.Style().configure("TButton", padding=6, relief="flat",
   background="#ccc")

btn = ttk.Button(text="Sample")
btn.pack()

root.mainloop()

```


map(_style_ , _query_opt =None_, _** kw_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Style.map "Link to this definition")

Query or sets dynamic values of the specified option(s) in _style_.
Each key in _kw_ is an option and each value should be a list or a tuple (usually) containing statespecs grouped in tuples, lists, or some other preference. A statespec is a compound of one or more states and then a value.
An example may make it more understandable:
Copy```
import tkinter
from tkinter import ttk

root = tkinter.Tk()

style = ttk.Style()
style.map("C.TButton",
    foreground=[('pressed', 'red'), ('active', 'blue')],
    background=[('pressed', '!disabled', 'black'), ('active', 'white')]
    )

colored_btn = ttk.Button(text="Test", style="C.TButton").pack()

root.mainloop()

```

Note that the order of the (states, value) sequences for an option does matter, if the order is changed to `[('active', 'blue'), ('pressed', 'red')]` in the foreground option, for example, the result would be a blue foreground when the widget were in active or pressed states.

lookup(_style_ , _option_ , _state =None_, _default =None_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Style.lookup "Link to this definition")

Returns the value specified for _option_ in _style_.
If _state_ is specified, it is expected to be a sequence of one or more states. If the _default_ argument is set, it is used as a fallback value in case no specification for option is found.
To check what font a Button uses by default:
Copy```
from tkinter import ttk

print(ttk.Style().lookup("TButton", "font"))

```


layout(_style_ , _layoutspec =None_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Style.layout "Link to this definition")

Define the widget layout for given _style_. If _layoutspec_ is omitted, return the layout specification for given style.
_layoutspec_ , if specified, is expected to be a list or some other sequence type (excluding strings), where each item should be a tuple and the first item is the layout name and the second item should have the format described in [Layouts](https://docs.python.org/3/library/tkinter.ttk.html#layouts).
To understand the format, see the following example (it is not intended to do anything useful):
Copy```
from tkinter import ttk
import tkinter

root = tkinter.Tk()

style = ttk.Style()
style.layout("TMenubutton", [
   ("Menubutton.background", None),
   ("Menubutton.button", {"children":
       [("Menubutton.focus", {"children":
           [("Menubutton.padding", {"children":
               [("Menubutton.label", {"side": "left", "expand": 1})]
           })]
       })]
   }),
])

mbtn = ttk.Menubutton(text='Text')
mbtn.pack()
root.mainloop()

```


element_create(_elementname_ , _etype_ , _* args_, _** kw_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Style.element_create "Link to this definition")

Create a new element in the current theme, of the given _etype_ which is expected to be either “image”, “from” or “vsapi”. The latter is only available in Tk 8.6 on Windows.
If “image” is used, _args_ should contain the default image name followed by statespec/value pairs (this is the imagespec), and _kw_ may have the following options:

border=padding

padding is a list of up to four integers, specifying the left, top, right, and bottom borders, respectively.

height=height

Specifies a minimum height for the element. If less than zero, the base image’s height is used as a default.

padding=padding

Specifies the element’s interior padding. Defaults to border’s value if not specified.

sticky=spec

Specifies how the image is placed within the final parcel. spec contains zero or more characters “n”, “s”, “w”, or “e”.

width=width

Specifies a minimum width for the element. If less than zero, the base image’s width is used as a default.
Example:
Copy```
img1 = tkinter.PhotoImage(master=root, file='button.png')
img1 = tkinter.PhotoImage(master=root, file='button-pressed.png')
img1 = tkinter.PhotoImage(master=root, file='button-active.png')
style = ttk.Style(root)
style.element_create('Button.button', 'image',
                     img1, ('pressed', img2), ('active', img3),
                     border=(2, 4), sticky='we')

```

If “from” is used as the value of _etype_ , `element_create()` will clone an existing element. _args_ is expected to contain a themename, from which the element will be cloned, and optionally an element to clone from. If this element to clone from is not specified, an empty element will be used. _kw_ is discarded.
Example:
Copy```
style = ttk.Style(root)
style.element_create('plain.background', 'from', 'default')

```

If “vsapi” is used as the value of _etype_ , `element_create()` will create a new element in the current theme whose visual appearance is drawn using the Microsoft Visual Styles API which is responsible for the themed styles on Windows XP and Vista. _args_ is expected to contain the Visual Styles class and part as given in the Microsoft documentation followed by an optional sequence of tuples of ttk states and the corresponding Visual Styles API state value. _kw_ may have the following options:

padding=padding

Specify the element’s interior padding. _padding_ is a list of up to four integers specifying the left, top, right and bottom padding quantities respectively. If fewer than four elements are specified, bottom defaults to top, right defaults to left, and top defaults to left. In other words, a list of three numbers specify the left, vertical, and right padding; a list of two numbers specify the horizontal and the vertical padding; a single number specifies the same padding all the way around the widget. This option may not be mixed with any other options.

margins=padding

Specifies the elements exterior padding. _padding_ is a list of up to four integers specifying the left, top, right and bottom padding quantities respectively. This option may not be mixed with any other options.

width=width

Specifies the width for the element. If this option is set then the Visual Styles API will not be queried for the recommended size or the part. If this option is set then _height_ should also be set. The _width_ and _height_ options cannot be mixed with the _padding_ or _margins_ options.

height=height

Specifies the height of the element. See the comments for _width_.
Example:
Copy```
style = ttk.Style(root)
style.element_create('pin', 'vsapi', 'EXPLORERBAR', 3, [
                     ('pressed', '!selected', 3),
                     ('active', '!selected', 2),
                     ('pressed', 'selected', 6),
                     ('active', 'selected', 5),
                     ('selected', 4),
                     ('', 1)])
style.layout('Explorer.Pin',
             [('Explorer.Pin.pin', {'sticky': 'news'})])
pin = ttk.Checkbutton(style='Explorer.Pin')
pin.pack(expand=True, fill='both')

```

Changed in version 3.13: Added support of the “vsapi” element factory.

element_names()[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Style.element_names "Link to this definition")

Returns the list of elements defined in the current theme.

element_options(_elementname_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Style.element_options "Link to this definition")

Returns the list of _elementname_ ’s options.

theme_create(_themename_ , _parent =None_, _settings =None_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Style.theme_create "Link to this definition")

Create a new theme.
It is an error if _themename_ already exists. If _parent_ is specified, the new theme will inherit styles, elements and layouts from the parent theme. If _settings_ are present they are expected to have the same syntax used for [`theme_settings()`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Style.theme_settings "tkinter.ttk.Style.theme_settings").

theme_settings(_themename_ , _settings_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Style.theme_settings "Link to this definition")

Temporarily sets the current theme to _themename_ , apply specified _settings_ and then restore the previous theme.
Each key in _settings_ is a style and each value may contain the keys ‘configure’, ‘map’, ‘layout’ and ‘element create’ and they are expected to have the same format as specified by the methods [`Style.configure()`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Style.configure "tkinter.ttk.Style.configure"), [`Style.map()`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Style.map "tkinter.ttk.Style.map"), [`Style.layout()`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Style.layout "tkinter.ttk.Style.layout") and [`Style.element_create()`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Style.element_create "tkinter.ttk.Style.element_create") respectively.
As an example, let’s change the Combobox for the default theme a bit:
Copy```
from tkinter import ttk
import tkinter

root = tkinter.Tk()

style = ttk.Style()
style.theme_settings("default", {
   "TCombobox": {
       "configure": {"padding": 5},
       "map": {
           "background": [("active", "green2"),
                          ("!disabled", "green4")],
           "fieldbackground": [("!disabled", "green3")],
           "foreground": [("focus", "OliveDrab1"),
                          ("!disabled", "OliveDrab2")]
       }
   }
})

combo = ttk.Combobox().pack()

root.mainloop()

```


theme_names()[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Style.theme_names "Link to this definition")

Returns a list of all known themes.

theme_use(_themename =None_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Style.theme_use "Link to this definition")

If _themename_ is not given, returns the theme in use. Otherwise, sets the current theme to _themename_ , refreshes all widgets and emits a <<ThemeChanged>> event.
### Layouts[¶](https://docs.python.org/3/library/tkinter.ttk.html#layouts "Link to this heading")
A layout can be just `None`, if it takes no options, or a dict of options specifying how to arrange the element. The layout mechanism uses a simplified version of the pack geometry manager: given an initial cavity, each element is allocated a parcel.
The valid options/values are:

_side_ : whichside

Specifies which side of the cavity to place the element; one of top, right, bottom or left. If omitted, the element occupies the entire cavity.

_sticky_ : nswe

Specifies where the element is placed inside its allocated parcel.

_unit_ : 0 or 1

If set to 1, causes the element and all of its descendants to be treated as a single element for the purposes of [`Widget.identify()`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Widget.identify "tkinter.ttk.Widget.identify") et al. It’s used for things like scrollbar thumbs with grips.

_children_ : [sublayout… ]

Specifies a list of elements to place inside the element. Each element is a tuple (or other sequence type) where the first item is the layout name, and the other is a [Layout](https://docs.python.org/3/library/tkinter.ttk.html#layouts).
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


«
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


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
