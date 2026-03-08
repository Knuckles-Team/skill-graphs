### Navigation
  * [index](https://flask.palletsprojects.com/en/stable/genindex/ "General Index")
  * [modules](https://flask.palletsprojects.com/en/stable/py-modindex/ "Python Module Index") |
  * [next](https://flask.palletsprojects.com/en/stable/tutorial/templates/ "Templates") |
  * [previous](https://flask.palletsprojects.com/en/stable/tutorial/database/ "Define and Access the Database") |
  * [Flask Documentation (3.1.x)](https://flask.palletsprojects.com/en/stable/) »
  * [Tutorial](https://flask.palletsprojects.com/en/stable/tutorial/) »
  * [Blueprints and Views](https://flask.palletsprojects.com/en/stable/tutorial/views/)


# Blueprints and Views[¶](https://flask.palletsprojects.com/en/stable/tutorial/views/#blueprints-and-views "Link to this heading")
A view function is the code you write to respond to requests to your application. Flask uses patterns to match the incoming request URL to the view that should handle it. The view returns data that Flask turns into an outgoing response. Flask can also go the other direction and generate a URL to a view based on its name and arguments.
## Create a Blueprint[¶](https://flask.palletsprojects.com/en/stable/tutorial/views/#create-a-blueprint "Link to this heading")
A [`Blueprint`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint "flask.Blueprint") is a way to organize a group of related views and other code. Rather than registering views and other code directly with an application, they are registered with a blueprint. Then the blueprint is registered with the application when it is available in the factory function.
Flaskr will have two blueprints, one for authentication functions and one for the blog posts functions. The code for each blueprint will go in a separate module. Since the blog needs to know about authentication, you’ll write the authentication one first.
`flaskr/auth.py`[¶](https://flask.palletsprojects.com/en/stable/tutorial/views/#id1 "Link to this code")
```
import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

```

This creates a [`Blueprint`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint "flask.Blueprint") named `'auth'`. Like the application object, the blueprint needs to know where it’s defined, so `__name__` is passed as the second argument. The `url_prefix` will be prepended to all the URLs associated with the blueprint.
Import and register the blueprint from the factory using [`app.register_blueprint()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.register_blueprint "flask.Flask.register_blueprint"). Place the new code at the end of the factory function before returning the app.
`flaskr/__init__.py`[¶](https://flask.palletsprojects.com/en/stable/tutorial/views/#id2 "Link to this code")
```
def create_app():
    app = ...
    # existing code omitted

    from . import auth
    app.register_blueprint(auth.bp)

    return app

```

The authentication blueprint will have views to register new users and to log in and log out.
## The First View: Register[¶](https://flask.palletsprojects.com/en/stable/tutorial/views/#the-first-view-register "Link to this heading")
When the user visits the `/auth/register` URL, the `register` view will return
For now you will just write the view code. On the next page, you’ll write templates to generate the HTML form.
`flaskr/auth.py`[¶](https://flask.palletsprojects.com/en/stable/tutorial/views/#id3 "Link to this code")
```
@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')

```

Here’s what the `register` view function is doing:
  1. [`@bp.route`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.route "flask.Blueprint.route") associates the URL `/register` with the `register` view function. When Flask receives a request to `/auth/register`, it will call the `register` view and use the return value as the response.
  2. If the user submitted the form, [`request.method`](https://flask.palletsprojects.com/en/stable/api/#flask.Request.method "flask.Request.method") will be `'POST'`. In this case, start validating the input.
  3. [`request.form`](https://flask.palletsprojects.com/en/stable/api/#flask.Request.form "flask.Request.form") is a special type of `username` and `password`.
  4. Validate that `username` and `password` are not empty.
  5. If validation succeeds, insert the new user data into the database.
     * `?` placeholders for any user input, and a tuple of values to replace the placeholders with. The database library will take care of escaping the values so you are not vulnerable to a _SQL injection attack_.
     * For security, passwords should never be stored in the database directly. Instead, [`generate_password_hash()`](https://werkzeug.palletsprojects.com/en/stable/utils/#werkzeug.security.generate_password_hash "\(in Werkzeug v3.1.x\)") is used to securely hash the password, and that hash is stored. Since this query modifies data,
     * An
  6. After storing the user, they are redirected to the login page. [`url_for()`](https://flask.palletsprojects.com/en/stable/api/#flask.url_for "flask.url_for") generates the URL for the login view based on its name. This is preferable to writing the URL directly as it allows you to change the URL later without changing all code that links to it. [`redirect()`](https://flask.palletsprojects.com/en/stable/api/#flask.redirect "flask.redirect") generates a redirect response to the generated URL.
  7. If validation fails, the error is shown to the user. [`flash()`](https://flask.palletsprojects.com/en/stable/api/#flask.flash "flask.flash") stores messages that can be retrieved when rendering the template.
  8. When the user initially navigates to `auth/register`, or there was a validation error, an HTML page with the registration form should be shown. [`render_template()`](https://flask.palletsprojects.com/en/stable/api/#flask.render_template "flask.render_template") will render a template containing the HTML, which you’ll write in the next step of the tutorial.


## Login[¶](https://flask.palletsprojects.com/en/stable/tutorial/views/#login "Link to this heading")
This view follows the same pattern as the `register` view above.
`flaskr/auth.py`[¶](https://flask.palletsprojects.com/en/stable/tutorial/views/#id4 "Link to this code")
```
@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')

```

There are a few differences from the `register` view:
  1. The user is queried first and stored in a variable for later use.
`None`. Later,
  2. [`check_password_hash()`](https://werkzeug.palletsprojects.com/en/stable/utils/#werkzeug.security.check_password_hash "\(in Werkzeug v3.1.x\)") hashes the submitted password in the same way as the stored hash and securely compares them. If they match, the password is valid.
  3. [`session`](https://flask.palletsprojects.com/en/stable/api/#flask.session "flask.session") is a `id` is stored in a new session. The data is stored in a _cookie_ that is sent to the browser, and the browser then sends it back with subsequent requests. Flask securely _signs_ the data so that it can’t be tampered with.


Now that the user’s `id` is stored in the [`session`](https://flask.palletsprojects.com/en/stable/api/#flask.session "flask.session"), it will be available on subsequent requests. At the beginning of each request, if a user is logged in their information should be loaded and made available to other views.
`flaskr/auth.py`[¶](https://flask.palletsprojects.com/en/stable/tutorial/views/#id5 "Link to this code")
```
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()

```

[`bp.before_app_request()`](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.before_app_request "flask.Blueprint.before_app_request") registers a function that runs before the view function, no matter what URL is requested. `load_logged_in_user` checks if a user id is stored in the [`session`](https://flask.palletsprojects.com/en/stable/api/#flask.session "flask.session") and gets that user’s data from the database, storing it on [`g.user`](https://flask.palletsprojects.com/en/stable/api/#flask.g "flask.g"), which lasts for the length of the request. If there is no user id, or if the id doesn’t exist, `g.user` will be `None`.
## Logout[¶](https://flask.palletsprojects.com/en/stable/tutorial/views/#logout "Link to this heading")
To log out, you need to remove the user id from the [`session`](https://flask.palletsprojects.com/en/stable/api/#flask.session "flask.session"). Then `load_logged_in_user` won’t load a user on subsequent requests.
`flaskr/auth.py`[¶](https://flask.palletsprojects.com/en/stable/tutorial/views/#id6 "Link to this code")
```
@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

```

## Require Authentication in Other Views[¶](https://flask.palletsprojects.com/en/stable/tutorial/views/#require-authentication-in-other-views "Link to this heading")
Creating, editing, and deleting blog posts will require a user to be logged in. A _decorator_ can be used to check this for each view it’s applied to.
`flaskr/auth.py`[¶](https://flask.palletsprojects.com/en/stable/tutorial/views/#id7 "Link to this code")
```
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view

```

This decorator returns a new view function that wraps the original view it’s applied to. The new function checks if a user is loaded and redirects to the login page otherwise. If a user is loaded the original view is called and continues normally. You’ll use this decorator when writing the blog views.
## Endpoints and URLs[¶](https://flask.palletsprojects.com/en/stable/tutorial/views/#endpoints-and-urls "Link to this heading")
The [`url_for()`](https://flask.palletsprojects.com/en/stable/api/#flask.url_for "flask.url_for") function generates the URL to a view based on a name and arguments. The name associated with a view is also called the _endpoint_ , and by default it’s the same as the name of the view function.
For example, the `hello()` view that was added to the app factory earlier in the tutorial has the name `'hello'` and can be linked to with `url_for('hello')`. If it took an argument, which you’ll see later, it would be linked to using `url_for('hello', who='World')`.
When using a blueprint, the name of the blueprint is prepended to the name of the function, so the endpoint for the `login` function you wrote above is `'auth.login'` because you added it to the `'auth'` blueprint.
Continue to [Templates](https://flask.palletsprojects.com/en/stable/tutorial/templates/).
[ ![Logo of Flask](https://flask.palletsprojects.com/en/stable/_static/flask-logo.svg) ](https://flask.palletsprojects.com/en/stable/)
### Contents
  * [Blueprints and Views](https://flask.palletsprojects.com/en/stable/tutorial/views/)
    * [Create a Blueprint](https://flask.palletsprojects.com/en/stable/tutorial/views/#create-a-blueprint)
    * [The First View: Register](https://flask.palletsprojects.com/en/stable/tutorial/views/#the-first-view-register)
    * [Login](https://flask.palletsprojects.com/en/stable/tutorial/views/#login)
    * [Logout](https://flask.palletsprojects.com/en/stable/tutorial/views/#logout)
    * [Require Authentication in Other Views](https://flask.palletsprojects.com/en/stable/tutorial/views/#require-authentication-in-other-views)
    * [Endpoints and URLs](https://flask.palletsprojects.com/en/stable/tutorial/views/#endpoints-and-urls)


### Navigation
  * [Overview](https://flask.palletsprojects.com/en/stable/)
    * [Tutorial](https://flask.palletsprojects.com/en/stable/tutorial/)
      * Previous: [Define and Access the Database](https://flask.palletsprojects.com/en/stable/tutorial/database/ "previous chapter")
      * Next: [Templates](https://flask.palletsprojects.com/en/stable/tutorial/templates/ "next chapter")


### Quick search
·
![](https://server.ethicalads.io/proxy/view/10130/019ccc1d-26ae-7191-a808-214dd9f1162d/)
© Copyright 2010 Pallets. Created using
