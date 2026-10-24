[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`http` — HTTP modules](https://docs.python.org/3/library/http.html)
    * [HTTP status codes](https://docs.python.org/3/library/http.html#http-status-codes)
    * [HTTP status category](https://docs.python.org/3/library/http.html#http-status-category)
    * [HTTP methods](https://docs.python.org/3/library/http.html#http-methods)


#### Previous topic
[`urllib.robotparser` — Parser for robots.txt](https://docs.python.org/3/library/urllib.robotparser.html "previous chapter")
#### Next topic
[`http.client` — HTTP protocol client](https://docs.python.org/3/library/http.client.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=http+%E2%80%94+HTTP+modules&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fhttp.html&pagesource=library%2Fhttp.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/http.client.html "http.client — HTTP protocol client") |
  * [previous](https://docs.python.org/3/library/urllib.robotparser.html "urllib.robotparser — Parser for robots.txt") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Internet Protocols and Support](https://docs.python.org/3/library/internet.html) »
  * [`http` — HTTP modules](https://docs.python.org/3/library/http.html)
  * |
  * Theme  Auto Light Dark |


#  `http` — HTTP modules[¶](https://docs.python.org/3/library/http.html#module-http "Link to this heading")
**Source code:**
* * *
`http` is a package that collects several modules for working with the HyperText Transfer Protocol:
  * [`http.client`](https://docs.python.org/3/library/http.client.html#module-http.client "http.client: HTTP and HTTPS protocol client \(requires sockets\).") is a low-level HTTP protocol client; for high-level URL opening use [`urllib.request`](https://docs.python.org/3/library/urllib.request.html#module-urllib.request "urllib.request: Extensible library for opening URLs.")
  * [`http.server`](https://docs.python.org/3/library/http.server.html#module-http.server "http.server: HTTP server and request handlers.") contains basic HTTP server classes based on [`socketserver`](https://docs.python.org/3/library/socketserver.html#module-socketserver "socketserver: A framework for network servers.")
  * [`http.cookies`](https://docs.python.org/3/library/http.cookies.html#module-http.cookies "http.cookies: Support for HTTP state management \(cookies\).") has utilities for implementing state management with cookies
  * [`http.cookiejar`](https://docs.python.org/3/library/http.cookiejar.html#module-http.cookiejar "http.cookiejar: Classes for automatic handling of HTTP cookies.") provides persistence of cookies


The `http` module also defines the following enums that help you work with http related code:

_class_ http.HTTPStatus[¶](https://docs.python.org/3/library/http.html#http.HTTPStatus "Link to this definition")

Added in version 3.5.
A subclass of [`enum.IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "enum.IntEnum") that defines a set of HTTP status codes, reason phrases and long descriptions written in English.
Usage:
Copy```
>>> from http import HTTPStatus
>>> HTTPStatus.OK
HTTPStatus.OK
>>> HTTPStatus.OK == 200
True
>>> HTTPStatus.OK.value
200
>>> HTTPStatus.OK.phrase
'OK'
>>> HTTPStatus.OK.description
'Request fulfilled, document follows'
>>> list(HTTPStatus)
[HTTPStatus.CONTINUE, HTTPStatus.SWITCHING_PROTOCOLS, ...]

```

## HTTP status codes[¶](https://docs.python.org/3/library/http.html#http-status-codes "Link to this heading")
Supported, [`http.HTTPStatus`](https://docs.python.org/3/library/http.html#http.HTTPStatus "http.HTTPStatus") are:
Code | Enum Name | Details
---|---|---
`100` | `CONTINUE` | HTTP Semantics
`101` | `SWITCHING_PROTOCOLS` | HTTP Semantics
`102` | `PROCESSING` | WebDAV
`103` | `EARLY_HINTS` | An HTTP Status Code for Indicating Hints
`200` | `OK` | HTTP Semantics
`201` | `CREATED` | HTTP Semantics
`202` | `ACCEPTED` | HTTP Semantics
`203` | `NON_AUTHORITATIVE_INFORMATION` | HTTP Semantics
`204` | `NO_CONTENT` | HTTP Semantics
`205` | `RESET_CONTENT` | HTTP Semantics
`206` | `PARTIAL_CONTENT` | HTTP Semantics
`207` | `MULTI_STATUS` | WebDAV
`208` | `ALREADY_REPORTED` | WebDAV Binding Extensions
`226` | `IM_USED` | Delta Encoding in HTTP
`300` | `MULTIPLE_CHOICES` | HTTP Semantics
`301` | `MOVED_PERMANENTLY` | HTTP Semantics
`302` | `FOUND` | HTTP Semantics
`303` | `SEE_OTHER` | HTTP Semantics
`304` | `NOT_MODIFIED` | HTTP Semantics
`305` | `USE_PROXY` | HTTP Semantics
`307` | `TEMPORARY_REDIRECT` | HTTP Semantics
`308` | `PERMANENT_REDIRECT` | HTTP Semantics
`400` | `BAD_REQUEST` | HTTP Semantics
`401` | `UNAUTHORIZED` | HTTP Semantics
`402` | `PAYMENT_REQUIRED` | HTTP Semantics
`403` | `FORBIDDEN` | HTTP Semantics
`404` | `NOT_FOUND` | HTTP Semantics
`405` | `METHOD_NOT_ALLOWED` | HTTP Semantics
`406` | `NOT_ACCEPTABLE` | HTTP Semantics
`407` | `PROXY_AUTHENTICATION_REQUIRED` | HTTP Semantics
`408` | `REQUEST_TIMEOUT` | HTTP Semantics
`409` | `CONFLICT` | HTTP Semantics
`410` | `GONE` | HTTP Semantics
`411` | `LENGTH_REQUIRED` | HTTP Semantics
`412` | `PRECONDITION_FAILED` | HTTP Semantics
`413` | `CONTENT_TOO_LARGE` | HTTP Semantics
`414` | `URI_TOO_LONG` | HTTP Semantics
`415` | `UNSUPPORTED_MEDIA_TYPE` | HTTP Semantics
`416` | `RANGE_NOT_SATISFIABLE` | HTTP Semantics
`417` | `EXPECTATION_FAILED` | HTTP Semantics
`418` | `IM_A_TEAPOT` | HTCPCP/1.0
`421` | `MISDIRECTED_REQUEST` | HTTP Semantics
`422` | `UNPROCESSABLE_CONTENT` | HTTP Semantics
`423` | `LOCKED` | WebDAV
`424` | `FAILED_DEPENDENCY` | WebDAV
`425` | `TOO_EARLY` | Using Early Data in HTTP
`426` | `UPGRADE_REQUIRED` | HTTP Semantics
`428` | `PRECONDITION_REQUIRED` | Additional HTTP Status Codes
`429` | `TOO_MANY_REQUESTS` | Additional HTTP Status Codes
`431` | `REQUEST_HEADER_FIELDS_TOO_LARGE` | Additional HTTP Status Codes
`451` | `UNAVAILABLE_FOR_LEGAL_REASONS` | An HTTP Status Code to Report Legal Obstacles
`500` | `INTERNAL_SERVER_ERROR` | HTTP Semantics
`501` | `NOT_IMPLEMENTED` | HTTP Semantics
`502` | `BAD_GATEWAY` | HTTP Semantics
`503` | `SERVICE_UNAVAILABLE` | HTTP Semantics
`504` | `GATEWAY_TIMEOUT` | HTTP Semantics
`505` | `HTTP_VERSION_NOT_SUPPORTED` | HTTP Semantics
`506` | `VARIANT_ALSO_NEGOTIATES` | Transparent Content Negotiation in HTTP
`507` | `INSUFFICIENT_STORAGE` | WebDAV
`508` | `LOOP_DETECTED` | WebDAV Binding Extensions
`510` | `NOT_EXTENDED` | An HTTP Extension Framework
`511` | `NETWORK_AUTHENTICATION_REQUIRED` | Additional HTTP Status Codes
In order to preserve backwards compatibility, enum values are also present in the [`http.client`](https://docs.python.org/3/library/http.client.html#module-http.client "http.client: HTTP and HTTPS protocol client \(requires sockets\).") module in the form of constants. The enum name is equal to the constant name (i.e. `http.HTTPStatus.OK` is also available as `http.client.OK`).
Changed in version 3.7: Added `421 MISDIRECTED_REQUEST` status code.
Added in version 3.8: Added `451 UNAVAILABLE_FOR_LEGAL_REASONS` status code.
Added in version 3.9: Added `103 EARLY_HINTS`, `418 IM_A_TEAPOT` and `425 TOO_EARLY` status codes.
Changed in version 3.13: Implemented RFC9110 naming for status constants. Old constant names are preserved for backwards compatibility: `413 REQUEST_ENTITY_TOO_LARGE`, `414 REQUEST_URI_TOO_LONG`, `416 REQUESTED_RANGE_NOT_SATISFIABLE` and `422 UNPROCESSABLE_ENTITY`.
## HTTP status category[¶](https://docs.python.org/3/library/http.html#http-status-category "Link to this heading")
Added in version 3.12.
The enum values have several properties to indicate the HTTP status category:
Property | Indicates that | Details
---|---|---
`is_informational` | `100 <= status <= 199` | HTTP Semantics
`is_success` | `200 <= status <= 299` | HTTP Semantics
`is_redirection` | `300 <= status <= 399` | HTTP Semantics
`is_client_error` | `400 <= status <= 499` | HTTP Semantics
`is_server_error` | `500 <= status <= 599` | HTTP Semantics
> Usage:
> Copy```
>>> from http import HTTPStatus
>>> HTTPStatus.OK.is_success
True
>>> HTTPStatus.OK.is_client_error
False

```


_class_ http.HTTPMethod[¶](https://docs.python.org/3/library/http.html#http.HTTPMethod "Link to this definition")

Added in version 3.11.
A subclass of [`enum.StrEnum`](https://docs.python.org/3/library/enum.html#enum.StrEnum "enum.StrEnum") that defines a set of HTTP methods and descriptions written in English.
Usage:
Copy```
>>> from http import HTTPMethod
>>>
>>> HTTPMethod.GET
<HTTPMethod.GET>
>>> HTTPMethod.GET == 'GET'
True
>>> HTTPMethod.GET.value
'GET'
>>> HTTPMethod.GET.description
'Retrieve the target.'
>>> list(HTTPMethod)
[<HTTPMethod.CONNECT>,
 <HTTPMethod.DELETE>,
 <HTTPMethod.GET>,
 <HTTPMethod.HEAD>,
 <HTTPMethod.OPTIONS>,
 <HTTPMethod.PATCH>,
 <HTTPMethod.POST>,
 <HTTPMethod.PUT>,
 <HTTPMethod.TRACE>]

```

## HTTP methods[¶](https://docs.python.org/3/library/http.html#http-methods "Link to this heading")
Supported, [`http.HTTPMethod`](https://docs.python.org/3/library/http.html#http.HTTPMethod "http.HTTPMethod") are:
Method | Enum Name | Details
---|---|---
`GET` | `GET` | HTTP Semantics
`HEAD` | `HEAD` | HTTP Semantics
`POST` | `POST` | HTTP Semantics
`PUT` | `PUT` | HTTP Semantics
`DELETE` | `DELETE` | HTTP Semantics
`CONNECT` | `CONNECT` | HTTP Semantics
`OPTIONS` | `OPTIONS` | HTTP Semantics
`TRACE` | `TRACE` | HTTP Semantics
`PATCH` | `PATCH` | HTTP/1.1
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`http` — HTTP modules](https://docs.python.org/3/library/http.html)
    * [HTTP status codes](https://docs.python.org/3/library/http.html#http-status-codes)
    * [HTTP status category](https://docs.python.org/3/library/http.html#http-status-category)
    * [HTTP methods](https://docs.python.org/3/library/http.html#http-methods)


#### Previous topic
[`urllib.robotparser` — Parser for robots.txt](https://docs.python.org/3/library/urllib.robotparser.html "previous chapter")
#### Next topic
[`http.client` — HTTP protocol client](https://docs.python.org/3/library/http.client.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=http+%E2%80%94+HTTP+modules&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fhttp.html&pagesource=library%2Fhttp.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/http.client.html "http.client — HTTP protocol client") |
  * [previous](https://docs.python.org/3/library/urllib.robotparser.html "urllib.robotparser — Parser for robots.txt") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Internet Protocols and Support](https://docs.python.org/3/library/internet.html) »
  * [`http` — HTTP modules](https://docs.python.org/3/library/http.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
