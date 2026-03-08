## Version 0.2[¶](https://flask.palletsprojects.com/en/stable/changes/#version-0-2 "Link to this heading")
Released 2010-05-12, codename J?germeister
  * Various bugfixes
  * Integrated JSON support
  * Added `get_template_attribute` helper function.
  * `Flask.add_url_rule` can now also register a view function.
  * Refactored internal request dispatching.
  * Server listens on 127.0.0.1 by default now to fix issues with chrome.
  * Added external URL support.
  * Added support for `send_file`.
  * Module support and internal request handling refactoring to better support pluggable applications.
  * Sessions can be set to be permanent now on a per-session basis.
  * Better error reporting on missing secret keys.
  * Added support for Google Appengine.
