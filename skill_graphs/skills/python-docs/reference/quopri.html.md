[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`binascii` — Convert between binary and ASCII](https://docs.python.org/3/library/binascii.html "previous chapter")
#### Next topic
[Structured Markup Processing Tools](https://docs.python.org/3/library/markup.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=quopri+%E2%80%94+Encode+and+decode+MIME+quoted-printable+data&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fquopri.html&pagesource=library%2Fquopri.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/markup.html "Structured Markup Processing Tools") |
  * [previous](https://docs.python.org/3/library/binascii.html "binascii — Convert between binary and ASCII") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Internet Data Handling](https://docs.python.org/3/library/netdata.html) »
  * [`quopri` — Encode and decode MIME quoted-printable data](https://docs.python.org/3/library/quopri.html)
  * |
  * Theme  Auto Light Dark |


#  `quopri` — Encode and decode MIME quoted-printable data[¶](https://docs.python.org/3/library/quopri.html#module-quopri "Link to this heading")
**Source code:**
* * *
This module performs quoted-printable transport encoding and decoding, as defined in [`base64`](https://docs.python.org/3/library/base64.html#module-base64 "base64: RFC 4648: Base16, Base32, Base64 Data Encodings; Base85 and Ascii85") module is more compact if there are many such characters, as when sending a graphics file.

quopri.decode(_input_ , _output_ , _header =False_)[¶](https://docs.python.org/3/library/quopri.html#quopri.decode "Link to this definition")

Decode the contents of the _input_ file and write the resulting decoded binary data to the _output_ file. _input_ and _output_ must be [binary file objects](https://docs.python.org/3/glossary.html#term-file-object). If the optional argument _header_ is present and true, underscore will be decoded as space. This is used to decode “Q”-encoded headers as described in

quopri.encode(_input_ , _output_ , _quotetabs_ , _header =False_)[¶](https://docs.python.org/3/library/quopri.html#quopri.encode "Link to this definition")

Encode the contents of the _input_ file and write the resulting quoted-printable data to the _output_ file. _input_ and _output_ must be [binary file objects](https://docs.python.org/3/glossary.html#term-file-object). _quotetabs_ , a non-optional flag which controls whether to encode embedded spaces and tabs; when true it encodes such embedded whitespace, and when false it leaves them unencoded. Note that spaces and tabs appearing at the end of lines are always encoded, as per _header_ is a flag which controls if spaces are encoded as underscores as per

quopri.decodestring(_s_ , _header =False_)[¶](https://docs.python.org/3/library/quopri.html#quopri.decodestring "Link to this definition")

Like [`decode()`](https://docs.python.org/3/library/quopri.html#quopri.decode "quopri.decode"), except that it accepts a source [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") and returns the corresponding decoded `bytes`.

quopri.encodestring(_s_ , _quotetabs =False_, _header =False_)[¶](https://docs.python.org/3/library/quopri.html#quopri.encodestring "Link to this definition")

Like [`encode()`](https://docs.python.org/3/library/quopri.html#quopri.encode "quopri.encode"), except that it accepts a source [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") and returns the corresponding encoded `bytes`. By default, it sends a `False` value to _quotetabs_ parameter of the `encode()` function.
See also

Module [`base64`](https://docs.python.org/3/library/base64.html#module-base64 "base64: RFC 4648: Base16, Base32, Base64 Data Encodings; Base85 and Ascii85")

Encode and decode MIME base64 data
#### Previous topic
[`binascii` — Convert between binary and ASCII](https://docs.python.org/3/library/binascii.html "previous chapter")
#### Next topic
[Structured Markup Processing Tools](https://docs.python.org/3/library/markup.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=quopri+%E2%80%94+Encode+and+decode+MIME+quoted-printable+data&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fquopri.html&pagesource=library%2Fquopri.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/markup.html "Structured Markup Processing Tools") |
  * [previous](https://docs.python.org/3/library/binascii.html "binascii — Convert between binary and ASCII") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Internet Data Handling](https://docs.python.org/3/library/netdata.html) »
  * [`quopri` — Encode and decode MIME quoted-printable data](https://docs.python.org/3/library/quopri.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
