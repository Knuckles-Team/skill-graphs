[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`readline` — GNU readline interface](https://docs.python.org/3/library/readline.html "previous chapter")
#### Next topic
[Binary Data Services](https://docs.python.org/3/library/binary.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=rlcompleter+%E2%80%94+Completion+function+for+GNU+readline&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Frlcompleter.html&pagesource=library%2Frlcompleter.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/binary.html "Binary Data Services") |
  * [previous](https://docs.python.org/3/library/readline.html "readline — GNU readline interface") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Text Processing Services](https://docs.python.org/3/library/text.html) »
  * [`rlcompleter` — Completion function for GNU readline](https://docs.python.org/3/library/rlcompleter.html)
  * |
  * Theme  Auto Light Dark |


#  `rlcompleter` — Completion function for GNU readline[¶](https://docs.python.org/3/library/rlcompleter.html#module-rlcompleter "Link to this heading")
**Source code:**
* * *
The `rlcompleter` module defines a completion function suitable to be passed to [`set_completer()`](https://docs.python.org/3/library/readline.html#readline.set_completer "readline.set_completer") in the [`readline`](https://docs.python.org/3/library/readline.html#module-readline "readline: GNU readline support for Python.") module.
When this module is imported on a Unix platform with the [`readline`](https://docs.python.org/3/library/readline.html#module-readline "readline: GNU readline support for Python.") module available, an instance of the [`Completer`](https://docs.python.org/3/library/rlcompleter.html#rlcompleter.Completer "rlcompleter.Completer") class is automatically created and its [`complete()`](https://docs.python.org/3/library/rlcompleter.html#rlcompleter.Completer.complete "rlcompleter.Completer.complete") method is set as the [readline completer](https://docs.python.org/3/library/readline.html#readline-completion). The method provides completion of valid Python [identifiers and keywords](https://docs.python.org/3/reference/lexical_analysis.html#identifiers).
Example:
Copy```
>>> import rlcompleter
>>> import readline
>>> readline.parse_and_bind("tab: complete")
>>> readline. <TAB PRESSED>
readline.__doc__          readline.get_line_buffer(  readline.read_init_file(
readline.__file__         readline.insert_text(      readline.set_completer(
readline.__name__         readline.parse_and_bind(
>>> readline.

```

The `rlcompleter` module is designed for use with Python’s [interactive mode](https://docs.python.org/3/tutorial/interpreter.html#tut-interactive). Unless Python is run with the [`-S`](https://docs.python.org/3/using/cmdline.html#cmdoption-S) option, the module is automatically imported and configured (see [Readline configuration](https://docs.python.org/3/library/site.html#rlcompleter-config)).
On platforms without [`readline`](https://docs.python.org/3/library/readline.html#module-readline "readline: GNU readline support for Python."), the [`Completer`](https://docs.python.org/3/library/rlcompleter.html#rlcompleter.Completer "rlcompleter.Completer") class defined by this module can still be used for custom purposes.

_class_ rlcompleter.Completer[¶](https://docs.python.org/3/library/rlcompleter.html#rlcompleter.Completer "Link to this definition")

Completer objects have the following method:

complete(_text_ , _state_)[¶](https://docs.python.org/3/library/rlcompleter.html#rlcompleter.Completer.complete "Link to this definition")

Return the next possible completion for _text_.
When called by the [`readline`](https://docs.python.org/3/library/readline.html#module-readline "readline: GNU readline support for Python.") module, this method is called successively with `state == 0, 1, 2, ...` until the method returns `None`.
If called for _text_ that doesn’t include a period character (`'.'`), it will complete from names currently defined in [`__main__`](https://docs.python.org/3/library/__main__.html#module-__main__ "__main__: The environment where top-level code is run. Covers command-line interfaces, import-time behavior, and ``__name__ == '__main__'``."), [`builtins`](https://docs.python.org/3/library/builtins.html#module-builtins "builtins: The module that provides the built-in namespace.") and keywords (as defined by the [`keyword`](https://docs.python.org/3/library/keyword.html#module-keyword "keyword: Test whether a string is a keyword in Python.") module).
If called for a dotted name, it will try to evaluate anything without obvious side-effects (functions will not be evaluated, but it can generate calls to [`__getattr__()`](https://docs.python.org/3/reference/datamodel.html#object.__getattr__ "object.__getattr__")) up to the last part, and find matches for the rest via the [`dir()`](https://docs.python.org/3/library/functions.html#dir "dir") function. Any exception raised during the evaluation of the expression is caught, silenced and [`None`](https://docs.python.org/3/library/constants.html#None "None") is returned.
#### Previous topic
[`readline` — GNU readline interface](https://docs.python.org/3/library/readline.html "previous chapter")
#### Next topic
[Binary Data Services](https://docs.python.org/3/library/binary.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=rlcompleter+%E2%80%94+Completion+function+for+GNU+readline&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Frlcompleter.html&pagesource=library%2Frlcompleter.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/binary.html "Binary Data Services") |
  * [previous](https://docs.python.org/3/library/readline.html "readline — GNU readline interface") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Text Processing Services](https://docs.python.org/3/library/text.html) »
  * [`rlcompleter` — Completion function for GNU readline](https://docs.python.org/3/library/rlcompleter.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
