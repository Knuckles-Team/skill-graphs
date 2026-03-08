### Navigation
  * [index](https://flask.palletsprojects.com/en/stable/genindex/ "General Index")
  * [modules](https://flask.palletsprojects.com/en/stable/py-modindex/ "Python Module Index") |
  * [next](https://flask.palletsprojects.com/en/stable/patterns/subclassing/ "Subclassing Flask") |
  * [previous](https://flask.palletsprojects.com/en/stable/patterns/requestchecksum/ "Request Content Checksums") |
  * [Flask Documentation (3.1.x)](https://flask.palletsprojects.com/en/stable/) »
  * [Patterns for Flask](https://flask.palletsprojects.com/en/stable/patterns/) »
  * [Background Tasks with Celery](https://flask.palletsprojects.com/en/stable/patterns/celery/)


# Background Tasks with Celery[¶](https://flask.palletsprojects.com/en/stable/patterns/celery/#background-tasks-with-celery "Link to this heading")
If your application has a long running task, such as processing some uploaded data or sending email, you don’t want to wait for it to finish during a request. Instead, use a task queue to send the necessary data to another process that will run the task in the background while the request returns immediately.
The Flask repository contains
## Install[¶](https://flask.palletsprojects.com/en/stable/patterns/celery/#install "Link to this heading")
Install Celery from PyPI, for example using pip:
```
$ pip install celery

```

## Integrate Celery with Flask[¶](https://flask.palletsprojects.com/en/stable/patterns/celery/#integrate-celery-with-flask "Link to this heading")
You can use Celery without any integration with Flask, but it’s convenient to configure it through Flask’s config, and to let tasks access the Flask application.
Celery uses similar ideas to Flask, with a `Celery` app object that has configuration and registers tasks. While creating a Flask app, use the following code to create and configure a Celery app as well.
```
from celery import Celery, Task

def celery_init_app(app: Flask) -> Celery:
    class FlaskTask(Task):
        def __call__(self, *args: object, **kwargs: object) -> object:
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_app = Celery(app.name, task_cls=FlaskTask)
    celery_app.config_from_object(app.config["CELERY"])
    celery_app.set_default()
    app.extensions["celery"] = celery_app
    return celery_app

```

This creates and returns a `Celery` app object. Celery `CELERY` key in the Flask configuration. The Celery app is set as the default, so that it is seen during each request. The `Task` subclass automatically runs task functions with a Flask app context active, so that services like your database connections are available.
Here’s a basic `example.py` that configures Celery to use Redis for communication. We enable a result backend, but ignore results by default. This allows us to store results only for tasks where we care about the result.
```
from flask import Flask

app = Flask(__name__)
app.config.from_mapping(
    CELERY=dict(
        broker_url="redis://localhost",
        result_backend="redis://localhost",
        task_ignore_result=True,
    ),
)
celery_app = celery_init_app(app)

```

Point the `celery worker` command at this and it will find the `celery_app` object.
```
$ celery -A example worker --loglevel INFO

```

You can also run the `celery beat` command to run tasks on a schedule. See Celery’s docs for more information about defining schedules.
```
$ celery -A example beat --loglevel INFO

```

## Application Factory[¶](https://flask.palletsprojects.com/en/stable/patterns/celery/#application-factory "Link to this heading")
When using the Flask application factory pattern, call the `celery_init_app` function inside the factory. It sets `app.extensions["celery"]` to the Celery app object, which can be used to get the Celery app from the Flask app returned by the factory.
```
def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_mapping(
        CELERY=dict(
            broker_url="redis://localhost",
            result_backend="redis://localhost",
            task_ignore_result=True,
        ),
    )
    app.config.from_prefixed_env()
    celery_init_app(app)
    return app

```

To use `celery` commands, Celery needs an app object, but that’s no longer directly available. Create a `make_celery.py` file that calls the Flask app factory and gets the Celery app from the returned Flask app.
```
from example import create_app

flask_app = create_app()
celery_app = flask_app.extensions["celery"]

```

Point the `celery` command to this file.
```
$ celery -A make_celery worker --loglevel INFO
$ celery -A make_celery beat --loglevel INFO

```

## Defining Tasks[¶](https://flask.palletsprojects.com/en/stable/patterns/celery/#defining-tasks "Link to this heading")
Using `@celery_app.task` to decorate task functions requires access to the `celery_app` object, which won’t be available when using the factory pattern. It also means that the decorated tasks are tied to the specific Flask and Celery app instances, which could be an issue during testing if you change configuration for a test.
Instead, use Celery’s `@shared_task` decorator. This creates task objects that will access whatever the “current app” is, which is a similar concept to Flask’s blueprints and app context. This is why we called `celery_app.set_default()` above.
Here’s an example task that adds two numbers together and returns the result.
```
from celery import shared_task

@shared_task(ignore_result=False)
def add_together(a: int, b: int) -> int:
    return a + b

```

Earlier, we configured Celery to ignore task results by default. Since we want to know the return value of this task, we set `ignore_result=False`. On the other hand, a task that didn’t need a result, such as sending an email, wouldn’t set this.
## Calling Tasks[¶](https://flask.palletsprojects.com/en/stable/patterns/celery/#calling-tasks "Link to this heading")
The decorated function becomes a task object with methods to call it in the background. The simplest way is to use the `delay(*args, **kwargs)` method. See Celery’s docs for more methods.
A Celery worker must be running to run the task. Starting a worker is shown in the previous sections.
```
from flask import request

@app.post("/add")
def start_add() -> dict[str, object]:
    a = request.form.get("a", type=int)
    b = request.form.get("b", type=int)
    result = add_together.delay(a, b)
    return {"result_id": result.id}

```

The route doesn’t get the task’s result immediately. That would defeat the purpose by blocking the response. Instead, we return the running task’s result id, which we can use later to get the result.
## Getting Results[¶](https://flask.palletsprojects.com/en/stable/patterns/celery/#getting-results "Link to this heading")
To fetch the result of the task we started above, we’ll add another route that takes the result id we returned before. We return whether the task is finished (ready), whether it finished successfully, and what the return value (or error) was if it is finished.
```
from celery.result import AsyncResult

@app.get("/result/<id>")
def task_result(id: str) -> dict[str, object]:
    result = AsyncResult(id)
    return {
        "ready": result.ready(),
        "successful": result.successful(),
        "value": result.result if result.ready() else None,
    }

```

Now you can start the task using the first route, then poll for the result using the second route. This keeps the Flask request workers from being blocked waiting for tasks to finish.
The Flask repository contains
## Passing Data to Tasks[¶](https://flask.palletsprojects.com/en/stable/patterns/celery/#passing-data-to-tasks "Link to this heading")
The “add” task above took two integers as arguments. To pass arguments to tasks, Celery has to serialize them to a format that it can pass to other processes. Therefore, passing complex objects is not recommended. For example, it would be impossible to pass a SQLAlchemy model object, since that object is probably not serializable and is tied to the session that queried it.
Pass the minimal amount of data necessary to fetch or recreate any complex data within the task. Consider a task that will run when the logged in user asks for an archive of their data. The Flask request knows the logged in user, and has the user object queried from the database. It got that by querying the database for a given id, so the task can do the same thing. Pass the user’s id rather than the user object.
```
@shared_task
def generate_user_archive(user_id: str) -> None:
    user = db.session.get(User, user_id)
    ...

generate_user_archive.delay(current_user.id)

```

[ ![Logo of Flask](https://flask.palletsprojects.com/en/stable/_static/flask-logo.svg) ](https://flask.palletsprojects.com/en/stable/)
### Contents
  * [Background Tasks with Celery](https://flask.palletsprojects.com/en/stable/patterns/celery/)
    * [Install](https://flask.palletsprojects.com/en/stable/patterns/celery/#install)
    * [Integrate Celery with Flask](https://flask.palletsprojects.com/en/stable/patterns/celery/#integrate-celery-with-flask)
    * [Application Factory](https://flask.palletsprojects.com/en/stable/patterns/celery/#application-factory)
    * [Defining Tasks](https://flask.palletsprojects.com/en/stable/patterns/celery/#defining-tasks)
    * [Calling Tasks](https://flask.palletsprojects.com/en/stable/patterns/celery/#calling-tasks)
    * [Getting Results](https://flask.palletsprojects.com/en/stable/patterns/celery/#getting-results)
    * [Passing Data to Tasks](https://flask.palletsprojects.com/en/stable/patterns/celery/#passing-data-to-tasks)


### Navigation
  * [Overview](https://flask.palletsprojects.com/en/stable/)
    * [Patterns for Flask](https://flask.palletsprojects.com/en/stable/patterns/)
      * Previous: [Request Content Checksums](https://flask.palletsprojects.com/en/stable/patterns/requestchecksum/ "previous chapter")
      * Next: [Subclassing Flask](https://flask.palletsprojects.com/en/stable/patterns/subclassing/ "next chapter")


### Quick search
·
![](https://server.ethicalads.io/proxy/view/10134/019ccc1a-4fe4-76f2-9af6-0466d4efaca7/)
© Copyright 2010 Pallets. Created using
