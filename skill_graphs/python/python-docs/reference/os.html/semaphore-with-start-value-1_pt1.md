# semaphore with start value '1'
fd = os.eventfd(1, os.EFD_SEMAPHORE | os.EFD_CLOEXEC)
try:
    # acquire semaphore
    v = os.eventfd_read(fd)
    try:
        do_work()
    finally:
        # release semaphore
        os.eventfd_write(fd, v)
finally:
    os.close(fd)

```

[Availability](https://docs.python.org/3/library/intro.html#availability): Linux >= 2.6.27 with glibc >= 2.8
Added in version 3.10.

os.eventfd_read(_fd_)[¶](https://docs.python.org/3/library/os.html#os.eventfd_read "Link to this definition")

Read value from an [`eventfd()`](https://docs.python.org/3/library/os.html#os.eventfd "os.eventfd") file descriptor and return a 64 bit unsigned int. The function does not verify that _fd_ is an `eventfd()`.
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux >= 2.6.27
Added in version 3.10.

os.eventfd_write(_fd_ , _value_)[¶](https://docs.python.org/3/library/os.html#os.eventfd_write "Link to this definition")

Add value to an [`eventfd()`](https://docs.python.org/3/library/os.html#os.eventfd "os.eventfd") file descriptor. _value_ must be a 64 bit unsigned int. The function does not verify that _fd_ is an `eventfd()`.
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux >= 2.6.27
Added in version 3.10.

os.EFD_CLOEXEC[¶](https://docs.python.org/3/library/os.html#os.EFD_CLOEXEC "Link to this definition")

Set close-on-exec flag for new [`eventfd()`](https://docs.python.org/3/library/os.html#os.eventfd "os.eventfd") file descriptor.
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux >= 2.6.27
Added in version 3.10.

os.EFD_NONBLOCK[¶](https://docs.python.org/3/library/os.html#os.EFD_NONBLOCK "Link to this definition")

Set [`O_NONBLOCK`](https://docs.python.org/3/library/os.html#os.O_NONBLOCK "os.O_NONBLOCK") status flag for new [`eventfd()`](https://docs.python.org/3/library/os.html#os.eventfd "os.eventfd") file descriptor.
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux >= 2.6.27
Added in version 3.10.

os.EFD_SEMAPHORE[¶](https://docs.python.org/3/library/os.html#os.EFD_SEMAPHORE "Link to this definition")

Provide semaphore-like semantics for reads from an [`eventfd()`](https://docs.python.org/3/library/os.html#os.eventfd "os.eventfd") file descriptor. On read the internal counter is decremented by one.
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux >= 2.6.30
Added in version 3.10.
### Timer File Descriptors[¶](https://docs.python.org/3/library/os.html#timer-file-descriptors "Link to this heading")
Added in version 3.13.
These functions provide support for Linux’s _timer file descriptor_ API. Naturally, they are all only available on Linux.

os.timerfd_create(_clockid_ , _/_ , _*_ , _flags =0_)[¶](https://docs.python.org/3/library/os.html#os.timerfd_create "Link to this definition")

Create and return a timer file descriptor (_timerfd_).
The file descriptor returned by `timerfd_create()` supports:
  * [`read()`](https://docs.python.org/3/library/os.html#os.read "os.read")
  * [`select()`](https://docs.python.org/3/library/select.html#select.select "select.select")
  * [`poll()`](https://docs.python.org/3/library/select.html#select.poll "select.poll")


The file descriptor’s [`read()`](https://docs.python.org/3/library/os.html#os.read "os.read") method can be called with a buffer size of 8. If the timer has already expired one or more times, `read()` returns the number of expirations with the host’s endianness, which may be converted to an [`int`](https://docs.python.org/3/library/functions.html#int "int") by `int.from_bytes(x, byteorder=sys.byteorder)`.
[`select()`](https://docs.python.org/3/library/select.html#select.select "select.select") and [`poll()`](https://docs.python.org/3/library/select.html#select.poll "select.poll") can be used to wait until timer expires and the file descriptor is readable.
_clockid_ must be a valid [clock ID](https://docs.python.org/3/library/time.html#time-clock-id-constants), as defined in the [`time`](https://docs.python.org/3/library/time.html#module-time "time: Time access and conversions.") module:
  * [`time.CLOCK_REALTIME`](https://docs.python.org/3/library/time.html#time.CLOCK_REALTIME "time.CLOCK_REALTIME")
  * [`time.CLOCK_MONOTONIC`](https://docs.python.org/3/library/time.html#time.CLOCK_MONOTONIC "time.CLOCK_MONOTONIC")
  * [`time.CLOCK_BOOTTIME`](https://docs.python.org/3/library/time.html#time.CLOCK_BOOTTIME "time.CLOCK_BOOTTIME") (Since Linux 3.15 for timerfd_create)


If _clockid_ is [`time.CLOCK_REALTIME`](https://docs.python.org/3/library/time.html#time.CLOCK_REALTIME "time.CLOCK_REALTIME"), a settable system-wide real-time clock is used. If system clock is changed, timer setting need to be updated. To cancel timer when system clock is changed, see [`TFD_TIMER_CANCEL_ON_SET`](https://docs.python.org/3/library/os.html#os.TFD_TIMER_CANCEL_ON_SET "os.TFD_TIMER_CANCEL_ON_SET").
If _clockid_ is [`time.CLOCK_MONOTONIC`](https://docs.python.org/3/library/time.html#time.CLOCK_MONOTONIC "time.CLOCK_MONOTONIC"), a non-settable monotonically increasing clock is used. Even if the system clock is changed, the timer setting will not be affected.
If _clockid_ is [`time.CLOCK_BOOTTIME`](https://docs.python.org/3/library/time.html#time.CLOCK_BOOTTIME "time.CLOCK_BOOTTIME"), same as [`time.CLOCK_MONOTONIC`](https://docs.python.org/3/library/time.html#time.CLOCK_MONOTONIC "time.CLOCK_MONOTONIC") except it includes any time that the system is suspended.
The file descriptor’s behaviour can be modified by specifying a _flags_ value. Any of the following variables may be used, combined using bitwise OR (the `|` operator):
  * [`TFD_NONBLOCK`](https://docs.python.org/3/library/os.html#os.TFD_NONBLOCK "os.TFD_NONBLOCK")
  * [`TFD_CLOEXEC`](https://docs.python.org/3/library/os.html#os.TFD_CLOEXEC "os.TFD_CLOEXEC")


If [`TFD_NONBLOCK`](https://docs.python.org/3/library/os.html#os.TFD_NONBLOCK "os.TFD_NONBLOCK") is not set as a flag, [`read()`](https://docs.python.org/3/library/os.html#os.read "os.read") blocks until the timer expires. If it is set as a flag, `read()` doesn’t block, but If there hasn’t been an expiration since the last call to read, `read()` raises [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") with `errno` is set to [`errno.EAGAIN`](https://docs.python.org/3/library/errno.html#errno.EAGAIN "errno.EAGAIN").
[`TFD_CLOEXEC`](https://docs.python.org/3/library/os.html#os.TFD_CLOEXEC "os.TFD_CLOEXEC") is always set by Python automatically.
The file descriptor must be closed with [`os.close()`](https://docs.python.org/3/library/os.html#os.close "os.close") when it is no longer needed, or else the file descriptor will be leaked.
See also
The
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux >= 2.6.27 with glibc >= 2.8
Added in version 3.13.

os.timerfd_settime(_fd_ , _/_ , _*_ , _flags =flags_, _initial =0.0_, _interval =0.0_)[¶](https://docs.python.org/3/library/os.html#os.timerfd_settime "Link to this definition")

Alter a timer file descriptor’s internal timer. This function operates the same interval timer as [`timerfd_settime_ns()`](https://docs.python.org/3/library/os.html#os.timerfd_settime_ns "os.timerfd_settime_ns").
_fd_ must be a valid timer file descriptor.
The timer’s behaviour can be modified by specifying a _flags_ value. Any of the following variables may be used, combined using bitwise OR (the `|` operator):
  * [`TFD_TIMER_ABSTIME`](https://docs.python.org/3/library/os.html#os.TFD_TIMER_ABSTIME "os.TFD_TIMER_ABSTIME")
  * [`TFD_TIMER_CANCEL_ON_SET`](https://docs.python.org/3/library/os.html#os.TFD_TIMER_CANCEL_ON_SET "os.TFD_TIMER_CANCEL_ON_SET")


The timer is disabled by setting _initial_ to zero (`0`). If _initial_ is equal to or greater than zero, the timer is enabled. If _initial_ is less than zero, it raises an [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") exception with `errno` set to [`errno.EINVAL`](https://docs.python.org/3/library/errno.html#errno.EINVAL "errno.EINVAL")
By default the timer will fire when _initial_ seconds have elapsed. (If _initial_ is zero, timer will fire immediately.)
However, if the [`TFD_TIMER_ABSTIME`](https://docs.python.org/3/library/os.html#os.TFD_TIMER_ABSTIME "os.TFD_TIMER_ABSTIME") flag is set, the timer will fire when the timer’s clock (set by _clockid_ in [`timerfd_create()`](https://docs.python.org/3/library/os.html#os.timerfd_create "os.timerfd_create")) reaches _initial_ seconds.
The timer’s interval is set by the _interval_ [`float`](https://docs.python.org/3/library/functions.html#float "float"). If _interval_ is zero, the timer only fires once, on the initial expiration. If _interval_ is greater than zero, the timer fires every time _interval_ seconds have elapsed since the previous expiration. If _interval_ is less than zero, it raises [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") with `errno` set to [`errno.EINVAL`](https://docs.python.org/3/library/errno.html#errno.EINVAL "errno.EINVAL")
If the [`TFD_TIMER_CANCEL_ON_SET`](https://docs.python.org/3/library/os.html#os.TFD_TIMER_CANCEL_ON_SET "os.TFD_TIMER_CANCEL_ON_SET") flag is set along with [`TFD_TIMER_ABSTIME`](https://docs.python.org/3/library/os.html#os.TFD_TIMER_ABSTIME "os.TFD_TIMER_ABSTIME") and the clock for this timer is [`time.CLOCK_REALTIME`](https://docs.python.org/3/library/time.html#time.CLOCK_REALTIME "time.CLOCK_REALTIME"), the timer is marked as cancelable if the real-time clock is changed discontinuously. Reading the descriptor is aborted with the error ECANCELED.
Linux manages system clock as UTC. A daylight-savings time transition is done by changing time offset only and doesn’t cause discontinuous system clock change.
Discontinuous system clock change will be caused by the following events:
  * `settimeofday`
  * `clock_settime`
  * set the system date and time by `date` command


Return a two-item tuple of (`next_expiration`, `interval`) from the previous timer state, before this function executed.
See also
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux >= 2.6.27 with glibc >= 2.8
Added in version 3.13.

os.timerfd_settime_ns(_fd_ , _/_ , _*_ , _flags =0_, _initial =0_, _interval =0_)[¶](https://docs.python.org/3/library/os.html#os.timerfd_settime_ns "Link to this definition")

Similar to [`timerfd_settime()`](https://docs.python.org/3/library/os.html#os.timerfd_settime "os.timerfd_settime"), but use time as nanoseconds. This function operates the same interval timer as `timerfd_settime()`.
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux >= 2.6.27 with glibc >= 2.8
Added in version 3.13.

os.timerfd_gettime(_fd_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.timerfd_gettime "Link to this definition")

Return a two-item tuple of floats (`next_expiration`, `interval`).
`next_expiration` denotes the relative time until the timer next fires, regardless of if the [`TFD_TIMER_ABSTIME`](https://docs.python.org/3/library/os.html#os.TFD_TIMER_ABSTIME "os.TFD_TIMER_ABSTIME") flag is set.
`interval` denotes the timer’s interval. If zero, the timer will only fire once, after `next_expiration` seconds have elapsed.
See also
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux >= 2.6.27 with glibc >= 2.8
Added in version 3.13.

os.timerfd_gettime_ns(_fd_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.timerfd_gettime_ns "Link to this definition")

Similar to [`timerfd_gettime()`](https://docs.python.org/3/library/os.html#os.timerfd_gettime "os.timerfd_gettime"), but return time as nanoseconds.
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux >= 2.6.27 with glibc >= 2.8
Added in version 3.13.

os.TFD_NONBLOCK[¶](https://docs.python.org/3/library/os.html#os.TFD_NONBLOCK "Link to this definition")

A flag for the [`timerfd_create()`](https://docs.python.org/3/library/os.html#os.timerfd_create "os.timerfd_create") function, which sets the [`O_NONBLOCK`](https://docs.python.org/3/library/os.html#os.O_NONBLOCK "os.O_NONBLOCK") status flag for the new timer file descriptor. If [`TFD_NONBLOCK`](https://docs.python.org/3/library/os.html#os.TFD_NONBLOCK "os.TFD_NONBLOCK") is not set as a flag, [`read()`](https://docs.python.org/3/library/os.html#os.read "os.read") blocks.
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux >= 2.6.27 with glibc >= 2.8
Added in version 3.13.

os.TFD_CLOEXEC[¶](https://docs.python.org/3/library/os.html#os.TFD_CLOEXEC "Link to this definition")

A flag for the [`timerfd_create()`](https://docs.python.org/3/library/os.html#os.timerfd_create "os.timerfd_create") function, If [`TFD_CLOEXEC`](https://docs.python.org/3/library/os.html#os.TFD_CLOEXEC "os.TFD_CLOEXEC") is set as a flag, set close-on-exec flag for new file descriptor.
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux >= 2.6.27 with glibc >= 2.8
Added in version 3.13.

os.TFD_TIMER_ABSTIME[¶](https://docs.python.org/3/library/os.html#os.TFD_TIMER_ABSTIME "Link to this definition")

A flag for the [`timerfd_settime()`](https://docs.python.org/3/library/os.html#os.timerfd_settime "os.timerfd_settime") and [`timerfd_settime_ns()`](https://docs.python.org/3/library/os.html#os.timerfd_settime_ns "os.timerfd_settime_ns") functions. If this flag is set, _initial_ is interpreted as an absolute value on the timer’s clock (in UTC seconds or nanoseconds since the Unix Epoch).
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux >= 2.6.27 with glibc >= 2.8
Added in version 3.13.

os.TFD_TIMER_CANCEL_ON_SET[¶](https://docs.python.org/3/library/os.html#os.TFD_TIMER_CANCEL_ON_SET "Link to this definition")

A flag for the [`timerfd_settime()`](https://docs.python.org/3/library/os.html#os.timerfd_settime "os.timerfd_settime") and [`timerfd_settime_ns()`](https://docs.python.org/3/library/os.html#os.timerfd_settime_ns "os.timerfd_settime_ns") functions along with [`TFD_TIMER_ABSTIME`](https://docs.python.org/3/library/os.html#os.TFD_TIMER_ABSTIME "os.TFD_TIMER_ABSTIME"). The timer is cancelled when the time of the underlying clock changes discontinuously.
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux >= 2.6.27 with glibc >= 2.8
Added in version 3.13.
### Linux extended attributes[¶](https://docs.python.org/3/library/os.html#linux-extended-attributes "Link to this heading")
Added in version 3.3.
These functions are all available on Linux only.

os.getxattr(_path_ , _attribute_ , _*_ , _follow_symlinks =True_)[¶](https://docs.python.org/3/library/os.html#os.getxattr "Link to this definition")

Return the value of the extended filesystem attribute _attribute_ for _path_. _attribute_ can be bytes or str (directly or indirectly through the [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "os.PathLike") interface). If it is str, it is encoded with the filesystem encoding.
This function can support [specifying a file descriptor](https://docs.python.org/3/library/os.html#path-fd) and [not following symlinks](https://docs.python.org/3/library/os.html#follow-symlinks).
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `os.getxattr` with arguments `path`, `attribute`.
Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object) for _path_ and _attribute_.

os.listxattr(_path =None_, _*_ , _follow_symlinks =True_)[¶](https://docs.python.org/3/library/os.html#os.listxattr "Link to this definition")

Return a list of the extended filesystem attributes on _path_. The attributes in the list are represented as strings decoded with the filesystem encoding. If _path_ is `None`, `listxattr()` will examine the current directory.
This function can support [specifying a file descriptor](https://docs.python.org/3/library/os.html#path-fd) and [not following symlinks](https://docs.python.org/3/library/os.html#follow-symlinks).
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `os.listxattr` with argument `path`.
Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).

os.removexattr(_path_ , _attribute_ , _*_ , _follow_symlinks =True_)[¶](https://docs.python.org/3/library/os.html#os.removexattr "Link to this definition")

Removes the extended filesystem attribute _attribute_ from _path_. _attribute_ should be bytes or str (directly or indirectly through the [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "os.PathLike") interface). If it is a string, it is encoded with the [filesystem encoding and error handler](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler).
This function can support [specifying a file descriptor](https://docs.python.org/3/library/os.html#path-fd) and [not following symlinks](https://docs.python.org/3/library/os.html#follow-symlinks).
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `os.removexattr` with arguments `path`, `attribute`.
Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object) for _path_ and _attribute_.

os.setxattr(_path_ , _attribute_ , _value_ , _flags =0_, _*_ , _follow_symlinks =True_)[¶](https://docs.python.org/3/library/os.html#os.setxattr "Link to this definition")

Set the extended filesystem attribute _attribute_ on _path_ to _value_. _attribute_ must be a bytes or str with no embedded NULs (directly or indirectly through the [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "os.PathLike") interface). If it is a str, it is encoded with the [filesystem encoding and error handler](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler). _flags_ may be [`XATTR_REPLACE`](https://docs.python.org/3/library/os.html#os.XATTR_REPLACE "os.XATTR_REPLACE") or [`XATTR_CREATE`](https://docs.python.org/3/library/os.html#os.XATTR_CREATE "os.XATTR_CREATE"). If `XATTR_REPLACE` is given and the attribute does not exist, `ENODATA` will be raised. If `XATTR_CREATE` is given and the attribute already exists, the attribute will not be created and `EEXISTS` will be raised.
This function can support [specifying a file descriptor](https://docs.python.org/3/library/os.html#path-fd) and [not following symlinks](https://docs.python.org/3/library/os.html#follow-symlinks).
Note
A bug in Linux kernel versions less than 2.6.39 caused the flags argument to be ignored on some filesystems.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `os.setxattr` with arguments `path`, `attribute`, `value`, `flags`.
Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object) for _path_ and _attribute_.

os.XATTR_SIZE_MAX[¶](https://docs.python.org/3/library/os.html#os.XATTR_SIZE_MAX "Link to this definition")

The maximum size the value of an extended attribute can be. Currently, this is 64 KiB on Linux.

os.XATTR_CREATE[¶](https://docs.python.org/3/library/os.html#os.XATTR_CREATE "Link to this definition")

This is a possible value for the flags argument in [`setxattr()`](https://docs.python.org/3/library/os.html#os.setxattr "os.setxattr"). It indicates the operation must create an attribute.

os.XATTR_REPLACE[¶](https://docs.python.org/3/library/os.html#os.XATTR_REPLACE "Link to this definition")

This is a possible value for the flags argument in [`setxattr()`](https://docs.python.org/3/library/os.html#os.setxattr "os.setxattr"). It indicates the operation must replace an existing attribute.
## Process Management[¶](https://docs.python.org/3/library/os.html#process-management "Link to this heading")
These functions may be used to create and manage processes.
The various [`exec*`](https://docs.python.org/3/library/os.html#os.execl "os.execl") functions take a list of arguments for the new program loaded into the process. In each case, the first of these arguments is passed to the new program as its own name rather than as an argument a user may have typed on a command line. For the C programmer, this is the `argv[0]` passed to a program’s `main()`. For example, `os.execv('/bin/echo', ['foo', 'bar'])` will only print `bar` on standard output; `foo` will seem to be ignored.

os.abort()[¶](https://docs.python.org/3/library/os.html#os.abort "Link to this definition")

Generate a `SIGABRT` signal to the current process. On Unix, the default behavior is to produce a core dump; on Windows, the process immediately returns an exit code of `3`. Be aware that calling this function will not call the Python signal handler registered for `SIGABRT` with [`signal.signal()`](https://docs.python.org/3/library/signal.html#signal.signal "signal.signal").

os.add_dll_directory(_path_)[¶](https://docs.python.org/3/library/os.html#os.add_dll_directory "Link to this definition")

Add a path to the DLL search path.
This search path is used when resolving dependencies for imported extension modules (the module itself is resolved through [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path")), and also by [`ctypes`](https://docs.python.org/3/library/ctypes.html#module-ctypes "ctypes: A foreign function library for Python.").
Remove the directory by calling **close()** on the returned object or using it in a [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement.
See the
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `os.add_dll_directory` with argument `path`.
[Availability](https://docs.python.org/3/library/intro.html#availability): Windows.
Added in version 3.8: Previous versions of CPython would resolve DLLs using the default behavior for the current process. This led to inconsistencies, such as only sometimes searching `PATH` or the current working directory, and OS functions such as `AddDllDirectory` having no effect.
In 3.8, the two primary ways DLLs are loaded now explicitly override the process-wide behavior to ensure consistency. See the [porting notes](https://docs.python.org/3/whatsnew/3.8.html#bpo-36085-whatsnew) for information on updating libraries.

os.execl(_path_ , _arg0_ , _arg1_ , _..._)[¶](https://docs.python.org/3/library/os.html#os.execl "Link to this definition")


os.execle(_path_ , _arg0_ , _arg1_ , _..._ , _env_)[¶](https://docs.python.org/3/library/os.html#os.execle "Link to this definition")


os.execlp(_file_ , _arg0_ , _arg1_ , _..._)[¶](https://docs.python.org/3/library/os.html#os.execlp "Link to this definition")


os.execlpe(_file_ , _arg0_ , _arg1_ , _..._ , _env_)[¶](https://docs.python.org/3/library/os.html#os.execlpe "Link to this definition")


os.execv(_path_ , _args_)[¶](https://docs.python.org/3/library/os.html#os.execv "Link to this definition")


os.execve(_path_ , _args_ , _env_)[¶](https://docs.python.org/3/library/os.html#os.execve "Link to this definition")


os.execvp(_file_ , _args_)[¶](https://docs.python.org/3/library/os.html#os.execvp "Link to this definition")


os.execvpe(_file_ , _args_ , _env_)[¶](https://docs.python.org/3/library/os.html#os.execvpe "Link to this definition")

These functions all execute a new program, replacing the current process; they do not return. On Unix, the new executable is loaded into the current process, and will have the same process id as the caller. Errors will be reported as [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") exceptions.
The current process is replaced immediately. Open file objects and descriptors are not flushed, so if there may be data buffered on these open files, you should flush them using `sys.stdout.flush()` or [`os.fsync()`](https://docs.python.org/3/library/os.html#os.fsync "os.fsync") before calling an `exec*` function.
The “l” and “v” variants of the `exec*` functions differ in how command-line arguments are passed. The “l” variants are perhaps the easiest to work with if the number of parameters is fixed when the code is written; the individual parameters simply become additional parameters to the `execl*()` functions. The “v” variants are good when the number of parameters is variable, with the arguments being passed in a list or tuple as the _args_ parameter. In either case, the arguments to the child process should start with the name of the command being run, but this is not enforced.
The variants which include a “p” near the end (`execlp()`, `execlpe()`, `execvp()`, and `execvpe()`) will use the `PATH` environment variable to locate the program _file_. When the environment is being replaced (using one of the `exec*e` variants, discussed in the next paragraph), the new environment is used as the source of the `PATH` variable. The other variants, `execl()`, `execle()`, `execv()`, and `execve()`, will not use the `PATH` variable to locate the executable; _path_ must contain an appropriate absolute or relative path. Relative paths must include at least one slash, even on Windows, as plain names will not be resolved.
For `execle()`, `execlpe()`, `execve()`, and `execvpe()` (note that these all end in “e”), the _env_ parameter must be a mapping which is used to define the environment variables for the new process (these are used instead of the current process’ environment); the functions `execl()`, `execlp()`, `execv()`, and `execvp()` all cause the new process to inherit the environment of the current process.
