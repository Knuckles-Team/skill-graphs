## Technical details[¶](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#technical-details "Link to this heading")
  * The session dictionary accepts any [`JSONSerializer`](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#django.contrib.sessions.serializers.JSONSerializer "django.contrib.sessions.serializers.JSONSerializer").
  * Session data is stored in a database table named `django_session` .
  * Django only sends a cookie if it needs to. If you don’t set any session data, it won’t send a session cookie.


### The `SessionStore` object[¶](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#the-sessionstore-object "Link to this heading")
When working with sessions internally, Django uses a session store object from the corresponding session engine. By convention, the session store object class is named `SessionStore` and is located in the module designated by [`SESSION_ENGINE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SESSION_ENGINE).
All `SessionStore` classes available in Django inherit from [`SessionBase`](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#django.contrib.sessions.backends.base.SessionBase "django.contrib.sessions.backends.base.SessionBase") and implement data manipulation methods, namely:
  * `exists()`
  * `create()`
  * `save()`
  * `delete()`
  * `load()`
  * [`clear_expired()`](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#django.contrib.sessions.backends.base.SessionBase.clear_expired "django.contrib.sessions.backends.base.SessionBase.clear_expired")


In order to build a custom session engine or to customize an existing one, you may create a new class inheriting from [`SessionBase`](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#django.contrib.sessions.backends.base.SessionBase "django.contrib.sessions.backends.base.SessionBase") or any other existing `SessionStore` class.
You can extend the session engines, but doing so with database-backed session engines generally requires some extra effort (see the next section for details).
