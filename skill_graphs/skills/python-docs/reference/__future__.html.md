[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`__future__` — Future statement definitions](https://docs.python.org/3/library/__future__.html)
    * [Module Contents](https://docs.python.org/3/library/__future__.html#module-contents)


#### Previous topic
[`traceback` — Print or retrieve a stack traceback](https://docs.python.org/3/library/traceback.html "previous chapter")
#### Next topic
[`gc` — Garbage Collector interface](https://docs.python.org/3/library/gc.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=__future__+%E2%80%94+Future+statement+definitions&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2F__future__.html&pagesource=library%2F__future__.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/gc.html "gc — Garbage Collector interface") |
  * [previous](https://docs.python.org/3/library/traceback.html "traceback — Print or retrieve a stack traceback") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Python Runtime Services](https://docs.python.org/3/library/python.html) »
  * [`__future__` — Future statement definitions](https://docs.python.org/3/library/__future__.html)
  * |
  * Theme  Auto Light Dark |


#  `__future__` — Future statement definitions[¶](https://docs.python.org/3/library/__future__.html#module-__future__ "Link to this heading")
**Source code:**
* * *
Imports of the form `from __future__ import feature` are called [future statements](https://docs.python.org/3/reference/simple_stmts.html#future). These are special-cased by the Python compiler to allow the use of new Python features in modules containing the future statement before the release in which the feature becomes standard.
While these future statements are given additional special meaning by the Python compiler, they are still executed like any other import statement and the `__future__` exists and is handled by the import system the same way any other Python module would be. This design serves three purposes:
  * To avoid confusing existing tools that analyze import statements and expect to find the modules they’re importing.
  * To document when incompatible changes were introduced, and when they will be — or were — made mandatory. This is a form of executable documentation, and can be inspected programmatically via importing `__future__` and examining its contents.
  * To ensure that [future statements](https://docs.python.org/3/reference/simple_stmts.html#future) run under releases prior to Python 2.1 at least yield runtime exceptions (the import of `__future__` will fail, because there was no module of that name prior to 2.1).


## Module Contents[¶](https://docs.python.org/3/library/__future__.html#module-contents "Link to this heading")
No feature description will ever be deleted from `__future__`. Since its introduction in Python 2.1 the following features have found their way into the language using this mechanism:
feature | optional in | mandatory in | effect
---|---|---|---

__future__.nested_scopes[¶](https://docs.python.org/3/library/__future__.html#future__.nested_scopes "Link to this definition")
| 2.1.0b1 | 2.2 | [**PEP 227**](https://peps.python.org/pep-0227/): _Statically Nested Scopes_

__future__.generators[¶](https://docs.python.org/3/library/__future__.html#future__.generators "Link to this definition")
| 2.2.0a1 | 2.3 | [**PEP 255**](https://peps.python.org/pep-0255/): _Simple Generators_

__future__.division[¶](https://docs.python.org/3/library/__future__.html#future__.division "Link to this definition")
| 2.2.0a2 | 3.0 | [**PEP 238**](https://peps.python.org/pep-0238/): _Changing the Division Operator_

__future__.absolute_import[¶](https://docs.python.org/3/library/__future__.html#future__.absolute_import "Link to this definition")
| 2.5.0a1 | 3.0 | [**PEP 328**](https://peps.python.org/pep-0328/): _Imports: Multi-Line and Absolute/Relative_

__future__.with_statement[¶](https://docs.python.org/3/library/__future__.html#future__.with_statement "Link to this definition")
| 2.5.0a1 | 2.6 | [**PEP 343**](https://peps.python.org/pep-0343/): _The “with” Statement_

__future__.print_function[¶](https://docs.python.org/3/library/__future__.html#future__.print_function "Link to this definition")
| 2.6.0a2 | 3.0 | [**PEP 3105**](https://peps.python.org/pep-3105/): _Make print a function_

__future__.unicode_literals[¶](https://docs.python.org/3/library/__future__.html#future__.unicode_literals "Link to this definition")
| 2.6.0a2 | 3.0 | [**PEP 3112**](https://peps.python.org/pep-3112/): _Bytes literals in Python 3000_

__future__.generator_stop[¶](https://docs.python.org/3/library/__future__.html#future__.generator_stop "Link to this definition")
| 3.5.0b1 | 3.7 | [**PEP 479**](https://peps.python.org/pep-0479/): _StopIteration handling inside generators_

__future__.annotations[¶](https://docs.python.org/3/library/__future__.html#future__.annotations "Link to this definition")
| 3.7.0b1 | Never [[1]](https://docs.python.org/3/library/__future__.html#id2) | [**PEP 563**](https://peps.python.org/pep-0563/): _Postponed evaluation of annotations_ , [**PEP 649**](https://peps.python.org/pep-0649/): _Deferred evaluation of annotations using descriptors_

_class_ __future__._Feature[¶](https://docs.python.org/3/library/__future__.html#future__._Feature "Link to this definition")

Each statement in `__future__.py` is of the form:
Copy```
FeatureName = _Feature(OptionalRelease, MandatoryRelease,
                       CompilerFlag)

```

where, normally, _OptionalRelease_ is less than _MandatoryRelease_ , and both are 5-tuples of the same form as [`sys.version_info`](https://docs.python.org/3/library/sys.html#sys.version_info "sys.version_info"):
Copy```
(PY_MAJOR_VERSION, # the 2 in 2.1.0a3; an int
 PY_MINOR_VERSION, # the 1; an int
 PY_MICRO_VERSION, # the 0; an int
 PY_RELEASE_LEVEL, # "alpha", "beta", "candidate" or "final"; string
 PY_RELEASE_SERIAL # the 3; an int
)

```


_Feature.getOptionalRelease()[¶](https://docs.python.org/3/library/__future__.html#future__._Feature.getOptionalRelease "Link to this definition")

_OptionalRelease_ records the first release in which the feature was accepted.

_Feature.getMandatoryRelease()[¶](https://docs.python.org/3/library/__future__.html#future__._Feature.getMandatoryRelease "Link to this definition")

In the case of a _MandatoryRelease_ that has not yet occurred, _MandatoryRelease_ predicts the release in which the feature will become part of the language.
Else _MandatoryRelease_ records when the feature became part of the language; in releases at or after that, modules no longer need a future statement to use the feature in question, but may continue to use such imports.
_MandatoryRelease_ may also be `None`, meaning that a planned feature got dropped or that it is not yet decided.

_Feature.compiler_flag[¶](https://docs.python.org/3/library/__future__.html#future__._Feature.compiler_flag "Link to this definition")

_CompilerFlag_ is the (bitfield) flag that should be passed in the fourth argument to the built-in function [`compile()`](https://docs.python.org/3/library/functions.html#compile "compile") to enable the feature in dynamically compiled code. This flag is stored in the `_Feature.compiler_flag` attribute on [`_Feature`](https://docs.python.org/3/library/__future__.html#future__._Feature "__future__._Feature") instances. [[1](https://docs.python.org/3/library/__future__.html#id1)]
`from __future__ import annotations` was previously scheduled to become mandatory in Python 3.10, but the change was delayed and ultimately canceled. This feature will eventually be deprecated and removed. See [**PEP 649**](https://peps.python.org/pep-0649/) and [**PEP 749**](https://peps.python.org/pep-0749/).
See also

[Future statements](https://docs.python.org/3/reference/simple_stmts.html#future)

How the compiler treats future imports.

[**PEP 236**](https://peps.python.org/pep-0236/) - Back to the __future__

The original proposal for the __future__ mechanism.
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`__future__` — Future statement definitions](https://docs.python.org/3/library/__future__.html)
    * [Module Contents](https://docs.python.org/3/library/__future__.html#module-contents)


#### Previous topic
[`traceback` — Print or retrieve a stack traceback](https://docs.python.org/3/library/traceback.html "previous chapter")
#### Next topic
[`gc` — Garbage Collector interface](https://docs.python.org/3/library/gc.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=__future__+%E2%80%94+Future+statement+definitions&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2F__future__.html&pagesource=library%2F__future__.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/gc.html "gc — Garbage Collector interface") |
  * [previous](https://docs.python.org/3/library/traceback.html "traceback — Print or retrieve a stack traceback") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Python Runtime Services](https://docs.python.org/3/library/python.html) »
  * [`__future__` — Future statement definitions](https://docs.python.org/3/library/__future__.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
