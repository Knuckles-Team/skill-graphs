## Progressbar[¶](https://docs.python.org/3/library/tkinter.ttk.html#progressbar "Link to this heading")
The `ttk.Progressbar` widget shows the status of a long-running operation. It can operate in two modes: 1) the determinate mode which shows the amount completed relative to the total amount of work to be done and 2) the indeterminate mode which provides an animated display to let the user know that work is progressing.
### Options[¶](https://docs.python.org/3/library/tkinter.ttk.html#id5 "Link to this heading")
This widget accepts the following specific options:
Option | Description
---|---
orient | One of “horizontal” or “vertical”. Specifies the orientation of the progress bar.
length | Specifies the length of the long axis of the progress bar (width if horizontal, height if vertical).
mode | One of “determinate” or “indeterminate”.
maximum | A number specifying the maximum value. Defaults to 100.
value | The current value of the progress bar. In “determinate” mode, this represents the amount of work completed. In “indeterminate” mode, it is interpreted as modulo _maximum_ ; that is, the progress bar completes one “cycle” when its value increases by _maximum_.
variable | A name which is linked to the option value. If specified, the value of the progress bar is automatically set to the value of this name whenever the latter is modified.
phase | Read-only option. The widget periodically increments the value of this option whenever its value is greater than 0 and, in determinate mode, less than maximum. This option may be used by the current theme to provide additional animation effects.
### ttk.Progressbar[¶](https://docs.python.org/3/library/tkinter.ttk.html#ttk-progressbar "Link to this heading")

_class_ tkinter.ttk.Progressbar[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Progressbar "Link to this definition")


start(_interval =None_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Progressbar.start "Link to this definition")

Begin autoincrement mode: schedules a recurring timer event that calls [`Progressbar.step()`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Progressbar.step "tkinter.ttk.Progressbar.step") every _interval_ milliseconds. If omitted, _interval_ defaults to 50 milliseconds.

step(_amount =None_)[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Progressbar.step "Link to this definition")

Increments the progress bar’s value by _amount_.
_amount_ defaults to 1.0 if omitted.

stop()[¶](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Progressbar.stop "Link to this definition")

Stop autoincrement mode: cancels any recurring timer event initiated by [`Progressbar.start()`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Progressbar.start "tkinter.ttk.Progressbar.start") for this progress bar.
