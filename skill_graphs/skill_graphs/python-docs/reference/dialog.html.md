[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [Tkinter Dialogs](https://docs.python.org/3/library/dialog.html)
    * [`tkinter.simpledialog` — Standard Tkinter input dialogs](https://docs.python.org/3/library/dialog.html#module-tkinter.simpledialog)
    * [`tkinter.filedialog` — File selection dialogs](https://docs.python.org/3/library/dialog.html#module-tkinter.filedialog)
      * [Native Load/Save Dialogs](https://docs.python.org/3/library/dialog.html#native-load-save-dialogs)
    * [`tkinter.commondialog` — Dialog window templates](https://docs.python.org/3/library/dialog.html#module-tkinter.commondialog)


#### Previous topic
[`tkinter.font` — Tkinter font wrapper](https://docs.python.org/3/library/tkinter.font.html "previous chapter")
#### Next topic
[`tkinter.messagebox` — Tkinter message prompts](https://docs.python.org/3/library/tkinter.messagebox.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Tkinter+Dialogs&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fdialog.html&pagesource=library%2Fdialog.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/tkinter.messagebox.html "tkinter.messagebox — Tkinter message prompts") |
  * [previous](https://docs.python.org/3/library/tkinter.font.html "tkinter.font — Tkinter font wrapper") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Graphical user interfaces with Tk](https://docs.python.org/3/library/tk.html) »
  * [Tkinter Dialogs](https://docs.python.org/3/library/dialog.html)
  * |
  * Theme  Auto Light Dark |


# Tkinter Dialogs[¶](https://docs.python.org/3/library/dialog.html#tkinter-dialogs "Link to this heading")
##  `tkinter.simpledialog` — Standard Tkinter input dialogs[¶](https://docs.python.org/3/library/dialog.html#module-tkinter.simpledialog "Link to this heading")
**Source code:**
* * *
The `tkinter.simpledialog` module contains convenience classes and functions for creating simple modal dialogs to get a value from the user.

tkinter.simpledialog.askfloat(_title_ , _prompt_ , _** kw_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.simpledialog.askfloat "Link to this definition")


tkinter.simpledialog.askinteger(_title_ , _prompt_ , _** kw_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.simpledialog.askinteger "Link to this definition")


tkinter.simpledialog.askstring(_title_ , _prompt_ , _** kw_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.simpledialog.askstring "Link to this definition")

The above three functions provide dialogs that prompt the user to enter a value of the desired type.

_class_ tkinter.simpledialog.Dialog(_parent_ , _title =None_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.simpledialog.Dialog "Link to this definition")

The base class for custom dialogs.

body(_master_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.simpledialog.Dialog.body "Link to this definition")

Override to construct the dialog’s interface and return the widget that should have initial focus.

buttonbox()[¶](https://docs.python.org/3/library/dialog.html#tkinter.simpledialog.Dialog.buttonbox "Link to this definition")

Default behaviour adds OK and Cancel buttons. Override for custom button layouts.
##  `tkinter.filedialog` — File selection dialogs[¶](https://docs.python.org/3/library/dialog.html#module-tkinter.filedialog "Link to this heading")
**Source code:**
* * *
The `tkinter.filedialog` module provides classes and factory functions for creating file/directory selection windows.
### Native Load/Save Dialogs[¶](https://docs.python.org/3/library/dialog.html#native-load-save-dialogs "Link to this heading")
The following classes and functions provide file dialog windows that combine a native look-and-feel with configuration options to customize behaviour. The following keyword arguments are applicable to the classes and functions listed below:
> _parent_ - the window to place the dialog on top of
> _title_ - the title of the window
> _initialdir_ - the directory that the dialog starts in
> _initialfile_ - the file selected upon opening of the dialog
> _filetypes_ - a sequence of (label, pattern) tuples, ‘*’ wildcard is allowed
> _defaultextension_ - default extension to append to file (save dialogs)
> _multiple_ - when true, selection of multiple items is allowed
**Static factory functions**
The below functions when called create a modal, native look-and-feel dialog, wait for the user’s selection, then return the selected value(s) or `None` to the caller.

tkinter.filedialog.askopenfile(_mode ='r'_, _** options_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.askopenfile "Link to this definition")


tkinter.filedialog.askopenfiles(_mode ='r'_, _** options_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.askopenfiles "Link to this definition")

The above two functions create an [`Open`](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.Open "tkinter.filedialog.Open") dialog and return the opened file object(s) in read-only mode.

tkinter.filedialog.asksaveasfile(_mode ='w'_, _** options_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.asksaveasfile "Link to this definition")

Create a [`SaveAs`](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.SaveAs "tkinter.filedialog.SaveAs") dialog and return a file object opened in write-only mode.

tkinter.filedialog.askopenfilename(_** options_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.askopenfilename "Link to this definition")


tkinter.filedialog.askopenfilenames(_** options_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.askopenfilenames "Link to this definition")

The above two functions create an [`Open`](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.Open "tkinter.filedialog.Open") dialog and return the selected filename(s) that correspond to existing file(s).

tkinter.filedialog.asksaveasfilename(_** options_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.asksaveasfilename "Link to this definition")

Create a [`SaveAs`](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.SaveAs "tkinter.filedialog.SaveAs") dialog and return the selected filename.

tkinter.filedialog.askdirectory(_** options_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.askdirectory "Link to this definition")

Prompt user to select a directory.
Additional keyword option:
_mustexist_ - determines if selection must be an existing directory.

_class_ tkinter.filedialog.Open(_master =None_, _** options_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.Open "Link to this definition")


_class_ tkinter.filedialog.SaveAs(_master =None_, _** options_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.SaveAs "Link to this definition")

The above two classes provide native dialog windows for saving and loading files.
**Convenience classes**
The below classes are used for creating file/directory windows from scratch. These do not emulate the native look-and-feel of the platform.

_class_ tkinter.filedialog.Directory(_master =None_, _** options_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.Directory "Link to this definition")

Create a dialog prompting the user to select a directory.
Note
The _FileDialog_ class should be subclassed for custom event handling and behaviour.

_class_ tkinter.filedialog.FileDialog(_master_ , _title =None_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.FileDialog "Link to this definition")

Create a basic file selection dialog.

cancel_command(_event =None_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.FileDialog.cancel_command "Link to this definition")

Trigger the termination of the dialog window.

dirs_double_event(_event_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.FileDialog.dirs_double_event "Link to this definition")

Event handler for double-click event on directory.

dirs_select_event(_event_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.FileDialog.dirs_select_event "Link to this definition")

Event handler for click event on directory.

files_double_event(_event_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.FileDialog.files_double_event "Link to this definition")

Event handler for double-click event on file.

files_select_event(_event_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.FileDialog.files_select_event "Link to this definition")

Event handler for single-click event on file.

filter_command(_event =None_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.FileDialog.filter_command "Link to this definition")

Filter the files by directory.

get_filter()[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.FileDialog.get_filter "Link to this definition")

Retrieve the file filter currently in use.

get_selection()[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.FileDialog.get_selection "Link to this definition")

Retrieve the currently selected item.

go(_dir_or_file =os.curdir_, _pattern ='*'_, _default =''_, _key =None_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.FileDialog.go "Link to this definition")

Render dialog and start event loop.

ok_event(_event_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.FileDialog.ok_event "Link to this definition")

Exit dialog returning current selection.

quit(_how =None_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.FileDialog.quit "Link to this definition")

Exit dialog returning filename, if any.

set_filter(_dir_ , _pat_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.FileDialog.set_filter "Link to this definition")

Set the file filter.

set_selection(_file_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.FileDialog.set_selection "Link to this definition")

Update the current file selection to _file_.

_class_ tkinter.filedialog.LoadFileDialog(_master_ , _title =None_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.LoadFileDialog "Link to this definition")

A subclass of FileDialog that creates a dialog window for selecting an existing file.

ok_command()[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.LoadFileDialog.ok_command "Link to this definition")

Test that a file is provided and that the selection indicates an already existing file.

_class_ tkinter.filedialog.SaveFileDialog(_master_ , _title =None_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.SaveFileDialog "Link to this definition")

A subclass of FileDialog that creates a dialog window for selecting a destination file.

ok_command()[¶](https://docs.python.org/3/library/dialog.html#tkinter.filedialog.SaveFileDialog.ok_command "Link to this definition")

Test whether or not the selection points to a valid file that is not a directory. Confirmation is required if an already existing file is selected.
##  `tkinter.commondialog` — Dialog window templates[¶](https://docs.python.org/3/library/dialog.html#module-tkinter.commondialog "Link to this heading")
**Source code:**
* * *
The `tkinter.commondialog` module provides the [`Dialog`](https://docs.python.org/3/library/dialog.html#tkinter.commondialog.Dialog "tkinter.commondialog.Dialog") class that is the base class for dialogs defined in other supporting modules.

_class_ tkinter.commondialog.Dialog(_master =None_, _** options_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.commondialog.Dialog "Link to this definition")


show(_** options_)[¶](https://docs.python.org/3/library/dialog.html#tkinter.commondialog.Dialog.show "Link to this definition")

Render the Dialog window.
See also
Modules [`tkinter.messagebox`](https://docs.python.org/3/library/tkinter.messagebox.html#module-tkinter.messagebox "tkinter.messagebox: Various types of alert dialogs"), [Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#tut-files)
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [Tkinter Dialogs](https://docs.python.org/3/library/dialog.html)
    * [`tkinter.simpledialog` — Standard Tkinter input dialogs](https://docs.python.org/3/library/dialog.html#module-tkinter.simpledialog)
    * [`tkinter.filedialog` — File selection dialogs](https://docs.python.org/3/library/dialog.html#module-tkinter.filedialog)
      * [Native Load/Save Dialogs](https://docs.python.org/3/library/dialog.html#native-load-save-dialogs)
    * [`tkinter.commondialog` — Dialog window templates](https://docs.python.org/3/library/dialog.html#module-tkinter.commondialog)


#### Previous topic
[`tkinter.font` — Tkinter font wrapper](https://docs.python.org/3/library/tkinter.font.html "previous chapter")
#### Next topic
[`tkinter.messagebox` — Tkinter message prompts](https://docs.python.org/3/library/tkinter.messagebox.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Tkinter+Dialogs&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fdialog.html&pagesource=library%2Fdialog.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/tkinter.messagebox.html "tkinter.messagebox — Tkinter message prompts") |
  * [previous](https://docs.python.org/3/library/tkinter.font.html "tkinter.font — Tkinter font wrapper") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Graphical user interfaces with Tk](https://docs.python.org/3/library/tk.html) »
  * [Tkinter Dialogs](https://docs.python.org/3/library/dialog.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
