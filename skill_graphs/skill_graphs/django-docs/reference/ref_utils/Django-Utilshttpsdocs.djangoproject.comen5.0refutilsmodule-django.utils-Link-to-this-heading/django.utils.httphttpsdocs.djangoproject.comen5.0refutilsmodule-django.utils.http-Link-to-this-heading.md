##  `django.utils.http`[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#module-django.utils.http "Link to this heading")

urlencode(_query_ , _doseq =False_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/http/#urlencode)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.http.urlencode "Link to this definition")

A version of Python’s `MultiValueDict` and non-string values.

http_date(_epoch_seconds =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/http/#http_date)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.http.http_date "Link to this definition")

Formats the time to match the
Accepts a floating point number expressed in seconds since the epoch in UTC–such as that outputted by `time.time()`. If set to `None`, defaults to the current time.
Outputs a string in the format `Wdy, DD Mon YYYY HH:MM:SS GMT`.

content_disposition_header(_as_attachment_ , _filename_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/http/#content_disposition_header)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.http.content_disposition_header "Link to this definition")

New in Django 4.2.
Constructs a `Content-Disposition` HTTP header value from the given `filename` as specified by `None` if `as_attachment` is `False` and `filename` is `None`, otherwise returns a string suitable for the `Content-Disposition` HTTP header.

base36_to_int(_s_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/http/#base36_to_int)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.http.base36_to_int "Link to this definition")

Converts a base 36 string to an integer.

int_to_base36(_i_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/http/#int_to_base36)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.http.int_to_base36 "Link to this definition")

Converts a positive integer to a base 36 string.

urlsafe_base64_encode(_s_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/http/#urlsafe_base64_encode)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.http.urlsafe_base64_encode "Link to this definition")

Encodes a bytestring to a base64 string for use in URLs, stripping any trailing equal signs.

urlsafe_base64_decode(_s_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/http/#urlsafe_base64_decode)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.http.urlsafe_base64_decode "Link to this definition")

Decodes a base64 encoded string, adding back any trailing equal signs that might have been stripped.
