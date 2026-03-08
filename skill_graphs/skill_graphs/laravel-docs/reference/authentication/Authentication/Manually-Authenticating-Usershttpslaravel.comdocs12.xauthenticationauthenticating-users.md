## [Manually Authenticating Users](https://laravel.com/docs/12.x/authentication#authenticating-users)
You are not required to use the authentication scaffolding included with Laravel's [application starter kits](https://laravel.com/docs/12.x/starter-kits). If you choose not to use this scaffolding, you will need to manage user authentication using the Laravel authentication classes directly. Don't worry, it's a cinch!
We will access Laravel's authentication services via the `Auth` [facade](https://laravel.com/docs/12.x/facades), so we'll need to make sure to import the `Auth` facade at the top of the class. Next, let's check out the `attempt` method. The `attempt` method is normally used to handle authentication attempts from your application's "login" form. If authentication is successful, you should regenerate the user's [session](https://laravel.com/docs/12.x/session) to prevent
```


 1<?php




 2 



 3namespace App\Http\Controllers;




 4 



 5use Illuminate\Http\Request;




 6use Illuminate\Http\RedirectResponse;




 7use Illuminate\Support\Facades\Auth;




 8 



 9class LoginController extends Controller




10{




11    /**




12     * Handle an authentication attempt.




13     */




14    public function authenticate(Request $request): RedirectResponse




15    {




16        $credentials = $request->validate([




17            'email' => ['required', 'email'],




18            'password' => ['required'],




19        ]);




20 



21        if (Auth::attempt($credentials)) {




22            $request->session()->regenerate();




23 



24            return redirect()->intended('dashboard');




25        }




26 



27        return back()->withErrors([




28            'email' => 'The provided credentials do not match our records.',




29        ])->onlyInput('email');




30    }




31}




<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Http\RedirectResponse;
use Illuminate\Support\Facades\Auth;

class LoginController extends Controller
{
    /**
     * Handle an authentication attempt.
     */
    public function authenticate(Request $request): RedirectResponse
    {
        $credentials = $request->validate([
            'email' => ['required', 'email'],
            'password' => ['required'],
        ]);

        if (Auth::attempt($credentials)) {
            $request->session()->regenerate();

            return redirect()->intended('dashboard');
        }

        return back()->withErrors([
            'email' => 'The provided credentials do not match our records.',
        ])->onlyInput('email');
    }
}

```

The `attempt` method accepts an array of key / value pairs as its first argument. The values in the array will be used to find the user in your database table. So, in the example above, the user will be retrieved by the value of the `email` column. If the user is found, the hashed password stored in the database will be compared with the `password` value passed to the method via the array. You should not hash the incoming request's `password` value, since the framework will automatically hash the value before comparing it to the hashed password in the database. An authenticated session will be started for the user if the two hashed passwords match.
Remember, Laravel's authentication services will retrieve users from your database based on your authentication guard's "provider" configuration. In the default `config/auth.php` configuration file, the Eloquent user provider is specified and it is instructed to use the `App\Models\User` model when retrieving users. You may change these values within your configuration file based on the needs of your application.
The `attempt` method will return `true` if authentication was successful. Otherwise, `false` will be returned.
The `intended` method provided by Laravel's redirector will redirect the user to the URL they were attempting to access before being intercepted by the authentication middleware. A fallback URI may be given to this method in case the intended destination is not available.
#### [Specifying Additional Conditions](https://laravel.com/docs/12.x/authentication#specifying-additional-conditions)
If you wish, you may also add extra query conditions to the authentication query in addition to the user's email and password. To accomplish this, we may simply add the query conditions to the array passed to the `attempt` method. For example, we may verify that the user is marked as "active":
```


1if (Auth::attempt(['email' => $email, 'password' => $password, 'active' => 1])) {




2    // Authentication was successful...




3}




if (Auth::attempt(['email' => $email, 'password' => $password, 'active' => 1])) {
    // Authentication was successful...
}

```

For complex query conditions, you may provide a closure in your array of credentials. This closure will be invoked with the query instance, allowing you to customize the query based on your application's needs:
```


1use Illuminate\Database\Eloquent\Builder;




2 



3if (Auth::attempt([




4    'email' => $email,




5    'password' => $password,




6    fn (Builder $query) => $query->has('activeSubscription'),




7])) {




8    // Authentication was successful...




9}




use Illuminate\Database\Eloquent\Builder;

if (Auth::attempt([
    'email' => $email,
    'password' => $password,
    fn (Builder $query) => $query->has('activeSubscription'),
])) {
    // Authentication was successful...
}

```

In these examples, `email` is not a required option, it is merely used as an example. You should use whatever column name corresponds to a "username" in your database table.
The `attemptWhen` method, which receives a closure as its second argument, may be used to perform more extensive inspection of the potential user before actually authenticating the user. The closure receives the potential user and should return `true` or `false` to indicate if the user may be authenticated:
```


1if (Auth::attemptWhen([




2    'email' => $email,




3    'password' => $password,




4], function (User $user) {




5    return $user->isNotBanned();




6})) {




7    // Authentication was successful...




8}




if (Auth::attemptWhen([
    'email' => $email,
    'password' => $password,
], function (User $user) {
    return $user->isNotBanned();
})) {
    // Authentication was successful...
}

```

#### [Accessing Specific Guard Instances](https://laravel.com/docs/12.x/authentication#accessing-specific-guard-instances)
Via the `Auth` facade's `guard` method, you may specify which guard instance you would like to utilize when authenticating the user. This allows you to manage authentication for separate parts of your application using entirely separate authenticatable models or user tables.
The guard name passed to the `guard` method should correspond to one of the guards configured in your `auth.php` configuration file:
```


1if (Auth::guard('admin')->attempt($credentials)) {




2    // ...




3}




if (Auth::guard('admin')->attempt($credentials)) {
    // ...
}

```

### [Remembering Users](https://laravel.com/docs/12.x/authentication#remembering-users)
Many web applications provide a "remember me" checkbox on their login form. If you would like to provide "remember me" functionality in your application, you may pass a boolean value as the second argument to the `attempt` method.
When this value is `true`, Laravel will keep the user authenticated indefinitely or until they manually logout. Your `users` table must include the string `remember_token` column, which will be used to store the "remember me" token. The `users` table migration included with new Laravel applications already includes this column:
```


1use Illuminate\Support\Facades\Auth;




2 



3if (Auth::attempt(['email' => $email, 'password' => $password], $remember)) {




4    // The user is being remembered...




5}




use Illuminate\Support\Facades\Auth;

if (Auth::attempt(['email' => $email, 'password' => $password], $remember)) {
    // The user is being remembered...
}

```

If your application offers "remember me" functionality, you may use the `viaRemember` method to determine if the currently authenticated user was authenticated using the "remember me" cookie:
```


1use Illuminate\Support\Facades\Auth;




2 



3if (Auth::viaRemember()) {




4    // ...




5}




use Illuminate\Support\Facades\Auth;

if (Auth::viaRemember()) {
    // ...
}

```

### [Other Authentication Methods](https://laravel.com/docs/12.x/authentication#other-authentication-methods)
#### [Authenticate a User Instance](https://laravel.com/docs/12.x/authentication#authenticate-a-user-instance)
If you need to set an existing user instance as the currently authenticated user, you may pass the user instance to the `Auth` facade's `login` method. The given user instance must be an implementation of the `Illuminate\Contracts\Auth\Authenticatable` [contract](https://laravel.com/docs/12.x/contracts). The `App\Models\User` model included with Laravel already implements this interface. This method of authentication is useful when you already have a valid user instance, such as directly after a user registers with your application:
```


1use Illuminate\Support\Facades\Auth;




2 



3Auth::login($user);




use Illuminate\Support\Facades\Auth;

Auth::login($user);

```

You may pass a boolean value as the second argument to the `login` method. This value indicates if "remember me" functionality is desired for the authenticated session. Remember, this means that the session will be authenticated indefinitely or until the user manually logs out of the application:
```


1Auth::login($user, $remember = true);




Auth::login($user, $remember = true);

```

If needed, you may specify an authentication guard before calling the `login` method:
```


1Auth::guard('admin')->login($user);




Auth::guard('admin')->login($user);

```

#### [Authenticate a User by ID](https://laravel.com/docs/12.x/authentication#authenticate-a-user-by-id)
To authenticate a user using their database record's primary key, you may use the `loginUsingId` method. This method accepts the primary key of the user you wish to authenticate:
```


1Auth::loginUsingId(1);




Auth::loginUsingId(1);

```

You may pass a boolean value to the `remember` argument of the `loginUsingId` method. This value indicates if "remember me" functionality is desired for the authenticated session. Remember, this means that the session will be authenticated indefinitely or until the user manually logs out of the application:
```


1Auth::loginUsingId(1, remember: true);




Auth::loginUsingId(1, remember: true);

```

#### [Authenticate a User Once](https://laravel.com/docs/12.x/authentication#authenticate-a-user-once)
You may use the `once` method to authenticate a user with the application for a single request. No sessions or cookies will be utilized when calling this method, and the `Login` event will not be dispatched:
```


1if (Auth::once($credentials)) {




2    // ...




3}




if (Auth::once($credentials)) {
    // ...
}

```
