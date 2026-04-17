## TarInfo Objects[¶](https://docs.python.org/3/library/tarfile.html#tarinfo-objects "Link to this heading")
A [`TarInfo`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "tarfile.TarInfo") object represents one member in a [`TarFile`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile "tarfile.TarFile"). Aside from storing all required attributes of a file (like file type, size, time, permissions, owner etc.), it provides some useful methods to determine its type. It does _not_ contain the file’s data itself.
[`TarInfo`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "tarfile.TarInfo") objects are returned by [`TarFile`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile "tarfile.TarFile")’s methods [`getmember()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.getmember "tarfile.TarFile.getmember"), [`getmembers()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.getmembers "tarfile.TarFile.getmembers") and [`gettarinfo()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.gettarinfo "tarfile.TarFile.gettarinfo").
Modifying the objects returned by [`getmember()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.getmember "tarfile.TarFile.getmember") or [`getmembers()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.getmembers "tarfile.TarFile.getmembers") will affect all subsequent operations on the archive. For cases where this is unwanted, you can use [`copy.copy()`](https://docs.python.org/3/library/copy.html#module-copy "copy: Shallow and deep copy operations.") or call the [`replace()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.replace "tarfile.TarInfo.replace") method to create a modified copy in one step.
Several attributes can be set to `None` to indicate that a piece of metadata is unused or unknown. Different [`TarInfo`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "tarfile.TarInfo") methods handle `None` differently:
  * The [`extract()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extract "tarfile.TarFile.extract") or [`extractall()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extractall "tarfile.TarFile.extractall") methods will ignore the corresponding metadata, leaving it set to a default.
  * [`addfile()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.addfile "tarfile.TarFile.addfile") will fail.
  * [`list()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.list "tarfile.TarFile.list") will print a placeholder string.



_class_ tarfile.TarInfo(_name =''_)[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "Link to this definition")

Create a `TarInfo` object.

_classmethod_ TarInfo.frombuf(_buf_ , _encoding_ , _errors_)[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.frombuf "Link to this definition")

Create and return a [`TarInfo`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "tarfile.TarInfo") object from string buffer _buf_.
Raises [`HeaderError`](https://docs.python.org/3/library/tarfile.html#tarfile.HeaderError "tarfile.HeaderError") if the buffer is invalid.

_classmethod_ TarInfo.fromtarfile(_tarfile_)[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.fromtarfile "Link to this definition")

Read the next member from the [`TarFile`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile "tarfile.TarFile") object _tarfile_ and return it as a [`TarInfo`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "tarfile.TarInfo") object.

TarInfo.tobuf(_format =DEFAULT_FORMAT_, _encoding =ENCODING_, _errors ='surrogateescape'_)[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.tobuf "Link to this definition")

Create a string buffer from a [`TarInfo`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "tarfile.TarInfo") object. For information on the arguments see the constructor of the [`TarFile`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile "tarfile.TarFile") class.
Changed in version 3.2: Use `'surrogateescape'` as the default for the _errors_ argument.
A `TarInfo` object has the following public data attributes:

TarInfo.name _:[ str](https://docs.python.org/3/library/stdtypes.html#str "str")_[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.name "Link to this definition")

Name of the archive member.

TarInfo.size _:[ int](https://docs.python.org/3/library/functions.html#int "int")_[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.size "Link to this definition")

Size in bytes.

TarInfo.mtime _:[ int](https://docs.python.org/3/library/functions.html#int "int")|[float](https://docs.python.org/3/library/functions.html#float "float")_[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.mtime "Link to this definition")

Time of last modification in seconds since the [epoch](https://docs.python.org/3/library/time.html#epoch), as in [`os.stat_result.st_mtime`](https://docs.python.org/3/library/os.html#os.stat_result.st_mtime "os.stat_result.st_mtime").
Changed in version 3.12: Can be set to `None` for [`extract()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extract "tarfile.TarFile.extract") and [`extractall()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extractall "tarfile.TarFile.extractall"), causing extraction to skip applying this attribute.

TarInfo.mode _:[ int](https://docs.python.org/3/library/functions.html#int "int")_[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.mode "Link to this definition")

Permission bits, as for [`os.chmod()`](https://docs.python.org/3/library/os.html#os.chmod "os.chmod").
Changed in version 3.12: Can be set to `None` for [`extract()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extract "tarfile.TarFile.extract") and [`extractall()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extractall "tarfile.TarFile.extractall"), causing extraction to skip applying this attribute.

TarInfo.type[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.type "Link to this definition")

File type. _type_ is usually one of these constants: [`REGTYPE`](https://docs.python.org/3/library/tarfile.html#tarfile.REGTYPE "tarfile.REGTYPE"), [`AREGTYPE`](https://docs.python.org/3/library/tarfile.html#tarfile.AREGTYPE "tarfile.AREGTYPE"), [`LNKTYPE`](https://docs.python.org/3/library/tarfile.html#tarfile.LNKTYPE "tarfile.LNKTYPE"), [`SYMTYPE`](https://docs.python.org/3/library/tarfile.html#tarfile.SYMTYPE "tarfile.SYMTYPE"), [`DIRTYPE`](https://docs.python.org/3/library/tarfile.html#tarfile.DIRTYPE "tarfile.DIRTYPE"), [`FIFOTYPE`](https://docs.python.org/3/library/tarfile.html#tarfile.FIFOTYPE "tarfile.FIFOTYPE"), [`CONTTYPE`](https://docs.python.org/3/library/tarfile.html#tarfile.CONTTYPE "tarfile.CONTTYPE"), [`CHRTYPE`](https://docs.python.org/3/library/tarfile.html#tarfile.CHRTYPE "tarfile.CHRTYPE"), [`BLKTYPE`](https://docs.python.org/3/library/tarfile.html#tarfile.BLKTYPE "tarfile.BLKTYPE"), [`GNUTYPE_SPARSE`](https://docs.python.org/3/library/tarfile.html#tarfile.GNUTYPE_SPARSE "tarfile.GNUTYPE_SPARSE"). To determine the type of a [`TarInfo`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "tarfile.TarInfo") object more conveniently, use the `is*()` methods below.

TarInfo.linkname _:[ str](https://docs.python.org/3/library/stdtypes.html#str "str")_[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.linkname "Link to this definition")

Name of the target file name, which is only present in [`TarInfo`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "tarfile.TarInfo") objects of type [`LNKTYPE`](https://docs.python.org/3/library/tarfile.html#tarfile.LNKTYPE "tarfile.LNKTYPE") and [`SYMTYPE`](https://docs.python.org/3/library/tarfile.html#tarfile.SYMTYPE "tarfile.SYMTYPE").
For symbolic links (`SYMTYPE`), the _linkname_ is relative to the directory that contains the link. For hard links (`LNKTYPE`), the _linkname_ is relative to the root of the archive.

TarInfo.uid _:[ int](https://docs.python.org/3/library/functions.html#int "int")_[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.uid "Link to this definition")

User ID of the user who originally stored this member.
Changed in version 3.12: Can be set to `None` for [`extract()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extract "tarfile.TarFile.extract") and [`extractall()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extractall "tarfile.TarFile.extractall"), causing extraction to skip applying this attribute.

TarInfo.gid _:[ int](https://docs.python.org/3/library/functions.html#int "int")_[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.gid "Link to this definition")

Group ID of the user who originally stored this member.
Changed in version 3.12: Can be set to `None` for [`extract()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extract "tarfile.TarFile.extract") and [`extractall()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extractall "tarfile.TarFile.extractall"), causing extraction to skip applying this attribute.

TarInfo.uname _:[ str](https://docs.python.org/3/library/stdtypes.html#str "str")_[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.uname "Link to this definition")

User name.
Changed in version 3.12: Can be set to `None` for [`extract()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extract "tarfile.TarFile.extract") and [`extractall()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extractall "tarfile.TarFile.extractall"), causing extraction to skip applying this attribute.

TarInfo.gname _:[ str](https://docs.python.org/3/library/stdtypes.html#str "str")_[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.gname "Link to this definition")

Group name.
Changed in version 3.12: Can be set to `None` for [`extract()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extract "tarfile.TarFile.extract") and [`extractall()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extractall "tarfile.TarFile.extractall"), causing extraction to skip applying this attribute.

TarInfo.chksum _:[ int](https://docs.python.org/3/library/functions.html#int "int")_[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.chksum "Link to this definition")

Header checksum.

TarInfo.devmajor _:[ int](https://docs.python.org/3/library/functions.html#int "int")_[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.devmajor "Link to this definition")

Device major number.

TarInfo.devminor _:[ int](https://docs.python.org/3/library/functions.html#int "int")_[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.devminor "Link to this definition")

Device minor number.

TarInfo.offset _:[ int](https://docs.python.org/3/library/functions.html#int "int")_[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.offset "Link to this definition")

The tar header starts here.

TarInfo.offset_data _:[ int](https://docs.python.org/3/library/functions.html#int "int")_[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.offset_data "Link to this definition")

The file’s data starts here.

TarInfo.sparse[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.sparse "Link to this definition")

Sparse member information.

TarInfo.pax_headers _:[ dict](https://docs.python.org/3/library/stdtypes.html#dict "dict")_[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.pax_headers "Link to this definition")

A dictionary containing key-value pairs of an associated pax extended header.

TarInfo.replace(_name =..._, _mtime =..._, _mode =..._, _linkname =..._, _uid =..._, _gid =..._, _uname =..._, _gname =..._, _deep =True_)[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.replace "Link to this definition")

Added in version 3.12.
Return a _new_ copy of the `TarInfo` object with the given attributes changed. For example, to return a `TarInfo` with the group name set to `'staff'`, use:
Copy```
new_tarinfo = old_tarinfo.replace(gname='staff')

```

By default, a deep copy is made. If _deep_ is false, the copy is shallow, i.e. `pax_headers` and any custom attributes are shared with the original `TarInfo` object.
A [`TarInfo`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "tarfile.TarInfo") object also provides some convenient query methods:

TarInfo.isfile()[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.isfile "Link to this definition")

Return [`True`](https://docs.python.org/3/library/constants.html#True "True") if the [`TarInfo`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "tarfile.TarInfo") object is a regular file.

TarInfo.isreg()[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.isreg "Link to this definition")

Same as [`isfile()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.isfile "tarfile.TarInfo.isfile").

TarInfo.isdir()[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.isdir "Link to this definition")

Return [`True`](https://docs.python.org/3/library/constants.html#True "True") if it is a directory.

TarInfo.issym()[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.issym "Link to this definition")

Return [`True`](https://docs.python.org/3/library/constants.html#True "True") if it is a symbolic link.

TarInfo.islnk()[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.islnk "Link to this definition")

Return [`True`](https://docs.python.org/3/library/constants.html#True "True") if it is a hard link.

TarInfo.ischr()[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.ischr "Link to this definition")

Return [`True`](https://docs.python.org/3/library/constants.html#True "True") if it is a character device.

TarInfo.isblk()[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.isblk "Link to this definition")

Return [`True`](https://docs.python.org/3/library/constants.html#True "True") if it is a block device.

TarInfo.isfifo()[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.isfifo "Link to this definition")

Return [`True`](https://docs.python.org/3/library/constants.html#True "True") if it is a FIFO.

TarInfo.isdev()[¶](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.isdev "Link to this definition")

Return [`True`](https://docs.python.org/3/library/constants.html#True "True") if it is one of character device, block device or FIFO.
## Extraction filters[¶](https://docs.python.org/3/library/tarfile.html#extraction-filters "Link to this heading")
Added in version 3.12.
The _tar_ format is designed to capture all details of a UNIX-like filesystem, which makes it very powerful. Unfortunately, the features make it easy to create tar files that have unintended – and possibly malicious – effects when extracted. For example, extracting a tar file can overwrite arbitrary files in various ways (e.g. by using absolute paths, `..` path components, or symlinks that affect later members).
In most cases, the full functionality is not needed. Therefore, _tarfile_ supports extraction filters: a mechanism to limit functionality, and thus mitigate some of the security issues.
Warning
None of the available filters blocks _all_ dangerous archive features. Never extract archives from untrusted sources without prior inspection. See also [Hints for further verification](https://docs.python.org/3/library/tarfile.html#tarfile-further-verification).
See also

[**PEP 706**](https://peps.python.org/pep-0706/)

Contains further motivation and rationale behind the design.
The _filter_ argument to [`TarFile.extract()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extract "tarfile.TarFile.extract") or [`extractall()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extractall "tarfile.TarFile.extractall") can be:
  * the string `'fully_trusted'`: Honor all metadata as specified in the archive. Should be used if the user trusts the archive completely, or implements their own complex verification.
  * the string `'tar'`: Honor most _tar_ -specific features (i.e. features of UNIX-like filesystems), but block features that are very likely to be surprising or malicious. See [`tar_filter()`](https://docs.python.org/3/library/tarfile.html#tarfile.tar_filter "tarfile.tar_filter") for details.
  * the string `'data'`: Ignore or block most features specific to UNIX-like filesystems. Intended for extracting cross-platform data archives. See [`data_filter()`](https://docs.python.org/3/library/tarfile.html#tarfile.data_filter "tarfile.data_filter") for details.
  * `None` (default): Use [`TarFile.extraction_filter`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extraction_filter "tarfile.TarFile.extraction_filter").
If that is also `None` (the default), the `'data'` filter will be used.
> Changed in version 3.14: The default filter is set to [`data`](https://docs.python.org/3/library/tarfile.html#tarfile.data_filter "tarfile.data_filter"). Previously, the default was equivalent to [`fully_trusted`](https://docs.python.org/3/library/tarfile.html#tarfile.fully_trusted_filter "tarfile.fully_trusted_filter").
  * A callable which will be called for each extracted member with a [TarInfo](https://docs.python.org/3/library/tarfile.html#tarinfo-objects) describing the member and the destination path to where the archive is extracted (i.e. the same path is used for all members):
Copy```
filter(member: TarInfo, path: str, /) -> TarInfo | None

```

The callable is called just before each member is extracted, so it can take the current state of the disk into account. It can:
    * return a [`TarInfo`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "tarfile.TarInfo") object which will be used instead of the metadata in the archive, or
    * return `None`, in which case the member will be skipped, or
    * raise an exception to abort the operation or skip the member, depending on [`errorlevel`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.errorlevel "tarfile.TarFile.errorlevel"). Note that when extraction is aborted, [`extractall()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extractall "tarfile.TarFile.extractall") may leave the archive partially extracted. It does not attempt to clean up.


### Default named filters[¶](https://docs.python.org/3/library/tarfile.html#default-named-filters "Link to this heading")
The pre-defined, named filters are available as functions, so they can be reused in custom filters:

tarfile.fully_trusted_filter(_member_ , _path_)[¶](https://docs.python.org/3/library/tarfile.html#tarfile.fully_trusted_filter "Link to this definition")

Return _member_ unchanged.
This implements the `'fully_trusted'` filter.

tarfile.tar_filter(_member_ , _path_)[¶](https://docs.python.org/3/library/tarfile.html#tarfile.tar_filter "Link to this definition")

Implements the `'tar'` filter.
  * Strip leading slashes (`/` and [`os.sep`](https://docs.python.org/3/library/os.html#os.sep "os.sep")) from filenames.
  * [Refuse](https://docs.python.org/3/library/tarfile.html#tarfile-extraction-refuse) to extract files with absolute paths (in case the name is absolute even after stripping slashes, e.g. `C:/foo` on Windows). This raises [`AbsolutePathError`](https://docs.python.org/3/library/tarfile.html#tarfile.AbsolutePathError "tarfile.AbsolutePathError").
  * [Refuse](https://docs.python.org/3/library/tarfile.html#tarfile-extraction-refuse) to extract files whose absolute path (after following symlinks) would end up outside the destination. This raises [`OutsideDestinationError`](https://docs.python.org/3/library/tarfile.html#tarfile.OutsideDestinationError "tarfile.OutsideDestinationError").
  * Clear high mode bits (setuid, setgid, sticky) and group/other write bits ([`S_IWGRP`](https://docs.python.org/3/library/stat.html#stat.S_IWGRP "stat.S_IWGRP") | [`S_IWOTH`](https://docs.python.org/3/library/stat.html#stat.S_IWOTH "stat.S_IWOTH")).


Return the modified `TarInfo` member.

tarfile.data_filter(_member_ , _path_)[¶](https://docs.python.org/3/library/tarfile.html#tarfile.data_filter "Link to this definition")

Implements the `'data'` filter. In addition to what `tar_filter` does:
  * Normalize link targets ([`TarInfo.linkname`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo.linkname "tarfile.TarInfo.linkname")) using [`os.path.normpath()`](https://docs.python.org/3/library/os.path.html#os.path.normpath "os.path.normpath"). Note that this removes internal `..` components, which may change the meaning of the link if the path in `TarInfo.linkname` traverses symbolic links.
  * [Refuse](https://docs.python.org/3/library/tarfile.html#tarfile-extraction-refuse) to extract links (hard or soft) that link to absolute paths, or ones that link outside the destination.
This raises [`AbsoluteLinkError`](https://docs.python.org/3/library/tarfile.html#tarfile.AbsoluteLinkError "tarfile.AbsoluteLinkError") or [`LinkOutsideDestinationError`](https://docs.python.org/3/library/tarfile.html#tarfile.LinkOutsideDestinationError "tarfile.LinkOutsideDestinationError").
Note that such files are refused even on platforms that do not support symbolic links.
  * [Refuse](https://docs.python.org/3/library/tarfile.html#tarfile-extraction-refuse) to extract device files (including pipes). This raises [`SpecialFileError`](https://docs.python.org/3/library/tarfile.html#tarfile.SpecialFileError "tarfile.SpecialFileError").
  * For regular files, including hard links:
    * Set the owner read and write permissions ([`S_IRUSR`](https://docs.python.org/3/library/stat.html#stat.S_IRUSR "stat.S_IRUSR") | [`S_IWUSR`](https://docs.python.org/3/library/stat.html#stat.S_IWUSR "stat.S_IWUSR")).
    * Remove the group & other executable permission ([`S_IXGRP`](https://docs.python.org/3/library/stat.html#stat.S_IXGRP "stat.S_IXGRP") | [`S_IXOTH`](https://docs.python.org/3/library/stat.html#stat.S_IXOTH "stat.S_IXOTH")) if the owner doesn’t have it ([`S_IXUSR`](https://docs.python.org/3/library/stat.html#stat.S_IXUSR "stat.S_IXUSR")).
  * For other files (directories), set `mode` to `None`, so that extraction methods skip applying permission bits.
  * Set user and group info (`uid`, `gid`, `uname`, `gname`) to `None`, so that extraction methods skip setting it.


Return the modified `TarInfo` member.
Note that this filter does not block _all_ dangerous archive features. See [Hints for further verification](https://docs.python.org/3/library/tarfile.html#tarfile-further-verification) for details.
Changed in version 3.14: Link targets are now normalized.
### Filter errors[¶](https://docs.python.org/3/library/tarfile.html#filter-errors "Link to this heading")
When a filter refuses to extract a file, it will raise an appropriate exception, a subclass of [`FilterError`](https://docs.python.org/3/library/tarfile.html#tarfile.FilterError "tarfile.FilterError"). This will abort the extraction if [`TarFile.errorlevel`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.errorlevel "tarfile.TarFile.errorlevel") is 1 or more. With `errorlevel=0` the error will be logged and the member will be skipped, but extraction will continue.
### Hints for further verification[¶](https://docs.python.org/3/library/tarfile.html#hints-for-further-verification "Link to this heading")
Even with `filter='data'`, _tarfile_ is not suited for extracting untrusted files without prior inspection. Among other issues, the pre-defined filters do not prevent denial-of-service attacks. Users should do additional checks.
Here is an incomplete list of things to consider:
  * Extract to a [`new temporary directory`](https://docs.python.org/3/library/tempfile.html#tempfile.mkdtemp "tempfile.mkdtemp") to prevent e.g. exploiting pre-existing links, and to make it easier to clean up after a failed extraction.
  * Disallow symbolic links if you do not need the functionality.
  * When working with untrusted data, use external (e.g. OS-level) limits on disk, memory and CPU usage.
  * Check filenames against an allow-list of characters (to filter out control characters, confusables, foreign path separators, and so on).
  * Check that filenames have expected extensions (discouraging files that execute when you “click on them”, or extension-less files like Windows special device names).
  * Limit the number of extracted files, total size of extracted data, filename length (including symlink length), and size of individual files.
  * Check for files that would be shadowed on case-insensitive filesystems.


Also note that:
  * Tar files may contain multiple versions of the same file. Later ones are expected to overwrite any earlier ones. This feature is crucial to allow updating tape archives, but can be abused maliciously.
  * _tarfile_ does not protect against issues with “live” data, e.g. an attacker tinkering with the destination (or source) directory while extraction (or archiving) is in progress.


### Supporting older Python versions[¶](https://docs.python.org/3/library/tarfile.html#supporting-older-python-versions "Link to this heading")
Extraction filters were added to Python 3.12, but may be backported to older versions as security updates. To check whether the feature is available, use e.g. `hasattr(tarfile, 'data_filter')` rather than checking the Python version.
The following examples show how to support Python versions with and without the feature. Note that setting `extraction_filter` will affect any subsequent operations.
  * Fully trusted archive:
Copy```
my_tarfile.extraction_filter = (lambda member, path: member)
my_tarfile.extractall()

```

  * Use the `'data'` filter if available, but revert to Python 3.11 behavior (`'fully_trusted'`) if this feature is not available:
Copy```
my_tarfile.extraction_filter = getattr(tarfile, 'data_filter',
                                       (lambda member, path: member))
my_tarfile.extractall()

```

  * Use the `'data'` filter; _fail_ if it is not available:
Copy```
my_tarfile.extractall(filter=tarfile.data_filter)

```

or:
Copy```
my_tarfile.extraction_filter = tarfile.data_filter
my_tarfile.extractall()

```

  * Use the `'data'` filter; _warn_ if it is not available:
Copy```
if hasattr(tarfile, 'data_filter'):
    my_tarfile.extractall(filter='data')
else:
    # remove this when no longer needed
    warn_the_user('Extracting may be unsafe; consider updating Python')
    my_tarfile.extractall()

```



### Stateful extraction filter example[¶](https://docs.python.org/3/library/tarfile.html#stateful-extraction-filter-example "Link to this heading")
While _tarfile_ ’s extraction methods take a simple _filter_ callable, custom filters may be more complex objects with an internal state. It may be useful to write these as context managers, to be used like this:
Copy```
with StatefulFilter() as filter_func:
    tar.extractall(path, filter=filter_func)

```

Such a filter can be written as, for example:
Copy```
class StatefulFilter:
    def __init__(self):
        self.file_count = 0

    def __enter__(self):
        return self

    def __call__(self, member, path):
        self.file_count += 1
        return member

    def __exit__(self, *exc_info):
        print(f'{self.file_count} files extracted')

```

## Command-Line Interface[¶](https://docs.python.org/3/library/tarfile.html#command-line-interface "Link to this heading")
Added in version 3.4.
The `tarfile` module provides a simple command-line interface to interact with tar archives.
If you want to create a new tar archive, specify its name after the [`-c`](https://docs.python.org/3/library/tarfile.html#cmdoption-tarfile-c) option and then list the filename(s) that should be included:
Copy```
$ python -m tarfile -c monty.tar  spam.txt eggs.txt

```

Passing a directory is also acceptable:
Copy```
$ python -m tarfile -c monty.tar life-of-brian_1979/

```

If you want to extract a tar archive into the current directory, use the [`-e`](https://docs.python.org/3/library/tarfile.html#cmdoption-tarfile-e) option:
Copy```
$ python -m tarfile -e monty.tar

```

You can also extract a tar archive into a different directory by passing the directory’s name:
Copy```
$ python -m tarfile -e monty.tar  other-dir/

```

For a list of the files in a tar archive, use the [`-l`](https://docs.python.org/3/library/tarfile.html#cmdoption-tarfile-l) option:
Copy```
$ python -m tarfile -l monty.tar

```

### Command-line options[¶](https://docs.python.org/3/library/tarfile.html#command-line-options "Link to this heading")

-l <tarfile>[¶](https://docs.python.org/3/library/tarfile.html#cmdoption-tarfile-l "Link to this definition")


--list <tarfile>[¶](https://docs.python.org/3/library/tarfile.html#cmdoption-tarfile-list "Link to this definition")

List files in a tarfile.

-c <tarfile> <source1> ... <sourceN>[¶](https://docs.python.org/3/library/tarfile.html#cmdoption-tarfile-c "Link to this definition")


--create <tarfile> <source1> ... <sourceN>[¶](https://docs.python.org/3/library/tarfile.html#cmdoption-tarfile-create "Link to this definition")

Create tarfile from source files.

-e <tarfile> [<output_dir>][¶](https://docs.python.org/3/library/tarfile.html#cmdoption-tarfile-e "Link to this definition")


--extract <tarfile> [<output_dir>][¶](https://docs.python.org/3/library/tarfile.html#cmdoption-tarfile-extract "Link to this definition")

Extract tarfile into the current directory if _output_dir_ is not specified.

-t <tarfile>[¶](https://docs.python.org/3/library/tarfile.html#cmdoption-tarfile-t "Link to this definition")


--test <tarfile>[¶](https://docs.python.org/3/library/tarfile.html#cmdoption-tarfile-test "Link to this definition")

Test whether the tarfile is valid or not.

-v, --verbose[¶](https://docs.python.org/3/library/tarfile.html#cmdoption-tarfile-v "Link to this definition")

Verbose output.

--filter <filtername>[¶](https://docs.python.org/3/library/tarfile.html#cmdoption-tarfile-filter "Link to this definition")

Specifies the _filter_ for `--extract`. See [Extraction filters](https://docs.python.org/3/library/tarfile.html#tarfile-extraction-filter) for details. Only string names are accepted (that is, `fully_trusted`, `tar`, and `data`).
