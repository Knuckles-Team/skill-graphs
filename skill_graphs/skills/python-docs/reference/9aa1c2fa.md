Note
When the underlying raw stream is non-blocking, implementations may either raise [`BlockingIOError`](https://docs.python.org/3/library/exceptions.html#BlockingIOError "BlockingIOError") or return `None` if no data is available. `io` implementations return `None`.

readinto(_b_ , _/_)[¶](https://docs.python.org/3/library/io.html#io.BufferedIOBase.readinto "Link to this definition")

Read bytes into a pre-allocated, writable [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) _b_ and return the number of bytes read. For example, _b_ might be a [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray "bytearray").
Like [`read()`](https://docs.python.org/3/library/io.html#io.BufferedIOBase.read "io.BufferedIOBase.read"), multiple reads may be issued to the underlying raw stream, unless the latter is interactive.
A [`BlockingIOError`](https://docs.python.org/3/library/exceptions.html#BlockingIOError "BlockingIOError") is raised if the underlying raw stream is in non blocking-mode, and has no data available at the moment.

readinto1(_b_ , _/_)[¶](https://docs.python.org/3/library/io.html#io.BufferedIOBase.readinto1 "Link to this definition")

Read bytes into a pre-allocated, writable [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) _b_ , using at most one call to the underlying raw stream’s [`read()`](https://docs.python.org/3/library/io.html#io.RawIOBase.read "io.RawIOBase.read") (or [`readinto()`](https://docs.python.org/3/library/io.html#io.RawIOBase.readinto "io.RawIOBase.readinto")) method. Return the number of bytes read.
A [`BlockingIOError`](https://docs.python.org/3/library/exceptions.html#BlockingIOError "BlockingIOError") is raised if the underlying raw stream is in non blocking-mode, and has no data available at the moment.
Added in version 3.5.

write(_b_ , _/_)[¶](https://docs.python.org/3/library/io.html#io.BufferedIOBase.write "Link to this definition")

Write the given [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object), _b_ , and return the number of bytes written (always equal to the length of _b_ in bytes, since if the write fails an [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") will be raised). Depending on the actual implementation, these bytes may be readily written to the underlying stream, or held in a buffer for performance and latency reasons.
When in non-blocking mode, a [`BlockingIOError`](https://docs.python.org/3/library/exceptions.html#BlockingIOError "BlockingIOError") is raised if the data needed to be written to the raw stream but it couldn’t accept all the data without blocking.
The caller may release or mutate _b_ after this method returns, so the implementation should only access _b_ during the method call.
### Raw File I/O[¶](https://docs.python.org/3/library/io.html#raw-file-i-o "Link to this heading")

_class_ io.FileIO(_name_ , _mode ='r'_, _closefd =True_, _opener =None_)[¶](https://docs.python.org/3/library/io.html#io.FileIO "Link to this definition")

A raw binary stream representing an OS-level file containing bytes data. It inherits from [`RawIOBase`](https://docs.python.org/3/library/io.html#io.RawIOBase "io.RawIOBase").
The _name_ can be one of two things:
  * a character string or [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") object representing the path to the file which will be opened. In this case closefd must be `True` (the default) otherwise an error will be raised.
  * an integer representing the number of an existing OS-level file descriptor to which the resulting `FileIO` object will give access. When the FileIO object is closed this fd will be closed as well, unless _closefd_ is set to `False`.


The _mode_ can be `'r'`, `'w'`, `'x'` or `'a'` for reading (default), writing, exclusive creation or appending. The file will be created if it doesn’t exist when opened for writing or appending; it will be truncated when opened for writing. [`FileExistsError`](https://docs.python.org/3/library/exceptions.html#FileExistsError "FileExistsError") will be raised if it already exists when opened for creating. Opening a file for creating implies writing, so this mode behaves in a similar way to `'w'`. Add a `'+'` to the mode to allow simultaneous reading and writing.
The [`read()`](https://docs.python.org/3/library/io.html#io.RawIOBase.read "io.RawIOBase.read") (when called with a positive argument), [`readinto()`](https://docs.python.org/3/library/io.html#io.RawIOBase.readinto "io.RawIOBase.readinto") and [`write()`](https://docs.python.org/3/library/io.html#io.RawIOBase.write "io.RawIOBase.write") methods on this class will only make one system call.
A custom opener can be used by passing a callable as _opener_. The underlying file descriptor for the file object is then obtained by calling _opener_ with (_name_ , _flags_). _opener_ must return an open file descriptor (passing [`os.open`](https://docs.python.org/3/library/os.html#os.open "os.open") as _opener_ results in functionality similar to passing `None`).
The newly created file is [non-inheritable](https://docs.python.org/3/library/os.html#fd-inheritance).
See the [`open()`](https://docs.python.org/3/library/functions.html#open "open") built-in function for examples on using the _opener_ parameter.
Changed in version 3.3: The _opener_ parameter was added. The `'x'` mode was added.
Changed in version 3.4: The file is now non-inheritable.
`FileIO` provides these data attributes in addition to those from [`RawIOBase`](https://docs.python.org/3/library/io.html#io.RawIOBase "io.RawIOBase") and [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase"):

mode[¶](https://docs.python.org/3/library/io.html#io.FileIO.mode "Link to this definition")

The mode as given in the constructor.

name[¶](https://docs.python.org/3/library/io.html#io.FileIO.name "Link to this definition")

The file name. This is the file descriptor of the file when no name is given in the constructor.
### Buffered Streams[¶](https://docs.python.org/3/library/io.html#buffered-streams "Link to this heading")
Buffered I/O streams provide a higher-level interface to an I/O device than raw I/O does.

_class_ io.BytesIO(_initial_bytes =b''_)[¶](https://docs.python.org/3/library/io.html#io.BytesIO "Link to this definition")

A binary stream using an in-memory bytes buffer. It inherits from [`BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase"). The buffer is discarded when the [`close()`](https://docs.python.org/3/library/io.html#io.IOBase.close "io.IOBase.close") method is called.
The optional argument _initial_bytes_ is a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) that contains initial data.
`BytesIO` provides or overrides these methods in addition to those from [`BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase") and [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase"):

getbuffer()[¶](https://docs.python.org/3/library/io.html#io.BytesIO.getbuffer "Link to this definition")

Return a readable and writable view over the contents of the buffer without copying them. Also, mutating the view will transparently update the contents of the buffer:
Copy```
>>> b = io.BytesIO(b"abcdef")
>>> view = b.getbuffer()
>>> view[2:4] = b"56"
>>> b.getvalue()
b'ab56ef'

```

Note
As long as the view exists, the `BytesIO` object cannot be resized or closed.
Added in version 3.2.

getvalue()[¶](https://docs.python.org/3/library/io.html#io.BytesIO.getvalue "Link to this definition")

Return [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") containing the entire contents of the buffer.

read1(_size =-1_, _/_)[¶](https://docs.python.org/3/library/io.html#io.BytesIO.read1 "Link to this definition")

In `BytesIO`, this is the same as [`read()`](https://docs.python.org/3/library/io.html#io.BufferedIOBase.read "io.BufferedIOBase.read").
Changed in version 3.7: The _size_ argument is now optional.

readinto1(_b_ , _/_)[¶](https://docs.python.org/3/library/io.html#io.BytesIO.readinto1 "Link to this definition")

In `BytesIO`, this is the same as [`readinto()`](https://docs.python.org/3/library/io.html#io.BufferedIOBase.readinto "io.BufferedIOBase.readinto").
Added in version 3.5.

_class_ io.BufferedReader(_raw_ , _buffer_size =DEFAULT_BUFFER_SIZE_)[¶](https://docs.python.org/3/library/io.html#io.BufferedReader "Link to this definition")

A buffered binary stream providing higher-level access to a readable, non seekable [`RawIOBase`](https://docs.python.org/3/library/io.html#io.RawIOBase "io.RawIOBase") raw binary stream. It inherits from [`BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase").
When reading data from this object, a larger amount of data may be requested from the underlying raw stream, and kept in an internal buffer. The buffered data can then be returned directly on subsequent reads.
The constructor creates a `BufferedReader` for the given readable _raw_ stream and _buffer_size_. If _buffer_size_ is omitted, [`DEFAULT_BUFFER_SIZE`](https://docs.python.org/3/library/io.html#io.DEFAULT_BUFFER_SIZE "io.DEFAULT_BUFFER_SIZE") is used.
`BufferedReader` provides or overrides these methods in addition to those from [`BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase") and [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase"):

peek(_size =0_, _/_)[¶](https://docs.python.org/3/library/io.html#io.BufferedReader.peek "Link to this definition")

Return bytes from the stream without advancing the position. The number of bytes returned may be less or more than requested. If the underlying raw stream is non-blocking and the operation would block, returns empty bytes.

read(_size =-1_, _/_)[¶](https://docs.python.org/3/library/io.html#io.BufferedReader.read "Link to this definition")

In `BufferedReader` this is the same as [`io.BufferedIOBase.read()`](https://docs.python.org/3/library/io.html#io.BufferedIOBase.read "io.BufferedIOBase.read")

read1(_size =-1_, _/_)[¶](https://docs.python.org/3/library/io.html#io.BufferedReader.read1 "Link to this definition")

In `BufferedReader` this is the same as [`io.BufferedIOBase.read1()`](https://docs.python.org/3/library/io.html#io.BufferedIOBase.read1 "io.BufferedIOBase.read1")
Changed in version 3.7: The _size_ argument is now optional.

_class_ io.BufferedWriter(_raw_ , _buffer_size =DEFAULT_BUFFER_SIZE_)[¶](https://docs.python.org/3/library/io.html#io.BufferedWriter "Link to this definition")

A buffered binary stream providing higher-level access to a writeable, non seekable [`RawIOBase`](https://docs.python.org/3/library/io.html#io.RawIOBase "io.RawIOBase") raw binary stream. It inherits from [`BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase").
When writing to this object, data is normally placed into an internal buffer. The buffer will be written out to the underlying [`RawIOBase`](https://docs.python.org/3/library/io.html#io.RawIOBase "io.RawIOBase") object under various conditions, including:
  * when the buffer gets too small for all pending data;
  * when [`flush()`](https://docs.python.org/3/library/io.html#io.BufferedWriter.flush "io.BufferedWriter.flush") is called;
  * when a [`seek()`](https://docs.python.org/3/library/io.html#io.IOBase.seek "io.IOBase.seek") is requested (for [`BufferedRandom`](https://docs.python.org/3/library/io.html#io.BufferedRandom "io.BufferedRandom") objects);
  * when the `BufferedWriter` object is closed or destroyed.


The constructor creates a `BufferedWriter` for the given writeable _raw_ stream. If the _buffer_size_ is not given, it defaults to [`DEFAULT_BUFFER_SIZE`](https://docs.python.org/3/library/io.html#io.DEFAULT_BUFFER_SIZE "io.DEFAULT_BUFFER_SIZE").
`BufferedWriter` provides or overrides these methods in addition to those from [`BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase") and [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase"):

flush()[¶](https://docs.python.org/3/library/io.html#io.BufferedWriter.flush "Link to this definition")

Force bytes held in the buffer into the raw stream. A [`BlockingIOError`](https://docs.python.org/3/library/exceptions.html#BlockingIOError "BlockingIOError") should be raised if the raw stream blocks.

write(_b_ , _/_)[¶](https://docs.python.org/3/library/io.html#io.BufferedWriter.write "Link to this definition")

Write the [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object), _b_ , and return the number of bytes written. When in non-blocking mode, a [`BlockingIOError`](https://docs.python.org/3/library/exceptions.html#BlockingIOError "BlockingIOError") with [`BlockingIOError.characters_written`](https://docs.python.org/3/library/exceptions.html#BlockingIOError.characters_written "BlockingIOError.characters_written") set is raised if the buffer needs to be written out but the raw stream blocks.

_class_ io.BufferedRandom(_raw_ , _buffer_size =DEFAULT_BUFFER_SIZE_)[¶](https://docs.python.org/3/library/io.html#io.BufferedRandom "Link to this definition")

A buffered binary stream providing higher-level access to a seekable [`RawIOBase`](https://docs.python.org/3/library/io.html#io.RawIOBase "io.RawIOBase") raw binary stream. It inherits from [`BufferedReader`](https://docs.python.org/3/library/io.html#io.BufferedReader "io.BufferedReader") and [`BufferedWriter`](https://docs.python.org/3/library/io.html#io.BufferedWriter "io.BufferedWriter").
The constructor creates a reader and writer for a seekable raw stream, given in the first argument. If the _buffer_size_ is omitted it defaults to [`DEFAULT_BUFFER_SIZE`](https://docs.python.org/3/library/io.html#io.DEFAULT_BUFFER_SIZE "io.DEFAULT_BUFFER_SIZE").
`BufferedRandom` is capable of anything [`BufferedReader`](https://docs.python.org/3/library/io.html#io.BufferedReader "io.BufferedReader") or [`BufferedWriter`](https://docs.python.org/3/library/io.html#io.BufferedWriter "io.BufferedWriter") can do. In addition, [`seek()`](https://docs.python.org/3/library/io.html#io.IOBase.seek "io.IOBase.seek") and [`tell()`](https://docs.python.org/3/library/io.html#io.IOBase.tell "io.IOBase.tell") are guaranteed to be implemented.

_class_ io.BufferedRWPair(_reader_ , _writer_ , _buffer_size =DEFAULT_BUFFER_SIZE_, _/_)[¶](https://docs.python.org/3/library/io.html#io.BufferedRWPair "Link to this definition")

A buffered binary stream providing higher-level access to two non seekable [`RawIOBase`](https://docs.python.org/3/library/io.html#io.RawIOBase "io.RawIOBase") raw binary streams—one readable, the other writeable. It inherits from [`BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase").
_reader_ and _writer_ are [`RawIOBase`](https://docs.python.org/3/library/io.html#io.RawIOBase "io.RawIOBase") objects that are readable and writeable respectively. If the _buffer_size_ is omitted it defaults to [`DEFAULT_BUFFER_SIZE`](https://docs.python.org/3/library/io.html#io.DEFAULT_BUFFER_SIZE "io.DEFAULT_BUFFER_SIZE").
`BufferedRWPair` implements all of [`BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase")'s methods except for [`detach()`](https://docs.python.org/3/library/io.html#io.BufferedIOBase.detach "io.BufferedIOBase.detach"), which raises [`UnsupportedOperation`](https://docs.python.org/3/library/io.html#io.UnsupportedOperation "io.UnsupportedOperation").
Warning
`BufferedRWPair` does not attempt to synchronize accesses to its underlying raw streams. You should not pass it the same object as reader and writer; use [`BufferedRandom`](https://docs.python.org/3/library/io.html#io.BufferedRandom "io.BufferedRandom") instead.
### Text I/O[¶](https://docs.python.org/3/library/io.html#id1 "Link to this heading")

_class_ io.TextIOBase[¶](https://docs.python.org/3/library/io.html#io.TextIOBase "Link to this definition")

Base class for text streams. This class provides a character and line based interface to stream I/O. It inherits from [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase").
`TextIOBase` provides or overrides these data attributes and methods in addition to those from [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase"):

encoding[¶](https://docs.python.org/3/library/io.html#io.TextIOBase.encoding "Link to this definition")

The name of the encoding used to decode the stream’s bytes into strings, and to encode strings into bytes.

errors[¶](https://docs.python.org/3/library/io.html#io.TextIOBase.errors "Link to this definition")

The error setting of the decoder or encoder.

newlines[¶](https://docs.python.org/3/library/io.html#io.TextIOBase.newlines "Link to this definition")

A string, a tuple of strings, or `None`, indicating the newlines translated so far. Depending on the implementation and the initial constructor flags, this may not be available.

buffer[¶](https://docs.python.org/3/library/io.html#io.TextIOBase.buffer "Link to this definition")

The underlying binary buffer (a [`BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase") or [`RawIOBase`](https://docs.python.org/3/library/io.html#io.RawIOBase "io.RawIOBase") instance) that `TextIOBase` deals with. This is not part of the `TextIOBase` API and may not exist in some implementations.

detach()[¶](https://docs.python.org/3/library/io.html#io.TextIOBase.detach "Link to this definition")

Separate the underlying binary buffer from the `TextIOBase` and return it.
After the underlying buffer has been detached, the `TextIOBase` is in an unusable state.
Some `TextIOBase` implementations, like [`StringIO`](https://docs.python.org/3/library/io.html#io.StringIO "io.StringIO"), may not have the concept of an underlying buffer and calling this method will raise [`UnsupportedOperation`](https://docs.python.org/3/library/io.html#io.UnsupportedOperation "io.UnsupportedOperation").
Added in version 3.1.

read(_size =-1_, _/_)[¶](https://docs.python.org/3/library/io.html#io.TextIOBase.read "Link to this definition")

Read and return at most _size_ characters from the stream as a single [`str`](https://docs.python.org/3/library/stdtypes.html#str "str"). If _size_ is negative or `None`, reads until EOF.

readline(_size =-1_, _/_)[¶](https://docs.python.org/3/library/io.html#io.TextIOBase.readline "Link to this definition")

Read until newline or EOF and return a single [`str`](https://docs.python.org/3/library/stdtypes.html#str "str"). If the stream is already at EOF, an empty string is returned.
If _size_ is specified, at most _size_ characters will be read.

seek(_offset_ , _whence =SEEK_SET_, _/_)[¶](https://docs.python.org/3/library/io.html#io.TextIOBase.seek "Link to this definition")

Change the stream position to the given _offset_. Behaviour depends on the _whence_ parameter. The default value for _whence_ is `SEEK_SET`.
  * `SEEK_SET` or `0`: seek from the start of the stream (the default); _offset_ must either be a number returned by [`TextIOBase.tell()`](https://docs.python.org/3/library/io.html#io.TextIOBase.tell "io.TextIOBase.tell"), or zero. Any other _offset_ value produces undefined behaviour.
  * `SEEK_CUR` or `1`: “seek” to the current position; _offset_ must be zero, which is a no-operation (all other values are unsupported).
  * `SEEK_END` or `2`: seek to the end of the stream; _offset_ must be zero (all other values are unsupported).


Return the new absolute position as an opaque number.
Added in version 3.1: The `SEEK_*` constants.

tell()[¶](https://docs.python.org/3/library/io.html#io.TextIOBase.tell "Link to this definition")

Return the current stream position as an opaque number. The number does not usually represent a number of bytes in the underlying binary storage.

write(_s_ , _/_)[¶](https://docs.python.org/3/library/io.html#io.TextIOBase.write "Link to this definition")

Write the string _s_ to the stream and return the number of characters written.

_class_ io.TextIOWrapper(_buffer_ , _encoding =None_, _errors =None_, _newline =None_, _line_buffering =False_, _write_through =False_)[¶](https://docs.python.org/3/library/io.html#io.TextIOWrapper "Link to this definition")

A buffered text stream providing higher-level access to a [`BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase") buffered binary stream. It inherits from [`TextIOBase`](https://docs.python.org/3/library/io.html#io.TextIOBase "io.TextIOBase").
_encoding_ gives the name of the encoding that the stream will be decoded or encoded with. In [UTF-8 Mode](https://docs.python.org/3/library/os.html#utf8-mode), this defaults to UTF-8. Otherwise, it defaults to [`locale.getencoding()`](https://docs.python.org/3/library/locale.html#locale.getencoding "locale.getencoding"). `encoding="locale"` can be used to specify the current locale’s encoding explicitly. See [Text Encoding](https://docs.python.org/3/library/io.html#io-text-encoding) for more information.
_errors_ is an optional string that specifies how encoding and decoding errors are to be handled. Pass `'strict'` to raise a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") exception if there is an encoding error (the default of `None` has the same effect), or pass `'ignore'` to ignore errors. (Note that ignoring encoding errors can lead to data loss.) `'replace'` causes a replacement marker (such as `'?'`) to be inserted where there is malformed data. `'backslashreplace'` causes malformed data to be replaced by a backslashed escape sequence. When writing, `'xmlcharrefreplace'` (replace with the appropriate XML character reference) or `'namereplace'` (replace with `\N{...}` escape sequences) can be used. Any other error handling name that has been registered with [`codecs.register_error()`](https://docs.python.org/3/library/codecs.html#codecs.register_error "codecs.register_error") is also valid.
_newline_ controls how line endings are handled. It can be `None`, `''`, `'\n'`, `'\r'`, and `'\r\n'`. It works as follows:
  * When reading input from the stream, if _newline_ is `None`, [universal newlines](https://docs.python.org/3/glossary.html#term-universal-newlines) mode is enabled. Lines in the input can end in `'\n'`, `'\r'`, or `'\r\n'`, and these are translated into `'\n'` before being returned to the caller. If _newline_ is `''`, universal newlines mode is enabled, but line endings are returned to the caller untranslated. If _newline_ has any of the other legal values, input lines are only terminated by the given string, and the line ending is returned to the caller untranslated.
  * When writing output to the stream, if _newline_ is `None`, any `'\n'` characters written are translated to the system default line separator, [`os.linesep`](https://docs.python.org/3/library/os.html#os.linesep "os.linesep"). If _newline_ is `''` or `'\n'`, no translation takes place. If _newline_ is any of the other legal values, any `'\n'` characters written are translated to the given string.


If _line_buffering_ is `True`, [`flush()`](https://docs.python.org/3/library/io.html#io.IOBase.flush "io.IOBase.flush") is implied when a call to write contains a newline character or a carriage return.
If _write_through_ is `True`, calls to [`write()`](https://docs.python.org/3/library/io.html#io.BufferedIOBase.write "io.BufferedIOBase.write") are guaranteed not to be buffered: any data written on the `TextIOWrapper` object is immediately handled to its underlying binary _buffer_.
Changed in version 3.3: The _write_through_ argument has been added.
Changed in version 3.3: The default _encoding_ is now `locale.getpreferredencoding(False)` instead of `locale.getpreferredencoding()`. Don’t change temporary the locale encoding using [`locale.setlocale()`](https://docs.python.org/3/library/locale.html#locale.setlocale "locale.setlocale"), use the current locale encoding instead of the user preferred encoding.
Changed in version 3.10: The _encoding_ argument now supports the `"locale"` dummy encoding name.
Note
When the underlying raw stream is non-blocking, a [`BlockingIOError`](https://docs.python.org/3/library/exceptions.html#BlockingIOError "BlockingIOError") may be raised if a read operation cannot be completed immediately.
`TextIOWrapper` provides these data attributes and methods in addition to those from [`TextIOBase`](https://docs.python.org/3/library/io.html#io.TextIOBase "io.TextIOBase") and [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase"):

line_buffering[¶](https://docs.python.org/3/library/io.html#io.TextIOWrapper.line_buffering "Link to this definition")

Whether line buffering is enabled.

write_through[¶](https://docs.python.org/3/library/io.html#io.TextIOWrapper.write_through "Link to this definition")

Whether writes are passed immediately to the underlying binary buffer.
Added in version 3.7.

reconfigure(_*_ , _encoding =None_, _errors =None_, _newline =None_, _line_buffering =None_, _write_through =None_)[¶](https://docs.python.org/3/library/io.html#io.TextIOWrapper.reconfigure "Link to this definition")
