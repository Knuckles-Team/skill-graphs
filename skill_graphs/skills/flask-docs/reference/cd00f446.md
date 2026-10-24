## Sessions[¶](https://flask.palletsprojects.com/en/stable/api/#sessions "Link to this heading")
If you have set [`Flask.secret_key`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.secret_key "flask.Flask.secret_key") (or configured it from [`SECRET_KEY`](https://flask.palletsprojects.com/en/stable/config/#SECRET_KEY "SECRET_KEY")) you can use sessions in Flask applications. A session makes it possible to remember information from one request to another. The way Flask does this is by using a signed cookie. The user can look at the session contents, but can’t modify it unless they know the secret key, so make sure to set that to something complex and unguessable.
To access the current session you can use the [`session`](https://flask.palletsprojects.com/en/stable/api/#flask.session "flask.session") object:

_class_ flask.session[¶](https://flask.palletsprojects.com/en/stable/api/#flask.session "Link to this definition")

The session object works pretty much like an ordinary dict, with the difference that it keeps track of modifications.
This is a proxy. See [Notes On Proxies](https://flask.palletsprojects.com/en/stable/reqcontext/#notes-on-proxies) for more information.
The following attributes are interesting:

new[¶](https://flask.palletsprojects.com/en/stable/api/#flask.session.new "Link to this definition")

`True` if the session is new, `False` otherwise.

modified[¶](https://flask.palletsprojects.com/en/stable/api/#flask.session.modified "Link to this definition")

`True` if the session object detected a modification. Be advised that modifications on mutable structures are not picked up automatically, in that situation you have to explicitly set the attribute to `True` yourself. Here an example:
```
# this change is not picked up because a mutable object (here
# a list) is changed.
session['objects'].append(42)
# so mark it as modified yourself
session.modified = True

```


permanent[¶](https://flask.palletsprojects.com/en/stable/api/#flask.session.permanent "Link to this definition")

If set to `True` the session lives for [`permanent_session_lifetime`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.permanent_session_lifetime "flask.Flask.permanent_session_lifetime") seconds. The default is 31 days. If set to `False` (which is the default) the session will be deleted when the user closes the browser.
