## JSON Support[¶](https://flask.palletsprojects.com/en/stable/api/#module-flask.json "Link to this heading")
Flask uses Python’s built-in [`flask.Flask.json_provider_class`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.json_provider_class "flask.Flask.json_provider_class") or [`flask.Flask.json`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.json "flask.Flask.json"). The functions provided by `flask.json` will use methods on `app.json` if an app context is active.
Jinja’s `|tojson` filter is configured to use the app’s JSON provider. The filter marks the output with `|safe`. Use it to render data inside HTML `<script>` tags.
```
<script>
    const names = {{ names|tojson }};
    renderChart(names, {{ axis_data|tojson }});
</script>

```


flask.json.jsonify(_* args_, _** kwargs_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.json.jsonify "Link to this definition")

Serialize the given arguments as JSON, and return a [`Response`](https://flask.palletsprojects.com/en/stable/api/#flask.Response "flask.Response") object with the `application/json` mimetype. A dict or list returned from a view will be converted to a JSON response automatically without needing to call this.
This requires an active request or application context, and calls [`app.json.response()`](https://flask.palletsprojects.com/en/stable/api/#flask.json.provider.JSONProvider.response "flask.json.provider.JSONProvider.response").
In debug mode, the output is formatted with indentation to make it easier to read. This may also be controlled by the provider.
Either positional or keyword arguments can be given, not both. If no arguments are given, `None` is serialized.

Parameters:

  * **args** (_t.Any_) – A single value to serialize, or multiple values to treat as a list to serialize.
  * **kwargs** (_t.Any_) – Treat as a dict to serialize.



Return type:

[Response](https://flask.palletsprojects.com/en/stable/api/#flask.Response "flask.Response") Changelog
Changed in version 2.2: Calls `current_app.json.response`, allowing an app to override the behavior.
Changed in version 2.0.2:
Changed in version 0.11: Added support for serializing top-level arrays. This was a security risk in ancient browsers. See [JSON Security](https://flask.palletsprojects.com/en/stable/web-security/#security-json).
Added in version 0.2.

flask.json.dumps(_obj_ , _** kwargs_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.json.dumps "Link to this definition")

Serialize data as JSON.
If [`current_app`](https://flask.palletsprojects.com/en/stable/api/#flask.current_app "flask.current_app") is available, it will use its [`app.json.dumps()`](https://flask.palletsprojects.com/en/stable/api/#flask.json.provider.JSONProvider.dumps "flask.json.provider.JSONProvider.dumps") method, otherwise it will use

Parameters:

  * **obj** (
  * **kwargs** (`dumps` implementation.



Return type:
Changelog
Changed in version 2.3: The `app` parameter was removed.
Changed in version 2.2: Calls `current_app.json.dumps`, allowing an app to override the behavior.
Changed in version 2.0.2:
Changed in version 2.0: `encoding` will be removed in Flask 2.1.
Changed in version 1.0.3: `app` can be passed directly, rather than requiring an app context for configuration.

flask.json.dump(_obj_ , _fp_ , _** kwargs_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.json.dump "Link to this definition")

Serialize data as JSON and write to a file.
If [`current_app`](https://flask.palletsprojects.com/en/stable/api/#flask.current_app "flask.current_app") is available, it will use its [`app.json.dump()`](https://flask.palletsprojects.com/en/stable/api/#flask.json.provider.JSONProvider.dump "flask.json.provider.JSONProvider.dump") method, otherwise it will use

Parameters:

  * **obj** (
  * **fp** (_[__]_) – A file opened for writing text. Should use the UTF-8 encoding to be valid JSON.
  * **kwargs** (`dump` implementation.



Return type:

None Changelog
Changed in version 2.3: The `app` parameter was removed.
Changed in version 2.2: Calls `current_app.json.dump`, allowing an app to override the behavior.
Changed in version 2.0: Writing to a binary file, and the `encoding` argument, will be removed in Flask 2.1.

flask.json.loads(_s_ , _** kwargs_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.json.loads "Link to this definition")

Deserialize data as JSON.
If [`current_app`](https://flask.palletsprojects.com/en/stable/api/#flask.current_app "flask.current_app") is available, it will use its [`app.json.loads()`](https://flask.palletsprojects.com/en/stable/api/#flask.json.provider.JSONProvider.loads "flask.json.provider.JSONProvider.loads") method, otherwise it will use

Parameters:

  * **s** (_|_
  * **kwargs** (`loads` implementation.



Return type:
Changelog
Changed in version 2.3: The `app` parameter was removed.
Changed in version 2.2: Calls `current_app.json.loads`, allowing an app to override the behavior.
Changed in version 2.0: `encoding` will be removed in Flask 2.1. The data must be a string or UTF-8 bytes.
Changed in version 1.0.3: `app` can be passed directly, rather than requiring an app context for configuration.

flask.json.load(_fp_ , _** kwargs_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.json.load "Link to this definition")

Deserialize data as JSON read from a file.
If [`current_app`](https://flask.palletsprojects.com/en/stable/api/#flask.current_app "flask.current_app") is available, it will use its [`app.json.load()`](https://flask.palletsprojects.com/en/stable/api/#flask.json.provider.JSONProvider.load "flask.json.provider.JSONProvider.load") method, otherwise it will use

Parameters:

  * **fp** (
  * **kwargs** (`load` implementation.



Return type:
Changelog
Changed in version 2.3: The `app` parameter was removed.
Changed in version 2.2: Calls `current_app.json.load`, allowing an app to override the behavior.
Changed in version 2.2: The `app` parameter will be removed in Flask 2.3.
Changed in version 2.0: `encoding` will be removed in Flask 2.1. The file must be text mode, or binary mode with UTF-8 bytes.

_class_ flask.json.provider.JSONProvider(_app_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.json.provider.JSONProvider "Link to this definition")

A standard set of JSON operations for an application. Subclasses of this can be used to customize JSON behavior or use different JSON libraries.
To implement a provider for a specific library, subclass this base class and implement at least [`dumps()`](https://flask.palletsprojects.com/en/stable/api/#flask.json.provider.JSONProvider.dumps "flask.json.provider.JSONProvider.dumps") and [`loads()`](https://flask.palletsprojects.com/en/stable/api/#flask.json.provider.JSONProvider.loads "flask.json.provider.JSONProvider.loads"). All other methods have default implementations.
To use a different provider, either subclass `Flask` and set [`json_provider_class`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.json_provider_class "flask.Flask.json_provider_class") to a provider class, or set [`app.json`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.json "flask.Flask.json") to an instance of the class.

Parameters:

**app** (_App_) – An application instance. This will be stored as a `weakref.proxy` on the `_app` attribute. Changelog
Added in version 2.2.

dumps(_obj_ , _** kwargs_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.json.provider.JSONProvider.dumps "Link to this definition")

Serialize data as JSON.

Parameters:

  * **obj** (
  * **kwargs** (



Return type:


dump(_obj_ , _fp_ , _** kwargs_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.json.provider.JSONProvider.dump "Link to this definition")

Serialize data as JSON and write to a file.

Parameters:

  * **obj** (
  * **fp** (_[__]_) – A file opened for writing text. Should use the UTF-8 encoding to be valid JSON.
  * **kwargs** (



Return type:

None

loads(_s_ , _** kwargs_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.json.provider.JSONProvider.loads "Link to this definition")

Deserialize data as JSON.

Parameters:

  * **s** (_|_
  * **kwargs** (



Return type:


load(_fp_ , _** kwargs_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.json.provider.JSONProvider.load "Link to this definition")

Deserialize data as JSON read from a file.

Parameters:

  * **fp** (
  * **kwargs** (



Return type:


response(_* args_, _** kwargs_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.json.provider.JSONProvider.response "Link to this definition")

Serialize the given arguments as JSON, and return a [`Response`](https://flask.palletsprojects.com/en/stable/api/#flask.Response "flask.Response") object with the `application/json` mimetype.
The [`jsonify()`](https://flask.palletsprojects.com/en/stable/api/#flask.json.jsonify "flask.json.jsonify") function calls this method for the current application.
Either positional or keyword arguments can be given, not both. If no arguments are given, `None` is serialized.

Parameters:

  * **args** (_t.Any_) – A single value to serialize, or multiple values to treat as a list to serialize.
  * **kwargs** (_t.Any_) – Treat as a dict to serialize.



Return type:

[Response](https://flask.palletsprojects.com/en/stable/api/#flask.Response "flask.Response")

_class_ flask.json.provider.DefaultJSONProvider(_app_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.json.provider.DefaultJSONProvider "Link to this definition")

Provide JSON operations using Python’s built-in
  * `dataclasses.dataclass` is passed to
  * `Markup` (or any object with a `__html__` method) will call the `__html__` method to get a string.



Parameters:

**app** (_App_)

_static_ default(_o_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.json.provider.DefaultJSONProvider.default "Link to this definition")

Apply this function to any object that `json.dumps()` does not know how to serialize. It should return a valid JSON type or raise a `TypeError`.

Parameters:

**o** (

Return type:


ensure_ascii _= True_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.json.provider.DefaultJSONProvider.ensure_ascii "Link to this definition")

Replace non-ASCII characters with escape sequences. This may be more compatible with some clients, but can be disabled for better performance and size.

sort_keys _= True_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.json.provider.DefaultJSONProvider.sort_keys "Link to this definition")

Sort the keys in any serialized dicts. This may be useful for some caching situations, but can be disabled for better performance. When enabled, keys must all be strings, they are not converted before sorting.

compact _: |__= None_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.json.provider.DefaultJSONProvider.compact "Link to this definition")

If `True`, or `None` out of debug mode, the [`response()`](https://flask.palletsprojects.com/en/stable/api/#flask.json.provider.DefaultJSONProvider.response "flask.json.provider.DefaultJSONProvider.response") output will not add indentation, newlines, or spaces. If `False`, or `None` in debug mode, it will use a non-compact representation.

mimetype _= 'application/json'_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.json.provider.DefaultJSONProvider.mimetype "Link to this definition")

The mimetype set in [`response()`](https://flask.palletsprojects.com/en/stable/api/#flask.json.provider.DefaultJSONProvider.response "flask.json.provider.DefaultJSONProvider.response").

dumps(_obj_ , _** kwargs_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.json.provider.DefaultJSONProvider.dumps "Link to this definition")

Serialize data as JSON to a string.
Keyword arguments are passed to [`default`](https://flask.palletsprojects.com/en/stable/api/#flask.json.provider.DefaultJSONProvider.default "flask.json.provider.DefaultJSONProvider.default"), [`ensure_ascii`](https://flask.palletsprojects.com/en/stable/api/#flask.json.provider.DefaultJSONProvider.ensure_ascii "flask.json.provider.DefaultJSONProvider.ensure_ascii"), and [`sort_keys`](https://flask.palletsprojects.com/en/stable/api/#flask.json.provider.DefaultJSONProvider.sort_keys "flask.json.provider.DefaultJSONProvider.sort_keys") attributes.

Parameters:

  * **obj** (
  * **kwargs** (



Return type:


loads(_s_ , _** kwargs_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.json.provider.DefaultJSONProvider.loads "Link to this definition")

Deserialize data as JSON from a string or bytes.

Parameters:

  * **s** (_|_
  * **kwargs** (



Return type:


response(_* args_, _** kwargs_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.json.provider.DefaultJSONProvider.response "Link to this definition")

Serialize the given arguments as JSON, and return a [`Response`](https://flask.palletsprojects.com/en/stable/api/#flask.Response "flask.Response") object with it. The response mimetype will be “application/json” and can be changed with [`mimetype`](https://flask.palletsprojects.com/en/stable/api/#flask.json.provider.DefaultJSONProvider.mimetype "flask.json.provider.DefaultJSONProvider.mimetype").
If [`compact`](https://flask.palletsprojects.com/en/stable/api/#flask.json.provider.DefaultJSONProvider.compact "flask.json.provider.DefaultJSONProvider.compact") is `False` or debug mode is enabled, the output will be formatted to be easier to read.
Either positional or keyword arguments can be given, not both. If no arguments are given, `None` is serialized.

Parameters:

  * **args** (_t.Any_) – A single value to serialize, or multiple values to treat as a list to serialize.
  * **kwargs** (_t.Any_) – Treat as a dict to serialize.



Return type:

[Response](https://flask.palletsprojects.com/en/stable/api/#flask.Response "flask.Response")
### Tagged JSON[¶](https://flask.palletsprojects.com/en/stable/api/#tagged-json "Link to this heading")
A compact representation for lossless serialization of non-standard JSON types. [`SecureCookieSessionInterface`](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SecureCookieSessionInterface "flask.sessions.SecureCookieSessionInterface") uses this to serialize the session data, but it may be useful in other places. It can be extended to support other types.

_class_ flask.json.tag.TaggedJSONSerializer[¶](https://flask.palletsprojects.com/en/stable/api/#flask.json.tag.TaggedJSONSerializer "Link to this definition")

Serializer that uses a tag system to compactly represent objects that are not JSON types. Passed as the intermediate serializer to `itsdangerous.Serializer`.
The following extra types are supported:
  * `Markup`



default_tags _=[<class 'flask.json.tag.TagDict'>, <class 'flask.json.tag.PassDict'>, <class 'flask.json.tag.TagTuple'>, <class 'flask.json.tag.PassList'>, <class 'flask.json.tag.TagBytes'>, <class 'flask.json.tag.TagMarkup'>, <class 'flask.json.tag.TagUUID'>, <class 'flask.json.tag.TagDateTime'>]_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.json.tag.TaggedJSONSerializer.default_tags "Link to this definition")

Tag classes to bind when creating the serializer. Other tags can be added later using [`register()`](https://flask.palletsprojects.com/en/stable/api/#flask.json.tag.TaggedJSONSerializer.register "flask.json.tag.TaggedJSONSerializer.register").

register(_tag_class_ , _force =False_, _index =None_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.json.tag.TaggedJSONSerializer.register "Link to this definition")

Register a new tag with this serializer.

Parameters:

  * **tag_class** (_[_[_JSONTag_](https://flask.palletsprojects.com/en/stable/api/#flask.json.tag.JSONTag "flask.json.tag.JSONTag") _]_) – tag class to register. Will be instantiated with this serializer instance.
  * **force** (
  * **index** (_|__None_) – index to insert the new tag in the tag order. Useful when the new tag is a special case of an existing tag. If `None` (default), the tag is appended to the end of the order.



Raises:

`force` is not true.

Return type:

None

tag(_value_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.json.tag.TaggedJSONSerializer.tag "Link to this definition")

Convert a value to a tagged representation if necessary.

Parameters:

**value** (

Return type:


untag(_value_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.json.tag.TaggedJSONSerializer.untag "Link to this definition")

Convert a tagged representation back to the original type.

Parameters:

**value** (_[__,__]_)

Return type:


dumps(_value_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.json.tag.TaggedJSONSerializer.dumps "Link to this definition")

Tag the value and dump it to a compact JSON string.

Parameters:

**value** (

Return type:


loads(_value_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.json.tag.TaggedJSONSerializer.loads "Link to this definition")

Load data from a JSON string and deserialized any tagged objects.

Parameters:

**value** (

Return type:


_class_ flask.json.tag.JSONTag(_serializer_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.json.tag.JSONTag "Link to this definition")

Base class for defining type tags for [`TaggedJSONSerializer`](https://flask.palletsprojects.com/en/stable/api/#flask.json.tag.TaggedJSONSerializer "flask.json.tag.TaggedJSONSerializer").

Parameters:

**serializer** ([_TaggedJSONSerializer_](https://flask.palletsprojects.com/en/stable/api/#flask.json.tag.TaggedJSONSerializer "flask.json.tag.TaggedJSONSerializer"))

key _:__= ''_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.json.tag.JSONTag.key "Link to this definition")

The tag to mark the serialized object with. If empty, this tag is only used as an intermediate step during tagging.

check(_value_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.json.tag.JSONTag.check "Link to this definition")

Check if the given value should be tagged by this tag.

Parameters:

**value** (

Return type:


to_json(_value_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.json.tag.JSONTag.to_json "Link to this definition")

Convert the Python object to an object that is a valid JSON type. The tag will be added later.

Parameters:

**value** (

Return type:


to_python(_value_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.json.tag.JSONTag.to_python "Link to this definition")

Convert the JSON representation back to the correct type. The tag will already be removed.

Parameters:

**value** (

Return type:


tag(_value_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.json.tag.JSONTag.tag "Link to this definition")

Convert the value to a valid JSON type and add the tag structure around it.

Parameters:

**value** (

Return type:

Let’s see an example that adds support for `[key, value]` pairs. Subclass [`JSONTag`](https://flask.palletsprojects.com/en/stable/api/#flask.json.tag.JSONTag "flask.json.tag.JSONTag") and give it the new key `' od'` to identify the type. The session serializer processes dicts first, so insert the new tag at the front of the order since `OrderedDict` must be processed before `dict`.
```
from flask.json.tag import JSONTag

class TagOrderedDict(JSONTag):
    __slots__ = ('serializer',)
    key = ' od'

    def check(self, value):
        return isinstance(value, OrderedDict)

    def to_json(self, value):
        return [[k, self.serializer.tag(v)] for k, v in iteritems(value)]

    def to_python(self, value):
        return OrderedDict(value)

app.session_interface.serializer.register(TagOrderedDict, index=0)

```
