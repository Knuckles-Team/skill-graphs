[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`importlib.metadata` – Accessing package metadata](https://docs.python.org/3/library/importlib.metadata.html)
    * [Overview](https://docs.python.org/3/library/importlib.metadata.html#overview)
    * [Functional API](https://docs.python.org/3/library/importlib.metadata.html#functional-api)
      * [Entry points](https://docs.python.org/3/library/importlib.metadata.html#entry-points)
      * [Distribution metadata](https://docs.python.org/3/library/importlib.metadata.html#distribution-metadata)
      * [Distribution versions](https://docs.python.org/3/library/importlib.metadata.html#distribution-versions)
      * [Distribution files](https://docs.python.org/3/library/importlib.metadata.html#distribution-files)
      * [Distribution requirements](https://docs.python.org/3/library/importlib.metadata.html#distribution-requirements)
      * [Mapping import to distribution packages](https://docs.python.org/3/library/importlib.metadata.html#mapping-import-to-distribution-packages)
    * [Distributions](https://docs.python.org/3/library/importlib.metadata.html#distributions)
    * [Distribution Discovery](https://docs.python.org/3/library/importlib.metadata.html#distribution-discovery)
    * [Implementing Custom Providers](https://docs.python.org/3/library/importlib.metadata.html#implementing-custom-providers)
      * [Example](https://docs.python.org/3/library/importlib.metadata.html#example)


#### Previous topic
[`importlib.resources.abc` – Abstract base classes for resources](https://docs.python.org/3/library/importlib.resources.abc.html "previous chapter")
#### Next topic
[The initialization of the `sys.path` module search path](https://docs.python.org/3/library/sys_path_init.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=importlib.metadata+%E2%80%93+Accessing+package+metadata&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fimportlib.metadata.html&pagesource=library%2Fimportlib.metadata.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/sys_path_init.html "The initialization of the sys.path module search path") |
  * [previous](https://docs.python.org/3/library/importlib.resources.abc.html "importlib.resources.abc – Abstract base classes for resources") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Importing Modules](https://docs.python.org/3/library/modules.html) »
  * [`importlib.metadata` – Accessing package metadata](https://docs.python.org/3/library/importlib.metadata.html)
  * |
  * Theme  Auto Light Dark |


#  `importlib.metadata` – Accessing package metadata[¶](https://docs.python.org/3/library/importlib.metadata.html#module-importlib.metadata "Link to this heading")
Added in version 3.8.
Changed in version 3.10: `importlib.metadata` is no longer provisional.
**Source code:**
`importlib.metadata` is a library that provides access to the metadata of an installed [Distribution Package](https://packaging.python.org/en/latest/glossary/#term-Distribution-Package), such as its entry points or its top-level names ([Import Package](https://packaging.python.org/en/latest/glossary/#term-Import-Package)s, modules, if any). Built in part on Python’s import system, this library intends to replace similar functionality in the `pkg_resources`. Along with [`importlib.resources`](https://docs.python.org/3/library/importlib.resources.html#module-importlib.resources "importlib.resources: Package resource reading, opening, and access"), this package can eliminate the need to use the older and less efficient `pkg_resources` package.
`importlib.metadata` operates on third-party _distribution packages_ installed into Python’s `site-packages` directory via tools such as `dist-info` or `egg-info` directories, and metadata defined by the [Core metadata specifications](https://packaging.python.org/en/latest/specifications/core-metadata/#core-metadata).
Important
These are _not_ necessarily equivalent to or correspond 1:1 with the top-level _import package_ names that can be imported inside Python code. One _distribution package_ can contain multiple _import packages_ (and single modules), and one top-level _import package_ may map to multiple _distribution packages_ if it is a namespace package. You can use [packages_distributions()](https://docs.python.org/3/library/importlib.metadata.html#package-distributions) to get a mapping between them.
By default, distribution metadata can live on the file system or in zip archives on [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path"). Through an extension mechanism, the metadata can live almost anywhere.
See also
The documentation for `importlib_metadata`, which supplies a backport of `importlib.metadata`. This includes an `pkg_resources`.
## Overview[¶](https://docs.python.org/3/library/importlib.metadata.html#overview "Link to this heading")
Let’s say you wanted to get the version string for a [Distribution Package](https://packaging.python.org/en/latest/glossary/#term-Distribution-Package) you’ve installed using `pip`. We start by creating a virtual environment and installing something into it:
Copy```
$ python -m venv example
$ source example/bin/activate
(example) $ python -m pip install wheel

```

You can get the version string for `wheel` by running the following:
Copy```
(example) $ python
>>> from importlib.metadata import version
>>> version('wheel')
'0.32.3'

```

You can also get a collection of entry points selectable by properties of the EntryPoint (typically ‘group’ or ‘name’), such as `console_scripts`, `distutils.commands` and others. Each group contains a collection of [EntryPoint](https://docs.python.org/3/library/importlib.metadata.html#entry-points) objects.
You can get the [metadata for a distribution](https://docs.python.org/3/library/importlib.metadata.html#metadata):
Copy```
>>> list(metadata('wheel'))
['Metadata-Version', 'Name', 'Version', 'Summary', 'Home-page', 'Author', 'Author-email', 'Maintainer', 'Maintainer-email', 'License', 'Project-URL', 'Project-URL', 'Project-URL', 'Keywords', 'Platform', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Requires-Python', 'Provides-Extra', 'Requires-Dist', 'Requires-Dist']

```

You can also get a [distribution’s version number](https://docs.python.org/3/library/importlib.metadata.html#version), list its [constituent files](https://docs.python.org/3/library/importlib.metadata.html#files), and get a list of the distribution’s [Distribution requirements](https://docs.python.org/3/library/importlib.metadata.html#requirements).

_exception_ importlib.metadata.PackageNotFoundError[¶](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.PackageNotFoundError "Link to this definition")

Subclass of [`ModuleNotFoundError`](https://docs.python.org/3/library/exceptions.html#ModuleNotFoundError "ModuleNotFoundError") raised by several functions in this module when queried for a distribution package which is not installed in the current Python environment.
## Functional API[¶](https://docs.python.org/3/library/importlib.metadata.html#functional-api "Link to this heading")
This package provides the following functionality via its public API.
### Entry points[¶](https://docs.python.org/3/library/importlib.metadata.html#entry-points "Link to this heading")

importlib.metadata.entry_points(_** select_params_)[¶](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.entry_points "Link to this definition")

Returns a [`EntryPoints`](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.EntryPoints "importlib.metadata.EntryPoints") instance describing entry points for the current environment. Any given keyword parameters are passed to the `select()` method for comparison to the attributes of the individual entry point definitions.
Note: it is not currently possible to query for entry points based on their `EntryPoint.dist` attribute (as different `Distribution` instances do not currently compare equal, even if they have the same attributes)

_class_ importlib.metadata.EntryPoints[¶](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.EntryPoints "Link to this definition")

Details of a collection of installed entry points.
Also provides a `.groups` attribute that reports all identified entry point groups, and a `.names` attribute that reports all identified entry point names.

_class_ importlib.metadata.EntryPoint[¶](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.EntryPoint "Link to this definition")

Details of an installed entry point.
Each `EntryPoint` instance has `.name`, `.group`, and `.value` attributes and a `.load()` method to resolve the value. There are also `.module`, `.attr`, and `.extras` attributes for getting the components of the `.value` attribute, and `.dist` for obtaining information regarding the distribution package that provides the entry point.
Query all entry points:
Copy```
>>> eps = entry_points()

```

The `entry_points()` function returns a `EntryPoints` object, a collection of all `EntryPoint` objects with `names` and `groups` attributes for convenience:
Copy```
>>> sorted(eps.groups)
['console_scripts', 'distutils.commands', 'distutils.setup_keywords', 'egg_info.writers', 'setuptools.installation']

```

`EntryPoints` has a `select()` method to select entry points matching specific properties. Select entry points in the `console_scripts` group:
Copy```
>>> scripts = eps.select(group='console_scripts')

```

Equivalently, since `entry_points()` passes keyword arguments through to select:
Copy```
>>> scripts = entry_points(group='console_scripts')

```

Pick out a specific script named “wheel” (found in the wheel project):
Copy```
>>> 'wheel' in scripts.names
True
>>> wheel = scripts['wheel']

```

Equivalently, query for that entry point during selection:
Copy```
>>> (wheel,) = entry_points(group='console_scripts', name='wheel')
>>> (wheel,) = entry_points().select(group='console_scripts', name='wheel')

```

Inspect the resolved entry point:
Copy```
>>> wheel
EntryPoint(name='wheel', value='wheel.cli:main', group='console_scripts')
>>> wheel.module
'wheel.cli'
>>> wheel.attr
'main'
>>> wheel.extras
[]
>>> main = wheel.load()
>>> main
<function main at 0x103528488>

```

The `group` and `name` are arbitrary values defined by the package author and usually a client will wish to resolve all entry points for a particular group. Read
Changed in version 3.12: The “selectable” entry points were introduced in `importlib_metadata` 3.6 and Python 3.10. Prior to those changes, `entry_points` accepted no parameters and always returned a dictionary of entry points, keyed by group. With `importlib_metadata` 5.0 and Python 3.12, `entry_points` always returns an `EntryPoints` object. See
Changed in version 3.13: `EntryPoint` objects no longer present a tuple-like interface ([`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__ "object.__getitem__")).
### Distribution metadata[¶](https://docs.python.org/3/library/importlib.metadata.html#distribution-metadata "Link to this heading")

importlib.metadata.metadata(_distribution_name_)[¶](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.metadata "Link to this definition")

Return the distribution metadata corresponding to the named distribution package as a [`PackageMetadata`](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.PackageMetadata "importlib.metadata.PackageMetadata") instance.
Raises [`PackageNotFoundError`](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.PackageNotFoundError "importlib.metadata.PackageNotFoundError") if the named distribution package is not installed in the current Python environment.

_class_ importlib.metadata.PackageMetadata[¶](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.PackageMetadata "Link to this definition")

A concrete implementation of the
In addition to providing the defined protocol methods and attributes, subscripting the instance is equivalent to calling the `get()` method.
Every [Distribution Package](https://packaging.python.org/en/latest/glossary/#term-Distribution-Package) includes some metadata, which you can extract using the `metadata()` function:
Copy```
>>> wheel_metadata = metadata('wheel')

```

The keys of the returned data structure name the metadata keywords, and the values are returned unparsed from the distribution metadata:
Copy```
>>> wheel_metadata['Requires-Python']
'>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*'

```

[`PackageMetadata`](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.PackageMetadata "importlib.metadata.PackageMetadata") also presents a `json` attribute that returns all the metadata in a JSON-compatible form per [**PEP 566**](https://peps.python.org/pep-0566/):
Copy```
>>> wheel_metadata.json['requires_python']
'>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*'

```

The full set of available metadata is not described here. See the PyPA [Core metadata specification](https://packaging.python.org/en/latest/specifications/core-metadata/#core-metadata) for additional details.
Changed in version 3.10: The `Description` is now included in the metadata when presented through the payload. Line continuation characters have been removed.
The `json` attribute was added.
### Distribution versions[¶](https://docs.python.org/3/library/importlib.metadata.html#distribution-versions "Link to this heading")

importlib.metadata.version(_distribution_name_)[¶](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.version "Link to this definition")

Return the installed distribution package [version](https://packaging.python.org/en/latest/specifications/core-metadata/#version) for the named distribution package.
Raises [`PackageNotFoundError`](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.PackageNotFoundError "importlib.metadata.PackageNotFoundError") if the named distribution package is not installed in the current Python environment.
The `version()` function is the quickest way to get a [Distribution Package](https://packaging.python.org/en/latest/glossary/#term-Distribution-Package)’s version number, as a string:
Copy```
>>> version('wheel')
'0.32.3'

```

### Distribution files[¶](https://docs.python.org/3/library/importlib.metadata.html#distribution-files "Link to this heading")

importlib.metadata.files(_distribution_name_)[¶](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.files "Link to this definition")

Return the full set of files contained within the named distribution package.
Raises [`PackageNotFoundError`](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.PackageNotFoundError "importlib.metadata.PackageNotFoundError") if the named distribution package is not installed in the current Python environment.
Returns [`None`](https://docs.python.org/3/library/constants.html#None "None") if the distribution is found but the installation database records reporting the files associated with the distribution package are missing.

_class_ importlib.metadata.PackagePath[¶](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.PackagePath "Link to this definition")

A [`pathlib.PurePath`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath "pathlib.PurePath") derived object with additional `dist`, `size`, and `hash` properties corresponding to the distribution package’s installation metadata for that file.
The `files()` function takes a [Distribution Package](https://packaging.python.org/en/latest/glossary/#term-Distribution-Package) name and returns all of the files installed by this distribution. Each file is reported as a [`PackagePath`](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.PackagePath "importlib.metadata.PackagePath") instance. For example:
Copy```
>>> util = [p for p in files('wheel') if 'util.py' in str(p)][0]
>>> util
PackagePath('wheel/util.py')
>>> util.size
859
>>> util.dist
<importlib.metadata._hooks.PathDistribution object at 0x101e0cef0>
>>> util.hash
<FileHash mode: sha256 value: bYkw5oMccfazVCoYQwKkkemoVyMAFoR34mmKBx8R1NI>

```

Once you have the file, you can also read its contents:
Copy```
>>> print(util.read_text())
import base64
import sys
...
def as_bytes(s):
    if isinstance(s, text_type):
        return s.encode('utf-8')
    return s

```

You can also use the `locate()` method to get the absolute path to the file:
Copy```
>>> util.locate()
PosixPath('/home/gustav/example/lib/site-packages/wheel/util.py')

```

In the case where the metadata file listing files (`RECORD` or `SOURCES.txt`) is missing, `files()` will return [`None`](https://docs.python.org/3/library/constants.html#None "None"). The caller may wish to wrap calls to `files()` in
### Distribution requirements[¶](https://docs.python.org/3/library/importlib.metadata.html#distribution-requirements "Link to this heading")

importlib.metadata.requires(_distribution_name_)[¶](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.requires "Link to this definition")

Return the declared dependency specifiers for the named distribution package.
Raises [`PackageNotFoundError`](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.PackageNotFoundError "importlib.metadata.PackageNotFoundError") if the named distribution package is not installed in the current Python environment.
To get the full set of requirements for a [Distribution Package](https://packaging.python.org/en/latest/glossary/#term-Distribution-Package), use the `requires()` function:
Copy```
>>> requires('wheel')
["pytest (>=3.0.0) ; extra == 'test'", "pytest-cov ; extra == 'test'"]

```

### Mapping import to distribution packages[¶](https://docs.python.org/3/library/importlib.metadata.html#mapping-import-to-distribution-packages "Link to this heading")

importlib.metadata.packages_distributions()[¶](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.packages_distributions "Link to this definition")

Return a mapping from the top level module and import package names found via [`sys.meta_path`](https://docs.python.org/3/library/sys.html#sys.meta_path "sys.meta_path") to the names of the distribution packages (if any) that provide the corresponding files.
To allow for namespace packages (which may have members provided by multiple distribution packages), each top level import name maps to a list of distribution names rather than mapping directly to a single name.
A convenience method to resolve the [Distribution Package](https://packaging.python.org/en/latest/glossary/#term-Distribution-Package) name (or names, in the case of a namespace package) that provide each importable top-level Python module or [Import Package](https://packaging.python.org/en/latest/glossary/#term-Import-Package):
Copy```
>>> packages_distributions()
{'importlib_metadata': ['importlib-metadata'], 'yaml': ['PyYAML'], 'jaraco': ['jaraco.classes', 'jaraco.functools'], ...}

```

Some editable installs,
Added in version 3.10.
## Distributions[¶](https://docs.python.org/3/library/importlib.metadata.html#distributions "Link to this heading")

importlib.metadata.distribution(_distribution_name_)[¶](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.distribution "Link to this definition")

Return a [`Distribution`](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.Distribution "importlib.metadata.Distribution") instance describing the named distribution package.
Raises [`PackageNotFoundError`](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.PackageNotFoundError "importlib.metadata.PackageNotFoundError") if the named distribution package is not installed in the current Python environment.

_class_ importlib.metadata.Distribution[¶](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.Distribution "Link to this definition")

Details of an installed distribution package.
Note: different `Distribution` instances do not currently compare equal, even if they relate to the same installed distribution and accordingly have the same attributes.
While the module level API described above is the most common and convenient usage, you can get all of that information from the `Distribution` class. `Distribution` is an abstract object that represents the metadata for a Python [Distribution Package](https://packaging.python.org/en/latest/glossary/#term-Distribution-Package). You can get the concrete `Distribution` subclass instance for an installed distribution package by calling the [`distribution()`](https://docs.python.org/3/library/importlib.metadata.html#importlib.metadata.distribution "importlib.metadata.distribution") function:
Copy```
>>> from importlib.metadata import distribution
>>> dist = distribution('wheel')
>>> type(dist)
<class 'importlib.metadata.PathDistribution'>

```

Thus, an alternative way to get the version number is through the `Distribution` instance:
Copy```
>>> dist.version
'0.32.3'

```

There are all kinds of additional metadata available on `Distribution` instances:
Copy```
>>> dist.metadata['Requires-Python']
'>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*'
>>> dist.metadata['License']
'MIT'

```

For editable packages, an `origin` property may present [**PEP 610**](https://peps.python.org/pep-0610/) metadata:
Copy```
>>> dist.origin.url
'file:///path/to/wheel-0.32.3.editable-py3-none-any.whl'

```

The full set of available metadata is not described here. See the PyPA [Core metadata specification](https://packaging.python.org/en/latest/specifications/core-metadata/#core-metadata) for additional details.
Added in version 3.13: The `.origin` property was added.
## Distribution Discovery[¶](https://docs.python.org/3/library/importlib.metadata.html#distribution-discovery "Link to this heading")
By default, this package provides built-in support for discovery of metadata for file system and zip file [Distribution Package](https://packaging.python.org/en/latest/glossary/#term-Distribution-Package)s. This metadata finder search defaults to `sys.path`, but varies slightly in how it interprets those values from how other import machinery does. In particular:
  * `importlib.metadata` does not honor [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") objects on `sys.path`.
  * `importlib.metadata` will incidentally honor [`pathlib.Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path") objects on `sys.path` even though such values will be ignored for imports.


## Implementing Custom Providers[¶](https://docs.python.org/3/library/importlib.metadata.html#implementing-custom-providers "Link to this heading")
`importlib.metadata` address two API surfaces, one for _consumers_ and another for _providers_. Most users are consumers, consuming metadata provided by the packages. There are other use-cases, however, where users wish to expose metadata through some other mechanism, such as alongside a custom importer. Such a use case calls for a _custom provider_.
Because [Distribution Package](https://packaging.python.org/en/latest/glossary/#term-Distribution-Package) metadata is not available through [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path") searches, or package loaders directly, the metadata for a distribution is found through import system [finders](https://docs.python.org/3/reference/import.html#finders-and-loaders). To find a distribution package’s metadata, `importlib.metadata` queries the list of [meta path finders](https://docs.python.org/3/glossary.html#term-meta-path-finder) on [`sys.meta_path`](https://docs.python.org/3/library/sys.html#sys.meta_path "sys.meta_path").
The implementation has hooks integrated into the `PathFinder`, serving metadata for distribution packages found on the file system.
The abstract class [`importlib.abc.MetaPathFinder`](https://docs.python.org/3/library/importlib.html#importlib.abc.MetaPathFinder "importlib.abc.MetaPathFinder") defines the interface expected of finders by Python’s import system. `importlib.metadata` extends this protocol by looking for an optional `find_distributions` callable on the finders from [`sys.meta_path`](https://docs.python.org/3/library/sys.html#sys.meta_path "sys.meta_path") and presents this extended interface as the `DistributionFinder` abstract base class, which defines this abstract method:
Copy```
@abc.abstractmethod
def find_distributions(context=DistributionFinder.Context()) -> Iterable[Distribution]:
    """Return an iterable of all Distribution instances capable of
    loading the metadata for packages for the indicated ``context``.
    """

```

The `DistributionFinder.Context` object provides `.path` and `.name` properties indicating the path to search and name to match and may supply other relevant context sought by the consumer.
In practice, to support finding distribution package metadata in locations other than the file system, subclass `Distribution` and implement the abstract methods. Then from a custom finder, return instances of this derived `Distribution` in the `find_distributions()` method.
### Example[¶](https://docs.python.org/3/library/importlib.metadata.html#example "Link to this heading")
Imagine a custom finder that loads Python modules from a database:
Copy```
class DatabaseImporter(importlib.abc.MetaPathFinder):
    def __init__(self, db):
        self.db = db

    def find_spec(self, fullname, target=None) -> ModuleSpec:
        return self.db.spec_from_name(fullname)

sys.meta_path.append(DatabaseImporter(connect_db(...)))

```

That importer now presumably provides importable modules from a database, but it provides no metadata or entry points. For this custom importer to provide metadata, it would also need to implement `DistributionFinder`:
Copy```
from importlib.metadata import DistributionFinder

class DatabaseImporter(DistributionFinder):
    ...

    def find_distributions(self, context=DistributionFinder.Context()):
        query = dict(name=context.name) if context.name else {}
        for dist_record in self.db.query_distributions(query):
            yield DatabaseDistribution(dist_record)

```

In this way, `query_distributions` would return records for each distribution served by the database matching the query. For example, if `requests-1.0` is in the database, `find_distributions` would yield a `DatabaseDistribution` for `Context(name='requests')` or `Context(name=None)`.
For the sake of simplicity, this example ignores `context.path`. The `path` attribute defaults to `sys.path` and is the set of import paths to be considered in the search. A `DatabaseImporter` could potentially function without any concern for a search path. Assuming the importer does no partitioning, the “path” would be irrelevant. In order to illustrate the purpose of `path`, the example would need to illustrate a more complex `DatabaseImporter` whose behavior varied depending on `sys.path`/`PYTHONPATH`. In that case, the `find_distributions` should honor the `context.path` and only yield `Distribution`s pertinent to that path.
`DatabaseDistribution`, then, would look something like:
Copy```
class DatabaseDistribution(importlib.metadata.Distribution):
    def __init__(self, record):
        self.record = record

    def read_text(self, filename):
        """
        Read a file like "METADATA" for the current distribution.
        """
        if filename == "METADATA":
            return f"""Name: {self.record.name}
Version: {self.record.version}
"""
        if filename == "entry_points.txt":
            return "\n".join(
              f"""[{ep.group}]\n{ep.name}={ep.value}"""
              for ep in self.record.entry_points)

    def locate_file(self, path):
        raise RuntimeError("This distribution has no file system")

```

This basic implementation should provide metadata and entry points for packages served by the `DatabaseImporter`, assuming that the `record` supplies suitable `.name`, `.version`, and `.entry_points` attributes.
The `DatabaseDistribution` may also provide other metadata files, like `RECORD` (required for `Distribution.files`) or override the implementation of `Distribution.files`. See the source for more inspiration.
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`importlib.metadata` – Accessing package metadata](https://docs.python.org/3/library/importlib.metadata.html)
    * [Overview](https://docs.python.org/3/library/importlib.metadata.html#overview)
    * [Functional API](https://docs.python.org/3/library/importlib.metadata.html#functional-api)
      * [Entry points](https://docs.python.org/3/library/importlib.metadata.html#entry-points)
      * [Distribution metadata](https://docs.python.org/3/library/importlib.metadata.html#distribution-metadata)
      * [Distribution versions](https://docs.python.org/3/library/importlib.metadata.html#distribution-versions)
      * [Distribution files](https://docs.python.org/3/library/importlib.metadata.html#distribution-files)
      * [Distribution requirements](https://docs.python.org/3/library/importlib.metadata.html#distribution-requirements)
      * [Mapping import to distribution packages](https://docs.python.org/3/library/importlib.metadata.html#mapping-import-to-distribution-packages)
    * [Distributions](https://docs.python.org/3/library/importlib.metadata.html#distributions)
    * [Distribution Discovery](https://docs.python.org/3/library/importlib.metadata.html#distribution-discovery)
    * [Implementing Custom Providers](https://docs.python.org/3/library/importlib.metadata.html#implementing-custom-providers)
      * [Example](https://docs.python.org/3/library/importlib.metadata.html#example)


#### Previous topic
[`importlib.resources.abc` – Abstract base classes for resources](https://docs.python.org/3/library/importlib.resources.abc.html "previous chapter")
#### Next topic
[The initialization of the `sys.path` module search path](https://docs.python.org/3/library/sys_path_init.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=importlib.metadata+%E2%80%93+Accessing+package+metadata&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fimportlib.metadata.html&pagesource=library%2Fimportlib.metadata.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/sys_path_init.html "The initialization of the sys.path module search path") |
  * [previous](https://docs.python.org/3/library/importlib.resources.abc.html "importlib.resources.abc – Abstract base classes for resources") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Importing Modules](https://docs.python.org/3/library/modules.html) »
  * [`importlib.metadata` – Accessing package metadata](https://docs.python.org/3/library/importlib.metadata.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
