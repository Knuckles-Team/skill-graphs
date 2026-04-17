## Notebook[¶](https://docs.python.org/3/library/tkinter.ttk.html#notebook "Link to this heading")
Ttk Notebook widget manages a collection of windows and displays a single one at a time. Each child window is associated with a tab, which the user may select to change the currently displayed window.
### Options[¶](https://docs.python.org/3/library/tkinter.ttk.html#id3 "Link to this heading")
This widget accepts the following specific options:
Option | Description
---|---
height | If present and greater than zero, specifies the desired height of the pane area (not including internal padding or tabs). Otherwise, the maximum height of all panes is used.
padding | Specifies the amount of extra space to add around the outside of the notebook. The padding is a list up to four length specifications left top right bottom. If fewer than four elements are specified, bottom defaults to top, right defaults to left, and top defaults to left.
width | If present and greater than zero, specified the desired width of the pane area (not including internal padding). Otherwise, the maximum width of all panes is used.
### Tab Options[¶](https://docs.python.org/3/library/tkinter.ttk.html#tab-options "Link to this heading")
There are also specific options for tabs:
Option | Description
---|---
state | Either “normal”, “disabled” or “hidden”. If “disabled”, then the tab is not selectable. If “hidden”, then the tab is not shown.
sticky | Specifies how the child window is positioned within the pane area. Value is a string containing zero or more of the characters “n”, “s”, “e” or “w”. Each letter refers to a side (north, south, east or west) that the child window will stick to, as per the `grid()` geometry manager.
padding | Specifies the amount of extra space to add between the notebook and this pane. Syntax is the same as for the option padding used by this widget.
text | Specifies a text to be displayed in the tab.
image | Specifies an image to display in the tab. See the option image described in [`Widget`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Widget "tkinter.ttk.Widget").
compound | Specifies how to display the image relative to the text, in the case both options text and image are present. See [Label Options](https://docs.python.org/3/library/tkinter.ttk.html#label-options) for legal values.
underline | Specifies the index (0-based) of a character to underline in the text string. The underlined character is used for mnemonic activation if [`Notebook.enable_traversal()`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Notebook.enable_traversal "tkinter.ttk.Notebook.enable_traversal") is called.
### Tab Identifiers[¶](https://docs.python.org/3/library/tkinter.ttk.html#tab-identifiers "Link to this heading")
The tab_id present in several methods of `ttk.Notebook` may take any of the following forms:
  * An integer between zero and the number of tabs
  * The name of a child window
  * A positional specification of the form “@x,y”, which identifies the tab
  * The literal string “current”, which identifies the currently selected tab
  * The literal string “end”, which returns the number of tabs (only valid for [`Notebook.index()`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Notebook.index "tkinter.ttk.Notebook.index"))


### Virtual Events[¶](https://docs.python.org/3/library/tkinter.ttk.html#id4 "Link to this heading")
This widget generates a **< <NotebookTabChanged>>** virtual event after a new tab is selected.
### ttk.Notebook[¶](https://docs.python.org/3/library/tkinter.ttk.html#ttk-notebook "Link to this heading")

_class_ tkinter.ttk.Notebook[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Notebook "Link to this definition")


add(_child_ , _** kw_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Notebook.add "Link to this definition")

Adds a new tab to the notebook.
If window is currently managed by the notebook but hidden, it is restored to its previous position.
See [Tab Options](https://docs.python.org/3/library/tkinter.ttk.html#tab-options) for the list of available options.

forget(_tab_id_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Notebook.forget "Link to this definition")

Removes the tab specified by _tab_id_ , unmaps and unmanages the associated window.

hide(_tab_id_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Notebook.hide "Link to this definition")

Hides the tab specified by _tab_id_.
The tab will not be displayed, but the associated window remains managed by the notebook and its configuration remembered. Hidden tabs may be restored with the [`add()`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Notebook.add "tkinter.ttk.Notebook.add") command.

identify(_x_ , _y_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Notebook.identify "Link to this definition")

Returns the name of the tab element at position _x_ , _y_ , or the empty string if none.

index(_tab_id_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Notebook.index "Link to this definition")

Returns the numeric index of the tab specified by _tab_id_ , or the total number of tabs if _tab_id_ is the string “end”.

insert(_pos_ , _child_ , _** kw_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Notebook.insert "Link to this definition")

Inserts a pane at the specified position.
_pos_ is either the string “end”, an integer index, or the name of a managed child. If _child_ is already managed by the notebook, moves it to the specified position.
See [Tab Options](https://docs.python.org/3/library/tkinter.ttk.html#tab-options) for the list of available options.

select(_tab_id =None_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Notebook.select "Link to this definition")

Selects the specified _tab_id_.
The associated child window will be displayed, and the previously selected window (if different) is unmapped. If _tab_id_ is omitted, returns the widget name of the currently selected pane.

tab(_tab_id_ , _option =None_, _** kw_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Notebook.tab "Link to this definition")

Query or modify the options of the specific _tab_id_.
If _kw_ is not given, returns a dictionary of the tab option values. If _option_ is specified, returns the value of that _option_. Otherwise, sets the options to the corresponding values.

tabs()[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Notebook.tabs "Link to this definition")

Returns a list of windows managed by the notebook.

enable_traversal()[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Notebook.enable_traversal "Link to this definition")

Enable keyboard traversal for a toplevel window containing this notebook.
This will extend the bindings for the toplevel window containing the notebook as follows:
  * `Control`-`Tab`: selects the tab following the currently selected one.
  * `Shift`-`Control`-`Tab`: selects the tab preceding the currently selected one.
  * `Alt`-`K`: where _K_ is the mnemonic (underlined) character of any tab, will select that tab.


Multiple notebooks in a single toplevel may be enabled for traversal, including nested notebooks. However, notebook traversal only works properly if all panes have the notebook they are in as master.
