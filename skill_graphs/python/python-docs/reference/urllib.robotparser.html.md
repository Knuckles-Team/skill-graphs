[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`urllib.error` — Exception classes raised by urllib.request](https://docs.python.org/3/library/urllib.error.html "previous chapter")
#### Next topic
[`http` — HTTP modules](https://docs.python.org/3/library/http.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=urllib.robotparser+%E2%80%94++Parser+for+robots.txt&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Furllib.robotparser.html&pagesource=library%2Furllib.robotparser.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/http.html "http — HTTP modules") |
  * [previous](https://docs.python.org/3/library/urllib.error.html "urllib.error — Exception classes raised by urllib.request") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Internet Protocols and Support](https://docs.python.org/3/library/internet.html) »
  * [`urllib.robotparser` — Parser for robots.txt](https://docs.python.org/3/library/urllib.robotparser.html)
  * |
  * Theme  Auto Light Dark |


#  `urllib.robotparser` — Parser for robots.txt[¶](https://docs.python.org/3/library/urllib.robotparser.html#module-urllib.robotparser "Link to this heading")
**Source code:**
* * *
This module provides a single class, [`RobotFileParser`](https://docs.python.org/3/library/urllib.robotparser.html#urllib.robotparser.RobotFileParser "urllib.robotparser.RobotFileParser"), which answers questions about whether or not a particular user agent can fetch a URL on the website that published the `robots.txt` file. For more details on the structure of `robots.txt` files, see

_class_ urllib.robotparser.RobotFileParser(_url =''_)[¶](https://docs.python.org/3/library/urllib.robotparser.html#urllib.robotparser.RobotFileParser "Link to this definition")

This class provides methods to read, parse and answer questions about the `robots.txt` file at _url_.

set_url(_url_)[¶](https://docs.python.org/3/library/urllib.robotparser.html#urllib.robotparser.RobotFileParser.set_url "Link to this definition")

Sets the URL referring to a `robots.txt` file.

read()[¶](https://docs.python.org/3/library/urllib.robotparser.html#urllib.robotparser.RobotFileParser.read "Link to this definition")

Reads the `robots.txt` URL and feeds it to the parser.

parse(_lines_)[¶](https://docs.python.org/3/library/urllib.robotparser.html#urllib.robotparser.RobotFileParser.parse "Link to this definition")

Parses the lines argument.

can_fetch(_useragent_ , _url_)[¶](https://docs.python.org/3/library/urllib.robotparser.html#urllib.robotparser.RobotFileParser.can_fetch "Link to this definition")

Returns `True` if the _useragent_ is allowed to fetch the _url_ according to the rules contained in the parsed `robots.txt` file.

mtime()[¶](https://docs.python.org/3/library/urllib.robotparser.html#urllib.robotparser.RobotFileParser.mtime "Link to this definition")

Returns the time the `robots.txt` file was last fetched. This is useful for long-running web spiders that need to check for new `robots.txt` files periodically.

modified()[¶](https://docs.python.org/3/library/urllib.robotparser.html#urllib.robotparser.RobotFileParser.modified "Link to this definition")

Sets the time the `robots.txt` file was last fetched to the current time.

crawl_delay(_useragent_)[¶](https://docs.python.org/3/library/urllib.robotparser.html#urllib.robotparser.RobotFileParser.crawl_delay "Link to this definition")

Returns the value of the `Crawl-delay` parameter from `robots.txt` for the _useragent_ in question. If there is no such parameter or it doesn’t apply to the _useragent_ specified or the `robots.txt` entry for this parameter has invalid syntax, return `None`.
Added in version 3.6.

request_rate(_useragent_)[¶](https://docs.python.org/3/library/urllib.robotparser.html#urllib.robotparser.RobotFileParser.request_rate "Link to this definition")

Returns the contents of the `Request-rate` parameter from `robots.txt` as a [named tuple](https://docs.python.org/3/glossary.html#term-named-tuple) `RequestRate(requests, seconds)`. If there is no such parameter or it doesn’t apply to the _useragent_ specified or the `robots.txt` entry for this parameter has invalid syntax, return `None`.
Added in version 3.6.

site_maps()[¶](https://docs.python.org/3/library/urllib.robotparser.html#urllib.robotparser.RobotFileParser.site_maps "Link to this definition")

Returns the contents of the `Sitemap` parameter from `robots.txt` in the form of a [`list()`](https://docs.python.org/3/library/stdtypes.html#list "list"). If there is no such parameter or the `robots.txt` entry for this parameter has invalid syntax, return `None`.
Added in version 3.8.
The following example demonstrates basic use of the [`RobotFileParser`](https://docs.python.org/3/library/urllib.robotparser.html#urllib.robotparser.RobotFileParser "urllib.robotparser.RobotFileParser") class:
Copy```
>>> import urllib.robotparser
>>> rp = urllib.robotparser.RobotFileParser()
>>> rp.set_url("http://www.pythontest.net/robots.txt")
>>> rp.read()
>>> rrate = rp.request_rate("*")
>>> rrate.requests
1
>>> rrate.seconds
1
>>> rp.crawl_delay("*")
6
>>> rp.can_fetch("*", "http://www.pythontest.net/")
True
>>> rp.can_fetch("*", "http://www.pythontest.net/no-robots-here/")
False

```

#### Previous topic
[`urllib.error` — Exception classes raised by urllib.request](https://docs.python.org/3/library/urllib.error.html "previous chapter")
#### Next topic
[`http` — HTTP modules](https://docs.python.org/3/library/http.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=urllib.robotparser+%E2%80%94++Parser+for+robots.txt&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Furllib.robotparser.html&pagesource=library%2Furllib.robotparser.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/http.html "http — HTTP modules") |
  * [previous](https://docs.python.org/3/library/urllib.error.html "urllib.error — Exception classes raised by urllib.request") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Internet Protocols and Support](https://docs.python.org/3/library/internet.html) »
  * [`urllib.robotparser` — Parser for robots.txt](https://docs.python.org/3/library/urllib.robotparser.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
