## [Implicit Grant](https://laravel.com/docs/12.x/passport#implicit-grant)
We no longer recommend using implicit grant tokens. Instead, you should choose
The implicit grant is similar to the authorization code grant; however, the token is returned to the client without exchanging an authorization code. This grant is most commonly used for JavaScript or mobile applications where the client credentials can't be securely stored. To enable the grant, call the `enableImplicitGrant` method in the `boot` method of your application's `App\Providers\AppServiceProvider` class:
```


1/**




2 * Bootstrap any application services.




3 */




4public function boot(): void




5{




6    Passport::enableImplicitGrant();




7}




/**
 * Bootstrap any application services.
 */
public function boot(): void
{
    Passport::enableImplicitGrant();
}

```

Before your application can issue tokens via the implicit grant, you will need to create an implicit grant client. You may do this using the `passport:client` Artisan command with the `--implicit` option.
```


1php artisan passport:client --implicit




php artisan passport:client --implicit

```

Once the grant has been enabled and an implicit client has been created, developers may use their client ID to request an access token from your application. The consuming application should make a redirect request to your application's `/oauth/authorize` route like so:
```


 1use Illuminate\Http\Request;




 2 



 3Route::get('/redirect', function (Request $request) {




 4    $request->session()->put('state', $state = Str::random(40));




 5 



 6    $query = http_build_query([




 7        'client_id' => 'your-client-id',




 8        'redirect_uri' => 'https://third-party-app.com/callback',




 9        'response_type' => 'token',




10        'scope' => 'user:read orders:create',




11        'state' => $state,




12        // 'prompt' => '', // "none", "consent", or "login"




13    ]);




14 



15    return redirect('https://passport-app.test/oauth/authorize?'.$query);




16});




use Illuminate\Http\Request;

Route::get('/redirect', function (Request $request) {
    $request->session()->put('state', $state = Str::random(40));

    $query = http_build_query([
        'client_id' => 'your-client-id',
        'redirect_uri' => 'https://third-party-app.com/callback',
        'response_type' => 'token',
        'scope' => 'user:read orders:create',
        'state' => $state,
        // 'prompt' => '', // "none", "consent", or "login"
    ]);

    return redirect('https://passport-app.test/oauth/authorize?'.$query);
});

```

Remember, the `/oauth/authorize` route is already defined by Passport. You do not need to manually define this route.
