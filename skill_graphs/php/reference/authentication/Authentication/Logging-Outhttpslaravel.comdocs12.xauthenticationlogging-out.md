## [Logging Out](https://laravel.com/docs/12.x/authentication#logging-out)
To manually log users out of your application, you may use the `logout` method provided by the `Auth` facade. This will remove the authentication information from the user's session so that subsequent requests are not authenticated.
In addition to calling the `logout` method, it is recommended that you invalidate the user's session and regenerate their [CSRF token](https://laravel.com/docs/12.x/csrf). After logging the user out, you would typically redirect the user to the root of your application:
```


 1use Illuminate\Http\Request;




 2use Illuminate\Http\RedirectResponse;




 3use Illuminate\Support\Facades\Auth;




 4 



 5/**




 6 * Log the user out of the application.




 7 */




 8public function logout(Request $request): RedirectResponse




 9{




10    Auth::logout();




11 



12    $request->session()->invalidate();




13 



14    $request->session()->regenerateToken();




15 



16    return redirect('/');




17}




use Illuminate\Http\Request;
use Illuminate\Http\RedirectResponse;
use Illuminate\Support\Facades\Auth;

/**
 * Log the user out of the application.
 */
public function logout(Request $request): RedirectResponse
{
    Auth::logout();

    $request->session()->invalidate();

    $request->session()->regenerateToken();

    return redirect('/');
}

```

### [Invalidating Sessions on Other Devices](https://laravel.com/docs/12.x/authentication#invalidating-sessions-on-other-devices)
Laravel also provides a mechanism for invalidating and "logging out" a user's sessions that are active on other devices without invalidating the session on their current device. This feature is typically utilized when a user is changing or updating their password and you would like to invalidate sessions on other devices while keeping the current device authenticated.
Before getting started, you should make sure that the `Illuminate\Session\Middleware\AuthenticateSession` middleware is included on the routes that should receive session authentication. Typically, you should place this middleware on a route group definition so that it can be applied to the majority of your application's routes. By default, the `AuthenticateSession` middleware may be attached to a route using the `auth.session` [middleware alias](https://laravel.com/docs/12.x/middleware#middleware-aliases):
```


1Route::middleware(['auth', 'auth.session'])->group(function () {




2    Route::get('/', function () {




3        // ...




4    });




5});




Route::middleware(['auth', 'auth.session'])->group(function () {
    Route::get('/', function () {
        // ...
    });
});

```

Then, you may use the `logoutOtherDevices` method provided by the `Auth` facade. This method requires the user to confirm their current password, which your application should accept through an input form:
```


1use Illuminate\Support\Facades\Auth;




2 



3Auth::logoutOtherDevices($currentPassword);




use Illuminate\Support\Facades\Auth;

Auth::logoutOtherDevices($currentPassword);

```

When the `logoutOtherDevices` method is invoked, the user's other sessions will be invalidated entirely, meaning they will be "logged out" of all guards they were previously authenticated by.
