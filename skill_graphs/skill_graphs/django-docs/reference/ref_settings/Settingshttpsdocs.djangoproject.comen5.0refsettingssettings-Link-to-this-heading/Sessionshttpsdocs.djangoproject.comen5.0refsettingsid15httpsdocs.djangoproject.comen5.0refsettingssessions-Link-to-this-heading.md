##  [Sessions](https://docs.djangoproject.com/en/5.0/ref/settings/#id15)[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#sessions "Link to this heading")
Settings for [`django.contrib.sessions`](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#module-django.contrib.sessions "django.contrib.sessions: Provides session management for Django projects.").
###  `SESSION_CACHE_ALIAS`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#session-cache-alias "Link to this heading")
Default: `'default'`
If you’re using [cache-based session storage](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#cached-sessions-backend), this selects the cache to use.
###  `SESSION_COOKIE_AGE`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#session-cookie-age "Link to this heading")
Default: `1209600` (2 weeks, in seconds)
The age of session cookies, in seconds.
###  `SESSION_COOKIE_DOMAIN`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#session-cookie-domain "Link to this heading")
Default: `None`
The domain to use for session cookies. Set this to a string such as `"example.com"` for cross-domain cookies, or use `None` for a standard domain cookie.
To use cross-domain cookies with [`CSRF_USE_SESSIONS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CSRF_USE_SESSIONS), you must include a leading dot (e.g. `".example.com"`) to accommodate the CSRF middleware’s referer checking.
Be cautious when updating this setting on a production site. If you update this setting to enable cross-domain cookies on a site that previously used standard domain cookies, existing user cookies will be set to the old domain. This may result in them being unable to log in as long as these cookies persist.
This setting also affects cookies set by [`django.contrib.messages`](https://docs.djangoproject.com/en/5.0/ref/contrib/messages/#module-django.contrib.messages "django.contrib.messages: Provides cookie- and session-based temporary message storage.").
###  `SESSION_COOKIE_HTTPONLY`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#session-cookie-httponly "Link to this heading")
Default: `True`
Whether to use `HttpOnly` flag on the session cookie. If this is set to `True`, client-side JavaScript will not be able to access the session cookie.
This makes it less trivial for an attacker to escalate a cross-site scripting vulnerability into full hijacking of a user’s session. There aren’t many good reasons for turning this off. Your code shouldn’t read session cookies from JavaScript.
###  `SESSION_COOKIE_NAME`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#session-cookie-name "Link to this heading")
Default: `'sessionid'`
The name of the cookie to use for sessions. This can be whatever you want (as long as it’s different from the other cookie names in your application).
###  `SESSION_COOKIE_PATH`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#session-cookie-path "Link to this heading")
Default: `'/'`
The path set on the session cookie. This should either match the URL path of your Django installation or be parent of that path.
This is useful if you have multiple Django instances running under the same hostname. They can use different cookie paths, and each instance will only see its own session cookie.
###  `SESSION_COOKIE_SAMESITE`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#session-cookie-samesite "Link to this heading")
Default: `'Lax'`
The value of the
Possible values for the setting are:
  * `'Strict'`: prevents the cookie from being sent by the browser to the target site in all cross-site browsing context, even when following a regular link.
For example, for a GitHub-like website this would mean that if a logged-in user follows a link to a private GitHub project posted on a corporate discussion forum or email, GitHub will not receive the session cookie and the user won’t be able to access the project. A bank website, however, most likely doesn’t want to allow any transactional pages to be linked from external sites so the `'Strict'` flag would be appropriate.
  * `'Lax'` (default): provides a balance between security and usability for websites that want to maintain user’s logged-in session after the user arrives from an external link.
In the GitHub scenario, the session cookie would be allowed when following a regular link from an external website and be blocked in CSRF-prone request methods (e.g. `POST`).
  * `'None'` (string): the session cookie will be sent with all same-site and cross-site requests.
  * `False`: disables the flag.


Note
Modern browsers provide a more secure default policy for the `SameSite` flag and will assume `Lax` for cookies without an explicit value set.
###  `SESSION_COOKIE_SECURE`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#session-cookie-secure "Link to this heading")
Default: `False`
Whether to use a secure cookie for the session cookie. If this is set to `True`, the cookie will be marked as “secure”, which means browsers may ensure that the cookie is only sent under an HTTPS connection.
Leaving this setting off isn’t a good idea because an attacker could capture an unencrypted session cookie with a packet sniffer and use the cookie to hijack the user’s session.
###  `SESSION_ENGINE`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#session-engine "Link to this heading")
Default: `'django.contrib.sessions.backends.db'`
Controls where Django stores session data. Included engines are:
  * `'django.contrib.sessions.backends.db'`
  * `'django.contrib.sessions.backends.file'`
  * `'django.contrib.sessions.backends.cache'`
  * `'django.contrib.sessions.backends.cached_db'`
  * `'django.contrib.sessions.backends.signed_cookies'`


See [Configuring the session engine](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#configuring-sessions) for more details.
###  `SESSION_EXPIRE_AT_BROWSER_CLOSE`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#session-expire-at-browser-close "Link to this heading")
Default: `False`
Whether to expire the session when the user closes their browser. See [Browser-length sessions vs. persistent sessions](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#browser-length-vs-persistent-sessions).
###  `SESSION_FILE_PATH`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#session-file-path "Link to this heading")
Default: `None`
If you’re using file-based session storage, this sets the directory in which Django will store session data. When the default value (`None`) is used, Django will use the standard temporary directory for the system.
###  `SESSION_SAVE_EVERY_REQUEST`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#session-save-every-request "Link to this heading")
Default: `False`
Whether to save the session data on every request. If this is `False` (default), then the session data will only be saved if it has been modified – that is, if any of its dictionary values have been assigned or deleted. Empty sessions won’t be created, even if this setting is active.
###  `SESSION_SERIALIZER`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#session-serializer "Link to this heading")
Default: `'django.contrib.sessions.serializers.JSONSerializer'`
Full import path of a serializer class to use for serializing session data. Included serializer is:
  * `'django.contrib.sessions.serializers.JSONSerializer'`


See [Session serialization](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#session-serialization) for details.
