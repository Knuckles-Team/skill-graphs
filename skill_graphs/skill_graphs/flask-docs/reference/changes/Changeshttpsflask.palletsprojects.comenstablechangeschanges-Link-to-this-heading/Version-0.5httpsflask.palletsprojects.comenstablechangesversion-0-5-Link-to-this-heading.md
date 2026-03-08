## Version 0.5[¶](https://flask.palletsprojects.com/en/stable/changes/#version-0-5 "Link to this heading")
Released 2010-07-06, codename Calvados
  * Fixed a bug with subdomains that was caused by the inability to specify the server name. The server name can now be set with the `SERVER_NAME` config key. This key is now also used to set the session cookie cross-subdomain wide.
  * Autoescaping is no longer active for all templates. Instead it is only active for `.html`, `.htm`, `.xml` and `.xhtml`. Inside templates this behavior can be changed with the `autoescape` tag.
  * Refactored Flask internally. It now consists of more than a single file.
  * `send_file` now emits etags and has the ability to do conditional responses builtin.
  * (temporarily) dropped support for zipped applications. This was a rarely used feature and led to some confusing behavior.
  * Added support for per-package template and static-file directories.
  * Removed support for `create_jinja_loader` which is no longer used in 0.5 due to the improved module support.
  * Added a helper function to expose files from any directory.
