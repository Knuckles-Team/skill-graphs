##  `django.utils.html`[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#module-django.utils.html "Link to this heading")
Usually you should build up HTML using Django’s templates to make use of its autoescape mechanism, using the utilities in [`django.utils.safestring`](https://docs.djangoproject.com/en/5.0/ref/utils/#module-django.utils.safestring "django.utils.safestring: Functions and classes for working with strings that can be displayed safely without further escaping in HTML.") where appropriate. This module provides some additional low level utilities for escaping HTML.

escape(_text_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/html/#escape)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.html.escape "Link to this definition")

Returns the given text with ampersands, quotes and angle brackets encoded for use in HTML. The input is first coerced to a string and the output has [`mark_safe()`](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.safestring.mark_safe "django.utils.safestring.mark_safe") applied.

conditional_escape(_text_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/html/#conditional_escape)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.html.conditional_escape "Link to this definition")

Similar to `escape()`, except that it doesn’t operate on preescaped strings, so it will not double escape.

format_html(_format_string_ , _* args_, _** kwargs_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/html/#format_html)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.html.format_html "Link to this definition")

This is similar to `format_string` is not escaped but all other args and kwargs are passed through [`conditional_escape()`](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.html.conditional_escape "django.utils.html.conditional_escape") before being passed to `str.format()`. Finally, the output has [`mark_safe()`](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.safestring.mark_safe "django.utils.safestring.mark_safe") applied.
For the case of building up small HTML fragments, this function is to be preferred over string interpolation using `%` or `str.format()` directly, because it applies escaping to all arguments - just like the template system applies escaping by default.
So, instead of writing:
```
mark_safe(
    "%s <b>%s</b> %s"
    % (
        some_html,
        escape(some_text),
        escape(some_other_text),
    )
)

```

You should instead use:
```
format_html(
    "{} <b>{}</b> {}",
    mark_safe(some_html),
    some_text,
    some_other_text,
)

```

This has the advantage that you don’t need to apply [`escape()`](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.html.escape "django.utils.html.escape") to each argument and risk a bug and an XSS vulnerability if you forget one.
Note that although this function uses `str.format()` to do the interpolation, some of the formatting options provided by `str.format()` (e.g. number formatting) will not work, since all arguments are passed through [`conditional_escape()`](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.html.conditional_escape "django.utils.html.conditional_escape") which (ultimately) calls [`force_str()`](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.encoding.force_str "django.utils.encoding.force_str") on the values.
Deprecated since version 5.0: Support for calling `format_html()` without passing args or kwargs is deprecated.

format_html_join(_sep_ , _format_string_ , _args_generator_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/html/#format_html_join)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.html.format_html_join "Link to this definition")

A wrapper of [`format_html()`](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.html.format_html "django.utils.html.format_html"), for the common case of a group of arguments that need to be formatted using the same format string, and then joined using `sep`. `sep` is also passed through [`conditional_escape()`](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.html.conditional_escape "django.utils.html.conditional_escape").
`args_generator` should be an iterator that returns the sequence of `args` that will be passed to [`format_html()`](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.html.format_html "django.utils.html.format_html"). For example:
```
format_html_join("\n", "<li>{} {}</li>", ((u.first_name, u.last_name) for u in users))

```


json_script(_value_ , _element_id =None_, _encoder =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/html/#json_script)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.html.json_script "Link to this definition")

Escapes all HTML/XML special characters with their Unicode escapes, so value is safe for use with JavaScript. Also wraps the escaped JSON in a `<script>` tag. If the `element_id` parameter is not `None`, the `<script>` tag is given the passed id. For example:
```
>>> json_script({"hello": "world"}, element_id="hello-data")
'<script id="hello-data" type="application/json">{"hello": "world"}</script>'

```

The `encoder`, which defaults to [`django.core.serializers.json.DjangoJSONEncoder`](https://docs.djangoproject.com/en/5.0/topics/serialization/#django.core.serializers.json.DjangoJSONEncoder "django.core.serializers.json.DjangoJSONEncoder"), will be used to serialize the data. See [JSON serialization](https://docs.djangoproject.com/en/5.0/topics/serialization/#serialization-formats-json) for more details about this serializer.
Changed in Django 4.2:
The `encoder` argument was added.

strip_tags(_value_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/html/#strip_tags)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.html.strip_tags "Link to this definition")

Tries to remove anything that looks like an HTML tag from the string, that is anything contained within `<>`.
Absolutely NO guarantee is provided about the resulting string being HTML safe. So NEVER mark safe the result of a `strip_tag` call without escaping it first, for example with [`escape()`](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.html.escape "django.utils.html.escape").
For example:
```
strip_tags(value)

```

If `value` is `"<b>Joel</b> <button>is</button> a <span>slug</span>"` the return value will be `"Joel is a slug"`.
If you are looking for a more robust solution, consider using a third-party HTML sanitizing tool.

html_safe()[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/html/#html_safe)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.html.html_safe "Link to this definition")

The `__html__()` method on a class helps non-Django templates detect classes whose output doesn’t require HTML escaping.
This decorator defines the `__html__()` method on the decorated class by wrapping `__str__()` in [`mark_safe()`](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.safestring.mark_safe "django.utils.safestring.mark_safe"). Ensure the `__str__()` method does indeed return text that doesn’t require HTML escaping.
