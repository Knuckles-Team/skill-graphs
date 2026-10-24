[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`fnmatch` — Unix filename pattern matching](https://docs.python.org/3/library/fnmatch.html "previous chapter")
#### Next topic
[`shutil` — High-level file operations](https://docs.python.org/3/library/shutil.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=linecache+%E2%80%94+Random+access+to+text+lines&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Flinecache.html&pagesource=library%2Flinecache.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/shutil.html "shutil — High-level file operations") |
  * [previous](https://docs.python.org/3/library/fnmatch.html "fnmatch — Unix filename pattern matching") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [File and Directory Access](https://docs.python.org/3/library/filesys.html) »
  * [`linecache` — Random access to text lines](https://docs.python.org/3/library/linecache.html)
  * |
  * Theme  Auto Light Dark |


#  `linecache` — Random access to text lines[¶](https://docs.python.org/3/library/linecache.html#module-linecache "Link to this heading")
**Source code:**
* * *
The `linecache` module allows one to get any line from a Python source file, while attempting to optimize internally, using a cache, the common case where many lines are read from a single file. This is used by the [`traceback`](https://docs.python.org/3/library/traceback.html#module-traceback "traceback: Print or retrieve a stack traceback.") module to retrieve source lines for inclusion in the formatted traceback.
The [`tokenize.open()`](https://docs.python.org/3/library/tokenize.html#tokenize.open "tokenize.open") function is used to open files. This function uses [`tokenize.detect_encoding()`](https://docs.python.org/3/library/tokenize.html#tokenize.detect_encoding "tokenize.detect_encoding") to get the encoding of the file; in the absence of an encoding token, the file encoding defaults to UTF-8.
The `linecache` module defines the following functions:

linecache.getline(_filename_ , _lineno_ , _module_globals =None_)[¶](https://docs.python.org/3/library/linecache.html#linecache.getline "Link to this definition")

Get line _lineno_ from file named _filename_. This function will never raise an exception — it will return `''` on errors (the terminating newline character will be included for lines that are found).
If _filename_ indicates a frozen module (starting with `'<frozen '`), the function will attempt to get the real file name from `module_globals['__file__']` if _module_globals_ is not `None`.
If a file named _filename_ is not found, the function first checks for a [**PEP 302**](https://peps.python.org/pep-0302/) `__loader__` in _module_globals_. If there is such a loader and it defines a `get_source` method, then that determines the source lines (if `get_source()` returns `None`, then `''` is returned). Finally, if _filename_ is a relative filename, it is looked up relative to the entries in the module search path, `sys.path`.
Changed in version 3.14: Support _filename_ of frozen modules.

linecache.clearcache()[¶](https://docs.python.org/3/library/linecache.html#linecache.clearcache "Link to this definition")

Clear the cache. Use this function if you no longer need lines from files previously read using [`getline()`](https://docs.python.org/3/library/linecache.html#linecache.getline "linecache.getline").

linecache.checkcache(_filename =None_)[¶](https://docs.python.org/3/library/linecache.html#linecache.checkcache "Link to this definition")

Check the cache for validity. Use this function if files in the cache may have changed on disk, and you require the updated version. If _filename_ is omitted, it will check all the entries in the cache.

linecache.lazycache(_filename_ , _module_globals_)[¶](https://docs.python.org/3/library/linecache.html#linecache.lazycache "Link to this definition")

Capture enough detail about a non-file-based module to permit getting its lines later via [`getline()`](https://docs.python.org/3/library/linecache.html#linecache.getline "linecache.getline") even if _module_globals_ is `None` in the later call. This avoids doing I/O until a line is actually needed, without having to carry the module globals around indefinitely.
Added in version 3.5.
Example:
Copy```
>>> import linecache
>>> linecache.getline(linecache.__file__, 8)
'import sys\n'

```

#### Previous topic
[`fnmatch` — Unix filename pattern matching](https://docs.python.org/3/library/fnmatch.html "previous chapter")
#### Next topic
[`shutil` — High-level file operations](https://docs.python.org/3/library/shutil.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=linecache+%E2%80%94+Random+access+to+text+lines&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Flinecache.html&pagesource=library%2Flinecache.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/shutil.html "shutil — High-level file operations") |
  * [previous](https://docs.python.org/3/library/fnmatch.html "fnmatch — Unix filename pattern matching") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [File and Directory Access](https://docs.python.org/3/library/filesys.html) »
  * [`linecache` — Random access to text lines](https://docs.python.org/3/library/linecache.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
