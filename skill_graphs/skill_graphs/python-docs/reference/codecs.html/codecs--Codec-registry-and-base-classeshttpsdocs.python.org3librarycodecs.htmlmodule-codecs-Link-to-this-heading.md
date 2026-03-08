#  `codecs` — Codec registry and base classes[¶](https://docs.python.org/3/library/codecs.html#module-codecs "Link to this heading")
**Source code:**
* * *
This module defines base classes for standard Python codecs (encoders and decoders) and provides access to the internal Python codec registry, which manages the codec and error handling lookup process. Most standard codecs are [text encodings](https://docs.python.org/3/glossary.html#term-text-encoding), which encode text to bytes (and decode bytes to text), but there are also codecs provided that encode text to text, and bytes to bytes. Custom codecs may encode and decode between arbitrary types, but some module features are restricted to be used specifically with text encodings or with codecs that encode to [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes").
The module defines the following functions for encoding and decoding with any codec:

codecs.encode(_obj_ , _encoding ='utf-8'_, _errors ='strict'_)[¶](https://docs.python.org/3/library/codecs.html#codecs.encode "Link to this definition")

Encodes _obj_ using the codec registered for _encoding_.
_Errors_ may be given to set the desired error handling scheme. The default error handler is `'strict'` meaning that encoding errors raise [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") (or a more codec specific subclass, such as [`UnicodeEncodeError`](https://docs.python.org/3/library/exceptions.html#UnicodeEncodeError "UnicodeEncodeError")). Refer to [Codec Base Classes](https://docs.python.org/3/library/codecs.html#codec-base-classes) for more information on codec error handling.

codecs.decode(_obj_ , _encoding ='utf-8'_, _errors ='strict'_)[¶](https://docs.python.org/3/library/codecs.html#codecs.decode "Link to this definition")

Decodes _obj_ using the codec registered for _encoding_.
_Errors_ may be given to set the desired error handling scheme. The default error handler is `'strict'` meaning that decoding errors raise [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") (or a more codec specific subclass, such as [`UnicodeDecodeError`](https://docs.python.org/3/library/exceptions.html#UnicodeDecodeError "UnicodeDecodeError")). Refer to [Codec Base Classes](https://docs.python.org/3/library/codecs.html#codec-base-classes) for more information on codec error handling.

codecs.charmap_build(_string_)[¶](https://docs.python.org/3/library/codecs.html#codecs.charmap_build "Link to this definition")

Return a mapping suitable for encoding with a custom single-byte encoding. Given a [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") _string_ of up to 256 characters representing a decoding table, returns either a compact internal mapping object `EncodingMap` or a [`dictionary`](https://docs.python.org/3/library/stdtypes.html#dict "dict") mapping character ordinals to byte values. Raises a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") on invalid input.
The full details for each codec can also be looked up directly:

codecs.lookup(_encoding_ , _/_)[¶](https://docs.python.org/3/library/codecs.html#codecs.lookup "Link to this definition")

Looks up the codec info in the Python codec registry and returns a [`CodecInfo`](https://docs.python.org/3/library/codecs.html#codecs.CodecInfo "codecs.CodecInfo") object as defined below.
Encodings are first looked up in the registry’s cache. If not found, the list of registered search functions is scanned. If no [`CodecInfo`](https://docs.python.org/3/library/codecs.html#codecs.CodecInfo "codecs.CodecInfo") object is found, a [`LookupError`](https://docs.python.org/3/library/exceptions.html#LookupError "LookupError") is raised. Otherwise, the `CodecInfo` object is stored in the cache and returned to the caller.

_class_ codecs.CodecInfo(_encode_ , _decode_ , _streamreader =None_, _streamwriter =None_, _incrementalencoder =None_, _incrementaldecoder =None_, _name =None_)[¶](https://docs.python.org/3/library/codecs.html#codecs.CodecInfo "Link to this definition")

Codec details when looking up the codec registry. The constructor arguments are stored in attributes of the same name:

name[¶](https://docs.python.org/3/library/codecs.html#codecs.CodecInfo.name "Link to this definition")

The name of the encoding.

encode[¶](https://docs.python.org/3/library/codecs.html#codecs.CodecInfo.encode "Link to this definition")


decode[¶](https://docs.python.org/3/library/codecs.html#codecs.CodecInfo.decode "Link to this definition")

The stateless encoding and decoding functions. These must be functions or methods which have the same interface as the [`encode()`](https://docs.python.org/3/library/codecs.html#codecs.Codec.encode "codecs.Codec.encode") and [`decode()`](https://docs.python.org/3/library/codecs.html#codecs.Codec.decode "codecs.Codec.decode") methods of Codec instances (see [Codec Interface](https://docs.python.org/3/library/codecs.html#codec-objects)). The functions or methods are expected to work in a stateless mode.

incrementalencoder[¶](https://docs.python.org/3/library/codecs.html#codecs.CodecInfo.incrementalencoder "Link to this definition")


incrementaldecoder[¶](https://docs.python.org/3/library/codecs.html#codecs.CodecInfo.incrementaldecoder "Link to this definition")

Incremental encoder and decoder classes or factory functions. These have to provide the interface defined by the base classes [`IncrementalEncoder`](https://docs.python.org/3/library/codecs.html#codecs.IncrementalEncoder "codecs.IncrementalEncoder") and [`IncrementalDecoder`](https://docs.python.org/3/library/codecs.html#codecs.IncrementalDecoder "codecs.IncrementalDecoder"), respectively. Incremental codecs can maintain state.

streamwriter[¶](https://docs.python.org/3/library/codecs.html#codecs.CodecInfo.streamwriter "Link to this definition")


streamreader[¶](https://docs.python.org/3/library/codecs.html#codecs.CodecInfo.streamreader "Link to this definition")

Stream writer and reader classes or factory functions. These have to provide the interface defined by the base classes [`StreamWriter`](https://docs.python.org/3/library/codecs.html#codecs.StreamWriter "codecs.StreamWriter") and [`StreamReader`](https://docs.python.org/3/library/codecs.html#codecs.StreamReader "codecs.StreamReader"), respectively. Stream codecs can maintain state.
To simplify access to the various codec components, the module provides these additional functions which use [`lookup()`](https://docs.python.org/3/library/codecs.html#codecs.lookup "codecs.lookup") for the codec lookup:

codecs.getencoder(_encoding_)[¶](https://docs.python.org/3/library/codecs.html#codecs.getencoder "Link to this definition")

Look up the codec for the given encoding and return its encoder function.
Raises a [`LookupError`](https://docs.python.org/3/library/exceptions.html#LookupError "LookupError") in case the encoding cannot be found.

codecs.getdecoder(_encoding_)[¶](https://docs.python.org/3/library/codecs.html#codecs.getdecoder "Link to this definition")

Look up the codec for the given encoding and return its decoder function.
Raises a [`LookupError`](https://docs.python.org/3/library/exceptions.html#LookupError "LookupError") in case the encoding cannot be found.

codecs.getincrementalencoder(_encoding_)[¶](https://docs.python.org/3/library/codecs.html#codecs.getincrementalencoder "Link to this definition")

Look up the codec for the given encoding and return its incremental encoder class or factory function.
Raises a [`LookupError`](https://docs.python.org/3/library/exceptions.html#LookupError "LookupError") in case the encoding cannot be found or the codec doesn’t support an incremental encoder.

codecs.getincrementaldecoder(_encoding_)[¶](https://docs.python.org/3/library/codecs.html#codecs.getincrementaldecoder "Link to this definition")

Look up the codec for the given encoding and return its incremental decoder class or factory function.
Raises a [`LookupError`](https://docs.python.org/3/library/exceptions.html#LookupError "LookupError") in case the encoding cannot be found or the codec doesn’t support an incremental decoder.

codecs.getreader(_encoding_)[¶](https://docs.python.org/3/library/codecs.html#codecs.getreader "Link to this definition")

Look up the codec for the given encoding and return its [`StreamReader`](https://docs.python.org/3/library/codecs.html#codecs.StreamReader "codecs.StreamReader") class or factory function.
Raises a [`LookupError`](https://docs.python.org/3/library/exceptions.html#LookupError "LookupError") in case the encoding cannot be found.

codecs.getwriter(_encoding_)[¶](https://docs.python.org/3/library/codecs.html#codecs.getwriter "Link to this definition")

Look up the codec for the given encoding and return its [`StreamWriter`](https://docs.python.org/3/library/codecs.html#codecs.StreamWriter "codecs.StreamWriter") class or factory function.
Raises a [`LookupError`](https://docs.python.org/3/library/exceptions.html#LookupError "LookupError") in case the encoding cannot be found.
Custom codecs are made available by registering a suitable codec search function:

codecs.register(_search_function_ , _/_)[¶](https://docs.python.org/3/library/codecs.html#codecs.register "Link to this definition")

Register a codec search function. Search functions are expected to take one argument, being the encoding name in all lower case letters with hyphens and spaces converted to underscores, and return a [`CodecInfo`](https://docs.python.org/3/library/codecs.html#codecs.CodecInfo "codecs.CodecInfo") object. In case a search function cannot find a given encoding, it should return `None`.
Changed in version 3.9: Hyphens and spaces are converted to underscore.

codecs.unregister(_search_function_ , _/_)[¶](https://docs.python.org/3/library/codecs.html#codecs.unregister "Link to this definition")

Unregister a codec search function and clear the registry’s cache. If the search function is not registered, do nothing.
Added in version 3.10.
While the builtin [`open()`](https://docs.python.org/3/library/functions.html#open "open") and the associated [`io`](https://docs.python.org/3/library/io.html#module-io "io: Core tools for working with streams.") module are the recommended approach for working with encoded text files, this module provides additional utility functions and classes that allow the use of a wider range of codecs when working with binary files:

codecs.open(_filename_ , _mode ='r'_, _encoding =None_, _errors ='strict'_, _buffering =-1_)[¶](https://docs.python.org/3/library/codecs.html#codecs.open "Link to this definition")

Open an encoded file using the given _mode_ and return an instance of [`StreamReaderWriter`](https://docs.python.org/3/library/codecs.html#codecs.StreamReaderWriter "codecs.StreamReaderWriter"), providing transparent encoding/decoding. The default file mode is `'r'`, meaning to open the file in read mode.
Note
If _encoding_ is not `None`, then the underlying encoded files are always opened in binary mode. No automatic conversion of `'\n'` is done on reading and writing. The _mode_ argument may be any binary mode acceptable to the built-in `open()` function; the `'b'` is automatically added.
_encoding_ specifies the encoding which is to be used for the file. Any encoding that encodes to and decodes from bytes is allowed, and the data types supported by the file methods depend on the codec used.
_errors_ may be given to define the error handling. It defaults to `'strict'` which causes a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") to be raised in case an encoding error occurs.
_buffering_ has the same meaning as for the built-in `open()` function. It defaults to -1 which means that the default buffer size will be used.
Changed in version 3.11: The `'U'` mode has been removed.
Deprecated since version 3.14: [`codecs.open()`](https://docs.python.org/3/library/codecs.html#codecs.open "codecs.open") has been superseded by `open()`.

codecs.EncodedFile(_file_ , _data_encoding_ , _file_encoding =None_, _errors ='strict'_)[¶](https://docs.python.org/3/library/codecs.html#codecs.EncodedFile "Link to this definition")

Return a [`StreamRecoder`](https://docs.python.org/3/library/codecs.html#codecs.StreamRecoder "codecs.StreamRecoder") instance, a wrapped version of _file_ which provides transparent transcoding. The original file is closed when the wrapped version is closed.
Data written to the wrapped file is decoded according to the given _data_encoding_ and then written to the original file as bytes using _file_encoding_. Bytes read from the original file are decoded according to _file_encoding_ , and the result is encoded using _data_encoding_.
If _file_encoding_ is not given, it defaults to _data_encoding_.
_errors_ may be given to define the error handling. It defaults to `'strict'`, which causes [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") to be raised in case an encoding error occurs.

codecs.iterencode(_iterator_ , _encoding_ , _errors ='strict'_, _** kwargs_)[¶](https://docs.python.org/3/library/codecs.html#codecs.iterencode "Link to this definition")

Uses an incremental encoder to iteratively encode the input provided by _iterator_. _iterator_ must yield [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") objects. This function is a [generator](https://docs.python.org/3/glossary.html#term-generator). The _errors_ argument (as well as any other keyword argument) is passed through to the incremental encoder.
This function requires that the codec accept text [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") objects to encode. Therefore it does not support bytes-to-bytes encoders such as `base64_codec`.

codecs.iterdecode(_iterator_ , _encoding_ , _errors ='strict'_, _** kwargs_)[¶](https://docs.python.org/3/library/codecs.html#codecs.iterdecode "Link to this definition")

Uses an incremental decoder to iteratively decode the input provided by _iterator_. _iterator_ must yield [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") objects. This function is a [generator](https://docs.python.org/3/glossary.html#term-generator). The _errors_ argument (as well as any other keyword argument) is passed through to the incremental decoder.
This function requires that the codec accept [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") objects to decode. Therefore it does not support text-to-text encoders such as `rot_13`, although `rot_13` may be used equivalently with [`iterencode()`](https://docs.python.org/3/library/codecs.html#codecs.iterencode "codecs.iterencode").

codecs.readbuffer_encode(_buffer_ , _errors =None_, _/_)[¶](https://docs.python.org/3/library/codecs.html#codecs.readbuffer_encode "Link to this definition")

Return a [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "tuple") containing the raw bytes of _buffer_ , a [buffer-compatible object](https://docs.python.org/3/c-api/buffer.html#bufferobjects) or [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") (encoded to UTF-8 before processing), and their length in bytes.
The _errors_ argument is ignored.
Copy```
>>> codecs.readbuffer_encode(b"Zito")
(b'Zito', 4)

```

The module also provides the following constants which are useful for reading and writing to platform dependent files:

codecs.BOM[¶](https://docs.python.org/3/library/codecs.html#codecs.BOM "Link to this definition")


codecs.BOM_BE[¶](https://docs.python.org/3/library/codecs.html#codecs.BOM_BE "Link to this definition")


codecs.BOM_LE[¶](https://docs.python.org/3/library/codecs.html#codecs.BOM_LE "Link to this definition")


codecs.BOM_UTF8[¶](https://docs.python.org/3/library/codecs.html#codecs.BOM_UTF8 "Link to this definition")


codecs.BOM_UTF16[¶](https://docs.python.org/3/library/codecs.html#codecs.BOM_UTF16 "Link to this definition")


codecs.BOM_UTF16_BE[¶](https://docs.python.org/3/library/codecs.html#codecs.BOM_UTF16_BE "Link to this definition")


codecs.BOM_UTF16_LE[¶](https://docs.python.org/3/library/codecs.html#codecs.BOM_UTF16_LE "Link to this definition")


codecs.BOM_UTF32[¶](https://docs.python.org/3/library/codecs.html#codecs.BOM_UTF32 "Link to this definition")


codecs.BOM_UTF32_BE[¶](https://docs.python.org/3/library/codecs.html#codecs.BOM_UTF32_BE "Link to this definition")


codecs.BOM_UTF32_LE[¶](https://docs.python.org/3/library/codecs.html#codecs.BOM_UTF32_LE "Link to this definition")

These constants define various byte sequences, being Unicode byte order marks (BOMs) for several encodings. They are used in UTF-16 and UTF-32 data streams to indicate the byte order used, and in UTF-8 as a Unicode signature. [`BOM_UTF16`](https://docs.python.org/3/library/codecs.html#codecs.BOM_UTF16 "codecs.BOM_UTF16") is either [`BOM_UTF16_BE`](https://docs.python.org/3/library/codecs.html#codecs.BOM_UTF16_BE "codecs.BOM_UTF16_BE") or [`BOM_UTF16_LE`](https://docs.python.org/3/library/codecs.html#codecs.BOM_UTF16_LE "codecs.BOM_UTF16_LE") depending on the platform’s native byte order, [`BOM`](https://docs.python.org/3/library/codecs.html#codecs.BOM "codecs.BOM") is an alias for `BOM_UTF16`, [`BOM_LE`](https://docs.python.org/3/library/codecs.html#codecs.BOM_LE "codecs.BOM_LE") for `BOM_UTF16_LE` and [`BOM_BE`](https://docs.python.org/3/library/codecs.html#codecs.BOM_BE "codecs.BOM_BE") for `BOM_UTF16_BE`. The others represent the BOM in UTF-8 and UTF-32 encodings.
## Codec Base Classes[¶](https://docs.python.org/3/library/codecs.html#codec-base-classes "Link to this heading")
The `codecs` module defines a set of base classes which define the interfaces for working with codec objects, and can also be used as the basis for custom codec implementations.
Each codec has to define four interfaces to make it usable as codec in Python: stateless encoder, stateless decoder, stream reader and stream writer. The stream reader and writers typically reuse the stateless encoder/decoder to implement the file protocols. Codec authors also need to define how the codec will handle encoding and decoding errors.
### Error Handlers[¶](https://docs.python.org/3/library/codecs.html#error-handlers "Link to this heading")
To simplify and standardize error handling, codecs may implement different error handling schemes by accepting the _errors_ string argument:
Copy```
>>> 'German ß, ♬'.encode(encoding='ascii', errors='backslashreplace')
b'German \\xdf, \\u266c'
>>> 'German ß, ♬'.encode(encoding='ascii', errors='xmlcharrefreplace')
b'German &#223;, &#9836;'

```

The following error handlers can be used with all Python [Standard Encodings](https://docs.python.org/3/library/codecs.html#standard-encodings) codecs:
Value | Meaning
---|---
`'strict'` | Raise [`UnicodeError`](https://docs.python.org/3/library/exceptions.html#UnicodeError "UnicodeError") (or a subclass), this is the default. Implemented in [`strict_errors()`](https://docs.python.org/3/library/codecs.html#codecs.strict_errors "codecs.strict_errors").
`'ignore'` | Ignore the malformed data and continue without further notice. Implemented in [`ignore_errors()`](https://docs.python.org/3/library/codecs.html#codecs.ignore_errors "codecs.ignore_errors").
`'replace'` | Replace with a replacement marker. On encoding, use `?` (ASCII character). On decoding, use `�` (U+FFFD, the official REPLACEMENT CHARACTER). Implemented in [`replace_errors()`](https://docs.python.org/3/library/codecs.html#codecs.replace_errors "codecs.replace_errors").
`'backslashreplace'` | Replace with backslashed escape sequences. On encoding, use hexadecimal form of Unicode code point with formats `\x_hh_``\u_xxxx_``\U_xxxxxxxx_`. On decoding, use hexadecimal form of byte value with format`\x _hh_`. Implemented in[`backslashreplace_errors()`](https://docs.python.org/3/library/codecs.html#codecs.backslashreplace_errors "codecs.backslashreplace_errors").
`'surrogateescape'` | On decoding, replace byte with individual surrogate code ranging from `U+DC80` to `U+DCFF`. This code will then be turned back into the same byte when the `'surrogateescape'` error handler is used when encoding the data. (See [**PEP 383**](https://peps.python.org/pep-0383/) for more.)
The following error handlers are only applicable to encoding (within [text encodings](https://docs.python.org/3/glossary.html#term-text-encoding)):
Value | Meaning
---|---
`'xmlcharrefreplace'` | Replace with XML/HTML numeric character reference, which is a decimal form of Unicode code point with format `&#_num_;`. Implemented in[`xmlcharrefreplace_errors()`](https://docs.python.org/3/library/codecs.html#codecs.xmlcharrefreplace_errors "codecs.xmlcharrefreplace_errors").
`'namereplace'` | Replace with `\N{...}` escape sequences, what appears in the braces is the Name property from Unicode Character Database. Implemented in [`namereplace_errors()`](https://docs.python.org/3/library/codecs.html#codecs.namereplace_errors "codecs.namereplace_errors").
In addition, the following error handler is specific to the given codecs:
Value | Codecs | Meaning
---|---|---
`'surrogatepass'` | utf-8, utf-16, utf-32, utf-16-be, utf-16-le, utf-32-be, utf-32-le | Allow encoding and decoding surrogate code point (`U+D800` - `U+DFFF`) as normal code point. Otherwise these codecs treat the presence of surrogate code point in [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") as an error.
Added in version 3.1: The `'surrogateescape'` and `'surrogatepass'` error handlers.
Changed in version 3.4: The `'surrogatepass'` error handler now works with utf-16* and utf-32* codecs.
Added in version 3.5: The `'namereplace'` error handler.
Changed in version 3.5: The `'backslashreplace'` error handler now works with decoding and translating.
The set of allowed values can be extended by registering a new named error handler:

codecs.register_error(_name_ , _error_handler_ , _/_)[¶](https://docs.python.org/3/library/codecs.html#codecs.register_error "Link to this definition")

Register the error handling function _error_handler_ under the name _name_. The _error_handler_ argument will be called during encoding and decoding in case of an error, when _name_ is specified as the errors parameter.
For encoding, _error_handler_ will be called with a [`UnicodeEncodeError`](https://docs.python.org/3/library/exceptions.html#UnicodeEncodeError "UnicodeEncodeError") instance, which contains information about the location of the error. The error handler must either raise this or a different exception, or return a tuple with a replacement for the unencodable part of the input and a position where encoding should continue. The replacement may be either [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") or [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes"). If the replacement is bytes, the encoder will simply copy them into the output buffer. If the replacement is a string, the encoder will encode the replacement. Encoding continues on original input at the specified position. Negative position values will be treated as being relative to the end of the input string. If the resulting position is out of bound an [`IndexError`](https://docs.python.org/3/library/exceptions.html#IndexError "IndexError") will be raised.
Decoding and translating works similarly, except [`UnicodeDecodeError`](https://docs.python.org/3/library/exceptions.html#UnicodeDecodeError "UnicodeDecodeError") or [`UnicodeTranslateError`](https://docs.python.org/3/library/exceptions.html#UnicodeTranslateError "UnicodeTranslateError") will be passed to the handler and that the replacement from the error handler will be put into the output directly.
Previously registered error handlers (including the standard error handlers) can be looked up by name:

codecs.lookup_error(_name_ , _/_)[¶](https://docs.python.org/3/library/codecs.html#codecs.lookup_error "Link to this definition")

Return the error handler previously registered under the name _name_.
Raises a [`LookupError`](https://docs.python.org/3/library/exceptions.html#LookupError "LookupError") in case the handler cannot be found.
The following standard error handlers are also made available as module level functions:

codecs.strict_errors(_exception_)[¶](https://docs.python.org/3/library/codecs.html#codecs.strict_errors "Link to this definition")

Implements the `'strict'` error handling.
Each encoding or decoding error raises a [`UnicodeError`](https://docs.python.org/3/library/exceptions.html#UnicodeError "UnicodeError").

codecs.ignore_errors(_exception_)[¶](https://docs.python.org/3/library/codecs.html#codecs.ignore_errors "Link to this definition")

Implements the `'ignore'` error handling.
Malformed data is ignored; encoding or decoding is continued without further notice.

codecs.replace_errors(_exception_)[¶](https://docs.python.org/3/library/codecs.html#codecs.replace_errors "Link to this definition")

Implements the `'replace'` error handling.
Substitutes `?` (ASCII character) for encoding errors or `�` (U+FFFD, the official REPLACEMENT CHARACTER) for decoding errors.

codecs.backslashreplace_errors(_exception_)[¶](https://docs.python.org/3/library/codecs.html#codecs.backslashreplace_errors "Link to this definition")

Implements the `'backslashreplace'` error handling.
Malformed data is replaced by a backslashed escape sequence. On encoding, use the hexadecimal form of Unicode code point with formats `\x_hh_``\u_xxxx_``\U_xxxxxxxx_`. On decoding, use the hexadecimal form of byte value with format`\x _hh_`.
Changed in version 3.5: Works with decoding and translating.

codecs.xmlcharrefreplace_errors(_exception_)[¶](https://docs.python.org/3/library/codecs.html#codecs.xmlcharrefreplace_errors "Link to this definition")

Implements the `'xmlcharrefreplace'` error handling (for encoding within [text encoding](https://docs.python.org/3/glossary.html#term-text-encoding) only).
The unencodable character is replaced by an appropriate XML/HTML numeric character reference, which is a decimal form of Unicode code point with format `&#_num_;`.

codecs.namereplace_errors(_exception_)[¶](https://docs.python.org/3/library/codecs.html#codecs.namereplace_errors "Link to this definition")

Implements the `'namereplace'` error handling (for encoding within [text encoding](https://docs.python.org/3/glossary.html#term-text-encoding) only).
The unencodable character is replaced by a `\N{...}` escape sequence. The set of characters that appear in the braces is the Name property from Unicode Character Database. For example, the German lowercase letter `'ß'` will be converted to byte sequence `\N{LATIN SMALL LETTER SHARP S}` .
Added in version 3.5.
### Stateless Encoding and Decoding[¶](https://docs.python.org/3/library/codecs.html#stateless-encoding-and-decoding "Link to this heading")
The base [`Codec`](https://docs.python.org/3/library/codecs.html#codecs.Codec "codecs.Codec") class defines these methods which also define the function interfaces of the stateless encoder and decoder:

_class_ codecs.Codec[¶](https://docs.python.org/3/library/codecs.html#codecs.Codec "Link to this definition")


encode(_input_ , _errors ='strict'_)[¶](https://docs.python.org/3/library/codecs.html#codecs.Codec.encode "Link to this definition")

Encodes the object _input_ and returns a tuple (output object, length consumed). For instance, [text encoding](https://docs.python.org/3/glossary.html#term-text-encoding) converts a string object to a bytes object using a particular character set encoding (e.g., `cp1252` or `iso-8859-1`).
The _errors_ argument defines the error handling to apply. It defaults to `'strict'` handling.
The method may not store state in the `Codec` instance. Use [`StreamWriter`](https://docs.python.org/3/library/codecs.html#codecs.StreamWriter "codecs.StreamWriter") for codecs which have to keep state in order to make encoding efficient.
The encoder must be able to handle zero length input and return an empty object of the output object type in this situation.

decode(_input_ , _errors ='strict'_)[¶](https://docs.python.org/3/library/codecs.html#codecs.Codec.decode "Link to this definition")

Decodes the object _input_ and returns a tuple (output object, length consumed). For instance, for a [text encoding](https://docs.python.org/3/glossary.html#term-text-encoding), decoding converts a bytes object encoded using a particular character set encoding to a string object.
For text encodings and bytes-to-bytes codecs, _input_ must be a bytes object or one which provides the read-only buffer interface – for example, buffer objects and memory mapped files.
The _errors_ argument defines the error handling to apply. It defaults to `'strict'` handling.
The method may not store state in the `Codec` instance. Use [`StreamReader`](https://docs.python.org/3/library/codecs.html#codecs.StreamReader "codecs.StreamReader") for codecs which have to keep state in order to make decoding efficient.
The decoder must be able to handle zero length input and return an empty object of the output object type in this situation.
### Incremental Encoding and Decoding[¶](https://docs.python.org/3/library/codecs.html#incremental-encoding-and-decoding "Link to this heading")
The [`IncrementalEncoder`](https://docs.python.org/3/library/codecs.html#codecs.IncrementalEncoder "codecs.IncrementalEncoder") and [`IncrementalDecoder`](https://docs.python.org/3/library/codecs.html#codecs.IncrementalDecoder "codecs.IncrementalDecoder") classes provide the basic interface for incremental encoding and decoding. Encoding/decoding the input isn’t done with one call to the stateless encoder/decoder function, but with multiple calls to the [`encode()`](https://docs.python.org/3/library/codecs.html#codecs.IncrementalEncoder.encode "codecs.IncrementalEncoder.encode")/[`decode()`](https://docs.python.org/3/library/codecs.html#codecs.IncrementalDecoder.decode "codecs.IncrementalDecoder.decode") method of the incremental encoder/decoder. The incremental encoder/decoder keeps track of the encoding/decoding process during method calls.
The joined output of calls to the [`encode()`](https://docs.python.org/3/library/codecs.html#codecs.IncrementalEncoder.encode "codecs.IncrementalEncoder.encode")/[`decode()`](https://docs.python.org/3/library/codecs.html#codecs.IncrementalDecoder.decode "codecs.IncrementalDecoder.decode") method is the same as if all the single inputs were joined into one, and this input was encoded/decoded with the stateless encoder/decoder.
#### IncrementalEncoder Objects[¶](https://docs.python.org/3/library/codecs.html#incrementalencoder-objects "Link to this heading")
The [`IncrementalEncoder`](https://docs.python.org/3/library/codecs.html#codecs.IncrementalEncoder "codecs.IncrementalEncoder") class is used for encoding an input in multiple steps. It defines the following methods which every incremental encoder must define in order to be compatible with the Python codec registry.

_class_ codecs.IncrementalEncoder(_errors ='strict'_)[¶](https://docs.python.org/3/library/codecs.html#codecs.IncrementalEncoder "Link to this definition")

Constructor for an `IncrementalEncoder` instance.
All incremental encoders must provide this constructor interface. They are free to add additional keyword arguments, but only the ones defined here are used by the Python codec registry.
The `IncrementalEncoder` may implement different error handling schemes by providing the _errors_ keyword argument. See [Error Handlers](https://docs.python.org/3/library/codecs.html#error-handlers) for possible values.
The _errors_ argument will be assigned to an attribute of the same name. Assigning to this attribute makes it possible to switch between different error handling strategies during the lifetime of the `IncrementalEncoder` object.

encode(_object_ , _final =False_)[¶](https://docs.python.org/3/library/codecs.html#codecs.IncrementalEncoder.encode "Link to this definition")

Encodes _object_ (taking the current state of the encoder into account) and returns the resulting encoded object. If this is the last call to `encode()` _final_ must be true (the default is false).

reset()[¶](https://docs.python.org/3/library/codecs.html#codecs.IncrementalEncoder.reset "Link to this definition")

Reset the encoder to the initial state. The output is discarded: call `.encode(object, final=True)`, passing an empty byte or text string if necessary, to reset the encoder and to get the output.

getstate()[¶](https://docs.python.org/3/library/codecs.html#codecs.IncrementalEncoder.getstate "Link to this definition")

Return the current state of the encoder which must be an integer. The implementation should make sure that `0` is the most common state. (States that are more complicated than integers can be converted into an integer by marshaling/pickling the state and encoding the bytes of the resulting string into an integer.)

setstate(_state_)[¶](https://docs.python.org/3/library/codecs.html#codecs.IncrementalEncoder.setstate "Link to this definition")

Set the state of the encoder to _state_. _state_ must be an encoder state returned by [`getstate()`](https://docs.python.org/3/library/codecs.html#codecs.IncrementalEncoder.getstate "codecs.IncrementalEncoder.getstate").
#### IncrementalDecoder Objects[¶](https://docs.python.org/3/library/codecs.html#incrementaldecoder-objects "Link to this heading")
The [`IncrementalDecoder`](https://docs.python.org/3/library/codecs.html#codecs.IncrementalDecoder "codecs.IncrementalDecoder") class is used for decoding an input in multiple steps. It defines the following methods which every incremental decoder must define in order to be compatible with the Python codec registry.

_class_ codecs.IncrementalDecoder(_errors ='strict'_)[¶](https://docs.python.org/3/library/codecs.html#codecs.IncrementalDecoder "Link to this definition")

Constructor for an `IncrementalDecoder` instance.
All incremental decoders must provide this constructor interface. They are free to add additional keyword arguments, but only the ones defined here are used by the Python codec registry.
The `IncrementalDecoder` may implement different error handling schemes by providing the _errors_ keyword argument. See [Error Handlers](https://docs.python.org/3/library/codecs.html#error-handlers) for possible values.
The _errors_ argument will be assigned to an attribute of the same name. Assigning to this attribute makes it possible to switch between different error handling strategies during the lifetime of the `IncrementalDecoder` object.

decode(_object_ , _final =False_)[¶](https://docs.python.org/3/library/codecs.html#codecs.IncrementalDecoder.decode "Link to this definition")

Decodes _object_ (taking the current state of the decoder into account) and returns the resulting decoded object. If this is the last call to `decode()` _final_ must be true (the default is false). If _final_ is true the decoder must decode the input completely and must flush all buffers. If this isn’t possible (e.g. because of incomplete byte sequences at the end of the input) it must initiate error handling just like in the stateless case (which might raise an exception).

reset()[¶](https://docs.python.org/3/library/codecs.html#codecs.IncrementalDecoder.reset "Link to this definition")

Reset the decoder to the initial state.

getstate()[¶](https://docs.python.org/3/library/codecs.html#codecs.IncrementalDecoder.getstate "Link to this definition")

Return the current state of the decoder. This must be a tuple with two items, the first must be the buffer containing the still undecoded input. The second must be an integer and can be additional state info. (The implementation should make sure that `0` is the most common additional state info.) If this additional state info is `0` it must be possible to set the decoder to the state which has no input buffered and `0` as the additional state info, so that feeding the previously buffered input to the decoder returns it to the previous state without producing any output. (Additional state info that is more complicated than integers can be converted into an integer by marshaling/pickling the info and encoding the bytes of the resulting string into an integer.)

setstate(_state_)[¶](https://docs.python.org/3/library/codecs.html#codecs.IncrementalDecoder.setstate "Link to this definition")

Set the state of the decoder to _state_. _state_ must be a decoder state returned by [`getstate()`](https://docs.python.org/3/library/codecs.html#codecs.IncrementalDecoder.getstate "codecs.IncrementalDecoder.getstate").
### Stream Encoding and Decoding[¶](https://docs.python.org/3/library/codecs.html#stream-encoding-and-decoding "Link to this heading")
The [`StreamWriter`](https://docs.python.org/3/library/codecs.html#codecs.StreamWriter "codecs.StreamWriter") and [`StreamReader`](https://docs.python.org/3/library/codecs.html#codecs.StreamReader "codecs.StreamReader") classes provide generic working interfaces which can be used to implement new encoding submodules very easily. See `encodings.utf_8` for an example of how this is done.
#### StreamWriter Objects[¶](https://docs.python.org/3/library/codecs.html#streamwriter-objects "Link to this heading")
The [`StreamWriter`](https://docs.python.org/3/library/codecs.html#codecs.StreamWriter "codecs.StreamWriter") class is a subclass of [`Codec`](https://docs.python.org/3/library/codecs.html#codecs.Codec "codecs.Codec") and defines the following methods which every stream writer must define in order to be compatible with the Python codec registry.

_class_ codecs.StreamWriter(_stream_ , _errors ='strict'_)[¶](https://docs.python.org/3/library/codecs.html#codecs.StreamWriter "Link to this definition")

Constructor for a `StreamWriter` instance.
All stream writers must provide this constructor interface. They are free to add additional keyword arguments, but only the ones defined here are used by the Python codec registry.
The _stream_ argument must be a file-like object open for writing text or binary data, as appropriate for the specific codec.
The `StreamWriter` may implement different error handling schemes by providing the _errors_ keyword argument. See [Error Handlers](https://docs.python.org/3/library/codecs.html#error-handlers) for the standard error handlers the underlying stream codec may support.
The _errors_ argument will be assigned to an attribute of the same name. Assigning to this attribute makes it possible to switch between different error handling strategies during the lifetime of the `StreamWriter` object.

write(_object_)[¶](https://docs.python.org/3/library/codecs.html#codecs.StreamWriter.write "Link to this definition")

Writes the object’s contents encoded to the stream.

writelines(_list_)[¶](https://docs.python.org/3/library/codecs.html#codecs.StreamWriter.writelines "Link to this definition")

Writes the concatenated iterable of strings to the stream (possibly by reusing the [`write()`](https://docs.python.org/3/library/codecs.html#codecs.StreamWriter.write "codecs.StreamWriter.write") method). Infinite or very large iterables are not supported. The standard bytes-to-bytes codecs do not support this method.

reset()[¶](https://docs.python.org/3/library/codecs.html#codecs.StreamWriter.reset "Link to this definition")

Resets the codec buffers used for keeping internal state.
Calling this method should ensure that the data on the output is put into a clean state that allows appending of new fresh data without having to rescan the whole stream to recover state.
In addition to the above methods, the [`StreamWriter`](https://docs.python.org/3/library/codecs.html#codecs.StreamWriter "codecs.StreamWriter") must also inherit all other methods and attributes from the underlying stream.
#### StreamReader Objects[¶](https://docs.python.org/3/library/codecs.html#streamreader-objects "Link to this heading")
The [`StreamReader`](https://docs.python.org/3/library/codecs.html#codecs.StreamReader "codecs.StreamReader") class is a subclass of [`Codec`](https://docs.python.org/3/library/codecs.html#codecs.Codec "codecs.Codec") and defines the following methods which every stream reader must define in order to be compatible with the Python codec registry.

_class_ codecs.StreamReader(_stream_ , _errors ='strict'_)[¶](https://docs.python.org/3/library/codecs.html#codecs.StreamReader "Link to this definition")

Constructor for a `StreamReader` instance.
All stream readers must provide this constructor interface. They are free to add additional keyword arguments, but only the ones defined here are used by the Python codec registry.
The _stream_ argument must be a file-like object open for reading text or binary data, as appropriate for the specific codec.
The `StreamReader` may implement different error handling schemes by providing the _errors_ keyword argument. See [Error Handlers](https://docs.python.org/3/library/codecs.html#error-handlers) for the standard error handlers the underlying stream codec may support.
The _errors_ argument will be assigned to an attribute of the same name. Assigning to this attribute makes it possible to switch between different error handling strategies during the lifetime of the `StreamReader` object.
The set of allowed values for the _errors_ argument can be extended with [`register_error()`](https://docs.python.org/3/library/codecs.html#codecs.register_error "codecs.register_error").

read(_size =-1_, _chars =-1_, _firstline =False_)[¶](https://docs.python.org/3/library/codecs.html#codecs.StreamReader.read "Link to this definition")

Decodes data from the stream and returns the resulting object.
The _chars_ argument indicates the number of decoded code points or bytes to return. The [`read()`](https://docs.python.org/3/library/codecs.html#codecs.StreamReader.read "codecs.StreamReader.read") method will never return more data than requested, but it might return less, if there is not enough available.
The _size_ argument indicates the approximate maximum number of encoded bytes or code points to read for decoding. The decoder can modify this setting as appropriate. The default value -1 indicates to read and decode as much as possible. This parameter is intended to prevent having to decode huge files in one step.
The _firstline_ flag indicates that it would be sufficient to only return the first line, if there are decoding errors on later lines.
The method should use a greedy read strategy meaning that it should read as much data as is allowed within the definition of the encoding and the given size, e.g. if optional encoding endings or state markers are available on the stream, these should be read too.

readline(_size =None_, _keepends =True_)[¶](https://docs.python.org/3/library/codecs.html#codecs.StreamReader.readline "Link to this definition")

Read one line from the input stream and return the decoded data.
_size_ , if given, is passed as size argument to the stream’s [`read()`](https://docs.python.org/3/library/codecs.html#codecs.StreamReader.read "codecs.StreamReader.read") method.
If _keepends_ is false line-endings will be stripped from the lines returned.

readlines(_sizehint =None_, _keepends =True_)[¶](https://docs.python.org/3/library/codecs.html#codecs.StreamReader.readlines "Link to this definition")

Read all lines available on the input stream and return them as a list of lines.
Line-endings are implemented using the codec’s [`decode()`](https://docs.python.org/3/library/codecs.html#codecs.decode "codecs.decode") method and are included in the list entries if _keepends_ is true.
_sizehint_ , if given, is passed as the _size_ argument to the stream’s [`read()`](https://docs.python.org/3/library/codecs.html#codecs.StreamReader.read "codecs.StreamReader.read") method.

reset()[¶](https://docs.python.org/3/library/codecs.html#codecs.StreamReader.reset "Link to this definition")

Resets the codec buffers used for keeping internal state.
Note that no stream repositioning should take place. This method is primarily intended to be able to recover from decoding errors.
In addition to the above methods, the [`StreamReader`](https://docs.python.org/3/library/codecs.html#codecs.StreamReader "codecs.StreamReader") must also inherit all other methods and attributes from the underlying stream.
#### StreamReaderWriter Objects[¶](https://docs.python.org/3/library/codecs.html#streamreaderwriter-objects "Link to this heading")
The [`StreamReaderWriter`](https://docs.python.org/3/library/codecs.html#codecs.StreamReaderWriter "codecs.StreamReaderWriter") is a convenience class that allows wrapping streams which work in both read and write modes.
The design is such that one can use the factory functions returned by the [`lookup()`](https://docs.python.org/3/library/codecs.html#codecs.lookup "codecs.lookup") function to construct the instance.

_class_ codecs.StreamReaderWriter(_stream_ , _Reader_ , _Writer_ , _errors ='strict'_)[¶](https://docs.python.org/3/library/codecs.html#codecs.StreamReaderWriter "Link to this definition")

Creates a `StreamReaderWriter` instance. _stream_ must be a file-like object. _Reader_ and _Writer_ must be factory functions or classes providing the [`StreamReader`](https://docs.python.org/3/library/codecs.html#codecs.StreamReader "codecs.StreamReader") and [`StreamWriter`](https://docs.python.org/3/library/codecs.html#codecs.StreamWriter "codecs.StreamWriter") interface resp. Error handling is done in the same way as defined for the stream readers and writers.
[`StreamReaderWriter`](https://docs.python.org/3/library/codecs.html#codecs.StreamReaderWriter "codecs.StreamReaderWriter") instances define the combined interfaces of [`StreamReader`](https://docs.python.org/3/library/codecs.html#codecs.StreamReader "codecs.StreamReader") and [`StreamWriter`](https://docs.python.org/3/library/codecs.html#codecs.StreamWriter "codecs.StreamWriter") classes. They inherit all other methods and attributes from the underlying stream.
#### StreamRecoder Objects[¶](https://docs.python.org/3/library/codecs.html#streamrecoder-objects "Link to this heading")
The [`StreamRecoder`](https://docs.python.org/3/library/codecs.html#codecs.StreamRecoder "codecs.StreamRecoder") translates data from one encoding to another, which is sometimes useful when dealing with different encoding environments.
The design is such that one can use the factory functions returned by the [`lookup()`](https://docs.python.org/3/library/codecs.html#codecs.lookup "codecs.lookup") function to construct the instance.

_class_ codecs.StreamRecoder(_stream_ , _encode_ , _decode_ , _Reader_ , _Writer_ , _errors ='strict'_)[¶](https://docs.python.org/3/library/codecs.html#codecs.StreamRecoder "Link to this definition")

Creates a `StreamRecoder` instance which implements a two-way conversion: _encode_ and _decode_ work on the frontend — the data visible to code calling [`read()`](https://docs.python.org/3/library/codecs.html#codecs.StreamReader.read "codecs.StreamReader.read") and [`write()`](https://docs.python.org/3/library/codecs.html#codecs.StreamWriter.write "codecs.StreamWriter.write"), while _Reader_ and _Writer_ work on the backend — the data in _stream_.
You can use these objects to do transparent transcodings, e.g., from Latin-1 to UTF-8 and back.
The _stream_ argument must be a file-like object.
The _encode_ and _decode_ arguments must adhere to the [`Codec`](https://docs.python.org/3/library/codecs.html#codecs.Codec "codecs.Codec") interface. _Reader_ and _Writer_ must be factory functions or classes providing objects of the [`StreamReader`](https://docs.python.org/3/library/codecs.html#codecs.StreamReader "codecs.StreamReader") and [`StreamWriter`](https://docs.python.org/3/library/codecs.html#codecs.StreamWriter "codecs.StreamWriter") interface respectively.
Error handling is done in the same way as defined for the stream readers and writers.
[`StreamRecoder`](https://docs.python.org/3/library/codecs.html#codecs.StreamRecoder "codecs.StreamRecoder") instances define the combined interfaces of [`StreamReader`](https://docs.python.org/3/library/codecs.html#codecs.StreamReader "codecs.StreamReader") and [`StreamWriter`](https://docs.python.org/3/library/codecs.html#codecs.StreamWriter "codecs.StreamWriter") classes. They inherit all other methods and attributes from the underlying stream.
