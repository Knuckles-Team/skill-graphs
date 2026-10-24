#  `tarfile` — Read and write tar archive files[¶](https://docs.python.org/3/library/tarfile.html#module-tarfile "Link to this heading")
**Source code:**
* * *
The `tarfile` module makes it possible to read and write tar archives, including those using gzip, bz2 and lzma compression. Use the [`zipfile`](https://docs.python.org/3/library/zipfile.html#module-zipfile "zipfile: Read and write ZIP-format archive files.") module to read or write `.zip` files, or the higher-level functions in [shutil](https://docs.python.org/3/library/shutil.html#archiving-operations).
Some facts and figures:
  * reads and writes [`gzip`](https://docs.python.org/3/library/gzip.html#module-gzip "gzip: Interfaces for gzip compression and decompression using file objects."), [`bz2`](https://docs.python.org/3/library/bz2.html#module-bz2 "bz2: Interfaces for bzip2 compression and decompression."), [`compression.zstd`](https://docs.python.org/3/library/compression.zstd.html#module-compression.zstd "compression.zstd: Low-level interface to compression and decompression routines in the zstd library."), and [`lzma`](https://docs.python.org/3/library/lzma.html#module-lzma "lzma: A Python wrapper for the liblzma compression library.") compressed archives if the respective modules are available.
If any of these [optional modules](https://docs.python.org/3/glossary.html#term-optional-module) are missing from your copy of CPython, look for documentation from your distributor (that is, whoever provided Python to you). If you are the distributor, see [Requirements for optional modules](https://docs.python.org/3/using/configure.html#optional-module-requirements).
  * read/write support for the POSIX.1-1988 (ustar) format.
  * read/write support for the GNU tar format including _longname_ and _longlink_ extensions, read-only support for all variants of the _sparse_ extension including restoration of sparse files.
  * read/write support for the POSIX.1-2001 (pax) format.
  * handles directories, regular files, hardlinks, symbolic links, fifos, character devices and block devices and is able to acquire and restore file information like timestamp, access permissions and owner.


Changed in version 3.3: Added support for [`lzma`](https://docs.python.org/3/library/lzma.html#module-lzma "lzma: A Python wrapper for the liblzma compression library.") compression.
Changed in version 3.12: Archives are extracted using a [filter](https://docs.python.org/3/library/tarfile.html#tarfile-extraction-filter), which makes it possible to either limit surprising/dangerous features, or to acknowledge that they are expected and the archive is fully trusted.
Changed in version 3.14: Set the default extraction filter to [`data`](https://docs.python.org/3/library/tarfile.html#tarfile.data_filter "tarfile.data_filter"), which disallows some dangerous features such as links to absolute paths or paths outside of the destination. Previously, the filter strategy was equivalent to [`fully_trusted`](https://docs.python.org/3/library/tarfile.html#tarfile.fully_trusted_filter "tarfile.fully_trusted_filter").
Changed in version 3.14: Added support for Zstandard compression using [`compression.zstd`](https://docs.python.org/3/library/compression.zstd.html#module-compression.zstd "compression.zstd: Low-level interface to compression and decompression routines in the zstd library.").

tarfile.open(_name =None_, _mode ='r'_, _fileobj =None_, _bufsize =10240_, _** kwargs_)[¶](https://docs.python.org/3/library/tarfile.html#tarfile.open "Link to this definition")

Return a [`TarFile`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile "tarfile.TarFile") object for the pathname _name_. For detailed information on `TarFile` objects and the keyword arguments that are allowed, see [TarFile Objects](https://docs.python.org/3/library/tarfile.html#tarfile-objects).
_mode_ has to be a string of the form `'filemode[:compression]'`, it defaults to `'r'`. Here is a full list of mode combinations:
mode | action
---|---
`'r'` or `'r:*'` | Open for reading with transparent compression (recommended).
`'r:'` | Open for reading exclusively without compression.
`'r:gz'` | Open for reading with gzip compression.
`'r:bz2'` | Open for reading with bzip2 compression.
`'r:xz'` | Open for reading with lzma compression.
`'r:zst'` | Open for reading with Zstandard compression.
`'x'` or `'x:'` | Create a tarfile exclusively without compression. Raise a [`FileExistsError`](https://docs.python.org/3/library/exceptions.html#FileExistsError "FileExistsError") exception if it already exists.
`'x:gz'` | Create a tarfile with gzip compression. Raise a [`FileExistsError`](https://docs.python.org/3/library/exceptions.html#FileExistsError "FileExistsError") exception if it already exists.
`'x:bz2'` | Create a tarfile with bzip2 compression. Raise a [`FileExistsError`](https://docs.python.org/3/library/exceptions.html#FileExistsError "FileExistsError") exception if it already exists.
`'x:xz'` | Create a tarfile with lzma compression. Raise a [`FileExistsError`](https://docs.python.org/3/library/exceptions.html#FileExistsError "FileExistsError") exception if it already exists.
`'x:zst'` | Create a tarfile with Zstandard compression. Raise a [`FileExistsError`](https://docs.python.org/3/library/exceptions.html#FileExistsError "FileExistsError") exception if it already exists.
`'a'` or `'a:'` | Open for appending with no compression. The file is created if it does not exist.
`'w'` or `'w:'` | Open for uncompressed writing.
`'w:gz'` | Open for gzip compressed writing.
`'w:bz2'` | Open for bzip2 compressed writing.
`'w:xz'` | Open for lzma compressed writing.
`'w:zst'` | Open for Zstandard compressed writing.
Note that `'a:gz'`, `'a:bz2'` or `'a:xz'` is not possible. If _mode_ is not suitable to open a certain (compressed) file for reading, [`ReadError`](https://docs.python.org/3/library/tarfile.html#tarfile.ReadError "tarfile.ReadError") is raised. Use _mode_ `'r'` to avoid this. If a compression method is not supported, [`CompressionError`](https://docs.python.org/3/library/tarfile.html#tarfile.CompressionError "tarfile.CompressionError") is raised.
If _fileobj_ is specified, it is used as an alternative to a [file object](https://docs.python.org/3/glossary.html#term-file-object) opened in binary mode for _name_. It is supposed to be at position 0.
For modes `'w:gz'`, `'x:gz'`, `'w|gz'`, `'w:bz2'`, `'x:bz2'`, `'w|bz2'`, [`tarfile.open()`](https://docs.python.org/3/library/tarfile.html#tarfile.open "tarfile.open") accepts the keyword argument _compresslevel_ (default `9`) to specify the compression level of the file.
For modes `'w:xz'`, `'x:xz'` and `'w|xz'`, [`tarfile.open()`](https://docs.python.org/3/library/tarfile.html#tarfile.open "tarfile.open") accepts the keyword argument _preset_ to specify the compression level of the file.
For modes `'w:zst'`, `'x:zst'` and `'w|zst'`, [`tarfile.open()`](https://docs.python.org/3/library/tarfile.html#tarfile.open "tarfile.open") accepts the keyword argument _level_ to specify the compression level of the file. The keyword argument _options_ may also be passed, providing advanced Zstandard compression parameters described by [`CompressionParameter`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter "compression.zstd.CompressionParameter"). The keyword argument _zstd_dict_ can be passed to provide a [`ZstdDict`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdDict "compression.zstd.ZstdDict"), a Zstandard dictionary used to improve compression of smaller amounts of data.
For special purposes, there is a second format for _mode_ : `'filemode|[compression]'`. [`tarfile.open()`](https://docs.python.org/3/library/tarfile.html#tarfile.open "tarfile.open") will return a [`TarFile`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile "tarfile.TarFile") object that processes its data as a stream of blocks. No random seeking will be done on the file. If given, _fileobj_ may be any object that has a [`read()`](https://docs.python.org/3/library/io.html#io.RawIOBase.read "io.RawIOBase.read") or [`write()`](https://docs.python.org/3/library/io.html#io.RawIOBase.write "io.RawIOBase.write") method (depending on the _mode_) that works with bytes. _bufsize_ specifies the blocksize and defaults to `20 * 512` bytes. Use this variant in combination with e.g. `sys.stdin.buffer`, a socket [file object](https://docs.python.org/3/glossary.html#term-file-object) or a tape device. However, such a `TarFile` object is limited in that it does not allow random access, see [Examples](https://docs.python.org/3/library/tarfile.html#tar-examples). The currently possible modes:
Mode | Action
---|---
`'r|*'` | Open a _stream_ of tar blocks for reading with transparent compression.
`'r|'` | Open a _stream_ of uncompressed tar blocks for reading.
`'r|gz'` | Open a gzip compressed _stream_ for reading.
`'r|bz2'` | Open a bzip2 compressed _stream_ for reading.
`'r|xz'` | Open an lzma compressed _stream_ for reading.
`'r|zst'` | Open a Zstandard compressed _stream_ for reading.
`'w|'` | Open an uncompressed _stream_ for writing.
`'w|gz'` | Open a gzip compressed _stream_ for writing.
`'w|bz2'` | Open a bzip2 compressed _stream_ for writing.
`'w|xz'` | Open an lzma compressed _stream_ for writing.
`'w|zst'` | Open a Zstandard compressed _stream_ for writing.
Changed in version 3.5: The `'x'` (exclusive creation) mode was added.
Changed in version 3.6: The _name_ parameter accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).
Changed in version 3.12: The _compresslevel_ keyword argument also works for streams.
Changed in version 3.14: The _preset_ keyword argument also works for streams.

_class_ tarfile.TarFile

Class for reading and writing tar archives. Do not use this class directly: use [`tarfile.open()`](https://docs.python.org/3/library/tarfile.html#tarfile.open "tarfile.open") instead. See [TarFile Objects](https://docs.python.org/3/library/tarfile.html#tarfile-objects).

tarfile.is_tarfile(_name_)[¶](https://docs.python.org/3/library/tarfile.html#tarfile.is_tarfile "Link to this definition")

Return [`True`](https://docs.python.org/3/library/constants.html#True "True") if _name_ is a tar archive file, that the `tarfile` module can read. _name_ may be a [`str`](https://docs.python.org/3/library/stdtypes.html#str "str"), file, or file-like object.
Changed in version 3.9: Support for file and file-like objects.
The `tarfile` module defines the following exceptions:

_exception_ tarfile.TarError[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarError "Link to this definition")

Base class for all `tarfile` exceptions.

_exception_ tarfile.ReadError[¶](https://docs.python.org/3/library/tarfile.html#tarfile.ReadError "Link to this definition")

Is raised when a tar archive is opened, that either cannot be handled by the `tarfile` module or is somehow invalid.

_exception_ tarfile.CompressionError[¶](https://docs.python.org/3/library/tarfile.html#tarfile.CompressionError "Link to this definition")

Is raised when a compression method is not supported or when the data cannot be decoded properly.

_exception_ tarfile.StreamError[¶](https://docs.python.org/3/library/tarfile.html#tarfile.StreamError "Link to this definition")

Is raised for the limitations that are typical for stream-like [`TarFile`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile "tarfile.TarFile") objects.

_exception_ tarfile.ExtractError[¶](https://docs.python.org/3/library/tarfile.html#tarfile.ExtractError "Link to this definition")

Is raised for _non-fatal_ errors when using [`TarFile.extract()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extract "tarfile.TarFile.extract"), but only if [`TarFile.errorlevel`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.errorlevel "tarfile.TarFile.errorlevel")`== 2`.

_exception_ tarfile.HeaderError[¶](https://docs.python.org/3/library/tarfile.html#tarfile.HeaderError "Link to this definition")

Is raised by [`TarInfo.frombuf()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.frombuf "tarfile.TarInfo.frombuf") if the buffer it gets is invalid.

_exception_ tarfile.FilterError[¶](https://docs.python.org/3/library/tarfile.html#tarfile.FilterError "Link to this definition")

Base class for members [refused](https://docs.python.org/3/library/tarfile.html#tarfile-extraction-refuse) by filters.

tarinfo[¶](https://docs.python.org/3/library/tarfile.html#tarfile.FilterError.tarinfo "Link to this definition")

Information about the member that the filter refused to extract, as [TarInfo](https://docs.python.org/3/library/tarfile.html#tarinfo-objects).

_exception_ tarfile.AbsolutePathError[¶](https://docs.python.org/3/library/tarfile.html#tarfile.AbsolutePathError "Link to this definition")

Raised to refuse extracting a member with an absolute path.

_exception_ tarfile.OutsideDestinationError[¶](https://docs.python.org/3/library/tarfile.html#tarfile.OutsideDestinationError "Link to this definition")

Raised to refuse extracting a member outside the destination directory.

_exception_ tarfile.SpecialFileError[¶](https://docs.python.org/3/library/tarfile.html#tarfile.SpecialFileError "Link to this definition")

Raised to refuse extracting a special file (e.g. a device or pipe).

_exception_ tarfile.AbsoluteLinkError[¶](https://docs.python.org/3/library/tarfile.html#tarfile.AbsoluteLinkError "Link to this definition")

Raised to refuse extracting a symbolic link with an absolute path.

_exception_ tarfile.LinkOutsideDestinationError[¶](https://docs.python.org/3/library/tarfile.html#tarfile.LinkOutsideDestinationError "Link to this definition")

Raised to refuse extracting a symbolic link pointing outside the destination directory.

_exception_ tarfile.LinkFallbackError[¶](https://docs.python.org/3/library/tarfile.html#tarfile.LinkFallbackError "Link to this definition")

Raised to refuse emulating a link (hard or symbolic) by extracting another archive member, when that member would be rejected by the filter location. The exception that was raised to reject the replacement member is available as `BaseException.__context__`.
Added in version 3.14.
The following constants are available at the module level:

tarfile.ENCODING[¶](https://docs.python.org/3/library/tarfile.html#tarfile.ENCODING "Link to this definition")

The default character encoding: `'utf-8'` on Windows, the value returned by [`sys.getfilesystemencoding()`](https://docs.python.org/3/library/sys.html#sys.getfilesystemencoding "sys.getfilesystemencoding") otherwise.

tarfile.REGTYPE[¶](https://docs.python.org/3/library/tarfile.html#tarfile.REGTYPE "Link to this definition")


tarfile.AREGTYPE[¶](https://docs.python.org/3/library/tarfile.html#tarfile.AREGTYPE "Link to this definition")

A regular file [`type`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.type "tarfile.TarInfo.type").

tarfile.LNKTYPE[¶](https://docs.python.org/3/library/tarfile.html#tarfile.LNKTYPE "Link to this definition")

A link (inside tarfile) [`type`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.type "tarfile.TarInfo.type").

tarfile.SYMTYPE[¶](https://docs.python.org/3/library/tarfile.html#tarfile.SYMTYPE "Link to this definition")

A symbolic link [`type`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.type "tarfile.TarInfo.type").

tarfile.CHRTYPE[¶](https://docs.python.org/3/library/tarfile.html#tarfile.CHRTYPE "Link to this definition")

A character special device [`type`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.type "tarfile.TarInfo.type").

tarfile.BLKTYPE[¶](https://docs.python.org/3/library/tarfile.html#tarfile.BLKTYPE "Link to this definition")

A block special device [`type`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.type "tarfile.TarInfo.type").

tarfile.DIRTYPE[¶](https://docs.python.org/3/library/tarfile.html#tarfile.DIRTYPE "Link to this definition")

A directory [`type`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.type "tarfile.TarInfo.type").

tarfile.FIFOTYPE[¶](https://docs.python.org/3/library/tarfile.html#tarfile.FIFOTYPE "Link to this definition")

A FIFO special device [`type`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.type "tarfile.TarInfo.type").

tarfile.CONTTYPE[¶](https://docs.python.org/3/library/tarfile.html#tarfile.CONTTYPE "Link to this definition")

A contiguous file [`type`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.type "tarfile.TarInfo.type").

tarfile.GNUTYPE_LONGNAME[¶](https://docs.python.org/3/library/tarfile.html#tarfile.GNUTYPE_LONGNAME "Link to this definition")

A GNU tar longname [`type`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.type "tarfile.TarInfo.type").

tarfile.GNUTYPE_LONGLINK[¶](https://docs.python.org/3/library/tarfile.html#tarfile.GNUTYPE_LONGLINK "Link to this definition")

A GNU tar longlink [`type`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.type "tarfile.TarInfo.type").

tarfile.GNUTYPE_SPARSE[¶](https://docs.python.org/3/library/tarfile.html#tarfile.GNUTYPE_SPARSE "Link to this definition")

A GNU tar sparse file [`type`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.type "tarfile.TarInfo.type").
Each of the following constants defines a tar archive format that the `tarfile` module is able to create. See section [Supported tar formats](https://docs.python.org/3/library/tarfile.html#tar-formats) for details.

tarfile.USTAR_FORMAT[¶](https://docs.python.org/3/library/tarfile.html#tarfile.USTAR_FORMAT "Link to this definition")

POSIX.1-1988 (ustar) format.

tarfile.GNU_FORMAT[¶](https://docs.python.org/3/library/tarfile.html#tarfile.GNU_FORMAT "Link to this definition")

GNU tar format.

tarfile.PAX_FORMAT[¶](https://docs.python.org/3/library/tarfile.html#tarfile.PAX_FORMAT "Link to this definition")

POSIX.1-2001 (pax) format.

tarfile.DEFAULT_FORMAT[¶](https://docs.python.org/3/library/tarfile.html#tarfile.DEFAULT_FORMAT "Link to this definition")

The default format for creating archives. This is currently [`PAX_FORMAT`](https://docs.python.org/3/library/tarfile.html#tarfile.PAX_FORMAT "tarfile.PAX_FORMAT").
Changed in version 3.8: The default format for new archives was changed to [`PAX_FORMAT`](https://docs.python.org/3/library/tarfile.html#tarfile.PAX_FORMAT "tarfile.PAX_FORMAT") from [`GNU_FORMAT`](https://docs.python.org/3/library/tarfile.html#tarfile.GNU_FORMAT "tarfile.GNU_FORMAT").
See also

Module [`zipfile`](https://docs.python.org/3/library/zipfile.html#module-zipfile "zipfile: Read and write ZIP-format archive files.")

Documentation of the [`zipfile`](https://docs.python.org/3/library/zipfile.html#module-zipfile "zipfile: Read and write ZIP-format archive files.") standard module.

[Archiving operations](https://docs.python.org/3/library/shutil.html#archiving-operations)

Documentation of the higher-level archiving facilities provided by the standard [`shutil`](https://docs.python.org/3/library/shutil.html#module-shutil "shutil: High-level file operations, including copying.") module.
Documentation for tar archive files, including GNU tar extensions.
