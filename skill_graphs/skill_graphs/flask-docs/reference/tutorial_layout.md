### Navigation
  * [index](https://flask.palletsprojects.com/en/stable/genindex/ "General Index")
  * [modules](https://flask.palletsprojects.com/en/stable/py-modindex/ "Python Module Index") |
  * [next](https://flask.palletsprojects.com/en/stable/tutorial/factory/ "Application Setup") |
  * [previous](https://flask.palletsprojects.com/en/stable/tutorial/ "Tutorial") |
  * [Flask Documentation (3.1.x)](https://flask.palletsprojects.com/en/stable/) »
  * [Tutorial](https://flask.palletsprojects.com/en/stable/tutorial/) »
  * [Project Layout](https://flask.palletsprojects.com/en/stable/tutorial/layout/)


# Project Layout[¶](https://flask.palletsprojects.com/en/stable/tutorial/layout/#project-layout "Link to this heading")
Create a project directory and enter it:
```
$ mkdir flask-tutorial
$ cd flask-tutorial

```

Then follow the [installation instructions](https://flask.palletsprojects.com/en/stable/installation/) to set up a Python virtual environment and install Flask for your project.
The tutorial will assume you’re working from the `flask-tutorial` directory from now on. The file names at the top of each code block are relative to this directory.
* * *
A Flask application can be as simple as a single file.
`hello.py`[¶](https://flask.palletsprojects.com/en/stable/tutorial/layout/#id1 "Link to this code")
```
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

```

However, as a project gets bigger, it becomes overwhelming to keep all the code in one file. Python projects use _packages_ to organize code into multiple modules that can be imported where needed, and the tutorial will do this as well.
The project directory will contain:
  * `flaskr/`, a Python package containing your application code and files.
  * `tests/`, a directory containing test modules.
  * `.venv/`, a Python virtual environment where Flask and other dependencies are installed.
  * Installation files telling Python how to install your project.
  * Version control config, such as
  * Any other project files you might add in the future.


By the end, your project layout will look like this:
```
/home/user/Projects/flask-tutorial
├── flaskr/
│   ├── __init__.py
│   ├── db.py
│   ├── schema.sql
│   ├── auth.py
│   ├── blog.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   └── blog/
│   │       ├── create.html
│   │       ├── index.html
│   │       └── update.html
│   └── static/
│       └── style.css
├── tests/
│   ├── conftest.py
│   ├── data.sql
│   ├── test_factory.py
│   ├── test_db.py
│   ├── test_auth.py
│   └── test_blog.py
├── .venv/
├── pyproject.toml
└── MANIFEST.in

```

If you’re using version control, the following files that are generated while running your project should be ignored. There may be other files based on the editor you use. In general, ignore files that you didn’t write. For example, with git:
`.gitignore`[¶](https://flask.palletsprojects.com/en/stable/tutorial/layout/#id2 "Link to this code")
```
.venv/

*.pyc
__pycache__/

instance/

.pytest_cache/
.coverage
htmlcov/

dist/
build/
*.egg-info/

```

Continue to [Application Setup](https://flask.palletsprojects.com/en/stable/tutorial/factory/).
[ ![Logo of Flask](https://flask.palletsprojects.com/en/stable/_static/flask-logo.svg) ](https://flask.palletsprojects.com/en/stable/)
### Navigation
  * [Overview](https://flask.palletsprojects.com/en/stable/)
    * [Tutorial](https://flask.palletsprojects.com/en/stable/tutorial/)
      * Previous: [Tutorial](https://flask.palletsprojects.com/en/stable/tutorial/ "previous chapter")
      * Next: [Application Setup](https://flask.palletsprojects.com/en/stable/tutorial/factory/ "next chapter")


### Quick search
·
![](https://server.ethicalads.io/proxy/view/10130/019ccc1d-26ae-7191-a808-214dd9f1162d/)
