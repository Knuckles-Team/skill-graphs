## Opcode collections[¶](https://docs.python.org/3/library/dis.html#opcode-collections "Link to this heading")
These collections are provided for automatic introspection of bytecode instructions:
Changed in version 3.12: The collections now contain pseudo instructions and instrumented instructions as well. These are opcodes with values `>= MIN_PSEUDO_OPCODE` and `>= MIN_INSTRUMENTED_OPCODE`.

dis.opname[¶](https://docs.python.org/3/library/dis.html#dis.opname "Link to this definition")

Sequence of operation names, indexable using the bytecode.

dis.opmap[¶](https://docs.python.org/3/library/dis.html#dis.opmap "Link to this definition")

Dictionary mapping operation names to bytecodes.

dis.cmp_op[¶](https://docs.python.org/3/library/dis.html#dis.cmp_op "Link to this definition")

Sequence of all compare operation names.

dis.hasarg[¶](https://docs.python.org/3/library/dis.html#dis.hasarg "Link to this definition")

Sequence of bytecodes that use their argument.
Added in version 3.12.

dis.hasconst[¶](https://docs.python.org/3/library/dis.html#dis.hasconst "Link to this definition")

Sequence of bytecodes that access a constant.

dis.hasfree[¶](https://docs.python.org/3/library/dis.html#dis.hasfree "Link to this definition")

Sequence of bytecodes that access a [free (closure) variable](https://docs.python.org/3/glossary.html#term-closure-variable). ‘free’ in this context refers to names in the current scope that are referenced by inner scopes or names in outer scopes that are referenced from this scope. It does _not_ include references to global or builtin scopes.

dis.hasname[¶](https://docs.python.org/3/library/dis.html#dis.hasname "Link to this definition")

Sequence of bytecodes that access an attribute by name.

dis.hasjump[¶](https://docs.python.org/3/library/dis.html#dis.hasjump "Link to this definition")

Sequence of bytecodes that have a jump target. All jumps are relative.
Added in version 3.13.

dis.haslocal[¶](https://docs.python.org/3/library/dis.html#dis.haslocal "Link to this definition")

Sequence of bytecodes that access a local variable.

dis.hascompare[¶](https://docs.python.org/3/library/dis.html#dis.hascompare "Link to this definition")

Sequence of bytecodes of Boolean operations.

dis.hasexc[¶](https://docs.python.org/3/library/dis.html#dis.hasexc "Link to this definition")

Sequence of bytecodes that set an exception handler.
Added in version 3.12.

dis.hasjrel[¶](https://docs.python.org/3/library/dis.html#dis.hasjrel "Link to this definition")

Sequence of bytecodes that have a relative jump target.
Deprecated since version 3.13: All jumps are now relative. Use [`hasjump`](https://docs.python.org/3/library/dis.html#dis.hasjump "dis.hasjump").

dis.hasjabs[¶](https://docs.python.org/3/library/dis.html#dis.hasjabs "Link to this definition")

Sequence of bytecodes that have an absolute jump target.
Deprecated since version 3.13: All jumps are now relative. This list is empty.
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`dis` — Disassembler for Python bytecode](https://docs.python.org/3/library/dis.html)
    * [Command-line interface](https://docs.python.org/3/library/dis.html#command-line-interface)
    * [Bytecode analysis](https://docs.python.org/3/library/dis.html#bytecode-analysis)
    * [Analysis functions](https://docs.python.org/3/library/dis.html#analysis-functions)
    * [Python Bytecode Instructions](https://docs.python.org/3/library/dis.html#python-bytecode-instructions)
    * [Opcode collections](https://docs.python.org/3/library/dis.html#opcode-collections)


#### Previous topic
[`compileall` — Byte-compile Python libraries](https://docs.python.org/3/library/compileall.html "previous chapter")
#### Next topic
[`pickletools` — Tools for pickle developers](https://docs.python.org/3/library/pickletools.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=dis+%E2%80%94+Disassembler+for+Python+bytecode&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fdis.html&pagesource=library%2Fdis.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/pickletools.html "pickletools — Tools for pickle developers") |
  * [previous](https://docs.python.org/3/library/compileall.html "compileall — Byte-compile Python libraries") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Python Language Services](https://docs.python.org/3/library/language.html) »
  * [`dis` — Disassembler for Python bytecode](https://docs.python.org/3/library/dis.html)
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
