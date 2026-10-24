[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[Tkinter Dialogs](https://docs.python.org/3/library/dialog.html "previous chapter")
#### Next topic
[`tkinter.scrolledtext` — Scrolled Text Widget](https://docs.python.org/3/library/tkinter.scrolledtext.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=tkinter.messagebox+%E2%80%94+Tkinter+message+prompts&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ftkinter.messagebox.html&pagesource=library%2Ftkinter.messagebox.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/tkinter.scrolledtext.html "tkinter.scrolledtext — Scrolled Text Widget") |
  * [previous](https://docs.python.org/3/library/dialog.html "Tkinter Dialogs") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Graphical user interfaces with Tk](https://docs.python.org/3/library/tk.html) »
  * [`tkinter.messagebox` — Tkinter message prompts](https://docs.python.org/3/library/tkinter.messagebox.html)
  * |
  * Theme  Auto Light Dark |


#  `tkinter.messagebox` — Tkinter message prompts[¶](https://docs.python.org/3/library/tkinter.messagebox.html#module-tkinter.messagebox "Link to this heading")
**Source code:**
* * *
The `tkinter.messagebox` module provides a template base class as well as a variety of convenience methods for commonly used configurations. The message boxes are modal and will return a subset of (`True`, `False`, `None`, [`OK`](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.OK "tkinter.messagebox.OK"), [`CANCEL`](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.CANCEL "tkinter.messagebox.CANCEL"), [`YES`](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.YES "tkinter.messagebox.YES"), [`NO`](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.NO "tkinter.messagebox.NO")) based on the user’s selection. Common message box styles and layouts include but are not limited to:
![../_images/tk_msg.png](https://docs.python.org/3/_images/tk_msg.png)

_class_ tkinter.messagebox.Message(_master =None_, _** options_)[¶](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.Message "Link to this definition")

Create a message window with an application-specified message, an icon and a set of buttons. Each of the buttons in the message window is identified by a unique symbolic name (see the _type_ options).
The following options are supported:
>

_command_

> Specifies the function to invoke when the user closes the dialog. The name of the button clicked by the user to close the dialog is passed as argument. This is only available on macOS.

_default_

> Gives the [symbolic name](https://docs.python.org/3/library/tkinter.messagebox.html#messagebox-buttons) of the default button for this message window ([`OK`](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.OK "tkinter.messagebox.OK"), [`CANCEL`](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.CANCEL "tkinter.messagebox.CANCEL"), and so on). If this option is not specified, the first button in the dialog will be made the default.

_detail_

> Specifies an auxiliary message to the main message given by the _message_ option. The message detail will be presented beneath the main message and, where supported by the OS, in a less emphasized font than the main message.

_icon_

> Specifies an [icon](https://docs.python.org/3/library/tkinter.messagebox.html#messagebox-icons) to display. If this option is not specified, then the [`INFO`](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.INFO "tkinter.messagebox.INFO") icon will be displayed.

_message_

> Specifies the message to display in this message box. The default value is an empty string.

_parent_

> Makes the specified window the logical parent of the message box. The message box is displayed on top of its parent window.

_title_

> Specifies a string to display as the title of the message box. This option is ignored on macOS, where platform guidelines forbid the use of a title on this kind of dialog.

_type_

> Arranges for a [predefined set of buttons](https://docs.python.org/3/library/tkinter.messagebox.html#messagebox-types) to be displayed.

show(_** options_)[¶](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.Message.show "Link to this definition")

Display a message window and wait for the user to select one of the buttons. Then return the symbolic name of the selected button. Keyword arguments can override options specified in the constructor.
**Information message box**

tkinter.messagebox.showinfo(_title =None_, _message =None_, _** options_)[¶](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.showinfo "Link to this definition")

Creates and displays an information message box with the specified title and message.
**Warning message boxes**

tkinter.messagebox.showwarning(_title =None_, _message =None_, _** options_)[¶](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.showwarning "Link to this definition")

Creates and displays a warning message box with the specified title and message.

tkinter.messagebox.showerror(_title =None_, _message =None_, _** options_)[¶](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.showerror "Link to this definition")

Creates and displays an error message box with the specified title and message.
**Question message boxes**

tkinter.messagebox.askquestion(_title =None_, _message =None_, _*_ , _type =YESNO_, _** options_)[¶](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.askquestion "Link to this definition")

Ask a question. By default shows buttons [`YES`](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.YES "tkinter.messagebox.YES") and [`NO`](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.NO "tkinter.messagebox.NO"). Returns the symbolic name of the selected button.

tkinter.messagebox.askokcancel(_title =None_, _message =None_, _** options_)[¶](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.askokcancel "Link to this definition")

Ask if operation should proceed. Shows buttons [`OK`](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.OK "tkinter.messagebox.OK") and [`CANCEL`](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.CANCEL "tkinter.messagebox.CANCEL"). Returns `True` if the answer is ok and `False` otherwise.

tkinter.messagebox.askretrycancel(_title =None_, _message =None_, _** options_)[¶](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.askretrycancel "Link to this definition")

Ask if operation should be retried. Shows buttons [`RETRY`](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.RETRY "tkinter.messagebox.RETRY") and [`CANCEL`](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.CANCEL "tkinter.messagebox.CANCEL"). Return `True` if the answer is yes and `False` otherwise.

tkinter.messagebox.askyesno(_title =None_, _message =None_, _** options_)[¶](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.askyesno "Link to this definition")

Ask a question. Shows buttons [`YES`](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.YES "tkinter.messagebox.YES") and [`NO`](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.NO "tkinter.messagebox.NO"). Returns `True` if the answer is yes and `False` otherwise.

tkinter.messagebox.askyesnocancel(_title =None_, _message =None_, _** options_)[¶](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.askyesnocancel "Link to this definition")

Ask a question. Shows buttons [`YES`](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.YES "tkinter.messagebox.YES"), [`NO`](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.NO "tkinter.messagebox.NO") and [`CANCEL`](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.CANCEL "tkinter.messagebox.CANCEL"). Return `True` if the answer is yes, `None` if cancelled, and `False` otherwise.
Symbolic names of buttons:

tkinter.messagebox.ABORT _= 'abort'_[¶](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.ABORT "Link to this definition")


tkinter.messagebox.RETRY _= 'retry'_[¶](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.RETRY "Link to this definition")


tkinter.messagebox.IGNORE _= 'ignore'_[¶](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.IGNORE "Link to this definition")


tkinter.messagebox.OK _= 'ok'_[¶](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.OK "Link to this definition")


tkinter.messagebox.CANCEL _= 'cancel'_[¶](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.CANCEL "Link to this definition")


tkinter.messagebox.YES _= 'yes'_[¶](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.YES "Link to this definition")


tkinter.messagebox.NO _= 'no'_[¶](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.NO "Link to this definition")

Predefined sets of buttons:

tkinter.messagebox.ABORTRETRYIGNORE _= 'abortretryignore'_[¶](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.ABORTRETRYIGNORE "Link to this definition")

Displays three buttons whose symbolic names are [`ABORT`](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.ABORT "tkinter.messagebox.ABORT"), [`RETRY`](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.RETRY "tkinter.messagebox.RETRY") and [`IGNORE`](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.IGNORE "tkinter.messagebox.IGNORE").

tkinter.messagebox.OK _= 'ok'_

Displays one button whose symbolic name is `OK`.

tkinter.messagebox.OKCANCEL _= 'okcancel'_[¶](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.OKCANCEL "Link to this definition")

Displays two buttons whose symbolic names are [`OK`](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.OK "tkinter.messagebox.OK") and [`CANCEL`](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.CANCEL "tkinter.messagebox.CANCEL").

tkinter.messagebox.RETRYCANCEL _= 'retrycancel'_[¶](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.RETRYCANCEL "Link to this definition")

Displays two buttons whose symbolic names are [`RETRY`](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.RETRY "tkinter.messagebox.RETRY") and [`CANCEL`](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.CANCEL "tkinter.messagebox.CANCEL").

tkinter.messagebox.YESNO _= 'yesno'_[¶](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.YESNO "Link to this definition")

Displays two buttons whose symbolic names are [`YES`](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.YES "tkinter.messagebox.YES") and [`NO`](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.NO "tkinter.messagebox.NO").

tkinter.messagebox.YESNOCANCEL _= 'yesnocancel'_[¶](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.YESNOCANCEL "Link to this definition")

Displays three buttons whose symbolic names are [`YES`](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.YES "tkinter.messagebox.YES"), [`NO`](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.NO "tkinter.messagebox.NO") and [`CANCEL`](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.CANCEL "tkinter.messagebox.CANCEL").
Icon images:

tkinter.messagebox.ERROR _= 'error'_[¶](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.ERROR "Link to this definition")


tkinter.messagebox.INFO _= 'info'_[¶](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.INFO "Link to this definition")


tkinter.messagebox.QUESTION _= 'question'_[¶](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.QUESTION "Link to this definition")


tkinter.messagebox.WARNING _= 'warning'_[¶](https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.WARNING "Link to this definition")

#### Previous topic
[Tkinter Dialogs](https://docs.python.org/3/library/dialog.html "previous chapter")
#### Next topic
[`tkinter.scrolledtext` — Scrolled Text Widget](https://docs.python.org/3/library/tkinter.scrolledtext.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=tkinter.messagebox+%E2%80%94+Tkinter+message+prompts&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ftkinter.messagebox.html&pagesource=library%2Ftkinter.messagebox.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/tkinter.scrolledtext.html "tkinter.scrolledtext — Scrolled Text Widget") |
  * [previous](https://docs.python.org/3/library/dialog.html "Tkinter Dialogs") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Graphical user interfaces with Tk](https://docs.python.org/3/library/tk.html) »
  * [`tkinter.messagebox` — Tkinter message prompts](https://docs.python.org/3/library/tkinter.messagebox.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
  *[*]: Keyword-only parameters separator (PEP 3102)
