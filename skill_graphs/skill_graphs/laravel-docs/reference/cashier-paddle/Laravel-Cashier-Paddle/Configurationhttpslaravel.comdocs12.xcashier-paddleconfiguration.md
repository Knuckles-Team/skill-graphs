## [Configuration](https://laravel.com/docs/12.x/cashier-paddle#configuration)
### [Billable Model](https://laravel.com/docs/12.x/cashier-paddle#billable-model)
Before using Cashier, you must add the `Billable` trait to your user model definition. This trait provides various methods to allow you to perform common billing tasks, such as creating subscriptions and updating payment method information:
```


1use Laravel\Paddle\Billable;




2 



3class User extends Authenticatable




4{




5    use Billable;




6}




use Laravel\Paddle\Billable;

class User extends Authenticatable
{
    use Billable;
}

```

If you have billable entities that are not users, you may also add the trait to those classes:
```


1use Illuminate\Database\Eloquent\Model;




2use Laravel\Paddle\Billable;




3 



4class Team extends Model




5{




6    use Billable;




7}




use Illuminate\Database\Eloquent\Model;
use Laravel\Paddle\Billable;

class Team extends Model
{
    use Billable;
}

```

### [API Keys](https://laravel.com/docs/12.x/cashier-paddle#api-keys)
Next, you should configure your Paddle keys in your application's `.env` file. You can retrieve your Paddle API keys from the Paddle control panel:
```


1PADDLE_CLIENT_SIDE_TOKEN=your-paddle-client-side-token




2PADDLE_API_KEY=your-paddle-api-key




3PADDLE_RETAIN_KEY=your-paddle-retain-key




4PADDLE_WEBHOOK_SECRET="your-paddle-webhook-secret"




5PADDLE_SANDBOX=true




PADDLE_CLIENT_SIDE_TOKEN=your-paddle-client-side-token
PADDLE_API_KEY=your-paddle-api-key
PADDLE_RETAIN_KEY=your-paddle-retain-key
PADDLE_WEBHOOK_SECRET="your-paddle-webhook-secret"
PADDLE_SANDBOX=true

```

The `PADDLE_SANDBOX` environment variable should be set to `true` when you are using [Paddle's Sandbox environment](https://laravel.com/docs/12.x/cashier-paddle#paddle-sandbox). The `PADDLE_SANDBOX` variable should be set to `false` if you are deploying your application to production and are using Paddle's live vendor environment.
The `PADDLE_RETAIN_KEY` is optional and should only be set if you're using Paddle with
### [Paddle JS](https://laravel.com/docs/12.x/cashier-paddle#paddle-js)
Paddle relies on its own JavaScript library to initiate the Paddle checkout widget. You can load the JavaScript library by placing the `@paddleJS` Blade directive right before your application layout's closing `</head>` tag:
```


1<head>




2    ...




3 



4    @paddleJS




5</head>




<head>
    ...

    @paddleJS
</head>

```

### [Currency Configuration](https://laravel.com/docs/12.x/cashier-paddle#currency-configuration)
You can specify a locale to be used when formatting money values for display on invoices. Internally, Cashier utilizes
```


1CASHIER_CURRENCY_LOCALE=nl_BE




CASHIER_CURRENCY_LOCALE=nl_BE

```

In order to use locales other than `en`, ensure the `ext-intl` PHP extension is installed and configured on your server.
### [Overriding Default Models](https://laravel.com/docs/12.x/cashier-paddle#overriding-default-models)
You are free to extend the models used internally by Cashier by defining your own model and extending the corresponding Cashier model:
```


1use Laravel\Paddle\Subscription as CashierSubscription;




2 



3class Subscription extends CashierSubscription




4{




5    // ...




6}




use Laravel\Paddle\Subscription as CashierSubscription;

class Subscription extends CashierSubscription
{
    // ...
}

```

After defining your model, you may instruct Cashier to use your custom model via the `Laravel\Paddle\Cashier` class. Typically, you should inform Cashier about your custom models in the `boot` method of your application's `App\Providers\AppServiceProvider` class:
```


 1use App\Models\Cashier\Subscription;




 2use App\Models\Cashier\Transaction;




 3 



 4/**




 5 * Bootstrap any application services.




 6 */




 7public function boot(): void




 8{




 9    Cashier::useSubscriptionModel(Subscription::class);




10    Cashier::useTransactionModel(Transaction::class);




11}




use App\Models\Cashier\Subscription;
use App\Models\Cashier\Transaction;

/**
 * Bootstrap any application services.
 */
public function boot(): void
{
    Cashier::useSubscriptionModel(Subscription::class);
    Cashier::useTransactionModel(Transaction::class);
}

```
