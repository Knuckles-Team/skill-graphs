## [Token Scopes](https://laravel.com/docs/12.x/passport#token-scopes)
Scopes allow your API clients to request a specific set of permissions when requesting authorization to access an account. For example, if you are building an e-commerce application, not all API consumers will need the ability to place orders. Instead, you may allow the consumers to only request authorization to access order shipment statuses. In other words, scopes allow your application's users to limit the actions a third-party application can perform on their behalf.
### [Defining Scopes](https://laravel.com/docs/12.x/passport#defining-scopes)
You may define your API's scopes using the `Passport::tokensCan` method in the `boot` method of your application's `App\Providers\AppServiceProvider` class. The `tokensCan` method accepts an array of scope names and scope descriptions. The scope description may be anything you wish and will be displayed to users on the authorization approval screen:
```


 1/**




 2 * Bootstrap any application services.




 3 */




 4public function boot(): void




 5{




 6    Passport::tokensCan([




 7        'user:read' => 'Retrieve the user info',




 8        'orders:create' => 'Place orders',




 9        'orders:read:status' => 'Check order status',




10    ]);




11}




/**
 * Bootstrap any application services.
 */
public function boot(): void
{
    Passport::tokensCan([
        'user:read' => 'Retrieve the user info',
        'orders:create' => 'Place orders',
        'orders:read:status' => 'Check order status',
    ]);
}

```

### [Default Scope](https://laravel.com/docs/12.x/passport#default-scope)
If a client does not request any specific scopes, you may configure your Passport server to attach default scopes to the token using the `defaultScopes` method. Typically, you should call this method from the `boot` method of your application's `App\Providers\AppServiceProvider` class:
```


 1use Laravel\Passport\Passport;




 2 



 3Passport::tokensCan([




 4    'user:read' => 'Retrieve the user info',




 5    'orders:create' => 'Place orders',




 6    'orders:read:status' => 'Check order status',




 7]);




 8 



 9Passport::defaultScopes([




10    'user:read',




11    'orders:create',




12]);




use Laravel\Passport\Passport;

Passport::tokensCan([
    'user:read' => 'Retrieve the user info',
    'orders:create' => 'Place orders',
    'orders:read:status' => 'Check order status',
]);

Passport::defaultScopes([
    'user:read',
    'orders:create',
]);

```

### [Assigning Scopes to Tokens](https://laravel.com/docs/12.x/passport#assigning-scopes-to-tokens)
#### [When Requesting Authorization Codes](https://laravel.com/docs/12.x/passport#when-requesting-authorization-codes)
When requesting an access token using the authorization code grant, consumers should specify their desired scopes as the `scope` query string parameter. The `scope` parameter should be a space-delimited list of scopes:
```


 1Route::get('/redirect', function () {




 2    $query = http_build_query([




 3        'client_id' => 'your-client-id',




 4        'redirect_uri' => 'https://third-party-app.com/callback',




 5        'response_type' => 'code',




 6        'scope' => 'user:read orders:create',




 7    ]);




 8 



 9    return redirect('https://passport-app.test/oauth/authorize?'.$query);




10});




Route::get('/redirect', function () {
    $query = http_build_query([
        'client_id' => 'your-client-id',
        'redirect_uri' => 'https://third-party-app.com/callback',
        'response_type' => 'code',
        'scope' => 'user:read orders:create',
    ]);

    return redirect('https://passport-app.test/oauth/authorize?'.$query);
});

```

#### [When Issuing Personal Access Tokens](https://laravel.com/docs/12.x/passport#when-issuing-personal-access-tokens)
If you are issuing personal access tokens using the `App\Models\User` model's `createToken` method, you may pass the array of desired scopes as the second argument to the method:
```


1$token = $user->createToken('My Token', ['orders:create'])->accessToken;




$token = $user->createToken('My Token', ['orders:create'])->accessToken;

```

### [Checking Scopes](https://laravel.com/docs/12.x/passport#checking-scopes)
Passport includes two middleware that may be used to verify that an incoming request is authenticated with a token that has been granted a given scope.
#### [Check For All Scopes](https://laravel.com/docs/12.x/passport#check-for-all-scopes)
The `Laravel\Passport\Http\Middleware\CheckToken` middleware may be assigned to a route to verify that the incoming request's access token has all the listed scopes:
```


1use Laravel\Passport\Http\Middleware\CheckToken;




2 



3Route::get('/orders', function () {




4    // Access token has both "orders:read" and "orders:create" scopes...




5})->middleware(['auth:api', CheckToken::using('orders:read', 'orders:create')]);




use Laravel\Passport\Http\Middleware\CheckToken;

Route::get('/orders', function () {
    // Access token has both "orders:read" and "orders:create" scopes...
})->middleware(['auth:api', CheckToken::using('orders:read', 'orders:create')]);

```

#### [Check for Any Scopes](https://laravel.com/docs/12.x/passport#check-for-any-scopes)
The `Laravel\Passport\Http\Middleware\CheckTokenForAnyScope` middleware may be assigned to a route to verify that the incoming request's access token has _at least one_ of the listed scopes:
```


1use Laravel\Passport\Http\Middleware\CheckTokenForAnyScope;




2 



3Route::get('/orders', function () {




4    // Access token has either "orders:read" or "orders:create" scope...




5})->middleware(['auth:api', CheckTokenForAnyScope::using('orders:read', 'orders:create')]);




use Laravel\Passport\Http\Middleware\CheckTokenForAnyScope;

Route::get('/orders', function () {
    // Access token has either "orders:read" or "orders:create" scope...
})->middleware(['auth:api', CheckTokenForAnyScope::using('orders:read', 'orders:create')]);

```

#### [Checking Scopes on a Token Instance](https://laravel.com/docs/12.x/passport#checking-scopes-on-a-token-instance)
Once an access token authenticated request has entered your application, you may still check if the token has a given scope using the `tokenCan` method on the authenticated `App\Models\User` instance:
```


1use Illuminate\Http\Request;




2 



3Route::get('/orders', function (Request $request) {




4    if ($request->user()->tokenCan('orders:create')) {




5        // ...




6    }




7});




use Illuminate\Http\Request;

Route::get('/orders', function (Request $request) {
    if ($request->user()->tokenCan('orders:create')) {
        // ...
    }
});

```

#### [Additional Scope Methods](https://laravel.com/docs/12.x/passport#additional-scope-methods)
The `scopeIds` method will return an array of all defined IDs / names:
```


1use Laravel\Passport\Passport;




2 



3Passport::scopeIds();




use Laravel\Passport\Passport;

Passport::scopeIds();

```

The `scopes` method will return an array of all defined scopes as instances of `Laravel\Passport\Scope`:
```


1Passport::scopes();




Passport::scopes();

```

The `scopesFor` method will return an array of `Laravel\Passport\Scope` instances matching the given IDs / names:
```


1Passport::scopesFor(['user:read', 'orders:create']);




Passport::scopesFor(['user:read', 'orders:create']);

```

You may determine if a given scope has been defined using the `hasScope` method:
```


1Passport::hasScope('orders:create');




Passport::hasScope('orders:create');

```
