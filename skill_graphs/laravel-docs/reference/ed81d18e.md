## [Adding Custom Guards](https://laravel.com/docs/12.x/authentication#adding-custom-guards)
You may define your own authentication guards using the `extend` method on the `Auth` facade. You should place your call to the `extend` method within a [service provider](https://laravel.com/docs/12.x/providers). Since Laravel already ships with an `AppServiceProvider`, we can place the code in that provider:
```


 1<?php




 2 



 3namespace App\Providers;




 4 



 5use App\Services\Auth\JwtGuard;




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




19        Auth::extend('jwt', function (Application $app, string $name, array $config) {




20            // Return an instance of Illuminate\Contracts\Auth\Guard...




21 



22            return new JwtGuard(Auth::createUserProvider($config['provider']));




23        });




24    }




25}




<?php

namespace App\Providers;

use App\Services\Auth\JwtGuard;
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
        Auth::extend('jwt', function (Application $app, string $name, array $config) {
            // Return an instance of Illuminate\Contracts\Auth\Guard...

            return new JwtGuard(Auth::createUserProvider($config['provider']));
        });
    }
}

```

As you can see in the example above, the callback passed to the `extend` method should return an implementation of `Illuminate\Contracts\Auth\Guard`. This interface contains a few methods you will need to implement to define a custom guard. Once your custom guard has been defined, you may reference the guard in the `guards` configuration of your `auth.php` configuration file:
```


1'guards' => [




2    'api' => [




3        'driver' => 'jwt',




4        'provider' => 'users',




5    ],




6],




'guards' => [
    'api' => [
        'driver' => 'jwt',
        'provider' => 'users',
    ],
],

```

### [Closure Request Guards](https://laravel.com/docs/12.x/authentication#closure-request-guards)
The simplest way to implement a custom, HTTP request based authentication system is by using the `Auth::viaRequest` method. This method allows you to quickly define your authentication process using a single closure.
To get started, call the `Auth::viaRequest` method within the `boot` method of your application's `AppServiceProvider`. The `viaRequest` method accepts an authentication driver name as its first argument. This name can be any string that describes your custom guard. The second argument passed to the method should be a closure that receives the incoming HTTP request and returns a user instance or, if authentication fails, `null`:
```


 1use App\Models\User;




 2use Illuminate\Http\Request;




 3use Illuminate\Support\Facades\Auth;




 4 



 5/**




 6 * Bootstrap any application services.




 7 */




 8public function boot(): void




 9{




10    Auth::viaRequest('custom-token', function (Request $request) {




11        return User::where('token', (string) $request->token)->first();




12    });




13}




use App\Models\User;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;

/**
 * Bootstrap any application services.
 */
public function boot(): void
{
    Auth::viaRequest('custom-token', function (Request $request) {
        return User::where('token', (string) $request->token)->first();
    });
}

```

Once your custom authentication driver has been defined, you may configure it as a driver within the `guards` configuration of your `auth.php` configuration file:
```


1'guards' => [




2    'api' => [




3        'driver' => 'custom-token',




4    ],




5],




'guards' => [
    'api' => [
        'driver' => 'custom-token',
    ],
],

```

Finally, you may reference the guard when assigning the authentication middleware to a route:
```


1Route::middleware('auth:api')->group(function () {




2    // ...




3});




Route::middleware('auth:api')->group(function () {
    // ...
});

```
