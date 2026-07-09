## Window Objects[¶](https://docs.python.org/3/library/curses.html#window-objects "Link to this heading")

_class_ curses.window[¶](https://docs.python.org/3/library/curses.html#curses.window "Link to this definition")

Window objects, as returned by [`initscr()`](https://docs.python.org/3/library/curses.html#curses.initscr "curses.initscr") and [`newwin()`](https://docs.python.org/3/library/curses.html#curses.newwin "curses.newwin") above, have the following methods and attributes:

window.addch(_ch_[, _attr_])[¶](https://docs.python.org/3/library/curses.html#curses.window.addch "Link to this definition")


window.addch(_y_ , _x_ , _ch_[, _attr_])

Paint character _ch_ at `(y, x)` with attributes _attr_ , overwriting any character previously painted at that location. By default, the character position and attributes are the current settings for the window object.
Note
Writing outside the window, subwindow, or pad raises a [`curses.error`](https://docs.python.org/3/library/curses.html#curses.error "curses.error"). Attempting to write to the lower right corner of a window, subwindow, or pad will cause an exception to be raised after the character is printed.

window.addnstr(_str_ , _n_[, _attr_])[¶](https://docs.python.org/3/library/curses.html#curses.window.addnstr "Link to this definition")


window.addnstr(_y_ , _x_ , _str_ , _n_[, _attr_])

Paint at most _n_ characters of the character string _str_ at `(y, x)` with attributes _attr_ , overwriting anything previously on the display.

window.addstr(_str_[, _attr_])[¶](https://docs.python.org/3/library/curses.html#curses.window.addstr "Link to this definition")


window.addstr(_y_ , _x_ , _str_[, _attr_])

Paint the character string _str_ at `(y, x)` with attributes _attr_ , overwriting anything previously on the display.
Note
  * Writing outside the window, subwindow, or pad raises [`curses.error`](https://docs.python.org/3/library/curses.html#curses.error "curses.error"). Attempting to write to the lower right corner of a window, subwindow, or pad will cause an exception to be raised after the string is printed.
  * A [bug in ncurses](https://bugs.python.org/issue35924), the backend for this Python module, can cause SegFaults when resizing windows. This is fixed in ncurses-6.1-20190511. If you are stuck with an earlier ncurses, you can avoid triggering this if you do not call [`addstr()`](https://docs.python.org/3/library/curses.html#curses.window.addstr "curses.window.addstr") with a _str_ that has embedded newlines. Instead, call `addstr()` separately for each line.



window.attroff(_attr_)[¶](https://docs.python.org/3/library/curses.html#curses.window.attroff "Link to this definition")

Remove attribute _attr_ from the “background” set applied to all writes to the current window.

window.attron(_attr_)[¶](https://docs.python.org/3/library/curses.html#curses.window.attron "Link to this definition")

Add attribute _attr_ to the “background” set applied to all writes to the current window.

window.attrset(_attr_)[¶](https://docs.python.org/3/library/curses.html#curses.window.attrset "Link to this definition")

Set the “background” set of attributes to _attr_. This set is initially `0` (no attributes).

window.bkgd(_ch_[, _attr_])[¶](https://docs.python.org/3/library/curses.html#curses.window.bkgd "Link to this definition")

Set the background property of the window to the character _ch_ , with attributes _attr_. The change is then applied to every character position in that window:
  * The attribute of every character in the window is changed to the new background attribute.
  * Wherever the former background character appears, it is changed to the new background character.



window.bkgdset(_ch_[, _attr_])[¶](https://docs.python.org/3/library/curses.html#curses.window.bkgdset "Link to this definition")

Set the window’s background. A window’s background consists of a character and any combination of attributes. The attribute part of the background is combined (OR’ed) with all non-blank characters that are written into the window. Both the character and attribute parts of the background are combined with the blank characters. The background becomes a property of the character and moves with the character through any scrolling and insert/delete line/character operations.

window.border([_ls_[, _rs_[, _ts_[, _bs_[, _tl_[, _tr_[, _bl_[, _br_]]]]]]]])[¶](https://docs.python.org/3/library/curses.html#curses.window.border "Link to this definition")

Draw a border around the edges of the window. Each parameter specifies the character to use for a specific part of the border; see the table below for more details.
Note
A `0` value for any parameter will cause the default character to be used for that parameter. Keyword parameters can _not_ be used. The defaults are listed in this table:
Parameter | Description | Default value
---|---|---
_ls_ | Left side | [`ACS_VLINE`](https://docs.python.org/3/library/curses.html#curses.ACS_VLINE "curses.ACS_VLINE")
_rs_ | Right side | [`ACS_VLINE`](https://docs.python.org/3/library/curses.html#curses.ACS_VLINE "curses.ACS_VLINE")
_ts_ | Top | [`ACS_HLINE`](https://docs.python.org/3/library/curses.html#curses.ACS_HLINE "curses.ACS_HLINE")
_bs_ | Bottom | [`ACS_HLINE`](https://docs.python.org/3/library/curses.html#curses.ACS_HLINE "curses.ACS_HLINE")
_tl_ | Upper-left corner | [`ACS_ULCORNER`](https://docs.python.org/3/library/curses.html#curses.ACS_ULCORNER "curses.ACS_ULCORNER")
_tr_ | Upper-right corner | [`ACS_URCORNER`](https://docs.python.org/3/library/curses.html#curses.ACS_URCORNER "curses.ACS_URCORNER")
_bl_ | Bottom-left corner | [`ACS_LLCORNER`](https://docs.python.org/3/library/curses.html#curses.ACS_LLCORNER "curses.ACS_LLCORNER")
_br_ | Bottom-right corner | [`ACS_LRCORNER`](https://docs.python.org/3/library/curses.html#curses.ACS_LRCORNER "curses.ACS_LRCORNER")

window.box([_vertch_ , _horch_])[¶](https://docs.python.org/3/library/curses.html#curses.window.box "Link to this definition")

Similar to [`border()`](https://docs.python.org/3/library/curses.html#curses.window.border "curses.window.border"), but both _ls_ and _rs_ are _vertch_ and both _ts_ and _bs_ are _horch_. The default corner characters are always used by this function.

window.chgat(_attr_)[¶](https://docs.python.org/3/library/curses.html#curses.window.chgat "Link to this definition")


window.chgat(_num_ , _attr_)


window.chgat(_y_ , _x_ , _attr_)


window.chgat(_y_ , _x_ , _num_ , _attr_)

Set the attributes of _num_ characters at the current cursor position, or at position `(y, x)` if supplied. If _num_ is not given or is `-1`, the attribute will be set on all the characters to the end of the line. This function moves cursor to position `(y, x)` if supplied. The changed line will be touched using the [`touchline()`](https://docs.python.org/3/library/curses.html#curses.window.touchline "curses.window.touchline") method so that the contents will be redisplayed by the next window refresh.

window.clear()[¶](https://docs.python.org/3/library/curses.html#curses.window.clear "Link to this definition")

Like [`erase()`](https://docs.python.org/3/library/curses.html#curses.window.erase "curses.window.erase"), but also cause the whole window to be repainted upon next call to [`refresh()`](https://docs.python.org/3/library/curses.html#curses.window.refresh "curses.window.refresh").

window.clearok(_flag_)[¶](https://docs.python.org/3/library/curses.html#curses.window.clearok "Link to this definition")

If _flag_ is `True`, the next call to [`refresh()`](https://docs.python.org/3/library/curses.html#curses.window.refresh "curses.window.refresh") will clear the window completely.

window.clrtobot()[¶](https://docs.python.org/3/library/curses.html#curses.window.clrtobot "Link to this definition")

Erase from cursor to the end of the window: all lines below the cursor are deleted, and then the equivalent of [`clrtoeol()`](https://docs.python.org/3/library/curses.html#curses.window.clrtoeol "curses.window.clrtoeol") is performed.

window.clrtoeol()[¶](https://docs.python.org/3/library/curses.html#curses.window.clrtoeol "Link to this definition")

Erase from cursor to the end of the line.

window.cursyncup()[¶](https://docs.python.org/3/library/curses.html#curses.window.cursyncup "Link to this definition")

Update the current cursor position of all the ancestors of the window to reflect the current cursor position of the window.

window.delch([_y_ , _x_])[¶](https://docs.python.org/3/library/curses.html#curses.window.delch "Link to this definition")

Delete any character at `(y, x)`.

window.deleteln()[¶](https://docs.python.org/3/library/curses.html#curses.window.deleteln "Link to this definition")

Delete the line under the cursor. All following lines are moved up by one line.

window.derwin(_begin_y_ , _begin_x_)[¶](https://docs.python.org/3/library/curses.html#curses.window.derwin "Link to this definition")


window.derwin(_nlines_ , _ncols_ , _begin_y_ , _begin_x_)

An abbreviation for “derive window”, `derwin()` is the same as calling [`subwin()`](https://docs.python.org/3/library/curses.html#curses.window.subwin "curses.window.subwin"), except that _begin_y_ and _begin_x_ are relative to the origin of the window, rather than relative to the entire screen. Return a window object for the derived window.

window.echochar(_ch_[, _attr_])[¶](https://docs.python.org/3/library/curses.html#curses.window.echochar "Link to this definition")

Add character _ch_ with attribute _attr_ , and immediately call [`refresh()`](https://docs.python.org/3/library/curses.html#curses.window.refresh "curses.window.refresh") on the window.

window.enclose(_y_ , _x_)[¶](https://docs.python.org/3/library/curses.html#curses.window.enclose "Link to this definition")

Test whether the given pair of screen-relative character-cell coordinates are enclosed by the given window, returning `True` or `False`. It is useful for determining what subset of the screen windows enclose the location of a mouse event.
Changed in version 3.10: Previously it returned `1` or `0` instead of `True` or `False`.

window.encoding[¶](https://docs.python.org/3/library/curses.html#curses.window.encoding "Link to this definition")

Encoding used to encode method arguments (Unicode strings and characters). The encoding attribute is inherited from the parent window when a subwindow is created, for example with [`window.subwin()`](https://docs.python.org/3/library/curses.html#curses.window.subwin "curses.window.subwin"). By default, current locale encoding is used (see [`locale.getencoding()`](https://docs.python.org/3/library/locale.html#locale.getencoding "locale.getencoding")).
Added in version 3.3.

window.erase()[¶](https://docs.python.org/3/library/curses.html#curses.window.erase "Link to this definition")

Clear the window.

window.getbegyx()[¶](https://docs.python.org/3/library/curses.html#curses.window.getbegyx "Link to this definition")

Return a tuple `(y, x)` of coordinates of upper-left corner.

window.getbkgd()[¶](https://docs.python.org/3/library/curses.html#curses.window.getbkgd "Link to this definition")

Return the given window’s current background character/attribute pair.

window.getch([_y_ , _x_])[¶](https://docs.python.org/3/library/curses.html#curses.window.getch "Link to this definition")

Get a character. Note that the integer returned does _not_ have to be in ASCII range: function keys, keypad keys and so on are represented by numbers higher than 255. In no-delay mode, return `-1` if there is no input, otherwise wait until a key is pressed.

window.get_wch([_y_ , _x_])[¶](https://docs.python.org/3/library/curses.html#curses.window.get_wch "Link to this definition")

Get a wide character. Return a character for most keys, or an integer for function keys, keypad keys, and other special keys. In no-delay mode, raise an exception if there is no input.
Added in version 3.3.

window.getkey([_y_ , _x_])[¶](https://docs.python.org/3/library/curses.html#curses.window.getkey "Link to this definition")

Get a character, returning a string instead of an integer, as [`getch()`](https://docs.python.org/3/library/curses.html#curses.window.getch "curses.window.getch") does. Function keys, keypad keys and other special keys return a multibyte string containing the key name. In no-delay mode, raise an exception if there is no input.

window.getmaxyx()[¶](https://docs.python.org/3/library/curses.html#curses.window.getmaxyx "Link to this definition")

Return a tuple `(y, x)` of the height and width of the window.

window.getparyx()[¶](https://docs.python.org/3/library/curses.html#curses.window.getparyx "Link to this definition")

Return the beginning coordinates of this window relative to its parent window as a tuple `(y, x)`. Return `(-1, -1)` if this window has no parent.

window.getstr()[¶](https://docs.python.org/3/library/curses.html#curses.window.getstr "Link to this definition")


window.getstr(_n_)


window.getstr(_y_ , _x_)


window.getstr(_y_ , _x_ , _n_)

Read a bytes object from the user, with primitive line editing capacity. The maximum value for _n_ is 2047.
Changed in version 3.14: The maximum value for _n_ was increased from 1023 to 2047.

window.getyx()[¶](https://docs.python.org/3/library/curses.html#curses.window.getyx "Link to this definition")

Return a tuple `(y, x)` of current cursor position relative to the window’s upper-left corner.

window.hline(_ch_ , _n_)[¶](https://docs.python.org/3/library/curses.html#curses.window.hline "Link to this definition")


window.hline(_y_ , _x_ , _ch_ , _n_)

Display a horizontal line starting at `(y, x)` with length _n_ consisting of the character _ch_.

window.idcok(_flag_)[¶](https://docs.python.org/3/library/curses.html#curses.window.idcok "Link to this definition")

If _flag_ is `False`, curses no longer considers using the hardware insert/delete character feature of the terminal; if _flag_ is `True`, use of character insertion and deletion is enabled. When curses is first initialized, use of character insert/delete is enabled by default.

window.idlok(_flag_)[¶](https://docs.python.org/3/library/curses.html#curses.window.idlok "Link to this definition")

If _flag_ is `True`, `curses` will try and use hardware line editing facilities. Otherwise, line insertion/deletion are disabled.

window.immedok(_flag_)[¶](https://docs.python.org/3/library/curses.html#curses.window.immedok "Link to this definition")

If _flag_ is `True`, any change in the window image automatically causes the window to be refreshed; you no longer have to call [`refresh()`](https://docs.python.org/3/library/curses.html#curses.window.refresh "curses.window.refresh") yourself. However, it may degrade performance considerably, due to repeated calls to wrefresh. This option is disabled by default.

window.inch([_y_ , _x_])[¶](https://docs.python.org/3/library/curses.html#curses.window.inch "Link to this definition")

Return the character at the given position in the window. The bottom 8 bits are the character proper, and upper bits are the attributes.

window.insch(_ch_[, _attr_])[¶](https://docs.python.org/3/library/curses.html#curses.window.insch "Link to this definition")


window.insch(_y_ , _x_ , _ch_[, _attr_])

Paint character _ch_ at `(y, x)` with attributes _attr_ , moving the line from position _x_ right by one character.

window.insdelln(_nlines_)[¶](https://docs.python.org/3/library/curses.html#curses.window.insdelln "Link to this definition")

Insert _nlines_ lines into the specified window above the current line. The _nlines_ bottom lines are lost. For negative _nlines_ , delete _nlines_ lines starting with the one under the cursor, and move the remaining lines up. The bottom _nlines_ lines are cleared. The current cursor position remains the same.

window.insertln()[¶](https://docs.python.org/3/library/curses.html#curses.window.insertln "Link to this definition")

Insert a blank line under the cursor. All following lines are moved down by one line.

window.insnstr(_str_ , _n_[, _attr_])[¶](https://docs.python.org/3/library/curses.html#curses.window.insnstr "Link to this definition")


window.insnstr(_y_ , _x_ , _str_ , _n_[, _attr_])

Insert a character string (as many characters as will fit on the line) before the character under the cursor, up to _n_ characters. If _n_ is zero or negative, the entire string is inserted. All characters to the right of the cursor are shifted right, with the rightmost characters on the line being lost. The cursor position does not change (after moving to _y_ , _x_ , if specified).

window.insstr(_str_[, _attr_])[¶](https://docs.python.org/3/library/curses.html#curses.window.insstr "Link to this definition")


window.insstr(_y_ , _x_ , _str_[, _attr_])

Insert a character string (as many characters as will fit on the line) before the character under the cursor. All characters to the right of the cursor are shifted right, with the rightmost characters on the line being lost. The cursor position does not change (after moving to _y_ , _x_ , if specified).

window.instr([_n_])[¶](https://docs.python.org/3/library/curses.html#curses.window.instr "Link to this definition")


window.instr(_y_ , _x_[, _n_])

Return a bytes object of characters, extracted from the window starting at the current cursor position, or at _y_ , _x_ if specified. Attributes are stripped from the characters. If _n_ is specified, `instr()` returns a string at most _n_ characters long (exclusive of the trailing NUL). The maximum value for _n_ is 2047.
Changed in version 3.14: The maximum value for _n_ was increased from 1023 to 2047.

window.is_linetouched(_line_)[¶](https://docs.python.org/3/library/curses.html#curses.window.is_linetouched "Link to this definition")

Return `True` if the specified line was modified since the last call to [`refresh()`](https://docs.python.org/3/library/curses.html#curses.window.refresh "curses.window.refresh"); otherwise return `False`. Raise a [`curses.error`](https://docs.python.org/3/library/curses.html#curses.error "curses.error") exception if _line_ is not valid for the given window.

window.is_wintouched()[¶](https://docs.python.org/3/library/curses.html#curses.window.is_wintouched "Link to this definition")

Return `True` if the specified window was modified since the last call to [`refresh()`](https://docs.python.org/3/library/curses.html#curses.window.refresh "curses.window.refresh"); otherwise return `False`.

window.keypad(_flag_)[¶](https://docs.python.org/3/library/curses.html#curses.window.keypad "Link to this definition")

If _flag_ is `True`, escape sequences generated by some keys (keypad, function keys) will be interpreted by `curses`. If _flag_ is `False`, escape sequences will be left as is in the input stream.

window.leaveok(_flag_)[¶](https://docs.python.org/3/library/curses.html#curses.window.leaveok "Link to this definition")

If _flag_ is `True`, cursor is left where it is on update, instead of being at “cursor position.” This reduces cursor movement where possible. If possible the cursor will be made invisible.
If _flag_ is `False`, cursor will always be at “cursor position” after an update.

window.move(_new_y_ , _new_x_)[¶](https://docs.python.org/3/library/curses.html#curses.window.move "Link to this definition")

Move cursor to `(new_y, new_x)`.

window.mvderwin(_y_ , _x_)[¶](https://docs.python.org/3/library/curses.html#curses.window.mvderwin "Link to this definition")

Move the window inside its parent window. The screen-relative parameters of the window are not changed. This routine is used to display different parts of the parent window at the same physical position on the screen.

window.mvwin(_new_y_ , _new_x_)[¶](https://docs.python.org/3/library/curses.html#curses.window.mvwin "Link to this definition")

Move the window so its upper-left corner is at `(new_y, new_x)`.

window.nodelay(_flag_)[¶](https://docs.python.org/3/library/curses.html#curses.window.nodelay "Link to this definition")

If _flag_ is `True`, [`getch()`](https://docs.python.org/3/library/curses.html#curses.window.getch "curses.window.getch") will be non-blocking.

window.notimeout(_flag_)[¶](https://docs.python.org/3/library/curses.html#curses.window.notimeout "Link to this definition")

If _flag_ is `True`, escape sequences will not be timed out.
If _flag_ is `False`, after a few milliseconds, an escape sequence will not be interpreted, and will be left in the input stream as is.

window.noutrefresh()[¶](https://docs.python.org/3/library/curses.html#curses.window.noutrefresh "Link to this definition")

Mark for refresh but wait. This function updates the data structure representing the desired state of the window, but does not force an update of the physical screen. To accomplish that, call [`doupdate()`](https://docs.python.org/3/library/curses.html#curses.doupdate "curses.doupdate").

window.overlay(_destwin_[, _sminrow_ , _smincol_ , _dminrow_ , _dmincol_ , _dmaxrow_ , _dmaxcol_])[¶](https://docs.python.org/3/library/curses.html#curses.window.overlay "Link to this definition")

Overlay the window on top of _destwin_. The windows need not be the same size, only the overlapping region is copied. This copy is non-destructive, which means that the current background character does not overwrite the old contents of _destwin_.
To get fine-grained control over the copied region, the second form of `overlay()` can be used. _sminrow_ and _smincol_ are the upper-left coordinates of the source window, and the other variables mark a rectangle in the destination window.

window.overwrite(_destwin_[, _sminrow_ , _smincol_ , _dminrow_ , _dmincol_ , _dmaxrow_ , _dmaxcol_])[¶](https://docs.python.org/3/library/curses.html#curses.window.overwrite "Link to this definition")

Overwrite the window on top of _destwin_. The windows need not be the same size, in which case only the overlapping region is copied. This copy is destructive, which means that the current background character overwrites the old contents of _destwin_.
To get fine-grained control over the copied region, the second form of `overwrite()` can be used. _sminrow_ and _smincol_ are the upper-left coordinates of the source window, the other variables mark a rectangle in the destination window.

window.putwin(_file_)[¶](https://docs.python.org/3/library/curses.html#curses.window.putwin "Link to this definition")

Write all data associated with the window into the provided file object. This information can be later retrieved using the [`getwin()`](https://docs.python.org/3/library/curses.html#curses.getwin "curses.getwin") function.

window.redrawln(_beg_ , _num_)[¶](https://docs.python.org/3/library/curses.html#curses.window.redrawln "Link to this definition")

Indicate that the _num_ screen lines, starting at line _beg_ , are corrupted and should be completely redrawn on the next [`refresh()`](https://docs.python.org/3/library/curses.html#curses.window.refresh "curses.window.refresh") call.

window.redrawwin()[¶](https://docs.python.org/3/library/curses.html#curses.window.redrawwin "Link to this definition")

Touch the entire window, causing it to be completely redrawn on the next [`refresh()`](https://docs.python.org/3/library/curses.html#curses.window.refresh "curses.window.refresh") call.

window.refresh([_pminrow_ , _pmincol_ , _sminrow_ , _smincol_ , _smaxrow_ , _smaxcol_])[¶](https://docs.python.org/3/library/curses.html#curses.window.refresh "Link to this definition")

Update the display immediately (sync actual screen with previous drawing/deleting methods).
The 6 optional arguments can only be specified when the window is a pad created with [`newpad()`](https://docs.python.org/3/library/curses.html#curses.newpad "curses.newpad"). The additional parameters are needed to indicate what part of the pad and screen are involved. _pminrow_ and _pmincol_ specify the upper left-hand corner of the rectangle to be displayed in the pad. _sminrow_ , _smincol_ , _smaxrow_ , and _smaxcol_ specify the edges of the rectangle to be displayed on the screen. The lower right-hand corner of the rectangle to be displayed in the pad is calculated from the screen coordinates, since the rectangles must be the same size. Both rectangles must be entirely contained within their respective structures. Negative values of _pminrow_ , _pmincol_ , _sminrow_ , or _smincol_ are treated as if they were zero.

window.resize(_nlines_ , _ncols_)[¶](https://docs.python.org/3/library/curses.html#curses.window.resize "Link to this definition")

Reallocate storage for a curses window to adjust its dimensions to the specified values. If either dimension is larger than the current values, the window’s data is filled with blanks that have the current background rendition (as set by [`bkgdset()`](https://docs.python.org/3/library/curses.html#curses.window.bkgdset "curses.window.bkgdset")) merged into them.

window.scroll([_lines=1_])[¶](https://docs.python.org/3/library/curses.html#curses.window.scroll "Link to this definition")

Scroll the screen or scrolling region upward by _lines_ lines.

window.scrollok(_flag_)[¶](https://docs.python.org/3/library/curses.html#curses.window.scrollok "Link to this definition")

Control what happens when the cursor of a window is moved off the edge of the window or scrolling region, either as a result of a newline action on the bottom line, or typing the last character of the last line. If _flag_ is `False`, the cursor is left on the bottom line. If _flag_ is `True`, the window is scrolled up one line. Note that in order to get the physical scrolling effect on the terminal, it is also necessary to call [`idlok()`](https://docs.python.org/3/library/curses.html#curses.window.idlok "curses.window.idlok").

window.setscrreg(_top_ , _bottom_)[¶](https://docs.python.org/3/library/curses.html#curses.window.setscrreg "Link to this definition")

Set the scrolling region from line _top_ to line _bottom_. All scrolling actions will take place in this region.

window.standend()[¶](https://docs.python.org/3/library/curses.html#curses.window.standend "Link to this definition")

Turn off the standout attribute. On some terminals this has the side effect of turning off all attributes.

window.standout()[¶](https://docs.python.org/3/library/curses.html#curses.window.standout "Link to this definition")

Turn on attribute _A_STANDOUT_.

window.subpad(_begin_y_ , _begin_x_)[¶](https://docs.python.org/3/library/curses.html#curses.window.subpad "Link to this definition")


window.subpad(_nlines_ , _ncols_ , _begin_y_ , _begin_x_)

Return a sub-window, whose upper-left corner is at `(begin_y, begin_x)`, and whose width/height is _ncols_ /_nlines_.

window.subwin(_begin_y_ , _begin_x_)[¶](https://docs.python.org/3/library/curses.html#curses.window.subwin "Link to this definition")


window.subwin(_nlines_ , _ncols_ , _begin_y_ , _begin_x_)

Return a sub-window, whose upper-left corner is at `(begin_y, begin_x)`, and whose width/height is _ncols_ /_nlines_.
By default, the sub-window will extend from the specified position to the lower right corner of the window.

window.syncdown()[¶](https://docs.python.org/3/library/curses.html#curses.window.syncdown "Link to this definition")

Touch each location in the window that has been touched in any of its ancestor windows. This routine is called by [`refresh()`](https://docs.python.org/3/library/curses.html#curses.window.refresh "curses.window.refresh"), so it should almost never be necessary to call it manually.

window.syncok(_flag_)[¶](https://docs.python.org/3/library/curses.html#curses.window.syncok "Link to this definition")

If _flag_ is `True`, then [`syncup()`](https://docs.python.org/3/library/curses.html#curses.window.syncup "curses.window.syncup") is called automatically whenever there is a change in the window.

window.syncup()[¶](https://docs.python.org/3/library/curses.html#curses.window.syncup "Link to this definition")

Touch all locations in ancestors of the window that have been changed in the window.

window.timeout(_delay_)[¶](https://docs.python.org/3/library/curses.html#curses.window.timeout "Link to this definition")

Set blocking or non-blocking read behavior for the window. If _delay_ is negative, blocking read is used (which will wait indefinitely for input). If _delay_ is zero, then non-blocking read is used, and [`getch()`](https://docs.python.org/3/library/curses.html#curses.window.getch "curses.window.getch") will return `-1` if no input is waiting. If _delay_ is positive, then `getch()` will block for _delay_ milliseconds, and return `-1` if there is still no input at the end of that time.

window.touchline(_start_ , _count_[, _changed_])[¶](https://docs.python.org/3/library/curses.html#curses.window.touchline "Link to this definition")

Pretend _count_ lines have been changed, starting with line _start_. If _changed_ is supplied, it specifies whether the affected lines are marked as having been changed (_changed_`=True`) or unchanged (_changed_`=False`).

window.touchwin()[¶](https://docs.python.org/3/library/curses.html#curses.window.touchwin "Link to this definition")

Pretend the whole window has been changed, for purposes of drawing optimizations.

window.untouchwin()[¶](https://docs.python.org/3/library/curses.html#curses.window.untouchwin "Link to this definition")

Mark all lines in the window as unchanged since the last call to [`refresh()`](https://docs.python.org/3/library/curses.html#curses.window.refresh "curses.window.refresh").

window.vline(_ch_ , _n_[, _attr_])[¶](https://docs.python.org/3/library/curses.html#curses.window.vline "Link to this definition")


window.vline(_y_ , _x_ , _ch_ , _n_[, _attr_])

Display a vertical line starting at `(y, x)` with length _n_ consisting of the character _ch_ with attributes _attr_.
