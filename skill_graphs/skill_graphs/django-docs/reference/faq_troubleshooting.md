This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/faq/troubleshooting/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/faq/troubleshooting/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/faq/troubleshooting/)
  * [pl](https://docs.djangoproject.com/pl/5.0/faq/troubleshooting/)
  * [ko](https://docs.djangoproject.com/ko/5.0/faq/troubleshooting/)
  * [ja](https://docs.djangoproject.com/ja/5.0/faq/troubleshooting/)
  * [it](https://docs.djangoproject.com/it/5.0/faq/troubleshooting/)
  * [id](https://docs.djangoproject.com/id/5.0/faq/troubleshooting/)
  * [fr](https://docs.djangoproject.com/fr/5.0/faq/troubleshooting/)
  * [es](https://docs.djangoproject.com/es/5.0/faq/troubleshooting/)
  * [el](https://docs.djangoproject.com/el/5.0/faq/troubleshooting/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/faq/troubleshooting/)
  * [6.0](https://docs.djangoproject.com/en/6.0/faq/troubleshooting/)
  * [5.2](https://docs.djangoproject.com/en/5.2/faq/troubleshooting/)
  * [5.1](https://docs.djangoproject.com/en/5.1/faq/troubleshooting/)
  * [4.2](https://docs.djangoproject.com/en/4.2/faq/troubleshooting/)
  * [4.1](https://docs.djangoproject.com/en/4.1/faq/troubleshooting/)
  * [4.0](https://docs.djangoproject.com/en/4.0/faq/troubleshooting/)
  * [3.2](https://docs.djangoproject.com/en/3.2/faq/troubleshooting/)
  * [3.1](https://docs.djangoproject.com/en/3.1/faq/troubleshooting/)
  * [3.0](https://docs.djangoproject.com/en/3.0/faq/troubleshooting/)
  * [2.2](https://docs.djangoproject.com/en/2.2/faq/troubleshooting/)
  * [2.1](https://docs.djangoproject.com/en/2.1/faq/troubleshooting/)
  * [2.0](https://docs.djangoproject.com/en/2.0/faq/troubleshooting/)
  * [1.11](https://docs.djangoproject.com/en/1.11/faq/troubleshooting/)
  * [1.10](https://docs.djangoproject.com/en/1.10/faq/troubleshooting/)
  * [1.8](https://docs.djangoproject.com/en/1.8/faq/troubleshooting/)


  * [](https://docs.djangoproject.com/en/5.0/faq/troubleshooting/#top)


# Troubleshooting[¶](https://docs.djangoproject.com/en/5.0/faq/troubleshooting/#troubleshooting "Link to this heading")
This page contains some advice about errors and problems commonly encountered during the development of Django applications.
## Problems running `django-admin`[¶](https://docs.djangoproject.com/en/5.0/faq/troubleshooting/#problems-running-django-admin "Link to this heading")
###  `command not found: django-admin`[¶](https://docs.djangoproject.com/en/5.0/faq/troubleshooting/#command-not-found-django-admin "Link to this heading")
[django-admin](https://docs.djangoproject.com/en/5.0/ref/django-admin/) should be on your system path if you installed Django via `pip`. If it’s not in your path, ensure you have your virtual environment activated and you can try running the equivalent command `python -m django`.
### macOS permissions[¶](https://docs.djangoproject.com/en/5.0/faq/troubleshooting/#macos-permissions "Link to this heading")
If you’re using macOS, you may see the message “permission denied” when you try to run `django-admin`. This is because, on Unix-based systems like macOS, a file must be marked as “executable” before it can be run as a program. To do this, open Terminal.app and navigate (using the `cd` command) to the directory where [django-admin](https://docs.djangoproject.com/en/5.0/ref/django-admin/) is installed, then run the command `sudo chmod +x django-admin`.
## Miscellaneous[¶](https://docs.djangoproject.com/en/5.0/faq/troubleshooting/#miscellaneous "Link to this heading")
### I’m getting a `UnicodeDecodeError`. What am I doing wrong?[¶](https://docs.djangoproject.com/en/5.0/faq/troubleshooting/#i-m-getting-a-unicodedecodeerror-what-am-i-doing-wrong "Link to this heading")
This class of errors happen when a bytestring containing non-ASCII sequences is transformed into a Unicode string and the specified encoding is incorrect. The output generally looks like this:
```
UnicodeDecodeError: 'ascii' codec can't decode byte 0x?? in position ?:
ordinal not in range(128)

```

The resolution mostly depends on the context, however here are two common pitfalls producing this error:
  * Your system locale may be a default ASCII locale, like the “C” locale on UNIX-like systems (can be checked by the `locale` command). If it’s the case, please refer to your system documentation to learn how you can change this to a UTF-8 locale.


Related resources:
  * [Unicode in Django](https://docs.djangoproject.com/en/5.0/ref/unicode/)

Previous page and next page
[](https://docs.djangoproject.com/en/5.0/faq/contributing/)
[API Reference ](https://docs.djangoproject.com/en/5.0/ref/)
[](https://docs.djangoproject.com/en/5.0/faq/troubleshooting/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Mehmet Caner Cakici donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [Troubleshooting](https://docs.djangoproject.com/en/5.0/faq/troubleshooting/)
    * [Problems running `django-admin`](https://docs.djangoproject.com/en/5.0/faq/troubleshooting/#problems-running-django-admin)
      * [`command not found: django-admin`](https://docs.djangoproject.com/en/5.0/faq/troubleshooting/#command-not-found-django-admin)
      * [macOS permissions](https://docs.djangoproject.com/en/5.0/faq/troubleshooting/#macos-permissions)
    * [Miscellaneous](https://docs.djangoproject.com/en/5.0/faq/troubleshooting/#miscellaneous)
      * [I’m getting a `UnicodeDecodeError`. What am I doing wrong?](https://docs.djangoproject.com/en/5.0/faq/troubleshooting/#i-m-getting-a-unicodedecodeerror-what-am-i-doing-wrong)


### Browse
  * Prev: [FAQ: Contributing code](https://docs.djangoproject.com/en/5.0/faq/contributing/)
  * Next: [API Reference](https://docs.djangoproject.com/en/5.0/ref/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [Django FAQ](https://docs.djangoproject.com/en/5.0/faq/)
      * Troubleshooting


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
