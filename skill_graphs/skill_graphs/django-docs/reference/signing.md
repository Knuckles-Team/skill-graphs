This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/topics/signing/#main-content)
[Django](https://www.djangoproject.com/)
The web framework for perfectionists with deadlines.
Menu Main navigation
  * [Overview](https://www.djangoproject.com/start/overview/)
  * [Download](https://www.djangoproject.com/download/)
  * [Documentation](https://docs.djangoproject.com/)
  * [News](https://www.djangoproject.com/weblog/)
  * [Issues](https://code.djangoproject.com/)
  * [Community](https://www.djangoproject.com/community/)
  * [Foundation](https://www.djangoproject.com/foundation/)
  * [♥ Donate](https://www.djangoproject.com/fundraising/)


Search Submit
Toggle theme (current theme: auto)
Toggle theme (current theme: light)
Toggle theme (current theme: dark)
Toggle Light / Dark / Auto color theme
[Documentation](https://docs.djangoproject.com/en/5.0/)
  * [ Getting Help ](https://docs.djangoproject.com/en/5.0/faq/help/)


  * Language: **en**
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/topics/signing/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/topics/signing/)
  * [pl](https://docs.djangoproject.com/pl/5.0/topics/signing/)
  * [ko](https://docs.djangoproject.com/ko/5.0/topics/signing/)
  * [ja](https://docs.djangoproject.com/ja/5.0/topics/signing/)
  * [it](https://docs.djangoproject.com/it/5.0/topics/signing/)
  * [id](https://docs.djangoproject.com/id/5.0/topics/signing/)
  * [fr](https://docs.djangoproject.com/fr/5.0/topics/signing/)
  * [es](https://docs.djangoproject.com/es/5.0/topics/signing/)
  * [el](https://docs.djangoproject.com/el/5.0/topics/signing/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/topics/signing/)
  * [6.0](https://docs.djangoproject.com/en/6.0/topics/signing/)
  * [5.2](https://docs.djangoproject.com/en/5.2/topics/signing/)
  * [5.1](https://docs.djangoproject.com/en/5.1/topics/signing/)
  * [4.2](https://docs.djangoproject.com/en/4.2/topics/signing/)
  * [4.1](https://docs.djangoproject.com/en/4.1/topics/signing/)
  * [4.0](https://docs.djangoproject.com/en/4.0/topics/signing/)
  * [3.2](https://docs.djangoproject.com/en/3.2/topics/signing/)
  * [3.1](https://docs.djangoproject.com/en/3.1/topics/signing/)
  * [3.0](https://docs.djangoproject.com/en/3.0/topics/signing/)
  * [2.2](https://docs.djangoproject.com/en/2.2/topics/signing/)
  * [2.1](https://docs.djangoproject.com/en/2.1/topics/signing/)
  * [2.0](https://docs.djangoproject.com/en/2.0/topics/signing/)
  * [1.11](https://docs.djangoproject.com/en/1.11/topics/signing/)
  * [1.10](https://docs.djangoproject.com/en/1.10/topics/signing/)
  * [1.8](https://docs.djangoproject.com/en/1.8/topics/signing/)


  * [](https://docs.djangoproject.com/en/5.0/topics/signing/#top)


# Cryptographic signing[¶](https://docs.djangoproject.com/en/5.0/topics/signing/#module-django.core.signing "Link to this heading")
The golden rule of web application security is to never trust data from untrusted sources. Sometimes it can be useful to pass data through an untrusted medium. Cryptographically signed values can be passed through an untrusted channel safe in the knowledge that any tampering will be detected.
Django provides both a low-level API for signing values and a high-level API for setting and reading signed cookies, one of the most common uses of signing in web applications.
You may also find signing useful for the following:
  * Generating “recover my account” URLs for sending to users who have lost their password.
  * Ensuring data stored in hidden form fields has not been tampered with.
  * Generating one-time secret URLs for allowing temporary access to a protected resource, for example a downloadable file that a user has paid for.


## Protecting `SECRET_KEY` and `SECRET_KEY_FALLBACKS`[¶](https://docs.djangoproject.com/en/5.0/topics/signing/#protecting-secret-key-and-secret-key-fallbacks "Link to this heading")
When you create a new Django project using [`startproject`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-startproject), the `settings.py` file is generated automatically and gets a random [`SECRET_KEY`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECRET_KEY) value. This value is the key to securing signed data – it is vital you keep this secure, or attackers could use it to generate their own signed values.
[`SECRET_KEY_FALLBACKS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECRET_KEY_FALLBACKS) can be used to rotate secret keys. The values will not be used to sign data, but if specified, they will be used to validate signed data and must be kept secure.
## Using the low-level API[¶](https://docs.djangoproject.com/en/5.0/topics/signing/#using-the-low-level-api "Link to this heading")
Django’s signing methods live in the `django.core.signing` module. To sign a value, first instantiate a `Signer` instance:
```
>>> from django.core.signing import Signer
>>> signer = Signer()
>>> value = signer.sign("My string")
>>> value
'My string:GdMGD6HNQ_qdgxYP8yBZAdAIV1w'

```

The signature is appended to the end of the string, following the colon. You can retrieve the original value using the `unsign` method:
```
>>> original = signer.unsign(value)
>>> original
'My string'

```

If you pass a non-string value to `sign`, the value will be forced to string before being signed, and the `unsign` result will give you that string value:
```
>>> signed = signer.sign(2.5)
>>> original = signer.unsign(signed)
>>> original
'2.5'

```

If you wish to protect a list, tuple, or dictionary you can do so using the `sign_object()` and `unsign_object()` methods:
```
>>> signed_obj = signer.sign_object({"message": "Hello!"})
>>> signed_obj
'eyJtZXNzYWdlIjoiSGVsbG8hIn0:Xdc-mOFDjs22KsQAqfVfi8PQSPdo3ckWJxPWwQOFhR4'
>>> obj = signer.unsign_object(signed_obj)
>>> obj
{'message': 'Hello!'}

```

See [Protecting complex data structures](https://docs.djangoproject.com/en/5.0/topics/signing/#signing-complex-data) for more details.
If the signature or value have been altered in any way, a `django.core.signing.BadSignature` exception will be raised:
```
>>> from django.core import signing
>>> value += "m"
>>> try:
...     original = signer.unsign(value)
... except signing.BadSignature:
...     print("Tampering detected!")
...

```

By default, the `Signer` class uses the [`SECRET_KEY`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECRET_KEY) setting to generate signatures. You can use a different secret by passing it to the `Signer` constructor:
```
>>> signer = Signer(key="my-other-secret")
>>> value = signer.sign("My string")
>>> value
'My string:EkfQJafvGyiofrdGnuthdxImIJw'

```


_class_ Signer(_*_ , _key =None_, _sep =':'_, _salt =None_, _algorithm =None_, _fallback_keys =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/signing/#Signer)[¶](https://docs.djangoproject.com/en/5.0/topics/signing/#django.core.signing.Signer "Link to this definition")

Returns a signer which uses `key` to generate signatures and `sep` to separate values. `sep` cannot be in the `algorithm` must be an algorithm supported by `'sha256'`. `fallback_keys` is a list of additional values used to validate signed data, defaults to [`SECRET_KEY_FALLBACKS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECRET_KEY_FALLBACKS).
Deprecated since version 4.2: Support for passing positional arguments is deprecated.
### Using the `salt` argument[¶](https://docs.djangoproject.com/en/5.0/topics/signing/#using-the-salt-argument "Link to this heading")
If you do not wish for every occurrence of a particular string to have the same signature hash, you can use the optional `salt` argument to the `Signer` class. Using a salt will seed the signing hash function with both the salt and your [`SECRET_KEY`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECRET_KEY):
```
>>> signer = Signer()
>>> signer.sign("My string")
'My string:GdMGD6HNQ_qdgxYP8yBZAdAIV1w'
>>> signer.sign_object({"message": "Hello!"})
'eyJtZXNzYWdlIjoiSGVsbG8hIn0:Xdc-mOFDjs22KsQAqfVfi8PQSPdo3ckWJxPWwQOFhR4'
>>> signer = Signer(salt="extra")
>>> signer.sign("My string")
'My string:Ee7vGi-ING6n02gkcJ-QLHg6vFw'
>>> signer.unsign("My string:Ee7vGi-ING6n02gkcJ-QLHg6vFw")
'My string'
>>> signer.sign_object({"message": "Hello!"})
'eyJtZXNzYWdlIjoiSGVsbG8hIn0:-UWSLCE-oUAHzhkHviYz3SOZYBjFKllEOyVZNuUtM-I'
>>> signer.unsign_object(
...     "eyJtZXNzYWdlIjoiSGVsbG8hIn0:-UWSLCE-oUAHzhkHviYz3SOZYBjFKllEOyVZNuUtM-I"
... )
{'message': 'Hello!'}

```

Using salt in this way puts the different signatures into different namespaces. A signature that comes from one namespace (a particular salt value) cannot be used to validate the same plaintext string in a different namespace that is using a different salt setting. The result is to prevent an attacker from using a signed string generated in one place in the code as input to another piece of code that is generating (and verifying) signatures using a different salt.
Unlike your [`SECRET_KEY`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECRET_KEY), your salt argument does not need to stay secret.
### Verifying timestamped values[¶](https://docs.djangoproject.com/en/5.0/topics/signing/#verifying-timestamped-values "Link to this heading")
`TimestampSigner` is a subclass of [`Signer`](https://docs.djangoproject.com/en/5.0/topics/signing/#django.core.signing.Signer "django.core.signing.Signer") that appends a signed timestamp to the value. This allows you to confirm that a signed value was created within a specified period of time:
```
>>> from datetime import timedelta
>>> from django.core.signing import TimestampSigner
>>> signer = TimestampSigner()
>>> value = signer.sign("hello")
>>> value
'hello:1NMg5H:oPVuCqlJWmChm1rA2lyTUtelC-c'
>>> signer.unsign(value)
'hello'
>>> signer.unsign(value, max_age=10)
SignatureExpired: Signature age 15.5289158821 > 10 seconds
>>> signer.unsign(value, max_age=20)
'hello'
>>> signer.unsign(value, max_age=timedelta(seconds=20))
'hello'

```


_class_ TimestampSigner(_*_ , _key =None_, _sep =':'_, _salt =None_, _algorithm ='sha256'_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/signing/#TimestampSigner)[¶](https://docs.djangoproject.com/en/5.0/topics/signing/#django.core.signing.TimestampSigner "Link to this definition")


sign(_value_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/signing/#TimestampSigner.sign)[¶](https://docs.djangoproject.com/en/5.0/topics/signing/#django.core.signing.TimestampSigner.sign "Link to this definition")

Sign `value` and append current timestamp to it.

unsign(_value_ , _max_age =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/signing/#TimestampSigner.unsign)[¶](https://docs.djangoproject.com/en/5.0/topics/signing/#django.core.signing.TimestampSigner.unsign "Link to this definition")

Checks if `value` was signed less than `max_age` seconds ago, otherwise raises `SignatureExpired`. The `max_age` parameter can accept an integer or a

sign_object(_obj_ , _serializer =JSONSerializer_, _compress =False_)[¶](https://docs.djangoproject.com/en/5.0/topics/signing/#django.core.signing.TimestampSigner.sign_object "Link to this definition")

Encode, optionally compress, append current timestamp, and sign complex data structure (e.g. list, tuple, or dictionary).

unsign_object(_signed_obj_ , _serializer =JSONSerializer_, _max_age =None_)[¶](https://docs.djangoproject.com/en/5.0/topics/signing/#django.core.signing.TimestampSigner.unsign_object "Link to this definition")

Checks if `signed_obj` was signed less than `max_age` seconds ago, otherwise raises `SignatureExpired`. The `max_age` parameter can accept an integer or a
Deprecated since version 4.2: Support for passing positional arguments is deprecated.
### Protecting complex data structures[¶](https://docs.djangoproject.com/en/5.0/topics/signing/#protecting-complex-data-structures "Link to this heading")
If you wish to protect a list, tuple or dictionary you can do so using the `Signer.sign_object()` and `unsign_object()` methods, or signing module’s `dumps()` or `loads()` functions (which are shortcuts for `TimestampSigner(salt='django.core.signing').sign_object()/unsign_object()`). These use JSON serialization under the hood. JSON ensures that even if your [`SECRET_KEY`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECRET_KEY) is stolen an attacker will not be able to execute arbitrary commands by exploiting the pickle format:
```
>>> from django.core import signing
>>> signer = signing.TimestampSigner()
>>> value = signer.sign_object({"foo": "bar"})
>>> value
'eyJmb28iOiJiYXIifQ:1kx6R3:D4qGKiptAqo5QW9iv4eNLc6xl4RwiFfes6oOcYhkYnc'
>>> signer.unsign_object(value)
{'foo': 'bar'}
>>> value = signing.dumps({"foo": "bar"})
>>> value
'eyJmb28iOiJiYXIifQ:1kx6Rf:LBB39RQmME-SRvilheUe5EmPYRbuDBgQp2tCAi7KGLk'
>>> signing.loads(value)
{'foo': 'bar'}

```

Because of the nature of JSON (there is no native distinction between lists and tuples) if you pass in a tuple, you will get a list from `signing.loads(object)`:
```
>>> from django.core import signing
>>> value = signing.dumps(("a", "b", "c"))
>>> signing.loads(value)
['a', 'b', 'c']

```


dumps(_obj_ , _key =None_, _salt ='django.core.signing'_, _serializer =JSONSerializer_, _compress =False_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/signing/#dumps)[¶](https://docs.djangoproject.com/en/5.0/topics/signing/#django.core.signing.dumps "Link to this definition")

Returns URL-safe, signed base64 compressed JSON string. Serialized object is signed using [`TimestampSigner`](https://docs.djangoproject.com/en/5.0/topics/signing/#django.core.signing.TimestampSigner "django.core.signing.TimestampSigner").

loads(_string_ , _key =None_, _salt ='django.core.signing'_, _serializer =JSONSerializer_, _max_age =None_, _fallback_keys =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/signing/#loads)[¶](https://docs.djangoproject.com/en/5.0/topics/signing/#django.core.signing.loads "Link to this definition")

Reverse of `dumps()`, raises `BadSignature` if signature fails. Checks `max_age` (in seconds) if given. Previous page and next page
[](https://docs.djangoproject.com/en/5.0/topics/conditional-view-processing/)
[Sending email ](https://docs.djangoproject.com/en/5.0/topics/email/)
[](https://docs.djangoproject.com/en/5.0/topics/signing/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Intevation GmbH donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [Cryptographic signing](https://docs.djangoproject.com/en/5.0/topics/signing/)
    * [Protecting `SECRET_KEY` and `SECRET_KEY_FALLBACKS`](https://docs.djangoproject.com/en/5.0/topics/signing/#protecting-secret-key-and-secret-key-fallbacks)
    * [Using the low-level API](https://docs.djangoproject.com/en/5.0/topics/signing/#using-the-low-level-api)
      * [Using the `salt` argument](https://docs.djangoproject.com/en/5.0/topics/signing/#using-the-salt-argument)
      * [Verifying timestamped values](https://docs.djangoproject.com/en/5.0/topics/signing/#verifying-timestamped-values)
      * [Protecting complex data structures](https://docs.djangoproject.com/en/5.0/topics/signing/#protecting-complex-data-structures)


### Browse
  * Prev: [Conditional View Processing](https://docs.djangoproject.com/en/5.0/topics/conditional-view-processing/)
  * Next: [Sending email](https://docs.djangoproject.com/en/5.0/topics/email/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [Using Django](https://docs.djangoproject.com/en/5.0/topics/)
      * Cryptographic signing


### Getting help

[FAQ](https://docs.djangoproject.com/en/5.0/faq/)
    Try the FAQ — it's got answers to many common questions.

[Index](https://docs.djangoproject.com/en/stable/genindex/), [Module Index](https://docs.djangoproject.com/en/stable/py-modindex/), or [Table of Contents](https://docs.djangoproject.com/en/stable/contents/)
    Handy when looking for specific information.

[Django Discord Server](https://chat.djangoproject.com)
    Join the Django Discord Community.

[Official Django Forum](https://forum.djangoproject.com/)
    Join the community on the Django Forum.

[Ticket tracker](https://code.djangoproject.com/)
    Report bugs with Django or Django documentation in our ticket tracker.
### Download:
Offline (Django 5.0): [HTML](https://media.djangoproject.com/docs/django-docs-5.0-en.zip) |
Provided by
### Diamond and Platinum Members
  * **JetBrains**


  * **Sentry**


  * **Kraken Tech**


## Django Links
### Learn More
  * [About Django](https://www.djangoproject.com/start/overview/)
  * [Getting Started with Django](https://www.djangoproject.com/start/)
  * [Team Organization](https://www.djangoproject.com/foundation/teams/)
  * [Django Software Foundation](https://www.djangoproject.com/foundation/)
  * [Code of Conduct](https://www.djangoproject.com/conduct/)
  * [Diversity Statement](https://www.djangoproject.com/diversity/)


### Get Involved
  * [Join a Group](https://www.djangoproject.com/community/)
  * [Contribute to Django](https://docs.djangoproject.com/en/dev/internals/contributing/)
  * [Submit a Bug](https://docs.djangoproject.com/en/dev/internals/contributing/bugs-and-features/)
  * [Report a Security Issue](https://docs.djangoproject.com/en/dev/internals/security/#reporting-security-issues)
  * [Individual membership](https://www.djangoproject.com/foundation/individual-members/)


### Get Help
  * [Getting Help FAQ](https://docs.djangoproject.com/en/stable/faq/)
  * [Django Discord](https://chat.djangoproject.com)
  * [Official Django Forum](https://forum.djangoproject.com/)


### Follow Us
  * [News RSS](https://www.djangoproject.com/rss/weblog/)


### Support Us
  * [Sponsor Django](https://www.djangoproject.com/fundraising/)
  * [Corporate membership](https://www.djangoproject.com/foundation/corporate-members/)
  * [Benevity Workplace Giving Program](https://www.djangoproject.com/fundraising/#benevity-giving)


[Django](https://www.djangoproject.com/)
  * Hosting by [In-kind donors](https://www.djangoproject.com/fundraising/#in-kind-donors)
  * Design by &


© 2005-2026 [ Django Software Foundation](https://www.djangoproject.com/foundation/) and individual contributors. Django is a [registered trademark](https://www.djangoproject.com/trademarks/) of the Django Software Foundation.
