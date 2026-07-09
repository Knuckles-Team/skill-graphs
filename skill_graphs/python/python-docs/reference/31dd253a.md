## Legacy interface[¶](https://docs.python.org/3/library/urllib.request.html#legacy-interface "Link to this heading")
The following functions and classes are ported from the Python 2 module `urllib` (as opposed to `urllib2`). They might become deprecated at some point in the future.

urllib.request.urlretrieve(_url_ , _filename =None_, _reporthook =None_, _data =None_)[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.urlretrieve "Link to this definition")

Copy a network object denoted by a URL to a local file. If the URL points to a local file, the object will not be copied unless filename is supplied. Return a tuple `(filename, headers)` where _filename_ is the local file name under which the object can be found, and _headers_ is whatever the `info()` method of the object returned by [`urlopen()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen "urllib.request.urlopen") returned (for a remote object). Exceptions are the same as for `urlopen()`.
The second argument, if present, specifies the file location to copy to (if absent, the location will be a tempfile with a generated name). The third argument, if present, is a callable that will be called once on establishment of the network connection and once after each block read thereafter. The callable will be passed three arguments; a count of blocks transferred so far, a block size in bytes, and the total size of the file. The third argument may be `-1` on older FTP servers which do not return a file size in response to a retrieval request.
The following example illustrates the most common usage scenario:
Copy```
>>> import urllib.request
>>> local_filename, headers = urllib.request.urlretrieve('http://python.org/')
>>> html = open(local_filename)
>>> html.close()

```

If the _url_ uses the `http:` scheme identifier, the optional _data_ argument may be given to specify a `POST` request (normally the request type is `GET`). The _data_ argument must be a bytes object in standard _application/x-www-form-urlencoded_ format; see the [`urllib.parse.urlencode()`](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urlencode "urllib.parse.urlencode") function.
`urlretrieve()` will raise [`ContentTooShortError`](https://docs.python.org/3/library/urllib.error.html#urllib.error.ContentTooShortError "urllib.error.ContentTooShortError") when it detects that the amount of data available was less than the expected amount (which is the size reported by a _Content-Length_ header). This can occur, for example, when the download is interrupted.
The _Content-Length_ is treated as a lower bound: if there’s more data to read, urlretrieve reads more data, but if less data is available, it raises the exception.
You can still retrieve the downloaded data in this case, it is stored in the `content` attribute of the exception instance.
If no _Content-Length_ header was supplied, urlretrieve can not check the size of the data it has downloaded, and just returns it. In this case you just have to assume that the download was successful.

urllib.request.urlcleanup()[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.urlcleanup "Link to this definition")

Cleans up temporary files that may have been left behind by previous calls to [`urlretrieve()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.urlretrieve "urllib.request.urlretrieve").
##  `urllib.request` Restrictions[¶](https://docs.python.org/3/library/urllib.request.html#urllib-request-restrictions "Link to this heading")
  * Currently, only the following protocols are supported: HTTP (versions 0.9 and 1.0), FTP, local files, and data URLs.
Changed in version 3.4: Added support for data URLs.
  * The caching feature of [`urlretrieve()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.urlretrieve "urllib.request.urlretrieve") has been disabled until someone finds the time to hack proper processing of Expiration time headers.
  * There should be a function to query whether a particular URL is in the cache.
  * For backward compatibility, if a URL appears to point to a local file but the file can’t be opened, the URL is re-interpreted using the FTP protocol. This can sometimes cause confusing error messages.
  * The [`urlopen()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen "urllib.request.urlopen") and [`urlretrieve()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.urlretrieve "urllib.request.urlretrieve") functions can cause arbitrarily long delays while waiting for a network connection to be set up. This means that it is difficult to build an interactive web client using these functions without using threads.
  * The data returned by [`urlopen()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen "urllib.request.urlopen") or [`urlretrieve()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.urlretrieve "urllib.request.urlretrieve") is the raw data returned by the server. This may be binary data (such as an image), plain text or (for example) HTML. The HTTP protocol provides type information in the reply header, which can be inspected by looking at the _Content-Type_ header. If the returned data is HTML, you can use the module [`html.parser`](https://docs.python.org/3/library/html.parser.html#module-html.parser "html.parser: A simple parser that can handle HTML and XHTML.") to parse it.
  * The code handling the FTP protocol cannot differentiate between a file and a directory. This can lead to unexpected behavior when attempting to read a URL that points to a file that is not accessible. If the URL ends in a `/`, it is assumed to refer to a directory and will be handled accordingly. But if an attempt to read a file leads to a 550 error (meaning the URL cannot be found or is not accessible, often for permission reasons), then the path is treated as a directory in order to handle the case when a directory is specified by a URL but the trailing `/` has been left off. This can cause misleading results when you try to fetch a file whose read permissions make it inaccessible; the FTP code will try to read it, fail with a 550 error, and then perform a directory listing for the unreadable file. If fine-grained control is needed, consider using the [`ftplib`](https://docs.python.org/3/library/ftplib.html#module-ftplib "ftplib: FTP protocol client \(requires sockets\).") module.


#  `urllib.response` — Response classes used by urllib[¶](https://docs.python.org/3/library/urllib.request.html#module-urllib.response "Link to this heading")
The `urllib.response` module defines functions and classes which define a minimal file-like interface, including `read()` and `readline()`. Functions defined by this module are used internally by the `urllib.request` module. The typical response object is a [`urllib.response.addinfourl`](https://docs.python.org/3/library/urllib.request.html#urllib.response.addinfourl "urllib.response.addinfourl") instance:

_class_ urllib.response.addinfourl[¶](https://docs.python.org/3/library/urllib.request.html#urllib.response.addinfourl "Link to this definition")


url[¶](https://docs.python.org/3/library/urllib.request.html#urllib.response.addinfourl.url "Link to this definition")

URL of the resource retrieved, commonly used to determine if a redirect was followed.

headers[¶](https://docs.python.org/3/library/urllib.request.html#urllib.response.addinfourl.headers "Link to this definition")

Returns the headers of the response in the form of an [`EmailMessage`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage "email.message.EmailMessage") instance.

status[¶](https://docs.python.org/3/library/urllib.request.html#urllib.response.addinfourl.status "Link to this definition")

Added in version 3.9.
Status code returned by server.

geturl()[¶](https://docs.python.org/3/library/urllib.request.html#urllib.response.addinfourl.geturl "Link to this definition")

Deprecated since version 3.9: Deprecated in favor of [`url`](https://docs.python.org/3/library/urllib.request.html#urllib.response.addinfourl.url "urllib.response.addinfourl.url").

info()[¶](https://docs.python.org/3/library/urllib.request.html#urllib.response.addinfourl.info "Link to this definition")

Deprecated since version 3.9: Deprecated in favor of [`headers`](https://docs.python.org/3/library/urllib.request.html#urllib.response.addinfourl.headers "urllib.response.addinfourl.headers").

code[¶](https://docs.python.org/3/library/urllib.request.html#urllib.response.addinfourl.code "Link to this definition")

Deprecated since version 3.9: Deprecated in favor of [`status`](https://docs.python.org/3/library/urllib.request.html#urllib.response.addinfourl.status "urllib.response.addinfourl.status").

getcode()[¶](https://docs.python.org/3/library/urllib.request.html#urllib.response.addinfourl.getcode "Link to this definition")

Deprecated since version 3.9: Deprecated in favor of [`status`](https://docs.python.org/3/library/urllib.request.html#urllib.response.addinfourl.status "urllib.response.addinfourl.status").
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`urllib.request` — Extensible library for opening URLs](https://docs.python.org/3/library/urllib.request.html)
    * [Request Objects](https://docs.python.org/3/library/urllib.request.html#request-objects)
    * [OpenerDirector Objects](https://docs.python.org/3/library/urllib.request.html#openerdirector-objects)
    * [BaseHandler Objects](https://docs.python.org/3/library/urllib.request.html#basehandler-objects)
    * [HTTPRedirectHandler Objects](https://docs.python.org/3/library/urllib.request.html#httpredirecthandler-objects)
    * [HTTPCookieProcessor Objects](https://docs.python.org/3/library/urllib.request.html#httpcookieprocessor-objects)
    * [ProxyHandler Objects](https://docs.python.org/3/library/urllib.request.html#proxyhandler-objects)
    * [HTTPPasswordMgr Objects](https://docs.python.org/3/library/urllib.request.html#httppasswordmgr-objects)
    * [HTTPPasswordMgrWithPriorAuth Objects](https://docs.python.org/3/library/urllib.request.html#httppasswordmgrwithpriorauth-objects)
    * [AbstractBasicAuthHandler Objects](https://docs.python.org/3/library/urllib.request.html#abstractbasicauthhandler-objects)
    * [HTTPBasicAuthHandler Objects](https://docs.python.org/3/library/urllib.request.html#httpbasicauthhandler-objects)
    * [ProxyBasicAuthHandler Objects](https://docs.python.org/3/library/urllib.request.html#proxybasicauthhandler-objects)
    * [AbstractDigestAuthHandler Objects](https://docs.python.org/3/library/urllib.request.html#abstractdigestauthhandler-objects)
    * [HTTPDigestAuthHandler Objects](https://docs.python.org/3/library/urllib.request.html#httpdigestauthhandler-objects)
    * [ProxyDigestAuthHandler Objects](https://docs.python.org/3/library/urllib.request.html#proxydigestauthhandler-objects)
    * [HTTPHandler Objects](https://docs.python.org/3/library/urllib.request.html#httphandler-objects)
    * [HTTPSHandler Objects](https://docs.python.org/3/library/urllib.request.html#httpshandler-objects)
    * [FileHandler Objects](https://docs.python.org/3/library/urllib.request.html#filehandler-objects)
    * [DataHandler Objects](https://docs.python.org/3/library/urllib.request.html#datahandler-objects)
    * [FTPHandler Objects](https://docs.python.org/3/library/urllib.request.html#ftphandler-objects)
    * [CacheFTPHandler Objects](https://docs.python.org/3/library/urllib.request.html#cacheftphandler-objects)
    * [UnknownHandler Objects](https://docs.python.org/3/library/urllib.request.html#unknownhandler-objects)
    * [HTTPErrorProcessor Objects](https://docs.python.org/3/library/urllib.request.html#httperrorprocessor-objects)
    * [Examples](https://docs.python.org/3/library/urllib.request.html#examples)
    * [Legacy interface](https://docs.python.org/3/library/urllib.request.html#legacy-interface)
    * [`urllib.request` Restrictions](https://docs.python.org/3/library/urllib.request.html#urllib-request-restrictions)
  * [`urllib.response` — Response classes used by urllib](https://docs.python.org/3/library/urllib.request.html#module-urllib.response)


#### Previous topic
[`urllib` — URL handling modules](https://docs.python.org/3/library/urllib.html "previous chapter")
#### Next topic
[`urllib.parse` — Parse URLs into components](https://docs.python.org/3/library/urllib.parse.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=urllib.request+%E2%80%94+Extensible+library+for+opening+URLs&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Furllib.request.html&pagesource=library%2Furllib.request.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/urllib.parse.html "urllib.parse — Parse URLs into components") |
  * [previous](https://docs.python.org/3/library/urllib.html "urllib — URL handling modules") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Internet Protocols and Support](https://docs.python.org/3/library/internet.html) »
  * [`urllib.request` — Extensible library for opening URLs](https://docs.python.org/3/library/urllib.request.html)
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
