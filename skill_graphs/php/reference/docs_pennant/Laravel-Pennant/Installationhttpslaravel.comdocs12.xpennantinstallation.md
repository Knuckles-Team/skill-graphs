## [Installation](https://laravel.com/docs/12.x/pennant#installation)
First, install Pennant into your project using the Composer package manager:
```


1composer require laravel/pennant




composer require laravel/pennant

```

Next, you should publish the Pennant configuration and migration files using the `vendor:publish` Artisan command:
```


1php artisan vendor:publish --provider="Laravel\Pennant\PennantServiceProvider"




php artisan vendor:publish --provider="Laravel\Pennant\PennantServiceProvider"

```

Finally, you should run your application's database migrations. This will create a `features` table that Pennant uses to power its `database` driver:
```


1php artisan migrate




php artisan migrate

```
