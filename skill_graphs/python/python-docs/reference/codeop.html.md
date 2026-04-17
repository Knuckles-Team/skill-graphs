[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`code` — Interpreter base classes](https://docs.python.org/3/library/code.html "previous chapter")
#### Next topic
[Importing Modules](https://docs.python.org/3/library/modules.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=codeop+%E2%80%94+Compile+Python+code&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fcodeop.html&pagesource=library%2Fcodeop.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/modules.html "Importing Modules") |
  * [previous](https://docs.python.org/3/library/code.html "code — Interpreter base classes") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Custom Python Interpreters](https://docs.python.org/3/library/custominterp.html) »
  * [`codeop` — Compile Python code](https://docs.python.org/3/library/codeop.html)
  * |
  * Theme  Auto Light Dark |


#  `codeop` — Compile Python code[¶](https://docs.python.org/3/library/codeop.html#module-codeop "Link to this heading")
**Source code:**
* * *
The `codeop` module provides utilities upon which the Python read-eval-print loop can be emulated, as is done in the [`code`](https://docs.python.org/3/library/code.html#module-code "code: Facilities to implement read-eval-print loops.") module. As a result, you probably don’t want to use the module directly; if you want to include such a loop in your program you probably want to use the `code` module instead.
There are two parts to this job:
  1. Being able to tell if a line of input completes a Python statement: in short, telling whether to print ‘`>>>`’ or ‘`...`’ next.
  2. Remembering which future statements the user has entered, so subsequent input can be compiled with these in effect.


The `codeop` module provides a way of doing each of these things, and a way of doing them both.
To do just the former:

codeop.compile_command(_source_ , _filename ='<input>'_, _symbol ='single'_)[¶](https://docs.python.org/3/library/codeop.html#codeop.compile_command "Link to this definition")

Tries to compile _source_ , which should be a string of Python code and return a code object if _source_ is valid Python code. In that case, the filename attribute of the code object will be _filename_ , which defaults to `'<input>'`. Returns `None` if _source_ is _not_ valid Python code, but is a prefix of valid Python code.
If there is a problem with _source_ , an exception will be raised. [`SyntaxError`](https://docs.python.org/3/library/exceptions.html#SyntaxError "SyntaxError") is raised if there is invalid Python syntax, and [`OverflowError`](https://docs.python.org/3/library/exceptions.html#OverflowError "OverflowError") or [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") if there is an invalid literal.
The _symbol_ argument determines whether _source_ is compiled as a statement (`'single'`, the default), as a sequence of [statement](https://docs.python.org/3/glossary.html#term-statement) (`'exec'`) or as an [expression](https://docs.python.org/3/glossary.html#term-expression) (`'eval'`). Any other value will cause [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") to be raised.
Note
It is possible (but not likely) that the parser stops parsing with a successful outcome before reaching the end of the source; in this case, trailing symbols may be ignored instead of causing an error. For example, a backslash followed by two newlines may be followed by arbitrary garbage. This will be fixed once the API for the parser is better.

_class_ codeop.Compile[¶](https://docs.python.org/3/library/codeop.html#codeop.Compile "Link to this definition")

Instances of this class have [`__call__()`](https://docs.python.org/3/reference/datamodel.html#object.__call__ "object.__call__") methods identical in signature to the built-in function [`compile()`](https://docs.python.org/3/library/functions.html#compile "compile"), but with the difference that if the instance compiles program text containing a [`__future__`](https://docs.python.org/3/library/__future__.html#module-__future__ "__future__: Future statement definitions") statement, the instance ‘remembers’ and compiles all subsequent program texts with the statement in force.

_class_ codeop.CommandCompiler[¶](https://docs.python.org/3/library/codeop.html#codeop.CommandCompiler "Link to this definition")

Instances of this class have [`__call__()`](https://docs.python.org/3/reference/datamodel.html#object.__call__ "object.__call__") methods identical in signature to [`compile_command()`](https://docs.python.org/3/library/codeop.html#codeop.compile_command "codeop.compile_command"); the difference is that if the instance compiles program text containing a [`__future__`](https://docs.python.org/3/library/__future__.html#module-__future__ "__future__: Future statement definitions") statement, the instance ‘remembers’ and compiles all subsequent program texts with the statement in force.
#### Previous topic
[`code` — Interpreter base classes](https://docs.python.org/3/library/code.html "previous chapter")
#### Next topic
[Importing Modules](https://docs.python.org/3/library/modules.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=codeop+%E2%80%94+Compile+Python+code&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fcodeop.html&pagesource=library%2Fcodeop.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/modules.html "Importing Modules") |
  * [previous](https://docs.python.org/3/library/code.html "code — Interpreter base classes") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Custom Python Interpreters](https://docs.python.org/3/library/custominterp.html) »
  * [`codeop` — Compile Python code](https://docs.python.org/3/library/codeop.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
