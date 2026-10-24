[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`operator` — Standard operators as functions](https://docs.python.org/3/library/operator.html "previous chapter")
#### Next topic
[`pathlib` — Object-oriented filesystem paths](https://docs.python.org/3/library/pathlib.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=File+and+Directory+Access&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ffilesys.html&pagesource=library%2Ffilesys.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/pathlib.html "pathlib — Object-oriented filesystem paths") |
  * [previous](https://docs.python.org/3/library/operator.html "operator — Standard operators as functions") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [File and Directory Access](https://docs.python.org/3/library/filesys.html)
  * |
  * Theme  Auto Light Dark |


# File and Directory Access[¶](https://docs.python.org/3/library/filesys.html#file-and-directory-access "Link to this heading")
The modules described in this chapter deal with disk files and directories. For example, there are modules for reading the properties of files, manipulating paths in a portable way, and creating temporary files. The full list of modules in this chapter is:
  * [`pathlib` — Object-oriented filesystem paths](https://docs.python.org/3/library/pathlib.html)
    * [Basic use](https://docs.python.org/3/library/pathlib.html#basic-use)
    * [Exceptions](https://docs.python.org/3/library/pathlib.html#exceptions)
    * [Pure paths](https://docs.python.org/3/library/pathlib.html#pure-paths)
      * [General properties](https://docs.python.org/3/library/pathlib.html#general-properties)
      * [Operators](https://docs.python.org/3/library/pathlib.html#operators)
      * [Accessing individual parts](https://docs.python.org/3/library/pathlib.html#accessing-individual-parts)
      * [Methods and properties](https://docs.python.org/3/library/pathlib.html#methods-and-properties)
    * [Concrete paths](https://docs.python.org/3/library/pathlib.html#concrete-paths)
      * [Parsing and generating URIs](https://docs.python.org/3/library/pathlib.html#parsing-and-generating-uris)
      * [Expanding and resolving paths](https://docs.python.org/3/library/pathlib.html#expanding-and-resolving-paths)
      * [Querying file type and status](https://docs.python.org/3/library/pathlib.html#querying-file-type-and-status)
      * [Reading and writing files](https://docs.python.org/3/library/pathlib.html#reading-and-writing-files)
      * [Reading directories](https://docs.python.org/3/library/pathlib.html#reading-directories)
      * [Creating files and directories](https://docs.python.org/3/library/pathlib.html#creating-files-and-directories)
      * [Copying, moving and deleting](https://docs.python.org/3/library/pathlib.html#copying-moving-and-deleting)
      * [Permissions and ownership](https://docs.python.org/3/library/pathlib.html#permissions-and-ownership)
    * [Pattern language](https://docs.python.org/3/library/pathlib.html#pattern-language)
    * [Comparison to the `glob` module](https://docs.python.org/3/library/pathlib.html#comparison-to-the-glob-module)
    * [Comparison to the `os` and `os.path` modules](https://docs.python.org/3/library/pathlib.html#comparison-to-the-os-and-os-path-modules)
      * [Corresponding tools](https://docs.python.org/3/library/pathlib.html#corresponding-tools)
    * [Protocols](https://docs.python.org/3/library/pathlib.html#module-pathlib.types)
  * [`os.path` — Common pathname manipulations](https://docs.python.org/3/library/os.path.html)
  * [`stat` — Interpreting `stat()` results](https://docs.python.org/3/library/stat.html)
  * [`filecmp` — File and Directory Comparisons](https://docs.python.org/3/library/filecmp.html)
    * [The `dircmp` class](https://docs.python.org/3/library/filecmp.html#the-dircmp-class)
  * [`tempfile` — Generate temporary files and directories](https://docs.python.org/3/library/tempfile.html)
    * [Examples](https://docs.python.org/3/library/tempfile.html#examples)
    * [Deprecated functions and variables](https://docs.python.org/3/library/tempfile.html#deprecated-functions-and-variables)
  * [`glob` — Unix style pathname pattern expansion](https://docs.python.org/3/library/glob.html)
    * [Examples](https://docs.python.org/3/library/glob.html#examples)
  * [`fnmatch` — Unix filename pattern matching](https://docs.python.org/3/library/fnmatch.html)
  * [`linecache` — Random access to text lines](https://docs.python.org/3/library/linecache.html)
  * [`shutil` — High-level file operations](https://docs.python.org/3/library/shutil.html)
    * [Directory and files operations](https://docs.python.org/3/library/shutil.html#directory-and-files-operations)
      * [Platform-dependent efficient copy operations](https://docs.python.org/3/library/shutil.html#platform-dependent-efficient-copy-operations)
      * [copytree example](https://docs.python.org/3/library/shutil.html#copytree-example)
      * [rmtree example](https://docs.python.org/3/library/shutil.html#rmtree-example)
    * [Archiving operations](https://docs.python.org/3/library/shutil.html#archiving-operations)
      * [Archiving example](https://docs.python.org/3/library/shutil.html#archiving-example)
      * [Archiving example with _base_dir_](https://docs.python.org/3/library/shutil.html#archiving-example-with-base-dir)
    * [Querying the size of the output terminal](https://docs.python.org/3/library/shutil.html#querying-the-size-of-the-output-terminal)


See also

Module [`os`](https://docs.python.org/3/library/os.html#module-os "os: Miscellaneous operating system interfaces.")

Operating system interfaces, including functions to work with files at a lower level than Python [file objects](https://docs.python.org/3/glossary.html#term-file-object).

Module [`io`](https://docs.python.org/3/library/io.html#module-io "io: Core tools for working with streams.")

Python’s built-in I/O library, including both abstract classes and some concrete classes such as file I/O.

Built-in function [`open()`](https://docs.python.org/3/library/functions.html#open "open")

The standard way to open files for reading and writing with Python.
#### Previous topic
[`operator` — Standard operators as functions](https://docs.python.org/3/library/operator.html "previous chapter")
#### Next topic
[`pathlib` — Object-oriented filesystem paths](https://docs.python.org/3/library/pathlib.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=File+and+Directory+Access&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ffilesys.html&pagesource=library%2Ffilesys.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/pathlib.html "pathlib — Object-oriented filesystem paths") |
  * [previous](https://docs.python.org/3/library/operator.html "operator — Standard operators as functions") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [File and Directory Access](https://docs.python.org/3/library/filesys.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
