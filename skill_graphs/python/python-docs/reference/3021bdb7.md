## Treeview[¶](https://docs.python.org/3/library/tkinter.ttk.html#treeview "Link to this heading")
The `ttk.Treeview` widget displays a hierarchical collection of items. Each item has a textual label, an optional image, and an optional list of data values. The data values are displayed in successive columns after the tree label.
The order in which data values are displayed may be controlled by setting the widget option `displaycolumns`. The tree widget can also display column headings. Columns may be accessed by number or symbolic names listed in the widget option columns. See [Column Identifiers](https://docs.python.org/3/library/tkinter.ttk.html#column-identifiers).
Each item is identified by a unique name. The widget will generate item IDs if they are not supplied by the caller. There is a distinguished root item, named `{}`. The root item itself is not displayed; its children appear at the top level of the hierarchy.
Each item also has a list of tags, which can be used to associate event bindings with individual items and control the appearance of the item.
The Treeview widget supports horizontal and vertical scrolling, according to the options described in [Scrollable Widget Options](https://docs.python.org/3/library/tkinter.ttk.html#scrollable-widget-options) and the methods [`Treeview.xview()`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.xview "tkinter.ttk.Treeview.xview") and [`Treeview.yview()`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.yview "tkinter.ttk.Treeview.yview").
### Options[¶](https://docs.python.org/3/library/tkinter.ttk.html#id7 "Link to this heading")
This widget accepts the following specific options:
Option | Description
---|---
columns | A list of column identifiers, specifying the number of columns and their names.
displaycolumns | A list of column identifiers (either symbolic or integer indices) specifying which data columns are displayed and the order in which they appear, or the string “#all”.
height | Specifies the number of rows which should be visible. Note: the requested width is determined from the sum of the column widths.
padding | Specifies the internal padding for the widget. The padding is a list of up to four length specifications.
selectmode |  Controls how the built-in class bindings manage the selection. One of “extended”, “browse” or “none”. If set to “extended” (the default), multiple items may be selected. If “browse”, only a single item will be selected at a time. If “none”, the selection will not be changed. Note that the application code and tag bindings can set the selection however they wish, regardless of the value of this option.
show |  A list containing zero or more of the following values, specifying which elements of the tree to display.
  * tree: display tree labels in column #0.
  * headings: display the heading row.

The default is “tree headings”, i.e., show all elements. **Note** : Column #0 always refers to the tree column, even if show=”tree” is not specified.
### Item Options[¶](https://docs.python.org/3/library/tkinter.ttk.html#item-options "Link to this heading")
The following item options may be specified for items in the insert and item widget commands.
Option | Description
---|---
text | The textual label to display for the item.
image | A Tk Image, displayed to the left of the label.
values |  The list of values associated with the item. Each item should have the same number of values as the widget option columns. If there are fewer values than columns, the remaining values are assumed empty. If there are more values than columns, the extra values are ignored.
open | `True`/`False` value indicating whether the item’s children should be displayed or hidden.
tags | A list of tags associated with this item.
### Tag Options[¶](https://docs.python.org/3/library/tkinter.ttk.html#tag-options "Link to this heading")
The following options may be specified on tags:
Option | Description
---|---
foreground | Specifies the text foreground color.
background | Specifies the cell or item background color.
font | Specifies the font to use when drawing text.
image | Specifies the item image, in case the item’s image option is empty.
### Column Identifiers[¶](https://docs.python.org/3/library/tkinter.ttk.html#column-identifiers "Link to this heading")
Column identifiers take any of the following forms:
  * A symbolic name from the list of columns option.
  * An integer n, specifying the nth data column.
  * A string of the form #n, where n is an integer, specifying the nth display column.


Notes:
  * Item’s option values may be displayed in a different order than the order in which they are stored.
  * Column #0 always refers to the tree column, even if show=”tree” is not specified.


A data column number is an index into an item’s option values list; a display column number is the column number in the tree where the values are displayed. Tree labels are displayed in column #0. If option displaycolumns is not set, then data column n is displayed in column #n+1. Again, **column #0 always refers to the tree column**.
### Virtual Events[¶](https://docs.python.org/3/library/tkinter.ttk.html#id8 "Link to this heading")
The Treeview widget generates the following virtual events.
Event | Description
---|---
<<TreeviewSelect>> | Generated whenever the selection changes.
<<TreeviewOpen>> | Generated just before settings the focus item to open=True.
<<TreeviewClose>> | Generated just after setting the focus item to open=False.
The [`Treeview.focus()`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.focus "tkinter.ttk.Treeview.focus") and [`Treeview.selection()`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.selection "tkinter.ttk.Treeview.selection") methods can be used to determine the affected item or items.
### ttk.Treeview[¶](https://docs.python.org/3/library/tkinter.ttk.html#ttk-treeview "Link to this heading")

_class_ tkinter.ttk.Treeview[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview "Link to this definition")


bbox(_item_ , _column =None_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.bbox "Link to this definition")

Returns the bounding box (relative to the treeview widget’s window) of the specified _item_ in the form (x, y, width, height).
If _column_ is specified, returns the bounding box of that cell. If the _item_ is not visible (i.e., if it is a descendant of a closed item or is scrolled offscreen), returns an empty string.

get_children(_item =None_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.get_children "Link to this definition")

Returns the list of children belonging to _item_.
If _item_ is not specified, returns root children.

set_children(_item_ , _* newchildren_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.set_children "Link to this definition")

Replaces _item_ ’s child with _newchildren_.
Children present in _item_ that are not present in _newchildren_ are detached from the tree. No items in _newchildren_ may be an ancestor of _item_. Note that not specifying _newchildren_ results in detaching _item_ ’s children.

column(_column_ , _option =None_, _** kw_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.column "Link to this definition")

Query or modify the options for the specified _column_.
If _kw_ is not given, returns a dict of the column option values. If _option_ is specified then the value for that _option_ is returned. Otherwise, sets the options to the corresponding values.
The valid options/values are:

_id_

Returns the column name. This is a read-only option.

_anchor_ : One of the standard Tk anchor values.

Specifies how the text in this column should be aligned with respect to the cell.

_minwidth_ : width

The minimum width of the column in pixels. The treeview widget will not make the column any smaller than specified by this option when the widget is resized or the user drags a column.

_stretch_ : `True`/`False`

Specifies whether the column’s width should be adjusted when the widget is resized.

_width_ : width

The width of the column in pixels.
To configure the tree column, call this with column = “#0”

delete(_* items_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.delete "Link to this definition")

Delete all specified _items_ and all their descendants.
The root item may not be deleted.

detach(_* items_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.detach "Link to this definition")

Unlinks all of the specified _items_ from the tree.
The items and all of their descendants are still present, and may be reinserted at another point in the tree, but will not be displayed.
The root item may not be detached.

exists(_item_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.exists "Link to this definition")

Returns `True` if the specified _item_ is present in the tree.

focus(_item =None_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.focus "Link to this definition")

If _item_ is specified, sets the focus item to _item_. Otherwise, returns the current focus item, or ‘’ if there is none.

heading(_column_ , _option =None_, _** kw_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.heading "Link to this definition")

Query or modify the heading options for the specified _column_.
If _kw_ is not given, returns a dict of the heading option values. If _option_ is specified then the value for that _option_ is returned. Otherwise, sets the options to the corresponding values.
The valid options/values are:

_text_ : text

The text to display in the column heading.

_image_ : imageName

Specifies an image to display to the right of the column heading.

_anchor_ : anchor

Specifies how the heading text should be aligned. One of the standard Tk anchor values.

_command_ : callback

A callback to be invoked when the heading label is pressed.
To configure the tree column heading, call this with column = “#0”.

identify(_component_ , _x_ , _y_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.identify "Link to this definition")

Returns a description of the specified _component_ under the point given by _x_ and _y_ , or the empty string if no such _component_ is present at that position.

identify_row(_y_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.identify_row "Link to this definition")

Returns the item ID of the item at position _y_.

identify_column(_x_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.identify_column "Link to this definition")

Returns the data column identifier of the cell at position _x_.
The tree column has ID #0.

identify_region(_x_ , _y_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.identify_region "Link to this definition")

Returns one of:
region | meaning
---|---
heading | Tree heading area.
separator | Space between two columns headings.
tree | The tree area.
cell | A data cell.
Availability: Tk 8.6.

identify_element(_x_ , _y_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.identify_element "Link to this definition")

Returns the element at position _x_ , _y_.
Availability: Tk 8.6.

index(_item_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.index "Link to this definition")

Returns the integer index of _item_ within its parent’s list of children.

insert(_parent_ , _index_ , _iid =None_, _** kw_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.insert "Link to this definition")

Creates a new item and returns the item identifier of the newly created item.
_parent_ is the item ID of the parent item, or the empty string to create a new top-level item. _index_ is an integer, or the value “end”, specifying where in the list of parent’s children to insert the new item. If _index_ is less than or equal to zero, the new node is inserted at the beginning; if _index_ is greater than or equal to the current number of children, it is inserted at the end. If _iid_ is specified, it is used as the item identifier; _iid_ must not already exist in the tree. Otherwise, a new unique identifier is generated.
See [Item Options](https://docs.python.org/3/library/tkinter.ttk.html#item-options) for the list of available options.

item(_item_ , _option =None_, _** kw_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.item "Link to this definition")

Query or modify the options for the specified _item_.
If no options are given, a dict with options/values for the item is returned. If _option_ is specified then the value for that option is returned. Otherwise, sets the options to the corresponding values as given by _kw_.

move(_item_ , _parent_ , _index_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.move "Link to this definition")

Moves _item_ to position _index_ in _parent_ ’s list of children.
It is illegal to move an item under one of its descendants. If _index_ is less than or equal to zero, _item_ is moved to the beginning; if greater than or equal to the number of children, it is moved to the end. If _item_ was detached it is reattached.

next(_item_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.next "Link to this definition")

Returns the identifier of _item_ ’s next sibling, or ‘’ if _item_ is the last child of its parent.

parent(_item_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.parent "Link to this definition")

Returns the ID of the parent of _item_ , or ‘’ if _item_ is at the top level of the hierarchy.

prev(_item_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.prev "Link to this definition")

Returns the identifier of _item_ ’s previous sibling, or ‘’ if _item_ is the first child of its parent.

reattach(_item_ , _parent_ , _index_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.reattach "Link to this definition")

An alias for [`Treeview.move()`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.move "tkinter.ttk.Treeview.move").

see(_item_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.see "Link to this definition")

Ensure that _item_ is visible.
Sets all of _item_ ’s ancestors open option to `True`, and scrolls the widget if necessary so that _item_ is within the visible portion of the tree.

selection()[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.selection "Link to this definition")

Returns a tuple of selected items.
Changed in version 3.8: `selection()` no longer takes arguments. For changing the selection state use the following selection methods.

selection_set(_* items_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.selection_set "Link to this definition")

_items_ becomes the new selection.
Changed in version 3.6: _items_ can be passed as separate arguments, not just as a single tuple.

selection_add(_* items_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.selection_add "Link to this definition")

Add _items_ to the selection.
Changed in version 3.6: _items_ can be passed as separate arguments, not just as a single tuple.

selection_remove(_* items_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.selection_remove "Link to this definition")

Remove _items_ from the selection.
Changed in version 3.6: _items_ can be passed as separate arguments, not just as a single tuple.

selection_toggle(_* items_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.selection_toggle "Link to this definition")

Toggle the selection state of each item in _items_.
Changed in version 3.6: _items_ can be passed as separate arguments, not just as a single tuple.

set(_item_ , _column =None_, _value =None_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.set "Link to this definition")

With one argument, returns a dictionary of column/value pairs for the specified _item_. With two arguments, returns the current value of the specified _column_. With three arguments, sets the value of given _column_ in given _item_ to the specified _value_.

tag_bind(_tagname_ , _sequence =None_, _callback =None_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.tag_bind "Link to this definition")

Bind a callback for the given event _sequence_ to the tag _tagname_. When an event is delivered to an item, the callbacks for each of the item’s tags option are called.

tag_configure(_tagname_ , _option =None_, _** kw_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.tag_configure "Link to this definition")

Query or modify the options for the specified _tagname_.
If _kw_ is not given, returns a dict of the option settings for _tagname_. If _option_ is specified, returns the value for that _option_ for the specified _tagname_. Otherwise, sets the options to the corresponding values for the given _tagname_.

tag_has(_tagname_ , _item =None_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.tag_has "Link to this definition")

If _item_ is specified, returns 1 or 0 depending on whether the specified _item_ has the given _tagname_. Otherwise, returns a list of all items that have the specified tag.
Availability: Tk 8.6

xview(_* args_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.xview "Link to this definition")

Query or modify horizontal position of the treeview.

yview(_* args_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.yview "Link to this definition")

Query or modify vertical position of the treeview.
