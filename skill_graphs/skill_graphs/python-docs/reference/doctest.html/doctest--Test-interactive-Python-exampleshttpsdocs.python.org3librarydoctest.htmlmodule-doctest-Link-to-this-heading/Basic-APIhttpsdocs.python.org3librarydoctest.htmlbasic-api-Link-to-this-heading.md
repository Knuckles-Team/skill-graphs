## Basic API[¶](https://docs.python.org/3/library/doctest.html#basic-api "Link to this heading")
The functions [`testmod()`](https://docs.python.org/3/library/doctest.html#doctest.testmod "doctest.testmod") and [`testfile()`](https://docs.python.org/3/library/doctest.html#doctest.testfile "doctest.testfile") provide a simple interface to doctest that should be sufficient for most basic uses. For a less formal introduction to these two functions, see sections [Simple Usage: Checking Examples in Docstrings](https://docs.python.org/3/library/doctest.html#doctest-simple-testmod) and [Simple Usage: Checking Examples in a Text File](https://docs.python.org/3/library/doctest.html#doctest-simple-testfile).

doctest.testfile(_filename_ , _module_relative =True_, _name =None_, _package =None_, _globs =None_, _verbose =None_, _report =True_, _optionflags =0_, _extraglobs =None_, _raise_on_error =False_, _parser =DocTestParser()_, _encoding =None_)[¶](https://docs.python.org/3/library/doctest.html#doctest.testfile "Link to this definition")

All arguments except _filename_ are optional, and should be specified in keyword form.
Test examples in the file named _filename_. Return `(failure_count, test_count)`.
Optional argument _module_relative_ specifies how the filename should be interpreted:
  * If _module_relative_ is `True` (the default), then _filename_ specifies an OS-independent module-relative path. By default, this path is relative to the calling module’s directory; but if the _package_ argument is specified, then it is relative to that package. To ensure OS-independence, _filename_ should use `/` characters to separate path segments, and may not be an absolute path (i.e., it may not begin with `/`).
  * If _module_relative_ is `False`, then _filename_ specifies an OS-specific path. The path may be absolute or relative; relative paths are resolved with respect to the current working directory.


Optional argument _name_ gives the name of the test; by default, or if `None`, `os.path.basename(filename)` is used.
Optional argument _package_ is a Python package or the name of a Python package whose directory should be used as the base directory for a module-relative filename. If no package is specified, then the calling module’s directory is used as the base directory for module-relative filenames. It is an error to specify _package_ if _module_relative_ is `False`.
Optional argument _globs_ gives a dict to be used as the globals when executing examples. A new shallow copy of this dict is created for the doctest, so its examples start with a clean slate. By default, or if `None`, a new empty dict is used.
Optional argument _extraglobs_ gives a dict merged into the globals used to execute examples. This works like [`dict.update()`](https://docs.python.org/3/library/stdtypes.html#dict.update "dict.update"): if _globs_ and _extraglobs_ have a common key, the associated value in _extraglobs_ appears in the combined dict. By default, or if `None`, no extra globals are used. This is an advanced feature that allows parameterization of doctests. For example, a doctest can be written for a base class, using a generic name for the class, then reused to test any number of subclasses by passing an _extraglobs_ dict mapping the generic name to the subclass to be tested.
Optional argument _verbose_ prints lots of stuff if true, and prints only failures if false; by default, or if `None`, it’s true if and only if `'-v'` is in [`sys.argv`](https://docs.python.org/3/library/sys.html#sys.argv "sys.argv").
Optional argument _report_ prints a summary at the end when true, else prints nothing at the end. In verbose mode, the summary is detailed, else the summary is very brief (in fact, empty if all tests passed).
Optional argument _optionflags_ (default value `0`) takes the [bitwise OR](https://docs.python.org/3/reference/expressions.html#bitwise) of option flags. See section [Option Flags](https://docs.python.org/3/library/doctest.html#doctest-options).
Optional argument _raise_on_error_ defaults to false. If true, an exception is raised upon the first failure or unexpected exception in an example. This allows failures to be post-mortem debugged. Default behavior is to continue running examples.
Optional argument _parser_ specifies a [`DocTestParser`](https://docs.python.org/3/library/doctest.html#doctest.DocTestParser "doctest.DocTestParser") (or subclass) that should be used to extract tests from the files. It defaults to a normal parser (i.e., `DocTestParser()`).
Optional argument _encoding_ specifies an encoding that should be used to convert the file to unicode.

doctest.testmod(_m =None_, _name =None_, _globs =None_, _verbose =None_, _report =True_, _optionflags =0_, _extraglobs =None_, _raise_on_error =False_, _exclude_empty =False_)[¶](https://docs.python.org/3/library/doctest.html#doctest.testmod "Link to this definition")

All arguments are optional, and all except for _m_ should be specified in keyword form.
Test examples in docstrings in functions and classes reachable from module _m_ (or module [`__main__`](https://docs.python.org/3/library/__main__.html#module-__main__ "__main__: The environment where top-level code is run. Covers command-line interfaces, import-time behavior, and ``__name__ == '__main__'``.") if _m_ is not supplied or is `None`), starting with `m.__doc__`.
Also test examples reachable from dict `m.__test__`, if it exists. `m.__test__` maps names (strings) to functions, classes and strings; function and class docstrings are searched for examples; strings are searched directly, as if they were docstrings.
Only docstrings attached to objects belonging to module _m_ are searched.
Return `(failure_count, test_count)`.
Optional argument _name_ gives the name of the module; by default, or if `None`, `m.__name__` is used.
Optional argument _exclude_empty_ defaults to false. If true, objects for which no doctests are found are excluded from consideration. The default is a backward compatibility hack, so that code still using [`doctest.master.summarize`](https://docs.python.org/3/library/doctest.html#doctest.DocTestRunner.summarize "doctest.DocTestRunner.summarize") in conjunction with `testmod()` continues to get output for objects with no tests. The _exclude_empty_ argument to the newer [`DocTestFinder`](https://docs.python.org/3/library/doctest.html#doctest.DocTestFinder "doctest.DocTestFinder") constructor defaults to true.
Optional arguments _extraglobs_ , _verbose_ , _report_ , _optionflags_ , _raise_on_error_ , and _globs_ are the same as for function [`testfile()`](https://docs.python.org/3/library/doctest.html#doctest.testfile "doctest.testfile") above, except that _globs_ defaults to `m.__dict__`.

doctest.run_docstring_examples(_f_ , _globs_ , _verbose =False_, _name ='NoName'_, _compileflags =None_, _optionflags =0_)[¶](https://docs.python.org/3/library/doctest.html#doctest.run_docstring_examples "Link to this definition")

Test examples associated with object _f_ ; for example, _f_ may be a string, a module, a function, or a class object.
A shallow copy of dictionary argument _globs_ is used for the execution context.
Optional argument _name_ is used in failure messages, and defaults to `"NoName"`.
If optional argument _verbose_ is true, output is generated even if there are no failures. By default, output is generated only in case of an example failure.
Optional argument _compileflags_ gives the set of flags that should be used by the Python compiler when running the examples. By default, or if `None`, flags are deduced corresponding to the set of future features found in _globs_.
Optional argument _optionflags_ works as for function [`testfile()`](https://docs.python.org/3/library/doctest.html#doctest.testfile "doctest.testfile") above.
