
Set the blocking mode of the specified file descriptor. Set the [`O_NONBLOCK`](https://docs.python.org/3/library/os.html#os.O_NONBLOCK "os.O_NONBLOCK") flag if blocking is `False`, clear the flag otherwise.
See also [`get_blocking()`](https://docs.python.org/3/library/os.html#os.get_blocking "os.get_blocking") and [`socket.socket.setblocking()`](https://docs.python.org/3/library/socket.html#socket.socket.setblocking "socket.socket.setblocking").
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, Windows.
The function is limited on WASI, see [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability) for more information.
On Windows, this function is limited to pipes.
Added in version 3.5.
Changed in version 3.12: Added support for pipes on Windows.

os.splice(_src_ , _dst_ , _count_ , _offset_src =None_, _offset_dst =None_, _flags =0_)[¶](https://docs.python.org/3/library/os.html#os.splice "Link to this definition")

Transfer _count_ bytes from file descriptor _src_ , starting from offset _offset_src_ , to file descriptor _dst_ , starting from offset _offset_dst_.
The splicing behaviour can be modified by specifying a _flags_ value. Any of the following variables may used, combined using bitwise OR (the `|` operator):
  * If [`SPLICE_F_MOVE`](https://docs.python.org/3/library/os.html#os.SPLICE_F_MOVE "os.SPLICE_F_MOVE") is specified, the kernel is asked to move pages instead of copying, but pages may still be copied if the kernel cannot move the pages from the pipe.
  * If [`SPLICE_F_NONBLOCK`](https://docs.python.org/3/library/os.html#os.SPLICE_F_NONBLOCK "os.SPLICE_F_NONBLOCK") is specified, the kernel is asked to not block on I/O. This makes the splice pipe operations nonblocking, but splice may nevertheless block because the spliced file descriptors may block.
  * If [`SPLICE_F_MORE`](https://docs.python.org/3/library/os.html#os.SPLICE_F_MORE "os.SPLICE_F_MORE") is specified, it hints to the kernel that more data will be coming in a subsequent splice.


At least one of the file descriptors must refer to a pipe. If _offset_src_ is `None`, then _src_ is read from the current position; respectively for _offset_dst_. The offset associated to the file descriptor that refers to a pipe must be `None`. The files pointed to by _src_ and _dst_ must reside in the same filesystem, otherwise an [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") is raised with [`errno`](https://docs.python.org/3/library/exceptions.html#OSError.errno "OSError.errno") set to [`errno.EXDEV`](https://docs.python.org/3/library/errno.html#errno.EXDEV "errno.EXDEV").
This copy is done without the additional cost of transferring data from the kernel to user space and then back into the kernel. Additionally, some filesystems could implement extra optimizations. The copy is done as if both files are opened as binary.
Upon successful completion, returns the number of bytes spliced to or from the pipe. A return value of 0 means end of input. If _src_ refers to a pipe, then this means that there was no data to transfer, and it would not make sense to block because there are no writers connected to the write end of the pipe.
See also
The
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux >= 2.6.17 with glibc >= 2.5
Added in version 3.10.

os.SPLICE_F_MOVE[¶](https://docs.python.org/3/library/os.html#os.SPLICE_F_MOVE "Link to this definition")


os.SPLICE_F_NONBLOCK[¶](https://docs.python.org/3/library/os.html#os.SPLICE_F_NONBLOCK "Link to this definition")


os.SPLICE_F_MORE[¶](https://docs.python.org/3/library/os.html#os.SPLICE_F_MORE "Link to this definition")

Added in version 3.10.

os.readv(_fd_ , _buffers_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.readv "Link to this definition")

Read from a file descriptor _fd_ into a number of mutable [bytes-like objects](https://docs.python.org/3/glossary.html#term-bytes-like-object) _buffers_. Transfer data into each buffer until it is full and then move on to the next buffer in the sequence to hold the rest of the data.
Return the total number of bytes actually read which can be less than the total capacity of all the objects.
The operating system may set a limit ([`sysconf()`](https://docs.python.org/3/library/os.html#os.sysconf "os.sysconf") value `'SC_IOV_MAX'`) on the number of buffers that can be used.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.
Added in version 3.3.

os.tcgetpgrp(_fd_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.tcgetpgrp "Link to this definition")

Return the process group associated with the terminal given by _fd_ (an open file descriptor as returned by [`os.open()`](https://docs.python.org/3/library/os.html#os.open "os.open")).
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI.

os.tcsetpgrp(_fd_ , _pg_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.tcsetpgrp "Link to this definition")

Set the process group associated with the terminal given by _fd_ (an open file descriptor as returned by [`os.open()`](https://docs.python.org/3/library/os.html#os.open "os.open")) to _pg_.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI.

os.ttyname(_fd_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.ttyname "Link to this definition")

Return a string which specifies the terminal device associated with file descriptor _fd_. If _fd_ is not associated with a terminal device, an exception is raised.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.

os.unlockpt(_fd_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.unlockpt "Link to this definition")

Unlock the slave pseudo-terminal device associated with the master pseudo-terminal device to which the file descriptor _fd_ refers. The file descriptor _fd_ is not closed upon failure.
Calls the C standard library function `unlockpt()`.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI.
Added in version 3.13.

os.write(_fd_ , _str_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.write "Link to this definition")

Write the bytestring in _str_ to file descriptor _fd_.
Return the number of bytes actually written.
Note
This function is intended for low-level I/O and must be applied to a file descriptor as returned by [`os.open()`](https://docs.python.org/3/library/os.html#os.open "os.open") or [`pipe()`](https://docs.python.org/3/library/os.html#os.pipe "os.pipe"). To write a “file object” returned by the built-in function [`open()`](https://docs.python.org/3/library/functions.html#open "open") or by [`popen()`](https://docs.python.org/3/library/os.html#os.popen "os.popen") or [`fdopen()`](https://docs.python.org/3/library/os.html#os.fdopen "os.fdopen"), or [`sys.stdout`](https://docs.python.org/3/library/sys.html#sys.stdout "sys.stdout") or [`sys.stderr`](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr"), use its `write()` method.
Changed in version 3.5: If the system call is interrupted and the signal handler does not raise an exception, the function now retries the system call instead of raising an [`InterruptedError`](https://docs.python.org/3/library/exceptions.html#InterruptedError "InterruptedError") exception (see [**PEP 475**](https://peps.python.org/pep-0475/) for the rationale).

os.writev(_fd_ , _buffers_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.writev "Link to this definition")

Write the contents of _buffers_ to file descriptor _fd_. _buffers_ must be a sequence of [bytes-like objects](https://docs.python.org/3/glossary.html#term-bytes-like-object). Buffers are processed in array order. Entire contents of the first buffer is written before proceeding to the second, and so on.
Returns the total number of bytes actually written.
The operating system may set a limit ([`sysconf()`](https://docs.python.org/3/library/os.html#os.sysconf "os.sysconf") value `'SC_IOV_MAX'`) on the number of buffers that can be used.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.
Added in version 3.3.
### Querying the size of a terminal[¶](https://docs.python.org/3/library/os.html#querying-the-size-of-a-terminal "Link to this heading")
Added in version 3.3.

os.get_terminal_size(_fd =STDOUT_FILENO_, _/_)[¶](https://docs.python.org/3/library/os.html#os.get_terminal_size "Link to this definition")

Return the size of the terminal window as `(columns, lines)`, tuple of type [`terminal_size`](https://docs.python.org/3/library/os.html#os.terminal_size "os.terminal_size").
The optional argument `fd` (default `STDOUT_FILENO`, or standard output) specifies which file descriptor should be queried.
If the file descriptor is not connected to a terminal, an [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") is raised.
[`shutil.get_terminal_size()`](https://docs.python.org/3/library/shutil.html#shutil.get_terminal_size "shutil.get_terminal_size") is the high-level function which should normally be used, `os.get_terminal_size` is the low-level implementation.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, Windows.

_class_ os.terminal_size[¶](https://docs.python.org/3/library/os.html#os.terminal_size "Link to this definition")

A subclass of tuple, holding `(columns, lines)` of the terminal window size.

columns[¶](https://docs.python.org/3/library/os.html#os.terminal_size.columns "Link to this definition")

Width of the terminal window in characters.

lines[¶](https://docs.python.org/3/library/os.html#os.terminal_size.lines "Link to this definition")

Height of the terminal window in characters.
### Inheritance of File Descriptors[¶](https://docs.python.org/3/library/os.html#inheritance-of-file-descriptors "Link to this heading")
Added in version 3.4.
A file descriptor has an “inheritable” flag which indicates if the file descriptor can be inherited by child processes. Since Python 3.4, file descriptors created by Python are non-inheritable by default.
On UNIX, non-inheritable file descriptors are closed in child processes at the execution of a new program, other file descriptors are inherited. Note that non-inheritable file descriptors are still _inherited_ by child processes on [`os.fork()`](https://docs.python.org/3/library/os.html#os.fork "os.fork").
On Windows, non-inheritable handles and file descriptors are closed in child processes, except for standard streams (file descriptors 0, 1 and 2: stdin, stdout and stderr), which are always inherited. Using [`spawn*`](https://docs.python.org/3/library/os.html#os.spawnl "os.spawnl") functions, all inheritable handles and all inheritable file descriptors are inherited. Using the [`subprocess`](https://docs.python.org/3/library/subprocess.html#module-subprocess "subprocess: Subprocess management.") module, all file descriptors except standard streams are closed, and inheritable handles are only inherited if the _close_fds_ parameter is `False`.
On WebAssembly platforms, the file descriptor cannot be modified.

os.get_inheritable(_fd_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.get_inheritable "Link to this definition")

Get the “inheritable” flag of the specified file descriptor (a boolean).

os.set_inheritable(_fd_ , _inheritable_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.set_inheritable "Link to this definition")

Set the “inheritable” flag of the specified file descriptor.

os.get_handle_inheritable(_handle_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.get_handle_inheritable "Link to this definition")

Get the “inheritable” flag of the specified handle (a boolean).
[Availability](https://docs.python.org/3/library/intro.html#availability): Windows.

os.set_handle_inheritable(_handle_ , _inheritable_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.set_handle_inheritable "Link to this definition")

Set the “inheritable” flag of the specified handle.
[Availability](https://docs.python.org/3/library/intro.html#availability): Windows.
