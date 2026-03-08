### Navigation
  * [index](https://flask.palletsprojects.com/en/stable/genindex/ "General Index")
  * [modules](https://flask.palletsprojects.com/en/stable/py-modindex/ "Python Module Index") |
  * [next](https://flask.palletsprojects.com/en/stable/patterns/appfactories/ "Application Factories") |
  * [previous](https://flask.palletsprojects.com/en/stable/patterns/ "Patterns for Flask") |
  * [Flask Documentation (3.1.x)](https://flask.palletsprojects.com/en/stable/) »
  * [Patterns for Flask](https://flask.palletsprojects.com/en/stable/patterns/) »
  * [Large Applications as Packages](https://flask.palletsprojects.com/en/stable/patterns/packages/)


# Large Applications as Packages[¶](https://flask.palletsprojects.com/en/stable/patterns/packages/#large-applications-as-packages "Link to this heading")
Imagine a simple flask application structure that looks like this:
```
/yourapplication
    yourapplication.py
    /static
        style.css
    /templates
        layout.html
        index.html
        login.html
        ...

```

While this is fine for small applications, for larger applications it’s a good idea to use a package instead of a module. The [Tutorial](https://flask.palletsprojects.com/en/stable/tutorial/) is structured to use the package pattern, see the
## Simple Packages[¶](https://flask.palletsprojects.com/en/stable/patterns/packages/#simple-packages "Link to this heading")
To convert that into a larger one, just create a new folder `yourapplication` inside the existing one and move everything below it. Then rename `yourapplication.py` to `__init__.py`. (Make sure to delete all `.pyc` files first, otherwise things would most likely break)
You should then end up with something like that:
```
/yourapplication
    /yourapplication
        __init__.py
        /static
            style.css
        /templates
            layout.html
            index.html
            login.html
            ...

```

But how do you run your application now? The naive `python yourapplication/__init__.py` will not work. Let’s just say that Python does not want modules in packages to be the startup file. But that is not a big problem, just add a new file called `pyproject.toml` next to the inner `yourapplication` folder with the following contents:
```
[project]
name = "yourapplication"
dependencies = [
    "flask",
]

[build-system]
requires = ["flit_core<4"]
build-backend = "flit_core.buildapi"

```

Install your application so it is importable:
```
$ pip install -e .

```

To use the `flask` command and run your application you need to set the `--app` option that tells Flask where to find the application instance:
```
$ flask --app yourapplication run

```

What did we gain from this? Now we can restructure the application a bit into multiple modules. The only thing you have to remember is the following quick checklist:
  1. the `Flask` application object creation has to be in the `__init__.py` file. That way each module can import it safely and the `__name__` variable will resolve to the correct package.
  2. all the view functions (the ones with a [`route()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.route "flask.Flask.route") decorator on top) have to be imported in the `__init__.py` file. Not the object itself, but the module it is in. Import the view module **after the application object is created**.


Here’s an example `__init__.py`:
```
from flask import Flask
app = Flask(__name__)

import yourapplication.views

```

And this is what `views.py` would look like:
```
from yourapplication import app

@app.route('/')
def index():
    return 'Hello World!'

```

You should then end up with something like that:
```
/yourapplication
    pyproject.toml
    /yourapplication
        __init__.py
        views.py
        /static
            style.css
        /templates
            layout.html
            index.html
            login.html
            ...

```

Circular Imports
Every Python programmer hates them, and yet we just added some: circular imports (That’s when two modules depend on each other. In this case `views.py` depends on `__init__.py`). Be advised that this is a bad idea in general but here it is actually fine. The reason for this is that we are not actually using the views in `__init__.py` and just ensuring the module is imported and we are doing that at the bottom of the file.
## Working with Blueprints[¶](https://flask.palletsprojects.com/en/stable/patterns/packages/#working-with-blueprints "Link to this heading")
If you have larger applications it’s recommended to divide them into smaller groups where each group is implemented with the help of a blueprint. For a gentle introduction into this topic refer to the [Modular Applications with Blueprints](https://flask.palletsprojects.com/en/stable/blueprints/) chapter of the documentation.
[ ![Logo of Flask](https://flask.palletsprojects.com/en/stable/_static/flask-logo.svg) ](https://flask.palletsprojects.com/en/stable/)
### Contents
  * [Large Applications as Packages](https://flask.palletsprojects.com/en/stable/patterns/packages/)
    * [Simple Packages](https://flask.palletsprojects.com/en/stable/patterns/packages/#simple-packages)
    * [Working with Blueprints](https://flask.palletsprojects.com/en/stable/patterns/packages/#working-with-blueprints)


### Navigation
  * [Overview](https://flask.palletsprojects.com/en/stable/)
    * [Patterns for Flask](https://flask.palletsprojects.com/en/stable/patterns/)
      * Previous: [Patterns for Flask](https://flask.palletsprojects.com/en/stable/patterns/ "previous chapter")
      * Next: [Application Factories](https://flask.palletsprojects.com/en/stable/patterns/appfactories/ "next chapter")


### Quick search
·
![](https://server.ethicalads.io/proxy/view/10129/019ccc1a-a6f3-7fb3-acbb-e7aba1d739fd/)
© Copyright 2010 Pallets. Created using
