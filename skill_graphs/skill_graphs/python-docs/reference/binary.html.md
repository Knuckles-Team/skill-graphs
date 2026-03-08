[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`rlcompleter` — Completion function for GNU readline](https://docs.python.org/3/library/rlcompleter.html "previous chapter")
#### Next topic
[`struct` — Interpret bytes as packed binary data](https://docs.python.org/3/library/struct.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Binary+Data+Services&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fbinary.html&pagesource=library%2Fbinary.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/struct.html "struct — Interpret bytes as packed binary data") |
  * [previous](https://docs.python.org/3/library/rlcompleter.html "rlcompleter — Completion function for GNU readline") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Binary Data Services](https://docs.python.org/3/library/binary.html)
  * |
  * Theme  Auto Light Dark |


# Binary Data Services[¶](https://docs.python.org/3/library/binary.html#binary-data-services "Link to this heading")
The modules described in this chapter provide some basic services operations for manipulation of binary data. Other operations on binary data, specifically in relation to file formats and network protocols, are described in the relevant sections.
Some libraries described under [Text Processing Services](https://docs.python.org/3/library/text.html#textservices) also work with either ASCII-compatible binary formats (for example, [`re`](https://docs.python.org/3/library/re.html#module-re "re: Regular expression operations.")) or all binary data (for example, [`difflib`](https://docs.python.org/3/library/difflib.html#module-difflib "difflib: Helpers for computing differences between objects.")).
In addition, see the documentation for Python’s built-in binary data types in [Binary Sequence Types — bytes, bytearray, memoryview](https://docs.python.org/3/library/stdtypes.html#binaryseq).
  * [`struct` — Interpret bytes as packed binary data](https://docs.python.org/3/library/struct.html)
    * [Functions and Exceptions](https://docs.python.org/3/library/struct.html#functions-and-exceptions)
    * [Format Strings](https://docs.python.org/3/library/struct.html#format-strings)
      * [Byte Order, Size, and Alignment](https://docs.python.org/3/library/struct.html#byte-order-size-and-alignment)
      * [Format Characters](https://docs.python.org/3/library/struct.html#format-characters)
      * [Examples](https://docs.python.org/3/library/struct.html#examples)
    * [Applications](https://docs.python.org/3/library/struct.html#applications)
      * [Native Formats](https://docs.python.org/3/library/struct.html#native-formats)
      * [Standard Formats](https://docs.python.org/3/library/struct.html#standard-formats)
    * [Classes](https://docs.python.org/3/library/struct.html#classes)
  * [`codecs` — Codec registry and base classes](https://docs.python.org/3/library/codecs.html)
    * [Codec Base Classes](https://docs.python.org/3/library/codecs.html#codec-base-classes)
      * [Error Handlers](https://docs.python.org/3/library/codecs.html#error-handlers)
      * [Stateless Encoding and Decoding](https://docs.python.org/3/library/codecs.html#stateless-encoding-and-decoding)
      * [Incremental Encoding and Decoding](https://docs.python.org/3/library/codecs.html#incremental-encoding-and-decoding)
        * [IncrementalEncoder Objects](https://docs.python.org/3/library/codecs.html#incrementalencoder-objects)
        * [IncrementalDecoder Objects](https://docs.python.org/3/library/codecs.html#incrementaldecoder-objects)
      * [Stream Encoding and Decoding](https://docs.python.org/3/library/codecs.html#stream-encoding-and-decoding)
        * [StreamWriter Objects](https://docs.python.org/3/library/codecs.html#streamwriter-objects)
        * [StreamReader Objects](https://docs.python.org/3/library/codecs.html#streamreader-objects)
        * [StreamReaderWriter Objects](https://docs.python.org/3/library/codecs.html#streamreaderwriter-objects)
        * [StreamRecoder Objects](https://docs.python.org/3/library/codecs.html#streamrecoder-objects)
    * [Encodings and Unicode](https://docs.python.org/3/library/codecs.html#encodings-and-unicode)
    * [Standard Encodings](https://docs.python.org/3/library/codecs.html#standard-encodings)
    * [Python Specific Encodings](https://docs.python.org/3/library/codecs.html#python-specific-encodings)
      * [Text Encodings](https://docs.python.org/3/library/codecs.html#text-encodings)
      * [Binary Transforms](https://docs.python.org/3/library/codecs.html#binary-transforms)
      * [Standalone Codec Functions](https://docs.python.org/3/library/codecs.html#standalone-codec-functions)
      * [Text Transforms](https://docs.python.org/3/library/codecs.html#text-transforms)
    * [`encodings` — Encodings package](https://docs.python.org/3/library/codecs.html#module-encodings)
    * [`encodings.idna` — Internationalized Domain Names in Applications](https://docs.python.org/3/library/codecs.html#module-encodings.idna)
    * [`encodings.mbcs` — Windows ANSI codepage](https://docs.python.org/3/library/codecs.html#module-encodings.mbcs)
    * [`encodings.utf_8_sig` — UTF-8 codec with BOM signature](https://docs.python.org/3/library/codecs.html#module-encodings.utf_8_sig)


#### Previous topic
[`rlcompleter` — Completion function for GNU readline](https://docs.python.org/3/library/rlcompleter.html "previous chapter")
#### Next topic
[`struct` — Interpret bytes as packed binary data](https://docs.python.org/3/library/struct.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Binary+Data+Services&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fbinary.html&pagesource=library%2Fbinary.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/struct.html "struct — Interpret bytes as packed binary data") |
  * [previous](https://docs.python.org/3/library/rlcompleter.html "rlcompleter — Completion function for GNU readline") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Binary Data Services](https://docs.python.org/3/library/binary.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
