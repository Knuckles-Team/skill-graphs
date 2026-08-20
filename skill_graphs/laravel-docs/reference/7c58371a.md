## [Protecting Routes](https://laravel.com/docs/12.x/passport#protecting-routes)
### [Via Middleware](https://laravel.com/docs/12.x/passport#via-middleware)
Passport includes an [authentication guard](https://laravel.com/docs/12.x/authentication#adding-custom-guards) that will validate access tokens on incoming requests. Once you have configured the `api` guard to use the `passport` driver, you only need to specify the `auth:api` middleware on any routes that should require a valid access token:
```


1Route::get('/user', function () {




2    // Only API authenticated users may access this route...




3})->middleware('auth:api');




Route::get('/user', function () {
    // Only API authenticated users may access this route...
})->middleware('auth:api');

```

If you are using the [client credentials grant](https://laravel.com/docs/12.x/passport#client-credentials-grant), you should use [the `Laravel\Passport\Http\Middleware\EnsureClientIsResourceOwner` middleware](https://laravel.com/docs/12.x/passport#client-credentials-grant) to protect your routes instead of the `auth:api` middleware.
#### [Multiple Authentication Guards](https://laravel.com/docs/12.x/passport#multiple-authentication-guards)
If your application authenticates different types of users that perhaps use entirely different Eloquent models, you will likely need to define a guard configuration for each user provider type in your application. This allows you to protect requests intended for specific user providers. For example, given the following guard configuration the `config/auth.php` configuration file:
```


 1'guards' => [




 2    'api' => [




 3        'driver' => 'passport',




 4        'provider' => 'users',




 5    ],




 6 



 7    'api-customers' => [




 8        'driver' => 'passport',




 9        'provider' => 'customers',




10    ],




11],




'guards' => [
    'api' => [
        'driver' => 'passport',
        'provider' => 'users',
    ],

    'api-customers' => [
        'driver' => 'passport',
        'provider' => 'customers',
    ],
],

```

The following route will utilize the `api-customers` guard, which uses the `customers` user provider, to authenticate incoming requests:
```


1Route::get('/customer', function () {




2    // ...




3})->middleware('auth:api-customers');




Route::get('/customer', function () {
    // ...
})->middleware('auth:api-customers');

```

For more information on using multiple user providers with Passport, please consult the [personal access tokens documentation](https://laravel.com/docs/12.x/passport#customizing-the-user-provider-for-pat) and [password grant documentation](https://laravel.com/docs/12.x/passport#customizing-the-user-provider).
### [Passing the Access Token](https://laravel.com/docs/12.x/passport#passing-the-access-token)
When calling routes that are protected by Passport, your application's API consumers should specify their access token as a `Bearer` token in the `Authorization` header of their request. For example, when using the `Http` Facade:
```


1use Illuminate\Support\Facades\Http;




2 



3$response = Http::withHeaders([




4    'Accept' => 'application/json',




5    'Authorization' => "Bearer $accessToken",




6])->get('https://passport-app.test/api/user');




7 



8return $response->json();




use Illuminate\Support\Facades\Http;

$response = Http::withHeaders([
    'Accept' => 'application/json',
    'Authorization' => "Bearer $accessToken",
])->get('https://passport-app.test/api/user');

return $response->json();

```
