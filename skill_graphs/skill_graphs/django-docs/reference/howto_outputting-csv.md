This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/howto/outputting-csv/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/howto/outputting-csv/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/howto/outputting-csv/)
  * [pl](https://docs.djangoproject.com/pl/5.0/howto/outputting-csv/)
  * [ko](https://docs.djangoproject.com/ko/5.0/howto/outputting-csv/)
  * [ja](https://docs.djangoproject.com/ja/5.0/howto/outputting-csv/)
  * [it](https://docs.djangoproject.com/it/5.0/howto/outputting-csv/)
  * [id](https://docs.djangoproject.com/id/5.0/howto/outputting-csv/)
  * [fr](https://docs.djangoproject.com/fr/5.0/howto/outputting-csv/)
  * [es](https://docs.djangoproject.com/es/5.0/howto/outputting-csv/)
  * [el](https://docs.djangoproject.com/el/5.0/howto/outputting-csv/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/howto/outputting-csv/)
  * [6.0](https://docs.djangoproject.com/en/6.0/howto/outputting-csv/)
  * [5.2](https://docs.djangoproject.com/en/5.2/howto/outputting-csv/)
  * [5.1](https://docs.djangoproject.com/en/5.1/howto/outputting-csv/)
  * [4.2](https://docs.djangoproject.com/en/4.2/howto/outputting-csv/)
  * [4.1](https://docs.djangoproject.com/en/4.1/howto/outputting-csv/)
  * [4.0](https://docs.djangoproject.com/en/4.0/howto/outputting-csv/)
  * [3.2](https://docs.djangoproject.com/en/3.2/howto/outputting-csv/)
  * [3.1](https://docs.djangoproject.com/en/3.1/howto/outputting-csv/)
  * [3.0](https://docs.djangoproject.com/en/3.0/howto/outputting-csv/)
  * [2.2](https://docs.djangoproject.com/en/2.2/howto/outputting-csv/)
  * [2.1](https://docs.djangoproject.com/en/2.1/howto/outputting-csv/)
  * [2.0](https://docs.djangoproject.com/en/2.0/howto/outputting-csv/)
  * [1.11](https://docs.djangoproject.com/en/1.11/howto/outputting-csv/)
  * [1.10](https://docs.djangoproject.com/en/1.10/howto/outputting-csv/)
  * [1.8](https://docs.djangoproject.com/en/1.8/howto/outputting-csv/)


  * [](https://docs.djangoproject.com/en/5.0/howto/outputting-csv/#top)


# How to create CSV output[¶](https://docs.djangoproject.com/en/5.0/howto/outputting-csv/#how-to-create-csv-output "Link to this heading")
This document explains how to output CSV (Comma Separated Values) dynamically using Django views. To do this, you can either use the Python CSV library or the Django template system.
## Using the Python CSV library[¶](https://docs.djangoproject.com/en/5.0/howto/outputting-csv/#using-the-python-csv-library "Link to this heading")
Python comes with a CSV library, [`HttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse") objects are file-like objects.
Here’s an example:
```
import csv
from django.http import HttpResponse


def some_view(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(
        content_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="somefilename.csv"'},
    )

    writer = csv.writer(response)
    writer.writerow(["First row", "Foo", "Bar", "Baz"])
    writer.writerow(["Second row", "A", "B", "C", '"Testing"', "Here's a quote"])

    return response

```

The code and comments should be self-explanatory, but a few things deserve a mention:
  * The response gets a special MIME type, _text/csv_. This tells browsers that the document is a CSV file, rather than an HTML file. If you leave this off, browsers will probably interpret the output as HTML, which will result in ugly, scary gobbledygook in the browser window.
  * The response gets an additional `Content-Disposition` header, which contains the name of the CSV file. This filename is arbitrary; call it whatever you want. It’ll be used by browsers in the “Save as…” dialog, etc.
  * You can hook into the CSV-generation API by passing `response` as the first argument to `csv.writer`. The `csv.writer` function expects a file-like object, and [`HttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse") objects fit the bill.
  * For each row in your CSV file, call `writer.writerow`, passing it an
  * The CSV module takes care of quoting for you, so you don’t have to worry about escaping strings with quotes or commas in them. Pass `writerow()` your raw strings, and it’ll do the right thing.


### Streaming large CSV files[¶](https://docs.djangoproject.com/en/5.0/howto/outputting-csv/#streaming-large-csv-files "Link to this heading")
When dealing with views that generate very large responses, you might want to consider using Django’s [`StreamingHttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.StreamingHttpResponse "django.http.StreamingHttpResponse") instead. For example, by streaming a file that takes a long time to generate you can avoid a load balancer dropping a connection that might have otherwise timed out while the server was generating the response.
In this example, we make full use of Python generators to efficiently handle the assembly and transmission of a large CSV file:
```
import csv

from django.http import StreamingHttpResponse


class Echo:
    """An object that implements just the write method of the file-like
    interface.
    """

    def write(self, value):
        """Write the value by returning it, instead of storing in a buffer."""
        return value


def some_streaming_csv_view(request):
    """A view that streams a large CSV file."""
    # Generate a sequence of rows. The range is based on the maximum number of
    # rows that can be handled by a single sheet in most spreadsheet
    # applications.
    rows = (["Row {}".format(idx), str(idx)] for idx in range(65536))
    pseudo_buffer = Echo()
    writer = csv.writer(pseudo_buffer)
    return StreamingHttpResponse(
        (writer.writerow(row) for row in rows),
        content_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="somefilename.csv"'},
    )

```

## Using the template system[¶](https://docs.djangoproject.com/en/5.0/howto/outputting-csv/#using-the-template-system "Link to this heading")
Alternatively, you can use the [Django template system](https://docs.djangoproject.com/en/5.0/topics/templates/) to generate CSV. This is lower-level than using the convenient Python
The idea here is to pass a list of items to your template, and have the template output the commas in a [`for`](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#std-templatetag-for) loop.
Here’s an example, which generates the same CSV file as above:
```
from django.http import HttpResponse
from django.template import loader


def some_view(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(
        content_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="somefilename.csv"'},
    )

    # The data is hard-coded here, but you could load it from a database or
    # some other source.
    csv_data = (
        ("First row", "Foo", "Bar", "Baz"),
        ("Second row", "A", "B", "C", '"Testing"', "Here's a quote"),
    )

    t = loader.get_template("my_template_name.txt")
    c = {"data": csv_data}
    response.write(t.render(c))
    return response

```

The only difference between this example and the previous example is that this one uses template loading instead of the CSV module. The rest of the code – such as the `content_type='text/csv'` – is the same.
Then, create the template `my_template_name.txt`, with this template code:
```
{% for row in data %}"{{ row.0|addslashes }}", "{{ row.1|addslashes }}", "{{ row.2|addslashes }}", "{{ row.3|addslashes }}", "{{ row.4|addslashes }}"
{% endfor %}

```

This short template iterates over the given data and displays a line of CSV for each row. It uses the [`addslashes`](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#std-templatefilter-addslashes) template filter to ensure there aren’t any problems with quotes.
## Other text-based formats[¶](https://docs.djangoproject.com/en/5.0/howto/outputting-csv/#other-text-based-formats "Link to this heading")
Notice that there isn’t very much specific to CSV here – just the specific output format. You can use either of these techniques to output any text-based format you can dream of. You can also use a similar technique to generate arbitrary binary data; see [How to create PDF files](https://docs.djangoproject.com/en/5.0/howto/outputting-pdf/) for an example.
Previous page and next page
[](https://docs.djangoproject.com/en/5.0/howto/logging/)
[How to create PDF files ](https://docs.djangoproject.com/en/5.0/howto/outputting-pdf/)
[](https://docs.djangoproject.com/en/5.0/howto/outputting-csv/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Paulo ALVES donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [How to create CSV output](https://docs.djangoproject.com/en/5.0/howto/outputting-csv/)
    * [Using the Python CSV library](https://docs.djangoproject.com/en/5.0/howto/outputting-csv/#using-the-python-csv-library)
      * [Streaming large CSV files](https://docs.djangoproject.com/en/5.0/howto/outputting-csv/#streaming-large-csv-files)
    * [Using the template system](https://docs.djangoproject.com/en/5.0/howto/outputting-csv/#using-the-template-system)
    * [Other text-based formats](https://docs.djangoproject.com/en/5.0/howto/outputting-csv/#other-text-based-formats)


### Browse
  * Prev: [How to configure and use logging](https://docs.djangoproject.com/en/5.0/howto/logging/)
  * Next: [How to create PDF files](https://docs.djangoproject.com/en/5.0/howto/outputting-pdf/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [“How-to” guides](https://docs.djangoproject.com/en/5.0/howto/)
      * How to create CSV output


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
