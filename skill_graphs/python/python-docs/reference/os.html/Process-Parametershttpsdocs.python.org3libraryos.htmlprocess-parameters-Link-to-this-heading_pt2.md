
Set the current process’s real and effective group ids.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI, not Android.

os.setresgid(_rgid_ , _egid_ , _sgid_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.setresgid "Link to this definition")

Set the current process’s real, effective, and saved group ids.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI, not Android.
Added in version 3.2.

os.setresuid(_ruid_ , _euid_ , _suid_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.setresuid "Link to this definition")

Set the current process’s real, effective, and saved user ids.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI, not Android.
Added in version 3.2.

os.setreuid(_ruid_ , _euid_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.setreuid "Link to this definition")

Set the current process’s real and effective user ids.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI, not Android.

os.getsid(_pid_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.getsid "Link to this definition")

Call the system call `getsid()`. See the Unix manual for the semantics.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI.

os.setsid()[¶](https://docs.python.org/3/library/os.html#os.setsid "Link to this definition")

Call the system call `setsid()`. See the Unix manual for the semantics.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI.

os.setuid(_uid_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.setuid "Link to this definition")

Set the current process’s user id.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI, not Android.

os.strerror(_code_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.strerror "Link to this definition")

Return the error message corresponding to the error code in _code_. On platforms where `strerror()` returns `NULL` when given an unknown error number, [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised.

os.supports_bytes_environ[¶](https://docs.python.org/3/library/os.html#os.supports_bytes_environ "Link to this definition")

`True` if the native OS type of the environment is bytes (eg. `False` on Windows).
Added in version 3.2.

os.umask(_mask_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.umask "Link to this definition")

Set the current numeric umask and return the previous umask.
The function is a stub on WASI, see [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability) for more information.

os.uname()[¶](https://docs.python.org/3/library/os.html#os.uname "Link to this definition")

Returns information identifying the current operating system. The return value is an object with five attributes:
  * `sysname` - operating system name
  * `nodename` - name of machine on network (implementation-defined)
  * `release` - operating system release
  * `version` - operating system version
  * `machine` - hardware identifier


For backwards compatibility, this object is also iterable, behaving like a five-tuple containing `sysname`, `nodename`, `release`, `version`, and `machine` in that order.
Some systems truncate `nodename` to 8 characters or to the leading component; a better way to get the hostname is [`socket.gethostname()`](https://docs.python.org/3/library/socket.html#socket.gethostname "socket.gethostname") or even `socket.gethostbyaddr(socket.gethostname())`.
On macOS, iOS and Android, this returns the _kernel_ name and version (i.e., `'Darwin'` on macOS and iOS; `'Linux'` on Android). [`platform.uname()`](https://docs.python.org/3/library/platform.html#platform.uname "platform.uname") can be used to get the user-facing operating system name and version on iOS and Android.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.
Changed in version 3.3: Return type changed from a tuple to a tuple-like object with named attributes.

os.unsetenv(_key_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.unsetenv "Link to this definition")

Unset (delete) the environment variable named _key_. Such changes to the environment affect subprocesses started with [`os.system()`](https://docs.python.org/3/library/os.html#os.system "os.system"), [`popen()`](https://docs.python.org/3/library/os.html#os.popen "os.popen") or [`fork()`](https://docs.python.org/3/library/os.html#os.fork "os.fork") and [`execv()`](https://docs.python.org/3/library/os.html#os.execv "os.execv").
Deletion of items in [`os.environ`](https://docs.python.org/3/library/os.html#os.environ "os.environ") is automatically translated into a corresponding call to `unsetenv()`; however, calls to `unsetenv()` don’t update `os.environ`, so it is actually preferable to delete items of `os.environ`.
See also the [`os.reload_environ()`](https://docs.python.org/3/library/os.html#os.reload_environ "os.reload_environ") function.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `os.unsetenv` with argument `key`.
Changed in version 3.9: The function is now always available and is also available on Windows.

os.unshare(_flags_)[¶](https://docs.python.org/3/library/os.html#os.unshare "Link to this definition")

Disassociate parts of the process execution context, and move them into a newly created namespace. See the _flags_ argument is a bit mask, combining zero or more of the [CLONE_* constants](https://docs.python.org/3/library/os.html#os-unshare-clone-flags), that specifies which parts of the execution context should be unshared from their existing associations and moved to a new namespace. If the _flags_ argument is `0`, no changes are made to the calling process’s execution context.
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux >= 2.6.16.
Added in version 3.12.
See also
The [`setns()`](https://docs.python.org/3/library/os.html#os.setns "os.setns") function.
Flags to the [`unshare()`](https://docs.python.org/3/library/os.html#os.unshare "os.unshare") function, if the implementation supports them. See

os.CLONE_FILES[¶](https://docs.python.org/3/library/os.html#os.CLONE_FILES "Link to this definition")


os.CLONE_FS[¶](https://docs.python.org/3/library/os.html#os.CLONE_FS "Link to this definition")


os.CLONE_NEWCGROUP[¶](https://docs.python.org/3/library/os.html#os.CLONE_NEWCGROUP "Link to this definition")


os.CLONE_NEWIPC[¶](https://docs.python.org/3/library/os.html#os.CLONE_NEWIPC "Link to this definition")


os.CLONE_NEWNET[¶](https://docs.python.org/3/library/os.html#os.CLONE_NEWNET "Link to this definition")


os.CLONE_NEWNS[¶](https://docs.python.org/3/library/os.html#os.CLONE_NEWNS "Link to this definition")


os.CLONE_NEWPID[¶](https://docs.python.org/3/library/os.html#os.CLONE_NEWPID "Link to this definition")


os.CLONE_NEWTIME[¶](https://docs.python.org/3/library/os.html#os.CLONE_NEWTIME "Link to this definition")


os.CLONE_NEWUSER[¶](https://docs.python.org/3/library/os.html#os.CLONE_NEWUSER "Link to this definition")


os.CLONE_NEWUTS[¶](https://docs.python.org/3/library/os.html#os.CLONE_NEWUTS "Link to this definition")


os.CLONE_SIGHAND[¶](https://docs.python.org/3/library/os.html#os.CLONE_SIGHAND "Link to this definition")


os.CLONE_SYSVSEM[¶](https://docs.python.org/3/library/os.html#os.CLONE_SYSVSEM "Link to this definition")


os.CLONE_THREAD[¶](https://docs.python.org/3/library/os.html#os.CLONE_THREAD "Link to this definition")


os.CLONE_VM[¶](https://docs.python.org/3/library/os.html#os.CLONE_VM "Link to this definition")

## File Object Creation[¶](https://docs.python.org/3/library/os.html#file-object-creation "Link to this heading")
These functions create new [file objects](https://docs.python.org/3/glossary.html#term-file-object). (See also [`open()`](https://docs.python.org/3/library/os.html#os.open "os.open") for opening file descriptors.)

os.fdopen(_fd_ , _* args_, _** kwargs_)[¶](https://docs.python.org/3/library/os.html#os.fdopen "Link to this definition")

Return an open file object connected to the file descriptor _fd_. This is an alias of the [`open()`](https://docs.python.org/3/library/functions.html#open "open") built-in function and accepts the same arguments. The only difference is that the first argument of `fdopen()` must always be an integer.
## File Descriptor Operations[¶](https://docs.python.org/3/library/os.html#file-descriptor-operations "Link to this heading")
These functions operate on I/O streams referenced using file descriptors.
File descriptors are small integers corresponding to a file that has been opened by the current process. For example, standard input is usually file descriptor 0, standard output is 1, and standard error is 2. Further files opened by a process will then be assigned 3, 4, 5, and so forth. The name “file descriptor” is slightly deceptive; on Unix platforms, sockets and pipes are also referenced by file descriptors.
The [`fileno()`](https://docs.python.org/3/library/io.html#io.IOBase.fileno "io.IOBase.fileno") method can be used to obtain the file descriptor associated with a [file object](https://docs.python.org/3/glossary.html#term-file-object) when required. Note that using the file descriptor directly will bypass the file object methods, ignoring aspects such as internal buffering of data.

os.close(_fd_)[¶](https://docs.python.org/3/library/os.html#os.close "Link to this definition")

Close file descriptor _fd_.
Note
This function is intended for low-level I/O and must be applied to a file descriptor as returned by [`os.open()`](https://docs.python.org/3/library/os.html#os.open "os.open") or [`pipe()`](https://docs.python.org/3/library/os.html#os.pipe "os.pipe"). To close a “file object” returned by the built-in function [`open()`](https://docs.python.org/3/library/functions.html#open "open") or by [`popen()`](https://docs.python.org/3/library/os.html#os.popen "os.popen") or [`fdopen()`](https://docs.python.org/3/library/os.html#os.fdopen "os.fdopen"), use its [`close()`](https://docs.python.org/3/library/io.html#io.IOBase.close "io.IOBase.close") method.

os.closerange(_fd_low_ , _fd_high_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.closerange "Link to this definition")

Close all file descriptors from _fd_low_ (inclusive) to _fd_high_ (exclusive), ignoring errors. Equivalent to (but much faster than):
Copy```
for fd in range(fd_low, fd_high):
    try:
        os.close(fd)
    except OSError:
        pass

```


os.copy_file_range(_src_ , _dst_ , _count_ , _offset_src =None_, _offset_dst =None_)[¶](https://docs.python.org/3/library/os.html#os.copy_file_range "Link to this definition")

Copy _count_ bytes from file descriptor _src_ , starting from offset _offset_src_ , to file descriptor _dst_ , starting from offset _offset_dst_. If _offset_src_ is `None`, then _src_ is read from the current position; respectively for _offset_dst_.
In Linux kernel older than 5.3, the files pointed to by _src_ and _dst_ must reside in the same filesystem, otherwise an [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") is raised with [`errno`](https://docs.python.org/3/library/exceptions.html#OSError.errno "OSError.errno") set to [`errno.EXDEV`](https://docs.python.org/3/library/errno.html#errno.EXDEV "errno.EXDEV").
This copy is done without the additional cost of transferring data from the kernel to user space and then back into the kernel. Additionally, some filesystems could implement extra optimizations, such as the use of reflinks (i.e., two or more inodes that share pointers to the same copy-on-write disk blocks; supported file systems include btrfs and XFS) and server-side copy (in the case of NFS).
The function copies bytes between two file descriptors. Text options, like the encoding and the line ending, are ignored.
The return value is the amount of bytes copied. This could be less than the amount requested.
Note
On Linux, [`os.copy_file_range()`](https://docs.python.org/3/library/os.html#os.copy_file_range "os.copy_file_range") should not be used for copying a range of a pseudo file from a special filesystem like procfs and sysfs. It will always copy no bytes and return 0 as if the file was empty because of a known Linux kernel issue.
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux >= 4.5 with glibc >= 2.27.
Added in version 3.8.

os.device_encoding(_fd_)[¶](https://docs.python.org/3/library/os.html#os.device_encoding "Link to this definition")

Return a string describing the encoding of the device associated with _fd_ if it is connected to a terminal; else return [`None`](https://docs.python.org/3/library/constants.html#None "None").
On Unix, if the [Python UTF-8 Mode](https://docs.python.org/3/library/os.html#utf8-mode) is enabled, return `'UTF-8'` rather than the device encoding.
Changed in version 3.10: On Unix, the function now implements the Python UTF-8 Mode.

os.dup(_fd_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.dup "Link to this definition")

Return a duplicate of file descriptor _fd_. The new file descriptor is [non-inheritable](https://docs.python.org/3/library/os.html#fd-inheritance).
On Windows, when duplicating a standard stream (0: stdin, 1: stdout, 2: stderr), the new file descriptor is [inheritable](https://docs.python.org/3/library/os.html#fd-inheritance).
[Availability](https://docs.python.org/3/library/intro.html#availability): not WASI.
Changed in version 3.4: The new file descriptor is now non-inheritable.

os.dup2(_fd_ , _fd2_ , _inheritable =True_)[¶](https://docs.python.org/3/library/os.html#os.dup2 "Link to this definition")

Duplicate file descriptor _fd_ to _fd2_ , closing the latter first if necessary. Return _fd2_. The new file descriptor is [inheritable](https://docs.python.org/3/library/os.html#fd-inheritance) by default or non-inheritable if _inheritable_ is `False`.
[Availability](https://docs.python.org/3/library/intro.html#availability): not WASI.
Changed in version 3.4: Add the optional _inheritable_ parameter.
Changed in version 3.7: Return _fd2_ on success. Previously, `None` was always returned.

os.fchmod(_fd_ , _mode_)[¶](https://docs.python.org/3/library/os.html#os.fchmod "Link to this definition")

Change the mode of the file given by _fd_ to the numeric _mode_. See the docs for [`chmod()`](https://docs.python.org/3/library/os.html#os.chmod "os.chmod") for possible values of _mode_. As of Python 3.3, this is equivalent to `os.chmod(fd, mode)`.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `os.chmod` with arguments `path`, `mode`, `dir_fd`.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, Windows.
The function is limited on WASI, see [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability) for more information.
Changed in version 3.13: Added support on Windows.

os.fchown(_fd_ , _uid_ , _gid_)[¶](https://docs.python.org/3/library/os.html#os.fchown "Link to this definition")

Change the owner and group id of the file given by _fd_ to the numeric _uid_ and _gid_. To leave one of the ids unchanged, set it to -1. See [`chown()`](https://docs.python.org/3/library/os.html#os.chown "os.chown"). As of Python 3.3, this is equivalent to `os.chown(fd, uid, gid)`.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `os.chown` with arguments `path`, `uid`, `gid`, `dir_fd`.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.
The function is limited on WASI, see [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability) for more information.

os.fdatasync(_fd_)[¶](https://docs.python.org/3/library/os.html#os.fdatasync "Link to this definition")

Force write of file with filedescriptor _fd_ to disk. Does not force update of metadata.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.
Note
This function is not available on MacOS.

os.fpathconf(_fd_ , _name_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.fpathconf "Link to this definition")

Return system configuration information relevant to an open file. _name_ specifies the configuration value to retrieve; it may be a string which is the name of a defined system value; these names are specified in a number of standards (POSIX.1, Unix 95, Unix 98, and others). Some platforms define additional names as well. The names known to the host operating system are given in the `pathconf_names` dictionary. For configuration variables not included in that mapping, passing an integer for _name_ is also accepted.
If _name_ is a string and is not known, [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised. If a specific value for _name_ is not supported by the host system, even if it is included in `pathconf_names`, an [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") is raised with [`errno.EINVAL`](https://docs.python.org/3/library/errno.html#errno.EINVAL "errno.EINVAL") for the error number.
As of Python 3.3, this is equivalent to `os.pathconf(fd, name)`.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.

os.fstat(_fd_)[¶](https://docs.python.org/3/library/os.html#os.fstat "Link to this definition")

Get the status of the file descriptor _fd_. Return a [`stat_result`](https://docs.python.org/3/library/os.html#os.stat_result "os.stat_result") object.
As of Python 3.3, this is equivalent to `os.stat(fd)`.
See also
The [`stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat") function.

os.fstatvfs(_fd_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.fstatvfs "Link to this definition")

Return information about the filesystem containing the file associated with file descriptor _fd_ , like [`statvfs()`](https://docs.python.org/3/library/os.html#os.statvfs "os.statvfs"). As of Python 3.3, this is equivalent to `os.statvfs(fd)`.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.

os.fsync(_fd_)[¶](https://docs.python.org/3/library/os.html#os.fsync "Link to this definition")

Force write of file with filedescriptor _fd_ to disk. On Unix, this calls the native `fsync()` function; on Windows, the MS `_commit()` function.
If you’re starting with a buffered Python [file object](https://docs.python.org/3/glossary.html#term-file-object) _f_ , first do `f.flush()`, and then do `os.fsync(f.fileno())`, to ensure that all internal buffers associated with _f_ are written to disk.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, Windows.

os.ftruncate(_fd_ , _length_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.ftruncate "Link to this definition")

Truncate the file corresponding to file descriptor _fd_ , so that it is at most _length_ bytes in size. As of Python 3.3, this is equivalent to `os.truncate(fd, length)`.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `os.truncate` with arguments `fd`, `length`.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, Windows.
Changed in version 3.5: Added support for Windows

os.get_blocking(_fd_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.get_blocking "Link to this definition")

Get the blocking mode of the file descriptor: `False` if the [`O_NONBLOCK`](https://docs.python.org/3/library/os.html#os.O_NONBLOCK "os.O_NONBLOCK") flag is set, `True` if the flag is cleared.
See also [`set_blocking()`](https://docs.python.org/3/library/os.html#os.set_blocking "os.set_blocking") and [`socket.socket.setblocking()`](https://docs.python.org/3/library/socket.html#socket.socket.setblocking "socket.socket.setblocking").
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, Windows.
The function is limited on WASI, see [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability) for more information.
On Windows, this function is limited to pipes.
Added in version 3.5.
Changed in version 3.12: Added support for pipes on Windows.

os.grantpt(_fd_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.grantpt "Link to this definition")

Grant access to the slave pseudo-terminal device associated with the master pseudo-terminal device to which the file descriptor _fd_ refers. The file descriptor _fd_ is not closed upon failure.
Calls the C standard library function `grantpt()`.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI.
Added in version 3.13.

os.isatty(_fd_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.isatty "Link to this definition")

Return `True` if the file descriptor _fd_ is open and connected to a tty(-like) device, else `False`.

os.lockf(_fd_ , _cmd_ , _len_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.lockf "Link to this definition")

Apply, test or remove a POSIX lock on an open file descriptor. _fd_ is an open file descriptor. _cmd_ specifies the command to use - one of [`F_LOCK`](https://docs.python.org/3/library/os.html#os.F_LOCK "os.F_LOCK"), [`F_TLOCK`](https://docs.python.org/3/library/os.html#os.F_TLOCK "os.F_TLOCK"), [`F_ULOCK`](https://docs.python.org/3/library/os.html#os.F_ULOCK "os.F_ULOCK") or [`F_TEST`](https://docs.python.org/3/library/os.html#os.F_TEST "os.F_TEST"). _len_ specifies the section of the file to lock.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `os.lockf` with arguments `fd`, `cmd`, `len`.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.
Added in version 3.3.

os.F_LOCK[¶](https://docs.python.org/3/library/os.html#os.F_LOCK "Link to this definition")


os.F_TLOCK[¶](https://docs.python.org/3/library/os.html#os.F_TLOCK "Link to this definition")


os.F_ULOCK[¶](https://docs.python.org/3/library/os.html#os.F_ULOCK "Link to this definition")


os.F_TEST[¶](https://docs.python.org/3/library/os.html#os.F_TEST "Link to this definition")

Flags that specify what action [`lockf()`](https://docs.python.org/3/library/os.html#os.lockf "os.lockf") will take.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.
Added in version 3.3.

os.login_tty(_fd_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.login_tty "Link to this definition")

Prepare the tty of which fd is a file descriptor for a new login session. Make the calling process a session leader; make the tty the controlling tty, the stdin, the stdout, and the stderr of the calling process; close fd.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI.
Added in version 3.11.

os.lseek(_fd_ , _pos_ , _whence_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.lseek "Link to this definition")

Set the current position of file descriptor _fd_ to position _pos_ , modified by _whence_ , and return the new position in bytes relative to the start of the file. Valid values for _whence_ are:
  * [`SEEK_SET`](https://docs.python.org/3/library/os.html#os.SEEK_SET "os.SEEK_SET") or `0` – set _pos_ relative to the beginning of the file
  * [`SEEK_CUR`](https://docs.python.org/3/library/os.html#os.SEEK_CUR "os.SEEK_CUR") or `1` – set _pos_ relative to the current file position
  * [`SEEK_END`](https://docs.python.org/3/library/os.html#os.SEEK_END "os.SEEK_END") or `2` – set _pos_ relative to the end of the file
  * [`SEEK_HOLE`](https://docs.python.org/3/library/os.html#os.SEEK_HOLE "os.SEEK_HOLE") – set _pos_ to the next data location, relative to _pos_
  * [`SEEK_DATA`](https://docs.python.org/3/library/os.html#os.SEEK_DATA "os.SEEK_DATA") – set _pos_ to the next data hole, relative to _pos_


Changed in version 3.3: Add support for `SEEK_HOLE` and `SEEK_DATA`.

os.SEEK_SET[¶](https://docs.python.org/3/library/os.html#os.SEEK_SET "Link to this definition")


os.SEEK_CUR[¶](https://docs.python.org/3/library/os.html#os.SEEK_CUR "Link to this definition")


os.SEEK_END[¶](https://docs.python.org/3/library/os.html#os.SEEK_END "Link to this definition")

Parameters to the [`lseek()`](https://docs.python.org/3/library/os.html#os.lseek "os.lseek") function and the [`seek()`](https://docs.python.org/3/library/io.html#io.IOBase.seek "io.IOBase.seek") method on [file-like objects](https://docs.python.org/3/glossary.html#term-file-object), for whence to adjust the file position indicator.

[`SEEK_SET`](https://docs.python.org/3/library/os.html#os.SEEK_SET "os.SEEK_SET")

Adjust the file position relative to the beginning of the file.

[`SEEK_CUR`](https://docs.python.org/3/library/os.html#os.SEEK_CUR "os.SEEK_CUR")

Adjust the file position relative to the current file position.

[`SEEK_END`](https://docs.python.org/3/library/os.html#os.SEEK_END "os.SEEK_END")

Adjust the file position relative to the end of the file.
Their values are 0, 1, and 2, respectively.

os.SEEK_HOLE[¶](https://docs.python.org/3/library/os.html#os.SEEK_HOLE "Link to this definition")


os.SEEK_DATA[¶](https://docs.python.org/3/library/os.html#os.SEEK_DATA "Link to this definition")
