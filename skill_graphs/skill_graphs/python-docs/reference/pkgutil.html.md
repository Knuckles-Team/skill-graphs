[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`zipimport` — Import modules from Zip archives](https://docs.python.org/3/library/zipimport.html "previous chapter")
#### Next topic
[`modulefinder` — Find modules used by a script](https://docs.python.org/3/library/modulefinder.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=pkgutil+%E2%80%94+Package+extension+utility&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fpkgutil.html&pagesource=library%2Fpkgutil.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/modulefinder.html "modulefinder — Find modules used by a script") |
  * [previous](https://docs.python.org/3/library/zipimport.html "zipimport — Import modules from Zip archives") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Importing Modules](https://docs.python.org/3/library/modules.html) »
  * [`pkgutil` — Package extension utility](https://docs.python.org/3/library/pkgutil.html)
  * |
  * Theme  Auto Light Dark |


#  `pkgutil` — Package extension utility[¶](https://docs.python.org/3/library/pkgutil.html#module-pkgutil "Link to this heading")
**Source code:**
* * *
This module provides utilities for the import system, in particular package support.

_class_ pkgutil.ModuleInfo(_module_finder_ , _name_ , _ispkg_)[¶](https://docs.python.org/3/library/pkgutil.html#pkgutil.ModuleInfo "Link to this definition")

A namedtuple that holds a brief summary of a module’s info.
Added in version 3.6.

pkgutil.extend_path(_path_ , _name_)[¶](https://docs.python.org/3/library/pkgutil.html#pkgutil.extend_path "Link to this definition")

Extend the search path for the modules which comprise a package. Intended use is to place the following code in a package’s `__init__.py`:
Copy```
from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

```

For each directory on [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path") that has a subdirectory that matches the package name, add the subdirectory to the package’s [`__path__`](https://docs.python.org/3/reference/datamodel.html#module.__path__ "module.__path__"). This is useful if one wants to distribute different parts of a single logical package as multiple directories.
It also looks for `*.pkg` files beginning where `*` matches the _name_ argument. This feature is similar to `*.pth` files (see the [`site`](https://docs.python.org/3/library/site.html#module-site "site: Module responsible for site-specific configuration.") module for more information), except that it doesn’t special-case lines starting with `import`. A `*.pkg` file is trusted at face value: apart from skipping blank lines and ignoring comments, all entries found in a `*.pkg` file are added to the path, regardless of whether they exist on the filesystem (this is a feature).
If the input path is not a list (as is the case for frozen packages) it is returned unchanged. The input path is not modified; an extended copy is returned. Items are only appended to the copy at the end.
It is assumed that [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path") is a sequence. Items of `sys.path` that are not strings referring to existing directories are ignored. Unicode items on `sys.path` that cause errors when used as filenames may cause this function to raise an exception (in line with [`os.path.isdir()`](https://docs.python.org/3/library/os.path.html#os.path.isdir "os.path.isdir") behavior).

pkgutil.get_importer(_path_item_)[¶](https://docs.python.org/3/library/pkgutil.html#pkgutil.get_importer "Link to this definition")

Retrieve a [finder](https://docs.python.org/3/glossary.html#term-finder) for the given _path_item_.
The returned finder is cached in [`sys.path_importer_cache`](https://docs.python.org/3/library/sys.html#sys.path_importer_cache "sys.path_importer_cache") if it was newly created by a path hook.
The cache (or part of it) can be cleared manually if a rescan of [`sys.path_hooks`](https://docs.python.org/3/library/sys.html#sys.path_hooks "sys.path_hooks") is necessary.
Changed in version 3.3: Updated to be based directly on [`importlib`](https://docs.python.org/3/library/importlib.html#module-importlib "importlib: The implementation of the import machinery.") rather than relying on the package internal [**PEP 302**](https://peps.python.org/pep-0302/) import emulation.

pkgutil.iter_importers(_fullname =''_)[¶](https://docs.python.org/3/library/pkgutil.html#pkgutil.iter_importers "Link to this definition")

Yield [finder](https://docs.python.org/3/glossary.html#term-finder) objects for the given module name.
If _fullname_ contains a `'.'`, the finders will be for the package containing _fullname_ , otherwise they will be all registered top level finders (i.e. those on both [`sys.meta_path`](https://docs.python.org/3/library/sys.html#sys.meta_path "sys.meta_path") and [`sys.path_hooks`](https://docs.python.org/3/library/sys.html#sys.path_hooks "sys.path_hooks")).
If the named module is in a package, that package is imported as a side effect of invoking this function.
If no module name is specified, all top level finders are produced.
Changed in version 3.3: Updated to be based directly on [`importlib`](https://docs.python.org/3/library/importlib.html#module-importlib "importlib: The implementation of the import machinery.") rather than relying on the package internal [**PEP 302**](https://peps.python.org/pep-0302/) import emulation.

pkgutil.iter_modules(_path =None_, _prefix =''_)[¶](https://docs.python.org/3/library/pkgutil.html#pkgutil.iter_modules "Link to this definition")

Yields [`ModuleInfo`](https://docs.python.org/3/library/pkgutil.html#pkgutil.ModuleInfo "pkgutil.ModuleInfo") for all submodules on _path_ , or, if _path_ is `None`, all top-level modules on [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path").
_path_ should be either `None` or a list of paths to look for modules in.
_prefix_ is a string to output on the front of every module name on output.
Note
Only works for a [finder](https://docs.python.org/3/glossary.html#term-finder) which defines an `iter_modules()` method. This interface is non-standard, so the module also provides implementations for [`importlib.machinery.FileFinder`](https://docs.python.org/3/library/importlib.html#importlib.machinery.FileFinder "importlib.machinery.FileFinder") and [`zipimport.zipimporter`](https://docs.python.org/3/library/zipimport.html#zipimport.zipimporter "zipimport.zipimporter").
Changed in version 3.3: Updated to be based directly on [`importlib`](https://docs.python.org/3/library/importlib.html#module-importlib "importlib: The implementation of the import machinery.") rather than relying on the package internal [**PEP 302**](https://peps.python.org/pep-0302/) import emulation.

pkgutil.walk_packages(_path =None_, _prefix =''_, _onerror =None_)[¶](https://docs.python.org/3/library/pkgutil.html#pkgutil.walk_packages "Link to this definition")

Yields [`ModuleInfo`](https://docs.python.org/3/library/pkgutil.html#pkgutil.ModuleInfo "pkgutil.ModuleInfo") for all modules recursively on _path_ , or, if _path_ is `None`, all accessible modules.
_path_ should be either `None` or a list of paths to look for modules in.
_prefix_ is a string to output on the front of every module name on output.
Note that this function must import all _packages_ (_not_ all modules!) on the given _path_ , in order to access the `__path__` attribute to find submodules.
_onerror_ is a function which gets called with one argument (the name of the package which was being imported) if any exception occurs while trying to import a package. If no _onerror_ function is supplied, [`ImportError`](https://docs.python.org/3/library/exceptions.html#ImportError "ImportError")s are caught and ignored, while all other exceptions are propagated, terminating the search.
Examples:
Copy```
# list all modules python can access
walk_packages()

# list all submodules of ctypes
walk_packages(ctypes.__path__, ctypes.__name__ + '.')

```

Note
Only works for a [finder](https://docs.python.org/3/glossary.html#term-finder) which defines an `iter_modules()` method. This interface is non-standard, so the module also provides implementations for [`importlib.machinery.FileFinder`](https://docs.python.org/3/library/importlib.html#importlib.machinery.FileFinder "importlib.machinery.FileFinder") and [`zipimport.zipimporter`](https://docs.python.org/3/library/zipimport.html#zipimport.zipimporter "zipimport.zipimporter").
Changed in version 3.3: Updated to be based directly on [`importlib`](https://docs.python.org/3/library/importlib.html#module-importlib "importlib: The implementation of the import machinery.") rather than relying on the package internal [**PEP 302**](https://peps.python.org/pep-0302/) import emulation.

pkgutil.get_data(_package_ , _resource_)[¶](https://docs.python.org/3/library/pkgutil.html#pkgutil.get_data "Link to this definition")

Get a resource from a package.
This is a wrapper for the [loader](https://docs.python.org/3/glossary.html#term-loader) [`get_data`](https://docs.python.org/3/library/importlib.html#importlib.abc.ResourceLoader.get_data "importlib.abc.ResourceLoader.get_data") API. The _package_ argument should be the name of a package, in standard module format (`foo.bar`). The _resource_ argument should be in the form of a relative filename, using `/` as the path separator. The parent directory name `..` is not allowed, and nor is a rooted name (starting with a `/`).
The function returns a binary string that is the contents of the specified resource.
For packages located in the filesystem, which have already been imported, this is the rough equivalent of:
Copy```
d = os.path.dirname(sys.modules[package].__file__)
data = open(os.path.join(d, resource), 'rb').read()

```

If the package cannot be located or loaded, or it uses a [loader](https://docs.python.org/3/glossary.html#term-loader) which does not support [`get_data`](https://docs.python.org/3/library/importlib.html#importlib.abc.ResourceLoader.get_data "importlib.abc.ResourceLoader.get_data"), then `None` is returned. In particular, the loader for [namespace packages](https://docs.python.org/3/glossary.html#term-namespace-package) does not support `get_data`.

pkgutil.resolve_name(_name_)[¶](https://docs.python.org/3/library/pkgutil.html#pkgutil.resolve_name "Link to this definition")

Resolve a name to an object.
This functionality is used in numerous places in the standard library (see [bpo-12915](https://bugs.python.org/issue?@action=redirect&bpo=12915)) - and equivalent functionality is also in widely used third-party packages such as setuptools, Django and Pyramid.
It is expected that _name_ will be a string in one of the following formats, where W is shorthand for a valid Python identifier and dot stands for a literal period in these pseudo-regexes:
  * `W(.W)*`
  * `W(.W)*:(W(.W)*)?`


The first form is intended for backward compatibility only. It assumes that some part of the dotted name is a package, and the rest is an object somewhere within that package, possibly nested inside other objects. Because the place where the package stops and the object hierarchy starts can’t be inferred by inspection, repeated attempts to import must be done with this form.
In the second form, the caller makes the division point clear through the provision of a single colon: the dotted name to the left of the colon is a package to be imported, and the dotted name to the right is the object hierarchy within that package. Only one import is needed in this form. If it ends with the colon, then a module object is returned.
The function will return an object (which might be a module), or raise one of the following exceptions:
[`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") – if _name_ isn’t in a recognised format.
[`ImportError`](https://docs.python.org/3/library/exceptions.html#ImportError "ImportError") – if an import failed when it shouldn’t have.
[`AttributeError`](https://docs.python.org/3/library/exceptions.html#AttributeError "AttributeError") – If a failure occurred when traversing the object hierarchy within the imported package to get to the desired object.
Added in version 3.9.
#### Previous topic
[`zipimport` — Import modules from Zip archives](https://docs.python.org/3/library/zipimport.html "previous chapter")
#### Next topic
[`modulefinder` — Find modules used by a script](https://docs.python.org/3/library/modulefinder.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=pkgutil+%E2%80%94+Package+extension+utility&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fpkgutil.html&pagesource=library%2Fpkgutil.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/modulefinder.html "modulefinder — Find modules used by a script") |
  * [previous](https://docs.python.org/3/library/zipimport.html "zipimport — Import modules from Zip archives") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Importing Modules](https://docs.python.org/3/library/modules.html) »
  * [`pkgutil` — Package extension utility](https://docs.python.org/3/library/pkgutil.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
