[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`glob` — Unix style pathname pattern expansion](https://docs.python.org/3/library/glob.html "previous chapter")
#### Next topic
[`linecache` — Random access to text lines](https://docs.python.org/3/library/linecache.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=fnmatch+%E2%80%94+Unix+filename+pattern+matching&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ffnmatch.html&pagesource=library%2Ffnmatch.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/linecache.html "linecache — Random access to text lines") |
  * [previous](https://docs.python.org/3/library/glob.html "glob — Unix style pathname pattern expansion") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [File and Directory Access](https://docs.python.org/3/library/filesys.html) »
  * [`fnmatch` — Unix filename pattern matching](https://docs.python.org/3/library/fnmatch.html)
  * |
  * Theme  Auto Light Dark |


#  `fnmatch` — Unix filename pattern matching[¶](https://docs.python.org/3/library/fnmatch.html#module-fnmatch "Link to this heading")
**Source code:**
* * *
This module provides support for Unix shell-style wildcards, which are _not_ the same as regular expressions (which are documented in the [`re`](https://docs.python.org/3/library/re.html#module-re "re: Regular expression operations.") module). The special characters used in shell-style wildcards are:
Pattern | Meaning
---|---
`*` | matches everything
`?` | matches any single character
`[seq]` | matches any character in _seq_
`[!seq]` | matches any character not in _seq_
For a literal match, wrap the meta-characters in brackets. For example, `'[?]'` matches the character `'?'`.
Note that the filename separator (`'/'` on Unix) is _not_ special to this module. See module [`glob`](https://docs.python.org/3/library/glob.html#module-glob "glob: Unix shell style pathname pattern expansion.") for pathname expansion (`glob` uses [`filter()`](https://docs.python.org/3/library/fnmatch.html#fnmatch.filter "fnmatch.filter") to match pathname segments). Similarly, filenames starting with a period are not special for this module, and are matched by the `*` and `?` patterns.
Unless stated otherwise, “filename string” and “pattern string” either refer to [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") or `ISO-8859-1` encoded [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") objects. Note that the functions documented below do not allow to mix a `bytes` pattern with a `str` filename, and vice-versa.
Finally, note that [`functools.lru_cache()`](https://docs.python.org/3/library/functools.html#functools.lru_cache "functools.lru_cache") with a _maxsize_ of 32768 is used to cache the (typed) compiled regex patterns in the following functions: [`fnmatch()`](https://docs.python.org/3/library/fnmatch.html#module-fnmatch "fnmatch: Unix shell style filename pattern matching."), [`fnmatchcase()`](https://docs.python.org/3/library/fnmatch.html#fnmatch.fnmatchcase "fnmatch.fnmatchcase"), [`filter()`](https://docs.python.org/3/library/fnmatch.html#fnmatch.filter "fnmatch.filter"), [`filterfalse()`](https://docs.python.org/3/library/fnmatch.html#fnmatch.filterfalse "fnmatch.filterfalse").

fnmatch.fnmatch(_name_ , _pat_)[¶](https://docs.python.org/3/library/fnmatch.html#fnmatch.fnmatch "Link to this definition")

Test whether the filename string _name_ matches the pattern string _pat_ , returning `True` or `False`. Both parameters are case-normalized using [`os.path.normcase()`](https://docs.python.org/3/library/os.path.html#os.path.normcase "os.path.normcase"). [`fnmatchcase()`](https://docs.python.org/3/library/fnmatch.html#fnmatch.fnmatchcase "fnmatch.fnmatchcase") can be used to perform a case-sensitive comparison, regardless of whether that’s standard for the operating system.
This example will print all file names in the current directory with the extension `.txt`:
Copy```
import fnmatch
import os

for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*.txt'):
        print(file)

```


fnmatch.fnmatchcase(_name_ , _pat_)[¶](https://docs.python.org/3/library/fnmatch.html#fnmatch.fnmatchcase "Link to this definition")

Test whether the filename string _name_ matches the pattern string _pat_ , returning `True` or `False`; the comparison is case-sensitive and does not apply [`os.path.normcase()`](https://docs.python.org/3/library/os.path.html#os.path.normcase "os.path.normcase").

fnmatch.filter(_names_ , _pat_)[¶](https://docs.python.org/3/library/fnmatch.html#fnmatch.filter "Link to this definition")

Construct a list from those elements of the [iterable](https://docs.python.org/3/glossary.html#term-iterable) of filename strings _names_ that match the pattern string _pat_. It is the same as `[n for n in names if fnmatch(n, pat)]`, but implemented more efficiently.

fnmatch.filterfalse(_names_ , _pat_)[¶](https://docs.python.org/3/library/fnmatch.html#fnmatch.filterfalse "Link to this definition")

Construct a list from those elements of the [iterable](https://docs.python.org/3/glossary.html#term-iterable) of filename strings _names_ that do not match the pattern string _pat_. It is the same as `[n for n in names if not fnmatch(n, pat)]`, but implemented more efficiently.
Added in version 3.14.

fnmatch.translate(_pat_)[¶](https://docs.python.org/3/library/fnmatch.html#fnmatch.translate "Link to this definition")

Return the shell-style pattern _pat_ converted to a regular expression for using with [`re.match()`](https://docs.python.org/3/library/re.html#re.match "re.match"). The pattern is expected to be a [`str`](https://docs.python.org/3/library/stdtypes.html#str "str").
Example:
Copy```
>>> import fnmatch, re
>>>
>>> regex = fnmatch.translate('*.txt')
>>> regex
'(?s:.*\\.txt)\\z'
>>> reobj = re.compile(regex)
>>> reobj.match('foobar.txt')
<re.Match object; span=(0, 10), match='foobar.txt'>

```

See also

Module [`glob`](https://docs.python.org/3/library/glob.html#module-glob "glob: Unix shell style pathname pattern expansion.")

Unix shell-style path expansion.
#### Previous topic
[`glob` — Unix style pathname pattern expansion](https://docs.python.org/3/library/glob.html "previous chapter")
#### Next topic
[`linecache` — Random access to text lines](https://docs.python.org/3/library/linecache.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=fnmatch+%E2%80%94+Unix+filename+pattern+matching&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ffnmatch.html&pagesource=library%2Ffnmatch.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/linecache.html "linecache — Random access to text lines") |
  * [previous](https://docs.python.org/3/library/glob.html "glob — Unix style pathname pattern expansion") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [File and Directory Access](https://docs.python.org/3/library/filesys.html) »
  * [`fnmatch` — Unix filename pattern matching](https://docs.python.org/3/library/fnmatch.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
