This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/howto/delete-app/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/howto/delete-app/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/howto/delete-app/)
  * [pl](https://docs.djangoproject.com/pl/5.0/howto/delete-app/)
  * [ko](https://docs.djangoproject.com/ko/5.0/howto/delete-app/)
  * [ja](https://docs.djangoproject.com/ja/5.0/howto/delete-app/)
  * [it](https://docs.djangoproject.com/it/5.0/howto/delete-app/)
  * [id](https://docs.djangoproject.com/id/5.0/howto/delete-app/)
  * [fr](https://docs.djangoproject.com/fr/5.0/howto/delete-app/)
  * [es](https://docs.djangoproject.com/es/5.0/howto/delete-app/)
  * [el](https://docs.djangoproject.com/el/5.0/howto/delete-app/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/howto/delete-app/)
  * [6.0](https://docs.djangoproject.com/en/6.0/howto/delete-app/)
  * [5.2](https://docs.djangoproject.com/en/5.2/howto/delete-app/)
  * [5.1](https://docs.djangoproject.com/en/5.1/howto/delete-app/)
  * [4.2](https://docs.djangoproject.com/en/4.2/howto/delete-app/)


  * [](https://docs.djangoproject.com/en/5.0/howto/delete-app/#top)


# How to delete a Django application[¶](https://docs.djangoproject.com/en/5.0/howto/delete-app/#how-to-delete-a-django-application "Link to this heading")
Django provides the ability to group sets of features into Python packages called [applications](https://docs.djangoproject.com/en/5.0/ref/applications/). When requirements change, apps may become obsolete or unnecessary. The following steps will help you delete an application safely.
  1. Remove all references to the app (imports, foreign keys etc.).
  2. Remove all models from the corresponding `models.py` file.
  3. Create relevant migrations by running [`makemigrations`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-makemigrations). This step generates a migration that deletes tables for the removed models, and any other required migration for updating relationships connected to those models.
  4. [Squash](https://docs.djangoproject.com/en/5.0/topics/migrations/#migration-squashing) out references to the app in other apps’ migrations.
  5. Apply migrations locally, runs tests, and verify the correctness of your project.
  6. Deploy/release your updated Django project.
  7. Remove the app from [`INSTALLED_APPS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-INSTALLED_APPS).
  8. Finally, remove the app’s directory.

Previous page and next page
[](https://docs.djangoproject.com/en/5.0/howto/writing-migrations/)
[Django FAQ ](https://docs.djangoproject.com/en/5.0/faq/)
[](https://docs.djangoproject.com/en/5.0/howto/delete-app/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Ilya Usanov donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [How to delete a Django application](https://docs.djangoproject.com/en/5.0/howto/delete-app/)


### Browse
  * Prev: [How to create database migrations](https://docs.djangoproject.com/en/5.0/howto/writing-migrations/)
  * Next: [Django FAQ](https://docs.djangoproject.com/en/5.0/faq/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [“How-to” guides](https://docs.djangoproject.com/en/5.0/howto/)
      * How to delete a Django application


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
