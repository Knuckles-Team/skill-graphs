## Enabling sessions[¶](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#enabling-sessions "Link to this heading")
Sessions are implemented via a piece of [middleware](https://docs.djangoproject.com/en/5.0/ref/middleware/).
To enable session functionality, do the following:
  * Edit the [`MIDDLEWARE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MIDDLEWARE) setting and make sure it contains `'django.contrib.sessions.middleware.SessionMiddleware'`. The default `settings.py` created by `django-admin startproject` has `SessionMiddleware` activated.


If you don’t want to use sessions, you might as well remove the `SessionMiddleware` line from [`MIDDLEWARE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MIDDLEWARE) and `'django.contrib.sessions'` from your [`INSTALLED_APPS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-INSTALLED_APPS). It’ll save you a small bit of overhead.
