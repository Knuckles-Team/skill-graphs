## Introduction[¶](https://docs.python.org/3/library/importlib.html#introduction "Link to this heading")
The purpose of the `importlib` package is three-fold.
One is to provide the implementation of the [`import`](https://docs.python.org/3/reference/simple_stmts.html#import) statement (and thus, by extension, the [`__import__()`](https://docs.python.org/3/library/functions.html#import__ "__import__") function) in Python source code. This provides an implementation of `import` which is portable to any Python interpreter. This also provides an implementation which is easier to comprehend than one implemented in a programming language other than Python.
Two, the components to implement [`import`](https://docs.python.org/3/reference/simple_stmts.html#import) are exposed in this package, making it easier for users to create their own custom objects (known generically as an [importer](https://docs.python.org/3/glossary.html#term-importer)) to participate in the import process.
Three, the package contains modules exposing additional functionality for managing aspects of Python packages:
  * [`importlib.metadata`](https://docs.python.org/3/library/importlib.metadata.html#module-importlib.metadata "importlib.metadata: Accessing package metadata") presents access to metadata from third-party distributions.
  * [`importlib.resources`](https://docs.python.org/3/library/importlib.resources.html#module-importlib.resources "importlib.resources: Package resource reading, opening, and access") provides routines for accessing non-code “resources” from Python packages.


See also

[The import statement](https://docs.python.org/3/reference/simple_stmts.html#import)

The language reference for the [`import`](https://docs.python.org/3/reference/simple_stmts.html#import) statement.

[Packages specification](https://www.python.org/doc/essays/packages/)

Original specification of packages. Some semantics have changed since the writing of this document (e.g. redirecting based on `None` in [`sys.modules`](https://docs.python.org/3/library/sys.html#sys.modules "sys.modules")).

The [`__import__()`](https://docs.python.org/3/library/importlib.html#importlib.__import__ "importlib.__import__") function

The [`import`](https://docs.python.org/3/reference/simple_stmts.html#import) statement is syntactic sugar for this function.

[The initialization of the sys.path module search path](https://docs.python.org/3/library/sys_path_init.html#sys-path-init)

The initialization of [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path").

[**PEP 235**](https://peps.python.org/pep-0235/)

Import on Case-Insensitive Platforms

[**PEP 263**](https://peps.python.org/pep-0263/)

Defining Python Source Code Encodings

[**PEP 302**](https://peps.python.org/pep-0302/)

New Import Hooks

[**PEP 328**](https://peps.python.org/pep-0328/)

Imports: Multi-Line and Absolute/Relative

[**PEP 366**](https://peps.python.org/pep-0366/)

Main module explicit relative imports

[**PEP 420**](https://peps.python.org/pep-0420/)

Implicit namespace packages

[**PEP 451**](https://peps.python.org/pep-0451/)

A ModuleSpec Type for the Import System

[**PEP 488**](https://peps.python.org/pep-0488/)

Elimination of PYO files

[**PEP 489**](https://peps.python.org/pep-0489/)

Multi-phase extension module initialization

[**PEP 552**](https://peps.python.org/pep-0552/)

Deterministic pycs

[**PEP 3120**](https://peps.python.org/pep-3120/)

Using UTF-8 as the Default Source Encoding

[**PEP 3147**](https://peps.python.org/pep-3147/)

PYC Repository Directories
