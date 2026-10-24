##  `importlib.machinery` – Importers and path hooks[¶](https://docs.python.org/3/library/importlib.html#module-importlib.machinery "Link to this heading")
**Source code:**
* * *
This module contains the various objects that help [`import`](https://docs.python.org/3/reference/simple_stmts.html#import) find and load modules.

importlib.machinery.SOURCE_SUFFIXES[¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.SOURCE_SUFFIXES "Link to this definition")

A list of strings representing the recognized file suffixes for source modules.
Added in version 3.3.

importlib.machinery.DEBUG_BYTECODE_SUFFIXES[¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.DEBUG_BYTECODE_SUFFIXES "Link to this definition")

A list of strings representing the file suffixes for non-optimized bytecode modules.
Added in version 3.3.
Deprecated since version 3.5: Use [`BYTECODE_SUFFIXES`](https://docs.python.org/3/library/importlib.html#importlib.machinery.BYTECODE_SUFFIXES "importlib.machinery.BYTECODE_SUFFIXES") instead.

importlib.machinery.OPTIMIZED_BYTECODE_SUFFIXES[¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.OPTIMIZED_BYTECODE_SUFFIXES "Link to this definition")

A list of strings representing the file suffixes for optimized bytecode modules.
Added in version 3.3.
Deprecated since version 3.5: Use [`BYTECODE_SUFFIXES`](https://docs.python.org/3/library/importlib.html#importlib.machinery.BYTECODE_SUFFIXES "importlib.machinery.BYTECODE_SUFFIXES") instead.

importlib.machinery.BYTECODE_SUFFIXES[¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.BYTECODE_SUFFIXES "Link to this definition")

A list of strings representing the recognized file suffixes for bytecode modules (including the leading dot).
Added in version 3.3.
Changed in version 3.5: The value is no longer dependent on `__debug__`.

importlib.machinery.EXTENSION_SUFFIXES[¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.EXTENSION_SUFFIXES "Link to this definition")

A list of strings representing the recognized file suffixes for extension modules.
Added in version 3.3.

importlib.machinery.all_suffixes()[¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.all_suffixes "Link to this definition")

Returns a combined list of strings representing all file suffixes for modules recognized by the standard import machinery. This is a helper for code which simply needs to know if a filesystem path potentially refers to a module without needing any details on the kind of module (for example, [`inspect.getmodulename()`](https://docs.python.org/3/library/inspect.html#inspect.getmodulename "inspect.getmodulename")).
Added in version 3.3.

_class_ importlib.machinery.BuiltinImporter[¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.BuiltinImporter "Link to this definition")

An [importer](https://docs.python.org/3/glossary.html#term-importer) for built-in modules. All known built-in modules are listed in [`sys.builtin_module_names`](https://docs.python.org/3/library/sys.html#sys.builtin_module_names "sys.builtin_module_names"). This class implements the [`importlib.abc.MetaPathFinder`](https://docs.python.org/3/library/importlib.html#importlib.abc.MetaPathFinder "importlib.abc.MetaPathFinder") and [`importlib.abc.InspectLoader`](https://docs.python.org/3/library/importlib.html#importlib.abc.InspectLoader "importlib.abc.InspectLoader") ABCs.
Only class methods are defined by this class to alleviate the need for instantiation.
Changed in version 3.5: As part of [**PEP 489**](https://peps.python.org/pep-0489/), the builtin importer now implements `Loader.create_module()` and `Loader.exec_module()`

_class_ importlib.machinery.FrozenImporter[¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.FrozenImporter "Link to this definition")

An [importer](https://docs.python.org/3/glossary.html#term-importer) for frozen modules. This class implements the [`importlib.abc.MetaPathFinder`](https://docs.python.org/3/library/importlib.html#importlib.abc.MetaPathFinder "importlib.abc.MetaPathFinder") and [`importlib.abc.InspectLoader`](https://docs.python.org/3/library/importlib.html#importlib.abc.InspectLoader "importlib.abc.InspectLoader") ABCs.
Only class methods are defined by this class to alleviate the need for instantiation.
Changed in version 3.4: Gained `create_module()` and `exec_module()` methods.

_class_ importlib.machinery.WindowsRegistryFinder[¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.WindowsRegistryFinder "Link to this definition")

[Finder](https://docs.python.org/3/glossary.html#term-finder) for modules declared in the Windows registry. This class implements the [`importlib.abc.MetaPathFinder`](https://docs.python.org/3/library/importlib.html#importlib.abc.MetaPathFinder "importlib.abc.MetaPathFinder") ABC.
Only class methods are defined by this class to alleviate the need for instantiation.
Added in version 3.3.
Deprecated since version 3.6: Use [`site`](https://docs.python.org/3/library/site.html#module-site "site: Module responsible for site-specific configuration.") configuration instead. Future versions of Python may not enable this finder by default.

_class_ importlib.machinery.PathFinder[¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.PathFinder "Link to this definition")

A [Finder](https://docs.python.org/3/glossary.html#term-finder) for [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path") and package `__path__` attributes. This class implements the [`importlib.abc.MetaPathFinder`](https://docs.python.org/3/library/importlib.html#importlib.abc.MetaPathFinder "importlib.abc.MetaPathFinder") ABC.
Only class methods are defined by this class to alleviate the need for instantiation.

_classmethod_ find_spec(_fullname_ , _path =None_, _target =None_)[¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.PathFinder.find_spec "Link to this definition")

Class method that attempts to find a [spec](https://docs.python.org/3/glossary.html#term-module-spec) for the module specified by _fullname_ on [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path") or, if defined, on _path_. For each path entry that is searched, [`sys.path_importer_cache`](https://docs.python.org/3/library/sys.html#sys.path_importer_cache "sys.path_importer_cache") is checked. If a non-false object is found then it is used as the [path entry finder](https://docs.python.org/3/glossary.html#term-path-entry-finder) to look for the module being searched for. If no entry is found in `sys.path_importer_cache`, then [`sys.path_hooks`](https://docs.python.org/3/library/sys.html#sys.path_hooks "sys.path_hooks") is searched for a finder for the path entry and, if found, is stored in `sys.path_importer_cache` along with being queried about the module. If no finder is ever found then `None` is both stored in the cache and returned.
Added in version 3.4.
Changed in version 3.5: If the current working directory – represented by an empty string – is no longer valid then `None` is returned but no value is cached in [`sys.path_importer_cache`](https://docs.python.org/3/library/sys.html#sys.path_importer_cache "sys.path_importer_cache").

_classmethod_ invalidate_caches()[¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.PathFinder.invalidate_caches "Link to this definition")

Calls [`importlib.abc.PathEntryFinder.invalidate_caches()`](https://docs.python.org/3/library/importlib.html#importlib.abc.PathEntryFinder.invalidate_caches "importlib.abc.PathEntryFinder.invalidate_caches") on all finders stored in [`sys.path_importer_cache`](https://docs.python.org/3/library/sys.html#sys.path_importer_cache "sys.path_importer_cache") that define the method. Otherwise entries in `sys.path_importer_cache` set to `None` are deleted.
Changed in version 3.7: Entries of `None` in [`sys.path_importer_cache`](https://docs.python.org/3/library/sys.html#sys.path_importer_cache "sys.path_importer_cache") are deleted.
Changed in version 3.4: Calls objects in [`sys.path_hooks`](https://docs.python.org/3/library/sys.html#sys.path_hooks "sys.path_hooks") with the current working directory for `''` (i.e. the empty string).

_class_ importlib.machinery.FileFinder(_path_ , _* loader_details_)[¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.FileFinder "Link to this definition")

A concrete implementation of [`importlib.abc.PathEntryFinder`](https://docs.python.org/3/library/importlib.html#importlib.abc.PathEntryFinder "importlib.abc.PathEntryFinder") which caches results from the file system.
The _path_ argument is the directory for which the finder is in charge of searching.
The _loader_details_ argument is a variable number of 2-item tuples each containing a loader and a sequence of file suffixes the loader recognizes. The loaders are expected to be callables which accept two arguments of the module’s name and the path to the file found.
The finder will cache the directory contents as necessary, making stat calls for each module search to verify the cache is not outdated. Because cache staleness relies upon the granularity of the operating system’s state information of the file system, there is a potential race condition of searching for a module, creating a new file, and then searching for the module the new file represents. If the operations happen fast enough to fit within the granularity of stat calls, then the module search will fail. To prevent this from happening, when you create a module dynamically, make sure to call [`importlib.invalidate_caches()`](https://docs.python.org/3/library/importlib.html#importlib.invalidate_caches "importlib.invalidate_caches").
Added in version 3.3.

path[¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.FileFinder.path "Link to this definition")

The path the finder will search in.

find_spec(_fullname_ , _target =None_)[¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.FileFinder.find_spec "Link to this definition")

Attempt to find the spec to handle _fullname_ within [`path`](https://docs.python.org/3/library/importlib.html#importlib.machinery.FileFinder.path "importlib.machinery.FileFinder.path").
Added in version 3.4.

invalidate_caches()[¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.FileFinder.invalidate_caches "Link to this definition")

Clear out the internal cache.

_classmethod_ path_hook(_* loader_details_)[¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.FileFinder.path_hook "Link to this definition")

A class method which returns a closure for use on [`sys.path_hooks`](https://docs.python.org/3/library/sys.html#sys.path_hooks "sys.path_hooks"). An instance of `FileFinder` is returned by the closure using the path argument given to the closure directly and _loader_details_ indirectly.
If the argument to the closure is not an existing directory, [`ImportError`](https://docs.python.org/3/library/exceptions.html#ImportError "ImportError") is raised.

_class_ importlib.machinery.SourceFileLoader(_fullname_ , _path_)[¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.SourceFileLoader "Link to this definition")

A concrete implementation of [`importlib.abc.SourceLoader`](https://docs.python.org/3/library/importlib.html#importlib.abc.SourceLoader "importlib.abc.SourceLoader") by subclassing [`importlib.abc.FileLoader`](https://docs.python.org/3/library/importlib.html#importlib.abc.FileLoader "importlib.abc.FileLoader") and providing some concrete implementations of other methods.
Added in version 3.3.

name[¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.SourceFileLoader.name "Link to this definition")

The name of the module that this loader will handle.

path[¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.SourceFileLoader.path "Link to this definition")

The path to the source file.

is_package(_fullname_)[¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.SourceFileLoader.is_package "Link to this definition")

Return `True` if [`path`](https://docs.python.org/3/library/importlib.html#importlib.machinery.SourceFileLoader.path "importlib.machinery.SourceFileLoader.path") appears to be for a package.

path_stats(_path_)[¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.SourceFileLoader.path_stats "Link to this definition")

Concrete implementation of [`importlib.abc.SourceLoader.path_stats()`](https://docs.python.org/3/library/importlib.html#importlib.abc.SourceLoader.path_stats "importlib.abc.SourceLoader.path_stats").

set_data(_path_ , _data_)[¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.SourceFileLoader.set_data "Link to this definition")

Concrete implementation of [`importlib.abc.SourceLoader.set_data()`](https://docs.python.org/3/library/importlib.html#importlib.abc.SourceLoader.set_data "importlib.abc.SourceLoader.set_data").

load_module(_name =None_)[¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.SourceFileLoader.load_module "Link to this definition")

Concrete implementation of [`importlib.abc.Loader.load_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.load_module "importlib.abc.Loader.load_module") where specifying the name of the module to load is optional.
Deprecated since version 3.6, will be removed in version 3.15: Use [`importlib.abc.Loader.exec_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.exec_module "importlib.abc.Loader.exec_module") instead.

_class_ importlib.machinery.SourcelessFileLoader(_fullname_ , _path_)[¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.SourcelessFileLoader "Link to this definition")

A concrete implementation of [`importlib.abc.FileLoader`](https://docs.python.org/3/library/importlib.html#importlib.abc.FileLoader "importlib.abc.FileLoader") which can import bytecode files (i.e. no source code files exist).
Please note that direct use of bytecode files (and thus not source code files) inhibits your modules from being usable by all Python implementations or new versions of Python which change the bytecode format.
Added in version 3.3.

name[¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.SourcelessFileLoader.name "Link to this definition")

The name of the module the loader will handle.

path[¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.SourcelessFileLoader.path "Link to this definition")

The path to the bytecode file.

is_package(_fullname_)[¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.SourcelessFileLoader.is_package "Link to this definition")

Determines if the module is a package based on [`path`](https://docs.python.org/3/library/importlib.html#importlib.machinery.SourcelessFileLoader.path "importlib.machinery.SourcelessFileLoader.path").

get_code(_fullname_)[¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.SourcelessFileLoader.get_code "Link to this definition")

Returns the code object for [`name`](https://docs.python.org/3/library/importlib.html#importlib.machinery.SourcelessFileLoader.name "importlib.machinery.SourcelessFileLoader.name") created from [`path`](https://docs.python.org/3/library/importlib.html#importlib.machinery.SourcelessFileLoader.path "importlib.machinery.SourcelessFileLoader.path").

get_source(_fullname_)[¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.SourcelessFileLoader.get_source "Link to this definition")

Returns `None` as bytecode files have no source when this loader is used.

load_module(_name =None_)[¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.SourcelessFileLoader.load_module "Link to this definition")

Concrete implementation of [`importlib.abc.Loader.load_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.load_module "importlib.abc.Loader.load_module") where specifying the name of the module to load is optional.
Deprecated since version 3.6, will be removed in version 3.15: Use [`importlib.abc.Loader.exec_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.exec_module "importlib.abc.Loader.exec_module") instead.

_class_ importlib.machinery.ExtensionFileLoader(_fullname_ , _path_)[¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.ExtensionFileLoader "Link to this definition")

A concrete implementation of [`importlib.abc.ExecutionLoader`](https://docs.python.org/3/library/importlib.html#importlib.abc.ExecutionLoader "importlib.abc.ExecutionLoader") for extension modules.
The _fullname_ argument specifies the name of the module the loader is to support. The _path_ argument is the path to the extension module’s file.
Note that, by default, importing an extension module will fail in subinterpreters if it doesn’t implement multi-phase init (see [**PEP 489**](https://peps.python.org/pep-0489/)), even if it would otherwise import successfully.
Added in version 3.3.
Changed in version 3.12: Multi-phase init is now required for use in subinterpreters.

name[¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.ExtensionFileLoader.name "Link to this definition")

Name of the module the loader supports.

path[¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.ExtensionFileLoader.path "Link to this definition")

Path to the extension module.

create_module(_spec_)[¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.ExtensionFileLoader.create_module "Link to this definition")

Creates the module object from the given specification in accordance with [**PEP 489**](https://peps.python.org/pep-0489/).
Added in version 3.5.

exec_module(_module_)[¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.ExtensionFileLoader.exec_module "Link to this definition")

Initializes the given module object in accordance with [**PEP 489**](https://peps.python.org/pep-0489/).
Added in version 3.5.

is_package(_fullname_)[¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.ExtensionFileLoader.is_package "Link to this definition")

Returns `True` if the file path points to a package’s `__init__` module based on [`EXTENSION_SUFFIXES`](https://docs.python.org/3/library/importlib.html#importlib.machinery.EXTENSION_SUFFIXES "importlib.machinery.EXTENSION_SUFFIXES").

get_code(_fullname_)[¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.ExtensionFileLoader.get_code "Link to this definition")

Returns `None` as extension modules lack a code object.

get_source(_fullname_)[¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.ExtensionFileLoader.get_source "Link to this definition")

Returns `None` as extension modules do not have source code.

get_filename(_fullname_)[¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.ExtensionFileLoader.get_filename "Link to this definition")

Returns [`path`](https://docs.python.org/3/library/importlib.html#importlib.machinery.ExtensionFileLoader.path "importlib.machinery.ExtensionFileLoader.path").
Added in version 3.4.

_class_ importlib.machinery.NamespaceLoader(_name_ , _path_ , _path_finder_)[¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.NamespaceLoader "Link to this definition")

A concrete implementation of [`importlib.abc.InspectLoader`](https://docs.python.org/3/library/importlib.html#importlib.abc.InspectLoader "importlib.abc.InspectLoader") for namespace packages. This is an alias for a private class and is only made public for introspecting the `__loader__` attribute on namespace packages:
Copy```
>>> from importlib.machinery import NamespaceLoader
>>> import my_namespace
>>> isinstance(my_namespace.__loader__, NamespaceLoader)
True
>>> import importlib.abc
>>> isinstance(my_namespace.__loader__, importlib.abc.Loader)
True

```

Added in version 3.11.

_class_ importlib.machinery.ModuleSpec(_name_ , _loader_ , _*_ , _origin =None_, _loader_state =None_, _is_package =None_)[¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec "Link to this definition")

A specification for a module’s import-system-related state. This is typically exposed as the module’s [`__spec__`](https://docs.python.org/3/reference/datamodel.html#module.__spec__ "module.__spec__") attribute. Many of these attributes are also available directly on a module: for example, `module.__spec__.origin == module.__file__`. Note, however, that while the _values_ are usually equivalent, they can differ since there is no synchronization between the two objects. For example, it is possible to update the module’s [`__file__`](https://docs.python.org/3/reference/datamodel.html#module.__file__ "module.__file__") at runtime and this will not be automatically reflected in the module’s [`__spec__.origin`](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec.origin "importlib.machinery.ModuleSpec.origin"), and vice versa.
Added in version 3.4.

name[¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec.name "Link to this definition")

The module’s fully qualified name (see [`module.__name__`](https://docs.python.org/3/reference/datamodel.html#module.__name__ "module.__name__")). The [finder](https://docs.python.org/3/glossary.html#term-finder) should always set this attribute to a non-empty string.

loader[¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec.loader "Link to this definition")

The [loader](https://docs.python.org/3/glossary.html#term-loader) used to load the module (see [`module.__loader__`](https://docs.python.org/3/reference/datamodel.html#module.__loader__ "module.__loader__")). The [finder](https://docs.python.org/3/glossary.html#term-finder) should always set this attribute.

origin[¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec.origin "Link to this definition")

The location the [loader](https://docs.python.org/3/glossary.html#term-loader) should use to load the module (see [`module.__file__`](https://docs.python.org/3/reference/datamodel.html#module.__file__ "module.__file__")). For example, for modules loaded from a `.py` file this is the filename. The [finder](https://docs.python.org/3/glossary.html#term-finder) should always set this attribute to a meaningful value for the loader to use. In the uncommon case that there is not one (like for namespace packages), it should be set to `None`.

submodule_search_locations[¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec.submodule_search_locations "Link to this definition")

A (possibly empty) [sequence](https://docs.python.org/3/glossary.html#term-sequence) of strings enumerating the locations in which a package’s submodules will be found (see [`module.__path__`](https://docs.python.org/3/reference/datamodel.html#module.__path__ "module.__path__")). Most of the time there will only be a single directory in this list.
The [finder](https://docs.python.org/3/glossary.html#term-finder) should set this attribute to a sequence, even an empty one, to indicate to the import system that the module is a package. It should be set to `None` for non-package modules. It is set automatically later to a special object for namespace packages.

loader_state[¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec.loader_state "Link to this definition")

The [finder](https://docs.python.org/3/glossary.html#term-finder) may set this attribute to an object containing additional, module-specific data to use when loading the module. Otherwise it should be set to `None`.

cached[¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec.cached "Link to this definition")

The filename of a compiled version of the module’s code (see [`module.__cached__`](https://docs.python.org/3/reference/datamodel.html#module.__cached__ "module.__cached__")). The [finder](https://docs.python.org/3/glossary.html#term-finder) should always set this attribute but it may be `None` for modules that do not need compiled code stored.

parent[¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec.parent "Link to this definition")

(Read-only) The fully qualified name of the package the module is in (or the empty string for a top-level module). See [`module.__package__`](https://docs.python.org/3/reference/datamodel.html#module.__package__ "module.__package__"). If the module is a package then this is the same as [`name`](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec.name "importlib.machinery.ModuleSpec.name").

has_location[¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec.has_location "Link to this definition")

`True` if the spec’s [`origin`](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec.origin "importlib.machinery.ModuleSpec.origin") refers to a loadable location, `False` otherwise. This value impacts how `origin` is interpreted and how the module’s [`__file__`](https://docs.python.org/3/reference/datamodel.html#module.__file__ "module.__file__") is populated.

_class_ importlib.machinery.AppleFrameworkLoader(_name_ , _path_)[¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.AppleFrameworkLoader "Link to this definition")

A specialization of [`importlib.machinery.ExtensionFileLoader`](https://docs.python.org/3/library/importlib.html#importlib.machinery.ExtensionFileLoader "importlib.machinery.ExtensionFileLoader") that is able to load extension modules in Framework format.
For compatibility with the iOS App Store, _all_ binary modules in an iOS app must be dynamic libraries, contained in a framework with appropriate metadata, stored in the `Frameworks` folder of the packaged app. There can be only a single binary per framework, and there can be no executable binary material outside the Frameworks folder.
To accommodate this requirement, when running on iOS, extension module binaries are _not_ packaged as `.so` files on `sys.path`, but as individual standalone frameworks. To discover those frameworks, this loader is registered against the `.fwork` file extension, with a `.fwork` file acting as a placeholder in the original location of the binary on `sys.path`. The `.fwork` file contains the path of the actual binary in the `Frameworks` folder, relative to the app bundle. To allow for resolving a framework-packaged binary back to the original location, the framework is expected to contain a `.origin` file that contains the location of the `.fwork` file, relative to the app bundle.
For example, consider the case of an import `from foo.bar import _whiz`, where `_whiz` is implemented with the binary module `sources/foo/bar/_whiz.abi3.so`, with `sources` being the location registered on `sys.path`, relative to the application bundle. This module _must_ be distributed as `Frameworks/foo.bar._whiz.framework/foo.bar._whiz` (creating the framework name from the full import path of the module), with an `Info.plist` file in the `.framework` directory identifying the binary as a framework. The `foo.bar._whiz` module would be represented in the original location with a `sources/foo/bar/_whiz.abi3.fwork` marker file, containing the path `Frameworks/foo.bar._whiz/foo.bar._whiz`. The framework would also contain `Frameworks/foo.bar._whiz.framework/foo.bar._whiz.origin`, containing the path to the `.fwork` file.
When a module is loaded with this loader, the `__file__` for the module will report as the location of the `.fwork` file. This allows code to use the `__file__` of a module as an anchor for file system traversal. However, the spec origin will reference the location of the _actual_ binary in the `.framework` folder.
The Xcode project building the app is responsible for converting any `.so` files from wherever they exist in the `PYTHONPATH` into frameworks in the `Frameworks` folder (including stripping extensions from the module file, the addition of framework metadata, and signing the resulting framework), and creating the `.fwork` and `.origin` files. This will usually be done with a build step in the Xcode project; see the iOS documentation for details on how to construct this build step.
Added in version 3.13.
[Availability](https://docs.python.org/3/library/intro.html#availability): iOS.

name[¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.AppleFrameworkLoader.name "Link to this definition")

Name of the module the loader supports.

path[¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.AppleFrameworkLoader.path "Link to this definition")

Path to the `.fwork` file for the extension module.
##  `importlib.util` – Utility code for importers[¶](https://docs.python.org/3/library/importlib.html#module-importlib.util "Link to this heading")
**Source code:**
* * *
This module contains the various objects that help in the construction of an [importer](https://docs.python.org/3/glossary.html#term-importer).

importlib.util.MAGIC_NUMBER[¶](https://docs.python.org/3/library/importlib.html#importlib.util.MAGIC_NUMBER "Link to this definition")

The bytes which represent the bytecode version number. If you need help with loading/writing bytecode then consider [`importlib.abc.SourceLoader`](https://docs.python.org/3/library/importlib.html#importlib.abc.SourceLoader "importlib.abc.SourceLoader").
Added in version 3.4.

importlib.util.cache_from_source(_path_ , _debug_override =None_, _*_ , _optimization =None_)[¶](https://docs.python.org/3/library/importlib.html#importlib.util.cache_from_source "Link to this definition")

Return the [**PEP 3147**](https://peps.python.org/pep-3147/)/[**PEP 488**](https://peps.python.org/pep-0488/) path to the byte-compiled file associated with the source _path_. For example, if _path_ is `/foo/bar/baz.py` the return value would be `/foo/bar/__pycache__/baz.cpython-32.pyc` for Python 3.2. The `cpython-32` string comes from the current magic tag (see `get_tag()`; if `sys.implementation.cache_tag` is not defined then [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError") will be raised).
The _optimization_ parameter is used to specify the optimization level of the bytecode file. An empty string represents no optimization, so `/foo/bar/baz.py` with an _optimization_ of `''` will result in a bytecode path of `/foo/bar/__pycache__/baz.cpython-32.pyc`. `None` causes the interpreter’s optimization level to be used. Any other value’s string representation is used, so `/foo/bar/baz.py` with an _optimization_ of `2` will lead to the bytecode path of `/foo/bar/__pycache__/baz.cpython-32.opt-2.pyc`. The string representation of _optimization_ can only be alphanumeric, else [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised.
The _debug_override_ parameter is deprecated and can be used to override the system’s value for `__debug__`. A `True` value is the equivalent of setting _optimization_ to the empty string. A `False` value is the same as setting _optimization_ to `1`. If both _debug_override_ an _optimization_ are not `None` then [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") is raised.
Added in version 3.4.
Changed in version 3.5: The _optimization_ parameter was added and the _debug_override_ parameter was deprecated.
Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).

importlib.util.source_from_cache(_path_)[¶](https://docs.python.org/3/library/importlib.html#importlib.util.source_from_cache "Link to this definition")

Given the _path_ to a [**PEP 3147**](https://peps.python.org/pep-3147/) file name, return the associated source code file path. For example, if _path_ is `/foo/bar/__pycache__/baz.cpython-32.pyc` the returned path would be `/foo/bar/baz.py`. _path_ need not exist, however if it does not conform to [**PEP 3147**](https://peps.python.org/pep-3147/) or [**PEP 488**](https://peps.python.org/pep-0488/) format, a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised. If `sys.implementation.cache_tag` is not defined, [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError") is raised.
Added in version 3.4.
Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).

importlib.util.decode_source(_source_bytes_)[¶](https://docs.python.org/3/library/importlib.html#importlib.util.decode_source "Link to this definition")

Decode the given bytes representing source code and return it as a string with universal newlines (as required by [`importlib.abc.InspectLoader.get_source()`](https://docs.python.org/3/library/importlib.html#importlib.abc.InspectLoader.get_source "importlib.abc.InspectLoader.get_source")).
Added in version 3.4.

importlib.util.resolve_name(_name_ , _package_)[¶](https://docs.python.org/3/library/importlib.html#importlib.util.resolve_name "Link to this definition")

Resolve a relative module name to an absolute one.
If **name** has no leading dots, then **name** is simply returned. This allows for usage such as `importlib.util.resolve_name('sys', __spec__.parent)` without doing a check to see if the **package** argument is needed.
[`ImportError`](https://docs.python.org/3/library/exceptions.html#ImportError "ImportError") is raised if **name** is a relative module name but **package** is a false value (e.g. `None` or the empty string). `ImportError` is also raised if a relative name would escape its containing package (e.g. requesting `..bacon` from within the `spam` package).
Added in version 3.3.
Changed in version 3.9: To improve consistency with import statements, raise [`ImportError`](https://docs.python.org/3/library/exceptions.html#ImportError "ImportError") instead of [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") for invalid relative import attempts.

importlib.util.find_spec(_name_ , _package =None_)[¶](https://docs.python.org/3/library/importlib.html#importlib.util.find_spec "Link to this definition")

Find the [spec](https://docs.python.org/3/glossary.html#term-module-spec) for a module, optionally relative to the specified **package** name. If the module is in [`sys.modules`](https://docs.python.org/3/library/sys.html#sys.modules "sys.modules"), then `sys.modules[name].__spec__` is returned (unless the spec would be `None` or is not set, in which case [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised). Otherwise a search using [`sys.meta_path`](https://docs.python.org/3/library/sys.html#sys.meta_path "sys.meta_path") is done. `None` is returned if no spec is found.
If **name** is for a submodule (contains a dot), the parent module is automatically imported.
**name** and **package** work the same as for `import_module()`.
Added in version 3.4.
Changed in version 3.7: Raises [`ModuleNotFoundError`](https://docs.python.org/3/library/exceptions.html#ModuleNotFoundError "ModuleNotFoundError") instead of [`AttributeError`](https://docs.python.org/3/library/exceptions.html#AttributeError "AttributeError") if **package** is in fact not a package (i.e. lacks a [`__path__`](https://docs.python.org/3/reference/datamodel.html#module.__path__ "module.__path__") attribute).

importlib.util.module_from_spec(_spec_)[¶](https://docs.python.org/3/library/importlib.html#importlib.util.module_from_spec "Link to this definition")

Create a new module based on **spec** and [`spec.loader.create_module`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.create_module "importlib.abc.Loader.create_module").
If [`spec.loader.create_module`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.create_module "importlib.abc.Loader.create_module") does not return `None`, then any pre-existing attributes will not be reset. Also, no [`AttributeError`](https://docs.python.org/3/library/exceptions.html#AttributeError "AttributeError") will be raised if triggered while accessing **spec** or setting an attribute on the module.
This function is preferred over using [`types.ModuleType`](https://docs.python.org/3/library/types.html#types.ModuleType "types.ModuleType") to create a new module as **spec** is used to set as many import-controlled attributes on the module as possible.
Added in version 3.5.

importlib.util.spec_from_loader(_name_ , _loader_ , _*_ , _origin =None_, _is_package =None_)[¶](https://docs.python.org/3/library/importlib.html#importlib.util.spec_from_loader "Link to this definition")

A factory function for creating a [`ModuleSpec`](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec "importlib.machinery.ModuleSpec") instance based on a loader. The parameters have the same meaning as they do for ModuleSpec. The function uses available [loader](https://docs.python.org/3/glossary.html#term-loader) APIs, such as `InspectLoader.is_package()`, to fill in any missing information on the spec.
Added in version 3.4.

importlib.util.spec_from_file_location(_name_ , _location_ , _*_ , _loader =None_, _submodule_search_locations =None_)[¶](https://docs.python.org/3/library/importlib.html#importlib.util.spec_from_file_location "Link to this definition")

A factory function for creating a [`ModuleSpec`](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec "importlib.machinery.ModuleSpec") instance based on the path to a file. Missing information will be filled in on the spec by making use of loader APIs and by the implication that the module will be file-based.
Added in version 3.4.
Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).

importlib.util.source_hash(_source_bytes_)[¶](https://docs.python.org/3/library/importlib.html#importlib.util.source_hash "Link to this definition")

Return the hash of _source_bytes_ as bytes. A hash-based `.pyc` file embeds the `source_hash()` of the corresponding source file’s contents in its header.
Added in version 3.7.

importlib.util._incompatible_extension_module_restrictions(_*_ , _disable_check_)[¶](https://docs.python.org/3/library/importlib.html#importlib.util._incompatible_extension_module_restrictions "Link to this definition")

A context manager that can temporarily skip the compatibility check for extension modules. By default the check is enabled and will fail when a single-phase init module is imported in a subinterpreter. It will also fail for a multi-phase init module that doesn’t explicitly support a per-interpreter GIL, when imported in an interpreter with its own GIL.
Note that this function is meant to accommodate an unusual case; one which is likely to eventually go away. There’s is a pretty good chance this is not what you were looking for.
You can get the same effect as this function by implementing the basic interface of multi-phase init ([**PEP 489**](https://peps.python.org/pep-0489/)) and lying about support for multiple interpreters (or per-interpreter GIL).
Warning
Using this function to disable the check can lead to unexpected behavior and even crashes. It should only be used during extension module development.
Added in version 3.12.

_class_ importlib.util.LazyLoader(_loader_)[¶](https://docs.python.org/3/library/importlib.html#importlib.util.LazyLoader "Link to this definition")

A class which postpones the execution of the loader of a module until the module has an attribute accessed.
This class **only** works with loaders that define [`exec_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.exec_module "importlib.abc.Loader.exec_module") as control over what module type is used for the module is required. For those same reasons, the loader’s [`create_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.create_module "importlib.abc.Loader.create_module") method must return `None` or a type for which its `__class__` attribute can be mutated along with not using [slots](https://docs.python.org/3/glossary.html#term-__slots__). Finally, modules which substitute the object placed into [`sys.modules`](https://docs.python.org/3/library/sys.html#sys.modules "sys.modules") will not work as there is no way to properly replace the module references throughout the interpreter safely; [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised if such a substitution is detected.
Note
For projects where startup time is critical, this class allows for potentially minimizing the cost of loading a module if it is never used. For projects where startup time is not essential then use of this class is **heavily** discouraged due to error messages created during loading being postponed and thus occurring out of context.
Added in version 3.5.
Changed in version 3.6: Began calling [`create_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.create_module "importlib.abc.Loader.create_module"), removing the compatibility warning for [`importlib.machinery.BuiltinImporter`](https://docs.python.org/3/library/importlib.html#importlib.machinery.BuiltinImporter "importlib.machinery.BuiltinImporter") and [`importlib.machinery.ExtensionFileLoader`](https://docs.python.org/3/library/importlib.html#importlib.machinery.ExtensionFileLoader "importlib.machinery.ExtensionFileLoader").

_classmethod_ factory(_loader_)[¶](https://docs.python.org/3/library/importlib.html#importlib.util.LazyLoader.factory "Link to this definition")

A class method which returns a callable that creates a lazy loader. This is meant to be used in situations where the loader is passed by class instead of by instance.
Copy```
suffixes = importlib.machinery.SOURCE_SUFFIXES
loader = importlib.machinery.SourceFileLoader
lazy_loader = importlib.util.LazyLoader.factory(loader)
finder = importlib.machinery.FileFinder(path, (lazy_loader, suffixes))

```
