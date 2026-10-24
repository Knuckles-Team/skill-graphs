[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`_thread` — Low-level threading API](https://docs.python.org/3/library/_thread.html "previous chapter")
#### Next topic
[`asyncio` — Asynchronous I/O](https://docs.python.org/3/library/asyncio.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Networking+and+Interprocess+Communication&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fipc.html&pagesource=library%2Fipc.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/asyncio.html "asyncio — Asynchronous I/O") |
  * [previous](https://docs.python.org/3/library/_thread.html "_thread — Low-level threading API") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Networking and Interprocess Communication](https://docs.python.org/3/library/ipc.html)
  * |
  * Theme  Auto Light Dark |


# Networking and Interprocess Communication[¶](https://docs.python.org/3/library/ipc.html#networking-and-interprocess-communication "Link to this heading")
The modules described in this chapter provide mechanisms for networking and inter-processes communication.
Some modules only work for two processes that are on the same machine, e.g. [`signal`](https://docs.python.org/3/library/signal.html#module-signal "signal: Set handlers for asynchronous events.") and [`mmap`](https://docs.python.org/3/library/mmap.html#module-mmap "mmap: Interface to memory-mapped files for Unix and Windows."). Other modules support networking protocols that two or more processes can use to communicate across machines.
The list of modules described in this chapter is:
  * [`asyncio` — Asynchronous I/O](https://docs.python.org/3/library/asyncio.html)
  * [`socket` — Low-level networking interface](https://docs.python.org/3/library/socket.html)
  * [`ssl` — TLS/SSL wrapper for socket objects](https://docs.python.org/3/library/ssl.html)
  * [`select` — Waiting for I/O completion](https://docs.python.org/3/library/select.html)
  * [`selectors` — High-level I/O multiplexing](https://docs.python.org/3/library/selectors.html)
  * [`signal` — Set handlers for asynchronous events](https://docs.python.org/3/library/signal.html)
  * [`mmap` — Memory-mapped file support](https://docs.python.org/3/library/mmap.html)


#### Previous topic
[`_thread` — Low-level threading API](https://docs.python.org/3/library/_thread.html "previous chapter")
#### Next topic
[`asyncio` — Asynchronous I/O](https://docs.python.org/3/library/asyncio.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Networking+and+Interprocess+Communication&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fipc.html&pagesource=library%2Fipc.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/asyncio.html "asyncio — Asynchronous I/O") |
  * [previous](https://docs.python.org/3/library/_thread.html "_thread — Low-level threading API") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Networking and Interprocess Communication](https://docs.python.org/3/library/ipc.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
