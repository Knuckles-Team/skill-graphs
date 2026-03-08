### Navigation
  * [index](https://flask.palletsprojects.com/en/stable/genindex/ "General Index")
  * [modules](https://flask.palletsprojects.com/en/stable/py-modindex/ "Python Module Index") |
  * [next](https://flask.palletsprojects.com/en/stable/shell/ "Working with the Shell") |
  * [previous](https://flask.palletsprojects.com/en/stable/cli/ "Command Line Interface") |
  * [Flask Documentation (3.1.x)](https://flask.palletsprojects.com/en/stable/) »
  * [Development Server](https://flask.palletsprojects.com/en/stable/server/)


# Development Server[¶](https://flask.palletsprojects.com/en/stable/server/#development-server "Link to this heading")
Flask provides a `run` command to run the application with a development server. In debug mode, this server provides an interactive debugger and will reload when code is changed.
Warning
Do not use the development server when deploying to production. It is intended for use only during local development. It is not designed to be particularly efficient, stable, or secure.
See [Deploying to Production](https://flask.palletsprojects.com/en/stable/deploying/) for deployment options.
## Command Line[¶](https://flask.palletsprojects.com/en/stable/server/#command-line "Link to this heading")
The `flask run` CLI command is the recommended way to run the development server. Use the `--app` option to point to your application, and the `--debug` option to enable debug mode.
```
$ flask --app hello run --debug

```

This enables debug mode, including the interactive debugger and reloader, and then starts the server on `flask run --help` to see the available options, and [Command Line Interface](https://flask.palletsprojects.com/en/stable/cli/) for detailed instructions about configuring and using the CLI.
### Address already in use[¶](https://flask.palletsprojects.com/en/stable/server/#address-already-in-use "Link to this heading")
If another program is already using port 5000, you’ll see an `OSError` when the server tries to start. It may have one of the following messages:
  * `OSError: [Errno 98] Address already in use`
  * `OSError: [WinError 10013] An attempt was made to access a socket in a way forbidden by its access permissions`


Either identify and stop the other program, or use `flask run --port 5001` to pick a different port.
You can use `netstat` or `lsof` to identify what process id is using a port, then use other operating system tools stop that process. The following example shows that process id 6847 is using port 5000.
`netstat` (Linux)`lsof` (macOS / Linux)`netstat` (Windows)
```
$ netstat -nlp | grep 5000
tcp 0 0 127.0.0.1:5000 0.0.0.0:* LISTEN 6847/python

```

```
$ lsof -P -i :5000
Python 6847 IPv4 TCP localhost:5000 (LISTEN)

```

```
> netstat -ano | findstr 5000
TCP 127.0.0.1:5000 0.0.0.0:0 LISTENING 6847

```

macOS Monterey and later automatically starts a service that uses port 5000. You can choose to disable this service instead of using a different port by searching for “AirPlay Receiver” in System Settings and toggling it off.
### Deferred Errors on Reload[¶](https://flask.palletsprojects.com/en/stable/server/#deferred-errors-on-reload "Link to this heading")
When using the `flask run` command with the reloader, the server will continue to run even if you introduce syntax errors or other initialization errors into the code. Accessing the site will show the interactive debugger for the error, rather than crashing the server.
If a syntax error is already present when calling `flask run`, it will fail immediately and show the traceback rather than waiting until the site is accessed. This is intended to make errors more visible initially while still allowing the server to handle errors on reload.
## In Code[¶](https://flask.palletsprojects.com/en/stable/server/#in-code "Link to this heading")
The development server can also be started from Python with the [`Flask.run()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.run "flask.Flask.run") method. This method takes arguments similar to the CLI options to control the server. The main difference from the CLI command is that the server will crash if there are errors when reloading. `debug=True` can be passed to enable debug mode.
Place the call in a main block, otherwise it will interfere when trying to import and run the application with a production server later.
```
if __name__ == "__main__":
    app.run(debug=True)

```

```
$ python hello.py

```

[ ![Logo of Flask](https://flask.palletsprojects.com/en/stable/_static/flask-logo.svg) ](https://flask.palletsprojects.com/en/stable/)
### Contents
  * [Development Server](https://flask.palletsprojects.com/en/stable/server/)
    * [Command Line](https://flask.palletsprojects.com/en/stable/server/#command-line)
      * [Address already in use](https://flask.palletsprojects.com/en/stable/server/#address-already-in-use)
      * [Deferred Errors on Reload](https://flask.palletsprojects.com/en/stable/server/#deferred-errors-on-reload)
    * [In Code](https://flask.palletsprojects.com/en/stable/server/#in-code)


### Navigation
  * [Overview](https://flask.palletsprojects.com/en/stable/)
    * Previous: [Command Line Interface](https://flask.palletsprojects.com/en/stable/cli/ "previous chapter")
    * Next: [Working with the Shell](https://flask.palletsprojects.com/en/stable/shell/ "next chapter")


### Quick search
·
![](https://server.ethicalads.io/proxy/view/10130/019ccc1c-813e-73f1-a9a8-2807ee73f037/)
