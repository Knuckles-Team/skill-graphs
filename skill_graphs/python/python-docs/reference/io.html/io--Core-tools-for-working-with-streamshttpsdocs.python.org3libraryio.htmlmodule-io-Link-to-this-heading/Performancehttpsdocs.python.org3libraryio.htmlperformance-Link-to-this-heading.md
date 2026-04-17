## Performance[¶](https://docs.python.org/3/library/io.html#performance "Link to this heading")
This section discusses the performance of the provided concrete I/O implementations.
### Binary I/O[¶](https://docs.python.org/3/library/io.html#id2 "Link to this heading")
By reading and writing only large chunks of data even when the user asks for a single byte, buffered I/O hides any inefficiency in calling and executing the operating system’s unbuffered I/O routines. The gain depends on the OS and the kind of I/O which is performed. For example, on some modern OSes such as Linux, unbuffered disk I/O can be as fast as buffered I/O. The bottom line, however, is that buffered I/O offers predictable performance regardless of the platform and the backing device. Therefore, it is almost always preferable to use buffered I/O rather than unbuffered I/O for binary data.
### Text I/O[¶](https://docs.python.org/3/library/io.html#id3 "Link to this heading")
Text I/O over a binary storage (such as a file) is significantly slower than binary I/O over the same storage, because it requires conversions between unicode and binary data using a character codec. This can become noticeable handling huge amounts of text data like large log files. Also, [`tell()`](https://docs.python.org/3/library/io.html#io.TextIOBase.tell "io.TextIOBase.tell") and [`seek()`](https://docs.python.org/3/library/io.html#io.TextIOBase.seek "io.TextIOBase.seek") are both quite slow due to the reconstruction algorithm used.
[`StringIO`](https://docs.python.org/3/library/io.html#io.StringIO "io.StringIO"), however, is a native in-memory unicode container and will exhibit similar speed to [`BytesIO`](https://docs.python.org/3/library/io.html#io.BytesIO "io.BytesIO").
### Multi-threading[¶](https://docs.python.org/3/library/io.html#multi-threading "Link to this heading")
[`FileIO`](https://docs.python.org/3/library/io.html#io.FileIO "io.FileIO") objects are thread-safe to the extent that the operating system calls (such as
Binary buffered objects (instances of [`BufferedReader`](https://docs.python.org/3/library/io.html#io.BufferedReader "io.BufferedReader"), [`BufferedWriter`](https://docs.python.org/3/library/io.html#io.BufferedWriter "io.BufferedWriter"), [`BufferedRandom`](https://docs.python.org/3/library/io.html#io.BufferedRandom "io.BufferedRandom") and [`BufferedRWPair`](https://docs.python.org/3/library/io.html#io.BufferedRWPair "io.BufferedRWPair")) protect their internal structures using a lock; it is therefore safe to call them from multiple threads at once.
[`TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper") objects are not thread-safe.
### Reentrancy[¶](https://docs.python.org/3/library/io.html#reentrancy "Link to this heading")
Binary buffered objects (instances of [`BufferedReader`](https://docs.python.org/3/library/io.html#io.BufferedReader "io.BufferedReader"), [`BufferedWriter`](https://docs.python.org/3/library/io.html#io.BufferedWriter "io.BufferedWriter"), [`BufferedRandom`](https://docs.python.org/3/library/io.html#io.BufferedRandom "io.BufferedRandom") and [`BufferedRWPair`](https://docs.python.org/3/library/io.html#io.BufferedRWPair "io.BufferedRWPair")) are not reentrant. While reentrant calls will not happen in normal situations, they can arise from doing I/O in a [`signal`](https://docs.python.org/3/library/signal.html#module-signal "signal: Set handlers for asynchronous events.") handler. If a thread tries to re-enter a buffered object which it is already accessing, a [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError") is raised. Note this doesn’t prohibit a different thread from entering the buffered object.
The above implicitly extends to text files, since the [`open()`](https://docs.python.org/3/library/functions.html#open "open") function will wrap a buffered object inside a [`TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper"). This includes standard streams and therefore affects the built-in [`print()`](https://docs.python.org/3/library/functions.html#print "print") function as well.
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`io` — Core tools for working with streams](https://docs.python.org/3/library/io.html)
    * [Overview](https://docs.python.org/3/library/io.html#overview)
      * [Text I/O](https://docs.python.org/3/library/io.html#text-i-o)
      * [Binary I/O](https://docs.python.org/3/library/io.html#binary-i-o)
      * [Raw I/O](https://docs.python.org/3/library/io.html#raw-i-o)
    * [Text Encoding](https://docs.python.org/3/library/io.html#text-encoding)
      * [Opt-in EncodingWarning](https://docs.python.org/3/library/io.html#opt-in-encodingwarning)
    * [High-level Module Interface](https://docs.python.org/3/library/io.html#high-level-module-interface)
    * [Class hierarchy](https://docs.python.org/3/library/io.html#class-hierarchy)
      * [I/O Base Classes](https://docs.python.org/3/library/io.html#i-o-base-classes)
      * [Raw File I/O](https://docs.python.org/3/library/io.html#raw-file-i-o)
      * [Buffered Streams](https://docs.python.org/3/library/io.html#buffered-streams)
      * [Text I/O](https://docs.python.org/3/library/io.html#id1)
    * [Static Typing](https://docs.python.org/3/library/io.html#static-typing)
    * [Performance](https://docs.python.org/3/library/io.html#performance)
      * [Binary I/O](https://docs.python.org/3/library/io.html#id2)
      * [Text I/O](https://docs.python.org/3/library/io.html#id3)
      * [Multi-threading](https://docs.python.org/3/library/io.html#multi-threading)
      * [Reentrancy](https://docs.python.org/3/library/io.html#reentrancy)


#### Previous topic
[`os` — Miscellaneous operating system interfaces](https://docs.python.org/3/library/os.html "previous chapter")
#### Next topic
[`time` — Time access and conversions](https://docs.python.org/3/library/time.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=io+%E2%80%94+Core+tools+for+working+with+streams&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fio.html&pagesource=library%2Fio.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/time.html "time — Time access and conversions") |
  * [previous](https://docs.python.org/3/library/os.html "os — Miscellaneous operating system interfaces") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Generic Operating System Services](https://docs.python.org/3/library/allows.html) »
  * [`io` — Core tools for working with streams](https://docs.python.org/3/library/io.html)
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
