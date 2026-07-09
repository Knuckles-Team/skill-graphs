## [Paths](https://laravel.com/docs/12.x/helpers#paths)
#### [`app_path()`](https://laravel.com/docs/12.x/helpers#method-app-path)
The `app_path` function returns the fully qualified path to your application's `app` directory. You may also use the `app_path` function to generate a fully qualified path to a file relative to the application directory:
```


1$path = app_path();




2 



3$path = app_path('Http/Controllers/Controller.php');




$path = app_path();

$path = app_path('Http/Controllers/Controller.php');

```

#### [`base_path()`](https://laravel.com/docs/12.x/helpers#method-base-path)
The `base_path` function returns the fully qualified path to your application's root directory. You may also use the `base_path` function to generate a fully qualified path to a given file relative to the project root directory:
```


1$path = base_path();




2 



3$path = base_path('vendor/bin');




$path = base_path();

$path = base_path('vendor/bin');

```

#### [`config_path()`](https://laravel.com/docs/12.x/helpers#method-config-path)
The `config_path` function returns the fully qualified path to your application's `config` directory. You may also use the `config_path` function to generate a fully qualified path to a given file within the application's configuration directory:
```


1$path = config_path();




2 



3$path = config_path('app.php');




$path = config_path();

$path = config_path('app.php');

```

#### [`database_path()`](https://laravel.com/docs/12.x/helpers#method-database-path)
The `database_path` function returns the fully qualified path to your application's `database` directory. You may also use the `database_path` function to generate a fully qualified path to a given file within the database directory:
```


1$path = database_path();




2 



3$path = database_path('factories/UserFactory.php');




$path = database_path();

$path = database_path('factories/UserFactory.php');

```

#### [`lang_path()`](https://laravel.com/docs/12.x/helpers#method-lang-path)
The `lang_path` function returns the fully qualified path to your application's `lang` directory. You may also use the `lang_path` function to generate a fully qualified path to a given file within the directory:
```


1$path = lang_path();




2 



3$path = lang_path('en/messages.php');




$path = lang_path();

$path = lang_path('en/messages.php');

```

By default, the Laravel application skeleton does not include the `lang` directory. If you would like to customize Laravel's language files, you may publish them via the `lang:publish` Artisan command.
#### [`public_path()`](https://laravel.com/docs/12.x/helpers#method-public-path)
The `public_path` function returns the fully qualified path to your application's `public` directory. You may also use the `public_path` function to generate a fully qualified path to a given file within the public directory:
```


1$path = public_path();




2 



3$path = public_path('css/app.css');




$path = public_path();

$path = public_path('css/app.css');

```

#### [`resource_path()`](https://laravel.com/docs/12.x/helpers#method-resource-path)
The `resource_path` function returns the fully qualified path to your application's `resources` directory. You may also use the `resource_path` function to generate a fully qualified path to a given file within the resources directory:
```


1$path = resource_path();




2 



3$path = resource_path('sass/app.scss');




$path = resource_path();

$path = resource_path('sass/app.scss');

```

#### [`storage_path()`](https://laravel.com/docs/12.x/helpers#method-storage-path)
The `storage_path` function returns the fully qualified path to your application's `storage` directory. You may also use the `storage_path` function to generate a fully qualified path to a given file within the storage directory:
```


1$path = storage_path();




2 



3$path = storage_path('app/file.txt');




$path = storage_path();

$path = storage_path('app/file.txt');

```
