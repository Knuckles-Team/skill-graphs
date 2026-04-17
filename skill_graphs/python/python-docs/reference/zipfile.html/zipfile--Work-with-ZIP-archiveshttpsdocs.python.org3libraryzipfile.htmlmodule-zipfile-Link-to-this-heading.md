#  `zipfile` — Work with ZIP archives[¶](https://docs.python.org/3/library/zipfile.html#module-zipfile "Link to this heading")
**Source code:**
* * *
The ZIP file format is a common archive and compression standard. This module provides tools to create, read, write, append, and list a ZIP file. Any advanced use of this module will require an understanding of the format, as defined in
This module does not handle multipart ZIP files. It can handle ZIP files that use the ZIP64 extensions (that is ZIP files that are more than 4 GiB in size). It supports decryption of encrypted files in ZIP archives, but it cannot create an encrypted file. Decryption is extremely slow as it is implemented in native Python rather than C.
Handling compressed archives requires [optional modules](https://docs.python.org/3/glossary.html#term-optional-module) such as [`zlib`](https://docs.python.org/3/library/zlib.html#module-zlib "zlib: Low-level interface to compression and decompression routines compatible with gzip."), [`bz2`](https://docs.python.org/3/library/bz2.html#module-bz2 "bz2: Interfaces for bzip2 compression and decompression."), [`lzma`](https://docs.python.org/3/library/lzma.html#module-lzma "lzma: A Python wrapper for the liblzma compression library."), and [`compression.zstd`](https://docs.python.org/3/library/compression.zstd.html#module-compression.zstd "compression.zstd: Low-level interface to compression and decompression routines in the zstd library."). If any of them are missing from your copy of CPython, look for documentation from your distributor (that is, whoever provided Python to you). If you are the distributor, see [Requirements for optional modules](https://docs.python.org/3/using/configure.html#optional-module-requirements).
The module defines the following items:

_exception_ zipfile.BadZipFile[¶](https://docs.python.org/3/library/zipfile.html#zipfile.BadZipFile "Link to this definition")

The error raised for bad ZIP files.
Added in version 3.2.

_exception_ zipfile.BadZipfile[¶](https://docs.python.org/3/library/zipfile.html#zipfile.BadZipfile "Link to this definition")

Alias of [`BadZipFile`](https://docs.python.org/3/library/zipfile.html#zipfile.BadZipFile "zipfile.BadZipFile"), for compatibility with older Python versions.
Deprecated since version 3.2.

_exception_ zipfile.LargeZipFile[¶](https://docs.python.org/3/library/zipfile.html#zipfile.LargeZipFile "Link to this definition")

The error raised when a ZIP file would require ZIP64 functionality but that has not been enabled.

_class_ zipfile.ZipFile

The class for reading and writing ZIP files. See section [ZipFile objects](https://docs.python.org/3/library/zipfile.html#zipfile-objects) for constructor details.

_class_ zipfile.Path

Class that implements a subset of the interface provided by [`pathlib.Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path"), including the full [`importlib.resources.abc.Traversable`](https://docs.python.org/3/library/importlib.resources.abc.html#importlib.resources.abc.Traversable "importlib.resources.abc.Traversable") interface.
Added in version 3.8.

_class_ zipfile.PyZipFile

Class for creating ZIP archives containing Python libraries.

_class_ zipfile.ZipInfo(_filename ='NoName'_, _date_time =(1980, 1, 1, 0, 0, 0)_)[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo "Link to this definition")

Class used to represent information about a member of an archive. Instances of this class are returned by the [`getinfo()`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.getinfo "zipfile.ZipFile.getinfo") and [`infolist()`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.infolist "zipfile.ZipFile.infolist") methods of [`ZipFile`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile "zipfile.ZipFile") objects. Most users of the `zipfile` module will not need to create these, but only use those created by this module. _filename_ should be the full name of the archive member, and _date_time_ should be a tuple containing six fields which describe the time of the last modification to the file; the fields are described in section [ZipInfo objects](https://docs.python.org/3/library/zipfile.html#zipinfo-objects).
Changed in version 3.13: A public `compress_level` attribute has been added to expose the formerly protected `_compresslevel`. The older protected name continues to work as a property for backwards compatibility.

_for_archive(_archive_)[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo._for_archive "Link to this definition")

Resolve the date_time, compression attributes, and external attributes to suitable defaults as used by [`ZipFile.writestr()`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.writestr "zipfile.ZipFile.writestr").
Returns self for chaining.
Added in version 3.14.

zipfile.is_zipfile(_filename_)[¶](https://docs.python.org/3/library/zipfile.html#zipfile.is_zipfile "Link to this definition")

Returns `True` if _filename_ is a valid ZIP file based on its magic number, otherwise returns `False`. _filename_ may be a file or file-like object too.
Changed in version 3.1: Support for file and file-like objects.

zipfile.ZIP_STORED[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZIP_STORED "Link to this definition")

The numeric constant for an uncompressed archive member.

zipfile.ZIP_DEFLATED[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZIP_DEFLATED "Link to this definition")

The numeric constant for the usual ZIP compression method. This requires the [`zlib`](https://docs.python.org/3/library/zlib.html#module-zlib "zlib: Low-level interface to compression and decompression routines compatible with gzip.") module.

zipfile.ZIP_BZIP2[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZIP_BZIP2 "Link to this definition")

The numeric constant for the BZIP2 compression method. This requires the [`bz2`](https://docs.python.org/3/library/bz2.html#module-bz2 "bz2: Interfaces for bzip2 compression and decompression.") module.
Added in version 3.3.

zipfile.ZIP_LZMA[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZIP_LZMA "Link to this definition")

The numeric constant for the LZMA compression method. This requires the [`lzma`](https://docs.python.org/3/library/lzma.html#module-lzma "lzma: A Python wrapper for the liblzma compression library.") module.
Added in version 3.3.

zipfile.ZIP_ZSTANDARD[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZIP_ZSTANDARD "Link to this definition")

The numeric constant for Zstandard compression. This requires the [`compression.zstd`](https://docs.python.org/3/library/compression.zstd.html#module-compression.zstd "compression.zstd: Low-level interface to compression and decompression routines in the zstd library.") module.
Note
In APPNOTE 6.3.7, the method ID `20` was assigned to Zstandard compression. This was changed in APPNOTE 6.3.8 to method ID `93` to avoid conflicts, with method ID `20` being deprecated. For compatibility, the `zipfile` module reads both method IDs but will only write data with method ID `93`.
Added in version 3.14.
Note
The ZIP file format specification has included support for bzip2 compression since 2001, for LZMA compression since 2006, and Zstandard compression since 2020. However, some tools (including older Python releases) do not support these compression methods, and may either refuse to process the ZIP file altogether, or fail to extract individual files.
See also
Documentation on the ZIP file format by Phil Katz, the creator of the format and algorithms used.
Information about the Info-ZIP project’s ZIP archive programs and development libraries.
