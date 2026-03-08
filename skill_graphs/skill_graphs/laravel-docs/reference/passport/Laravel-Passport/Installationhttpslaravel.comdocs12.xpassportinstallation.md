## [Installation](https://laravel.com/docs/12.x/passport#installation)
You may install Laravel Passport via the `install:api` Artisan command:
```


1php artisan install:api --passport




php artisan install:api --passport

```

This command will publish and run the database migrations necessary for creating the tables your application needs to store OAuth2 clients and access tokens. The command will also create the encryption keys required to generate secure access tokens.
After running the `install:api` command, add the `Laravel\Passport\HasApiTokens` trait and `Laravel\Passport\Contracts\OAuthenticatable` interface to your `App\Models\User` model. This trait will provide a few helper methods to your model which allow you to inspect the authenticated user's token and scopes:
```


 1<?php




 2 



 3namespace App\Models;




 4 



 5use Illuminate\Database\Eloquent\Factories\HasFactory;




 6use Illuminate\Foundation\Auth\User as Authenticatable;




 7use Illuminate\Notifications\Notifiable;




 8use Laravel\Passport\Contracts\OAuthenticatable;




 9use Laravel\Passport\HasApiTokens;




10 



11class User extends Authenticatable implements OAuthenticatable




12{




13    use HasApiTokens, HasFactory, Notifiable;




14}




<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Foundation\Auth\User as Authenticatable;
use Illuminate\Notifications\Notifiable;
use Laravel\Passport\Contracts\OAuthenticatable;
use Laravel\Passport\HasApiTokens;

class User extends Authenticatable implements OAuthenticatable
{
    use HasApiTokens, HasFactory, Notifiable;
}

```

Finally, in your application's `config/auth.php` configuration file, you should define an `api` authentication guard and set the `driver` option to `passport`. This will instruct your application to use Passport's `TokenGuard` when authenticating incoming API requests:
```


 1'guards' => [




 2    'web' => [




 3        'driver' => 'session',




 4        'provider' => 'users',




 5    ],




 6 



 7    'api' => [




 8        'driver' => 'passport',




 9        'provider' => 'users',




10    ],




11],




'guards' => [
    'web' => [
        'driver' => 'session',
        'provider' => 'users',
    ],

    'api' => [
        'driver' => 'passport',
        'provider' => 'users',
    ],
],

```

### [Deploying Passport](https://laravel.com/docs/12.x/passport#deploying-passport)
When deploying Passport to your application's servers for the first time, you will likely need to run the `passport:keys` command. This command generates the encryption keys Passport needs in order to generate access tokens. The generated keys are not typically kept in source control:
```


1php artisan passport:keys




php artisan passport:keys

```

If necessary, you may define the path where Passport's keys should be loaded from. You may use the `Passport::loadKeysFrom` method to accomplish this. Typically, this method should be called from the `boot` method of your application's `App\Providers\AppServiceProvider` class:
```


1/**




2 * Bootstrap any application services.




3 */




4public function boot(): void




5{




6    Passport::loadKeysFrom(__DIR__.'/../secrets/oauth');




7}




/**
 * Bootstrap any application services.
 */
public function boot(): void
{
    Passport::loadKeysFrom(__DIR__.'/../secrets/oauth');
}

```

#### [Loading Keys From the Environment](https://laravel.com/docs/12.x/passport#loading-keys-from-the-environment)
Alternatively, you may publish Passport's configuration file using the `vendor:publish` Artisan command:
```


1php artisan vendor:publish --tag=passport-config




php artisan vendor:publish --tag=passport-config

```

After the configuration file has been published, you may load your application's encryption keys by defining them as environment variables:
```


1PASSPORT_PRIVATE_KEY="-----BEGIN RSA PRIVATE KEY-----




2<private key here>




3-----END RSA PRIVATE KEY-----"




4 



5PASSPORT_PUBLIC_KEY="-----BEGIN PUBLIC KEY-----




6<public key here>




7-----END PUBLIC KEY-----"




PASSPORT_PRIVATE_KEY="-----BEGIN RSA PRIVATE KEY-----
<private key here>
-----END RSA PRIVATE KEY-----"

PASSPORT_PUBLIC_KEY="-----BEGIN PUBLIC KEY-----
<public key here>
-----END PUBLIC KEY-----"

```

### [Upgrading Passport](https://laravel.com/docs/12.x/passport#upgrading-passport)
When upgrading to a new major version of Passport, it's important that you carefully review
