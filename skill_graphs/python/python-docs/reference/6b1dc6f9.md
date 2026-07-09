[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
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


#### Previous topic
[`unittest` — Unit testing framework](https://docs.python.org/3/library/unittest.html "previous chapter")
#### Next topic
[`unittest.mock` — getting started](https://docs.python.org/3/library/unittest.mock-examples.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=unittest.mock+%E2%80%94+mock+object+library&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Funittest.mock.html&pagesource=library%2Funittest.mock.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/unittest.mock-examples.html "unittest.mock — getting started") |
  * [previous](https://docs.python.org/3/library/unittest.html "unittest — Unit testing framework") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Development Tools](https://docs.python.org/3/library/development.html) »
  * [`unittest.mock` — mock object library](https://docs.python.org/3/library/unittest.mock.html)
  * |
  * Theme  Auto Light Dark |
