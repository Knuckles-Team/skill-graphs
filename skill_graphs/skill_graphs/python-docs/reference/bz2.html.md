[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`bz2` — Support for **bzip2** compression](https://docs.python.org/3/library/bz2.html)
    * [(De)compression of files](https://docs.python.org/3/library/bz2.html#de-compression-of-files)
    * [Incremental (de)compression](https://docs.python.org/3/library/bz2.html#incremental-de-compression)
    * [One-shot (de)compression](https://docs.python.org/3/library/bz2.html#one-shot-de-compression)
    * [Examples of usage](https://docs.python.org/3/library/bz2.html#examples-of-usage)


#### Previous topic
[`gzip` — Support for **gzip** files](https://docs.python.org/3/library/gzip.html "previous chapter")
#### Next topic
[`lzma` — Compression using the LZMA algorithm](https://docs.python.org/3/library/lzma.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=bz2+%E2%80%94+Support+for+bzip2+compression&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fbz2.html&pagesource=library%2Fbz2.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/lzma.html "lzma — Compression using the LZMA algorithm") |
  * [previous](https://docs.python.org/3/library/gzip.html "gzip — Support for gzip files") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Data Compression and Archiving](https://docs.python.org/3/library/archiving.html) »
  * [`bz2` — Support for **bzip2** compression](https://docs.python.org/3/library/bz2.html)
  * |
  * Theme  Auto Light Dark |


#  `bz2` — Support for **bzip2** compression[¶](https://docs.python.org/3/library/bz2.html#module-bz2 "Link to this heading")
**Source code:**
* * *
This module provides a comprehensive interface for compressing and decompressing data using the bzip2 compression algorithm.
The `bz2` module contains:
  * The [`open()`](https://docs.python.org/3/library/bz2.html#bz2.open "bz2.open") function and [`BZ2File`](https://docs.python.org/3/library/bz2.html#bz2.BZ2File "bz2.BZ2File") class for reading and writing compressed files.
  * The [`BZ2Compressor`](https://docs.python.org/3/library/bz2.html#bz2.BZ2Compressor "bz2.BZ2Compressor") and [`BZ2Decompressor`](https://docs.python.org/3/library/bz2.html#bz2.BZ2Decompressor "bz2.BZ2Decompressor") classes for incremental (de)compression.
  * The [`compress()`](https://docs.python.org/3/library/bz2.html#bz2.compress "bz2.compress") and [`decompress()`](https://docs.python.org/3/library/bz2.html#bz2.decompress "bz2.decompress") functions for one-shot (de)compression.


This is an [optional module](https://docs.python.org/3/glossary.html#term-optional-module). If it is missing from your copy of CPython, look for documentation from your distributor (that is, whoever provided Python to you). If you are the distributor, see [Requirements for optional modules](https://docs.python.org/3/using/configure.html#optional-module-requirements).
## (De)compression of files[¶](https://docs.python.org/3/library/bz2.html#de-compression-of-files "Link to this heading")

bz2.open(_filename_ , _mode ='rb'_, _compresslevel =9_, _encoding =None_, _errors =None_, _newline =None_)[¶](https://docs.python.org/3/library/bz2.html#bz2.open "Link to this definition")

Open a bzip2-compressed file in binary or text mode, returning a [file object](https://docs.python.org/3/glossary.html#term-file-object).
As with the constructor for [`BZ2File`](https://docs.python.org/3/library/bz2.html#bz2.BZ2File "bz2.BZ2File"), the _filename_ argument can be an actual filename (a [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") or [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") object), or an existing file object to read from or write to.
The _mode_ argument can be any of `'r'`, `'rb'`, `'w'`, `'wb'`, `'x'`, `'xb'`, `'a'` or `'ab'` for binary mode, or `'rt'`, `'wt'`, `'xt'`, or `'at'` for text mode. The default is `'rb'`.
The _compresslevel_ argument is an integer from 1 to 9, as for the [`BZ2File`](https://docs.python.org/3/library/bz2.html#bz2.BZ2File "bz2.BZ2File") constructor.
For binary mode, this function is equivalent to the [`BZ2File`](https://docs.python.org/3/library/bz2.html#bz2.BZ2File "bz2.BZ2File") constructor: `BZ2File(filename, mode, compresslevel=compresslevel)`. In this case, the _encoding_ , _errors_ and _newline_ arguments must not be provided.
For text mode, a [`BZ2File`](https://docs.python.org/3/library/bz2.html#bz2.BZ2File "bz2.BZ2File") object is created, and wrapped in an [`io.TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper") instance with the specified encoding, error handling behavior, and line ending(s).
Added in version 3.3.
Changed in version 3.4: The `'x'` (exclusive creation) mode was added.
Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).

_class_ bz2.BZ2File(_filename_ , _mode ='r'_, _*_ , _compresslevel =9_)[¶](https://docs.python.org/3/library/bz2.html#bz2.BZ2File "Link to this definition")

Open a bzip2-compressed file in binary mode.
If _filename_ is a [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") or [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") object, open the named file directly. Otherwise, _filename_ should be a [file object](https://docs.python.org/3/glossary.html#term-file-object), which will be used to read or write the compressed data.
The _mode_ argument can be either `'r'` for reading (default), `'w'` for overwriting, `'x'` for exclusive creation, or `'a'` for appending. These can equivalently be given as `'rb'`, `'wb'`, `'xb'` and `'ab'` respectively.
If _filename_ is a file object (rather than an actual file name), a mode of `'w'` does not truncate the file, and is instead equivalent to `'a'`.
If _mode_ is `'w'` or `'a'`, _compresslevel_ can be an integer between `1` and `9` specifying the level of compression: `1` produces the least compression, and `9` (default) produces the most compression.
If _mode_ is `'r'`, the input file may be the concatenation of multiple compressed streams.
`BZ2File` provides all of the members specified by the [`io.BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase"), except for [`detach()`](https://docs.python.org/3/library/io.html#io.BufferedIOBase.detach "io.BufferedIOBase.detach") and [`truncate()`](https://docs.python.org/3/library/io.html#io.IOBase.truncate "io.IOBase.truncate"). Iteration and the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement are supported.
`BZ2File` also provides the following methods and attributes:

peek([_n_])[¶](https://docs.python.org/3/library/bz2.html#bz2.BZ2File.peek "Link to this definition")

Return buffered data without advancing the file position. At least one byte of data will be returned (unless at EOF). The exact number of bytes returned is unspecified.
Note
While calling `peek()` does not change the file position of the `BZ2File`, it may change the position of the underlying file object (e.g. if the `BZ2File` was constructed by passing a file object for _filename_).
Added in version 3.3.

fileno()[¶](https://docs.python.org/3/library/bz2.html#bz2.BZ2File.fileno "Link to this definition")

Return the file descriptor for the underlying file.
Added in version 3.3.

readable()[¶](https://docs.python.org/3/library/bz2.html#bz2.BZ2File.readable "Link to this definition")

Return whether the file was opened for reading.
Added in version 3.3.

seekable()[¶](https://docs.python.org/3/library/bz2.html#bz2.BZ2File.seekable "Link to this definition")

Return whether the file supports seeking.
Added in version 3.3.

writable()[¶](https://docs.python.org/3/library/bz2.html#bz2.BZ2File.writable "Link to this definition")

Return whether the file was opened for writing.
Added in version 3.3.

read1(_size =-1_)[¶](https://docs.python.org/3/library/bz2.html#bz2.BZ2File.read1 "Link to this definition")

Read up to _size_ uncompressed bytes, while trying to avoid making multiple reads from the underlying stream. Reads up to a buffer’s worth of data if size is negative.
Returns `b''` if the file is at EOF.
Added in version 3.3.

readinto(_b_)[¶](https://docs.python.org/3/library/bz2.html#bz2.BZ2File.readinto "Link to this definition")

Read bytes into _b_.
Returns the number of bytes read (0 for EOF).
Added in version 3.3.

mode[¶](https://docs.python.org/3/library/bz2.html#bz2.BZ2File.mode "Link to this definition")

`'rb'` for reading and `'wb'` for writing.
Added in version 3.13.

name[¶](https://docs.python.org/3/library/bz2.html#bz2.BZ2File.name "Link to this definition")

The bzip2 file name. Equivalent to the [`name`](https://docs.python.org/3/library/io.html#io.FileIO.name "io.FileIO.name") attribute of the underlying [file object](https://docs.python.org/3/glossary.html#term-file-object).
Added in version 3.13.
Changed in version 3.1: Support for the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement was added.
Changed in version 3.3: Support was added for _filename_ being a [file object](https://docs.python.org/3/glossary.html#term-file-object) instead of an actual filename.
The `'a'` (append) mode was added, along with support for reading multi-stream files.
Changed in version 3.4: The `'x'` (exclusive creation) mode was added.
Changed in version 3.5: The [`read()`](https://docs.python.org/3/library/io.html#io.BufferedIOBase.read "io.BufferedIOBase.read") method now accepts an argument of `None`.
Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).
Changed in version 3.9: The _buffering_ parameter has been removed. It was ignored and deprecated since Python 3.0. Pass an open file object to control how the file is opened.
The _compresslevel_ parameter became keyword-only.
Changed in version 3.10: This class is thread unsafe in the face of multiple simultaneous readers or writers, just like its equivalent classes in [`gzip`](https://docs.python.org/3/library/gzip.html#module-gzip "gzip: Interfaces for gzip compression and decompression using file objects.") and [`lzma`](https://docs.python.org/3/library/lzma.html#module-lzma "lzma: A Python wrapper for the liblzma compression library.") have always been.
## Incremental (de)compression[¶](https://docs.python.org/3/library/bz2.html#incremental-de-compression "Link to this heading")

_class_ bz2.BZ2Compressor(_compresslevel =9_)[¶](https://docs.python.org/3/library/bz2.html#bz2.BZ2Compressor "Link to this definition")

Create a new compressor object. This object may be used to compress data incrementally. For one-shot compression, use the [`compress()`](https://docs.python.org/3/library/bz2.html#bz2.compress "bz2.compress") function instead.
_compresslevel_ , if given, must be an integer between `1` and `9`. The default is `9`.

compress(_data_)[¶](https://docs.python.org/3/library/bz2.html#bz2.BZ2Compressor.compress "Link to this definition")

Provide data to the compressor object. Returns a chunk of compressed data if possible, or an empty byte string otherwise.
When you have finished providing data to the compressor, call the [`flush()`](https://docs.python.org/3/library/bz2.html#bz2.BZ2Compressor.flush "bz2.BZ2Compressor.flush") method to finish the compression process.

flush()[¶](https://docs.python.org/3/library/bz2.html#bz2.BZ2Compressor.flush "Link to this definition")

Finish the compression process. Returns the compressed data left in internal buffers.
The compressor object may not be used after this method has been called.

_class_ bz2.BZ2Decompressor[¶](https://docs.python.org/3/library/bz2.html#bz2.BZ2Decompressor "Link to this definition")

Create a new decompressor object. This object may be used to decompress data incrementally. For one-shot compression, use the [`decompress()`](https://docs.python.org/3/library/bz2.html#bz2.decompress "bz2.decompress") function instead.
Note
This class does not transparently handle inputs containing multiple compressed streams, unlike [`decompress()`](https://docs.python.org/3/library/bz2.html#bz2.decompress "bz2.decompress") and [`BZ2File`](https://docs.python.org/3/library/bz2.html#bz2.BZ2File "bz2.BZ2File"). If you need to decompress a multi-stream input with `BZ2Decompressor`, you must use a new decompressor for each stream.

decompress(_data_ , _max_length =-1_)[¶](https://docs.python.org/3/library/bz2.html#bz2.BZ2Decompressor.decompress "Link to this definition")

Decompress _data_ (a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)), returning uncompressed data as bytes. Some of _data_ may be buffered internally, for use in later calls to `decompress()`. The returned data should be concatenated with the output of any previous calls to `decompress()`.
If _max_length_ is nonnegative, returns at most _max_length_ bytes of decompressed data. If this limit is reached and further output can be produced, the [`needs_input`](https://docs.python.org/3/library/bz2.html#bz2.BZ2Decompressor.needs_input "bz2.BZ2Decompressor.needs_input") attribute will be set to `False`. In this case, the next call to `decompress()` may provide _data_ as `b''` to obtain more of the output.
If all of the input data was decompressed and returned (either because this was less than _max_length_ bytes, or because _max_length_ was negative), the [`needs_input`](https://docs.python.org/3/library/bz2.html#bz2.BZ2Decompressor.needs_input "bz2.BZ2Decompressor.needs_input") attribute will be set to `True`.
Attempting to decompress data after the end of stream is reached raises an [`EOFError`](https://docs.python.org/3/library/exceptions.html#EOFError "EOFError"). Any data found after the end of the stream is ignored and saved in the [`unused_data`](https://docs.python.org/3/library/bz2.html#bz2.BZ2Decompressor.unused_data "bz2.BZ2Decompressor.unused_data") attribute.
Changed in version 3.5: Added the _max_length_ parameter.

eof[¶](https://docs.python.org/3/library/bz2.html#bz2.BZ2Decompressor.eof "Link to this definition")

`True` if the end-of-stream marker has been reached.
Added in version 3.3.

unused_data[¶](https://docs.python.org/3/library/bz2.html#bz2.BZ2Decompressor.unused_data "Link to this definition")

Data found after the end of the compressed stream.
If this attribute is accessed before the end of the stream has been reached, its value will be `b''`.

needs_input[¶](https://docs.python.org/3/library/bz2.html#bz2.BZ2Decompressor.needs_input "Link to this definition")

`False` if the [`decompress()`](https://docs.python.org/3/library/bz2.html#bz2.BZ2Decompressor.decompress "bz2.BZ2Decompressor.decompress") method can provide more decompressed data before requiring new uncompressed input.
Added in version 3.5.
## One-shot (de)compression[¶](https://docs.python.org/3/library/bz2.html#one-shot-de-compression "Link to this heading")

bz2.compress(_data_ , _compresslevel =9_)[¶](https://docs.python.org/3/library/bz2.html#bz2.compress "Link to this definition")

Compress _data_ , a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object).
_compresslevel_ , if given, must be an integer between `1` and `9`. The default is `9`.
For incremental compression, use a [`BZ2Compressor`](https://docs.python.org/3/library/bz2.html#bz2.BZ2Compressor "bz2.BZ2Compressor") instead.

bz2.decompress(_data_)[¶](https://docs.python.org/3/library/bz2.html#bz2.decompress "Link to this definition")

Decompress _data_ , a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object).
If _data_ is the concatenation of multiple compressed streams, decompress all of the streams.
For incremental decompression, use a [`BZ2Decompressor`](https://docs.python.org/3/library/bz2.html#bz2.BZ2Decompressor "bz2.BZ2Decompressor") instead.
Changed in version 3.3: Support for multi-stream inputs was added.
## Examples of usage[¶](https://docs.python.org/3/library/bz2.html#examples-of-usage "Link to this heading")
Below are some examples of typical usage of the `bz2` module.
Using [`compress()`](https://docs.python.org/3/library/bz2.html#bz2.compress "bz2.compress") and [`decompress()`](https://docs.python.org/3/library/bz2.html#bz2.decompress "bz2.decompress") to demonstrate round-trip compression:
Copy```
>>> import bz2
>>> data = b"""\
... Donec rhoncus quis sapien sit amet molestie. Fusce scelerisque vel augue
... nec ullamcorper. Nam rutrum pretium placerat. Aliquam vel tristique lorem,
... sit amet cursus ante. In interdum laoreet mi, sit amet ultrices purus
... pulvinar a. Nam gravida euismod magna, non various justo tincidunt feugiat.
... Aliquam pharetra lacus non risus vehicula rutrum. Maecenas aliquam leo
... felis. Pellentesque semper nunc sit amet nibh ullamcorper, ac elementum
... dolor luctus. Curabitur lacinia mi ornare consectetur vestibulum."""
>>> c = bz2.compress(data)
>>> len(data) / len(c)  # Data compression ratio
1.513595166163142
>>> d = bz2.decompress(c)
>>> data == d  # Check equality to original object after round-trip
True

```

Using [`BZ2Compressor`](https://docs.python.org/3/library/bz2.html#bz2.BZ2Compressor "bz2.BZ2Compressor") for incremental compression:
Copy```
>>> import bz2
>>> def gen_data(chunks=10, chunksize=1000):
...     """Yield incremental blocks of chunksize bytes."""
...     for _ in range(chunks):
...         yield b"z" * chunksize
...
>>> comp = bz2.BZ2Compressor()
>>> out = b""
>>> for chunk in gen_data():
...     # Provide data to the compressor object
...     out = out + comp.compress(chunk)
...
>>> # Finish the compression process.  Call this once you have
>>> # finished providing data to the compressor.
>>> out = out + comp.flush()

```

The example above uses a very “nonrandom” stream of data (a stream of `b"z"` chunks). Random data tends to compress poorly, while ordered, repetitive data usually yields a high compression ratio.
Writing and reading a bzip2-compressed file in binary mode:
Copy```
>>> import bz2
>>> data = b"""\
... Donec rhoncus quis sapien sit amet molestie. Fusce scelerisque vel augue
... nec ullamcorper. Nam rutrum pretium placerat. Aliquam vel tristique lorem,
... sit amet cursus ante. In interdum laoreet mi, sit amet ultrices purus
... pulvinar a. Nam gravida euismod magna, non various justo tincidunt feugiat.
... Aliquam pharetra lacus non risus vehicula rutrum. Maecenas aliquam leo
... felis. Pellentesque semper nunc sit amet nibh ullamcorper, ac elementum
... dolor luctus. Curabitur lacinia mi ornare consectetur vestibulum."""
>>> with bz2.open("myfile.bz2", "wb") as f:
...     # Write compressed data to file
...     unused = f.write(data)
...
>>> with bz2.open("myfile.bz2", "rb") as f:
...     # Decompress data from file
...     content = f.read()
...
>>> content == data  # Check equality to original object after round-trip
True

```

### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`bz2` — Support for **bzip2** compression](https://docs.python.org/3/library/bz2.html)
    * [(De)compression of files](https://docs.python.org/3/library/bz2.html#de-compression-of-files)
    * [Incremental (de)compression](https://docs.python.org/3/library/bz2.html#incremental-de-compression)
    * [One-shot (de)compression](https://docs.python.org/3/library/bz2.html#one-shot-de-compression)
    * [Examples of usage](https://docs.python.org/3/library/bz2.html#examples-of-usage)


#### Previous topic
[`gzip` — Support for **gzip** files](https://docs.python.org/3/library/gzip.html "previous chapter")
#### Next topic
[`lzma` — Compression using the LZMA algorithm](https://docs.python.org/3/library/lzma.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=bz2+%E2%80%94+Support+for+bzip2+compression&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fbz2.html&pagesource=library%2Fbz2.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/lzma.html "lzma — Compression using the LZMA algorithm") |
  * [previous](https://docs.python.org/3/library/gzip.html "gzip — Support for gzip files") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Data Compression and Archiving](https://docs.python.org/3/library/archiving.html) »
  * [`bz2` — Support for **bzip2** compression](https://docs.python.org/3/library/bz2.html)
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
