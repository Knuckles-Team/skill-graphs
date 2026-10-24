[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`tomllib` — Parse TOML files](https://docs.python.org/3/library/tomllib.html)
    * [Examples](https://docs.python.org/3/library/tomllib.html#examples)
    * [Conversion Table](https://docs.python.org/3/library/tomllib.html#conversion-table)


#### Previous topic
[`configparser` — Configuration file parser](https://docs.python.org/3/library/configparser.html "previous chapter")
#### Next topic
[`netrc` — netrc file processing](https://docs.python.org/3/library/netrc.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=tomllib+%E2%80%94+Parse+TOML+files&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ftomllib.html&pagesource=library%2Ftomllib.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/netrc.html "netrc — netrc file processing") |
  * [previous](https://docs.python.org/3/library/configparser.html "configparser — Configuration file parser") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [File Formats](https://docs.python.org/3/library/fileformats.html) »
  * [`tomllib` — Parse TOML files](https://docs.python.org/3/library/tomllib.html)
  * |
  * Theme  Auto Light Dark |


#  `tomllib` — Parse TOML files[¶](https://docs.python.org/3/library/tomllib.html#module-tomllib "Link to this heading")
Added in version 3.11.
**Source code:**
* * *
This module provides an interface for parsing TOML 1.0.0 (Tom’s Obvious Minimal Language,
See also
The [`marshal`](https://docs.python.org/3/library/marshal.html#module-marshal "marshal: Convert Python objects to streams of bytes and back \(with different constraints\).") and [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.") modules.
See also
The
This module defines the following functions:

tomllib.load(_fp_ , _/_ , _*_ , _parse_float =float_)[¶](https://docs.python.org/3/library/tomllib.html#tomllib.load "Link to this definition")

Read a TOML file. The first argument should be a readable and binary file object. Return a [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict"). Convert TOML types to Python using this [conversion table](https://docs.python.org/3/library/tomllib.html#toml-to-py-table).
_parse_float_ will be called with the string of every TOML float to be decoded. By default, this is equivalent to `float(num_str)`. This can be used to use another datatype or parser for TOML floats (e.g. [`decimal.Decimal`](https://docs.python.org/3/library/decimal.html#decimal.Decimal "decimal.Decimal")). The callable must not return a [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict") or a [`list`](https://docs.python.org/3/library/stdtypes.html#list "list"), else a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised.
A [`TOMLDecodeError`](https://docs.python.org/3/library/tomllib.html#tomllib.TOMLDecodeError "tomllib.TOMLDecodeError") will be raised on an invalid TOML document.

tomllib.loads(_s_ , _/_ , _*_ , _parse_float =float_)[¶](https://docs.python.org/3/library/tomllib.html#tomllib.loads "Link to this definition")

Load TOML from a [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") object. Return a [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict"). Convert TOML types to Python using this [conversion table](https://docs.python.org/3/library/tomllib.html#toml-to-py-table). The _parse_float_ argument has the same meaning as in [`load()`](https://docs.python.org/3/library/tomllib.html#tomllib.load "tomllib.load").
A [`TOMLDecodeError`](https://docs.python.org/3/library/tomllib.html#tomllib.TOMLDecodeError "tomllib.TOMLDecodeError") will be raised on an invalid TOML document.
The following exceptions are available:

_exception_ tomllib.TOMLDecodeError(_msg_ , _doc_ , _pos_)[¶](https://docs.python.org/3/library/tomllib.html#tomllib.TOMLDecodeError "Link to this definition")

Subclass of [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") with the following additional attributes:

msg[¶](https://docs.python.org/3/library/tomllib.html#tomllib.TOMLDecodeError.msg "Link to this definition")

The unformatted error message.

doc[¶](https://docs.python.org/3/library/tomllib.html#tomllib.TOMLDecodeError.doc "Link to this definition")

The TOML document being parsed.

pos[¶](https://docs.python.org/3/library/tomllib.html#tomllib.TOMLDecodeError.pos "Link to this definition")

The index of _doc_ where parsing failed.

lineno[¶](https://docs.python.org/3/library/tomllib.html#tomllib.TOMLDecodeError.lineno "Link to this definition")

The line corresponding to _pos_.

colno[¶](https://docs.python.org/3/library/tomllib.html#tomllib.TOMLDecodeError.colno "Link to this definition")

The column corresponding to _pos_.
Changed in version 3.14: Added the _msg_ , _doc_ and _pos_ parameters. Added the [`msg`](https://docs.python.org/3/library/tomllib.html#tomllib.TOMLDecodeError.msg "tomllib.TOMLDecodeError.msg"), [`doc`](https://docs.python.org/3/library/tomllib.html#tomllib.TOMLDecodeError.doc "tomllib.TOMLDecodeError.doc"), [`pos`](https://docs.python.org/3/library/tomllib.html#tomllib.TOMLDecodeError.pos "tomllib.TOMLDecodeError.pos"), [`lineno`](https://docs.python.org/3/library/tomllib.html#tomllib.TOMLDecodeError.lineno "tomllib.TOMLDecodeError.lineno") and [`colno`](https://docs.python.org/3/library/tomllib.html#tomllib.TOMLDecodeError.colno "tomllib.TOMLDecodeError.colno") attributes.
Deprecated since version 3.14: Passing free-form positional arguments is deprecated.
## Examples[¶](https://docs.python.org/3/library/tomllib.html#examples "Link to this heading")
Parsing a TOML file:
Copy```
import tomllib

with open("pyproject.toml", "rb") as f:
    data = tomllib.load(f)

```

Parsing a TOML string:
Copy```
import tomllib

toml_str = """
python-version = "3.11.0"
python-implementation = "CPython"
"""

data = tomllib.loads(toml_str)

```

## Conversion Table[¶](https://docs.python.org/3/library/tomllib.html#conversion-table "Link to this heading")
TOML | Python
---|---
TOML document | dict
string | str
integer | int
float | float (configurable with _parse_float_)
boolean | bool
offset date-time | datetime.datetime (`tzinfo` attribute set to an instance of `datetime.timezone`)
local date-time | datetime.datetime (`tzinfo` attribute set to `None`)
local date | datetime.date
local time | datetime.time
array | list
table | dict
inline table | dict
array of tables | list of dicts
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`tomllib` — Parse TOML files](https://docs.python.org/3/library/tomllib.html)
    * [Examples](https://docs.python.org/3/library/tomllib.html#examples)
    * [Conversion Table](https://docs.python.org/3/library/tomllib.html#conversion-table)


#### Previous topic
[`configparser` — Configuration file parser](https://docs.python.org/3/library/configparser.html "previous chapter")
#### Next topic
[`netrc` — netrc file processing](https://docs.python.org/3/library/netrc.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=tomllib+%E2%80%94+Parse+TOML+files&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ftomllib.html&pagesource=library%2Ftomllib.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/netrc.html "netrc — netrc file processing") |
  * [previous](https://docs.python.org/3/library/configparser.html "configparser — Configuration file parser") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [File Formats](https://docs.python.org/3/library/fileformats.html) »
  * [`tomllib` — Parse TOML files](https://docs.python.org/3/library/tomllib.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)
