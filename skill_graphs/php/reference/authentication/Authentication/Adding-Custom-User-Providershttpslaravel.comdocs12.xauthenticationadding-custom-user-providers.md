## [Adding Custom User Providers](https://laravel.com/docs/12.x/authentication#adding-custom-user-providers)
If you are not using a traditional relational database to store your users, you will need to extend Laravel with your own authentication user provider. We will use the `provider` method on the `Auth` facade to define a custom user provider. The user provider resolver should return an implementation of `Illuminate\Contracts\Auth\UserProvider`:
```


 1<?php




 2 



 3namespace App\Providers;




 4 



 5use App\Extensions\MongoUserProvider;




 6use Illuminate\Contracts\Foundation\Application;




 7use Illuminate\Support\Facades\Auth;




 8use Illuminate\Support\ServiceProvider;




 9 



10class AppServiceProvider extends ServiceProvider




11{




12    // ...




13 



14    /**




15     * Bootstrap any application services.




16     */




17    public function boot(): void




18    {




19        Auth::provider('mongo', function (Application $app, array $config) {




20            // Return an instance of Illuminate\Contracts\Auth\UserProvider...




21 



22            return new MongoUserProvider($app->make('mongo.connection'));




23        });




24    }




25}




<?php

namespace App\Providers;

use App\Extensions\MongoUserProvider;
use Illuminate\Contracts\Foundation\Application;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\ServiceProvider;

class AppServiceProvider extends ServiceProvider
{
    // ...

    /**
     * Bootstrap any application services.
     */
    public function boot(): void
    {
        Auth::provider('mongo', function (Application $app, array $config) {
            // Return an instance of Illuminate\Contracts\Auth\UserProvider...

            return new MongoUserProvider($app->make('mongo.connection'));
        });
    }
}

```

After you have registered the provider using the `provider` method, you may switch to the new user provider in your `auth.php` configuration file. First, define a `provider` that uses your new driver:
```


1'providers' => [




2    'users' => [




3        'driver' => 'mongo',




4    ],




5],




'providers' => [
    'users' => [
        'driver' => 'mongo',
    ],
],

```

Finally, you may reference this provider in your `guards` configuration:
```


1'guards' => [




2    'web' => [




3        'driver' => 'session',




4        'provider' => 'users',




5    ],




6],




'guards' => [
    'web' => [
        'driver' => 'session',
        'provider' => 'users',
    ],
],

```

### [The User Provider Contract](https://laravel.com/docs/12.x/authentication#the-user-provider-contract)
`Illuminate\Contracts\Auth\UserProvider` implementations are responsible for fetching an `Illuminate\Contracts\Auth\Authenticatable` implementation out of a persistent storage system, such as MySQL, MongoDB, etc. These two interfaces allow the Laravel authentication mechanisms to continue functioning regardless of how the user data is stored or what type of class is used to represent the authenticated user:
Let's take a look at the `Illuminate\Contracts\Auth\UserProvider` contract:
```


 1<?php




 2 



 3namespace Illuminate\Contracts\Auth;




 4 



 5interface UserProvider




 6{




 7    public function retrieveById($identifier);




 8    public function retrieveByToken($identifier, $token);




 9    public function updateRememberToken(Authenticatable $user, $token);




10    public function retrieveByCredentials(array $credentials);




11    public function validateCredentials(Authenticatable $user, array $credentials);




12    public function rehashPasswordIfRequired(Authenticatable $user, array $credentials, bool $force = false);




13}




<?php

namespace Illuminate\Contracts\Auth;

interface UserProvider
{
    public function retrieveById($identifier);
    public function retrieveByToken($identifier, $token);
    public function updateRememberToken(Authenticatable $user, $token);
    public function retrieveByCredentials(array $credentials);
    public function validateCredentials(Authenticatable $user, array $credentials);
    public function rehashPasswordIfRequired(Authenticatable $user, array $credentials, bool $force = false);
}

```

The `retrieveById` function typically receives a key representing the user, such as an auto-incrementing ID from a MySQL database. The `Authenticatable` implementation matching the ID should be retrieved and returned by the method.
The `retrieveByToken` function retrieves a user by their unique `$identifier` and "remember me" `$token`, typically stored in a database column like `remember_token`. As with the previous method, the `Authenticatable` implementation with a matching token value should be returned by this method.
The `updateRememberToken` method updates the `$user` instance's `remember_token` with the new `$token`. A fresh token is assigned to users on a successful "remember me" authentication attempt or when the user is logging out.
The `retrieveByCredentials` method receives the array of credentials passed to the `Auth::attempt` method when attempting to authenticate with an application. The method should then "query" the underlying persistent storage for the user matching those credentials. Typically, this method will run a query with a "where" condition that searches for a user record with a "username" matching the value of `$credentials['username']`. The method should return an implementation of `Authenticatable`. **This method should not attempt to do any password validation or authentication.**
The `validateCredentials` method should compare the given `$user` with the `$credentials` to authenticate the user. For example, this method will typically use the `Hash::check` method to compare the value of `$user->getAuthPassword()` to the value of `$credentials['password']`. This method should return `true` or `false` indicating whether the password is valid.
The `rehashPasswordIfRequired` method should rehash the given `$user`'s password if required and supported. For example, this method will typically use the `Hash::needsRehash` method to determine if the `$credentials['password']` value needs to be rehashed. If the password needs to be rehashed, the method should use the `Hash::make` method to rehash the password and update the user's record in the underlying persistent storage.
### [The Authenticatable Contract](https://laravel.com/docs/12.x/authentication#the-authenticatable-contract)
Now that we have explored each of the methods on the `UserProvider`, let's take a look at the `Authenticatable` contract. Remember, user providers should return implementations of this interface from the `retrieveById`, `retrieveByToken`, and `retrieveByCredentials` methods:
```


 1<?php




 2 



 3namespace Illuminate\Contracts\Auth;




 4 



 5interface Authenticatable




 6{




 7    public function getAuthIdentifierName();




 8    public function getAuthIdentifier();




 9    public function getAuthPasswordName();




10    public function getAuthPassword();




11    public function getRememberToken();




12    public function setRememberToken($value);




13    public function getRememberTokenName();




14}




<?php

namespace Illuminate\Contracts\Auth;

interface Authenticatable
{
    public function getAuthIdentifierName();
    public function getAuthIdentifier();
    public function getAuthPasswordName();
    public function getAuthPassword();
    public function getRememberToken();
    public function setRememberToken($value);
    public function getRememberTokenName();
}

```

This interface is simple. The `getAuthIdentifierName` method should return the name of the "primary key" column for the user and the `getAuthIdentifier` method should return the "primary key" of the user. When using a MySQL back-end, this would likely be the auto-incrementing primary key assigned to the user record. The `getAuthPasswordName` method should return the name of the user's password column. The `getAuthPassword` method should return the user's hashed password.
This interface allows the authentication system to work with any "user" class, regardless of what ORM or storage abstraction layer you are using. By default, Laravel includes an `App\Models\User` class in the `app/Models` directory which implements this interface.
