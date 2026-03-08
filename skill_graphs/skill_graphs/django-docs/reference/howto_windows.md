This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/howto/windows/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/howto/windows/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/howto/windows/)
  * [pl](https://docs.djangoproject.com/pl/5.0/howto/windows/)
  * [ko](https://docs.djangoproject.com/ko/5.0/howto/windows/)
  * [ja](https://docs.djangoproject.com/ja/5.0/howto/windows/)
  * [it](https://docs.djangoproject.com/it/5.0/howto/windows/)
  * [id](https://docs.djangoproject.com/id/5.0/howto/windows/)
  * [fr](https://docs.djangoproject.com/fr/5.0/howto/windows/)
  * [es](https://docs.djangoproject.com/es/5.0/howto/windows/)
  * [el](https://docs.djangoproject.com/el/5.0/howto/windows/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/howto/windows/)
  * [6.0](https://docs.djangoproject.com/en/6.0/howto/windows/)
  * [5.2](https://docs.djangoproject.com/en/5.2/howto/windows/)
  * [5.1](https://docs.djangoproject.com/en/5.1/howto/windows/)
  * [4.2](https://docs.djangoproject.com/en/4.2/howto/windows/)
  * [4.1](https://docs.djangoproject.com/en/4.1/howto/windows/)
  * [4.0](https://docs.djangoproject.com/en/4.0/howto/windows/)
  * [3.2](https://docs.djangoproject.com/en/3.2/howto/windows/)
  * [3.1](https://docs.djangoproject.com/en/3.1/howto/windows/)
  * [3.0](https://docs.djangoproject.com/en/3.0/howto/windows/)
  * [2.2](https://docs.djangoproject.com/en/2.2/howto/windows/)
  * [2.1](https://docs.djangoproject.com/en/2.1/howto/windows/)
  * [2.0](https://docs.djangoproject.com/en/2.0/howto/windows/)
  * [1.11](https://docs.djangoproject.com/en/1.11/howto/windows/)
  * [1.10](https://docs.djangoproject.com/en/1.10/howto/windows/)
  * [1.8](https://docs.djangoproject.com/en/1.8/howto/windows/)


  * [](https://docs.djangoproject.com/en/5.0/howto/windows/#top)


# How to install Django on Windows[¶](https://docs.djangoproject.com/en/5.0/howto/windows/#how-to-install-django-on-windows "Link to this heading")
This document will guide you through installing Python 3.12 and Django on Windows. It also provides instructions for setting up a virtual environment, which makes it easier to work on Python projects. This is meant as a beginner’s guide for users working on Django projects and does not reflect how Django should be installed when developing changes for Django itself.
The steps in this guide have been tested with Windows 10. In other versions, the steps would be similar. You will need to be familiar with using the Windows command prompt.
## Install Python[¶](https://docs.djangoproject.com/en/5.0/howto/windows/#install-python "Link to this heading")
Django is a Python web framework, thus requiring Python to be installed on your machine. At the time of writing, Python 3.12 is the latest version.
To install Python on your machine go to
After installation, open the command prompt and check that the Python version matches the version you installed by executing:
```
...\> py --version

```

See also
For more details, see
## About `pip`[¶](https://docs.djangoproject.com/en/5.0/howto/windows/#about-pip "Link to this heading")
`pip` to install Python packages from the command line.
## Setting up a virtual environment[¶](https://docs.djangoproject.com/en/5.0/howto/windows/#setting-up-a-virtual-environment "Link to this heading")
It is best practice to provide a dedicated environment for each Django project you create. There are many options to manage environments and packages within the Python ecosystem, some of which are recommended in the
To create a virtual environment for your project, open a new command prompt, navigate to the folder where you want to create your project and then enter the following:
```
...\> py -m venv project-name

```

This will create a folder called ‘project-name’ if it does not already exist and set up the virtual environment. To activate the environment, run:
```
...\> project-name\Scripts\activate.bat

```

The virtual environment will be activated and you’ll see “(project-name)” next to the command prompt to designate that. Each time you start a new command prompt, you’ll need to activate the environment again.
## Install Django[¶](https://docs.djangoproject.com/en/5.0/howto/windows/#install-django "Link to this heading")
Django can be installed easily using `pip` within your virtual environment.
In the command prompt, ensure your virtual environment is active, and execute the following command:
```
...\> py -m pip install Django

```

This will download and install the latest Django release.
After the installation has completed, you can verify your Django installation by executing `django-admin --version` in the command prompt.
See [Get your database running](https://docs.djangoproject.com/en/5.0/topics/install/#database-installation) for information on database installation with Django.
## Colored terminal output[¶](https://docs.djangoproject.com/en/5.0/howto/windows/#colored-terminal-output "Link to this heading")
A quality-of-life feature adds colored (rather than monochrome) output to the terminal. In modern terminals this should work for both CMD and PowerShell. If for some reason this needs to be disabled, set the environmental variable [`DJANGO_COLORS`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#envvar-DJANGO_COLORS) to `nocolor`.
On older Windows versions, or legacy terminals,
```
...\> py -m pip install "colorama >= 0.4.6"

```

See [Syntax coloring](https://docs.djangoproject.com/en/5.0/ref/django-admin/#syntax-coloring) for more information on color settings.
## Common pitfalls[¶](https://docs.djangoproject.com/en/5.0/howto/windows/#common-pitfalls "Link to this heading")
  * If `django-admin` only displays the help text no matter what arguments it is given, there is probably a problem with the file association in Windows. Check if there is more than one environment variable set for running Python scripts in `PATH`. This usually occurs when there is more than one Python version installed.
  * If you are connecting to the internet behind a proxy, there might be problems in running the command `py -m pip install Django`. Set the environment variables for proxy configuration in the command prompt as follows:
```
...\> set http_proxy=http://username:password@proxyserver:proxyport
...\> set https_proxy=https://username:password@proxyserver:proxyport

```

  * In general, Django assumes that `UTF-8` encoding is used for I/O. This may cause problems if your system is set to use a different encoding. Recent versions of Python allow setting the `UTF-8` encoding. Windows 10 also provides a system-wide setting by checking `Use Unicode UTF-8 for worldwide language support` in Language ‣ Administrative Language Settings ‣ Change system locale in system settings.

Previous page and next page
[](https://docs.djangoproject.com/en/5.0/howto/static-files/deployment/)
[How to create database migrations ](https://docs.djangoproject.com/en/5.0/howto/writing-migrations/)
[](https://docs.djangoproject.com/en/5.0/howto/windows/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ OrthoPatients donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [How to install Django on Windows](https://docs.djangoproject.com/en/5.0/howto/windows/)
    * [Install Python](https://docs.djangoproject.com/en/5.0/howto/windows/#install-python)
    * [About `pip`](https://docs.djangoproject.com/en/5.0/howto/windows/#about-pip)
    * [Setting up a virtual environment](https://docs.djangoproject.com/en/5.0/howto/windows/#setting-up-a-virtual-environment)
    * [Install Django](https://docs.djangoproject.com/en/5.0/howto/windows/#install-django)
    * [Colored terminal output](https://docs.djangoproject.com/en/5.0/howto/windows/#colored-terminal-output)
    * [Common pitfalls](https://docs.djangoproject.com/en/5.0/howto/windows/#common-pitfalls)


### Browse
  * Prev: [How to deploy static files](https://docs.djangoproject.com/en/5.0/howto/static-files/deployment/)
  * Next: [How to create database migrations](https://docs.djangoproject.com/en/5.0/howto/writing-migrations/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [“How-to” guides](https://docs.djangoproject.com/en/5.0/howto/)
      * How to install Django on Windows


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
