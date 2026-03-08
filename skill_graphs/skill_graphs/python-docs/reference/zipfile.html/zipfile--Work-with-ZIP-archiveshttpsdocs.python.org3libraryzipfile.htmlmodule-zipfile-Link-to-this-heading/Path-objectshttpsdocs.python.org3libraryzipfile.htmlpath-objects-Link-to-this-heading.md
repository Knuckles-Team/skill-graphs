## Path objects[¶](https://docs.python.org/3/library/zipfile.html#path-objects "Link to this heading")

_class_ zipfile.Path(_root_ , _at =''_)[¶](https://docs.python.org/3/library/zipfile.html#zipfile.Path "Link to this definition")

Construct a Path object from a `root` zipfile (which may be a [`ZipFile`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile "zipfile.ZipFile") instance or `file` suitable for passing to the `ZipFile` constructor).
`at` specifies the location of this Path within the zipfile, e.g. ‘dir/file.txt’, ‘dir/’, or ‘’. Defaults to the empty string, indicating the root.
Note
The `Path` class does not sanitize filenames within the ZIP archive. Unlike the [`ZipFile.extract()`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.extract "zipfile.ZipFile.extract") and [`ZipFile.extractall()`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.extractall "zipfile.ZipFile.extractall") methods, it is the caller’s responsibility to validate or sanitize filenames to prevent path traversal vulnerabilities (e.g., filenames containing “..” or absolute paths). When handling untrusted archives, consider resolving filenames using [`os.path.abspath()`](https://docs.python.org/3/library/os.path.html#os.path.abspath "os.path.abspath") and checking against the target directory with [`os.path.commonpath()`](https://docs.python.org/3/library/os.path.html#os.path.commonpath "os.path.commonpath").
Path objects expose the following features of [`pathlib.Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path") objects:
Path objects are traversable using the `/` operator or `joinpath`.

Path.name[¶](https://docs.python.org/3/library/zipfile.html#zipfile.Path.name "Link to this definition")

The final path component.

Path.open(_mode='r'_ , _*_ , _pwd_ , _**_)[¶](https://docs.python.org/3/library/zipfile.html#zipfile.Path.open "Link to this definition")

Invoke [`ZipFile.open()`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.open "zipfile.ZipFile.open") on the current path. Allows opening for read or write, text or binary through supported modes: ‘r’, ‘w’, ‘rb’, ‘wb’. Positional and keyword arguments are passed through to [`io.TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper") when opened as text and ignored otherwise. `pwd` is the `pwd` parameter to `ZipFile.open()`.
Changed in version 3.9: Added support for text and binary modes for open. Default mode is now text.
Changed in version 3.11.2: The `encoding` parameter can be supplied as a positional argument without causing a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError"). As it could in 3.9. Code needing to be compatible with unpatched 3.10 and 3.11 versions must pass all [`io.TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper") arguments, `encoding` included, as keywords.

Path.iterdir()[¶](https://docs.python.org/3/library/zipfile.html#zipfile.Path.iterdir "Link to this definition")

Enumerate the children of the current directory.

Path.is_dir()[¶](https://docs.python.org/3/library/zipfile.html#zipfile.Path.is_dir "Link to this definition")

Return `True` if the current context references a directory.

Path.is_file()[¶](https://docs.python.org/3/library/zipfile.html#zipfile.Path.is_file "Link to this definition")

Return `True` if the current context references a file.

Path.is_symlink()[¶](https://docs.python.org/3/library/zipfile.html#zipfile.Path.is_symlink "Link to this definition")

Return `True` if the current context references a symbolic link.
Added in version 3.12.
Changed in version 3.13: Previously, `is_symlink` would unconditionally return `False`.

Path.exists()[¶](https://docs.python.org/3/library/zipfile.html#zipfile.Path.exists "Link to this definition")

Return `True` if the current context references a file or directory in the zip file.

Path.suffix[¶](https://docs.python.org/3/library/zipfile.html#zipfile.Path.suffix "Link to this definition")

The last dot-separated portion of the final component, if any. This is commonly called the file extension.
Added in version 3.11: Added `Path.suffix` property.

Path.stem[¶](https://docs.python.org/3/library/zipfile.html#zipfile.Path.stem "Link to this definition")

The final path component, without its suffix.
Added in version 3.11: Added `Path.stem` property.

Path.suffixes[¶](https://docs.python.org/3/library/zipfile.html#zipfile.Path.suffixes "Link to this definition")

A list of the path’s suffixes, commonly called file extensions.
Added in version 3.11: Added `Path.suffixes` property.

Path.read_text(_*_ , _**_)[¶](https://docs.python.org/3/library/zipfile.html#zipfile.Path.read_text "Link to this definition")

Read the current file as unicode text. Positional and keyword arguments are passed through to [`io.TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper") (except `buffer`, which is implied by the context).
Changed in version 3.11.2: The `encoding` parameter can be supplied as a positional argument without causing a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError"). As it could in 3.9. Code needing to be compatible with unpatched 3.10 and 3.11 versions must pass all [`io.TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper") arguments, `encoding` included, as keywords.

Path.read_bytes()[¶](https://docs.python.org/3/library/zipfile.html#zipfile.Path.read_bytes "Link to this definition")

Read the current file as bytes.

Path.joinpath(_* other_)[¶](https://docs.python.org/3/library/zipfile.html#zipfile.Path.joinpath "Link to this definition")

Return a new Path object with each of the _other_ arguments joined. The following are equivalent:
Copy```
>>> Path(...).joinpath('child').joinpath('grandchild')
>>> Path(...).joinpath('child', 'grandchild')
>>> Path(...) / 'child' / 'grandchild'

```

Changed in version 3.10: Prior to 3.10, `joinpath` was undocumented and accepted exactly one parameter.
The `zipp.Path` in place of `zipfile.Path` for early access to changes.
## PyZipFile objects[¶](https://docs.python.org/3/library/zipfile.html#pyzipfile-objects "Link to this heading")
The [`PyZipFile`](https://docs.python.org/3/library/zipfile.html#zipfile.PyZipFile "zipfile.PyZipFile") constructor takes the same parameters as the [`ZipFile`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile "zipfile.ZipFile") constructor, and one additional parameter, _optimize_.

_class_ zipfile.PyZipFile(_file_ , _mode ='r'_, _compression =ZIP_STORED_, _allowZip64 =True_, _optimize =-1_)[¶](https://docs.python.org/3/library/zipfile.html#zipfile.PyZipFile "Link to this definition")

Changed in version 3.2: Added the _optimize_ parameter.
Changed in version 3.4: ZIP64 extensions are enabled by default.
Instances have one method in addition to those of [`ZipFile`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile "zipfile.ZipFile") objects:

writepy(_pathname_ , _basename =''_, _filterfunc =None_)[¶](https://docs.python.org/3/library/zipfile.html#zipfile.PyZipFile.writepy "Link to this definition")

Search for files `*.py` and add the corresponding file to the archive.
If the _optimize_ parameter to `PyZipFile` was not given or `-1`, the corresponding file is a `*.pyc` file, compiling if necessary.
If the _optimize_ parameter to `PyZipFile` was `0`, `1` or `2`, only files with that optimization level (see [`compile()`](https://docs.python.org/3/library/functions.html#compile "compile")) are added to the archive, compiling if necessary.
If _pathname_ is a file, the filename must end with `.py`, and just the (corresponding `*.pyc`) file is added at the top level (no path information). If _pathname_ is a file that does not end with `.py`, a [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError") will be raised. If it is a directory, and the directory is not a package directory, then all the files `*.pyc` are added at the top level. If the directory is a package directory, then all `*.pyc` are added under the package name as a file path, and if any subdirectories are package directories, all of these are added recursively in sorted order.
_basename_ is intended for internal use only.
_filterfunc_ , if given, must be a function taking a single string argument. It will be passed each path (including each individual full file path) before it is added to the archive. If _filterfunc_ returns a false value, the path will not be added, and if it is a directory its contents will be ignored. For example, if our test files are all either in `test` directories or start with the string `test_`, we can use a _filterfunc_ to exclude them:
Copy```
>>> zf = PyZipFile('myprog.zip')
>>> def notests(s):
...     fn = os.path.basename(s)
...     return (not (fn == 'test' or fn.startswith('test_')))
...
>>> zf.writepy('myprog', filterfunc=notests)

```

The `writepy()` method makes archives with file names like this:
Copy```
string.pyc                   # Top level name
test/__init__.pyc            # Package directory
test/testall.pyc             # Module test.testall
test/bogus/__init__.pyc      # Subpackage directory
test/bogus/myfile.pyc        # Submodule test.bogus.myfile

```

Changed in version 3.4: Added the _filterfunc_ parameter.
Changed in version 3.6.2: The _pathname_ parameter accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).
Changed in version 3.7: Recursion sorts directory entries.
## ZipInfo objects[¶](https://docs.python.org/3/library/zipfile.html#zipinfo-objects "Link to this heading")
Instances of the [`ZipInfo`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo "zipfile.ZipInfo") class are returned by the [`getinfo()`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.getinfo "zipfile.ZipFile.getinfo") and [`infolist()`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.infolist "zipfile.ZipFile.infolist") methods of [`ZipFile`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile "zipfile.ZipFile") objects. Each object stores information about a single member of the ZIP archive.
There is one classmethod to make a [`ZipInfo`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo "zipfile.ZipInfo") instance for a filesystem file:

_classmethod_ ZipInfo.from_file(_filename_ , _arcname =None_, _*_ , _strict_timestamps =True_)[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo.from_file "Link to this definition")

Construct a [`ZipInfo`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo "zipfile.ZipInfo") instance for a file on the filesystem, in preparation for adding it to a zip file.
_filename_ should be the path to a file or directory on the filesystem.
If _arcname_ is specified, it is used as the name within the archive. If _arcname_ is not specified, the name will be the same as _filename_ , but with any drive letter and leading path separators removed.
The _strict_timestamps_ argument, when set to `False`, allows to zip files older than 1980-01-01 at the cost of setting the timestamp to 1980-01-01. Similar behavior occurs with files newer than 2107-12-31, the timestamp is also set to the limit.
Added in version 3.6.
Changed in version 3.6.2: The _filename_ parameter accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).
Changed in version 3.8: Added the _strict_timestamps_ keyword-only parameter.
Instances have the following methods and attributes:

ZipInfo.is_dir()[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo.is_dir "Link to this definition")

Return `True` if this archive member is a directory.
This uses the entry’s name: directories should always end with `/`.
Added in version 3.6.

ZipInfo.filename[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo.filename "Link to this definition")

Name of the file in the archive.

ZipInfo.date_time[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo.date_time "Link to this definition")

The time and date of the last modification to the archive member. This is a tuple of six values representing the “last [modified] file time” and “last [modified] file date” fields from the ZIP file’s central directory.
The tuple contains:
Index | Value
---|---
`0` | Year (>= 1980)
`1` | Month (one-based)
`2` | Day of month (one-based)
`3` | Hours (zero-based)
`4` | Minutes (zero-based)
`5` | Seconds (zero-based)
Note
The ZIP format supports multiple timestamp fields in different locations (central directory, extra fields for NTFS/UNIX systems, etc.). This attribute specifically returns the timestamp from the central directory. The central directory timestamp format in ZIP files does not support timestamps before 1980. While some extra field formats (such as UNIX timestamps) can represent earlier dates, this attribute only returns the central directory timestamp.
The central directory timestamp is interpreted as representing local time, rather than UTC time, to match the behavior of other zip tools.

ZipInfo.compress_type[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo.compress_type "Link to this definition")

Type of compression for the archive member.

ZipInfo.comment[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo.comment "Link to this definition")

Comment for the individual archive member as a [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") object.

ZipInfo.extra[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo.extra "Link to this definition")

Expansion field data. The [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") object.

ZipInfo.create_system[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo.create_system "Link to this definition")

System which created ZIP archive.

ZipInfo.create_version[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo.create_version "Link to this definition")

PKZIP version which created ZIP archive.

ZipInfo.extract_version[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo.extract_version "Link to this definition")

PKZIP version needed to extract archive.

ZipInfo.reserved[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo.reserved "Link to this definition")

Must be zero.

ZipInfo.flag_bits[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo.flag_bits "Link to this definition")

ZIP flag bits.

ZipInfo.volume[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo.volume "Link to this definition")

Volume number of file header.

ZipInfo.internal_attr[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo.internal_attr "Link to this definition")

Internal attributes.

ZipInfo.external_attr[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo.external_attr "Link to this definition")

External file attributes.

ZipInfo.header_offset[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo.header_offset "Link to this definition")

Byte offset to the file header.

ZipInfo.CRC[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo.CRC "Link to this definition")

CRC-32 of the uncompressed file.

ZipInfo.compress_size[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo.compress_size "Link to this definition")

Size of the compressed data.

ZipInfo.file_size[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo.file_size "Link to this definition")

Size of the uncompressed file.
## Command-line interface[¶](https://docs.python.org/3/library/zipfile.html#command-line-interface "Link to this heading")
The `zipfile` module provides a simple command-line interface to interact with ZIP archives.
If you want to create a new ZIP archive, specify its name after the [`-c`](https://docs.python.org/3/library/zipfile.html#cmdoption-zipfile-c) option and then list the filename(s) that should be included:
Copy```
$ python -m zipfile -c monty.zip spam.txt eggs.txt

```

Passing a directory is also acceptable:
Copy```
$ python -m zipfile -c monty.zip life-of-brian_1979/

```

If you want to extract a ZIP archive into the specified directory, use the [`-e`](https://docs.python.org/3/library/zipfile.html#cmdoption-zipfile-e) option:
Copy```
$ python -m zipfile -e monty.zip target-dir/

```

For a list of the files in a ZIP archive, use the [`-l`](https://docs.python.org/3/library/zipfile.html#cmdoption-zipfile-l) option:
Copy```
$ python -m zipfile -l monty.zip

```

### Command-line options[¶](https://docs.python.org/3/library/zipfile.html#command-line-options "Link to this heading")

-l <zipfile>[¶](https://docs.python.org/3/library/zipfile.html#cmdoption-zipfile-l "Link to this definition")


--list <zipfile>[¶](https://docs.python.org/3/library/zipfile.html#cmdoption-zipfile-list "Link to this definition")

List files in a zipfile.

-c <zipfile> <source1> ... <sourceN>[¶](https://docs.python.org/3/library/zipfile.html#cmdoption-zipfile-c "Link to this definition")


--create <zipfile> <source1> ... <sourceN>[¶](https://docs.python.org/3/library/zipfile.html#cmdoption-zipfile-create "Link to this definition")

Create zipfile from source files.

-e <zipfile> <output_dir>[¶](https://docs.python.org/3/library/zipfile.html#cmdoption-zipfile-e "Link to this definition")


--extract <zipfile> <output_dir>[¶](https://docs.python.org/3/library/zipfile.html#cmdoption-zipfile-extract "Link to this definition")

Extract zipfile into target directory.

-t <zipfile>[¶](https://docs.python.org/3/library/zipfile.html#cmdoption-zipfile-t "Link to this definition")


--test <zipfile>[¶](https://docs.python.org/3/library/zipfile.html#cmdoption-zipfile-test "Link to this definition")

Test whether the zipfile is valid or not.

--metadata-encoding <encoding>[¶](https://docs.python.org/3/library/zipfile.html#cmdoption-zipfile-metadata-encoding "Link to this definition")

Specify encoding of member names for [`-l`](https://docs.python.org/3/library/zipfile.html#cmdoption-zipfile-l), [`-e`](https://docs.python.org/3/library/zipfile.html#cmdoption-zipfile-e) and [`-t`](https://docs.python.org/3/library/zipfile.html#cmdoption-zipfile-t).
Added in version 3.11.
## Decompression pitfalls[¶](https://docs.python.org/3/library/zipfile.html#decompression-pitfalls "Link to this heading")
The extraction in zipfile module might fail due to some pitfalls listed below.
### From file itself[¶](https://docs.python.org/3/library/zipfile.html#from-file-itself "Link to this heading")
Decompression may fail due to incorrect password / CRC checksum / ZIP format or unsupported compression method / decryption.
### File system limitations[¶](https://docs.python.org/3/library/zipfile.html#file-system-limitations "Link to this heading")
Exceeding limitations on different file systems can cause decompression failed. Such as allowable characters in the directory entries, length of the file name, length of the pathname, size of a single file, and number of files, etc.
### Resources limitations[¶](https://docs.python.org/3/library/zipfile.html#resources-limitations "Link to this heading")
The lack of memory or disk volume would lead to decompression failed. For example, decompression bombs (aka
### Interruption[¶](https://docs.python.org/3/library/zipfile.html#interruption "Link to this heading")
Interruption during the decompression, such as pressing control-C or killing the decompression process may result in incomplete decompression of the archive.
### Default behaviors of extraction[¶](https://docs.python.org/3/library/zipfile.html#default-behaviors-of-extraction "Link to this heading")
Not knowing the default extraction behaviors can cause unexpected decompression results. For example, when extracting the same archive twice, it overwrites files without asking.
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`zipfile` — Work with ZIP archives](https://docs.python.org/3/library/zipfile.html)
    * [ZipFile objects](https://docs.python.org/3/library/zipfile.html#zipfile-objects)
    * [Path objects](https://docs.python.org/3/library/zipfile.html#path-objects)
    * [PyZipFile objects](https://docs.python.org/3/library/zipfile.html#pyzipfile-objects)
    * [ZipInfo objects](https://docs.python.org/3/library/zipfile.html#zipinfo-objects)
    * [Command-line interface](https://docs.python.org/3/library/zipfile.html#command-line-interface)
      * [Command-line options](https://docs.python.org/3/library/zipfile.html#command-line-options)
    * [Decompression pitfalls](https://docs.python.org/3/library/zipfile.html#decompression-pitfalls)
      * [From file itself](https://docs.python.org/3/library/zipfile.html#from-file-itself)
      * [File system limitations](https://docs.python.org/3/library/zipfile.html#file-system-limitations)
      * [Resources limitations](https://docs.python.org/3/library/zipfile.html#resources-limitations)
      * [Interruption](https://docs.python.org/3/library/zipfile.html#interruption)
      * [Default behaviors of extraction](https://docs.python.org/3/library/zipfile.html#default-behaviors-of-extraction)


#### Previous topic
[`lzma` — Compression using the LZMA algorithm](https://docs.python.org/3/library/lzma.html "previous chapter")
#### Next topic
[`tarfile` — Read and write tar archive files](https://docs.python.org/3/library/tarfile.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=zipfile+%E2%80%94+Work+with+ZIP+archives&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fzipfile.html&pagesource=library%2Fzipfile.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/tarfile.html "tarfile — Read and write tar archive files") |
  * [previous](https://docs.python.org/3/library/lzma.html "lzma — Compression using the LZMA algorithm") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Data Compression and Archiving](https://docs.python.org/3/library/archiving.html) »
  * [`zipfile` — Work with ZIP archives](https://docs.python.org/3/library/zipfile.html)
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
