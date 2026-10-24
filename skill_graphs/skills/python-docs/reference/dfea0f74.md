# Concatenate all the partial results:
result = b"".join([out1, out2, out3, out4])

```

Writing compressed data to an already-open file:
Copy```
from compression import zstd

with open("myfile", "wb") as f:
    f.write(b"This data will not be compressed\n")
    with zstd.open(f, "w") as zstf:
        zstf.write(b"This *will* be compressed\n")
    f.write(b"Not compressed\n")

```

Creating a compressed file using compression parameters:
Copy```
from compression import zstd

options = {
   zstd.CompressionParameter.checksum_flag: 1
}
with zstd.open("file.zst", "w", options=options) as f:
    f.write(b"Mind if I squeeze in?")

```

### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`compression.zstd` — Compression compatible with the Zstandard format](https://docs.python.org/3/library/compression.zstd.html)
    * [Exceptions](https://docs.python.org/3/library/compression.zstd.html#exceptions)
    * [Reading and writing compressed files](https://docs.python.org/3/library/compression.zstd.html#reading-and-writing-compressed-files)
    * [Compressing and decompressing data in memory](https://docs.python.org/3/library/compression.zstd.html#compressing-and-decompressing-data-in-memory)
    * [Zstandard dictionaries](https://docs.python.org/3/library/compression.zstd.html#zstandard-dictionaries)
    * [Advanced parameter control](https://docs.python.org/3/library/compression.zstd.html#advanced-parameter-control)
    * [Miscellaneous](https://docs.python.org/3/library/compression.zstd.html#miscellaneous)
    * [Examples](https://docs.python.org/3/library/compression.zstd.html#examples)


#### Previous topic
[The `compression` package](https://docs.python.org/3/library/compression.html "previous chapter")
#### Next topic
[`zlib` — Compression compatible with **gzip**](https://docs.python.org/3/library/zlib.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=compression.zstd+%E2%80%94+Compression+compatible+with+the+Zstandard+format&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fcompression.zstd.html&pagesource=library%2Fcompression.zstd.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/zlib.html "zlib — Compression compatible with gzip") |
  * [previous](https://docs.python.org/3/library/compression.html "The compression package") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Data Compression and Archiving](https://docs.python.org/3/library/archiving.html) »
  * [`compression.zstd` — Compression compatible with the Zstandard format](https://docs.python.org/3/library/compression.zstd.html)
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
