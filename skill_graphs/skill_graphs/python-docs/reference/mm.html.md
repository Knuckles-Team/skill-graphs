[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`ipaddress` — IPv4/IPv6 manipulation library](https://docs.python.org/3/library/ipaddress.html "previous chapter")
#### Next topic
[`wave` — Read and write WAV files](https://docs.python.org/3/library/wave.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Multimedia+Services&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fmm.html&pagesource=library%2Fmm.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/wave.html "wave — Read and write WAV files") |
  * [previous](https://docs.python.org/3/library/ipaddress.html "ipaddress — IPv4/IPv6 manipulation library") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Multimedia Services](https://docs.python.org/3/library/mm.html)
  * |
  * Theme  Auto Light Dark |


# Multimedia Services[¶](https://docs.python.org/3/library/mm.html#multimedia-services "Link to this heading")
The modules described in this chapter implement various algorithms or interfaces that are mainly useful for multimedia applications. They are available at the discretion of the installation. Here’s an overview:
  * [`wave` — Read and write WAV files](https://docs.python.org/3/library/wave.html)
    * [Wave_read Objects](https://docs.python.org/3/library/wave.html#wave-read-objects)
    * [Wave_write Objects](https://docs.python.org/3/library/wave.html#wave-write-objects)
  * [`colorsys` — Conversions between color systems](https://docs.python.org/3/library/colorsys.html)


#### Previous topic
[`ipaddress` — IPv4/IPv6 manipulation library](https://docs.python.org/3/library/ipaddress.html "previous chapter")
#### Next topic
[`wave` — Read and write WAV files](https://docs.python.org/3/library/wave.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Multimedia+Services&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fmm.html&pagesource=library%2Fmm.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/wave.html "wave — Read and write WAV files") |
  * [previous](https://docs.python.org/3/library/ipaddress.html "ipaddress — IPv4/IPv6 manipulation library") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Multimedia Services](https://docs.python.org/3/library/mm.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
