[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`__main__` — Top-level code environment](https://docs.python.org/3/library/__main__.html)
    * [`__name__ == '__main__'`](https://docs.python.org/3/library/__main__.html#name-main)
      * [What is the “top-level code environment”?](https://docs.python.org/3/library/__main__.html#what-is-the-top-level-code-environment)
      * [Idiomatic Usage](https://docs.python.org/3/library/__main__.html#idiomatic-usage)
      * [Packaging Considerations](https://docs.python.org/3/library/__main__.html#packaging-considerations)
    * [`__main__.py` in Python Packages](https://docs.python.org/3/library/__main__.html#main-py-in-python-packages)
      * [Idiomatic Usage](https://docs.python.org/3/library/__main__.html#id1)
    * [`import __main__`](https://docs.python.org/3/library/__main__.html#import-main)


#### Previous topic
[`builtins` — Built-in objects](https://docs.python.org/3/library/builtins.html "previous chapter")
#### Next topic
[`warnings` — Warning control](https://docs.python.org/3/library/warnings.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=__main__+%E2%80%94+Top-level+code+environment&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2F__main__.html&pagesource=library%2F__main__.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/warnings.html "warnings — Warning control") |
  * [previous](https://docs.python.org/3/library/builtins.html "builtins — Built-in objects") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Python Runtime Services](https://docs.python.org/3/library/python.html) »
  * [`__main__` — Top-level code environment](https://docs.python.org/3/library/__main__.html)
  * |
  * Theme  Auto Light Dark |


#  `__main__` — Top-level code environment[¶](https://docs.python.org/3/library/__main__.html#module-__main__ "Link to this heading")
* * *
In Python, the special name `__main__` is used for two important constructs:
  1. the name of the top-level environment of the program, which can be checked using the `__name__ == '__main__'` expression; and
  2. the `__main__.py` file in Python packages.


Both of these mechanisms are related to Python modules; how users interact with them and how they interact with each other. They are explained in detail below. If you’re new to Python modules, see the tutorial section [Modules](https://docs.python.org/3/tutorial/modules.html#tut-modules) for an introduction.
##  `__name__ == '__main__'`[¶](https://docs.python.org/3/library/__main__.html#name-main "Link to this heading")
When a Python module or package is imported, `__name__` is set to the module’s name. Usually, this is the name of the Python file itself without the `.py` extension:
Copy```
>>> import configparser
>>> configparser.__name__
'configparser'

```

If the file is part of a package, `__name__` will also include the parent package’s path:
Copy```
>>> from concurrent.futures import process
>>> process.__name__
'concurrent.futures.process'

```

However, if the module is executed in the top-level code environment, its `__name__` is set to the string `'__main__'`.
### What is the “top-level code environment”?[¶](https://docs.python.org/3/library/__main__.html#what-is-the-top-level-code-environment "Link to this heading")
`__main__` is the name of the environment where top-level code is run. “Top-level code” is the first user-specified Python module that starts running. It’s “top-level” because it imports all other modules that the program needs. Sometimes “top-level code” is called an _entry point_ to the application.
The top-level code environment can be:
  * the scope of an interactive prompt:
Copy```
>>> __name__
'__main__'

```

  * the Python module passed to the Python interpreter as a file argument:
Copy```
$ python helloworld.py
Hello, world!

```

  * the Python module or package passed to the Python interpreter with the [`-m`](https://docs.python.org/3/using/cmdline.html#cmdoption-m) argument:
Copy```
$ python -m tarfile
usage: tarfile.py [-h] [-v] (...)

```

  * Python code read by the Python interpreter from standard input:
Copy```
$ echo "import this" | python
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
...

```

  * Python code passed to the Python interpreter with the [`-c`](https://docs.python.org/3/using/cmdline.html#cmdoption-c) argument:
Copy```
$ python -c "import this"
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
...

```



In each of these situations, the top-level module’s `__name__` is set to `'__main__'`.
As a result, a module can discover whether or not it is running in the top-level environment by checking its own `__name__`, which allows a common idiom for conditionally executing code when the module is not initialized from an import statement:
Copy```
if __name__ == '__main__':
    # Execute when the module is not initialized from an import statement.
    ...

```

See also
For a more detailed look at how `__name__` is set in all situations, see the tutorial section [Modules](https://docs.python.org/3/tutorial/modules.html#tut-modules).
### Idiomatic Usage[¶](https://docs.python.org/3/library/__main__.html#idiomatic-usage "Link to this heading")
Some modules contain code that is intended for script use only, like parsing command-line arguments or fetching data from standard input. If a module like this was imported from a different module, for example to unit test it, the script code would unintentionally execute as well.
This is where using the `if __name__ == '__main__'` code block comes in handy. Code within this block won’t run unless the module is executed in the top-level environment.
Putting as few statements as possible in the block below `if __name__ == '__main__'` can improve code clarity and correctness. Most often, a function named `main` encapsulates the program’s primary behavior:
Copy```
# echo.py

import shlex
import sys

def echo(phrase: str) -> None:
   """A dummy wrapper around print."""
   # for demonstration purposes, you can imagine that there is some
   # valuable and reusable logic inside this function
   print(phrase)

def main() -> int:
    """Echo the input arguments to standard output"""
    phrase = shlex.join(sys.argv)
    echo(phrase)
    return 0

if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit

```

Note that if the module didn’t encapsulate code inside the `main` function but instead put it directly within the `if __name__ == '__main__'` block, the `phrase` variable would be global to the entire module. This is error-prone as other functions within the module could be unintentionally using the global variable instead of a local name. A `main` function solves this problem.
Using a `main` function has the added benefit of the `echo` function itself being isolated and importable elsewhere. When `echo.py` is imported, the `echo` and `main` functions will be defined, but neither of them will be called, because `__name__ != '__main__'`.
### Packaging Considerations[¶](https://docs.python.org/3/library/__main__.html#packaging-considerations "Link to this heading")
`main` functions are often used to create command-line tools by specifying them as entry points for console scripts. When this is done, `main` is passed into [`sys.exit()`](https://docs.python.org/3/library/sys.html#sys.exit "sys.exit"). For example:
Copy```
sys.exit(main())

```

Since the call to `main` is wrapped in [`sys.exit()`](https://docs.python.org/3/library/sys.html#sys.exit "sys.exit"), the expectation is that your function will return some value acceptable as an input to `sys.exit()`; typically, an integer or `None` (which is implicitly returned if your function does not have a return statement).
By proactively following this convention ourselves, our module will have the same behavior when run directly (i.e. `python echo.py`) as it will have if we later package it as a console script entry-point in a pip-installable package.
In particular, be careful about returning strings from your `main` function. [`sys.exit()`](https://docs.python.org/3/library/sys.html#sys.exit "sys.exit") will interpret a string argument as a failure message, so your program will have an exit code of `1`, indicating failure, and the string will be written to [`sys.stderr`](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr"). The `echo.py` example from earlier exemplifies using the `sys.exit(main())` convention.
See also
[Python Packaging User Guide](https://packaging.python.org/) contains a collection of tutorials and references on how to distribute and install Python packages with modern tools.
##  `__main__.py` in Python Packages[¶](https://docs.python.org/3/library/__main__.html#main-py-in-python-packages "Link to this heading")
If you are not familiar with Python packages, see section [Packages](https://docs.python.org/3/tutorial/modules.html#tut-packages) of the tutorial. Most commonly, the `__main__.py` file is used to provide a command-line interface for a package. Consider the following hypothetical package, “bandclass”:
```
bandclass
  ├── __init__.py
  ├── __main__.py
  └── student.py

```

`__main__.py` will be executed when the package itself is invoked directly from the command line using the [`-m`](https://docs.python.org/3/using/cmdline.html#cmdoption-m) flag. For example:
Copy```
$ python -m bandclass

```

This command will cause `__main__.py` to run. How you utilize this mechanism will depend on the nature of the package you are writing, but in this hypothetical case, it might make sense to allow the teacher to search for students:
Copy```
# bandclass/__main__.py

import sys
from .student import search_students

student_name = sys.argv[1] if len(sys.argv) >= 2 else ''
print(f'Found student: {search_students(student_name)}')

```

Note that `from .student import search_students` is an example of a relative import. This import style can be used when referencing modules within a package. For more details, see [Intra-package References](https://docs.python.org/3/tutorial/modules.html#intra-package-references) in the [Modules](https://docs.python.org/3/tutorial/modules.html#tut-modules) section of the tutorial.
### Idiomatic Usage[¶](https://docs.python.org/3/library/__main__.html#id1 "Link to this heading")
The content of `__main__.py` typically isn’t fenced with an `if __name__ == '__main__'` block. Instead, those files are kept short and import functions to execute from other modules. Those other modules can then be easily unit-tested and are properly reusable.
If used, an `if __name__ == '__main__'` block will still work as expected for a `__main__.py` file within a package, because its `__name__` attribute will include the package’s path if imported:
Copy```
>>> import asyncio.__main__
>>> asyncio.__main__.__name__
'asyncio.__main__'

```

This won’t work for `__main__.py` files in the root directory of a `.zip` file though. Hence, for consistency, a minimal `__main__.py` without a `__name__` check is preferred.
See also
See [`venv`](https://docs.python.org/3/library/venv.html#module-venv "venv: Creation of virtual environments.") for an example of a package with a minimal `__main__.py` in the standard library. It doesn’t contain a `if __name__ == '__main__'` block. You can invoke it with `python -m venv [directory]`.
See [`runpy`](https://docs.python.org/3/library/runpy.html#module-runpy "runpy: Locate and run Python modules without importing them first.") for more details on the [`-m`](https://docs.python.org/3/using/cmdline.html#cmdoption-m) flag to the interpreter executable.
See [`zipapp`](https://docs.python.org/3/library/zipapp.html#module-zipapp "zipapp: Manage executable Python zip archives") for how to run applications packaged as _.zip_ files. In this case Python looks for a `__main__.py` file in the root directory of the archive.
##  `import __main__`[¶](https://docs.python.org/3/library/__main__.html#import-main "Link to this heading")
Regardless of which module a Python program was started with, other modules running within that same program can import the top-level environment’s scope ([namespace](https://docs.python.org/3/glossary.html#term-namespace)) by importing the `__main__` module. This doesn’t import a `__main__.py` file but rather whichever module that received the special name `'__main__'`.
Here is an example module that consumes the `__main__` namespace:
Copy```
# namely.py

import __main__

def did_user_define_their_name():
    return 'my_name' in dir(__main__)

def print_user_name():
    if not did_user_define_their_name():
        raise ValueError('Define the variable `my_name`!')

    print(__main__.my_name)

```

Example usage of this module could be as follows:
Copy```
# start.py

import sys

from namely import print_user_name

# my_name = "Dinsdale"

def main():
    try:
        print_user_name()
    except ValueError as ve:
        return str(ve)

if __name__ == "__main__":
    sys.exit(main())

```

Now, if we started our program, the result would look like this:
Copy```
$ python start.py
Define the variable `my_name`!

```

The exit code of the program would be 1, indicating an error. Uncommenting the line with `my_name = "Dinsdale"` fixes the program and now it exits with status code 0, indicating success:
Copy```
$ python start.py
Dinsdale

```

Note that importing `__main__` doesn’t cause any issues with unintentionally running top-level code meant for script use which is put in the `if __name__ == "__main__"` block of the `start` module. Why does this work?
Python inserts an empty `__main__` module in [`sys.modules`](https://docs.python.org/3/library/sys.html#sys.modules "sys.modules") at interpreter startup, and populates it by running top-level code. In our example this is the `start` module which runs line by line and imports `namely`. In turn, `namely` imports `__main__` (which is really `start`). That’s an import cycle! Fortunately, since the partially populated `__main__` module is present in `sys.modules`, Python passes that to `namely`. See [Special considerations for __main__](https://docs.python.org/3/reference/import.html#import-dunder-main) in the import system’s reference for details on how this works.
The Python REPL is another example of a “top-level environment”, so anything defined in the REPL becomes part of the `__main__` scope:
Copy```
>>> import namely
>>> namely.did_user_define_their_name()
False
>>> namely.print_user_name()
Traceback (most recent call last):
...
ValueError: Define the variable `my_name`!
>>> my_name = 'Jabberwocky'
>>> namely.did_user_define_their_name()
True
>>> namely.print_user_name()
Jabberwocky

```

The `__main__` scope is used in the implementation of [`pdb`](https://docs.python.org/3/library/pdb.html#module-pdb "pdb: The Python debugger for interactive interpreters.") and [`rlcompleter`](https://docs.python.org/3/library/rlcompleter.html#module-rlcompleter "rlcompleter: Python identifier completion, suitable for the GNU readline library.").
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`__main__` — Top-level code environment](https://docs.python.org/3/library/__main__.html)
    * [`__name__ == '__main__'`](https://docs.python.org/3/library/__main__.html#name-main)
      * [What is the “top-level code environment”?](https://docs.python.org/3/library/__main__.html#what-is-the-top-level-code-environment)
      * [Idiomatic Usage](https://docs.python.org/3/library/__main__.html#idiomatic-usage)
      * [Packaging Considerations](https://docs.python.org/3/library/__main__.html#packaging-considerations)
    * [`__main__.py` in Python Packages](https://docs.python.org/3/library/__main__.html#main-py-in-python-packages)
      * [Idiomatic Usage](https://docs.python.org/3/library/__main__.html#id1)
    * [`import __main__`](https://docs.python.org/3/library/__main__.html#import-main)


#### Previous topic
[`builtins` — Built-in objects](https://docs.python.org/3/library/builtins.html "previous chapter")
#### Next topic
[`warnings` — Warning control](https://docs.python.org/3/library/warnings.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=__main__+%E2%80%94+Top-level+code+environment&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2F__main__.html&pagesource=library%2F__main__.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/warnings.html "warnings — Warning control") |
  * [previous](https://docs.python.org/3/library/builtins.html "builtins — Built-in objects") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Python Runtime Services](https://docs.python.org/3/library/python.html) »
  * [`__main__` — Top-level code environment](https://docs.python.org/3/library/__main__.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
