## [Installation](https://laravel.com/docs/12.x/billing#installation)
First, install the Cashier package for Stripe using the Composer package manager:
```


1composer require laravel/cashier




composer require laravel/cashier

```

After installing the package, publish Cashier's migrations using the `vendor:publish` Artisan command:
```


1php artisan vendor:publish --tag="cashier-migrations"




php artisan vendor:publish --tag="cashier-migrations"

```

Then, migrate your database:
```


1php artisan migrate




php artisan migrate

```

Cashier's migrations will add several columns to your `users` table. They will also create a new `subscriptions` table to hold all of your customer's subscriptions and a `subscription_items` table for subscriptions with multiple prices.
If you wish, you can also publish Cashier's configuration file using the `vendor:publish` Artisan command:
```


1php artisan vendor:publish --tag="cashier-config"




php artisan vendor:publish --tag="cashier-config"

```

Lastly, to ensure Cashier properly handles all Stripe events, remember to [configure Cashier's webhook handling](https://laravel.com/docs/12.x/billing#handling-stripe-webhooks).
Stripe recommends that any column used for storing Stripe identifiers should be case-sensitive. Therefore, you should ensure the column collation for the `stripe_id` column is set to `utf8_bin` when using MySQL. More information regarding this can be found in the
