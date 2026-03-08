## Core system checks[¶](https://docs.djangoproject.com/en/5.0/ref/checks/#core-system-checks "Link to this heading")
### Asynchronous support[¶](https://docs.djangoproject.com/en/5.0/ref/checks/#asynchronous-support "Link to this heading")
The following checks verify your setup for [Asynchronous support](https://docs.djangoproject.com/en/5.0/topics/async/):
  * **async.E001** : You should not set the [`DJANGO_ALLOW_ASYNC_UNSAFE`](https://docs.djangoproject.com/en/5.0/topics/async/#envvar-DJANGO_ALLOW_ASYNC_UNSAFE) environment variable in deployment. This disables [async safety protection](https://docs.djangoproject.com/en/5.0/topics/async/#async-safety).


### Backwards compatibility[¶](https://docs.djangoproject.com/en/5.0/ref/checks/#backwards-compatibility "Link to this heading")
Compatibility checks warn of potential problems that might occur after upgrading Django.
  * **2_0.W001** : Your URL pattern `<pattern>` has a `route` that contains `(?P<`, begins with a `^`, or ends with a `$`. This was likely an oversight when migrating from `url()` to [`path()`](https://docs.djangoproject.com/en/5.0/ref/urls/#django.urls.path "django.urls.path").
  * **4_0.E001** : As of Django 4.0, the values in the [`CSRF_TRUSTED_ORIGINS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CSRF_TRUSTED_ORIGINS) setting must start with a scheme (usually `http://` or `https://`) but found `<hostname>`.


### Caches[¶](https://docs.djangoproject.com/en/5.0/ref/checks/#caches "Link to this heading")
The following checks verify that your [`CACHES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CACHES) setting is correctly configured:
  * **caches.E001** : You must define a `'default'` cache in your [`CACHES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CACHES) setting.
  * **caches.W002** : Your `<cache>` configuration might expose your cache or lead to corruption of your data because its [`LOCATION`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CACHES-LOCATION) matches/is inside/contains [`MEDIA_ROOT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MEDIA_ROOT)/[`STATIC_ROOT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STATIC_ROOT)/[`STATICFILES_DIRS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STATICFILES_DIRS).
  * **caches.W003** : Your `<cache>` cache [`LOCATION`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CACHES-LOCATION) is relative. Use an absolute path instead.


### Database[¶](https://docs.djangoproject.com/en/5.0/ref/checks/#database "Link to this heading")
#### MySQL and MariaDB[¶](https://docs.djangoproject.com/en/5.0/ref/checks/#mysql-and-mariadb "Link to this heading")
If you’re using MySQL or MariaDB, the following checks will be performed:
  * **mysql.E001** : MySQL/MariaDB does not allow unique `CharField`s to have a `max_length` > 255. _This check was changed to_ `mysql.W003` _in Django 3.1 as the real maximum size depends on many factors._
  * **mysql.W002** : MySQL/MariaDB Strict Mode is not set for database connection `<alias>`. See also [Setting sql_mode](https://docs.djangoproject.com/en/5.0/ref/databases/#mysql-sql-mode).
  * **mysql.W003** : MySQL/MariaDB may not allow unique `CharField`s to have a `max_length` > 255.


### Managing files[¶](https://docs.djangoproject.com/en/5.0/ref/checks/#managing-files "Link to this heading")
The following checks verify your setup for [Managing files](https://docs.djangoproject.com/en/5.0/topics/files/):
  * **files.E001** : The [`FILE_UPLOAD_TEMP_DIR`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-FILE_UPLOAD_TEMP_DIR) setting refers to the nonexistent directory `<path>`.


### Model fields[¶](https://docs.djangoproject.com/en/5.0/ref/checks/#model-fields "Link to this heading")
  * **fields.E001** : Field names must not end with an underscore.
  * **fields.E002** : Field names must not contain `"__"`.
  * **fields.E003** : `pk` is a reserved word that cannot be used as a field name.
  * **fields.E004** : `choices` must be a mapping (e.g. a dictionary) or an iterable (e.g. a list or tuple).
  * **fields.E005** : `choices` must be a mapping of actual values to human readable names or an iterable containing `(actual value, human readable name)` tuples.
  * **fields.E006** : `db_index` must be `None`, `True` or `False`.
  * **fields.E007** : Primary keys must not have `null=True`.
  * **fields.E008** : All `validators` must be callable.
  * **fields.E009** : `max_length` is too small to fit the longest value in `choices` (`<count>` characters).
  * **fields.E010** : `<field>` default should be a callable instead of an instance so that it’s not shared between all field instances.
  * **fields.E011** : `<database>` does not support default database values with expressions (`db_default`).
  * **fields.E012** : `<expression>` cannot be used in `db_default`.
  * **fields.E100** : `AutoField`s must set primary_key=True.
  * **fields.E110** : `BooleanField`s do not accept null values. _This check appeared before support for null values was added in Django 2.1._
  * **fields.E120** : `CharField`s must define a `max_length` attribute.
  * **fields.E121** : `max_length` must be a positive integer.
  * **fields.W122** : `max_length` is ignored when used with `<integer field type>`.
  * **fields.E130** : `DecimalField`s must define a `decimal_places` attribute.
  * **fields.E131** : `decimal_places` must be a non-negative integer.
  * **fields.E132** : `DecimalField`s must define a `max_digits` attribute.
  * **fields.E133** : `max_digits` must be a positive integer.
  * **fields.E134** : `max_digits` must be greater or equal to `decimal_places`.
  * **fields.E140** : `FilePathField`s must have either `allow_files` or `allow_folders` set to True.
  * **fields.E150** : `GenericIPAddressField`s cannot have `blank=True` if `null=False`, as blank values are stored as nulls.
  * **fields.E160** : The options `auto_now`, `auto_now_add`, and `default` are mutually exclusive. Only one of these options may be present.
  * **fields.W161** : Fixed default value provided.
  * **fields.W162** : `<database>` does not support a database index on `<field data type>` columns.
  * **fields.W163** : `<database>` does not support comments on columns (`db_comment`).
  * **fields.E170** : `BinaryField`’s `default` cannot be a string. Use bytes content instead.
  * **fields.E180** : `<database>` does not support `JSONField`s.
  * **fields.E190** : `<database>` does not support a database collation on `<field_type>`s.
  * **fields.E220** : `<database>` does not support `GeneratedField`s.
  * **fields.E221** : `<database>` does not support non-persisted `GeneratedField`s.
  * **fields.E222** : `<database>` does not support persisted `GeneratedField`s.
  * **fields.E223** : `GeneratedField.output_field` has errors: …
  * **fields.W224** : `GeneratedField.output_field` has warnings: …
  * **fields.E900** : `IPAddressField` has been removed except for support in historical migrations.
  * **fields.W900** : `IPAddressField` has been deprecated. Support for it (except in historical migrations) will be removed in Django 1.9. _This check appeared in Django 1.7 and 1.8_.
  * **fields.W901** : `CommaSeparatedIntegerField` has been deprecated. Support for it (except in historical migrations) will be removed in Django 2.0. _This check appeared in Django 1.10 and 1.11_.
  * **fields.E901** : `CommaSeparatedIntegerField` is removed except for support in historical migrations.
  * **fields.W902** : `FloatRangeField` is deprecated and will be removed in Django 3.1. _This check appeared in Django 2.2 and 3.0_.
  * **fields.W903** : `NullBooleanField` is deprecated. Support for it (except in historical migrations) will be removed in Django 4.0. _This check appeared in Django 3.1 and 3.2_.
  * **fields.E903** : `NullBooleanField` is removed except for support in historical migrations.
  * **fields.W904** : `django.contrib.postgres.fields.JSONField` is deprecated. Support for it (except in historical migrations) will be removed in Django 4.0. _This check appeared in Django 3.1 and 3.2_.
  * **fields.E904** : `django.contrib.postgres.fields.JSONField` is removed except for support in historical migrations.
  * **fields.W905** : `django.contrib.postgres.fields.CICharField` is deprecated. Support for it (except in historical migrations) will be removed in Django 5.1.
  * **fields.W906** : `django.contrib.postgres.fields.CIEmailField` is deprecated. Support for it (except in historical migrations) will be removed in Django 5.1.
  * **fields.W907** : `django.contrib.postgres.fields.CITextField` is deprecated. Support for it (except in historical migrations) will be removed in Django 5.1.


#### File fields[¶](https://docs.djangoproject.com/en/5.0/ref/checks/#file-fields "Link to this heading")
  * **fields.E200** : `unique` is not a valid argument for a `FileField`. _This check is removed in Django 1.11_.
  * **fields.E201** : `primary_key` is not a valid argument for a `FileField`.
  * **fields.E202** : `FileField`’s `upload_to` argument must be a relative path, not an absolute path.
  * **fields.E210** : Cannot use `ImageField` because Pillow is not installed.


#### Related fields[¶](https://docs.djangoproject.com/en/5.0/ref/checks/#related-fields "Link to this heading")
  * **fields.E300** : Field defines a relation with model `<model>`, which is either not installed, or is abstract.
  * **fields.E301** : Field defines a relation with the model `<app_label>.<model>` which has been swapped out.
  * **fields.E302** : Reverse accessor `<related model>.<accessor name>` for `<app_label>.<model>.<field name>` clashes with field name `<app_label>.<model>.<field name>`.
  * **fields.E303** : Reverse query name for `<app_label>.<model>.<field name>` clashes with field name `<app_label>.<model>.<field name>`.
  * **fields.E304** : Reverse accessor `<related model>.<accessor name>` for `<app_label>.<model>.<field name>` clashes with reverse accessor for `<app_label>.<model>.<field name>`.
  * **fields.E305** : Reverse query name for `<app_label>.<model>.<field name>` clashes with reverse query name for `<app_label>.<model>.<field name>`.
  * **fields.E306** : The name `<name>` is invalid `related_name` for field `<model>.<field name>`.
  * **fields.E307** : The field `<app label>.<model>.<field name>` was declared with a lazy reference to `<app label>.<model>`, but app `<app label>` isn’t installed or doesn’t provide model `<model>`.
  * **fields.E308** : Reverse query name `<related query name>` must not end with an underscore.
  * **fields.E309** : Reverse query name `<related query name>` must not contain `'__'`.
  * **fields.E310** : No subset of the fields `<field1>`, `<field2>`, … on model `<model>` is unique.
  * **fields.E311** : `<model>.<field name>` must be unique because it is referenced by a `ForeignKey`.
  * **fields.E312** : The `to_field` `<field name>` doesn’t exist on the related model `<app label>.<model>`.
  * **fields.E320** : Field specifies `on_delete=SET_NULL`, but cannot be null.
  * **fields.E321** : The field specifies `on_delete=SET_DEFAULT`, but has no default value.
  * **fields.E330** : `ManyToManyField`s cannot be unique.
  * **fields.E331** : Field specifies a many-to-many relation through model `<model>`, which has not been installed.
  * **fields.E332** : Many-to-many fields with intermediate tables must not be symmetrical. _This check appeared before Django 3.0._
  * **fields.E333** : The model is used as an intermediate model by `<model>`, but it has more than two foreign keys to `<model>`, which is ambiguous. You must specify which two foreign keys Django should use via the `through_fields` keyword argument.
  * **fields.E334** : The model is used as an intermediate model by `<model>`, but it has more than one foreign key from `<model>`, which is ambiguous. You must specify which foreign key Django should use via the `through_fields` keyword argument.
  * **fields.E335** : The model is used as an intermediate model by `<model>`, but it has more than one foreign key to `<model>`, which is ambiguous. You must specify which foreign key Django should use via the `through_fields` keyword argument.
  * **fields.E336** : The model is used as an intermediary model by `<model>`, but it does not have foreign key to `<model>` or `<model>`.
  * **fields.E337** : Field specifies `through_fields` but does not provide the names of the two link fields that should be used for the relation through `<model>`.
  * **fields.E338** : The intermediary model `<through model>` has no field `<field name>`.
  * **fields.E339** : `<model>.<field name>` is not a foreign key to `<model>`.
  * **fields.E340** : The field’s intermediary table `<table name>` clashes with the table name of `<model>`/`<model>.<field name>`.
  * **fields.W340** : `null` has no effect on `ManyToManyField`.
  * **fields.W341** : `ManyToManyField` does not support `validators`.
  * **fields.W342** : Setting `unique=True` on a `ForeignKey` has the same effect as using a `OneToOneField`.
  * **fields.W343** : `limit_choices_to` has no effect on `ManyToManyField` with a `through` model. _This check appeared before Django 4.0._
  * **fields.W344** : The field’s intermediary table `<table name>` clashes with the table name of `<model>`/`<model>.<field name>`.
  * **fields.W345** : `related_name` has no effect on `ManyToManyField` with a symmetrical relationship, e.g. to “self”.
  * **fields.W346** : `db_comment` has no effect on `ManyToManyField`.


### Models[¶](https://docs.djangoproject.com/en/5.0/ref/checks/#models "Link to this heading")
  * **models.E001** : `<swappable>` is not of the form `app_label.app_name`.
  * **models.E002** : `<SETTING>` references `<model>`, which has not been installed, or is abstract.
  * **models.E003** : The model has two identical many-to-many relations through the intermediate model `<app_label>.<model>`.
  * **models.E004** : `id` can only be used as a field name if the field also sets `primary_key=True`.
  * **models.E005** : The field `<field name>` from parent model `<model>` clashes with the field `<field name>` from parent model `<model>`.
  * **models.E006** : The field `<field name>` clashes with the field `<field name>` from model `<model>`.
  * **models.E007** : Field `<field name>` has column name `<column name>` that is used by another field.
  * **models.E008** : `index_together` must be a list or tuple.
  * **models.E009** : All `index_together` elements must be lists or tuples.
  * **models.E010** : `unique_together` must be a list or tuple.
  * **models.E011** : All `unique_together` elements must be lists or tuples.
  * **models.E012** : `constraints/indexes/index_together/unique_together` refers to the nonexistent field `<field name>`.
  * **models.E013** : `constraints/indexes/index_together/unique_together` refers to a `ManyToManyField` `<field name>`, but `ManyToManyField`s are not supported for that option.
  * **models.E014** : `ordering` must be a tuple or list (even if you want to order by only one field).
  * **models.E015** : `ordering` refers to the nonexistent field, related field, or lookup `<field name>`.
  * **models.E016** : `constraints/indexes/index_together/unique_together` refers to field `<field_name>` which is not local to model `<model>`.
  * **models.E017** : Proxy model `<model>` contains model fields.
  * **models.E018** : Autogenerated column name too long for field `<field>`. Maximum length is `<maximum length>` for database `<alias>`.
  * **models.E019** : Autogenerated column name too long for M2M field `<M2M field>`. Maximum length is `<maximum length>` for database `<alias>`.
  * **models.E020** : The `<model>.check()` class method is currently overridden.
  * **models.E021** : `ordering` and `order_with_respect_to` cannot be used together.
  * **models.E022** : `<function>` contains a lazy reference to `<app label>.<model>`, but app `<app label>` isn’t installed or doesn’t provide model `<model>`.
  * **models.E023** : The model name `<model>` cannot start or end with an underscore as it collides with the query lookup syntax.
  * **models.E024** : The model name `<model>` cannot contain double underscores as it collides with the query lookup syntax.
  * **models.E025** : The property `<property name>` clashes with a related field accessor.
  * **models.E026** : The model cannot have more than one field with `primary_key=True`.
  * **models.W027** : `<database>` does not support check constraints.
  * **models.E028** : `db_table` `<db_table>` is used by multiple models: `<model list>`.
  * **models.E029** : index name `<index>` is not unique for model `<model>`.
  * **models.E030** : index name `<index>` is not unique among models: `<model list>`.
  * **models.E031** : constraint name `<constraint>` is not unique for model `<model>`.
  * **models.E032** : constraint name `<constraint>` is not unique among models: `<model list>`.
  * **models.E033** : The index name `<index>` cannot start with an underscore or a number.
  * **models.E034** : The index name `<index>` cannot be longer than `<max_length>` characters.
  * **models.W035** : `db_table` `<db_table>` is used by multiple models: `<model list>`.
  * **models.W036** : `<database>` does not support unique constraints with conditions.
  * **models.W037** : `<database>` does not support indexes with conditions.
  * **models.W038** : `<database>` does not support deferrable unique constraints.
  * **models.W039** : `<database>` does not support unique constraints with non-key columns.
  * **models.W040** : `<database>` does not support indexes with non-key columns.
  * **models.E041** : `constraints` refers to the joined field `<field name>`.
  * **models.W042** : Auto-created primary key used when not defining a primary key type, by default `django.db.models.AutoField`.
  * **models.W043** : `<database>` does not support indexes on expressions.
  * **models.W044** : `<database>` does not support unique constraints on expressions.
  * **models.W045** : Check constraint `<constraint>` contains `RawSQL()` expression and won’t be validated during the model `full_clean()`.
  * **models.W046** : `<database>` does not support comments on tables (`db_table_comment`).
  * **models.W047** : `<database>` does not support unique constraints with nulls distinct.


### Security[¶](https://docs.djangoproject.com/en/5.0/ref/checks/#security "Link to this heading")
The security checks do not make your site secure. They do not audit code, do intrusion detection, or do anything particularly complex. Rather, they help perform an automated, low-hanging-fruit checklist, that can help you to improve your site’s security.
Some of these checks may not be appropriate for your particular deployment configuration. For instance, if you do your HTTP to HTTPS redirection in a load balancer, it’d be irritating to be constantly warned about not having enabled [`SECURE_SSL_REDIRECT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECURE_SSL_REDIRECT). Use [`SILENCED_SYSTEM_CHECKS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SILENCED_SYSTEM_CHECKS) to silence unneeded checks.
The following checks are run if you use the [`check --deploy`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-check-deploy) option:
  * **security.W001** : You do not have [`django.middleware.security.SecurityMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.middleware.security.SecurityMiddleware "django.middleware.security.SecurityMiddleware") in your [`MIDDLEWARE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MIDDLEWARE) so the [`SECURE_HSTS_SECONDS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECURE_HSTS_SECONDS), [`SECURE_CONTENT_TYPE_NOSNIFF`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECURE_CONTENT_TYPE_NOSNIFF), [`SECURE_REFERRER_POLICY`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECURE_REFERRER_POLICY), [`SECURE_CROSS_ORIGIN_OPENER_POLICY`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECURE_CROSS_ORIGIN_OPENER_POLICY), and [`SECURE_SSL_REDIRECT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECURE_SSL_REDIRECT) settings will have no effect.
  * **security.W002** : You do not have [`django.middleware.clickjacking.XFrameOptionsMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.middleware.clickjacking.XFrameOptionsMiddleware "django.middleware.clickjacking.XFrameOptionsMiddleware") in your [`MIDDLEWARE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MIDDLEWARE), so your pages will not be served with an `'x-frame-options'` header. Unless there is a good reason for your site to be served in a frame, you should consider enabling this header to help prevent clickjacking attacks.
  * **security.W003** : You don’t appear to be using Django’s built-in cross-site request forgery protection via the middleware ([`django.middleware.csrf.CsrfViewMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.middleware.csrf.CsrfViewMiddleware "django.middleware.csrf.CsrfViewMiddleware") is not in your [`MIDDLEWARE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MIDDLEWARE)). Enabling the middleware is the safest approach to ensure you don’t leave any holes.
  * **security.W004** : You have not set a value for the [`SECURE_HSTS_SECONDS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECURE_HSTS_SECONDS) setting. If your entire site is served only over SSL, you may want to consider setting a value and enabling [HTTP Strict Transport Security](https://docs.djangoproject.com/en/5.0/ref/middleware/#http-strict-transport-security). Be sure to read the documentation first; enabling HSTS carelessly can cause serious, irreversible problems.
  * **security.W005** : You have not set the [`SECURE_HSTS_INCLUDE_SUBDOMAINS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECURE_HSTS_INCLUDE_SUBDOMAINS) setting to `True`. Without this, your site is potentially vulnerable to attack via an insecure connection to a subdomain. Only set this to `True` if you are certain that all subdomains of your domain should be served exclusively via SSL.
  * **security.W006** : Your [`SECURE_CONTENT_TYPE_NOSNIFF`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECURE_CONTENT_TYPE_NOSNIFF) setting is not set to `True`, so your pages will not be served with an `'X-Content-Type-Options: nosniff'` header. You should consider enabling this header to prevent the browser from identifying content types incorrectly.
  * **security.W007** : Your `SECURE_BROWSER_XSS_FILTER` setting is not set to `True`, so your pages will not be served with an `'X-XSS-Protection: 1; mode=block'` header. You should consider enabling this header to activate the browser’s XSS filtering and help prevent XSS attacks. _This check is removed in Django 3.0 as the_ `X-XSS-Protection` _header is no longer honored by modern browsers._
  * **security.W008** : Your [`SECURE_SSL_REDIRECT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECURE_SSL_REDIRECT) setting is not set to `True`. Unless your site should be available over both SSL and non-SSL connections, you may want to either set this setting to `True` or configure a load balancer or reverse-proxy server to redirect all connections to HTTPS.
  * **security.W009** : Your [`SECRET_KEY`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECRET_KEY) has less than 50 characters, less than 5 unique characters, or it’s prefixed with `'django-insecure-'` indicating that it was generated automatically by Django. Please generate a long and random value, otherwise many of Django’s security-critical features will be vulnerable to attack.
  * **security.W010** : You have [`django.contrib.sessions`](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#module-django.contrib.sessions "django.contrib.sessions: Provides session management for Django projects.") in your [`INSTALLED_APPS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-INSTALLED_APPS) but you have not set [`SESSION_COOKIE_SECURE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SESSION_COOKIE_SECURE) to `True`. Using a secure-only session cookie makes it more difficult for network traffic sniffers to hijack user sessions.
  * **security.W011** : You have [`django.contrib.sessions.middleware.SessionMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.contrib.sessions.middleware.SessionMiddleware "django.contrib.sessions.middleware.SessionMiddleware") in your [`MIDDLEWARE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MIDDLEWARE), but you have not set [`SESSION_COOKIE_SECURE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SESSION_COOKIE_SECURE) to `True`. Using a secure-only session cookie makes it more difficult for network traffic sniffers to hijack user sessions.
  * **security.W012** : [`SESSION_COOKIE_SECURE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SESSION_COOKIE_SECURE) is not set to `True`. Using a secure-only session cookie makes it more difficult for network traffic sniffers to hijack user sessions.
  * **security.W013** : You have [`django.contrib.sessions`](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#module-django.contrib.sessions "django.contrib.sessions: Provides session management for Django projects.") in your [`INSTALLED_APPS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-INSTALLED_APPS), but you have not set [`SESSION_COOKIE_HTTPONLY`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SESSION_COOKIE_HTTPONLY) to `True`. Using an `HttpOnly` session cookie makes it more difficult for cross-site scripting attacks to hijack user sessions.
  * **security.W014** : You have [`django.contrib.sessions.middleware.SessionMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.contrib.sessions.middleware.SessionMiddleware "django.contrib.sessions.middleware.SessionMiddleware") in your [`MIDDLEWARE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MIDDLEWARE), but you have not set [`SESSION_COOKIE_HTTPONLY`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SESSION_COOKIE_HTTPONLY) to `True`. Using an `HttpOnly` session cookie makes it more difficult for cross-site scripting attacks to hijack user sessions.
  * **security.W015** : [`SESSION_COOKIE_HTTPONLY`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SESSION_COOKIE_HTTPONLY) is not set to `True`. Using an `HttpOnly` session cookie makes it more difficult for cross-site scripting attacks to hijack user sessions.
  * **security.W016** : [`CSRF_COOKIE_SECURE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CSRF_COOKIE_SECURE) is not set to `True`. Using a secure-only CSRF cookie makes it more difficult for network traffic sniffers to steal the CSRF token.
  * **security.W017** : [`CSRF_COOKIE_HTTPONLY`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CSRF_COOKIE_HTTPONLY) is not set to `True`. Using an `HttpOnly` CSRF cookie makes it more difficult for cross-site scripting attacks to steal the CSRF token. _This check is removed in Django 1.11 as the_ [`CSRF_COOKIE_HTTPONLY`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CSRF_COOKIE_HTTPONLY) _setting offers no practical benefit._
  * **security.W018** : You should not have [`DEBUG`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DEBUG) set to `True` in deployment.
  * **security.W019** : You have [`django.middleware.clickjacking.XFrameOptionsMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.middleware.clickjacking.XFrameOptionsMiddleware "django.middleware.clickjacking.XFrameOptionsMiddleware") in your [`MIDDLEWARE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MIDDLEWARE), but [`X_FRAME_OPTIONS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-X_FRAME_OPTIONS) is not set to `'DENY'`. Unless there is a good reason for your site to serve other parts of itself in a frame, you should change it to `'DENY'`.
  * **security.W020** : [`ALLOWED_HOSTS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-ALLOWED_HOSTS) must not be empty in deployment.
  * **security.W021** : You have not set the [`SECURE_HSTS_PRELOAD`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECURE_HSTS_PRELOAD) setting to `True`. Without this, your site cannot be submitted to the browser preload list.
  * **security.W022** : You have not set the [`SECURE_REFERRER_POLICY`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECURE_REFERRER_POLICY) setting. Without this, your site will not send a Referrer-Policy header. You should consider enabling this header to protect user privacy.
  * **security.E023** : You have set the [`SECURE_REFERRER_POLICY`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECURE_REFERRER_POLICY) setting to an invalid value.
  * **security.E024** : You have set the [`SECURE_CROSS_ORIGIN_OPENER_POLICY`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECURE_CROSS_ORIGIN_OPENER_POLICY) setting to an invalid value.
  * **security.W025** : Your [`SECRET_KEY_FALLBACKS[n]`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECRET_KEY_FALLBACKS) has less than 50 characters, less than 5 unique characters, or it’s prefixed with `'django-insecure-'` indicating that it was generated automatically by Django. Please generate a long and random value, otherwise many of Django’s security-critical features will be vulnerable to attack.


The following checks verify that your security-related settings are correctly configured:
  * **security.E100** : `DEFAULT_HASHING_ALGORITHM` must be `'sha1'` or `'sha256'`. _This check appeared in Django 3.1 and 3.2_.
  * **security.E101** : The CSRF failure view `'path.to.view'` does not take the correct number of arguments.
  * **security.E102** : The CSRF failure view `'path.to.view'` could not be imported.


### Signals[¶](https://docs.djangoproject.com/en/5.0/ref/checks/#signals "Link to this heading")
  * **signals.E001** : `<handler>` was connected to the `<signal>` signal with a lazy reference to the sender `<app label>.<model>`, but app `<app label>` isn’t installed or doesn’t provide model `<model>`.


### Templates[¶](https://docs.djangoproject.com/en/5.0/ref/checks/#templates "Link to this heading")
The following checks verify that your [`TEMPLATES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TEMPLATES) setting is correctly configured:
  * **templates.E001** : You have `'APP_DIRS': True` in your [`TEMPLATES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TEMPLATES) but also specify `'loaders'` in `OPTIONS`. Either remove `APP_DIRS` or remove the `'loaders'` option.
  * **templates.E002** : `string_if_invalid` in [`TEMPLATES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TEMPLATES) [`OPTIONS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TEMPLATES-OPTIONS) must be a string but got: `{value}` (`{type}`).
  * **templates.E003** :`<name>` is used for multiple template tag modules: `<module list>`. _This check was changed to_ `templates.W003` _in Django 4.1.2_.
  * **templates.W003** :`<name>` is used for multiple template tag modules: `<module list>`.


### Translation[¶](https://docs.djangoproject.com/en/5.0/ref/checks/#translation "Link to this heading")
The following checks are performed on your translation configuration:
  * **translation.E001** : You have provided an invalid value for the [`LANGUAGE_CODE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-LANGUAGE_CODE) setting: `<value>`.
  * **translation.E002** : You have provided an invalid language code in the [`LANGUAGES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-LANGUAGES) setting: `<value>`.
  * **translation.E003** : You have provided an invalid language code in the [`LANGUAGES_BIDI`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-LANGUAGES_BIDI) setting: `<value>`.
  * **translation.E004** : You have provided a value for the [`LANGUAGE_CODE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-LANGUAGE_CODE) setting that is not in the [`LANGUAGES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-LANGUAGES) setting.


### URLs[¶](https://docs.djangoproject.com/en/5.0/ref/checks/#urls "Link to this heading")
The following checks are performed on your URL configuration:
  * **urls.W001** : Your URL pattern `<pattern>` uses [`include()`](https://docs.djangoproject.com/en/5.0/ref/urls/#django.urls.include "django.urls.include") with a `route` ending with a `$`. Remove the dollar from the `route` to avoid problems including URLs.
  * **urls.W002** : Your URL pattern `<pattern>` has a `route` beginning with a `/`. Remove this slash as it is unnecessary. If this pattern is targeted in an [`include()`](https://docs.djangoproject.com/en/5.0/ref/urls/#django.urls.include "django.urls.include"), ensure the [`include()`](https://docs.djangoproject.com/en/5.0/ref/urls/#django.urls.include "django.urls.include") pattern has a trailing `/`.
  * **urls.W003** : Your URL pattern `<pattern>` has a `name` including a `:`. Remove the colon, to avoid ambiguous namespace references.
  * **urls.E004** : Your URL pattern `<pattern>` is invalid. Ensure that `urlpatterns` is a list of [`path()`](https://docs.djangoproject.com/en/5.0/ref/urls/#django.urls.path "django.urls.path") and/or [`re_path()`](https://docs.djangoproject.com/en/5.0/ref/urls/#django.urls.re_path "django.urls.re_path") instances.
  * **urls.W005** : URL namespace `<namespace>` isn’t unique. You may not be able to reverse all URLs in this namespace.
  * **urls.E006** : The [`MEDIA_URL`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MEDIA_URL)/ [`STATIC_URL`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STATIC_URL) setting must end with a slash.
  * **urls.E007** : The custom `handlerXXX` view `'path.to.view'` does not take the correct number of arguments (…).
  * **urls.E008** : The custom `handlerXXX` view `'path.to.view'` could not be imported.
  * **urls.E009** : Your URL pattern `<pattern>` has an invalid view, pass `<view>.as_view()` instead of `<view>`.
  * **urls.W010** : Your URL pattern `<pattern>` has an unmatched `<angle bracket>`.
