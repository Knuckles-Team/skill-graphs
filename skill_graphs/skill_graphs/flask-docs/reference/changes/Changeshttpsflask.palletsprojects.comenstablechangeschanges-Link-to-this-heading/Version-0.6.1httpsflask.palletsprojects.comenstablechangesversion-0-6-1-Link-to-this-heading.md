## Version 0.6.1[¶](https://flask.palletsprojects.com/en/stable/changes/#version-0-6-1 "Link to this heading")
Released 2010-12-31
  * Fixed an issue where the default `OPTIONS` response was not exposing all valid methods in the `Allow` header.
  * Jinja template loading syntax now allows “./” in front of a template load path. Previously this caused issues with module setups.
  * Fixed an issue where the subdomain setting for modules was ignored for the static folder.
  * Fixed a security problem that allowed clients to download arbitrary files if the host server was a windows based operating system and the client uses backslashes to escape the directory the files where exposed from.
