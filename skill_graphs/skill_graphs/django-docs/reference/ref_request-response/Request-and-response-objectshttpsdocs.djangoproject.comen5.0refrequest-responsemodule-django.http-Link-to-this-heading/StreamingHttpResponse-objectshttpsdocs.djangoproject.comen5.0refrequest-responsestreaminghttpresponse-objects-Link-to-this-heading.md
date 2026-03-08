##  `StreamingHttpResponse` objects[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#streaminghttpresponse-objects "Link to this heading")

_class_ StreamingHttpResponse[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/http/response/#StreamingHttpResponse)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.StreamingHttpResponse "Link to this definition")

The [`StreamingHttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.StreamingHttpResponse "django.http.StreamingHttpResponse") class is used to stream a response from Django to the browser.
Advanced usage
[`StreamingHttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.StreamingHttpResponse "django.http.StreamingHttpResponse") is somewhat advanced, in that it is important to know whether you’ll be serving your application synchronously under WSGI or asynchronously under ASGI, and adjust your usage appropriately.
Please read these notes with care.
An example usage of [`StreamingHttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.StreamingHttpResponse "django.http.StreamingHttpResponse") under WSGI is streaming content when generating the response would take too long or uses too much memory. For instance, it’s useful for [generating large CSV files](https://docs.djangoproject.com/en/5.0/howto/outputting-csv/#streaming-csv-files).
There are performance considerations when doing this, though. Django, under WSGI, is designed for short-lived requests. Streaming responses will tie a worker process for the entire duration of the response. This may result in poor performance.
Generally speaking, you would perform expensive tasks outside of the request-response cycle, rather than resorting to a streamed response.
When serving under ASGI, however, a [`StreamingHttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.StreamingHttpResponse "django.http.StreamingHttpResponse") need not stop other requests from being served whilst waiting for I/O. This opens up the possibility of long-lived requests for streaming content and implementing patterns such as long-polling, and server-sent events.
Even under ASGI note, [`StreamingHttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.StreamingHttpResponse "django.http.StreamingHttpResponse") should only be used in situations where it is absolutely required that the whole content isn’t iterated before transferring the data to the client. Because the content can’t be accessed, many middleware can’t function normally. For example the `ETag` and `Content-Length` headers can’t be generated for streaming responses.
The [`StreamingHttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.StreamingHttpResponse "django.http.StreamingHttpResponse") is not a subclass of [`HttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse"), because it features a slightly different API. However, it is almost identical, with the following notable differences:
  * It should be given an iterator that yields bytestrings,
  * You cannot access its content, except by iterating the response object itself. This should only occur when the response is returned to the client: you should not iterate the response yourself.
Under WSGI the response will be iterated synchronously. Under ASGI the response will be iterated asynchronously. (This is why the iterator type must match the protocol you’re using.)
To avoid a crash, an incorrect iterator type will be mapped to the correct type during iteration, and a warning will be raised, but in order to do this the iterator must be fully-consumed, which defeats the purpose of using a [`StreamingHttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.StreamingHttpResponse "django.http.StreamingHttpResponse") at all.
  * It has no `content` attribute. Instead, it has a [`streaming_content`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.StreamingHttpResponse.streaming_content "django.http.StreamingHttpResponse.streaming_content") attribute. This can be used in middleware to wrap the response iterable, but should not be consumed.
  * You cannot use the file-like object `tell()` or `write()` methods. Doing so will raise an exception.


The [`HttpResponseBase`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponseBase "django.http.HttpResponseBase") base class is common between [`HttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse") and [`StreamingHttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.StreamingHttpResponse "django.http.StreamingHttpResponse").
Changed in Django 4.2:
Support for asynchronous iteration was added.
### Attributes[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#id6 "Link to this heading")

StreamingHttpResponse.streaming_content[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.StreamingHttpResponse.streaming_content "Link to this definition")

An iterator of the response content, bytestring encoded according to [`HttpResponse.charset`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse.charset "django.http.HttpResponse.charset").

StreamingHttpResponse.status_code[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.StreamingHttpResponse.status_code "Link to this definition")

The
Unless [`reason_phrase`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.StreamingHttpResponse.reason_phrase "django.http.StreamingHttpResponse.reason_phrase") is explicitly set, modifying the value of `status_code` outside the constructor will also modify the value of `reason_phrase`.

StreamingHttpResponse.reason_phrase[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.StreamingHttpResponse.reason_phrase "Link to this definition")

The HTTP reason phrase for the response. It uses the
Unless explicitly set, `reason_phrase` is determined by the value of [`status_code`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.StreamingHttpResponse.status_code "django.http.StreamingHttpResponse.status_code").

StreamingHttpResponse.streaming[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.StreamingHttpResponse.streaming "Link to this definition")

This is always `True`.

StreamingHttpResponse.is_async[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.StreamingHttpResponse.is_async "Link to this definition")

New in Django 4.2.
Boolean indicating whether [`StreamingHttpResponse.streaming_content`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.StreamingHttpResponse.streaming_content "django.http.StreamingHttpResponse.streaming_content") is an asynchronous iterator or not.
This is useful for middleware needing to wrap [`StreamingHttpResponse.streaming_content`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.StreamingHttpResponse.streaming_content "django.http.StreamingHttpResponse.streaming_content").
### Handling disconnects[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#handling-disconnects "Link to this heading")
New in Django 5.0.
If the client disconnects during a streaming response, Django will cancel the coroutine that is handling the response. If you want to clean up resources manually, you can do so by catching the `asyncio.CancelledError`:
```
async def streaming_response():
    try:
        # Do some work here
        async for chunk in my_streaming_iterator():
            yield chunk
    except asyncio.CancelledError:
        # Handle disconnect
        ...
        raise


async def my_streaming_view(request):
    return StreamingHttpResponse(streaming_response())

```

This example only shows how to handle client disconnection while the response is streaming. If you perform long-running operations in your view before returning the `StreamingHttpResponse` object, then you may also want to [handle disconnections in the view](https://docs.djangoproject.com/en/5.0/topics/async/#async-handling-disconnect) itself.
