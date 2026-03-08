##  [Messages](https://docs.djangoproject.com/en/5.0/ref/settings/#id14)[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#messages "Link to this heading")
Settings for [`django.contrib.messages`](https://docs.djangoproject.com/en/5.0/ref/contrib/messages/#module-django.contrib.messages "django.contrib.messages: Provides cookie- and session-based temporary message storage.").
###  `MESSAGE_LEVEL`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#message-level "Link to this heading")
Default: `messages.INFO`
Sets the minimum message level that will be recorded by the messages framework. See [message levels](https://docs.djangoproject.com/en/5.0/ref/contrib/messages/#message-level) for more details.
Avoiding circular imports
If you override `MESSAGE_LEVEL` in your settings file and rely on any of the built-in constants, you must import the constants module directly to avoid the potential for circular imports, e.g.:
```
from django.contrib.messages import constants as message_constants

MESSAGE_LEVEL = message_constants.DEBUG

```

If desired, you may specify the numeric values for the constants directly according to the values in the above [constants table](https://docs.djangoproject.com/en/5.0/ref/contrib/messages/#message-level-constants).
###  `MESSAGE_STORAGE`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#message-storage "Link to this heading")
Default: `'django.contrib.messages.storage.fallback.FallbackStorage'`
Controls where Django stores message data. Valid values are:
  * `'django.contrib.messages.storage.fallback.FallbackStorage'`
  * `'django.contrib.messages.storage.session.SessionStorage'`
  * `'django.contrib.messages.storage.cookie.CookieStorage'`


See [message storage backends](https://docs.djangoproject.com/en/5.0/ref/contrib/messages/#message-storage-backends) for more details.
The backends that use cookies – [`CookieStorage`](https://docs.djangoproject.com/en/5.0/ref/contrib/messages/#django.contrib.messages.storage.cookie.CookieStorage "django.contrib.messages.storage.cookie.CookieStorage") and [`FallbackStorage`](https://docs.djangoproject.com/en/5.0/ref/contrib/messages/#django.contrib.messages.storage.fallback.FallbackStorage "django.contrib.messages.storage.fallback.FallbackStorage") – use the value of [`SESSION_COOKIE_DOMAIN`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SESSION_COOKIE_DOMAIN), [`SESSION_COOKIE_SECURE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SESSION_COOKIE_SECURE) and [`SESSION_COOKIE_HTTPONLY`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SESSION_COOKIE_HTTPONLY) when setting their cookies.
###  `MESSAGE_TAGS`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#message-tags "Link to this heading")
Default:
```
{
    messages.DEBUG: "debug",
    messages.INFO: "info",
    messages.SUCCESS: "success",
    messages.WARNING: "warning",
    messages.ERROR: "error",
}

```

This sets the mapping of message level to message tag, which is typically rendered as a CSS class in HTML. If you specify a value, it will extend the default. This means you only have to specify those values which you need to override. See [Displaying messages](https://docs.djangoproject.com/en/5.0/ref/contrib/messages/#message-displaying) above for more details.
Avoiding circular imports
If you override `MESSAGE_TAGS` in your settings file and rely on any of the built-in constants, you must import the `constants` module directly to avoid the potential for circular imports, e.g.:
```
from django.contrib.messages import constants as message_constants

MESSAGE_TAGS = {message_constants.INFO: ""}

```

If desired, you may specify the numeric values for the constants directly according to the values in the above [constants table](https://docs.djangoproject.com/en/5.0/ref/contrib/messages/#message-level-constants).
