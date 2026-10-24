## Simple Usage: Checking Examples in a Text File[¶](https://docs.python.org/3/library/doctest.html#simple-usage-checking-examples-in-a-text-file "Link to this heading")
Another simple application of doctest is testing interactive examples in a text file. This can be done with the [`testfile()`](https://docs.python.org/3/library/doctest.html#doctest.testfile "doctest.testfile") function:
Copy```
import doctest
doctest.testfile("example.txt")

```

That short script executes and verifies any interactive Python examples contained in the file `example.txt`. The file content is treated as if it were a single giant docstring; the file doesn’t need to contain a Python program! For example, perhaps `example.txt` contains this:
```
The ``example`` module
======================

Using ``factorial``
-------------------

This is an example text file in reStructuredText format.  First import
``factorial`` from the ``example`` module:

    >>> from example import factorial

Now use it:

    >>> factorial(6)
    120

```

Running `doctest.testfile("example.txt")` then finds the error in this documentation:
Copy```
File "./example.txt", line 14, in example.txt
Failed example:
    factorial(6)
Expected:
    120
Got:
    720

```

As with [`testmod()`](https://docs.python.org/3/library/doctest.html#doctest.testmod "doctest.testmod"), [`testfile()`](https://docs.python.org/3/library/doctest.html#doctest.testfile "doctest.testfile") won’t display anything unless an example fails. If an example does fail, then the failing example(s) and the cause(s) of the failure(s) are printed to stdout, using the same format as `testmod()`.
By default, [`testfile()`](https://docs.python.org/3/library/doctest.html#doctest.testfile "doctest.testfile") looks for files in the calling module’s directory. See section [Basic API](https://docs.python.org/3/library/doctest.html#doctest-basic-api) for a description of the optional arguments that can be used to tell it to look for files in other locations.
Like [`testmod()`](https://docs.python.org/3/library/doctest.html#doctest.testmod "doctest.testmod"), [`testfile()`](https://docs.python.org/3/library/doctest.html#doctest.testfile "doctest.testfile")’s verbosity can be set with the `-v` command-line switch or with the optional keyword argument _verbose_.
There is also a command line shortcut for running [`testfile()`](https://docs.python.org/3/library/doctest.html#doctest.testfile "doctest.testfile"), see section [Command-line Usage](https://docs.python.org/3/library/doctest.html#doctest-cli).
For more information on [`testfile()`](https://docs.python.org/3/library/doctest.html#doctest.testfile "doctest.testfile"), see section [Basic API](https://docs.python.org/3/library/doctest.html#doctest-basic-api).
