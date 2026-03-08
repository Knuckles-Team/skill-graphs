##  [Core Settings](https://docs.djangoproject.com/en/5.0/ref/settings/#id12)[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#core-settings "Link to this heading")
Here’s a list of settings available in Django core and their default values. Settings provided by contrib apps are listed below, followed by a topical index of the core settings. For introductory material, see the [settings topic guide](https://docs.djangoproject.com/en/5.0/topics/settings/).
###  `ABSOLUTE_URL_OVERRIDES`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#absolute-url-overrides "Link to this heading")
Default: `{}` (Empty dictionary)
A dictionary mapping `"app_label.model_name"` strings to functions that take a model object and return its URL. This is a way of inserting or overriding `get_absolute_url()` methods on a per-installation basis. Example:
```
ABSOLUTE_URL_OVERRIDES = {
    "blogs.blog": lambda o: "/blogs/%s/" % o.slug,
    "news.story": lambda o: "/stories/%s/%s/" % (o.pub_year, o.slug),
}

```

The model name used in this setting should be all lowercase, regardless of the case of the actual model class name.
###  `ADMINS`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#admins "Link to this heading")
Default: `[]` (Empty list)
A list of all the people who get code error notifications. When [`DEBUG=False`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DEBUG) and [`AdminEmailHandler`](https://docs.djangoproject.com/en/5.0/ref/logging/#django.utils.log.AdminEmailHandler "django.utils.log.AdminEmailHandler") is configured in [`LOGGING`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-LOGGING) (done by default), Django emails these people the details of exceptions raised in the request/response cycle.
Each item in the list should be a tuple of (Full name, email address). Example:
```
[("John", "john@example.com"), ("Mary", "mary@example.com")]

```

###  `ALLOWED_HOSTS`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#allowed-hosts "Link to this heading")
Default: `[]` (Empty list)
A list of strings representing the host/domain names that this Django site can serve. This is a security measure to prevent [HTTP Host header attacks](https://docs.djangoproject.com/en/5.0/topics/security/#host-headers-virtual-hosting), which are possible even under many seemingly-safe web server configurations.
Values in this list can be fully qualified names (e.g. `'www.example.com'`), in which case they will be matched against the request’s `Host` header exactly (case-insensitive, not including port). A value beginning with a period can be used as a subdomain wildcard: `'.example.com'` will match `example.com`, `www.example.com`, and any other subdomain of `example.com`. A value of `'*'` will match anything; in this case you are responsible to provide your own validation of the `Host` header (perhaps in a middleware; if so this middleware must be listed first in [`MIDDLEWARE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MIDDLEWARE)).
Django also allows the `Host` header which Django strips when performing host validation.
If the `Host` header (or `X-Forwarded-Host` if [`USE_X_FORWARDED_HOST`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-USE_X_FORWARDED_HOST) is enabled) does not match any value in this list, the [`django.http.HttpRequest.get_host()`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.get_host "django.http.HttpRequest.get_host") method will raise [`SuspiciousOperation`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.SuspiciousOperation "django.core.exceptions.SuspiciousOperation").
When [`DEBUG`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DEBUG) is `True` and `ALLOWED_HOSTS` is empty, the host is validated against `['.localhost', '127.0.0.1', '[::1]']`.
`ALLOWED_HOSTS` is also [checked when running tests](https://docs.djangoproject.com/en/5.0/topics/testing/advanced/#topics-testing-advanced-multiple-hosts).
This validation only applies via [`get_host()`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.get_host "django.http.HttpRequest.get_host"); if your code accesses the `Host` header directly from `request.META` you are bypassing this security protection.
###  `APPEND_SLASH`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#append-slash "Link to this heading")
Default: `True`
When set to `True`, if the request URL does not match any of the patterns in the URLconf and it doesn’t end in a slash, an HTTP redirect is issued to the same URL with a slash appended. Note that the redirect may cause any data submitted in a POST request to be lost.
The [`APPEND_SLASH`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-APPEND_SLASH) setting is only used if [`CommonMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.middleware.common.CommonMiddleware "django.middleware.common.CommonMiddleware") is installed (see [Middleware](https://docs.djangoproject.com/en/5.0/topics/http/middleware/)). See also [`PREPEND_WWW`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-PREPEND_WWW).
###  `CACHES`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#caches "Link to this heading")
Default:
```
{
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    }
}

```

A dictionary containing the settings for all caches to be used with Django. It is a nested dictionary whose contents maps cache aliases to a dictionary containing the options for an individual cache.
The [`CACHES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CACHES) setting must configure a `default` cache; any number of additional caches may also be specified. If you are using a cache backend other than the local memory cache, or you need to define multiple caches, other options will be required. The following cache options are available.
####  `BACKEND`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#backend "Link to this heading")
Default: `''` (Empty string)
The cache backend to use. The built-in cache backends are:
  * `'django.core.cache.backends.db.DatabaseCache'`
  * `'django.core.cache.backends.dummy.DummyCache'`
  * `'django.core.cache.backends.filebased.FileBasedCache'`
  * `'django.core.cache.backends.locmem.LocMemCache'`
  * `'django.core.cache.backends.memcached.PyMemcacheCache'`
  * `'django.core.cache.backends.memcached.PyLibMCCache'`
  * `'django.core.cache.backends.redis.RedisCache'`


You can use a cache backend that doesn’t ship with Django by setting [`BACKEND`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CACHES-BACKEND) to a fully-qualified path of a cache backend class (i.e. `mypackage.backends.whatever.WhateverCache`).
####  `KEY_FUNCTION`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#key-function "Link to this heading")
A string containing a dotted path to a function (or any callable) that defines how to compose a prefix, version and key into a final cache key. The default implementation is equivalent to the function:
```
def make_key(key, key_prefix, version):
    return ":".join([key_prefix, str(version), key])

```

You may use any key function you want, as long as it has the same argument signature.
See the [cache documentation](https://docs.djangoproject.com/en/5.0/topics/cache/#cache-key-transformation) for more information.
####  `KEY_PREFIX`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#key-prefix "Link to this heading")
Default: `''` (Empty string)
A string that will be automatically included (prepended by default) to all cache keys used by the Django server.
See the [cache documentation](https://docs.djangoproject.com/en/5.0/topics/cache/#cache-key-prefixing) for more information.
####  `LOCATION`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#location "Link to this heading")
Default: `''` (Empty string)
The location of the cache to use. This might be the directory for a file system cache, a host and port for a memcache server, or an identifying name for a local memory cache. e.g.:
```
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": "/var/tmp/django_cache",
    }
}

```

####  `OPTIONS`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#options "Link to this heading")
Default: `None`
Extra parameters to pass to the cache backend. Available parameters vary depending on your cache backend.
Some information on available parameters can be found in the [cache arguments](https://docs.djangoproject.com/en/5.0/topics/cache/#cache-arguments) documentation. For more information, consult your backend module’s own documentation.
####  `TIMEOUT`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#timeout "Link to this heading")
Default: `300`
The number of seconds before a cache entry is considered stale. If the value of this setting is `None`, cache entries will not expire. A value of `0` causes keys to immediately expire (effectively “don’t cache”).
####  `VERSION`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#version "Link to this heading")
Default: `1`
The default version number for cache keys generated by the Django server.
See the [cache documentation](https://docs.djangoproject.com/en/5.0/topics/cache/#cache-versioning) for more information.
###  `CACHE_MIDDLEWARE_ALIAS`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#cache-middleware-alias "Link to this heading")
Default: `'default'`
The cache connection to use for the [cache middleware](https://docs.djangoproject.com/en/5.0/topics/cache/#the-per-site-cache).
###  `CACHE_MIDDLEWARE_KEY_PREFIX`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#cache-middleware-key-prefix "Link to this heading")
Default: `''` (Empty string)
A string which will be prefixed to the cache keys generated by the [cache middleware](https://docs.djangoproject.com/en/5.0/topics/cache/#the-per-site-cache). This prefix is combined with the [`KEY_PREFIX`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CACHES-KEY_PREFIX) setting; it does not replace it.
See [Django’s cache framework](https://docs.djangoproject.com/en/5.0/topics/cache/).
###  `CACHE_MIDDLEWARE_SECONDS`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#cache-middleware-seconds "Link to this heading")
Default: `600`
The default integer number of seconds to cache a page for the [cache middleware](https://docs.djangoproject.com/en/5.0/topics/cache/#the-per-site-cache).
See [Django’s cache framework](https://docs.djangoproject.com/en/5.0/topics/cache/).
###  `CSRF_COOKIE_AGE`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#csrf-cookie-age "Link to this heading")
Default: `31449600` (approximately 1 year, in seconds)
The age of CSRF cookies, in seconds.
The reason for setting a long-lived expiration time is to avoid problems in the case of a user closing a browser or bookmarking a page and then loading that page from a browser cache. Without persistent cookies, the form submission would fail in this case.
Some browsers (specifically Internet Explorer) can disallow the use of persistent cookies or can have the indexes to the cookie jar corrupted on disk, thereby causing CSRF protection checks to (sometimes intermittently) fail. Change this setting to `None` to use session-based CSRF cookies, which keep the cookies in-memory instead of on persistent storage.
###  `CSRF_COOKIE_DOMAIN`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#csrf-cookie-domain "Link to this heading")
Default: `None`
The domain to be used when setting the CSRF cookie. This can be useful for easily allowing cross-subdomain requests to be excluded from the normal cross site request forgery protection. It should be set to a string such as `".example.com"` to allow a POST request from a form on one subdomain to be accepted by a view served from another subdomain.
Please note that the presence of this setting does not imply that Django’s CSRF protection is safe from cross-subdomain attacks by default - please see the [CSRF limitations](https://docs.djangoproject.com/en/5.0/ref/csrf/#csrf-limitations) section.
###  `CSRF_COOKIE_HTTPONLY`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#csrf-cookie-httponly "Link to this heading")
Default: `False`
Whether to use `HttpOnly` flag on the CSRF cookie. If this is set to `True`, client-side JavaScript will not be able to access the CSRF cookie.
Designating the CSRF cookie as `HttpOnly` doesn’t offer any practical protection because CSRF is only to protect against cross-domain attacks. If an attacker can read the cookie via JavaScript, they’re already on the same domain as far as the browser knows, so they can do anything they like anyway. (XSS is a much bigger hole than CSRF.)
Although the setting offers little practical benefit, it’s sometimes required by security auditors.
If you enable this and need to send the value of the CSRF token with an AJAX request, your JavaScript must pull the value [from a hidden CSRF token form input](https://docs.djangoproject.com/en/5.0/howto/csrf/#acquiring-csrf-token-from-html) instead of [from the cookie](https://docs.djangoproject.com/en/5.0/howto/csrf/#acquiring-csrf-token-from-cookie).
See [`SESSION_COOKIE_HTTPONLY`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SESSION_COOKIE_HTTPONLY) for details on `HttpOnly`.
###  `CSRF_COOKIE_NAME`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#csrf-cookie-name "Link to this heading")
Default: `'csrftoken'`
The name of the cookie to use for the CSRF authentication token. This can be whatever you want (as long as it’s different from the other cookie names in your application). See [Cross Site Request Forgery protection](https://docs.djangoproject.com/en/5.0/ref/csrf/).
###  `CSRF_COOKIE_PATH`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#csrf-cookie-path "Link to this heading")
Default: `'/'`
The path set on the CSRF cookie. This should either match the URL path of your Django installation or be a parent of that path.
This is useful if you have multiple Django instances running under the same hostname. They can use different cookie paths, and each instance will only see its own CSRF cookie.
###  `CSRF_COOKIE_SAMESITE`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#csrf-cookie-samesite "Link to this heading")
Default: `'Lax'`
The value of the
See [`SESSION_COOKIE_SAMESITE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SESSION_COOKIE_SAMESITE) for details about `SameSite`.
###  `CSRF_COOKIE_SECURE`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#csrf-cookie-secure "Link to this heading")
Default: `False`
Whether to use a secure cookie for the CSRF cookie. If this is set to `True`, the cookie will be marked as “secure”, which means browsers may ensure that the cookie is only sent with an HTTPS connection.
###  `CSRF_USE_SESSIONS`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#csrf-use-sessions "Link to this heading")
Default: `False`
Whether to store the CSRF token in the user’s session instead of in a cookie. It requires the use of [`django.contrib.sessions`](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#module-django.contrib.sessions "django.contrib.sessions: Provides session management for Django projects.").
Storing the CSRF token in a cookie (Django’s default) is safe, but storing it in the session is common practice in other web frameworks and therefore sometimes demanded by security auditors.
Since the [default error views](https://docs.djangoproject.com/en/5.0/ref/views/#error-views) require the CSRF token, [`SessionMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.contrib.sessions.middleware.SessionMiddleware "django.contrib.sessions.middleware.SessionMiddleware") must appear in [`MIDDLEWARE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MIDDLEWARE) before any middleware that may raise an exception to trigger an error view (such as [`PermissionDenied`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.PermissionDenied "django.core.exceptions.PermissionDenied")) if you’re using `CSRF_USE_SESSIONS`. See [Middleware ordering](https://docs.djangoproject.com/en/5.0/ref/middleware/#middleware-ordering).
###  `CSRF_FAILURE_VIEW`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#csrf-failure-view "Link to this heading")
Default: `'django.views.csrf.csrf_failure'`
A dotted path to the view function to be used when an incoming request is rejected by the [CSRF protection](https://docs.djangoproject.com/en/5.0/ref/csrf/). The function should have this signature:
```
def csrf_failure(request, reason=""): ...

```

where `reason` is a short message (intended for developers or logging, not for end users) indicating the reason the request was rejected. It should return an [`HttpResponseForbidden`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponseForbidden "django.http.HttpResponseForbidden").
`django.views.csrf.csrf_failure()` accepts an additional `template_name` parameter that defaults to `'403_csrf.html'`. If a template with that name exists, it will be used to render the page.
###  `CSRF_HEADER_NAME`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#csrf-header-name "Link to this heading")
Default: `'HTTP_X_CSRFTOKEN'`
The name of the request header used for CSRF authentication.
As with other HTTP headers in `request.META`, the header name received from the server is normalized by converting all characters to uppercase, replacing any hyphens with underscores, and adding an `'HTTP_'` prefix to the name. For example, if your client sends a `'X-XSRF-TOKEN'` header, the setting should be `'HTTP_X_XSRF_TOKEN'`.
###  `CSRF_TRUSTED_ORIGINS`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#csrf-trusted-origins "Link to this heading")
Default: `[]` (Empty list)
A list of trusted origins for unsafe requests (e.g. `POST`).
For requests that include the `Origin` header, Django’s CSRF protection requires that header match the origin present in the `Host` header.
For a [`secure`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.is_secure "django.http.HttpRequest.is_secure") unsafe request that doesn’t include the `Origin` header, the request must have a `Referer` header that matches the origin present in the `Host` header.
These checks prevent, for example, a `POST` request from `subdomain.example.com` from succeeding against `api.example.com`. If you need cross-origin unsafe requests, continuing the example, add `'https://subdomain.example.com'` to this list (and/or `http://...` if requests originate from an insecure page).
The setting also supports subdomains, so you could add `'https://*.example.com'`, for example, to allow access from all subdomains of `example.com`.
###  `DATABASES`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#databases "Link to this heading")
Default: `{}` (Empty dictionary)
A dictionary containing the settings for all databases to be used with Django. It is a nested dictionary whose contents map a database alias to a dictionary containing the options for an individual database.
The [`DATABASES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATABASES) setting must configure a `default` database; any number of additional databases may also be specified.
The simplest possible settings file is for a single-database setup using SQLite. This can be configured using the following:
```
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "mydatabase",
    }
}

```

When connecting to other database backends, such as MariaDB, MySQL, Oracle, or PostgreSQL, additional connection parameters will be required. See the [`ENGINE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATABASE-ENGINE) setting below on how to specify other database types. This example is for PostgreSQL:
```
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "mydatabase",
        "USER": "mydatabaseuser",
        "PASSWORD": "mypassword",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}

```

The following inner options that may be required for more complex configurations are available:
####  `ATOMIC_REQUESTS`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#atomic-requests "Link to this heading")
Default: `False`
Set this to `True` to wrap each view in a transaction on this database. See [Tying transactions to HTTP requests](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#tying-transactions-to-http-requests).
####  `AUTOCOMMIT`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#autocommit "Link to this heading")
Default: `True`
Set this to `False` if you want to [disable Django’s transaction management](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#deactivate-transaction-management) and implement your own.
####  `ENGINE`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#engine "Link to this heading")
Default: `''` (Empty string)
The database backend to use. The built-in database backends are:
  * `'django.db.backends.postgresql'`
  * `'django.db.backends.mysql'`
  * `'django.db.backends.sqlite3'`
  * `'django.db.backends.oracle'`


You can use a database backend that doesn’t ship with Django by setting `ENGINE` to a fully-qualified path (i.e. `mypackage.backends.whatever`).
####  `HOST`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#host "Link to this heading")
Default: `''` (Empty string)
Which host to use when connecting to the database. An empty string means localhost. Not used with SQLite.
If this value starts with a forward slash (`'/'`) and you’re using MySQL, MySQL will connect via a Unix socket to the specified socket. For example:
```
"HOST": "/var/run/mysql"

```

If you’re using MySQL and this value _doesn’t_ start with a forward slash, then this value is assumed to be the host.
If you’re using PostgreSQL, by default (empty [`HOST`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-HOST)), the connection to the database is done through UNIX domain sockets (‘local’ lines in `pg_hba.conf`). If your UNIX domain socket is not in the standard location, use the same value of `unix_socket_directory` from `postgresql.conf`. If you want to connect through TCP sockets, set [`HOST`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-HOST) to ‘localhost’ or ‘127.0.0.1’ (‘host’ lines in `pg_hba.conf`). On Windows, you should always define [`HOST`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-HOST), as UNIX domain sockets are not available.
####  `NAME`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#name "Link to this heading")
Default: `''` (Empty string)
The name of the database to use. For SQLite, it’s the full path to the database file. When specifying the path, always use forward slashes, even on Windows (e.g. `C:/homes/user/mysite/sqlite3.db`).
####  `CONN_MAX_AGE`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#conn-max-age "Link to this heading")
Default: `0`
The lifetime of a database connection, as an integer of seconds. Use `0` to close database connections at the end of each request — Django’s historical behavior — and `None` for unlimited [persistent database connections](https://docs.djangoproject.com/en/5.0/ref/databases/#persistent-database-connections).
####  `CONN_HEALTH_CHECKS`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#conn-health-checks "Link to this heading")
Default: `False`
If set to `True`, existing [persistent database connections](https://docs.djangoproject.com/en/5.0/ref/databases/#persistent-database-connections) will be health checked before they are reused in each request performing database access. If the health check fails, the connection will be reestablished without failing the request when the connection is no longer usable but the database server is ready to accept and serve new connections (e.g. after database server restart closing existing connections).
####  `OPTIONS`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-OPTIONS "Link to this heading")
Default: `{}` (Empty dictionary)
Extra parameters to use when connecting to the database. Available parameters vary depending on your database backend.
Some information on available parameters can be found in the [Database Backends](https://docs.djangoproject.com/en/5.0/ref/databases/) documentation. For more information, consult your backend module’s own documentation.
####  `PASSWORD`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#password "Link to this heading")
Default: `''` (Empty string)
The password to use when connecting to the database. Not used with SQLite.
####  `PORT`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#port "Link to this heading")
Default: `''` (Empty string)
The port to use when connecting to the database. An empty string means the default port. Not used with SQLite.
####  `TIME_ZONE`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#time-zone "Link to this heading")
Default: `None`
A string representing the time zone for this database connection or `None`. This inner option of the [`DATABASES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATABASES) setting accepts the same values as the general [`TIME_ZONE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TIME_ZONE) setting.
