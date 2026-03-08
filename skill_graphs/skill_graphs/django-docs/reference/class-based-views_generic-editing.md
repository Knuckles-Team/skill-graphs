This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-editing/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/topics/class-based-views/generic-editing/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/topics/class-based-views/generic-editing/)
  * [pl](https://docs.djangoproject.com/pl/5.0/topics/class-based-views/generic-editing/)
  * [ko](https://docs.djangoproject.com/ko/5.0/topics/class-based-views/generic-editing/)
  * [ja](https://docs.djangoproject.com/ja/5.0/topics/class-based-views/generic-editing/)
  * [it](https://docs.djangoproject.com/it/5.0/topics/class-based-views/generic-editing/)
  * [id](https://docs.djangoproject.com/id/5.0/topics/class-based-views/generic-editing/)
  * [fr](https://docs.djangoproject.com/fr/5.0/topics/class-based-views/generic-editing/)
  * [es](https://docs.djangoproject.com/es/5.0/topics/class-based-views/generic-editing/)
  * [el](https://docs.djangoproject.com/el/5.0/topics/class-based-views/generic-editing/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/topics/class-based-views/generic-editing/)
  * [6.0](https://docs.djangoproject.com/en/6.0/topics/class-based-views/generic-editing/)
  * [5.2](https://docs.djangoproject.com/en/5.2/topics/class-based-views/generic-editing/)
  * [5.1](https://docs.djangoproject.com/en/5.1/topics/class-based-views/generic-editing/)
  * [4.2](https://docs.djangoproject.com/en/4.2/topics/class-based-views/generic-editing/)
  * [4.1](https://docs.djangoproject.com/en/4.1/topics/class-based-views/generic-editing/)
  * [4.0](https://docs.djangoproject.com/en/4.0/topics/class-based-views/generic-editing/)
  * [3.2](https://docs.djangoproject.com/en/3.2/topics/class-based-views/generic-editing/)
  * [3.1](https://docs.djangoproject.com/en/3.1/topics/class-based-views/generic-editing/)
  * [3.0](https://docs.djangoproject.com/en/3.0/topics/class-based-views/generic-editing/)
  * [2.2](https://docs.djangoproject.com/en/2.2/topics/class-based-views/generic-editing/)
  * [2.1](https://docs.djangoproject.com/en/2.1/topics/class-based-views/generic-editing/)
  * [2.0](https://docs.djangoproject.com/en/2.0/topics/class-based-views/generic-editing/)
  * [1.11](https://docs.djangoproject.com/en/1.11/topics/class-based-views/generic-editing/)
  * [1.10](https://docs.djangoproject.com/en/1.10/topics/class-based-views/generic-editing/)
  * [1.8](https://docs.djangoproject.com/en/1.8/topics/class-based-views/generic-editing/)


  * [](https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-editing/#top)


# Form handling with class-based views[¶](https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-editing/#form-handling-with-class-based-views "Link to this heading")
Form processing generally has 3 paths:
  * Initial GET (blank or prepopulated form)
  * POST with invalid data (typically redisplay form with errors)
  * POST with valid data (process the data and typically redirect)


Implementing this yourself often results in a lot of repeated boilerplate code (see [Using a form in a view](https://docs.djangoproject.com/en/5.0/topics/forms/#using-a-form-in-a-view)). To help avoid this, Django provides a collection of generic class-based views for form processing.
## Basic forms[¶](https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-editing/#basic-forms "Link to this heading")
Given a contact form:
`forms.py`[¶](https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-editing/#id2 "Link to this code")
```
from django import forms


class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass

```

The view can be constructed using a `FormView`:
`views.py`[¶](https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-editing/#id3 "Link to this code")
```
from myapp.forms import ContactForm
from django.views.generic.edit import FormView


class ContactFormView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = "/thanks/"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)

```

Notes:
  * FormView inherits [`TemplateResponseMixin`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin "django.views.generic.base.TemplateResponseMixin") so [`template_name`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.template_name "django.views.generic.base.TemplateResponseMixin.template_name") can be used here.
  * The default implementation for [`form_valid()`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.FormMixin.form_valid "django.views.generic.edit.FormMixin.form_valid") simply redirects to the [`success_url`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.FormMixin.success_url "django.views.generic.edit.FormMixin.success_url").


## Model forms[¶](https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-editing/#model-forms "Link to this heading")
Generic views really shine when working with models. These generic views will automatically create a [`ModelForm`](https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/#django.forms.ModelForm "django.forms.ModelForm"), so long as they can work out which model class to use:
  * If the [`model`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.ModelFormMixin.model "django.views.generic.edit.ModelFormMixin.model") attribute is given, that model class will be used.
  * If [`get_object()`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.get_object "django.views.generic.detail.SingleObjectMixin.get_object") returns an object, the class of that object will be used.
  * If a [`queryset`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.queryset "django.views.generic.detail.SingleObjectMixin.queryset") is given, the model for that queryset will be used.


Model form views provide a [`form_valid()`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.ModelFormMixin.form_valid "django.views.generic.edit.ModelFormMixin.form_valid") implementation that saves the model automatically. You can override this if you have any special requirements; see below for examples.
You don’t even need to provide a `success_url` for [`CreateView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/generic-editing/#django.views.generic.edit.CreateView "django.views.generic.edit.CreateView") or [`UpdateView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/generic-editing/#django.views.generic.edit.UpdateView "django.views.generic.edit.UpdateView") - they will use [`get_absolute_url()`](https://docs.djangoproject.com/en/5.0/ref/models/instances/#django.db.models.Model.get_absolute_url "django.db.models.Model.get_absolute_url") on the model object if available.
If you want to use a custom [`ModelForm`](https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/#django.forms.ModelForm "django.forms.ModelForm") (for instance to add extra validation), set [`form_class`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.FormMixin.form_class "django.views.generic.edit.FormMixin.form_class") on your view.
Note
When specifying a custom form class, you must still specify the model, even though the [`form_class`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.FormMixin.form_class "django.views.generic.edit.FormMixin.form_class") may be a [`ModelForm`](https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/#django.forms.ModelForm "django.forms.ModelForm").
First we need to add [`get_absolute_url()`](https://docs.djangoproject.com/en/5.0/ref/models/instances/#django.db.models.Model.get_absolute_url "django.db.models.Model.get_absolute_url") to our `Author` class:
`models.py`[¶](https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-editing/#id4 "Link to this code")
```
from django.db import models
from django.urls import reverse


class Author(models.Model):
    name = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse("author-detail", kwargs={"pk": self.pk})

```

Then we can use [`CreateView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/flattened-index/#CreateView "CreateView") and friends to do the actual work. Notice how we’re just configuring the generic class-based views here; we don’t have to write any logic ourselves:
`views.py`[¶](https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-editing/#id5 "Link to this code")
```
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from myapp.models import Author


class AuthorCreateView(CreateView):
    model = Author
    fields = ["name"]


class AuthorUpdateView(UpdateView):
    model = Author
    fields = ["name"]


class AuthorDeleteView(DeleteView):
    model = Author
    success_url = reverse_lazy("author-list")

```

Note
We have to use [`reverse_lazy()`](https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#django.urls.reverse_lazy "django.urls.reverse_lazy") instead of `reverse()`, as the urls are not loaded when the file is imported.
The `fields` attribute works the same way as the `fields` attribute on the inner `Meta` class on [`ModelForm`](https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/#django.forms.ModelForm "django.forms.ModelForm"). Unless you define the form class in another way, the attribute is required and the view will raise an [`ImproperlyConfigured`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.ImproperlyConfigured "django.core.exceptions.ImproperlyConfigured") exception if it’s not.
If you specify both the [`fields`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.ModelFormMixin.fields "django.views.generic.edit.ModelFormMixin.fields") and [`form_class`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.FormMixin.form_class "django.views.generic.edit.FormMixin.form_class") attributes, an [`ImproperlyConfigured`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.ImproperlyConfigured "django.core.exceptions.ImproperlyConfigured") exception will be raised.
Finally, we hook these new views into the URLconf:
`urls.py`[¶](https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-editing/#id6 "Link to this code")
```
from django.urls import path
from myapp.views import AuthorCreateView, AuthorDeleteView, AuthorUpdateView

urlpatterns = [
    # ...
    path("author/add/", AuthorCreateView.as_view(), name="author-add"),
    path("author/<int:pk>/", AuthorUpdateView.as_view(), name="author-update"),
    path("author/<int:pk>/delete/", AuthorDeleteView.as_view(), name="author-delete"),
]

```

Note
These views inherit [`SingleObjectTemplateResponseMixin`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectTemplateResponseMixin "django.views.generic.detail.SingleObjectTemplateResponseMixin") which uses [`template_name_suffix`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectTemplateResponseMixin.template_name_suffix "django.views.generic.detail.SingleObjectTemplateResponseMixin.template_name_suffix") to construct the [`template_name`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.template_name "django.views.generic.base.TemplateResponseMixin.template_name") based on the model.
In this example:
  * [`CreateView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/flattened-index/#CreateView "CreateView") and [`UpdateView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/flattened-index/#UpdateView "UpdateView") use `myapp/author_form.html`
  * [`DeleteView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/flattened-index/#DeleteView "DeleteView") uses `myapp/author_confirm_delete.html`


If you wish to have separate templates for [`CreateView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/flattened-index/#CreateView "CreateView") and [`UpdateView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/flattened-index/#UpdateView "UpdateView"), you can set either [`template_name`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.template_name "django.views.generic.base.TemplateResponseMixin.template_name") or [`template_name_suffix`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectTemplateResponseMixin.template_name_suffix "django.views.generic.detail.SingleObjectTemplateResponseMixin.template_name_suffix") on your view class.
## Models and `request.user`[¶](https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-editing/#models-and-request-user "Link to this heading")
To track the user that created an object using a [`CreateView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/flattened-index/#CreateView "CreateView"), you can use a custom [`ModelForm`](https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/#django.forms.ModelForm "django.forms.ModelForm") to do this. First, add the foreign key relation to the model:
`models.py`[¶](https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-editing/#id7 "Link to this code")
```
from django.contrib.auth.models import User
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    # ...

```

In the view, ensure that you don’t include `created_by` in the list of fields to edit, and override [`form_valid()`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.ModelFormMixin.form_valid "django.views.generic.edit.ModelFormMixin.form_valid") to add the user:
`views.py`[¶](https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-editing/#id8 "Link to this code")
```
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from myapp.models import Author


class AuthorCreateView(LoginRequiredMixin, CreateView):
    model = Author
    fields = ["name"]

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

```

[`LoginRequiredMixin`](https://docs.djangoproject.com/en/5.0/topics/auth/default/#django.contrib.auth.mixins.LoginRequiredMixin "django.contrib.auth.mixins.LoginRequiredMixin") prevents users who aren’t logged in from accessing the form. If you omit that, you’ll need to handle unauthorized users in [`form_valid()`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.ModelFormMixin.form_valid "django.views.generic.edit.ModelFormMixin.form_valid").
## Content negotiation example[¶](https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-editing/#content-negotiation-example "Link to this heading")
Here is an example showing how you might go about implementing a form that works with an API-based workflow as well as ‘normal’ form POSTs:
```
from django.http import JsonResponse
from django.views.generic.edit import CreateView
from myapp.models import Author


class JsonableResponseMixin:
    """
    Mixin to add JSON support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """

    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.accepts("text/html"):
            return response
        else:
            return JsonResponse(form.errors, status=400)

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super().form_valid(form)
        if self.request.accepts("text/html"):
            return response
        else:
            data = {
                "pk": self.object.pk,
            }
            return JsonResponse(data)


class AuthorCreateView(JsonableResponseMixin, CreateView):
    model = Author
    fields = ["name"]

```

Previous page and next page
[](https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-display/)
[Using mixins with class-based views ](https://docs.djangoproject.com/en/5.0/topics/class-based-views/mixins/)
[](https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-editing/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Experius donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [Form handling with class-based views](https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-editing/)
    * [Basic forms](https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-editing/#basic-forms)
    * [Model forms](https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-editing/#model-forms)
    * [Models and `request.user`](https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-editing/#models-and-request-user)
    * [Content negotiation example](https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-editing/#content-negotiation-example)


### Browse
  * Prev: [Built-in class-based generic views](https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-display/)
  * Next: [Using mixins with class-based views](https://docs.djangoproject.com/en/5.0/topics/class-based-views/mixins/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [Using Django](https://docs.djangoproject.com/en/5.0/topics/)
      * [Class-based views](https://docs.djangoproject.com/en/5.0/topics/class-based-views/)
        * Form handling with class-based views


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
