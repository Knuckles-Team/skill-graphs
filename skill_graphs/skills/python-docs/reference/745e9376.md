## Files and Directories[¶](https://docs.python.org/3/library/os.html#files-and-directories "Link to this heading")
On some Unix platforms, many of these functions support one or more of these features:
  * **specifying a file descriptor:** Normally the _path_ argument provided to functions in the `os` module must be a string specifying a file path. However, some functions now alternatively accept an open file descriptor for their _path_ argument. The function will then operate on the file referred to by the descriptor. For POSIX systems, Python will call the variant of the function prefixed with `f` (e.g. call `fchdir` instead of `chdir`).
You can check whether or not _path_ can be specified as a file descriptor for a particular function on your platform using [`os.supports_fd`](https://docs.python.org/3/library/os.html#os.supports_fd "os.supports_fd"). If this functionality is unavailable, using it will raise a [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError").
If the function also supports _dir_fd_ or _follow_symlinks_ arguments, it’s an error to specify one of those when supplying _path_ as a file descriptor.


  * **paths relative to directory descriptors:** If _dir_fd_ is not `None`, it should be a file descriptor referring to a directory, and the path to operate on should be relative; path will then be relative to that directory. If the path is absolute, _dir_fd_ is ignored. For POSIX systems, Python will call the variant of the function with an `at` suffix and possibly prefixed with `f` (e.g. call `faccessat` instead of `access`).
You can check whether or not _dir_fd_ is supported for a particular function on your platform using [`os.supports_dir_fd`](https://docs.python.org/3/library/os.html#os.supports_dir_fd "os.supports_dir_fd"). If it’s unavailable, using it will raise a [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError").


  * **not following symlinks:** If _follow_symlinks_ is `False`, and the last element of the path to operate on is a symbolic link, the function will operate on the symbolic link itself rather than the file pointed to by the link. For POSIX systems, Python will call the `l...` variant of the function.
You can check whether or not _follow_symlinks_ is supported for a particular function on your platform using [`os.supports_follow_symlinks`](https://docs.python.org/3/library/os.html#os.supports_follow_symlinks "os.supports_follow_symlinks"). If it’s unavailable, using it will raise a [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError").



os.access(_path_ , _mode_ , _*_ , _dir_fd =None_, _effective_ids =False_, _follow_symlinks =True_)[¶](https://docs.python.org/3/library/os.html#os.access "Link to this definition")

Use the real uid/gid to test for access to _path_. Note that most operations will use the effective uid/gid, therefore this routine can be used in a suid/sgid environment to test if the invoking user has the specified access to _path_. _mode_ should be [`F_OK`](https://docs.python.org/3/library/os.html#os.F_OK "os.F_OK") to test the existence of _path_ , or it can be the inclusive OR of one or more of [`R_OK`](https://docs.python.org/3/library/os.html#os.R_OK "os.R_OK"), [`W_OK`](https://docs.python.org/3/library/os.html#os.W_OK "os.W_OK"), and [`X_OK`](https://docs.python.org/3/library/os.html#os.X_OK "os.X_OK") to test permissions. Return [`True`](https://docs.python.org/3/library/constants.html#True "True") if access is allowed, [`False`](https://docs.python.org/3/library/constants.html#False "False") if not. See the Unix man page
This function can support specifying [paths relative to directory descriptors](https://docs.python.org/3/library/os.html#dir-fd) and [not following symlinks](https://docs.python.org/3/library/os.html#follow-symlinks).
If _effective_ids_ is `True`, `access()` will perform its access checks using the effective uid/gid instead of the real uid/gid. _effective_ids_ may not be supported on your platform; you can check whether or not it is available using [`os.supports_effective_ids`](https://docs.python.org/3/library/os.html#os.supports_effective_ids "os.supports_effective_ids"). If it is unavailable, using it will raise a [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError").
Note
Using `access()` to check if a user is authorized to e.g. open a file before actually doing so using [`open()`](https://docs.python.org/3/library/functions.html#open "open") creates a security hole, because the user might exploit the short time interval between checking and opening the file to manipulate it. It’s preferable to use [EAFP](https://docs.python.org/3/glossary.html#term-EAFP) techniques. For example:
Copy```
if os.access("myfile", os.R_OK):
    with open("myfile") as fp:
        return fp.read()
return "some default data"

```

is better written as:
Copy```
try:
    fp = open("myfile")
except PermissionError:
    return "some default data"
else:
    with fp:
        return fp.read()

```

Note
I/O operations may fail even when `access()` indicates that they would succeed, particularly for operations on network filesystems which may have permissions semantics beyond the usual POSIX permission-bit model.
Changed in version 3.3: Added the _dir_fd_ , _effective_ids_ , and _follow_symlinks_ parameters.
Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).

os.F_OK[¶](https://docs.python.org/3/library/os.html#os.F_OK "Link to this definition")


os.R_OK[¶](https://docs.python.org/3/library/os.html#os.R_OK "Link to this definition")


os.W_OK[¶](https://docs.python.org/3/library/os.html#os.W_OK "Link to this definition")


os.X_OK[¶](https://docs.python.org/3/library/os.html#os.X_OK "Link to this definition")

Values to pass as the _mode_ parameter of [`access()`](https://docs.python.org/3/library/os.html#os.access "os.access") to test the existence, readability, writability and executability of _path_ , respectively.

os.chdir(_path_)[¶](https://docs.python.org/3/library/os.html#os.chdir "Link to this definition")

Change the current working directory to _path_.
This function can support [specifying a file descriptor](https://docs.python.org/3/library/os.html#path-fd). The descriptor must refer to an opened directory, not an open file.
This function can raise [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") and subclasses such as [`FileNotFoundError`](https://docs.python.org/3/library/exceptions.html#FileNotFoundError "FileNotFoundError"), [`PermissionError`](https://docs.python.org/3/library/exceptions.html#PermissionError "PermissionError"), and [`NotADirectoryError`](https://docs.python.org/3/library/exceptions.html#NotADirectoryError "NotADirectoryError").
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `os.chdir` with argument `path`.
Changed in version 3.3: Added support for specifying _path_ as a file descriptor on some platforms.
Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).

os.chflags(_path_ , _flags_ , _*_ , _follow_symlinks =True_)[¶](https://docs.python.org/3/library/os.html#os.chflags "Link to this definition")

Set the flags of _path_ to the numeric _flags_. _flags_ may take a combination (bitwise OR) of the following values (as defined in the [`stat`](https://docs.python.org/3/library/stat.html#module-stat "stat: Utilities for interpreting the results of os.stat\(\), os.lstat\(\) and os.fstat\(\).") module):
  * [`stat.UF_NODUMP`](https://docs.python.org/3/library/stat.html#stat.UF_NODUMP "stat.UF_NODUMP")
  * [`stat.UF_IMMUTABLE`](https://docs.python.org/3/library/stat.html#stat.UF_IMMUTABLE "stat.UF_IMMUTABLE")
  * [`stat.UF_APPEND`](https://docs.python.org/3/library/stat.html#stat.UF_APPEND "stat.UF_APPEND")
  * [`stat.UF_OPAQUE`](https://docs.python.org/3/library/stat.html#stat.UF_OPAQUE "stat.UF_OPAQUE")
  * [`stat.UF_NOUNLINK`](https://docs.python.org/3/library/stat.html#stat.UF_NOUNLINK "stat.UF_NOUNLINK")
  * [`stat.UF_COMPRESSED`](https://docs.python.org/3/library/stat.html#stat.UF_COMPRESSED "stat.UF_COMPRESSED")
  * [`stat.UF_HIDDEN`](https://docs.python.org/3/library/stat.html#stat.UF_HIDDEN "stat.UF_HIDDEN")
  * [`stat.SF_ARCHIVED`](https://docs.python.org/3/library/stat.html#stat.SF_ARCHIVED "stat.SF_ARCHIVED")
  * [`stat.SF_IMMUTABLE`](https://docs.python.org/3/library/stat.html#stat.SF_IMMUTABLE "stat.SF_IMMUTABLE")
  * [`stat.SF_APPEND`](https://docs.python.org/3/library/stat.html#stat.SF_APPEND "stat.SF_APPEND")
  * [`stat.SF_NOUNLINK`](https://docs.python.org/3/library/stat.html#stat.SF_NOUNLINK "stat.SF_NOUNLINK")
  * [`stat.SF_SNAPSHOT`](https://docs.python.org/3/library/stat.html#stat.SF_SNAPSHOT "stat.SF_SNAPSHOT")


This function can support [not following symlinks](https://docs.python.org/3/library/os.html#follow-symlinks).
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `os.chflags` with arguments `path`, `flags`.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI.
Changed in version 3.3: Added the _follow_symlinks_ parameter.
Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).

os.chmod(_path_ , _mode_ , _*_ , _dir_fd =None_, _follow_symlinks =True_)[¶](https://docs.python.org/3/library/os.html#os.chmod "Link to this definition")

Change the mode of _path_ to the numeric _mode_. _mode_ may take one of the following values (as defined in the [`stat`](https://docs.python.org/3/library/stat.html#module-stat "stat: Utilities for interpreting the results of os.stat\(\), os.lstat\(\) and os.fstat\(\).") module) or bitwise ORed combinations of them:
  * [`stat.S_ISUID`](https://docs.python.org/3/library/stat.html#stat.S_ISUID "stat.S_ISUID")
  * [`stat.S_ISGID`](https://docs.python.org/3/library/stat.html#stat.S_ISGID "stat.S_ISGID")
  * [`stat.S_ENFMT`](https://docs.python.org/3/library/stat.html#stat.S_ENFMT "stat.S_ENFMT")
  * [`stat.S_ISVTX`](https://docs.python.org/3/library/stat.html#stat.S_ISVTX "stat.S_ISVTX")
  * [`stat.S_IREAD`](https://docs.python.org/3/library/stat.html#stat.S_IREAD "stat.S_IREAD")
  * [`stat.S_IWRITE`](https://docs.python.org/3/library/stat.html#stat.S_IWRITE "stat.S_IWRITE")
  * [`stat.S_IEXEC`](https://docs.python.org/3/library/stat.html#stat.S_IEXEC "stat.S_IEXEC")
  * [`stat.S_IRWXU`](https://docs.python.org/3/library/stat.html#stat.S_IRWXU "stat.S_IRWXU")
  * [`stat.S_IRUSR`](https://docs.python.org/3/library/stat.html#stat.S_IRUSR "stat.S_IRUSR")
  * [`stat.S_IWUSR`](https://docs.python.org/3/library/stat.html#stat.S_IWUSR "stat.S_IWUSR")
  * [`stat.S_IXUSR`](https://docs.python.org/3/library/stat.html#stat.S_IXUSR "stat.S_IXUSR")
  * [`stat.S_IRWXG`](https://docs.python.org/3/library/stat.html#stat.S_IRWXG "stat.S_IRWXG")
  * [`stat.S_IRGRP`](https://docs.python.org/3/library/stat.html#stat.S_IRGRP "stat.S_IRGRP")
  * [`stat.S_IWGRP`](https://docs.python.org/3/library/stat.html#stat.S_IWGRP "stat.S_IWGRP")
  * [`stat.S_IXGRP`](https://docs.python.org/3/library/stat.html#stat.S_IXGRP "stat.S_IXGRP")
  * [`stat.S_IRWXO`](https://docs.python.org/3/library/stat.html#stat.S_IRWXO "stat.S_IRWXO")
  * [`stat.S_IROTH`](https://docs.python.org/3/library/stat.html#stat.S_IROTH "stat.S_IROTH")
  * [`stat.S_IWOTH`](https://docs.python.org/3/library/stat.html#stat.S_IWOTH "stat.S_IWOTH")
  * [`stat.S_IXOTH`](https://docs.python.org/3/library/stat.html#stat.S_IXOTH "stat.S_IXOTH")


This function can support [specifying a file descriptor](https://docs.python.org/3/library/os.html#path-fd), [paths relative to directory descriptors](https://docs.python.org/3/library/os.html#dir-fd) and [not following symlinks](https://docs.python.org/3/library/os.html#follow-symlinks).
Note
Although Windows supports `chmod()`, you can only set the file’s read-only flag with it (via the `stat.S_IWRITE` and `stat.S_IREAD` constants or a corresponding integer value). All other bits are ignored. The default value of _follow_symlinks_ is `False` on Windows.
The function is limited on WASI, see [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability) for more information.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `os.chmod` with arguments `path`, `mode`, `dir_fd`.
Changed in version 3.3: Added support for specifying _path_ as an open file descriptor, and the _dir_fd_ and _follow_symlinks_ arguments.
Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).
Changed in version 3.13: Added support for a file descriptor and the _follow_symlinks_ argument on Windows.

os.chown(_path_ , _uid_ , _gid_ , _*_ , _dir_fd =None_, _follow_symlinks =True_)[¶](https://docs.python.org/3/library/os.html#os.chown "Link to this definition")

Change the owner and group id of _path_ to the numeric _uid_ and _gid_. To leave one of the ids unchanged, set it to -1.
This function can support [specifying a file descriptor](https://docs.python.org/3/library/os.html#path-fd), [paths relative to directory descriptors](https://docs.python.org/3/library/os.html#dir-fd) and [not following symlinks](https://docs.python.org/3/library/os.html#follow-symlinks).
See [`shutil.chown()`](https://docs.python.org/3/library/shutil.html#shutil.chown "shutil.chown") for a higher-level function that accepts names in addition to numeric ids.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `os.chown` with arguments `path`, `uid`, `gid`, `dir_fd`.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.
The function is limited on WASI, see [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability) for more information.
Changed in version 3.3: Added support for specifying _path_ as an open file descriptor, and the _dir_fd_ and _follow_symlinks_ arguments.
Changed in version 3.6: Supports a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).

os.chroot(_path_)[¶](https://docs.python.org/3/library/os.html#os.chroot "Link to this definition")

Change the root directory of the current process to _path_.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI, not Android.
Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).

os.fchdir(_fd_)[¶](https://docs.python.org/3/library/os.html#os.fchdir "Link to this definition")

Change the current working directory to the directory represented by the file descriptor _fd_. The descriptor must refer to an opened directory, not an open file. As of Python 3.3, this is equivalent to `os.chdir(fd)`.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `os.chdir` with argument `path`.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.

os.getcwd()[¶](https://docs.python.org/3/library/os.html#os.getcwd "Link to this definition")

Return a string representing the current working directory.

os.getcwdb()[¶](https://docs.python.org/3/library/os.html#os.getcwdb "Link to this definition")

Return a bytestring representing the current working directory.
Changed in version 3.8: The function now uses the UTF-8 encoding on Windows, rather than the ANSI code page: see [**PEP 529**](https://peps.python.org/pep-0529/) for the rationale. The function is no longer deprecated on Windows.

os.lchflags(_path_ , _flags_)[¶](https://docs.python.org/3/library/os.html#os.lchflags "Link to this definition")

Set the flags of _path_ to the numeric _flags_ , like [`chflags()`](https://docs.python.org/3/library/os.html#os.chflags "os.chflags"), but do not follow symbolic links. As of Python 3.3, this is equivalent to `os.chflags(path, flags, follow_symlinks=False)`.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `os.chflags` with arguments `path`, `flags`.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI.
Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).

os.lchmod(_path_ , _mode_)[¶](https://docs.python.org/3/library/os.html#os.lchmod "Link to this definition")

Change the mode of _path_ to the numeric _mode_. If path is a symlink, this affects the symlink rather than the target. See the docs for [`chmod()`](https://docs.python.org/3/library/os.html#os.chmod "os.chmod") for possible values of _mode_. As of Python 3.3, this is equivalent to `os.chmod(path, mode, follow_symlinks=False)`.
`lchmod()` is not part of POSIX, but Unix implementations may have it if changing the mode of symbolic links is supported.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `os.chmod` with arguments `path`, `mode`, `dir_fd`.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, Windows, not Linux, FreeBSD >= 1.3, NetBSD >= 1.3, not OpenBSD
Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).
Changed in version 3.13: Added support on Windows.

os.lchown(_path_ , _uid_ , _gid_)[¶](https://docs.python.org/3/library/os.html#os.lchown "Link to this definition")

Change the owner and group id of _path_ to the numeric _uid_ and _gid_. This function will not follow symbolic links. As of Python 3.3, this is equivalent to `os.chown(path, uid, gid, follow_symlinks=False)`.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `os.chown` with arguments `path`, `uid`, `gid`, `dir_fd`.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.
Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).

os.link(_src_ , _dst_ , _*_ , _src_dir_fd =None_, _dst_dir_fd =None_, _follow_symlinks =True_)[¶](https://docs.python.org/3/library/os.html#os.link "Link to this definition")

Create a hard link pointing to _src_ named _dst_.
This function can support specifying _src_dir_fd_ and/or _dst_dir_fd_ to supply [paths relative to directory descriptors](https://docs.python.org/3/library/os.html#dir-fd), and [not following symlinks](https://docs.python.org/3/library/os.html#follow-symlinks). The default value of _follow_symlinks_ is `False` on Windows.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `os.link` with arguments `src`, `dst`, `src_dir_fd`, `dst_dir_fd`.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, Windows.
Changed in version 3.2: Added Windows support.
Changed in version 3.3: Added the _src_dir_fd_ , _dst_dir_fd_ , and _follow_symlinks_ parameters.
Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object) for _src_ and _dst_.

os.listdir(_path ='.'_)[¶](https://docs.python.org/3/library/os.html#os.listdir "Link to this definition")

Return a list containing the names of the entries in the directory given by _path_. The list is in arbitrary order, and does not include the special entries `'.'` and `'..'` even if they are present in the directory. If a file is removed from or added to the directory during the call of this function, whether a name for that file be included is unspecified.
_path_ may be a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object). If _path_ is of type `bytes` (directly or indirectly through the [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "os.PathLike") interface), the filenames returned will also be of type `bytes`; in all other circumstances, they will be of type `str`.
This function can also support [specifying a file descriptor](https://docs.python.org/3/library/os.html#path-fd); the file descriptor must refer to a directory.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `os.listdir` with argument `path`.
Note
To encode `str` filenames to `bytes`, use [`fsencode()`](https://docs.python.org/3/library/os.html#os.fsencode "os.fsencode").
See also
The [`scandir()`](https://docs.python.org/3/library/os.html#os.scandir "os.scandir") function returns directory entries along with file attribute information, giving better performance for many common use cases.
Changed in version 3.2: The _path_ parameter became optional.
Changed in version 3.3: Added support for specifying _path_ as an open file descriptor.
Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).

os.listdrives()[¶](https://docs.python.org/3/library/os.html#os.listdrives "Link to this definition")

Return a list containing the names of drives on a Windows system.
A drive name typically looks like `'C:\\'`. Not every drive name will be associated with a volume, and some may be inaccessible for a variety of reasons, including permissions, network connectivity or missing media. This function does not test for access.
May raise [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") if an error occurs collecting the drive names.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `os.listdrives` with no arguments.
[Availability](https://docs.python.org/3/library/intro.html#availability): Windows
Added in version 3.12.

os.listmounts(_volume_)[¶](https://docs.python.org/3/library/os.html#os.listmounts "Link to this definition")

Return a list containing the mount points for a volume on a Windows system.
_volume_ must be represented as a GUID path, like those returned by [`os.listvolumes()`](https://docs.python.org/3/library/os.html#os.listvolumes "os.listvolumes"). Volumes may be mounted in multiple locations or not at all. In the latter case, the list will be empty. Mount points that are not associated with a volume will not be returned by this function.
The mount points return by this function will be absolute paths, and may be longer than the drive name.
Raises [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") if the volume is not recognized or if an error occurs collecting the paths.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `os.listmounts` with argument `volume`.
[Availability](https://docs.python.org/3/library/intro.html#availability): Windows
Added in version 3.12.

os.listvolumes()[¶](https://docs.python.org/3/library/os.html#os.listvolumes "Link to this definition")

Return a list containing the volumes in the system.
Volumes are typically represented as a GUID path that looks like `\\?\Volume{xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}\`. Files can usually be accessed through a GUID path, permissions allowing. However, users are generally not familiar with them, and so the recommended use of this function is to retrieve mount points using [`os.listmounts()`](https://docs.python.org/3/library/os.html#os.listmounts "os.listmounts").
May raise [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") if an error occurs collecting the volumes.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `os.listvolumes` with no arguments.
[Availability](https://docs.python.org/3/library/intro.html#availability): Windows
Added in version 3.12.

os.lstat(_path_ , _*_ , _dir_fd =None_)[¶](https://docs.python.org/3/library/os.html#os.lstat "Link to this definition")

Perform the equivalent of an `lstat()` system call on the given path. Similar to [`stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat"), but does not follow symbolic links. Return a [`stat_result`](https://docs.python.org/3/library/os.html#os.stat_result "os.stat_result") object.
On platforms that do not support symbolic links, this is an alias for [`stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat").
As of Python 3.3, this is equivalent to `os.stat(path, dir_fd=dir_fd, follow_symlinks=False)`.
This function can also support [paths relative to directory descriptors](https://docs.python.org/3/library/os.html#dir-fd).
See also
The [`stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat") function.
Changed in version 3.2: Added support for Windows 6.0 (Vista) symbolic links.
Changed in version 3.3: Added the _dir_fd_ parameter.
Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).
Changed in version 3.8: On Windows, now opens reparse points that represent another path (name surrogates), including symbolic links and directory junctions. Other kinds of reparse points are resolved by the operating system as for [`stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat").

os.mkdir(_path_ , _mode =0o777_, _*_ , _dir_fd =None_)[¶](https://docs.python.org/3/library/os.html#os.mkdir "Link to this definition")

Create a directory named _path_ with numeric mode _mode_.
If the directory already exists, [`FileExistsError`](https://docs.python.org/3/library/exceptions.html#FileExistsError "FileExistsError") is raised. If a parent directory in the path does not exist, [`FileNotFoundError`](https://docs.python.org/3/library/exceptions.html#FileNotFoundError "FileNotFoundError") is raised.
