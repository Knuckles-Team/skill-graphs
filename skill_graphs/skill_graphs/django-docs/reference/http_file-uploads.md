This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/topics/http/file-uploads/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/topics/http/file-uploads/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/topics/http/file-uploads/)
  * [pl](https://docs.djangoproject.com/pl/5.0/topics/http/file-uploads/)
  * [ko](https://docs.djangoproject.com/ko/5.0/topics/http/file-uploads/)
  * [ja](https://docs.djangoproject.com/ja/5.0/topics/http/file-uploads/)
  * [it](https://docs.djangoproject.com/it/5.0/topics/http/file-uploads/)
  * [id](https://docs.djangoproject.com/id/5.0/topics/http/file-uploads/)
  * [fr](https://docs.djangoproject.com/fr/5.0/topics/http/file-uploads/)
  * [es](https://docs.djangoproject.com/es/5.0/topics/http/file-uploads/)
  * [el](https://docs.djangoproject.com/el/5.0/topics/http/file-uploads/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/topics/http/file-uploads/)
  * [6.0](https://docs.djangoproject.com/en/6.0/topics/http/file-uploads/)
  * [5.2](https://docs.djangoproject.com/en/5.2/topics/http/file-uploads/)
  * [5.1](https://docs.djangoproject.com/en/5.1/topics/http/file-uploads/)
  * [4.2](https://docs.djangoproject.com/en/4.2/topics/http/file-uploads/)
  * [4.1](https://docs.djangoproject.com/en/4.1/topics/http/file-uploads/)
  * [4.0](https://docs.djangoproject.com/en/4.0/topics/http/file-uploads/)
  * [3.2](https://docs.djangoproject.com/en/3.2/topics/http/file-uploads/)
  * [3.1](https://docs.djangoproject.com/en/3.1/topics/http/file-uploads/)
  * [3.0](https://docs.djangoproject.com/en/3.0/topics/http/file-uploads/)
  * [2.2](https://docs.djangoproject.com/en/2.2/topics/http/file-uploads/)
  * [2.1](https://docs.djangoproject.com/en/2.1/topics/http/file-uploads/)
  * [2.0](https://docs.djangoproject.com/en/2.0/topics/http/file-uploads/)
  * [1.11](https://docs.djangoproject.com/en/1.11/topics/http/file-uploads/)
  * [1.10](https://docs.djangoproject.com/en/1.10/topics/http/file-uploads/)
  * [1.8](https://docs.djangoproject.com/en/1.8/topics/http/file-uploads/)


  * [](https://docs.djangoproject.com/en/5.0/topics/http/file-uploads/#top)


# File Uploads[¶](https://docs.djangoproject.com/en/5.0/topics/http/file-uploads/#file-uploads "Link to this heading")
When Django handles a file upload, the file data ends up placed in [`request.FILES`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.FILES "django.http.HttpRequest.FILES") (for more on the `request` object see the documentation for [request and response objects](https://docs.djangoproject.com/en/5.0/ref/request-response/)). This document explains how files are stored on disk and in memory, and how to customize the default behavior.
Warning
There are security risks if you are accepting uploaded content from untrusted users! See the security guide’s topic on [User-uploaded content](https://docs.djangoproject.com/en/5.0/topics/security/#user-uploaded-content-security) for mitigation details.
## Basic file uploads[¶](https://docs.djangoproject.com/en/5.0/topics/http/file-uploads/#basic-file-uploads "Link to this heading")
Consider a form containing a [`FileField`](https://docs.djangoproject.com/en/5.0/ref/forms/fields/#django.forms.FileField "django.forms.FileField"):
`forms.py`[¶](https://docs.djangoproject.com/en/5.0/topics/http/file-uploads/#id3 "Link to this code")
```
from django import forms


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

```

A view handling this form will receive the file data in [`request.FILES`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.FILES "django.http.HttpRequest.FILES"), which is a dictionary containing a key for each [`FileField`](https://docs.djangoproject.com/en/5.0/ref/forms/fields/#django.forms.FileField "django.forms.FileField") (or [`ImageField`](https://docs.djangoproject.com/en/5.0/ref/forms/fields/#django.forms.ImageField "django.forms.ImageField"), or other [`FileField`](https://docs.djangoproject.com/en/5.0/ref/forms/fields/#django.forms.FileField "django.forms.FileField") subclass) in the form. So the data from the above form would be accessible as `request.FILES['file']`.
Note that [`request.FILES`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.FILES "django.http.HttpRequest.FILES") will only contain data if the request method was `POST`, at least one file field was actually posted, and the `<form>` that posted the request has the attribute `enctype="multipart/form-data"`. Otherwise, `request.FILES` will be empty.
Most of the time, you’ll pass the file data from `request` into the form as described in [Binding uploaded files to a form](https://docs.djangoproject.com/en/5.0/ref/forms/api/#binding-uploaded-files). This would look something like:
`views.py`[¶](https://docs.djangoproject.com/en/5.0/topics/http/file-uploads/#id4 "Link to this code")
```
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm

# Imaginary function to handle an uploaded file.
from somewhere import handle_uploaded_file


def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES["file"])
            return HttpResponseRedirect("/success/url/")
    else:
        form = UploadFileForm()
    return render(request, "upload.html", {"form": form})

```

Notice that we have to pass [`request.FILES`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.FILES "django.http.HttpRequest.FILES") into the form’s constructor; this is how file data gets bound into a form.
Here’s a common way you might handle an uploaded file:
```
def handle_uploaded_file(f):
    with open("some/file/name.txt", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)

```

Looping over `UploadedFile.chunks()` instead of using `read()` ensures that large files don’t overwhelm your system’s memory.
There are a few other methods and attributes available on `UploadedFile` objects; see [`UploadedFile`](https://docs.djangoproject.com/en/5.0/ref/files/uploads/#django.core.files.uploadedfile.UploadedFile "django.core.files.uploadedfile.UploadedFile") for a complete reference.
### Handling uploaded files with a model[¶](https://docs.djangoproject.com/en/5.0/topics/http/file-uploads/#handling-uploaded-files-with-a-model "Link to this heading")
If you’re saving a file on a [`Model`](https://docs.djangoproject.com/en/5.0/ref/models/instances/#django.db.models.Model "django.db.models.Model") with a [`FileField`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.FileField "django.db.models.FileField"), using a [`ModelForm`](https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/#django.forms.ModelForm "django.forms.ModelForm") makes this process much easier. The file object will be saved to the location specified by the [`upload_to`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.FileField.upload_to "django.db.models.FileField.upload_to") argument of the corresponding [`FileField`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.FileField "django.db.models.FileField") when calling `form.save()`:
```
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ModelFormWithFileField


def upload_file(request):
    if request.method == "POST":
        form = ModelFormWithFileField(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return HttpResponseRedirect("/success/url/")
    else:
        form = ModelFormWithFileField()
    return render(request, "upload.html", {"form": form})

```

If you are constructing an object manually, you can assign the file object from [`request.FILES`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.FILES "django.http.HttpRequest.FILES") to the file field in the model:
```
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from .models import ModelWithFileField


def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = ModelWithFileField(file_field=request.FILES["file"])
            instance.save()
            return HttpResponseRedirect("/success/url/")
    else:
        form = UploadFileForm()
    return render(request, "upload.html", {"form": form})

```

If you are constructing an object manually outside of a request, you can assign a [`File`](https://docs.djangoproject.com/en/5.0/ref/files/file/#django.core.files.File "django.core.files.File") like object to the [`FileField`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.FileField "django.db.models.FileField"):
```
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile


class MyCommand(BaseCommand):
    def handle(self, *args, **options):
        content_file = ContentFile(b"Hello world!", name="hello-world.txt")
        instance = ModelWithFileField(file_field=content_file)
        instance.save()

```

### Uploading multiple files[¶](https://docs.djangoproject.com/en/5.0/topics/http/file-uploads/#uploading-multiple-files "Link to this heading")
If you want to upload multiple files using one form field, create a subclass of the field’s widget and set its `allow_multiple_selected` class attribute to `True`.
In order for such files to be all validated by your form (and have the value of the field include them all), you will also have to subclass `FileField`. See below for an example.
Multiple file field
Django is likely to have a proper multiple file field support at some point in the future.
`forms.py`[¶](https://docs.djangoproject.com/en/5.0/topics/http/file-uploads/#id5 "Link to this code")
```
from django import forms


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = [single_file_clean(data, initial)]
        return result


class FileFieldForm(forms.Form):
    file_field = MultipleFileField()

```

Then override the `form_valid()` method of your [`FormView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/generic-editing/#django.views.generic.edit.FormView "django.views.generic.edit.FormView") subclass to handle multiple file uploads:
`views.py`[¶](https://docs.djangoproject.com/en/5.0/topics/http/file-uploads/#id6 "Link to this code")
```
from django.views.generic.edit import FormView
from .forms import FileFieldForm


class FileFieldFormView(FormView):
    form_class = FileFieldForm
    template_name = "upload.html"  # Replace with your template.
    success_url = "..."  # Replace with your URL or reverse().

    def form_valid(self, form):
        files = form.cleaned_data["file_field"]
        for f in files:
            ...  # Do something with each file.
        return super().form_valid(form)

```

Warning
This will allow you to handle multiple files at the form level only. Be aware that you cannot use it to put multiple files on a single model instance (in a single field), for example, even if the custom widget is used with a form field related to a model `FileField`.
Changed in Django 3.2.19:
In previous versions, there was no support for the `allow_multiple_selected` class attribute, and users were advised to create the widget with the HTML attribute `multiple` set through the `attrs` argument. However, this caused validation of the form field to be applied only to the last file submitted, which could have adverse security implications.
## Upload Handlers[¶](https://docs.djangoproject.com/en/5.0/topics/http/file-uploads/#upload-handlers "Link to this heading")
When a user uploads a file, Django passes off the file data to an _upload handler_ – a small class that handles file data as it gets uploaded. Upload handlers are initially defined in the [`FILE_UPLOAD_HANDLERS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-FILE_UPLOAD_HANDLERS) setting, which defaults to:
```
[
    "django.core.files.uploadhandler.MemoryFileUploadHandler",
    "django.core.files.uploadhandler.TemporaryFileUploadHandler",
]

```

Together [`MemoryFileUploadHandler`](https://docs.djangoproject.com/en/5.0/ref/files/uploads/#django.core.files.uploadhandler.MemoryFileUploadHandler "django.core.files.uploadhandler.MemoryFileUploadHandler") and [`TemporaryFileUploadHandler`](https://docs.djangoproject.com/en/5.0/ref/files/uploads/#django.core.files.uploadhandler.TemporaryFileUploadHandler "django.core.files.uploadhandler.TemporaryFileUploadHandler") provide Django’s default file upload behavior of reading small files into memory and large ones onto disk.
You can write custom handlers that customize how Django handles files. You could, for example, use custom handlers to enforce user-level quotas, compress data on the fly, render progress bars, and even send data to another storage location directly without storing it locally. See [Writing custom upload handlers](https://docs.djangoproject.com/en/5.0/ref/files/uploads/#custom-upload-handlers) for details on how you can customize or completely replace upload behavior.
### Where uploaded data is stored[¶](https://docs.djangoproject.com/en/5.0/topics/http/file-uploads/#where-uploaded-data-is-stored "Link to this heading")
Before you save uploaded files, the data needs to be stored somewhere.
By default, if an uploaded file is smaller than 2.5 megabytes, Django will hold the entire contents of the upload in memory. This means that saving the file involves only a read from memory and a write to disk and thus is very fast.
However, if an uploaded file is too large, Django will write the uploaded file to a temporary file stored in your system’s temporary directory. On a Unix-like platform this means you can expect Django to generate a file called something like `/tmp/tmpzfp6I6.upload`. If an upload is large enough, you can watch this file grow in size as Django streams the data onto disk.
These specifics – 2.5 megabytes; `/tmp`; etc. – are “reasonable defaults” which can be customized as described in the next section.
### Changing upload handler behavior[¶](https://docs.djangoproject.com/en/5.0/topics/http/file-uploads/#changing-upload-handler-behavior "Link to this heading")
There are a few settings which control Django’s file upload behavior. See [File Upload Settings](https://docs.djangoproject.com/en/5.0/ref/settings/#file-upload-settings) for details.
### Modifying upload handlers on the fly[¶](https://docs.djangoproject.com/en/5.0/topics/http/file-uploads/#modifying-upload-handlers-on-the-fly "Link to this heading")
Sometimes particular views require different upload behavior. In these cases, you can override upload handlers on a per-request basis by modifying `request.upload_handlers`. By default, this list will contain the upload handlers given by [`FILE_UPLOAD_HANDLERS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-FILE_UPLOAD_HANDLERS), but you can modify the list as you would any other list.
For instance, suppose you’ve written a `ProgressBarUploadHandler` that provides feedback on upload progress to some sort of AJAX widget. You’d add this handler to your upload handlers like this:
```
request.upload_handlers.insert(0, ProgressBarUploadHandler(request))

```

You’d probably want to use `list.insert()` in this case (instead of `append()`) because a progress bar handler would need to run _before_ any other handlers. Remember, the upload handlers are processed in order.
If you want to replace the upload handlers completely, you can assign a new list:
```
request.upload_handlers = [ProgressBarUploadHandler(request)]

```

Note
You can only modify upload handlers _before_ accessing `request.POST` or `request.FILES` – it doesn’t make sense to change upload handlers after upload handling has already started. If you try to modify `request.upload_handlers` after reading from `request.POST` or `request.FILES` Django will throw an error.
Thus, you should always modify uploading handlers as early in your view as possible.
Also, `request.POST` is accessed by [`CsrfViewMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.middleware.csrf.CsrfViewMiddleware "django.middleware.csrf.CsrfViewMiddleware") which is enabled by default. This means you will need to use [`csrf_exempt()`](https://docs.djangoproject.com/en/5.0/ref/csrf/#django.views.decorators.csrf.csrf_exempt "django.views.decorators.csrf.csrf_exempt") on your view to allow you to change the upload handlers. You will then need to use [`csrf_protect()`](https://docs.djangoproject.com/en/5.0/ref/csrf/#django.views.decorators.csrf.csrf_protect "django.views.decorators.csrf.csrf_protect") on the function that actually processes the request. Note that this means that the handlers may start receiving the file upload before the CSRF checks have been done. Example code:
```
from django.views.decorators.csrf import csrf_exempt, csrf_protect


@csrf_exempt
def upload_file_view(request):
    request.upload_handlers.insert(0, ProgressBarUploadHandler(request))
    return _upload_file_view(request)


@csrf_protect
def _upload_file_view(request):
    # Process request
    ...

```

If you are using a class-based view, you will need to use [`csrf_exempt()`](https://docs.djangoproject.com/en/5.0/ref/csrf/#django.views.decorators.csrf.csrf_exempt "django.views.decorators.csrf.csrf_exempt") on its [`dispatch()`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/#django.views.generic.base.View.dispatch "django.views.generic.base.View.dispatch") method and [`csrf_protect()`](https://docs.djangoproject.com/en/5.0/ref/csrf/#django.views.decorators.csrf.csrf_protect "django.views.decorators.csrf.csrf_protect") on the method that actually processes the request. Example code:
```
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt, csrf_protect


@method_decorator(csrf_exempt, name="dispatch")
class UploadFileView(View):
    def setup(self, request, *args, **kwargs):
        request.upload_handlers.insert(0, ProgressBarUploadHandler(request))
        super().setup(request, *args, **kwargs)

    @method_decorator(csrf_protect)
    def post(self, request, *args, **kwargs):
        # Process request
        ...

```

Previous page and next page
[](https://docs.djangoproject.com/en/5.0/topics/http/decorators/)
[Django shortcut functions ](https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/)
[](https://docs.djangoproject.com/en/5.0/topics/http/file-uploads/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Valtteri Mäkelä donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [File Uploads](https://docs.djangoproject.com/en/5.0/topics/http/file-uploads/)
    * [Basic file uploads](https://docs.djangoproject.com/en/5.0/topics/http/file-uploads/#basic-file-uploads)
      * [Handling uploaded files with a model](https://docs.djangoproject.com/en/5.0/topics/http/file-uploads/#handling-uploaded-files-with-a-model)
      * [Uploading multiple files](https://docs.djangoproject.com/en/5.0/topics/http/file-uploads/#uploading-multiple-files)
    * [Upload Handlers](https://docs.djangoproject.com/en/5.0/topics/http/file-uploads/#upload-handlers)
      * [Where uploaded data is stored](https://docs.djangoproject.com/en/5.0/topics/http/file-uploads/#where-uploaded-data-is-stored)
      * [Changing upload handler behavior](https://docs.djangoproject.com/en/5.0/topics/http/file-uploads/#changing-upload-handler-behavior)
      * [Modifying upload handlers on the fly](https://docs.djangoproject.com/en/5.0/topics/http/file-uploads/#modifying-upload-handlers-on-the-fly)


### Browse
  * Prev: [View decorators](https://docs.djangoproject.com/en/5.0/topics/http/decorators/)
  * Next: [Django shortcut functions](https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [Using Django](https://docs.djangoproject.com/en/5.0/topics/)
      * [Handling HTTP requests](https://docs.djangoproject.com/en/5.0/topics/http/)
        * File Uploads


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
