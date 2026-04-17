## [Writing Policies](https://laravel.com/docs/12.x/authorization#writing-policies)
### [Policy Methods](https://laravel.com/docs/12.x/authorization#policy-methods)
Once the policy class has been registered, you may add methods for each action it authorizes. For example, let's define an `update` method on our `PostPolicy` which determines if a given `App\Models\User` can update a given `App\Models\Post` instance.
The `update` method will receive a `User` and a `Post` instance as its arguments, and should return `true` or `false` indicating whether the user is authorized to update the given `Post`. So, in this example, we will verify that the user's `id` matches the `user_id` on the post:
```


 1<?php




 2 



 3namespace App\Policies;




 4 



 5use App\Models\Post;




 6use App\Models\User;




 7 



 8class PostPolicy




 9{




10    /**




11     * Determine if the given post can be updated by the user.




12     */




13    public function update(User $user, Post $post): bool




14    {




15        return $user->id === $post->user_id;




16    }




17}




<?php

namespace App\Policies;

use App\Models\Post;
use App\Models\User;

class PostPolicy
{
    /**
     * Determine if the given post can be updated by the user.
     */
    public function update(User $user, Post $post): bool
    {
        return $user->id === $post->user_id;
    }
}

```

You may continue to define additional methods on the policy as needed for the various actions it authorizes. For example, you might define `view` or `delete` methods to authorize various `Post` related actions, but remember you are free to give your policy methods any name you like.
If you used the `--model` option when generating your policy via the Artisan console, it will already contain methods for the `viewAny`, `view`, `create`, `update`, `delete`, `restore`, and `forceDelete` actions.
All policies are resolved via the Laravel [service container](https://laravel.com/docs/12.x/container), allowing you to type-hint any needed dependencies in the policy's constructor to have them automatically injected.
### [Policy Responses](https://laravel.com/docs/12.x/authorization#policy-responses)
So far, we have only examined policy methods that return simple boolean values. However, sometimes you may wish to return a more detailed response, including an error message. To do so, you may return an `Illuminate\Auth\Access\Response` instance from your policy method:
```


 1use App\Models\Post;




 2use App\Models\User;




 3use Illuminate\Auth\Access\Response;




 4 



 5/**




 6 * Determine if the given post can be updated by the user.




 7 */




 8public function update(User $user, Post $post): Response




 9{




10    return $user->id === $post->user_id




11        ? Response::allow()




12        : Response::deny('You do not own this post.');




13}




use App\Models\Post;
use App\Models\User;
use Illuminate\Auth\Access\Response;

/**
 * Determine if the given post can be updated by the user.
 */
public function update(User $user, Post $post): Response
{
    return $user->id === $post->user_id
        ? Response::allow()
        : Response::deny('You do not own this post.');
}

```

When returning an authorization response from your policy, the `Gate::allows` method will still return a simple boolean value; however, you may use the `Gate::inspect` method to get the full authorization response returned by the gate:
```


1use Illuminate\Support\Facades\Gate;




2 



3$response = Gate::inspect('update', $post);




4 



5if ($response->allowed()) {




6    // The action is authorized...




7} else {




8    echo $response->message();




9}




use Illuminate\Support\Facades\Gate;

$response = Gate::inspect('update', $post);

if ($response->allowed()) {
    // The action is authorized...
} else {
    echo $response->message();
}

```

When using the `Gate::authorize` method, which throws an `AuthorizationException` if the action is not authorized, the error message provided by the authorization response will be propagated to the HTTP response:
```


1Gate::authorize('update', $post);




2 



3// The action is authorized...




Gate::authorize('update', $post);

// The action is authorized...

```

#### [Customizing the HTTP Response Status](https://laravel.com/docs/12.x/authorization#customizing-policy-response-status)
When an action is denied via a policy method, a `403` HTTP response is returned; however, it can sometimes be useful to return an alternative HTTP status code. You may customize the HTTP status code returned for a failed authorization check using the `denyWithStatus` static constructor on the `Illuminate\Auth\Access\Response` class:
```


 1use App\Models\Post;




 2use App\Models\User;




 3use Illuminate\Auth\Access\Response;




 4 



 5/**




 6 * Determine if the given post can be updated by the user.




 7 */




 8public function update(User $user, Post $post): Response




 9{




10    return $user->id === $post->user_id




11        ? Response::allow()




12        : Response::denyWithStatus(404);




13}




use App\Models\Post;
use App\Models\User;
use Illuminate\Auth\Access\Response;

/**
 * Determine if the given post can be updated by the user.
 */
public function update(User $user, Post $post): Response
{
    return $user->id === $post->user_id
        ? Response::allow()
        : Response::denyWithStatus(404);
}

```

Because hiding resources via a `404` response is such a common pattern for web applications, the `denyAsNotFound` method is offered for convenience:
```


 1use App\Models\Post;




 2use App\Models\User;




 3use Illuminate\Auth\Access\Response;




 4 



 5/**




 6 * Determine if the given post can be updated by the user.




 7 */




 8public function update(User $user, Post $post): Response




 9{




10    return $user->id === $post->user_id




11        ? Response::allow()




12        : Response::denyAsNotFound();




13}




use App\Models\Post;
use App\Models\User;
use Illuminate\Auth\Access\Response;

/**
 * Determine if the given post can be updated by the user.
 */
public function update(User $user, Post $post): Response
{
    return $user->id === $post->user_id
        ? Response::allow()
        : Response::denyAsNotFound();
}

```

### [Methods Without Models](https://laravel.com/docs/12.x/authorization#methods-without-models)
Some policy methods only receive an instance of the currently authenticated user. This situation is most common when authorizing `create` actions. For example, if you are creating a blog, you may wish to determine if a user is authorized to create any posts at all. In these situations, your policy method should only expect to receive a user instance:
```


1/**




2 * Determine if the given user can create posts.




3 */




4public function create(User $user): bool




5{




6    return $user->role == 'writer';




7}




/**
 * Determine if the given user can create posts.
 */
public function create(User $user): bool
{
    return $user->role == 'writer';
}

```

### [Guest Users](https://laravel.com/docs/12.x/authorization#guest-users)
By default, all gates and policies automatically return `false` if the incoming HTTP request was not initiated by an authenticated user. However, you may allow these authorization checks to pass through to your gates and policies by declaring an "optional" type-hint or supplying a `null` default value for the user argument definition:
```


 1<?php




 2 



 3namespace App\Policies;




 4 



 5use App\Models\Post;




 6use App\Models\User;




 7 



 8class PostPolicy




 9{




10    /**




11     * Determine if the given post can be updated by the user.




12     */




13    public function update(?User $user, Post $post): bool




14    {




15        return $user?->id === $post->user_id;




16    }




17}




<?php

namespace App\Policies;

use App\Models\Post;
use App\Models\User;

class PostPolicy
{
    /**
     * Determine if the given post can be updated by the user.
     */
    public function update(?User $user, Post $post): bool
    {
        return $user?->id === $post->user_id;
    }
}

```

### [Policy Filters](https://laravel.com/docs/12.x/authorization#policy-filters)
For certain users, you may wish to authorize all actions within a given policy. To accomplish this, define a `before` method on the policy. The `before` method will be executed before any other methods on the policy, giving you an opportunity to authorize the action before the intended policy method is actually called. This feature is most commonly used for authorizing application administrators to perform any action:
```


 1use App\Models\User;




 2 



 3/**




 4 * Perform pre-authorization checks.




 5 */




 6public function before(User $user, string $ability): bool|null




 7{




 8    if ($user->isAdministrator()) {




 9        return true;




10    }




11 



12    return null;




13}




use App\Models\User;

/**
 * Perform pre-authorization checks.
 */
public function before(User $user, string $ability): bool|null
{
    if ($user->isAdministrator()) {
        return true;
    }

    return null;
}

```

If you would like to deny all authorization checks for a particular type of user then you may return `false` from the `before` method. If `null` is returned, the authorization check will fall through to the policy method.
The `before` method of a policy class will not be called if the class doesn't contain a method with a name matching the name of the ability being checked.
