[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`urllib.parse` — Parse URLs into components](https://docs.python.org/3/library/urllib.parse.html "previous chapter")
#### Next topic
[`urllib.robotparser` — Parser for robots.txt](https://docs.python.org/3/library/urllib.robotparser.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=urllib.error+%E2%80%94+Exception+classes+raised+by+urllib.request&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Furllib.error.html&pagesource=library%2Furllib.error.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/urllib.robotparser.html "urllib.robotparser — Parser for robots.txt") |
  * [previous](https://docs.python.org/3/library/urllib.parse.html "urllib.parse — Parse URLs into components") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Internet Protocols and Support](https://docs.python.org/3/library/internet.html) »
  * [`urllib.error` — Exception classes raised by urllib.request](https://docs.python.org/3/library/urllib.error.html)
  * |
  * Theme  Auto Light Dark |


#  `urllib.error` — Exception classes raised by urllib.request[¶](https://docs.python.org/3/library/urllib.error.html#module-urllib.error "Link to this heading")
**Source code:**
* * *
The `urllib.error` module defines the exception classes for exceptions raised by [`urllib.request`](https://docs.python.org/3/library/urllib.request.html#module-urllib.request "urllib.request: Extensible library for opening URLs."). The base exception class is [`URLError`](https://docs.python.org/3/library/urllib.error.html#urllib.error.URLError "urllib.error.URLError").
The following exceptions are raised by `urllib.error` as appropriate:

_exception_ urllib.error.URLError[¶](https://docs.python.org/3/library/urllib.error.html#urllib.error.URLError "Link to this definition")

The handlers raise this exception (or derived exceptions) when they run into a problem. It is a subclass of [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError").

reason[¶](https://docs.python.org/3/library/urllib.error.html#urllib.error.URLError.reason "Link to this definition")

The reason for this error. It can be a message string or another exception instance.
Changed in version 3.3: `URLError` used to be a subtype of [`IOError`](https://docs.python.org/3/library/exceptions.html#IOError "IOError"), which is now an alias of [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError").

_exception_ urllib.error.HTTPError(_url_ , _code_ , _msg_ , _hdrs_ , _fp_)[¶](https://docs.python.org/3/library/urllib.error.html#urllib.error.HTTPError "Link to this definition")

Though being an exception (a subclass of [`URLError`](https://docs.python.org/3/library/urllib.error.html#urllib.error.URLError "urllib.error.URLError")), an `HTTPError` can also function as a non-exceptional file-like return value (the same thing that [`urlopen()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen "urllib.request.urlopen") returns). This is useful when handling exotic HTTP errors, such as requests for authentication.

url[¶](https://docs.python.org/3/library/urllib.error.html#urllib.error.HTTPError.url "Link to this definition")

Contains the request URL. An alias for _filename_ attribute.

code[¶](https://docs.python.org/3/library/urllib.error.html#urllib.error.HTTPError.code "Link to this definition")

An HTTP status code as defined in [`http.server.BaseHTTPRequestHandler.responses`](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.responses "http.server.BaseHTTPRequestHandler.responses").

reason[¶](https://docs.python.org/3/library/urllib.error.html#urllib.error.HTTPError.reason "Link to this definition")

This is usually a string explaining the reason for this error. An alias for _msg_ attribute.

headers[¶](https://docs.python.org/3/library/urllib.error.html#urllib.error.HTTPError.headers "Link to this definition")

The HTTP response headers for the HTTP request that caused the `HTTPError`. An alias for _hdrs_ attribute.
Added in version 3.4.

fp[¶](https://docs.python.org/3/library/urllib.error.html#urllib.error.HTTPError.fp "Link to this definition")

A file-like object where the HTTP error body can be read from.

_exception_ urllib.error.ContentTooShortError(_msg_ , _content_)[¶](https://docs.python.org/3/library/urllib.error.html#urllib.error.ContentTooShortError "Link to this definition")

This exception is raised when the [`urlretrieve()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.urlretrieve "urllib.request.urlretrieve") function detects that the amount of the downloaded data is less than the expected amount (given by the _Content-Length_ header).

content[¶](https://docs.python.org/3/library/urllib.error.html#urllib.error.ContentTooShortError.content "Link to this definition")

The downloaded (and supposedly truncated) data.
#### Previous topic
[`urllib.parse` — Parse URLs into components](https://docs.python.org/3/library/urllib.parse.html "previous chapter")
#### Next topic
[`urllib.robotparser` — Parser for robots.txt](https://docs.python.org/3/library/urllib.robotparser.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=urllib.error+%E2%80%94+Exception+classes+raised+by+urllib.request&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Furllib.error.html&pagesource=library%2Furllib.error.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/urllib.robotparser.html "urllib.robotparser — Parser for robots.txt") |
  * [previous](https://docs.python.org/3/library/urllib.parse.html "urllib.parse — Parse URLs into components") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Internet Protocols and Support](https://docs.python.org/3/library/internet.html) »
  * [`urllib.error` — Exception classes raised by urllib.request](https://docs.python.org/3/library/urllib.error.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
