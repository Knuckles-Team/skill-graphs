## TarFile Objects[¶](https://docs.python.org/3/library/tarfile.html#tarfile-objects "Link to this heading")
The [`TarFile`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile "tarfile.TarFile") object provides an interface to a tar archive. A tar archive is a sequence of blocks. An archive member (a stored file) is made up of a header block followed by data blocks. It is possible to store a file in a tar archive several times. Each archive member is represented by a [`TarInfo`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "tarfile.TarInfo") object, see [TarInfo Objects](https://docs.python.org/3/library/tarfile.html#tarinfo-objects) for details.
A [`TarFile`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile "tarfile.TarFile") object can be used as a context manager in a [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement. It will automatically be closed when the block is completed. Please note that in the event of an exception an archive opened for writing will not be finalized; only the internally used file object will be closed. See the [Examples](https://docs.python.org/3/library/tarfile.html#tar-examples) section for a use case.
Added in version 3.2: Added support for the context management protocol.

_class_ tarfile.TarFile(_name =None_, _mode ='r'_, _fileobj =None_, _format =DEFAULT_FORMAT_, _tarinfo =TarInfo_, _dereference =False_, _ignore_zeros =False_, _encoding =ENCODING_, _errors ='surrogateescape'_, _pax_headers =None_, _debug =0_, _errorlevel =1_, _stream =False_)[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile "Link to this definition")

All following arguments are optional and can be accessed as instance attributes as well.
_name_ is the pathname of the archive. _name_ may be a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object). It can be omitted if _fileobj_ is given. In this case, the file object’s `name` attribute is used if it exists.
_mode_ is either `'r'` to read from an existing archive, `'a'` to append data to an existing file, `'w'` to create a new file overwriting an existing one, or `'x'` to create a new file only if it does not already exist.
If _fileobj_ is given, it is used for reading or writing data. If it can be determined, _mode_ is overridden by _fileobj_ ’s mode. _fileobj_ will be used from position 0.
Note
_fileobj_ is not closed, when `TarFile` is closed.
_format_ controls the archive format for writing. It must be one of the constants [`USTAR_FORMAT`](https://docs.python.org/3/library/tarfile.html#tarfile.USTAR_FORMAT "tarfile.USTAR_FORMAT"), [`GNU_FORMAT`](https://docs.python.org/3/library/tarfile.html#tarfile.GNU_FORMAT "tarfile.GNU_FORMAT") or [`PAX_FORMAT`](https://docs.python.org/3/library/tarfile.html#tarfile.PAX_FORMAT "tarfile.PAX_FORMAT") that are defined at module level. When reading, format will be automatically detected, even if different formats are present in a single archive.
The _tarinfo_ argument can be used to replace the default [`TarInfo`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "tarfile.TarInfo") class with a different one.
If _dereference_ is [`False`](https://docs.python.org/3/library/constants.html#False "False"), add symbolic and hard links to the archive. If it is [`True`](https://docs.python.org/3/library/constants.html#True "True"), add the content of the target files to the archive. This has no effect on systems that do not support symbolic links.
If _ignore_zeros_ is [`False`](https://docs.python.org/3/library/constants.html#False "False"), treat an empty block as the end of the archive. If it is [`True`](https://docs.python.org/3/library/constants.html#True "True"), skip empty (and invalid) blocks and try to get as many members as possible. This is only useful for reading concatenated or damaged archives.
_debug_ can be set from `0` (no debug messages) up to `3` (all debug messages). The messages are written to `sys.stderr`.
_errorlevel_ controls how extraction errors are handled, see [`the corresponding attribute`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.errorlevel "tarfile.TarFile.errorlevel").
The _encoding_ and _errors_ arguments define the character encoding to be used for reading or writing the archive and how conversion errors are going to be handled. The default settings will work for most users. See section [Unicode issues](https://docs.python.org/3/library/tarfile.html#tar-unicode) for in-depth information.
The _pax_headers_ argument is an optional dictionary of strings which will be added as a pax global header if _format_ is [`PAX_FORMAT`](https://docs.python.org/3/library/tarfile.html#tarfile.PAX_FORMAT "tarfile.PAX_FORMAT").
If _stream_ is set to [`True`](https://docs.python.org/3/library/constants.html#True "True") then while reading the archive info about files in the archive are not cached, saving memory.
Changed in version 3.2: Use `'surrogateescape'` as the default for the _errors_ argument.
Changed in version 3.5: The `'x'` (exclusive creation) mode was added.
Changed in version 3.6: The _name_ parameter accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).
Changed in version 3.13: Add the _stream_ parameter.

_classmethod_ TarFile.open(_..._)[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.open "Link to this definition")

Alternative constructor. The [`tarfile.open()`](https://docs.python.org/3/library/tarfile.html#tarfile.open "tarfile.open") function is actually a shortcut to this classmethod.

TarFile.getmember(_name_)[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.getmember "Link to this definition")

Return a [`TarInfo`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "tarfile.TarInfo") object for member _name_. If _name_ can not be found in the archive, [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "KeyError") is raised.
Note
If a member occurs more than once in the archive, its last occurrence is assumed to be the most up-to-date version.

TarFile.getmembers()[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.getmembers "Link to this definition")

Return the members of the archive as a list of [`TarInfo`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "tarfile.TarInfo") objects. The list has the same order as the members in the archive.

TarFile.getnames()[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.getnames "Link to this definition")

Return the members as a list of their names. It has the same order as the list returned by [`getmembers()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.getmembers "tarfile.TarFile.getmembers").

TarFile.list(_verbose =True_, _*_ , _members =None_)[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.list "Link to this definition")

Print a table of contents to `sys.stdout`. If _verbose_ is [`False`](https://docs.python.org/3/library/constants.html#False "False"), only the names of the members are printed. If it is [`True`](https://docs.python.org/3/library/constants.html#True "True"), output similar to that of **ls -l** is produced. If optional _members_ is given, it must be a subset of the list returned by [`getmembers()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.getmembers "tarfile.TarFile.getmembers").
Changed in version 3.5: Added the _members_ parameter.

TarFile.next()[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.next "Link to this definition")

Return the next member of the archive as a [`TarInfo`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "tarfile.TarInfo") object, when [`TarFile`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile "tarfile.TarFile") is opened for reading. Return [`None`](https://docs.python.org/3/library/constants.html#None "None") if there is no more available.

TarFile.extractall(_path ='.'_, _members =None_, _*_ , _numeric_owner =False_, _filter =None_)[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extractall "Link to this definition")

Extract all members from the archive to the current working directory or directory _path_. If optional _members_ is given, it must be a subset of the list returned by [`getmembers()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.getmembers "tarfile.TarFile.getmembers"). Directory information like owner, modification time and permissions are set after all members have been extracted. This is done to work around two problems: A directory’s modification time is reset each time a file is created in it. And, if a directory’s permissions do not allow writing, extracting files to it will fail.
If _numeric_owner_ is [`True`](https://docs.python.org/3/library/constants.html#True "True"), the uid and gid numbers from the tarfile are used to set the owner/group for the extracted files. Otherwise, the named values from the tarfile are used.
The _filter_ argument specifies how `members` are modified or rejected before extraction. See [Extraction filters](https://docs.python.org/3/library/tarfile.html#tarfile-extraction-filter) for details. It is recommended to set this explicitly only if specific _tar_ features are required, or as `filter='data'` to support Python versions with a less secure default (3.13 and lower).
Warning
Never extract archives from untrusted sources without prior inspection.
Since Python 3.14, the default ([`data`](https://docs.python.org/3/library/tarfile.html#tarfile.data_filter "tarfile.data_filter")) will prevent the most dangerous security issues. However, it will not prevent _all_ unintended or insecure behavior. Read the [Extraction filters](https://docs.python.org/3/library/tarfile.html#tarfile-extraction-filter) section for details.
Changed in version 3.5: Added the _numeric_owner_ parameter.
Changed in version 3.6: The _path_ parameter accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).
Changed in version 3.12: Added the _filter_ parameter.
Changed in version 3.14: The _filter_ parameter now defaults to `'data'`.

TarFile.extract(_member_ , _path =''_, _set_attrs =True_, _*_ , _numeric_owner =False_, _filter =None_)[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extract "Link to this definition")

Extract a member from the archive to the current working directory, using its full name. Its file information is extracted as accurately as possible. _member_ may be a filename or a [`TarInfo`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "tarfile.TarInfo") object. You can specify a different directory using _path_. _path_ may be a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object). File attributes (owner, mtime, mode) are set unless _set_attrs_ is false.
The _numeric_owner_ and _filter_ arguments are the same as for [`extractall()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extractall "tarfile.TarFile.extractall").
Note
The `extract()` method does not take care of several extraction issues. In most cases you should consider using the [`extractall()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extractall "tarfile.TarFile.extractall") method.
Warning
Never extract archives from untrusted sources without prior inspection. See the warning for [`extractall()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extractall "tarfile.TarFile.extractall") for details.
Changed in version 3.2: Added the _set_attrs_ parameter.
Changed in version 3.5: Added the _numeric_owner_ parameter.
Changed in version 3.6: The _path_ parameter accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).
Changed in version 3.12: Added the _filter_ parameter.

TarFile.extractfile(_member_)[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extractfile "Link to this definition")

Extract a member from the archive as a file object. _member_ may be a filename or a [`TarInfo`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "tarfile.TarInfo") object. If _member_ is a regular file or a link, an [`io.BufferedReader`](https://docs.python.org/3/library/io.html#io.BufferedReader "io.BufferedReader") object is returned. For all other existing members, [`None`](https://docs.python.org/3/library/constants.html#None "None") is returned. If _member_ does not appear in the archive, [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "KeyError") is raised.
Changed in version 3.3: Return an [`io.BufferedReader`](https://docs.python.org/3/library/io.html#io.BufferedReader "io.BufferedReader") object.
Changed in version 3.13: The returned [`io.BufferedReader`](https://docs.python.org/3/library/io.html#io.BufferedReader "io.BufferedReader") object has the `mode` attribute which is always equal to `'rb'`.

TarFile.errorlevel _:[ int](https://docs.python.org/3/library/functions.html#int "int")_[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.errorlevel "Link to this definition")

If _errorlevel_ is `0`, errors are ignored when using [`TarFile.extract()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extract "tarfile.TarFile.extract") and [`TarFile.extractall()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extractall "tarfile.TarFile.extractall"). Nevertheless, they appear as error messages in the debug output when _debug_ is greater than 0. If `1` (the default), all _fatal_ errors are raised as [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") or [`FilterError`](https://docs.python.org/3/library/tarfile.html#tarfile.FilterError "tarfile.FilterError") exceptions. If `2`, all _non-fatal_ errors are raised as [`TarError`](https://docs.python.org/3/library/tarfile.html#tarfile.TarError "tarfile.TarError") exceptions as well.
Some exceptions, e.g. ones caused by wrong argument types or data corruption, are always raised.
Custom [extraction filters](https://docs.python.org/3/library/tarfile.html#tarfile-extraction-filter) should raise [`FilterError`](https://docs.python.org/3/library/tarfile.html#tarfile.FilterError "tarfile.FilterError") for _fatal_ errors and [`ExtractError`](https://docs.python.org/3/library/tarfile.html#tarfile.ExtractError "tarfile.ExtractError") for _non-fatal_ ones.
Note that when an exception is raised, the archive may be partially extracted. It is the user’s responsibility to clean up.

TarFile.extraction_filter[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extraction_filter "Link to this definition")

Added in version 3.12.
The [extraction filter](https://docs.python.org/3/library/tarfile.html#tarfile-extraction-filter) used as a default for the _filter_ argument of [`extract()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extract "tarfile.TarFile.extract") and [`extractall()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extractall "tarfile.TarFile.extractall").
The attribute may be `None` or a callable. String names are not allowed for this attribute, unlike the _filter_ argument to [`extract()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extract "tarfile.TarFile.extract").
If `extraction_filter` is `None` (the default), extraction methods will use the [`data`](https://docs.python.org/3/library/tarfile.html#tarfile.data_filter "tarfile.data_filter") filter by default.
The attribute may be set on instances or overridden in subclasses. It also is possible to set it on the `TarFile` class itself to set a global default, although, since it affects all uses of _tarfile_ , it is best practice to only do so in top-level applications or [`site configuration`](https://docs.python.org/3/library/site.html#module-site "site: Module responsible for site-specific configuration."). To set a global default this way, a filter function needs to be wrapped in [`staticmethod()`](https://docs.python.org/3/library/functions.html#staticmethod "staticmethod") to prevent injection of a `self` argument.
Changed in version 3.14: The default filter is set to [`data`](https://docs.python.org/3/library/tarfile.html#tarfile.data_filter "tarfile.data_filter"), which disallows some dangerous features such as links to absolute paths or paths outside of the destination. Previously, the default was equivalent to [`fully_trusted`](https://docs.python.org/3/library/tarfile.html#tarfile.fully_trusted_filter "tarfile.fully_trusted_filter").

TarFile.add(_name_ , _arcname =None_, _recursive =True_, _*_ , _filter =None_)[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.add "Link to this definition")

Add the file _name_ to the archive. _name_ may be any type of file (directory, fifo, symbolic link, etc.). If given, _arcname_ specifies an alternative name for the file in the archive. Directories are added recursively by default. This can be avoided by setting _recursive_ to [`False`](https://docs.python.org/3/library/constants.html#False "False"). Recursion adds entries in sorted order. If _filter_ is given, it should be a function that takes a [`TarInfo`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "tarfile.TarInfo") object argument and returns the changed `TarInfo` object. If it instead returns [`None`](https://docs.python.org/3/library/constants.html#None "None") the `TarInfo` object will be excluded from the archive. See [Examples](https://docs.python.org/3/library/tarfile.html#tar-examples) for an example.
Changed in version 3.2: Added the _filter_ parameter.
Changed in version 3.7: Recursion adds entries in sorted order.

TarFile.addfile(_tarinfo_ , _fileobj =None_)[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.addfile "Link to this definition")

Add the [`TarInfo`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "tarfile.TarInfo") object _tarinfo_ to the archive. If _tarinfo_ represents a non zero-size regular file, the _fileobj_ argument should be a [binary file](https://docs.python.org/3/glossary.html#term-binary-file), and `tarinfo.size` bytes are read from it and added to the archive. You can create `TarInfo` objects directly, or by using [`gettarinfo()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.gettarinfo "tarfile.TarFile.gettarinfo").
Changed in version 3.13: _fileobj_ must be given for non-zero-sized regular files.

TarFile.gettarinfo(_name =None_, _arcname =None_, _fileobj =None_)[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.gettarinfo "Link to this definition")

Create a [`TarInfo`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "tarfile.TarInfo") object from the result of [`os.stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat") or equivalent on an existing file. The file is either named by _name_ , or specified as a [file object](https://docs.python.org/3/glossary.html#term-file-object) _fileobj_ with a file descriptor. _name_ may be a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object). If given, _arcname_ specifies an alternative name for the file in the archive, otherwise, the name is taken from _fileobj_ ’s [`name`](https://docs.python.org/3/library/io.html#io.FileIO.name "io.FileIO.name") attribute, or the _name_ argument. The name should be a text string.
You can modify some of the [`TarInfo`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "tarfile.TarInfo")’s attributes before you add it using [`addfile()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.addfile "tarfile.TarFile.addfile"). If the file object is not an ordinary file object positioned at the beginning of the file, attributes such as [`size`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.size "tarfile.TarInfo.size") may need modifying. This is the case for objects such as [`GzipFile`](https://docs.python.org/3/library/gzip.html#gzip.GzipFile "gzip.GzipFile"). The [`name`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.name "tarfile.TarInfo.name") may also be modified, in which case _arcname_ could be a dummy string.
Changed in version 3.6: The _name_ parameter accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).

TarFile.close()[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.close "Link to this definition")

Close the [`TarFile`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile "tarfile.TarFile"). In write mode, two finishing zero blocks are appended to the archive.

TarFile.pax_headers _:[ dict](https://docs.python.org/3/library/stdtypes.html#dict "dict")_[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.pax_headers "Link to this definition")

A dictionary containing key-value pairs of pax global headers.
