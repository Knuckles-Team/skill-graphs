## Functions[¶](https://docs.python.org/3/library/curses.html#functions "Link to this heading")
The module `curses` defines the following exception:

_exception_ curses.error[¶](https://docs.python.org/3/library/curses.html#curses.error "Link to this definition")

Exception raised when a curses library function returns an error.
Note
Whenever _x_ or _y_ arguments to a function or a method are optional, they default to the current cursor location. Whenever _attr_ is optional, it defaults to [`A_NORMAL`](https://docs.python.org/3/library/curses.html#curses.A_NORMAL "curses.A_NORMAL").
The module `curses` defines the following functions:

curses.assume_default_colors(_fg_ , _bg_ , _/_)[¶](https://docs.python.org/3/library/curses.html#curses.assume_default_colors "Link to this definition")

Allow use of default values for colors on terminals supporting this feature. Use this to support transparency in your application.
  * Assign terminal default foreground/background colors to color number `-1`. So `init_pair(x, COLOR_RED, -1)` will initialize pair _x_ as red on default background and `init_pair(x, -1, COLOR_BLUE)` will initialize pair _x_ as default foreground on blue.
  * Change the definition of the color-pair `0` to `(fg, bg)`.


Added in version 3.14.

curses.baudrate()[¶](https://docs.python.org/3/library/curses.html#curses.baudrate "Link to this definition")

Return the output speed of the terminal in bits per second. On software terminal emulators it will have a fixed high value. Included for historical reasons; in former times, it was used to write output loops for time delays and occasionally to change interfaces depending on the line speed.

curses.beep()[¶](https://docs.python.org/3/library/curses.html#curses.beep "Link to this definition")

Emit a short attention sound.

curses.can_change_color()[¶](https://docs.python.org/3/library/curses.html#curses.can_change_color "Link to this definition")

Return `True` or `False`, depending on whether the programmer can change the colors displayed by the terminal.

curses.cbreak()[¶](https://docs.python.org/3/library/curses.html#curses.cbreak "Link to this definition")

Enter cbreak mode. In cbreak mode (sometimes called “rare” mode) normal tty line buffering is turned off and characters are available to be read one by one. However, unlike raw mode, special characters (interrupt, quit, suspend, and flow control) retain their effects on the tty driver and calling program. Calling first [`raw()`](https://docs.python.org/3/library/curses.html#curses.raw "curses.raw") then `cbreak()` leaves the terminal in cbreak mode.

curses.color_content(_color_number_)[¶](https://docs.python.org/3/library/curses.html#curses.color_content "Link to this definition")

Return the intensity of the red, green, and blue (RGB) components in the color _color_number_ , which must be between `0` and `COLORS - 1`. Return a 3-tuple, containing the R,G,B values for the given color, which will be between `0` (no component) and `1000` (maximum amount of component).

curses.color_pair(_pair_number_)[¶](https://docs.python.org/3/library/curses.html#curses.color_pair "Link to this definition")

Return the attribute value for displaying text in the specified color pair. Only the first 256 color pairs are supported. This attribute value can be combined with [`A_STANDOUT`](https://docs.python.org/3/library/curses.html#curses.A_STANDOUT "curses.A_STANDOUT"), [`A_REVERSE`](https://docs.python.org/3/library/curses.html#curses.A_REVERSE "curses.A_REVERSE"), and the other `A_*` attributes. [`pair_number()`](https://docs.python.org/3/library/curses.html#curses.pair_number "curses.pair_number") is the counterpart to this function.

curses.curs_set(_visibility_)[¶](https://docs.python.org/3/library/curses.html#curses.curs_set "Link to this definition")

Set the cursor state. _visibility_ can be set to `0`, `1`, or `2`, for invisible, normal, or very visible. If the terminal supports the visibility requested, return the previous cursor state; otherwise raise an exception. On many terminals, the “visible” mode is an underline cursor and the “very visible” mode is a block cursor.

curses.def_prog_mode()[¶](https://docs.python.org/3/library/curses.html#curses.def_prog_mode "Link to this definition")

Save the current terminal mode as the “program” mode, the mode when the running program is using curses. (Its counterpart is the “shell” mode, for when the program is not in curses.) Subsequent calls to [`reset_prog_mode()`](https://docs.python.org/3/library/curses.html#curses.reset_prog_mode "curses.reset_prog_mode") will restore this mode.

curses.def_shell_mode()[¶](https://docs.python.org/3/library/curses.html#curses.def_shell_mode "Link to this definition")

Save the current terminal mode as the “shell” mode, the mode when the running program is not using curses. (Its counterpart is the “program” mode, when the program is using curses capabilities.) Subsequent calls to [`reset_shell_mode()`](https://docs.python.org/3/library/curses.html#curses.reset_shell_mode "curses.reset_shell_mode") will restore this mode.

curses.delay_output(_ms_)[¶](https://docs.python.org/3/library/curses.html#curses.delay_output "Link to this definition")

Insert an _ms_ millisecond pause in output.

curses.doupdate()[¶](https://docs.python.org/3/library/curses.html#curses.doupdate "Link to this definition")

Update the physical screen. The curses library keeps two data structures, one representing the current physical screen contents and a virtual screen representing the desired next state. The `doupdate()` ground updates the physical screen to match the virtual screen.
The virtual screen may be updated by a [`noutrefresh()`](https://docs.python.org/3/library/curses.html#curses.window.noutrefresh "curses.window.noutrefresh") call after write operations such as [`addstr()`](https://docs.python.org/3/library/curses.html#curses.window.addstr "curses.window.addstr") have been performed on a window. The normal [`refresh()`](https://docs.python.org/3/library/curses.html#curses.window.refresh "curses.window.refresh") call is simply `noutrefresh()` followed by `doupdate()`; if you have to update multiple windows, you can speed performance and perhaps reduce screen flicker by issuing `noutrefresh()` calls on all windows, followed by a single `doupdate()`.

curses.echo()[¶](https://docs.python.org/3/library/curses.html#curses.echo "Link to this definition")

Enter echo mode. In echo mode, each character input is echoed to the screen as it is entered.

curses.endwin()[¶](https://docs.python.org/3/library/curses.html#curses.endwin "Link to this definition")

De-initialize the library, and return terminal to normal status.

curses.erasechar()[¶](https://docs.python.org/3/library/curses.html#curses.erasechar "Link to this definition")

Return the user’s current erase character as a one-byte bytes object. Under Unix operating systems this is a property of the controlling tty of the curses program, and is not set by the curses library itself.

curses.filter()[¶](https://docs.python.org/3/library/curses.html#curses.filter "Link to this definition")

The `filter()` routine, if used, must be called before [`initscr()`](https://docs.python.org/3/library/curses.html#curses.initscr "curses.initscr") is called. The effect is that, during those calls, `LINES` is set to `1`; the capabilities `clear`, `cup`, `cud`, `cud1`, `cuu1`, `cuu`, `vpa` are disabled; and the `home` string is set to the value of `cr`. The effect is that the cursor is confined to the current line, and so are screen updates. This may be used for enabling character-at-a-time line editing without touching the rest of the screen.

curses.flash()[¶](https://docs.python.org/3/library/curses.html#curses.flash "Link to this definition")

Flash the screen. That is, change it to reverse-video and then change it back in a short interval. Some people prefer such as ‘visible bell’ to the audible attention signal produced by [`beep()`](https://docs.python.org/3/library/curses.html#curses.beep "curses.beep").

curses.flushinp()[¶](https://docs.python.org/3/library/curses.html#curses.flushinp "Link to this definition")

Flush all input buffers. This throws away any typeahead that has been typed by the user and has not yet been processed by the program.

curses.getmouse()[¶](https://docs.python.org/3/library/curses.html#curses.getmouse "Link to this definition")

After [`getch()`](https://docs.python.org/3/library/curses.html#curses.window.getch "curses.window.getch") returns [`KEY_MOUSE`](https://docs.python.org/3/library/curses.html#curses.KEY_MOUSE "curses.KEY_MOUSE") to signal a mouse event, this method should be called to retrieve the queued mouse event, represented as a 5-tuple `(id, x, y, z, bstate)`. _id_ is an ID value used to distinguish multiple devices, and _x_ , _y_ , _z_ are the event’s coordinates. (_z_ is currently unused.) _bstate_ is an integer value whose bits will be set to indicate the type of event, and will be the bitwise OR of one or more of the following constants, where _n_ is the button number from 1 to 5: [`BUTTONn_PRESSED`](https://docs.python.org/3/library/curses.html#curses.BUTTONn_PRESSED "curses.BUTTONn_PRESSED"), [`BUTTONn_RELEASED`](https://docs.python.org/3/library/curses.html#curses.BUTTONn_RELEASED "curses.BUTTONn_RELEASED"), [`BUTTONn_CLICKED`](https://docs.python.org/3/library/curses.html#curses.BUTTONn_CLICKED "curses.BUTTONn_CLICKED"), [`BUTTONn_DOUBLE_CLICKED`](https://docs.python.org/3/library/curses.html#curses.BUTTONn_DOUBLE_CLICKED "curses.BUTTONn_DOUBLE_CLICKED"), [`BUTTONn_TRIPLE_CLICKED`](https://docs.python.org/3/library/curses.html#curses.BUTTONn_TRIPLE_CLICKED "curses.BUTTONn_TRIPLE_CLICKED"), [`BUTTON_SHIFT`](https://docs.python.org/3/library/curses.html#curses.BUTTON_SHIFT "curses.BUTTON_SHIFT"), [`BUTTON_CTRL`](https://docs.python.org/3/library/curses.html#curses.BUTTON_CTRL "curses.BUTTON_CTRL"), [`BUTTON_ALT`](https://docs.python.org/3/library/curses.html#curses.BUTTON_ALT "curses.BUTTON_ALT").
Changed in version 3.10: The `BUTTON5_*` constants are now exposed if they are provided by the underlying curses library.

curses.getsyx()[¶](https://docs.python.org/3/library/curses.html#curses.getsyx "Link to this definition")

Return the current coordinates of the virtual screen cursor as a tuple `(y, x)`. If [`leaveok`](https://docs.python.org/3/library/curses.html#curses.window.leaveok "curses.window.leaveok") is currently `True`, then return `(-1, -1)`.

curses.getwin(_file_)[¶](https://docs.python.org/3/library/curses.html#curses.getwin "Link to this definition")

Read window related data stored in the file by an earlier [`window.putwin()`](https://docs.python.org/3/library/curses.html#curses.window.putwin "curses.window.putwin") call. The routine then creates and initializes a new window using that data, returning the new window object.

curses.has_colors()[¶](https://docs.python.org/3/library/curses.html#curses.has_colors "Link to this definition")

Return `True` if the terminal can display colors; otherwise, return `False`.

curses.has_extended_color_support()[¶](https://docs.python.org/3/library/curses.html#curses.has_extended_color_support "Link to this definition")

Return `True` if the module supports extended colors; otherwise, return `False`. Extended color support allows more than 256 color pairs for terminals that support more than 16 colors (e.g. xterm-256color).
Extended color support requires ncurses version 6.1 or later.
Added in version 3.10.

curses.has_ic()[¶](https://docs.python.org/3/library/curses.html#curses.has_ic "Link to this definition")

Return `True` if the terminal has insert- and delete-character capabilities. This function is included for historical reasons only, as all modern software terminal emulators have such capabilities.

curses.has_il()[¶](https://docs.python.org/3/library/curses.html#curses.has_il "Link to this definition")

Return `True` if the terminal has insert- and delete-line capabilities, or can simulate them using scrolling regions. This function is included for historical reasons only, as all modern software terminal emulators have such capabilities.

curses.has_key(_ch_)[¶](https://docs.python.org/3/library/curses.html#curses.has_key "Link to this definition")

Take a key value _ch_ , and return `True` if the current terminal type recognizes a key with that value.

curses.halfdelay(_tenths_)[¶](https://docs.python.org/3/library/curses.html#curses.halfdelay "Link to this definition")

Used for half-delay mode, which is similar to cbreak mode in that characters typed by the user are immediately available to the program. However, after blocking for _tenths_ tenths of seconds, raise an exception if nothing has been typed. The value of _tenths_ must be a number between `1` and `255`. Use [`nocbreak()`](https://docs.python.org/3/library/curses.html#curses.nocbreak "curses.nocbreak") to leave half-delay mode.

curses.init_color(_color_number_ , _r_ , _g_ , _b_)[¶](https://docs.python.org/3/library/curses.html#curses.init_color "Link to this definition")

Change the definition of a color, taking the number of the color to be changed followed by three RGB values (for the amounts of red, green, and blue components). The value of _color_number_ must be between `0` and `COLORS - 1`. Each of _r_ , _g_ , _b_ , must be a value between `0` and `1000`. When `init_color()` is used, all occurrences of that color on the screen immediately change to the new definition. This function is a no-op on most terminals; it is active only if [`can_change_color()`](https://docs.python.org/3/library/curses.html#curses.can_change_color "curses.can_change_color") returns `True`.

curses.init_pair(_pair_number_ , _fg_ , _bg_)[¶](https://docs.python.org/3/library/curses.html#curses.init_pair "Link to this definition")

Change the definition of a color-pair. It takes three arguments: the number of the color-pair to be changed, the foreground color number, and the background color number. The value of _pair_number_ must be between `1` and `COLOR_PAIRS - 1` (the `0` color pair can only be changed by [`use_default_colors()`](https://docs.python.org/3/library/curses.html#curses.use_default_colors "curses.use_default_colors") and [`assume_default_colors()`](https://docs.python.org/3/library/curses.html#curses.assume_default_colors "curses.assume_default_colors")). The value of _fg_ and _bg_ arguments must be between `0` and `COLORS - 1`, or, after calling `use_default_colors()` or `assume_default_colors()`, `-1`. If the color-pair was previously initialized, the screen is refreshed and all occurrences of that color-pair are changed to the new definition.

curses.initscr()[¶](https://docs.python.org/3/library/curses.html#curses.initscr "Link to this definition")

Initialize the library. Return a [window](https://docs.python.org/3/library/curses.html#curses-window-objects) object which represents the whole screen.
Note
If there is an error opening the terminal, the underlying curses library may cause the interpreter to exit.

curses.is_term_resized(_nlines_ , _ncols_)[¶](https://docs.python.org/3/library/curses.html#curses.is_term_resized "Link to this definition")

Return `True` if [`resize_term()`](https://docs.python.org/3/library/curses.html#curses.resize_term "curses.resize_term") would modify the window structure, `False` otherwise.

curses.isendwin()[¶](https://docs.python.org/3/library/curses.html#curses.isendwin "Link to this definition")

Return `True` if [`endwin()`](https://docs.python.org/3/library/curses.html#curses.endwin "curses.endwin") has been called (that is, the curses library has been deinitialized).

curses.keyname(_k_)[¶](https://docs.python.org/3/library/curses.html#curses.keyname "Link to this definition")

Return the name of the key numbered _k_ as a bytes object. The name of a key generating printable ASCII character is the key’s character. The name of a control-key combination is a two-byte bytes object consisting of a caret (`b'^'`) followed by the corresponding printable ASCII character. The name of an alt-key combination (128–255) is a bytes object consisting of the prefix `b'M-'` followed by the name of the corresponding ASCII character.

curses.killchar()[¶](https://docs.python.org/3/library/curses.html#curses.killchar "Link to this definition")

Return the user’s current line kill character as a one-byte bytes object. Under Unix operating systems this is a property of the controlling tty of the curses program, and is not set by the curses library itself.

curses.longname()[¶](https://docs.python.org/3/library/curses.html#curses.longname "Link to this definition")

Return a bytes object containing the terminfo long name field describing the current terminal. The maximum length of a verbose description is 128 characters. It is defined only after the call to [`initscr()`](https://docs.python.org/3/library/curses.html#curses.initscr "curses.initscr").

curses.meta(_flag_)[¶](https://docs.python.org/3/library/curses.html#curses.meta "Link to this definition")

If _flag_ is `True`, allow 8-bit characters to be input. If _flag_ is `False`, allow only 7-bit chars.

curses.mouseinterval(_interval_)[¶](https://docs.python.org/3/library/curses.html#curses.mouseinterval "Link to this definition")

Set the maximum time in milliseconds that can elapse between press and release events in order for them to be recognized as a click, and return the previous interval value. The default value is 200 milliseconds, or one fifth of a second.

curses.mousemask(_mousemask_)[¶](https://docs.python.org/3/library/curses.html#curses.mousemask "Link to this definition")

Set the mouse events to be reported, and return a tuple `(availmask, oldmask)`. _availmask_ indicates which of the specified mouse events can be reported; on complete failure it returns `0`. _oldmask_ is the previous value of the given window’s mouse event mask. If this function is never called, no mouse events are ever reported.

curses.napms(_ms_)[¶](https://docs.python.org/3/library/curses.html#curses.napms "Link to this definition")

Sleep for _ms_ milliseconds.

curses.newpad(_nlines_ , _ncols_)[¶](https://docs.python.org/3/library/curses.html#curses.newpad "Link to this definition")

Create and return a pointer to a new pad data structure with the given number of lines and columns. Return a pad as a window object.
A pad is like a window, except that it is not restricted by the screen size, and is not necessarily associated with a particular part of the screen. Pads can be used when a large window is needed, and only a part of the window will be on the screen at one time. Automatic refreshes of pads (such as from scrolling or echoing of input) do not occur. The [`refresh()`](https://docs.python.org/3/library/curses.html#curses.window.refresh "curses.window.refresh") and [`noutrefresh()`](https://docs.python.org/3/library/curses.html#curses.window.noutrefresh "curses.window.noutrefresh") methods of a pad require 6 arguments to specify the part of the pad to be displayed and the location on the screen to be used for the display. The arguments are _pminrow_ , _pmincol_ , _sminrow_ , _smincol_ , _smaxrow_ , _smaxcol_ ; the _p_ arguments refer to the upper left corner of the pad region to be displayed and the _s_ arguments define a clipping box on the screen within which the pad region is to be displayed.

curses.newwin(_nlines_ , _ncols_)[¶](https://docs.python.org/3/library/curses.html#curses.newwin "Link to this definition")


curses.newwin(_nlines_ , _ncols_ , _begin_y_ , _begin_x_)

Return a new [window](https://docs.python.org/3/library/curses.html#curses-window-objects), whose left-upper corner is at `(begin_y, begin_x)`, and whose height/width is _nlines_ /_ncols_.
By default, the window will extend from the specified position to the lower right corner of the screen.

curses.nl()[¶](https://docs.python.org/3/library/curses.html#curses.nl "Link to this definition")

Enter newline mode. This mode translates the return key into newline on input, and translates newline into return and line-feed on output. Newline mode is initially on.

curses.nocbreak()[¶](https://docs.python.org/3/library/curses.html#curses.nocbreak "Link to this definition")

Leave cbreak mode. Return to normal “cooked” mode with line buffering.

curses.noecho()[¶](https://docs.python.org/3/library/curses.html#curses.noecho "Link to this definition")

Leave echo mode. Echoing of input characters is turned off.

curses.nonl()[¶](https://docs.python.org/3/library/curses.html#curses.nonl "Link to this definition")

Leave newline mode. Disable translation of return into newline on input, and disable low-level translation of newline into newline/return on output (but this does not change the behavior of `addch('\n')`, which always does the equivalent of return and line feed on the virtual screen). With translation off, curses can sometimes speed up vertical motion a little; also, it will be able to detect the return key on input.

curses.noqiflush()[¶](https://docs.python.org/3/library/curses.html#curses.noqiflush "Link to this definition")

When the `noqiflush()` routine is used, normal flush of input and output queues associated with the `INTR`, `QUIT` and `SUSP` characters will not be done. You may want to call `noqiflush()` in a signal handler if you want output to continue as though the interrupt had not occurred, after the handler exits.

curses.noraw()[¶](https://docs.python.org/3/library/curses.html#curses.noraw "Link to this definition")

Leave raw mode. Return to normal “cooked” mode with line buffering.

curses.pair_content(_pair_number_)[¶](https://docs.python.org/3/library/curses.html#curses.pair_content "Link to this definition")

Return a tuple `(fg, bg)` containing the colors for the requested color pair. The value of _pair_number_ must be between `0` and `COLOR_PAIRS - 1`.

curses.pair_number(_attr_)[¶](https://docs.python.org/3/library/curses.html#curses.pair_number "Link to this definition")

Return the number of the color-pair set by the attribute value _attr_. [`color_pair()`](https://docs.python.org/3/library/curses.html#curses.color_pair "curses.color_pair") is the counterpart to this function.

curses.putp(_str_)[¶](https://docs.python.org/3/library/curses.html#curses.putp "Link to this definition")

Equivalent to `tputs(str, 1, putchar)`; emit the value of a specified terminfo capability for the current terminal. Note that the output of `putp()` always goes to standard output.

curses.qiflush([_flag_])[¶](https://docs.python.org/3/library/curses.html#curses.qiflush "Link to this definition")

If _flag_ is `False`, the effect is the same as calling [`noqiflush()`](https://docs.python.org/3/library/curses.html#curses.noqiflush "curses.noqiflush"). If _flag_ is `True`, or no argument is provided, the queues will be flushed when these control characters are read.

curses.raw()[¶](https://docs.python.org/3/library/curses.html#curses.raw "Link to this definition")

Enter raw mode. In raw mode, normal line buffering and processing of interrupt, quit, suspend, and flow control keys are turned off; characters are presented to curses input functions one by one.

curses.reset_prog_mode()[¶](https://docs.python.org/3/library/curses.html#curses.reset_prog_mode "Link to this definition")

Restore the terminal to “program” mode, as previously saved by [`def_prog_mode()`](https://docs.python.org/3/library/curses.html#curses.def_prog_mode "curses.def_prog_mode").

curses.reset_shell_mode()[¶](https://docs.python.org/3/library/curses.html#curses.reset_shell_mode "Link to this definition")

Restore the terminal to “shell” mode, as previously saved by [`def_shell_mode()`](https://docs.python.org/3/library/curses.html#curses.def_shell_mode "curses.def_shell_mode").

curses.resetty()[¶](https://docs.python.org/3/library/curses.html#curses.resetty "Link to this definition")

Restore the state of the terminal modes to what it was at the last call to [`savetty()`](https://docs.python.org/3/library/curses.html#curses.savetty "curses.savetty").

curses.resize_term(_nlines_ , _ncols_)[¶](https://docs.python.org/3/library/curses.html#curses.resize_term "Link to this definition")

Backend function used by [`resizeterm()`](https://docs.python.org/3/library/curses.html#curses.resizeterm "curses.resizeterm"), performing most of the work; when resizing the windows, `resize_term()` blank-fills the areas that are extended. The calling application should fill in these areas with appropriate data. The `resize_term()` function attempts to resize all windows. However, due to the calling convention of pads, it is not possible to resize these without additional interaction with the application.

curses.resizeterm(_nlines_ , _ncols_)[¶](https://docs.python.org/3/library/curses.html#curses.resizeterm "Link to this definition")

Resize the standard and current windows to the specified dimensions, and adjusts other bookkeeping data used by the curses library that record the window dimensions (in particular the SIGWINCH handler).

curses.savetty()[¶](https://docs.python.org/3/library/curses.html#curses.savetty "Link to this definition")

Save the current state of the terminal modes in a buffer, usable by [`resetty()`](https://docs.python.org/3/library/curses.html#curses.resetty "curses.resetty").

curses.get_escdelay()[¶](https://docs.python.org/3/library/curses.html#curses.get_escdelay "Link to this definition")

Retrieves the value set by [`set_escdelay()`](https://docs.python.org/3/library/curses.html#curses.set_escdelay "curses.set_escdelay").
Added in version 3.9.

curses.set_escdelay(_ms_)[¶](https://docs.python.org/3/library/curses.html#curses.set_escdelay "Link to this definition")

Sets the number of milliseconds to wait after reading an escape character, to distinguish between an individual escape character entered on the keyboard from escape sequences sent by cursor and function keys.
Added in version 3.9.

curses.get_tabsize()[¶](https://docs.python.org/3/library/curses.html#curses.get_tabsize "Link to this definition")

Retrieves the value set by [`set_tabsize()`](https://docs.python.org/3/library/curses.html#curses.set_tabsize "curses.set_tabsize").
Added in version 3.9.

curses.set_tabsize(_size_)[¶](https://docs.python.org/3/library/curses.html#curses.set_tabsize "Link to this definition")

Sets the number of columns used by the curses library when converting a tab character to spaces as it adds the tab to a window.
Added in version 3.9.

curses.setsyx(_y_ , _x_)[¶](https://docs.python.org/3/library/curses.html#curses.setsyx "Link to this definition")

Set the virtual screen cursor to _y_ , _x_. If _y_ and _x_ are both `-1`, then [`leaveok`](https://docs.python.org/3/library/curses.html#curses.window.leaveok "curses.window.leaveok") is set `True`.

curses.setupterm(_term =None_, _fd =-1_)[¶](https://docs.python.org/3/library/curses.html#curses.setupterm "Link to this definition")

Initialize the terminal. _term_ is a string giving the terminal name, or `None`; if omitted or `None`, the value of the `TERM` environment variable will be used. _fd_ is the file descriptor to which any initialization sequences will be sent; if not supplied or `-1`, the file descriptor for `sys.stdout` will be used.

curses.start_color()[¶](https://docs.python.org/3/library/curses.html#curses.start_color "Link to this definition")

Must be called if the programmer wants to use colors, and before any other color manipulation routine is called. It is good practice to call this routine right after [`initscr()`](https://docs.python.org/3/library/curses.html#curses.initscr "curses.initscr").
`start_color()` initializes eight basic colors (black, red, green, yellow, blue, magenta, cyan, and white), and two global variables in the `curses` module, [`COLORS`](https://docs.python.org/3/library/curses.html#curses.COLORS "curses.COLORS") and [`COLOR_PAIRS`](https://docs.python.org/3/library/curses.html#curses.COLOR_PAIRS "curses.COLOR_PAIRS"), containing the maximum number of colors and color-pairs the terminal can support. It also restores the colors on the terminal to the values they had when the terminal was just turned on.

curses.termattrs()[¶](https://docs.python.org/3/library/curses.html#curses.termattrs "Link to this definition")

Return a logical OR of all video attributes supported by the terminal. This information is useful when a curses program needs complete control over the appearance of the screen.

curses.termname()[¶](https://docs.python.org/3/library/curses.html#curses.termname "Link to this definition")

Return the value of the environment variable `TERM`, as a bytes object, truncated to 14 characters.

curses.tigetflag(_capname_)[¶](https://docs.python.org/3/library/curses.html#curses.tigetflag "Link to this definition")

Return the value of the Boolean capability corresponding to the terminfo capability name _capname_ as an integer. Return the value `-1` if _capname_ is not a Boolean capability, or `0` if it is canceled or absent from the terminal description.

curses.tigetnum(_capname_)[¶](https://docs.python.org/3/library/curses.html#curses.tigetnum "Link to this definition")

Return the value of the numeric capability corresponding to the terminfo capability name _capname_ as an integer. Return the value `-2` if _capname_ is not a numeric capability, or `-1` if it is canceled or absent from the terminal description.

curses.tigetstr(_capname_)[¶](https://docs.python.org/3/library/curses.html#curses.tigetstr "Link to this definition")

Return the value of the string capability corresponding to the terminfo capability name _capname_ as a bytes object. Return `None` if _capname_ is not a terminfo “string capability”, or is canceled or absent from the terminal description.

curses.tparm(_str_[, _..._])[¶](https://docs.python.org/3/library/curses.html#curses.tparm "Link to this definition")

Instantiate the bytes object _str_ with the supplied parameters, where _str_ should be a parameterized string obtained from the terminfo database. E.g. `tparm(tigetstr("cup"), 5, 3)` could result in `b'\033[6;4H'`, the exact result depending on terminal type.

curses.typeahead(_fd_)[¶](https://docs.python.org/3/library/curses.html#curses.typeahead "Link to this definition")

Specify that the file descriptor _fd_ be used for typeahead checking. If _fd_ is `-1`, then no typeahead checking is done.
The curses library does “line-breakout optimization” by looking for typeahead periodically while updating the screen. If input is found, and it is coming from a tty, the current update is postponed until refresh or doupdate is called again, allowing faster response to commands typed in advance. This function allows specifying a different file descriptor for typeahead checking.

curses.unctrl(_ch_)[¶](https://docs.python.org/3/library/curses.html#curses.unctrl "Link to this definition")

Return a bytes object which is a printable representation of the character _ch_. Control characters are represented as a caret followed by the character, for example as `b'^C'`. Printing characters are left as they are.

curses.ungetch(_ch_)[¶](https://docs.python.org/3/library/curses.html#curses.ungetch "Link to this definition")

Push _ch_ so the next [`getch()`](https://docs.python.org/3/library/curses.html#curses.window.getch "curses.window.getch") will return it.
Note
Only one _ch_ can be pushed before `getch()` is called.

curses.update_lines_cols()[¶](https://docs.python.org/3/library/curses.html#curses.update_lines_cols "Link to this definition")

Update the [`LINES`](https://docs.python.org/3/library/curses.html#curses.LINES "curses.LINES") and [`COLS`](https://docs.python.org/3/library/curses.html#curses.COLS "curses.COLS") module variables. Useful for detecting manual screen resize.
Added in version 3.5.

curses.unget_wch(_ch_)[¶](https://docs.python.org/3/library/curses.html#curses.unget_wch "Link to this definition")

Push _ch_ so the next [`get_wch()`](https://docs.python.org/3/library/curses.html#curses.window.get_wch "curses.window.get_wch") will return it.
Note
Only one _ch_ can be pushed before `get_wch()` is called.
Added in version 3.3.

curses.ungetmouse(_id_ , _x_ , _y_ , _z_ , _bstate_)[¶](https://docs.python.org/3/library/curses.html#curses.ungetmouse "Link to this definition")

Push a [`KEY_MOUSE`](https://docs.python.org/3/library/curses.html#curses.KEY_MOUSE "curses.KEY_MOUSE") event onto the input queue, associating the given state data with it.

curses.use_env(_flag_)[¶](https://docs.python.org/3/library/curses.html#curses.use_env "Link to this definition")

If used, this function should be called before [`initscr()`](https://docs.python.org/3/library/curses.html#curses.initscr "curses.initscr") or newterm are called. When _flag_ is `False`, the values of lines and columns specified in the terminfo database will be used, even if environment variables `LINES` and `COLUMNS` (used by default) are set, or if curses is running in a window (in which case default behavior would be to use the window size if `LINES` and `COLUMNS` are not set).

curses.use_default_colors()[¶](https://docs.python.org/3/library/curses.html#curses.use_default_colors "Link to this definition")

Equivalent to `assume_default_colors(-1, -1)`.

curses.wrapper(_func_ , _/_ , _* args_, _** kwargs_)[¶](https://docs.python.org/3/library/curses.html#curses.wrapper "Link to this definition")

Initialize curses and call another callable object, _func_ , which should be the rest of your curses-using application. If the application raises an exception, this function will restore the terminal to a sane state before re-raising the exception and generating a traceback. The callable object _func_ is then passed the main window ‘stdscr’ as its first argument, followed by any other arguments passed to `wrapper()`. Before calling _func_ , `wrapper()` turns on cbreak mode, turns off echo, enables the terminal keypad, and initializes colors if the terminal has color support. On exit (whether normally or by exception) it restores cooked mode, turns on echo, and disables the terminal keypad.
