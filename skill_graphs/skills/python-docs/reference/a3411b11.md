If _follow_symlinks_ is `False`, return `True` only if this entry is a directory (without following symlinks); return `False` if the entry is any other kind of file or if it doesn’t exist anymore.
The result is cached on the `os.DirEntry` object, with a separate cache for _follow_symlinks_ `True` and `False`. Call [`os.stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat") along with [`stat.S_ISDIR()`](https://docs.python.org/3/library/stat.html#stat.S_ISDIR "stat.S_ISDIR") to fetch up-to-date information.
On the first, uncached call, no system call is required in most cases. Specifically, for non-symlinks, neither Windows or Unix require a system call, except on certain Unix file systems, such as network file systems, that return `dirent.d_type == DT_UNKNOWN`. If the entry is a symlink, a system call will be required to follow the symlink unless _follow_symlinks_ is `False`.
This method can raise [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError"), such as [`PermissionError`](https://docs.python.org/3/library/exceptions.html#PermissionError "PermissionError"), but [`FileNotFoundError`](https://docs.python.org/3/library/exceptions.html#FileNotFoundError "FileNotFoundError") is caught and not raised.

is_file(_*_ , _follow_symlinks =True_)[¶](https://docs.python.org/3/library/os.html#os.DirEntry.is_file "Link to this definition")

Return `True` if this entry is a file or a symbolic link pointing to a file; return `False` if the entry is or points to a directory or other non-file entry, or if it doesn’t exist anymore.
If _follow_symlinks_ is `False`, return `True` only if this entry is a file (without following symlinks); return `False` if the entry is a directory or other non-file entry, or if it doesn’t exist anymore.
The result is cached on the `os.DirEntry` object. Caching, system calls made, and exceptions raised are as per [`is_dir()`](https://docs.python.org/3/library/os.html#os.DirEntry.is_dir "os.DirEntry.is_dir").

is_symlink()[¶](https://docs.python.org/3/library/os.html#os.DirEntry.is_symlink "Link to this definition")

Return `True` if this entry is a symbolic link (even if broken); return `False` if the entry points to a directory or any kind of file, or if it doesn’t exist anymore.
The result is cached on the `os.DirEntry` object. Call [`os.path.islink()`](https://docs.python.org/3/library/os.path.html#os.path.islink "os.path.islink") to fetch up-to-date information.
On the first, uncached call, no system call is required in most cases. Specifically, neither Windows or Unix require a system call, except on certain Unix file systems, such as network file systems, that return `dirent.d_type == DT_UNKNOWN`.
This method can raise [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError"), such as [`PermissionError`](https://docs.python.org/3/library/exceptions.html#PermissionError "PermissionError"), but [`FileNotFoundError`](https://docs.python.org/3/library/exceptions.html#FileNotFoundError "FileNotFoundError") is caught and not raised.

is_junction()[¶](https://docs.python.org/3/library/os.html#os.DirEntry.is_junction "Link to this definition")

Return `True` if this entry is a junction (even if broken); return `False` if the entry points to a regular directory, any kind of file, a symlink, or if it doesn’t exist anymore.
The result is cached on the `os.DirEntry` object. Call [`os.path.isjunction()`](https://docs.python.org/3/library/os.path.html#os.path.isjunction "os.path.isjunction") to fetch up-to-date information.
Added in version 3.12.

stat(_*_ , _follow_symlinks =True_)[¶](https://docs.python.org/3/library/os.html#os.DirEntry.stat "Link to this definition")

Return a [`stat_result`](https://docs.python.org/3/library/os.html#os.stat_result "os.stat_result") object for this entry. This method follows symbolic links by default; to stat a symbolic link add the `follow_symlinks=False` argument.
On Unix, this method always requires a system call. On Windows, it only requires a system call if _follow_symlinks_ is `True` and the entry is a reparse point (for example, a symbolic link or directory junction).
On Windows, the `st_ino`, `st_dev` and `st_nlink` attributes of the [`stat_result`](https://docs.python.org/3/library/os.html#os.stat_result "os.stat_result") are always set to zero. Call [`os.stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat") to get these attributes.
The result is cached on the `os.DirEntry` object, with a separate cache for _follow_symlinks_ `True` and `False`. Call [`os.stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat") to fetch up-to-date information.
Note that there is a nice correspondence between several attributes and methods of `os.DirEntry` and of [`pathlib.Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path"). In particular, the `name` attribute has the same meaning, as do the `is_dir()`, `is_file()`, `is_symlink()`, `is_junction()`, and `stat()` methods.
Added in version 3.5.
Changed in version 3.6: Added support for the [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "os.PathLike") interface. Added support for [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") paths on Windows.
Changed in version 3.12: The `st_ctime` attribute of a stat result is deprecated on Windows. The file creation time is properly available as `st_birthtime`, and in the future `st_ctime` may be changed to return zero or the metadata change time, if available.

os.stat(_path_ , _*_ , _dir_fd =None_, _follow_symlinks =True_)[¶](https://docs.python.org/3/library/os.html#os.stat "Link to this definition")

Get the status of a file or a file descriptor. Perform the equivalent of a `stat()` system call on the given path. _path_ may be specified as either a string or bytes – directly or indirectly through the [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "os.PathLike") interface – or as an open file descriptor. Return a [`stat_result`](https://docs.python.org/3/library/os.html#os.stat_result "os.stat_result") object.
This function normally follows symlinks; to stat a symlink add the argument `follow_symlinks=False`, or use [`lstat()`](https://docs.python.org/3/library/os.html#os.lstat "os.lstat").
This function can support [specifying a file descriptor](https://docs.python.org/3/library/os.html#path-fd) and [not following symlinks](https://docs.python.org/3/library/os.html#follow-symlinks).
On Windows, passing `follow_symlinks=False` will disable following all name-surrogate reparse points, which includes symlinks and directory junctions. Other types of reparse points that do not resemble links or that the operating system is unable to follow will be opened directly. When following a chain of multiple links, this may result in the original link being returned instead of the non-link that prevented full traversal. To obtain stat results for the final path in this case, use the [`os.path.realpath()`](https://docs.python.org/3/library/os.path.html#os.path.realpath "os.path.realpath") function to resolve the path name as far as possible and call [`lstat()`](https://docs.python.org/3/library/os.html#os.lstat "os.lstat") on the result. This does not apply to dangling symlinks or junction points, which will raise the usual exceptions.
Example:
Copy```
>>> import os
>>> statinfo = os.stat('somefile.txt')
>>> statinfo
os.stat_result(st_mode=33188, st_ino=7876932, st_dev=234881026,
st_nlink=1, st_uid=501, st_gid=501, st_size=264, st_atime=1297230295,
st_mtime=1297230027, st_ctime=1297230027)
>>> statinfo.st_size
264

```

See also
[`fstat()`](https://docs.python.org/3/library/os.html#os.fstat "os.fstat") and [`lstat()`](https://docs.python.org/3/library/os.html#os.lstat "os.lstat") functions.
Changed in version 3.3: Added the _dir_fd_ and _follow_symlinks_ parameters, specifying a file descriptor instead of a path.
Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).
Changed in version 3.8: On Windows, all reparse points that can be resolved by the operating system are now followed, and passing `follow_symlinks=False` disables following all name surrogate reparse points. If the operating system reaches a reparse point that it is not able to follow, _stat_ now returns the information for the original path as if `follow_symlinks=False` had been specified instead of raising an error.

_class_ os.stat_result[¶](https://docs.python.org/3/library/os.html#os.stat_result "Link to this definition")

Object whose attributes correspond roughly to the members of the `stat` structure. It is used for the result of [`os.stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat"), [`os.fstat()`](https://docs.python.org/3/library/os.html#os.fstat "os.fstat") and [`os.lstat()`](https://docs.python.org/3/library/os.html#os.lstat "os.lstat").
Attributes:

st_mode[¶](https://docs.python.org/3/library/os.html#os.stat_result.st_mode "Link to this definition")

File mode: file type and file mode bits (permissions).

st_ino[¶](https://docs.python.org/3/library/os.html#os.stat_result.st_ino "Link to this definition")

Platform dependent, but if non-zero, uniquely identifies the file for a given value of `st_dev`. Typically:
  * the inode number on Unix,
  * the



st_dev[¶](https://docs.python.org/3/library/os.html#os.stat_result.st_dev "Link to this definition")

Identifier of the device on which this file resides.

st_nlink[¶](https://docs.python.org/3/library/os.html#os.stat_result.st_nlink "Link to this definition")

Number of hard links.

st_uid[¶](https://docs.python.org/3/library/os.html#os.stat_result.st_uid "Link to this definition")

User identifier of the file owner.

st_gid[¶](https://docs.python.org/3/library/os.html#os.stat_result.st_gid "Link to this definition")

Group identifier of the file owner.

st_size[¶](https://docs.python.org/3/library/os.html#os.stat_result.st_size "Link to this definition")

Size of the file in bytes, if it is a regular file or a symbolic link. The size of a symbolic link is the length of the pathname it contains, without a terminating null byte.
Timestamps:

st_atime[¶](https://docs.python.org/3/library/os.html#os.stat_result.st_atime "Link to this definition")

Time of most recent access expressed in seconds.

st_mtime[¶](https://docs.python.org/3/library/os.html#os.stat_result.st_mtime "Link to this definition")

Time of most recent content modification expressed in seconds.

st_ctime[¶](https://docs.python.org/3/library/os.html#os.stat_result.st_ctime "Link to this definition")

Time of most recent metadata change expressed in seconds.
Changed in version 3.12: `st_ctime` is deprecated on Windows. Use `st_birthtime` for the file creation time. In the future, `st_ctime` will contain the time of the most recent metadata change, as for other platforms.

st_atime_ns[¶](https://docs.python.org/3/library/os.html#os.stat_result.st_atime_ns "Link to this definition")

Time of most recent access expressed in nanoseconds as an integer.
Added in version 3.3.

st_mtime_ns[¶](https://docs.python.org/3/library/os.html#os.stat_result.st_mtime_ns "Link to this definition")

Time of most recent content modification expressed in nanoseconds as an integer.
Added in version 3.3.

st_ctime_ns[¶](https://docs.python.org/3/library/os.html#os.stat_result.st_ctime_ns "Link to this definition")

Time of most recent metadata change expressed in nanoseconds as an integer.
Added in version 3.3.
Changed in version 3.12: `st_ctime_ns` is deprecated on Windows. Use `st_birthtime_ns` for the file creation time. In the future, `st_ctime` will contain the time of the most recent metadata change, as for other platforms.

st_birthtime[¶](https://docs.python.org/3/library/os.html#os.stat_result.st_birthtime "Link to this definition")

Time of file creation expressed in seconds. This attribute is not always available, and may raise [`AttributeError`](https://docs.python.org/3/library/exceptions.html#AttributeError "AttributeError").
Changed in version 3.12: `st_birthtime` is now available on Windows.

st_birthtime_ns[¶](https://docs.python.org/3/library/os.html#os.stat_result.st_birthtime_ns "Link to this definition")

Time of file creation expressed in nanoseconds as an integer. This attribute is not always available, and may raise [`AttributeError`](https://docs.python.org/3/library/exceptions.html#AttributeError "AttributeError").
Added in version 3.12.
Note
The exact meaning and resolution of the [`st_atime`](https://docs.python.org/3/library/os.html#os.stat_result.st_atime "os.stat_result.st_atime"), [`st_mtime`](https://docs.python.org/3/library/os.html#os.stat_result.st_mtime "os.stat_result.st_mtime"), [`st_ctime`](https://docs.python.org/3/library/os.html#os.stat_result.st_ctime "os.stat_result.st_ctime") and [`st_birthtime`](https://docs.python.org/3/library/os.html#os.stat_result.st_birthtime "os.stat_result.st_birthtime") attributes depend on the operating system and the file system. For example, on Windows systems using the FAT32 file systems, `st_mtime` has 2-second resolution, and `st_atime` has only 1-day resolution. See your operating system documentation for details.
Similarly, although [`st_atime_ns`](https://docs.python.org/3/library/os.html#os.stat_result.st_atime_ns "os.stat_result.st_atime_ns"), [`st_mtime_ns`](https://docs.python.org/3/library/os.html#os.stat_result.st_mtime_ns "os.stat_result.st_mtime_ns"), [`st_ctime_ns`](https://docs.python.org/3/library/os.html#os.stat_result.st_ctime_ns "os.stat_result.st_ctime_ns") and [`st_birthtime_ns`](https://docs.python.org/3/library/os.html#os.stat_result.st_birthtime_ns "os.stat_result.st_birthtime_ns") are always expressed in nanoseconds, many systems do not provide nanosecond precision. On systems that do provide nanosecond precision, the floating-point object used to store [`st_atime`](https://docs.python.org/3/library/os.html#os.stat_result.st_atime "os.stat_result.st_atime"), [`st_mtime`](https://docs.python.org/3/library/os.html#os.stat_result.st_mtime "os.stat_result.st_mtime"), [`st_ctime`](https://docs.python.org/3/library/os.html#os.stat_result.st_ctime "os.stat_result.st_ctime") and [`st_birthtime`](https://docs.python.org/3/library/os.html#os.stat_result.st_birthtime "os.stat_result.st_birthtime") cannot preserve all of it, and as such will be slightly inexact. If you need the exact timestamps you should always use `st_atime_ns`, `st_mtime_ns`, `st_ctime_ns` and `st_birthtime_ns`.
On some Unix systems (such as Linux), the following attributes may also be available:

st_blocks[¶](https://docs.python.org/3/library/os.html#os.stat_result.st_blocks "Link to this definition")

Number of 512-byte blocks allocated for file. This may be smaller than [`st_size`](https://docs.python.org/3/library/os.html#os.stat_result.st_size "os.stat_result.st_size")/512 when the file has holes.

st_blksize[¶](https://docs.python.org/3/library/os.html#os.stat_result.st_blksize "Link to this definition")

“Preferred” blocksize for efficient file system I/O. Writing to a file in smaller chunks may cause an inefficient read-modify-rewrite.

st_rdev[¶](https://docs.python.org/3/library/os.html#os.stat_result.st_rdev "Link to this definition")

Type of device if an inode device.

st_flags[¶](https://docs.python.org/3/library/os.html#os.stat_result.st_flags "Link to this definition")

User defined flags for file.
On other Unix systems (such as FreeBSD), the following attributes may be available (but may be only filled out if root tries to use them):

st_gen[¶](https://docs.python.org/3/library/os.html#os.stat_result.st_gen "Link to this definition")

File generation number.
On Solaris and derivatives, the following attributes may also be available:

st_fstype[¶](https://docs.python.org/3/library/os.html#os.stat_result.st_fstype "Link to this definition")

String that uniquely identifies the type of the filesystem that contains the file.
On macOS systems, the following attributes may also be available:

st_rsize[¶](https://docs.python.org/3/library/os.html#os.stat_result.st_rsize "Link to this definition")

Real size of the file.

st_creator[¶](https://docs.python.org/3/library/os.html#os.stat_result.st_creator "Link to this definition")

Creator of the file.

st_type[¶](https://docs.python.org/3/library/os.html#os.stat_result.st_type "Link to this definition")

File type.
On Windows systems, the following attributes are also available:

st_file_attributes[¶](https://docs.python.org/3/library/os.html#os.stat_result.st_file_attributes "Link to this definition")

Windows file attributes: `dwFileAttributes` member of the `BY_HANDLE_FILE_INFORMATION` structure returned by `GetFileInformationByHandle()`. See the `FILE_ATTRIBUTE_* <stat.FILE_ATTRIBUTE_ARCHIVE>` constants in the [`stat`](https://docs.python.org/3/library/stat.html#module-stat "stat: Utilities for interpreting the results of os.stat\(\), os.lstat\(\) and os.fstat\(\).") module.
Added in version 3.5.

st_reparse_tag[¶](https://docs.python.org/3/library/os.html#os.stat_result.st_reparse_tag "Link to this definition")

When [`st_file_attributes`](https://docs.python.org/3/library/os.html#os.stat_result.st_file_attributes "os.stat_result.st_file_attributes") has the [`FILE_ATTRIBUTE_REPARSE_POINT`](https://docs.python.org/3/library/stat.html#stat.FILE_ATTRIBUTE_REPARSE_POINT "stat.FILE_ATTRIBUTE_REPARSE_POINT") set, this field contains the tag identifying the type of reparse point. See the [`IO_REPARSE_TAG_*`](https://docs.python.org/3/library/stat.html#stat.IO_REPARSE_TAG_SYMLINK "stat.IO_REPARSE_TAG_SYMLINK") constants in the [`stat`](https://docs.python.org/3/library/stat.html#module-stat "stat: Utilities for interpreting the results of os.stat\(\), os.lstat\(\) and os.fstat\(\).") module.
The standard module [`stat`](https://docs.python.org/3/library/stat.html#module-stat "stat: Utilities for interpreting the results of os.stat\(\), os.lstat\(\) and os.fstat\(\).") defines functions and constants that are useful for extracting information from a `stat` structure. (On Windows, some items are filled with dummy values.)
For backward compatibility, a `stat_result` instance is also accessible as a tuple of at least 10 integers giving the most important (and portable) members of the `stat` structure, in the order [`st_mode`](https://docs.python.org/3/library/os.html#os.stat_result.st_mode "os.stat_result.st_mode"), [`st_ino`](https://docs.python.org/3/library/os.html#os.stat_result.st_ino "os.stat_result.st_ino"), [`st_dev`](https://docs.python.org/3/library/os.html#os.stat_result.st_dev "os.stat_result.st_dev"), [`st_nlink`](https://docs.python.org/3/library/os.html#os.stat_result.st_nlink "os.stat_result.st_nlink"), [`st_uid`](https://docs.python.org/3/library/os.html#os.stat_result.st_uid "os.stat_result.st_uid"), [`st_gid`](https://docs.python.org/3/library/os.html#os.stat_result.st_gid "os.stat_result.st_gid"), [`st_size`](https://docs.python.org/3/library/os.html#os.stat_result.st_size "os.stat_result.st_size"), [`st_atime`](https://docs.python.org/3/library/os.html#os.stat_result.st_atime "os.stat_result.st_atime"), [`st_mtime`](https://docs.python.org/3/library/os.html#os.stat_result.st_mtime "os.stat_result.st_mtime"), [`st_ctime`](https://docs.python.org/3/library/os.html#os.stat_result.st_ctime "os.stat_result.st_ctime"). More items may be added at the end by some implementations. For compatibility with older Python versions, accessing `stat_result` as a tuple always returns integers.
Changed in version 3.5: Windows now returns the file index as [`st_ino`](https://docs.python.org/3/library/os.html#os.stat_result.st_ino "os.stat_result.st_ino") when available.
Changed in version 3.7: Added the [`st_fstype`](https://docs.python.org/3/library/os.html#os.stat_result.st_fstype "os.stat_result.st_fstype") member to Solaris/derivatives.
Changed in version 3.8: Added the [`st_reparse_tag`](https://docs.python.org/3/library/os.html#os.stat_result.st_reparse_tag "os.stat_result.st_reparse_tag") member on Windows.
Changed in version 3.8: On Windows, the [`st_mode`](https://docs.python.org/3/library/os.html#os.stat_result.st_mode "os.stat_result.st_mode") member now identifies special files as `S_IFCHR`, `S_IFIFO` or `S_IFBLK` as appropriate.
Changed in version 3.12: On Windows, [`st_ctime`](https://docs.python.org/3/library/os.html#os.stat_result.st_ctime "os.stat_result.st_ctime") is deprecated. Eventually, it will contain the last metadata change time, for consistency with other platforms, but for now still contains creation time. Use [`st_birthtime`](https://docs.python.org/3/library/os.html#os.stat_result.st_birthtime "os.stat_result.st_birthtime") for the creation time.
On Windows, [`st_ino`](https://docs.python.org/3/library/os.html#os.stat_result.st_ino "os.stat_result.st_ino") may now be up to 128 bits, depending on the file system. Previously it would not be above 64 bits, and larger file identifiers would be arbitrarily packed.
On Windows, [`st_rdev`](https://docs.python.org/3/library/os.html#os.stat_result.st_rdev "os.stat_result.st_rdev") no longer returns a value. Previously it would contain the same as [`st_dev`](https://docs.python.org/3/library/os.html#os.stat_result.st_dev "os.stat_result.st_dev"), which was incorrect.
Added the [`st_birthtime`](https://docs.python.org/3/library/os.html#os.stat_result.st_birthtime "os.stat_result.st_birthtime") member on Windows.

os.statvfs(_path_)[¶](https://docs.python.org/3/library/os.html#os.statvfs "Link to this definition")

Perform a `statvfs()` system call on the given path. The return value is an object whose attributes describe the filesystem on the given path, and correspond to the members of the `statvfs` structure, namely: `f_bsize`, `f_frsize`, `f_blocks`, `f_bfree`, `f_bavail`, `f_files`, `f_ffree`, `f_favail`, `f_flag`, `f_namemax`, `f_fsid`.
Two module-level constants are defined for the `f_flag` attribute’s bit-flags: if `ST_RDONLY` is set, the filesystem is mounted read-only, and if `ST_NOSUID` is set, the semantics of setuid/setgid bits are disabled or not supported.
Additional module-level constants are defined for GNU/glibc based systems. These are `ST_NODEV` (disallow access to device special files), `ST_NOEXEC` (disallow program execution), `ST_SYNCHRONOUS` (writes are synced at once), `ST_MANDLOCK` (allow mandatory locks on an FS), `ST_WRITE` (write on file/directory/symlink), `ST_APPEND` (append-only file), `ST_IMMUTABLE` (immutable file), `ST_NOATIME` (do not update access times), `ST_NODIRATIME` (do not update directory access times), `ST_RELATIME` (update atime relative to mtime/ctime).
This function can support [specifying a file descriptor](https://docs.python.org/3/library/os.html#path-fd).
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.
Changed in version 3.2: The `ST_RDONLY` and `ST_NOSUID` constants were added.
Changed in version 3.3: Added support for specifying _path_ as an open file descriptor.
Changed in version 3.4: The `ST_NODEV`, `ST_NOEXEC`, `ST_SYNCHRONOUS`, `ST_MANDLOCK`, `ST_WRITE`, `ST_APPEND`, `ST_IMMUTABLE`, `ST_NOATIME`, `ST_NODIRATIME`, and `ST_RELATIME` constants were added.
Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).
Changed in version 3.7: Added the `f_fsid` attribute.

os.supports_dir_fd[¶](https://docs.python.org/3/library/os.html#os.supports_dir_fd "Link to this definition")

A [`set`](https://docs.python.org/3/library/stdtypes.html#set "set") object indicating which functions in the `os` module accept an open file descriptor for their _dir_fd_ parameter. Different platforms provide different features, and the underlying functionality Python uses to implement the _dir_fd_ parameter is not available on all platforms Python supports. For consistency’s sake, functions that may support _dir_fd_ always allow specifying the parameter, but will throw an exception if the functionality is used when it’s not locally available. (Specifying `None` for _dir_fd_ is always supported on all platforms.)
To check whether a particular function accepts an open file descriptor for its _dir_fd_ parameter, use the `in` operator on `supports_dir_fd`. As an example, this expression evaluates to `True` if [`os.stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat") accepts open file descriptors for _dir_fd_ on the local platform:
Copy```
os.stat in os.supports_dir_fd

```

Currently _dir_fd_ parameters only work on Unix platforms; none of them work on Windows.
Added in version 3.3.

os.supports_effective_ids[¶](https://docs.python.org/3/library/os.html#os.supports_effective_ids "Link to this definition")

A [`set`](https://docs.python.org/3/library/stdtypes.html#set "set") object indicating whether [`os.access()`](https://docs.python.org/3/library/os.html#os.access "os.access") permits specifying `True` for its _effective_ids_ parameter on the local platform. (Specifying `False` for _effective_ids_ is always supported on all platforms.) If the local platform supports it, the collection will contain `os.access()`; otherwise it will be empty.
This expression evaluates to `True` if [`os.access()`](https://docs.python.org/3/library/os.html#os.access "os.access") supports `effective_ids=True` on the local platform:
