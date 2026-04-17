[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`gzip` — Support for **gzip** files](https://docs.python.org/3/library/gzip.html)
    * [Examples of usage](https://docs.python.org/3/library/gzip.html#examples-of-usage)
    * [Command-line interface](https://docs.python.org/3/library/gzip.html#command-line-interface)
      * [Command-line options](https://docs.python.org/3/library/gzip.html#command-line-options)


#### Previous topic
[`zlib` — Compression compatible with **gzip**](https://docs.python.org/3/library/zlib.html "previous chapter")
#### Next topic
[`bz2` — Support for **bzip2** compression](https://docs.python.org/3/library/bz2.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=gzip+%E2%80%94+Support+for+gzip+files&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fgzip.html&pagesource=library%2Fgzip.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/bz2.html "bz2 — Support for bzip2 compression") |
  * [previous](https://docs.python.org/3/library/zlib.html "zlib — Compression compatible with gzip") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Data Compression and Archiving](https://docs.python.org/3/library/archiving.html) »
  * [`gzip` — Support for **gzip** files](https://docs.python.org/3/library/gzip.html)
  * |
  * Theme  Auto Light Dark |


#  `gzip` — Support for **gzip** files[¶](https://docs.python.org/3/library/gzip.html#module-gzip "Link to this heading")
**Source code:**
* * *
This module provides a simple interface to compress and decompress files just like the GNU programs **gzip** and **gunzip** would.
This is an [optional module](https://docs.python.org/3/glossary.html#term-optional-module). If it is missing from your copy of CPython, look for documentation from your distributor (that is, whoever provided Python to you). If you are the distributor, see [Requirements for optional modules](https://docs.python.org/3/using/configure.html#optional-module-requirements).
The data compression is provided by the [`zlib`](https://docs.python.org/3/library/zlib.html#module-zlib "zlib: Low-level interface to compression and decompression routines compatible with gzip.") module.
The `gzip` module provides the [`GzipFile`](https://docs.python.org/3/library/gzip.html#gzip.GzipFile "gzip.GzipFile") class, as well as the [`open()`](https://docs.python.org/3/library/gzip.html#gzip.open "gzip.open"), [`compress()`](https://docs.python.org/3/library/gzip.html#gzip.compress "gzip.compress") and [`decompress()`](https://docs.python.org/3/library/gzip.html#gzip.decompress "gzip.decompress") convenience functions. The `GzipFile` class reads and writes **gzip** -format files, automatically compressing or decompressing the data so that it looks like an ordinary [file object](https://docs.python.org/3/glossary.html#term-file-object).
Note that additional file formats which can be decompressed by the **gzip** and **gunzip** programs, such as those produced by **compress** and **pack** , are not supported by this module.
The module defines the following items:

gzip.open(_filename_ , _mode ='rb'_, _compresslevel =9_, _encoding =None_, _errors =None_, _newline =None_)[¶](https://docs.python.org/3/library/gzip.html#gzip.open "Link to this definition")

Open a gzip-compressed file in binary or text mode, returning a [file object](https://docs.python.org/3/glossary.html#term-file-object).
The _filename_ argument can be an actual filename (a [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") or [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") object), or an existing file object to read from or write to.
The _mode_ argument can be any of `'r'`, `'rb'`, `'a'`, `'ab'`, `'w'`, `'wb'`, `'x'` or `'xb'` for binary mode, or `'rt'`, `'at'`, `'wt'`, or `'xt'` for text mode. The default is `'rb'`.
The _compresslevel_ argument is an integer from 0 to 9, as for the [`GzipFile`](https://docs.python.org/3/library/gzip.html#gzip.GzipFile "gzip.GzipFile") constructor.
For binary mode, this function is equivalent to the [`GzipFile`](https://docs.python.org/3/library/gzip.html#gzip.GzipFile "gzip.GzipFile") constructor: `GzipFile(filename, mode, compresslevel)`. In this case, the _encoding_ , _errors_ and _newline_ arguments must not be provided.
For text mode, a [`GzipFile`](https://docs.python.org/3/library/gzip.html#gzip.GzipFile "gzip.GzipFile") object is created, and wrapped in an [`io.TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper") instance with the specified encoding, error handling behavior, and line ending(s).
Changed in version 3.3: Added support for _filename_ being a file object, support for text mode, and the _encoding_ , _errors_ and _newline_ arguments.
Changed in version 3.4: Added support for the `'x'`, `'xb'` and `'xt'` modes.
Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).

_exception_ gzip.BadGzipFile[¶](https://docs.python.org/3/library/gzip.html#gzip.BadGzipFile "Link to this definition")

An exception raised for invalid gzip files. It inherits from [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError"). [`EOFError`](https://docs.python.org/3/library/exceptions.html#EOFError "EOFError") and [`zlib.error`](https://docs.python.org/3/library/zlib.html#zlib.error "zlib.error") can also be raised for invalid gzip files.
Added in version 3.8.

_class_ gzip.GzipFile(_filename =None_, _mode =None_, _compresslevel =9_, _fileobj =None_, _mtime =None_)[¶](https://docs.python.org/3/library/gzip.html#gzip.GzipFile "Link to this definition")

Constructor for the `GzipFile` class, which simulates most of the methods of a [file object](https://docs.python.org/3/glossary.html#term-file-object), with the exception of the [`truncate()`](https://docs.python.org/3/library/io.html#io.IOBase.truncate "io.IOBase.truncate") method. At least one of _fileobj_ and _filename_ must be given a non-trivial value.
The new class instance is based on _fileobj_ , which can be a regular file, an [`io.BytesIO`](https://docs.python.org/3/library/io.html#io.BytesIO "io.BytesIO") object, or any other object which simulates a file. It defaults to `None`, in which case _filename_ is opened to provide a file object.
When _fileobj_ is not `None`, the _filename_ argument is only used to be included in the **gzip** file header, which may include the original filename of the uncompressed file. It defaults to the filename of _fileobj_ , if discernible; otherwise, it defaults to the empty string, and in this case the original filename is not included in the header.
The _mode_ argument can be any of `'r'`, `'rb'`, `'a'`, `'ab'`, `'w'`, `'wb'`, `'x'`, or `'xb'`, depending on whether the file will be read or written. The default is the mode of _fileobj_ if discernible; otherwise, the default is `'rb'`. In future Python releases the mode of _fileobj_ will not be used. It is better to always specify _mode_ for writing.
Note that the file is always opened in binary mode. To open a compressed file in text mode, use [`open()`](https://docs.python.org/3/library/gzip.html#gzip.open "gzip.open") (or wrap your `GzipFile` with an [`io.TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper")).
The _compresslevel_ argument is an integer from `0` to `9` controlling the level of compression; `1` is fastest and produces the least compression, and `9` is slowest and produces the most compression. `0` is no compression. The default is `9`.
The optional _mtime_ argument is the timestamp requested by gzip. The time is in Unix format, i.e., seconds since 00:00:00 UTC, January 1, 1970. If _mtime_ is omitted or `None`, the current time is used. Use _mtime_ = 0 to generate a compressed stream that does not depend on creation time.
See below for the [`mtime`](https://docs.python.org/3/library/gzip.html#gzip.GzipFile.mtime "gzip.GzipFile.mtime") attribute that is set when decompressing.
Calling a `GzipFile` object’s `close()` method does not close _fileobj_ , since you might wish to append more material after the compressed data. This also allows you to pass an [`io.BytesIO`](https://docs.python.org/3/library/io.html#io.BytesIO "io.BytesIO") object opened for writing as _fileobj_ , and retrieve the resulting memory buffer using the `io.BytesIO` object’s [`getvalue()`](https://docs.python.org/3/library/io.html#io.BytesIO.getvalue "io.BytesIO.getvalue") method.
`GzipFile` supports the [`io.BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase") interface, including iteration and the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement. Only the [`truncate()`](https://docs.python.org/3/library/io.html#io.IOBase.truncate "io.IOBase.truncate") method isn’t implemented.
`GzipFile` also provides the following method and attribute:

peek(_n_)[¶](https://docs.python.org/3/library/gzip.html#gzip.GzipFile.peek "Link to this definition")

Read _n_ uncompressed bytes without advancing the file position. The number of bytes returned may be more or less than requested.
Note
While calling `peek()` does not change the file position of the `GzipFile`, it may change the position of the underlying file object (e.g. if the `GzipFile` was constructed with the _fileobj_ parameter).
Added in version 3.2.

mode[¶](https://docs.python.org/3/library/gzip.html#gzip.GzipFile.mode "Link to this definition")

`'rb'` for reading and `'wb'` for writing.
Changed in version 3.13: In previous versions it was an integer `1` or `2`.

mtime[¶](https://docs.python.org/3/library/gzip.html#gzip.GzipFile.mtime "Link to this definition")

When decompressing, this attribute is set to the last timestamp in the most recently read header. It is an integer, holding the number of seconds since the Unix epoch (00:00:00 UTC, January 1, 1970). The initial value before reading any headers is `None`.

name[¶](https://docs.python.org/3/library/gzip.html#gzip.GzipFile.name "Link to this definition")

The path to the gzip file on disk, as a [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") or [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes"). Equivalent to the output of [`os.fspath()`](https://docs.python.org/3/library/os.html#os.fspath "os.fspath") on the original input path, with no other normalization, resolution or expansion.
Changed in version 3.1: Support for the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement was added, along with the _mtime_ constructor argument and [`mtime`](https://docs.python.org/3/library/gzip.html#gzip.GzipFile.mtime "gzip.GzipFile.mtime") attribute.
Changed in version 3.2: Support for zero-padded and unseekable files was added.
Changed in version 3.3: The [`io.BufferedIOBase.read1()`](https://docs.python.org/3/library/io.html#io.BufferedIOBase.read1 "io.BufferedIOBase.read1") method is now implemented.
Changed in version 3.4: Added support for the `'x'` and `'xb'` modes.
Changed in version 3.5: Added support for writing arbitrary [bytes-like objects](https://docs.python.org/3/glossary.html#term-bytes-like-object). The [`read()`](https://docs.python.org/3/library/io.html#io.BufferedIOBase.read "io.BufferedIOBase.read") method now accepts an argument of `None`.
Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).
Deprecated since version 3.9: Opening `GzipFile` for writing without specifying the _mode_ argument is deprecated.
Changed in version 3.12: Remove the `filename` attribute, use the [`name`](https://docs.python.org/3/library/gzip.html#gzip.GzipFile.name "gzip.GzipFile.name") attribute instead.

gzip.compress(_data_ , _compresslevel =9_, _*_ , _mtime =0_)[¶](https://docs.python.org/3/library/gzip.html#gzip.compress "Link to this definition")

Compress the _data_ , returning a [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") object containing the compressed data. _compresslevel_ and _mtime_ have the same meaning as in the [`GzipFile`](https://docs.python.org/3/library/gzip.html#gzip.GzipFile "gzip.GzipFile") constructor above, but _mtime_ defaults to 0 for reproducible output.
Added in version 3.2.
Changed in version 3.8: Added the _mtime_ parameter for reproducible output.
Changed in version 3.11: Speed is improved by compressing all data at once instead of in a streamed fashion. Calls with _mtime_ set to `0` are delegated to [`zlib.compress()`](https://docs.python.org/3/library/zlib.html#zlib.compress "zlib.compress") for better speed. In this situation the output may contain a gzip header “OS” byte value other than 255 “unknown” as supplied by the underlying zlib implementation.
Changed in version 3.13: The gzip header OS byte is guaranteed to be set to 255 when this function is used as was the case in 3.10 and earlier.
Changed in version 3.14: The _mtime_ parameter now defaults to 0 for reproducible output. For the previous behaviour of using the current time, pass `None` to _mtime_.

gzip.decompress(_data_)[¶](https://docs.python.org/3/library/gzip.html#gzip.decompress "Link to this definition")

Decompress the _data_ , returning a [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") object containing the uncompressed data. This function is capable of decompressing multi-member gzip data (multiple gzip blocks concatenated together). When the data is certain to contain only one member the [`zlib.decompress()`](https://docs.python.org/3/library/zlib.html#zlib.decompress "zlib.decompress") function with _wbits_ set to 31 is faster.
Added in version 3.2.
Changed in version 3.11: Speed is improved by decompressing members at once in memory instead of in a streamed fashion.
## Examples of usage[¶](https://docs.python.org/3/library/gzip.html#examples-of-usage "Link to this heading")
Example of how to read a compressed file:
Copy```
import gzip
with gzip.open('/home/joe/file.txt.gz', 'rb') as f:
    file_content = f.read()

```

Example of how to create a compressed GZIP file:
Copy```
import gzip
content = b"Lots of content here"
with gzip.open('/home/joe/file.txt.gz', 'wb') as f:
    f.write(content)

```

Example of how to GZIP compress an existing file:
Copy```
import gzip
import shutil
with open('/home/joe/file.txt', 'rb') as f_in:
    with gzip.open('/home/joe/file.txt.gz', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

```

Example of how to GZIP compress a binary string:
Copy```
import gzip
s_in = b"Lots of content here"
s_out = gzip.compress(s_in)

```

See also

Module [`zlib`](https://docs.python.org/3/library/zlib.html#module-zlib "zlib: Low-level interface to compression and decompression routines compatible with gzip.")

The basic data compression module needed to support the **gzip** file format.
In case gzip (de)compression is a bottleneck, the
## Command-line interface[¶](https://docs.python.org/3/library/gzip.html#command-line-interface "Link to this heading")
The `gzip` module provides a simple command line interface to compress or decompress files.
Once executed the `gzip` module keeps the input file(s).
Changed in version 3.8: Add a new command line interface with a usage. By default, when you will execute the CLI, the default compression level is 6.
### Command-line options[¶](https://docs.python.org/3/library/gzip.html#command-line-options "Link to this heading")

file[¶](https://docs.python.org/3/library/gzip.html#cmdoption-gzip-arg-file "Link to this definition")

If _file_ is not specified, read from [`sys.stdin`](https://docs.python.org/3/library/sys.html#sys.stdin "sys.stdin").

--fast[¶](https://docs.python.org/3/library/gzip.html#cmdoption-gzip-fast "Link to this definition")

Indicates the fastest compression method (less compression).

--best[¶](https://docs.python.org/3/library/gzip.html#cmdoption-gzip-best "Link to this definition")

Indicates the slowest compression method (best compression).

-d, --decompress[¶](https://docs.python.org/3/library/gzip.html#cmdoption-gzip-d "Link to this definition")

Decompress the given file.

-h, --help[¶](https://docs.python.org/3/library/gzip.html#cmdoption-gzip-h "Link to this definition")

Show the help message.
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`gzip` — Support for **gzip** files](https://docs.python.org/3/library/gzip.html)
    * [Examples of usage](https://docs.python.org/3/library/gzip.html#examples-of-usage)
    * [Command-line interface](https://docs.python.org/3/library/gzip.html#command-line-interface)
      * [Command-line options](https://docs.python.org/3/library/gzip.html#command-line-options)


#### Previous topic
[`zlib` — Compression compatible with **gzip**](https://docs.python.org/3/library/zlib.html "previous chapter")
#### Next topic
[`bz2` — Support for **bzip2** compression](https://docs.python.org/3/library/bz2.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=gzip+%E2%80%94+Support+for+gzip+files&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fgzip.html&pagesource=library%2Fgzip.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/bz2.html "bz2 — Support for bzip2 compression") |
  * [previous](https://docs.python.org/3/library/zlib.html "zlib — Compression compatible with gzip") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Data Compression and Archiving](https://docs.python.org/3/library/archiving.html) »
  * [`gzip` — Support for **gzip** files](https://docs.python.org/3/library/gzip.html)
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
