## Version 0.3[¶](https://flask.palletsprojects.com/en/stable/changes/#version-0-3 "Link to this heading")
Released 2010-05-28, codename Schnaps
  * Added support for categories for flashed messages.
  * The application now configures a `logging.Handler` and will log request handling exceptions to that logger when not in debug mode. This makes it possible to receive mails on server errors for example.
  * Added support for context binding that does not require the use of the with statement for playing in the console.
  * The request context is now available within the with statement making it possible to further push the request context or pop it.
  * Added support for configurations.
