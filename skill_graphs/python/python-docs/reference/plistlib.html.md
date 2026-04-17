[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`plistlib` — Generate and parse Apple `.plist` files](https://docs.python.org/3/library/plistlib.html)
    * [Examples](https://docs.python.org/3/library/plistlib.html#examples)


#### Previous topic
[`netrc` — netrc file processing](https://docs.python.org/3/library/netrc.html "previous chapter")
#### Next topic
[Cryptographic Services](https://docs.python.org/3/library/crypto.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=plistlib+%E2%80%94+Generate+and+parse+Apple+.plist+files&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fplistlib.html&pagesource=library%2Fplistlib.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/crypto.html "Cryptographic Services") |
  * [previous](https://docs.python.org/3/library/netrc.html "netrc — netrc file processing") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [File Formats](https://docs.python.org/3/library/fileformats.html) »
  * [`plistlib` — Generate and parse Apple `.plist` files](https://docs.python.org/3/library/plistlib.html)
  * |
  * Theme  Auto Light Dark |


#  `plistlib` — Generate and parse Apple `.plist` files[¶](https://docs.python.org/3/library/plistlib.html#module-plistlib "Link to this heading")
**Source code:**
* * *
This module provides an interface for reading and writing the “property list” files used by Apple, primarily on macOS and iOS. This module supports both binary and XML plist files.
The property list (`.plist`) file format is a simple serialization supporting basic object types, like dictionaries, lists, numbers and strings. Usually the top level object is a dictionary.
To write out and to parse a plist file, use the [`dump()`](https://docs.python.org/3/library/plistlib.html#plistlib.dump "plistlib.dump") and [`load()`](https://docs.python.org/3/library/plistlib.html#plistlib.load "plistlib.load") functions.
To work with plist data in bytes or string objects, use [`dumps()`](https://docs.python.org/3/library/plistlib.html#plistlib.dumps "plistlib.dumps") and [`loads()`](https://docs.python.org/3/library/plistlib.html#plistlib.loads "plistlib.loads").
Values can be strings, integers, floats, booleans, tuples, lists, dictionaries (but only with string keys), [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes"), [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray "bytearray") or [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") objects.
Changed in version 3.4: New API, old API deprecated. Support for binary format plists added.
Changed in version 3.8: Support added for reading and writing [`UID`](https://docs.python.org/3/library/plistlib.html#plistlib.UID "plistlib.UID") tokens in binary plists as used by NSKeyedArchiver and NSKeyedUnarchiver.
Changed in version 3.9: Old API removed.
See also
Apple’s documentation of the file format.
This module defines the following functions:

plistlib.load(_fp_ , _*_ , _fmt =None_, _dict_type =dict_, _aware_datetime =False_)[¶](https://docs.python.org/3/library/plistlib.html#plistlib.load "Link to this definition")

Read a plist file. _fp_ should be a readable and binary file object. Return the unpacked root object (which usually is a dictionary).
The _fmt_ is the format of the file and the following values are valid:
  * [`None`](https://docs.python.org/3/library/constants.html#None "None"): Autodetect the file format
  * [`FMT_XML`](https://docs.python.org/3/library/plistlib.html#plistlib.FMT_XML "plistlib.FMT_XML"): XML file format
  * [`FMT_BINARY`](https://docs.python.org/3/library/plistlib.html#plistlib.FMT_BINARY "plistlib.FMT_BINARY"): Binary plist format


The _dict_type_ is the type used for dictionaries that are read from the plist file.
When _aware_datetime_ is true, fields with type `datetime.datetime` will be created as [aware object](https://docs.python.org/3/library/datetime.html#datetime-naive-aware), with `tzinfo` as [`datetime.UTC`](https://docs.python.org/3/library/datetime.html#datetime.UTC "datetime.UTC").
XML data for the [`FMT_XML`](https://docs.python.org/3/library/plistlib.html#plistlib.FMT_XML "plistlib.FMT_XML") format is parsed using the Expat parser from [`xml.parsers.expat`](https://docs.python.org/3/library/pyexpat.html#module-xml.parsers.expat "xml.parsers.expat: An interface to the Expat non-validating XML parser.") – see its documentation for possible exceptions on ill-formed XML. Unknown elements will simply be ignored by the plist parser.
The parser raises [`InvalidFileException`](https://docs.python.org/3/library/plistlib.html#plistlib.InvalidFileException "plistlib.InvalidFileException") when the file cannot be parsed.
Added in version 3.4.
Changed in version 3.13: The keyword-only parameter _aware_datetime_ has been added.

plistlib.loads(_data_ , _*_ , _fmt =None_, _dict_type =dict_, _aware_datetime =False_)[¶](https://docs.python.org/3/library/plistlib.html#plistlib.loads "Link to this definition")

Load a plist from a bytes or string object. See [`load()`](https://docs.python.org/3/library/plistlib.html#plistlib.load "plistlib.load") for an explanation of the keyword arguments.
Added in version 3.4.
Changed in version 3.13: _data_ can be a string when _fmt_ equals [`FMT_XML`](https://docs.python.org/3/library/plistlib.html#plistlib.FMT_XML "plistlib.FMT_XML").

plistlib.dump(_value_ , _fp_ , _*_ , _fmt =FMT_XML_, _sort_keys =True_, _skipkeys =False_, _aware_datetime =False_)[¶](https://docs.python.org/3/library/plistlib.html#plistlib.dump "Link to this definition")

Write _value_ to a plist file. _fp_ should be a writable, binary file object.
The _fmt_ argument specifies the format of the plist file and can be one of the following values:
  * [`FMT_XML`](https://docs.python.org/3/library/plistlib.html#plistlib.FMT_XML "plistlib.FMT_XML"): XML formatted plist file
  * [`FMT_BINARY`](https://docs.python.org/3/library/plistlib.html#plistlib.FMT_BINARY "plistlib.FMT_BINARY"): Binary formatted plist file


When _sort_keys_ is true (the default) the keys for dictionaries will be written to the plist in sorted order, otherwise they will be written in the iteration order of the dictionary.
When _skipkeys_ is false (the default) the function raises [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") when a key of a dictionary is not a string, otherwise such keys are skipped.
When _aware_datetime_ is true and any field with type `datetime.datetime` is set as an [aware object](https://docs.python.org/3/library/datetime.html#datetime-naive-aware), it will convert to UTC timezone before writing it.
A [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") will be raised if the object is of an unsupported type or a container that contains objects of unsupported types.
An [`OverflowError`](https://docs.python.org/3/library/exceptions.html#OverflowError "OverflowError") will be raised for integer values that cannot be represented in (binary) plist files.
Added in version 3.4.
Changed in version 3.13: The keyword-only parameter _aware_datetime_ has been added.

plistlib.dumps(_value_ , _*_ , _fmt =FMT_XML_, _sort_keys =True_, _skipkeys =False_, _aware_datetime =False_)[¶](https://docs.python.org/3/library/plistlib.html#plistlib.dumps "Link to this definition")

Return _value_ as a plist-formatted bytes object. See the documentation for [`dump()`](https://docs.python.org/3/library/plistlib.html#plistlib.dump "plistlib.dump") for an explanation of the keyword arguments of this function.
Added in version 3.4.
The following classes are available:

_class_ plistlib.UID(_data_)[¶](https://docs.python.org/3/library/plistlib.html#plistlib.UID "Link to this definition")

Wraps an [`int`](https://docs.python.org/3/library/functions.html#int "int"). This is used when reading or writing NSKeyedArchiver encoded data, which contains UID (see PList manual).

data[¶](https://docs.python.org/3/library/plistlib.html#plistlib.UID.data "Link to this definition")

Int value of the UID. It must be in the range `0 <= data < 2**64`.
Added in version 3.8.
The following constants are available:

plistlib.FMT_XML[¶](https://docs.python.org/3/library/plistlib.html#plistlib.FMT_XML "Link to this definition")

The XML format for plist files.
Added in version 3.4.

plistlib.FMT_BINARY[¶](https://docs.python.org/3/library/plistlib.html#plistlib.FMT_BINARY "Link to this definition")

The binary format for plist files
Added in version 3.4.
The module defines the following exceptions:

_exception_ plistlib.InvalidFileException[¶](https://docs.python.org/3/library/plistlib.html#plistlib.InvalidFileException "Link to this definition")

Raised when a file cannot be parsed.
Added in version 3.4.
## Examples[¶](https://docs.python.org/3/library/plistlib.html#examples "Link to this heading")
Generating a plist:
Copy```
import datetime
import plistlib

pl = dict(
    aString = "Doodah",
    aList = ["A", "B", 12, 32.1, [1, 2, 3]],
    aFloat = 0.1,
    anInt = 728,
    aDict = dict(
        anotherString = "<hello & hi there!>",
        aThirdString = "M\xe4ssig, Ma\xdf",
        aTrueValue = True,
        aFalseValue = False,
    ),
    someData = b"<binary gunk>",
    someMoreData = b"<lots of binary gunk>" * 10,
    aDate = datetime.datetime.now()
)
print(plistlib.dumps(pl).decode())

```

Parsing a plist:
Copy```
import plistlib

plist = b"""<plist version="1.0">
<dict>
    <key>foo</key>
    <string>bar</string>
</dict>
</plist>"""
pl = plistlib.loads(plist)
print(pl["foo"])

```

### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`plistlib` — Generate and parse Apple `.plist` files](https://docs.python.org/3/library/plistlib.html)
    * [Examples](https://docs.python.org/3/library/plistlib.html#examples)


#### Previous topic
[`netrc` — netrc file processing](https://docs.python.org/3/library/netrc.html "previous chapter")
#### Next topic
[Cryptographic Services](https://docs.python.org/3/library/crypto.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=plistlib+%E2%80%94+Generate+and+parse+Apple+.plist+files&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fplistlib.html&pagesource=library%2Fplistlib.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/crypto.html "Cryptographic Services") |
  * [previous](https://docs.python.org/3/library/netrc.html "netrc — netrc file processing") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [File Formats](https://docs.python.org/3/library/fileformats.html) »
  * [`plistlib` — Generate and parse Apple `.plist` files](https://docs.python.org/3/library/plistlib.html)
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
