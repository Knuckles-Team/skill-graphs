### Navigation
  * [index](https://flask.palletsprojects.com/en/stable/genindex/ "General Index")
  * [modules](https://flask.palletsprojects.com/en/stable/py-modindex/ "Python Module Index") |
  * [next](https://flask.palletsprojects.com/en/stable/config/ "Configuration Handling") |
  * [previous](https://flask.palletsprojects.com/en/stable/debugging/ "Debugging Application Errors") |
  * [Flask Documentation (3.1.x)](https://flask.palletsprojects.com/en/stable/) »
  * [Logging](https://flask.palletsprojects.com/en/stable/logging/)


# Logging[¶](https://flask.palletsprojects.com/en/stable/logging/#logging "Link to this heading")
Flask uses standard Python [`app.logger`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.logger "flask.Flask.logger"), which takes the same name as [`app.name`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.name "flask.Flask.name"). This logger can also be used to log your own messages.
```
@app.route('/login', methods=['POST'])
def login():
    user = get_user(request.form['username'])

    if user.check_password(request.form['password']):
        login_user(user)
        app.logger.info('%s logged in successfully', user.username)
        return redirect(url_for('index'))
    else:
        app.logger.info('%s failed to log in', user.username)
        abort(401)

```

If you don’t configure logging, Python’s default log level is usually ‘warning’. Nothing below the configured level will be visible.
## Basic Configuration[¶](https://flask.palletsprojects.com/en/stable/logging/#basic-configuration "Link to this heading")
When you want to configure logging for your project, you should do it as soon as possible when the program starts. If [`app.logger`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.logger "flask.Flask.logger") is accessed before logging is configured, it will add a default handler. If possible, configure logging before creating the application object.
This example uses
```
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)

```

### Default Configuration[¶](https://flask.palletsprojects.com/en/stable/logging/#default-configuration "Link to this heading")
If you do not configure logging yourself, Flask will add a [`app.logger`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.logger "flask.Flask.logger") automatically. During requests, it will write to the stream specified by the WSGI server in `environ['wsgi.errors']` (which is usually
### Removing the Default Handler[¶](https://flask.palletsprojects.com/en/stable/logging/#removing-the-default-handler "Link to this heading")
If you configured logging after accessing [`app.logger`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.logger "flask.Flask.logger"), and need to remove the default handler, you can import and remove it:
```
from flask.logging import default_handler

app.logger.removeHandler(default_handler)

```

## Email Errors to Admins[¶](https://flask.palletsprojects.com/en/stable/logging/#email-errors-to-admins "Link to this heading")
When running the application on a remote server for production, you probably won’t be looking at the log messages very often. The WSGI server will probably send log messages to a file, and you’ll only check that file if a user tells you something went wrong.
To be proactive about discovering and fixing bugs, you can configure a
```
import logging
from logging.handlers import SMTPHandler

mail_handler = SMTPHandler(
    mailhost='127.0.0.1',
    fromaddr='server-error@example.com',
    toaddrs=['admin@example.com'],
    subject='Application Error'
)
mail_handler.setLevel(logging.ERROR)
mail_handler.setFormatter(logging.Formatter(
    '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
))

if not app.debug:
    app.logger.addHandler(mail_handler)

```

This requires that you have an SMTP server set up on the same server. See the Python docs for more information about configuring the handler.
## Injecting Request Information[¶](https://flask.palletsprojects.com/en/stable/logging/#injecting-request-information "Link to this heading")
Seeing more information about the request, such as the IP address, may help debugging some errors. You can subclass
```
from flask import has_request_context, request
from flask.logging import default_handler

class RequestFormatter(logging.Formatter):
    def format(self, record):
        if has_request_context():
            record.url = request.url
            record.remote_addr = request.remote_addr
        else:
            record.url = None
            record.remote_addr = None

        return super().format(record)

formatter = RequestFormatter(
    '[%(asctime)s] %(remote_addr)s requested %(url)s\n'
    '%(levelname)s in %(module)s: %(message)s'
)
default_handler.setFormatter(formatter)
mail_handler.setFormatter(formatter)

```

## Other Libraries[¶](https://flask.palletsprojects.com/en/stable/logging/#other-libraries "Link to this heading")
Other libraries may use logging extensively, and you want to see relevant messages from those logs too. The simplest way to do this is to add handlers to the root logger instead of only the app logger.
```
from flask.logging import default_handler

root = logging.getLogger()
root.addHandler(default_handler)
root.addHandler(mail_handler)

```

Depending on your project, it may be more useful to configure each logger you care about separately, instead of configuring only the root logger.
```
for logger in (
    logging.getLogger(app.name),
    logging.getLogger('sqlalchemy'),
    logging.getLogger('other_package'),
):
    logger.addHandler(default_handler)
    logger.addHandler(mail_handler)

```

### Werkzeug[¶](https://flask.palletsprojects.com/en/stable/logging/#werkzeug "Link to this heading")
Werkzeug logs basic request/response information to the `'werkzeug'` logger. If the root logger has no handlers configured, Werkzeug adds a
### Flask Extensions[¶](https://flask.palletsprojects.com/en/stable/logging/#flask-extensions "Link to this heading")
Depending on the situation, an extension may choose to log to [`app.logger`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.logger "flask.Flask.logger") or its own named logger. Consult each extension’s documentation for details.
[ ![Logo of Flask](https://flask.palletsprojects.com/en/stable/_static/flask-logo.svg) ](https://flask.palletsprojects.com/en/stable/)
### Contents
  * [Logging](https://flask.palletsprojects.com/en/stable/logging/)
    * [Basic Configuration](https://flask.palletsprojects.com/en/stable/logging/#basic-configuration)
      * [Default Configuration](https://flask.palletsprojects.com/en/stable/logging/#default-configuration)
      * [Removing the Default Handler](https://flask.palletsprojects.com/en/stable/logging/#removing-the-default-handler)
    * [Email Errors to Admins](https://flask.palletsprojects.com/en/stable/logging/#email-errors-to-admins)
    * [Injecting Request Information](https://flask.palletsprojects.com/en/stable/logging/#injecting-request-information)
    * [Other Libraries](https://flask.palletsprojects.com/en/stable/logging/#other-libraries)
      * [Werkzeug](https://flask.palletsprojects.com/en/stable/logging/#werkzeug)
      * [Flask Extensions](https://flask.palletsprojects.com/en/stable/logging/#flask-extensions)


### Navigation
  * [Overview](https://flask.palletsprojects.com/en/stable/)
    * Previous: [Debugging Application Errors](https://flask.palletsprojects.com/en/stable/debugging/ "previous chapter")
    * Next: [Configuration Handling](https://flask.palletsprojects.com/en/stable/config/ "next chapter")


### Quick search
·
![](https://server.ethicalads.io/proxy/view/10134/019ccc1a-4fe4-76f2-9af6-0466d4efaca7/)
© Copyright 2010 Pallets. Created using
