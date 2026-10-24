[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`sqlite3` — DB-API 2.0 interface for SQLite databases](https://docs.python.org/3/library/sqlite3.html "previous chapter")
#### Next topic
[The `compression` package](https://docs.python.org/3/library/compression.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Data+Compression+and+Archiving&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Farchiving.html&pagesource=library%2Farchiving.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/compression.html "The compression package") |
  * [previous](https://docs.python.org/3/library/sqlite3.html "sqlite3 — DB-API 2.0 interface for SQLite databases") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Data Compression and Archiving](https://docs.python.org/3/library/archiving.html)
  * |
  * Theme  Auto Light Dark |


# Data Compression and Archiving[¶](https://docs.python.org/3/library/archiving.html#data-compression-and-archiving "Link to this heading")
The modules described in this chapter support data compression with the zlib, gzip, bzip2, lzma, and zstd algorithms, and the creation of ZIP- and tar-format archives. See also [Archiving operations](https://docs.python.org/3/library/shutil.html#archiving-operations) provided by the [`shutil`](https://docs.python.org/3/library/shutil.html#module-shutil "shutil: High-level file operations, including copying.") module.
  * [The `compression` package](https://docs.python.org/3/library/compression.html)
  * [`compression.zstd` — Compression compatible with the Zstandard format](https://docs.python.org/3/library/compression.zstd.html)
    * [Exceptions](https://docs.python.org/3/library/compression.zstd.html#exceptions)
    * [Reading and writing compressed files](https://docs.python.org/3/library/compression.zstd.html#reading-and-writing-compressed-files)
    * [Compressing and decompressing data in memory](https://docs.python.org/3/library/compression.zstd.html#compressing-and-decompressing-data-in-memory)
    * [Zstandard dictionaries](https://docs.python.org/3/library/compression.zstd.html#zstandard-dictionaries)
    * [Advanced parameter control](https://docs.python.org/3/library/compression.zstd.html#advanced-parameter-control)
    * [Miscellaneous](https://docs.python.org/3/library/compression.zstd.html#miscellaneous)
    * [Examples](https://docs.python.org/3/library/compression.zstd.html#examples)
  * [`zlib` — Compression compatible with **gzip**](https://docs.python.org/3/library/zlib.html)
  * [`gzip` — Support for **gzip** files](https://docs.python.org/3/library/gzip.html)
    * [Examples of usage](https://docs.python.org/3/library/gzip.html#examples-of-usage)
    * [Command-line interface](https://docs.python.org/3/library/gzip.html#command-line-interface)
      * [Command-line options](https://docs.python.org/3/library/gzip.html#command-line-options)
  * [`bz2` — Support for **bzip2** compression](https://docs.python.org/3/library/bz2.html)
    * [(De)compression of files](https://docs.python.org/3/library/bz2.html#de-compression-of-files)
    * [Incremental (de)compression](https://docs.python.org/3/library/bz2.html#incremental-de-compression)
    * [One-shot (de)compression](https://docs.python.org/3/library/bz2.html#one-shot-de-compression)
    * [Examples of usage](https://docs.python.org/3/library/bz2.html#examples-of-usage)
  * [`lzma` — Compression using the LZMA algorithm](https://docs.python.org/3/library/lzma.html)
    * [Reading and writing compressed files](https://docs.python.org/3/library/lzma.html#reading-and-writing-compressed-files)
    * [Compressing and decompressing data in memory](https://docs.python.org/3/library/lzma.html#compressing-and-decompressing-data-in-memory)
    * [Miscellaneous](https://docs.python.org/3/library/lzma.html#miscellaneous)
    * [Specifying custom filter chains](https://docs.python.org/3/library/lzma.html#specifying-custom-filter-chains)
    * [Examples](https://docs.python.org/3/library/lzma.html#examples)
  * [`zipfile` — Work with ZIP archives](https://docs.python.org/3/library/zipfile.html)
    * [ZipFile objects](https://docs.python.org/3/library/zipfile.html#zipfile-objects)
    * [Path objects](https://docs.python.org/3/library/zipfile.html#path-objects)
    * [PyZipFile objects](https://docs.python.org/3/library/zipfile.html#pyzipfile-objects)
    * [ZipInfo objects](https://docs.python.org/3/library/zipfile.html#zipinfo-objects)
    * [Command-line interface](https://docs.python.org/3/library/zipfile.html#command-line-interface)
      * [Command-line options](https://docs.python.org/3/library/zipfile.html#command-line-options)
    * [Decompression pitfalls](https://docs.python.org/3/library/zipfile.html#decompression-pitfalls)
      * [From file itself](https://docs.python.org/3/library/zipfile.html#from-file-itself)
      * [File system limitations](https://docs.python.org/3/library/zipfile.html#file-system-limitations)
      * [Resources limitations](https://docs.python.org/3/library/zipfile.html#resources-limitations)
      * [Interruption](https://docs.python.org/3/library/zipfile.html#interruption)
      * [Default behaviors of extraction](https://docs.python.org/3/library/zipfile.html#default-behaviors-of-extraction)
  * [`tarfile` — Read and write tar archive files](https://docs.python.org/3/library/tarfile.html)
    * [TarFile Objects](https://docs.python.org/3/library/tarfile.html#tarfile-objects)
    * [TarInfo Objects](https://docs.python.org/3/library/tarfile.html#tarinfo-objects)
    * [Extraction filters](https://docs.python.org/3/library/tarfile.html#extraction-filters)
      * [Default named filters](https://docs.python.org/3/library/tarfile.html#default-named-filters)
      * [Filter errors](https://docs.python.org/3/library/tarfile.html#filter-errors)
      * [Hints for further verification](https://docs.python.org/3/library/tarfile.html#hints-for-further-verification)
      * [Supporting older Python versions](https://docs.python.org/3/library/tarfile.html#supporting-older-python-versions)
      * [Stateful extraction filter example](https://docs.python.org/3/library/tarfile.html#stateful-extraction-filter-example)
    * [Command-Line Interface](https://docs.python.org/3/library/tarfile.html#command-line-interface)
      * [Command-line options](https://docs.python.org/3/library/tarfile.html#command-line-options)
    * [Examples](https://docs.python.org/3/library/tarfile.html#examples)
      * [Reading examples](https://docs.python.org/3/library/tarfile.html#reading-examples)
      * [Writing examples](https://docs.python.org/3/library/tarfile.html#writing-examples)
    * [Supported tar formats](https://docs.python.org/3/library/tarfile.html#supported-tar-formats)
    * [Unicode issues](https://docs.python.org/3/library/tarfile.html#unicode-issues)


#### Previous topic
[`sqlite3` — DB-API 2.0 interface for SQLite databases](https://docs.python.org/3/library/sqlite3.html "previous chapter")
#### Next topic
[The `compression` package](https://docs.python.org/3/library/compression.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Data+Compression+and+Archiving&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Farchiving.html&pagesource=library%2Farchiving.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/compression.html "The compression package") |
  * [previous](https://docs.python.org/3/library/sqlite3.html "sqlite3 — DB-API 2.0 interface for SQLite databases") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Data Compression and Archiving](https://docs.python.org/3/library/archiving.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
