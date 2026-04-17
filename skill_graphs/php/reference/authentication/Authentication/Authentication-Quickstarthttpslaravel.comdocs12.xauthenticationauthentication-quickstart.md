## [Authentication Quickstart](https://laravel.com/docs/12.x/authentication#authentication-quickstart)
This portion of the documentation discusses authenticating users via the [Laravel application starter kits](https://laravel.com/docs/12.x/starter-kits), which includes UI scaffolding to help you get started quickly. If you would like to integrate with Laravel's authentication systems directly, check out the documentation on [manually authenticating users](https://laravel.com/docs/12.x/authentication#authenticating-users).
### [Install a Starter Kit](https://laravel.com/docs/12.x/authentication#install-a-starter-kit)
First, you should [install a Laravel application starter kit](https://laravel.com/docs/12.x/starter-kits). Our starter kits offer beautifully designed starting points for incorporating authentication into your fresh Laravel application.
### [Retrieving the Authenticated User](https://laravel.com/docs/12.x/authentication#retrieving-the-authenticated-user)
After creating an application from a starter kit and allowing users to register and authenticate with your application, you will often need to interact with the currently authenticated user. While handling an incoming request, you may access the authenticated user via the `Auth` facade's `user` method:
```


1use Illuminate\Support\Facades\Auth;




2 



3// Retrieve the currently authenticated user...




4$user = Auth::user();




5 



6// Retrieve the currently authenticated user's ID...




7$id = Auth::id();




use Illuminate\Support\Facades\Auth;

// Retrieve the currently authenticated user...
$user = Auth::user();

// Retrieve the currently authenticated user's ID...
$id = Auth::id();

```

Alternatively, once a user is authenticated, you may access the authenticated user via an `Illuminate\Http\Request` instance. Remember, type-hinted classes will automatically be injected into your controller methods. By type-hinting the `Illuminate\Http\Request` object, you may gain convenient access to the authenticated user from any controller method in your application via the request's `user` method:
```


 1<?php




 2 



 3namespace App\Http\Controllers;




 4 



 5use Illuminate\Http\RedirectResponse;




 6use Illuminate\Http\Request;




 7 



 8class FlightController extends Controller




 9{




10    /**




11     * Update the flight information for an existing flight.




12     */




13    public function update(Request $request): RedirectResponse




14    {




15        $user = $request->user();




16 



17        // ...




18 



19        return redirect('/flights');




20    }




21}




<?php

namespace App\Http\Controllers;

use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;

class FlightController extends Controller
{
    /**
     * Update the flight information for an existing flight.
     */
    public function update(Request $request): RedirectResponse
    {
        $user = $request->user();

        // ...

        return redirect('/flights');
    }
}

```

#### [Determining if the Current User is Authenticated](https://laravel.com/docs/12.x/authentication#determining-if-the-current-user-is-authenticated)
To determine if the user making the incoming HTTP request is authenticated, you may use the `check` method on the `Auth` facade. This method will return `true` if the user is authenticated:
```


1use Illuminate\Support\Facades\Auth;




2 



3if (Auth::check()) {




4    // The user is logged in...




5}




use Illuminate\Support\Facades\Auth;

if (Auth::check()) {
    // The user is logged in...
}

```

Even though it is possible to determine if a user is authenticated using the `check` method, you will typically use a middleware to verify that the user is authenticated before allowing the user access to certain routes / controllers. To learn more about this, check out the documentation on [protecting routes](https://laravel.com/docs/12.x/authentication#protecting-routes).
### [Protecting Routes](https://laravel.com/docs/12.x/authentication#protecting-routes)
[Route middleware](https://laravel.com/docs/12.x/middleware) can be used to only allow authenticated users to access a given route. Laravel ships with an `auth` middleware, which is a [middleware alias](https://laravel.com/docs/12.x/middleware#middleware-aliases) for the `Illuminate\Auth\Middleware\Authenticate` class. Since this middleware is already aliased internally by Laravel, all you need to do is attach the middleware to a route definition:
```


1Route::get('/flights', function () {




2    // Only authenticated users may access this route...




3})->middleware('auth');




Route::get('/flights', function () {
    // Only authenticated users may access this route...
})->middleware('auth');

```

#### [Redirecting Unauthenticated Users](https://laravel.com/docs/12.x/authentication#redirecting-unauthenticated-users)
When the `auth` middleware detects an unauthenticated user, it will redirect the user to the `login` [named route](https://laravel.com/docs/12.x/routing#named-routes). You may modify this behavior using the `redirectGuestsTo` method within your application's `bootstrap/app.php` file:
```


1use Illuminate\Http\Request;




2 



3->withMiddleware(function (Middleware $middleware): void {




4    $middleware->redirectGuestsTo('/login');




5 



6    // Using a closure...




7    $middleware->redirectGuestsTo(fn (Request $request) => route('login'));




8})




use Illuminate\Http\Request;

->withMiddleware(function (Middleware $middleware): void {
    $middleware->redirectGuestsTo('/login');

    // Using a closure...
    $middleware->redirectGuestsTo(fn (Request $request) => route('login'));
})

```

#### [Redirecting Authenticated Users](https://laravel.com/docs/12.x/authentication#redirecting-authenticated-users)
When the `guest` middleware detects an authenticated user, it will redirect the user to the `dashboard` or `home` named route. You may modify this behavior using the `redirectUsersTo` method within your application's `bootstrap/app.php` file:
```


1use Illuminate\Http\Request;




2 



3->withMiddleware(function (Middleware $middleware): void {




4    $middleware->redirectUsersTo('/panel');




5 



6    // Using a closure...




7    $middleware->redirectUsersTo(fn (Request $request) => route('panel'));




8})




use Illuminate\Http\Request;

->withMiddleware(function (Middleware $middleware): void {
    $middleware->redirectUsersTo('/panel');

    // Using a closure...
    $middleware->redirectUsersTo(fn (Request $request) => route('panel'));
})

```

#### [Specifying a Guard](https://laravel.com/docs/12.x/authentication#specifying-a-guard)
When attaching the `auth` middleware to a route, you may also specify which "guard" should be used to authenticate the user. The guard specified should correspond to one of the keys in the `guards` array of your `auth.php` configuration file:
```


1Route::get('/flights', function () {




2    // Only authenticated users may access this route...




3})->middleware('auth:admin');




Route::get('/flights', function () {
    // Only authenticated users may access this route...
})->middleware('auth:admin');

```

### [Login Throttling](https://laravel.com/docs/12.x/authentication#login-throttling)
If you are using one of our [application starter kits](https://laravel.com/docs/12.x/starter-kits), rate limiting will automatically be applied to login attempts. By default, the user will not be able to login for one minute if they fail to provide the correct credentials after several attempts. The throttling is unique to the user's username / email address and their IP address.
If you would like to rate limit other routes in your application, check out the [rate limiting documentation](https://laravel.com/docs/12.x/routing#rate-limiting).
