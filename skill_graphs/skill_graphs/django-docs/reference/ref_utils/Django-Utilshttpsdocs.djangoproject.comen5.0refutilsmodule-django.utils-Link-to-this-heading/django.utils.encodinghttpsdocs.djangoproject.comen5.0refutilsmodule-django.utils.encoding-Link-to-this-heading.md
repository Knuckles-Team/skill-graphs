##  `django.utils.encoding`[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#module-django.utils.encoding "Link to this heading")

smart_str(_s_ , _encoding ='utf-8'_, _strings_only =False_, _errors ='strict'_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/encoding/#smart_str)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.encoding.smart_str "Link to this definition")

Returns a `str` object representing arbitrary object `s`. Treats bytestrings using the `encoding` codec.
If `strings_only` is `True`, don’t convert (some) non-string-like objects.

is_protected_type(_obj_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/encoding/#is_protected_type)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.encoding.is_protected_type "Link to this definition")

Determine if the object instance is of a protected type.
Objects of protected types are preserved as-is when passed to `force_str(strings_only=True)`.

force_str(_s_ , _encoding ='utf-8'_, _strings_only =False_, _errors ='strict'_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/encoding/#force_str)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.encoding.force_str "Link to this definition")

Similar to `smart_str()`, except that lazy instances are resolved to strings, rather than kept as lazy objects.
If `strings_only` is `True`, don’t convert (some) non-string-like objects.

smart_bytes(_s_ , _encoding ='utf-8'_, _strings_only =False_, _errors ='strict'_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/encoding/#smart_bytes)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.encoding.smart_bytes "Link to this definition")

Returns a bytestring version of arbitrary object `s`, encoded as specified in `encoding`.
If `strings_only` is `True`, don’t convert (some) non-string-like objects.

force_bytes(_s_ , _encoding ='utf-8'_, _strings_only =False_, _errors ='strict'_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/encoding/#force_bytes)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.encoding.force_bytes "Link to this definition")

Similar to `smart_bytes`, except that lazy instances are resolved to bytestrings, rather than kept as lazy objects.
If `strings_only` is `True`, don’t convert (some) non-string-like objects.

iri_to_uri(_iri_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/encoding/#iri_to_uri)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.encoding.iri_to_uri "Link to this definition")

Convert an Internationalized Resource Identifier (IRI) portion to a URI portion that is suitable for inclusion in a URL.
This is the algorithm from section 3.1 of
Takes an IRI (string or UTF-8 bytes) and returns a string containing the encoded result.

uri_to_iri(_uri_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/encoding/#uri_to_iri)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.encoding.uri_to_iri "Link to this definition")

Converts a Uniform Resource Identifier into an Internationalized Resource Identifier.
This is an algorithm from section 3.2 of
Takes a URI in ASCII bytes and returns a string containing the encoded result.

filepath_to_uri(_path_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/encoding/#filepath_to_uri)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.encoding.filepath_to_uri "Link to this definition")

Convert a file system path to a URI portion that is suitable for inclusion in a URL. The path is assumed to be either UTF-8 bytes, string, or a
This method will encode certain characters that would normally be recognized as special characters for URIs. Note that this method does not encode the ‘ character, as it is a valid character within URIs. See `encodeURIComponent()` JavaScript function for more details.
Returns an ASCII string containing the encoded result.

escape_uri_path(_path_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/encoding/#escape_uri_path)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.encoding.escape_uri_path "Link to this definition")

Escapes the unsafe characters from the path portion of a Uniform Resource Identifier (URI).
