[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`filecmp` — File and Directory Comparisons](https://docs.python.org/3/library/filecmp.html)
    * [The `dircmp` class](https://docs.python.org/3/library/filecmp.html#the-dircmp-class)


#### Previous topic
[`stat` — Interpreting `stat()` results](https://docs.python.org/3/library/stat.html "previous chapter")
#### Next topic
[`tempfile` — Generate temporary files and directories](https://docs.python.org/3/library/tempfile.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=filecmp+%E2%80%94+File+and+Directory+Comparisons&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ffilecmp.html&pagesource=library%2Ffilecmp.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/tempfile.html "tempfile — Generate temporary files and directories") |
  * [previous](https://docs.python.org/3/library/stat.html "stat — Interpreting stat\(\) results") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [File and Directory Access](https://docs.python.org/3/library/filesys.html) »
  * [`filecmp` — File and Directory Comparisons](https://docs.python.org/3/library/filecmp.html)
  * |
  * Theme  Auto Light Dark |


#  `filecmp` — File and Directory Comparisons[¶](https://docs.python.org/3/library/filecmp.html#module-filecmp "Link to this heading")
**Source code:**
* * *
The `filecmp` module defines functions to compare files and directories, with various optional time/correctness trade-offs. For comparing files, see also the [`difflib`](https://docs.python.org/3/library/difflib.html#module-difflib "difflib: Helpers for computing differences between objects.") module.
The `filecmp` module defines the following functions:

filecmp.cmp(_f1_ , _f2_ , _shallow =True_)[¶](https://docs.python.org/3/library/filecmp.html#filecmp.cmp "Link to this definition")

Compare the files named _f1_ and _f2_ , returning `True` if they seem equal, `False` otherwise.
If _shallow_ is true and the [`os.stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat") signatures (file type, size, and modification time) of both files are identical, the files are taken to be equal.
Otherwise, the files are treated as different if their sizes or contents differ.
Note that no external programs are called from this function, giving it portability and efficiency.
This function uses a cache for past comparisons and the results, with cache entries invalidated if the [`os.stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat") information for the file changes. The entire cache may be cleared using [`clear_cache()`](https://docs.python.org/3/library/filecmp.html#filecmp.clear_cache "filecmp.clear_cache").

filecmp.cmpfiles(_dir1_ , _dir2_ , _common_ , _shallow =True_)[¶](https://docs.python.org/3/library/filecmp.html#filecmp.cmpfiles "Link to this definition")

Compare the files in the two directories _dir1_ and _dir2_ whose names are given by _common_.
Returns three lists of file names: _match_ , _mismatch_ , _errors_. _match_ contains the list of files that match, _mismatch_ contains the names of those that don’t, and _errors_ lists the names of files which could not be compared. Files are listed in _errors_ if they don’t exist in one of the directories, the user lacks permission to read them or if the comparison could not be done for some other reason.
The _shallow_ parameter has the same meaning and default value as for [`filecmp.cmp()`](https://docs.python.org/3/library/filecmp.html#filecmp.cmp "filecmp.cmp").
For example, `cmpfiles('a', 'b', ['c', 'd/e'])` will compare `a/c` with `b/c` and `a/d/e` with `b/d/e`. `'c'` and `'d/e'` will each be in one of the three returned lists.

filecmp.clear_cache()[¶](https://docs.python.org/3/library/filecmp.html#filecmp.clear_cache "Link to this definition")

Clear the filecmp cache. This may be useful if a file is compared so quickly after it is modified that it is within the mtime resolution of the underlying filesystem.
Added in version 3.4.
## The [`dircmp`](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp "filecmp.dircmp") class[¶](https://docs.python.org/3/library/filecmp.html#the-dircmp-class "Link to this heading")

_class_ filecmp.dircmp(_a_ , _b_ , _ignore =None_, _hide =None_, _*_ , _shallow =True_)[¶](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp "Link to this definition")

Construct a new directory comparison object, to compare the directories _a_ and _b_. _ignore_ is a list of names to ignore, and defaults to [`filecmp.DEFAULT_IGNORES`](https://docs.python.org/3/library/filecmp.html#filecmp.DEFAULT_IGNORES "filecmp.DEFAULT_IGNORES"). _hide_ is a list of names to hide, and defaults to `[os.curdir, os.pardir]`.
The `dircmp` class compares files by doing _shallow_ comparisons as described for [`filecmp.cmp()`](https://docs.python.org/3/library/filecmp.html#filecmp.cmp "filecmp.cmp") by default using the _shallow_ parameter.
Changed in version 3.13: Added the _shallow_ parameter.
The `dircmp` class provides the following methods:

report()[¶](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp.report "Link to this definition")

Print (to [`sys.stdout`](https://docs.python.org/3/library/sys.html#sys.stdout "sys.stdout")) a comparison between _a_ and _b_.

report_partial_closure()[¶](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp.report_partial_closure "Link to this definition")

Print a comparison between _a_ and _b_ and common immediate subdirectories.

report_full_closure()[¶](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp.report_full_closure "Link to this definition")

Print a comparison between _a_ and _b_ and common subdirectories (recursively).
The `dircmp` class offers a number of interesting attributes that may be used to get various bits of information about the directory trees being compared.
Note that via [`__getattr__()`](https://docs.python.org/3/reference/datamodel.html#object.__getattr__ "object.__getattr__") hooks, all attributes are computed lazily, so there is no speed penalty if only those attributes which are lightweight to compute are used.

left[¶](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp.left "Link to this definition")

The directory _a_.

right[¶](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp.right "Link to this definition")

The directory _b_.

left_list[¶](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp.left_list "Link to this definition")

Files and subdirectories in _a_ , filtered by _hide_ and _ignore_.

right_list[¶](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp.right_list "Link to this definition")

Files and subdirectories in _b_ , filtered by _hide_ and _ignore_.

common[¶](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp.common "Link to this definition")

Files and subdirectories in both _a_ and _b_.

left_only[¶](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp.left_only "Link to this definition")

Files and subdirectories only in _a_.

right_only[¶](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp.right_only "Link to this definition")

Files and subdirectories only in _b_.

common_dirs[¶](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp.common_dirs "Link to this definition")

Subdirectories in both _a_ and _b_.

common_files[¶](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp.common_files "Link to this definition")

Files in both _a_ and _b_.

common_funny[¶](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp.common_funny "Link to this definition")

Names in both _a_ and _b_ , such that the type differs between the directories, or names for which [`os.stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat") reports an error.

same_files[¶](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp.same_files "Link to this definition")

Files which are identical in both _a_ and _b_ , using the class’s file comparison operator.

diff_files[¶](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp.diff_files "Link to this definition")

Files which are in both _a_ and _b_ , whose contents differ according to the class’s file comparison operator.

funny_files[¶](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp.funny_files "Link to this definition")

Files which are in both _a_ and _b_ , but could not be compared.

subdirs[¶](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp.subdirs "Link to this definition")

A dictionary mapping names in [`common_dirs`](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp.common_dirs "filecmp.dircmp.common_dirs") to `dircmp` instances (or MyDirCmp instances if this instance is of type MyDirCmp, a subclass of `dircmp`).
Changed in version 3.10: Previously entries were always `dircmp` instances. Now entries are the same type as _self_ , if _self_ is a subclass of `dircmp`.

filecmp.DEFAULT_IGNORES[¶](https://docs.python.org/3/library/filecmp.html#filecmp.DEFAULT_IGNORES "Link to this definition")

Added in version 3.4.
List of directories ignored by [`dircmp`](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp "filecmp.dircmp") by default.
Here is a simplified example of using the `subdirs` attribute to search recursively through two directories to show common different files:
Copy```
>>> from filecmp import dircmp
>>> def print_diff_files(dcmp):
...     for name in dcmp.diff_files:
...         print("diff_file %s found in %s and %s" % (name, dcmp.left,
...               dcmp.right))
...     for sub_dcmp in dcmp.subdirs.values():
...         print_diff_files(sub_dcmp)
...
>>> dcmp = dircmp('dir1', 'dir2')
>>> print_diff_files(dcmp)

```

### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`filecmp` — File and Directory Comparisons](https://docs.python.org/3/library/filecmp.html)
    * [The `dircmp` class](https://docs.python.org/3/library/filecmp.html#the-dircmp-class)


#### Previous topic
[`stat` — Interpreting `stat()` results](https://docs.python.org/3/library/stat.html "previous chapter")
#### Next topic
[`tempfile` — Generate temporary files and directories](https://docs.python.org/3/library/tempfile.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=filecmp+%E2%80%94+File+and+Directory+Comparisons&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ffilecmp.html&pagesource=library%2Ffilecmp.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/tempfile.html "tempfile — Generate temporary files and directories") |
  * [previous](https://docs.python.org/3/library/stat.html "stat — Interpreting stat\(\) results") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [File and Directory Access](https://docs.python.org/3/library/filesys.html) »
  * [`filecmp` — File and Directory Comparisons](https://docs.python.org/3/library/filecmp.html)
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
