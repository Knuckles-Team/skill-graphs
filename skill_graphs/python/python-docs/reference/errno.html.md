[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`platform` — Access to underlying platform’s identifying data](https://docs.python.org/3/library/platform.html "previous chapter")
#### Next topic
[`ctypes` — A foreign function library for Python](https://docs.python.org/3/library/ctypes.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=errno+%E2%80%94+Standard+errno+system+symbols&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ferrno.html&pagesource=library%2Ferrno.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/ctypes.html "ctypes — A foreign function library for Python") |
  * [previous](https://docs.python.org/3/library/platform.html "platform — Access to underlying platform’s identifying data") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Generic Operating System Services](https://docs.python.org/3/library/allows.html) »
  * [`errno` — Standard errno system symbols](https://docs.python.org/3/library/errno.html)
  * |
  * Theme  Auto Light Dark |


#  `errno` — Standard errno system symbols[¶](https://docs.python.org/3/library/errno.html#module-errno "Link to this heading")
* * *
This module makes available standard `errno` system symbols. The value of each symbol is the corresponding integer value. The names and descriptions are borrowed from `linux/include/errno.h`, which should be all-inclusive.

errno.errorcode[¶](https://docs.python.org/3/library/errno.html#errno.errorcode "Link to this definition")

Dictionary providing a mapping from the errno value to the string name in the underlying system. For instance, `errno.errorcode[errno.EPERM]` maps to `'EPERM'`.
To translate a numeric error code to an error message, use [`os.strerror()`](https://docs.python.org/3/library/os.html#os.strerror "os.strerror").
Of the following list, symbols that are not used on the current platform are not defined by the module. The specific list of defined symbols is available as `errno.errorcode.keys()`. Symbols available can include:

errno.EPERM[¶](https://docs.python.org/3/library/errno.html#errno.EPERM "Link to this definition")

Operation not permitted. This error is mapped to the exception [`PermissionError`](https://docs.python.org/3/library/exceptions.html#PermissionError "PermissionError").

errno.ENOENT[¶](https://docs.python.org/3/library/errno.html#errno.ENOENT "Link to this definition")

No such file or directory. This error is mapped to the exception [`FileNotFoundError`](https://docs.python.org/3/library/exceptions.html#FileNotFoundError "FileNotFoundError").

errno.ESRCH[¶](https://docs.python.org/3/library/errno.html#errno.ESRCH "Link to this definition")

No such process. This error is mapped to the exception [`ProcessLookupError`](https://docs.python.org/3/library/exceptions.html#ProcessLookupError "ProcessLookupError").

errno.EINTR[¶](https://docs.python.org/3/library/errno.html#errno.EINTR "Link to this definition")

Interrupted system call. This error is mapped to the exception [`InterruptedError`](https://docs.python.org/3/library/exceptions.html#InterruptedError "InterruptedError").

errno.EIO[¶](https://docs.python.org/3/library/errno.html#errno.EIO "Link to this definition")

I/O error

errno.ENXIO[¶](https://docs.python.org/3/library/errno.html#errno.ENXIO "Link to this definition")

No such device or address

errno.E2BIG[¶](https://docs.python.org/3/library/errno.html#errno.E2BIG "Link to this definition")

Arg list too long

errno.ENOEXEC[¶](https://docs.python.org/3/library/errno.html#errno.ENOEXEC "Link to this definition")

Exec format error

errno.EBADF[¶](https://docs.python.org/3/library/errno.html#errno.EBADF "Link to this definition")

Bad file number

errno.ECHILD[¶](https://docs.python.org/3/library/errno.html#errno.ECHILD "Link to this definition")

No child processes. This error is mapped to the exception [`ChildProcessError`](https://docs.python.org/3/library/exceptions.html#ChildProcessError "ChildProcessError").

errno.EAGAIN[¶](https://docs.python.org/3/library/errno.html#errno.EAGAIN "Link to this definition")

Try again. This error is mapped to the exception [`BlockingIOError`](https://docs.python.org/3/library/exceptions.html#BlockingIOError "BlockingIOError").

errno.ENOMEM[¶](https://docs.python.org/3/library/errno.html#errno.ENOMEM "Link to this definition")

Out of memory

errno.EACCES[¶](https://docs.python.org/3/library/errno.html#errno.EACCES "Link to this definition")

Permission denied. This error is mapped to the exception [`PermissionError`](https://docs.python.org/3/library/exceptions.html#PermissionError "PermissionError").

errno.EFAULT[¶](https://docs.python.org/3/library/errno.html#errno.EFAULT "Link to this definition")

Bad address

errno.ENOTBLK[¶](https://docs.python.org/3/library/errno.html#errno.ENOTBLK "Link to this definition")

Block device required

errno.EBUSY[¶](https://docs.python.org/3/library/errno.html#errno.EBUSY "Link to this definition")

Device or resource busy

errno.EEXIST[¶](https://docs.python.org/3/library/errno.html#errno.EEXIST "Link to this definition")

File exists. This error is mapped to the exception [`FileExistsError`](https://docs.python.org/3/library/exceptions.html#FileExistsError "FileExistsError").

errno.EXDEV[¶](https://docs.python.org/3/library/errno.html#errno.EXDEV "Link to this definition")

Cross-device link

errno.ENODEV[¶](https://docs.python.org/3/library/errno.html#errno.ENODEV "Link to this definition")

No such device

errno.ENOTDIR[¶](https://docs.python.org/3/library/errno.html#errno.ENOTDIR "Link to this definition")

Not a directory. This error is mapped to the exception [`NotADirectoryError`](https://docs.python.org/3/library/exceptions.html#NotADirectoryError "NotADirectoryError").

errno.EISDIR[¶](https://docs.python.org/3/library/errno.html#errno.EISDIR "Link to this definition")

Is a directory. This error is mapped to the exception [`IsADirectoryError`](https://docs.python.org/3/library/exceptions.html#IsADirectoryError "IsADirectoryError").

errno.EINVAL[¶](https://docs.python.org/3/library/errno.html#errno.EINVAL "Link to this definition")

Invalid argument

errno.ENFILE[¶](https://docs.python.org/3/library/errno.html#errno.ENFILE "Link to this definition")

File table overflow

errno.EMFILE[¶](https://docs.python.org/3/library/errno.html#errno.EMFILE "Link to this definition")

Too many open files

errno.ENOTTY[¶](https://docs.python.org/3/library/errno.html#errno.ENOTTY "Link to this definition")

Not a typewriter

errno.ETXTBSY[¶](https://docs.python.org/3/library/errno.html#errno.ETXTBSY "Link to this definition")

Text file busy

errno.EFBIG[¶](https://docs.python.org/3/library/errno.html#errno.EFBIG "Link to this definition")

File too large

errno.ENOSPC[¶](https://docs.python.org/3/library/errno.html#errno.ENOSPC "Link to this definition")

No space left on device

errno.ESPIPE[¶](https://docs.python.org/3/library/errno.html#errno.ESPIPE "Link to this definition")

Illegal seek

errno.EROFS[¶](https://docs.python.org/3/library/errno.html#errno.EROFS "Link to this definition")

Read-only file system

errno.EMLINK[¶](https://docs.python.org/3/library/errno.html#errno.EMLINK "Link to this definition")

Too many links

errno.EPIPE[¶](https://docs.python.org/3/library/errno.html#errno.EPIPE "Link to this definition")

Broken pipe. This error is mapped to the exception [`BrokenPipeError`](https://docs.python.org/3/library/exceptions.html#BrokenPipeError "BrokenPipeError").

errno.EDOM[¶](https://docs.python.org/3/library/errno.html#errno.EDOM "Link to this definition")

Math argument out of domain of func

errno.ERANGE[¶](https://docs.python.org/3/library/errno.html#errno.ERANGE "Link to this definition")

Math result not representable

errno.EDEADLK[¶](https://docs.python.org/3/library/errno.html#errno.EDEADLK "Link to this definition")

Resource deadlock would occur

errno.ENAMETOOLONG[¶](https://docs.python.org/3/library/errno.html#errno.ENAMETOOLONG "Link to this definition")

File name too long

errno.ENOLCK[¶](https://docs.python.org/3/library/errno.html#errno.ENOLCK "Link to this definition")

No record locks available

errno.ENOSYS[¶](https://docs.python.org/3/library/errno.html#errno.ENOSYS "Link to this definition")

Function not implemented

errno.ENOTEMPTY[¶](https://docs.python.org/3/library/errno.html#errno.ENOTEMPTY "Link to this definition")

Directory not empty

errno.ELOOP[¶](https://docs.python.org/3/library/errno.html#errno.ELOOP "Link to this definition")

Too many symbolic links encountered

errno.EWOULDBLOCK[¶](https://docs.python.org/3/library/errno.html#errno.EWOULDBLOCK "Link to this definition")

Operation would block. This error is mapped to the exception [`BlockingIOError`](https://docs.python.org/3/library/exceptions.html#BlockingIOError "BlockingIOError").

errno.ENOMSG[¶](https://docs.python.org/3/library/errno.html#errno.ENOMSG "Link to this definition")

No message of desired type

errno.EIDRM[¶](https://docs.python.org/3/library/errno.html#errno.EIDRM "Link to this definition")

Identifier removed

errno.ECHRNG[¶](https://docs.python.org/3/library/errno.html#errno.ECHRNG "Link to this definition")

Channel number out of range

errno.EL2NSYNC[¶](https://docs.python.org/3/library/errno.html#errno.EL2NSYNC "Link to this definition")

Level 2 not synchronized

errno.EL3HLT[¶](https://docs.python.org/3/library/errno.html#errno.EL3HLT "Link to this definition")

Level 3 halted

errno.EL3RST[¶](https://docs.python.org/3/library/errno.html#errno.EL3RST "Link to this definition")

Level 3 reset

errno.ELNRNG[¶](https://docs.python.org/3/library/errno.html#errno.ELNRNG "Link to this definition")

Link number out of range

errno.EUNATCH[¶](https://docs.python.org/3/library/errno.html#errno.EUNATCH "Link to this definition")

Protocol driver not attached

errno.ENOCSI[¶](https://docs.python.org/3/library/errno.html#errno.ENOCSI "Link to this definition")

No CSI structure available

errno.EL2HLT[¶](https://docs.python.org/3/library/errno.html#errno.EL2HLT "Link to this definition")

Level 2 halted

errno.EBADE[¶](https://docs.python.org/3/library/errno.html#errno.EBADE "Link to this definition")

Invalid exchange

errno.EBADR[¶](https://docs.python.org/3/library/errno.html#errno.EBADR "Link to this definition")

Invalid request descriptor

errno.EXFULL[¶](https://docs.python.org/3/library/errno.html#errno.EXFULL "Link to this definition")

Exchange full

errno.ENOANO[¶](https://docs.python.org/3/library/errno.html#errno.ENOANO "Link to this definition")

No anode

errno.EBADRQC[¶](https://docs.python.org/3/library/errno.html#errno.EBADRQC "Link to this definition")

Invalid request code

errno.EBADSLT[¶](https://docs.python.org/3/library/errno.html#errno.EBADSLT "Link to this definition")

Invalid slot

errno.EDEADLOCK[¶](https://docs.python.org/3/library/errno.html#errno.EDEADLOCK "Link to this definition")

File locking deadlock error

errno.EBFONT[¶](https://docs.python.org/3/library/errno.html#errno.EBFONT "Link to this definition")

Bad font file format

errno.ENOSTR[¶](https://docs.python.org/3/library/errno.html#errno.ENOSTR "Link to this definition")

Device not a stream

errno.ENODATA[¶](https://docs.python.org/3/library/errno.html#errno.ENODATA "Link to this definition")

No data available

errno.ETIME[¶](https://docs.python.org/3/library/errno.html#errno.ETIME "Link to this definition")

Timer expired

errno.ENOSR[¶](https://docs.python.org/3/library/errno.html#errno.ENOSR "Link to this definition")

Out of streams resources

errno.ENONET[¶](https://docs.python.org/3/library/errno.html#errno.ENONET "Link to this definition")

Machine is not on the network

errno.ENOPKG[¶](https://docs.python.org/3/library/errno.html#errno.ENOPKG "Link to this definition")

Package not installed

errno.EREMOTE[¶](https://docs.python.org/3/library/errno.html#errno.EREMOTE "Link to this definition")

Object is remote

errno.ENOLINK[¶](https://docs.python.org/3/library/errno.html#errno.ENOLINK "Link to this definition")

Link has been severed

errno.EADV[¶](https://docs.python.org/3/library/errno.html#errno.EADV "Link to this definition")

Advertise error

errno.ESRMNT[¶](https://docs.python.org/3/library/errno.html#errno.ESRMNT "Link to this definition")

Srmount error

errno.ECOMM[¶](https://docs.python.org/3/library/errno.html#errno.ECOMM "Link to this definition")

Communication error on send

errno.EPROTO[¶](https://docs.python.org/3/library/errno.html#errno.EPROTO "Link to this definition")

Protocol error

errno.EMULTIHOP[¶](https://docs.python.org/3/library/errno.html#errno.EMULTIHOP "Link to this definition")

Multihop attempted

errno.EDOTDOT[¶](https://docs.python.org/3/library/errno.html#errno.EDOTDOT "Link to this definition")

RFS specific error

errno.EBADMSG[¶](https://docs.python.org/3/library/errno.html#errno.EBADMSG "Link to this definition")

Not a data message

errno.EOVERFLOW[¶](https://docs.python.org/3/library/errno.html#errno.EOVERFLOW "Link to this definition")

Value too large for defined data type

errno.ENOTUNIQ[¶](https://docs.python.org/3/library/errno.html#errno.ENOTUNIQ "Link to this definition")

Name not unique on network

errno.EBADFD[¶](https://docs.python.org/3/library/errno.html#errno.EBADFD "Link to this definition")

File descriptor in bad state

errno.EREMCHG[¶](https://docs.python.org/3/library/errno.html#errno.EREMCHG "Link to this definition")

Remote address changed

errno.ELIBACC[¶](https://docs.python.org/3/library/errno.html#errno.ELIBACC "Link to this definition")

Can not access a needed shared library

errno.ELIBBAD[¶](https://docs.python.org/3/library/errno.html#errno.ELIBBAD "Link to this definition")

Accessing a corrupted shared library

errno.ELIBSCN[¶](https://docs.python.org/3/library/errno.html#errno.ELIBSCN "Link to this definition")

.lib section in a.out corrupted

errno.ELIBMAX[¶](https://docs.python.org/3/library/errno.html#errno.ELIBMAX "Link to this definition")

Attempting to link in too many shared libraries

errno.ELIBEXEC[¶](https://docs.python.org/3/library/errno.html#errno.ELIBEXEC "Link to this definition")

Cannot exec a shared library directly

errno.EILSEQ[¶](https://docs.python.org/3/library/errno.html#errno.EILSEQ "Link to this definition")

Illegal byte sequence

errno.ERESTART[¶](https://docs.python.org/3/library/errno.html#errno.ERESTART "Link to this definition")

Interrupted system call should be restarted

errno.ESTRPIPE[¶](https://docs.python.org/3/library/errno.html#errno.ESTRPIPE "Link to this definition")

Streams pipe error

errno.EUSERS[¶](https://docs.python.org/3/library/errno.html#errno.EUSERS "Link to this definition")

Too many users

errno.ENOTSOCK[¶](https://docs.python.org/3/library/errno.html#errno.ENOTSOCK "Link to this definition")

Socket operation on non-socket

errno.EDESTADDRREQ[¶](https://docs.python.org/3/library/errno.html#errno.EDESTADDRREQ "Link to this definition")

Destination address required

errno.EMSGSIZE[¶](https://docs.python.org/3/library/errno.html#errno.EMSGSIZE "Link to this definition")

Message too long

errno.EPROTOTYPE[¶](https://docs.python.org/3/library/errno.html#errno.EPROTOTYPE "Link to this definition")

Protocol wrong type for socket

errno.ENOPROTOOPT[¶](https://docs.python.org/3/library/errno.html#errno.ENOPROTOOPT "Link to this definition")

Protocol not available

errno.EPROTONOSUPPORT[¶](https://docs.python.org/3/library/errno.html#errno.EPROTONOSUPPORT "Link to this definition")

Protocol not supported

errno.ESOCKTNOSUPPORT[¶](https://docs.python.org/3/library/errno.html#errno.ESOCKTNOSUPPORT "Link to this definition")

Socket type not supported

errno.EOPNOTSUPP[¶](https://docs.python.org/3/library/errno.html#errno.EOPNOTSUPP "Link to this definition")

Operation not supported on transport endpoint

errno.ENOTSUP[¶](https://docs.python.org/3/library/errno.html#errno.ENOTSUP "Link to this definition")

Operation not supported
Added in version 3.2.

errno.EPFNOSUPPORT[¶](https://docs.python.org/3/library/errno.html#errno.EPFNOSUPPORT "Link to this definition")

Protocol family not supported

errno.EAFNOSUPPORT[¶](https://docs.python.org/3/library/errno.html#errno.EAFNOSUPPORT "Link to this definition")

Address family not supported by protocol

errno.EADDRINUSE[¶](https://docs.python.org/3/library/errno.html#errno.EADDRINUSE "Link to this definition")

Address already in use

errno.EADDRNOTAVAIL[¶](https://docs.python.org/3/library/errno.html#errno.EADDRNOTAVAIL "Link to this definition")

Cannot assign requested address

errno.ENETDOWN[¶](https://docs.python.org/3/library/errno.html#errno.ENETDOWN "Link to this definition")

Network is down

errno.ENETUNREACH[¶](https://docs.python.org/3/library/errno.html#errno.ENETUNREACH "Link to this definition")

Network is unreachable

errno.ENETRESET[¶](https://docs.python.org/3/library/errno.html#errno.ENETRESET "Link to this definition")

Network dropped connection because of reset

errno.ECONNABORTED[¶](https://docs.python.org/3/library/errno.html#errno.ECONNABORTED "Link to this definition")

Software caused connection abort. This error is mapped to the exception [`ConnectionAbortedError`](https://docs.python.org/3/library/exceptions.html#ConnectionAbortedError "ConnectionAbortedError").

errno.ECONNRESET[¶](https://docs.python.org/3/library/errno.html#errno.ECONNRESET "Link to this definition")

Connection reset by peer. This error is mapped to the exception [`ConnectionResetError`](https://docs.python.org/3/library/exceptions.html#ConnectionResetError "ConnectionResetError").

errno.ENOBUFS[¶](https://docs.python.org/3/library/errno.html#errno.ENOBUFS "Link to this definition")

No buffer space available

errno.EISCONN[¶](https://docs.python.org/3/library/errno.html#errno.EISCONN "Link to this definition")

Transport endpoint is already connected

errno.ENOTCONN[¶](https://docs.python.org/3/library/errno.html#errno.ENOTCONN "Link to this definition")

Transport endpoint is not connected

errno.ESHUTDOWN[¶](https://docs.python.org/3/library/errno.html#errno.ESHUTDOWN "Link to this definition")

Cannot send after transport endpoint shutdown. This error is mapped to the exception [`BrokenPipeError`](https://docs.python.org/3/library/exceptions.html#BrokenPipeError "BrokenPipeError").

errno.ETOOMANYREFS[¶](https://docs.python.org/3/library/errno.html#errno.ETOOMANYREFS "Link to this definition")

Too many references: cannot splice

errno.ETIMEDOUT[¶](https://docs.python.org/3/library/errno.html#errno.ETIMEDOUT "Link to this definition")

Connection timed out. This error is mapped to the exception [`TimeoutError`](https://docs.python.org/3/library/exceptions.html#TimeoutError "TimeoutError").

errno.ECONNREFUSED[¶](https://docs.python.org/3/library/errno.html#errno.ECONNREFUSED "Link to this definition")

Connection refused. This error is mapped to the exception [`ConnectionRefusedError`](https://docs.python.org/3/library/exceptions.html#ConnectionRefusedError "ConnectionRefusedError").

errno.EHOSTDOWN[¶](https://docs.python.org/3/library/errno.html#errno.EHOSTDOWN "Link to this definition")

Host is down

errno.EHOSTUNREACH[¶](https://docs.python.org/3/library/errno.html#errno.EHOSTUNREACH "Link to this definition")

No route to host

errno.EHWPOISON[¶](https://docs.python.org/3/library/errno.html#errno.EHWPOISON "Link to this definition")

Memory page has hardware error.
Added in version 3.14.

errno.EALREADY[¶](https://docs.python.org/3/library/errno.html#errno.EALREADY "Link to this definition")

Operation already in progress. This error is mapped to the exception [`BlockingIOError`](https://docs.python.org/3/library/exceptions.html#BlockingIOError "BlockingIOError").

errno.EINPROGRESS[¶](https://docs.python.org/3/library/errno.html#errno.EINPROGRESS "Link to this definition")

Operation now in progress. This error is mapped to the exception [`BlockingIOError`](https://docs.python.org/3/library/exceptions.html#BlockingIOError "BlockingIOError").

errno.ESTALE[¶](https://docs.python.org/3/library/errno.html#errno.ESTALE "Link to this definition")

Stale NFS file handle

errno.EUCLEAN[¶](https://docs.python.org/3/library/errno.html#errno.EUCLEAN "Link to this definition")

Structure needs cleaning

errno.ENOTNAM[¶](https://docs.python.org/3/library/errno.html#errno.ENOTNAM "Link to this definition")

Not a XENIX named type file

errno.ENAVAIL[¶](https://docs.python.org/3/library/errno.html#errno.ENAVAIL "Link to this definition")

No XENIX semaphores available

errno.EISNAM[¶](https://docs.python.org/3/library/errno.html#errno.EISNAM "Link to this definition")

Is a named type file

errno.EREMOTEIO[¶](https://docs.python.org/3/library/errno.html#errno.EREMOTEIO "Link to this definition")

Remote I/O error

errno.EDQUOT[¶](https://docs.python.org/3/library/errno.html#errno.EDQUOT "Link to this definition")

Quota exceeded

errno.EQFULL[¶](https://docs.python.org/3/library/errno.html#errno.EQFULL "Link to this definition")

Interface output queue is full
Added in version 3.11.

errno.ENOMEDIUM[¶](https://docs.python.org/3/library/errno.html#errno.ENOMEDIUM "Link to this definition")

No medium found

errno.EMEDIUMTYPE[¶](https://docs.python.org/3/library/errno.html#errno.EMEDIUMTYPE "Link to this definition")

Wrong medium type

errno.ENOKEY[¶](https://docs.python.org/3/library/errno.html#errno.ENOKEY "Link to this definition")

Required key not available

errno.EKEYEXPIRED[¶](https://docs.python.org/3/library/errno.html#errno.EKEYEXPIRED "Link to this definition")

Key has expired

errno.EKEYREVOKED[¶](https://docs.python.org/3/library/errno.html#errno.EKEYREVOKED "Link to this definition")

Key has been revoked

errno.EKEYREJECTED[¶](https://docs.python.org/3/library/errno.html#errno.EKEYREJECTED "Link to this definition")

Key was rejected by service

errno.ERFKILL[¶](https://docs.python.org/3/library/errno.html#errno.ERFKILL "Link to this definition")

Operation not possible due to RF-kill

errno.ELOCKUNMAPPED[¶](https://docs.python.org/3/library/errno.html#errno.ELOCKUNMAPPED "Link to this definition")

Locked lock was unmapped

errno.ENOTACTIVE[¶](https://docs.python.org/3/library/errno.html#errno.ENOTACTIVE "Link to this definition")

Facility is not active

errno.EAUTH[¶](https://docs.python.org/3/library/errno.html#errno.EAUTH "Link to this definition")

Authentication error
Added in version 3.2.

errno.EBADARCH[¶](https://docs.python.org/3/library/errno.html#errno.EBADARCH "Link to this definition")

Bad CPU type in executable
Added in version 3.2.

errno.EBADEXEC[¶](https://docs.python.org/3/library/errno.html#errno.EBADEXEC "Link to this definition")

Bad executable (or shared library)
Added in version 3.2.

errno.EBADMACHO[¶](https://docs.python.org/3/library/errno.html#errno.EBADMACHO "Link to this definition")

Malformed Mach-o file
Added in version 3.2.

errno.EDEVERR[¶](https://docs.python.org/3/library/errno.html#errno.EDEVERR "Link to this definition")

Device error
Added in version 3.2.

errno.EFTYPE[¶](https://docs.python.org/3/library/errno.html#errno.EFTYPE "Link to this definition")

Inappropriate file type or format
Added in version 3.2.

errno.ENEEDAUTH[¶](https://docs.python.org/3/library/errno.html#errno.ENEEDAUTH "Link to this definition")

Need authenticator
Added in version 3.2.

errno.ENOATTR[¶](https://docs.python.org/3/library/errno.html#errno.ENOATTR "Link to this definition")

Attribute not found
Added in version 3.2.

errno.ENOPOLICY[¶](https://docs.python.org/3/library/errno.html#errno.ENOPOLICY "Link to this definition")

Policy not found
Added in version 3.2.

errno.EPROCLIM[¶](https://docs.python.org/3/library/errno.html#errno.EPROCLIM "Link to this definition")

Too many processes
Added in version 3.2.

errno.EPROCUNAVAIL[¶](https://docs.python.org/3/library/errno.html#errno.EPROCUNAVAIL "Link to this definition")

Bad procedure for program
Added in version 3.2.

errno.EPROGMISMATCH[¶](https://docs.python.org/3/library/errno.html#errno.EPROGMISMATCH "Link to this definition")

Program version wrong
Added in version 3.2.

errno.EPROGUNAVAIL[¶](https://docs.python.org/3/library/errno.html#errno.EPROGUNAVAIL "Link to this definition")

RPC prog. not avail
Added in version 3.2.

errno.EPWROFF[¶](https://docs.python.org/3/library/errno.html#errno.EPWROFF "Link to this definition")

Device power is off
Added in version 3.2.

errno.EBADRPC[¶](https://docs.python.org/3/library/errno.html#errno.EBADRPC "Link to this definition")

RPC struct is bad
Added in version 3.2.

errno.ERPCMISMATCH[¶](https://docs.python.org/3/library/errno.html#errno.ERPCMISMATCH "Link to this definition")

RPC version wrong
Added in version 3.2.

errno.ESHLIBVERS[¶](https://docs.python.org/3/library/errno.html#errno.ESHLIBVERS "Link to this definition")

Shared library version mismatch
Added in version 3.2.

errno.ENOTCAPABLE[¶](https://docs.python.org/3/library/errno.html#errno.ENOTCAPABLE "Link to this definition")

Capabilities insufficient. This error is mapped to the exception [`PermissionError`](https://docs.python.org/3/library/exceptions.html#PermissionError "PermissionError").
[Availability](https://docs.python.org/3/library/intro.html#availability): WASI, FreeBSD
Added in version 3.11.1.

errno.ECANCELED[¶](https://docs.python.org/3/library/errno.html#errno.ECANCELED "Link to this definition")

Operation canceled
Added in version 3.2.

errno.EOWNERDEAD[¶](https://docs.python.org/3/library/errno.html#errno.EOWNERDEAD "Link to this definition")

Owner died
Added in version 3.2.

errno.ENOTRECOVERABLE[¶](https://docs.python.org/3/library/errno.html#errno.ENOTRECOVERABLE "Link to this definition")

State not recoverable
Added in version 3.2.
#### Previous topic
[`platform` — Access to underlying platform’s identifying data](https://docs.python.org/3/library/platform.html "previous chapter")
#### Next topic
[`ctypes` — A foreign function library for Python](https://docs.python.org/3/library/ctypes.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=errno+%E2%80%94+Standard+errno+system+symbols&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ferrno.html&pagesource=library%2Ferrno.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/ctypes.html "ctypes — A foreign function library for Python") |
  * [previous](https://docs.python.org/3/library/platform.html "platform — Access to underlying platform’s identifying data") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Generic Operating System Services](https://docs.python.org/3/library/allows.html) »
  * [`errno` — Standard errno system symbols](https://docs.python.org/3/library/errno.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
