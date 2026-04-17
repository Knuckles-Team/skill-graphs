## [Password Grant](https://laravel.com/docs/12.x/passport#password-grant)
We no longer recommend using password grant tokens. Instead, you should choose
The OAuth2 password grant allows your other first-party clients, such as a mobile application, to obtain an access token using an email address / username and password. This allows you to issue access tokens securely to your first-party clients without requiring your users to go through the entire OAuth2 authorization code redirect flow.
To enable the password grant, call the `enablePasswordGrant` method in the `boot` method of your application's `App\Providers\AppServiceProvider` class:
```


1/**




2 * Bootstrap any application services.




3 */




4public function boot(): void




5{




6    Passport::enablePasswordGrant();




7}




/**
 * Bootstrap any application services.
 */
public function boot(): void
{
    Passport::enablePasswordGrant();
}

```

### [Creating a Password Grant Client](https://laravel.com/docs/12.x/passport#creating-a-password-grant-client)
Before your application can issue tokens via the password grant, you will need to create a password grant client. You may do this using the `passport:client` Artisan command with the `--password` option.
```


1php artisan passport:client --password




php artisan passport:client --password

```

### [Requesting Tokens](https://laravel.com/docs/12.x/passport#requesting-password-grant-tokens)
Once you have enabled the grant and have created a password grant client, you may request an access token by issuing a `POST` request to the `/oauth/token` route with the user's email address and password. Remember, this route is already registered by Passport so there is no need to define it manually. If the request is successful, you will receive an `access_token` and `refresh_token` in the JSON response from the server:
```


 1use Illuminate\Support\Facades\Http;




 2 



 3$response = Http::asForm()->post('https://passport-app.test/oauth/token', [




 4    'grant_type' => 'password',




 5    'client_id' => 'your-client-id',




 6    'client_secret' => 'your-client-secret', // Required for confidential clients only...




 7    'username' => 'taylor@laravel.com',




 8    'password' => 'my-password',




 9    'scope' => 'user:read orders:create',




10]);




11 



12return $response->json();




use Illuminate\Support\Facades\Http;

$response = Http::asForm()->post('https://passport-app.test/oauth/token', [
    'grant_type' => 'password',
    'client_id' => 'your-client-id',
    'client_secret' => 'your-client-secret', // Required for confidential clients only...
    'username' => 'taylor@laravel.com',
    'password' => 'my-password',
    'scope' => 'user:read orders:create',
]);

return $response->json();

```

Remember, access tokens are long-lived by default. However, you are free to [configure your maximum access token lifetime](https://laravel.com/docs/12.x/passport#configuration) if needed.
### [Requesting All Scopes](https://laravel.com/docs/12.x/passport#requesting-all-scopes)
When using the password grant or client credentials grant, you may wish to authorize the token for all of the scopes supported by your application. You can do this by requesting the `*` scope. If you request the `*` scope, the `can` method on the token instance will always return `true`. This scope may only be assigned to a token that is issued using the `password` or `client_credentials` grant:
```


 1use Illuminate\Support\Facades\Http;




 2 



 3$response = Http::asForm()->post('https://passport-app.test/oauth/token', [




 4    'grant_type' => 'password',




 5    'client_id' => 'your-client-id',




 6    'client_secret' => 'your-client-secret', // Required for confidential clients only...




 7    'username' => 'taylor@laravel.com',




 8    'password' => 'my-password',




 9    'scope' => '*',




10]);




use Illuminate\Support\Facades\Http;

$response = Http::asForm()->post('https://passport-app.test/oauth/token', [
    'grant_type' => 'password',
    'client_id' => 'your-client-id',
    'client_secret' => 'your-client-secret', // Required for confidential clients only...
    'username' => 'taylor@laravel.com',
    'password' => 'my-password',
    'scope' => '*',
]);

```

### [Customizing the User Provider](https://laravel.com/docs/12.x/passport#customizing-the-user-provider)
If your application uses more than one [authentication user provider](https://laravel.com/docs/12.x/authentication#introduction), you may specify which user provider the password grant client uses by providing a `--provider` option when creating the client via the `artisan passport:client --password` command. The given provider name should match a valid provider defined in your application's `config/auth.php` configuration file. You can then [protect your route using middleware](https://laravel.com/docs/12.x/passport#multiple-authentication-guards) to ensure that only users from the guard's specified provider are authorized.
### [Customizing the Username Field](https://laravel.com/docs/12.x/passport#customizing-the-username-field)
When authenticating using the password grant, Passport will use the `email` attribute of your authenticatable model as the "username". However, you may customize this behavior by defining a `findForPassport` method on your model:
```


 1<?php




 2 



 3namespace App\Models;




 4 



 5use Illuminate\Foundation\Auth\User as Authenticatable;




 6use Illuminate\Notifications\Notifiable;




 7use Laravel\Passport\Bridge\Client;




 8use Laravel\Passport\Contracts\OAuthenticatable;




 9use Laravel\Passport\HasApiTokens;




10 



11class User extends Authenticatable implements OAuthenticatable




12{




13    use HasApiTokens, Notifiable;




14 



15    /**




16     * Find the user instance for the given username.




17     */




18    public function findForPassport(string $username, Client $client): User




19    {




20        return $this->where('username', $username)->first();




21    }




22}




<?php

namespace App\Models;

use Illuminate\Foundation\Auth\User as Authenticatable;
use Illuminate\Notifications\Notifiable;
use Laravel\Passport\Bridge\Client;
use Laravel\Passport\Contracts\OAuthenticatable;
use Laravel\Passport\HasApiTokens;

class User extends Authenticatable implements OAuthenticatable
{
    use HasApiTokens, Notifiable;

    /**
     * Find the user instance for the given username.
     */
    public function findForPassport(string $username, Client $client): User
    {
        return $this->where('username', $username)->first();
    }
}

```

### [Customizing the Password Validation](https://laravel.com/docs/12.x/passport#customizing-the-password-validation)
When authenticating using the password grant, Passport will use the `password` attribute of your model to validate the given password. If your model does not have a `password` attribute or you wish to customize the password validation logic, you can define a `validateForPassportPasswordGrant` method on your model:
```


 1<?php




 2 



 3namespace App\Models;




 4 



 5use Illuminate\Foundation\Auth\User as Authenticatable;




 6use Illuminate\Notifications\Notifiable;




 7use Illuminate\Support\Facades\Hash;




 8use Laravel\Passport\Contracts\OAuthenticatable;




 9use Laravel\Passport\HasApiTokens;




10 



11class User extends Authenticatable implements OAuthenticatable




12{




13    use HasApiTokens, Notifiable;




14 



15    /**




16     * Validate the password of the user for the Passport password grant.




17     */




18    public function validateForPassportPasswordGrant(string $password): bool




19    {




20        return Hash::check($password, $this->password);




21    }




22}




<?php

namespace App\Models;

use Illuminate\Foundation\Auth\User as Authenticatable;
use Illuminate\Notifications\Notifiable;
use Illuminate\Support\Facades\Hash;
use Laravel\Passport\Contracts\OAuthenticatable;
use Laravel\Passport\HasApiTokens;

class User extends Authenticatable implements OAuthenticatable
{
    use HasApiTokens, Notifiable;

    /**
     * Validate the password of the user for the Passport password grant.
     */
    public function validateForPassportPasswordGrant(string $password): bool
    {
        return Hash::check($password, $this->password);
    }
}

```
