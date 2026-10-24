## Class-Based Views[¶](https://flask.palletsprojects.com/en/stable/api/#class-based-views "Link to this heading")
Changelog
Added in version 0.7.

_class_ flask.views.View[¶](https://flask.palletsprojects.com/en/stable/api/#flask.views.View "Link to this definition")

Subclass this class and override [`dispatch_request()`](https://flask.palletsprojects.com/en/stable/api/#flask.views.View.dispatch_request "flask.views.View.dispatch_request") to create a generic class-based view. Call [`as_view()`](https://flask.palletsprojects.com/en/stable/api/#flask.views.View.as_view "flask.views.View.as_view") to create a view function that creates an instance of the class with the given arguments and calls its `dispatch_request` method with any URL variables.
See [Class-based Views](https://flask.palletsprojects.com/en/stable/views/) for a detailed guide.
```
class Hello(View):
    init_every_request = False

    def dispatch_request(self, name):
        return f"Hello, {name}!"

app.add_url_rule(
    "/hello/<name>", view_func=Hello.as_view("hello")
)

```

Set [`methods`](https://flask.palletsprojects.com/en/stable/api/#flask.views.View.methods "flask.views.View.methods") on the class to change what methods the view accepts.
Set [`decorators`](https://flask.palletsprojects.com/en/stable/api/#flask.views.View.decorators "flask.views.View.decorators") on the class to apply a list of decorators to the generated view function. Decorators applied to the class itself will not be applied to the generated view function!
Set [`init_every_request`](https://flask.palletsprojects.com/en/stable/api/#flask.views.View.init_every_request "flask.views.View.init_every_request") to `False` for efficiency, unless you need to store request-global data on `self`.

methods _:[[]|]__= None_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.views.View.methods "Link to this definition")

The methods this view is registered for. Uses the same default (`["GET", "HEAD", "OPTIONS"]`) as `route` and `add_url_rule` by default.

provide_automatic_options _:[|]__= None_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.views.View.provide_automatic_options "Link to this definition")

Control whether the `OPTIONS` method is handled automatically. Uses the same default (`True`) as `route` and `add_url_rule` by default.

decorators _:[[[[...],]]]__=[]_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.views.View.decorators "Link to this definition")

A list of decorators to apply, in order, to the generated view function. Remember that `@decorator` syntax is applied bottom to top, so the first decorator in the list would be the bottom decorator.
Changelog
Added in version 0.8.

init_every_request _:[]__= True_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.views.View.init_every_request "Link to this definition")

Create a new instance of this view class for every request by default. If a view subclass sets this to `False`, the same instance is used for every request.
A single instance is more efficient, especially if complex setup is done during init. However, storing data on `self` is no longer safe across requests, and [`g`](https://flask.palletsprojects.com/en/stable/api/#flask.g "flask.g") should be used instead.
Changelog
Added in version 2.2.

dispatch_request()[¶](https://flask.palletsprojects.com/en/stable/api/#flask.views.View.dispatch_request "Link to this definition")

The actual view function behavior. Subclasses must override this and return a valid response. Any variables from the URL rule are passed as keyword arguments.

Return type:

ft.ResponseReturnValue

_classmethod_ as_view(_name_ , _* class_args_, _** class_kwargs_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.views.View.as_view "Link to this definition")

Convert the class into a view function that can be registered for a route.
By default, the generated view will create a new instance of the view class for every request and call its [`dispatch_request()`](https://flask.palletsprojects.com/en/stable/api/#flask.views.View.dispatch_request "flask.views.View.dispatch_request") method. If the view class sets [`init_every_request`](https://flask.palletsprojects.com/en/stable/api/#flask.views.View.init_every_request "flask.views.View.init_every_request") to `False`, the same instance will be used for every request.
Except for `name`, all other arguments passed to this method are forwarded to the view class `__init__` method.
Changelog
Changed in version 2.2: Added the `init_every_request` class attribute.

Parameters:

  * **name** (
  * **class_args** (_t.Any_)
  * **class_kwargs** (_t.Any_)



Return type:

ft.RouteCallable

_class_ flask.views.MethodView[¶](https://flask.palletsprojects.com/en/stable/api/#flask.views.MethodView "Link to this definition")

Dispatches request methods to the corresponding instance methods. For example, if you implement a `get` method, it will be used to handle `GET` requests.
This can be useful for defining a REST API.
`methods` is automatically set based on the methods defined on the class.
See [Class-based Views](https://flask.palletsprojects.com/en/stable/views/) for a detailed guide.
```
class CounterAPI(MethodView):
    def get(self):
        return str(session.get("counter", 0))

    def post(self):
        session["counter"] = session.get("counter", 0) + 1
        return redirect(url_for("counter"))

app.add_url_rule(
    "/counter", view_func=CounterAPI.as_view("counter")
)

```


dispatch_request(_** kwargs_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.views.MethodView.dispatch_request "Link to this definition")

The actual view function behavior. Subclasses must override this and return a valid response. Any variables from the URL rule are passed as keyword arguments.

Parameters:

**kwargs** (_t.Any_)

Return type:

ft.ResponseReturnValue
