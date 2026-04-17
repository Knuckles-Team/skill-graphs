[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`importlib.resources` – Package resource reading, opening and access](https://docs.python.org/3/library/importlib.resources.html "previous chapter")
#### Next topic
[`importlib.metadata` – Accessing package metadata](https://docs.python.org/3/library/importlib.metadata.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=importlib.resources.abc+%E2%80%93+Abstract+base+classes+for+resources&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fimportlib.resources.abc.html&pagesource=library%2Fimportlib.resources.abc.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/importlib.metadata.html "importlib.metadata – Accessing package metadata") |
  * [previous](https://docs.python.org/3/library/importlib.resources.html "importlib.resources – Package resource reading, opening and access") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Importing Modules](https://docs.python.org/3/library/modules.html) »
  * [`importlib.resources.abc` – Abstract base classes for resources](https://docs.python.org/3/library/importlib.resources.abc.html)
  * |
  * Theme  Auto Light Dark |


#  `importlib.resources.abc` – Abstract base classes for resources[¶](https://docs.python.org/3/library/importlib.resources.abc.html#module-importlib.resources.abc "Link to this heading")
**Source code:**
* * *
Added in version 3.11.

_class_ importlib.resources.abc.ResourceReader[¶](https://docs.python.org/3/library/importlib.resources.abc.html#importlib.resources.abc.ResourceReader "Link to this definition")

_Superseded by TraversableResources_
An [abstract base class](https://docs.python.org/3/glossary.html#term-abstract-base-class) to provide the ability to read _resources_.
From the perspective of this ABC, a _resource_ is a binary artifact that is shipped within a package. Typically this is something like a data file that lives next to the `__init__.py` file of the package. The purpose of this class is to help abstract out the accessing of such data files so that it does not matter if the package and its data file(s) are stored e.g. in a zip file versus on the file system.
For any of methods of this class, a _resource_ argument is expected to be a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object) which represents conceptually just a file name. This means that no subdirectory paths should be included in the _resource_ argument. This is because the location of the package the reader is for, acts as the “directory”. Hence the metaphor for directories and file names is packages and resources, respectively. This is also why instances of this class are expected to directly correlate to a specific package (instead of potentially representing multiple packages or a module).
Loaders that wish to support resource reading are expected to provide a method called `get_resource_reader(fullname)` which returns an object implementing this ABC’s interface. If the module specified by fullname is not a package, this method should return [`None`](https://docs.python.org/3/library/constants.html#None "None"). An object compatible with this ABC should only be returned when the specified module is a package.
Deprecated since version 3.12: Use [`importlib.resources.abc.TraversableResources`](https://docs.python.org/3/library/importlib.resources.abc.html#importlib.resources.abc.TraversableResources "importlib.resources.abc.TraversableResources") instead.

_abstractmethod_ open_resource(_resource_)[¶](https://docs.python.org/3/library/importlib.resources.abc.html#importlib.resources.abc.ResourceReader.open_resource "Link to this definition")

Returns an opened, [file-like object](https://docs.python.org/3/glossary.html#term-file-like-object) for binary reading of the _resource_.
If the resource cannot be found, [`FileNotFoundError`](https://docs.python.org/3/library/exceptions.html#FileNotFoundError "FileNotFoundError") is raised.

_abstractmethod_ resource_path(_resource_)[¶](https://docs.python.org/3/library/importlib.resources.abc.html#importlib.resources.abc.ResourceReader.resource_path "Link to this definition")

Returns the file system path to the _resource_.
If the resource does not concretely exist on the file system, raise [`FileNotFoundError`](https://docs.python.org/3/library/exceptions.html#FileNotFoundError "FileNotFoundError").

_abstractmethod_ is_resource(_path_)[¶](https://docs.python.org/3/library/importlib.resources.abc.html#importlib.resources.abc.ResourceReader.is_resource "Link to this definition")

Returns `True` if the named _path_ is considered a resource. [`FileNotFoundError`](https://docs.python.org/3/library/exceptions.html#FileNotFoundError "FileNotFoundError") is raised if _path_ does not exist.
Changed in version 3.10: The argument _name_ was renamed to _path_.

_abstractmethod_ contents()[¶](https://docs.python.org/3/library/importlib.resources.abc.html#importlib.resources.abc.ResourceReader.contents "Link to this definition")

Returns an [iterable](https://docs.python.org/3/glossary.html#term-iterable) of strings over the contents of the package. Do note that it is not required that all names returned by the iterator be actual resources, e.g. it is acceptable to return names for which [`is_resource()`](https://docs.python.org/3/library/importlib.resources.abc.html#importlib.resources.abc.ResourceReader.is_resource "importlib.resources.abc.ResourceReader.is_resource") would be false.
Allowing non-resource names to be returned is to allow for situations where how a package and its resources are stored are known a priori and the non-resource names would be useful. For instance, returning subdirectory names is allowed so that when it is known that the package and resources are stored on the file system then those subdirectory names can be used directly.
The abstract method returns an iterable of no items.

_class_ importlib.resources.abc.Traversable[¶](https://docs.python.org/3/library/importlib.resources.abc.html#importlib.resources.abc.Traversable "Link to this definition")

An object with a subset of [`pathlib.Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path") methods suitable for traversing directories and opening files.
For a representation of the object on the file-system, use [`importlib.resources.as_file()`](https://docs.python.org/3/library/importlib.resources.html#importlib.resources.as_file "importlib.resources.as_file").

name[¶](https://docs.python.org/3/library/importlib.resources.abc.html#importlib.resources.abc.Traversable.name "Link to this definition")

Abstract. The base name of this object without any parent references.

_abstractmethod_ iterdir()[¶](https://docs.python.org/3/library/importlib.resources.abc.html#importlib.resources.abc.Traversable.iterdir "Link to this definition")

Yield Traversable objects in self.

_abstractmethod_ is_dir()[¶](https://docs.python.org/3/library/importlib.resources.abc.html#importlib.resources.abc.Traversable.is_dir "Link to this definition")

Return `True` if self is a directory.

_abstractmethod_ is_file()[¶](https://docs.python.org/3/library/importlib.resources.abc.html#importlib.resources.abc.Traversable.is_file "Link to this definition")

Return `True` if self is a file.

_abstractmethod_ joinpath(_* pathsegments_)[¶](https://docs.python.org/3/library/importlib.resources.abc.html#importlib.resources.abc.Traversable.joinpath "Link to this definition")

Traverse directories according to _pathsegments_ and return the result as `Traversable`.
Each _pathsegments_ argument may contain multiple names separated by forward slashes (`/`, `posixpath.sep` ). For example, the following are equivalent:
Copy```
files.joinpath('subdir', 'subsuddir', 'file.txt')
files.joinpath('subdir/subsuddir/file.txt')

```

Note that some `Traversable` implementations might not be updated to the latest version of the protocol. For compatibility with such implementations, provide a single argument without path separators to each call to `joinpath`. For example:
Copy```
files.joinpath('subdir').joinpath('subsubdir').joinpath('file.txt')

```

Changed in version 3.11: `joinpath` accepts multiple _pathsegments_ , and these segments may contain forward slashes as path separators. Previously, only a single _child_ argument was accepted.

_abstractmethod_ __truediv__(_child_)[¶](https://docs.python.org/3/library/importlib.resources.abc.html#importlib.resources.abc.Traversable.__truediv__ "Link to this definition")

Return Traversable child in self. Equivalent to `joinpath(child)`.

_abstractmethod_ open(_mode ='r'_, _* args_, _** kwargs_)[¶](https://docs.python.org/3/library/importlib.resources.abc.html#importlib.resources.abc.Traversable.open "Link to this definition")

_mode_ may be ‘r’ or ‘rb’ to open as text or binary. Return a handle suitable for reading (same as [`pathlib.Path.open`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.open "pathlib.Path.open")).
When opening as text, accepts encoding parameters such as those accepted by [`io.TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper").

read_bytes()[¶](https://docs.python.org/3/library/importlib.resources.abc.html#importlib.resources.abc.Traversable.read_bytes "Link to this definition")

Read contents of self as bytes.

read_text(_encoding =None_)[¶](https://docs.python.org/3/library/importlib.resources.abc.html#importlib.resources.abc.Traversable.read_text "Link to this definition")

Read contents of self as text.

_class_ importlib.resources.abc.TraversableResources[¶](https://docs.python.org/3/library/importlib.resources.abc.html#importlib.resources.abc.TraversableResources "Link to this definition")

An abstract base class for resource readers capable of serving the [`importlib.resources.files()`](https://docs.python.org/3/library/importlib.resources.html#importlib.resources.files "importlib.resources.files") interface. Subclasses [`ResourceReader`](https://docs.python.org/3/library/importlib.resources.abc.html#importlib.resources.abc.ResourceReader "importlib.resources.abc.ResourceReader") and provides concrete implementations of the `ResourceReader`’s abstract methods. Therefore, any loader supplying `TraversableResources` also supplies `ResourceReader`.
Loaders that wish to support resource reading are expected to implement this interface.

_abstractmethod_ files()[¶](https://docs.python.org/3/library/importlib.resources.abc.html#importlib.resources.abc.TraversableResources.files "Link to this definition")

Returns a [`importlib.resources.abc.Traversable`](https://docs.python.org/3/library/importlib.resources.abc.html#importlib.resources.abc.Traversable "importlib.resources.abc.Traversable") object for the loaded package.
#### Previous topic
[`importlib.resources` – Package resource reading, opening and access](https://docs.python.org/3/library/importlib.resources.html "previous chapter")
#### Next topic
[`importlib.metadata` – Accessing package metadata](https://docs.python.org/3/library/importlib.metadata.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=importlib.resources.abc+%E2%80%93+Abstract+base+classes+for+resources&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fimportlib.resources.abc.html&pagesource=library%2Fimportlib.resources.abc.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/importlib.metadata.html "importlib.metadata – Accessing package metadata") |
  * [previous](https://docs.python.org/3/library/importlib.resources.html "importlib.resources – Package resource reading, opening and access") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Importing Modules](https://docs.python.org/3/library/modules.html) »
  * [`importlib.resources.abc` – Abstract base classes for resources](https://docs.python.org/3/library/importlib.resources.abc.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
