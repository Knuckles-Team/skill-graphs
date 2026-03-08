##  `django.utils.translation`[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#module-django.utils.translation "Link to this heading")
For a complete discussion on the usage of the following see the [translation documentation](https://docs.djangoproject.com/en/5.0/topics/i18n/translation/).

gettext(_message_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/translation/#gettext)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.translation.gettext "Link to this definition")

Translates `message` and returns it as a string.

pgettext(_context_ , _message_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/translation/#pgettext)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.translation.pgettext "Link to this definition")

Translates `message` given the `context` and returns it as a string.
For more information, see [Contextual markers](https://docs.djangoproject.com/en/5.0/topics/i18n/translation/#contextual-markers).

gettext_lazy(_message_)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.translation.gettext_lazy "Link to this definition")


pgettext_lazy(_context_ , _message_)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.translation.pgettext_lazy "Link to this definition")

Same as the non-lazy versions above, but using lazy execution.
See [lazy translations documentation](https://docs.djangoproject.com/en/5.0/topics/i18n/translation/#lazy-translations).

gettext_noop(_message_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/translation/#gettext_noop)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.translation.gettext_noop "Link to this definition")

Marks strings for translation but doesn’t translate them now. This can be used to store strings in global variables that should stay in the base language (because they might be used externally) and will be translated later.

ngettext(_singular_ , _plural_ , _number_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/translation/#ngettext)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.translation.ngettext "Link to this definition")

Translates `singular` and `plural` and returns the appropriate string based on `number`.

npgettext(_context_ , _singular_ , _plural_ , _number_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/translation/#npgettext)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.translation.npgettext "Link to this definition")

Translates `singular` and `plural` and returns the appropriate string based on `number` and the `context`.

ngettext_lazy(_singular_ , _plural_ , _number_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/translation/#ngettext_lazy)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.translation.ngettext_lazy "Link to this definition")


npgettext_lazy(_context_ , _singular_ , _plural_ , _number_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/translation/#npgettext_lazy)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.translation.npgettext_lazy "Link to this definition")

Same as the non-lazy versions above, but using lazy execution.
See [lazy translations documentation](https://docs.djangoproject.com/en/5.0/topics/i18n/translation/#lazy-translations).

activate(_language_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/translation/#activate)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.translation.activate "Link to this definition")

Fetches the translation object for a given language and activates it as the current translation object for the current thread.

deactivate()[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/translation/#deactivate)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.translation.deactivate "Link to this definition")

Deactivates the currently active translation object so that further _ calls will resolve against the default translation object, again.

deactivate_all()[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/translation/#deactivate_all)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.translation.deactivate_all "Link to this definition")

Makes the active translation object a `NullTranslations()` instance. This is useful when we want delayed translations to appear as the original string for some reason.

override(_language_ , _deactivate =False_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/translation/#override)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.translation.override "Link to this definition")

A Python context manager that uses [`django.utils.translation.activate()`](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.translation.activate "django.utils.translation.activate") to fetch the translation object for a given language, activates it as the translation object for the current thread and reactivates the previous active language on exit. Optionally, it can deactivate the temporary translation on exit with [`django.utils.translation.deactivate()`](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.translation.deactivate "django.utils.translation.deactivate") if the `deactivate` argument is `True`. If you pass `None` as the language argument, a `NullTranslations()` instance is activated within the context.
`override` is also usable as a function decorator.

check_for_language(_lang_code_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/translation/#check_for_language)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.translation.check_for_language "Link to this definition")

Checks whether there is a global language file for the given language code (e.g. ‘fr’, ‘pt_BR’). This is used to decide whether a user-provided language is available.

get_language()[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/translation/#get_language)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.translation.get_language "Link to this definition")

Returns the currently selected language code. Returns `None` if translations are temporarily deactivated (by [`deactivate_all()`](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.translation.deactivate_all "django.utils.translation.deactivate_all") or when `None` is passed to [`override()`](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.translation.override "django.utils.translation.override")).

get_language_bidi()[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/translation/#get_language_bidi)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.translation.get_language_bidi "Link to this definition")

Returns selected language’s BiDi layout:
  * `False` = left-to-right layout
  * `True` = right-to-left layout



get_language_from_request(_request_ , _check_path =False_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/translation/#get_language_from_request)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.translation.get_language_from_request "Link to this definition")

Analyzes the request to find what language the user wants the system to show. Only languages listed in settings.LANGUAGES are taken into account. If the user requests a sublanguage where we have a main language, we send out the main language.
If `check_path` is `True`, the function first checks the requested URL for whether its path begins with a language code listed in the [`LANGUAGES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-LANGUAGES) setting.

get_supported_language_variant(_lang_code_ , _strict =False_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/translation/#get_supported_language_variant)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.translation.get_supported_language_variant "Link to this definition")

Returns `lang_code` if it’s in the [`LANGUAGES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-LANGUAGES) setting, possibly selecting a more generic variant. For example, `'es'` is returned if `lang_code` is `'es-ar'` and `'es'` is in [`LANGUAGES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-LANGUAGES) but `'es-ar'` isn’t.
`lang_code` has a maximum accepted length of 500 characters. A `lang_code` exceeds this limit and `strict` is `True`, or if there is no generic variant and `strict` is `False`.
If `strict` is `False` (the default), a country-specific variant may be returned when neither the language code nor its generic variant is found. For example, if only `'es-co'` is in [`LANGUAGES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-LANGUAGES), that’s returned for `lang_code`s like `'es'` and `'es-ar'`. Those matches aren’t returned if `strict=True`.
Raises
Changed in Django 4.2.15:
In older versions, `lang_code` values over 500 characters were processed without raising a

to_locale(_language_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/translation/#to_locale)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.translation.to_locale "Link to this definition")

Turns a language name (en-us) into a locale name (en_US).

templatize(_src_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/translation/#templatize)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.translation.templatize "Link to this definition")

Turns a Django template into something that is understood by `xgettext`. It does so by translating the Django translation tags into standard `gettext` function invocations. Previous page and next page
[`django.urls` functions for use in URLconfs](https://docs.djangoproject.com/en/5.0/ref/urls/)
[Validators ](https://docs.djangoproject.com/en/5.0/ref/validators/)
[](https://docs.djangoproject.com/en/5.0/ref/utils/#top)
