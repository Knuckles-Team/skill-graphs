

## Comparison to the [`os`](https://docs.python.org/3/library/os.html#module-os "os: Miscellaneous operating system interfaces.") and [`os.path`](https://docs.python.org/3/library/os.path.html#module-os.path "os.path: Operations on pathnames.") modules[¶](https://docs.python.org/3/library/pathlib.html#comparison-to-the-os-and-os-path-modules "Link to this heading")
pathlib implements path operations using [`PurePath`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath "pathlib.PurePath") and [`Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path") objects, and so it’s said to be _object-oriented_. On the other hand, the [`os`](https://docs.python.org/3/library/os.html#module-os "os: Miscellaneous operating system interfaces.") and [`os.path`](https://docs.python.org/3/library/os.path.html#module-os.path "os.path: Operations on pathnames.") modules supply functions that work with low-level `str` and `bytes` objects, which is a more _procedural_ approach. Some users consider the object-oriented style to be more readable.
Many functions in [`os`](https://docs.python.org/3/library/os.html#module-os "os: Miscellaneous operating system interfaces.") and [`os.path`](https://docs.python.org/3/library/os.path.html#module-os.path "os.path: Operations on pathnames.") support `bytes` paths and [paths relative to directory descriptors](https://docs.python.org/3/library/os.html#dir-fd). These features aren’t available in pathlib.
Python’s `str` and `bytes` types, and portions of the [`os`](https://docs.python.org/3/library/os.html#module-os "os: Miscellaneous operating system interfaces.") and [`os.path`](https://docs.python.org/3/library/os.path.html#module-os.path "os.path: Operations on pathnames.") modules, are written in C and are very speedy. pathlib is written in pure Python and is often slower, but rarely slow enough to matter.
pathlib’s path normalization is slightly more opinionated and consistent than [`os.path`](https://docs.python.org/3/library/os.path.html#module-os.path "os.path: Operations on pathnames."). For example, whereas [`os.path.abspath()`](https://docs.python.org/3/library/os.path.html#os.path.abspath "os.path.abspath") eliminates “`..`” segments from a path, which may change its meaning if symlinks are involved, [`Path.absolute()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.absolute "pathlib.Path.absolute") preserves these segments for greater safety.
pathlib’s path normalization may render it unsuitable for some applications:
  1. pathlib normalizes `Path("my_folder/")` to `Path("my_folder")`, which changes a path’s meaning when supplied to various operating system APIs and command-line utilities. Specifically, the absence of a trailing separator may allow the path to be resolved as either a file or directory, rather than a directory only.
  2. pathlib normalizes `Path("./my_program")` to `Path("my_program")`, which changes a path’s meaning when used as an executable search path, such as in a shell or when spawning a child process. Specifically, the absence of a separator in the path may force it to be looked up in `PATH` rather than the current directory.


As a consequence of these differences, pathlib is not a drop-in replacement for [`os.path`](https://docs.python.org/3/library/os.path.html#module-os.path "os.path: Operations on pathnames.").
### Corresponding tools[¶](https://docs.python.org/3/library/pathlib.html#corresponding-tools "Link to this heading")
Below is a table mapping various [`os`](https://docs.python.org/3/library/os.html#module-os "os: Miscellaneous operating system interfaces.") functions to their corresponding [`PurePath`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath "pathlib.PurePath")/[`Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path") equivalent.
[`os`](https://docs.python.org/3/library/os.html#module-os "os: Miscellaneous operating system interfaces.") and [`os.path`](https://docs.python.org/3/library/os.path.html#module-os.path "os.path: Operations on pathnames.") | `pathlib`
---|---
[`os.path.dirname()`](https://docs.python.org/3/library/os.path.html#os.path.dirname "os.path.dirname") | [`PurePath.parent`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.parent "pathlib.PurePath.parent")
[`os.path.basename()`](https://docs.python.org/3/library/os.path.html#os.path.basename "os.path.basename") | [`PurePath.name`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.name "pathlib.PurePath.name")
[`os.path.splitext()`](https://docs.python.org/3/library/os.path.html#os.path.splitext "os.path.splitext") | [`PurePath.stem`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.stem "pathlib.PurePath.stem"), [`PurePath.suffix`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.suffix "pathlib.PurePath.suffix")
[`os.path.join()`](https://docs.python.org/3/library/os.path.html#os.path.join "os.path.join") | [`PurePath.joinpath()`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.joinpath "pathlib.PurePath.joinpath")
[`os.path.isabs()`](https://docs.python.org/3/library/os.path.html#os.path.isabs "os.path.isabs") | [`PurePath.is_absolute()`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.is_absolute "pathlib.PurePath.is_absolute")
[`os.path.relpath()`](https://docs.python.org/3/library/os.path.html#os.path.relpath "os.path.relpath") | [`PurePath.relative_to()`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.relative_to "pathlib.PurePath.relative_to") [[1]](https://docs.python.org/3/library/pathlib.html#id7)
[`os.path.expanduser()`](https://docs.python.org/3/library/os.path.html#os.path.expanduser "os.path.expanduser") | [`Path.expanduser()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.expanduser "pathlib.Path.expanduser") [[2]](https://docs.python.org/3/library/pathlib.html#id8)
[`os.path.realpath()`](https://docs.python.org/3/library/os.path.html#os.path.realpath "os.path.realpath") | [`Path.resolve()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.resolve "pathlib.Path.resolve")
[`os.path.abspath()`](https://docs.python.org/3/library/os.path.html#os.path.abspath "os.path.abspath") | [`Path.absolute()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.absolute "pathlib.Path.absolute") [[3]](https://docs.python.org/3/library/pathlib.html#id9)
[`os.path.exists()`](https://docs.python.org/3/library/os.path.html#os.path.exists "os.path.exists") | [`Path.exists()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.exists "pathlib.Path.exists")
[`os.path.isfile()`](https://docs.python.org/3/library/os.path.html#os.path.isfile "os.path.isfile") | [`Path.is_file()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_file "pathlib.Path.is_file")
[`os.path.isdir()`](https://docs.python.org/3/library/os.path.html#os.path.isdir "os.path.isdir") | [`Path.is_dir()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_dir "pathlib.Path.is_dir")
[`os.path.islink()`](https://docs.python.org/3/library/os.path.html#os.path.islink "os.path.islink") | [`Path.is_symlink()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_symlink "pathlib.Path.is_symlink")
[`os.path.isjunction()`](https://docs.python.org/3/library/os.path.html#os.path.isjunction "os.path.isjunction") | [`Path.is_junction()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_junction "pathlib.Path.is_junction")
[`os.path.ismount()`](https://docs.python.org/3/library/os.path.html#os.path.ismount "os.path.ismount") | [`Path.is_mount()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_mount "pathlib.Path.is_mount")
[`os.path.samefile()`](https://docs.python.org/3/library/os.path.html#os.path.samefile "os.path.samefile") | [`Path.samefile()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.samefile "pathlib.Path.samefile")
[`os.getcwd()`](https://docs.python.org/3/library/os.html#os.getcwd "os.getcwd") | [`Path.cwd()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.cwd "pathlib.Path.cwd")
[`os.stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat") | [`Path.stat()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.stat "pathlib.Path.stat")
[`os.lstat()`](https://docs.python.org/3/library/os.html#os.lstat "os.lstat") | [`Path.lstat()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.lstat "pathlib.Path.lstat")
[`os.listdir()`](https://docs.python.org/3/library/os.html#os.listdir "os.listdir") | [`Path.iterdir()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.iterdir "pathlib.Path.iterdir")
[`os.walk()`](https://docs.python.org/3/library/os.html#os.walk "os.walk") | [`Path.walk()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.walk "pathlib.Path.walk") [[4]](https://docs.python.org/3/library/pathlib.html#id10)
[`os.mkdir()`](https://docs.python.org/3/library/os.html#os.mkdir "os.mkdir"), [`os.makedirs()`](https://docs.python.org/3/library/os.html#os.makedirs "os.makedirs") | [`Path.mkdir()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.mkdir "pathlib.Path.mkdir")
[`os.link()`](https://docs.python.org/3/library/os.html#os.link "os.link") | [`Path.hardlink_to()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.hardlink_to "pathlib.Path.hardlink_to")
[`os.symlink()`](https://docs.python.org/3/library/os.html#os.symlink "os.symlink") | [`Path.symlink_to()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.symlink_to "pathlib.Path.symlink_to")
[`os.readlink()`](https://docs.python.org/3/library/os.html#os.readlink "os.readlink") | [`Path.readlink()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.readlink "pathlib.Path.readlink")
[`os.rename()`](https://docs.python.org/3/library/os.html#os.rename "os.rename") | [`Path.rename()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.rename "pathlib.Path.rename")
[`os.replace()`](https://docs.python.org/3/library/os.html#os.replace "os.replace") | [`Path.replace()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.replace "pathlib.Path.replace")
[`os.remove()`](https://docs.python.org/3/library/os.html#os.remove "os.remove"), [`os.unlink()`](https://docs.python.org/3/library/os.html#os.unlink "os.unlink") | [`Path.unlink()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.unlink "pathlib.Path.unlink")
[`os.rmdir()`](https://docs.python.org/3/library/os.html#os.rmdir "os.rmdir") | [`Path.rmdir()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.rmdir "pathlib.Path.rmdir")
[`os.chmod()`](https://docs.python.org/3/library/os.html#os.chmod "os.chmod") | [`Path.chmod()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.chmod "pathlib.Path.chmod")
[`os.lchmod()`](https://docs.python.org/3/library/os.html#os.lchmod "os.lchmod") | [`Path.lchmod()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.lchmod "pathlib.Path.lchmod")
Footnotes
[[1](https://docs.python.org/3/library/pathlib.html#id3)]
[`os.path.relpath()`](https://docs.python.org/3/library/os.path.html#os.path.relpath "os.path.relpath") calls [`abspath()`](https://docs.python.org/3/library/os.path.html#os.path.abspath "os.path.abspath") to make paths absolute and remove “`..`” parts, whereas [`PurePath.relative_to()`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.relative_to "pathlib.PurePath.relative_to") is a lexical operation that raises [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") when its inputs’ anchors differ (e.g. if one path is absolute and the other relative.)
[[2](https://docs.python.org/3/library/pathlib.html#id4)]
[`os.path.expanduser()`](https://docs.python.org/3/library/os.path.html#os.path.expanduser "os.path.expanduser") returns the path unchanged if the home directory can’t be resolved, whereas [`Path.expanduser()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.expanduser "pathlib.Path.expanduser") raises [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError").
[[3](https://docs.python.org/3/library/pathlib.html#id5)]
[`os.path.abspath()`](https://docs.python.org/3/library/os.path.html#os.path.abspath "os.path.abspath") removes “`..`” components without resolving symlinks, which may change the meaning of the path, whereas [`Path.absolute()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.absolute "pathlib.Path.absolute") leaves any “`..`” components in the path.
[[4](https://docs.python.org/3/library/pathlib.html#id6)]
[`os.walk()`](https://docs.python.org/3/library/os.html#os.walk "os.walk") always follows symlinks when categorizing paths into _dirnames_ and _filenames_ , whereas [`Path.walk()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.walk "pathlib.Path.walk") categorizes all symlinks into _filenames_ when _follow_symlinks_ is false (the default.)
## Protocols[¶](https://docs.python.org/3/library/pathlib.html#module-pathlib.types "Link to this heading")
The `pathlib.types` module provides types for static type checking.
Added in version 3.14.

_class_ pathlib.types.PathInfo[¶](https://docs.python.org/3/library/pathlib.html#pathlib.types.PathInfo "Link to this definition")

A [`typing.Protocol`](https://docs.python.org/3/library/typing.html#typing.Protocol "typing.Protocol") describing the [`Path.info`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.info "pathlib.Path.info") attribute. Implementations may return cached results from their methods.

exists(_*_ , _follow_symlinks =True_)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.types.PathInfo.exists "Link to this definition")

Return `True` if the path is an existing file or directory, or any other kind of file; return `False` if the path doesn’t exist.
If _follow_symlinks_ is `False`, return `True` for symlinks without checking if their targets exist.

is_dir(_*_ , _follow_symlinks =True_)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.types.PathInfo.is_dir "Link to this definition")

Return `True` if the path is a directory, or a symbolic link pointing to a directory; return `False` if the path is (or points to) any other kind of file, or if it doesn’t exist.
If _follow_symlinks_ is `False`, return `True` only if the path is a directory (without following symlinks); return `False` if the path is any other kind of file, or if it doesn’t exist.

is_file(_*_ , _follow_symlinks =True_)[¶](https://docs.python.org/3/library/pathlib.html#pathlib.types.PathInfo.is_file "Link to this definition")

Return `True` if the path is a file, or a symbolic link pointing to a file; return `False` if the path is (or points to) a directory or other non-file, or if it doesn’t exist.
If _follow_symlinks_ is `False`, return `True` only if the path is a file (without following symlinks); return `False` if the path is a directory or other non-file, or if it doesn’t exist.

is_symlink()[¶](https://docs.python.org/3/library/pathlib.html#pathlib.types.PathInfo.is_symlink "Link to this definition")

Return `True` if the path is a symbolic link (even if broken); return `False` if the path is a directory or any kind of file, or if it doesn’t exist.
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`pathlib` — Object-oriented filesystem paths](https://docs.python.org/3/library/pathlib.html)
    * [Basic use](https://docs.python.org/3/library/pathlib.html#basic-use)
    * [Exceptions](https://docs.python.org/3/library/pathlib.html#exceptions)
    * [Pure paths](https://docs.python.org/3/library/pathlib.html#pure-paths)
      * [General properties](https://docs.python.org/3/library/pathlib.html#general-properties)
      * [Operators](https://docs.python.org/3/library/pathlib.html#operators)
      * [Accessing individual parts](https://docs.python.org/3/library/pathlib.html#accessing-individual-parts)
      * [Methods and properties](https://docs.python.org/3/library/pathlib.html#methods-and-properties)
    * [Concrete paths](https://docs.python.org/3/library/pathlib.html#concrete-paths)
      * [Parsing and generating URIs](https://docs.python.org/3/library/pathlib.html#parsing-and-generating-uris)
      * [Expanding and resolving paths](https://docs.python.org/3/library/pathlib.html#expanding-and-resolving-paths)
      * [Querying file type and status](https://docs.python.org/3/library/pathlib.html#querying-file-type-and-status)
      * [Reading and writing files](https://docs.python.org/3/library/pathlib.html#reading-and-writing-files)
      * [Reading directories](https://docs.python.org/3/library/pathlib.html#reading-directories)
      * [Creating files and directories](https://docs.python.org/3/library/pathlib.html#creating-files-and-directories)
      * [Copying, moving and deleting](https://docs.python.org/3/library/pathlib.html#copying-moving-and-deleting)
      * [Permissions and ownership](https://docs.python.org/3/library/pathlib.html#permissions-and-ownership)
    * [Pattern language](https://docs.python.org/3/library/pathlib.html#pattern-language)
    * [Comparison to the `glob` module](https://docs.python.org/3/library/pathlib.html#comparison-to-the-glob-module)
    * [Comparison to the `os` and `os.path` modules](https://docs.python.org/3/library/pathlib.html#comparison-to-the-os-and-os-path-modules)
      * [Corresponding tools](https://docs.python.org/3/library/pathlib.html#corresponding-tools)
    * [Protocols](https://docs.python.org/3/library/pathlib.html#module-pathlib.types)


#### Previous topic
[File and Directory Access](https://docs.python.org/3/library/filesys.html "previous chapter")
#### Next topic
[`os.path` — Common pathname manipulations](https://docs.python.org/3/library/os.path.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=pathlib+%E2%80%94+Object-oriented+filesystem+paths&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fpathlib.html&pagesource=library%2Fpathlib.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/os.path.html "os.path — Common pathname manipulations") |
  * [previous](https://docs.python.org/3/library/filesys.html "File and Directory Access") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [File and Directory Access](https://docs.python.org/3/library/filesys.html) »
  * [`pathlib` — Object-oriented filesystem paths](https://docs.python.org/3/library/pathlib.html#reading-and-writing-files)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
  *[*]: Keyword-only parameters separator (PEP 3102)
