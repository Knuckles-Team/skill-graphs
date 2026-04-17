# Customize the default User-Agent header value:
req.add_header('User-Agent', 'urllib-example/0.1 (Contact: . . .)')
with urllib.request.urlopen(req) as f:
    print(f.read().decode('utf-8'))

```

[`OpenerDirector`](https://docs.python.org/3/library/urllib.request.html#urllib.request.OpenerDirector "urllib.request.OpenerDirector") automatically adds a _User-Agent_ header to every [`Request`](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request "urllib.request.Request"). To change this:
Copy```
import urllib.request
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
with opener.open('http://www.example.com/') as f:
   print(f.read().decode('utf-8'))

```

Also, remember that a few standard headers (_Content-Length_ , _Content-Type_ and _Host_) are added when the [`Request`](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request "urllib.request.Request") is passed to [`urlopen()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen "urllib.request.urlopen") (or [`OpenerDirector.open()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.OpenerDirector.open "urllib.request.OpenerDirector.open")).
Here is an example session that uses the `GET` method to retrieve a URL containing parameters:
Copy```
>>> import urllib.request
>>> import urllib.parse
>>> params = urllib.parse.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
>>> url = "http://www.musi-cal.com/cgi-bin/query?%s" % params
>>> with urllib.request.urlopen(url) as f:
...     print(f.read().decode('utf-8'))
...

```

The following example uses the `POST` method instead. Note that params output from urlencode is encoded to bytes before it is sent to urlopen as data:
Copy```
>>> import urllib.request
>>> import urllib.parse
>>> data = urllib.parse.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
>>> data = data.encode('ascii')
>>> with urllib.request.urlopen("http://requestb.in/xrbl82xr", data) as f:
...     print(f.read().decode('utf-8'))
...

```

The following example uses an explicitly specified HTTP proxy, overriding environment settings:
Copy```
>>> import urllib.request
>>> proxies = {'http': 'http://proxy.example.com:8080/'}
>>> opener = urllib.request.build_opener(urllib.request.ProxyHandler(proxies))
>>> with opener.open("http://www.python.org") as f:
...     f.read().decode('utf-8')
...

```

The following example uses no proxies at all, overriding environment settings:
Copy```
>>> import urllib.request
>>> opener = urllib.request.build_opener(urllib.request.ProxyHandler({}}))
>>> with opener.open("http://www.python.org/") as f:
...     f.read().decode('utf-8')
...

```
