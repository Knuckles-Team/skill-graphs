## Examples[¶](https://docs.python.org/3/library/tarfile.html#examples "Link to this heading")
### Reading examples[¶](https://docs.python.org/3/library/tarfile.html#reading-examples "Link to this heading")
How to extract an entire tar archive to the current working directory:
Copy```
import tarfile
tar = tarfile.open("sample.tar.gz")
tar.extractall(filter='data')
tar.close()

```

How to extract a subset of a tar archive with [`TarFile.extractall()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extractall "tarfile.TarFile.extractall") using a generator function instead of a list:
Copy```
import os
import tarfile

def py_files(members):
    for tarinfo in members:
        if os.path.splitext(tarinfo.name)[1] == ".py":
            yield tarinfo

tar = tarfile.open("sample.tar.gz")
tar.extractall(members=py_files(tar))
tar.close()

```

How to read a gzip compressed tar archive and display some member information:
Copy```
import tarfile
tar = tarfile.open("sample.tar.gz", "r:gz")
for tarinfo in tar:
    print(tarinfo.name, "is", tarinfo.size, "bytes in size and is ", end="")
    if tarinfo.isreg():
        print("a regular file.")
    elif tarinfo.isdir():
        print("a directory.")
    else:
        print("something else.")
tar.close()

```

### Writing examples[¶](https://docs.python.org/3/library/tarfile.html#writing-examples "Link to this heading")
How to create an uncompressed tar archive from a list of filenames:
Copy```
import tarfile
tar = tarfile.open("sample.tar", "w")
for name in ["foo", "bar", "quux"]:
    tar.add(name)
tar.close()

```

The same example using the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement:
Copy```
import tarfile
with tarfile.open("sample.tar", "w") as tar:
    for name in ["foo", "bar", "quux"]:
        tar.add(name)

```

How to create and write an archive to stdout using [`sys.stdout.buffer`](https://docs.python.org/3/library/sys.html#sys.stdout "sys.stdout") in the _fileobj_ parameter in [`TarFile.add()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.add "tarfile.TarFile.add"):
Copy```
import sys
import tarfile
with tarfile.open("sample.tar.gz", "w|gz", fileobj=sys.stdout.buffer) as tar:
    for name in ["foo", "bar", "quux"]:
        tar.add(name)

```

How to create an archive and reset the user information using the _filter_ parameter in [`TarFile.add()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.add "tarfile.TarFile.add"):
Copy```
import tarfile
def reset(tarinfo):
    tarinfo.uid = tarinfo.gid = 0
    tarinfo.uname = tarinfo.gname = "root"
    return tarinfo
tar = tarfile.open("sample.tar.gz", "w:gz")
tar.add("foo", filter=reset)
tar.close()

```

## Supported tar formats[¶](https://docs.python.org/3/library/tarfile.html#supported-tar-formats "Link to this heading")
There are three tar formats that can be created with the `tarfile` module:
  * The POSIX.1-1988 ustar format ([`USTAR_FORMAT`](https://docs.python.org/3/library/tarfile.html#tarfile.USTAR_FORMAT "tarfile.USTAR_FORMAT")). It supports filenames up to a length of at best 256 characters and linknames up to 100 characters. The maximum file size is 8 GiB. This is an old and limited but widely supported format.
  * The GNU tar format ([`GNU_FORMAT`](https://docs.python.org/3/library/tarfile.html#tarfile.GNU_FORMAT "tarfile.GNU_FORMAT")). It supports long filenames and linknames, files bigger than 8 GiB and sparse files. It is the de facto standard on GNU/Linux systems. `tarfile` fully supports the GNU tar extensions for long names, sparse file support is read-only.
  * The POSIX.1-2001 pax format ([`PAX_FORMAT`](https://docs.python.org/3/library/tarfile.html#tarfile.PAX_FORMAT "tarfile.PAX_FORMAT")). It is the most flexible format with virtually no limits. It supports long filenames and linknames, large files and stores pathnames in a portable way. Modern tar implementations, including GNU tar, bsdtar/libarchive and star, fully support extended _pax_ features; some old or unmaintained libraries may not, but should treat _pax_ archives as if they were in the universally supported _ustar_ format. It is the current default format for new archives.
It extends the existing _ustar_ format with extra headers for information that cannot be stored otherwise. There are two flavours of pax headers: Extended headers only affect the subsequent file header, global headers are valid for the complete archive and affect all following files. All the data in a pax header is encoded in _UTF-8_ for portability reasons.


There are some more variants of the tar format which can be read, but not created:
  * The ancient V7 format. This is the first tar format from Unix Seventh Edition, storing only regular files and directories. Names must not be longer than 100 characters, there is no user/group name information. Some archives have miscalculated header checksums in case of fields with non-ASCII characters.
  * The SunOS tar extended format. This format is a variant of the POSIX.1-2001 pax format, but is not compatible.


## Unicode issues[¶](https://docs.python.org/3/library/tarfile.html#unicode-issues "Link to this heading")
The tar format was originally conceived to make backups on tape drives with the main focus on preserving file system information. Nowadays tar archives are commonly used for file distribution and exchanging archives over networks. One problem of the original format (which is the basis of all other formats) is that there is no concept of supporting different character encodings. For example, an ordinary tar archive created on a _UTF-8_ system cannot be read correctly on a _Latin-1_ system if it contains non-_ASCII_ characters. Textual metadata (like filenames, linknames, user/group names) will appear damaged. Unfortunately, there is no way to autodetect the encoding of an archive. The pax format was designed to solve this problem. It stores non-ASCII metadata using the universal character encoding _UTF-8_.
The details of character conversion in `tarfile` are controlled by the _encoding_ and _errors_ keyword arguments of the [`TarFile`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile "tarfile.TarFile") class.
_encoding_ defines the character encoding to use for the metadata in the archive. The default value is [`sys.getfilesystemencoding()`](https://docs.python.org/3/library/sys.html#sys.getfilesystemencoding "sys.getfilesystemencoding") or `'ascii'` as a fallback. Depending on whether the archive is read or written, the metadata must be either decoded or encoded. If _encoding_ is not set appropriately, this conversion may fail.
The _errors_ argument defines how characters are treated that cannot be converted. Possible values are listed in section [Error Handlers](https://docs.python.org/3/library/codecs.html#error-handlers). The default scheme is `'surrogateescape'` which Python also uses for its file system calls, see [File Names, Command Line Arguments, and Environment Variables](https://docs.python.org/3/library/os.html#os-filenames).
For [`PAX_FORMAT`](https://docs.python.org/3/library/tarfile.html#tarfile.PAX_FORMAT "tarfile.PAX_FORMAT") archives (the default), _encoding_ is generally not needed because all the metadata is stored using _UTF-8_. _encoding_ is only used in the rare cases when binary pax headers are decoded or when strings with surrogate characters are stored.
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`tarfile` — Read and write tar archive files](https://docs.python.org/3/library/tarfile.html)
    * [TarFile Objects](https://docs.python.org/3/library/tarfile.html#tarfile-objects)
    * [TarInfo Objects](https://docs.python.org/3/library/tarfile.html#tarinfo-objects)
    * [Extraction filters](https://docs.python.org/3/library/tarfile.html#extraction-filters)
      * [Default named filters](https://docs.python.org/3/library/tarfile.html#default-named-filters)
      * [Filter errors](https://docs.python.org/3/library/tarfile.html#filter-errors)
      * [Hints for further verification](https://docs.python.org/3/library/tarfile.html#hints-for-further-verification)
      * [Supporting older Python versions](https://docs.python.org/3/library/tarfile.html#supporting-older-python-versions)
      * [Stateful extraction filter example](https://docs.python.org/3/library/tarfile.html#stateful-extraction-filter-example)
    * [Command-Line Interface](https://docs.python.org/3/library/tarfile.html#command-line-interface)
      * [Command-line options](https://docs.python.org/3/library/tarfile.html#command-line-options)
    * [Examples](https://docs.python.org/3/library/tarfile.html#examples)
      * [Reading examples](https://docs.python.org/3/library/tarfile.html#reading-examples)
      * [Writing examples](https://docs.python.org/3/library/tarfile.html#writing-examples)
    * [Supported tar formats](https://docs.python.org/3/library/tarfile.html#supported-tar-formats)
    * [Unicode issues](https://docs.python.org/3/library/tarfile.html#unicode-issues)


#### Previous topic
[`zipfile` — Work with ZIP archives](https://docs.python.org/3/library/zipfile.html "previous chapter")
#### Next topic
[File Formats](https://docs.python.org/3/library/fileformats.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=tarfile+%E2%80%94+Read+and+write+tar+archive+files&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ftarfile.html&pagesource=library%2Ftarfile.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/fileformats.html "File Formats") |
  * [previous](https://docs.python.org/3/library/zipfile.html "zipfile — Work with ZIP archives") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Data Compression and Archiving](https://docs.python.org/3/library/archiving.html) »
  * [`tarfile` — Read and write tar archive files](https://docs.python.org/3/library/tarfile.html)
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
