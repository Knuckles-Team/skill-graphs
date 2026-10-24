## Organizing test code[¶](https://docs.python.org/3/library/unittest.html#organizing-test-code "Link to this heading")
The basic building blocks of unit testing are _test cases_ — single scenarios that must be set up and checked for correctness. In `unittest`, test cases are represented by [`unittest.TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") instances. To make your own test cases you must write subclasses of [`TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") or use [`FunctionTestCase`](https://docs.python.org/3/library/unittest.html#unittest.FunctionTestCase "unittest.FunctionTestCase").
The testing code of a [`TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") instance should be entirely self contained, such that it can be run either in isolation or in arbitrary combination with any number of other test cases.
The simplest [`TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") subclass will simply implement a test method (i.e. a method whose name starts with `test`) in order to perform specific testing code:
Copy```
import unittest

class DefaultWidgetSizeTestCase(unittest.TestCase):
    def test_default_widget_size(self):
        widget = Widget('The widget')
        self.assertEqual(widget.size(), (50, 50))

```

Note that in order to test something, we use one of the [assert* methods](https://docs.python.org/3/library/unittest.html#assert-methods) provided by the [`TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") base class. If the test fails, an exception will be raised with an explanatory message, and `unittest` will identify the test case as a _failure_. Any other exceptions will be treated as _errors_.
Tests can be numerous, and their set-up can be repetitive. Luckily, we can factor out set-up code by implementing a method called [`setUp()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUp "unittest.TestCase.setUp"), which the testing framework will automatically call for every single test we run:
Copy```
import unittest

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), (50,50),
                         'incorrect default size')

    def test_widget_resize(self):
        self.widget.resize(100,150)
        self.assertEqual(self.widget.size(), (100,150),
                         'wrong size after resize')

```

Note
The order in which the various tests will be run is determined by sorting the test method names with respect to the built-in ordering for strings.
If the [`setUp()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUp "unittest.TestCase.setUp") method raises an exception while the test is running, the framework will consider the test to have suffered an error, and the test method will not be executed.
Similarly, we can provide a [`tearDown()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.tearDown "unittest.TestCase.tearDown") method that tidies up after the test method has been run:
Copy```
import unittest

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def tearDown(self):
        self.widget.dispose()

```

If [`setUp()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUp "unittest.TestCase.setUp") succeeded, [`tearDown()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.tearDown "unittest.TestCase.tearDown") will be run whether the test method succeeded or not.
Such a working environment for the testing code is called a _test fixture_. A new TestCase instance is created as a unique test fixture used to execute each individual test method. Thus [`setUp()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUp "unittest.TestCase.setUp"), [`tearDown()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.tearDown "unittest.TestCase.tearDown"), and `TestCase.__init__()` will be called once per test.
It is recommended that you use TestCase implementations to group tests together according to the features they test. `unittest` provides a mechanism for this: the _test suite_ , represented by `unittest`’s [`TestSuite`](https://docs.python.org/3/library/unittest.html#unittest.TestSuite "unittest.TestSuite") class. In most cases, calling [`unittest.main()`](https://docs.python.org/3/library/unittest.html#unittest.main "unittest.main") will do the right thing and collect all the module’s test cases for you and execute them.
However, should you want to customize the building of your test suite, you can do it yourself:
Copy```
def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase('test_default_widget_size'))
    suite.addTest(WidgetTestCase('test_widget_resize'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())

```

You can place the definitions of test cases and test suites in the same modules as the code they are to test (such as `widget.py`), but there are several advantages to placing the test code in a separate module, such as `test_widget.py`:
  * The test module can be run standalone from the command line.
  * The test code can more easily be separated from shipped code.
  * There is less temptation to change test code to fit the code it tests without a good reason.
  * Test code should be modified much less frequently than the code it tests.
  * Tested code can be refactored more easily.
  * Tests for modules written in C must be in separate modules anyway, so why not be consistent?
  * If the testing strategy changes, there is no need to change the source code.
