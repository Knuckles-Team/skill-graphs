## [Authorization Code Grant](https://laravel.com/docs/12.x/passport#authorization-code-grant)
Using OAuth2 via authorization codes is how most developers are familiar with OAuth2. When using authorization codes, a client application will redirect a user to your server where they will either approve or deny the request to issue an access token to the client.
To get started, we need to instruct Passport how to return our "authorization" view.
All the authorization view's rendering logic may be customized using the appropriate methods available via the `Laravel\Passport\Passport` class. Typically, you should call this method from the `boot` method of your application's `App\Providers\AppServiceProvider` class:
```


 1use Inertia\Inertia;




 2use Laravel\Passport\Passport;




 3 



 4/**




 5 * Bootstrap any application services.




 6 */




 7public function boot(): void




 8{




 9    // By providing a view name...




10    Passport::authorizationView('auth.oauth.authorize');




11 



12    // By providing a closure...




13    Passport::authorizationView(




14        fn ($parameters) => Inertia::render('Auth/OAuth/Authorize', [




15            'request' => $parameters['request'],




16            'authToken' => $parameters['authToken'],




17            'client' => $parameters['client'],




18            'user' => $parameters['user'],




19            'scopes' => $parameters['scopes'],




20        ])




21    );




22}




use Inertia\Inertia;
use Laravel\Passport\Passport;

/**
 * Bootstrap any application services.
 */
public function boot(): void
{
    // By providing a view name...
    Passport::authorizationView('auth.oauth.authorize');

    // By providing a closure...
    Passport::authorizationView(
        fn ($parameters) => Inertia::render('Auth/OAuth/Authorize', [
            'request' => $parameters['request'],
            'authToken' => $parameters['authToken'],
            'client' => $parameters['client'],
            'user' => $parameters['user'],
            'scopes' => $parameters['scopes'],
        ])
    );
}

```

Passport will automatically define the `/oauth/authorize` route that returns this view. Your `auth.oauth.authorize` template should include a form that makes a POST request to the `passport.authorizations.approve` route to approve the authorization and a form that makes a DELETE request to the `passport.authorizations.deny` route to deny the authorization. The `passport.authorizations.approve` and `passport.authorizations.deny` routes expect `state`, `client_id`, and `auth_token` fields.
### [Managing Clients](https://laravel.com/docs/12.x/passport#managing-clients)
Developers building applications that need to interact with your application's API will need to register their application with yours by creating a "client". Typically, this consists of providing the name of their application and a URI that your application can redirect to after users approve their request for authorization.
#### [First-Party Clients](https://laravel.com/docs/12.x/passport#managing-first-party-clients)
The simplest way to create a client is using the `passport:client` Artisan command. This command may be used to create first-party clients or testing your OAuth2 functionality. When you run the `passport:client` command, Passport will prompt you for more information about your client and will provide you with a client ID and secret:
```


1php artisan passport:client




php artisan passport:client

```

If you would like to allow multiple redirect URIs for your client, you may specify them using a comma-delimited list when prompted for the URI by the `passport:client` command. Any URIs which contain commas should be URI encoded:
```


1https://third-party-app.com/callback,https://example.com/oauth/redirect




https://third-party-app.com/callback,https://example.com/oauth/redirect

```

#### [Third-Party Clients](https://laravel.com/docs/12.x/passport#managing-third-party-clients)
Since your application's users will not be able to utilize the `passport:client` command, you may use `createAuthorizationCodeGrantClient` method of the `Laravel\Passport\ClientRepository` class to register a client for a given user:
```


 1use App\Models\User;




 2use Laravel\Passport\ClientRepository;




 3 



 4$user = User::find($userId);




 5 



 6// Creating an OAuth app client that belongs to the given user...




 7$client = app(ClientRepository::class)->createAuthorizationCodeGrantClient(




 8    user: $user,




 9    name: 'Example App',




10    redirectUris: ['https://third-party-app.com/callback'],




11    confidential: false,




12    enableDeviceFlow: true




13);




14 



15// Retrieving all the OAuth app clients that belong to the user...




16$clients = $user->oauthApps()->get();




use App\Models\User;
use Laravel\Passport\ClientRepository;

$user = User::find($userId);

// Creating an OAuth app client that belongs to the given user...
$client = app(ClientRepository::class)->createAuthorizationCodeGrantClient(
    user: $user,
    name: 'Example App',
    redirectUris: ['https://third-party-app.com/callback'],
    confidential: false,
    enableDeviceFlow: true
);

// Retrieving all the OAuth app clients that belong to the user...
$clients = $user->oauthApps()->get();

```

The `createAuthorizationCodeGrantClient` method returns an instance of `Laravel\Passport\Client`. You may display the `$client->id` as the client ID and `$client->plainSecret` as the client secret to the user.
### [Requesting Tokens](https://laravel.com/docs/12.x/passport#requesting-tokens)
#### [Redirecting for Authorization](https://laravel.com/docs/12.x/passport#requesting-tokens-redirecting-for-authorization)
Once a client has been created, developers may use their client ID and secret to request an authorization code and access token from your application. First, the consuming application should make a redirect request to your application's `/oauth/authorize` route like so:
```


 1use Illuminate\Http\Request;




 2use Illuminate\Support\Str;




 3 



 4Route::get('/redirect', function (Request $request) {




 5    $request->session()->put('state', $state = Str::random(40));




 6 



 7    $query = http_build_query([




 8        'client_id' => 'your-client-id',




 9        'redirect_uri' => 'https://third-party-app.com/callback',




10        'response_type' => 'code',




11        'scope' => 'user:read orders:create',




12        'state' => $state,




13        // 'prompt' => '', // "none", "consent", or "login"




14    ]);




15 



16    return redirect('https://passport-app.test/oauth/authorize?'.$query);




17});




use Illuminate\Http\Request;
use Illuminate\Support\Str;

Route::get('/redirect', function (Request $request) {
    $request->session()->put('state', $state = Str::random(40));

    $query = http_build_query([
        'client_id' => 'your-client-id',
        'redirect_uri' => 'https://third-party-app.com/callback',
        'response_type' => 'code',
        'scope' => 'user:read orders:create',
        'state' => $state,
        // 'prompt' => '', // "none", "consent", or "login"
    ]);

    return redirect('https://passport-app.test/oauth/authorize?'.$query);
});

```

The `prompt` parameter may be used to specify the authentication behavior of the Passport application.
If the `prompt` value is `none`, Passport will always throw an authentication error if the user is not already authenticated with the Passport application. If the value is `consent`, Passport will always display the authorization approval screen, even if all scopes were previously granted to the consuming application. When the value is `login`, the Passport application will always prompt the user to re-login to the application, even if they already have an existing session.
If no `prompt` value is provided, the user will be prompted for authorization only if they have not previously authorized access to the consuming application for the requested scopes.
Remember, the `/oauth/authorize` route is already defined by Passport. You do not need to manually define this route.
#### [Approving the Request](https://laravel.com/docs/12.x/passport#approving-the-request)
When receiving authorization requests, Passport will automatically respond based on the value of `prompt` parameter (if present) and may display a template to the user allowing them to approve or deny the authorization request. If they approve the request, they will be redirected back to the `redirect_uri` that was specified by the consuming application. The `redirect_uri` must match the `redirect` URL that was specified when the client was created.
Sometimes you may wish to skip the authorization prompt, such as when authorizing a first-party client. You may accomplish this by [extending the `Client` model](https://laravel.com/docs/12.x/passport#overriding-default-models) and defining a `skipsAuthorization` method. If `skipsAuthorization` returns `true` the client will be approved and the user will be redirected back to the `redirect_uri` immediately, unless the consuming application has explicitly set the `prompt` parameter when redirecting for authorization:
```


 1<?php




 2 



 3namespace App\Models\Passport;




 4 



 5use Illuminate\Contracts\Auth\Authenticatable;




 6use Laravel\Passport\Client as BaseClient;




 7 



 8class Client extends BaseClient




 9{




10    /**




11     * Determine if the client should skip the authorization prompt.




12     *




13     * @param  \Laravel\Passport\Scope[]  $scopes




14     */




15    public function skipsAuthorization(Authenticatable $user, array $scopes): bool




16    {




17        return $this->firstParty();




18    }




19}




<?php

namespace App\Models\Passport;

use Illuminate\Contracts\Auth\Authenticatable;
use Laravel\Passport\Client as BaseClient;

class Client extends BaseClient
{
    /**
     * Determine if the client should skip the authorization prompt.
     *
     * @param  \Laravel\Passport\Scope[]  $scopes
     */
    public function skipsAuthorization(Authenticatable $user, array $scopes): bool
    {
        return $this->firstParty();
    }
}

```

#### [Converting Authorization Codes to Access Tokens](https://laravel.com/docs/12.x/passport#requesting-tokens-converting-authorization-codes-to-access-tokens)
If the user approves the authorization request, they will be redirected back to the consuming application. The consumer should first verify the `state` parameter against the value that was stored prior to the redirect. If the state parameter matches then the consumer should issue a `POST` request to your application to request an access token. The request should include the authorization code that was issued by your application when the user approved the authorization request:
```


 1use Illuminate\Http\Request;




 2use Illuminate\Support\Facades\Http;




 3 



 4Route::get('/callback', function (Request $request) {




 5    $state = $request->session()->pull('state');




 6 



 7    throw_unless(




 8        strlen($state) > 0 && $state === $request->state,




 9        InvalidArgumentException::class,




10        'Invalid state value.'




11    );




12 



13    $response = Http::asForm()->post('https://passport-app.test/oauth/token', [




14        'grant_type' => 'authorization_code',




15        'client_id' => 'your-client-id',




16        'client_secret' => 'your-client-secret',




17        'redirect_uri' => 'https://third-party-app.com/callback',




18        'code' => $request->code,




19    ]);




20 



21    return $response->json();




22});




use Illuminate\Http\Request;
use Illuminate\Support\Facades\Http;

Route::get('/callback', function (Request $request) {
    $state = $request->session()->pull('state');

    throw_unless(
        strlen($state) > 0 && $state === $request->state,
        InvalidArgumentException::class,
        'Invalid state value.'
    );

    $response = Http::asForm()->post('https://passport-app.test/oauth/token', [
        'grant_type' => 'authorization_code',
        'client_id' => 'your-client-id',
        'client_secret' => 'your-client-secret',
        'redirect_uri' => 'https://third-party-app.com/callback',
        'code' => $request->code,
    ]);

    return $response->json();
});

```

This `/oauth/token` route will return a JSON response containing `access_token`, `refresh_token`, and `expires_in` attributes. The `expires_in` attribute contains the number of seconds until the access token expires.
Like the `/oauth/authorize` route, the `/oauth/token` route is defined for you by Passport. There is no need to manually define this route.
### [Managing Tokens](https://laravel.com/docs/12.x/passport#managing-tokens)
You may retrieve user's authorized tokens using the `tokens` method of the `Laravel\Passport\HasApiTokens` trait. For example, this may be used to offer your users a dashboard to keep track of their connections with third-party applications:
```


 1use App\Models\User;




 2use Illuminate\Database\Eloquent\Collection;




 3use Illuminate\Support\Facades\Date;




 4use Laravel\Passport\Token;




 5 



 6$user = User::find($userId);




 7 



 8// Retrieving all of the valid tokens for the user...




 9$tokens = $user->tokens()




10    ->where('revoked', false)




11    ->where('expires_at', '>', Date::now())




12    ->get();




13 



14// Retrieving all the user's connections to third-party OAuth app clients...




15$connections = $tokens->load('client')




16    ->reject(fn (Token $token) => $token->client->firstParty())




17    ->groupBy('client_id')




18    ->map(fn (Collection $tokens) => [




19        'client' => $tokens->first()->client,




20        'scopes' => $tokens->pluck('scopes')->flatten()->unique()->values()->all(),




21        'tokens_count' => $tokens->count(),




22    ])




23    ->values();




use App\Models\User;
use Illuminate\Database\Eloquent\Collection;
use Illuminate\Support\Facades\Date;
use Laravel\Passport\Token;

$user = User::find($userId);

// Retrieving all of the valid tokens for the user...
$tokens = $user->tokens()
    ->where('revoked', false)
    ->where('expires_at', '>', Date::now())
    ->get();

// Retrieving all the user's connections to third-party OAuth app clients...
$connections = $tokens->load('client')
    ->reject(fn (Token $token) => $token->client->firstParty())
    ->groupBy('client_id')
    ->map(fn (Collection $tokens) => [
        'client' => $tokens->first()->client,
        'scopes' => $tokens->pluck('scopes')->flatten()->unique()->values()->all(),
        'tokens_count' => $tokens->count(),
    ])
    ->values();

```

### [Refreshing Tokens](https://laravel.com/docs/12.x/passport#refreshing-tokens)
If your application issues short-lived access tokens, users will need to refresh their access tokens via the refresh token that was provided to them when the access token was issued:
```


 1use Illuminate\Support\Facades\Http;




 2 



 3$response = Http::asForm()->post('https://passport-app.test/oauth/token', [




 4    'grant_type' => 'refresh_token',




 5    'refresh_token' => 'the-refresh-token',




 6    'client_id' => 'your-client-id',




 7    'client_secret' => 'your-client-secret', // Required for confidential clients only...




 8    'scope' => 'user:read orders:create',




 9]);




10 



11return $response->json();




use Illuminate\Support\Facades\Http;

$response = Http::asForm()->post('https://passport-app.test/oauth/token', [
    'grant_type' => 'refresh_token',
    'refresh_token' => 'the-refresh-token',
    'client_id' => 'your-client-id',
    'client_secret' => 'your-client-secret', // Required for confidential clients only...
    'scope' => 'user:read orders:create',
]);

return $response->json();

```

This `/oauth/token` route will return a JSON response containing `access_token`, `refresh_token`, and `expires_in` attributes. The `expires_in` attribute contains the number of seconds until the access token expires.
### [Revoking Tokens](https://laravel.com/docs/12.x/passport#revoking-tokens)
You may revoke a token by using the `revoke` method on the `Laravel\Passport\Token` model. You may revoke a token's refresh token using the `revoke` method on the `Laravel\Passport\RefreshToken` model:
```


 1use Laravel\Passport\Passport;




 2use Laravel\Passport\Token;




 3 



 4$token = Passport::token()->find($tokenId);




 5 



 6// Revoke an access token...




 7$token->revoke();




 8 



 9// Revoke the token's refresh token...




10$token->refreshToken?->revoke();




11 



12// Revoke all of the user's tokens...




13User::find($userId)->tokens()->each(function (Token $token) {




14    $token->revoke();




15    $token->refreshToken?->revoke();




16});




use Laravel\Passport\Passport;
use Laravel\Passport\Token;

$token = Passport::token()->find($tokenId);

// Revoke an access token...
$token->revoke();

// Revoke the token's refresh token...
$token->refreshToken?->revoke();

// Revoke all of the user's tokens...
User::find($userId)->tokens()->each(function (Token $token) {
    $token->revoke();
    $token->refreshToken?->revoke();
});

```

### [Purging Tokens](https://laravel.com/docs/12.x/passport#purging-tokens)
When tokens have been revoked or expired, you might want to purge them from the database. Passport's included `passport:purge` Artisan command can do this for you:
```


 1# Purge revoked and expired tokens, auth codes, and device codes...




 2php artisan passport:purge




 3 



 4# Only purge tokens expired for more than 6 hours...




 5php artisan passport:purge --hours=6




 6 



 7# Only purge revoked tokens, auth codes, and device codes...




 8php artisan passport:purge --revoked




 9 



10# Only purge expired tokens, auth codes, and device codes...




11php artisan passport:purge --expired




# Purge revoked and expired tokens, auth codes, and device codes...
php artisan passport:purge

# Only purge tokens expired for more than 6 hours...
php artisan passport:purge --hours=6

# Only purge revoked tokens, auth codes, and device codes...
php artisan passport:purge --revoked

# Only purge expired tokens, auth codes, and device codes...
php artisan passport:purge --expired

```

You may also configure a [scheduled job](https://laravel.com/docs/12.x/scheduling) in your application's `routes/console.php` file to automatically prune your tokens on a schedule:
```


1use Illuminate\Support\Facades\Schedule;




2 



3Schedule::command('passport:purge')->hourly();




use Illuminate\Support\Facades\Schedule;

Schedule::command('passport:purge')->hourly();

```
