[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`zipimport` — Import modules from Zip archives](https://docs.python.org/3/library/zipimport.html)
    * [zipimporter Objects](https://docs.python.org/3/library/zipimport.html#zipimporter-objects)
    * [Examples](https://docs.python.org/3/library/zipimport.html#examples)


#### Previous topic
[Importing Modules](https://docs.python.org/3/library/modules.html "previous chapter")
#### Next topic
[`pkgutil` — Package extension utility](https://docs.python.org/3/library/pkgutil.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=zipimport+%E2%80%94+Import+modules+from+Zip+archives&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fzipimport.html&pagesource=library%2Fzipimport.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/pkgutil.html "pkgutil — Package extension utility") |
  * [previous](https://docs.python.org/3/library/modules.html "Importing Modules") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Importing Modules](https://docs.python.org/3/library/modules.html) »
  * [`zipimport` — Import modules from Zip archives](https://docs.python.org/3/library/zipimport.html)
  * |
  * Theme  Auto Light Dark |


#  `zipimport` — Import modules from Zip archives[¶](https://docs.python.org/3/library/zipimport.html#module-zipimport "Link to this heading")
**Source code:**
* * *
This module adds the ability to import Python modules (`*.py`, `*.pyc`) and packages from ZIP-format archives. It is usually not needed to use the `zipimport` module explicitly; it is automatically used by the built-in [`import`](https://docs.python.org/3/reference/simple_stmts.html#import) mechanism for [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path") items that are paths to ZIP archives.
Typically, [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path") is a list of directory names as strings. This module also allows an item of `sys.path` to be a string naming a ZIP file archive. The ZIP archive can contain a subdirectory structure to support package imports, and a path within the archive can be specified to only import from a subdirectory. For example, the path `example.zip/lib/` would only import from the `lib/` subdirectory within the archive.
Any files may be present in the ZIP archive, but importers are only invoked for `.py` and `.pyc` files. ZIP import of dynamic modules (`.pyd`, `.so`) is disallowed. Note that if an archive only contains `.py` files, Python will not attempt to modify the archive by adding the corresponding `.pyc` file, meaning that if a ZIP archive doesn’t contain `.pyc` files, importing may be rather slow.
Changed in version 3.13: ZIP64 is supported
Changed in version 3.8: Previously, ZIP archives with an archive comment were not supported.
See also
Documentation on the ZIP file format by Phil Katz, the creator of the format and algorithms used.

[**PEP 273**](https://peps.python.org/pep-0273/) - Import Modules from Zip Archives

Written by James C. Ahlstrom, who also provided an implementation. Python 2.3 follows the specification in [**PEP 273**](https://peps.python.org/pep-0273/), but uses an implementation written by Just van Rossum that uses the import hooks described in [**PEP 302**](https://peps.python.org/pep-0302/).

[`importlib`](https://docs.python.org/3/library/importlib.html#module-importlib "importlib: The implementation of the import machinery.") - The implementation of the import machinery

Package providing the relevant protocols for all importers to implement.
This module defines an exception:

_exception_ zipimport.ZipImportError[¶](https://docs.python.org/3/library/zipimport.html#zipimport.ZipImportError "Link to this definition")

Exception raised by zipimporter objects. It’s a subclass of [`ImportError`](https://docs.python.org/3/library/exceptions.html#ImportError "ImportError"), so it can be caught as `ImportError`, too.
## zipimporter Objects[¶](https://docs.python.org/3/library/zipimport.html#zipimporter-objects "Link to this heading")
[`zipimporter`](https://docs.python.org/3/library/zipimport.html#zipimport.zipimporter "zipimport.zipimporter") is the class for importing ZIP files.

_class_ zipimport.zipimporter(_archivepath_)[¶](https://docs.python.org/3/library/zipimport.html#zipimport.zipimporter "Link to this definition")

Create a new zipimporter instance. _archivepath_ must be a path to a ZIP file, or to a specific path within a ZIP file. For example, an _archivepath_ of `foo/bar.zip/lib` will look for modules in the `lib` directory inside the ZIP file `foo/bar.zip` (provided that it exists).
[`ZipImportError`](https://docs.python.org/3/library/zipimport.html#zipimport.ZipImportError "zipimport.ZipImportError") is raised if _archivepath_ doesn’t point to a valid ZIP archive.
Changed in version 3.12: Methods `find_loader()` and `find_module()`, deprecated in 3.10 are now removed. Use [`find_spec()`](https://docs.python.org/3/library/zipimport.html#zipimport.zipimporter.find_spec "zipimport.zipimporter.find_spec") instead.

create_module(_spec_)[¶](https://docs.python.org/3/library/zipimport.html#zipimport.zipimporter.create_module "Link to this definition")

Implementation of [`importlib.abc.Loader.create_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.create_module "importlib.abc.Loader.create_module") that returns [`None`](https://docs.python.org/3/library/constants.html#None "None") to explicitly request the default semantics.
Added in version 3.10.

exec_module(_module_)[¶](https://docs.python.org/3/library/zipimport.html#zipimport.zipimporter.exec_module "Link to this definition")

Implementation of [`importlib.abc.Loader.exec_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.exec_module "importlib.abc.Loader.exec_module").
Added in version 3.10.

find_spec(_fullname_ , _target =None_)[¶](https://docs.python.org/3/library/zipimport.html#zipimport.zipimporter.find_spec "Link to this definition")

An implementation of [`importlib.abc.PathEntryFinder.find_spec()`](https://docs.python.org/3/library/importlib.html#importlib.abc.PathEntryFinder.find_spec "importlib.abc.PathEntryFinder.find_spec").
Added in version 3.10.

get_code(_fullname_)[¶](https://docs.python.org/3/library/zipimport.html#zipimport.zipimporter.get_code "Link to this definition")

Return the code object for the specified module. Raise [`ZipImportError`](https://docs.python.org/3/library/zipimport.html#zipimport.ZipImportError "zipimport.ZipImportError") if the module couldn’t be imported.

get_data(_pathname_)[¶](https://docs.python.org/3/library/zipimport.html#zipimport.zipimporter.get_data "Link to this definition")

Return the data associated with _pathname_. Raise [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") if the file wasn’t found.
Changed in version 3.3: [`IOError`](https://docs.python.org/3/library/exceptions.html#IOError "IOError") used to be raised, it is now an alias of [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError").

get_filename(_fullname_)[¶](https://docs.python.org/3/library/zipimport.html#zipimport.zipimporter.get_filename "Link to this definition")

Return the value `__file__` would be set to if the specified module was imported. Raise [`ZipImportError`](https://docs.python.org/3/library/zipimport.html#zipimport.ZipImportError "zipimport.ZipImportError") if the module couldn’t be imported.
Added in version 3.1.

get_source(_fullname_)[¶](https://docs.python.org/3/library/zipimport.html#zipimport.zipimporter.get_source "Link to this definition")

Return the source code for the specified module. Raise [`ZipImportError`](https://docs.python.org/3/library/zipimport.html#zipimport.ZipImportError "zipimport.ZipImportError") if the module couldn’t be found, return [`None`](https://docs.python.org/3/library/constants.html#None "None") if the archive does contain the module, but has no source for it.

is_package(_fullname_)[¶](https://docs.python.org/3/library/zipimport.html#zipimport.zipimporter.is_package "Link to this definition")

Return `True` if the module specified by _fullname_ is a package. Raise [`ZipImportError`](https://docs.python.org/3/library/zipimport.html#zipimport.ZipImportError "zipimport.ZipImportError") if the module couldn’t be found.

load_module(_fullname_)[¶](https://docs.python.org/3/library/zipimport.html#zipimport.zipimporter.load_module "Link to this definition")

Load the module specified by _fullname_. _fullname_ must be the fully qualified (dotted) module name. Returns the imported module on success, raises [`ZipImportError`](https://docs.python.org/3/library/zipimport.html#zipimport.ZipImportError "zipimport.ZipImportError") on failure.
Deprecated since version 3.10, will be removed in version 3.15: Use [`exec_module()`](https://docs.python.org/3/library/zipimport.html#zipimport.zipimporter.exec_module "zipimport.zipimporter.exec_module") instead.

invalidate_caches()[¶](https://docs.python.org/3/library/zipimport.html#zipimport.zipimporter.invalidate_caches "Link to this definition")

Clear out the internal cache of information about files found within the ZIP archive.
Added in version 3.10.

archive[¶](https://docs.python.org/3/library/zipimport.html#zipimport.zipimporter.archive "Link to this definition")

The file name of the importer’s associated ZIP file, without a possible subpath.

prefix[¶](https://docs.python.org/3/library/zipimport.html#zipimport.zipimporter.prefix "Link to this definition")

The subpath within the ZIP file where modules are searched. This is the empty string for zipimporter objects which point to the root of the ZIP file.
The [`archive`](https://docs.python.org/3/library/zipimport.html#zipimport.zipimporter.archive "zipimport.zipimporter.archive") and [`prefix`](https://docs.python.org/3/library/zipimport.html#zipimport.zipimporter.prefix "zipimport.zipimporter.prefix") attributes, when combined with a slash, equal the original _archivepath_ argument given to the `zipimporter` constructor.
## Examples[¶](https://docs.python.org/3/library/zipimport.html#examples "Link to this heading")
Here is an example that imports a module from a ZIP archive - note that the `zipimport` module is not explicitly used.
Copy```
$ unzip -l example_archive.zip
Archive:  example_archive.zip
  Length     Date   Time    Name
 --------    ----   ----    ----
     8467  01-01-00 12:30   example.py
 --------                   -------
     8467                   1 file

```

Copy```
>>> import sys
>>> # Add the archive to the front of the module search path
>>> sys.path.insert(0, 'example_archive.zip')
>>> import example
>>> example.__file__
'example_archive.zip/example.py'

```

### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`zipimport` — Import modules from Zip archives](https://docs.python.org/3/library/zipimport.html)
    * [zipimporter Objects](https://docs.python.org/3/library/zipimport.html#zipimporter-objects)
    * [Examples](https://docs.python.org/3/library/zipimport.html#examples)


#### Previous topic
[Importing Modules](https://docs.python.org/3/library/modules.html "previous chapter")
#### Next topic
[`pkgutil` — Package extension utility](https://docs.python.org/3/library/pkgutil.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=zipimport+%E2%80%94+Import+modules+from+Zip+archives&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fzipimport.html&pagesource=library%2Fzipimport.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/pkgutil.html "pkgutil — Package extension utility") |
  * [previous](https://docs.python.org/3/library/modules.html "Importing Modules") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Importing Modules](https://docs.python.org/3/library/modules.html) »
  * [`zipimport` — Import modules from Zip archives](https://docs.python.org/3/library/zipimport.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
