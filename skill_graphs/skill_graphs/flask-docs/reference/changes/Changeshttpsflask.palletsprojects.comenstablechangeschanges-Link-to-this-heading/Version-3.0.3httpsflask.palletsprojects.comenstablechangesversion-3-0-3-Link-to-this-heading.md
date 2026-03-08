## Version 3.0.3[¶](https://flask.palletsprojects.com/en/stable/changes/#version-3-0-3 "Link to this heading")
Released 2024-04-07
  * The default `hashlib.sha1` may not be available in FIPS builds. Don’t access it at import time so the developer has time to change the default.
  * Don’t initialize the `cli` attribute in the sansio scaffold, but rather in the `Flask` concrete class.
