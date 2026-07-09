## [Gates](https://laravel.com/docs/12.x/authorization#gates)
### [Writing Gates](https://laravel.com/docs/12.x/authorization#writing-gates)
Gates are a great way to learn the basics of Laravel's authorization features; however, when building robust Laravel applications you should consider using [policies](https://laravel.com/docs/12.x/authorization#creating-policies) to organize your authorization rules.
Gates are simply closures that determine if a user is authorized to perform a given action. Typically, gates are defined within the `boot` method of the `App\Providers\AppServiceProvider` class using the `Gate` facade. Gates always receive a user instance as their first argument and may optionally receive additional arguments such as a relevant Eloquent model.
In this example, we'll define a gate to determine if a user can update a given `App\Models\Post` model. The gate will accomplish this by comparing the user's `id` against the `user_id` of the user that created the post:
```


 1use App\Models\Post;




 2use App\Models\User;




 3use Illuminate\Support\Facades\Gate;




 4 



 5/**




 6 * Bootstrap any application services.




 7 */




 8public function boot(): void




 9{




10    Gate::define('update-post', function (User $user, Post $post) {




11        return $user->id === $post->user_id;




12    });




13}




use App\Models\Post;
use App\Models\User;
use Illuminate\Support\Facades\Gate;

/**
 * Bootstrap any application services.
 */
public function boot(): void
{
    Gate::define('update-post', function (User $user, Post $post) {
        return $user->id === $post->user_id;
    });
}

```

Like controllers, gates may also be defined using a class callback array:
```


 1use App\Policies\PostPolicy;




 2use Illuminate\Support\Facades\Gate;




 3 



 4/**




 5 * Bootstrap any application services.




 6 */




 7public function boot(): void




 8{




 9    Gate::define('update-post', [PostPolicy::class, 'update']);




10}




use App\Policies\PostPolicy;
use Illuminate\Support\Facades\Gate;

/**
 * Bootstrap any application services.
 */
public function boot(): void
{
    Gate::define('update-post', [PostPolicy::class, 'update']);
}

```

### [Authorizing Actions](https://laravel.com/docs/12.x/authorization#authorizing-actions-via-gates)
To authorize an action using gates, you should use the `allows` or `denies` methods provided by the `Gate` facade. Note that you are not required to pass the currently authenticated user to these methods. Laravel will automatically take care of passing the user into the gate closure. It is typical to call the gate authorization methods within your application's controllers before performing an action that requires authorization:
```


 1<?php




 2 



 3namespace App\Http\Controllers;




 4 



 5use App\Models\Post;




 6use Illuminate\Http\RedirectResponse;




 7use Illuminate\Http\Request;




 8use Illuminate\Support\Facades\Gate;




 9 



10class PostController extends Controller




11{




12    /**




13     * Update the given post.




14     */




15    public function update(Request $request, Post $post): RedirectResponse




16    {




17        if (! Gate::allows('update-post', $post)) {




18            abort(403);




19        }




20 



21        // Update the post...




22 



23        return redirect('/posts');




24    }




25}




<?php

namespace App\Http\Controllers;

use App\Models\Post;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Gate;

class PostController extends Controller
{
    /**
     * Update the given post.
     */
    public function update(Request $request, Post $post): RedirectResponse
    {
        if (! Gate::allows('update-post', $post)) {
            abort(403);
        }

        // Update the post...

        return redirect('/posts');
    }
}

```

If you would like to determine if a user other than the currently authenticated user is authorized to perform an action, you may use the `forUser` method on the `Gate` facade:
```


1if (Gate::forUser($user)->allows('update-post', $post)) {




2    // The user can update the post...




3}




4 



5if (Gate::forUser($user)->denies('update-post', $post)) {




6    // The user can't update the post...




7}




if (Gate::forUser($user)->allows('update-post', $post)) {
    // The user can update the post...
}

if (Gate::forUser($user)->denies('update-post', $post)) {
    // The user can't update the post...
}

```

You may authorize multiple actions at a time using the `any` or `none` methods:
```


1if (Gate::any(['update-post', 'delete-post'], $post)) {




2    // The user can update or delete the post...




3}




4 



5if (Gate::none(['update-post', 'delete-post'], $post)) {




6    // The user can't update or delete the post...




7}




if (Gate::any(['update-post', 'delete-post'], $post)) {
    // The user can update or delete the post...
}

if (Gate::none(['update-post', 'delete-post'], $post)) {
    // The user can't update or delete the post...
}

```

#### [Authorizing or Throwing Exceptions](https://laravel.com/docs/12.x/authorization#authorizing-or-throwing-exceptions)
If you would like to attempt to authorize an action and automatically throw an `Illuminate\Auth\Access\AuthorizationException` if the user is not allowed to perform the given action, you may use the `Gate` facade's `authorize` method. Instances of `AuthorizationException` are automatically converted to a 403 HTTP response by Laravel:
```


1Gate::authorize('update-post', $post);




2 



3// The action is authorized...




Gate::authorize('update-post', $post);

// The action is authorized...

```

#### [Supplying Additional Context](https://laravel.com/docs/12.x/authorization#gates-supplying-additional-context)
The gate methods for authorizing abilities (`allows`, `denies`, `check`, `any`, `none`, `authorize`, `can`, `cannot`) and the authorization [Blade directives](https://laravel.com/docs/12.x/authorization#via-blade-templates) (`@can`, `@cannot`, `@canany`) can receive an array as their second argument. These array elements are passed as parameters to the gate closure, and can be used for additional context when making authorization decisions:
```


 1use App\Models\Category;




 2use App\Models\User;




 3use Illuminate\Support\Facades\Gate;




 4 



 5Gate::define('create-post', function (User $user, Category $category, bool $pinned) {




 6    if (! $user->canPublishToGroup($category->group)) {




 7        return false;




 8    } elseif ($pinned && ! $user->canPinPosts()) {




 9        return false;




10    }




11 



12    return true;




13});




14 



15if (Gate::check('create-post', [$category, $pinned])) {




16    // The user can create the post...




17}




use App\Models\Category;
use App\Models\User;
use Illuminate\Support\Facades\Gate;

Gate::define('create-post', function (User $user, Category $category, bool $pinned) {
    if (! $user->canPublishToGroup($category->group)) {
        return false;
    } elseif ($pinned && ! $user->canPinPosts()) {
        return false;
    }

    return true;
});

if (Gate::check('create-post', [$category, $pinned])) {
    // The user can create the post...
}

```

### [Gate Responses](https://laravel.com/docs/12.x/authorization#gate-responses)
So far, we have only examined gates that return simple boolean values. However, sometimes you may wish to return a more detailed response, including an error message. To do so, you may return an `Illuminate\Auth\Access\Response` from your gate:
```


1use App\Models\User;




2use Illuminate\Auth\Access\Response;




3use Illuminate\Support\Facades\Gate;




4 



5Gate::define('edit-settings', function (User $user) {




6    return $user->isAdmin




7        ? Response::allow()




8        : Response::deny('You must be an administrator.');




9});




use App\Models\User;
use Illuminate\Auth\Access\Response;
use Illuminate\Support\Facades\Gate;

Gate::define('edit-settings', function (User $user) {
    return $user->isAdmin
        ? Response::allow()
        : Response::deny('You must be an administrator.');
});

```

Even when you return an authorization response from your gate, the `Gate::allows` method will still return a simple boolean value; however, you may use the `Gate::inspect` method to get the full authorization response returned by the gate:
```


1$response = Gate::inspect('edit-settings');




2 



3if ($response->allowed()) {




4    // The action is authorized...




5} else {




6    echo $response->message();




7}




$response = Gate::inspect('edit-settings');

if ($response->allowed()) {
    // The action is authorized...
} else {
    echo $response->message();
}

```

When using the `Gate::authorize` method, which throws an `AuthorizationException` if the action is not authorized, the error message provided by the authorization response will be propagated to the HTTP response:
```


1Gate::authorize('edit-settings');




2 



3// The action is authorized...




Gate::authorize('edit-settings');

// The action is authorized...

```

#### [Customizing The HTTP Response Status](https://laravel.com/docs/12.x/authorization#customizing-gate-response-status)
When an action is denied via a Gate, a `403` HTTP response is returned; however, it can sometimes be useful to return an alternative HTTP status code. You may customize the HTTP status code returned for a failed authorization check using the `denyWithStatus` static constructor on the `Illuminate\Auth\Access\Response` class:
```


1use App\Models\User;




2use Illuminate\Auth\Access\Response;




3use Illuminate\Support\Facades\Gate;




4 



5Gate::define('edit-settings', function (User $user) {




6    return $user->isAdmin




7        ? Response::allow()




8        : Response::denyWithStatus(404);




9});




use App\Models\User;
use Illuminate\Auth\Access\Response;
use Illuminate\Support\Facades\Gate;

Gate::define('edit-settings', function (User $user) {
    return $user->isAdmin
        ? Response::allow()
        : Response::denyWithStatus(404);
});

```

Because hiding resources via a `404` response is such a common pattern for web applications, the `denyAsNotFound` method is offered for convenience:
```


1use App\Models\User;




2use Illuminate\Auth\Access\Response;




3use Illuminate\Support\Facades\Gate;




4 



5Gate::define('edit-settings', function (User $user) {




6    return $user->isAdmin




7        ? Response::allow()




8        : Response::denyAsNotFound();




9});




use App\Models\User;
use Illuminate\Auth\Access\Response;
use Illuminate\Support\Facades\Gate;

Gate::define('edit-settings', function (User $user) {
    return $user->isAdmin
        ? Response::allow()
        : Response::denyAsNotFound();
});

```

### [Intercepting Gate Checks](https://laravel.com/docs/12.x/authorization#intercepting-gate-checks)
Sometimes, you may wish to grant all abilities to a specific user. You may use the `before` method to define a closure that is run before all other authorization checks:
```


1use App\Models\User;




2use Illuminate\Support\Facades\Gate;




3 



4Gate::before(function (User $user, string $ability) {




5    if ($user->isAdministrator()) {




6        return true;




7    }




8});




use App\Models\User;
use Illuminate\Support\Facades\Gate;

Gate::before(function (User $user, string $ability) {
    if ($user->isAdministrator()) {
        return true;
    }
});

```

If the `before` closure returns a non-null result that result will be considered the result of the authorization check.
You may use the `after` method to define a closure to be executed after all other authorization checks:
```


1use App\Models\User;




2 



3Gate::after(function (User $user, string $ability, bool|null $result, mixed $arguments) {




4    if ($user->isAdministrator()) {




5        return true;




6    }




7});




use App\Models\User;

Gate::after(function (User $user, string $ability, bool|null $result, mixed $arguments) {
    if ($user->isAdministrator()) {
        return true;
    }
});

```

Values returned by `after` closures will not override the result of the authorization check unless the gate or policy returned `null`.
### [Inline Authorization](https://laravel.com/docs/12.x/authorization#inline-authorization)
Occasionally, you may wish to determine if the currently authenticated user is authorized to perform a given action without writing a dedicated gate that corresponds to the action. Laravel allows you to perform these types of "inline" authorization checks via the `Gate::allowIf` and `Gate::denyIf` methods. Inline authorization does not execute any defined ["before" or "after" authorization hooks](https://laravel.com/docs/12.x/authorization#intercepting-gate-checks):
```


1use App\Models\User;




2use Illuminate\Support\Facades\Gate;




3 



4Gate::allowIf(fn (User $user) => $user->isAdministrator());




5 



6Gate::denyIf(fn (User $user) => $user->banned());




use App\Models\User;
use Illuminate\Support\Facades\Gate;

Gate::allowIf(fn (User $user) => $user->isAdministrator());

Gate::denyIf(fn (User $user) => $user->banned());

```

If the action is not authorized or if no user is currently authenticated, Laravel will automatically throw an `Illuminate\Auth\Access\AuthorizationException` exception. Instances of `AuthorizationException` are automatically converted to a 403 HTTP response by Laravel's exception handler.
