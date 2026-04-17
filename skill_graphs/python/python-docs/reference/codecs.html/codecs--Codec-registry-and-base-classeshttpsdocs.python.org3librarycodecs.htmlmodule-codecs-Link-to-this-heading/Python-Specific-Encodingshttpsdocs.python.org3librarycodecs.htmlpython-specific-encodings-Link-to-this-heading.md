## Python Specific Encodings[¶](https://docs.python.org/3/library/codecs.html#python-specific-encodings "Link to this heading")
A number of predefined codecs are specific to Python, so their codec names have no meaning outside Python. These are listed in the tables below based on the expected input and output types (note that while text encodings are the most common use case for codecs, the underlying codec infrastructure supports arbitrary data transforms rather than just text encodings). For asymmetric codecs, the stated meaning describes the encoding direction.
### Text Encodings[¶](https://docs.python.org/3/library/codecs.html#text-encodings "Link to this heading")
The following codecs provide [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") to [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") encoding and [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) to `str` decoding, similar to the Unicode text encodings.
Codec | Aliases | Meaning
---|---|---
idna |  | Implement [`encodings.idna`](https://docs.python.org/3/library/codecs.html#module-encodings.idna "encodings.idna: Internationalized Domain Names implementation"). Only `errors='strict'` is supported.
mbcs | ansi, dbcs | Windows only: Encode the operand according to the ANSI codepage (CP_ACP).
oem |  |  Windows only: Encode the operand according to the OEM codepage (CP_OEMCP). Added in version 3.6.
palmos |  | Encoding of PalmOS 3.5.
punycode |  | Implement
raw_unicode_escape |  | Latin-1 encoding with `\u_XXXX_`and`\U _XXXXXXXX_`for other code points. Existing backslashes are not escaped in any way. It is used in the Python pickle protocol.
undefined |  |  This Codec should only be used for testing purposes. Raise an exception for all conversions, even empty strings. The error handler is ignored.
unicode_escape |  | Encoding suitable as the contents of a Unicode literal in ASCII-encoded Python source code, except that quotes are not escaped. Decode from Latin-1 source code. Beware that Python source code actually uses UTF-8 by default.
Changed in version 3.8: “unicode_internal” codec is removed.
### Binary Transforms[¶](https://docs.python.org/3/library/codecs.html#binary-transforms "Link to this heading")
The following codecs provide binary transforms: [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) to [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") mappings. They are not supported by [`bytes.decode()`](https://docs.python.org/3/library/stdtypes.html#bytes.decode "bytes.decode") (which only produces [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") output).
Codec | Aliases | Meaning | Encoder / decoder
---|---|---|---
base64_codec [[1]](https://docs.python.org/3/library/codecs.html#b64) | base64, base_64 |  Convert the operand to multiline MIME base64 (the result always includes a trailing `'\n'`). Changed in version 3.4: accepts any [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) as input for encoding and decoding | [`base64.encodebytes()`](https://docs.python.org/3/library/base64.html#base64.encodebytes "base64.encodebytes") / [`base64.decodebytes()`](https://docs.python.org/3/library/base64.html#base64.decodebytes "base64.decodebytes")
bz2_codec | bz2 | Compress the operand using bz2. | [`bz2.compress()`](https://docs.python.org/3/library/bz2.html#bz2.compress "bz2.compress") / [`bz2.decompress()`](https://docs.python.org/3/library/bz2.html#bz2.decompress "bz2.decompress")
hex_codec | hex | Convert the operand to hexadecimal representation, with two digits per byte. | [`binascii.b2a_hex()`](https://docs.python.org/3/library/binascii.html#binascii.b2a_hex "binascii.b2a_hex") / [`binascii.a2b_hex()`](https://docs.python.org/3/library/binascii.html#binascii.a2b_hex "binascii.a2b_hex")
quopri_codec | quopri, quotedprintable, quoted_printable | Convert the operand to MIME quoted printable. | [`quopri.encode()`](https://docs.python.org/3/library/quopri.html#quopri.encode "quopri.encode") with `quotetabs=True` / [`quopri.decode()`](https://docs.python.org/3/library/quopri.html#quopri.decode "quopri.decode")
uu_codec | uu | Convert the operand using uuencode. |
zlib_codec | zip, zlib | Compress the operand using gzip. | [`zlib.compress()`](https://docs.python.org/3/library/zlib.html#zlib.compress "zlib.compress") / [`zlib.decompress()`](https://docs.python.org/3/library/zlib.html#zlib.decompress "zlib.decompress")
[[1](https://docs.python.org/3/library/codecs.html#id5)]
In addition to [bytes-like objects](https://docs.python.org/3/glossary.html#term-bytes-like-object), `'base64_codec'` also accepts ASCII-only instances of [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") for decoding
Added in version 3.2: Restoration of the binary transforms.
Changed in version 3.4: Restoration of the aliases for the binary transforms.
### Standalone Codec Functions[¶](https://docs.python.org/3/library/codecs.html#standalone-codec-functions "Link to this heading")
The following functions provide encoding and decoding functionality similar to codecs, but are not available as named codecs through [`codecs.encode()`](https://docs.python.org/3/library/codecs.html#codecs.encode "codecs.encode") or [`codecs.decode()`](https://docs.python.org/3/library/codecs.html#codecs.decode "codecs.decode"). They are used internally (for example, by [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.")) and behave similarly to the `string_escape` codec that was removed in Python 3.

codecs.escape_encode(_input_ , _errors =None_)[¶](https://docs.python.org/3/library/codecs.html#codecs.codecs.escape_encode "Link to this definition")

Encode _input_ using escape sequences. Similar to how [`repr()`](https://docs.python.org/3/library/functions.html#repr "repr") on bytes produces escaped byte values.
_input_ must be a [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") object.
Returns a tuple `(output, length)` where _output_ is a [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") object and _length_ is the number of bytes consumed.

codecs.escape_decode(_input_ , _errors =None_)[¶](https://docs.python.org/3/library/codecs.html#codecs.codecs.escape_decode "Link to this definition")

Decode _input_ from escape sequences back to the original bytes.
_input_ must be a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object).
Returns a tuple `(output, length)` where _output_ is a [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") object and _length_ is the number of bytes consumed.
### Text Transforms[¶](https://docs.python.org/3/library/codecs.html#text-transforms "Link to this heading")
The following codec provides a text transform: a [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") to `str` mapping. It is not supported by [`str.encode()`](https://docs.python.org/3/library/stdtypes.html#str.encode "str.encode") (which only produces [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") output).
Codec | Aliases | Meaning
---|---|---
rot_13 | rot13 | Return the Caesar-cypher encryption of the operand.
Added in version 3.2: Restoration of the `rot_13` text transform.
Changed in version 3.4: Restoration of the `rot13` alias.
