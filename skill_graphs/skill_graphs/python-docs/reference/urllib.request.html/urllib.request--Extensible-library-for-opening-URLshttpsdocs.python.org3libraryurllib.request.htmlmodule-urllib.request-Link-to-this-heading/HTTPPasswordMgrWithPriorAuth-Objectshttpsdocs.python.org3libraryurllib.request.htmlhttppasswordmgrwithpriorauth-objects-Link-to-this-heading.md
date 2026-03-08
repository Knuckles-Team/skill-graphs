## HTTPPasswordMgrWithPriorAuth Objects[¶](https://docs.python.org/3/library/urllib.request.html#httppasswordmgrwithpriorauth-objects "Link to this heading")
This password manager extends [`HTTPPasswordMgrWithDefaultRealm`](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPPasswordMgrWithDefaultRealm "urllib.request.HTTPPasswordMgrWithDefaultRealm") to support tracking URIs for which authentication credentials should always be sent.

HTTPPasswordMgrWithPriorAuth.add_password(_realm_ , _uri_ , _user_ , _passwd_ , _is_authenticated =False_)[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPPasswordMgrWithPriorAuth.add_password "Link to this definition")

_realm_ , _uri_ , _user_ , _passwd_ are as for [`HTTPPasswordMgr.add_password()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPPasswordMgr.add_password "urllib.request.HTTPPasswordMgr.add_password"). _is_authenticated_ sets the initial value of the `is_authenticated` flag for the given URI or list of URIs. If _is_authenticated_ is specified as `True`, _realm_ is ignored.

HTTPPasswordMgrWithPriorAuth.find_user_password(_realm_ , _authuri_)[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPPasswordMgrWithPriorAuth.find_user_password "Link to this definition")

Same as for [`HTTPPasswordMgrWithDefaultRealm`](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPPasswordMgrWithDefaultRealm "urllib.request.HTTPPasswordMgrWithDefaultRealm") objects

HTTPPasswordMgrWithPriorAuth.update_authenticated(_self_ , _uri_ , _is_authenticated =False_)[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPPasswordMgrWithPriorAuth.update_authenticated "Link to this definition")

Update the `is_authenticated` flag for the given _uri_ or list of URIs.

HTTPPasswordMgrWithPriorAuth.is_authenticated(_self_ , _authuri_)[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPPasswordMgrWithPriorAuth.is_authenticated "Link to this definition")

Returns the current state of the `is_authenticated` flag for the given URI.
