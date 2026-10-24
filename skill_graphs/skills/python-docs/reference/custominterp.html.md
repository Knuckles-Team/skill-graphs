[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`site` — Site-specific configuration hook](https://docs.python.org/3/library/site.html "previous chapter")
#### Next topic
[`code` — Interpreter base classes](https://docs.python.org/3/library/code.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Custom+Python+Interpreters&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fcustominterp.html&pagesource=library%2Fcustominterp.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/code.html "code — Interpreter base classes") |
  * [previous](https://docs.python.org/3/library/site.html "site — Site-specific configuration hook") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Custom Python Interpreters](https://docs.python.org/3/library/custominterp.html)
  * |
  * Theme  Auto Light Dark |


# Custom Python Interpreters[¶](https://docs.python.org/3/library/custominterp.html#custom-python-interpreters "Link to this heading")
The modules described in this chapter allow writing interfaces similar to Python’s interactive interpreter. If you want a Python interpreter that supports some special feature in addition to the Python language, you should look at the [`code`](https://docs.python.org/3/library/code.html#module-code "code: Facilities to implement read-eval-print loops.") module. (The [`codeop`](https://docs.python.org/3/library/codeop.html#module-codeop "codeop: Compile \(possibly incomplete\) Python code.") module is lower-level, used to support compiling a possibly incomplete chunk of Python code.)
The full list of modules described in this chapter is:
  * [`code` — Interpreter base classes](https://docs.python.org/3/library/code.html)
    * [Interactive Interpreter Objects](https://docs.python.org/3/library/code.html#interactive-interpreter-objects)
    * [Interactive Console Objects](https://docs.python.org/3/library/code.html#interactive-console-objects)
  * [`codeop` — Compile Python code](https://docs.python.org/3/library/codeop.html)


#### Previous topic
[`site` — Site-specific configuration hook](https://docs.python.org/3/library/site.html "previous chapter")
#### Next topic
[`code` — Interpreter base classes](https://docs.python.org/3/library/code.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Custom+Python+Interpreters&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fcustominterp.html&pagesource=library%2Fcustominterp.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/code.html "code — Interpreter base classes") |
  * [previous](https://docs.python.org/3/library/site.html "site — Site-specific configuration hook") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Custom Python Interpreters](https://docs.python.org/3/library/custominterp.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
