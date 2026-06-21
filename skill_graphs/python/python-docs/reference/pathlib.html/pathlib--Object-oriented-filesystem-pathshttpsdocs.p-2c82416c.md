#  `pathlib` — Object-oriented filesystem paths[¶](https://docs.python.org/3/library/pathlib.html#module-pathlib "Link to this heading")
Added in version 3.4.
**Source code:**
* * *
This module offers classes representing filesystem paths with semantics appropriate for different operating systems. Path classes are divided between [pure paths](https://docs.python.org/3/library/pathlib.html#pure-paths), which provide purely computational operations without I/O, and [concrete paths](https://docs.python.org/3/library/pathlib.html#concrete-paths), which inherit from pure paths but also provide I/O operations.
![Inheritance diagram showing the classes available in pathlib. The most basic class is PurePath, which has three direct subclasses: PurePosixPath, PureWindowsPath, and Path. Further to these four classes, there are two classes that use multiple inheritance: PosixPath subclasses PurePosixPath and Path, and WindowsPath subclasses PureWindowsPath and Path.](https://docs.python.org/3/_images/pathlib-inheritance.png)
If you’ve never used this module before or just aren’t sure which class is right for your task, [`Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path") is most likely what you need. It instantiates a [concrete path](https://docs.python.org/3/library/pathlib.html#concrete-paths) for the platform the code is running on.
Pure paths are useful in some special cases; for example:
  1. If you want to manipulate Windows paths on a Unix machine (or vice versa). You cannot instantiate a [`WindowsPath`](https://docs.python.org/3/library/pathlib.html#pathlib.WindowsPath "pathlib.WindowsPath") when running on Unix, but you can instantiate [`PureWindowsPath`](https://docs.python.org/3/library/pathlib.html#pathlib.PureWindowsPath "pathlib.PureWindowsPath").
  2. You want to make sure that your code only manipulates paths without actually accessing the OS. In this case, instantiating one of the pure classes may be useful since those simply don’t have any OS-accessing operations.


See also
[**PEP 428**](https://peps.python.org/pep-0428/): The pathlib module – object-oriented filesystem paths.
See also
For low-level path manipulation on strings, you can also use the [`os.path`](https://docs.python.org/3/library/os.path.html#module-os.path "os.path: Operations on pathnames.") module.
