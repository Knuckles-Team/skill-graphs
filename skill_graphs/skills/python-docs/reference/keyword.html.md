[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`token` — Constants used with Python parse trees](https://docs.python.org/3/library/token.html "previous chapter")
#### Next topic
[`tokenize` — Tokenizer for Python source](https://docs.python.org/3/library/tokenize.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=keyword+%E2%80%94+Testing+for+Python+keywords&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fkeyword.html&pagesource=library%2Fkeyword.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/tokenize.html "tokenize — Tokenizer for Python source") |
  * [previous](https://docs.python.org/3/library/token.html "token — Constants used with Python parse trees") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Python Language Services](https://docs.python.org/3/library/language.html) »
  * [`keyword` — Testing for Python keywords](https://docs.python.org/3/library/keyword.html)
  * |
  * Theme  Auto Light Dark |


#  `keyword` — Testing for Python keywords[¶](https://docs.python.org/3/library/keyword.html#module-keyword "Link to this heading")
**Source code:**
* * *
This module allows a Python program to determine if a string is a [keyword](https://docs.python.org/3/reference/lexical_analysis.html#keywords) or [soft keyword](https://docs.python.org/3/reference/lexical_analysis.html#soft-keywords).

keyword.iskeyword(_s_)[¶](https://docs.python.org/3/library/keyword.html#keyword.iskeyword "Link to this definition")

Return `True` if _s_ is a Python [keyword](https://docs.python.org/3/reference/lexical_analysis.html#keywords).

keyword.kwlist[¶](https://docs.python.org/3/library/keyword.html#keyword.kwlist "Link to this definition")

Sequence containing all the [keywords](https://docs.python.org/3/reference/lexical_analysis.html#keywords) defined for the interpreter. If any keywords are defined to only be active when particular [`__future__`](https://docs.python.org/3/library/__future__.html#module-__future__ "__future__: Future statement definitions") statements are in effect, these will be included as well.

keyword.issoftkeyword(_s_)[¶](https://docs.python.org/3/library/keyword.html#keyword.issoftkeyword "Link to this definition")

Return `True` if _s_ is a Python [soft keyword](https://docs.python.org/3/reference/lexical_analysis.html#soft-keywords).
Added in version 3.9.

keyword.softkwlist[¶](https://docs.python.org/3/library/keyword.html#keyword.softkwlist "Link to this definition")

Sequence containing all the [soft keywords](https://docs.python.org/3/reference/lexical_analysis.html#soft-keywords) defined for the interpreter. If any soft keywords are defined to only be active when particular [`__future__`](https://docs.python.org/3/library/__future__.html#module-__future__ "__future__: Future statement definitions") statements are in effect, these will be included as well.
Added in version 3.9.
#### Previous topic
[`token` — Constants used with Python parse trees](https://docs.python.org/3/library/token.html "previous chapter")
#### Next topic
[`tokenize` — Tokenizer for Python source](https://docs.python.org/3/library/tokenize.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=keyword+%E2%80%94+Testing+for+Python+keywords&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fkeyword.html&pagesource=library%2Fkeyword.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/tokenize.html "tokenize — Tokenizer for Python source") |
  * [previous](https://docs.python.org/3/library/token.html "token — Constants used with Python parse trees") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Python Language Services](https://docs.python.org/3/library/language.html) »
  * [`keyword` — Testing for Python keywords](https://docs.python.org/3/library/keyword.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
