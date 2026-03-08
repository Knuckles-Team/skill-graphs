## [Installation](https://laravel.com/docs/12.x/cashier-paddle#installation)
First, install the Cashier package for Paddle using the Composer package manager:
```


1composer require laravel/cashier-paddle




composer require laravel/cashier-paddle

```

Next, you should publish the Cashier migration files using the `vendor:publish` Artisan command:
```


1php artisan vendor:publish --tag="cashier-migrations"




php artisan vendor:publish --tag="cashier-migrations"

```

Then, you should run your application's database migrations. The Cashier migrations will create a new `customers` table. In addition, new `subscriptions` and `subscription_items` tables will be created to store all of your customer's subscriptions. Lastly, a new `transactions` table will be created to store all of the Paddle transactions associated with your customers:
```


1php artisan migrate




php artisan migrate

```

To ensure Cashier properly handles all Paddle events, remember to [set up Cashier's webhook handling](https://laravel.com/docs/12.x/cashier-paddle#handling-paddle-webhooks).
### [Paddle Sandbox](https://laravel.com/docs/12.x/cashier-paddle#paddle-sandbox)
During local and staging development, you should
When using the Paddle Sandbox environment, you should set the `PADDLE_SANDBOX` environment variable to `true` within your application's `.env` file:
```


1PADDLE_SANDBOX=true




PADDLE_SANDBOX=true

```

After you have finished developing your application you may
