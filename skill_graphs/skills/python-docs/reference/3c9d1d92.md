## ProxyHandler Objects[¶](https://docs.python.org/3/library/urllib.request.html#proxyhandler-objects "Link to this heading")

ProxyHandler.<protocol>_open(request)

The [`ProxyHandler`](https://docs.python.org/3/library/urllib.request.html#urllib.request.ProxyHandler "urllib.request.ProxyHandler") will have a method `<protocol>_open()` for every _protocol_ which has a proxy in the _proxies_ dictionary given in the constructor. The method will modify requests to go through the proxy, by calling `request.set_proxy()`, and call the next handler in the chain to actually execute the protocol.
