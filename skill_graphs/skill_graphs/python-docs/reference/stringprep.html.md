[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`unicodedata` — Unicode Database](https://docs.python.org/3/library/unicodedata.html "previous chapter")
#### Next topic
[`readline` — GNU readline interface](https://docs.python.org/3/library/readline.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=stringprep+%E2%80%94+Internet+String+Preparation&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fstringprep.html&pagesource=library%2Fstringprep.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/readline.html "readline — GNU readline interface") |
  * [previous](https://docs.python.org/3/library/unicodedata.html "unicodedata — Unicode Database") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Text Processing Services](https://docs.python.org/3/library/text.html) »
  * [`stringprep` — Internet String Preparation](https://docs.python.org/3/library/stringprep.html)
  * |
  * Theme  Auto Light Dark |


#  `stringprep` — Internet String Preparation[¶](https://docs.python.org/3/library/stringprep.html#module-stringprep "Link to this heading")
**Source code:**
* * *
When identifying things (such as host names) in the internet, it is often necessary to compare such identifications for “equality”. Exactly how this comparison is executed may depend on the application domain, e.g. whether it should be case-insensitive or not. It may be also necessary to restrict the possible identifications, to allow only identifications consisting of “printable” characters.
`stringprep` procedure are part of the profile. One example of a `stringprep` profile is `nameprep`, which is used for internationalized domain names.
The module `stringprep` only exposes the tables from `mkstringprep.py` utility.
As a result, these tables are exposed as functions, not as data structures. There are two kinds of tables in the RFC: sets and mappings. For a set, `stringprep` provides the “characteristic function”, i.e. a function that returns `True` if the parameter is part of the set. For mappings, it provides the mapping function: given the key, it returns the associated value. Below is a list of all functions available in the module.

stringprep.in_table_a1(_code_)[¶](https://docs.python.org/3/library/stringprep.html#stringprep.in_table_a1 "Link to this definition")

Determine whether _code_ is in tableA.1 (Unassigned code points in Unicode 3.2).

stringprep.in_table_b1(_code_)[¶](https://docs.python.org/3/library/stringprep.html#stringprep.in_table_b1 "Link to this definition")

Determine whether _code_ is in tableB.1 (Commonly mapped to nothing).

stringprep.map_table_b2(_code_)[¶](https://docs.python.org/3/library/stringprep.html#stringprep.map_table_b2 "Link to this definition")

Return the mapped value for _code_ according to tableB.2 (Mapping for case-folding used with NFKC).

stringprep.map_table_b3(_code_)[¶](https://docs.python.org/3/library/stringprep.html#stringprep.map_table_b3 "Link to this definition")

Return the mapped value for _code_ according to tableB.3 (Mapping for case-folding used with no normalization).

stringprep.in_table_c11(_code_)[¶](https://docs.python.org/3/library/stringprep.html#stringprep.in_table_c11 "Link to this definition")

Determine whether _code_ is in tableC.1.1 (ASCII space characters).

stringprep.in_table_c12(_code_)[¶](https://docs.python.org/3/library/stringprep.html#stringprep.in_table_c12 "Link to this definition")

Determine whether _code_ is in tableC.1.2 (Non-ASCII space characters).

stringprep.in_table_c11_c12(_code_)[¶](https://docs.python.org/3/library/stringprep.html#stringprep.in_table_c11_c12 "Link to this definition")

Determine whether _code_ is in tableC.1 (Space characters, union of C.1.1 and C.1.2).

stringprep.in_table_c21(_code_)[¶](https://docs.python.org/3/library/stringprep.html#stringprep.in_table_c21 "Link to this definition")

Determine whether _code_ is in tableC.2.1 (ASCII control characters).

stringprep.in_table_c22(_code_)[¶](https://docs.python.org/3/library/stringprep.html#stringprep.in_table_c22 "Link to this definition")

Determine whether _code_ is in tableC.2.2 (Non-ASCII control characters).

stringprep.in_table_c21_c22(_code_)[¶](https://docs.python.org/3/library/stringprep.html#stringprep.in_table_c21_c22 "Link to this definition")

Determine whether _code_ is in tableC.2 (Control characters, union of C.2.1 and C.2.2).

stringprep.in_table_c3(_code_)[¶](https://docs.python.org/3/library/stringprep.html#stringprep.in_table_c3 "Link to this definition")

Determine whether _code_ is in tableC.3 (Private use).

stringprep.in_table_c4(_code_)[¶](https://docs.python.org/3/library/stringprep.html#stringprep.in_table_c4 "Link to this definition")

Determine whether _code_ is in tableC.4 (Non-character code points).

stringprep.in_table_c5(_code_)[¶](https://docs.python.org/3/library/stringprep.html#stringprep.in_table_c5 "Link to this definition")

Determine whether _code_ is in tableC.5 (Surrogate codes).

stringprep.in_table_c6(_code_)[¶](https://docs.python.org/3/library/stringprep.html#stringprep.in_table_c6 "Link to this definition")

Determine whether _code_ is in tableC.6 (Inappropriate for plain text).

stringprep.in_table_c7(_code_)[¶](https://docs.python.org/3/library/stringprep.html#stringprep.in_table_c7 "Link to this definition")

Determine whether _code_ is in tableC.7 (Inappropriate for canonical representation).

stringprep.in_table_c8(_code_)[¶](https://docs.python.org/3/library/stringprep.html#stringprep.in_table_c8 "Link to this definition")

Determine whether _code_ is in tableC.8 (Change display properties or are deprecated).

stringprep.in_table_c9(_code_)[¶](https://docs.python.org/3/library/stringprep.html#stringprep.in_table_c9 "Link to this definition")

Determine whether _code_ is in tableC.9 (Tagging characters).

stringprep.in_table_d1(_code_)[¶](https://docs.python.org/3/library/stringprep.html#stringprep.in_table_d1 "Link to this definition")

Determine whether _code_ is in tableD.1 (Characters with bidirectional property “R” or “AL”).

stringprep.in_table_d2(_code_)[¶](https://docs.python.org/3/library/stringprep.html#stringprep.in_table_d2 "Link to this definition")

Determine whether _code_ is in tableD.2 (Characters with bidirectional property “L”).
#### Previous topic
[`unicodedata` — Unicode Database](https://docs.python.org/3/library/unicodedata.html "previous chapter")
#### Next topic
[`readline` — GNU readline interface](https://docs.python.org/3/library/readline.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=stringprep+%E2%80%94+Internet+String+Preparation&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fstringprep.html&pagesource=library%2Fstringprep.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/readline.html "readline — GNU readline interface") |
  * [previous](https://docs.python.org/3/library/unicodedata.html "unicodedata — Unicode Database") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Text Processing Services](https://docs.python.org/3/library/text.html) »
  * [`stringprep` — Internet String Preparation](https://docs.python.org/3/library/stringprep.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
