## Ttk Widgets[¶](https://docs.python.org/3/library/tkinter.ttk.html#ttk-widgets "Link to this heading")
Ttk comes with 18 widgets, twelve of which already existed in tkinter: `Button`, `Checkbutton`, `Entry`, `Frame`, `Label`, `LabelFrame`, `Menubutton`, `PanedWindow`, `Radiobutton`, `Scale`, `Scrollbar`, and [`Spinbox`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Spinbox "tkinter.ttk.Spinbox"). The other six are new: [`Combobox`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Combobox "tkinter.ttk.Combobox"), [`Notebook`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Notebook "tkinter.ttk.Notebook"), [`Progressbar`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Progressbar "tkinter.ttk.Progressbar"), `Separator`, `Sizegrip` and [`Treeview`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview "tkinter.ttk.Treeview"). And all them are subclasses of [`Widget`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Widget "tkinter.ttk.Widget").
Using the Ttk widgets gives the application an improved look and feel. As discussed above, there are differences in how the styling is coded.
Tk code:
Copy```
l1 = tkinter.Label(text="Test", fg="black", bg="white")
l2 = tkinter.Label(text="Test", fg="black", bg="white")

```

Ttk code:
Copy```
style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="white")

l1 = ttk.Label(text="Test", style="BW.TLabel")
l2 = ttk.Label(text="Test", style="BW.TLabel")

```

For more information about [TtkStyling](https://docs.python.org/3/library/tkinter.ttk.html#ttkstyling), see the [`Style`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Style "tkinter.ttk.Style") class documentation.
