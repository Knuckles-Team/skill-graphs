##  `django.utils.text`[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#module-django.utils.text "Link to this heading")

format_lazy(_format_string_ , _* args_, _** kwargs_)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.text.format_lazy "Link to this definition")

A version of `format_string`, `args`, and/or `kwargs` contain lazy objects. The first argument is the string to be formatted. For example:
```
from django.utils.text import format_lazy
from django.utils.translation import pgettext_lazy

urlpatterns = [
    path(
        format_lazy("{person}/<int:pk>/", person=pgettext_lazy("URL", "person")),
        PersonDetailView.as_view(),
    ),
]

```

This example allows translators to translate part of the URL. If “person” is translated to “persona”, the regular expression will match `persona/(?P<pk>\d+)/$`, e.g. `persona/5/`.

slugify(_value_ , _allow_unicode =False_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/text/#slugify)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.text.slugify "Link to this definition")

Converts a string to a URL slug by:
  1. Converting to ASCII if `allow_unicode` is `False` (the default).
  2. Converting to lowercase.
  3. Removing characters that aren’t alphanumerics, underscores, hyphens, or whitespace.
  4. Replacing any whitespace or repeated dashes with single dashes.
  5. Removing leading and trailing whitespace, dashes, and underscores.


For example:
```
>>> slugify(" Joel is a slug ")
'joel-is-a-slug'

```

If you want to allow Unicode characters, pass `allow_unicode=True`. For example:
```
>>> slugify("你好 World", allow_unicode=True)
'你好-world'

```
