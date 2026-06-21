## ZipFile objects[¶](https://docs.python.org/3/library/zipfile.html#zipfile-objects "Link to this heading")

_class_ zipfile.ZipFile(_file_ , _mode ='r'_, _compression =ZIP_STORED_, _allowZip64 =True_, _compresslevel =None_, _*_ , _strict_timestamps =True_, _metadata_encoding =None_)[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile "Link to this definition")

Open a ZIP file, where _file_ can be a path to a file (a string), a file-like object or a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).
The _mode_ parameter should be `'r'` to read an existing file, `'w'` to truncate and write a new file, `'a'` to append to an existing file, or `'x'` to exclusively create and write a new file. If _mode_ is `'x'` and _file_ refers to an existing file, a [`FileExistsError`](https://docs.python.org/3/library/exceptions.html#FileExistsError "FileExistsError") will be raised. If _mode_ is `'a'` and _file_ refers to an existing ZIP file, then additional files are added to it. If _file_ does not refer to a ZIP file, then a new ZIP archive is appended to the file. This is meant for adding a ZIP archive to another file (such as `python.exe`). If _mode_ is `'a'` and the file does not exist at all, it is created. If _mode_ is `'r'` or `'a'`, the file should be seekable.
_compression_ is the ZIP compression method to use when writing the archive, and should be [`ZIP_STORED`](https://docs.python.org/3/library/zipfile.html#zipfile.ZIP_STORED "zipfile.ZIP_STORED"), [`ZIP_DEFLATED`](https://docs.python.org/3/library/zipfile.html#zipfile.ZIP_DEFLATED "zipfile.ZIP_DEFLATED"), [`ZIP_BZIP2`](https://docs.python.org/3/library/zipfile.html#zipfile.ZIP_BZIP2 "zipfile.ZIP_BZIP2"), [`ZIP_LZMA`](https://docs.python.org/3/library/zipfile.html#zipfile.ZIP_LZMA "zipfile.ZIP_LZMA"), or [`ZIP_ZSTANDARD`](https://docs.python.org/3/library/zipfile.html#zipfile.ZIP_ZSTANDARD "zipfile.ZIP_ZSTANDARD"); unrecognized values will cause [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError") to be raised. If `ZIP_DEFLATED`, `ZIP_BZIP2`, `ZIP_LZMA`, or `ZIP_ZSTANDARD` is specified but the corresponding module ([`zlib`](https://docs.python.org/3/library/zlib.html#module-zlib "zlib: Low-level interface to compression and decompression routines compatible with gzip."), [`bz2`](https://docs.python.org/3/library/bz2.html#module-bz2 "bz2: Interfaces for bzip2 compression and decompression."), [`lzma`](https://docs.python.org/3/library/lzma.html#module-lzma "lzma: A Python wrapper for the liblzma compression library."), or [`compression.zstd`](https://docs.python.org/3/library/compression.zstd.html#module-compression.zstd "compression.zstd: Low-level interface to compression and decompression routines in the zstd library.")) is not available, [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError") is raised. The default is `ZIP_STORED`.
If _allowZip64_ is `True` (the default) zipfile will create ZIP files that use the ZIP64 extensions when the zipfile is larger than 4 GiB. If it is `false` `zipfile` will raise an exception when the ZIP file would require ZIP64 extensions.
The _compresslevel_ parameter controls the compression level to use when writing files to the archive. When using [`ZIP_STORED`](https://docs.python.org/3/library/zipfile.html#zipfile.ZIP_STORED "zipfile.ZIP_STORED") or [`ZIP_LZMA`](https://docs.python.org/3/library/zipfile.html#zipfile.ZIP_LZMA "zipfile.ZIP_LZMA") it has no effect. When using [`ZIP_DEFLATED`](https://docs.python.org/3/library/zipfile.html#zipfile.ZIP_DEFLATED "zipfile.ZIP_DEFLATED") integers `0` through `9` are accepted (see [`zlib`](https://docs.python.org/3/library/zlib.html#zlib.compressobj "zlib.compressobj") for more information). When using [`ZIP_BZIP2`](https://docs.python.org/3/library/zipfile.html#zipfile.ZIP_BZIP2 "zipfile.ZIP_BZIP2") integers `1` through `9` are accepted (see [`bz2`](https://docs.python.org/3/library/bz2.html#bz2.BZ2File "bz2.BZ2File") for more information). When using [`ZIP_ZSTANDARD`](https://docs.python.org/3/library/zipfile.html#zipfile.ZIP_ZSTANDARD "zipfile.ZIP_ZSTANDARD") integers `-131072` through `22` are commonly accepted (see [`CompressionParameter.compression_level`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.compression_level "compression.zstd.CompressionParameter.compression_level") for more on retrieving valid values and their meaning).
The _strict_timestamps_ argument, when set to `False`, allows to zip files older than 1980-01-01 at the cost of setting the timestamp to 1980-01-01. Similar behavior occurs with files newer than 2107-12-31, the timestamp is also set to the limit.
When mode is `'r'`, _metadata_encoding_ may be set to the name of a codec, which will be used to decode metadata such as the names of members and ZIP comments.
If the file is created with mode `'w'`, `'x'` or `'a'` and then [`closed`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.close "zipfile.ZipFile.close") without adding any files to the archive, the appropriate ZIP structures for an empty archive will be written to the file.
ZipFile is also a context manager and therefore supports the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement. In the example, _myzip_ is closed after the `with` statement’s suite is finished—even if an exception occurs:
Copy```
with ZipFile('spam.zip', 'w') as myzip:
    myzip.write('eggs.txt')

```

Note
_metadata_encoding_ is an instance-wide setting for the ZipFile. It is not possible to set this on a per-member basis.
This attribute is a workaround for legacy implementations which produce archives with names in the current locale encoding or code page (mostly on Windows). According to the .ZIP standard, the encoding of metadata may be specified to be either IBM code page (default) or UTF-8 by a flag in the archive header. That flag takes precedence over _metadata_encoding_ , which is a Python-specific extension.
Changed in version 3.2: Added the ability to use `ZipFile` as a context manager.
Changed in version 3.3: Added support for [`bzip2`](https://docs.python.org/3/library/bz2.html#module-bz2 "bz2: Interfaces for bzip2 compression and decompression.") and [`lzma`](https://docs.python.org/3/library/lzma.html#module-lzma "lzma: A Python wrapper for the liblzma compression library.") compression.
Changed in version 3.4: ZIP64 extensions are enabled by default.
Changed in version 3.5: Added support for writing to unseekable streams. Added support for the `'x'` mode.
Changed in version 3.6: Previously, a plain [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError") was raised for unrecognized compression values.
Changed in version 3.6.2: The _file_ parameter accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).
Changed in version 3.7: Add the _compresslevel_ parameter.
Changed in version 3.8: The _strict_timestamps_ keyword-only parameter.
Changed in version 3.11: Added support for specifying member name encoding for reading metadata in the zipfile’s directory and file headers.

ZipFile.close()[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.close "Link to this definition")

Close the archive file. You must call `close()` before exiting your program or essential records will not be written.

ZipFile.getinfo(_name_)[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.getinfo "Link to this definition")

Return a [`ZipInfo`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo "zipfile.ZipInfo") object with information about the archive member _name_. Calling `getinfo()` for a name not currently contained in the archive will raise a [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "KeyError").

ZipFile.infolist()[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.infolist "Link to this definition")

Return a list containing a [`ZipInfo`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo "zipfile.ZipInfo") object for each member of the archive. The objects are in the same order as their entries in the actual ZIP file on disk if an existing archive was opened.

ZipFile.namelist()[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.namelist "Link to this definition")

Return a list of archive members by name.

ZipFile.open(_name_ , _mode ='r'_, _pwd =None_, _*_ , _force_zip64 =False_)[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.open "Link to this definition")

Access a member of the archive as a binary file-like object. _name_ can be either the name of a file within the archive or a [`ZipInfo`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo "zipfile.ZipInfo") object. The _mode_ parameter, if included, must be `'r'` (the default) or `'w'`. _pwd_ is the password used to decrypt encrypted ZIP files as a [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") object.
`open()` is also a context manager and therefore supports the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement:
Copy```
with ZipFile('spam.zip') as myzip:
    with myzip.open('eggs.txt') as myfile:
        print(myfile.read())

```

With _mode_ `'r'` the file-like object (`ZipExtFile`) is read-only and provides the following methods: [`read()`](https://docs.python.org/3/library/io.html#io.BufferedIOBase.read "io.BufferedIOBase.read"), [`readline()`](https://docs.python.org/3/library/io.html#io.IOBase.readline "io.IOBase.readline"), [`readlines()`](https://docs.python.org/3/library/io.html#io.IOBase.readlines "io.IOBase.readlines"), [`seek()`](https://docs.python.org/3/library/io.html#io.IOBase.seek "io.IOBase.seek"), [`tell()`](https://docs.python.org/3/library/io.html#io.IOBase.tell "io.IOBase.tell"), [`__iter__()`](https://docs.python.org/3/library/stdtypes.html#container.__iter__ "container.__iter__"), [`__next__()`](https://docs.python.org/3/library/stdtypes.html#iterator.__next__ "iterator.__next__"). These objects can operate independently of the ZipFile.
With `mode='w'`, a writable file handle is returned, which supports the [`write()`](https://docs.python.org/3/library/io.html#io.BufferedIOBase.write "io.BufferedIOBase.write") method. While a writable file handle is open, attempting to read or write other files in the ZIP file will raise a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError").
In both cases the file-like object has also attributes `name`, which is equivalent to the name of a file within the archive, and `mode`, which is `'rb'` or `'wb'` depending on the input mode.
When writing a file, if the file size is not known in advance but may exceed 2 GiB, pass `force_zip64=True` to ensure that the header format is capable of supporting large files. If the file size is known in advance, construct a [`ZipInfo`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo "zipfile.ZipInfo") object with [`file_size`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo.file_size "zipfile.ZipInfo.file_size") set, and use that as the _name_ parameter.
Note
The `open()`, [`read()`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.read "zipfile.ZipFile.read") and [`extract()`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.extract "zipfile.ZipFile.extract") methods can take a filename or a [`ZipInfo`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo "zipfile.ZipInfo") object. You will appreciate this when trying to read a ZIP file that contains members with duplicate names.
Changed in version 3.6: Removed support of `mode='U'`. Use [`io.TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper") for reading compressed text files in [universal newlines](https://docs.python.org/3/glossary.html#term-universal-newlines) mode.
Changed in version 3.6: `ZipFile.open()` can now be used to write files into the archive with the `mode='w'` option.
Changed in version 3.6: Calling `open()` on a closed ZipFile will raise a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError"). Previously, a [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError") was raised.
Changed in version 3.13: Added attributes `name` and `mode` for the writeable file-like object. The value of the `mode` attribute for the readable file-like object was changed from `'r'` to `'rb'`.

ZipFile.extract(_member_ , _path =None_, _pwd =None_)[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.extract "Link to this definition")

Extract a member from the archive to the current working directory; _member_ must be its full name or a [`ZipInfo`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo "zipfile.ZipInfo") object. Its file information is extracted as accurately as possible. _path_ specifies a different directory to extract to. _member_ can be a filename or a `ZipInfo` object. _pwd_ is the password used for encrypted files as a [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") object.
Returns the normalized path created (a directory or new file).
Note
If a member filename is an absolute path, a drive/UNC sharepoint and leading (back)slashes will be stripped, e.g.: `///foo/bar` becomes `foo/bar` on Unix, and `C:\foo\bar` becomes `foo\bar` on Windows. And all `".."` components in a member filename will be removed, e.g.: `../../foo../../ba..r` becomes `foo../ba..r`. On Windows illegal characters (`:`, `<`, `>`, `|`, `"`, `?`, and `*`) replaced by underscore (`_`).
Changed in version 3.6: Calling `extract()` on a closed ZipFile will raise a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError"). Previously, a [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError") was raised.
Changed in version 3.6.2: The _path_ parameter accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).

ZipFile.extractall(_path =None_, _members =None_, _pwd =None_)[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.extractall "Link to this definition")

Extract all members from the archive to the current working directory. _path_ specifies a different directory to extract to. _members_ is optional and must be a subset of the list returned by [`namelist()`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.namelist "zipfile.ZipFile.namelist"). _pwd_ is the password used for encrypted files as a [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") object.
Warning
Never extract archives from untrusted sources without prior inspection. It is possible that files are created outside of _path_ , e.g. members that have absolute filenames starting with `"/"` or filenames with two dots `".."`. This module attempts to prevent that. See [`extract()`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.extract "zipfile.ZipFile.extract") note.
Changed in version 3.6: Calling `extractall()` on a closed ZipFile will raise a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError"). Previously, a [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError") was raised.
Changed in version 3.6.2: The _path_ parameter accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).

ZipFile.printdir()[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.printdir "Link to this definition")

Print a table of contents for the archive to `sys.stdout`.

ZipFile.setpassword(_pwd_)[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.setpassword "Link to this definition")

Set _pwd_ (a [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") object) as default password to extract encrypted files.

ZipFile.read(_name_ , _pwd =None_)[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.read "Link to this definition")

Return the bytes of the file _name_ in the archive. _name_ is the name of the file in the archive, or a [`ZipInfo`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo "zipfile.ZipInfo") object. The archive must be open for read or append. _pwd_ is the password used for encrypted files as a [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") object and, if specified, overrides the default password set with [`setpassword()`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.setpassword "zipfile.ZipFile.setpassword"). Calling `read()` on a ZipFile that uses a compression method other than [`ZIP_STORED`](https://docs.python.org/3/library/zipfile.html#zipfile.ZIP_STORED "zipfile.ZIP_STORED"), [`ZIP_DEFLATED`](https://docs.python.org/3/library/zipfile.html#zipfile.ZIP_DEFLATED "zipfile.ZIP_DEFLATED"), [`ZIP_BZIP2`](https://docs.python.org/3/library/zipfile.html#zipfile.ZIP_BZIP2 "zipfile.ZIP_BZIP2"), [`ZIP_LZMA`](https://docs.python.org/3/library/zipfile.html#zipfile.ZIP_LZMA "zipfile.ZIP_LZMA"), or [`ZIP_ZSTANDARD`](https://docs.python.org/3/library/zipfile.html#zipfile.ZIP_ZSTANDARD "zipfile.ZIP_ZSTANDARD") will raise a [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError"). An error will also be raised if the corresponding compression module is not available.
Changed in version 3.6: Calling `read()` on a closed ZipFile will raise a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError"). Previously, a [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError") was raised.

ZipFile.testzip()[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.testzip "Link to this definition")

Read all the files in the archive and check their CRC’s and file headers. Return the name of the first bad file, or else return `None`.
Changed in version 3.6: Calling `testzip()` on a closed ZipFile will raise a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError"). Previously, a [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError") was raised.

ZipFile.write(_filename_ , _arcname =None_, _compress_type =None_, _compresslevel =None_)[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.write "Link to this definition")

Write the file named _filename_ to the archive, giving it the archive name _arcname_ (by default, this will be the same as _filename_ , but without a drive letter and with leading path separators removed). If given, _compress_type_ overrides the value given for the _compression_ parameter to the constructor for the new entry. Similarly, _compresslevel_ will override the constructor if given. The archive must be open with mode `'w'`, `'x'` or `'a'`.
Note
The ZIP file standard historically did not specify a metadata encoding, but strongly recommended CP437 (the original IBM PC encoding) for interoperability. Recent versions allow use of UTF-8 (only). In this module, UTF-8 will automatically be used to write the member names if they contain any non-ASCII characters. It is not possible to write member names in any encoding other than ASCII or UTF-8.
Note
Archive names should be relative to the archive root, that is, they should not start with a path separator.
Note
If `arcname` (or `filename`, if `arcname` is not given) contains a null byte, the name of the file in the archive will be truncated at the null byte.
Note
A leading slash in the filename may lead to the archive being impossible to open in some zip programs on Windows systems.
Changed in version 3.6: Calling `write()` on a ZipFile created with mode `'r'` or a closed ZipFile will raise a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError"). Previously, a [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError") was raised.

ZipFile.writestr(_zinfo_or_arcname_ , _data_ , _compress_type =None_, _compresslevel =None_)[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.writestr "Link to this definition")

Write a file into the archive. The contents is _data_ , which may be either a [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") or a [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") instance; if it is a `str`, it is encoded as UTF-8 first. _zinfo_or_arcname_ is either the file name it will be given in the archive, or a [`ZipInfo`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo "zipfile.ZipInfo") instance. If it’s an instance, at least the filename, date, and time must be given. If it’s a name, the date and time is set to the current date and time. The archive must be opened with mode `'w'`, `'x'` or `'a'`.
If given, _compress_type_ overrides the value given for the _compression_ parameter to the constructor for the new entry, or in the _zinfo_or_arcname_ (if that is a [`ZipInfo`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo "zipfile.ZipInfo") instance). Similarly, _compresslevel_ will override the constructor if given.
Note
When passing a [`ZipInfo`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo "zipfile.ZipInfo") instance as the _zinfo_or_arcname_ parameter, the compression method used will be that specified in the _compress_type_ member of the given `ZipInfo` instance. By default, the `ZipInfo` constructor sets this member to [`ZIP_STORED`](https://docs.python.org/3/library/zipfile.html#zipfile.ZIP_STORED "zipfile.ZIP_STORED").
Changed in version 3.2: The _compress_type_ argument.
Changed in version 3.6: Calling `writestr()` on a ZipFile created with mode `'r'` or a closed ZipFile will raise a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError"). Previously, a [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError") was raised.

ZipFile.mkdir(_zinfo_or_directory_ , _mode =511_)[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.mkdir "Link to this definition")

Create a directory inside the archive. If _zinfo_or_directory_ is a string, a directory is created inside the archive with the mode that is specified in the _mode_ argument. If, however, _zinfo_or_directory_ is a [`ZipInfo`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo "zipfile.ZipInfo") instance then the _mode_ argument is ignored.
The archive must be opened with mode `'w'`, `'x'` or `'a'`.
Added in version 3.11.
The following data attributes are also available:

ZipFile.filename[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.filename "Link to this definition")

Name of the ZIP file.

ZipFile.debug[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.debug "Link to this definition")

The level of debug output to use. This may be set from `0` (the default, no output) to `3` (the most output). Debugging information is written to `sys.stdout`.

ZipFile.comment[¶](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.comment "Link to this definition")

The comment associated with the ZIP file as a [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") object. If assigning a comment to a [`ZipFile`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile "zipfile.ZipFile") instance created with mode `'w'`, `'x'` or `'a'`, it should be no longer than 65535 bytes. Comments longer than this will be truncated.
