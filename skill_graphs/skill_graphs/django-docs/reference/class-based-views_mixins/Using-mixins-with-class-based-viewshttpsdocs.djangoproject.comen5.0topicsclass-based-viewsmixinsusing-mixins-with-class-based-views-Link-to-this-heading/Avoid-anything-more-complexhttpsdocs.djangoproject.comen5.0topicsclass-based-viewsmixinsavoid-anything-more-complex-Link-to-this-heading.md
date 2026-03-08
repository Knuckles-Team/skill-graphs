## Avoid anything more complex[¶](https://docs.djangoproject.com/en/5.0/topics/class-based-views/mixins/#avoid-anything-more-complex "Link to this heading")
Generally you can use [`TemplateResponseMixin`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin "django.views.generic.base.TemplateResponseMixin") and [`SingleObjectMixin`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin "django.views.generic.detail.SingleObjectMixin") when you need their functionality. As shown above, with a bit of care you can even combine `SingleObjectMixin` with [`ListView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/generic-display/#django.views.generic.list.ListView "django.views.generic.list.ListView"). However things get increasingly complex as you try to do so, and a good rule of thumb is:
Hint
Each of your views should use only mixins or views from one of the groups of generic class-based views: [detail, list](https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-display/), [editing](https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-editing/) and date. For example it’s fine to combine [`TemplateView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/flattened-index/#TemplateView "TemplateView") (built in view) with [`MultipleObjectMixin`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin "django.views.generic.list.MultipleObjectMixin") (generic list), but you’re likely to have problems combining `SingleObjectMixin` (generic detail) with `MultipleObjectMixin` (generic list).
To show what happens when you try to get more sophisticated, we show an example that sacrifices readability and maintainability when there is a simpler solution. First, let’s look at a naive attempt to combine [`DetailView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/generic-display/#django.views.generic.detail.DetailView "django.views.generic.detail.DetailView") with [`FormMixin`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.FormMixin "django.views.generic.edit.FormMixin") to enable us to `POST` a Django [`Form`](https://docs.djangoproject.com/en/5.0/ref/forms/api/#django.forms.Form "django.forms.Form") to the same URL as we’re displaying an object using [`DetailView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/flattened-index/#DetailView "DetailView").
### Using `FormMixin` with `DetailView`[¶](https://docs.djangoproject.com/en/5.0/topics/class-based-views/mixins/#using-formmixin-with-detailview "Link to this heading")
Think back to our earlier example of using [`View`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/flattened-index/#View "View") and [`SingleObjectMixin`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin "django.views.generic.detail.SingleObjectMixin") together. We were recording a user’s interest in a particular author; say now that we want to let them leave a message saying why they like them. Again, let’s assume we’re not going to store this in a relational database but instead in something more esoteric that we won’t worry about here.
At this point it’s natural to reach for a [`Form`](https://docs.djangoproject.com/en/5.0/ref/forms/api/#django.forms.Form "django.forms.Form") to encapsulate the information sent from the user’s browser to Django. Say also that we’re heavily invested in `AuthorDetailView` to do that.
We’ll keep the `GET` handling from [`DetailView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/flattened-index/#DetailView "DetailView"), although we’ll have to add a [`Form`](https://docs.djangoproject.com/en/5.0/ref/forms/api/#django.forms.Form "django.forms.Form") into the context data so we can render it in the template. We’ll also want to pull in form processing from [`FormMixin`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.FormMixin "django.views.generic.edit.FormMixin"), and write a bit of code so that on `POST` the form gets called appropriately.
Note
We use [`FormMixin`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.FormMixin "django.views.generic.edit.FormMixin") and implement `post()` ourselves rather than try to mix [`DetailView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/flattened-index/#DetailView "DetailView") with [`FormView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/flattened-index/#FormView "FormView") (which provides a suitable `post()` already) because both of the views implement `get()`, and things would get much more confusing.
Our new `AuthorDetailView` looks like this:
```
# CAUTION: you almost certainly do not want to do this.
# It is provided as part of a discussion of problems you can
# run into when combining different generic class-based view
# functionality that is not designed to be used together.

from django import forms
from django.http import HttpResponseForbidden
from django.urls import reverse
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin
from books.models import Author


class AuthorInterestForm(forms.Form):
    message = forms.CharField()


class AuthorDetailView(FormMixin, DetailView):
    model = Author
    form_class = AuthorInterestForm

    def get_success_url(self):
        return reverse("author-detail", kwargs={"pk": self.object.pk})

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        # Here, we would record the user's interest using the message
        # passed in form.cleaned_data['message']
        return super().form_valid(form)

```

`get_success_url()` provides somewhere to redirect to, which gets used in the default implementation of `form_valid()`. We have to provide our own `post()` as noted earlier.
### A better solution[¶](https://docs.djangoproject.com/en/5.0/topics/class-based-views/mixins/#a-better-solution "Link to this heading")
The number of subtle interactions between [`FormMixin`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.FormMixin "django.views.generic.edit.FormMixin") and [`DetailView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/flattened-index/#DetailView "DetailView") is already testing our ability to manage things. It’s unlikely you’d want to write this kind of class yourself.
In this case, you could write the `post()` method yourself, keeping [`DetailView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/flattened-index/#DetailView "DetailView") as the only generic functionality, although writing [`Form`](https://docs.djangoproject.com/en/5.0/ref/forms/api/#django.forms.Form "django.forms.Form") handling code involves a lot of duplication.
Alternatively, it would still be less work than the above approach to have a separate view for processing the form, which could use [`FormView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/generic-editing/#django.views.generic.edit.FormView "django.views.generic.edit.FormView") distinct from [`DetailView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/flattened-index/#DetailView "DetailView") without concerns.
### An alternative better solution[¶](https://docs.djangoproject.com/en/5.0/topics/class-based-views/mixins/#an-alternative-better-solution "Link to this heading")
What we’re really trying to do here is to use two different class based views from the same URL. So why not do just that? We have a very clear division here: `GET` requests should get the [`DetailView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/flattened-index/#DetailView "DetailView") (with the [`Form`](https://docs.djangoproject.com/en/5.0/ref/forms/api/#django.forms.Form "django.forms.Form") added to the context data), and `POST` requests should get the [`FormView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/flattened-index/#FormView "FormView"). Let’s set up those views first.
The `AuthorDetailView` view is almost the same as [when we first introduced AuthorDetailView](https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-display/#generic-views-extra-work); we have to write our own `get_context_data()` to make the `AuthorInterestForm` available to the template. We’ll skip the `get_object()` override from before for clarity:
```
from django import forms
from django.views.generic import DetailView
from books.models import Author


class AuthorInterestForm(forms.Form):
    message = forms.CharField()


class AuthorDetailView(DetailView):
    model = Author

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = AuthorInterestForm()
        return context

```

Then the `AuthorInterestFormView` is a [`FormView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/flattened-index/#FormView "FormView"), but we have to bring in [`SingleObjectMixin`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin "django.views.generic.detail.SingleObjectMixin") so we can find the author we’re talking about, and we have to remember to set `template_name` to ensure that form errors will render the same template as `AuthorDetailView` is using on `GET`:
```
from django.http import HttpResponseForbidden
from django.urls import reverse
from django.views.generic import FormView
from django.views.generic.detail import SingleObjectMixin


class AuthorInterestFormView(SingleObjectMixin, FormView):
    template_name = "books/author_detail.html"
    form_class = AuthorInterestForm
    model = Author

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("author-detail", kwargs={"pk": self.object.pk})

```

Finally we bring this together in a new `AuthorView` view. We already know that calling [`as_view()`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/#django.views.generic.base.View.as_view "django.views.generic.base.View.as_view") on a class-based view gives us something that behaves exactly like a function based view, so we can do that at the point we choose between the two subviews.
You can pass through keyword arguments to [`as_view()`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/#django.views.generic.base.View.as_view "django.views.generic.base.View.as_view") in the same way you would in your URLconf, such as if you wanted the `AuthorInterestFormView` behavior to also appear at another URL but using a different template:
```
from django.views import View


class AuthorView(View):
    def get(self, request, *args, **kwargs):
        view = AuthorDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = AuthorInterestFormView.as_view()
        return view(request, *args, **kwargs)

```

This approach can also be used with any other generic class-based views or your own class-based views inheriting directly from [`View`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/flattened-index/#View "View") or [`TemplateView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/flattened-index/#TemplateView "TemplateView"), as it keeps the different views as separate as possible.
