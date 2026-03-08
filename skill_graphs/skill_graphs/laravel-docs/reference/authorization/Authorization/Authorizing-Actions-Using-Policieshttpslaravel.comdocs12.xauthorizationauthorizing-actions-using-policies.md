## [Authorizing Actions Using Policies](https://laravel.com/docs/12.x/authorization#authorizing-actions-using-policies)
### [Via the User Model](https://laravel.com/docs/12.x/authorization#via-the-user-model)
The `App\Models\User` model that is included with your Laravel application includes two helpful methods for authorizing actions: `can` and `cannot`. The `can` and `cannot` methods receive the name of the action you wish to authorize and the relevant model. For example, let's determine if a user is authorized to update a given `App\Models\Post` model. Typically, this will be done within a controller method:
```


 1<?php




 2 



 3namespace App\Http\Controllers;




 4 



 5use App\Models\Post;




 6use Illuminate\Http\RedirectResponse;




 7use Illuminate\Http\Request;




 8 



 9class PostController extends Controller




10{




11    /**




12     * Update the given post.




13     */




14    public function update(Request $request, Post $post): RedirectResponse




15    {




16        if ($request->user()->cannot('update', $post)) {




17            abort(403);




18        }




19 



20        // Update the post...




21 



22        return redirect('/posts');




23    }




24}




<?php

namespace App\Http\Controllers;

use App\Models\Post;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;

class PostController extends Controller
{
    /**
     * Update the given post.
     */
    public function update(Request $request, Post $post): RedirectResponse
    {
        if ($request->user()->cannot('update', $post)) {
            abort(403);
        }

        // Update the post...

        return redirect('/posts');
    }
}

```

If a [policy is registered](https://laravel.com/docs/12.x/authorization#registering-policies) for the given model, the `can` method will automatically call the appropriate policy and return the boolean result. If no policy is registered for the model, the `can` method will attempt to call the closure-based Gate matching the given action name.
#### [Actions That Don't Require Models](https://laravel.com/docs/12.x/authorization#user-model-actions-that-dont-require-models)
Remember, some actions may correspond to policy methods like `create` that do not require a model instance. In these situations, you may pass a class name to the `can` method. The class name will be used to determine which policy to use when authorizing the action:
```


 1<?php




 2 



 3namespace App\Http\Controllers;




 4 



 5use App\Models\Post;




 6use Illuminate\Http\RedirectResponse;




 7use Illuminate\Http\Request;




 8 



 9class PostController extends Controller




10{




11    /**




12     * Create a post.




13     */




14    public function store(Request $request): RedirectResponse




15    {




16        if ($request->user()->cannot('create', Post::class)) {




17            abort(403);




18        }




19 



20        // Create the post...




21 



22        return redirect('/posts');




23    }




24}




<?php

namespace App\Http\Controllers;

use App\Models\Post;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;

class PostController extends Controller
{
    /**
     * Create a post.
     */
    public function store(Request $request): RedirectResponse
    {
        if ($request->user()->cannot('create', Post::class)) {
            abort(403);
        }

        // Create the post...

        return redirect('/posts');
    }
}

```

### [Via the `Gate` Facade](https://laravel.com/docs/12.x/authorization#via-the-gate-facade)
In addition to helpful methods provided to the `App\Models\User` model, you can always authorize actions via the `Gate` facade's `authorize` method.
Like the `can` method, this method accepts the name of the action you wish to authorize and the relevant model. If the action is not authorized, the `authorize` method will throw an `Illuminate\Auth\Access\AuthorizationException` exception which the Laravel exception handler will automatically convert to an HTTP response with a 403 status code:
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




13     * Update the given blog post.




14     *




15     * @throws \Illuminate\Auth\Access\AuthorizationException




16     */




17    public function update(Request $request, Post $post): RedirectResponse




18    {




19        Gate::authorize('update', $post);




20 



21        // The current user can update the blog post...




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
     * Update the given blog post.
     *
     * @throws \Illuminate\Auth\Access\AuthorizationException
     */
    public function update(Request $request, Post $post): RedirectResponse
    {
        Gate::authorize('update', $post);

        // The current user can update the blog post...

        return redirect('/posts');
    }
}

```

#### [Actions That Don't Require Models](https://laravel.com/docs/12.x/authorization#controller-actions-that-dont-require-models)
As previously discussed, some policy methods like `create` do not require a model instance. In these situations, you should pass a class name to the `authorize` method. The class name will be used to determine which policy to use when authorizing the action:
```


 1use App\Models\Post;




 2use Illuminate\Http\RedirectResponse;




 3use Illuminate\Http\Request;




 4use Illuminate\Support\Facades\Gate;




 5 



 6/**




 7 * Create a new blog post.




 8 *




 9 * @throws \Illuminate\Auth\Access\AuthorizationException




10 */




11public function create(Request $request): RedirectResponse




12{




13    Gate::authorize('create', Post::class);




14 



15    // The current user can create blog posts...




16 



17    return redirect('/posts');




18}




use App\Models\Post;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Gate;

/**
 * Create a new blog post.
 *
 * @throws \Illuminate\Auth\Access\AuthorizationException
 */
public function create(Request $request): RedirectResponse
{
    Gate::authorize('create', Post::class);

    // The current user can create blog posts...

    return redirect('/posts');
}

```

### [Via Middleware](https://laravel.com/docs/12.x/authorization#via-middleware)
Laravel includes a middleware that can authorize actions before the incoming request even reaches your routes or controllers. By default, the `Illuminate\Auth\Middleware\Authorize` middleware may be attached to a route using the `can` [middleware alias](https://laravel.com/docs/12.x/middleware#middleware-aliases), which is automatically registered by Laravel. Let's explore an example of using the `can` middleware to authorize that a user can update a post:
```


1use App\Models\Post;




2 



3Route::put('/post/{post}', function (Post $post) {




4    // The current user may update the post...




5})->middleware('can:update,post');




use App\Models\Post;

Route::put('/post/{post}', function (Post $post) {
    // The current user may update the post...
})->middleware('can:update,post');

```

In this example, we're passing the `can` middleware two arguments. The first is the name of the action we wish to authorize and the second is the route parameter we wish to pass to the policy method. In this case, since we are using [implicit model binding](https://laravel.com/docs/12.x/routing#implicit-binding), an `App\Models\Post` model will be passed to the policy method. If the user is not authorized to perform the given action, an HTTP response with a 403 status code will be returned by the middleware.
For convenience, you may also attach the `can` middleware to your route using the `can` method:
```


1use App\Models\Post;




2 



3Route::put('/post/{post}', function (Post $post) {




4    // The current user may update the post...




5})->can('update', 'post');




use App\Models\Post;

Route::put('/post/{post}', function (Post $post) {
    // The current user may update the post...
})->can('update', 'post');

```

#### [Actions That Don't Require Models](https://laravel.com/docs/12.x/authorization#middleware-actions-that-dont-require-models)
Again, some policy methods like `create` do not require a model instance. In these situations, you may pass a class name to the middleware. The class name will be used to determine which policy to use when authorizing the action:
```


1Route::post('/post', function () {




2    // The current user may create posts...




3})->middleware('can:create,App\Models\Post');




Route::post('/post', function () {
    // The current user may create posts...
})->middleware('can:create,App\Models\Post');

```

Specifying the entire class name within a string middleware definition can become cumbersome. For that reason, you may choose to attach the `can` middleware to your route using the `can` method:
```


1use App\Models\Post;




2 



3Route::post('/post', function () {




4    // The current user may create posts...




5})->can('create', Post::class);




use App\Models\Post;

Route::post('/post', function () {
    // The current user may create posts...
})->can('create', Post::class);

```

### [Via Blade Templates](https://laravel.com/docs/12.x/authorization#via-blade-templates)
When writing Blade templates, you may wish to display a portion of the page only if the user is authorized to perform a given action. For example, you may wish to show an update form for a blog post only if the user can actually update the post. In this situation, you may use the `@can` and `@cannot` directives:
```


 1@can('update', $post)




 2    <!-- The current user can update the post... -->




 3@elsecan('create', App\Models\Post::class)




 4    <!-- The current user can create new posts... -->




 5@else




 6    <!-- ... -->




 7@endcan




 8 



 9@cannot('update', $post)




10    <!-- The current user cannot update the post... -->




11@elsecannot('create', App\Models\Post::class)




12    <!-- The current user cannot create new posts... -->




13@endcannot




@can('update', $post)
    <!-- The current user can update the post... -->
@elsecan('create', App\Models\Post::class)
    <!-- The current user can create new posts... -->
@else
    <!-- ... -->
@endcan

@cannot('update', $post)
    <!-- The current user cannot update the post... -->
@elsecannot('create', App\Models\Post::class)
    <!-- The current user cannot create new posts... -->
@endcannot

```

These directives are convenient shortcuts for writing `@if` and `@unless` statements. The `@can` and `@cannot` statements above are equivalent to the following statements:
```


1@if (Auth::user()->can('update', $post))




2    <!-- The current user can update the post... -->




3@endif




4 



5@unless (Auth::user()->can('update', $post))




6    <!-- The current user cannot update the post... -->




7@endunless




@if (Auth::user()->can('update', $post))
    <!-- The current user can update the post... -->
@endif

@unless (Auth::user()->can('update', $post))
    <!-- The current user cannot update the post... -->
@endunless

```

You may also determine if a user is authorized to perform any action from a given array of actions. To accomplish this, use the `@canany` directive:
```


1@canany(['update', 'view', 'delete'], $post)




2    <!-- The current user can update, view, or delete the post... -->




3@elsecanany(['create'], \App\Models\Post::class)




4    <!-- The current user can create a post... -->




5@endcanany




@canany(['update', 'view', 'delete'], $post)
    <!-- The current user can update, view, or delete the post... -->
@elsecanany(['create'], \App\Models\Post::class)
    <!-- The current user can create a post... -->
@endcanany

```

#### [Actions That Don't Require Models](https://laravel.com/docs/12.x/authorization#blade-actions-that-dont-require-models)
Like most of the other authorization methods, you may pass a class name to the `@can` and `@cannot` directives if the action does not require a model instance:
```


1@can('create', App\Models\Post::class)




2    <!-- The current user can create posts... -->




3@endcan




4 



5@cannot('create', App\Models\Post::class)




6    <!-- The current user can't create posts... -->




7@endcannot




@can('create', App\Models\Post::class)
    <!-- The current user can create posts... -->
@endcan

@cannot('create', App\Models\Post::class)
    <!-- The current user can't create posts... -->
@endcannot

```

### [Supplying Additional Context](https://laravel.com/docs/12.x/authorization#supplying-additional-context)
When authorizing actions using policies, you may pass an array as the second argument to the various authorization functions and helpers. The first element in the array will be used to determine which policy should be invoked, while the rest of the array elements are passed as parameters to the policy method and can be used for additional context when making authorization decisions. For example, consider the following `PostPolicy` method definition which contains an additional `$category` parameter:
```


1/**




2 * Determine if the given post can be updated by the user.




3 */




4public function update(User $user, Post $post, int $category): bool




5{




6    return $user->id === $post->user_id &&




7           $user->canUpdateCategory($category);




8}




/**
 * Determine if the given post can be updated by the user.
 */
public function update(User $user, Post $post, int $category): bool
{
    return $user->id === $post->user_id &&
           $user->canUpdateCategory($category);
}

```

When attempting to determine if the authenticated user can update a given post, we can invoke this policy method like so:
```


 1/**




 2 * Update the given blog post.




 3 *




 4 * @throws \Illuminate\Auth\Access\AuthorizationException




 5 */




 6public function update(Request $request, Post $post): RedirectResponse




 7{




 8    Gate::authorize('update', [$post, $request->category]);




 9 



10    // The current user can update the blog post...




11 



12    return redirect('/posts');




13}




/**
 * Update the given blog post.
 *
 * @throws \Illuminate\Auth\Access\AuthorizationException
 */
public function update(Request $request, Post $post): RedirectResponse
{
    Gate::authorize('update', [$post, $request->category]);

    // The current user can update the blog post...

    return redirect('/posts');
}

```
