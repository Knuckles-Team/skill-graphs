## Using sessions out of views[¶](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#using-sessions-out-of-views "Link to this heading")
Note
The examples in this section import the `SessionStore` object directly from the `django.contrib.sessions.backends.db` backend. In your own code, you should consider importing `SessionStore` from the session engine designated by [`SESSION_ENGINE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SESSION_ENGINE), as below:
```
>>> from importlib import import_module
>>> from django.conf import settings
>>> SessionStore = import_module(settings.SESSION_ENGINE).SessionStore

```

An API is available to manipulate session data outside of a view:
```
>>> from django.contrib.sessions.backends.db import SessionStore
>>> s = SessionStore()
>>> # stored as seconds since epoch since datetimes are not serializable in JSON.
>>> s["last_login"] = 1376587691
>>> s.create()
>>> s.session_key
'2b1189a188b44ad18c35e113ac6ceead'
>>> s = SessionStore(session_key="2b1189a188b44ad18c35e113ac6ceead")
>>> s["last_login"]
1376587691

```

`SessionStore.create()` is designed to create a new session (i.e. one not loaded from the session store and with `session_key=None`). `save()` is designed to save an existing session (i.e. one loaded from the session store). Calling `save()` on a new session may also work but has a small chance of generating a `session_key` that collides with an existing one. `create()` calls `save()` and loops until an unused `session_key` is generated.
If you’re using the `django.contrib.sessions.backends.db` backend, each session is a normal Django model. The `Session` model is defined in
```
>>> from django.contrib.sessions.models import Session
>>> s = Session.objects.get(pk="2b1189a188b44ad18c35e113ac6ceead")
>>> s.expire_date
datetime.datetime(2005, 8, 20, 13, 35, 12)

```

Note that you’ll need to call [`get_decoded()`](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#django.contrib.sessions.base_session.AbstractBaseSession.get_decoded "django.contrib.sessions.base_session.AbstractBaseSession.get_decoded") to get the session dictionary. This is necessary because the dictionary is stored in an encoded format:
```
>>> s.session_data
'KGRwMQpTJ19hdXRoX3VzZXJfaWQnCnAyCkkxCnMuMTExY2ZjODI2Yj...'
>>> s.get_decoded()
{'user_id': 42}

```
