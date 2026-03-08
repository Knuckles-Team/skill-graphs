This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/howto/outputting-pdf/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/howto/outputting-pdf/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/howto/outputting-pdf/)
  * [pl](https://docs.djangoproject.com/pl/5.0/howto/outputting-pdf/)
  * [ko](https://docs.djangoproject.com/ko/5.0/howto/outputting-pdf/)
  * [ja](https://docs.djangoproject.com/ja/5.0/howto/outputting-pdf/)
  * [it](https://docs.djangoproject.com/it/5.0/howto/outputting-pdf/)
  * [id](https://docs.djangoproject.com/id/5.0/howto/outputting-pdf/)
  * [fr](https://docs.djangoproject.com/fr/5.0/howto/outputting-pdf/)
  * [es](https://docs.djangoproject.com/es/5.0/howto/outputting-pdf/)
  * [el](https://docs.djangoproject.com/el/5.0/howto/outputting-pdf/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/howto/outputting-pdf/)
  * [6.0](https://docs.djangoproject.com/en/6.0/howto/outputting-pdf/)
  * [5.2](https://docs.djangoproject.com/en/5.2/howto/outputting-pdf/)
  * [5.1](https://docs.djangoproject.com/en/5.1/howto/outputting-pdf/)
  * [4.2](https://docs.djangoproject.com/en/4.2/howto/outputting-pdf/)
  * [4.1](https://docs.djangoproject.com/en/4.1/howto/outputting-pdf/)
  * [4.0](https://docs.djangoproject.com/en/4.0/howto/outputting-pdf/)
  * [3.2](https://docs.djangoproject.com/en/3.2/howto/outputting-pdf/)
  * [3.1](https://docs.djangoproject.com/en/3.1/howto/outputting-pdf/)
  * [3.0](https://docs.djangoproject.com/en/3.0/howto/outputting-pdf/)
  * [2.2](https://docs.djangoproject.com/en/2.2/howto/outputting-pdf/)
  * [2.1](https://docs.djangoproject.com/en/2.1/howto/outputting-pdf/)
  * [2.0](https://docs.djangoproject.com/en/2.0/howto/outputting-pdf/)
  * [1.11](https://docs.djangoproject.com/en/1.11/howto/outputting-pdf/)
  * [1.10](https://docs.djangoproject.com/en/1.10/howto/outputting-pdf/)
  * [1.8](https://docs.djangoproject.com/en/1.8/howto/outputting-pdf/)


  * [](https://docs.djangoproject.com/en/5.0/howto/outputting-pdf/#top)


# How to create PDF files[¶](https://docs.djangoproject.com/en/5.0/howto/outputting-pdf/#how-to-create-pdf-files "Link to this heading")
This document explains how to output PDF files dynamically using Django views. This is made possible by the excellent, open-source
The advantage of generating PDF files dynamically is that you can create customized PDFs for different purposes – say, for different users or different pieces of content.
For example, Django was used at
## Install ReportLab[¶](https://docs.djangoproject.com/en/5.0/howto/outputting-pdf/#install-reportlab "Link to this heading")
The ReportLab library is `pip`:
/ 
```
$ python -m pip install reportlab

```

```
...\> py -m pip install reportlab

```

Test your installation by importing it in the Python interactive interpreter:
```
>>> import reportlab

```

If that command doesn’t raise any errors, the installation worked.
## Write your view[¶](https://docs.djangoproject.com/en/5.0/howto/outputting-pdf/#write-your-view "Link to this heading")
The key to generating PDFs dynamically with Django is that the ReportLab API acts on file-like objects, and Django’s [`FileResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.FileResponse "django.http.FileResponse") objects accept file-like objects.
Here’s a “Hello World” example:
```
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas


def some_view(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename="hello.pdf")

```

The code and comments should be self-explanatory, but a few things deserve a mention:
  * The response will automatically set the MIME type _application/pdf_ based on the filename extension. This tells browsers that the document is a PDF file, rather than an HTML file or a generic _application/octet-stream_ binary content.
  * When `as_attachment=True` is passed to `FileResponse`, it sets the appropriate `Content-Disposition` header and that tells web browsers to pop-up a dialog box prompting/confirming how to handle the document even if a default is set on the machine. If the `as_attachment` parameter is omitted, browsers will handle the PDF using whatever program/plugin they’ve been configured to use for PDFs.
  * You can provide an arbitrary `filename` parameter. It’ll be used by browsers in the “Save as…” dialog.
  * You can hook into the ReportLab API: The same buffer passed as the first argument to `canvas.Canvas` can be fed to the [`FileResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.FileResponse "django.http.FileResponse") class.
  * Note that all subsequent PDF-generation methods are called on the PDF object (in this case, `p`) – not on `buffer`.
  * Finally, it’s important to call `showPage()` and `save()` on the PDF file.


Note
ReportLab is not thread-safe. Some of our users have reported odd issues with building PDF-generating Django views that are accessed by many people at the same time.
## Other formats[¶](https://docs.djangoproject.com/en/5.0/howto/outputting-pdf/#other-formats "Link to this heading")
Notice that there isn’t a lot in these examples that’s PDF-specific – just the bits using `reportlab`. You can use a similar technique to generate any arbitrary format that you can find a Python library for. Also see [How to create CSV output](https://docs.djangoproject.com/en/5.0/howto/outputting-csv/) for another example and some techniques you can use when generated text-based formats.
See also
Django Packages provides a
Previous page and next page
[](https://docs.djangoproject.com/en/5.0/howto/outputting-csv/)
[How to override templates ](https://docs.djangoproject.com/en/5.0/howto/overriding-templates/)
[](https://docs.djangoproject.com/en/5.0/howto/outputting-pdf/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Paolo Dina donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [How to create PDF files](https://docs.djangoproject.com/en/5.0/howto/outputting-pdf/)
    * [Install ReportLab](https://docs.djangoproject.com/en/5.0/howto/outputting-pdf/#install-reportlab)
    * [Write your view](https://docs.djangoproject.com/en/5.0/howto/outputting-pdf/#write-your-view)
    * [Other formats](https://docs.djangoproject.com/en/5.0/howto/outputting-pdf/#other-formats)


### Browse
  * Prev: [How to create CSV output](https://docs.djangoproject.com/en/5.0/howto/outputting-csv/)
  * Next: [How to override templates](https://docs.djangoproject.com/en/5.0/howto/overriding-templates/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [“How-to” guides](https://docs.djangoproject.com/en/5.0/howto/)
      * How to create PDF files


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
