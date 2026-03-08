## Version 3.1.0[¶](https://flask.palletsprojects.com/en/stable/changes/#version-3-1-0 "Link to this heading")
Released 2024-11-13
  * Drop support for Python 3.8.
  * Update minimum dependency versions to latest feature releases. Werkzeug >= 3.1, ItsDangerous >= 2.2, Blinker >= 1.9.
  * Provide a configuration option to control automatic option responses.
  * `Flask.open_resource`/`open_instance_resource` and `Blueprint.open_resource` take an `encoding` parameter to use when opening in text mode. It defaults to `utf-8`.
  * `Request.max_content_length` can be customized per-request instead of only through the `MAX_CONTENT_LENGTH` config. Added `MAX_FORM_MEMORY_SIZE` and `MAX_FORM_PARTS` config. Added documentation about resource limits to the security page.
  * Add support for the `Partitioned` cookie attribute (CHIPS), with the `SESSION_COOKIE_PARTITIONED` config.
  * `-e path` takes precedence over default `.env` and `.flaskenv` files. `load_dotenv` loads default files in addition to a path unless `load_defaults=False` is passed.
  * Support key rotation with the `SECRET_KEY_FALLBACKS` config, a list of old secret keys that can still be used for unsigning. Extensions will need to add support.
  * Fix how setting `host_matching=True` or `subdomain_matching=False` interacts with `SERVER_NAME`. Setting `SERVER_NAME` no longer restricts requests to only that domain.
  * `Request.trusted_hosts` is checked during routing, and can be set through the `TRUSTED_HOSTS` config.
