##  [Sites](https://docs.djangoproject.com/en/5.0/ref/settings/#id16)[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#sites "Link to this heading")
Settings for [`django.contrib.sites`](https://docs.djangoproject.com/en/5.0/ref/contrib/sites/#module-django.contrib.sites "django.contrib.sites: Lets you operate multiple websites from the same database and Django project").
###  `SITE_ID`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#site-id "Link to this heading")
Default: Not defined
The ID, as an integer, of the current site in the `django_site` database table. This is used so that application data can hook into specific sites and a single database can manage content for multiple sites.
