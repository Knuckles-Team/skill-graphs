This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/ref/exceptions/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/ref/exceptions/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/ref/exceptions/)
  * [pl](https://docs.djangoproject.com/pl/5.0/ref/exceptions/)
  * [ko](https://docs.djangoproject.com/ko/5.0/ref/exceptions/)
  * [ja](https://docs.djangoproject.com/ja/5.0/ref/exceptions/)
  * [it](https://docs.djangoproject.com/it/5.0/ref/exceptions/)
  * [id](https://docs.djangoproject.com/id/5.0/ref/exceptions/)
  * [fr](https://docs.djangoproject.com/fr/5.0/ref/exceptions/)
  * [es](https://docs.djangoproject.com/es/5.0/ref/exceptions/)
  * [el](https://docs.djangoproject.com/el/5.0/ref/exceptions/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/ref/exceptions/)
  * [6.0](https://docs.djangoproject.com/en/6.0/ref/exceptions/)
  * [5.2](https://docs.djangoproject.com/en/5.2/ref/exceptions/)
  * [5.1](https://docs.djangoproject.com/en/5.1/ref/exceptions/)
  * [4.2](https://docs.djangoproject.com/en/4.2/ref/exceptions/)
  * [4.1](https://docs.djangoproject.com/en/4.1/ref/exceptions/)
  * [4.0](https://docs.djangoproject.com/en/4.0/ref/exceptions/)
  * [3.2](https://docs.djangoproject.com/en/3.2/ref/exceptions/)
  * [3.1](https://docs.djangoproject.com/en/3.1/ref/exceptions/)
  * [3.0](https://docs.djangoproject.com/en/3.0/ref/exceptions/)
  * [2.2](https://docs.djangoproject.com/en/2.2/ref/exceptions/)
  * [2.1](https://docs.djangoproject.com/en/2.1/ref/exceptions/)
  * [2.0](https://docs.djangoproject.com/en/2.0/ref/exceptions/)
  * [1.11](https://docs.djangoproject.com/en/1.11/ref/exceptions/)
  * [1.10](https://docs.djangoproject.com/en/1.10/ref/exceptions/)
  * [1.8](https://docs.djangoproject.com/en/1.8/ref/exceptions/)


  * [](https://docs.djangoproject.com/en/5.0/ref/exceptions/#top)


# Django Exceptions[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django-exceptions "Link to this heading")
Django raises some of its own exceptions as well as standard Python exceptions.
## Django Core Exceptions[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#module-django.core.exceptions "Link to this heading")
Django core exception classes are defined in `django.core.exceptions`.
###  `AppRegistryNotReady`[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#appregistrynotready "Link to this heading")

_exception_ AppRegistryNotReady[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/exceptions/#AppRegistryNotReady)[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.AppRegistryNotReady "Link to this definition")

This exception is raised when attempting to use models before the [app loading process](https://docs.djangoproject.com/en/5.0/ref/applications/#app-loading-process), which initializes the ORM, is complete.
###  `ObjectDoesNotExist`[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#objectdoesnotexist "Link to this heading")

_exception_ ObjectDoesNotExist[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/exceptions/#ObjectDoesNotExist)[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.ObjectDoesNotExist "Link to this definition")

The base class for [`Model.DoesNotExist`](https://docs.djangoproject.com/en/5.0/ref/models/class/#django.db.models.Model.DoesNotExist "django.db.models.Model.DoesNotExist") exceptions. A `try/except` for `ObjectDoesNotExist` will catch [`DoesNotExist`](https://docs.djangoproject.com/en/5.0/ref/models/class/#django.db.models.Model.DoesNotExist "django.db.models.Model.DoesNotExist") exceptions for all models.
See [`get()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.get "django.db.models.query.QuerySet.get").
###  `EmptyResultSet`[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#emptyresultset "Link to this heading")

_exception_ EmptyResultSet[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/exceptions/#EmptyResultSet)[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.EmptyResultSet "Link to this definition")

`EmptyResultSet` may be raised during query generation if a query won’t return any results. Most Django projects won’t encounter this exception, but it might be useful for implementing custom lookups and expressions.
###  `FullResultSet`[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#fullresultset "Link to this heading")

_exception_ FullResultSet[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/exceptions/#FullResultSet)[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.FullResultSet "Link to this definition")

New in Django 4.2:
`FullResultSet` may be raised during query generation if a query will match everything. Most Django projects won’t encounter this exception, but it might be useful for implementing custom lookups and expressions.
###  `FieldDoesNotExist`[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#fielddoesnotexist "Link to this heading")

_exception_ FieldDoesNotExist[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/exceptions/#FieldDoesNotExist)[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.FieldDoesNotExist "Link to this definition")

The `FieldDoesNotExist` exception is raised by a model’s `_meta.get_field()` method when the requested field does not exist on the model or on the model’s parents.
###  `MultipleObjectsReturned`[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#multipleobjectsreturned "Link to this heading")

_exception_ MultipleObjectsReturned[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/exceptions/#MultipleObjectsReturned)[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.MultipleObjectsReturned "Link to this definition")

The base class for [`Model.MultipleObjectsReturned`](https://docs.djangoproject.com/en/5.0/ref/models/class/#django.db.models.Model.MultipleObjectsReturned "django.db.models.Model.MultipleObjectsReturned") exceptions. A `try/except` for `MultipleObjectsReturned` will catch [`MultipleObjectsReturned`](https://docs.djangoproject.com/en/5.0/ref/models/class/#django.db.models.Model.MultipleObjectsReturned "django.db.models.Model.MultipleObjectsReturned") exceptions for all models.
See [`get()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.get "django.db.models.query.QuerySet.get").
###  `SuspiciousOperation`[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#suspiciousoperation "Link to this heading")

_exception_ SuspiciousOperation[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/exceptions/#SuspiciousOperation)[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.SuspiciousOperation "Link to this definition")

The [`SuspiciousOperation`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.SuspiciousOperation "django.core.exceptions.SuspiciousOperation") exception is raised when a user has performed an operation that should be considered suspicious from a security perspective, such as tampering with a session cookie. Subclasses of `SuspiciousOperation` include:
  * `DisallowedHost`
  * `DisallowedModelAdminLookup`
  * `DisallowedModelAdminToField`
  * `DisallowedRedirect`
  * `InvalidSessionKey`
  * `RequestDataTooBig`
  * `SuspiciousFileOperation`
  * `SuspiciousMultipartForm`
  * `SuspiciousSession`
  * `TooManyFieldsSent`
  * `TooManyFilesSent`


If a `SuspiciousOperation` exception reaches the ASGI/WSGI handler level it is logged at the `Error` level and results in a [`HttpResponseBadRequest`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponseBadRequest "django.http.HttpResponseBadRequest"). See the [logging documentation](https://docs.djangoproject.com/en/5.0/topics/logging/) for more information.
Changed in Django 3.2.18:
`SuspiciousOperation` is raised when too many files are submitted.
###  `PermissionDenied`[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#permissiondenied "Link to this heading")

_exception_ PermissionDenied[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/exceptions/#PermissionDenied)[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.PermissionDenied "Link to this definition")

The [`PermissionDenied`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.PermissionDenied "django.core.exceptions.PermissionDenied") exception is raised when a user does not have permission to perform the action requested.
###  `ViewDoesNotExist`[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#viewdoesnotexist "Link to this heading")

_exception_ ViewDoesNotExist[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/exceptions/#ViewDoesNotExist)[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.ViewDoesNotExist "Link to this definition")

The [`ViewDoesNotExist`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.ViewDoesNotExist "django.core.exceptions.ViewDoesNotExist") exception is raised by [`django.urls`](https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#module-django.urls "django.urls") when a requested view does not exist.
###  `MiddlewareNotUsed`[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#middlewarenotused "Link to this heading")

_exception_ MiddlewareNotUsed[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/exceptions/#MiddlewareNotUsed)[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.MiddlewareNotUsed "Link to this definition")

The [`MiddlewareNotUsed`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.MiddlewareNotUsed "django.core.exceptions.MiddlewareNotUsed") exception is raised when a middleware is not used in the server configuration.
###  `ImproperlyConfigured`[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#improperlyconfigured "Link to this heading")

_exception_ ImproperlyConfigured[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/exceptions/#ImproperlyConfigured)[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.ImproperlyConfigured "Link to this definition")

The [`ImproperlyConfigured`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.ImproperlyConfigured "django.core.exceptions.ImproperlyConfigured") exception is raised when Django is somehow improperly configured – for example, if a value in `settings.py` is incorrect or unparseable.
###  `FieldError`[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#fielderror "Link to this heading")

_exception_ FieldError[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/exceptions/#FieldError)[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.FieldError "Link to this definition")

The [`FieldError`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.FieldError "django.core.exceptions.FieldError") exception is raised when there is a problem with a model field. This can happen for several reasons:
  * A field in a model clashes with a field of the same name from an abstract base class
  * An infinite loop is caused by ordering
  * A keyword cannot be parsed from the filter parameters
  * A field cannot be determined from a keyword in the query parameters
  * A join is not permitted on the specified field
  * A field name is invalid
  * A query contains invalid order_by arguments


###  `ValidationError`[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#validationerror "Link to this heading")

_exception_ ValidationError[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/exceptions/#ValidationError)[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.ValidationError "Link to this definition")

The [`ValidationError`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.ValidationError "django.core.exceptions.ValidationError") exception is raised when data fails form or model field validation. For more information about validation, see [Form and Field Validation](https://docs.djangoproject.com/en/5.0/ref/forms/validation/), [Model Field Validation](https://docs.djangoproject.com/en/5.0/ref/models/instances/#validating-objects) and the [Validator Reference](https://docs.djangoproject.com/en/5.0/ref/validators/).
####  `NON_FIELD_ERRORS`[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#non-field-errors "Link to this heading")

NON_FIELD_ERRORS[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.NON_FIELD_ERRORS "Link to this definition")

`ValidationError`s that don’t belong to a particular field in a form or model are classified as `NON_FIELD_ERRORS`. This constant is used as a key in dictionaries that otherwise map fields to their respective list of errors.
###  `BadRequest`[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#badrequest "Link to this heading")

_exception_ BadRequest[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/exceptions/#BadRequest)[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.BadRequest "Link to this definition")

The [`BadRequest`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.BadRequest "django.core.exceptions.BadRequest") exception is raised when the request cannot be processed due to a client error. If a `BadRequest` exception reaches the ASGI/WSGI handler level it results in a [`HttpResponseBadRequest`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponseBadRequest "django.http.HttpResponseBadRequest").
###  `RequestAborted`[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#requestaborted "Link to this heading")

_exception_ RequestAborted[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/exceptions/#RequestAborted)[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.RequestAborted "Link to this definition")

The [`RequestAborted`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.RequestAborted "django.core.exceptions.RequestAborted") exception is raised when an HTTP body being read in by the handler is cut off midstream and the client connection closes, or when the client does not send data and hits a timeout where the server closes the connection.
It is internal to the HTTP handler modules and you are unlikely to see it elsewhere. If you are modifying HTTP handling code, you should raise this when you encounter an aborted request to make sure the socket is closed cleanly.
###  `SynchronousOnlyOperation`[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#synchronousonlyoperation "Link to this heading")

_exception_ SynchronousOnlyOperation[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/exceptions/#SynchronousOnlyOperation)[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.SynchronousOnlyOperation "Link to this definition")

The [`SynchronousOnlyOperation`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.SynchronousOnlyOperation "django.core.exceptions.SynchronousOnlyOperation") exception is raised when code that is only allowed in synchronous Python code is called from an asynchronous context (a thread with a running asynchronous event loop). These parts of Django are generally heavily reliant on thread-safety to function and don’t work correctly under coroutines sharing the same thread.
If you are trying to call code that is synchronous-only from an asynchronous thread, then create a synchronous thread and call it in that. You can accomplish this is with [`asgiref.sync.sync_to_async()`](https://docs.djangoproject.com/en/5.0/topics/async/#asgiref.sync.sync_to_async "asgiref.sync.sync_to_async").
## URL Resolver exceptions[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#url-resolver-exceptions "Link to this heading")
URL Resolver exceptions are defined in `django.urls`.
###  `Resolver404`[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#resolver404 "Link to this heading")

_exception_ Resolver404[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/urls/exceptions/#Resolver404)[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.urls.Resolver404 "Link to this definition")

The [`Resolver404`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.urls.Resolver404 "django.urls.Resolver404") exception is raised by [`resolve()`](https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#django.urls.resolve "django.urls.resolve") if the path passed to `resolve()` doesn’t map to a view. It’s a subclass of [`django.http.Http404`](https://docs.djangoproject.com/en/5.0/topics/http/views/#django.http.Http404 "django.http.Http404").
###  `NoReverseMatch`[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#noreversematch "Link to this heading")

_exception_ NoReverseMatch[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/urls/exceptions/#NoReverseMatch)[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.urls.NoReverseMatch "Link to this definition")

The [`NoReverseMatch`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.urls.NoReverseMatch "django.urls.NoReverseMatch") exception is raised by [`django.urls`](https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#module-django.urls "django.urls") when a matching URL in your URLconf cannot be identified based on the parameters supplied.
## Database Exceptions[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#database-exceptions "Link to this heading")
Database exceptions may be imported from `django.db`.
Django wraps the standard database exceptions so that your Django code has a guaranteed common implementation of these classes.

_exception_ Error[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/utils/#Error)[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.db.Error "Link to this definition")


_exception_ InterfaceError[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/utils/#InterfaceError)[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.db.InterfaceError "Link to this definition")


_exception_ DatabaseError[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/utils/#DatabaseError)[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.db.DatabaseError "Link to this definition")


_exception_ DataError[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/utils/#DataError)[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.db.DataError "Link to this definition")


_exception_ OperationalError[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/utils/#OperationalError)[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.db.OperationalError "Link to this definition")


_exception_ IntegrityError[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/utils/#IntegrityError)[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.db.IntegrityError "Link to this definition")


_exception_ InternalError[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/utils/#InternalError)[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.db.InternalError "Link to this definition")


_exception_ ProgrammingError[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/utils/#ProgrammingError)[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.db.ProgrammingError "Link to this definition")


_exception_ NotSupportedError[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/utils/#NotSupportedError)[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.db.NotSupportedError "Link to this definition")

The Django wrappers for database exceptions behave exactly the same as the underlying database exceptions. See
As per `__cause__` attribute is set with the original (underlying) database exception, allowing access to any additional information provided.

_exception_ models.ProtectedError[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.db.models.ProtectedError "Link to this definition")

Raised to prevent deletion of referenced objects when using [`django.db.models.PROTECT`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.PROTECT "django.db.models.PROTECT"). [`models.ProtectedError`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.db.models.ProtectedError "django.db.models.ProtectedError") is a subclass of [`IntegrityError`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.db.IntegrityError "django.db.IntegrityError").

_exception_ models.RestrictedError[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.db.models.RestrictedError "Link to this definition")

Raised to prevent deletion of referenced objects when using [`django.db.models.RESTRICT`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.RESTRICT "django.db.models.RESTRICT"). [`models.RestrictedError`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.db.models.RestrictedError "django.db.models.RestrictedError") is a subclass of [`IntegrityError`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.db.IntegrityError "django.db.IntegrityError").
## HTTP Exceptions[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#http-exceptions "Link to this heading")
HTTP exceptions may be imported from `django.http`.
###  `UnreadablePostError`[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#unreadableposterror "Link to this heading")

_exception_ UnreadablePostError[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/http/request/#UnreadablePostError)[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.http.UnreadablePostError "Link to this definition")

[`UnreadablePostError`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.http.UnreadablePostError "django.http.UnreadablePostError") is raised when a user cancels an upload.
## Sessions Exceptions[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#sessions-exceptions "Link to this heading")
Sessions exceptions are defined in `django.contrib.sessions.exceptions`.
###  `SessionInterrupted`[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#sessioninterrupted "Link to this heading")

_exception_ SessionInterrupted[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/contrib/sessions/exceptions/#SessionInterrupted)[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.contrib.sessions.exceptions.SessionInterrupted "Link to this definition")

[`SessionInterrupted`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.contrib.sessions.exceptions.SessionInterrupted "django.contrib.sessions.exceptions.SessionInterrupted") is raised when a session is destroyed in a concurrent request. It’s a subclass of [`BadRequest`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.BadRequest "django.core.exceptions.BadRequest").
## Transaction Exceptions[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#transaction-exceptions "Link to this heading")
Transaction exceptions are defined in `django.db.transaction`.
###  `TransactionManagementError`[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#transactionmanagementerror "Link to this heading")

_exception_ TransactionManagementError[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/transaction/#TransactionManagementError)[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.db.transaction.TransactionManagementError "Link to this definition")

[`TransactionManagementError`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.db.transaction.TransactionManagementError "django.db.transaction.TransactionManagementError") is raised for any and all problems related to database transactions.
## Testing Framework Exceptions[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#testing-framework-exceptions "Link to this heading")
Exceptions provided by the `django.test` package.
###  `RedirectCycleError`[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#redirectcycleerror "Link to this heading")

_exception_ client.RedirectCycleError[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.test.client.RedirectCycleError "Link to this definition")

[`RedirectCycleError`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.test.client.RedirectCycleError "django.test.client.RedirectCycleError") is raised when the test client detects a loop or an overly long chain of redirects.
## Python Exceptions[¶](https://docs.djangoproject.com/en/5.0/ref/exceptions/#python-exceptions "Link to this heading")
Django raises built-in Python exceptions when appropriate as well. See the Python documentation for further information on the
Previous page and next page
[`django-admin` and `manage.py`](https://docs.djangoproject.com/en/5.0/ref/django-admin/)
[File handling ](https://docs.djangoproject.com/en/5.0/ref/files/)
[](https://docs.djangoproject.com/en/5.0/ref/exceptions/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ @ReajulHasanRaju donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [Django Exceptions](https://docs.djangoproject.com/en/5.0/ref/exceptions/)
    * [Django Core Exceptions](https://docs.djangoproject.com/en/5.0/ref/exceptions/#module-django.core.exceptions)
      * [`AppRegistryNotReady`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#appregistrynotready)
      * [`ObjectDoesNotExist`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#objectdoesnotexist)
      * [`EmptyResultSet`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#emptyresultset)
      * [`FullResultSet`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#fullresultset)
      * [`FieldDoesNotExist`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#fielddoesnotexist)
      * [`MultipleObjectsReturned`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#multipleobjectsreturned)
      * [`SuspiciousOperation`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#suspiciousoperation)
      * [`PermissionDenied`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#permissiondenied)
      * [`ViewDoesNotExist`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#viewdoesnotexist)
      * [`MiddlewareNotUsed`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#middlewarenotused)
      * [`ImproperlyConfigured`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#improperlyconfigured)
      * [`FieldError`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#fielderror)
      * [`ValidationError`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#validationerror)
        * [`NON_FIELD_ERRORS`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#non-field-errors)
      * [`BadRequest`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#badrequest)
      * [`RequestAborted`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#requestaborted)
      * [`SynchronousOnlyOperation`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#synchronousonlyoperation)
    * [URL Resolver exceptions](https://docs.djangoproject.com/en/5.0/ref/exceptions/#url-resolver-exceptions)
      * [`Resolver404`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#resolver404)
      * [`NoReverseMatch`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#noreversematch)
    * [Database Exceptions](https://docs.djangoproject.com/en/5.0/ref/exceptions/#database-exceptions)
    * [HTTP Exceptions](https://docs.djangoproject.com/en/5.0/ref/exceptions/#http-exceptions)
      * [`UnreadablePostError`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#unreadableposterror)
    * [Sessions Exceptions](https://docs.djangoproject.com/en/5.0/ref/exceptions/#sessions-exceptions)
      * [`SessionInterrupted`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#sessioninterrupted)
    * [Transaction Exceptions](https://docs.djangoproject.com/en/5.0/ref/exceptions/#transaction-exceptions)
      * [`TransactionManagementError`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#transactionmanagementerror)
    * [Testing Framework Exceptions](https://docs.djangoproject.com/en/5.0/ref/exceptions/#testing-framework-exceptions)
      * [`RedirectCycleError`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#redirectcycleerror)
    * [Python Exceptions](https://docs.djangoproject.com/en/5.0/ref/exceptions/#python-exceptions)


### Browse
  * Prev: [`django-admin` and `manage.py`](https://docs.djangoproject.com/en/5.0/ref/django-admin/)
  * Next: [File handling](https://docs.djangoproject.com/en/5.0/ref/files/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [API Reference](https://docs.djangoproject.com/en/5.0/ref/)
      * Django Exceptions


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
