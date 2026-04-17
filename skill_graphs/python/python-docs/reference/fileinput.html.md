[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`getpass` — Portable password input](https://docs.python.org/3/library/getpass.html "previous chapter")
#### Next topic
[`curses` — Terminal handling for character-cell displays](https://docs.python.org/3/library/curses.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=fileinput+%E2%80%94+Iterate+over+lines+from+multiple+input+streams&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ffileinput.html&pagesource=library%2Ffileinput.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/curses.html "curses — Terminal handling for character-cell displays") |
  * [previous](https://docs.python.org/3/library/getpass.html "getpass — Portable password input") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Command-line interface libraries](https://docs.python.org/3/library/cmdlinelibs.html) »
  * [`fileinput` — Iterate over lines from multiple input streams](https://docs.python.org/3/library/fileinput.html)
  * |
  * Theme  Auto Light Dark |


#  `fileinput` — Iterate over lines from multiple input streams[¶](https://docs.python.org/3/library/fileinput.html#module-fileinput "Link to this heading")
**Source code:**
* * *
This module implements a helper class and functions to quickly write a loop over standard input or a list of files. If you just want to read or write one file see [`open()`](https://docs.python.org/3/library/functions.html#open "open").
The typical use is:
Copy```
import fileinput
for line in fileinput.input(encoding="utf-8"):
    process(line)

```

This iterates over the lines of all files listed in `sys.argv[1:]`, defaulting to `sys.stdin` if the list is empty. If a filename is `'-'`, it is also replaced by `sys.stdin` and the optional arguments _mode_ and _openhook_ are ignored. To specify an alternative list of filenames, pass it as the first argument to [`input()`](https://docs.python.org/3/library/fileinput.html#fileinput.input "fileinput.input"). A single file name is also allowed.
All files are opened in text mode by default, but you can override this by specifying the _mode_ parameter in the call to [`input()`](https://docs.python.org/3/library/fileinput.html#fileinput.input "fileinput.input") or [`FileInput`](https://docs.python.org/3/library/fileinput.html#fileinput.FileInput "fileinput.FileInput"). If an I/O error occurs during opening or reading a file, [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") is raised.
Changed in version 3.3: [`IOError`](https://docs.python.org/3/library/exceptions.html#IOError "IOError") used to be raised; it is now an alias of [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError").
If `sys.stdin` is used more than once, the second and further use will return no lines, except perhaps for interactive use, or if it has been explicitly reset (e.g. using `sys.stdin.seek(0)`).
Empty files are opened and immediately closed; the only time their presence in the list of filenames is noticeable at all is when the last file opened is empty.
Lines are returned with any newlines intact, which means that the last line in a file may not have one.
You can control how files are opened by providing an opening hook via the _openhook_ parameter to [`fileinput.input()`](https://docs.python.org/3/library/fileinput.html#fileinput.input "fileinput.input") or [`FileInput()`](https://docs.python.org/3/library/fileinput.html#fileinput.FileInput "fileinput.FileInput"). The hook must be a function that takes two arguments, _filename_ and _mode_ , and returns an accordingly opened file-like object. If _encoding_ and/or _errors_ are specified, they will be passed to the hook as additional keyword arguments. This module provides a [`hook_compressed()`](https://docs.python.org/3/library/fileinput.html#fileinput.hook_compressed "fileinput.hook_compressed") to support compressed files.
The following function is the primary interface of this module:

fileinput.input(_files =None_, _inplace =False_, _backup =''_, _*_ , _mode ='r'_, _openhook =None_, _encoding =None_, _errors =None_)[¶](https://docs.python.org/3/library/fileinput.html#fileinput.input "Link to this definition")

Create an instance of the [`FileInput`](https://docs.python.org/3/library/fileinput.html#fileinput.FileInput "fileinput.FileInput") class. The instance will be used as global state for the functions of this module, and is also returned to use during iteration. The parameters to this function will be passed along to the constructor of the `FileInput` class.
The [`FileInput`](https://docs.python.org/3/library/fileinput.html#fileinput.FileInput "fileinput.FileInput") instance can be used as a context manager in the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement. In this example, _input_ is closed after the `with` statement is exited, even if an exception occurs:
Copy```
with fileinput.input(files=('spam.txt', 'eggs.txt'), encoding="utf-8") as f:
    for line in f:
        process(line)

```

Changed in version 3.2: Can be used as a context manager.
Changed in version 3.8: The keyword parameters _mode_ and _openhook_ are now keyword-only.
Changed in version 3.10: The keyword-only parameter _encoding_ and _errors_ are added.
The following functions use the global state created by [`fileinput.input()`](https://docs.python.org/3/library/fileinput.html#fileinput.input "fileinput.input"); if there is no active state, [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError") is raised.

fileinput.filename()[¶](https://docs.python.org/3/library/fileinput.html#fileinput.filename "Link to this definition")

Return the name of the file currently being read. Before the first line has been read, returns `None`.

fileinput.fileno()[¶](https://docs.python.org/3/library/fileinput.html#fileinput.fileno "Link to this definition")

Return the integer “file descriptor” for the current file. When no file is opened (before the first line and between files), returns `-1`.

fileinput.lineno()[¶](https://docs.python.org/3/library/fileinput.html#fileinput.lineno "Link to this definition")

Return the cumulative line number of the line that has just been read. Before the first line has been read, returns `0`. After the last line of the last file has been read, returns the line number of that line.

fileinput.filelineno()[¶](https://docs.python.org/3/library/fileinput.html#fileinput.filelineno "Link to this definition")

Return the line number in the current file. Before the first line has been read, returns `0`. After the last line of the last file has been read, returns the line number of that line within the file.

fileinput.isfirstline()[¶](https://docs.python.org/3/library/fileinput.html#fileinput.isfirstline "Link to this definition")

Return `True` if the line just read is the first line of its file, otherwise return `False`.

fileinput.isstdin()[¶](https://docs.python.org/3/library/fileinput.html#fileinput.isstdin "Link to this definition")

Return `True` if the last line was read from `sys.stdin`, otherwise return `False`.

fileinput.nextfile()[¶](https://docs.python.org/3/library/fileinput.html#fileinput.nextfile "Link to this definition")

Close the current file so that the next iteration will read the first line from the next file (if any); lines not read from the file will not count towards the cumulative line count. The filename is not changed until after the first line of the next file has been read. Before the first line has been read, this function has no effect; it cannot be used to skip the first file. After the last line of the last file has been read, this function has no effect.

fileinput.close()[¶](https://docs.python.org/3/library/fileinput.html#fileinput.close "Link to this definition")

Close the sequence.
The class which implements the sequence behavior provided by the module is available for subclassing as well:

_class_ fileinput.FileInput(_files =None_, _inplace =False_, _backup =''_, _*_ , _mode ='r'_, _openhook =None_, _encoding =None_, _errors =None_)[¶](https://docs.python.org/3/library/fileinput.html#fileinput.FileInput "Link to this definition")

Class `FileInput` is the implementation; its methods [`filename()`](https://docs.python.org/3/library/fileinput.html#fileinput.filename "fileinput.filename"), [`fileno()`](https://docs.python.org/3/library/fileinput.html#fileinput.fileno "fileinput.fileno"), [`lineno()`](https://docs.python.org/3/library/fileinput.html#fileinput.lineno "fileinput.lineno"), [`filelineno()`](https://docs.python.org/3/library/fileinput.html#fileinput.filelineno "fileinput.filelineno"), [`isfirstline()`](https://docs.python.org/3/library/fileinput.html#fileinput.isfirstline "fileinput.isfirstline"), [`isstdin()`](https://docs.python.org/3/library/fileinput.html#fileinput.isstdin "fileinput.isstdin"), [`nextfile()`](https://docs.python.org/3/library/fileinput.html#fileinput.nextfile "fileinput.nextfile") and [`close()`](https://docs.python.org/3/library/fileinput.html#fileinput.close "fileinput.close") correspond to the functions of the same name in the module. In addition it is [iterable](https://docs.python.org/3/glossary.html#term-iterable) and has a [`readline()`](https://docs.python.org/3/library/io.html#io.TextIOBase.readline "io.TextIOBase.readline") method which returns the next input line. The sequence must be accessed in strictly sequential order; random access and `readline()` cannot be mixed.
With _mode_ you can specify which file mode will be passed to [`open()`](https://docs.python.org/3/library/functions.html#open "open"). It must be one of `'r'` and `'rb'`.
The _openhook_ , when given, must be a function that takes two arguments, _filename_ and _mode_ , and returns an accordingly opened file-like object. You cannot use _inplace_ and _openhook_ together.
You can specify _encoding_ and _errors_ that is passed to [`open()`](https://docs.python.org/3/library/functions.html#open "open") or _openhook_.
A `FileInput` instance can be used as a context manager in the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement. In this example, _input_ is closed after the `with` statement is exited, even if an exception occurs:
Copy```
with FileInput(files=('spam.txt', 'eggs.txt')) as input:
    process(input)

```

Changed in version 3.2: Can be used as a context manager.
Changed in version 3.8: The keyword parameter _mode_ and _openhook_ are now keyword-only.
Changed in version 3.10: The keyword-only parameter _encoding_ and _errors_ are added.
Changed in version 3.11: The `'rU'` and `'U'` modes and the `__getitem__()` method have been removed.
**Optional in-place filtering:** if the keyword argument `inplace=True` is passed to [`fileinput.input()`](https://docs.python.org/3/library/fileinput.html#fileinput.input "fileinput.input") or to the [`FileInput`](https://docs.python.org/3/library/fileinput.html#fileinput.FileInput "fileinput.FileInput") constructor, the file is moved to a backup file and standard output is directed to the input file (if a file of the same name as the backup file already exists, it will be replaced silently). This makes it possible to write a filter that rewrites its input file in place. If the _backup_ parameter is given (typically as `backup='.<some extension>'`), it specifies the extension for the backup file, and the backup file remains around; by default, the extension is `'.bak'` and it is deleted when the output file is closed. In-place filtering is disabled when standard input is read.
The two following opening hooks are provided by this module:

fileinput.hook_compressed(_filename_ , _mode_ , _*_ , _encoding =None_, _errors =None_)[¶](https://docs.python.org/3/library/fileinput.html#fileinput.hook_compressed "Link to this definition")

Transparently opens files compressed with gzip and bzip2 (recognized by the extensions `'.gz'` and `'.bz2'`) using the [`gzip`](https://docs.python.org/3/library/gzip.html#module-gzip "gzip: Interfaces for gzip compression and decompression using file objects.") and [`bz2`](https://docs.python.org/3/library/bz2.html#module-bz2 "bz2: Interfaces for bzip2 compression and decompression.") modules. If the filename extension is not `'.gz'` or `'.bz2'`, the file is opened normally (ie, using [`open()`](https://docs.python.org/3/library/functions.html#open "open") without any decompression).
The _encoding_ and _errors_ values are passed to [`io.TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper") for compressed files and open for normal files.
Usage example: `fi = fileinput.FileInput(openhook=fileinput.hook_compressed, encoding="utf-8")`
Changed in version 3.10: The keyword-only parameter _encoding_ and _errors_ are added.

fileinput.hook_encoded(_encoding_ , _errors =None_)[¶](https://docs.python.org/3/library/fileinput.html#fileinput.hook_encoded "Link to this definition")

Returns a hook which opens each file with [`open()`](https://docs.python.org/3/library/functions.html#open "open"), using the given _encoding_ and _errors_ to read the file.
Usage example: `fi = fileinput.FileInput(openhook=fileinput.hook_encoded("utf-8", "surrogateescape"))`
Changed in version 3.6: Added the optional _errors_ parameter.
Deprecated since version 3.10: This function is deprecated since [`fileinput.input()`](https://docs.python.org/3/library/fileinput.html#fileinput.input "fileinput.input") and [`FileInput`](https://docs.python.org/3/library/fileinput.html#fileinput.FileInput "fileinput.FileInput") now have _encoding_ and _errors_ parameters.
#### Previous topic
[`getpass` — Portable password input](https://docs.python.org/3/library/getpass.html "previous chapter")
#### Next topic
[`curses` — Terminal handling for character-cell displays](https://docs.python.org/3/library/curses.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=fileinput+%E2%80%94+Iterate+over+lines+from+multiple+input+streams&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ffileinput.html&pagesource=library%2Ffileinput.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/curses.html "curses — Terminal handling for character-cell displays") |
  * [previous](https://docs.python.org/3/library/getpass.html "getpass — Portable password input") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Command-line interface libraries](https://docs.python.org/3/library/cmdlinelibs.html) »
  * [`fileinput` — Iterate over lines from multiple input streams](https://docs.python.org/3/library/fileinput.html)
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
