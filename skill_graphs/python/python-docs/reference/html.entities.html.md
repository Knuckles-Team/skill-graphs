[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`html.parser` — Simple HTML and XHTML parser](https://docs.python.org/3/library/html.parser.html "previous chapter")
#### Next topic
[XML Processing Modules](https://docs.python.org/3/library/xml.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=html.entities+%E2%80%94+Definitions+of+HTML+general+entities&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fhtml.entities.html&pagesource=library%2Fhtml.entities.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/xml.html "XML Processing Modules") |
  * [previous](https://docs.python.org/3/library/html.parser.html "html.parser — Simple HTML and XHTML parser") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Structured Markup Processing Tools](https://docs.python.org/3/library/markup.html) »
  * [`html.entities` — Definitions of HTML general entities](https://docs.python.org/3/library/html.entities.html)
  * |
  * Theme  Auto Light Dark |


#  `html.entities` — Definitions of HTML general entities[¶](https://docs.python.org/3/library/html.entities.html#module-html.entities "Link to this heading")
**Source code:**
* * *
This module defines four dictionaries, [`html5`](https://docs.python.org/3/library/html.entities.html#html.entities.html5 "html.entities.html5"), [`name2codepoint`](https://docs.python.org/3/library/html.entities.html#html.entities.name2codepoint "html.entities.name2codepoint"), [`codepoint2name`](https://docs.python.org/3/library/html.entities.html#html.entities.codepoint2name "html.entities.codepoint2name"), and [`entitydefs`](https://docs.python.org/3/library/html.entities.html#html.entities.entitydefs "html.entities.entitydefs").

html.entities.html5[¶](https://docs.python.org/3/library/html.entities.html#html.entities.html5 "Link to this definition")

A dictionary that maps HTML5 named character references [[1]](https://docs.python.org/3/library/html.entities.html#id2) to the equivalent Unicode character(s), e.g. `html5['gt;'] == '>'`. Note that the trailing semicolon is included in the name (e.g. `'gt;'`), however some of the names are accepted by the standard even without the semicolon: in this case the name is present with and without the `';'`. See also [`html.unescape()`](https://docs.python.org/3/library/html.html#html.unescape "html.unescape").
Added in version 3.3.

html.entities.entitydefs[¶](https://docs.python.org/3/library/html.entities.html#html.entities.entitydefs "Link to this definition")

A dictionary mapping XHTML 1.0 entity definitions to their replacement text in ISO Latin-1.

html.entities.name2codepoint[¶](https://docs.python.org/3/library/html.entities.html#html.entities.name2codepoint "Link to this definition")

A dictionary that maps HTML4 entity names to the Unicode code points.

html.entities.codepoint2name[¶](https://docs.python.org/3/library/html.entities.html#html.entities.codepoint2name "Link to this definition")

A dictionary that maps Unicode code points to HTML4 entity names.
Footnotes
[[1](https://docs.python.org/3/library/html.entities.html#id1)]
See
#### Previous topic
[`html.parser` — Simple HTML and XHTML parser](https://docs.python.org/3/library/html.parser.html "previous chapter")
#### Next topic
[XML Processing Modules](https://docs.python.org/3/library/xml.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=html.entities+%E2%80%94+Definitions+of+HTML+general+entities&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fhtml.entities.html&pagesource=library%2Fhtml.entities.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/xml.html "XML Processing Modules") |
  * [previous](https://docs.python.org/3/library/html.parser.html "html.parser — Simple HTML and XHTML parser") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Structured Markup Processing Tools](https://docs.python.org/3/library/markup.html) »
  * [`html.entities` — Definitions of HTML general entities](https://docs.python.org/3/library/html.entities.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
