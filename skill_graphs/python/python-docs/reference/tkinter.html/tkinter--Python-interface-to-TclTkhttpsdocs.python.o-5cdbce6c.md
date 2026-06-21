#  `tkinter` — Python interface to Tcl/Tk[¶](https://docs.python.org/3/library/tkinter.html#module-tkinter "Link to this heading")
**Source code:**
* * *
The `tkinter` package (“Tk interface”) is the standard Python interface to the Tcl/Tk GUI toolkit. Both Tk and `tkinter` are available on most Unix platforms, including macOS, as well as on Windows systems.
Running `python -m tkinter` from the command line should open a window demonstrating a simple Tk interface, letting you know that `tkinter` is properly installed on your system, and also showing what version of Tcl/Tk is installed, so you can read the Tcl/Tk documentation specific to that version.
Tkinter supports a range of Tcl/Tk versions, built either with or without thread support. The official Python binary release bundles Tcl/Tk 8.6 threaded. See the source code for the [`_tkinter`](https://docs.python.org/3/library/tkinter.html#module-_tkinter "_tkinter: A binary module that contains the low-level interface to Tcl/Tk.") module for more information about supported versions.
Tkinter is not a thin wrapper, but adds a fair amount of its own logic to make the experience more pythonic. This documentation will concentrate on these additions and changes, and refer to the official Tcl/Tk documentation for details that are unchanged.
Note
Tcl/Tk 8.5 (2007) introduced a modern set of themed user interface components along with a new API to use them. Both old and new APIs are still available. Most documentation you will find online still uses the old API and can be woefully outdated.
This is an [optional module](https://docs.python.org/3/glossary.html#term-optional-module). If it is missing from your copy of CPython, look for documentation from your distributor (that is, whoever provided Python to you). If you are the distributor, see [Requirements for optional modules](https://docs.python.org/3/using/configure.html#optional-module-requirements).
See also
  *
Extensive tutorial on creating user interfaces with Tkinter. Explains key concepts, and illustrates recommended approaches using the modern API.
  *
Reference documentation for Tkinter 8.5 detailing available classes, methods, and options.


Tcl/Tk Resources:
  *
Comprehensive reference to each of the underlying Tcl/Tk commands used by Tkinter.
  *
Additional documentation, and links to Tcl/Tk core development.


Books:
  *
By Mark Roseman. (ISBN 978-1999149567)
  *
By Alan D. Moore. (ISBN 978-1788835886)
  *
By Mark Lutz; has excellent coverage of Tkinter. (ISBN 978-0596158101)
  *
By John Ousterhout, inventor of Tcl/Tk, and Ken Jones; does not cover Tkinter. (ISBN 978-0321336330)


## Architecture[¶](https://docs.python.org/3/library/tkinter.html#architecture "Link to this heading")
Tcl/Tk is not a single library but rather consists of a few distinct modules, each with separate functionality and its own official documentation. Python’s binary releases also ship an add-on module together with it.

Tcl

Tcl is a dynamic interpreted programming language, just like Python. Though it can be used on its own as a general-purpose programming language, it is most commonly embedded into C applications as a scripting engine or an interface to the Tk toolkit. The Tcl library has a C interface to create and manage one or more instances of a Tcl interpreter, run Tcl commands and scripts in those instances, and add custom commands implemented in either Tcl or C. Each interpreter has an event queue, and there are facilities to send events to it and process them. Unlike Python, Tcl’s execution model is designed around cooperative multitasking, and Tkinter bridges this difference (see [Threading model](https://docs.python.org/3/library/tkinter.html#threading-model) for details).

Tk

Tk is a [`Tk`](https://docs.python.org/3/library/tkinter.html#tkinter.Tk "tkinter.Tk") object embeds its own Tcl interpreter instance with Tk loaded into it. Tk’s widgets are very customizable, though at the cost of a dated appearance. Tk uses Tcl’s event queue to generate and process GUI events.

Ttk

Themed Tk (Ttk) is a newer family of Tk widgets that provide a much better appearance on different platforms than many of the classic Tk widgets. Ttk is distributed as part of Tk, starting with Tk version 8.5. Python bindings are provided in a separate module, [`tkinter.ttk`](https://docs.python.org/3/library/tkinter.ttk.html#module-tkinter.ttk "tkinter.ttk: Tk themed widget set").
Internally, Tk and Ttk use facilities of the underlying operating system, i.e., Xlib on Unix/X11, Cocoa on macOS, GDI on Windows.
When your Python application uses a class in Tkinter, e.g., to create a widget, the `tkinter` module first assembles a Tcl/Tk command string. It passes that Tcl command string to an internal [`_tkinter`](https://docs.python.org/3/library/tkinter.html#module-_tkinter "_tkinter: A binary module that contains the low-level interface to Tcl/Tk.") binary module, which then calls the Tcl interpreter to evaluate it. The Tcl interpreter will then call into the Tk and/or Ttk packages, which will in turn make calls to Xlib, Cocoa, or GDI.
## Tkinter Modules[¶](https://docs.python.org/3/library/tkinter.html#tkinter-modules "Link to this heading")
Support for Tkinter is spread across several modules. Most applications will need the main `tkinter` module, as well as the [`tkinter.ttk`](https://docs.python.org/3/library/tkinter.ttk.html#module-tkinter.ttk "tkinter.ttk: Tk themed widget set") module, which provides the modern themed widget set and API:
Copy```
from tkinter import *
from tkinter import ttk

```


_class_ tkinter.Tk(_screenName =None_, _baseName =None_, _className ='Tk'_, _useTk =True_, _sync =False_, _use =None_)[¶](https://docs.python.org/3/library/tkinter.html#tkinter.Tk "Link to this definition")

Construct a toplevel Tk widget, which is usually the main window of an application, and initialize a Tcl interpreter for this widget. Each instance has its own associated Tcl interpreter.
The `Tk` class is typically instantiated using all default values. However, the following keyword arguments are currently recognized:

_screenName_

When given (as a string), sets the `DISPLAY` environment variable. (X11 only)

_baseName_

Name of the profile file. By default, _baseName_ is derived from the program name (`sys.argv[0]`).

_className_

Name of the widget class. Used as a profile file and also as the name with which Tcl is invoked (_argv0_ in _interp_).

_useTk_

If `True`, initialize the Tk subsystem. The [`tkinter.Tcl()`](https://docs.python.org/3/library/tkinter.html#tkinter.Tcl "tkinter.Tcl") function sets this to `False`.

_sync_

If `True`, execute all X server commands synchronously, so that errors are reported immediately. Can be used for debugging. (X11 only)

_use_

Specifies the _id_ of the window in which to embed the application, instead of it being created as an independent toplevel window. _id_ must be specified in the same way as the value for the -use option for toplevel widgets (that is, it has a form like that returned by `winfo_id()`).
Note that on some platforms this will only work correctly if _id_ refers to a Tk frame or toplevel that has its -container option enabled.
`Tk` reads and interprets profile files, named `._className_.tcl`and`. _baseName_.tcl`, into the Tcl interpreter and calls[`exec()`](https://docs.python.org/3/library/functions.html#exec "exec") on the contents of `._className_.py`and`. _baseName_.py`. The path for the profile files is the`HOME` environment variable or, if that isn’t defined, then [`os.curdir`](https://docs.python.org/3/library/os.html#os.curdir "os.curdir").

tk[¶](https://docs.python.org/3/library/tkinter.html#tkinter.Tk.tk "Link to this definition")

The Tk application object created by instantiating `Tk`. This provides access to the Tcl interpreter. Each widget that is attached the same instance of `Tk` has the same value for its [`tk`](https://docs.python.org/3/library/tkinter.html#tkinter.Tk.tk "tkinter.Tk.tk") attribute.

master[¶](https://docs.python.org/3/library/tkinter.html#tkinter.Tk.master "Link to this definition")

The widget object that contains this widget. For `Tk`, the `master` is [`None`](https://docs.python.org/3/library/constants.html#None "None") because it is the main window. The terms _master_ and _parent_ are similar and sometimes used interchangeably as argument names; however, calling `winfo_parent()` returns a string of the widget name whereas `master` returns the object. _parent_ /_child_ reflects the tree-like relationship while _master_ (or _container_)/_content_ reflects the container structure.

children[¶](https://docs.python.org/3/library/tkinter.html#tkinter.Tk.children "Link to this definition")

The immediate descendants of this widget as a [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict") with the child widget names as the keys and the child instance objects as the values.

tkinter.Tcl(_screenName =None_, _baseName =None_, _className ='Tk'_, _useTk =False_)[¶](https://docs.python.org/3/library/tkinter.html#tkinter.Tcl "Link to this definition")

The `Tcl()` function is a factory function which creates an object much like that created by the [`Tk`](https://docs.python.org/3/library/tkinter.html#tkinter.Tk "tkinter.Tk") class, except that it does not initialize the Tk subsystem. This is most often useful when driving the Tcl interpreter in an environment where one doesn’t want to create extraneous toplevel windows, or where one cannot (such as Unix/Linux systems without an X server). An object created by the `Tcl()` object can have a Toplevel window created (and the Tk subsystem initialized) by calling its `loadtk()` method.
The modules that provide Tk support include:

`tkinter`

Main Tkinter module.

[`tkinter.colorchooser`](https://docs.python.org/3/library/tkinter.colorchooser.html#module-tkinter.colorchooser "tkinter.colorchooser: Color choosing dialog")

Dialog to let the user choose a color.

[`tkinter.commondialog`](https://docs.python.org/3/library/dialog.html#module-tkinter.commondialog "tkinter.commondialog: Tkinter base class for dialogs")

Base class for the dialogs defined in the other modules listed here.

[`tkinter.filedialog`](https://docs.python.org/3/library/dialog.html#module-tkinter.filedialog "tkinter.filedialog: Dialog classes for file selection")

Common dialogs to allow the user to specify a file to open or save.

[`tkinter.font`](https://docs.python.org/3/library/tkinter.font.html#module-tkinter.font "tkinter.font: Tkinter font-wrapping class")

Utilities to help work with fonts.

[`tkinter.messagebox`](https://docs.python.org/3/library/tkinter.messagebox.html#module-tkinter.messagebox "tkinter.messagebox: Various types of alert dialogs")

Access to standard Tk dialog boxes.

[`tkinter.scrolledtext`](https://docs.python.org/3/library/tkinter.scrolledtext.html#module-tkinter.scrolledtext "tkinter.scrolledtext: Text widget with a vertical scroll bar.")

Text widget with a vertical scroll bar built in.

[`tkinter.simpledialog`](https://docs.python.org/3/library/dialog.html#module-tkinter.simpledialog "tkinter.simpledialog: Simple dialog windows")

Basic dialogs and convenience functions.

[`tkinter.ttk`](https://docs.python.org/3/library/tkinter.ttk.html#module-tkinter.ttk "tkinter.ttk: Tk themed widget set")

Themed widget set introduced in Tk 8.5, providing modern alternatives for many of the classic widgets in the main `tkinter` module.
Additional modules:

[`_tkinter`](https://docs.python.org/3/library/tkinter.html#module-_tkinter "_tkinter: A binary module that contains the low-level interface to Tcl/Tk.")

A binary module that contains the low-level interface to Tcl/Tk. It is automatically imported by the main `tkinter` module, and should never be used directly by application programmers. It is usually a shared library (or DLL), but might in some cases be statically linked with the Python interpreter.

[`idlelib`](https://docs.python.org/3/library/idle.html#module-idlelib "idlelib: Implementation package for the IDLE shell/editor.")

Python’s Integrated Development and Learning Environment (IDLE). Based on `tkinter`.

`tkinter.constants`

Symbolic constants that can be used in place of strings when passing various parameters to Tkinter calls. Automatically imported by the main `tkinter` module.

[`tkinter.dnd`](https://docs.python.org/3/library/tkinter.dnd.html#module-tkinter.dnd "tkinter.dnd: Tkinter drag-and-drop interface")

(experimental) Drag-and-drop support for `tkinter`. This will become deprecated when it is replaced with the Tk DND.

[`turtle`](https://docs.python.org/3/library/turtle.html#module-turtle "turtle: An educational framework for simple graphics applications")

Turtle graphics in a Tk window.
## Tkinter Life Preserver[¶](https://docs.python.org/3/library/tkinter.html#tkinter-life-preserver "Link to this heading")
This section is not designed to be an exhaustive tutorial on either Tk or Tkinter. For that, refer to one of the external resources noted earlier. Instead, this section provides a very quick orientation to what a Tkinter application looks like, identifies foundational Tk concepts, and explains how the Tkinter wrapper is structured.
The remainder of this section will help you to identify the classes, methods, and options you’ll need in your Tkinter application, and where to find more detailed documentation on them, including in the official Tcl/Tk reference manual.
### A Hello World Program[¶](https://docs.python.org/3/library/tkinter.html#a-hello-world-program "Link to this heading")
We’ll start by walking through a “Hello World” application in Tkinter. This isn’t the smallest one we could write, but has enough to illustrate some key concepts you’ll need to know.
Copy```
from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()

```

After the imports, the next line creates an instance of the `Tk` class, which initializes Tk and creates its associated Tcl interpreter. It also creates a toplevel window, known as the root window, which serves as the main window of the application.
The following line creates a frame widget, which in this case will contain a label and a button we’ll create next. The frame is fit inside the root window.
The next line creates a label widget holding a static text string. The `grid()` method is used to specify the relative layout (position) of the label within its containing frame widget, similar to how tables in HTML work.
A button widget is then created, and placed to the right of the label. When pressed, it will call the `destroy()` method of the root window.
Finally, the `mainloop()` method puts everything on the display, and responds to user input until the program terminates.
### Important Tk Concepts[¶](https://docs.python.org/3/library/tkinter.html#important-tk-concepts "Link to this heading")
Even this simple program illustrates the following key Tk concepts:

widgets

A Tkinter user interface is made up of individual _widgets_. Each widget is represented as a Python object, instantiated from classes like `ttk.Frame`, `ttk.Label`, and `ttk.Button`.

widget hierarchy

Widgets are arranged in a _hierarchy_. The label and button were contained within a frame, which in turn was contained within the root window. When creating each _child_ widget, its _parent_ widget is passed as the first argument to the widget constructor.

configuration options

Widgets have _configuration options_ , which modify their appearance and behavior, such as the text to display in a label or button. Different classes of widgets will have different sets of options.

geometry management

Widgets aren’t automatically added to the user interface when they are created. A _geometry manager_ like `grid` controls where in the user interface they are placed.

event loop

Tkinter reacts to user input, changes from your program, and even refreshes the display only when actively running an _event loop_. If your program isn’t running the event loop, your user interface won’t update.
### Understanding How Tkinter Wraps Tcl/Tk[¶](https://docs.python.org/3/library/tkinter.html#understanding-how-tkinter-wraps-tcl-tk "Link to this heading")
When your application uses Tkinter’s classes and methods, internally Tkinter is assembling strings representing Tcl/Tk commands, and executing those commands in the Tcl interpreter attached to your application’s `Tk` instance.
Whether it’s trying to navigate reference documentation, trying to find the right method or option, adapting some existing code, or debugging your Tkinter application, there are times that it will be useful to understand what those underlying Tcl/Tk commands look like.
To illustrate, here is the Tcl/Tk equivalent of the main part of the Tkinter script above.
Copy```
ttk::frame .frm -padding 10
grid .frm
grid [ttk::label .frm.lbl -text "Hello World!"] -column 0 -row 0
grid [ttk::button .frm.btn -text "Quit" -command "destroy ."] -column 1 -row 0

```

Tcl’s syntax is similar to many shell languages, where the first word is the command to be executed, with arguments to that command following it, separated by spaces. Without getting into too many details, notice the following:
  * The commands used to create widgets (like `ttk::frame`) correspond to widget classes in Tkinter.
  * Tcl widget options (like `-text`) correspond to keyword arguments in Tkinter.
  * Widgets are referred to by a _pathname_ in Tcl (like `.frm.btn`), whereas Tkinter doesn’t use names but object references.
  * A widget’s place in the widget hierarchy is encoded in its (hierarchical) pathname, which uses a `.` (dot) as a path separator. The pathname for the root window is just `.` (dot). In Tkinter, the hierarchy is defined not by pathname but by specifying the parent widget when creating each child widget.
  * Operations which are implemented as separate _commands_ in Tcl (like `grid` or `destroy`) are represented as _methods_ on Tkinter widget objects. As you’ll see shortly, at other times Tcl uses what appear to be method calls on widget objects, which more closely mirror what is used in Tkinter.


### How do I…? What option does…?[¶](https://docs.python.org/3/library/tkinter.html#how-do-i-what-option-does "Link to this heading")
If you’re not sure how to do something in Tkinter, and you can’t immediately find it in the tutorial or reference documentation you’re using, there are a few strategies that can be helpful.
First, remember that the details of how individual widgets work may vary across different versions of both Tkinter and Tcl/Tk. If you’re searching documentation, make sure it corresponds to the Python and Tcl/Tk versions installed on your system.
When searching for how to use an API, it helps to know the exact name of the class, option, or method that you’re using. Introspection, either in an interactive Python shell or with [`print()`](https://docs.python.org/3/library/functions.html#print "print"), can help you identify what you need.
To find out what configuration options are available on any widget, call its `configure()` method, which returns a dictionary containing a variety of information about each object, including its default and current values. Use `keys()` to get just the names of each option.
Copy```
btn = ttk.Button(frm, ...)
print(btn.configure().keys())

```

As most widgets have many configuration options in common, it can be useful to find out which are specific to a particular widget class. Comparing the list of options to that of a simpler widget, like a frame, is one way to do that.
Copy```
print(set(btn.configure().keys()) - set(frm.configure().keys()))

```

Similarly, you can find the available methods for a widget object using the standard [`dir()`](https://docs.python.org/3/library/functions.html#dir "dir") function. If you try it, you’ll see there are over 200 common widget methods, so again identifying those specific to a widget class is helpful.
Copy```
print(dir(btn))
print(set(dir(btn)) - set(dir(frm)))

```

### Navigating the Tcl/Tk Reference Manual[¶](https://docs.python.org/3/library/tkinter.html#navigating-the-tcl-tk-reference-manual "Link to this heading")
As noted, the official
While all operations in Tkinter are implemented as method calls on widget objects, you’ve seen that many Tcl/Tk operations appear as commands that take a widget pathname as its first parameter, followed by optional parameters, e.g.
Copy```
destroy .
grid .frm.btn -column 0 -row 0

```

Others, however, look more like methods called on a widget object (in fact, when you create a widget in Tcl/Tk, it creates a Tcl command with the name of the widget pathname, with the first parameter to that command being the name of a method to call).
Copy```
.frm.btn invoke
.frm.lbl configure -text "Goodbye"

```

In the official Tcl/Tk reference documentation, you’ll find most operations that look like method calls on the man page for a specific widget (e.g., you’ll find the `invoke()` method on the
You’ll find many common options and methods in the
You’ll also find that many Tkinter methods have compound names, e.g., `winfo_x()`, `winfo_height()`, `winfo_viewable()`. You’d find documentation for all of these in the
Note
Somewhat confusingly, there are also methods on all Tkinter widgets that don’t actually operate on the widget, but operate at a global scope, independent of any widget. Examples are methods for accessing the clipboard or the system bell. (They happen to be implemented as methods in the base `Widget` class that all Tkinter widgets inherit from).
## Threading model[¶](https://docs.python.org/3/library/tkinter.html#threading-model "Link to this heading")
Python and Tcl/Tk have very different threading models, which `tkinter` tries to bridge. If you use threads, you may need to be aware of this.
A Python interpreter may have many threads associated with it. In Tcl, multiple threads can be created, but each thread has a separate Tcl interpreter instance associated with it. Threads can also create more than one interpreter instance, though each interpreter instance can be used only by the one thread that created it.
Each `Tk` object created by `tkinter` contains a Tcl interpreter. It also keeps track of which thread created that interpreter. Calls to `tkinter` can be made from any Python thread. Internally, if a call comes from a thread other than the one that created the `Tk` object, an event is posted to the interpreter’s event queue, and when executed, the result is returned to the calling Python thread.
Tcl/Tk applications are normally event-driven, meaning that after initialization, the interpreter runs an event loop (i.e. `Tk.mainloop()`) and responds to events. Because it is single-threaded, event handlers must respond quickly, otherwise they will block other events from being processed. To avoid this, any long-running computations should not run in an event handler, but are either broken into smaller pieces using timers, or run in another thread. This is different from many GUI toolkits where the GUI runs in a completely separate thread from all application code including event handlers.
If the Tcl interpreter is not running the event loop and processing events, any `tkinter` calls made from threads other than the one running the Tcl interpreter will fail.
A number of special cases exist:
  * Tcl/Tk libraries can be built so they are not thread-aware. In this case, `tkinter` calls the library from the originating Python thread, even if this is different than the thread that created the Tcl interpreter. A global lock ensures only one call occurs at a time.
  * While `tkinter` allows you to create more than one instance of a `Tk` object (with its own interpreter), all interpreters that are part of the same thread share a common event queue, which gets ugly fast. In practice, don’t create more than one instance of `Tk` at a time. Otherwise, it’s best to create them in separate threads and ensure you’re running a thread-aware Tcl/Tk build.
  * Blocking event handlers are not the only way to prevent the Tcl interpreter from reentering the event loop. It is even possible to run multiple nested event loops or abandon the event loop entirely. If you’re doing anything tricky when it comes to events or threads, be aware of these possibilities.
  * There are a few select `tkinter` functions that presently work only when called from the thread that created the Tcl interpreter.


## Handy Reference[¶](https://docs.python.org/3/library/tkinter.html#handy-reference "Link to this heading")
### Setting Options[¶](https://docs.python.org/3/library/tkinter.html#setting-options "Link to this heading")
Options control things like the color and border width of a widget. Options can be set in three ways:

At object creation time, using keyword arguments

Copy```
fred = Button(self, fg="red", bg="blue")

```


After object creation, treating the option name like a dictionary index

Copy```
fred["fg"] = "red"
fred["bg"] = "blue"

```


Use the config() method to update multiple attrs subsequent to object creation

Copy```
fred.config(fg="red", bg="blue")

```

For a complete explanation of a given option and its behavior, see the Tk man pages for the widget in question.
Note that the man pages list “STANDARD OPTIONS” and “WIDGET SPECIFIC OPTIONS” for each widget. The former is a list of options that are common to many widgets, the latter are the options that are idiosyncratic to that particular widget. The Standard Options are documented on the
No distinction between standard and widget-specific options is made in this document. Some options don’t apply to some kinds of widgets. Whether a given widget responds to a particular option depends on the class of the widget; buttons have a `command` option, labels do not.
The options supported by a given widget are listed in that widget’s man page, or can be queried at runtime by calling the `config()` method without arguments, or by calling the `keys()` method on that widget. The return value of these calls is a dictionary whose key is the name of the option as a string (for example, `'relief'`) and whose values are 5-tuples.
Some options, like `bg` are synonyms for common options with long names (`bg` is shorthand for “background”). Passing the `config()` method the name of a shorthand option will return a 2-tuple, not 5-tuple. The 2-tuple passed back will contain the name of the synonym and the “real” option (such as `('bg', 'background')`).
Index | Meaning | Example
---|---|---
0 | option name | `'relief'`
1 | option name for database lookup | `'relief'`
2 | option class for database lookup | `'Relief'`
3 | default value | `'raised'`
4 | current value | `'groove'`
Example:
Copy```
>>> print(fred.config())
{'relief': ('relief', 'relief', 'Relief', 'raised', 'groove')}

```

Of course, the dictionary printed will include all the options available and their values. This is meant only as an example.
### The Packer[¶](https://docs.python.org/3/library/tkinter.html#the-packer "Link to this heading")
The packer is one of Tk’s geometry-management mechanisms. Geometry managers are used to specify the relative positioning of widgets within their container. In contrast to the more cumbersome _placer_ (which is used less commonly, and we do not cover here), the packer takes qualitative relationship specification - _above_ , _to the left of_ , _filling_ , etc - and works everything out to determine the exact placement coordinates for you.
The size of any container widget is determined by the size of the “content widgets” inside. The packer is used to control where content widgets appear inside the container into which they are packed. You can pack widgets into frames, and frames into other frames, in order to achieve the kind of layout you desire. Additionally, the arrangement is dynamically adjusted to accommodate incremental changes to the configuration, once it is packed.
Note that widgets do not appear until they have had their geometry specified with a geometry manager. It’s a common early mistake to leave out the geometry specification, and then be surprised when the widget is created but nothing appears. A widget will appear only after it has had, for example, the packer’s `pack()` method applied to it.
The pack() method can be called with keyword-option/value pairs that control where the widget is to appear within its container, and how it is to behave when the main application window is resized. Here are some examples:
Copy```
fred.pack()                     # defaults to side = "top"
fred.pack(side="left")
fred.pack(expand=1)

```

### Packer Options[¶](https://docs.python.org/3/library/tkinter.html#packer-options "Link to this heading")
For more extensive information on the packer and the options that it can take, see the man pages and page 183 of John Ousterhout’s book.

anchor

Anchor type. Denotes where the packer is to place each content in its parcel.

expand

Boolean, `0` or `1`.

fill

Legal values: `'x'`, `'y'`, `'both'`, `'none'`.

ipadx and ipady

A distance - designating internal padding on each side of the content.

padx and pady

A distance - designating external padding on each side of the content.

side

Legal values are: `'left'`, `'right'`, `'top'`, `'bottom'`.
### Coupling Widget Variables[¶](https://docs.python.org/3/library/tkinter.html#coupling-widget-variables "Link to this heading")
The current-value setting of some widgets (like text entry widgets) can be connected directly to application variables by using special options. These options are `variable`, `textvariable`, `onvalue`, `offvalue`, and `value`. This connection works both ways: if the variable changes for any reason, the widget it’s connected to will be updated to reflect the new value.
Unfortunately, in the current implementation of `tkinter` it is not possible to hand over an arbitrary Python variable to a widget through a `variable` or `textvariable` option. The only kinds of variables for which this works are variables that are subclassed from a class called Variable, defined in `tkinter`.
There are many useful subclasses of Variable already defined: `StringVar`, `IntVar`, `DoubleVar`, and `BooleanVar`. To read the current value of such a variable, call the `get()` method on it, and to change its value you call the `set()` method. If you follow this protocol, the widget will always track the value of the variable, with no further intervention on your part.
For example:
Copy```
import tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

        # Create the application variable.
        self.contents = tk.StringVar()
        # Set it to some value.
        self.contents.set("this is a variable")
        # Tell the entry widget to watch this variable.
        self.entrythingy["textvariable"] = self.contents

        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        self.entrythingy.bind('<Key-Return>',
                             self.print_contents)

    def print_contents(self, event):
        print("Hi. The current entry content is:",
              self.contents.get())

root = tk.Tk()
myapp = App(root)
myapp.mainloop()

```

### The Window Manager[¶](https://docs.python.org/3/library/tkinter.html#the-window-manager "Link to this heading")
In Tk, there is a utility command, `wm`, for interacting with the window manager. Options to the `wm` command allow you to control things like titles, placement, icon bitmaps, and the like. In `tkinter`, these commands have been implemented as methods on the `Wm` class. Toplevel widgets are subclassed from the `Wm` class, and so can call the `Wm` methods directly.
To get at the toplevel window that contains a given widget, you can often just refer to the widget’s `master`. Of course if the widget has been packed inside of a frame, the `master` won’t represent a toplevel window. To get at the toplevel window that contains an arbitrary widget, you can call the `_root()` method. This method begins with an underscore to denote the fact that this function is part of the implementation, and not an interface to Tk functionality.
Here are some examples of typical usage:
Copy```
import tkinter as tk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
