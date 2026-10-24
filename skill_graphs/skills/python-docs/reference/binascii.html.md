[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`base64` — Base16, Base32, Base64, Base85 Data Encodings](https://docs.python.org/3/library/base64.html "previous chapter")
#### Next topic
[`quopri` — Encode and decode MIME quoted-printable data](https://docs.python.org/3/library/quopri.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=binascii+%E2%80%94+Convert+between+binary+and+ASCII&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fbinascii.html&pagesource=library%2Fbinascii.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/quopri.html "quopri — Encode and decode MIME quoted-printable data") |
  * [previous](https://docs.python.org/3/library/base64.html "base64 — Base16, Base32, Base64, Base85 Data Encodings") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Internet Data Handling](https://docs.python.org/3/library/netdata.html) »
  * [`binascii` — Convert between binary and ASCII](https://docs.python.org/3/library/binascii.html)
  * |
  * Theme  Auto Light Dark |


#  `binascii` — Convert between binary and ASCII[¶](https://docs.python.org/3/library/binascii.html#module-binascii "Link to this heading")
* * *
The `binascii` module contains a number of methods to convert between binary and various ASCII-encoded binary representations. Normally, you will not use these functions directly but use wrapper modules like [`base64`](https://docs.python.org/3/library/base64.html#module-base64 "base64: RFC 4648: Base16, Base32, Base64 Data Encodings; Base85 and Ascii85") instead. The `binascii` module contains low-level functions written in C for greater speed that are used by the higher-level modules.
Note
`a2b_*` functions accept Unicode strings containing only ASCII characters. Other functions only accept [bytes-like objects](https://docs.python.org/3/glossary.html#term-bytes-like-object) (such as [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes"), [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray "bytearray") and other objects that support the buffer protocol).
Changed in version 3.3: ASCII-only unicode strings are now accepted by the `a2b_*` functions.
The `binascii` module defines the following functions:

binascii.a2b_uu(_string_)[¶](https://docs.python.org/3/library/binascii.html#binascii.a2b_uu "Link to this definition")

Convert a single line of uuencoded data back to binary and return the binary data. Lines normally contain 45 (binary) bytes, except for the last line. Line data may be followed by whitespace.

binascii.b2a_uu(_data_ , _*_ , _backtick =False_)[¶](https://docs.python.org/3/library/binascii.html#binascii.b2a_uu "Link to this definition")

Convert binary data to a line of ASCII characters, the return value is the converted line, including a newline char. The length of _data_ should be at most 45. If _backtick_ is true, zeros are represented by `'`'` instead of spaces.
Changed in version 3.7: Added the _backtick_ parameter.

binascii.a2b_base64(_string_ , _/_ , _*_ , _strict_mode =False_)[¶](https://docs.python.org/3/library/binascii.html#binascii.a2b_base64 "Link to this definition")

Convert a block of base64 data back to binary and return the binary data. More than one line may be passed at a time.
If _strict_mode_ is true, only valid base64 data will be converted. Invalid base64 data will raise [`binascii.Error`](https://docs.python.org/3/library/binascii.html#binascii.Error "binascii.Error").
Valid base64:
  * Conforms to
  * Contains only characters from the base64 alphabet.
  * Contains no excess data after padding (including excess padding, newlines, etc.).
  * Does not start with a padding.


Changed in version 3.11: Added the _strict_mode_ parameter.

binascii.b2a_base64(_data_ , _*_ , _newline =True_)[¶](https://docs.python.org/3/library/binascii.html#binascii.b2a_base64 "Link to this definition")

Convert binary data to a line of ASCII characters in base64 coding. The return value is the converted line, including a newline char if _newline_ is true. The output of this function conforms to
Changed in version 3.6: Added the _newline_ parameter.

binascii.a2b_qp(_data_ , _header =False_)[¶](https://docs.python.org/3/library/binascii.html#binascii.a2b_qp "Link to this definition")

Convert a block of quoted-printable data back to binary and return the binary data. More than one line may be passed at a time. If the optional argument _header_ is present and true, underscores will be decoded as spaces.

binascii.b2a_qp(_data_ , _quotetabs =False_, _istext =True_, _header =False_)[¶](https://docs.python.org/3/library/binascii.html#binascii.b2a_qp "Link to this definition")

Convert binary data to a line(s) of ASCII characters in quoted-printable encoding. The return value is the converted line(s). If the optional argument _quotetabs_ is present and true, all tabs and spaces will be encoded. If the optional argument _istext_ is present and true, newlines are not encoded but trailing whitespace will be encoded. If the optional argument _header_ is present and true, spaces will be encoded as underscores per _header_ is present and false, newline characters will be encoded as well; otherwise linefeed conversion might corrupt the binary data stream.

binascii.crc_hqx(_data_ , _value_)[¶](https://docs.python.org/3/library/binascii.html#binascii.crc_hqx "Link to this definition")

Compute a 16-bit CRC value of _data_ , starting with _value_ as the initial CRC, and return the result. This uses the CRC-CCITT polynomial _x_ 16 + _x_ 12 + _x_ 5 + 1, often represented as 0x1021. This CRC is used in the binhex4 format.

binascii.crc32(_data_[, _value_])[¶](https://docs.python.org/3/library/binascii.html#binascii.crc32 "Link to this definition")

Compute CRC-32, the unsigned 32-bit checksum of _data_ , starting with an initial CRC of _value_. The default initial CRC is zero. The algorithm is consistent with the ZIP file checksum. Since the algorithm is designed for use as a checksum algorithm, it is not suitable for use as a general hash algorithm. Use as follows:
Copy```
print(binascii.crc32(b"hello world"))
# Or, in two pieces:
crc = binascii.crc32(b"hello")
crc = binascii.crc32(b" world", crc)
print('crc32 = {:#010x}'.format(crc))

```

Changed in version 3.0: The result is always unsigned.

binascii.b2a_hex(_data_[, _sep_[, _bytes_per_sep=1_]])[¶](https://docs.python.org/3/library/binascii.html#binascii.b2a_hex "Link to this definition")


binascii.hexlify(_data_[, _sep_[, _bytes_per_sep=1_]])[¶](https://docs.python.org/3/library/binascii.html#binascii.hexlify "Link to this definition")

Return the hexadecimal representation of the binary _data_. Every byte of _data_ is converted into the corresponding 2-digit hex representation. The returned bytes object is therefore twice as long as the length of _data_.
Similar functionality (but returning a text string) is also conveniently accessible using the [`bytes.hex()`](https://docs.python.org/3/library/stdtypes.html#bytes.hex "bytes.hex") method.
If _sep_ is specified, it must be a single character str or bytes object. It will be inserted in the output after every _bytes_per_sep_ input bytes. Separator placement is counted from the right end of the output by default, if you wish to count from the left, supply a negative _bytes_per_sep_ value.
Copy```
>>> import binascii
>>> binascii.b2a_hex(b'\xb9\x01\xef')
b'b901ef'
>>> binascii.hexlify(b'\xb9\x01\xef', '-')
b'b9-01-ef'
>>> binascii.b2a_hex(b'\xb9\x01\xef', b'_', 2)
b'b9_01ef'
>>> binascii.b2a_hex(b'\xb9\x01\xef', b' ', -2)
b'b901 ef'

```

Changed in version 3.8: The _sep_ and _bytes_per_sep_ parameters were added.

binascii.a2b_hex(_hexstr_)[¶](https://docs.python.org/3/library/binascii.html#binascii.a2b_hex "Link to this definition")


binascii.unhexlify(_hexstr_)[¶](https://docs.python.org/3/library/binascii.html#binascii.unhexlify "Link to this definition")

Return the binary data represented by the hexadecimal string _hexstr_. This function is the inverse of [`b2a_hex()`](https://docs.python.org/3/library/binascii.html#binascii.b2a_hex "binascii.b2a_hex"). _hexstr_ must contain an even number of hexadecimal digits (which can be upper or lower case), otherwise an [`Error`](https://docs.python.org/3/library/binascii.html#binascii.Error "binascii.Error") exception is raised.
Similar functionality (accepting only text string arguments, but more liberal towards whitespace) is also accessible using the [`bytes.fromhex()`](https://docs.python.org/3/library/stdtypes.html#bytes.fromhex "bytes.fromhex") class method.

_exception_ binascii.Error[¶](https://docs.python.org/3/library/binascii.html#binascii.Error "Link to this definition")

Exception raised on errors. These are usually programming errors.

_exception_ binascii.Incomplete[¶](https://docs.python.org/3/library/binascii.html#binascii.Incomplete "Link to this definition")

Exception raised on incomplete data. These are usually not programming errors, but may be handled by reading a little more data and trying again.
See also

Module [`base64`](https://docs.python.org/3/library/base64.html#module-base64 "base64: RFC 4648: Base16, Base32, Base64 Data Encodings; Base85 and Ascii85")

Support for RFC compliant base64-style encoding in base 16, 32, 64, and 85.

Module [`quopri`](https://docs.python.org/3/library/quopri.html#module-quopri "quopri: Encode and decode files using the MIME quoted-printable encoding.")

Support for quoted-printable encoding used in MIME email messages.
#### Previous topic
[`base64` — Base16, Base32, Base64, Base85 Data Encodings](https://docs.python.org/3/library/base64.html "previous chapter")
#### Next topic
[`quopri` — Encode and decode MIME quoted-printable data](https://docs.python.org/3/library/quopri.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=binascii+%E2%80%94+Convert+between+binary+and+ASCII&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fbinascii.html&pagesource=library%2Fbinascii.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/quopri.html "quopri — Encode and decode MIME quoted-printable data") |
  * [previous](https://docs.python.org/3/library/base64.html "base64 — Base16, Base32, Base64, Base85 Data Encodings") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Internet Data Handling](https://docs.python.org/3/library/netdata.html) »
  * [`binascii` — Convert between binary and ASCII](https://docs.python.org/3/library/binascii.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
