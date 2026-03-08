##  `contrib` app checks[¶](https://docs.djangoproject.com/en/5.0/ref/checks/#contrib-app-checks "Link to this heading")
###  `admin`[¶](https://docs.djangoproject.com/en/5.0/ref/checks/#admin "Link to this heading")
Admin checks are all performed as part of the `admin` tag.
The following checks are performed on any [`ModelAdmin`](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin "django.contrib.admin.ModelAdmin") (or subclass) that is registered with the admin site:
  * **admin.E001** : The value of `raw_id_fields` must be a list or tuple.
  * **admin.E002** : The value of `raw_id_fields[n]` refers to `<field name>`, which is not a field of `<model>`.
  * **admin.E003** : The value of `raw_id_fields[n]` must be a foreign key or a many-to-many field.
  * **admin.E004** : The value of `fields` must be a list or tuple.
  * **admin.E005** : Both `fieldsets` and `fields` are specified.
  * **admin.E006** : The value of `fields` contains duplicate field(s).
  * **admin.E007** : The value of `fieldsets` must be a list or tuple.
  * **admin.E008** : The value of `fieldsets[n]` must be a list or tuple.
  * **admin.E009** : The value of `fieldsets[n]` must be of length 2.
  * **admin.E010** : The value of `fieldsets[n][1]` must be a dictionary.
  * **admin.E011** : The value of `fieldsets[n][1]` must contain the key `fields`.
  * **admin.E012** : There are duplicate field(s) in `fieldsets[n][1]`.
  * **admin.E013** : The value of `fields[n]/filter_horizontal[n]/filter_vertical[n]/fieldsets[n][m]` cannot include the `ManyToManyField` `<field name>`, because that field manually specifies a relationship model.
  * **admin.E014** : The value of `exclude` must be a list or tuple.
  * **admin.E015** : The value of `exclude` contains duplicate field(s).
  * **admin.E016** : The value of `form` must inherit from `BaseModelForm`.
  * **admin.E017** : The value of `filter_vertical` must be a list or tuple.
  * **admin.E018** : The value of `filter_horizontal` must be a list or tuple.
  * **admin.E019** : The value of `filter_vertical[n]/filter_horizontal[n]` refers to `<field name>`, which is not a field of `<model>`.
  * **admin.E020** : The value of `filter_vertical[n]/filter_horizontal[n]` must be a many-to-many field.
  * **admin.E021** : The value of `radio_fields` must be a dictionary.
  * **admin.E022** : The value of `radio_fields` refers to `<field name>`, which is not a field of `<model>`.
  * **admin.E023** : The value of `radio_fields` refers to `<field name>`, which is not an instance of `ForeignKey`, and does not have a `choices` definition.
  * **admin.E024** : The value of `radio_fields[<field name>]` must be either `admin.HORIZONTAL` or `admin.VERTICAL`.
  * **admin.E025** : The value of `view_on_site` must be either a callable or a boolean value.
  * **admin.E026** : The value of `prepopulated_fields` must be a dictionary.
  * **admin.E027** : The value of `prepopulated_fields` refers to `<field name>`, which is not a field of `<model>`.
  * **admin.E028** : The value of `prepopulated_fields` refers to `<field name>`, which must not be a `DateTimeField`, a `ForeignKey`, a `OneToOneField`, or a `ManyToManyField` field.
  * **admin.E029** : The value of `prepopulated_fields[<field name>]` must be a list or tuple.
  * **admin.E030** : The value of `prepopulated_fields` refers to `<field name>`, which is not a field of `<model>`.
  * **admin.E031** : The value of `ordering` must be a list or tuple.
  * **admin.E032** : The value of `ordering` has the random ordering marker `?`, but contains other fields as well.
  * **admin.E033** : The value of `ordering` refers to `<field name>`, which is not a field of `<model>`.
  * **admin.E034** : The value of `readonly_fields` must be a list or tuple.
  * **admin.E035** : The value of `readonly_fields[n]` refers to `<field_name>`, which is not a callable, an attribute of `<ModelAdmin class>`, or an attribute of `<model>`.
  * **admin.E036** : The value of `autocomplete_fields` must be a list or tuple.
  * **admin.E037** : The value of `autocomplete_fields[n]` refers to `<field name>`, which is not a field of `<model>`.
  * **admin.E038** : The value of `autocomplete_fields[n]` must be a foreign key or a many-to-many field.
  * **admin.E039** : An admin for model `<model>` has to be registered to be referenced by `<modeladmin>.autocomplete_fields`.
  * **admin.E040** : `<modeladmin>` must define `search_fields`, because it’s referenced by `<other_modeladmin>.autocomplete_fields`.


####  `ModelAdmin`[¶](https://docs.djangoproject.com/en/5.0/ref/checks/#modeladmin "Link to this heading")
The following checks are performed on any [`ModelAdmin`](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin "django.contrib.admin.ModelAdmin") that is registered with the admin site:
  * **admin.E101** : The value of `save_as` must be a boolean.
  * **admin.E102** : The value of `save_on_top` must be a boolean.
  * **admin.E103** : The value of `inlines` must be a list or tuple.
  * **admin.E104** : `<InlineModelAdmin class>` must inherit from `InlineModelAdmin`.
  * **admin.E105** : `<InlineModelAdmin class>` must have a `model` attribute.
  * **admin.E106** : The value of `<InlineModelAdmin class>.model` must be a `Model`.
  * **admin.E107** : The value of `list_display` must be a list or tuple.
  * **admin.E108** : The value of `list_display[n]` refers to `<label>`, which is not a callable, an attribute of `<ModelAdmin class>`, or an attribute or method on `<model>`.
  * **admin.E109** : The value of `list_display[n]` must not be a many-to-many field or a reverse foreign key.
  * **admin.E110** : The value of `list_display_links` must be a list, a tuple, or `None`.
  * **admin.E111** : The value of `list_display_links[n]` refers to `<label>`, which is not defined in `list_display`.
  * **admin.E112** : The value of `list_filter` must be a list or tuple.
  * **admin.E113** : The value of `list_filter[n]` must inherit from `ListFilter`.
  * **admin.E114** : The value of `list_filter[n]` must not inherit from `FieldListFilter`.
  * **admin.E115** : The value of `list_filter[n][1]` must inherit from `FieldListFilter`.
  * **admin.E116** : The value of `list_filter[n]` refers to `<label>`, which does not refer to a Field.
  * **admin.E117** : The value of `list_select_related` must be a boolean, tuple or list.
  * **admin.E118** : The value of `list_per_page` must be an integer.
  * **admin.E119** : The value of `list_max_show_all` must be an integer.
  * **admin.E120** : The value of `list_editable` must be a list or tuple.
  * **admin.E121** : The value of `list_editable[n]` refers to `<label>`, which is not a field of `<model>`.
  * **admin.E122** : The value of `list_editable[n]` refers to `<label>`, which is not contained in `list_display`.
  * **admin.E123** : The value of `list_editable[n]` cannot be in both `list_editable` and `list_display_links`.
  * **admin.E124** : The value of `list_editable[n]` refers to the first field in `list_display` (`<label>`), which cannot be used unless `list_display_links` is set.
  * **admin.E125** : The value of `list_editable[n]` refers to `<field name>`, which is not editable through the admin.
  * **admin.E126** : The value of `search_fields` must be a list or tuple.
  * **admin.E127** : The value of `date_hierarchy` refers to `<field name>`, which does not refer to a Field.
  * **admin.E128** : The value of `date_hierarchy` must be a `DateField` or `DateTimeField`.
  * **admin.E129** : `<modeladmin>` must define a `has_<foo>_permission()` method for the `<action>` action.
  * **admin.E130** : `__name__` attributes of actions defined in `<modeladmin>` must be unique. Name `<name>` is not unique.


####  `InlineModelAdmin`[¶](https://docs.djangoproject.com/en/5.0/ref/checks/#inlinemodeladmin "Link to this heading")
The following checks are performed on any [`InlineModelAdmin`](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#django.contrib.admin.InlineModelAdmin "django.contrib.admin.InlineModelAdmin") that is registered as an inline on a [`ModelAdmin`](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin "django.contrib.admin.ModelAdmin").
  * **admin.E201** : Cannot exclude the field `<field name>`, because it is the foreign key to the parent model `<app_label>.<model>`.
  * **admin.E202** : `<model>` has no `ForeignKey` to `<parent model>`./ `<model>` has more than one `ForeignKey` to `<parent model>`. You must specify a `fk_name` attribute.
  * **admin.E203** : The value of `extra` must be an integer.
  * **admin.E204** : The value of `max_num` must be an integer.
  * **admin.E205** : The value of `min_num` must be an integer.
  * **admin.E206** : The value of `formset` must inherit from `BaseModelFormSet`.


####  `GenericInlineModelAdmin`[¶](https://docs.djangoproject.com/en/5.0/ref/checks/#genericinlinemodeladmin "Link to this heading")
The following checks are performed on any [`GenericInlineModelAdmin`](https://docs.djangoproject.com/en/5.0/ref/contrib/contenttypes/#django.contrib.contenttypes.admin.GenericInlineModelAdmin "django.contrib.contenttypes.admin.GenericInlineModelAdmin") that is registered as an inline on a [`ModelAdmin`](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin "django.contrib.admin.ModelAdmin").
  * **admin.E301** : `'ct_field'` references `<label>`, which is not a field on `<model>`.
  * **admin.E302** : `'ct_fk_field'` references `<label>`, which is not a field on `<model>`.
  * **admin.E303** : `<model>` has no `GenericForeignKey`.
  * **admin.E304** : `<model>` has no `GenericForeignKey` using content type field `<field name>` and object ID field `<field name>`.


####  `AdminSite`[¶](https://docs.djangoproject.com/en/5.0/ref/checks/#adminsite "Link to this heading")
The following checks are performed on the default [`AdminSite`](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#django.contrib.admin.AdminSite "django.contrib.admin.AdminSite"):
  * **admin.E401** : [`django.contrib.contenttypes`](https://docs.djangoproject.com/en/5.0/ref/contrib/contenttypes/#module-django.contrib.contenttypes "django.contrib.contenttypes: Provides generic interface to installed models.") must be in [`INSTALLED_APPS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-INSTALLED_APPS) in order to use the admin application.
  * **admin.E402** : [`django.contrib.auth.context_processors.auth`](https://docs.djangoproject.com/en/5.0/ref/templates/api/#django.contrib.auth.context_processors.auth "django.contrib.auth.context_processors.auth") must be enabled in [`DjangoTemplates`](https://docs.djangoproject.com/en/5.0/topics/templates/#django.template.backends.django.DjangoTemplates "django.template.backends.django.DjangoTemplates") ([`TEMPLATES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TEMPLATES)) if using the default auth backend in order to use the admin application.
  * **admin.E403** : A [`django.template.backends.django.DjangoTemplates`](https://docs.djangoproject.com/en/5.0/topics/templates/#django.template.backends.django.DjangoTemplates "django.template.backends.django.DjangoTemplates") instance must be configured in [`TEMPLATES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TEMPLATES) in order to use the admin application.
  * **admin.E404** : `django.contrib.messages.context_processors.messages` must be enabled in [`DjangoTemplates`](https://docs.djangoproject.com/en/5.0/topics/templates/#django.template.backends.django.DjangoTemplates "django.template.backends.django.DjangoTemplates") ([`TEMPLATES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TEMPLATES)) in order to use the admin application.
  * **admin.E405** : [`django.contrib.auth`](https://docs.djangoproject.com/en/5.0/topics/auth/#module-django.contrib.auth "django.contrib.auth: Django's authentication framework.") must be in [`INSTALLED_APPS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-INSTALLED_APPS) in order to use the admin application.
  * **admin.E406** : [`django.contrib.messages`](https://docs.djangoproject.com/en/5.0/ref/contrib/messages/#module-django.contrib.messages "django.contrib.messages: Provides cookie- and session-based temporary message storage.") must be in [`INSTALLED_APPS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-INSTALLED_APPS) in order to use the admin application.
  * **admin.E408** : [`django.contrib.auth.middleware.AuthenticationMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.contrib.auth.middleware.AuthenticationMiddleware "django.contrib.auth.middleware.AuthenticationMiddleware") must be in [`MIDDLEWARE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MIDDLEWARE) in order to use the admin application.
  * **admin.E409** : [`django.contrib.messages.middleware.MessageMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.contrib.messages.middleware.MessageMiddleware "django.contrib.messages.middleware.MessageMiddleware") must be in [`MIDDLEWARE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MIDDLEWARE) in order to use the admin application.
  * **admin.E410** : [`django.contrib.sessions.middleware.SessionMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.contrib.sessions.middleware.SessionMiddleware "django.contrib.sessions.middleware.SessionMiddleware") must be in [`MIDDLEWARE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MIDDLEWARE) in order to use the admin application.
  * **admin.W411** : `django.template.context_processors.request` must be enabled in [`DjangoTemplates`](https://docs.djangoproject.com/en/5.0/topics/templates/#django.template.backends.django.DjangoTemplates "django.template.backends.django.DjangoTemplates") ([`TEMPLATES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TEMPLATES)) in order to use the admin navigation sidebar.


###  `auth`[¶](https://docs.djangoproject.com/en/5.0/ref/checks/#auth "Link to this heading")
  * **auth.E001** : `REQUIRED_FIELDS` must be a list or tuple.
  * **auth.E002** : The field named as the `USERNAME_FIELD` for a custom user model must not be included in `REQUIRED_FIELDS`.
  * **auth.E003** : `<field>` must be unique because it is named as the `USERNAME_FIELD`.
  * **auth.W004** : `<field>` is named as the `USERNAME_FIELD`, but it is not unique.
  * **auth.E005** : The permission codenamed `<codename>` clashes with a builtin permission for model `<model>`.
  * **auth.E006** : The permission codenamed `<codename>` is duplicated for model `<model>`.
  * **auth.E007** : The [`verbose_name`](https://docs.djangoproject.com/en/5.0/ref/models/options/#django.db.models.Options.verbose_name "django.db.models.Options.verbose_name") of model `<model>` must be at most 244 characters for its builtin permission names to be at most 255 characters.
  * **auth.E008** : The permission named `<name>` of model `<model>` is longer than 255 characters.
  * **auth.C009** : `<User model>.is_anonymous` must be an attribute or property rather than a method. Ignoring this is a security issue as anonymous users will be treated as authenticated!
  * **auth.C010** : `<User model>.is_authenticated` must be an attribute or property rather than a method. Ignoring this is a security issue as anonymous users will be treated as authenticated!
  * **auth.E011** : The name of model `<model>` must be at most 93 characters for its builtin permission names to be at most 100 characters.
  * **auth.E012** : The permission codenamed `<codename>` of model `<model>` is longer than 100 characters.


###  `contenttypes`[¶](https://docs.djangoproject.com/en/5.0/ref/checks/#contenttypes "Link to this heading")
The following checks are performed when a model contains a [`GenericForeignKey`](https://docs.djangoproject.com/en/5.0/ref/contrib/contenttypes/#django.contrib.contenttypes.fields.GenericForeignKey "django.contrib.contenttypes.fields.GenericForeignKey") or [`GenericRelation`](https://docs.djangoproject.com/en/5.0/ref/contrib/contenttypes/#django.contrib.contenttypes.fields.GenericRelation "django.contrib.contenttypes.fields.GenericRelation"):
  * **contenttypes.E001** : The `GenericForeignKey` object ID references the nonexistent field `<field>`.
  * **contenttypes.E002** : The `GenericForeignKey` content type references the nonexistent field `<field>`.
  * **contenttypes.E003** : `<field>` is not a `ForeignKey`.
  * **contenttypes.E004** : `<field>` is not a `ForeignKey` to `contenttypes.ContentType`.
  * **contenttypes.E005** : Model names must be at most 100 characters.


###  `postgres`[¶](https://docs.djangoproject.com/en/5.0/ref/checks/#postgres "Link to this heading")
The following checks are performed on [`django.contrib.postgres`](https://docs.djangoproject.com/en/5.0/ref/contrib/postgres/#module-django.contrib.postgres "django.contrib.postgres: PostgreSQL-specific fields and features") model fields:
  * **postgres.E001** : Base field for array has errors: …
  * **postgres.E002** : Base field for array cannot be a related field.
  * **postgres.E003** : `<field>` default should be a callable instead of an instance so that it’s not shared between all field instances. _This check was changed to_ `fields.E010` _in Django 3.1_.
  * **postgres.W004** : Base field for array has warnings: …


###  `sites`[¶](https://docs.djangoproject.com/en/5.0/ref/checks/#sites "Link to this heading")
The following checks are performed on any model using a [`CurrentSiteManager`](https://docs.djangoproject.com/en/5.0/ref/contrib/sites/#django.contrib.sites.managers.CurrentSiteManager "django.contrib.sites.managers.CurrentSiteManager"):
  * **sites.E001** : `CurrentSiteManager` could not find a field named `<field name>`.
  * **sites.E002** : `CurrentSiteManager` cannot use `<field>` as it is not a foreign key or a many-to-many field.


The following checks verify that [`django.contrib.sites`](https://docs.djangoproject.com/en/5.0/ref/contrib/sites/#module-django.contrib.sites "django.contrib.sites: Lets you operate multiple websites from the same database and Django project") is correctly configured:
  * **sites.E101** : The [`SITE_ID`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SITE_ID) setting must be an integer.


###  `staticfiles`[¶](https://docs.djangoproject.com/en/5.0/ref/checks/#staticfiles "Link to this heading")
The following checks verify that [`django.contrib.staticfiles`](https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/#module-django.contrib.staticfiles "django.contrib.staticfiles: An app for handling static files.") is correctly configured:
  * **staticfiles.E001** : The [`STATICFILES_DIRS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STATICFILES_DIRS) setting is not a tuple or list.
  * **staticfiles.E002** : The [`STATICFILES_DIRS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STATICFILES_DIRS) setting should not contain the [`STATIC_ROOT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STATIC_ROOT) setting.
  * **staticfiles.E003** : The prefix `<prefix>` in the [`STATICFILES_DIRS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STATICFILES_DIRS) setting must not end with a slash.
  * **staticfiles.W004** : The directory `<directory>` in the [`STATICFILES_DIRS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STATICFILES_DIRS) does not exist.
  * **staticfiles.E005** : The [`STORAGES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STORAGES) setting must define a `staticfiles` storage.

Previous page and next page
[](https://docs.djangoproject.com/en/5.0/ref/applications/)
[Built-in class-based views API ](https://docs.djangoproject.com/en/5.0/ref/class-based-views/)
[](https://docs.djangoproject.com/en/5.0/ref/checks/#top)
