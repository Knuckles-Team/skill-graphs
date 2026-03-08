## More than just HTML[¶](https://docs.djangoproject.com/en/5.0/topics/class-based-views/mixins/#more-than-just-html "Link to this heading")
Where class-based views shine is when you want to do the same thing many times. Suppose you’re writing an API, and every view should return JSON instead of rendered HTML.
We can create a mixin class to use in all of our views, handling the conversion to JSON once.
For example, a JSON mixin might look something like this:
```
from django.http import JsonResponse


class JSONResponseMixin:
    """
    A mixin that can be used to render a JSON response.
    """

    def render_to_json_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        return JsonResponse(self.get_data(context), **response_kwargs)

    def get_data(self, context):
        """
        Returns an object that will be serialized as JSON by json.dumps().
        """
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return context

```

Note
Check out the [Serializing Django objects](https://docs.djangoproject.com/en/5.0/topics/serialization/) documentation for more information on how to correctly transform Django models and querysets into JSON.
This mixin provides a `render_to_json_response()` method with the same signature as [`render_to_response()`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.render_to_response "django.views.generic.base.TemplateResponseMixin.render_to_response"). To use it, we need to mix it into a `TemplateView` for example, and override `render_to_response()` to call `render_to_json_response()` instead:
```
from django.views.generic import TemplateView


class JSONView(JSONResponseMixin, TemplateView):
    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(context, **response_kwargs)

```

Equally we could use our mixin with one of the generic views. We can make our own version of [`DetailView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/generic-display/#django.views.generic.detail.DetailView "django.views.generic.detail.DetailView") by mixing `JSONResponseMixin` with the [`BaseDetailView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/generic-display/#django.views.generic.detail.BaseDetailView "django.views.generic.detail.BaseDetailView") – (the [`DetailView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/generic-display/#django.views.generic.detail.DetailView "django.views.generic.detail.DetailView") before template rendering behavior has been mixed in):
```
from django.views.generic.detail import BaseDetailView


class JSONDetailView(JSONResponseMixin, BaseDetailView):
    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(context, **response_kwargs)

```

This view can then be deployed in the same way as any other [`DetailView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/generic-display/#django.views.generic.detail.DetailView "django.views.generic.detail.DetailView"), with exactly the same behavior – except for the format of the response.
If you want to be really adventurous, you could even mix a [`DetailView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/generic-display/#django.views.generic.detail.DetailView "django.views.generic.detail.DetailView") subclass that is able to return _both_ HTML and JSON content, depending on some property of the HTTP request, such as a query argument or an HTTP header. Mix in both the `JSONResponseMixin` and a [`SingleObjectTemplateResponseMixin`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectTemplateResponseMixin "django.views.generic.detail.SingleObjectTemplateResponseMixin"), and override the implementation of [`render_to_response()`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.render_to_response "django.views.generic.base.TemplateResponseMixin.render_to_response") to defer to the appropriate rendering method depending on the type of response that the user requested:
```
from django.views.generic.detail import SingleObjectTemplateResponseMixin


class HybridDetailView(
    JSONResponseMixin, SingleObjectTemplateResponseMixin, BaseDetailView
):
    def render_to_response(self, context):
        # Look for a 'format=json' GET argument
        if self.request.GET.get("format") == "json":
            return self.render_to_json_response(context)
        else:
            return super().render_to_response(context)

```

Because of the way that Python resolves method overloading, the call to `super().render_to_response(context)` ends up calling the [`render_to_response()`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.render_to_response "django.views.generic.base.TemplateResponseMixin.render_to_response") implementation of [`TemplateResponseMixin`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin "django.views.generic.base.TemplateResponseMixin").
Previous page and next page
[](https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-editing/)
[Migrations ](https://docs.djangoproject.com/en/5.0/topics/migrations/)
[](https://docs.djangoproject.com/en/5.0/topics/class-based-views/mixins/#top)
