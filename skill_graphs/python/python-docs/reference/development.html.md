[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`turtle` — Turtle graphics](https://docs.python.org/3/library/turtle.html "previous chapter")
#### Next topic
[`typing` — Support for type hints](https://docs.python.org/3/library/typing.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Development+Tools&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fdevelopment.html&pagesource=library%2Fdevelopment.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/typing.html "typing — Support for type hints") |
  * [previous](https://docs.python.org/3/library/turtle.html "turtle — Turtle graphics") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Development Tools](https://docs.python.org/3/library/development.html)
  * |
  * Theme  Auto Light Dark |


# Development Tools[¶](https://docs.python.org/3/library/development.html#development-tools "Link to this heading")
The modules described in this chapter help you write software. For example, the [`pydoc`](https://docs.python.org/3/library/pydoc.html#module-pydoc "pydoc: Documentation generator and online help system.") module takes a module and generates documentation based on the module’s contents. The [`doctest`](https://docs.python.org/3/library/doctest.html#module-doctest "doctest: Test pieces of code within docstrings.") and [`unittest`](https://docs.python.org/3/library/unittest.html#module-unittest "unittest: Unit testing framework for Python.") modules contains frameworks for writing unit tests that automatically exercise code and verify that the expected output is produced.
The list of modules described in this chapter is:
  * [`typing` — Support for type hints](https://docs.python.org/3/library/typing.html)
    * [Specification for the Python Type System](https://docs.python.org/3/library/typing.html#specification-for-the-python-type-system)
    * [Type aliases](https://docs.python.org/3/library/typing.html#type-aliases)
    * [NewType](https://docs.python.org/3/library/typing.html#newtype)
    * [Annotating callable objects](https://docs.python.org/3/library/typing.html#annotating-callable-objects)
    * [Generics](https://docs.python.org/3/library/typing.html#generics)
    * [Annotating tuples](https://docs.python.org/3/library/typing.html#annotating-tuples)
    * [The type of class objects](https://docs.python.org/3/library/typing.html#the-type-of-class-objects)
    * [Annotating generators and coroutines](https://docs.python.org/3/library/typing.html#annotating-generators-and-coroutines)
    * [User-defined generic types](https://docs.python.org/3/library/typing.html#user-defined-generic-types)
    * [The `Any` type](https://docs.python.org/3/library/typing.html#the-any-type)
    * [Nominal vs structural subtyping](https://docs.python.org/3/library/typing.html#nominal-vs-structural-subtyping)
    * [Module contents](https://docs.python.org/3/library/typing.html#module-contents)
      * [Special typing primitives](https://docs.python.org/3/library/typing.html#special-typing-primitives)
        * [Special types](https://docs.python.org/3/library/typing.html#special-types)
        * [Special forms](https://docs.python.org/3/library/typing.html#special-forms)
        * [Building generic types and type aliases](https://docs.python.org/3/library/typing.html#building-generic-types-and-type-aliases)
        * [Other special directives](https://docs.python.org/3/library/typing.html#other-special-directives)
      * [Protocols](https://docs.python.org/3/library/typing.html#protocols)
      * [ABCs and Protocols for working with I/O](https://docs.python.org/3/library/typing.html#abcs-and-protocols-for-working-with-i-o)
      * [Functions and decorators](https://docs.python.org/3/library/typing.html#functions-and-decorators)
      * [Introspection helpers](https://docs.python.org/3/library/typing.html#introspection-helpers)
      * [Constant](https://docs.python.org/3/library/typing.html#constant)
      * [Deprecated aliases](https://docs.python.org/3/library/typing.html#deprecated-aliases)
        * [Aliases to built-in types](https://docs.python.org/3/library/typing.html#aliases-to-built-in-types)
        * [Aliases to types in `collections`](https://docs.python.org/3/library/typing.html#aliases-to-types-in-collections)
        * [Aliases to other concrete types](https://docs.python.org/3/library/typing.html#aliases-to-other-concrete-types)
        * [Aliases to container ABCs in `collections.abc`](https://docs.python.org/3/library/typing.html#aliases-to-container-abcs-in-collections-abc)
        * [Aliases to asynchronous ABCs in `collections.abc`](https://docs.python.org/3/library/typing.html#aliases-to-asynchronous-abcs-in-collections-abc)
        * [Aliases to other ABCs in `collections.abc`](https://docs.python.org/3/library/typing.html#aliases-to-other-abcs-in-collections-abc)
        * [Aliases to `contextlib` ABCs](https://docs.python.org/3/library/typing.html#aliases-to-contextlib-abcs)
    * [Deprecation Timeline of Major Features](https://docs.python.org/3/library/typing.html#deprecation-timeline-of-major-features)
  * [`pydoc` — Documentation generator and online help system](https://docs.python.org/3/library/pydoc.html)
  * [Python Development Mode](https://docs.python.org/3/library/devmode.html)
    * [Effects of the Python Development Mode](https://docs.python.org/3/library/devmode.html#effects-of-the-python-development-mode)
    * [ResourceWarning Example](https://docs.python.org/3/library/devmode.html#resourcewarning-example)
    * [Bad file descriptor error example](https://docs.python.org/3/library/devmode.html#bad-file-descriptor-error-example)
  * [`doctest` — Test interactive Python examples](https://docs.python.org/3/library/doctest.html)
    * [Simple Usage: Checking Examples in Docstrings](https://docs.python.org/3/library/doctest.html#simple-usage-checking-examples-in-docstrings)
    * [Simple Usage: Checking Examples in a Text File](https://docs.python.org/3/library/doctest.html#simple-usage-checking-examples-in-a-text-file)
    * [Command-line Usage](https://docs.python.org/3/library/doctest.html#command-line-usage)
    * [How It Works](https://docs.python.org/3/library/doctest.html#how-it-works)
      * [Which Docstrings Are Examined?](https://docs.python.org/3/library/doctest.html#which-docstrings-are-examined)
      * [How are Docstring Examples Recognized?](https://docs.python.org/3/library/doctest.html#how-are-docstring-examples-recognized)
      * [What’s the Execution Context?](https://docs.python.org/3/library/doctest.html#what-s-the-execution-context)
      * [What About Exceptions?](https://docs.python.org/3/library/doctest.html#what-about-exceptions)
      * [Option Flags](https://docs.python.org/3/library/doctest.html#option-flags)
      * [Directives](https://docs.python.org/3/library/doctest.html#directives)
      * [Warnings](https://docs.python.org/3/library/doctest.html#warnings)
    * [Basic API](https://docs.python.org/3/library/doctest.html#basic-api)
    * [Unittest API](https://docs.python.org/3/library/doctest.html#unittest-api)
    * [Advanced API](https://docs.python.org/3/library/doctest.html#advanced-api)
      * [DocTest Objects](https://docs.python.org/3/library/doctest.html#doctest-objects)
      * [Example Objects](https://docs.python.org/3/library/doctest.html#example-objects)
      * [DocTestFinder objects](https://docs.python.org/3/library/doctest.html#doctestfinder-objects)
      * [DocTestParser objects](https://docs.python.org/3/library/doctest.html#doctestparser-objects)
      * [TestResults objects](https://docs.python.org/3/library/doctest.html#testresults-objects)
      * [DocTestRunner objects](https://docs.python.org/3/library/doctest.html#doctestrunner-objects)
      * [OutputChecker objects](https://docs.python.org/3/library/doctest.html#outputchecker-objects)
    * [Debugging](https://docs.python.org/3/library/doctest.html#debugging)
    * [Soapbox](https://docs.python.org/3/library/doctest.html#soapbox)
  * [`unittest` — Unit testing framework](https://docs.python.org/3/library/unittest.html)
    * [Basic example](https://docs.python.org/3/library/unittest.html#basic-example)
    * [Command-Line Interface](https://docs.python.org/3/library/unittest.html#command-line-interface)
      * [Command-line options](https://docs.python.org/3/library/unittest.html#command-line-options)
    * [Test Discovery](https://docs.python.org/3/library/unittest.html#test-discovery)
    * [Organizing test code](https://docs.python.org/3/library/unittest.html#organizing-test-code)
    * [Reusing old test code](https://docs.python.org/3/library/unittest.html#re-using-old-test-code)
    * [Skipping tests and expected failures](https://docs.python.org/3/library/unittest.html#skipping-tests-and-expected-failures)
    * [Distinguishing test iterations using subtests](https://docs.python.org/3/library/unittest.html#distinguishing-test-iterations-using-subtests)
    * [Classes and functions](https://docs.python.org/3/library/unittest.html#classes-and-functions)
      * [Test cases](https://docs.python.org/3/library/unittest.html#test-cases)
      * [Grouping tests](https://docs.python.org/3/library/unittest.html#grouping-tests)
      * [Loading and running tests](https://docs.python.org/3/library/unittest.html#loading-and-running-tests)
        * [load_tests Protocol](https://docs.python.org/3/library/unittest.html#load-tests-protocol)
    * [Class and Module Fixtures](https://docs.python.org/3/library/unittest.html#class-and-module-fixtures)
      * [setUpClass and tearDownClass](https://docs.python.org/3/library/unittest.html#setupclass-and-teardownclass)
      * [setUpModule and tearDownModule](https://docs.python.org/3/library/unittest.html#setupmodule-and-teardownmodule)
    * [Signal Handling](https://docs.python.org/3/library/unittest.html#signal-handling)
  * [`unittest.mock` — mock object library](https://docs.python.org/3/library/unittest.mock.html)
    * [Quick Guide](https://docs.python.org/3/library/unittest.mock.html#quick-guide)
    * [The Mock Class](https://docs.python.org/3/library/unittest.mock.html#the-mock-class)
      * [Calling](https://docs.python.org/3/library/unittest.mock.html#calling)
      * [Deleting Attributes](https://docs.python.org/3/library/unittest.mock.html#deleting-attributes)
      * [Mock names and the name attribute](https://docs.python.org/3/library/unittest.mock.html#mock-names-and-the-name-attribute)
      * [Attaching Mocks as Attributes](https://docs.python.org/3/library/unittest.mock.html#attaching-mocks-as-attributes)
    * [The patchers](https://docs.python.org/3/library/unittest.mock.html#the-patchers)
      * [patch](https://docs.python.org/3/library/unittest.mock.html#patch)
      * [patch.object](https://docs.python.org/3/library/unittest.mock.html#patch-object)
      * [patch.dict](https://docs.python.org/3/library/unittest.mock.html#patch-dict)
      * [patch.multiple](https://docs.python.org/3/library/unittest.mock.html#patch-multiple)
      * [patch methods: start and stop](https://docs.python.org/3/library/unittest.mock.html#patch-methods-start-and-stop)
      * [patch builtins](https://docs.python.org/3/library/unittest.mock.html#patch-builtins)
      * [TEST_PREFIX](https://docs.python.org/3/library/unittest.mock.html#test-prefix)
      * [Nesting Patch Decorators](https://docs.python.org/3/library/unittest.mock.html#nesting-patch-decorators)
      * [Where to patch](https://docs.python.org/3/library/unittest.mock.html#where-to-patch)
      * [Patching Descriptors and Proxy Objects](https://docs.python.org/3/library/unittest.mock.html#patching-descriptors-and-proxy-objects)
    * [MagicMock and magic method support](https://docs.python.org/3/library/unittest.mock.html#magicmock-and-magic-method-support)
      * [Mocking Magic Methods](https://docs.python.org/3/library/unittest.mock.html#mocking-magic-methods)
      * [Magic Mock](https://docs.python.org/3/library/unittest.mock.html#magic-mock)
    * [Helpers](https://docs.python.org/3/library/unittest.mock.html#helpers)
      * [sentinel](https://docs.python.org/3/library/unittest.mock.html#sentinel)
      * [DEFAULT](https://docs.python.org/3/library/unittest.mock.html#default)
      * [call](https://docs.python.org/3/library/unittest.mock.html#call)
      * [create_autospec](https://docs.python.org/3/library/unittest.mock.html#create-autospec)
      * [ANY](https://docs.python.org/3/library/unittest.mock.html#any)
      * [FILTER_DIR](https://docs.python.org/3/library/unittest.mock.html#filter-dir)
      * [mock_open](https://docs.python.org/3/library/unittest.mock.html#mock-open)
      * [Autospeccing](https://docs.python.org/3/library/unittest.mock.html#autospeccing)
      * [Sealing mocks](https://docs.python.org/3/library/unittest.mock.html#sealing-mocks)
    * [Order of precedence of `side_effect`, `return_value` and _wraps_](https://docs.python.org/3/library/unittest.mock.html#order-of-precedence-of-side-effect-return-value-and-wraps)
  * [`unittest.mock` — getting started](https://docs.python.org/3/library/unittest.mock-examples.html)
    * [Using Mock](https://docs.python.org/3/library/unittest.mock-examples.html#using-mock)
      * [Mock Patching Methods](https://docs.python.org/3/library/unittest.mock-examples.html#mock-patching-methods)
      * [Mock for Method Calls on an Object](https://docs.python.org/3/library/unittest.mock-examples.html#mock-for-method-calls-on-an-object)
      * [Mocking Classes](https://docs.python.org/3/library/unittest.mock-examples.html#mocking-classes)
      * [Naming your mocks](https://docs.python.org/3/library/unittest.mock-examples.html#naming-your-mocks)
      * [Tracking all Calls](https://docs.python.org/3/library/unittest.mock-examples.html#tracking-all-calls)
      * [Setting Return Values and Attributes](https://docs.python.org/3/library/unittest.mock-examples.html#setting-return-values-and-attributes)
      * [Raising exceptions with mocks](https://docs.python.org/3/library/unittest.mock-examples.html#raising-exceptions-with-mocks)
      * [Side effect functions and iterables](https://docs.python.org/3/library/unittest.mock-examples.html#side-effect-functions-and-iterables)
      * [Mocking asynchronous iterators](https://docs.python.org/3/library/unittest.mock-examples.html#mocking-asynchronous-iterators)
      * [Mocking asynchronous context manager](https://docs.python.org/3/library/unittest.mock-examples.html#mocking-asynchronous-context-manager)
      * [Creating a Mock from an Existing Object](https://docs.python.org/3/library/unittest.mock-examples.html#creating-a-mock-from-an-existing-object)
      * [Using side_effect to return per file content](https://docs.python.org/3/library/unittest.mock-examples.html#using-side-effect-to-return-per-file-content)
    * [Patch Decorators](https://docs.python.org/3/library/unittest.mock-examples.html#patch-decorators)
    * [Further Examples](https://docs.python.org/3/library/unittest.mock-examples.html#further-examples)
      * [Mocking chained calls](https://docs.python.org/3/library/unittest.mock-examples.html#mocking-chained-calls)
      * [Partial mocking](https://docs.python.org/3/library/unittest.mock-examples.html#partial-mocking)
      * [Mocking a Generator Method](https://docs.python.org/3/library/unittest.mock-examples.html#mocking-a-generator-method)
      * [Applying the same patch to every test method](https://docs.python.org/3/library/unittest.mock-examples.html#applying-the-same-patch-to-every-test-method)
      * [Mocking Unbound Methods](https://docs.python.org/3/library/unittest.mock-examples.html#mocking-unbound-methods)
      * [Checking multiple calls with mock](https://docs.python.org/3/library/unittest.mock-examples.html#checking-multiple-calls-with-mock)
      * [Coping with mutable arguments](https://docs.python.org/3/library/unittest.mock-examples.html#coping-with-mutable-arguments)
      * [Nesting Patches](https://docs.python.org/3/library/unittest.mock-examples.html#nesting-patches)
      * [Mocking a dictionary with MagicMock](https://docs.python.org/3/library/unittest.mock-examples.html#mocking-a-dictionary-with-magicmock)
      * [Mock subclasses and their attributes](https://docs.python.org/3/library/unittest.mock-examples.html#mock-subclasses-and-their-attributes)
      * [Mocking imports with patch.dict](https://docs.python.org/3/library/unittest.mock-examples.html#mocking-imports-with-patch-dict)
      * [Tracking order of calls and less verbose call assertions](https://docs.python.org/3/library/unittest.mock-examples.html#tracking-order-of-calls-and-less-verbose-call-assertions)
      * [More complex argument matching](https://docs.python.org/3/library/unittest.mock-examples.html#more-complex-argument-matching)
  * [`test` — Regression tests package for Python](https://docs.python.org/3/library/test.html)
    * [Writing Unit Tests for the `test` package](https://docs.python.org/3/library/test.html#writing-unit-tests-for-the-test-package)
    * [Running tests using the command-line interface](https://docs.python.org/3/library/test.html#module-test.regrtest)
  * [`test.support` — Utilities for the Python test suite](https://docs.python.org/3/library/test.html#module-test.support)
  * [`test.support.socket_helper` — Utilities for socket tests](https://docs.python.org/3/library/test.html#module-test.support.socket_helper)
  * [`test.support.script_helper` — Utilities for the Python execution tests](https://docs.python.org/3/library/test.html#module-test.support.script_helper)
  * [`test.support.bytecode_helper` — Support tools for testing correct bytecode generation](https://docs.python.org/3/library/test.html#module-test.support.bytecode_helper)
  * [`test.support.threading_helper` — Utilities for threading tests](https://docs.python.org/3/library/test.html#module-test.support.threading_helper)
  * [`test.support.os_helper` — Utilities for os tests](https://docs.python.org/3/library/test.html#module-test.support.os_helper)
  * [`test.support.import_helper` — Utilities for import tests](https://docs.python.org/3/library/test.html#module-test.support.import_helper)
  * [`test.support.warnings_helper` — Utilities for warnings tests](https://docs.python.org/3/library/test.html#module-test.support.warnings_helper)


#### Previous topic
[`turtle` — Turtle graphics](https://docs.python.org/3/library/turtle.html "previous chapter")
#### Next topic
[`typing` — Support for type hints](https://docs.python.org/3/library/typing.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Development+Tools&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fdevelopment.html&pagesource=library%2Fdevelopment.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/typing.html "typing — Support for type hints") |
  * [previous](https://docs.python.org/3/library/turtle.html "turtle — Turtle graphics") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Development Tools](https://docs.python.org/3/library/development.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
