## [Personal Access Tokens](https://laravel.com/docs/12.x/passport#personal-access-tokens)
Sometimes, your users may want to issue access tokens to themselves without going through the typical authorization code redirect flow. Allowing users to issue tokens to themselves via your application's UI can be useful for allowing users to experiment with your API or may serve as a simpler approach to issuing access tokens in general.
If your application is using Passport primarily to issue personal access tokens, consider using [Laravel Sanctum](https://laravel.com/docs/12.x/sanctum), Laravel's light-weight first-party library for issuing API access tokens.
### [Creating a Personal Access Client](https://laravel.com/docs/12.x/passport#creating-a-personal-access-client)
Before your application can issue personal access tokens, you will need to create a personal access client. You may do this by executing the `passport:client` Artisan command with the `--personal` option. If you have already run the `passport:install` command, you do not need to run this command:
```


1php artisan passport:client --personal




php artisan passport:client --personal

```

### [Customizing the User Provider](https://laravel.com/docs/12.x/passport#customizing-the-user-provider-for-pat)
If your application uses more than one [authentication user provider](https://laravel.com/docs/12.x/authentication#introduction), you may specify which user provider the personal access grant client uses by providing a `--provider` option when creating the client via the `artisan passport:client --personal` command. The given provider name should match a valid provider defined in your application's `config/auth.php` configuration file. You can then [protect your route using middleware](https://laravel.com/docs/12.x/passport#multiple-authentication-guards) to ensure that only users from the guard's specified provider are authorized.
### [Managing Personal Access Tokens](https://laravel.com/docs/12.x/passport#managing-personal-access-tokens)
Once you have created a personal access client, you may issue tokens for a given user using the `createToken` method on the `App\Models\User` model instance. The `createToken` method accepts the name of the token as its first argument and an optional array of [scopes](https://laravel.com/docs/12.x/passport#token-scopes) as its second argument:
```


 1use App\Models\User;




 2use Illuminate\Support\Facades\Date;




 3use Laravel\Passport\Token;




 4 



 5$user = User::find($userId);




 6 



 7// Creating a token without scopes...




 8$token = $user->createToken('My Token')->accessToken;




 9 



10// Creating a token with scopes...




11$token = $user->createToken('My Token', ['user:read', 'orders:create'])->accessToken;




12 



13// Creating a token with all scopes...




14$token = $user->createToken('My Token', ['*'])->accessToken;




15 



16// Retrieving all the valid personal access tokens that belong to the user...




17$tokens = $user->tokens()




18    ->with('client')




19    ->where('revoked', false)




20    ->where('expires_at', '>', Date::now())




21    ->get()




22    ->filter(fn (Token $token) => $token->client->hasGrantType('personal_access'));




use App\Models\User;
use Illuminate\Support\Facades\Date;
use Laravel\Passport\Token;

$user = User::find($userId);

// Creating a token without scopes...
$token = $user->createToken('My Token')->accessToken;

// Creating a token with scopes...
$token = $user->createToken('My Token', ['user:read', 'orders:create'])->accessToken;

// Creating a token with all scopes...
$token = $user->createToken('My Token', ['*'])->accessToken;

// Retrieving all the valid personal access tokens that belong to the user...
$tokens = $user->tokens()
    ->with('client')
    ->where('revoked', false)
    ->where('expires_at', '>', Date::now())
    ->get()
    ->filter(fn (Token $token) => $token->client->hasGrantType('personal_access'));

```
