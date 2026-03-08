## Useful Functions and Classes[¶](https://flask.palletsprojects.com/en/stable/api/#useful-functions-and-classes "Link to this heading")

flask.current_app[¶](https://flask.palletsprojects.com/en/stable/api/#flask.current_app "Link to this definition")

A proxy to the application handling the current request. This is useful to access the application without needing to import it, or if it can’t be imported, such as when using the application factory pattern or in blueprints and extensions.
This is only available when an [application context](https://flask.palletsprojects.com/en/stable/appcontext/) is pushed. This happens automatically during requests and CLI commands. It can be controlled manually with [`app_context()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.app_context "flask.Flask.app_context").
This is a proxy. See [Notes On Proxies](https://flask.palletsprojects.com/en/stable/reqcontext/#notes-on-proxies) for more information.

flask.has_request_context()[¶](https://flask.palletsprojects.com/en/stable/api/#flask.has_request_context "Link to this definition")

If you have code that wants to test if a request context is there or not this function can be used. For instance, you may want to take advantage of request information if the request object is available, but fail silently if it is unavailable.
```
class User(db.Model):

    def __init__(self, username, remote_addr=None):
        self.username = username
        if remote_addr is None and has_request_context():
            remote_addr = request.remote_addr
        self.remote_addr = remote_addr

```

Alternatively you can also just test any of the context bound objects (such as [`request`](https://flask.palletsprojects.com/en/stable/api/#flask.request "flask.request") or [`g`](https://flask.palletsprojects.com/en/stable/api/#flask.g "flask.g")) for truthness:
```
class User(db.Model):

    def __init__(self, username, remote_addr=None):
        self.username = username
        if remote_addr is None and request:
            remote_addr = request.remote_addr
        self.remote_addr = remote_addr

```

Changelog
Added in version 0.7.

Return type:


flask.copy_current_request_context(_f_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.copy_current_request_context "Link to this definition")

Decorate a function to run inside the current request context. This can be used when starting a background task, otherwise it will not see the app and request objects that were active in the parent.
Warning
Due to the following caveats, it is often safer (and simpler) to pass the data you need when starting the task, rather than using this and relying on the context objects.
In order to avoid execution switching partially though reading data, either read the request body (access `form`, `json`, `data`, etc) before starting the task, or use a lock. This can be an issue when using threading, but shouldn’t be an issue when using greenlet/gevent or asyncio.
If the task will access `session`, be sure to do so in the parent as well so that the `Vary: cookie` header will be set. Modifying `session` in the task should be avoided, as it may execute after the response cookie has already been written.
```
import gevent
from flask import copy_current_request_context

@app.route('/')
def index():
    @copy_current_request_context
    def do_some_work():
        # do some work here, it can access flask.request or
        # flask.session like you would otherwise in the view function.
        ...
    gevent.spawn(do_some_work)
    return 'Regular response'

```

Changelog
Added in version 0.10.

Parameters:

**f** (_F_)

Return type:

_F_

flask.has_app_context()[¶](https://flask.palletsprojects.com/en/stable/api/#flask.has_app_context "Link to this definition")

Works like [`has_request_context()`](https://flask.palletsprojects.com/en/stable/api/#flask.has_request_context "flask.has_request_context") but for the application context. You can also just do a boolean check on the [`current_app`](https://flask.palletsprojects.com/en/stable/api/#flask.current_app "flask.current_app") object instead.
Changelog
Added in version 0.9.

Return type:


flask.url_for(_endpoint_ , _*_ , __anchor =None_, __method =None_, __scheme =None_, __external =None_, _** values_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.url_for "Link to this definition")

Generate a URL to the given endpoint with the given values.
This requires an active request or application context, and calls [`current_app.url_for()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.url_for "flask.Flask.url_for"). See that method for full documentation.

Parameters:

  * **endpoint** (`.`, the current blueprint name (if any) will be used.
  * **_anchor** (_|__None_) – If given, append this as `#anchor` to the URL.
  * **_method** (_|__None_) – If given, generate the URL associated with this method for the endpoint.
  * **_scheme** (_|__None_) – If given, the URL will have this scheme if it is external.
  * **_external** (_|__None_) – If given, prefer the URL to be internal (False) or require it to be external (True). External URLs include the scheme and domain. When not in an active request, URLs are external by default.
  * **values** (`?a=b&c=d`.



Return type:
Changelog
Changed in version 2.2: Calls `current_app.url_for`, allowing an app to override the behavior.
Changed in version 0.10: The `_scheme` parameter was added.
Changed in version 0.9: The `_anchor` and `_method` parameters were added.
Changed in version 0.9: Calls `app.handle_url_build_error` on build errors.

flask.abort(_code_ , _* args_, _** kwargs_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.abort "Link to this definition")

Raise an [`HTTPException`](https://werkzeug.palletsprojects.com/en/stable/exceptions/#werkzeug.exceptions.HTTPException "\(in Werkzeug v3.1.x\)") for the given status code.
If [`current_app`](https://flask.palletsprojects.com/en/stable/api/#flask.current_app "flask.current_app") is available, it will call its [`aborter`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.aborter "flask.Flask.aborter") object, otherwise it will use [`werkzeug.exceptions.abort()`](https://werkzeug.palletsprojects.com/en/stable/exceptions/#werkzeug.exceptions.abort "\(in Werkzeug v3.1.x\)").

Parameters:

  * **code** (_|_[_Response_](https://werkzeug.palletsprojects.com/en/stable/wrappers/#werkzeug.wrappers.Response "\(in Werkzeug v3.1.x\)")) – The status code for the exception, which must be registered in `app.aborter`.
  * **args** (
  * **kwargs** (



Return type:
Changelog
Added in version 2.2: Calls `current_app.aborter` if available instead of always using Werkzeug’s default `abort`.

flask.redirect(_location_ , _code =302_, _Response =None_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.redirect "Link to this definition")

Create a redirect response object.
If [`current_app`](https://flask.palletsprojects.com/en/stable/api/#flask.current_app "flask.current_app") is available, it will use its [`redirect()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.redirect "flask.Flask.redirect") method, otherwise it will use [`werkzeug.utils.redirect()`](https://werkzeug.palletsprojects.com/en/stable/utils/#werkzeug.utils.redirect "\(in Werkzeug v3.1.x\)").

Parameters:

  * **location** (
  * **code** (
  * **Response** (_[_[_Response_](https://werkzeug.palletsprojects.com/en/stable/wrappers/#werkzeug.wrappers.Response "\(in Werkzeug v3.1.x\)") _]__|__None_) – The response class to use. Not used when `current_app` is active, which uses `app.response_class`.



Return type:

[_Response_](https://werkzeug.palletsprojects.com/en/stable/wrappers/#werkzeug.wrappers.Response "\(in Werkzeug v3.1.x\)") Changelog
Added in version 2.2: Calls `current_app.redirect` if available instead of always using Werkzeug’s default `redirect`.

flask.make_response(_* args_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.make_response "Link to this definition")

Sometimes it is necessary to set additional headers in a view. Because views do not have to return response objects but can return a value that is converted into a response object by Flask itself, it becomes tricky to add headers to it. This function can be called instead of using a return and you will get a response object which you can use to attach headers.
If view looked like this and you want to add a new header:
```
def index():
    return render_template('index.html', foo=42)

```

You can now do something like this:
```
def index():
    response = make_response(render_template('index.html', foo=42))
    response.headers['X-Parachutes'] = 'parachutes are cool'
    return response

```

This function accepts the very same arguments you can return from a view function. This for example creates a response with a 404 error code:
```
response = make_response(render_template('not_found.html'), 404)

```

The other use case of this function is to force the return value of a view function into a response which is helpful with view decorators:
```
response = make_response(view_function())
response.headers['X-Parachutes'] = 'parachutes are cool'

```

Internally this function does the following things:
  * if no arguments are passed, it creates a new response argument
  * if one argument is passed, [`flask.Flask.make_response()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.make_response "flask.Flask.make_response") is invoked with it.
  * if more than one argument is passed, the arguments are passed to the [`flask.Flask.make_response()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.make_response "flask.Flask.make_response") function as tuple.

Changelog
Added in version 0.6.

Parameters:

**args** (_t.Any_)

Return type:

[Response](https://flask.palletsprojects.com/en/stable/api/#flask.Response "flask.Response")

flask.after_this_request(_f_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.after_this_request "Link to this definition")

Executes a function after this request. This is useful to modify response objects. The function is passed the response object and has to return the same or a new one.
Example:
```
@app.route('/')
def index():
    @after_this_request
    def add_header(response):
        response.headers['X-Foo'] = 'Parachute'
        return response
    return 'Hello World!'

```

This is more useful if a function other than the view function wants to modify a response. For instance think of a decorator that wants to add some headers without converting the return value into a response object.
Changelog
Added in version 0.9.

Parameters:

**f** (_[__[__]__,__]__|__[__[__]__,__[__]__]_)

Return type:


flask.send_file(_path_or_file_ , _mimetype =None_, _as_attachment =False_, _download_name =None_, _conditional =True_, _etag =True_, _last_modified =None_, _max_age =None_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.send_file "Link to this definition")

Send the contents of a file to the client.
The first argument can be a file path or a file-like object. Paths are preferred in most cases because Werkzeug can manage the file and get extra information from the path. Passing a file-like object requires that the file is opened in binary mode, and is mostly useful when building a file in memory with
Never pass file paths provided by a user. The path is assumed to be trusted, so a user could craft a path to access a file you didn’t intend. Use [`send_from_directory()`](https://flask.palletsprojects.com/en/stable/api/#flask.send_from_directory "flask.send_from_directory") to safely serve user-requested paths from within a directory.
If the WSGI server sets a `file_wrapper` in `environ`, it is used, otherwise Werkzeug’s built-in wrapper is used. Alternatively, if the HTTP server supports `X-Sendfile`, configuring Flask with `USE_X_SENDFILE = True` will tell the server to send the given path, which is much more efficient than reading it in Python.

Parameters:

  * **path_or_file** (_[__t.AnyStr_ _]__|__|__t.IO_ _[__]_) – The path to the file to send, relative to the current working directory if a relative path is given. Alternatively, a file-like object opened in binary mode. Make sure the file pointer is seeked to the start of the data.
  * **mimetype** (_|__None_) – The MIME type to send for the file. If not provided, it will try to detect it from the file name.
  * **as_attachment** (
  * **download_name** (_|__None_) – The default name browsers will use when saving the file. Defaults to the passed file name.
  * **conditional** (`environ`.
  * **etag** (_|_
  * **last_modified** (_datetime_ _|__|__|__None_) – The last modified time to send for the file, in seconds. If not provided, it will try to detect it from the file path.
  * **max_age** (_None_ _|__(__|__t.Callable_ _[__[__|__None_ _]__,__|__None_ _]__)_) – How long the client should cache the file, in seconds. If set, `Cache-Control` will be `public`, otherwise it will be `no-cache` to prefer conditional caching.



Return type:

[Response](https://flask.palletsprojects.com/en/stable/api/#flask.Response "flask.Response") Changelog
Changed in version 2.0: `download_name` replaces the `attachment_filename` parameter. If `as_attachment=False`, it is passed with `Content-Disposition: inline` instead.
Changed in version 2.0: `max_age` replaces the `cache_timeout` parameter. `conditional` is enabled and `max_age` is not set by default.
Changed in version 2.0: `etag` replaces the `add_etags` parameter. It can be a string to use instead of generating one.
Changed in version 2.0: Passing a file-like object that inherits from
Added in version 2.0: Moved the implementation to Werkzeug. This is now a wrapper to pass some Flask-specific arguments.
Changed in version 1.1: `filename` may be a
Changed in version 1.1: Passing a
Changed in version 1.0.3: Filenames are encoded with ASCII instead of Latin-1 for broader compatibility with WSGI servers.
Changed in version 1.0: UTF-8 filenames as specified in
Changed in version 0.12: The filename is no longer automatically inferred from file objects. If you want to use automatic MIME and etag support, pass a filename via `filename_or_fp` or `attachment_filename`.
Changed in version 0.12: `attachment_filename` is preferred over `filename` for MIME detection.
Changed in version 0.9: `cache_timeout` defaults to [`Flask.get_send_file_max_age()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.get_send_file_max_age "flask.Flask.get_send_file_max_age").
Changed in version 0.7: MIME guessing and etag support for file-like objects was removed because it was unreliable. Pass a filename if you are able to, otherwise attach an etag yourself.
Changed in version 0.5: The `add_etags`, `cache_timeout` and `conditional` parameters were added. The default behavior is to add etags.
Added in version 0.2.

flask.send_from_directory(_directory_ , _path_ , _** kwargs_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.send_from_directory "Link to this definition")

Send a file from within a directory using [`send_file()`](https://flask.palletsprojects.com/en/stable/api/#flask.send_file "flask.send_file").
```
@app.route("/uploads/<path:name>")
def download_file(name):
    return send_from_directory(
        app.config['UPLOAD_FOLDER'], name, as_attachment=True
    )

```

This is a secure way to serve files from a folder, such as static files or uploads. Uses [`safe_join()`](https://werkzeug.palletsprojects.com/en/stable/utils/#werkzeug.security.safe_join "\(in Werkzeug v3.1.x\)") to ensure the path coming from the client is not maliciously crafted to point outside the specified directory.
If the final path does not point to an existing regular file, raises a 404 [`NotFound`](https://werkzeug.palletsprojects.com/en/stable/exceptions/#werkzeug.exceptions.NotFound "\(in Werkzeug v3.1.x\)") error.

Parameters:

  * **directory** (_[__]__|_`path` must be located under, relative to the current application’s root path. This _must not_ be a value provided by the client, otherwise it becomes insecure.
  * **path** (_[__]__|_`directory`.
  * **kwargs** (_t.Any_) – Arguments to pass to [`send_file()`](https://flask.palletsprojects.com/en/stable/api/#flask.send_file "flask.send_file").



Return type:

[Response](https://flask.palletsprojects.com/en/stable/api/#flask.Response "flask.Response") Changelog
Changed in version 2.0: `path` replaces the `filename` parameter.
Added in version 2.0: Moved the implementation to Werkzeug. This is now a wrapper to pass some Flask-specific arguments.
Added in version 0.5.
