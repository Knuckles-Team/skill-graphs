### Navigation
  * [index](https://flask.palletsprojects.com/en/stable/genindex/ "General Index")
  * [modules](https://flask.palletsprojects.com/en/stable/py-modindex/ "Python Module Index") |
  * [next](https://flask.palletsprojects.com/en/stable/tutorial/views/ "Blueprints and Views") |
  * [previous](https://flask.palletsprojects.com/en/stable/tutorial/factory/ "Application Setup") |
  * [Flask Documentation (3.1.x)](https://flask.palletsprojects.com/en/stable/) »
  * [Tutorial](https://flask.palletsprojects.com/en/stable/tutorial/) »
  * [Define and Access the Database](https://flask.palletsprojects.com/en/stable/tutorial/database/)


# Define and Access the Database[¶](https://flask.palletsprojects.com/en/stable/tutorial/database/#define-and-access-the-database "Link to this heading")
The application will use a
SQLite is convenient because it doesn’t require setting up a separate database server and is built-in to Python. However, if concurrent requests try to write to the database at the same time, they will slow down as each write happens sequentially. Small applications won’t notice this. Once you become big, you may want to switch to a different database.
The tutorial doesn’t go into detail about SQL. If you are not familiar with it, the SQLite docs describe the
## Connect to the Database[¶](https://flask.palletsprojects.com/en/stable/tutorial/database/#connect-to-the-database "Link to this heading")
The first thing to do when working with a SQLite database (and most other Python database libraries) is to create a connection to it. Any queries and operations are performed using the connection, which is closed after the work is finished.
In web applications this connection is typically tied to the request. It is created at some point when handling a request, and closed before the response is sent.
`flaskr/db.py`[¶](https://flask.palletsprojects.com/en/stable/tutorial/database/#id1 "Link to this code")
```
import sqlite3
from datetime import datetime

import click
from flask import current_app, g


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

```

[`g`](https://flask.palletsprojects.com/en/stable/api/#flask.g "flask.g") is a special object that is unique for each request. It is used to store data that might be accessed by multiple functions during the request. The connection is stored and reused instead of creating a new connection if `get_db` is called a second time in the same request.
[`current_app`](https://flask.palletsprojects.com/en/stable/api/#flask.current_app "flask.current_app") is another special object that points to the Flask application handling the request. Since you used an application factory, there is no application object when writing the rest of your code. `get_db` will be called when the application has been created and is handling a request, so [`current_app`](https://flask.palletsprojects.com/en/stable/api/#flask.current_app "flask.current_app") can be used.
`DATABASE` configuration key. This file doesn’t have to exist yet, and won’t until you initialize the database later.
`close_db` checks if a connection was created by checking if `g.db` was set. If the connection exists, it is closed. Further down you will tell your application about the `close_db` function in the application factory so that it is called after each request.
## Create the Tables[¶](https://flask.palletsprojects.com/en/stable/tutorial/database/#create-the-tables "Link to this heading")
In SQLite, data is stored in _tables_ and _columns_. These need to be created before you can store and retrieve data. Flaskr will store users in the `user` table, and posts in the `post` table. Create a file with the SQL commands needed to create empty tables:
`flaskr/schema.sql`[¶](https://flask.palletsprojects.com/en/stable/tutorial/database/#id2 "Link to this code")
```
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);

```

Add the Python functions that will run these SQL commands to the `db.py` file:
`flaskr/db.py`[¶](https://flask.palletsprojects.com/en/stable/tutorial/database/#id3 "Link to this code")
```
def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


sqlite3.register_converter(
    "timestamp", lambda v: datetime.fromisoformat(v.decode())
)

```

[`open_resource()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.open_resource "flask.Flask.open_resource") opens a file relative to the `flaskr` package, which is useful since you won’t necessarily know where that location is when deploying the application later. `get_db` returns a database connection, which is used to execute the commands read from the file.
[`click.command()`](https://click.palletsprojects.com/en/stable/api/#click.command "\(in Click v8.3.x\)") defines a command line command called `init-db` that calls the `init_db` function and shows a success message to the user. You can read [Command Line Interface](https://flask.palletsprojects.com/en/stable/cli/) to learn more about writing commands.
The call to
## Register with the Application[¶](https://flask.palletsprojects.com/en/stable/tutorial/database/#register-with-the-application "Link to this heading")
The `close_db` and `init_db_command` functions need to be registered with the application instance; otherwise, they won’t be used by the application. However, since you’re using a factory function, that instance isn’t available when writing the functions. Instead, write a function that takes an application and does the registration.
`flaskr/db.py`[¶](https://flask.palletsprojects.com/en/stable/tutorial/database/#id4 "Link to this code")
```
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

```

[`app.teardown_appcontext()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.teardown_appcontext "flask.Flask.teardown_appcontext") tells Flask to call that function when cleaning up after returning the response.
[`app.cli.add_command()`](https://click.palletsprojects.com/en/stable/api/#click.Group.add_command "\(in Click v8.3.x\)") adds a new command that can be called with the `flask` command.
Import and call this function from the factory. Place the new code at the end of the factory function before returning the app.
`flaskr/__init__.py`[¶](https://flask.palletsprojects.com/en/stable/tutorial/database/#id5 "Link to this code")
```
def create_app():
    app = ...
    # existing code omitted

    from . import db
    db.init_app(app)

    return app

```

## Initialize the Database File[¶](https://flask.palletsprojects.com/en/stable/tutorial/database/#initialize-the-database-file "Link to this heading")
Now that `init-db` has been registered with the app, it can be called using the `flask` command, similar to the `run` command from the previous page.
Note
If you’re still running the server from the previous page, you can either stop the server, or run this command in a new terminal. If you use a new terminal, remember to change to your project directory and activate the env as described in [Installation](https://flask.palletsprojects.com/en/stable/installation/).
Run the `init-db` command:
```
$ flask --app flaskr init-db
Initialized the database.

```

There will now be a `flaskr.sqlite` file in the `instance` folder in your project.
Continue to [Blueprints and Views](https://flask.palletsprojects.com/en/stable/tutorial/views/).
[ ![Logo of Flask](https://flask.palletsprojects.com/en/stable/_static/flask-logo.svg) ](https://flask.palletsprojects.com/en/stable/)
### Contents
  * [Define and Access the Database](https://flask.palletsprojects.com/en/stable/tutorial/database/)
    * [Connect to the Database](https://flask.palletsprojects.com/en/stable/tutorial/database/#connect-to-the-database)
    * [Create the Tables](https://flask.palletsprojects.com/en/stable/tutorial/database/#create-the-tables)
    * [Register with the Application](https://flask.palletsprojects.com/en/stable/tutorial/database/#register-with-the-application)
    * [Initialize the Database File](https://flask.palletsprojects.com/en/stable/tutorial/database/#initialize-the-database-file)


### Navigation
  * [Overview](https://flask.palletsprojects.com/en/stable/)
    * [Tutorial](https://flask.palletsprojects.com/en/stable/tutorial/)
      * Previous: [Application Setup](https://flask.palletsprojects.com/en/stable/tutorial/factory/ "previous chapter")
      * Next: [Blueprints and Views](https://flask.palletsprojects.com/en/stable/tutorial/views/ "next chapter")


### Quick search
·
![](https://server.ethicalads.io/proxy/view/10130/019ccc1c-813e-73f1-a9a8-2807ee73f037/)
© Copyright 2010 Pallets. Created using
