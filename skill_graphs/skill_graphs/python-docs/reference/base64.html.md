[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`base64` — Base16, Base32, Base64, Base85 Data Encodings](https://docs.python.org/3/library/base64.html)
    * [RFC 4648 Encodings](https://docs.python.org/3/library/base64.html#rfc-4648-encodings)
    * [Base85 Encodings](https://docs.python.org/3/library/base64.html#base85-encodings)
    * [Legacy Interface](https://docs.python.org/3/library/base64.html#legacy-interface)
    * [Security Considerations](https://docs.python.org/3/library/base64.html#security-considerations)


#### Previous topic
[`mimetypes` — Map filenames to MIME types](https://docs.python.org/3/library/mimetypes.html "previous chapter")
#### Next topic
[`binascii` — Convert between binary and ASCII](https://docs.python.org/3/library/binascii.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=base64+%E2%80%94+Base16%2C+Base32%2C+Base64%2C+Base85+Data+Encodings&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fbase64.html&pagesource=library%2Fbase64.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/binascii.html "binascii — Convert between binary and ASCII") |
  * [previous](https://docs.python.org/3/library/mimetypes.html "mimetypes — Map filenames to MIME types") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Internet Data Handling](https://docs.python.org/3/library/netdata.html) »
  * [`base64` — Base16, Base32, Base64, Base85 Data Encodings](https://docs.python.org/3/library/base64.html)
  * |
  * Theme  Auto Light Dark |


#  `base64` — Base16, Base32, Base64, Base85 Data Encodings[¶](https://docs.python.org/3/library/base64.html#module-base64 "Link to this heading")
**Source code:**
* * *
This module provides functions for encoding binary data to printable ASCII characters and decoding such encodings back to binary data. This includes the [encodings specified in](https://docs.python.org/3/library/base64.html#base64-rfc-4648) [Base85 encodings](https://docs.python.org/3/library/base64.html#base64-base-85).
There are two interfaces provided by this module. The modern interface supports encoding [bytes-like objects](https://docs.python.org/3/glossary.html#term-bytes-like-object) to ASCII [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes"), and decoding bytes-like objects or strings containing ASCII to `bytes`. Both base-64 alphabets defined in
The [legacy interface](https://docs.python.org/3/library/base64.html#base64-legacy) does not support decoding from strings, but it does provide functions for encoding and decoding to and from [file objects](https://docs.python.org/3/glossary.html#term-file-object). It only supports the Base64 standard alphabet, and it adds newlines every 76 characters as per [`email`](https://docs.python.org/3/library/email.html#module-email "email: Package supporting the parsing, manipulating, and generating email messages.") package instead.
Changed in version 3.3: ASCII-only Unicode strings are now accepted by the decoding functions of the modern interface.
Changed in version 3.4: Any [bytes-like objects](https://docs.python.org/3/glossary.html#term-bytes-like-object) are now accepted by all encoding and decoding functions in this module. Ascii85/Base85 support added.
## RFC 4648 Encodings[¶](https://docs.python.org/3/library/base64.html#rfc-4648-encodings "Link to this heading")
The

base64.b64encode(_s_ , _altchars =None_)[¶](https://docs.python.org/3/library/base64.html#base64.b64encode "Link to this definition")

Encode the [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) _s_ using Base64 and return the encoded [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes").
Optional _altchars_ must be a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) of length 2 which specifies an alternative alphabet for the `+` and `/` characters. This allows an application to e.g. generate URL or filesystem safe Base64 strings. The default is `None`, for which the standard Base64 alphabet is used.
May assert or raise a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") if the length of _altchars_ is not 2. Raises a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") if _altchars_ is not a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object).

base64.b64decode(_s_ , _altchars =None_, _validate =False_)[¶](https://docs.python.org/3/library/base64.html#base64.b64decode "Link to this definition")

Decode the Base64 encoded [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) or ASCII string _s_ and return the decoded [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes").
Optional _altchars_ must be a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) or ASCII string of length 2 which specifies the alternative alphabet used instead of the `+` and `/` characters.
A [`binascii.Error`](https://docs.python.org/3/library/binascii.html#binascii.Error "binascii.Error") exception is raised if _s_ is incorrectly padded.
If _validate_ is `False` (the default), characters that are neither in the normal base-64 alphabet nor the alternative alphabet are discarded prior to the padding check. If _validate_ is `True`, these non-alphabet characters in the input result in a [`binascii.Error`](https://docs.python.org/3/library/binascii.html#binascii.Error "binascii.Error").
For more information about the strict base64 check, see [`binascii.a2b_base64()`](https://docs.python.org/3/library/binascii.html#binascii.a2b_base64 "binascii.a2b_base64")
May assert or raise a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") if the length of _altchars_ is not 2.

base64.standard_b64encode(_s_)[¶](https://docs.python.org/3/library/base64.html#base64.standard_b64encode "Link to this definition")

Encode [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) _s_ using the standard Base64 alphabet and return the encoded [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes").

base64.standard_b64decode(_s_)[¶](https://docs.python.org/3/library/base64.html#base64.standard_b64decode "Link to this definition")

Decode [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) or ASCII string _s_ using the standard Base64 alphabet and return the decoded [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes").

base64.urlsafe_b64encode(_s_)[¶](https://docs.python.org/3/library/base64.html#base64.urlsafe_b64encode "Link to this definition")

Encode [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) _s_ using the URL- and filesystem-safe alphabet, which substitutes `-` instead of `+` and `_` instead of `/` in the standard Base64 alphabet, and return the encoded [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes"). The result can still contain `=`.

base64.urlsafe_b64decode(_s_)[¶](https://docs.python.org/3/library/base64.html#base64.urlsafe_b64decode "Link to this definition")

Decode [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) or ASCII string _s_ using the URL- and filesystem-safe alphabet, which substitutes `-` instead of `+` and `_` instead of `/` in the standard Base64 alphabet, and return the decoded [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes").

base64.b32encode(_s_)[¶](https://docs.python.org/3/library/base64.html#base64.b32encode "Link to this definition")

Encode the [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) _s_ using Base32 and return the encoded [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes").

base64.b32decode(_s_ , _casefold =False_, _map01 =None_)[¶](https://docs.python.org/3/library/base64.html#base64.b32decode "Link to this definition")

Decode the Base32 encoded [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) or ASCII string _s_ and return the decoded [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes").
Optional _casefold_ is a flag specifying whether a lowercase alphabet is acceptable as input. For security purposes, the default is `False`.
_map01_ when not `None`, specifies which letter the digit 1 should be mapped to (when _map01_ is not `None`, the digit 0 is always mapped to the letter O). For security purposes the default is `None`, so that 0 and 1 are not allowed in the input.
A [`binascii.Error`](https://docs.python.org/3/library/binascii.html#binascii.Error "binascii.Error") is raised if _s_ is incorrectly padded or if there are non-alphabet characters present in the input.

base64.b32hexencode(_s_)[¶](https://docs.python.org/3/library/base64.html#base64.b32hexencode "Link to this definition")

Similar to [`b32encode()`](https://docs.python.org/3/library/base64.html#base64.b32encode "base64.b32encode") but uses the Extended Hex Alphabet, as defined in
Added in version 3.10.

base64.b32hexdecode(_s_ , _casefold =False_)[¶](https://docs.python.org/3/library/base64.html#base64.b32hexdecode "Link to this definition")

Similar to [`b32decode()`](https://docs.python.org/3/library/base64.html#base64.b32decode "base64.b32decode") but uses the Extended Hex Alphabet, as defined in
This version does not allow the digit 0 (zero) to the letter O (oh) and digit 1 (one) to either the letter I (eye) or letter L (el) mappings, all these characters are included in the Extended Hex Alphabet and are not interchangeable.
Added in version 3.10.

base64.b16encode(_s_)[¶](https://docs.python.org/3/library/base64.html#base64.b16encode "Link to this definition")

Encode the [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) _s_ using Base16 and return the encoded [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes").

base64.b16decode(_s_ , _casefold =False_)[¶](https://docs.python.org/3/library/base64.html#base64.b16decode "Link to this definition")

Decode the Base16 encoded [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) or ASCII string _s_ and return the decoded [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes").
Optional _casefold_ is a flag specifying whether a lowercase alphabet is acceptable as input. For security purposes, the default is `False`.
A [`binascii.Error`](https://docs.python.org/3/library/binascii.html#binascii.Error "binascii.Error") is raised if _s_ is incorrectly padded or if there are non-alphabet characters present in the input.
## Base85 Encodings[¶](https://docs.python.org/3/library/base64.html#base85-encodings "Link to this heading")
Base85 encoding is not formally specified but rather a de facto standard, thus different systems perform the encoding differently.
The [`a85encode()`](https://docs.python.org/3/library/base64.html#base64.a85encode "base64.a85encode") and [`b85encode()`](https://docs.python.org/3/library/base64.html#base64.b85encode "base64.b85encode") functions in this module are two implementations of the de facto standard. You should call the function with the Base85 implementation used by the software you intend to work with.
The two functions present in this module differ in how they handle the following:
  * Whether to include enclosing `<~` and `~>` markers
  * Whether to include newline characters
  * The set of ASCII characters used for encoding
  * Handling of null bytes


Refer to the documentation of the individual functions for more information.

base64.a85encode(_b_ , _*_ , _foldspaces =False_, _wrapcol =0_, _pad =False_, _adobe =False_)[¶](https://docs.python.org/3/library/base64.html#base64.a85encode "Link to this definition")

Encode the [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) _b_ using Ascii85 and return the encoded [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes").
_foldspaces_ is an optional flag that uses the special short sequence ‘y’ instead of 4 consecutive spaces (ASCII 0x20) as supported by ‘btoa’. This feature is not supported by the “standard” Ascii85 encoding.
_wrapcol_ controls whether the output should have newline (`b'\n'`) characters added to it. If this is non-zero, each output line will be at most this many characters long, excluding the trailing newline.
_pad_ controls whether the input is padded to a multiple of 4 before encoding. Note that the `btoa` implementation always pads.
_adobe_ controls whether the encoded byte sequence is framed with `<~` and `~>`, which is used by the Adobe implementation.
Added in version 3.4.

base64.a85decode(_b_ , _*_ , _foldspaces =False_, _adobe =False_, _ignorechars =b' \t\n\r\x0b'_)[¶](https://docs.python.org/3/library/base64.html#base64.a85decode "Link to this definition")

Decode the Ascii85 encoded [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) or ASCII string _b_ and return the decoded [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes").
_foldspaces_ is a flag that specifies whether the ‘y’ short sequence should be accepted as shorthand for 4 consecutive spaces (ASCII 0x20). This feature is not supported by the “standard” Ascii85 encoding.
_adobe_ controls whether the input sequence is in Adobe Ascii85 format (i.e. is framed with <~ and ~>).
_ignorechars_ should be a byte string containing characters to ignore from the input. This should only contain whitespace characters, and by default contains all whitespace characters in ASCII.
Added in version 3.4.

base64.b85encode(_b_ , _pad =False_)[¶](https://docs.python.org/3/library/base64.html#base64.b85encode "Link to this definition")

Encode the [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) _b_ using base85 (as used in e.g. git-style binary diffs) and return the encoded [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes").
If _pad_ is true, the input is padded with `b'\0'` so its length is a multiple of 4 bytes before encoding.
Added in version 3.4.

base64.b85decode(_b_)[¶](https://docs.python.org/3/library/base64.html#base64.b85decode "Link to this definition")

Decode the base85-encoded [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) or ASCII string _b_ and return the decoded [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes"). Padding is implicitly removed, if necessary.
Added in version 3.4.

base64.z85encode(_s_)[¶](https://docs.python.org/3/library/base64.html#base64.z85encode "Link to this definition")

Encode the [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) _s_ using Z85 (as used in ZeroMQ) and return the encoded [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes"). See
Added in version 3.13.

base64.z85decode(_s_)[¶](https://docs.python.org/3/library/base64.html#base64.z85decode "Link to this definition")

Decode the Z85-encoded [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) or ASCII string _s_ and return the decoded [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes"). See
Added in version 3.13.
## Legacy Interface[¶](https://docs.python.org/3/library/base64.html#legacy-interface "Link to this heading")

base64.decode(_input_ , _output_)[¶](https://docs.python.org/3/library/base64.html#base64.decode "Link to this definition")

Decode the contents of the binary _input_ file and write the resulting binary data to the _output_ file. _input_ and _output_ must be [file objects](https://docs.python.org/3/glossary.html#term-file-object). _input_ will be read until `input.readline()` returns an empty bytes object.

base64.decodebytes(_s_)[¶](https://docs.python.org/3/library/base64.html#base64.decodebytes "Link to this definition")

Decode the [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) _s_ , which must contain one or more lines of base64 encoded data, and return the decoded [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes").
Added in version 3.1.

base64.encode(_input_ , _output_)[¶](https://docs.python.org/3/library/base64.html#base64.encode "Link to this definition")

Encode the contents of the binary _input_ file and write the resulting base64 encoded data to the _output_ file. _input_ and _output_ must be [file objects](https://docs.python.org/3/glossary.html#term-file-object). _input_ will be read until `input.read()` returns an empty bytes object. `encode()` inserts a newline character (`b'\n'`) after every 76 bytes of the output, as well as ensuring that the output always ends with a newline, as per

base64.encodebytes(_s_)[¶](https://docs.python.org/3/library/base64.html#base64.encodebytes "Link to this definition")

Encode the [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) _s_ , which can contain arbitrary binary data, and return [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") containing the base64-encoded data, with newlines (`b'\n'`) inserted after every 76 bytes of output, and ensuring that there is a trailing newline, as per
Added in version 3.1.
An example usage of the module:
Copy```
>>> import base64
>>> encoded = base64.b64encode(b'data to be encoded')
>>> encoded
b'ZGF0YSB0byBiZSBlbmNvZGVk'
>>> data = base64.b64decode(encoded)
>>> data
b'data to be encoded'

```

## Security Considerations[¶](https://docs.python.org/3/library/base64.html#security-considerations "Link to this heading")
A new security considerations section was added to
See also

Module [`binascii`](https://docs.python.org/3/library/binascii.html#module-binascii "binascii: Tools for converting between binary and various ASCII-encoded binary representations.")

Support module containing ASCII-to-binary and binary-to-ASCII conversions.
Section 5.2, “Base64 Content-Transfer-Encoding,” provides the definition of the base64 encoding.
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`base64` — Base16, Base32, Base64, Base85 Data Encodings](https://docs.python.org/3/library/base64.html)
    * [RFC 4648 Encodings](https://docs.python.org/3/library/base64.html#rfc-4648-encodings)
    * [Base85 Encodings](https://docs.python.org/3/library/base64.html#base85-encodings)
    * [Legacy Interface](https://docs.python.org/3/library/base64.html#legacy-interface)
    * [Security Considerations](https://docs.python.org/3/library/base64.html#security-considerations)


#### Previous topic
[`mimetypes` — Map filenames to MIME types](https://docs.python.org/3/library/mimetypes.html "previous chapter")
#### Next topic
[`binascii` — Convert between binary and ASCII](https://docs.python.org/3/library/binascii.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=base64+%E2%80%94+Base16%2C+Base32%2C+Base64%2C+Base85+Data+Encodings&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fbase64.html&pagesource=library%2Fbase64.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/binascii.html "binascii — Convert between binary and ASCII") |
  * [previous](https://docs.python.org/3/library/mimetypes.html "mimetypes — Map filenames to MIME types") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Internet Data Handling](https://docs.python.org/3/library/netdata.html) »
  * [`base64` — Base16, Base32, Base64, Base85 Data Encodings](https://docs.python.org/3/library/base64.html)
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
