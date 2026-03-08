##  [Auth](https://docs.djangoproject.com/en/5.0/ref/settings/#id13)[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#auth "Link to this heading")
Settings for [`django.contrib.auth`](https://docs.djangoproject.com/en/5.0/topics/auth/#module-django.contrib.auth "django.contrib.auth: Django's authentication framework.").
###  `AUTHENTICATION_BACKENDS`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#authentication-backends "Link to this heading")
Default: `['django.contrib.auth.backends.ModelBackend']`
A list of authentication backend classes (as strings) to use when attempting to authenticate a user. See the [authentication backends documentation](https://docs.djangoproject.com/en/5.0/topics/auth/customizing/#authentication-backends) for details.
###  `AUTH_USER_MODEL`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#auth-user-model "Link to this heading")
Default: `'auth.User'`
The model to use to represent a User. See [Substituting a custom User model](https://docs.djangoproject.com/en/5.0/topics/auth/customizing/#auth-custom-user).
Warning
You cannot change the AUTH_USER_MODEL setting during the lifetime of a project (i.e. once you have made and migrated models that depend on it) without serious effort. It is intended to be set at the project start, and the model it refers to must be available in the first migration of the app that it lives in. See [Substituting a custom User model](https://docs.djangoproject.com/en/5.0/topics/auth/customizing/#auth-custom-user) for more details.
###  `LOGIN_REDIRECT_URL`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#login-redirect-url "Link to this heading")
Default: `'/accounts/profile/'`
The URL or [named URL pattern](https://docs.djangoproject.com/en/5.0/topics/http/urls/#naming-url-patterns) where requests are redirected after login when the [`LoginView`](https://docs.djangoproject.com/en/5.0/topics/auth/default/#django.contrib.auth.views.LoginView "django.contrib.auth.views.LoginView") doesn’t get a `next` GET parameter.
###  `LOGIN_URL`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#login-url "Link to this heading")
Default: `'/accounts/login/'`
The URL or [named URL pattern](https://docs.djangoproject.com/en/5.0/topics/http/urls/#naming-url-patterns) where requests are redirected for login when using the [`login_required()`](https://docs.djangoproject.com/en/5.0/topics/auth/default/#django.contrib.auth.decorators.login_required "django.contrib.auth.decorators.login_required") decorator, [`LoginRequiredMixin`](https://docs.djangoproject.com/en/5.0/topics/auth/default/#django.contrib.auth.mixins.LoginRequiredMixin "django.contrib.auth.mixins.LoginRequiredMixin"), or [`AccessMixin`](https://docs.djangoproject.com/en/5.0/topics/auth/default/#django.contrib.auth.mixins.AccessMixin "django.contrib.auth.mixins.AccessMixin").
###  `LOGOUT_REDIRECT_URL`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#logout-redirect-url "Link to this heading")
Default: `None`
The URL or [named URL pattern](https://docs.djangoproject.com/en/5.0/topics/http/urls/#naming-url-patterns) where requests are redirected after logout if [`LogoutView`](https://docs.djangoproject.com/en/5.0/topics/auth/default/#django.contrib.auth.views.LogoutView "django.contrib.auth.views.LogoutView") doesn’t have a `next_page` attribute.
If `None`, no redirect will be performed and the logout view will be rendered.
###  `PASSWORD_RESET_TIMEOUT`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#password-reset-timeout "Link to this heading")
Default: `259200` (3 days, in seconds)
The number of seconds a password reset link is valid for.
Used by the [`PasswordResetConfirmView`](https://docs.djangoproject.com/en/5.0/topics/auth/default/#django.contrib.auth.views.PasswordResetConfirmView "django.contrib.auth.views.PasswordResetConfirmView").
Note
Reducing the value of this timeout doesn’t make any difference to the ability of an attacker to brute-force a password reset token. Tokens are designed to be safe from brute-forcing without any timeout.
This timeout exists to protect against some unlikely attack scenarios, such as someone gaining access to email archives that may contain old, unused password reset tokens.
###  `PASSWORD_HASHERS`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#password-hashers "Link to this heading")
See [How Django stores passwords](https://docs.djangoproject.com/en/5.0/topics/auth/passwords/#auth-password-storage).
Default:
```
[
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.ScryptPasswordHasher",
]

```

###  `AUTH_PASSWORD_VALIDATORS`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators "Link to this heading")
Default: `[]` (Empty list)
The list of validators that are used to check the strength of user’s passwords. See [Password validation](https://docs.djangoproject.com/en/5.0/topics/auth/passwords/#password-validation) for more details. By default, no validation is performed and all passwords are accepted.
