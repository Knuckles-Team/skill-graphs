## Test Discovery[¶](https://docs.python.org/3/library/unittest.html#test-discovery "Link to this heading")
Added in version 3.2.
Unittest supports simple test discovery. In order to be compatible with test discovery, all of the test files must be [modules](https://docs.python.org/3/tutorial/modules.html#tut-modules) or [packages](https://docs.python.org/3/tutorial/modules.html#tut-packages) importable from the top-level directory of the project (this means that their filenames must be valid [identifiers](https://docs.python.org/3/reference/lexical_analysis.html#identifiers)).
Test discovery is implemented in [`TestLoader.discover()`](https://docs.python.org/3/library/unittest.html#unittest.TestLoader.discover "unittest.TestLoader.discover"), but can also be used from the command line. The basic command-line usage is:
Copy```
cd project_directory
python -m unittest discover

```

Note
As a shortcut, `python -m unittest` is the equivalent of `python -m unittest discover`. If you want to pass arguments to test discovery the `discover` sub-command must be used explicitly.
The `discover` sub-command has the following options:

-v, --verbose[¶](https://docs.python.org/3/library/unittest.html#cmdoption-unittest-discover-v "Link to this definition")

Verbose output

-s, --start-directory directory[¶](https://docs.python.org/3/library/unittest.html#cmdoption-unittest-discover-s "Link to this definition")

Directory to start discovery (`.` default)

-p, --pattern pattern[¶](https://docs.python.org/3/library/unittest.html#cmdoption-unittest-discover-p "Link to this definition")

Pattern to match test files (`test*.py` default)

-t, --top-level-directory directory[¶](https://docs.python.org/3/library/unittest.html#cmdoption-unittest-discover-t "Link to this definition")

Top level directory of project (defaults to start directory)
The [`-s`](https://docs.python.org/3/library/unittest.html#cmdoption-unittest-discover-s), [`-p`](https://docs.python.org/3/library/unittest.html#cmdoption-unittest-discover-p), and [`-t`](https://docs.python.org/3/library/unittest.html#cmdoption-unittest-discover-t) options can be passed in as positional arguments in that order. The following two command lines are equivalent:
Copy```
python -m unittest discover -s project_directory -p "*_test.py"
python -m unittest discover project_directory "*_test.py"

```

As well as being a path it is possible to pass a package name, for example `myproject.subpackage.test`, as the start directory. The package name you supply will then be imported and its location on the filesystem will be used as the start directory.
Caution
Test discovery loads tests by importing them. Once test discovery has found all the test files from the start directory you specify it turns the paths into package names to import. For example `foo/bar/baz.py` will be imported as `foo.bar.baz`.
If you have a package installed globally and attempt test discovery on a different copy of the package then the import _could_ happen from the wrong place. If this happens test discovery will warn you and exit.
If you supply the start directory as a package name rather than a path to a directory then discover assumes that whichever location it imports from is the location you intended, so you will not get the warning.
Test modules and packages can customize test loading and discovery by through the [load_tests protocol](https://docs.python.org/3/library/unittest.html#id1).
Changed in version 3.4: Test discovery supports [namespace packages](https://docs.python.org/3/glossary.html#term-namespace-package).
Changed in version 3.11: Test discovery dropped the [namespace packages](https://docs.python.org/3/glossary.html#term-namespace-package) support. It has been broken since Python 3.7. Start directory and its subdirectories containing tests must be regular package that have `__init__.py` file.
If the start directory is the dotted name of the package, the ancestor packages can be namespace packages.
Changed in version 3.14: Test discovery supports [namespace package](https://docs.python.org/3/glossary.html#term-namespace-package) as start directory again. To avoid scanning directories unrelated to Python, tests are not searched in subdirectories that do not contain `__init__.py`.
