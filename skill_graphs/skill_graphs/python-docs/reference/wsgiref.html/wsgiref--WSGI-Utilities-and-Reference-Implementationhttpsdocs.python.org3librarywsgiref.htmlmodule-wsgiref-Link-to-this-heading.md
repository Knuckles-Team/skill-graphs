#  `wsgiref` — WSGI Utilities and Reference Implementation[¶](https://docs.python.org/3/library/wsgiref.html#module-wsgiref "Link to this heading")
**Source code:**
* * *
Warning
`wsgiref` is a reference implementation and is not recommended for production. The module only implements basic security checks.
The Web Server Gateway Interface (WSGI) is a standard interface between web server software and web applications written in Python. Having a standard interface makes it easy to use an application that supports WSGI with a number of different web servers.
Only authors of web servers and programming frameworks need to know every detail and corner case of the WSGI design. You don’t need to understand every detail of WSGI just to install a WSGI application or to write a web application using an existing framework.
`wsgiref` is a reference implementation of the WSGI specification that can be used to add WSGI support to a web server or framework. It provides utilities for manipulating WSGI environment variables and response headers, base classes for implementing WSGI servers, a demo HTTP server that serves WSGI applications, types for static type checking, and a validation tool that checks WSGI servers and applications for conformance to the WSGI specification ([**PEP 3333**](https://peps.python.org/pep-3333/)).
See
##  `wsgiref.util` – WSGI environment utilities[¶](https://docs.python.org/3/library/wsgiref.html#module-wsgiref.util "Link to this heading")
This module provides a variety of utility functions for working with WSGI environments. A WSGI environment is a dictionary containing HTTP request variables as described in [**PEP 3333**](https://peps.python.org/pep-3333/). All of the functions taking an _environ_ parameter expect a WSGI-compliant dictionary to be supplied; please see [**PEP 3333**](https://peps.python.org/pep-3333/) for a detailed specification and [`WSGIEnvironment`](https://docs.python.org/3/library/wsgiref.html#wsgiref.types.WSGIEnvironment "wsgiref.types.WSGIEnvironment") for a type alias that can be used in type annotations.

wsgiref.util.guess_scheme(_environ_)[¶](https://docs.python.org/3/library/wsgiref.html#wsgiref.util.guess_scheme "Link to this definition")

Return a guess for whether `wsgi.url_scheme` should be “http” or “https”, by checking for a `HTTPS` environment variable in the _environ_ dictionary. The return value is a string.
This function is useful when creating a gateway that wraps CGI or a CGI-like protocol such as FastCGI. Typically, servers providing such protocols will include a `HTTPS` variable with a value of “1”, “yes”, or “on” when a request is received via SSL. So, this function returns “https” if such a value is found, and “http” otherwise.

wsgiref.util.request_uri(_environ_ , _include_query =True_)[¶](https://docs.python.org/3/library/wsgiref.html#wsgiref.util.request_uri "Link to this definition")

Return the full request URI, optionally including the query string, using the algorithm found in the “URL Reconstruction” section of [**PEP 3333**](https://peps.python.org/pep-3333/). If _include_query_ is false, the query string is not included in the resulting URI.

wsgiref.util.application_uri(_environ_)[¶](https://docs.python.org/3/library/wsgiref.html#wsgiref.util.application_uri "Link to this definition")

Similar to [`request_uri()`](https://docs.python.org/3/library/wsgiref.html#wsgiref.util.request_uri "wsgiref.util.request_uri"), except that the `PATH_INFO` and `QUERY_STRING` variables are ignored. The result is the base URI of the application object addressed by the request.

wsgiref.util.shift_path_info(_environ_)[¶](https://docs.python.org/3/library/wsgiref.html#wsgiref.util.shift_path_info "Link to this definition")

Shift a single name from `PATH_INFO` to `SCRIPT_NAME` and return the name. The _environ_ dictionary is _modified_ in-place; use a copy if you need to keep the original `PATH_INFO` or `SCRIPT_NAME` intact.
If there are no remaining path segments in `PATH_INFO`, `None` is returned.
Typically, this routine is used to process each portion of a request URI path, for example to treat the path as a series of dictionary keys. This routine modifies the passed-in environment to make it suitable for invoking another WSGI application that is located at the target URI. For example, if there is a WSGI application at `/foo`, and the request URI path is `/foo/bar/baz`, and the WSGI application at `/foo` calls `shift_path_info()`, it will receive the string “bar”, and the environment will be updated to be suitable for passing to a WSGI application at `/foo/bar`. That is, `SCRIPT_NAME` will change from `/foo` to `/foo/bar`, and `PATH_INFO` will change from `/bar/baz` to `/baz`.
When `PATH_INFO` is just a “/”, this routine returns an empty string and appends a trailing slash to `SCRIPT_NAME`, even though empty path segments are normally ignored, and `SCRIPT_NAME` doesn’t normally end in a slash. This is intentional behavior, to ensure that an application can tell the difference between URIs ending in `/x` from ones ending in `/x/` when using this routine to do object traversal.

wsgiref.util.setup_testing_defaults(_environ_)[¶](https://docs.python.org/3/library/wsgiref.html#wsgiref.util.setup_testing_defaults "Link to this definition")

Update _environ_ with trivial defaults for testing purposes.
This routine adds various parameters required for WSGI, including `HTTP_HOST`, `SERVER_NAME`, `SERVER_PORT`, `REQUEST_METHOD`, `SCRIPT_NAME`, `PATH_INFO`, and all of the [**PEP 3333**](https://peps.python.org/pep-3333/)-defined `wsgi.*` variables. It only supplies default values, and does not replace any existing settings for these variables.
This routine is intended to make it easier for unit tests of WSGI servers and applications to set up dummy environments. It should NOT be used by actual WSGI servers or applications, since the data is fake!
Example usage (see also [`demo_app()`](https://docs.python.org/3/library/wsgiref.html#wsgiref.simple_server.demo_app "wsgiref.simple_server.demo_app") for another example):
Copy```
from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server
