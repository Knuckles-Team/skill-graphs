## HTTPPasswordMgr Objects[¶](https://docs.python.org/3/library/urllib.request.html#httppasswordmgr-objects "Link to this heading")
These methods are available on [`HTTPPasswordMgr`](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPPasswordMgr "urllib.request.HTTPPasswordMgr") and [`HTTPPasswordMgrWithDefaultRealm`](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPPasswordMgrWithDefaultRealm "urllib.request.HTTPPasswordMgrWithDefaultRealm") objects.

HTTPPasswordMgr.add_password(_realm_ , _uri_ , _user_ , _passwd_)[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPPasswordMgr.add_password "Link to this definition")

_uri_ can be either a single URI, or a sequence of URIs. _realm_ , _user_ and _passwd_ must be strings. This causes `(user, passwd)` to be used as authentication tokens when authentication for _realm_ and a super-URI of any of the given URIs is given.

HTTPPasswordMgr.find_user_password(_realm_ , _authuri_)[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPPasswordMgr.find_user_password "Link to this definition")

Get user/password for given realm and URI, if any. This method will return `(None, None)` if there is no matching user/password.
For [`HTTPPasswordMgrWithDefaultRealm`](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPPasswordMgrWithDefaultRealm "urllib.request.HTTPPasswordMgrWithDefaultRealm") objects, the realm `None` will be searched if the given _realm_ has no matching user/password.
