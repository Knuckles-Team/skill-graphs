[Skip to main content](https://docs.djangoproject.com/en/6.0/ref/forms/validation/#main-content)
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
[Documentation](https://docs.djangoproject.com/en/6.0/)
  * [ Getting Help ](https://docs.djangoproject.com/en/6.0/faq/help/)


  * Language: **en**
  * [zh-hans](https://docs.djangoproject.com/zh-hans/6.0/ref/forms/validation/)
  * [sv](https://docs.djangoproject.com/sv/6.0/ref/forms/validation/)
  * [pt-br](https://docs.djangoproject.com/pt-br/6.0/ref/forms/validation/)
  * [pl](https://docs.djangoproject.com/pl/6.0/ref/forms/validation/)
  * [ko](https://docs.djangoproject.com/ko/6.0/ref/forms/validation/)
  * [ja](https://docs.djangoproject.com/ja/6.0/ref/forms/validation/)
  * [it](https://docs.djangoproject.com/it/6.0/ref/forms/validation/)
  * [id](https://docs.djangoproject.com/id/6.0/ref/forms/validation/)
  * [fr](https://docs.djangoproject.com/fr/6.0/ref/forms/validation/)
  * [es](https://docs.djangoproject.com/es/6.0/ref/forms/validation/)
  * [el](https://docs.djangoproject.com/el/6.0/ref/forms/validation/)


  * Documentation version: **6.0**
  * [dev](https://docs.djangoproject.com/en/dev/ref/forms/validation/)
  * [5.2](https://docs.djangoproject.com/en/5.2/ref/forms/validation/)
  * [5.1](https://docs.djangoproject.com/en/5.1/ref/forms/validation/)
  * [5.0](https://docs.djangoproject.com/en/5.0/ref/forms/validation/)
  * [4.2](https://docs.djangoproject.com/en/4.2/ref/forms/validation/)
  * [4.1](https://docs.djangoproject.com/en/4.1/ref/forms/validation/)
  * [4.0](https://docs.djangoproject.com/en/4.0/ref/forms/validation/)
  * [3.2](https://docs.djangoproject.com/en/3.2/ref/forms/validation/)
  * [3.1](https://docs.djangoproject.com/en/3.1/ref/forms/validation/)
  * [3.0](https://docs.djangoproject.com/en/3.0/ref/forms/validation/)
  * [2.2](https://docs.djangoproject.com/en/2.2/ref/forms/validation/)
  * [2.1](https://docs.djangoproject.com/en/2.1/ref/forms/validation/)
  * [2.0](https://docs.djangoproject.com/en/2.0/ref/forms/validation/)
  * [1.11](https://docs.djangoproject.com/en/1.11/ref/forms/validation/)
  * [1.10](https://docs.djangoproject.com/en/1.10/ref/forms/validation/)
  * [1.8](https://docs.djangoproject.com/en/1.8/ref/forms/validation/)


  * [](https://docs.djangoproject.com/en/6.0/ref/forms/validation/#top)


# Form and field validation[¶](https://docs.djangoproject.com/en/6.0/ref/forms/validation/#form-and-field-validation "Link to this heading")
Form validation happens when the data is cleaned. If you want to customize this process, there are various places to make changes, each one serving a different purpose. Three types of cleaning methods are run during form processing. These are normally executed when you call the `is_valid()` method on a form. There are other things that can also trigger cleaning and validation (accessing the `errors` attribute or calling `full_clean()` directly), but normally they won’t be needed.
In general, any cleaning method can raise `ValidationError` if there is a problem with the data it is processing, passing the relevant information to the `ValidationError` constructor. [See below](https://docs.djangoproject.com/en/6.0/ref/forms/validation/#raising-validation-error) for the best practice in raising `ValidationError`. If no `ValidationError` is raised, the method should return the cleaned (normalized) data as a Python object.
Most validation can be done using [validators](https://docs.djangoproject.com/en/6.0/ref/forms/validation/#validators) - helpers that can be reused. Validators are functions (or callables) that take a single argument and raise `ValidationError` on invalid input. Validators are run after the field’s `to_python` and `validate` methods have been called.
Validation of a form is split into several steps, which can be customized or overridden:
  * The `to_python()` method on a `Field` is the first step in every validation. It coerces the value to a correct datatype and raises `ValidationError` if that is not possible. This method accepts the raw value from the widget and returns the converted value. For example, a `FloatField` will turn the data into a Python `float` or raise a `ValidationError`.
  * The `validate()` method on a `Field` handles field-specific validation that is not suitable for a validator. It takes a value that has been coerced to a correct datatype and raises `ValidationError` on any error. This method does not return anything and shouldn’t alter the value. You should override it to handle validation logic that you can’t or don’t want to put in a validator.
  * The `run_validators()` method on a `Field` runs all of the field’s validators and aggregates all the errors into a single `ValidationError`. You shouldn’t need to override this method.
  * The `clean()` method on a `Field` subclass is responsible for running `to_python()`, `validate()`, and `run_validators()` in the correct order and propagating their errors. If, at any time, any of the methods raise `ValidationError`, the validation stops and that error is raised. This method returns the clean data, which is then inserted into the `cleaned_data` dictionary of the form.
  * The `clean_<fieldname>()` method is called on a form subclass – where `<fieldname>` is replaced with the name of the form field attribute. This method does any cleaning that is specific to that particular attribute, unrelated to the type of field that it is. This method is not passed any parameters. You will need to look up the value of the field in `self.cleaned_data` and remember that it will be a Python object at this point, not the original string submitted in the form (it will be in `cleaned_data` because the general field `clean()` method, above, has already cleaned the data once).
For example, if you wanted to validate that the contents of a `CharField` called `serialnumber` was unique, `clean_serialnumber()` would be the right place to do this. You don’t need a specific field (it’s a `CharField`), but you want a formfield-specific piece of validation and, possibly, cleaning/normalizing the data.
The return value of this method replaces the existing value in `cleaned_data`, so it must be the field’s value from `cleaned_data` (even if this method didn’t change it) or a new cleaned value.
  * The form subclass’s `clean()` method can perform validation that requires access to multiple form fields. This is where you might put in checks such as “if field `A` is supplied, field `B` must contain a valid email address”. This method can return a completely different dictionary if it wishes, which will be used as the `cleaned_data`.
Since the field validation methods have been run by the time `clean()` is called, you also have access to the form’s `errors` attribute which contains all the errors raised by cleaning of individual fields.
Note that any errors raised by your [`Form.clean()`](https://docs.djangoproject.com/en/6.0/ref/forms/api/#django.forms.Form.clean "django.forms.Form.clean") override will not be associated with any field in particular. They go into a special “field” (called `__all__`), which you can access via the [`non_field_errors()`](https://docs.djangoproject.com/en/6.0/ref/forms/api/#django.forms.Form.non_field_errors "django.forms.Form.non_field_errors") method if you need to. If you want to attach errors to a specific field in the form, you need to call [`add_error()`](https://docs.djangoproject.com/en/6.0/ref/forms/api/#django.forms.Form.add_error "django.forms.Form.add_error").
Also note that there are special considerations when overriding the `clean()` method of a `ModelForm` subclass. (see the [ModelForm documentation](https://docs.djangoproject.com/en/6.0/topics/forms/modelforms/#overriding-modelform-clean-method) for more information)


These methods are run in the order given above, one field at a time. That is, for each field in the form (in the order they are declared in the form definition), the `Field.clean()` method (or its override) is run, then `clean_<fieldname>()`. Finally, once those two methods are run for every field, the [`Form.clean()`](https://docs.djangoproject.com/en/6.0/ref/forms/api/#django.forms.Form.clean "django.forms.Form.clean") method, or its override, is executed whether or not the previous methods have raised errors.
Examples of each of these methods are provided below.
As mentioned, any of these methods can raise a `ValidationError`. For any field, if the `Field.clean()` method raises a `ValidationError`, any field-specific cleaning method is not called. However, the cleaning methods for all remaining fields are still executed.
## Raising `ValidationError`[¶](https://docs.djangoproject.com/en/6.0/ref/forms/validation/#raising-validationerror "Link to this heading")
In order to make error messages flexible and easy to override, consider the following guidelines:
  * Provide a descriptive error `code` to the constructor:
```
# Good
ValidationError(_("Invalid value"), code="invalid")

# Bad
ValidationError(_("Invalid value"))

```

  * Don’t coerce variables into the message; use placeholders and the `params` argument of the constructor:
```
# Good
ValidationError(
    _("Invalid value: %(value)s"),
    params={"value": "42"},
)

# Bad
ValidationError(_("Invalid value: %s") % value)

```

  * Use mapping keys instead of positional formatting. This enables putting the variables in any order or omitting them altogether when rewriting the message:
```
# Good
ValidationError(
    _("Invalid value: %(value)s"),
    params={"value": "42"},
)

# Bad
ValidationError(
    _("Invalid value: %s"),
    params=("42",),
)

```

  * Wrap the message with `gettext` to enable translation:
```
# Good
ValidationError(_("Invalid value"))

# Bad
ValidationError("Invalid value")

```



Putting it all together:
```
raise ValidationError(
    _("Invalid value: %(value)s"),
    code="invalid",
    params={"value": "42"},
)

```

Following these guidelines is particularly necessary if you write reusable forms, form fields, and model fields.
While not recommended, if you are at the end of the validation chain (i.e. your form `clean()` method) and you know you will _never_ need to override your error message you can still opt for the less verbose:
```
ValidationError(_("Invalid value: %s") % value)

```

The [`Form.errors.as_data()`](https://docs.djangoproject.com/en/6.0/ref/forms/api/#django.forms.Form.errors.as_data "django.forms.Form.errors.as_data") and [`Form.errors.as_json()`](https://docs.djangoproject.com/en/6.0/ref/forms/api/#django.forms.Form.errors.as_json "django.forms.Form.errors.as_json") methods greatly benefit from fully featured `ValidationError`s (with a `code` name and a `params` dictionary).
### Raising multiple errors[¶](https://docs.djangoproject.com/en/6.0/ref/forms/validation/#raising-multiple-errors "Link to this heading")
If you detect multiple errors during a cleaning method and wish to signal all of them to the form submitter, it is possible to pass a list of errors to the `ValidationError` constructor.
As above, it is recommended to pass a list of `ValidationError` instances with `code`s and `params` but a list of strings will also work:
```
# Good
raise ValidationError(
    [
        ValidationError(_("Error 1"), code="error1"),
        ValidationError(_("Error 2"), code="error2"),
    ]
)

# Bad
raise ValidationError(
    [
        _("Error 1"),
        _("Error 2"),
    ]
)

```

## Using validation in practice[¶](https://docs.djangoproject.com/en/6.0/ref/forms/validation/#using-validation-in-practice "Link to this heading")
The previous sections explained how validation works in general for forms. Since it can sometimes be easier to put things into place by seeing each feature in use, here are a series of small examples that use each of the previous features.
### Using validators[¶](https://docs.djangoproject.com/en/6.0/ref/forms/validation/#using-validators "Link to this heading")
Django’s form (and model) fields support use of utility functions and classes known as validators. A validator is a callable object or function that takes a value and returns nothing if the value is valid or raises a [`ValidationError`](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.core.exceptions.ValidationError "django.core.exceptions.ValidationError") if not. These can be passed to a field’s constructor, via the field’s `validators` argument, or defined on the [`Field`](https://docs.djangoproject.com/en/6.0/ref/forms/fields/#django.forms.Field "django.forms.Field") class itself with the `default_validators` attribute.
Validators can be used to validate values inside the field, let’s have a look at Django’s `SlugField`:
```
from django.core import validators
from django.forms import CharField


class SlugField(CharField):
    default_validators = [validators.validate_slug]

```

As you can see, `SlugField` is a `CharField` with a customized validator that validates that submitted text obeys to some character rules. This can also be done on field definition so:
```
slug = forms.SlugField()

```

is equivalent to:
```
slug = forms.CharField(validators=[validators.validate_slug])

```

Common cases such as validating against an email or a regular expression can be handled using existing validator classes available in Django. For example, `validators.validate_slug` is an instance of a [`RegexValidator`](https://docs.djangoproject.com/en/6.0/ref/validators/#django.core.validators.RegexValidator "django.core.validators.RegexValidator") constructed with the first argument being the pattern: `^[-a-zA-Z0-9_]+\Z`. See the section on [writing validators](https://docs.djangoproject.com/en/6.0/ref/validators/) to see a list of what is already available and for an example of how to write a validator.
### Form field default cleaning[¶](https://docs.djangoproject.com/en/6.0/ref/forms/validation/#form-field-default-cleaning "Link to this heading")
Let’s first create a custom form field that validates its input is a string containing comma-separated email addresses. The full class looks like this:
```
from django import forms
from django.core.validators import validate_email


class MultiEmailField(forms.Field):
    def to_python(self, value):
        """Normalize data to a list of strings."""
        # Return an empty list if no input was given.
        if not value:
            return []
        return value.split(",")

    def validate(self, value):
        """Check if value consists only of valid emails."""
        # Use the parent's handling of required fields, etc.
        super().validate(value)
        for email in value:
            validate_email(email)

```

Every form that uses this field will have these methods run before anything else can be done with the field’s data. This is cleaning that is specific to this type of field, regardless of how it is subsequently used.
Let’s create a `ContactForm` to demonstrate how you’d use this field:
```
class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()
    recipients = MultiEmailField()
    cc_myself = forms.BooleanField(required=False)

```

Use `MultiEmailField` like any other form field. When the `is_valid()` method is called on the form, the `MultiEmailField.clean()` method will be run as part of the cleaning process and it will, in turn, call the custom `to_python()` and `validate()` methods.
### Cleaning a specific field attribute[¶](https://docs.djangoproject.com/en/6.0/ref/forms/validation/#cleaning-a-specific-field-attribute "Link to this heading")
Continuing on from the previous example, suppose that in our `ContactForm`, we want to make sure that the `recipients` field always contains the address `"fred@example.com"`. This is validation that is specific to our form, so we don’t want to put it into the general `MultiEmailField` class. Instead, we write a cleaning method that operates on the `recipients` field, like so:
```
from django import forms
from django.core.exceptions import ValidationError


class ContactForm(forms.Form):
    # Everything as before.
    ...

    def clean_recipients(self):
        data = self.cleaned_data["recipients"]
        if "fred@example.com" not in data:
            raise ValidationError("You have forgotten about Fred!")

        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return data

```

### Cleaning and validating fields that depend on each other[¶](https://docs.djangoproject.com/en/6.0/ref/forms/validation/#cleaning-and-validating-fields-that-depend-on-each-other "Link to this heading")
Suppose we add another requirement to our contact form: if the `cc_myself` field is `True`, the `subject` must contain the word `"help"`. We are performing validation on more than one field at a time, so the form’s [`clean()`](https://docs.djangoproject.com/en/6.0/ref/forms/api/#django.forms.Form.clean "django.forms.Form.clean") method is a good spot to do this. Notice that we are talking about the `clean()` method on the form here, whereas earlier we were writing a `clean()` method on a field. It’s important to keep the field and form difference clear when working out where to validate things. Fields are single data points, forms are a collection of fields.
By the time the form’s `clean()` method is called, all the individual field clean methods will have been run (the previous two sections), so `self.cleaned_data` will be populated with any data that has survived so far. So you also need to remember to allow for the fact that the fields you are wanting to validate might not have survived the initial individual field checks.
There are two ways to report any errors from this step. Probably the most common method is to display the error at the top of the form. To create such an error, you can raise a `ValidationError` from the `clean()` method. For example:
```
from django import forms
from django.core.exceptions import ValidationError


class ContactForm(forms.Form):
    # Everything as before.
    ...

    def clean(self):
        cleaned_data = super().clean()
        cc_myself = cleaned_data.get("cc_myself")
        subject = cleaned_data.get("subject")

        if cc_myself and subject:
            # Only do something if both fields are valid so far.
            if "help" not in subject:
                raise ValidationError(
                    "Did not send for 'help' in the subject despite CC'ing yourself."
                )

```

In this code, if the validation error is raised, the form will display an error message at the top of the form (normally) describing the problem. Such errors are non-field errors, which are displayed in the template with `{{ form.non_field_errors }}`.
The call to `super().clean()` in the example code ensures that any validation logic in parent classes is maintained. If your form inherits another that doesn’t return a `cleaned_data` dictionary in its `clean()` method (doing so is optional), then don’t assign `cleaned_data` to the result of the `super()` call and use `self.cleaned_data` instead:
```
def clean(self):
    super().clean()
    cc_myself = self.cleaned_data.get("cc_myself")
    ...

```

The second approach for reporting validation errors might involve assigning the error message to one of the fields. In this case, let’s assign an error message to both the “subject” and “cc_myself” rows in the form display. Be careful when doing this in practice, since it can lead to confusing form output. We’re showing what is possible here and leaving it up to you and your designers to work out what works effectively in your particular situation. Our new code (replacing the previous sample) looks like this:
```
from django import forms


class ContactForm(forms.Form):
    # Everything as before.
    ...

    def clean(self):
        cleaned_data = super().clean()
        cc_myself = cleaned_data.get("cc_myself")
        subject = cleaned_data.get("subject")

        if cc_myself and subject and "help" not in subject:
            msg = "Must put 'help' in subject when cc'ing yourself."
            self.add_error("cc_myself", msg)
            self.add_error("subject", msg)

```

The second argument of `add_error()` can be a string, or preferably an instance of `ValidationError`. See [Raising ValidationError](https://docs.djangoproject.com/en/6.0/ref/forms/validation/#raising-validation-error) for more details. Note that `add_error()` automatically removes the field from `cleaned_data`.
Previous page and next page
[](https://docs.djangoproject.com/en/6.0/ref/forms/widgets/)
[Logging ](https://docs.djangoproject.com/en/6.0/ref/logging/)
[](https://docs.djangoproject.com/en/6.0/ref/forms/validation/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Duy Nguyen donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [Form and field validation](https://docs.djangoproject.com/en/6.0/ref/forms/validation/)
    * [Raising `ValidationError`](https://docs.djangoproject.com/en/6.0/ref/forms/validation/#raising-validationerror)
      * [Raising multiple errors](https://docs.djangoproject.com/en/6.0/ref/forms/validation/#raising-multiple-errors)
    * [Using validation in practice](https://docs.djangoproject.com/en/6.0/ref/forms/validation/#using-validation-in-practice)
      * [Using validators](https://docs.djangoproject.com/en/6.0/ref/forms/validation/#using-validators)
      * [Form field default cleaning](https://docs.djangoproject.com/en/6.0/ref/forms/validation/#form-field-default-cleaning)
      * [Cleaning a specific field attribute](https://docs.djangoproject.com/en/6.0/ref/forms/validation/#cleaning-a-specific-field-attribute)
      * [Cleaning and validating fields that depend on each other](https://docs.djangoproject.com/en/6.0/ref/forms/validation/#cleaning-and-validating-fields-that-depend-on-each-other)


### Browse
  * Prev: [Widgets](https://docs.djangoproject.com/en/6.0/ref/forms/widgets/)
  * Next: [Logging](https://docs.djangoproject.com/en/6.0/ref/logging/)
  * [Table of contents](https://docs.djangoproject.com/en/6.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/6.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/6.0/py-modindex/)


### You are here:
  * [Django 6.0 documentation](https://docs.djangoproject.com/en/6.0/)
    * [API Reference](https://docs.djangoproject.com/en/6.0/ref/)
      * [Forms](https://docs.djangoproject.com/en/6.0/ref/forms/)
        * Form and field validation


### Getting help

[FAQ](https://docs.djangoproject.com/en/6.0/faq/)
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
Offline (Django 6.0): [HTML](https://media.djangoproject.com/docs/django-docs-6.0-en.zip) |
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
