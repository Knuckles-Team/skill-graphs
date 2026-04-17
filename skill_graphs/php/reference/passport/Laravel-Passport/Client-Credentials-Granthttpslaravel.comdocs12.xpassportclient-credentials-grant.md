## [Client Credentials Grant](https://laravel.com/docs/12.x/passport#client-credentials-grant)
The client credentials grant is suitable for machine-to-machine authentication. For example, you might use this grant in a scheduled job which is performing maintenance tasks over an API.
Before your application can issue tokens via the client credentials grant, you will need to create a client credentials grant client. You may do this using the `--client` option of the `passport:client` Artisan command:
```


1php artisan passport:client --client




php artisan passport:client --client

```

Next, assign the `Laravel\Passport\Http\Middleware\EnsureClientIsResourceOwner` middleware to a route:
```


1use Laravel\Passport\Http\Middleware\EnsureClientIsResourceOwner;




2 



3Route::get('/orders', function (Request $request) {




4    // Access token is valid and the client is resource owner...




5})->middleware(EnsureClientIsResourceOwner::class);




use Laravel\Passport\Http\Middleware\EnsureClientIsResourceOwner;

Route::get('/orders', function (Request $request) {
    // Access token is valid and the client is resource owner...
})->middleware(EnsureClientIsResourceOwner::class);

```

To restrict access to the route to specific scopes, you may provide a list of the required scopes to the `using` method`:
```


1Route::get('/orders', function (Request $request) {




2    // Access token is valid, the client is resource owner, and has both "servers:read" and "servers:create" scopes...




3})->middleware(EnsureClientIsResourceOwner::using('servers:read', 'servers:create'));




Route::get('/orders', function (Request $request) {
    // Access token is valid, the client is resource owner, and has both "servers:read" and "servers:create" scopes...
})->middleware(EnsureClientIsResourceOwner::using('servers:read', 'servers:create'));

```

### [Retrieving Tokens](https://laravel.com/docs/12.x/passport#retrieving-tokens)
To retrieve a token using this grant type, make a request to the `oauth/token` endpoint:
```


 1use Illuminate\Support\Facades\Http;




 2 



 3$response = Http::asForm()->post('https://passport-app.test/oauth/token', [




 4    'grant_type' => 'client_credentials',




 5    'client_id' => 'your-client-id',




 6    'client_secret' => 'your-client-secret',




 7    'scope' => 'servers:read servers:create',




 8]);




 9 



10return $response->json()['access_token'];




use Illuminate\Support\Facades\Http;

$response = Http::asForm()->post('https://passport-app.test/oauth/token', [
    'grant_type' => 'client_credentials',
    'client_id' => 'your-client-id',
    'client_secret' => 'your-client-secret',
    'scope' => 'servers:read servers:create',
]);

return $response->json()['access_token'];

```
