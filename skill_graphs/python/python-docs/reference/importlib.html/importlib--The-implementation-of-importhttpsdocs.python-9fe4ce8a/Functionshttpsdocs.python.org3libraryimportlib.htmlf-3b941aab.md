## Functions[¶](https://docs.python.org/3/library/importlib.html#functions "Link to this heading")

importlib.__import__(_name_ , _globals =None_, _locals =None_, _fromlist =()_, _level =0_)[¶](https://docs.python.org/3/library/importlib.html#importlib.__import__ "Link to this definition")

An implementation of the built-in `__import__()` function.
Note
Programmatic importing of modules should use [`import_module()`](https://docs.python.org/3/library/importlib.html#importlib.import_module "importlib.import_module") instead of this function.

importlib.import_module(_name_ , _package =None_)[¶](https://docs.python.org/3/library/importlib.html#importlib.import_module "Link to this definition")

Import a module. The _name_ argument specifies what module to import in absolute or relative terms (e.g. either `pkg.mod` or `..mod`). If the name is specified in relative terms, then the _package_ argument must be set to the name of the package which is to act as the anchor for resolving the package name (e.g. `import_module('..mod', 'pkg.subpkg')` will import `pkg.mod`).
The `import_module()` function acts as a simplifying wrapper around [`importlib.__import__()`](https://docs.python.org/3/library/importlib.html#importlib.__import__ "importlib.__import__"). This means all semantics of the function are derived from `importlib.__import__()`. The most important difference between these two functions is that `import_module()` returns the specified package or module (e.g. `pkg.mod`), while [`__import__()`](https://docs.python.org/3/library/functions.html#import__ "__import__") returns the top-level package or module (e.g. `pkg`).
If you are dynamically importing a module that was created since the interpreter began execution (e.g., created a Python source file), you may need to call [`invalidate_caches()`](https://docs.python.org/3/library/importlib.html#importlib.invalidate_caches "importlib.invalidate_caches") in order for the new module to be noticed by the import system.
Changed in version 3.3: Parent packages are automatically imported.

importlib.invalidate_caches()[¶](https://docs.python.org/3/library/importlib.html#importlib.invalidate_caches "Link to this definition")

Invalidate the internal caches of finders stored at [`sys.meta_path`](https://docs.python.org/3/library/sys.html#sys.meta_path "sys.meta_path"). If a finder implements `invalidate_caches()` then it will be called to perform the invalidation. This function should be called if any modules are created/installed while your program is running to guarantee all finders will notice the new module’s existence.
Added in version 3.3.
Changed in version 3.10: Namespace packages created/installed in a different [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path") location after the same namespace was already imported are noticed.

importlib.reload(_module_)[¶](https://docs.python.org/3/library/importlib.html#importlib.reload "Link to this definition")

Reload a previously imported _module_. The argument must be a module object, so it must have been successfully imported before. This is useful if you have edited the module source file using an external editor and want to try out the new version without leaving the Python interpreter. The return value is the module object (which can be different if re-importing causes a different object to be placed in [`sys.modules`](https://docs.python.org/3/library/sys.html#sys.modules "sys.modules")).
When `reload()` is executed:
  * Python module’s code is recompiled and the module-level code re-executed, defining a new set of objects which are bound to names in the module’s dictionary by reusing the [loader](https://docs.python.org/3/glossary.html#term-loader) which originally loaded the module. The `init` function of extension modules is not called a second time.
  * As with all other objects in Python the old objects are only reclaimed after their reference counts drop to zero.
  * The names in the module namespace are updated to point to any new or changed objects.
  * Other references to the old objects (such as names external to the module) are not rebound to refer to the new objects and must be updated in each namespace where they occur if that is desired.


There are a number of other caveats:
When a module is reloaded, its dictionary (containing the module’s global variables) is retained. Redefinitions of names will override the old definitions, so this is generally not a problem. If the new version of a module does not define a name that was defined by the old version, the old definition remains. This feature can be used to the module’s advantage if it maintains a global table or cache of objects — with a [`try`](https://docs.python.org/3/reference/compound_stmts.html#try) statement it can test for the table’s presence and skip its initialization if desired:
Copy```
try:
    cache
except NameError:
    cache = {}

```

It is generally not very useful to reload built-in or dynamically loaded modules. Reloading [`sys`](https://docs.python.org/3/library/sys.html#module-sys "sys: Access system-specific parameters and functions."), [`__main__`](https://docs.python.org/3/library/__main__.html#module-__main__ "__main__: The environment where top-level code is run. Covers command-line interfaces, import-time behavior, and ``__name__ == '__main__'``."), [`builtins`](https://docs.python.org/3/library/builtins.html#module-builtins "builtins: The module that provides the built-in namespace.") and other key modules is not recommended. In many cases extension modules are not designed to be initialized more than once, and may fail in arbitrary ways when reloaded.
If a module imports objects from another module using [`from`](https://docs.python.org/3/reference/simple_stmts.html#from) … [`import`](https://docs.python.org/3/reference/simple_stmts.html#import) …, calling `reload()` for the other module does not redefine the objects imported from it — one way around this is to re-execute the `from` statement, another is to use `import` and qualified names (_module.name_) instead.
If a module instantiates instances of a class, reloading the module that defines the class does not affect the method definitions of the instances — they continue to use the old class definition. The same is true for derived classes.
Added in version 3.4.
Changed in version 3.7: [`ModuleNotFoundError`](https://docs.python.org/3/library/exceptions.html#ModuleNotFoundError "ModuleNotFoundError") is raised when the module being reloaded lacks a [`ModuleSpec`](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec "importlib.machinery.ModuleSpec").
Warning
This function is not thread-safe. Calling it from multiple threads can result in unexpected behavior. It’s recommended to use the [`threading.Lock`](https://docs.python.org/3/library/threading.html#threading.Lock "threading.Lock") or other synchronization primitives for thread-safe module reloading.
##  `importlib.abc` – Abstract base classes related to import[¶](https://docs.python.org/3/library/importlib.html#module-importlib.abc "Link to this heading")
**Source code:**
* * *
The `importlib.abc` module contains all of the core abstract base classes used by [`import`](https://docs.python.org/3/reference/simple_stmts.html#import). Some subclasses of the core abstract base classes are also provided to help in implementing the core ABCs.
ABC hierarchy:
Copy```
object
 +-- MetaPathFinder
 +-- PathEntryFinder
 +-- Loader
      +-- ResourceLoader --------+
      +-- InspectLoader          |
           +-- ExecutionLoader --+
                                 +-- FileLoader
                                 +-- SourceLoader

```


_class_ importlib.abc.MetaPathFinder[¶](https://docs.python.org/3/library/importlib.html#importlib.abc.MetaPathFinder "Link to this definition")

An abstract base class representing a [meta path finder](https://docs.python.org/3/glossary.html#term-meta-path-finder).
Added in version 3.3.
Changed in version 3.10: No longer a subclass of `Finder`.

find_spec(_fullname_ , _path_ , _target =None_)[¶](https://docs.python.org/3/library/importlib.html#importlib.abc.MetaPathFinder.find_spec "Link to this definition")

An abstract method for finding a [spec](https://docs.python.org/3/glossary.html#term-module-spec) for the specified module. If this is a top-level import, _path_ will be `None`. Otherwise, this is a search for a subpackage or module and _path_ will be the value of [`__path__`](https://docs.python.org/3/reference/datamodel.html#module.__path__ "module.__path__") from the parent package. If a spec cannot be found, `None` is returned. When passed in, `target` is a module object that the finder may use to make a more educated guess about what spec to return. [`importlib.util.spec_from_loader()`](https://docs.python.org/3/library/importlib.html#importlib.util.spec_from_loader "importlib.util.spec_from_loader") may be useful for implementing concrete `MetaPathFinders`.
Added in version 3.4.

invalidate_caches()[¶](https://docs.python.org/3/library/importlib.html#importlib.abc.MetaPathFinder.invalidate_caches "Link to this definition")

An optional method which, when called, should invalidate any internal cache used by the finder. Used by [`importlib.invalidate_caches()`](https://docs.python.org/3/library/importlib.html#importlib.invalidate_caches "importlib.invalidate_caches") when invalidating the caches of all finders on [`sys.meta_path`](https://docs.python.org/3/library/sys.html#sys.meta_path "sys.meta_path").
Changed in version 3.4: Returns `None` when called instead of [`NotImplemented`](https://docs.python.org/3/library/constants.html#NotImplemented "NotImplemented").

_class_ importlib.abc.PathEntryFinder[¶](https://docs.python.org/3/library/importlib.html#importlib.abc.PathEntryFinder "Link to this definition")

An abstract base class representing a [path entry finder](https://docs.python.org/3/glossary.html#term-path-entry-finder). Though it bears some similarities to [`MetaPathFinder`](https://docs.python.org/3/library/importlib.html#importlib.abc.MetaPathFinder "importlib.abc.MetaPathFinder"), `PathEntryFinder` is meant for use only within the path-based import subsystem provided by [`importlib.machinery.PathFinder`](https://docs.python.org/3/library/importlib.html#importlib.machinery.PathFinder "importlib.machinery.PathFinder").
Added in version 3.3.
Changed in version 3.10: No longer a subclass of `Finder`.

find_spec(_fullname_ , _target =None_)[¶](https://docs.python.org/3/library/importlib.html#importlib.abc.PathEntryFinder.find_spec "Link to this definition")

An abstract method for finding a [spec](https://docs.python.org/3/glossary.html#term-module-spec) for the specified module. The finder will search for the module only within the [path entry](https://docs.python.org/3/glossary.html#term-path-entry) to which it is assigned. If a spec cannot be found, `None` is returned. When passed in, `target` is a module object that the finder may use to make a more educated guess about what spec to return. [`importlib.util.spec_from_loader()`](https://docs.python.org/3/library/importlib.html#importlib.util.spec_from_loader "importlib.util.spec_from_loader") may be useful for implementing concrete `PathEntryFinders`.
Added in version 3.4.

invalidate_caches()[¶](https://docs.python.org/3/library/importlib.html#importlib.abc.PathEntryFinder.invalidate_caches "Link to this definition")

An optional method which, when called, should invalidate any internal cache used by the finder. Used by [`importlib.machinery.PathFinder.invalidate_caches()`](https://docs.python.org/3/library/importlib.html#importlib.machinery.PathFinder.invalidate_caches "importlib.machinery.PathFinder.invalidate_caches") when invalidating the caches of all cached finders.

_class_ importlib.abc.Loader[¶](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader "Link to this definition")

An abstract base class for a [loader](https://docs.python.org/3/glossary.html#term-loader). See [**PEP 302**](https://peps.python.org/pep-0302/) for the exact definition for a loader.
Loaders that wish to support resource reading should implement a `get_resource_reader()` method as specified by [`importlib.resources.abc.ResourceReader`](https://docs.python.org/3/library/importlib.resources.abc.html#importlib.resources.abc.ResourceReader "importlib.resources.abc.ResourceReader").
Changed in version 3.7: Introduced the optional `get_resource_reader()` method.

create_module(_spec_)[¶](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.create_module "Link to this definition")

A method that returns the module object to use when importing a module. This method may return `None`, indicating that default module creation semantics should take place.
Added in version 3.4.
Changed in version 3.6: This method is no longer optional when [`exec_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.exec_module "importlib.abc.Loader.exec_module") is defined.

exec_module(_module_)[¶](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.exec_module "Link to this definition")

An abstract method that executes the module in its own namespace when a module is imported or reloaded. The module should already be initialized when `exec_module()` is called. When this method exists, [`create_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.create_module "importlib.abc.Loader.create_module") must be defined.
Added in version 3.4.
Changed in version 3.6: [`create_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.create_module "importlib.abc.Loader.create_module") must also be defined.

load_module(_fullname_)[¶](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.load_module "Link to this definition")

A legacy method for loading a module. If the module cannot be loaded, [`ImportError`](https://docs.python.org/3/library/exceptions.html#ImportError "ImportError") is raised, otherwise the loaded module is returned.
If the requested module already exists in [`sys.modules`](https://docs.python.org/3/library/sys.html#sys.modules "sys.modules"), that module should be used and reloaded. Otherwise the loader should create a new module and insert it into `sys.modules` before any loading begins, to prevent recursion from the import. If the loader inserted a module and the load fails, it must be removed by the loader from `sys.modules`; modules already in `sys.modules` before the loader began execution should be left alone.
The loader should set several attributes on the module (note that some of these attributes can change when a module is reloaded):
  * [`module.__name__`](https://docs.python.org/3/reference/datamodel.html#module.__name__ "module.__name__")
  * [`module.__file__`](https://docs.python.org/3/reference/datamodel.html#module.__file__ "module.__file__")
  * [`module.__cached__`](https://docs.python.org/3/reference/datamodel.html#module.__cached__ "module.__cached__") _(deprecated)_
  * [`module.__path__`](https://docs.python.org/3/reference/datamodel.html#module.__path__ "module.__path__")
  * [`module.__package__`](https://docs.python.org/3/reference/datamodel.html#module.__package__ "module.__package__") _(deprecated)_
  * [`module.__loader__`](https://docs.python.org/3/reference/datamodel.html#module.__loader__ "module.__loader__") _(deprecated)_


When [`exec_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.exec_module "importlib.abc.Loader.exec_module") is available then backwards-compatible functionality is provided.
Changed in version 3.4: Raise [`ImportError`](https://docs.python.org/3/library/exceptions.html#ImportError "ImportError") when called instead of [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError"). Functionality provided when [`exec_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.exec_module "importlib.abc.Loader.exec_module") is available.
Deprecated since version 3.4, will be removed in version 3.15: The recommended API for loading a module is [`exec_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.exec_module "importlib.abc.Loader.exec_module") (and [`create_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.create_module "importlib.abc.Loader.create_module")). Loaders should implement it instead of `load_module()`. The import machinery takes care of all the other responsibilities of `load_module()` when `exec_module()` is implemented.

_class_ importlib.abc.ResourceLoader[¶](https://docs.python.org/3/library/importlib.html#importlib.abc.ResourceLoader "Link to this definition")

_Superseded by TraversableResources_
> An abstract base class for a [loader](https://docs.python.org/3/glossary.html#term-loader) which implements the optional [**PEP 302**](https://peps.python.org/pep-0302/) protocol for loading arbitrary resources from the storage back-end.
> Deprecated since version 3.7: This ABC is deprecated in favour of supporting resource loading through [`importlib.resources.abc.TraversableResources`](https://docs.python.org/3/library/importlib.resources.abc.html#importlib.resources.abc.TraversableResources "importlib.resources.abc.TraversableResources"). This class exists for backwards compatibility only with other ABCs in this module.

_abstractmethod_ get_data(_path_)[¶](https://docs.python.org/3/library/importlib.html#importlib.abc.ResourceLoader.get_data "Link to this definition")

>> An abstract method to return the bytes for the data located at _path_. Loaders that have a file-like storage back-end that allows storing arbitrary data can implement this abstract method to give direct access to the data stored. [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") is to be raised if the _path_ cannot be found. The _path_ is expected to be constructed using a module’s [`__file__`](https://docs.python.org/3/reference/datamodel.html#module.__file__ "module.__file__") attribute or an item from a package’s [`__path__`](https://docs.python.org/3/reference/datamodel.html#module.__path__ "module.__path__").
>> Changed in version 3.4: Raises [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") instead of [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError").

_class_ importlib.abc.InspectLoader[¶](https://docs.python.org/3/library/importlib.html#importlib.abc.InspectLoader "Link to this definition")

An abstract base class for a [loader](https://docs.python.org/3/glossary.html#term-loader) which implements the optional [**PEP 302**](https://peps.python.org/pep-0302/) protocol for loaders that inspect modules.

get_code(_fullname_)[¶](https://docs.python.org/3/library/importlib.html#importlib.abc.InspectLoader.get_code "Link to this definition")

Return the code object for a module, or `None` if the module does not have a code object (as would be the case, for example, for a built-in module). Raise an [`ImportError`](https://docs.python.org/3/library/exceptions.html#ImportError "ImportError") if loader cannot find the requested module.
Note
While the method has a default implementation, it is suggested that it be overridden if possible for performance.
Changed in version 3.4: No longer abstract and a concrete implementation is provided.

_abstractmethod_ get_source(_fullname_)[¶](https://docs.python.org/3/library/importlib.html#importlib.abc.InspectLoader.get_source "Link to this definition")

> An abstract method to return the source of a module. It is returned as a text string using [universal newlines](https://docs.python.org/3/glossary.html#term-universal-newlines), translating all recognized line separators into `'\n'` characters. Returns `None` if no source is available (e.g. a built-in module). Raises [`ImportError`](https://docs.python.org/3/library/exceptions.html#ImportError "ImportError") if the loader cannot find the module specified.
> Changed in version 3.4: Raises [`ImportError`](https://docs.python.org/3/library/exceptions.html#ImportError "ImportError") instead of [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError").

is_package(_fullname_)[¶](https://docs.python.org/3/library/importlib.html#importlib.abc.InspectLoader.is_package "Link to this definition")

An optional method to return a true value if the module is a package, a false value otherwise. [`ImportError`](https://docs.python.org/3/library/exceptions.html#ImportError "ImportError") is raised if the [loader](https://docs.python.org/3/glossary.html#term-loader) cannot find the module.
Changed in version 3.4: Raises [`ImportError`](https://docs.python.org/3/library/exceptions.html#ImportError "ImportError") instead of [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError").

_static_ source_to_code(_data_ , _path ='<string>'_)[¶](https://docs.python.org/3/library/importlib.html#importlib.abc.InspectLoader.source_to_code "Link to this definition")

Create a code object from Python source.
The _data_ argument can be whatever the [`compile()`](https://docs.python.org/3/library/functions.html#compile "compile") function supports (i.e. string or bytes). The _path_ argument should be the “path” to where the source code originated from, which can be an abstract concept (e.g. location in a zip file).
With the subsequent code object one can execute it in a module by running `exec(code, module.__dict__)`.
Added in version 3.4.
Changed in version 3.5: Made the method static.

exec_module(_module_)[¶](https://docs.python.org/3/library/importlib.html#importlib.abc.InspectLoader.exec_module "Link to this definition")

Implementation of [`Loader.exec_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.exec_module "importlib.abc.Loader.exec_module").
Added in version 3.4.

load_module(_fullname_)[¶](https://docs.python.org/3/library/importlib.html#importlib.abc.InspectLoader.load_module "Link to this definition")

Implementation of [`Loader.load_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.load_module "importlib.abc.Loader.load_module").
Deprecated since version 3.4, will be removed in version 3.15: use [`exec_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.InspectLoader.exec_module "importlib.abc.InspectLoader.exec_module") instead.

_class_ importlib.abc.ExecutionLoader[¶](https://docs.python.org/3/library/importlib.html#importlib.abc.ExecutionLoader "Link to this definition")

An abstract base class which inherits from [`InspectLoader`](https://docs.python.org/3/library/importlib.html#importlib.abc.InspectLoader "importlib.abc.InspectLoader") that, when implemented, helps a module to be executed as a script. The ABC represents an optional [**PEP 302**](https://peps.python.org/pep-0302/) protocol.

_abstractmethod_ get_filename(_fullname_)[¶](https://docs.python.org/3/library/importlib.html#importlib.abc.ExecutionLoader.get_filename "Link to this definition")

> An abstract method that is to return the value of [`__file__`](https://docs.python.org/3/reference/datamodel.html#module.__file__ "module.__file__") for the specified module. If no path is available, [`ImportError`](https://docs.python.org/3/library/exceptions.html#ImportError "ImportError") is raised.
> If source code is available, then the method should return the path to the source file, regardless of whether a bytecode was used to load the module.
> Changed in version 3.4: Raises [`ImportError`](https://docs.python.org/3/library/exceptions.html#ImportError "ImportError") instead of [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError").

_class_ importlib.abc.FileLoader(_fullname_ , _path_)[¶](https://docs.python.org/3/library/importlib.html#importlib.abc.FileLoader "Link to this definition")

An abstract base class which inherits from [`ResourceLoader`](https://docs.python.org/3/library/importlib.html#importlib.abc.ResourceLoader "importlib.abc.ResourceLoader") and [`ExecutionLoader`](https://docs.python.org/3/library/importlib.html#importlib.abc.ExecutionLoader "importlib.abc.ExecutionLoader"), providing concrete implementations of [`ResourceLoader.get_data()`](https://docs.python.org/3/library/importlib.html#importlib.abc.ResourceLoader.get_data "importlib.abc.ResourceLoader.get_data") and [`ExecutionLoader.get_filename()`](https://docs.python.org/3/library/importlib.html#importlib.abc.ExecutionLoader.get_filename "importlib.abc.ExecutionLoader.get_filename").
The _fullname_ argument is a fully resolved name of the module the loader is to handle. The _path_ argument is the path to the file for the module.
Added in version 3.3.

name[¶](https://docs.python.org/3/library/importlib.html#importlib.abc.FileLoader.name "Link to this definition")

The name of the module the loader can handle.

path[¶](https://docs.python.org/3/library/importlib.html#importlib.abc.FileLoader.path "Link to this definition")

Path to the file of the module.

load_module(_fullname_)[¶](https://docs.python.org/3/library/importlib.html#importlib.abc.FileLoader.load_module "Link to this definition")

Calls super’s `load_module()`.
Deprecated since version 3.4, will be removed in version 3.15: Use [`Loader.exec_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.exec_module "importlib.abc.Loader.exec_module") instead.

_abstractmethod_ get_filename(_fullname_)[¶](https://docs.python.org/3/library/importlib.html#importlib.abc.FileLoader.get_filename "Link to this definition")

Returns [`path`](https://docs.python.org/3/library/importlib.html#importlib.abc.FileLoader.path "importlib.abc.FileLoader.path").

_abstractmethod_ get_data(_path_)[¶](https://docs.python.org/3/library/importlib.html#importlib.abc.FileLoader.get_data "Link to this definition")

Reads _path_ as a binary file and returns the bytes from it.

_class_ importlib.abc.SourceLoader[¶](https://docs.python.org/3/library/importlib.html#importlib.abc.SourceLoader "Link to this definition")

An abstract base class for implementing source (and optionally bytecode) file loading. The class inherits from both [`ResourceLoader`](https://docs.python.org/3/library/importlib.html#importlib.abc.ResourceLoader "importlib.abc.ResourceLoader") and [`ExecutionLoader`](https://docs.python.org/3/library/importlib.html#importlib.abc.ExecutionLoader "importlib.abc.ExecutionLoader"), requiring the implementation of:
  * [`ResourceLoader.get_data()`](https://docs.python.org/3/library/importlib.html#importlib.abc.ResourceLoader.get_data "importlib.abc.ResourceLoader.get_data")
  *

[`ExecutionLoader.get_filename()`](https://docs.python.org/3/library/importlib.html#importlib.abc.ExecutionLoader.get_filename "importlib.abc.ExecutionLoader.get_filename")

Should only return the path to the source file; sourceless loading is not supported.


The abstract methods defined by this class are to add optional bytecode file support. Not implementing these optional methods (or causing them to raise [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError")) causes the loader to only work with source code. Implementing the methods allows the loader to work with source _and_ bytecode files; it does not allow for _sourceless_ loading where only bytecode is provided. Bytecode files are an optimization to speed up loading by removing the parsing step of Python’s compiler, and so no bytecode-specific API is exposed.

path_stats(_path_)[¶](https://docs.python.org/3/library/importlib.html#importlib.abc.SourceLoader.path_stats "Link to this definition")

Optional abstract method which returns a [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict") containing metadata about the specified path. Supported dictionary keys are:
  * `'mtime'` (mandatory): an integer or floating-point number representing the modification time of the source code;
  * `'size'` (optional): the size in bytes of the source code.


Any other keys in the dictionary are ignored, to allow for future extensions. If the path cannot be handled, [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") is raised.
Added in version 3.3.
Changed in version 3.4: Raise [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") instead of [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError").

path_mtime(_path_)[¶](https://docs.python.org/3/library/importlib.html#importlib.abc.SourceLoader.path_mtime "Link to this definition")

Optional abstract method which returns the modification time for the specified path.
Deprecated since version 3.3: This method is deprecated in favour of [`path_stats()`](https://docs.python.org/3/library/importlib.html#importlib.abc.SourceLoader.path_stats "importlib.abc.SourceLoader.path_stats"). You don’t have to implement it, but it is still available for compatibility purposes. Raise [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") if the path cannot be handled.
Changed in version 3.4: Raise [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") instead of [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError").

set_data(_path_ , _data_)[¶](https://docs.python.org/3/library/importlib.html#importlib.abc.SourceLoader.set_data "Link to this definition")

Optional abstract method which writes the specified bytes to a file path. Any intermediate directories which do not exist are to be created automatically.
When writing to the path fails because the path is read-only ([`errno.EACCES`](https://docs.python.org/3/library/errno.html#errno.EACCES "errno.EACCES")/[`PermissionError`](https://docs.python.org/3/library/exceptions.html#PermissionError "PermissionError")), do not propagate the exception.
Changed in version 3.4: No longer raises [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError") when called.

get_code(_fullname_)[¶](https://docs.python.org/3/library/importlib.html#importlib.abc.SourceLoader.get_code "Link to this definition")

Concrete implementation of [`InspectLoader.get_code()`](https://docs.python.org/3/library/importlib.html#importlib.abc.InspectLoader.get_code "importlib.abc.InspectLoader.get_code").

exec_module(_module_)[¶](https://docs.python.org/3/library/importlib.html#importlib.abc.SourceLoader.exec_module "Link to this definition")

Concrete implementation of [`Loader.exec_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.exec_module "importlib.abc.Loader.exec_module").
Added in version 3.4.

load_module(_fullname_)[¶](https://docs.python.org/3/library/importlib.html#importlib.abc.SourceLoader.load_module "Link to this definition")

Concrete implementation of [`Loader.load_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.load_module "importlib.abc.Loader.load_module").
Deprecated since version 3.4, will be removed in version 3.15: Use [`exec_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.SourceLoader.exec_module "importlib.abc.SourceLoader.exec_module") instead.

get_source(_fullname_)[¶](https://docs.python.org/3/library/importlib.html#importlib.abc.SourceLoader.get_source "Link to this definition")

Concrete implementation of [`InspectLoader.get_source()`](https://docs.python.org/3/library/importlib.html#importlib.abc.InspectLoader.get_source "importlib.abc.InspectLoader.get_source").

is_package(_fullname_)[¶](https://docs.python.org/3/library/importlib.html#importlib.abc.SourceLoader.is_package "Link to this definition")

Concrete implementation of [`InspectLoader.is_package()`](https://docs.python.org/3/library/importlib.html#importlib.abc.InspectLoader.is_package "importlib.abc.InspectLoader.is_package"). A module is determined to be a package if its file path (as provided by [`ExecutionLoader.get_filename()`](https://docs.python.org/3/library/importlib.html#importlib.abc.ExecutionLoader.get_filename "importlib.abc.ExecutionLoader.get_filename")) is a file named `__init__` when the file extension is removed **and** the module name itself does not end in `__init__`.
