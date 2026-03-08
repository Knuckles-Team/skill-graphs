## Extending database-backed session engines[¶](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#extending-database-backed-session-engines "Link to this heading")
Creating a custom database-backed session engine built upon those included in Django (namely `db` and `cached_db`) may be done by inheriting [`AbstractBaseSession`](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#django.contrib.sessions.base_session.AbstractBaseSession "django.contrib.sessions.base_session.AbstractBaseSession") and either `SessionStore` class.
`AbstractBaseSession` and `BaseSessionManager` are importable from `django.contrib.sessions.base_session` so that they can be imported without including `django.contrib.sessions` in [`INSTALLED_APPS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-INSTALLED_APPS).

_class_ base_session.AbstractBaseSession[¶](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#django.contrib.sessions.base_session.AbstractBaseSession "Link to this definition")

The abstract base session model.

session_key[¶](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#django.contrib.sessions.base_session.AbstractBaseSession.session_key "Link to this definition")

Primary key. The field itself may contain up to 40 characters. The current implementation generates a 32-character string (a random sequence of digits and lowercase ASCII letters).

session_data[¶](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#django.contrib.sessions.base_session.AbstractBaseSession.session_data "Link to this definition")

A string containing an encoded and serialized session dictionary.

expire_date[¶](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#django.contrib.sessions.base_session.AbstractBaseSession.expire_date "Link to this definition")

A datetime designating when the session expires.
Expired sessions are not available to a user, however, they may still be stored in the database until the [`clearsessions`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-clearsessions) management command is run.

_classmethod_ get_session_store_class()[¶](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#django.contrib.sessions.base_session.AbstractBaseSession.get_session_store_class "Link to this definition")

Returns a session store class to be used with this session model.

get_decoded()[¶](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#django.contrib.sessions.base_session.AbstractBaseSession.get_decoded "Link to this definition")

Returns decoded session data.
Decoding is performed by the session store class.
You can also customize the model manager by subclassing [`BaseSessionManager`](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#django.contrib.sessions.base_session.BaseSessionManager "django.contrib.sessions.base_session.BaseSessionManager"):

_class_ base_session.BaseSessionManager[¶](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#django.contrib.sessions.base_session.BaseSessionManager "Link to this definition")


encode(_session_dict_)[¶](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#django.contrib.sessions.base_session.BaseSessionManager.encode "Link to this definition")

Returns the given session dictionary serialized and encoded as a string.
Encoding is performed by the session store class tied to a model class.

save(_session_key_ , _session_dict_ , _expire_date_)[¶](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#django.contrib.sessions.base_session.BaseSessionManager.save "Link to this definition")

Saves session data for a provided session key, or deletes the session in case the data is empty.
Customization of `SessionStore` classes is achieved by overriding methods and properties described below:

_class_ backends.db.SessionStore[¶](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#django.contrib.sessions.backends.db.SessionStore "Link to this definition")

Implements database-backed session store.

_classmethod_ get_model_class()[¶](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#django.contrib.sessions.backends.db.SessionStore.get_model_class "Link to this definition")

Override this method to return a custom session model if you need one.

create_model_instance(_data_)[¶](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#django.contrib.sessions.backends.db.SessionStore.create_model_instance "Link to this definition")

Returns a new instance of the session model object, which represents the current session state.
Overriding this method provides the ability to modify session model data before it’s saved to database.

_class_ backends.cached_db.SessionStore[¶](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#django.contrib.sessions.backends.cached_db.SessionStore "Link to this definition")

Implements cached database-backed session store.

cache_key_prefix[¶](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#django.contrib.sessions.backends.cached_db.SessionStore.cache_key_prefix "Link to this definition")

A prefix added to a session key to build a cache key string.
### Example[¶](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#example "Link to this heading")
The example below shows a custom database-backed session engine that includes an additional database column to store an account ID (thus providing an option to query the database for all active sessions for an account):
```
from django.contrib.sessions.backends.db import SessionStore as DBStore
from django.contrib.sessions.base_session import AbstractBaseSession
from django.db import models


class CustomSession(AbstractBaseSession):
    account_id = models.IntegerField(null=True, db_index=True)

    @classmethod
    def get_session_store_class(cls):
        return SessionStore


class SessionStore(DBStore):
    @classmethod
    def get_model_class(cls):
        return CustomSession

    def create_model_instance(self, data):
        obj = super().create_model_instance(data)
        try:
            account_id = int(data.get("_auth_user_id"))
        except (ValueError, TypeError):
            account_id = None
        obj.account_id = account_id
        return obj

```

If you are migrating from the Django’s built-in `cached_db` session store to a custom one based on `cached_db`, you should override the cache key prefix in order to prevent a namespace clash:
```
class SessionStore(CachedDBStore):
    cache_key_prefix = "mysessions.custom_cached_db_backend"

    # ...

```
