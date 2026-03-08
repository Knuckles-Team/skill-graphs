## When sessions are saved[¶](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#when-sessions-are-saved "Link to this heading")
By default, Django only saves to the session database when the session has been modified – that is if any of its dictionary values have been assigned or deleted:
```
# Session is modified.
request.session["foo"] = "bar"

# Session is modified.
del request.session["foo"]

# Session is modified.
request.session["foo"] = {}

# Gotcha: Session is NOT modified, because this alters
# request.session['foo'] instead of request.session.
request.session["foo"]["bar"] = "baz"

```

In the last case of the above example, we can tell the session object explicitly that it has been modified by setting the `modified` attribute on the session object:
```
request.session.modified = True

```

To change this default behavior, set the [`SESSION_SAVE_EVERY_REQUEST`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SESSION_SAVE_EVERY_REQUEST) setting to `True`. When set to `True`, Django will save the session to the database on every single request.
Note that the session cookie is only sent when a session has been created or modified. If [`SESSION_SAVE_EVERY_REQUEST`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SESSION_SAVE_EVERY_REQUEST) is `True`, the session cookie will be sent on every request.
Similarly, the `expires` part of a session cookie is updated each time the session cookie is sent.
The session is not saved if the response’s status code is 500.
