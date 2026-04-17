## Overview[¶](https://docs.python.org/3/library/io.html#overview "Link to this heading")
The `io` module provides Python’s main facilities for dealing with various types of I/O. There are three main types of I/O: _text I/O_ , _binary I/O_ and _raw I/O_. These are generic categories, and various backing stores can be used for each of them. A concrete object belonging to any of these categories is called a [file object](https://docs.python.org/3/glossary.html#term-file-object). Other common terms are _stream_ and _file-like object_.
Independent of its category, each concrete stream object will also have various capabilities: it can be read-only, write-only, or read-write. It can also allow arbitrary random access (seeking forwards or backwards to any location), or only sequential access (for example in the case of a socket or pipe).
All streams are careful about the type of data you give to them. For example giving a [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") object to the `write()` method of a binary stream will raise a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError"). So will giving a [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") object to the `write()` method of a text stream.
Changed in version 3.3: Operations that used to raise [`IOError`](https://docs.python.org/3/library/exceptions.html#IOError "IOError") now raise [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError"), since `IOError` is now an alias of `OSError`.
### Text I/O[¶](https://docs.python.org/3/library/io.html#text-i-o "Link to this heading")
Text I/O expects and produces [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") objects. This means that whenever the backing store is natively made of bytes (such as in the case of a file), encoding and decoding of data is made transparently as well as optional translation of platform-specific newline characters.
The easiest way to create a text stream is with [`open()`](https://docs.python.org/3/library/functions.html#open "open"), optionally specifying an encoding:
Copy```
f = open("myfile.txt", "r", encoding="utf-8")

```

In-memory text streams are also available as [`StringIO`](https://docs.python.org/3/library/io.html#io.StringIO "io.StringIO") objects:
Copy```
f = io.StringIO("some initial text data")

```

Note
When working with a non-blocking stream, be aware that read operations on text I/O objects might raise a [`BlockingIOError`](https://docs.python.org/3/library/exceptions.html#BlockingIOError "BlockingIOError") if the stream cannot perform the operation immediately.
The text stream API is described in detail in the documentation of [`TextIOBase`](https://docs.python.org/3/library/io.html#io.TextIOBase "io.TextIOBase").
### Binary I/O[¶](https://docs.python.org/3/library/io.html#binary-i-o "Link to this heading")
Binary I/O (also called _buffered I/O_) expects [bytes-like objects](https://docs.python.org/3/glossary.html#term-bytes-like-object) and produces [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") objects. No encoding, decoding, or newline translation is performed. This category of streams can be used for all kinds of non-text data, and also when manual control over the handling of text data is desired.
The easiest way to create a binary stream is with [`open()`](https://docs.python.org/3/library/functions.html#open "open") with `'b'` in the mode string:
Copy```
f = open("myfile.jpg", "rb")

```

In-memory binary streams are also available as [`BytesIO`](https://docs.python.org/3/library/io.html#io.BytesIO "io.BytesIO") objects:
Copy```
f = io.BytesIO(b"some initial binary data: \x00\x01")

```

The binary stream API is described in detail in the docs of [`BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase").
Other library modules may provide additional ways to create text or binary streams. See [`socket.socket.makefile()`](https://docs.python.org/3/library/socket.html#socket.socket.makefile "socket.socket.makefile") for example.
### Raw I/O[¶](https://docs.python.org/3/library/io.html#raw-i-o "Link to this heading")
Raw I/O (also called _unbuffered I/O_) is generally used as a low-level building-block for binary and text streams; it is rarely useful to directly manipulate a raw stream from user code. Nevertheless, you can create a raw stream by opening a file in binary mode with buffering disabled:
Copy```
f = open("myfile.jpg", "rb", buffering=0)

```

The raw stream API is described in detail in the docs of [`RawIOBase`](https://docs.python.org/3/library/io.html#io.RawIOBase "io.RawIOBase").
## Text Encoding[¶](https://docs.python.org/3/library/io.html#text-encoding "Link to this heading")
The default encoding of [`TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper") and [`open()`](https://docs.python.org/3/library/functions.html#open "open") is locale-specific ([`locale.getencoding()`](https://docs.python.org/3/library/locale.html#locale.getencoding "locale.getencoding")).
However, many developers forget to specify the encoding when opening text files encoded in UTF-8 (e.g. JSON, TOML, Markdown, etc…) since most Unix platforms use UTF-8 locale by default. This causes bugs because the locale encoding is not UTF-8 for most Windows users. For example:
Copy```
# May not work on Windows when non-ASCII characters in the file.
with open("README.md") as f:
    long_description = f.read()

```

Accordingly, it is highly recommended that you specify the encoding explicitly when opening text files. If you want to use UTF-8, pass `encoding="utf-8"`. To use the current locale encoding, `encoding="locale"` is supported since Python 3.10.
See also

[Python UTF-8 Mode](https://docs.python.org/3/library/os.html#utf8-mode)

Python UTF-8 Mode can be used to change the default encoding to UTF-8 from locale-specific encoding.

[**PEP 686**](https://peps.python.org/pep-0686/)

Python 3.15 will make [Python UTF-8 Mode](https://docs.python.org/3/library/os.html#utf8-mode) default.
### Opt-in EncodingWarning[¶](https://docs.python.org/3/library/io.html#opt-in-encodingwarning "Link to this heading")
Added in version 3.10: See [**PEP 597**](https://peps.python.org/pep-0597/) for more details.
To find where the default locale encoding is used, you can enable the [`-X warn_default_encoding`](https://docs.python.org/3/using/cmdline.html#cmdoption-X) command line option or set the [`PYTHONWARNDEFAULTENCODING`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONWARNDEFAULTENCODING) environment variable, which will emit an [`EncodingWarning`](https://docs.python.org/3/library/exceptions.html#EncodingWarning "EncodingWarning") when the default encoding is used.
If you are providing an API that uses [`open()`](https://docs.python.org/3/library/functions.html#open "open") or [`TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper") and passes `encoding=None` as a parameter, you can use [`text_encoding()`](https://docs.python.org/3/library/io.html#io.text_encoding "io.text_encoding") so that callers of the API will emit an [`EncodingWarning`](https://docs.python.org/3/library/exceptions.html#EncodingWarning "EncodingWarning") if they don’t pass an `encoding`. However, please consider using UTF-8 by default (i.e. `encoding="utf-8"`) for new APIs.
