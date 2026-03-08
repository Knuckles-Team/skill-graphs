## [Password Confirmation](https://laravel.com/docs/12.x/authentication#password-confirmation)
While building your application, you may occasionally have actions that should require the user to confirm their password before the action is performed or before the user is redirected to a sensitive area of the application. Laravel includes built-in middleware to make this process a breeze. Implementing this feature will require you to define two routes: one route to display a view asking the user to confirm their password and another route to confirm that the password is valid and redirect the user to their intended destination.
The following documentation discusses how to integrate with Laravel's password confirmation features directly; however, if you would like to get started more quickly, the [Laravel application starter kits](https://laravel.com/docs/12.x/starter-kits) include support for this feature!
### [Configuration](https://laravel.com/docs/12.x/authentication#password-confirmation-configuration)
After confirming their password, a user will not be asked to confirm their password again for three hours. However, you may configure the length of time before the user is re-prompted for their password by changing the value of the `password_timeout` configuration value within your application's `config/auth.php` configuration file.
### [Routing](https://laravel.com/docs/12.x/authentication#password-confirmation-routing)
#### [The Password Confirmation Form](https://laravel.com/docs/12.x/authentication#the-password-confirmation-form)
First, we will define a route to display a view that requests the user to confirm their password:
```


1Route::get('/confirm-password', function () {




2    return view('auth.confirm-password');




3})->middleware('auth')->name('password.confirm');




Route::get('/confirm-password', function () {
    return view('auth.confirm-password');
})->middleware('auth')->name('password.confirm');

```

As you might expect, the view that is returned by this route should have a form containing a `password` field. In addition, feel free to include text within the view that explains that the user is entering a protected area of the application and must confirm their password.
#### [Confirming the Password](https://laravel.com/docs/12.x/authentication#confirming-the-password)
Next, we will define a route that will handle the form request from the "confirm password" view. This route will be responsible for validating the password and redirecting the user to their intended destination:
```


 1use Illuminate\Http\Request;




 2use Illuminate\Support\Facades\Hash;




 3 



 4Route::post('/confirm-password', function (Request $request) {




 5    if (! Hash::check($request->password, $request->user()->password)) {




 6        return back()->withErrors([




 7            'password' => ['The provided password does not match our records.']




 8        ]);




 9    }




10 



11    $request->session()->passwordConfirmed();




12 



13    return redirect()->intended();




14})->middleware(['auth', 'throttle:6,1']);




use Illuminate\Http\Request;
use Illuminate\Support\Facades\Hash;

Route::post('/confirm-password', function (Request $request) {
    if (! Hash::check($request->password, $request->user()->password)) {
        return back()->withErrors([
            'password' => ['The provided password does not match our records.']
        ]);
    }

    $request->session()->passwordConfirmed();

    return redirect()->intended();
})->middleware(['auth', 'throttle:6,1']);

```

Before moving on, let's examine this route in more detail. First, the request's `password` field is determined to actually match the authenticated user's password. If the password is valid, we need to inform Laravel's session that the user has confirmed their password. The `passwordConfirmed` method will set a timestamp in the user's session that Laravel can use to determine when the user last confirmed their password. Finally, we can redirect the user to their intended destination.
### [Protecting Routes](https://laravel.com/docs/12.x/authentication#password-confirmation-protecting-routes)
You should ensure that any route that performs an action which requires recent password confirmation is assigned the `password.confirm` middleware. This middleware is included with the default installation of Laravel and will automatically store the user's intended destination in the session so that the user may be redirected to that location after confirming their password. After storing the user's intended destination in the session, the middleware will redirect the user to the `password.confirm` [named route](https://laravel.com/docs/12.x/routing#named-routes):
```


1Route::get('/settings', function () {




2    // ...




3})->middleware(['password.confirm']);




4 



5Route::post('/settings', function () {




6    // ...




7})->middleware(['password.confirm']);




Route::get('/settings', function () {
    // ...
})->middleware(['password.confirm']);

Route::post('/settings', function () {
    // ...
})->middleware(['password.confirm']);

```
