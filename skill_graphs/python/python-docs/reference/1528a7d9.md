
Parameters to the [`lseek()`](https://docs.python.org/3/library/os.html#os.lseek "os.lseek") function and the [`seek()`](https://docs.python.org/3/library/io.html#io.IOBase.seek "io.IOBase.seek") method on [file-like objects](https://docs.python.org/3/glossary.html#term-file-object), for seeking file data and holes on sparsely allocated files.

`SEEK_DATA`

Adjust the file offset to the next location containing data, relative to the seek position.

`SEEK_HOLE`

Adjust the file offset to the next location containing a hole, relative to the seek position. A hole is defined as a sequence of zeros.
Note
These operations only make sense for filesystems that support them.
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux >= 3.1, macOS, Unix
Added in version 3.3.

os.open(_path_ , _flags_ , _mode =0o777_, _*_ , _dir_fd =None_)[¶](https://docs.python.org/3/library/os.html#os.open "Link to this definition")

Open the file _path_ and set various flags according to _flags_ and possibly its mode according to _mode_. When computing _mode_ , the current umask value is first masked out. Return the file descriptor for the newly opened file. The new file descriptor is [non-inheritable](https://docs.python.org/3/library/os.html#fd-inheritance).
For a description of the flag and mode values, see the C run-time documentation; flag constants (like [`O_RDONLY`](https://docs.python.org/3/library/os.html#os.O_RDONLY "os.O_RDONLY") and [`O_WRONLY`](https://docs.python.org/3/library/os.html#os.O_WRONLY "os.O_WRONLY")) are defined in the `os` module. In particular, on Windows adding [`O_BINARY`](https://docs.python.org/3/library/os.html#os.O_BINARY "os.O_BINARY") is needed to open files in binary mode.
This function can support [paths relative to directory descriptors](https://docs.python.org/3/library/os.html#dir-fd) with the _dir_fd_ parameter.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `open` with arguments `path`, `mode`, `flags`.
Changed in version 3.4: The new file descriptor is now non-inheritable.
Note
This function is intended for low-level I/O. For normal usage, use the built-in function `open()`, which returns a [file object](https://docs.python.org/3/glossary.html#term-file-object) with `read()` and `write()` methods (and many more). To wrap a file descriptor in a file object, use [`fdopen()`](https://docs.python.org/3/library/os.html#os.fdopen "os.fdopen").
Changed in version 3.3: Added the _dir_fd_ parameter.
Changed in version 3.5: If the system call is interrupted and the signal handler does not raise an exception, the function now retries the system call instead of raising an [`InterruptedError`](https://docs.python.org/3/library/exceptions.html#InterruptedError "InterruptedError") exception (see [**PEP 475**](https://peps.python.org/pep-0475/) for the rationale).
Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).
The following constants are options for the _flags_ parameter to the [`open()`](https://docs.python.org/3/library/os.html#os.open "os.open") function. They can be combined using the bitwise OR operator `|`. Some of them are not available on all platforms. For descriptions of their availability and use, consult the

os.O_RDONLY[¶](https://docs.python.org/3/library/os.html#os.O_RDONLY "Link to this definition")


os.O_WRONLY[¶](https://docs.python.org/3/library/os.html#os.O_WRONLY "Link to this definition")


os.O_RDWR[¶](https://docs.python.org/3/library/os.html#os.O_RDWR "Link to this definition")


os.O_APPEND[¶](https://docs.python.org/3/library/os.html#os.O_APPEND "Link to this definition")


os.O_CREAT[¶](https://docs.python.org/3/library/os.html#os.O_CREAT "Link to this definition")


os.O_EXCL[¶](https://docs.python.org/3/library/os.html#os.O_EXCL "Link to this definition")


os.O_TRUNC[¶](https://docs.python.org/3/library/os.html#os.O_TRUNC "Link to this definition")

The above constants are available on Unix and Windows.

os.O_DSYNC[¶](https://docs.python.org/3/library/os.html#os.O_DSYNC "Link to this definition")


os.O_RSYNC[¶](https://docs.python.org/3/library/os.html#os.O_RSYNC "Link to this definition")


os.O_SYNC[¶](https://docs.python.org/3/library/os.html#os.O_SYNC "Link to this definition")


os.O_NDELAY[¶](https://docs.python.org/3/library/os.html#os.O_NDELAY "Link to this definition")


os.O_NONBLOCK[¶](https://docs.python.org/3/library/os.html#os.O_NONBLOCK "Link to this definition")


os.O_NOCTTY[¶](https://docs.python.org/3/library/os.html#os.O_NOCTTY "Link to this definition")


os.O_CLOEXEC[¶](https://docs.python.org/3/library/os.html#os.O_CLOEXEC "Link to this definition")

The above constants are only available on Unix.
Changed in version 3.3: Add `O_CLOEXEC` constant.

os.O_BINARY[¶](https://docs.python.org/3/library/os.html#os.O_BINARY "Link to this definition")


os.O_NOINHERIT[¶](https://docs.python.org/3/library/os.html#os.O_NOINHERIT "Link to this definition")


os.O_SHORT_LIVED[¶](https://docs.python.org/3/library/os.html#os.O_SHORT_LIVED "Link to this definition")


os.O_TEMPORARY[¶](https://docs.python.org/3/library/os.html#os.O_TEMPORARY "Link to this definition")


os.O_RANDOM[¶](https://docs.python.org/3/library/os.html#os.O_RANDOM "Link to this definition")


os.O_SEQUENTIAL[¶](https://docs.python.org/3/library/os.html#os.O_SEQUENTIAL "Link to this definition")


os.O_TEXT[¶](https://docs.python.org/3/library/os.html#os.O_TEXT "Link to this definition")

The above constants are only available on Windows.

os.O_EVTONLY[¶](https://docs.python.org/3/library/os.html#os.O_EVTONLY "Link to this definition")


os.O_FSYNC[¶](https://docs.python.org/3/library/os.html#os.O_FSYNC "Link to this definition")


os.O_SYMLINK[¶](https://docs.python.org/3/library/os.html#os.O_SYMLINK "Link to this definition")


os.O_NOFOLLOW_ANY[¶](https://docs.python.org/3/library/os.html#os.O_NOFOLLOW_ANY "Link to this definition")

The above constants are only available on macOS.
Changed in version 3.10: Add `O_EVTONLY`, `O_FSYNC`, `O_SYMLINK` and `O_NOFOLLOW_ANY` constants.

os.O_ASYNC[¶](https://docs.python.org/3/library/os.html#os.O_ASYNC "Link to this definition")


os.O_DIRECT[¶](https://docs.python.org/3/library/os.html#os.O_DIRECT "Link to this definition")


os.O_DIRECTORY[¶](https://docs.python.org/3/library/os.html#os.O_DIRECTORY "Link to this definition")


os.O_NOFOLLOW[¶](https://docs.python.org/3/library/os.html#os.O_NOFOLLOW "Link to this definition")


os.O_NOATIME[¶](https://docs.python.org/3/library/os.html#os.O_NOATIME "Link to this definition")


os.O_PATH[¶](https://docs.python.org/3/library/os.html#os.O_PATH "Link to this definition")


os.O_TMPFILE[¶](https://docs.python.org/3/library/os.html#os.O_TMPFILE "Link to this definition")


os.O_SHLOCK[¶](https://docs.python.org/3/library/os.html#os.O_SHLOCK "Link to this definition")


os.O_EXLOCK[¶](https://docs.python.org/3/library/os.html#os.O_EXLOCK "Link to this definition")

The above constants are extensions and not present if they are not defined by the C library.
Changed in version 3.4: Add `O_PATH` on systems that support it. Add `O_TMPFILE`, only available on Linux Kernel 3.11 or newer.

os.openpty()[¶](https://docs.python.org/3/library/os.html#os.openpty "Link to this definition")

Open a new pseudo-terminal pair. Return a pair of file descriptors `(master, slave)` for the pty and the tty, respectively. The new file descriptors are [non-inheritable](https://docs.python.org/3/library/os.html#fd-inheritance). For a (slightly) more portable approach, use the [`pty`](https://docs.python.org/3/library/pty.html#module-pty "pty: Pseudo-Terminal Handling for Unix.") module.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI.
Changed in version 3.4: The new file descriptors are now non-inheritable.

os.pipe()[¶](https://docs.python.org/3/library/os.html#os.pipe "Link to this definition")

Create a pipe. Return a pair of file descriptors `(r, w)` usable for reading and writing, respectively. The new file descriptor is [non-inheritable](https://docs.python.org/3/library/os.html#fd-inheritance).
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, Windows.
Changed in version 3.4: The new file descriptors are now non-inheritable.

os.pipe2(_flags_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.pipe2 "Link to this definition")

Create a pipe with _flags_ set atomically. _flags_ can be constructed by ORing together one or more of these values: [`O_NONBLOCK`](https://docs.python.org/3/library/os.html#os.O_NONBLOCK "os.O_NONBLOCK"), [`O_CLOEXEC`](https://docs.python.org/3/library/os.html#os.O_CLOEXEC "os.O_CLOEXEC"). Return a pair of file descriptors `(r, w)` usable for reading and writing, respectively.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI.
Added in version 3.3.

os.posix_fallocate(_fd_ , _offset_ , _len_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.posix_fallocate "Link to this definition")

Ensures that enough disk space is allocated for the file specified by _fd_ starting from _offset_ and continuing for _len_ bytes.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.
Added in version 3.3.

os.posix_fadvise(_fd_ , _offset_ , _len_ , _advice_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.posix_fadvise "Link to this definition")

Announces an intention to access data in a specific pattern thus allowing the kernel to make optimizations. The advice applies to the region of the file specified by _fd_ starting at _offset_ and continuing for _len_ bytes. _advice_ is one of [`POSIX_FADV_NORMAL`](https://docs.python.org/3/library/os.html#os.POSIX_FADV_NORMAL "os.POSIX_FADV_NORMAL"), [`POSIX_FADV_SEQUENTIAL`](https://docs.python.org/3/library/os.html#os.POSIX_FADV_SEQUENTIAL "os.POSIX_FADV_SEQUENTIAL"), [`POSIX_FADV_RANDOM`](https://docs.python.org/3/library/os.html#os.POSIX_FADV_RANDOM "os.POSIX_FADV_RANDOM"), [`POSIX_FADV_NOREUSE`](https://docs.python.org/3/library/os.html#os.POSIX_FADV_NOREUSE "os.POSIX_FADV_NOREUSE"), [`POSIX_FADV_WILLNEED`](https://docs.python.org/3/library/os.html#os.POSIX_FADV_WILLNEED "os.POSIX_FADV_WILLNEED") or [`POSIX_FADV_DONTNEED`](https://docs.python.org/3/library/os.html#os.POSIX_FADV_DONTNEED "os.POSIX_FADV_DONTNEED").
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.
Added in version 3.3.

os.POSIX_FADV_NORMAL[¶](https://docs.python.org/3/library/os.html#os.POSIX_FADV_NORMAL "Link to this definition")


os.POSIX_FADV_SEQUENTIAL[¶](https://docs.python.org/3/library/os.html#os.POSIX_FADV_SEQUENTIAL "Link to this definition")


os.POSIX_FADV_RANDOM[¶](https://docs.python.org/3/library/os.html#os.POSIX_FADV_RANDOM "Link to this definition")


os.POSIX_FADV_NOREUSE[¶](https://docs.python.org/3/library/os.html#os.POSIX_FADV_NOREUSE "Link to this definition")


os.POSIX_FADV_WILLNEED[¶](https://docs.python.org/3/library/os.html#os.POSIX_FADV_WILLNEED "Link to this definition")


os.POSIX_FADV_DONTNEED[¶](https://docs.python.org/3/library/os.html#os.POSIX_FADV_DONTNEED "Link to this definition")

Flags that can be used in _advice_ in [`posix_fadvise()`](https://docs.python.org/3/library/os.html#os.posix_fadvise "os.posix_fadvise") that specify the access pattern that is likely to be used.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.
Added in version 3.3.

os.pread(_fd_ , _n_ , _offset_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.pread "Link to this definition")

Read at most _n_ bytes from file descriptor _fd_ at a position of _offset_ , leaving the file offset unchanged.
Return a bytestring containing the bytes read. If the end of the file referred to by _fd_ has been reached, an empty bytes object is returned.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.
Added in version 3.3.

os.posix_openpt(_oflag_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.posix_openpt "Link to this definition")

Open and return a file descriptor for a master pseudo-terminal device.
Calls the C standard library function `posix_openpt()`. The _oflag_ argument is used to set file status flags and file access modes as specified in the manual page of `posix_openpt()` of your system.
The returned file descriptor is [non-inheritable](https://docs.python.org/3/library/os.html#fd-inheritance). If the value [`O_CLOEXEC`](https://docs.python.org/3/library/os.html#os.O_CLOEXEC "os.O_CLOEXEC") is available on the system, it is added to _oflag_.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI.
Added in version 3.13.

os.preadv(_fd_ , _buffers_ , _offset_ , _flags =0_, _/_)[¶](https://docs.python.org/3/library/os.html#os.preadv "Link to this definition")

Read from a file descriptor _fd_ at a position of _offset_ into mutable [bytes-like objects](https://docs.python.org/3/glossary.html#term-bytes-like-object) _buffers_ , leaving the file offset unchanged. Transfer data into each buffer until it is full and then move on to the next buffer in the sequence to hold the rest of the data.
The flags argument contains a bitwise OR of zero or more of the following flags:
  * [`RWF_HIPRI`](https://docs.python.org/3/library/os.html#os.RWF_HIPRI "os.RWF_HIPRI")
  * [`RWF_NOWAIT`](https://docs.python.org/3/library/os.html#os.RWF_NOWAIT "os.RWF_NOWAIT")


Return the total number of bytes actually read which can be less than the total capacity of all the objects.
The operating system may set a limit ([`sysconf()`](https://docs.python.org/3/library/os.html#os.sysconf "os.sysconf") value `'SC_IOV_MAX'`) on the number of buffers that can be used.
Combine the functionality of [`os.readv()`](https://docs.python.org/3/library/os.html#os.readv "os.readv") and [`os.pread()`](https://docs.python.org/3/library/os.html#os.pread "os.pread").
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux >= 2.6.30, FreeBSD >= 6.0, OpenBSD >= 2.7, AIX >= 7.1.
Using flags requires Linux >= 4.6.
Added in version 3.7.

os.RWF_NOWAIT[¶](https://docs.python.org/3/library/os.html#os.RWF_NOWAIT "Link to this definition")

Do not wait for data which is not immediately available. If this flag is specified, the system call will return instantly if it would have to read data from the backing storage or wait for a lock.
If some data was successfully read, it will return the number of bytes read. If no bytes were read, it will return `-1` and set errno to [`errno.EAGAIN`](https://docs.python.org/3/library/errno.html#errno.EAGAIN "errno.EAGAIN").
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux >= 4.14.
Added in version 3.7.

os.RWF_HIPRI[¶](https://docs.python.org/3/library/os.html#os.RWF_HIPRI "Link to this definition")

High priority read/write. Allows block-based filesystems to use polling of the device, which provides lower latency, but may use additional resources.
Currently, on Linux, this feature is usable only on a file descriptor opened using the [`O_DIRECT`](https://docs.python.org/3/library/os.html#os.O_DIRECT "os.O_DIRECT") flag.
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux >= 4.6.
Added in version 3.7.

os.ptsname(_fd_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.ptsname "Link to this definition")

Return the name of the slave pseudo-terminal device associated with the master pseudo-terminal device to which the file descriptor _fd_ refers. The file descriptor _fd_ is not closed upon failure.
Calls the reentrant C standard library function `ptsname_r()` if it is available; otherwise, the C standard library function `ptsname()`, which is not guaranteed to be thread-safe, is called.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI.
Added in version 3.13.

os.pwrite(_fd_ , _str_ , _offset_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.pwrite "Link to this definition")

Write the bytestring in _str_ to file descriptor _fd_ at position of _offset_ , leaving the file offset unchanged.
Return the number of bytes actually written.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.
Added in version 3.3.

os.pwritev(_fd_ , _buffers_ , _offset_ , _flags =0_, _/_)[¶](https://docs.python.org/3/library/os.html#os.pwritev "Link to this definition")

Write the _buffers_ contents to file descriptor _fd_ at an offset _offset_ , leaving the file offset unchanged. _buffers_ must be a sequence of [bytes-like objects](https://docs.python.org/3/glossary.html#term-bytes-like-object). Buffers are processed in array order. Entire contents of the first buffer is written before proceeding to the second, and so on.
The flags argument contains a bitwise OR of zero or more of the following flags:
  * [`RWF_DSYNC`](https://docs.python.org/3/library/os.html#os.RWF_DSYNC "os.RWF_DSYNC")
  * [`RWF_SYNC`](https://docs.python.org/3/library/os.html#os.RWF_SYNC "os.RWF_SYNC")
  * [`RWF_APPEND`](https://docs.python.org/3/library/os.html#os.RWF_APPEND "os.RWF_APPEND")


Return the total number of bytes actually written.
The operating system may set a limit ([`sysconf()`](https://docs.python.org/3/library/os.html#os.sysconf "os.sysconf") value `'SC_IOV_MAX'`) on the number of buffers that can be used.
Combine the functionality of [`os.writev()`](https://docs.python.org/3/library/os.html#os.writev "os.writev") and [`os.pwrite()`](https://docs.python.org/3/library/os.html#os.pwrite "os.pwrite").
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux >= 2.6.30, FreeBSD >= 6.0, OpenBSD >= 2.7, AIX >= 7.1.
Using flags requires Linux >= 4.6.
Added in version 3.7.

os.RWF_DSYNC[¶](https://docs.python.org/3/library/os.html#os.RWF_DSYNC "Link to this definition")

Provide a per-write equivalent of the [`O_DSYNC`](https://docs.python.org/3/library/os.html#os.O_DSYNC "os.O_DSYNC") [`os.open()`](https://docs.python.org/3/library/os.html#os.open "os.open") flag. This flag effect applies only to the data range written by the system call.
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux >= 4.7.
Added in version 3.7.

os.RWF_SYNC[¶](https://docs.python.org/3/library/os.html#os.RWF_SYNC "Link to this definition")

Provide a per-write equivalent of the [`O_SYNC`](https://docs.python.org/3/library/os.html#os.O_SYNC "os.O_SYNC") [`os.open()`](https://docs.python.org/3/library/os.html#os.open "os.open") flag. This flag effect applies only to the data range written by the system call.
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux >= 4.7.
Added in version 3.7.

os.RWF_APPEND[¶](https://docs.python.org/3/library/os.html#os.RWF_APPEND "Link to this definition")

Provide a per-write equivalent of the [`O_APPEND`](https://docs.python.org/3/library/os.html#os.O_APPEND "os.O_APPEND") [`os.open()`](https://docs.python.org/3/library/os.html#os.open "os.open") flag. This flag is meaningful only for [`os.pwritev()`](https://docs.python.org/3/library/os.html#os.pwritev "os.pwritev"), and its effect applies only to the data range written by the system call. The _offset_ argument does not affect the write operation; the data is always appended to the end of the file. However, if the _offset_ argument is `-1`, the current file _offset_ is updated.
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux >= 4.16.
Added in version 3.10.

os.read(_fd_ , _n_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.read "Link to this definition")

Read at most _n_ bytes from file descriptor _fd_.
Return a bytestring containing the bytes read. If the end of the file referred to by _fd_ has been reached, an empty bytes object is returned.
Note
This function is intended for low-level I/O and must be applied to a file descriptor as returned by [`os.open()`](https://docs.python.org/3/library/os.html#os.open "os.open") or [`pipe()`](https://docs.python.org/3/library/os.html#os.pipe "os.pipe"). To read a “file object” returned by the built-in function [`open()`](https://docs.python.org/3/library/functions.html#open "open") or by [`popen()`](https://docs.python.org/3/library/os.html#os.popen "os.popen") or [`fdopen()`](https://docs.python.org/3/library/os.html#os.fdopen "os.fdopen"), or [`sys.stdin`](https://docs.python.org/3/library/sys.html#sys.stdin "sys.stdin"), use its `read()` or `readline()` methods.
Changed in version 3.5: If the system call is interrupted and the signal handler does not raise an exception, the function now retries the system call instead of raising an [`InterruptedError`](https://docs.python.org/3/library/exceptions.html#InterruptedError "InterruptedError") exception (see [**PEP 475**](https://peps.python.org/pep-0475/) for the rationale).

os.readinto(_fd_ , _buffer_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.readinto "Link to this definition")

Read from a file descriptor _fd_ into a mutable [buffer object](https://docs.python.org/3/c-api/buffer.html#bufferobjects) _buffer_.
The _buffer_ should be mutable and [bytes-like](https://docs.python.org/3/glossary.html#term-bytes-like-object). On success, returns the number of bytes read. Less bytes may be read than the size of the buffer. The underlying system call will be retried when interrupted by a signal, unless the signal handler raises an exception. Other errors will not be retried and an error will be raised.
Returns 0 if _fd_ is at end of file or if the provided _buffer_ has length 0 (which can be used to check for errors without reading data). Never returns negative.
Note
This function is intended for low-level I/O and must be applied to a file descriptor as returned by [`os.open()`](https://docs.python.org/3/library/os.html#os.open "os.open") or [`os.pipe()`](https://docs.python.org/3/library/os.html#os.pipe "os.pipe"). To read a “file object” returned by the built-in function [`open()`](https://docs.python.org/3/library/functions.html#open "open"), or [`sys.stdin`](https://docs.python.org/3/library/sys.html#sys.stdin "sys.stdin"), use its member functions, for example [`io.BufferedIOBase.readinto()`](https://docs.python.org/3/library/io.html#io.BufferedIOBase.readinto "io.BufferedIOBase.readinto"), [`io.BufferedIOBase.read()`](https://docs.python.org/3/library/io.html#io.BufferedIOBase.read "io.BufferedIOBase.read"), or [`io.TextIOBase.read()`](https://docs.python.org/3/library/io.html#io.TextIOBase.read "io.TextIOBase.read")
Added in version 3.14.

os.sendfile(_out_fd_ , _in_fd_ , _offset_ , _count_)[¶](https://docs.python.org/3/library/os.html#os.sendfile "Link to this definition")


os.sendfile(_out_fd_ , _in_fd_ , _offset_ , _count_ , _headers =()_, _trailers =()_, _flags =0_)

Copy _count_ bytes from file descriptor _in_fd_ to file descriptor _out_fd_ starting at _offset_. Return the number of bytes sent. When EOF is reached return `0`.
The first function notation is supported by all platforms that define `sendfile()`.
On Linux, if _offset_ is given as `None`, the bytes are read from the current position of _in_fd_ and the position of _in_fd_ is updated.
The second case may be used on macOS and FreeBSD where _headers_ and _trailers_ are arbitrary sequences of buffers that are written before and after the data from _in_fd_ is written. It returns the same as the first case.
On macOS and FreeBSD, a value of `0` for _count_ specifies to send until the end of _in_fd_ is reached.
All platforms support sockets as _out_fd_ file descriptor, and some platforms allow other types (e.g. regular file, pipe) as well.
Cross-platform applications should not use _headers_ , _trailers_ and _flags_ arguments.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI.
Note
For a higher-level wrapper of `sendfile()`, see [`socket.socket.sendfile()`](https://docs.python.org/3/library/socket.html#socket.socket.sendfile "socket.socket.sendfile").
Added in version 3.3.
Changed in version 3.9: Parameters _out_ and _in_ was renamed to _out_fd_ and _in_fd_.

os.SF_NODISKIO[¶](https://docs.python.org/3/library/os.html#os.SF_NODISKIO "Link to this definition")


os.SF_MNOWAIT[¶](https://docs.python.org/3/library/os.html#os.SF_MNOWAIT "Link to this definition")


os.SF_SYNC[¶](https://docs.python.org/3/library/os.html#os.SF_SYNC "Link to this definition")

Parameters to the [`sendfile()`](https://docs.python.org/3/library/os.html#os.sendfile "os.sendfile") function, if the implementation supports them.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI.
Added in version 3.3.

os.SF_NOCACHE[¶](https://docs.python.org/3/library/os.html#os.SF_NOCACHE "Link to this definition")

Parameter to the [`sendfile()`](https://docs.python.org/3/library/os.html#os.sendfile "os.sendfile") function, if the implementation supports it. The data won’t be cached in the virtual memory and will be freed afterwards.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI.
Added in version 3.11.

os.set_blocking(_fd_ , _blocking_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.set_blocking "Link to this definition")
