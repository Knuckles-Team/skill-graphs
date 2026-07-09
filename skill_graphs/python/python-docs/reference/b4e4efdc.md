
ast.PyCF_ALLOW_TOP_LEVEL_AWAIT[¶](https://docs.python.org/3/library/ast.html#ast.PyCF_ALLOW_TOP_LEVEL_AWAIT "Link to this definition")

Enables support for top-level `await`, `async for`, `async with` and async comprehensions.
Added in version 3.8.

ast.PyCF_ONLY_AST[¶](https://docs.python.org/3/library/ast.html#ast.PyCF_ONLY_AST "Link to this definition")

Generates and returns an abstract syntax tree instead of returning a compiled code object.

ast.PyCF_OPTIMIZED_AST[¶](https://docs.python.org/3/library/ast.html#ast.PyCF_OPTIMIZED_AST "Link to this definition")

The returned AST is optimized according to the _optimize_ argument in [`compile()`](https://docs.python.org/3/library/functions.html#compile "compile") or [`ast.parse()`](https://docs.python.org/3/library/ast.html#ast.parse "ast.parse").
Added in version 3.13.

ast.PyCF_TYPE_COMMENTS[¶](https://docs.python.org/3/library/ast.html#ast.PyCF_TYPE_COMMENTS "Link to this definition")

Enables support for [**PEP 484**](https://peps.python.org/pep-0484/) and [**PEP 526**](https://peps.python.org/pep-0526/) style type comments (`# type: <type>`, `# type: ignore <stuff>`).
Added in version 3.8.

ast.compare(_a_ , _b_ , _/_ , _*_ , _compare_attributes =False_)[¶](https://docs.python.org/3/library/ast.html#ast.compare "Link to this definition")

Recursively compares two ASTs.
_compare_attributes_ affects whether AST attributes are considered in the comparison. If _compare_attributes_ is `False` (default), then attributes are ignored. Otherwise they must all be equal. This option is useful to check whether the ASTs are structurally equal but differ in whitespace or similar details. Attributes include line numbers and column offsets.
Added in version 3.14.
## Command-line usage[¶](https://docs.python.org/3/library/ast.html#command-line-usage "Link to this heading")
Added in version 3.9.
The `ast` module can be executed as a script from the command line. It is as simple as:
Copy```
python -m ast [-m <mode>] [-a] [infile]

```

The following options are accepted:

-h, --help[¶](https://docs.python.org/3/library/ast.html#cmdoption-ast-h "Link to this definition")

Show the help message and exit.

-m <mode>[¶](https://docs.python.org/3/library/ast.html#cmdoption-ast-m "Link to this definition")


--mode <mode>[¶](https://docs.python.org/3/library/ast.html#cmdoption-ast-mode "Link to this definition")

Specify what kind of code must be compiled, like the _mode_ argument in [`parse()`](https://docs.python.org/3/library/ast.html#ast.parse "ast.parse").

--no-type-comments[¶](https://docs.python.org/3/library/ast.html#cmdoption-ast-no-type-comments "Link to this definition")

Don’t parse type comments.

-a, --include-attributes[¶](https://docs.python.org/3/library/ast.html#cmdoption-ast-a "Link to this definition")

Include attributes such as line numbers and column offsets.

-i <indent>[¶](https://docs.python.org/3/library/ast.html#cmdoption-ast-i "Link to this definition")


--indent <indent>[¶](https://docs.python.org/3/library/ast.html#cmdoption-ast-indent "Link to this definition")

Indentation of nodes in AST (number of spaces).

--feature-version <version>[¶](https://docs.python.org/3/library/ast.html#cmdoption-ast-feature-version "Link to this definition")

Python version in the format 3.x (for example, 3.10). Defaults to the current version of the interpreter.
Added in version 3.14.

-O <level>[¶](https://docs.python.org/3/library/ast.html#cmdoption-ast-O "Link to this definition")


--optimize <level>[¶](https://docs.python.org/3/library/ast.html#cmdoption-ast-optimize "Link to this definition")

Optimization level for parser. Defaults to no optimization.
Added in version 3.14.

--show-empty[¶](https://docs.python.org/3/library/ast.html#cmdoption-ast-show-empty "Link to this definition")

Show empty lists and fields that are `None`. Defaults to not showing empty objects.
Added in version 3.14.
If `infile` is specified its contents are parsed to AST and dumped to stdout. Otherwise, the content is read from stdin.
See also
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`ast` — Abstract syntax trees](https://docs.python.org/3/library/ast.html)
    * [Abstract grammar](https://docs.python.org/3/library/ast.html#abstract-grammar)
    * [Node classes](https://docs.python.org/3/library/ast.html#node-classes)
      * [Root nodes](https://docs.python.org/3/library/ast.html#root-nodes)
      * [Literals](https://docs.python.org/3/library/ast.html#literals)
      * [Variables](https://docs.python.org/3/library/ast.html#variables)
      * [Expressions](https://docs.python.org/3/library/ast.html#expressions)
        * [Subscripting](https://docs.python.org/3/library/ast.html#subscripting)
        * [Comprehensions](https://docs.python.org/3/library/ast.html#comprehensions)
      * [Statements](https://docs.python.org/3/library/ast.html#statements)
        * [Imports](https://docs.python.org/3/library/ast.html#imports)
      * [Control flow](https://docs.python.org/3/library/ast.html#control-flow)
      * [Pattern matching](https://docs.python.org/3/library/ast.html#pattern-matching)
      * [Type annotations](https://docs.python.org/3/library/ast.html#type-annotations)
      * [Type parameters](https://docs.python.org/3/library/ast.html#type-parameters)
      * [Function and class definitions](https://docs.python.org/3/library/ast.html#function-and-class-definitions)
      * [Async and await](https://docs.python.org/3/library/ast.html#async-and-await)
    * [`ast` helpers](https://docs.python.org/3/library/ast.html#ast-helpers)
    * [Compiler flags](https://docs.python.org/3/library/ast.html#compiler-flags)
    * [Command-line usage](https://docs.python.org/3/library/ast.html#command-line-usage)


#### Previous topic
[Python Language Services](https://docs.python.org/3/library/language.html "previous chapter")
#### Next topic
[`symtable` — Access to the compiler’s symbol tables](https://docs.python.org/3/library/symtable.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=ast+%E2%80%94+Abstract+syntax+trees&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fast.html&pagesource=library%2Fast.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/symtable.html "symtable — Access to the compiler’s symbol tables") |
  * [previous](https://docs.python.org/3/library/language.html "Python Language Services") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Python Language Services](https://docs.python.org/3/library/language.html) »
  * [`ast` — Abstract syntax trees](https://docs.python.org/3/library/ast.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)
