#  `unittest` — Unit testing framework[¶](https://docs.python.org/3/library/unittest.html#module-unittest "Link to this heading")
**Source code:**
* * *
(If you are already familiar with the basic concepts of testing, you might want to skip to [the list of assert methods](https://docs.python.org/3/library/unittest.html#assert-methods).)
The `unittest` unit testing framework was originally inspired by JUnit and has a similar flavor as major unit testing frameworks in other languages. It supports test automation, sharing of setup and shutdown code for tests, aggregation of tests into collections, and independence of the tests from the reporting framework.
To achieve this, `unittest` supports some important concepts in an object-oriented way:

test fixture

A _test fixture_ represents the preparation needed to perform one or more tests, and any associated cleanup actions. This may involve, for example, creating temporary or proxy databases, directories, or starting a server process.

test case

A _test case_ is the individual unit of testing. It checks for a specific response to a particular set of inputs. `unittest` provides a base class, [`TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase"), which may be used to create new test cases.

test suite

A _test suite_ is a collection of test cases, test suites, or both. It is used to aggregate tests that should be executed together.

test runner

A _test runner_ is a component which orchestrates the execution of tests and provides the outcome to the user. The runner may use a graphical interface, a textual interface, or return a special value to indicate the results of executing the tests.
See also

Module [`doctest`](https://docs.python.org/3/library/doctest.html#module-doctest "doctest: Test pieces of code within docstrings.")

Another test-support module with a very different flavor.
Kent Beck’s original paper on testing frameworks using the pattern shared by `unittest`.
Third-party unittest framework with a lighter-weight syntax for writing tests. For example, `assert func(10) == 42`.

[The Python Testing Tools Taxonomy](https://wiki.python.org/moin/PythonTestingToolsTaxonomy)

An extensive list of Python testing tools including functional testing frameworks and mock object libraries.
A special-interest-group for discussion of testing, and testing tools, in Python.
The script `Tools/unittestgui/unittestgui.py` in the Python source distribution is a GUI tool for test discovery and execution. This is intended largely for ease of use for those new to unit testing. For production environments it is recommended that tests be driven by a continuous integration system such as
