## Version 0.10.1[¶](https://flask.palletsprojects.com/en/stable/changes/#version-0-10-1 "Link to this heading")
Released 2013-06-14
  * Fixed an issue where `|tojson` was not quoting single quotes which made the filter not work properly in HTML attributes. Now it’s possible to use that filter in single quoted attributes. This should make using that filter with angular.js easier.
  * Added support for byte strings back to the session system. This broke compatibility with the common case of people putting binary data for token verification into the session.
  * Fixed an issue where registering the same method twice for the same endpoint would trigger an exception incorrectly.
