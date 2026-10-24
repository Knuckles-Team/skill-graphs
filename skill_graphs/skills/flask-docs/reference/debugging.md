### Navigation
  * [index](https://flask.palletsprojects.com/en/stable/genindex/ "General Index")
  * [modules](https://flask.palletsprojects.com/en/stable/py-modindex/ "Python Module Index") |
  * [next](https://flask.palletsprojects.com/en/stable/logging/ "Logging") |
  * [previous](https://flask.palletsprojects.com/en/stable/errorhandling/ "Handling Application Errors") |
  * [Flask Documentation (3.1.x)](https://flask.palletsprojects.com/en/stable/) »
  * [Debugging Application Errors](https://flask.palletsprojects.com/en/stable/debugging/)


# Debugging Application Errors[¶](https://flask.palletsprojects.com/en/stable/debugging/#debugging-application-errors "Link to this heading")
## In Production[¶](https://flask.palletsprojects.com/en/stable/debugging/#in-production "Link to this heading")
**Do not run the development server, or enable the built-in debugger, in a production environment.** The debugger allows executing arbitrary Python code from the browser. It’s protected by a pin, but that should not be relied on for security.
Use an error logging tool, such as Sentry, as described in [Error Logging Tools](https://flask.palletsprojects.com/en/stable/errorhandling/#error-logging-tools), or enable logging and notifications as described in [Logging](https://flask.palletsprojects.com/en/stable/logging/).
If you have access to the server, you could add some code to start an external debugger if `request.remote_addr` matches your IP. Some IDE debuggers also have a remote mode so breakpoints on the server can be interacted with locally. Only enable a debugger temporarily.
## The Built-In Debugger[¶](https://flask.palletsprojects.com/en/stable/debugging/#the-built-in-debugger "Link to this heading")
The built-in Werkzeug development server provides a debugger which shows an interactive traceback in the browser when an unhandled error occurs during a request. This debugger should only be used during development.
![screenshot of debugger in action](https://flask.palletsprojects.com/en/stable/_images/debugger.png)
Warning
The debugger allows executing arbitrary Python code from the browser. It is protected by a pin, but still represents a major security risk. Do not run the development server or debugger in a production environment.
The debugger is enabled by default when the development server is run in debug mode.
```
$ flask --app hello run --debug

```

When running from Python code, passing `debug=True` enables debug mode, which is mostly equivalent.
```
app.run(debug=True)

```

[Development Server](https://flask.palletsprojects.com/en/stable/server/) and [Command Line Interface](https://flask.palletsprojects.com/en/stable/cli/) have more information about running the debugger and debug mode. More information about the debugger can be found in the [Werkzeug documentation](https://werkzeug.palletsprojects.com/debug/).
## External Debuggers[¶](https://flask.palletsprojects.com/en/stable/debugging/#external-debuggers "Link to this heading")
External debuggers, such as those provided by IDEs, can offer a more powerful debugging experience than the built-in debugger. They can also be used to step through code during a request before an error is raised, or if no error is raised. Some even have a remote mode so you can debug code running on another machine.
When using an external debugger, the app should still be in debug mode, otherwise Flask turns unhandled errors into generic 500 error pages. However, the built-in debugger and reloader should be disabled so they don’t interfere with the external debugger.
```
$ flask --app hello run --debug --no-debugger --no-reload

```

When running from Python:
```
app.run(debug=True, use_debugger=False, use_reloader=False)

```

Disabling these isn’t required, an external debugger will continue to work with the following caveats.
  * If the built-in debugger is not disabled, it will catch unhandled exceptions before the external debugger can.
  * If the reloader is not disabled, it could cause an unexpected reload if code changes during a breakpoint.
  * The development server will still catch unhandled exceptions if the built-in debugger is disabled, otherwise it would crash on any error. If you want that (and usually you don’t) pass `passthrough_errors=True` to `app.run`.
```
app.run(
    debug=True, passthrough_errors=True,
    use_debugger=False, use_reloader=False
)

```



[ ![Logo of Flask](https://flask.palletsprojects.com/en/stable/_static/flask-logo.svg) ](https://flask.palletsprojects.com/en/stable/)
### Contents
  * [Debugging Application Errors](https://flask.palletsprojects.com/en/stable/debugging/)
    * [In Production](https://flask.palletsprojects.com/en/stable/debugging/#in-production)
    * [The Built-In Debugger](https://flask.palletsprojects.com/en/stable/debugging/#the-built-in-debugger)
    * [External Debuggers](https://flask.palletsprojects.com/en/stable/debugging/#external-debuggers)


### Navigation
  * [Overview](https://flask.palletsprojects.com/en/stable/)
    * Previous: [Handling Application Errors](https://flask.palletsprojects.com/en/stable/errorhandling/ "previous chapter")
    * Next: [Logging](https://flask.palletsprojects.com/en/stable/logging/ "next chapter")


### Quick search
·
![](https://server.ethicalads.io/proxy/view/10132/019ccf13-2a40-7603-93bc-c521e8b0f85c/)
