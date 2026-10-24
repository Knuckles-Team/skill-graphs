## Constants[¶](https://docs.python.org/3/library/curses.html#constants "Link to this heading")
The `curses` module defines the following data members:

curses.ERR[¶](https://docs.python.org/3/library/curses.html#curses.ERR "Link to this definition")

Some curses routines that return an integer, such as [`getch()`](https://docs.python.org/3/library/curses.html#curses.window.getch "curses.window.getch"), return [`ERR`](https://docs.python.org/3/library/curses.html#curses.ERR "curses.ERR") upon failure.

curses.OK[¶](https://docs.python.org/3/library/curses.html#curses.OK "Link to this definition")

Some curses routines that return an integer, such as [`napms()`](https://docs.python.org/3/library/curses.html#curses.napms "curses.napms"), return [`OK`](https://docs.python.org/3/library/curses.html#curses.OK "curses.OK") upon success.

curses.version[¶](https://docs.python.org/3/library/curses.html#curses.version "Link to this definition")

A bytes object representing the current version of the module.

curses.ncurses_version[¶](https://docs.python.org/3/library/curses.html#curses.ncurses_version "Link to this definition")

A named tuple containing the three components of the ncurses library version: _major_ , _minor_ , and _patch_. All values are integers. The components can also be accessed by name, so `curses.ncurses_version[0]` is equivalent to `curses.ncurses_version.major` and so on.
Availability: if the ncurses library is used.
Added in version 3.8.

curses.COLORS[¶](https://docs.python.org/3/library/curses.html#curses.COLORS "Link to this definition")

The maximum number of colors the terminal can support. It is defined only after the call to [`start_color()`](https://docs.python.org/3/library/curses.html#curses.start_color "curses.start_color").

curses.COLOR_PAIRS[¶](https://docs.python.org/3/library/curses.html#curses.COLOR_PAIRS "Link to this definition")

The maximum number of color pairs the terminal can support. It is defined only after the call to [`start_color()`](https://docs.python.org/3/library/curses.html#curses.start_color "curses.start_color").

curses.COLS[¶](https://docs.python.org/3/library/curses.html#curses.COLS "Link to this definition")

The width of the screen, i.e., the number of columns. It is defined only after the call to [`initscr()`](https://docs.python.org/3/library/curses.html#curses.initscr "curses.initscr"). Updated by [`update_lines_cols()`](https://docs.python.org/3/library/curses.html#curses.update_lines_cols "curses.update_lines_cols"), [`resizeterm()`](https://docs.python.org/3/library/curses.html#curses.resizeterm "curses.resizeterm") and [`resize_term()`](https://docs.python.org/3/library/curses.html#curses.resize_term "curses.resize_term").

curses.LINES[¶](https://docs.python.org/3/library/curses.html#curses.LINES "Link to this definition")

The height of the screen, i.e., the number of lines. It is defined only after the call to [`initscr()`](https://docs.python.org/3/library/curses.html#curses.initscr "curses.initscr"). Updated by [`update_lines_cols()`](https://docs.python.org/3/library/curses.html#curses.update_lines_cols "curses.update_lines_cols"), [`resizeterm()`](https://docs.python.org/3/library/curses.html#curses.resizeterm "curses.resizeterm") and [`resize_term()`](https://docs.python.org/3/library/curses.html#curses.resize_term "curses.resize_term").
Some constants are available to specify character cell attributes. The exact constants available are system dependent.
Attribute | Meaning
---|---

curses.A_ALTCHARSET[¶](https://docs.python.org/3/library/curses.html#curses.A_ALTCHARSET "Link to this definition")
| Alternate character set mode

curses.A_BLINK[¶](https://docs.python.org/3/library/curses.html#curses.A_BLINK "Link to this definition")
| Blink mode

curses.A_BOLD[¶](https://docs.python.org/3/library/curses.html#curses.A_BOLD "Link to this definition")
| Bold mode

curses.A_DIM[¶](https://docs.python.org/3/library/curses.html#curses.A_DIM "Link to this definition")
| Dim mode

curses.A_INVIS[¶](https://docs.python.org/3/library/curses.html#curses.A_INVIS "Link to this definition")
| Invisible or blank mode

curses.A_ITALIC[¶](https://docs.python.org/3/library/curses.html#curses.A_ITALIC "Link to this definition")
| Italic mode

curses.A_NORMAL[¶](https://docs.python.org/3/library/curses.html#curses.A_NORMAL "Link to this definition")
| Normal attribute

curses.A_PROTECT[¶](https://docs.python.org/3/library/curses.html#curses.A_PROTECT "Link to this definition")
| Protected mode

curses.A_REVERSE[¶](https://docs.python.org/3/library/curses.html#curses.A_REVERSE "Link to this definition")
| Reverse background and foreground colors

curses.A_STANDOUT[¶](https://docs.python.org/3/library/curses.html#curses.A_STANDOUT "Link to this definition")
| Standout mode

curses.A_UNDERLINE[¶](https://docs.python.org/3/library/curses.html#curses.A_UNDERLINE "Link to this definition")
| Underline mode

curses.A_HORIZONTAL[¶](https://docs.python.org/3/library/curses.html#curses.A_HORIZONTAL "Link to this definition")
| Horizontal highlight

curses.A_LEFT[¶](https://docs.python.org/3/library/curses.html#curses.A_LEFT "Link to this definition")
| Left highlight

curses.A_LOW[¶](https://docs.python.org/3/library/curses.html#curses.A_LOW "Link to this definition")
| Low highlight

curses.A_RIGHT[¶](https://docs.python.org/3/library/curses.html#curses.A_RIGHT "Link to this definition")
| Right highlight

curses.A_TOP[¶](https://docs.python.org/3/library/curses.html#curses.A_TOP "Link to this definition")
| Top highlight

curses.A_VERTICAL[¶](https://docs.python.org/3/library/curses.html#curses.A_VERTICAL "Link to this definition")
| Vertical highlight
Added in version 3.7: `A_ITALIC` was added.
Several constants are available to extract corresponding attributes returned by some methods.
Bit-mask | Meaning
---|---

curses.A_ATTRIBUTES[¶](https://docs.python.org/3/library/curses.html#curses.A_ATTRIBUTES "Link to this definition")
| Bit-mask to extract attributes

curses.A_CHARTEXT[¶](https://docs.python.org/3/library/curses.html#curses.A_CHARTEXT "Link to this definition")
| Bit-mask to extract a character

curses.A_COLOR[¶](https://docs.python.org/3/library/curses.html#curses.A_COLOR "Link to this definition")
| Bit-mask to extract color-pair field information
Keys are referred to by integer constants with names starting with `KEY_`. The exact keycaps available are system dependent.
Key constant | Key
---|---

curses.KEY_MIN[¶](https://docs.python.org/3/library/curses.html#curses.KEY_MIN "Link to this definition")
| Minimum key value

curses.KEY_BREAK[¶](https://docs.python.org/3/library/curses.html#curses.KEY_BREAK "Link to this definition")
| Break key (unreliable)

curses.KEY_DOWN[¶](https://docs.python.org/3/library/curses.html#curses.KEY_DOWN "Link to this definition")
| Down-arrow

curses.KEY_UP[¶](https://docs.python.org/3/library/curses.html#curses.KEY_UP "Link to this definition")
| Up-arrow

curses.KEY_LEFT[¶](https://docs.python.org/3/library/curses.html#curses.KEY_LEFT "Link to this definition")
| Left-arrow

curses.KEY_RIGHT[¶](https://docs.python.org/3/library/curses.html#curses.KEY_RIGHT "Link to this definition")
| Right-arrow

curses.KEY_HOME[¶](https://docs.python.org/3/library/curses.html#curses.KEY_HOME "Link to this definition")
| Home key (upward+left arrow)

curses.KEY_BACKSPACE[¶](https://docs.python.org/3/library/curses.html#curses.KEY_BACKSPACE "Link to this definition")
| Backspace (unreliable)

curses.KEY_F0[¶](https://docs.python.org/3/library/curses.html#curses.KEY_F0 "Link to this definition")
| Function keys. Up to 64 function keys are supported.

curses.KEY_Fn[¶](https://docs.python.org/3/library/curses.html#curses.KEY_Fn "Link to this definition")
| Value of function key _n_

curses.KEY_DL[¶](https://docs.python.org/3/library/curses.html#curses.KEY_DL "Link to this definition")
| Delete line

curses.KEY_IL[¶](https://docs.python.org/3/library/curses.html#curses.KEY_IL "Link to this definition")
| Insert line

curses.KEY_DC[¶](https://docs.python.org/3/library/curses.html#curses.KEY_DC "Link to this definition")
| Delete character

curses.KEY_IC[¶](https://docs.python.org/3/library/curses.html#curses.KEY_IC "Link to this definition")
| Insert char or enter insert mode

curses.KEY_EIC[¶](https://docs.python.org/3/library/curses.html#curses.KEY_EIC "Link to this definition")
| Exit insert char mode

curses.KEY_CLEAR[¶](https://docs.python.org/3/library/curses.html#curses.KEY_CLEAR "Link to this definition")
| Clear screen

curses.KEY_EOS[¶](https://docs.python.org/3/library/curses.html#curses.KEY_EOS "Link to this definition")
| Clear to end of screen

curses.KEY_EOL[¶](https://docs.python.org/3/library/curses.html#curses.KEY_EOL "Link to this definition")
| Clear to end of line

curses.KEY_SF[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SF "Link to this definition")
| Scroll 1 line forward

curses.KEY_SR[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SR "Link to this definition")
| Scroll 1 line backward (reverse)

curses.KEY_NPAGE[¶](https://docs.python.org/3/library/curses.html#curses.KEY_NPAGE "Link to this definition")
| Next page

curses.KEY_PPAGE[¶](https://docs.python.org/3/library/curses.html#curses.KEY_PPAGE "Link to this definition")
| Previous page

curses.KEY_STAB[¶](https://docs.python.org/3/library/curses.html#curses.KEY_STAB "Link to this definition")
| Set tab

curses.KEY_CTAB[¶](https://docs.python.org/3/library/curses.html#curses.KEY_CTAB "Link to this definition")
| Clear tab

curses.KEY_CATAB[¶](https://docs.python.org/3/library/curses.html#curses.KEY_CATAB "Link to this definition")
| Clear all tabs

curses.KEY_ENTER[¶](https://docs.python.org/3/library/curses.html#curses.KEY_ENTER "Link to this definition")
| Enter or send (unreliable)

curses.KEY_SRESET[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SRESET "Link to this definition")
| Soft (partial) reset (unreliable)

curses.KEY_RESET[¶](https://docs.python.org/3/library/curses.html#curses.KEY_RESET "Link to this definition")
| Reset or hard reset (unreliable)

curses.KEY_PRINT[¶](https://docs.python.org/3/library/curses.html#curses.KEY_PRINT "Link to this definition")
| Print

curses.KEY_LL[¶](https://docs.python.org/3/library/curses.html#curses.KEY_LL "Link to this definition")
| Home down or bottom (lower left)

curses.KEY_A1[¶](https://docs.python.org/3/library/curses.html#curses.KEY_A1 "Link to this definition")
| Upper left of keypad

curses.KEY_A3[¶](https://docs.python.org/3/library/curses.html#curses.KEY_A3 "Link to this definition")
| Upper right of keypad

curses.KEY_B2[¶](https://docs.python.org/3/library/curses.html#curses.KEY_B2 "Link to this definition")
| Center of keypad

curses.KEY_C1[¶](https://docs.python.org/3/library/curses.html#curses.KEY_C1 "Link to this definition")
| Lower left of keypad

curses.KEY_C3[¶](https://docs.python.org/3/library/curses.html#curses.KEY_C3 "Link to this definition")
| Lower right of keypad

curses.KEY_BTAB[¶](https://docs.python.org/3/library/curses.html#curses.KEY_BTAB "Link to this definition")
| Back tab

curses.KEY_BEG[¶](https://docs.python.org/3/library/curses.html#curses.KEY_BEG "Link to this definition")
| Beg (beginning)

curses.KEY_CANCEL[¶](https://docs.python.org/3/library/curses.html#curses.KEY_CANCEL "Link to this definition")
| Cancel

curses.KEY_CLOSE[¶](https://docs.python.org/3/library/curses.html#curses.KEY_CLOSE "Link to this definition")
| Close

curses.KEY_COMMAND[¶](https://docs.python.org/3/library/curses.html#curses.KEY_COMMAND "Link to this definition")
| Cmd (command)

curses.KEY_COPY[¶](https://docs.python.org/3/library/curses.html#curses.KEY_COPY "Link to this definition")
| Copy

curses.KEY_CREATE[¶](https://docs.python.org/3/library/curses.html#curses.KEY_CREATE "Link to this definition")
| Create

curses.KEY_END[¶](https://docs.python.org/3/library/curses.html#curses.KEY_END "Link to this definition")
| End

curses.KEY_EXIT[¶](https://docs.python.org/3/library/curses.html#curses.KEY_EXIT "Link to this definition")
| Exit

curses.KEY_FIND[¶](https://docs.python.org/3/library/curses.html#curses.KEY_FIND "Link to this definition")
| Find

curses.KEY_HELP[¶](https://docs.python.org/3/library/curses.html#curses.KEY_HELP "Link to this definition")
| Help

curses.KEY_MARK[¶](https://docs.python.org/3/library/curses.html#curses.KEY_MARK "Link to this definition")
| Mark

curses.KEY_MESSAGE[¶](https://docs.python.org/3/library/curses.html#curses.KEY_MESSAGE "Link to this definition")
| Message

curses.KEY_MOVE[¶](https://docs.python.org/3/library/curses.html#curses.KEY_MOVE "Link to this definition")
| Move

curses.KEY_NEXT[¶](https://docs.python.org/3/library/curses.html#curses.KEY_NEXT "Link to this definition")
| Next

curses.KEY_OPEN[¶](https://docs.python.org/3/library/curses.html#curses.KEY_OPEN "Link to this definition")
| Open

curses.KEY_OPTIONS[¶](https://docs.python.org/3/library/curses.html#curses.KEY_OPTIONS "Link to this definition")
| Options

curses.KEY_PREVIOUS[¶](https://docs.python.org/3/library/curses.html#curses.KEY_PREVIOUS "Link to this definition")
| Prev (previous)

curses.KEY_REDO[¶](https://docs.python.org/3/library/curses.html#curses.KEY_REDO "Link to this definition")
| Redo

curses.KEY_REFERENCE[¶](https://docs.python.org/3/library/curses.html#curses.KEY_REFERENCE "Link to this definition")
| Ref (reference)

curses.KEY_REFRESH[¶](https://docs.python.org/3/library/curses.html#curses.KEY_REFRESH "Link to this definition")
| Refresh

curses.KEY_REPLACE[¶](https://docs.python.org/3/library/curses.html#curses.KEY_REPLACE "Link to this definition")
| Replace

curses.KEY_RESTART[¶](https://docs.python.org/3/library/curses.html#curses.KEY_RESTART "Link to this definition")
| Restart

curses.KEY_RESUME[¶](https://docs.python.org/3/library/curses.html#curses.KEY_RESUME "Link to this definition")
| Resume

curses.KEY_SAVE[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SAVE "Link to this definition")
| Save

curses.KEY_SBEG[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SBEG "Link to this definition")
| Shifted Beg (beginning)

curses.KEY_SCANCEL[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SCANCEL "Link to this definition")
| Shifted Cancel

curses.KEY_SCOMMAND[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SCOMMAND "Link to this definition")
| Shifted Command

curses.KEY_SCOPY[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SCOPY "Link to this definition")
| Shifted Copy

curses.KEY_SCREATE[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SCREATE "Link to this definition")
| Shifted Create

curses.KEY_SDC[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SDC "Link to this definition")
| Shifted Delete char

curses.KEY_SDL[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SDL "Link to this definition")
| Shifted Delete line

curses.KEY_SELECT[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SELECT "Link to this definition")
| Select

curses.KEY_SEND[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SEND "Link to this definition")
| Shifted End

curses.KEY_SEOL[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SEOL "Link to this definition")
| Shifted Clear line

curses.KEY_SEXIT[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SEXIT "Link to this definition")
| Shifted Exit

curses.KEY_SFIND[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SFIND "Link to this definition")
| Shifted Find

curses.KEY_SHELP[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SHELP "Link to this definition")
| Shifted Help

curses.KEY_SHOME[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SHOME "Link to this definition")
| Shifted Home

curses.KEY_SIC[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SIC "Link to this definition")
| Shifted Input

curses.KEY_SLEFT[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SLEFT "Link to this definition")
| Shifted Left arrow

curses.KEY_SMESSAGE[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SMESSAGE "Link to this definition")
| Shifted Message

curses.KEY_SMOVE[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SMOVE "Link to this definition")
| Shifted Move

curses.KEY_SNEXT[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SNEXT "Link to this definition")
| Shifted Next

curses.KEY_SOPTIONS[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SOPTIONS "Link to this definition")
| Shifted Options

curses.KEY_SPREVIOUS[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SPREVIOUS "Link to this definition")
| Shifted Prev

curses.KEY_SPRINT[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SPRINT "Link to this definition")
| Shifted Print

curses.KEY_SREDO[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SREDO "Link to this definition")
| Shifted Redo

curses.KEY_SREPLACE[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SREPLACE "Link to this definition")
| Shifted Replace

curses.KEY_SRIGHT[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SRIGHT "Link to this definition")
| Shifted Right arrow

curses.KEY_SRSUME[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SRSUME "Link to this definition")
| Shifted Resume

curses.KEY_SSAVE[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SSAVE "Link to this definition")
| Shifted Save

curses.KEY_SSUSPEND[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SSUSPEND "Link to this definition")
| Shifted Suspend

curses.KEY_SUNDO[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SUNDO "Link to this definition")
| Shifted Undo

curses.KEY_SUSPEND[¶](https://docs.python.org/3/library/curses.html#curses.KEY_SUSPEND "Link to this definition")
| Suspend

curses.KEY_UNDO[¶](https://docs.python.org/3/library/curses.html#curses.KEY_UNDO "Link to this definition")
| Undo

curses.KEY_MOUSE[¶](https://docs.python.org/3/library/curses.html#curses.KEY_MOUSE "Link to this definition")
| Mouse event has occurred

curses.KEY_RESIZE[¶](https://docs.python.org/3/library/curses.html#curses.KEY_RESIZE "Link to this definition")
| Terminal resize event

curses.KEY_MAX[¶](https://docs.python.org/3/library/curses.html#curses.KEY_MAX "Link to this definition")
| Maximum key value
On VT100s and their software emulations, such as X terminal emulators, there are normally at least four function keys ([`KEY_F1`](https://docs.python.org/3/library/curses.html#curses.KEY_Fn "curses.KEY_Fn"), `KEY_F2`, `KEY_F3`, `KEY_F4`) available, and the arrow keys mapped to [`KEY_UP`](https://docs.python.org/3/library/curses.html#curses.KEY_UP "curses.KEY_UP"), [`KEY_DOWN`](https://docs.python.org/3/library/curses.html#curses.KEY_DOWN "curses.KEY_DOWN"), [`KEY_LEFT`](https://docs.python.org/3/library/curses.html#curses.KEY_LEFT "curses.KEY_LEFT") and [`KEY_RIGHT`](https://docs.python.org/3/library/curses.html#curses.KEY_RIGHT "curses.KEY_RIGHT") in the obvious way. If your machine has a PC keyboard, it is safe to expect arrow keys and twelve function keys (older PC keyboards may have only ten function keys); also, the following keypad mappings are standard:
Keycap | Constant
---|---
`Insert` | KEY_IC
`Delete` | KEY_DC
`Home` | KEY_HOME
`End` | KEY_END
`Page Up` | KEY_PPAGE
`Page Down` | KEY_NPAGE
The following table lists characters from the alternate character set. These are inherited from the VT100 terminal, and will generally be available on software emulations such as X terminals. When there is no graphic available, curses falls back on a crude printable ASCII approximation.
Note
These are available only after [`initscr()`](https://docs.python.org/3/library/curses.html#curses.initscr "curses.initscr") has been called.
ACS code | Meaning
---|---

curses.ACS_BBSS[¶](https://docs.python.org/3/library/curses.html#curses.ACS_BBSS "Link to this definition")
| alternate name for upper right corner

curses.ACS_BLOCK[¶](https://docs.python.org/3/library/curses.html#curses.ACS_BLOCK "Link to this definition")
| solid square block

curses.ACS_BOARD[¶](https://docs.python.org/3/library/curses.html#curses.ACS_BOARD "Link to this definition")
| board of squares

curses.ACS_BSBS[¶](https://docs.python.org/3/library/curses.html#curses.ACS_BSBS "Link to this definition")
| alternate name for horizontal line

curses.ACS_BSSB[¶](https://docs.python.org/3/library/curses.html#curses.ACS_BSSB "Link to this definition")
| alternate name for upper left corner

curses.ACS_BSSS[¶](https://docs.python.org/3/library/curses.html#curses.ACS_BSSS "Link to this definition")
| alternate name for top tee

curses.ACS_BTEE[¶](https://docs.python.org/3/library/curses.html#curses.ACS_BTEE "Link to this definition")
| bottom tee

curses.ACS_BULLET[¶](https://docs.python.org/3/library/curses.html#curses.ACS_BULLET "Link to this definition")
| bullet

curses.ACS_CKBOARD[¶](https://docs.python.org/3/library/curses.html#curses.ACS_CKBOARD "Link to this definition")
| checker board (stipple)

curses.ACS_DARROW[¶](https://docs.python.org/3/library/curses.html#curses.ACS_DARROW "Link to this definition")
| arrow pointing down

curses.ACS_DEGREE[¶](https://docs.python.org/3/library/curses.html#curses.ACS_DEGREE "Link to this definition")
| degree symbol

curses.ACS_DIAMOND[¶](https://docs.python.org/3/library/curses.html#curses.ACS_DIAMOND "Link to this definition")
| diamond

curses.ACS_GEQUAL[¶](https://docs.python.org/3/library/curses.html#curses.ACS_GEQUAL "Link to this definition")
| greater-than-or-equal-to

curses.ACS_HLINE[¶](https://docs.python.org/3/library/curses.html#curses.ACS_HLINE "Link to this definition")
| horizontal line

curses.ACS_LANTERN[¶](https://docs.python.org/3/library/curses.html#curses.ACS_LANTERN "Link to this definition")
| lantern symbol

curses.ACS_LARROW[¶](https://docs.python.org/3/library/curses.html#curses.ACS_LARROW "Link to this definition")
| left arrow

curses.ACS_LEQUAL[¶](https://docs.python.org/3/library/curses.html#curses.ACS_LEQUAL "Link to this definition")
| less-than-or-equal-to

curses.ACS_LLCORNER[¶](https://docs.python.org/3/library/curses.html#curses.ACS_LLCORNER "Link to this definition")
| lower left-hand corner

curses.ACS_LRCORNER[¶](https://docs.python.org/3/library/curses.html#curses.ACS_LRCORNER "Link to this definition")
| lower right-hand corner

curses.ACS_LTEE[¶](https://docs.python.org/3/library/curses.html#curses.ACS_LTEE "Link to this definition")
| left tee

curses.ACS_NEQUAL[¶](https://docs.python.org/3/library/curses.html#curses.ACS_NEQUAL "Link to this definition")
| not-equal sign

curses.ACS_PI[¶](https://docs.python.org/3/library/curses.html#curses.ACS_PI "Link to this definition")
| letter pi

curses.ACS_PLMINUS[¶](https://docs.python.org/3/library/curses.html#curses.ACS_PLMINUS "Link to this definition")
| plus-or-minus sign

curses.ACS_PLUS[¶](https://docs.python.org/3/library/curses.html#curses.ACS_PLUS "Link to this definition")
| big plus sign

curses.ACS_RARROW[¶](https://docs.python.org/3/library/curses.html#curses.ACS_RARROW "Link to this definition")
| right arrow

curses.ACS_RTEE[¶](https://docs.python.org/3/library/curses.html#curses.ACS_RTEE "Link to this definition")
| right tee

curses.ACS_S1[¶](https://docs.python.org/3/library/curses.html#curses.ACS_S1 "Link to this definition")
| scan line 1

curses.ACS_S3[¶](https://docs.python.org/3/library/curses.html#curses.ACS_S3 "Link to this definition")
| scan line 3

curses.ACS_S7[¶](https://docs.python.org/3/library/curses.html#curses.ACS_S7 "Link to this definition")
| scan line 7

curses.ACS_S9[¶](https://docs.python.org/3/library/curses.html#curses.ACS_S9 "Link to this definition")
| scan line 9

curses.ACS_SBBS[¶](https://docs.python.org/3/library/curses.html#curses.ACS_SBBS "Link to this definition")
| alternate name for lower right corner

curses.ACS_SBSB[¶](https://docs.python.org/3/library/curses.html#curses.ACS_SBSB "Link to this definition")
| alternate name for vertical line

curses.ACS_SBSS[¶](https://docs.python.org/3/library/curses.html#curses.ACS_SBSS "Link to this definition")
| alternate name for right tee

curses.ACS_SSBB[¶](https://docs.python.org/3/library/curses.html#curses.ACS_SSBB "Link to this definition")
| alternate name for lower left corner

curses.ACS_SSBS[¶](https://docs.python.org/3/library/curses.html#curses.ACS_SSBS "Link to this definition")
| alternate name for bottom tee

curses.ACS_SSSB[¶](https://docs.python.org/3/library/curses.html#curses.ACS_SSSB "Link to this definition")
| alternate name for left tee

curses.ACS_SSSS[¶](https://docs.python.org/3/library/curses.html#curses.ACS_SSSS "Link to this definition")
| alternate name for crossover or big plus

curses.ACS_STERLING[¶](https://docs.python.org/3/library/curses.html#curses.ACS_STERLING "Link to this definition")
| pound sterling

curses.ACS_TTEE[¶](https://docs.python.org/3/library/curses.html#curses.ACS_TTEE "Link to this definition")
| top tee

curses.ACS_UARROW[¶](https://docs.python.org/3/library/curses.html#curses.ACS_UARROW "Link to this definition")
| up arrow

curses.ACS_ULCORNER[¶](https://docs.python.org/3/library/curses.html#curses.ACS_ULCORNER "Link to this definition")
| upper left corner

curses.ACS_URCORNER[¶](https://docs.python.org/3/library/curses.html#curses.ACS_URCORNER "Link to this definition")
| upper right corner

curses.ACS_VLINE[¶](https://docs.python.org/3/library/curses.html#curses.ACS_VLINE "Link to this definition")
| vertical line
The following table lists mouse button constants used by [`getmouse()`](https://docs.python.org/3/library/curses.html#curses.getmouse "curses.getmouse"):
Mouse button constant | Meaning
---|---

curses.BUTTONn_PRESSED[¶](https://docs.python.org/3/library/curses.html#curses.BUTTONn_PRESSED "Link to this definition")
| Mouse button _n_ pressed

curses.BUTTONn_RELEASED[¶](https://docs.python.org/3/library/curses.html#curses.BUTTONn_RELEASED "Link to this definition")
| Mouse button _n_ released

curses.BUTTONn_CLICKED[¶](https://docs.python.org/3/library/curses.html#curses.BUTTONn_CLICKED "Link to this definition")
| Mouse button _n_ clicked

curses.BUTTONn_DOUBLE_CLICKED[¶](https://docs.python.org/3/library/curses.html#curses.BUTTONn_DOUBLE_CLICKED "Link to this definition")
| Mouse button _n_ double clicked

curses.BUTTONn_TRIPLE_CLICKED[¶](https://docs.python.org/3/library/curses.html#curses.BUTTONn_TRIPLE_CLICKED "Link to this definition")
| Mouse button _n_ triple clicked

curses.BUTTON_SHIFT[¶](https://docs.python.org/3/library/curses.html#curses.BUTTON_SHIFT "Link to this definition")
| Shift was down during button state change

curses.BUTTON_CTRL[¶](https://docs.python.org/3/library/curses.html#curses.BUTTON_CTRL "Link to this definition")
| Control was down during button state change

curses.BUTTON_ALT[¶](https://docs.python.org/3/library/curses.html#curses.BUTTON_ALT "Link to this definition")
| Control was down during button state change
Changed in version 3.10: The `BUTTON5_*` constants are now exposed if they are provided by the underlying curses library.
The following table lists the predefined colors:
Constant | Color
---|---

curses.COLOR_BLACK[¶](https://docs.python.org/3/library/curses.html#curses.COLOR_BLACK "Link to this definition")
| Black

curses.COLOR_BLUE[¶](https://docs.python.org/3/library/curses.html#curses.COLOR_BLUE "Link to this definition")
| Blue

curses.COLOR_CYAN[¶](https://docs.python.org/3/library/curses.html#curses.COLOR_CYAN "Link to this definition")
| Cyan (light greenish blue)

curses.COLOR_GREEN[¶](https://docs.python.org/3/library/curses.html#curses.COLOR_GREEN "Link to this definition")
| Green

curses.COLOR_MAGENTA[¶](https://docs.python.org/3/library/curses.html#curses.COLOR_MAGENTA "Link to this definition")
| Magenta (purplish red)

curses.COLOR_RED[¶](https://docs.python.org/3/library/curses.html#curses.COLOR_RED "Link to this definition")
| Red

curses.COLOR_WHITE[¶](https://docs.python.org/3/library/curses.html#curses.COLOR_WHITE "Link to this definition")
| White

curses.COLOR_YELLOW[¶](https://docs.python.org/3/library/curses.html#curses.COLOR_YELLOW "Link to this definition")
| Yellow
