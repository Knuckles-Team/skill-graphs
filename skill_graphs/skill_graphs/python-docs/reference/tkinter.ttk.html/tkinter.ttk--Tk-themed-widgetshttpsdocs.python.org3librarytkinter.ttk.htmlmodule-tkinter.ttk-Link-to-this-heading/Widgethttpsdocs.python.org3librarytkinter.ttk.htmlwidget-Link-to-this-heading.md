## Widget[¶](https://docs.python.org/3/library/tkinter.ttk.html#widget "Link to this heading")
`ttk.Widget` defines standard options and methods supported by Tk themed widgets and is not supposed to be directly instantiated.
### Standard Options[¶](https://docs.python.org/3/library/tkinter.ttk.html#standard-options "Link to this heading")
All the `ttk` Widgets accept the following options:
Option | Description
---|---
class | Specifies the window class. The class is used when querying the option database for the window’s other options, to determine the default bindtags for the window, and to select the widget’s default layout and style. This option is read-only, and may only be specified when the window is created.
cursor | Specifies the mouse cursor to be used for the widget. If set to the empty string (the default), the cursor is inherited for the parent widget.
takefocus | Determines whether the window accepts the focus during keyboard traversal. 0, 1 or an empty string is returned. If 0 is returned, it means that the window should be skipped entirely during keyboard traversal. If 1, it means that the window should receive the input focus as long as it is viewable. And an empty string means that the traversal scripts make the decision about whether or not to focus on the window.
style | May be used to specify a custom widget style.
### Scrollable Widget Options[¶](https://docs.python.org/3/library/tkinter.ttk.html#scrollable-widget-options "Link to this heading")
The following options are supported by widgets that are controlled by a scrollbar.
Option | Description
---|---
xscrollcommand |  Used to communicate with horizontal scrollbars. When the view in the widget’s window change, the widget will generate a Tcl command based on the scrollcommand. Usually this option consists of the method `Scrollbar.set()` of some scrollbar. This will cause the scrollbar to be updated whenever the view in the window changes.
yscrollcommand | Used to communicate with vertical scrollbars. For some more information, see above.
### Label Options[¶](https://docs.python.org/3/library/tkinter.ttk.html#label-options "Link to this heading")
The following options are supported by labels, buttons and other button-like widgets.
Option | Description
---|---
text | Specifies a text string to be displayed inside the widget.
textvariable | Specifies a name whose value will be used in place of the text option resource.
underline | If set, specifies the index (0-based) of a character to underline in the text string. The underline character is used for mnemonic activation.
image | Specifies an image to display. This is a list of 1 or more elements. The first element is the default image name. The rest of the list if a sequence of statespec/value pairs as defined by [`Style.map()`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Style.map "tkinter.ttk.Style.map"), specifying different images to use when the widget is in a particular state or a combination of states. All images in the list should have the same size.
compound |  Specifies how to display the image relative to the text, in the case both text and images options are present. Valid values are:
  * text: display text only
  * image: display image only
  * top, bottom, left, right: display image above, below, left of, or right of the text, respectively.
  * none: the default. display the image if present, otherwise the text.


width | If greater than zero, specifies how much space, in character widths, to allocate for the text label, if less than zero, specifies a minimum width. If zero or unspecified, the natural width of the text label is used.
### Compatibility Options[¶](https://docs.python.org/3/library/tkinter.ttk.html#compatibility-options "Link to this heading")
Option | Description
---|---
state | May be set to “normal” or “disabled” to control the “disabled” state bit. This is a write-only option: setting it changes the widget state, but the [`Widget.state()`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Widget.state "tkinter.ttk.Widget.state") method does not affect this option.
### Widget States[¶](https://docs.python.org/3/library/tkinter.ttk.html#widget-states "Link to this heading")
The widget state is a bitmap of independent state flags.
Flag | Description
---|---
active | The mouse cursor is over the widget and pressing a mouse button will cause some action to occur
disabled | Widget is disabled under program control
focus | Widget has keyboard focus
pressed | Widget is being pressed
selected | “On”, “true”, or “current” for things like Checkbuttons and radiobuttons
background | Windows and Mac have a notion of an “active” or foreground window. The _background_ state is set for widgets in a background window, and cleared for those in the foreground window
readonly | Widget should not allow user modification
alternate | A widget-specific alternate display format
invalid | The widget’s value is invalid
A state specification is a sequence of state names, optionally prefixed with an exclamation point indicating that the bit is off.
### ttk.Widget[¶](https://docs.python.org/3/library/tkinter.ttk.html#ttk-widget "Link to this heading")
Besides the methods described below, the `ttk.Widget` supports the methods `tkinter.Widget.cget()` and `tkinter.Widget.configure()`.

_class_ tkinter.ttk.Widget[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Widget "Link to this definition")


identify(_x_ , _y_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Widget.identify "Link to this definition")

Returns the name of the element at position _x_ _y_ , or the empty string if the point does not lie within any element.
_x_ and _y_ are pixel coordinates relative to the widget.

instate(_statespec_ , _callback =None_, _* args_, _** kw_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Widget.instate "Link to this definition")

Test the widget’s state. If a callback is not specified, returns `True` if the widget state matches _statespec_ and `False` otherwise. If callback is specified then it is called with args if widget state matches _statespec_.

state(_statespec =None_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Widget.state "Link to this definition")

Modify or inquire widget state. If _statespec_ is specified, sets the widget state according to it and return a new _statespec_ indicating which flags were changed. If _statespec_ is not specified, returns the currently enabled state flags.
_statespec_ will usually be a list or a tuple.
