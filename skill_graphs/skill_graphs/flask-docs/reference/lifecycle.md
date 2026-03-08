### Navigation
  * [index](https://flask.palletsprojects.com/en/stable/genindex/ "General Index")
  * [modules](https://flask.palletsprojects.com/en/stable/py-modindex/ "Python Module Index") |
  * [next](https://flask.palletsprojects.com/en/stable/appcontext/ "The Application Context") |
  * [previous](https://flask.palletsprojects.com/en/stable/views/ "Class-based Views") |
  * [Flask Documentation (3.1.x)](https://flask.palletsprojects.com/en/stable/) »
  * [Application Structure and Lifecycle](https://flask.palletsprojects.com/en/stable/lifecycle/)


# Application Structure and Lifecycle[¶](https://flask.palletsprojects.com/en/stable/lifecycle/#application-structure-and-lifecycle "Link to this heading")
Flask makes it pretty easy to write a web application. But there are quite a few different parts to an application and to each request it handles. Knowing what happens during application setup, serving, and handling requests will help you know what’s possible in Flask and how to structure your application.
## Application Setup[¶](https://flask.palletsprojects.com/en/stable/lifecycle/#application-setup "Link to this heading")
The first step in creating a Flask application is creating the application object. Each Flask application is an instance of the [`Flask`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask "flask.Flask") class, which collects all configuration, extensions, and views.
```
from flask import Flask

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY="dev",
)
app.config.from_prefixed_env()

@app.route("/")
def index():
    return "Hello, World!"

```

This is known as the “application setup phase”, it’s the code you write that’s outside any view functions or other handlers. It can be split up between different modules and sub-packages, but all code that you want to be part of your application must be imported in order for it to be registered.
All application setup must be completed before you start serving your application and handling requests. This is because WSGI servers divide work between multiple workers, or can be distributed across multiple machines. If the configuration changed in one worker, there’s no way for Flask to ensure consistency between other workers.
Flask tries to help developers catch some of these setup ordering issues by showing an error if setup-related methods are called after requests are handled. In that case you’ll see this error:
> The setup method ‘route’ can no longer be called on the application. It has already handled its first request, any changes will not be applied consistently. Make sure all imports, decorators, functions, etc. needed to set up the application are done before running it.
However, it is not possible for Flask to detect all cases of out-of-order setup. In general, don’t do anything to modify the `Flask` app object and `Blueprint` objects from within view functions that run during requests. This includes:
  * Adding routes, view functions, and other request handlers with `@app.route`, `@app.errorhandler`, `@app.before_request`, etc.
  * Registering blueprints.
  * Loading configuration with `app.config`.
  * Setting up the Jinja template environment with `app.jinja_env`.
  * Setting a session interface, instead of the default itsdangerous cookie.
  * Setting a JSON provider with `app.json`, instead of the default provider.
  * Creating and initializing Flask extensions.


## Serving the Application[¶](https://flask.palletsprojects.com/en/stable/lifecycle/#serving-the-application "Link to this heading")
Flask is a WSGI application framework. The other half of WSGI is the WSGI server. During development, Flask, through Werkzeug, provides a development WSGI server with the `flask run` CLI command. When you are done with development, use a production server to serve your application, see [Deploying to Production](https://flask.palletsprojects.com/en/stable/deploying/).
Regardless of what server you’re using, it will follow the
  1. Browser or other client makes HTTP request.
  2. WSGI server receives request.
  3. WSGI server converts HTTP data to WSGI `environ` dict.
  4. WSGI server calls WSGI application with the `environ`.
  5. Flask, the WSGI application, does all its internal processing to route the request to a view function, handle errors, etc.
  6. Flask translates View function return into WSGI response data, passes it to WSGI server.
  7. WSGI server creates and send an HTTP response.
  8. Client receives the HTTP response.


### Middleware[¶](https://flask.palletsprojects.com/en/stable/lifecycle/#middleware "Link to this heading")
The WSGI application above is a callable that behaves in a certain way. Middleware is a WSGI application that wraps another WSGI application. It’s a similar concept to Python decorators. The outermost middleware will be called by the server. It can modify the data passed to it, then call the WSGI application (or further middleware) that it wraps, and so on. And it can take the return value of that call and modify it further.
From the WSGI server’s perspective, there is one WSGI application, the one it calls directly. Typically, Flask is the “real” application at the end of the chain of middleware. But even Flask can call further WSGI applications, although that’s an advanced, uncommon use case.
A common middleware you’ll see used with Flask is Werkzeug’s [`ProxyFix`](https://werkzeug.palletsprojects.com/en/stable/middleware/proxy_fix/#werkzeug.middleware.proxy_fix.ProxyFix "\(in Werkzeug v3.1.x\)"), which modifies the request to look like it came directly from a client even if it passed through HTTP proxies on the way. There are other middleware that can handle serving static files, authentication, etc.
## How a Request is Handled[¶](https://flask.palletsprojects.com/en/stable/lifecycle/#how-a-request-is-handled "Link to this heading")
For us, the interesting part of the steps above is when Flask gets called by the WSGI server (or middleware). At that point, it will do quite a lot to handle the request and generate the response. At the most basic, it will match the URL to a view function, call the view function, and pass the return value back to the server. But there are many more parts that you can use to customize its behavior.
  1. WSGI server calls the Flask object, which calls [`Flask.wsgi_app()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.wsgi_app "flask.Flask.wsgi_app").
  2. A [`RequestContext`](https://flask.palletsprojects.com/en/stable/api/#flask.ctx.RequestContext "flask.ctx.RequestContext") object is created. This converts the WSGI `environ` dict into a [`Request`](https://flask.palletsprojects.com/en/stable/api/#flask.Request "flask.Request") object. It also creates an `AppContext` object.
  3. The [app context](https://flask.palletsprojects.com/en/stable/appcontext/) is pushed, which makes [`current_app`](https://flask.palletsprojects.com/en/stable/api/#flask.current_app "flask.current_app") and [`g`](https://flask.palletsprojects.com/en/stable/api/#flask.g "flask.g") available.
  4. The [`appcontext_pushed`](https://flask.palletsprojects.com/en/stable/api/#flask.appcontext_pushed "flask.appcontext_pushed") signal is sent.
  5. The [request context](https://flask.palletsprojects.com/en/stable/reqcontext/) is pushed, which makes [`request`](https://flask.palletsprojects.com/en/stable/api/#flask.request "flask.request") and [`session`](https://flask.palletsprojects.com/en/stable/api/#flask.session "flask.session") available.
  6. The session is opened, loading any existing session data using the app’s [`session_interface`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.session_interface "flask.Flask.session_interface"), an instance of [`SessionInterface`](https://flask.palletsprojects.com/en/stable/api/#flask.sessions.SessionInterface "flask.sessions.SessionInterface").
  7. The URL is matched against the URL rules registered with the [`route()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.route "flask.Flask.route") decorator during application setup. If there is no match, the error - usually a 404, 405, or redirect - is stored to be handled later.
  8. The [`request_started`](https://flask.palletsprojects.com/en/stable/api/#flask.request_started "flask.request_started") signal is sent.
  9. Any [`url_value_preprocessor()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.url_value_preprocessor "flask.Flask.url_value_preprocessor") decorated functions are called.
  10. Any [`before_request()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.before_request "flask.Flask.before_request") decorated functions are called. If any of these function returns a value it is treated as the response immediately.
  11. If the URL didn’t match a route a few steps ago, that error is raised now.
  12. The [`route()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.route "flask.Flask.route") decorated view function associated with the matched URL is called and returns a value to be used as the response.
  13. If any step so far raised an exception, and there is an [`errorhandler()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.errorhandler "flask.Flask.errorhandler") decorated function that matches the exception class or HTTP error code, it is called to handle the error and return a response.
  14. Whatever returned a response value - a before request function, the view, or an error handler, that value is converted to a [`Response`](https://flask.palletsprojects.com/en/stable/api/#flask.Response "flask.Response") object.
  15. Any [`after_this_request()`](https://flask.palletsprojects.com/en/stable/api/#flask.after_this_request "flask.after_this_request") decorated functions are called, then cleared.
  16. Any [`after_request()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.after_request "flask.Flask.after_request") decorated functions are called, which can modify the response object.
  17. The session is saved, persisting any modified session data using the app’s [`session_interface`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.session_interface "flask.Flask.session_interface").
  18. The [`request_finished`](https://flask.palletsprojects.com/en/stable/api/#flask.request_finished "flask.request_finished") signal is sent.
  19. If any step so far raised an exception, and it was not handled by an error handler function, it is handled now. HTTP exceptions are treated as responses with their corresponding status code, other exceptions are converted to a generic 500 response. The [`got_request_exception`](https://flask.palletsprojects.com/en/stable/api/#flask.got_request_exception "flask.got_request_exception") signal is sent.
  20. The response object’s status, headers, and body are returned to the WSGI server.
  21. Any [`teardown_request()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.teardown_request "flask.Flask.teardown_request") decorated functions are called.
  22. The [`request_tearing_down`](https://flask.palletsprojects.com/en/stable/api/#flask.request_tearing_down "flask.request_tearing_down") signal is sent.
  23. The request context is popped, [`request`](https://flask.palletsprojects.com/en/stable/api/#flask.request "flask.request") and [`session`](https://flask.palletsprojects.com/en/stable/api/#flask.session "flask.session") are no longer available.
  24. Any [`teardown_appcontext()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.teardown_appcontext "flask.Flask.teardown_appcontext") decorated functions are called.
  25. The [`appcontext_tearing_down`](https://flask.palletsprojects.com/en/stable/api/#flask.appcontext_tearing_down "flask.appcontext_tearing_down") signal is sent.
  26. The app context is popped, [`current_app`](https://flask.palletsprojects.com/en/stable/api/#flask.current_app "flask.current_app") and [`g`](https://flask.palletsprojects.com/en/stable/api/#flask.g "flask.g") are no longer available.
  27. The [`appcontext_popped`](https://flask.palletsprojects.com/en/stable/api/#flask.appcontext_popped "flask.appcontext_popped") signal is sent.


There are even more decorators and customization points than this, but that aren’t part of every request lifecycle. They’re more specific to certain things you might use during a request, such as templates, building URLs, or handling JSON data. See the rest of this documentation, as well as the [API](https://flask.palletsprojects.com/en/stable/api/) to explore further.
[ ![Logo of Flask](https://flask.palletsprojects.com/en/stable/_static/flask-logo.svg) ](https://flask.palletsprojects.com/en/stable/)
### Contents
  * [Application Structure and Lifecycle](https://flask.palletsprojects.com/en/stable/lifecycle/)
    * [Application Setup](https://flask.palletsprojects.com/en/stable/lifecycle/#application-setup)
    * [Serving the Application](https://flask.palletsprojects.com/en/stable/lifecycle/#serving-the-application)
      * [Middleware](https://flask.palletsprojects.com/en/stable/lifecycle/#middleware)
    * [How a Request is Handled](https://flask.palletsprojects.com/en/stable/lifecycle/#how-a-request-is-handled)


### Navigation
  * [Overview](https://flask.palletsprojects.com/en/stable/)
    * Previous: [Class-based Views](https://flask.palletsprojects.com/en/stable/views/ "previous chapter")
    * Next: [The Application Context](https://flask.palletsprojects.com/en/stable/appcontext/ "next chapter")


### Quick search
·
![](https://server.ethicalads.io/proxy/view/10134/019ccc1a-4fe4-76f2-9af6-0466d4efaca7/)
© Copyright 2010 Pallets. Created using
