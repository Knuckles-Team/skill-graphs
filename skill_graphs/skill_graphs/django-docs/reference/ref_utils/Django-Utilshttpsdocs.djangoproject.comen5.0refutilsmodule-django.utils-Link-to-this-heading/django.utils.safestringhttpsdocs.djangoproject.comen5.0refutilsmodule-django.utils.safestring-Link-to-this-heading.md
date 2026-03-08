##  `django.utils.safestring`[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#module-django.utils.safestring "Link to this heading")
Functions and classes for working with “safe strings”: strings that can be displayed safely without further escaping in HTML. Marking something as a “safe string” means that the producer of the string has already turned characters that should not be interpreted by the HTML engine (e.g. ‘<’) into the appropriate entities.

_class_ SafeString[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/safestring/#SafeString)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.safestring.SafeString "Link to this definition")

A `str` subclass that has been specifically marked as “safe” (requires no further escaping) for HTML output purposes.

mark_safe(_s_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/safestring/#mark_safe)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.safestring.mark_safe "Link to this definition")

Explicitly mark a string as safe for (HTML) output purposes. The returned object can be used everywhere a string is appropriate.
Can be called multiple times on a single string.
Can also be used as a decorator.
For building up fragments of HTML, you should normally be using [`django.utils.html.format_html()`](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.html.format_html "django.utils.html.format_html") instead.
String marked safe will become unsafe again if modified. For example:
```
>>> mystr = "<b>Hello World</b>   "
>>> mystr = mark_safe(mystr)
>>> type(mystr)
<class 'django.utils.safestring.SafeString'>

>>> mystr = mystr.strip()  # removing whitespace
>>> type(mystr)
<type 'str'>

```
