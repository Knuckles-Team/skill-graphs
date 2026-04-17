[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`xml.parsers.expat` — Fast XML parsing using Expat](https://docs.python.org/3/library/pyexpat.html "previous chapter")
#### Next topic
[`webbrowser` — Convenient web-browser controller](https://docs.python.org/3/library/webbrowser.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Internet+Protocols+and+Support&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Finternet.html&pagesource=library%2Finternet.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/webbrowser.html "webbrowser — Convenient web-browser controller") |
  * [previous](https://docs.python.org/3/library/pyexpat.html "xml.parsers.expat — Fast XML parsing using Expat") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Internet Protocols and Support](https://docs.python.org/3/library/internet.html)
  * |
  * Theme  Auto Light Dark |


# Internet Protocols and Support[¶](https://docs.python.org/3/library/internet.html#internet-protocols-and-support "Link to this heading")
[`socket`](https://docs.python.org/3/library/socket.html#module-socket "socket: Low-level networking interface."), which is currently supported on most popular platforms. Here is an overview:
  * [`webbrowser` — Convenient web-browser controller](https://docs.python.org/3/library/webbrowser.html)
    * [Command-line interface](https://docs.python.org/3/library/webbrowser.html#command-line-interface)
    * [Browser controller objects](https://docs.python.org/3/library/webbrowser.html#browser-controller-objects)
  * [`wsgiref` — WSGI Utilities and Reference Implementation](https://docs.python.org/3/library/wsgiref.html)
    * [`wsgiref.util` – WSGI environment utilities](https://docs.python.org/3/library/wsgiref.html#module-wsgiref.util)
    * [`wsgiref.headers` – WSGI response header tools](https://docs.python.org/3/library/wsgiref.html#module-wsgiref.headers)
    * [`wsgiref.simple_server` – a simple WSGI HTTP server](https://docs.python.org/3/library/wsgiref.html#module-wsgiref.simple_server)
    * [`wsgiref.validate` — WSGI conformance checker](https://docs.python.org/3/library/wsgiref.html#module-wsgiref.validate)
    * [`wsgiref.handlers` – server/gateway base classes](https://docs.python.org/3/library/wsgiref.html#module-wsgiref.handlers)
    * [`wsgiref.types` – WSGI types for static type checking](https://docs.python.org/3/library/wsgiref.html#module-wsgiref.types)
    * [Examples](https://docs.python.org/3/library/wsgiref.html#examples)
  * [`urllib` — URL handling modules](https://docs.python.org/3/library/urllib.html)
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
  * [`urllib.parse` — Parse URLs into components](https://docs.python.org/3/library/urllib.parse.html)
    * [URL Parsing](https://docs.python.org/3/library/urllib.parse.html#url-parsing)
    * [URL parsing security](https://docs.python.org/3/library/urllib.parse.html#url-parsing-security)
    * [Parsing ASCII Encoded Bytes](https://docs.python.org/3/library/urllib.parse.html#parsing-ascii-encoded-bytes)
    * [Structured Parse Results](https://docs.python.org/3/library/urllib.parse.html#structured-parse-results)
    * [URL Quoting](https://docs.python.org/3/library/urllib.parse.html#url-quoting)
  * [`urllib.error` — Exception classes raised by urllib.request](https://docs.python.org/3/library/urllib.error.html)
  * [`urllib.robotparser` — Parser for robots.txt](https://docs.python.org/3/library/urllib.robotparser.html)
  * [`http` — HTTP modules](https://docs.python.org/3/library/http.html)
    * [HTTP status codes](https://docs.python.org/3/library/http.html#http-status-codes)
    * [HTTP status category](https://docs.python.org/3/library/http.html#http-status-category)
    * [HTTP methods](https://docs.python.org/3/library/http.html#http-methods)
  * [`http.client` — HTTP protocol client](https://docs.python.org/3/library/http.client.html)
    * [HTTPConnection Objects](https://docs.python.org/3/library/http.client.html#httpconnection-objects)
    * [HTTPResponse Objects](https://docs.python.org/3/library/http.client.html#httpresponse-objects)
    * [Examples](https://docs.python.org/3/library/http.client.html#examples)
    * [HTTPMessage Objects](https://docs.python.org/3/library/http.client.html#httpmessage-objects)
  * [`ftplib` — FTP protocol client](https://docs.python.org/3/library/ftplib.html)
    * [Reference](https://docs.python.org/3/library/ftplib.html#reference)
      * [FTP objects](https://docs.python.org/3/library/ftplib.html#ftp-objects)
      * [FTP_TLS objects](https://docs.python.org/3/library/ftplib.html#ftp-tls-objects)
      * [Module variables](https://docs.python.org/3/library/ftplib.html#module-variables)
  * [`poplib` — POP3 protocol client](https://docs.python.org/3/library/poplib.html)
    * [POP3 Objects](https://docs.python.org/3/library/poplib.html#pop3-objects)
    * [POP3 Example](https://docs.python.org/3/library/poplib.html#pop3-example)
  * [`imaplib` — IMAP4 protocol client](https://docs.python.org/3/library/imaplib.html)
    * [IMAP4 Objects](https://docs.python.org/3/library/imaplib.html#imap4-objects)
    * [IMAP4 Example](https://docs.python.org/3/library/imaplib.html#imap4-example)
  * [`smtplib` — SMTP protocol client](https://docs.python.org/3/library/smtplib.html)
    * [SMTP Objects](https://docs.python.org/3/library/smtplib.html#smtp-objects)
    * [SMTP Example](https://docs.python.org/3/library/smtplib.html#smtp-example)
  * [`uuid` — UUID objects according to **RFC 9562**](https://docs.python.org/3/library/uuid.html)
    * [Command-Line Usage](https://docs.python.org/3/library/uuid.html#command-line-usage)
    * [Example](https://docs.python.org/3/library/uuid.html#example)
    * [Command-Line Example](https://docs.python.org/3/library/uuid.html#command-line-example)
  * [`socketserver` — A framework for network servers](https://docs.python.org/3/library/socketserver.html)
    * [Server Creation Notes](https://docs.python.org/3/library/socketserver.html#server-creation-notes)
    * [Server Objects](https://docs.python.org/3/library/socketserver.html#server-objects)
    * [Request Handler Objects](https://docs.python.org/3/library/socketserver.html#request-handler-objects)
    * [Examples](https://docs.python.org/3/library/socketserver.html#examples)
      * [`socketserver.TCPServer` Example](https://docs.python.org/3/library/socketserver.html#socketserver-tcpserver-example)
      * [`socketserver.UDPServer` Example](https://docs.python.org/3/library/socketserver.html#socketserver-udpserver-example)
      * [Asynchronous Mixins](https://docs.python.org/3/library/socketserver.html#asynchronous-mixins)
  * [`http.server` — HTTP servers](https://docs.python.org/3/library/http.server.html)
    * [Command-line interface](https://docs.python.org/3/library/http.server.html#command-line-interface)
    * [Security considerations](https://docs.python.org/3/library/http.server.html#security-considerations)
  * [`http.cookies` — HTTP state management](https://docs.python.org/3/library/http.cookies.html)
    * [Cookie Objects](https://docs.python.org/3/library/http.cookies.html#cookie-objects)
    * [Morsel Objects](https://docs.python.org/3/library/http.cookies.html#morsel-objects)
    * [Example](https://docs.python.org/3/library/http.cookies.html#example)
  * [`http.cookiejar` — Cookie handling for HTTP clients](https://docs.python.org/3/library/http.cookiejar.html)
    * [CookieJar and FileCookieJar Objects](https://docs.python.org/3/library/http.cookiejar.html#cookiejar-and-filecookiejar-objects)
    * [FileCookieJar subclasses and co-operation with web browsers](https://docs.python.org/3/library/http.cookiejar.html#filecookiejar-subclasses-and-co-operation-with-web-browsers)
    * [CookiePolicy Objects](https://docs.python.org/3/library/http.cookiejar.html#cookiepolicy-objects)
    * [DefaultCookiePolicy Objects](https://docs.python.org/3/library/http.cookiejar.html#defaultcookiepolicy-objects)
    * [Cookie Objects](https://docs.python.org/3/library/http.cookiejar.html#cookie-objects)
    * [Examples](https://docs.python.org/3/library/http.cookiejar.html#examples)
  * [`xmlrpc` — XMLRPC server and client modules](https://docs.python.org/3/library/xmlrpc.html)
  * [`xmlrpc.client` — XML-RPC client access](https://docs.python.org/3/library/xmlrpc.client.html)
    * [ServerProxy Objects](https://docs.python.org/3/library/xmlrpc.client.html#serverproxy-objects)
    * [DateTime Objects](https://docs.python.org/3/library/xmlrpc.client.html#datetime-objects)
    * [Binary Objects](https://docs.python.org/3/library/xmlrpc.client.html#binary-objects)
    * [Fault Objects](https://docs.python.org/3/library/xmlrpc.client.html#fault-objects)
    * [ProtocolError Objects](https://docs.python.org/3/library/xmlrpc.client.html#protocolerror-objects)
    * [MultiCall Objects](https://docs.python.org/3/library/xmlrpc.client.html#multicall-objects)
    * [Convenience Functions](https://docs.python.org/3/library/xmlrpc.client.html#convenience-functions)
    * [Example of Client Usage](https://docs.python.org/3/library/xmlrpc.client.html#example-of-client-usage)
    * [Example of Client and Server Usage](https://docs.python.org/3/library/xmlrpc.client.html#example-of-client-and-server-usage)
  * [`xmlrpc.server` — Basic XML-RPC servers](https://docs.python.org/3/library/xmlrpc.server.html)
    * [SimpleXMLRPCServer Objects](https://docs.python.org/3/library/xmlrpc.server.html#simplexmlrpcserver-objects)
      * [SimpleXMLRPCServer Example](https://docs.python.org/3/library/xmlrpc.server.html#simplexmlrpcserver-example)
    * [CGIXMLRPCRequestHandler](https://docs.python.org/3/library/xmlrpc.server.html#cgixmlrpcrequesthandler)
    * [Documenting XMLRPC server](https://docs.python.org/3/library/xmlrpc.server.html#documenting-xmlrpc-server)
    * [DocXMLRPCServer Objects](https://docs.python.org/3/library/xmlrpc.server.html#docxmlrpcserver-objects)
    * [DocCGIXMLRPCRequestHandler](https://docs.python.org/3/library/xmlrpc.server.html#doccgixmlrpcrequesthandler)
  * [`ipaddress` — IPv4/IPv6 manipulation library](https://docs.python.org/3/library/ipaddress.html)
    * [Convenience factory functions](https://docs.python.org/3/library/ipaddress.html#convenience-factory-functions)
    * [IP Addresses](https://docs.python.org/3/library/ipaddress.html#ip-addresses)
      * [Address objects](https://docs.python.org/3/library/ipaddress.html#address-objects)
      * [Conversion to Strings and Integers](https://docs.python.org/3/library/ipaddress.html#conversion-to-strings-and-integers)
      * [Operators](https://docs.python.org/3/library/ipaddress.html#operators)
        * [Comparison operators](https://docs.python.org/3/library/ipaddress.html#comparison-operators)
        * [Arithmetic operators](https://docs.python.org/3/library/ipaddress.html#arithmetic-operators)
    * [IP Network definitions](https://docs.python.org/3/library/ipaddress.html#ip-network-definitions)
      * [Prefix, net mask and host mask](https://docs.python.org/3/library/ipaddress.html#prefix-net-mask-and-host-mask)
      * [Network objects](https://docs.python.org/3/library/ipaddress.html#network-objects)
      * [Operators](https://docs.python.org/3/library/ipaddress.html#id1)
        * [Logical operators](https://docs.python.org/3/library/ipaddress.html#logical-operators)
        * [Iteration](https://docs.python.org/3/library/ipaddress.html#iteration)
        * [Networks as containers of addresses](https://docs.python.org/3/library/ipaddress.html#networks-as-containers-of-addresses)
    * [Interface objects](https://docs.python.org/3/library/ipaddress.html#interface-objects)
      * [Operators](https://docs.python.org/3/library/ipaddress.html#id2)
        * [Logical operators](https://docs.python.org/3/library/ipaddress.html#id3)
    * [Other Module Level Functions](https://docs.python.org/3/library/ipaddress.html#other-module-level-functions)
    * [Custom Exceptions](https://docs.python.org/3/library/ipaddress.html#custom-exceptions)


#### Previous topic
[`xml.parsers.expat` — Fast XML parsing using Expat](https://docs.python.org/3/library/pyexpat.html "previous chapter")
#### Next topic
[`webbrowser` — Convenient web-browser controller](https://docs.python.org/3/library/webbrowser.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Internet+Protocols+and+Support&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Finternet.html&pagesource=library%2Finternet.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/webbrowser.html "webbrowser — Convenient web-browser controller") |
  * [previous](https://docs.python.org/3/library/pyexpat.html "xml.parsers.expat — Fast XML parsing using Expat") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Internet Protocols and Support](https://docs.python.org/3/library/internet.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
