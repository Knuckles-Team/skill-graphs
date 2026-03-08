## Setting test cookies[¶](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#setting-test-cookies "Link to this heading")
As a convenience, Django provides a way to test whether the user’s browser accepts cookies. Call the [`set_test_cookie()`](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#django.contrib.sessions.backends.base.SessionBase.set_test_cookie "django.contrib.sessions.backends.base.SessionBase.set_test_cookie") method of `request.session` in a view, and call [`test_cookie_worked()`](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#django.contrib.sessions.backends.base.SessionBase.test_cookie_worked "django.contrib.sessions.backends.base.SessionBase.test_cookie_worked") in a subsequent view – not in the same view call.
This awkward split between `set_test_cookie()` and `test_cookie_worked()` is necessary due to the way cookies work. When you set a cookie, you can’t actually tell whether a browser accepted it until the browser’s next request.
It’s good practice to use [`delete_test_cookie()`](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#django.contrib.sessions.backends.base.SessionBase.delete_test_cookie "django.contrib.sessions.backends.base.SessionBase.delete_test_cookie") to clean up after yourself. Do this after you’ve verified that the test cookie worked.
Here’s a typical usage example:
```
from django.http import HttpResponse
from django.shortcuts import render


def login(request):
    if request.method == "POST":
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
            return HttpResponse("You're logged in.")
        else:
            return HttpResponse("Please enable cookies and try again.")
    request.session.set_test_cookie()
    return render(request, "foo/login_form.html")

```
