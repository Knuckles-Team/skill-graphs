##  `FileResponse` objects[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#fileresponse-objects "Link to this heading")

_class_ FileResponse(_open_file_ , _as_attachment =False_, _filename =''_, _** kwargs_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/http/response/#FileResponse)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.FileResponse "Link to this definition")

[`FileResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.FileResponse "django.http.FileResponse") is a subclass of [`StreamingHttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.StreamingHttpResponse "django.http.StreamingHttpResponse") optimized for binary files. It uses
If `as_attachment=True`, the `Content-Disposition` header is set to `attachment`, which asks the browser to offer the file to the user as a download. Otherwise, a `Content-Disposition` header with a value of `inline` (the browser default) will be set only if a filename is available.
If `open_file` doesn’t have a name or if the name of `open_file` isn’t appropriate, provide a custom file name using the `filename` parameter. Note that if you pass a file-like object like `io.BytesIO`, it’s your task to `seek()` it before passing it to `FileResponse`.
The `Content-Length` header is automatically set when it can be guessed from the content of `open_file`.
The `Content-Type` header is automatically set when it can be guessed from the `filename`, or the name of `open_file`.
`FileResponse` accepts any file-like object with binary content, for example a file open in binary mode like so:
```
>>> from django.http import FileResponse
>>> response = FileResponse(open("myfile.png", "rb"))

```

The file will be closed automatically, so don’t open it with a context manager.
Use under ASGI
Python’s file API is synchronous. This means that the file must be fully consumed in order to be served under ASGI.
In order to stream a file asynchronously you need to use a third-party package that provides an asynchronous file API, such as
### Methods[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#id7 "Link to this heading")

FileResponse.set_headers(_open_file_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/http/response/#FileResponse.set_headers)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.FileResponse.set_headers "Link to this definition")

This method is automatically called during the response initialization and set various headers (`Content-Length`, `Content-Type`, and `Content-Disposition`) depending on `open_file`.
