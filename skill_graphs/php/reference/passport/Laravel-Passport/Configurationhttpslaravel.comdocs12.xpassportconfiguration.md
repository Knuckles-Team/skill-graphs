## [Configuration](https://laravel.com/docs/12.x/passport#configuration)
### [Token Lifetimes](https://laravel.com/docs/12.x/passport#token-lifetimes)
By default, Passport issues long-lived access tokens that expire after one year. If you would like to configure a longer / shorter token lifetime, you may use the `tokensExpireIn`, `refreshTokensExpireIn`, and `personalAccessTokensExpireIn` methods. These methods should be called from the `boot` method of your application's `App\Providers\AppServiceProvider` class:
```


 1use Carbon\CarbonInterval;




 2 



 3/**




 4 * Bootstrap any application services.




 5 */




 6public function boot(): void




 7{




 8    Passport::tokensExpireIn(CarbonInterval::days(15));




 9    Passport::refreshTokensExpireIn(CarbonInterval::days(30));




10    Passport::personalAccessTokensExpireIn(CarbonInterval::months(6));




11}




use Carbon\CarbonInterval;

/**
 * Bootstrap any application services.
 */
public function boot(): void
{
    Passport::tokensExpireIn(CarbonInterval::days(15));
    Passport::refreshTokensExpireIn(CarbonInterval::days(30));
    Passport::personalAccessTokensExpireIn(CarbonInterval::months(6));
}

```

The `expires_at` columns on Passport's database tables are read-only and for display purposes only. When issuing tokens, Passport stores the expiration information within the signed and encrypted tokens. If you need to invalidate a token you should [revoke it](https://laravel.com/docs/12.x/passport#revoking-tokens).
### [Overriding Default Models](https://laravel.com/docs/12.x/passport#overriding-default-models)
You are free to extend the models used internally by Passport by defining your own model and extending the corresponding Passport model:
```


1use Laravel\Passport\Client as PassportClient;




2 



3class Client extends PassportClient




4{




5    // ...




6}




use Laravel\Passport\Client as PassportClient;

class Client extends PassportClient
{
    // ...
}

```

After defining your model, you may instruct Passport to use your custom model via the `Laravel\Passport\Passport` class. Typically, you should inform Passport about your custom models in the `boot` method of your application's `App\Providers\AppServiceProvider` class:
```


 1use App\Models\Passport\AuthCode;




 2use App\Models\Passport\Client;




 3use App\Models\Passport\DeviceCode;




 4use App\Models\Passport\RefreshToken;




 5use App\Models\Passport\Token;




 6use Laravel\Passport\Passport;




 7 



 8/**




 9 * Bootstrap any application services.




10 */




11public function boot(): void




12{




13    Passport::useTokenModel(Token::class);




14    Passport::useRefreshTokenModel(RefreshToken::class);




15    Passport::useAuthCodeModel(AuthCode::class);




16    Passport::useClientModel(Client::class);




17    Passport::useDeviceCodeModel(DeviceCode::class);




18}




use App\Models\Passport\AuthCode;
use App\Models\Passport\Client;
use App\Models\Passport\DeviceCode;
use App\Models\Passport\RefreshToken;
use App\Models\Passport\Token;
use Laravel\Passport\Passport;

/**
 * Bootstrap any application services.
 */
public function boot(): void
{
    Passport::useTokenModel(Token::class);
    Passport::useRefreshTokenModel(RefreshToken::class);
    Passport::useAuthCodeModel(AuthCode::class);
    Passport::useClientModel(Client::class);
    Passport::useDeviceCodeModel(DeviceCode::class);
}

```

### [Overriding Routes](https://laravel.com/docs/12.x/passport#overriding-routes)
Sometimes you may wish to customize the routes defined by Passport. To achieve this, you first need to ignore the routes registered by Passport by adding `Passport::ignoreRoutes` to the `register` method of your application's `AppServiceProvider`:
```


1use Laravel\Passport\Passport;




2 



3/**




4 * Register any application services.




5 */




6public function register(): void




7{




8    Passport::ignoreRoutes();




9}




use Laravel\Passport\Passport;

/**
 * Register any application services.
 */
public function register(): void
{
    Passport::ignoreRoutes();
}

```

Then, you may copy the routes defined by Passport in `routes/web.php` file and modify them to your liking:
```


1Route::group([




2    'as' => 'passport.',




3    'prefix' => config('passport.path', 'oauth'),




4    'namespace' => '\Laravel\Passport\Http\Controllers',




5], function () {




6    // Passport routes...




7});




Route::group([
    'as' => 'passport.',
    'prefix' => config('passport.path', 'oauth'),
    'namespace' => '\Laravel\Passport\Http\Controllers',
], function () {
    // Passport routes...
});

```
