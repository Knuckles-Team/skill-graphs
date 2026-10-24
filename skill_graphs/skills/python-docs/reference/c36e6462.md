
unittest.removeResult(_result_)[¶](https://docs.python.org/3/library/unittest.html#unittest.removeResult "Link to this definition")

Remove a registered result. Once a result has been removed then [`stop()`](https://docs.python.org/3/library/unittest.html#unittest.TestResult.stop "unittest.TestResult.stop") will no longer be called on that result object in response to a control-c.

unittest.removeHandler(_function =None_)[¶](https://docs.python.org/3/library/unittest.html#unittest.removeHandler "Link to this definition")

When called without arguments this function removes the control-c handler if it has been installed. This function can also be used as a test decorator to temporarily remove the handler while the test is being executed:
Copy```
@unittest.removeHandler
def test_signal_handling(self):
    ...

```

### [Table of Contents](https://docs.python.org/3/contents.html)
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


#### Previous topic
[`doctest` — Test interactive Python examples](https://docs.python.org/3/library/doctest.html "previous chapter")
#### Next topic
[`unittest.mock` — mock object library](https://docs.python.org/3/library/unittest.mock.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=unittest+%E2%80%94+Unit+testing+framework&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Funittest.html&pagesource=library%2Funittest.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/unittest.mock.html "unittest.mock — mock object library") |
  * [previous](https://docs.python.org/3/library/doctest.html "doctest — Test interactive Python examples") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Development Tools](https://docs.python.org/3/library/development.html) »
  * [`unittest` — Unit testing framework](https://docs.python.org/3/library/unittest.html)
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
  *[/]: Positional-only parameter separator (PEP 570)
  *[LIFO]: last-in, first-out
