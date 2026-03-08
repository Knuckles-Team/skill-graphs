## [Driver Prerequisites](https://laravel.com/docs/12.x/scout#driver-prerequisites)
### [Algolia](https://laravel.com/docs/12.x/scout#algolia)
When using the Algolia driver, you should configure your Algolia `id` and `secret` credentials in your `config/scout.php` configuration file. Once your credentials have been configured, you will also need to install the Algolia PHP SDK via the Composer package manager:
```


1composer require algolia/algoliasearch-client-php




composer require algolia/algoliasearch-client-php

```

### [Meilisearch](https://laravel.com/docs/12.x/scout#meilisearch)
[Laravel Sail](https://laravel.com/docs/12.x/sail#meilisearch), Laravel's officially supported Docker development environment.
When using the Meilisearch driver you will need to install the Meilisearch PHP SDK via the Composer package manager:
```


1composer require meilisearch/meilisearch-php http-interop/http-factory-guzzle




composer require meilisearch/meilisearch-php http-interop/http-factory-guzzle

```

Then, set the `SCOUT_DRIVER` environment variable as well as your Meilisearch `host` and `key` credentials within your application's `.env` file:
```


1SCOUT_DRIVER=meilisearch




2MEILISEARCH_HOST=http://127.0.0.1:7700




3MEILISEARCH_KEY=masterKey




SCOUT_DRIVER=meilisearch
MEILISEARCH_HOST=http://127.0.0.1:7700
MEILISEARCH_KEY=masterKey

```

For more information regarding Meilisearch, please consult the
In addition, you should ensure that you install a version of `meilisearch/meilisearch-php` that is compatible with your Meilisearch binary version by reviewing
When upgrading Scout on an application that utilizes Meilisearch, you should always
### [Typesense](https://laravel.com/docs/12.x/scout#typesense)
You can
To get started using Typesense with Scout, install the Typesense PHP SDK via the Composer package manager:
```


1composer require typesense/typesense-php




composer require typesense/typesense-php

```

Then, set the `SCOUT_DRIVER` environment variable as well as your Typesense host and API key credentials within your application's .env file:
```


1SCOUT_DRIVER=typesense




2TYPESENSE_API_KEY=masterKey




3TYPESENSE_HOST=localhost




SCOUT_DRIVER=typesense
TYPESENSE_API_KEY=masterKey
TYPESENSE_HOST=localhost

```

If you are using [Laravel Sail](https://laravel.com/docs/12.x/sail), you may need to adjust the `TYPESENSE_HOST` environment variable to match the Docker container name. You may also optionally specify your installation's port, path, and protocol:
```


1TYPESENSE_PORT=8108




2TYPESENSE_PATH=




3TYPESENSE_PROTOCOL=http




TYPESENSE_PORT=8108
TYPESENSE_PATH=
TYPESENSE_PROTOCOL=http

```

Additional settings and schema definitions for your Typesense collections can be found within your application's `config/scout.php` configuration file. For more information regarding Typesense, please consult the
