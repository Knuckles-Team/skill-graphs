[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[The initialization of the `sys.path` module search path](https://docs.python.org/3/library/sys_path_init.html "previous chapter")
#### Next topic
[`ast` — Abstract syntax trees](https://docs.python.org/3/library/ast.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Python+Language+Services&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Flanguage.html&pagesource=library%2Flanguage.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/ast.html "ast — Abstract syntax trees") |
  * [previous](https://docs.python.org/3/library/sys_path_init.html "The initialization of the sys.path module search path") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Python Language Services](https://docs.python.org/3/library/language.html)
  * |
  * Theme  Auto Light Dark |


# Python Language Services[¶](https://docs.python.org/3/library/language.html#python-language-services "Link to this heading")
Python provides a number of modules to assist in working with the Python language. These modules support tokenizing, parsing, syntax analysis, bytecode disassembly, and various other facilities.
These modules include:
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
  * [`symtable` — Access to the compiler’s symbol tables](https://docs.python.org/3/library/symtable.html)
    * [Generating Symbol Tables](https://docs.python.org/3/library/symtable.html#generating-symbol-tables)
    * [Examining Symbol Tables](https://docs.python.org/3/library/symtable.html#examining-symbol-tables)
    * [Command-Line Usage](https://docs.python.org/3/library/symtable.html#command-line-usage)
  * [`token` — Constants used with Python parse trees](https://docs.python.org/3/library/token.html)
  * [`keyword` — Testing for Python keywords](https://docs.python.org/3/library/keyword.html)
  * [`tokenize` — Tokenizer for Python source](https://docs.python.org/3/library/tokenize.html)
    * [Tokenizing Input](https://docs.python.org/3/library/tokenize.html#tokenizing-input)
    * [Command-Line Usage](https://docs.python.org/3/library/tokenize.html#command-line-usage)
    * [Examples](https://docs.python.org/3/library/tokenize.html#examples)
  * [`tabnanny` — Detection of ambiguous indentation](https://docs.python.org/3/library/tabnanny.html)
  * [`pyclbr` — Python module browser support](https://docs.python.org/3/library/pyclbr.html)
    * [Function Objects](https://docs.python.org/3/library/pyclbr.html#function-objects)
    * [Class Objects](https://docs.python.org/3/library/pyclbr.html#class-objects)
  * [`py_compile` — Compile Python source files](https://docs.python.org/3/library/py_compile.html)
    * [Command-Line Interface](https://docs.python.org/3/library/py_compile.html#command-line-interface)
  * [`compileall` — Byte-compile Python libraries](https://docs.python.org/3/library/compileall.html)
    * [Command-line use](https://docs.python.org/3/library/compileall.html#command-line-use)
    * [Public functions](https://docs.python.org/3/library/compileall.html#public-functions)
  * [`dis` — Disassembler for Python bytecode](https://docs.python.org/3/library/dis.html)
    * [Command-line interface](https://docs.python.org/3/library/dis.html#command-line-interface)
    * [Bytecode analysis](https://docs.python.org/3/library/dis.html#bytecode-analysis)
    * [Analysis functions](https://docs.python.org/3/library/dis.html#analysis-functions)
    * [Python Bytecode Instructions](https://docs.python.org/3/library/dis.html#python-bytecode-instructions)
    * [Opcode collections](https://docs.python.org/3/library/dis.html#opcode-collections)
  * [`pickletools` — Tools for pickle developers](https://docs.python.org/3/library/pickletools.html)
    * [Command-line usage](https://docs.python.org/3/library/pickletools.html#command-line-usage)
      * [Command-line options](https://docs.python.org/3/library/pickletools.html#command-line-options)
    * [Programmatic interface](https://docs.python.org/3/library/pickletools.html#programmatic-interface)


#### Previous topic
[The initialization of the `sys.path` module search path](https://docs.python.org/3/library/sys_path_init.html "previous chapter")
#### Next topic
[`ast` — Abstract syntax trees](https://docs.python.org/3/library/ast.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Python+Language+Services&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Flanguage.html&pagesource=library%2Flanguage.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/ast.html "ast — Abstract syntax trees") |
  * [previous](https://docs.python.org/3/library/sys_path_init.html "The initialization of the sys.path module search path") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Python Language Services](https://docs.python.org/3/library/language.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
