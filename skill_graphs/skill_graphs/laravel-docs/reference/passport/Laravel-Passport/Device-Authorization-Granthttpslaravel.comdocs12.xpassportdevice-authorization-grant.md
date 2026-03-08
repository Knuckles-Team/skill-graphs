## [Device Authorization Grant](https://laravel.com/docs/12.x/passport#device-authorization-grant)
The OAuth2 device authorization grant allows browserless or limited input devices, such as TVs and game consoles, to obtain an access token by exchanging a "device code". When using device flow, the device client will instruct the user to use a secondary device, such as a computer or a smartphone and connect to your server where they will enter the provided "user code" and either approve or deny the access request.
To get started, we need to instruct Passport how to return our "user code" and "authorization" views.
All the authorization view's rendering logic may be customized using the appropriate methods available via the `Laravel\Passport\Passport` class. Typically, you should call this method from the `boot` method of your application's `App\Providers\AppServiceProvider` class.
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




10    Passport::deviceUserCodeView('auth.oauth.device.user-code');




11    Passport::deviceAuthorizationView('auth.oauth.device.authorize');




12 



13    // By providing a closure...




14    Passport::deviceUserCodeView(




15        fn ($parameters) => Inertia::render('Auth/OAuth/Device/UserCode')




16    );




17 



18    Passport::deviceAuthorizationView(




19        fn ($parameters) => Inertia::render('Auth/OAuth/Device/Authorize', [




20            'request' => $parameters['request'],




21            'authToken' => $parameters['authToken'],




22            'client' => $parameters['client'],




23            'user' => $parameters['user'],




24            'scopes' => $parameters['scopes'],




25        ])




26    );




27 



28    // ...




29}




use Inertia\Inertia;
use Laravel\Passport\Passport;

/**
 * Bootstrap any application services.
 */
public function boot(): void
{
    // By providing a view name...
    Passport::deviceUserCodeView('auth.oauth.device.user-code');
    Passport::deviceAuthorizationView('auth.oauth.device.authorize');

    // By providing a closure...
    Passport::deviceUserCodeView(
        fn ($parameters) => Inertia::render('Auth/OAuth/Device/UserCode')
    );

    Passport::deviceAuthorizationView(
        fn ($parameters) => Inertia::render('Auth/OAuth/Device/Authorize', [
            'request' => $parameters['request'],
            'authToken' => $parameters['authToken'],
            'client' => $parameters['client'],
            'user' => $parameters['user'],
            'scopes' => $parameters['scopes'],
        ])
    );

    // ...
}

```

Passport will automatically define routes that return these views. Your `auth.oauth.device.user-code` template should include a form that makes a GET request to the `passport.device.authorizations.authorize` route. The `passport.device.authorizations.authorize` route expects a `user_code` query parameter.
Your `auth.oauth.device.authorize` template should include a form that makes a POST request to the `passport.device.authorizations.approve` route to approve the authorization and a form that makes a DELETE request to the `passport.device.authorizations.deny` route to deny the authorization. The `passport.device.authorizations.approve` and `passport.device.authorizations.deny` routes expect `state`, `client_id`, and `auth_token` fields.
### [Creating a Device Authorization Grant Client](https://laravel.com/docs/12.x/passport#creating-a-device-authorization-grant-client)
Before your application can issue tokens via the device authorization grant, you will need to create a device flow enabled client. You may do this using the `passport:client` Artisan command with the `--device` option. This command will create a first-party device flow enabled client and provide you with a client ID and secret:
```


1php artisan passport:client --device




php artisan passport:client --device

```

Additionally, you may use `createDeviceAuthorizationGrantClient` method on the `ClientRepository` class to register a third-party client that belongs to the given user:
```


 1use App\Models\User;




 2use Laravel\Passport\ClientRepository;




 3 



 4$user = User::find($userId);




 5 



 6$client = app(ClientRepository::class)->createDeviceAuthorizationGrantClient(




 7    user: $user,




 8    name: 'Example Device',




 9    confidential: false,




10);




use App\Models\User;
use Laravel\Passport\ClientRepository;

$user = User::find($userId);

$client = app(ClientRepository::class)->createDeviceAuthorizationGrantClient(
    user: $user,
    name: 'Example Device',
    confidential: false,
);

```

### [Requesting Tokens](https://laravel.com/docs/12.x/passport#requesting-device-authorization-grant-tokens)
#### [Requesting a Device Code](https://laravel.com/docs/12.x/passport#device-code)
Once a client has been created, developers may use their client ID to request a device code from your application. First, the consuming device should make a `POST` request to your application's `/oauth/device/code` route to request a device code:
```


1use Illuminate\Support\Facades\Http;




2 



3$response = Http::asForm()->post('https://passport-app.test/oauth/device/code', [




4    'client_id' => 'your-client-id',




5    'scope' => 'user:read orders:create',




6]);




7 



8return $response->json();




use Illuminate\Support\Facades\Http;

$response = Http::asForm()->post('https://passport-app.test/oauth/device/code', [
    'client_id' => 'your-client-id',
    'scope' => 'user:read orders:create',
]);

return $response->json();

```

This will return a JSON response containing `device_code`, `user_code`, `verification_uri`, `interval`, and `expires_in` attributes. The `expires_in` attribute contains the number of seconds until the device code expires. The `interval` attribute contains the number of seconds the consuming device should wait between requests when polling `/oauth/token` route to avoid rate limit errors.
Remember, the `/oauth/device/code` route is already defined by Passport. You do not need to manually define this route.
#### [Displaying the Verification URI and User Code](https://laravel.com/docs/12.x/passport#user-code)
Once a device code request has been obtained, the consuming device should instruct the user to use another device and visit the provided `verification_uri` and enter the `user_code` in order to approve the authorization request.
#### [Polling Token Request](https://laravel.com/docs/12.x/passport#polling-token-request)
Since the user will be using a separate device to grant (or deny) access, the consuming device should poll your application's `/oauth/token` route to determine when the user has responded to the request. The consuming device should use the minimum polling `interval` provided in the JSON response when requesting device code to avoid rate limit errors:
```


 1use Illuminate\Support\Facades\Http;




 2use Illuminate\Support\Sleep;




 3 



 4$interval = 5;




 5 



 6do {




 7    Sleep::for($interval)->seconds();




 8 



 9    $response = Http::asForm()->post('https://passport-app.test/oauth/token', [




10        'grant_type' => 'urn:ietf:params:oauth:grant-type:device_code',




11        'client_id' => 'your-client-id',




12        'client_secret' => 'your-client-secret', // Required for confidential clients only...




13        'device_code' => 'the-device-code',




14    ]);




15 



16    if ($response->json('error') === 'slow_down') {




17        $interval += 5;




18    }




19} while (in_array($response->json('error'), ['authorization_pending', 'slow_down']));




20 



21return $response->json();




use Illuminate\Support\Facades\Http;
use Illuminate\Support\Sleep;

$interval = 5;

do {
    Sleep::for($interval)->seconds();

    $response = Http::asForm()->post('https://passport-app.test/oauth/token', [
        'grant_type' => 'urn:ietf:params:oauth:grant-type:device_code',
        'client_id' => 'your-client-id',
        'client_secret' => 'your-client-secret', // Required for confidential clients only...
        'device_code' => 'the-device-code',
    ]);

    if ($response->json('error') === 'slow_down') {
        $interval += 5;
    }
} while (in_array($response->json('error'), ['authorization_pending', 'slow_down']));

return $response->json();

```

If the user has approved the authorization request, this will return a JSON response containing `access_token`, `refresh_token`, and `expires_in` attributes. The `expires_in` attribute contains the number of seconds until the access token expires.
