## Examples[¶](https://docs.python.org/3/library/urllib.request.html#examples "Link to this heading")
In addition to the examples below, more examples are given in [HOWTO Fetch Internet Resources Using The urllib Package](https://docs.python.org/3/howto/urllib2.html#urllib-howto).
This example gets the python.org main page and displays the first 300 bytes of it:
Copy```
>>> import urllib.request
>>> with urllib.request.urlopen('http://www.python.org/') as f:
...     print(f.read(300))
...
b'<!doctype html>\n<!--[if lt IE 7]>   <html class="no-js ie6 lt-ie7 lt-ie8 lt-ie9">   <![endif]-->\n<!--[if IE 7]>      <html class="no-js ie7 lt-ie8 lt-ie9">          <![endif]-->\n<!--[if IE 8]>      <html class="no-js ie8 lt-ie9">

```

Note that urlopen returns a bytes object. This is because there is no way for urlopen to automatically determine the encoding of the byte stream it receives from the HTTP server. In general, a program will decode the returned bytes object to string once it determines or guesses the appropriate encoding.
The following HTML spec document,
For additional information, see the W3C document:
As the python.org website uses _utf-8_ encoding as specified in its meta tag, we will use the same for decoding the bytes object:
Copy```
>>> with urllib.request.urlopen('http://www.python.org/') as f:
...     print(f.read(100).decode('utf-8'))
...
<!doctype html>
<!--[if lt IE 7]>   <html class="no-js ie6 lt-ie7 lt-ie8 lt-ie9">   <![endif]-->
<!-

```

It is also possible to achieve the same result without using the [context manager](https://docs.python.org/3/glossary.html#term-context-manager) approach:
Copy```
>>> import urllib.request
>>> f = urllib.request.urlopen('http://www.python.org/')
>>> try:
...     print(f.read(100).decode('utf-8'))
... finally:
...     f.close()
...
<!doctype html>
<!--[if lt IE 7]>   <html class="no-js ie6 lt-ie7 lt-ie8 lt-ie9">   <![endif]-->
<!--

```

In the following example, we are sending a data-stream to the stdin of a CGI and reading the data it returns to us. Note that this example will only work when the Python installation supports SSL.
Copy```
>>> import urllib.request
>>> req = urllib.request.Request(url='https://localhost/cgi-bin/test.cgi',
...                       data=b'This data is passed to stdin of the CGI')
>>> with urllib.request.urlopen(req) as f:
...     print(f.read().decode('utf-8'))
...
Got Data: "This data is passed to stdin of the CGI"

```

The code for the sample CGI used in the above example is:
Copy```
#!/usr/bin/env python
import sys
data = sys.stdin.read()
print('Content-type: text/plain\n\nGot Data: "%s"' % data)

```

Here is an example of doing a `PUT` request using [`Request`](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request "urllib.request.Request"):
Copy```
import urllib.request
DATA = b'some data'
req = urllib.request.Request(url='http://localhost:8080', data=DATA, method='PUT')
with urllib.request.urlopen(req) as f:
    pass
print(f.status)
print(f.reason)

```

Use of Basic HTTP Authentication:
Copy```
import urllib.request
