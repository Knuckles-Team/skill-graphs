##  `JsonResponse` objects[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#jsonresponse-objects "Link to this heading")

_class_ JsonResponse(_data_ , _encoder =DjangoJSONEncoder_, _safe =True_, _json_dumps_params =None_, _** kwargs_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/http/response/#JsonResponse)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.JsonResponse "Link to this definition")

An [`HttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse") subclass that helps to create a JSON-encoded response. It inherits most behavior from its superclass with a couple differences:
Its default `Content-Type` header is set to _application/json_.
The first parameter, `data`, should be a `dict` instance. If the `safe` parameter is set to `False` (see below) it can be any JSON-serializable object.
The `encoder`, which defaults to [`django.core.serializers.json.DjangoJSONEncoder`](https://docs.djangoproject.com/en/5.0/topics/serialization/#django.core.serializers.json.DjangoJSONEncoder "django.core.serializers.json.DjangoJSONEncoder"), will be used to serialize the data. See [JSON serialization](https://docs.djangoproject.com/en/5.0/topics/serialization/#serialization-formats-json) for more details about this serializer.
The `safe` boolean parameter defaults to `True`. If it’s set to `False`, any object can be passed for serialization (otherwise only `dict` instances are allowed). If `safe` is `True` and a non-`dict` object is passed as the first argument, a
The `json_dumps_params` parameter is a dictionary of keyword arguments to pass to the `json.dumps()` call used to generate the response.
### Usage[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#id5 "Link to this heading")
Typical usage could look like:
```
>>> from django.http import JsonResponse
>>> response = JsonResponse({"foo": "bar"})
>>> response.content
b'{"foo": "bar"}'

```

#### Serializing non-dictionary objects[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#serializing-non-dictionary-objects "Link to this heading")
In order to serialize objects other than `dict` you must set the `safe` parameter to `False`:
```
>>> response = JsonResponse([1, 2, 3], safe=False)

```

Without passing `safe=False`, a
Note that an API based on `dict` objects is more extensible, flexible, and makes it easier to maintain forwards compatibility. Therefore, you should avoid using non-dict objects in JSON-encoded response.
Warning
Before the `Array` constructor. For this reason, Django does not allow passing non-dict objects to the [`JsonResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.JsonResponse "django.http.JsonResponse") constructor by default. However, most modern browsers implement ECMAScript 5 which removes this attack vector. Therefore it is possible to disable this security precaution.
#### Changing the default JSON encoder[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#changing-the-default-json-encoder "Link to this heading")
If you need to use a different JSON encoder class you can pass the `encoder` parameter to the constructor method:
```
>>> response = JsonResponse(data, encoder=MyJSONEncoder)

```
