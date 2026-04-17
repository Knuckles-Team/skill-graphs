[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
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


#### Previous topic
[`unittest.mock` — mock object library](https://docs.python.org/3/library/unittest.mock.html "previous chapter")
#### Next topic
[`test` — Regression tests package for Python](https://docs.python.org/3/library/test.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=unittest.mock+%E2%80%94+getting+started&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Funittest.mock-examples.html&pagesource=library%2Funittest.mock-examples.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/test.html "test — Regression tests package for Python") |
  * [previous](https://docs.python.org/3/library/unittest.mock.html "unittest.mock — mock object library") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Development Tools](https://docs.python.org/3/library/development.html) »
  * [`unittest.mock` — getting started](https://docs.python.org/3/library/unittest.mock-examples.html)
  * |
  * Theme  Auto Light Dark |
