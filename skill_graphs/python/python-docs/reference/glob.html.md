[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`glob` — Unix style pathname pattern expansion](https://docs.python.org/3/library/glob.html)
    * [Examples](https://docs.python.org/3/library/glob.html#examples)


#### Previous topic
[`tempfile` — Generate temporary files and directories](https://docs.python.org/3/library/tempfile.html "previous chapter")
#### Next topic
[`fnmatch` — Unix filename pattern matching](https://docs.python.org/3/library/fnmatch.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=glob+%E2%80%94+Unix+style+pathname+pattern+expansion&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fglob.html&pagesource=library%2Fglob.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/fnmatch.html "fnmatch — Unix filename pattern matching") |
  * [previous](https://docs.python.org/3/library/tempfile.html "tempfile — Generate temporary files and directories") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [File and Directory Access](https://docs.python.org/3/library/filesys.html) »
  * [`glob` — Unix style pathname pattern expansion](https://docs.python.org/3/library/glob.html)
  * |
  * Theme  Auto Light Dark |


#  `glob` — Unix style pathname pattern expansion[¶](https://docs.python.org/3/library/glob.html#module-glob "Link to this heading")
**Source code:**
* * *
The `glob` module finds pathnames using pattern matching rules similar to the Unix shell. No tilde expansion is done, but `*`, `?`, and character ranges expressed with `[]` will be correctly matched. This is done by using the [`os.scandir()`](https://docs.python.org/3/library/os.html#os.scandir "os.scandir") and [`fnmatch.fnmatch()`](https://docs.python.org/3/library/fnmatch.html#fnmatch.fnmatch "fnmatch.fnmatch") functions in concert, and not by actually invoking a subshell.
Note
The pathnames are returned in no particular order. If you need a specific order, sort the results.
Files beginning with a dot (`.`) can only be matched by patterns that also start with a dot, unlike [`fnmatch.fnmatch()`](https://docs.python.org/3/library/fnmatch.html#fnmatch.fnmatch "fnmatch.fnmatch") or [`pathlib.Path.glob()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.glob "pathlib.Path.glob"). For tilde and shell variable expansion, use [`os.path.expanduser()`](https://docs.python.org/3/library/os.path.html#os.path.expanduser "os.path.expanduser") and [`os.path.expandvars()`](https://docs.python.org/3/library/os.path.html#os.path.expandvars "os.path.expandvars").
For a literal match, wrap the meta-characters in brackets. For example, `'[?]'` matches the character `'?'`.
The `glob` module defines the following functions:

glob.glob(_pathname_ , _*_ , _root_dir =None_, _dir_fd =None_, _recursive =False_, _include_hidden =False_)[¶](https://docs.python.org/3/library/glob.html#glob.glob "Link to this definition")

Return a possibly empty list of path names that match _pathname_ , which must be a string containing a path specification. _pathname_ can be either absolute (like `/usr/src/Python-1.5/Makefile`) or relative (like `../../Tools/*/*.gif`), and can contain shell-style wildcards. Broken symlinks are included in the results (as in the shell). Whether or not the results are sorted depends on the file system. If a file that satisfies conditions is removed or added during the call of this function, whether a path name for that file will be included is unspecified.
If _root_dir_ is not `None`, it should be a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object) specifying the root directory for searching. It has the same effect on `glob()` as changing the current directory before calling it. If _pathname_ is relative, the result will contain paths relative to _root_dir_.
This function can support [paths relative to directory descriptors](https://docs.python.org/3/library/os.html#dir-fd) with the _dir_fd_ parameter.
If _recursive_ is true, the pattern “`**`” will match any files and zero or more directories, subdirectories and symbolic links to directories. If the pattern is followed by an [`os.sep`](https://docs.python.org/3/library/os.html#os.sep "os.sep") or [`os.altsep`](https://docs.python.org/3/library/os.html#os.altsep "os.altsep") then files will not match.
If _include_hidden_ is true, “`**`” pattern will match hidden directories.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `glob.glob` with arguments `pathname`, `recursive`.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `glob.glob/2` with arguments `pathname`, `recursive`, `root_dir`, `dir_fd`.
Note
Using the “`**`” pattern in large directory trees may consume an inordinate amount of time.
Note
This function may return duplicate path names if _pathname_ contains multiple “`**`” patterns and _recursive_ is true.
Changed in version 3.5: Support for recursive globs using “`**`”.
Changed in version 3.10: Added the _root_dir_ and _dir_fd_ parameters.
Changed in version 3.11: Added the _include_hidden_ parameter.

glob.iglob(_pathname_ , _*_ , _root_dir =None_, _dir_fd =None_, _recursive =False_, _include_hidden =False_)[¶](https://docs.python.org/3/library/glob.html#glob.iglob "Link to this definition")

Return an [iterator](https://docs.python.org/3/glossary.html#term-iterator) which yields the same values as [`glob()`](https://docs.python.org/3/library/glob.html#module-glob "glob: Unix shell style pathname pattern expansion.") without actually storing them all simultaneously.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `glob.glob` with arguments `pathname`, `recursive`.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `glob.glob/2` with arguments `pathname`, `recursive`, `root_dir`, `dir_fd`.
Note
This function may return duplicate path names if _pathname_ contains multiple “`**`” patterns and _recursive_ is true.
Changed in version 3.5: Support for recursive globs using “`**`”.
Changed in version 3.10: Added the _root_dir_ and _dir_fd_ parameters.
Changed in version 3.11: Added the _include_hidden_ parameter.

glob.escape(_pathname_)[¶](https://docs.python.org/3/library/glob.html#glob.escape "Link to this definition")

Escape all special characters (`'?'`, `'*'` and `'['`). This is useful if you want to match an arbitrary literal string that may have special characters in it. Special characters in drive/UNC sharepoints are not escaped, e.g. on Windows `escape('//?/c:/Quo vadis?.txt')` returns `'//?/c:/Quo vadis[?].txt'`.
Added in version 3.4.

glob.translate(_pathname_ , _*_ , _recursive =False_, _include_hidden =False_, _seps =None_)[¶](https://docs.python.org/3/library/glob.html#glob.translate "Link to this definition")

Convert the given path specification to a regular expression for use with [`re.match()`](https://docs.python.org/3/library/re.html#re.match "re.match"). The path specification can contain shell-style wildcards.
For example:
Copy```
>>> import glob, re
>>>
>>> regex = glob.translate('**/*.txt', recursive=True, include_hidden=True)
>>> regex
'(?s:(?:.+/)?[^/]*\\.txt)\\z'
>>> reobj = re.compile(regex)
>>> reobj.match('foo/bar/baz.txt')
<re.Match object; span=(0, 15), match='foo/bar/baz.txt'>

```

Path separators and segments are meaningful to this function, unlike [`fnmatch.translate()`](https://docs.python.org/3/library/fnmatch.html#fnmatch.translate "fnmatch.translate"). By default wildcards do not match path separators, and `*` pattern segments match precisely one path segment.
If _recursive_ is true, the pattern segment “`**`” will match any number of path segments.
If _include_hidden_ is true, wildcards can match path segments that start with a dot (`.`).
A sequence of path separators may be supplied to the _seps_ argument. If not given, [`os.sep`](https://docs.python.org/3/library/os.html#os.sep "os.sep") and [`altsep`](https://docs.python.org/3/library/os.html#os.altsep "os.altsep") (if available) are used.
See also
[`pathlib.PurePath.full_match()`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.full_match "pathlib.PurePath.full_match") and [`pathlib.Path.glob()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.glob "pathlib.Path.glob") methods, which call this function to implement pattern matching and globbing.
Added in version 3.13.
## Examples[¶](https://docs.python.org/3/library/glob.html#examples "Link to this heading")
Consider a directory containing the following files: `1.gif`, `2.txt`, `card.gif` and a subdirectory `sub` which contains only the file `3.txt`. [`glob()`](https://docs.python.org/3/library/glob.html#module-glob "glob: Unix shell style pathname pattern expansion.") will produce the following results. Notice how any leading components of the path are preserved.
Copy```
>>> import glob
>>> glob.glob('./[0-9].*')
['./1.gif', './2.txt']
>>> glob.glob('*.gif')
['1.gif', 'card.gif']
>>> glob.glob('?.gif')
['1.gif']
>>> glob.glob('**/*.txt', recursive=True)
['2.txt', 'sub/3.txt']
>>> glob.glob('./**/', recursive=True)
['./', './sub/']

```

If the directory contains files starting with `.` they won’t be matched by default. For example, consider a directory containing `card.gif` and `.card.gif`:
Copy```
>>> import glob
>>> glob.glob('*.gif')
['card.gif']
>>> glob.glob('.c*')
['.card.gif']

```

See also
The [`fnmatch`](https://docs.python.org/3/library/fnmatch.html#module-fnmatch "fnmatch: Unix shell style filename pattern matching.") module offers shell-style filename (not path) expansion.
See also
The [`pathlib`](https://docs.python.org/3/library/pathlib.html#module-pathlib "pathlib: Object-oriented filesystem paths") module offers high-level path objects.
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`glob` — Unix style pathname pattern expansion](https://docs.python.org/3/library/glob.html)
    * [Examples](https://docs.python.org/3/library/glob.html#examples)


#### Previous topic
[`tempfile` — Generate temporary files and directories](https://docs.python.org/3/library/tempfile.html "previous chapter")
#### Next topic
[`fnmatch` — Unix filename pattern matching](https://docs.python.org/3/library/fnmatch.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=glob+%E2%80%94+Unix+style+pathname+pattern+expansion&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fglob.html&pagesource=library%2Fglob.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/fnmatch.html "fnmatch — Unix filename pattern matching") |
  * [previous](https://docs.python.org/3/library/tempfile.html "tempfile — Generate temporary files and directories") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [File and Directory Access](https://docs.python.org/3/library/filesys.html) »
  * [`glob` — Unix style pathname pattern expansion](https://docs.python.org/3/library/glob.html)
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
