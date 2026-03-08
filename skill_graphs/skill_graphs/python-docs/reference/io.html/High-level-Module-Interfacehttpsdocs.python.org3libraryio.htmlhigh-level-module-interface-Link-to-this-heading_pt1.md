## High-level Module Interface[¶](https://docs.python.org/3/library/io.html#high-level-module-interface "Link to this heading")

io.DEFAULT_BUFFER_SIZE[¶](https://docs.python.org/3/library/io.html#io.DEFAULT_BUFFER_SIZE "Link to this definition")

An int containing the default buffer size used by the module’s buffered I/O classes. [`open()`](https://docs.python.org/3/library/functions.html#open "open") uses the file’s blksize (as obtained by [`os.stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat")) if possible.

io.open(_file_ , _mode ='r'_, _buffering =-1_, _encoding =None_, _errors =None_, _newline =None_, _closefd =True_, _opener =None_)[¶](https://docs.python.org/3/library/io.html#io.open "Link to this definition")

This is an alias for the builtin `open()` function.
This function raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `open` with arguments _path_ , _mode_ and _flags_. The _mode_ and _flags_ arguments may have been modified or inferred from the original call.

io.open_code(_path_)[¶](https://docs.python.org/3/library/io.html#io.open_code "Link to this definition")

Opens the provided file with mode `'rb'`. This function should be used when the intent is to treat the contents as executable code.
_path_ should be a [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") and an absolute path.
The behavior of this function may be overridden by an earlier call to the [`PyFile_SetOpenCodeHook()`](https://docs.python.org/3/c-api/file.html#c.PyFile_SetOpenCodeHook "PyFile_SetOpenCodeHook"). However, assuming that _path_ is a [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") and an absolute path, `open_code(path)` should always behave the same as `open(path, 'rb')`. Overriding the behavior is intended for additional validation or preprocessing of the file.
Added in version 3.8.

io.text_encoding(_encoding_ , _stacklevel =2_, _/_)[¶](https://docs.python.org/3/library/io.html#io.text_encoding "Link to this definition")

This is a helper function for callables that use [`open()`](https://docs.python.org/3/library/functions.html#open "open") or [`TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper") and have an `encoding=None` parameter.
This function returns _encoding_ if it is not `None`. Otherwise, it returns `"locale"` or `"utf-8"` depending on [UTF-8 Mode](https://docs.python.org/3/library/os.html#utf8-mode).
This function emits an [`EncodingWarning`](https://docs.python.org/3/library/exceptions.html#EncodingWarning "EncodingWarning") if [`sys.flags.warn_default_encoding`](https://docs.python.org/3/library/sys.html#sys.flags "sys.flags") is true and _encoding_ is `None`. _stacklevel_ specifies where the warning is emitted. For example:
Copy```
def read_text(path, encoding=None):
    encoding = io.text_encoding(encoding)  # stacklevel=2
    with open(path, encoding) as f:
        return f.read()

```

In this example, an [`EncodingWarning`](https://docs.python.org/3/library/exceptions.html#EncodingWarning "EncodingWarning") is emitted for the caller of `read_text()`.
See [Text Encoding](https://docs.python.org/3/library/io.html#io-text-encoding) for more information.
Added in version 3.10.
Changed in version 3.11: `text_encoding()` returns “utf-8” when UTF-8 mode is enabled and _encoding_ is `None`.

_exception_ io.BlockingIOError[¶](https://docs.python.org/3/library/io.html#io.BlockingIOError "Link to this definition")

This is a compatibility alias for the builtin `BlockingIOError` exception.

_exception_ io.UnsupportedOperation[¶](https://docs.python.org/3/library/io.html#io.UnsupportedOperation "Link to this definition")

An exception inheriting [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") and [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") that is raised when an unsupported operation is called on a stream.
See also

[`sys`](https://docs.python.org/3/library/sys.html#module-sys "sys: Access system-specific parameters and functions.")

contains the standard IO streams: [`sys.stdin`](https://docs.python.org/3/library/sys.html#sys.stdin "sys.stdin"), [`sys.stdout`](https://docs.python.org/3/library/sys.html#sys.stdout "sys.stdout"), and [`sys.stderr`](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr").
## Class hierarchy[¶](https://docs.python.org/3/library/io.html#class-hierarchy "Link to this heading")
The implementation of I/O streams is organized as a hierarchy of classes. First [abstract base classes](https://docs.python.org/3/glossary.html#term-abstract-base-class) (ABCs), which are used to specify the various categories of streams, then concrete classes providing the standard stream implementations.
Note
The abstract base classes also provide default implementations of some methods in order to help implementation of concrete stream classes. For example, [`BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase") provides unoptimized implementations of `readinto()` and `readline()`.
At the top of the I/O hierarchy is the abstract base class [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase"). It defines the basic interface to a stream. Note, however, that there is no separation between reading and writing to streams; implementations are allowed to raise [`UnsupportedOperation`](https://docs.python.org/3/library/io.html#io.UnsupportedOperation "io.UnsupportedOperation") if they do not support a given operation.
The [`RawIOBase`](https://docs.python.org/3/library/io.html#io.RawIOBase "io.RawIOBase") ABC extends [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase"). It deals with the reading and writing of bytes to a stream. [`FileIO`](https://docs.python.org/3/library/io.html#io.FileIO "io.FileIO") subclasses `RawIOBase` to provide an interface to files in the machine’s file system.
The [`BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase") ABC extends [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase"). It deals with buffering on a raw binary stream ([`RawIOBase`](https://docs.python.org/3/library/io.html#io.RawIOBase "io.RawIOBase")). Its subclasses, [`BufferedWriter`](https://docs.python.org/3/library/io.html#io.BufferedWriter "io.BufferedWriter"), [`BufferedReader`](https://docs.python.org/3/library/io.html#io.BufferedReader "io.BufferedReader"), and [`BufferedRWPair`](https://docs.python.org/3/library/io.html#io.BufferedRWPair "io.BufferedRWPair") buffer raw binary streams that are writable, readable, and both readable and writable, respectively. [`BufferedRandom`](https://docs.python.org/3/library/io.html#io.BufferedRandom "io.BufferedRandom") provides a buffered interface to seekable streams. Another `BufferedIOBase` subclass, [`BytesIO`](https://docs.python.org/3/library/io.html#io.BytesIO "io.BytesIO"), is a stream of in-memory bytes.
The [`TextIOBase`](https://docs.python.org/3/library/io.html#io.TextIOBase "io.TextIOBase") ABC extends [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase"). It deals with streams whose bytes represent text, and handles encoding and decoding to and from strings. [`TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper"), which extends `TextIOBase`, is a buffered text interface to a buffered raw stream ([`BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase")). Finally, [`StringIO`](https://docs.python.org/3/library/io.html#io.StringIO "io.StringIO") is an in-memory stream for text.
Argument names are not part of the specification, and only the arguments of [`open()`](https://docs.python.org/3/library/functions.html#open "open") are intended to be used as keyword arguments.
The following table summarizes the ABCs provided by the `io` module:
ABC | Inherits | Stub Methods | Mixin Methods and Properties
---|---|---|---
[`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase") |  | `fileno`, `seek`, and `truncate` | `close`, `closed`, `__enter__`, `__exit__`, `flush`, `isatty`, `__iter__`, `__next__`, `readable`, `readline`, `readlines`, `seekable`, `tell`, `writable`, and `writelines`
[`RawIOBase`](https://docs.python.org/3/library/io.html#io.RawIOBase "io.RawIOBase") | [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase") | `readinto` and `write` | Inherited [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase") methods, `read`, and `readall`
[`BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase") | [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase") | `detach`, `read`, `read1`, and `write` | Inherited [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase") methods, `readinto`, and `readinto1`
[`TextIOBase`](https://docs.python.org/3/library/io.html#io.TextIOBase "io.TextIOBase") | [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase") | `detach`, `read`, `readline`, and `write` | Inherited [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase") methods, `encoding`, `errors`, and `newlines`
### I/O Base Classes[¶](https://docs.python.org/3/library/io.html#i-o-base-classes "Link to this heading")

_class_ io.IOBase[¶](https://docs.python.org/3/library/io.html#io.IOBase "Link to this definition")

The abstract base class for all I/O classes.
This class provides empty abstract implementations for many methods that derived classes can override selectively; the default implementations represent a file that cannot be read, written or seeked.
Even though `IOBase` does not declare `read()` or `write()` because their signatures will vary, implementations and clients should consider those methods part of the interface. Also, implementations may raise a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") (or [`UnsupportedOperation`](https://docs.python.org/3/library/io.html#io.UnsupportedOperation "io.UnsupportedOperation")) when operations they do not support are called.
The basic type used for binary data read from or written to a file is [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes"). Other [bytes-like objects](https://docs.python.org/3/glossary.html#term-bytes-like-object) are accepted as method arguments too. Text I/O classes work with [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") data.
Note that calling any method (even inquiries) on a closed stream is undefined. Implementations may raise [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") in this case.
`IOBase` (and its subclasses) supports the iterator protocol, meaning that an `IOBase` object can be iterated over yielding the lines in a stream. Lines are defined slightly differently depending on whether the stream is a binary stream (yielding bytes), or a text stream (yielding character strings). See [`readline()`](https://docs.python.org/3/library/io.html#io.IOBase.readline "io.IOBase.readline") below.
`IOBase` is also a context manager and therefore supports the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement. In this example, _file_ is closed after the `with` statement’s suite is finished—even if an exception occurs:
Copy```
with open('spam.txt', 'w') as file:
    file.write('Spam and eggs!')

```

`IOBase` provides these data attributes and methods:

close()[¶](https://docs.python.org/3/library/io.html#io.IOBase.close "Link to this definition")

Flush and close this stream. This method has no effect if the file is already closed. Once the file is closed, any operation on the file (e.g. reading or writing) will raise a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError").
As a convenience, it is allowed to call this method more than once; only the first call, however, will have an effect.

closed[¶](https://docs.python.org/3/library/io.html#io.IOBase.closed "Link to this definition")

`True` if the stream is closed.

fileno()[¶](https://docs.python.org/3/library/io.html#io.IOBase.fileno "Link to this definition")

Return the underlying file descriptor (an integer) of the stream if it exists. An [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") is raised if the IO object does not use a file descriptor.

flush()[¶](https://docs.python.org/3/library/io.html#io.IOBase.flush "Link to this definition")

Flush the write buffers of the stream if applicable. This does nothing for read-only and non-blocking streams.

isatty()[¶](https://docs.python.org/3/library/io.html#io.IOBase.isatty "Link to this definition")

Return `True` if the stream is interactive (i.e., connected to a terminal/tty device).

readable()[¶](https://docs.python.org/3/library/io.html#io.IOBase.readable "Link to this definition")

Return `True` if the stream can be read from. If `False`, `read()` will raise [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError").

readline(_size =-1_, _/_)[¶](https://docs.python.org/3/library/io.html#io.IOBase.readline "Link to this definition")

Read and return one line from the stream. If _size_ is specified, at most _size_ bytes will be read.
The line terminator is always `b'\n'` for binary files; for text files, the _newline_ argument to [`open()`](https://docs.python.org/3/library/functions.html#open "open") can be used to select the line terminator(s) recognized.

readlines(_hint =-1_, _/_)[¶](https://docs.python.org/3/library/io.html#io.IOBase.readlines "Link to this definition")

Read and return a list of lines from the stream. _hint_ can be specified to control the number of lines read: no more lines will be read if the total size (in bytes/characters) of all lines so far exceeds _hint_.
_hint_ values of `0` or less, as well as `None`, are treated as no hint.
Note that it’s already possible to iterate on file objects using `for line in file: ...` without calling `file.readlines()`.

seek(_offset_ , _whence =os.SEEK_SET_, _/_)[¶](https://docs.python.org/3/library/io.html#io.IOBase.seek "Link to this definition")

Change the stream position to the given byte _offset_ , interpreted relative to the position indicated by _whence_ , and return the new absolute position. Values for _whence_ are:
  * [`os.SEEK_SET`](https://docs.python.org/3/library/os.html#os.SEEK_SET "os.SEEK_SET") or `0` – start of the stream (the default); _offset_ should be zero or positive
  * [`os.SEEK_CUR`](https://docs.python.org/3/library/os.html#os.SEEK_CUR "os.SEEK_CUR") or `1` – current stream position; _offset_ may be negative
  * [`os.SEEK_END`](https://docs.python.org/3/library/os.html#os.SEEK_END "os.SEEK_END") or `2` – end of the stream; _offset_ is usually negative


Added in version 3.1: The `SEEK_*` constants.
Added in version 3.3: Some operating systems could support additional values, like [`os.SEEK_HOLE`](https://docs.python.org/3/library/os.html#os.SEEK_HOLE "os.SEEK_HOLE") or [`os.SEEK_DATA`](https://docs.python.org/3/library/os.html#os.SEEK_DATA "os.SEEK_DATA"). The valid values for a file could depend on it being open in text or binary mode.

seekable()[¶](https://docs.python.org/3/library/io.html#io.IOBase.seekable "Link to this definition")

Return `True` if the stream supports random access. If `False`, [`seek()`](https://docs.python.org/3/library/io.html#io.IOBase.seek "io.IOBase.seek"), [`tell()`](https://docs.python.org/3/library/io.html#io.IOBase.tell "io.IOBase.tell") and [`truncate()`](https://docs.python.org/3/library/io.html#io.IOBase.truncate "io.IOBase.truncate") will raise [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError").

tell()[¶](https://docs.python.org/3/library/io.html#io.IOBase.tell "Link to this definition")

Return the current stream position.

truncate(_size =None_, _/_)[¶](https://docs.python.org/3/library/io.html#io.IOBase.truncate "Link to this definition")

Resize the stream to the given _size_ in bytes (or the current position if _size_ is not specified). The current stream position isn’t changed. This resizing can extend or reduce the current file size. In case of extension, the contents of the new file area depend on the platform (on most systems, additional bytes are zero-filled). The new file size is returned.
Changed in version 3.5: Windows will now zero-fill files when extending.

writable()[¶](https://docs.python.org/3/library/io.html#io.IOBase.writable "Link to this definition")

Return `True` if the stream supports writing. If `False`, `write()` and [`truncate()`](https://docs.python.org/3/library/io.html#io.IOBase.truncate "io.IOBase.truncate") will raise [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError").

writelines(_lines_ , _/_)[¶](https://docs.python.org/3/library/io.html#io.IOBase.writelines "Link to this definition")

Write a list of lines to the stream. Line separators are not added, so it is usual for each of the lines provided to have a line separator at the end.

__del__()[¶](https://docs.python.org/3/library/io.html#io.IOBase.__del__ "Link to this definition")

Prepare for object destruction. `IOBase` provides a default implementation of this method that calls the instance’s [`close()`](https://docs.python.org/3/library/io.html#io.IOBase.close "io.IOBase.close") method.

_class_ io.RawIOBase[¶](https://docs.python.org/3/library/io.html#io.RawIOBase "Link to this definition")

Base class for raw binary streams. It inherits from [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase").
Raw binary streams typically provide low-level access to an underlying OS device or API, and do not try to encapsulate it in high-level primitives (this functionality is done at a higher-level in buffered binary streams and text streams, described later in this page).
`RawIOBase` provides these methods in addition to those from [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase"):

read(_size =-1_, _/_)[¶](https://docs.python.org/3/library/io.html#io.RawIOBase.read "Link to this definition")

Read up to _size_ bytes from the object and return them. As a convenience, if _size_ is unspecified or -1, all bytes until EOF are returned. Otherwise, only one system call is ever made. Fewer than _size_ bytes may be returned if the operating system call returns fewer than _size_ bytes.
If 0 bytes are returned, and _size_ was not 0, this indicates end of file. If the object is in non-blocking mode and no bytes are available, `None` is returned.
The default implementation defers to [`readall()`](https://docs.python.org/3/library/io.html#io.RawIOBase.readall "io.RawIOBase.readall") and [`readinto()`](https://docs.python.org/3/library/io.html#io.RawIOBase.readinto "io.RawIOBase.readinto").

readall()[¶](https://docs.python.org/3/library/io.html#io.RawIOBase.readall "Link to this definition")

Read and return all the bytes from the stream until EOF, using multiple calls to the stream if necessary.

readinto(_b_ , _/_)[¶](https://docs.python.org/3/library/io.html#io.RawIOBase.readinto "Link to this definition")

Read bytes into a pre-allocated, writable [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) _b_ , and return the number of bytes read. For example, _b_ might be a [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray "bytearray"). If the object is in non-blocking mode and no bytes are available, `None` is returned.

write(_b_ , _/_)[¶](https://docs.python.org/3/library/io.html#io.RawIOBase.write "Link to this definition")

Write the given [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object), _b_ , to the underlying raw stream, and return the number of bytes written. This can be less than the length of _b_ in bytes, depending on specifics of the underlying raw stream, and especially if it is in non-blocking mode. `None` is returned if the raw stream is set not to block and no single byte could be readily written to it. The caller may release or mutate _b_ after this method returns, so the implementation should only access _b_ during the method call.

_class_ io.BufferedIOBase[¶](https://docs.python.org/3/library/io.html#io.BufferedIOBase "Link to this definition")

Base class for binary streams that support some kind of buffering. It inherits from [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase").
The main difference with [`RawIOBase`](https://docs.python.org/3/library/io.html#io.RawIOBase "io.RawIOBase") is that methods [`read()`](https://docs.python.org/3/library/io.html#io.BufferedIOBase.read "io.BufferedIOBase.read"), [`readinto()`](https://docs.python.org/3/library/io.html#io.BufferedIOBase.readinto "io.BufferedIOBase.readinto") and [`write()`](https://docs.python.org/3/library/io.html#io.BufferedIOBase.write "io.BufferedIOBase.write") will try (respectively) to read as much input as requested or to emit all provided data.
In addition, if the underlying raw stream is in non-blocking mode, when the system returns would block [`write()`](https://docs.python.org/3/library/io.html#io.BufferedIOBase.write "io.BufferedIOBase.write") will raise [`BlockingIOError`](https://docs.python.org/3/library/exceptions.html#BlockingIOError "BlockingIOError") with [`BlockingIOError.characters_written`](https://docs.python.org/3/library/exceptions.html#BlockingIOError.characters_written "BlockingIOError.characters_written") and [`read()`](https://docs.python.org/3/library/io.html#io.BufferedIOBase.read "io.BufferedIOBase.read") will return data read so far or `None` if no data is available.
Besides, the [`read()`](https://docs.python.org/3/library/io.html#io.BufferedIOBase.read "io.BufferedIOBase.read") method does not have a default implementation that defers to [`readinto()`](https://docs.python.org/3/library/io.html#io.BufferedIOBase.readinto "io.BufferedIOBase.readinto").
A typical `BufferedIOBase` implementation should not inherit from a [`RawIOBase`](https://docs.python.org/3/library/io.html#io.RawIOBase "io.RawIOBase") implementation, but wrap one, like [`BufferedWriter`](https://docs.python.org/3/library/io.html#io.BufferedWriter "io.BufferedWriter") and [`BufferedReader`](https://docs.python.org/3/library/io.html#io.BufferedReader "io.BufferedReader") do.
`BufferedIOBase` provides or overrides these data attributes and methods in addition to those from [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase"):

raw[¶](https://docs.python.org/3/library/io.html#io.BufferedIOBase.raw "Link to this definition")

The underlying raw stream (a [`RawIOBase`](https://docs.python.org/3/library/io.html#io.RawIOBase "io.RawIOBase") instance) that `BufferedIOBase` deals with. This is not part of the `BufferedIOBase` API and may not exist on some implementations.

detach()[¶](https://docs.python.org/3/library/io.html#io.BufferedIOBase.detach "Link to this definition")

Separate the underlying raw stream from the buffer and return it.
After the raw stream has been detached, the buffer is in an unusable state.
Some buffers, like [`BytesIO`](https://docs.python.org/3/library/io.html#io.BytesIO "io.BytesIO"), do not have the concept of a single raw stream to return from this method. They raise [`UnsupportedOperation`](https://docs.python.org/3/library/io.html#io.UnsupportedOperation "io.UnsupportedOperation").
Added in version 3.1.

read(_size =-1_, _/_)[¶](https://docs.python.org/3/library/io.html#io.BufferedIOBase.read "Link to this definition")

Read and return up to _size_ bytes. If the argument is omitted, `None`, or negative read as much as possible.
Fewer bytes may be returned than requested. An empty [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") object is returned if the stream is already at EOF. More than one read may be made and calls may be retried if specific errors are encountered, see [`os.read()`](https://docs.python.org/3/library/os.html#os.read "os.read") and [**PEP 475**](https://peps.python.org/pep-0475/) for more details. Less than size bytes being returned does not imply that EOF is imminent.
When reading as much as possible the default implementation will use `raw.readall` if available (which should implement [`RawIOBase.readall()`](https://docs.python.org/3/library/io.html#io.RawIOBase.readall "io.RawIOBase.readall")), otherwise will read in a loop until read returns `None`, an empty [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes"), or a non-retryable error. For most streams this is to EOF, but for non-blocking streams more data may become available.
Note
When the underlying raw stream is non-blocking, implementations may either raise [`BlockingIOError`](https://docs.python.org/3/library/exceptions.html#BlockingIOError "BlockingIOError") or return `None` if no data is available. `io` implementations return `None`.

read1(_size =-1_, _/_)[¶](https://docs.python.org/3/library/io.html#io.BufferedIOBase.read1 "Link to this definition")

Read and return up to _size_ bytes, calling [`readinto()`](https://docs.python.org/3/library/io.html#io.RawIOBase.readinto "io.RawIOBase.readinto") which may retry if [`EINTR`](https://docs.python.org/3/library/errno.html#errno.EINTR "errno.EINTR") is encountered per [**PEP 475**](https://peps.python.org/pep-0475/). If _size_ is `-1` or not provided, the implementation will choose an arbitrary value for _size_.
