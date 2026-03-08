## [Route Model Binding](https://laravel.com/docs/12.x/routing#route-model-binding)
When injecting a model ID to a route or controller action, you will often query the database to retrieve the model that corresponds to that ID. Laravel route model binding provides a convenient way to automatically inject the model instances directly into your routes. For example, instead of injecting a user's ID, you can inject the entire `User` model instance that matches the given ID.
### [Implicit Binding](https://laravel.com/docs/12.x/routing#implicit-binding)
Laravel automatically resolves Eloquent models defined in routes or controller actions whose type-hinted variable names match a route segment name. For example:
```


1use App\Models\User;




2 



3Route::get('/users/{user}', function (User $user) {




4    return $user->email;




5});




use App\Models\User;

Route::get('/users/{user}', function (User $user) {
    return $user->email;
});

```

Since the `$user` variable is type-hinted as the `App\Models\User` Eloquent model and the variable name matches the `{user}` URI segment, Laravel will automatically inject the model instance that has an ID matching the corresponding value from the request URI. If a matching model instance is not found in the database, a 404 HTTP response will automatically be generated.
Of course, implicit binding is also possible when using controller methods. Again, note the `{user}` URI segment matches the `$user` variable in the controller which contains an `App\Models\User` type-hint:
```


 1use App\Http\Controllers\UserController;




 2use App\Models\User;




 3 



 4// Route definition...




 5Route::get('/users/{user}', [UserController::class, 'show']);




 6 



 7// Controller method definition...




 8public function show(User $user)




 9{




10    return view('user.profile', ['user' => $user]);




11}




use App\Http\Controllers\UserController;
use App\Models\User;

// Route definition...
Route::get('/users/{user}', [UserController::class, 'show']);

// Controller method definition...
public function show(User $user)
{
    return view('user.profile', ['user' => $user]);
}

```

#### [Soft Deleted Models](https://laravel.com/docs/12.x/routing#implicit-soft-deleted-models)
Typically, implicit model binding will not retrieve models that have been [soft deleted](https://laravel.com/docs/12.x/eloquent#soft-deleting). However, you may instruct the implicit binding to retrieve these models by chaining the `withTrashed` method onto your route's definition:
```


1use App\Models\User;




2 



3Route::get('/users/{user}', function (User $user) {




4    return $user->email;




5})->withTrashed();




use App\Models\User;

Route::get('/users/{user}', function (User $user) {
    return $user->email;
})->withTrashed();

```

#### [Customizing the Key](https://laravel.com/docs/12.x/routing#customizing-the-default-key-name)
Sometimes you may wish to resolve Eloquent models using a column other than `id`. To do so, you may specify the column in the route parameter definition:
```


1use App\Models\Post;




2 



3Route::get('/posts/{post:slug}', function (Post $post) {




4    return $post;




5});




use App\Models\Post;

Route::get('/posts/{post:slug}', function (Post $post) {
    return $post;
});

```

If you would like model binding to always use a database column other than `id` when retrieving a given model class, you may override the `getRouteKeyName` method on the Eloquent model:
```


1/**




2 * Get the route key for the model.




3 */




4public function getRouteKeyName(): string




5{




6    return 'slug';




7}




/**
 * Get the route key for the model.
 */
public function getRouteKeyName(): string
{
    return 'slug';
}

```

#### [Custom Keys and Scoping](https://laravel.com/docs/12.x/routing#implicit-model-binding-scoping)
When implicitly binding multiple Eloquent models in a single route definition, you may wish to scope the second Eloquent model such that it must be a child of the previous Eloquent model. For example, consider this route definition that retrieves a blog post by slug for a specific user:
```


1use App\Models\Post;




2use App\Models\User;




3 



4Route::get('/users/{user}/posts/{post:slug}', function (User $user, Post $post) {




5    return $post;




6});




use App\Models\Post;
use App\Models\User;

Route::get('/users/{user}/posts/{post:slug}', function (User $user, Post $post) {
    return $post;
});

```

When using a custom keyed implicit binding as a nested route parameter, Laravel will automatically scope the query to retrieve the nested model by its parent using conventions to guess the relationship name on the parent. In this case, it will be assumed that the `User` model has a relationship named `posts` (the plural form of the route parameter name) which can be used to retrieve the `Post` model.
If you wish, you may instruct Laravel to scope "child" bindings even when a custom key is not provided. To do so, you may invoke the `scopeBindings` method when defining your route:
```


1use App\Models\Post;




2use App\Models\User;




3 



4Route::get('/users/{user}/posts/{post}', function (User $user, Post $post) {




5    return $post;




6})->scopeBindings();




use App\Models\Post;
use App\Models\User;

Route::get('/users/{user}/posts/{post}', function (User $user, Post $post) {
    return $post;
})->scopeBindings();

```

Or, you may instruct an entire group of route definitions to use scoped bindings:
```


1Route::scopeBindings()->group(function () {




2    Route::get('/users/{user}/posts/{post}', function (User $user, Post $post) {




3        return $post;




4    });




5});




Route::scopeBindings()->group(function () {
    Route::get('/users/{user}/posts/{post}', function (User $user, Post $post) {
        return $post;
    });
});

```

Similarly, you may explicitly instruct Laravel to not scope bindings by invoking the `withoutScopedBindings` method:
```


1Route::get('/users/{user}/posts/{post:slug}', function (User $user, Post $post) {




2    return $post;




3})->withoutScopedBindings();




Route::get('/users/{user}/posts/{post:slug}', function (User $user, Post $post) {
    return $post;
})->withoutScopedBindings();

```

#### [Customizing Missing Model Behavior](https://laravel.com/docs/12.x/routing#customizing-missing-model-behavior)
Typically, a 404 HTTP response will be generated if an implicitly bound model is not found. However, you may customize this behavior by calling the `missing` method when defining your route. The `missing` method accepts a closure that will be invoked if an implicitly bound model cannot be found:
```


1use App\Http\Controllers\LocationsController;




2use Illuminate\Http\Request;




3use Illuminate\Support\Facades\Redirect;




4 



5Route::get('/locations/{location:slug}', [LocationsController::class, 'show'])




6    ->name('locations.view')




7    ->missing(function (Request $request) {




8        return Redirect::route('locations.index');




9    });




use App\Http\Controllers\LocationsController;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Redirect;

Route::get('/locations/{location:slug}', [LocationsController::class, 'show'])
    ->name('locations.view')
    ->missing(function (Request $request) {
        return Redirect::route('locations.index');
    });

```

### [Implicit Enum Binding](https://laravel.com/docs/12.x/routing#implicit-enum-binding)
PHP 8.1 introduced support for
```


1<?php




2 



3namespace App\Enums;




4 



5enum Category: string




6{




7    case Fruits = 'fruits';




8    case People = 'people';




9}




<?php

namespace App\Enums;

enum Category: string
{
    case Fruits = 'fruits';
    case People = 'people';
}

```

You may define a route that will only be invoked if the `{category}` route segment is `fruits` or `people`. Otherwise, Laravel will return a 404 HTTP response:
```


1use App\Enums\Category;




2use Illuminate\Support\Facades\Route;




3 



4Route::get('/categories/{category}', function (Category $category) {




5    return $category->value;




6});




use App\Enums\Category;
use Illuminate\Support\Facades\Route;

Route::get('/categories/{category}', function (Category $category) {
    return $category->value;
});

```

### [Explicit Binding](https://laravel.com/docs/12.x/routing#explicit-binding)
You are not required to use Laravel's implicit, convention based model resolution in order to use model binding. You can also explicitly define how route parameters correspond to models. To register an explicit binding, use the router's `model` method to specify the class for a given parameter. You should define your explicit model bindings at the beginning of the `boot` method of your `AppServiceProvider` class:
```


 1use App\Models\User;




 2use Illuminate\Support\Facades\Route;




 3 



 4/**




 5 * Bootstrap any application services.




 6 */




 7public function boot(): void




 8{




 9    Route::model('user', User::class);




10}




use App\Models\User;
use Illuminate\Support\Facades\Route;

/**
 * Bootstrap any application services.
 */
public function boot(): void
{
    Route::model('user', User::class);
}

```

Next, define a route that contains a `{user}` parameter:
```


1use App\Models\User;




2 



3Route::get('/users/{user}', function (User $user) {




4    // ...




5});




use App\Models\User;

Route::get('/users/{user}', function (User $user) {
    // ...
});

```

Since we have bound all `{user}` parameters to the `App\Models\User` model, an instance of that class will be injected into the route. So, for example, a request to `users/1` will inject the `User` instance from the database which has an ID of `1`.
If a matching model instance is not found in the database, a 404 HTTP response will be automatically generated.
#### [Customizing the Resolution Logic](https://laravel.com/docs/12.x/routing#customizing-the-resolution-logic)
If you wish to define your own model binding resolution logic, you may use the `Route::bind` method. The closure you pass to the `bind` method will receive the value of the URI segment and should return the instance of the class that should be injected into the route. Again, this customization should take place in the `boot` method of your application's `AppServiceProvider`:
```


 1use App\Models\User;




 2use Illuminate\Support\Facades\Route;




 3 



 4/**




 5 * Bootstrap any application services.




 6 */




 7public function boot(): void




 8{




 9    Route::bind('user', function (string $value) {




10        return User::where('name', $value)->firstOrFail();




11    });




12}




use App\Models\User;
use Illuminate\Support\Facades\Route;

/**
 * Bootstrap any application services.
 */
public function boot(): void
{
    Route::bind('user', function (string $value) {
        return User::where('name', $value)->firstOrFail();
    });
}

```

Alternatively, you may override the `resolveRouteBinding` method on your Eloquent model. This method will receive the value of the URI segment and should return the instance of the class that should be injected into the route:
```


 1/**




 2 * Retrieve the model for a bound value.




 3 *




 4 * @param  mixed  $value




 5 * @param  string|null  $field




 6 * @return \Illuminate\Database\Eloquent\Model|null




 7 */




 8public function resolveRouteBinding($value, $field = null)




 9{




10    return $this->where('name', $value)->firstOrFail();




11}




/**
 * Retrieve the model for a bound value.
 *
 * @param  mixed  $value
 * @param  string|null  $field
 * @return \Illuminate\Database\Eloquent\Model|null
 */
public function resolveRouteBinding($value, $field = null)
{
    return $this->where('name', $value)->firstOrFail();
}

```

If a route is utilizing [implicit binding scoping](https://laravel.com/docs/12.x/routing#implicit-model-binding-scoping), the `resolveChildRouteBinding` method will be used to resolve the child binding of the parent model:
```


 1/**




 2 * Retrieve the child model for a bound value.




 3 *




 4 * @param  string  $childType




 5 * @param  mixed  $value




 6 * @param  string|null  $field




 7 * @return \Illuminate\Database\Eloquent\Model|null




 8 */




 9public function resolveChildRouteBinding($childType, $value, $field)




10{




11    return parent::resolveChildRouteBinding($childType, $value, $field);




12}




/**
 * Retrieve the child model for a bound value.
 *
 * @param  string  $childType
 * @param  mixed  $value
 * @param  string|null  $field
 * @return \Illuminate\Database\Eloquent\Model|null
 */
public function resolveChildRouteBinding($childType, $value, $field)
{
    return parent::resolveChildRouteBinding($childType, $value, $field);
}

```
