This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/ref/validators/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/ref/validators/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/ref/validators/)
  * [pl](https://docs.djangoproject.com/pl/5.0/ref/validators/)
  * [ko](https://docs.djangoproject.com/ko/5.0/ref/validators/)
  * [ja](https://docs.djangoproject.com/ja/5.0/ref/validators/)
  * [it](https://docs.djangoproject.com/it/5.0/ref/validators/)
  * [id](https://docs.djangoproject.com/id/5.0/ref/validators/)
  * [fr](https://docs.djangoproject.com/fr/5.0/ref/validators/)
  * [es](https://docs.djangoproject.com/es/5.0/ref/validators/)
  * [el](https://docs.djangoproject.com/el/5.0/ref/validators/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/ref/validators/)
  * [6.0](https://docs.djangoproject.com/en/6.0/ref/validators/)
  * [5.2](https://docs.djangoproject.com/en/5.2/ref/validators/)
  * [5.1](https://docs.djangoproject.com/en/5.1/ref/validators/)
  * [4.2](https://docs.djangoproject.com/en/4.2/ref/validators/)
  * [4.1](https://docs.djangoproject.com/en/4.1/ref/validators/)
  * [4.0](https://docs.djangoproject.com/en/4.0/ref/validators/)
  * [3.2](https://docs.djangoproject.com/en/3.2/ref/validators/)
  * [3.1](https://docs.djangoproject.com/en/3.1/ref/validators/)
  * [3.0](https://docs.djangoproject.com/en/3.0/ref/validators/)
  * [2.2](https://docs.djangoproject.com/en/2.2/ref/validators/)
  * [2.1](https://docs.djangoproject.com/en/2.1/ref/validators/)
  * [2.0](https://docs.djangoproject.com/en/2.0/ref/validators/)
  * [1.11](https://docs.djangoproject.com/en/1.11/ref/validators/)
  * [1.10](https://docs.djangoproject.com/en/1.10/ref/validators/)
  * [1.8](https://docs.djangoproject.com/en/1.8/ref/validators/)


  * [](https://docs.djangoproject.com/en/5.0/ref/validators/#top)


# Validators[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#module-django.core.validators "Link to this heading")
## Writing validators[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#writing-validators "Link to this heading")
A validator is a callable that takes a value and raises a [`ValidationError`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.ValidationError "django.core.exceptions.ValidationError") if it doesn’t meet some criteria. Validators can be useful for reusing validation logic between different types of fields.
For example, here’s a validator that only allows even numbers:
```
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            _("%(value)s is not an even number"),
            params={"value": value},
        )

```

You can add this to a model field via the field’s [`validators`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.Field.validators "django.db.models.Field.validators") argument:
```
from django.db import models


class MyModel(models.Model):
    even_field = models.IntegerField(validators=[validate_even])

```

Because values are converted to Python before validators are run, you can even use the same validator with forms:
```
from django import forms


class MyForm(forms.Form):
    even_field = forms.IntegerField(validators=[validate_even])

```

You can also use a class with a `__call__()` method for more complex or configurable validators. [`RegexValidator`](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.RegexValidator "django.core.validators.RegexValidator"), for example, uses this technique. If a class-based validator is used in the [`validators`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.Field.validators "django.db.models.Field.validators") model field option, you should make sure it is [serializable by the migration framework](https://docs.djangoproject.com/en/5.0/topics/migrations/#migration-serializing) by adding [deconstruct()](https://docs.djangoproject.com/en/5.0/topics/migrations/#custom-deconstruct-method) and `__eq__()` methods.
## How validators are run[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#how-validators-are-run "Link to this heading")
See the [form validation](https://docs.djangoproject.com/en/5.0/ref/forms/validation/) for more information on how validators are run in forms, and [Validating objects](https://docs.djangoproject.com/en/5.0/ref/models/instances/#validating-objects) for how they’re run in models. Note that validators will not be run automatically when you save a model, but if you are using a [`ModelForm`](https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/#django.forms.ModelForm "django.forms.ModelForm"), it will run your validators on any fields that are included in your form. See the [ModelForm documentation](https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/) for information on how model validation interacts with forms.
## Built-in validators[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#built-in-validators "Link to this heading")
The [`django.core.validators`](https://docs.djangoproject.com/en/5.0/ref/validators/#module-django.core.validators "django.core.validators: Validation utilities and base classes") module contains a collection of callable validators for use with model and form fields. They’re used internally but are available for use with your own fields, too. They can be used in addition to, or in lieu of custom `field.clean()` methods.
###  `RegexValidator`[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#regexvalidator "Link to this heading")

_class_ RegexValidator(_regex =None_, _message =None_, _code =None_, _inverse_match =None_, _flags =0_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/validators/#RegexValidator)[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.RegexValidator "Link to this definition")


Parameters:

  * **regex** – If not `None`, overrides [`regex`](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.RegexValidator.regex "django.core.validators.RegexValidator.regex"). Can be a regular expression string or a pre-compiled regular expression.
  * **message** – If not `None`, overrides [`message`](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.RegexValidator.message "django.core.validators.RegexValidator.message").
  * **code** – If not `None`, overrides [`code`](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.RegexValidator.code "django.core.validators.RegexValidator.code").
  * **inverse_match** – If not `None`, overrides [`inverse_match`](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.RegexValidator.inverse_match "django.core.validators.RegexValidator.inverse_match").
  * **flags** – If not `None`, overrides [`flags`](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.RegexValidator.flags "django.core.validators.RegexValidator.flags"). In that case, [`regex`](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.RegexValidator.regex "django.core.validators.RegexValidator.regex") must be a regular expression string, or


A [`RegexValidator`](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.RegexValidator "django.core.validators.RegexValidator") searches the provided `value` for a given regular expression with [`ValidationError`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.ValidationError "django.core.exceptions.ValidationError") with [`message`](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.RegexValidator.message "django.core.validators.RegexValidator.message") and [`code`](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.RegexValidator.code "django.core.validators.RegexValidator.code") if a match **is not** found. Its behavior can be inverted by setting [`inverse_match`](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.RegexValidator.inverse_match "django.core.validators.RegexValidator.inverse_match") to `True`, in which case the [`ValidationError`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.ValidationError "django.core.exceptions.ValidationError") is raised when a match **is** found.

regex[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.RegexValidator.regex "Link to this definition")

The regular expression pattern to search for within the provided `value`, using `value`.

message[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.RegexValidator.message "Link to this definition")

The error message used by [`ValidationError`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.ValidationError "django.core.exceptions.ValidationError") if validation fails. Defaults to `"Enter a valid value"`.

code[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.RegexValidator.code "Link to this definition")

The error code used by [`ValidationError`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.ValidationError "django.core.exceptions.ValidationError") if validation fails. Defaults to `"invalid"`.

inverse_match[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.RegexValidator.inverse_match "Link to this definition")

The match mode for [`regex`](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.RegexValidator.regex "django.core.validators.RegexValidator.regex"). Defaults to `False`.

flags[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.RegexValidator.flags "Link to this definition")

The [`regex`](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.RegexValidator.regex "django.core.validators.RegexValidator.regex"). If [`regex`](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.RegexValidator.regex "django.core.validators.RegexValidator.regex") is a pre-compiled regular expression, and [`flags`](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.RegexValidator.flags "django.core.validators.RegexValidator.flags") is overridden, `0`.
###  `EmailValidator`[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#emailvalidator "Link to this heading")

_class_ EmailValidator(_message =None_, _code =None_, _allowlist =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/validators/#EmailValidator)[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.EmailValidator "Link to this definition")


Parameters:

  * **message** – If not `None`, overrides [`message`](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.EmailValidator.message "django.core.validators.EmailValidator.message").
  * **code** – If not `None`, overrides [`code`](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.EmailValidator.code "django.core.validators.EmailValidator.code").
  * **allowlist** – If not `None`, overrides [`allowlist`](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.EmailValidator.allowlist "django.core.validators.EmailValidator.allowlist").


An [`EmailValidator`](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.EmailValidator "django.core.validators.EmailValidator") ensures that a value looks like an email, and raises a [`ValidationError`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.ValidationError "django.core.exceptions.ValidationError") with [`message`](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.EmailValidator.message "django.core.validators.EmailValidator.message") and [`code`](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.EmailValidator.code "django.core.validators.EmailValidator.code") if it doesn’t. Values longer than 320 characters are always considered invalid.

message[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.EmailValidator.message "Link to this definition")

The error message used by [`ValidationError`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.ValidationError "django.core.exceptions.ValidationError") if validation fails. Defaults to `"Enter a valid email address"`.

code[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.EmailValidator.code "Link to this definition")

The error code used by [`ValidationError`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.ValidationError "django.core.exceptions.ValidationError") if validation fails. Defaults to `"invalid"`.

allowlist[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.EmailValidator.allowlist "Link to this definition")

Allowlist of email domains. By default, a regular expression (the `domain_regex` attribute) is used to validate whatever appears after the `@` sign. However, if that string appears in the `allowlist`, this validation is bypassed. If not provided, the default `allowlist` is `['localhost']`. Other domains that don’t contain a dot won’t pass validation, so you’d need to add them to the `allowlist` as necessary.
Changed in Django 3.2.20:
In older versions, values longer than 320 characters could be considered valid.
###  `URLValidator`[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#urlvalidator "Link to this heading")

_class_ URLValidator(_schemes =None_, _regex =None_, _message =None_, _code =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/validators/#URLValidator)[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.URLValidator "Link to this definition")

A [`RegexValidator`](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.RegexValidator "django.core.validators.RegexValidator") subclass that ensures a value looks like a URL, and raises an error code of `'invalid'` if it doesn’t. Values longer than [`max_length`](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.URLValidator.max_length "django.core.validators.URLValidator.max_length") characters are always considered invalid.
Loopback addresses and reserved IP spaces are considered valid. Literal IPv6 addresses (
In addition to the optional arguments of its parent [`RegexValidator`](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.RegexValidator "django.core.validators.RegexValidator") class, `URLValidator` accepts an extra optional attribute:

schemes[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.URLValidator.schemes "Link to this definition")

URL/URI scheme list to validate against. If not provided, the default list is `['http', 'https', 'ftp', 'ftps']`. As a reference, the IANA website provides a full list of
Warning
Values starting with `file:///` will not pass validation even when the `file` scheme is provided. Valid values must contain a host.

max_length[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.URLValidator.max_length "Link to this definition")

New in Django 3.2.20.
The maximum length of values that could be considered valid. Defaults to 2048 characters.
Changed in Django 3.2.20:
In older versions, values longer than 2048 characters could be considered valid.
###  `validate_email`[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#validate-email "Link to this heading")

validate_email[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.validate_email "Link to this definition")

An [`EmailValidator`](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.EmailValidator "django.core.validators.EmailValidator") instance without any customizations.
###  `validate_slug`[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#validate-slug "Link to this heading")

validate_slug[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.validate_slug "Link to this definition")

A [`RegexValidator`](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.RegexValidator "django.core.validators.RegexValidator") instance that ensures a value consists of only letters, numbers, underscores or hyphens.
###  `validate_unicode_slug`[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#validate-unicode-slug "Link to this heading")

validate_unicode_slug[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.validate_unicode_slug "Link to this definition")

A [`RegexValidator`](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.RegexValidator "django.core.validators.RegexValidator") instance that ensures a value consists of only Unicode letters, numbers, underscores, or hyphens.
###  `validate_ipv4_address`[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#validate-ipv4-address "Link to this heading")

validate_ipv4_address[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/validators/#validate_ipv4_address)[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.validate_ipv4_address "Link to this definition")

A [`RegexValidator`](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.RegexValidator "django.core.validators.RegexValidator") instance that ensures a value looks like an IPv4 address.
###  `validate_ipv6_address`[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#validate-ipv6-address "Link to this heading")

validate_ipv6_address[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/validators/#validate_ipv6_address)[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.validate_ipv6_address "Link to this definition")

Uses `django.utils.ipv6` to check the validity of an IPv6 address.
###  `validate_ipv46_address`[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#validate-ipv46-address "Link to this heading")

validate_ipv46_address[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/validators/#validate_ipv46_address)[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.validate_ipv46_address "Link to this definition")

Uses both `validate_ipv4_address` and `validate_ipv6_address` to ensure a value is either a valid IPv4 or IPv6 address.
###  `validate_comma_separated_integer_list`[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#validate-comma-separated-integer-list "Link to this heading")

validate_comma_separated_integer_list[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.validate_comma_separated_integer_list "Link to this definition")

A [`RegexValidator`](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.RegexValidator "django.core.validators.RegexValidator") instance that ensures a value is a comma-separated list of integers.
###  `int_list_validator`[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#int-list-validator "Link to this heading")

int_list_validator(_sep =','_, _message =None_, _code ='invalid'_, _allow_negative =False_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/validators/#int_list_validator)[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.int_list_validator "Link to this definition")

Returns a [`RegexValidator`](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.RegexValidator "django.core.validators.RegexValidator") instance that ensures a string consists of integers separated by `sep`. It allows negative integers when `allow_negative` is `True`.
###  `MaxValueValidator`[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#maxvaluevalidator "Link to this heading")

_class_ MaxValueValidator(_limit_value_ , _message =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/validators/#MaxValueValidator)[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.MaxValueValidator "Link to this definition")

Raises a [`ValidationError`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.ValidationError "django.core.exceptions.ValidationError") with a code of `'max_value'` if `value` is greater than `limit_value`, which may be a callable.
###  `MinValueValidator`[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#minvaluevalidator "Link to this heading")

_class_ MinValueValidator(_limit_value_ , _message =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/validators/#MinValueValidator)[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.MinValueValidator "Link to this definition")

Raises a [`ValidationError`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.ValidationError "django.core.exceptions.ValidationError") with a code of `'min_value'` if `value` is less than `limit_value`, which may be a callable.
###  `MaxLengthValidator`[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#maxlengthvalidator "Link to this heading")

_class_ MaxLengthValidator(_limit_value_ , _message =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/validators/#MaxLengthValidator)[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.MaxLengthValidator "Link to this definition")

Raises a [`ValidationError`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.ValidationError "django.core.exceptions.ValidationError") with a code of `'max_length'` if the length of `value` is greater than `limit_value`, which may be a callable.
###  `MinLengthValidator`[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#minlengthvalidator "Link to this heading")

_class_ MinLengthValidator(_limit_value_ , _message =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/validators/#MinLengthValidator)[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.MinLengthValidator "Link to this definition")

Raises a [`ValidationError`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.ValidationError "django.core.exceptions.ValidationError") with a code of `'min_length'` if the length of `value` is less than `limit_value`, which may be a callable.
###  `DecimalValidator`[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#decimalvalidator "Link to this heading")

_class_ DecimalValidator(_max_digits_ , _decimal_places_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/validators/#DecimalValidator)[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.DecimalValidator "Link to this definition")

Raises [`ValidationError`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.ValidationError "django.core.exceptions.ValidationError") with the following codes:
  * `'max_digits'` if the number of digits is larger than `max_digits`.
  * `'max_decimal_places'` if the number of decimals is larger than `decimal_places`.
  * `'max_whole_digits'` if the number of whole digits is larger than the difference between `max_digits` and `decimal_places`.


###  `FileExtensionValidator`[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#fileextensionvalidator "Link to this heading")

_class_ FileExtensionValidator(_allowed_extensions_ , _message_ , _code_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/validators/#FileExtensionValidator)[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.FileExtensionValidator "Link to this definition")

Raises a [`ValidationError`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.ValidationError "django.core.exceptions.ValidationError") with a code of `'invalid_extension'` if the extension of `value.name` (`value` is a [`File`](https://docs.djangoproject.com/en/5.0/ref/files/file/#django.core.files.File "django.core.files.File")) isn’t found in `allowed_extensions`. The extension is compared case-insensitively with `allowed_extensions`.
Warning
Don’t rely on validation of the file extension to determine a file’s type. Files can be renamed to have any extension no matter what data they contain.
###  `validate_image_file_extension`[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#validate-image-file-extension "Link to this heading")

validate_image_file_extension[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/validators/#validate_image_file_extension)[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.validate_image_file_extension "Link to this definition")

Uses Pillow to ensure that `value.name` (`value` is a [`File`](https://docs.djangoproject.com/en/5.0/ref/files/file/#django.core.files.File "django.core.files.File")) has
###  `ProhibitNullCharactersValidator`[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#prohibitnullcharactersvalidator "Link to this heading")

_class_ ProhibitNullCharactersValidator(_message =None_, _code =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/validators/#ProhibitNullCharactersValidator)[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.ProhibitNullCharactersValidator "Link to this definition")

Raises a [`ValidationError`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.ValidationError "django.core.exceptions.ValidationError") if `str(value)` contains one or more null characters (`'\x00'`).

Parameters:

  * **message** – If not `None`, overrides [`message`](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.ProhibitNullCharactersValidator.message "django.core.validators.ProhibitNullCharactersValidator.message").
  * **code** – If not `None`, overrides [`code`](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.ProhibitNullCharactersValidator.code "django.core.validators.ProhibitNullCharactersValidator.code").



message[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.ProhibitNullCharactersValidator.message "Link to this definition")

The error message used by [`ValidationError`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.ValidationError "django.core.exceptions.ValidationError") if validation fails. Defaults to `"Null characters are not allowed."`.

code[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.ProhibitNullCharactersValidator.code "Link to this definition")

The error code used by [`ValidationError`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.ValidationError "django.core.exceptions.ValidationError") if validation fails. Defaults to `"null_characters_not_allowed"`.
###  `StepValueValidator`[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#stepvaluevalidator "Link to this heading")

_class_ StepValueValidator(_limit_value_ , _message =None_, _offset =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/validators/#StepValueValidator)[¶](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.StepValueValidator "Link to this definition")

Raises a [`ValidationError`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.ValidationError "django.core.exceptions.ValidationError") with a code of `'step_size'` if `value` is not an integral multiple of `limit_value`, which can be a float, integer or decimal value or a callable. When `offset` is set, the validation occurs against `limit_value` plus `offset`. For example, for `StepValueValidator(3, offset=1.4)` valid values include `1.4`, `4.4`, `7.4`, `10.4`, and so on.
Changed in Django 5.0:
The `offset` argument was added. Previous page and next page
[](https://docs.djangoproject.com/en/5.0/ref/utils/)
[Built-in Views ](https://docs.djangoproject.com/en/5.0/ref/views/)
[](https://docs.djangoproject.com/en/5.0/ref/validators/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Marco Rougeth donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [Validators](https://docs.djangoproject.com/en/5.0/ref/validators/)
    * [Writing validators](https://docs.djangoproject.com/en/5.0/ref/validators/#writing-validators)
    * [How validators are run](https://docs.djangoproject.com/en/5.0/ref/validators/#how-validators-are-run)
    * [Built-in validators](https://docs.djangoproject.com/en/5.0/ref/validators/#built-in-validators)
      * [`RegexValidator`](https://docs.djangoproject.com/en/5.0/ref/validators/#regexvalidator)
      * [`EmailValidator`](https://docs.djangoproject.com/en/5.0/ref/validators/#emailvalidator)
      * [`URLValidator`](https://docs.djangoproject.com/en/5.0/ref/validators/#urlvalidator)
      * [`validate_email`](https://docs.djangoproject.com/en/5.0/ref/validators/#validate-email)
      * [`validate_slug`](https://docs.djangoproject.com/en/5.0/ref/validators/#validate-slug)
      * [`validate_unicode_slug`](https://docs.djangoproject.com/en/5.0/ref/validators/#validate-unicode-slug)
      * [`validate_ipv4_address`](https://docs.djangoproject.com/en/5.0/ref/validators/#validate-ipv4-address)
      * [`validate_ipv6_address`](https://docs.djangoproject.com/en/5.0/ref/validators/#validate-ipv6-address)
      * [`validate_ipv46_address`](https://docs.djangoproject.com/en/5.0/ref/validators/#validate-ipv46-address)
      * [`validate_comma_separated_integer_list`](https://docs.djangoproject.com/en/5.0/ref/validators/#validate-comma-separated-integer-list)
      * [`int_list_validator`](https://docs.djangoproject.com/en/5.0/ref/validators/#int-list-validator)
      * [`MaxValueValidator`](https://docs.djangoproject.com/en/5.0/ref/validators/#maxvaluevalidator)
      * [`MinValueValidator`](https://docs.djangoproject.com/en/5.0/ref/validators/#minvaluevalidator)
      * [`MaxLengthValidator`](https://docs.djangoproject.com/en/5.0/ref/validators/#maxlengthvalidator)
      * [`MinLengthValidator`](https://docs.djangoproject.com/en/5.0/ref/validators/#minlengthvalidator)
      * [`DecimalValidator`](https://docs.djangoproject.com/en/5.0/ref/validators/#decimalvalidator)
      * [`FileExtensionValidator`](https://docs.djangoproject.com/en/5.0/ref/validators/#fileextensionvalidator)
      * [`validate_image_file_extension`](https://docs.djangoproject.com/en/5.0/ref/validators/#validate-image-file-extension)
      * [`ProhibitNullCharactersValidator`](https://docs.djangoproject.com/en/5.0/ref/validators/#prohibitnullcharactersvalidator)
      * [`StepValueValidator`](https://docs.djangoproject.com/en/5.0/ref/validators/#stepvaluevalidator)


### Browse
  * Prev: [Django Utils](https://docs.djangoproject.com/en/5.0/ref/utils/)
  * Next: [Built-in Views](https://docs.djangoproject.com/en/5.0/ref/views/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [API Reference](https://docs.djangoproject.com/en/5.0/ref/)
      * Validators


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
