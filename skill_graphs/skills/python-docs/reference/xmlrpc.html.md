[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`http.cookiejar` — Cookie handling for HTTP clients](https://docs.python.org/3/library/http.cookiejar.html "previous chapter")
#### Next topic
[`xmlrpc.client` — XML-RPC client access](https://docs.python.org/3/library/xmlrpc.client.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=xmlrpc+%E2%80%94+XMLRPC+server+and+client+modules&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fxmlrpc.html&pagesource=library%2Fxmlrpc.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/xmlrpc.client.html "xmlrpc.client — XML-RPC client access") |
  * [previous](https://docs.python.org/3/library/http.cookiejar.html "http.cookiejar — Cookie handling for HTTP clients") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Internet Protocols and Support](https://docs.python.org/3/library/internet.html) »
  * [`xmlrpc` — XMLRPC server and client modules](https://docs.python.org/3/library/xmlrpc.html)
  * |
  * Theme  Auto Light Dark |


#  `xmlrpc` — XMLRPC server and client modules[¶](https://docs.python.org/3/library/xmlrpc.html#module-xmlrpc "Link to this heading")
XML-RPC is a Remote Procedure Call method that uses XML passed via HTTP as a transport. With it, a client can call methods with parameters on a remote server (the server is named by a URI) and get back structured data.
`xmlrpc` is a package that collects server and client modules implementing XML-RPC. The modules are:
  * [`xmlrpc.client`](https://docs.python.org/3/library/xmlrpc.client.html#module-xmlrpc.client "xmlrpc.client: XML-RPC client access.")
  * [`xmlrpc.server`](https://docs.python.org/3/library/xmlrpc.server.html#module-xmlrpc.server "xmlrpc.server: Basic XML-RPC server implementations.")


#### Previous topic
[`http.cookiejar` — Cookie handling for HTTP clients](https://docs.python.org/3/library/http.cookiejar.html "previous chapter")
#### Next topic
[`xmlrpc.client` — XML-RPC client access](https://docs.python.org/3/library/xmlrpc.client.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=xmlrpc+%E2%80%94+XMLRPC+server+and+client+modules&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fxmlrpc.html&pagesource=library%2Fxmlrpc.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/xmlrpc.client.html "xmlrpc.client — XML-RPC client access") |
  * [previous](https://docs.python.org/3/library/http.cookiejar.html "http.cookiejar — Cookie handling for HTTP clients") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Internet Protocols and Support](https://docs.python.org/3/library/internet.html) »
  * [`xmlrpc` — XMLRPC server and client modules](https://docs.python.org/3/library/xmlrpc.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
