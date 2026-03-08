## Using sessions in views[¶](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#using-sessions-in-views "Link to this heading")
When `SessionMiddleware` is activated, each [`HttpRequest`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest "django.http.HttpRequest") object – the first argument to any Django view function – will have a `session` attribute, which is a dictionary-like object.
You can read it and write to `request.session` at any point in your view. You can edit it multiple times.

_class_ backends.base.SessionBase[¶](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#django.contrib.sessions.backends.base.SessionBase "Link to this definition")

This is the base class for all session objects. It has the following standard dictionary methods:

__getitem__(_key_)[¶](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#django.contrib.sessions.backends.base.SessionBase.__getitem__ "Link to this definition")

Example: `fav_color = request.session['fav_color']`

__setitem__(_key_ , _value_)[¶](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#django.contrib.sessions.backends.base.SessionBase.__setitem__ "Link to this definition")

Example: `request.session['fav_color'] = 'blue'`

__delitem__(_key_)[¶](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#django.contrib.sessions.backends.base.SessionBase.__delitem__ "Link to this definition")

Example: `del request.session['fav_color']`. This raises `KeyError` if the given `key` isn’t already in the session.

__contains__(_key_)[¶](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#django.contrib.sessions.backends.base.SessionBase.__contains__ "Link to this definition")

Example: `'fav_color' in request.session`

get(_key_ , _default =None_)[¶](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#django.contrib.sessions.backends.base.SessionBase.get "Link to this definition")

Example: `fav_color = request.session.get('fav_color', 'red')`

pop(_key_ , _default =__not_given_)[¶](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#django.contrib.sessions.backends.base.SessionBase.pop "Link to this definition")

Example: `fav_color = request.session.pop('fav_color', 'blue')`

keys()[¶](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#django.contrib.sessions.backends.base.SessionBase.keys "Link to this definition")


items()[¶](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#django.contrib.sessions.backends.base.SessionBase.items "Link to this definition")


setdefault()[¶](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#django.contrib.sessions.backends.base.SessionBase.setdefault "Link to this definition")


clear()[¶](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#django.contrib.sessions.backends.base.SessionBase.clear "Link to this definition")

It also has these methods:

flush()[¶](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#django.contrib.sessions.backends.base.SessionBase.flush "Link to this definition")

Deletes the current session data from the session and deletes the session cookie. This is used if you want to ensure that the previous session data can’t be accessed again from the user’s browser (for example, the [`django.contrib.auth.logout()`](https://docs.djangoproject.com/en/5.0/topics/auth/default/#django.contrib.auth.logout "django.contrib.auth.logout") function calls it).

set_test_cookie()[¶](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#django.contrib.sessions.backends.base.SessionBase.set_test_cookie "Link to this definition")

Sets a test cookie to determine whether the user’s browser supports cookies. Due to the way cookies work, you won’t be able to test this until the user’s next page request. See [Setting test cookies](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#setting-test-cookies) below for more information.

test_cookie_worked()[¶](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#django.contrib.sessions.backends.base.SessionBase.test_cookie_worked "Link to this definition")

Returns either `True` or `False`, depending on whether the user’s browser accepted the test cookie. Due to the way cookies work, you’ll have to call `set_test_cookie()` on a previous, separate page request. See [Setting test cookies](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#setting-test-cookies) below for more information.

delete_test_cookie()[¶](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#django.contrib.sessions.backends.base.SessionBase.delete_test_cookie "Link to this definition")

Deletes the test cookie. Use this to clean up after yourself.

get_session_cookie_age()[¶](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#django.contrib.sessions.backends.base.SessionBase.get_session_cookie_age "Link to this definition")

Returns the value of the setting [`SESSION_COOKIE_AGE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SESSION_COOKIE_AGE). This can be overridden in a custom session backend.

set_expiry(_value_)[¶](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#django.contrib.sessions.backends.base.SessionBase.set_expiry "Link to this definition")

Sets the expiration time for the session. You can pass a number of different values:
  * If `value` is an integer, the session will expire after that many seconds of inactivity. For example, calling `request.session.set_expiry(300)` would make the session expire in 5 minutes.
  * If `value` is a `datetime` or `timedelta` object, the session will expire at that specific date/time.
  * If `value` is `0`, the user’s session cookie will expire when the user’s web browser is closed.
  * If `value` is `None`, the session reverts to using the global session expiry policy.


Reading a session is not considered activity for expiration purposes. Session expiration is computed from the last time the session was _modified_.

get_expiry_age()[¶](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#django.contrib.sessions.backends.base.SessionBase.get_expiry_age "Link to this definition")

Returns the number of seconds until this session expires. For sessions with no custom expiration (or those set to expire at browser close), this will equal [`SESSION_COOKIE_AGE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SESSION_COOKIE_AGE).
This function accepts two optional keyword arguments:
  * `modification`: last modification of the session, as a
  * `expiry`: expiry information for the session, as a `None`. Defaults to the value stored in the session by [`set_expiry()`](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#django.contrib.sessions.backends.base.SessionBase.set_expiry "django.contrib.sessions.backends.base.SessionBase.set_expiry"), if there is one, or `None`.


Note
This method is used by session backends to determine the session expiry age in seconds when saving the session. It is not really intended for usage outside of that context.
In particular, while it is **possible** to determine the remaining lifetime of a session **just when** you have the correct `modification` value **and** the `expiry` is set as a `datetime` object, where you do have the `modification` value, it is more straight-forward to calculate the expiry by-hand:
```
expires_at = modification + timedelta(seconds=settings.SESSION_COOKIE_AGE)

```


get_expiry_date()[¶](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#django.contrib.sessions.backends.base.SessionBase.get_expiry_date "Link to this definition")

Returns the date this session will expire. For sessions with no custom expiration (or those set to expire at browser close), this will equal the date [`SESSION_COOKIE_AGE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SESSION_COOKIE_AGE) seconds from now.
This function accepts the same keyword arguments as [`get_expiry_age()`](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#django.contrib.sessions.backends.base.SessionBase.get_expiry_age "django.contrib.sessions.backends.base.SessionBase.get_expiry_age"), and similar notes on usage apply.

get_expire_at_browser_close()[¶](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#django.contrib.sessions.backends.base.SessionBase.get_expire_at_browser_close "Link to this definition")

Returns either `True` or `False`, depending on whether the user’s session cookie will expire when the user’s web browser is closed.

clear_expired()[¶](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#django.contrib.sessions.backends.base.SessionBase.clear_expired "Link to this definition")

Removes expired sessions from the session store. This class method is called by [`clearsessions`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-clearsessions).

cycle_key()[¶](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#django.contrib.sessions.backends.base.SessionBase.cycle_key "Link to this definition")

Creates a new session key while retaining the current session data. [`django.contrib.auth.login()`](https://docs.djangoproject.com/en/5.0/topics/auth/default/#django.contrib.auth.login "django.contrib.auth.login") calls this method to mitigate against session fixation.
### Session serialization[¶](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#session-serialization "Link to this heading")
By default, Django serializes session data using JSON. You can use the [`SESSION_SERIALIZER`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SESSION_SERIALIZER) setting to customize the session serialization format. Even with the caveats described in [Write your own serializer](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#custom-serializers), we highly recommend sticking with JSON serialization _especially if you are using the cookie backend_.
For example, here’s an attack scenario if you use [signed cookie session backend](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#cookie-session-backend) and [`SECRET_KEY`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECRET_KEY) (or any key of [`SECRET_KEY_FALLBACKS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECRET_KEY_FALLBACKS)) is known by an attacker (there isn’t an inherent vulnerability in Django that would cause it to leak), the attacker could insert a string into their session which, when unpickled, executes arbitrary code on the server. The technique for doing so is simple and easily available on the internet. Although the cookie session storage signs the cookie-stored data to prevent tampering, a [`SECRET_KEY`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECRET_KEY) leak immediately escalates to a remote code execution vulnerability.
#### Bundled serializers[¶](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#bundled-serializers "Link to this heading")

_class_ serializers.JSONSerializer[¶](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#django.contrib.sessions.serializers.JSONSerializer "Link to this definition")

A wrapper around the JSON serializer from [`django.core.signing`](https://docs.djangoproject.com/en/5.0/topics/signing/#module-django.core.signing "django.core.signing: Django's signing framework."). Can only serialize basic data types.
In addition, as JSON supports only string keys, note that using non-string keys in `request.session` won’t work as expected:
```
>>> # initial assignment
>>> request.session[0] = "bar"
>>> # subsequent requests following serialization & deserialization
>>> # of session data
>>> request.session[0]  # KeyError
>>> request.session["0"]
'bar'

```

Similarly, data that can’t be encoded in JSON, such as non-UTF8 bytes like `'\xd9'` (which raises
See the [Write your own serializer](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#custom-serializers) section for more details on limitations of JSON serialization.
#### Write your own serializer[¶](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#write-your-own-serializer "Link to this heading")
Note that the [`JSONSerializer`](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#django.contrib.sessions.serializers.JSONSerializer "django.contrib.sessions.serializers.JSONSerializer") cannot handle arbitrary Python data types. As is often the case, there is a trade-off between convenience and security. If you wish to store more advanced data types including `datetime` and `Decimal` in JSON backed sessions, you will need to write a custom serializer (or convert such values to a JSON serializable object before storing them in `request.session`). While serializing these values is often straightforward ([`DjangoJSONEncoder`](https://docs.djangoproject.com/en/5.0/topics/serialization/#django.core.serializers.json.DjangoJSONEncoder "django.core.serializers.json.DjangoJSONEncoder") may be helpful), writing a decoder that can reliably get back the same thing that you put in is more fragile. For example, you run the risk of returning a `datetime` that was actually a string that just happened to be in the same format chosen for `datetime`s).
Your serializer class must implement two methods, `dumps(self, obj)` and `loads(self, data)`, to serialize and deserialize the dictionary of session data, respectively.
### Session object guidelines[¶](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#session-object-guidelines "Link to this heading")
  * Use normal Python strings as dictionary keys on `request.session`. This is more of a convention than a hard-and-fast rule.
  * Session dictionary keys that begin with an underscore are reserved for internal use by Django.
  * Don’t override `request.session` with a new object, and don’t access or set its attributes. Use it like a Python dictionary.


### Examples[¶](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#examples "Link to this heading")
This simplistic view sets a `has_commented` variable to `True` after a user posts a comment. It doesn’t let a user post a comment more than once:
```
def post_comment(request, new_comment):
    if request.session.get("has_commented", False):
        return HttpResponse("You've already commented.")
    c = comments.Comment(comment=new_comment)
    c.save()
    request.session["has_commented"] = True
    return HttpResponse("Thanks for your comment!")

```

This simplistic view logs in a “member” of the site:
```
def login(request):
    m = Member.objects.get(username=request.POST["username"])
    if m.check_password(request.POST["password"]):
        request.session["member_id"] = m.id
        return HttpResponse("You're logged in.")
    else:
        return HttpResponse("Your username and password didn't match.")

```

…And this one logs a member out, according to `login()` above:
```
def logout(request):
    try:
        del request.session["member_id"]
    except KeyError:
        pass
    return HttpResponse("You're logged out.")

```

The standard [`django.contrib.auth.logout()`](https://docs.djangoproject.com/en/5.0/topics/auth/default/#django.contrib.auth.logout "django.contrib.auth.logout") function actually does a bit more than this to prevent inadvertent data leakage. It calls the [`flush()`](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#django.contrib.sessions.backends.base.SessionBase.flush "django.contrib.sessions.backends.base.SessionBase.flush") method of `request.session`. We are using this example as a demonstration of how to work with session objects, not as a full `logout()` implementation.
