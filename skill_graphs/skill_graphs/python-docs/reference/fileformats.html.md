[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`tarfile` — Read and write tar archive files](https://docs.python.org/3/library/tarfile.html "previous chapter")
#### Next topic
[`csv` — CSV File Reading and Writing](https://docs.python.org/3/library/csv.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=File+Formats&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ffileformats.html&pagesource=library%2Ffileformats.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/csv.html "csv — CSV File Reading and Writing") |
  * [previous](https://docs.python.org/3/library/tarfile.html "tarfile — Read and write tar archive files") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [File Formats](https://docs.python.org/3/library/fileformats.html)
  * |
  * Theme  Auto Light Dark |


# File Formats[¶](https://docs.python.org/3/library/fileformats.html#file-formats "Link to this heading")
The modules described in this chapter parse various miscellaneous file formats that aren’t markup languages and are not related to e-mail.
  * [`csv` — CSV File Reading and Writing](https://docs.python.org/3/library/csv.html)
    * [Module Contents](https://docs.python.org/3/library/csv.html#module-contents)
    * [Dialects and Formatting Parameters](https://docs.python.org/3/library/csv.html#dialects-and-formatting-parameters)
    * [Reader Objects](https://docs.python.org/3/library/csv.html#reader-objects)
    * [Writer Objects](https://docs.python.org/3/library/csv.html#writer-objects)
    * [Examples](https://docs.python.org/3/library/csv.html#examples)
  * [`configparser` — Configuration file parser](https://docs.python.org/3/library/configparser.html)
    * [Quick Start](https://docs.python.org/3/library/configparser.html#quick-start)
    * [Supported Datatypes](https://docs.python.org/3/library/configparser.html#supported-datatypes)
    * [Fallback Values](https://docs.python.org/3/library/configparser.html#fallback-values)
    * [Supported INI File Structure](https://docs.python.org/3/library/configparser.html#supported-ini-file-structure)
    * [Unnamed Sections](https://docs.python.org/3/library/configparser.html#unnamed-sections)
    * [Interpolation of values](https://docs.python.org/3/library/configparser.html#interpolation-of-values)
    * [Mapping Protocol Access](https://docs.python.org/3/library/configparser.html#mapping-protocol-access)
    * [Customizing Parser Behaviour](https://docs.python.org/3/library/configparser.html#customizing-parser-behaviour)
    * [Legacy API Examples](https://docs.python.org/3/library/configparser.html#legacy-api-examples)
    * [ConfigParser Objects](https://docs.python.org/3/library/configparser.html#configparser-objects)
    * [RawConfigParser Objects](https://docs.python.org/3/library/configparser.html#rawconfigparser-objects)
    * [Exceptions](https://docs.python.org/3/library/configparser.html#exceptions)
  * [`tomllib` — Parse TOML files](https://docs.python.org/3/library/tomllib.html)
    * [Examples](https://docs.python.org/3/library/tomllib.html#examples)
    * [Conversion Table](https://docs.python.org/3/library/tomllib.html#conversion-table)
  * [`netrc` — netrc file processing](https://docs.python.org/3/library/netrc.html)
    * [netrc Objects](https://docs.python.org/3/library/netrc.html#netrc-objects)
  * [`plistlib` — Generate and parse Apple `.plist` files](https://docs.python.org/3/library/plistlib.html)
    * [Examples](https://docs.python.org/3/library/plistlib.html#examples)


#### Previous topic
[`tarfile` — Read and write tar archive files](https://docs.python.org/3/library/tarfile.html "previous chapter")
#### Next topic
[`csv` — CSV File Reading and Writing](https://docs.python.org/3/library/csv.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=File+Formats&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ffileformats.html&pagesource=library%2Ffileformats.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/csv.html "csv — CSV File Reading and Writing") |
  * [previous](https://docs.python.org/3/library/tarfile.html "tarfile — Read and write tar archive files") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [File Formats](https://docs.python.org/3/library/fileformats.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
