## [Writing Resources](https://laravel.com/docs/12.x/eloquent-resources#writing-resources)
If you have not read the [concept overview](https://laravel.com/docs/12.x/eloquent-resources#concept-overview), you are highly encouraged to do so before proceeding with this documentation.
Resources only need to transform a given model into an array. So, each resource contains a `toArray` method which translates your model's attributes into an API friendly array that can be returned from your application's routes or controllers:
```


 1<?php




 2 



 3namespace App\Http\Resources;




 4 



 5use Illuminate\Http\Request;




 6use Illuminate\Http\Resources\Json\JsonResource;




 7 



 8class UserResource extends JsonResource




 9{




10    /**




11     * Transform the resource into an array.




12     *




13     * @return array<string, mixed>




14     */




15    public function toArray(Request $request): array




16    {




17        return [




18            'id' => $this->id,




19            'name' => $this->name,




20            'email' => $this->email,




21            'created_at' => $this->created_at,




22            'updated_at' => $this->updated_at,




23        ];




24    }




25}




<?php

namespace App\Http\Resources;

use Illuminate\Http\Request;
use Illuminate\Http\Resources\Json\JsonResource;

class UserResource extends JsonResource
{
    /**
     * Transform the resource into an array.
     *
     * @return array<string, mixed>
     */
    public function toArray(Request $request): array
    {
        return [
            'id' => $this->id,
            'name' => $this->name,
            'email' => $this->email,
            'created_at' => $this->created_at,
            'updated_at' => $this->updated_at,
        ];
    }
}

```

Once a resource has been defined, it may be returned directly from a route or controller:
```


1use App\Models\User;




2 



3Route::get('/user/{id}', function (string $id) {




4    return User::findOrFail($id)->toUserResource();




5});




use App\Models\User;

Route::get('/user/{id}', function (string $id) {
    return User::findOrFail($id)->toUserResource();
});

```

#### [Relationships](https://laravel.com/docs/12.x/eloquent-resources#relationships)
If you would like to include related resources in your response, you may add them to the array returned by your resource's `toArray` method. In this example, we will use the `PostResource` resource's `collection` method to add the user's blog posts to the resource response:
```


 1use App\Http\Resources\PostResource;




 2use Illuminate\Http\Request;




 3 



 4/**




 5 * Transform the resource into an array.




 6 *




 7 * @return array<string, mixed>




 8 */




 9public function toArray(Request $request): array




10{




11    return [




12        'id' => $this->id,




13        'name' => $this->name,




14        'email' => $this->email,




15        'posts' => PostResource::collection($this->posts),




16        'created_at' => $this->created_at,




17        'updated_at' => $this->updated_at,




18    ];




19}




use App\Http\Resources\PostResource;
use Illuminate\Http\Request;

/**
 * Transform the resource into an array.
 *
 * @return array<string, mixed>
 */
public function toArray(Request $request): array
{
    return [
        'id' => $this->id,
        'name' => $this->name,
        'email' => $this->email,
        'posts' => PostResource::collection($this->posts),
        'created_at' => $this->created_at,
        'updated_at' => $this->updated_at,
    ];
}

```

If you would like to include relationships only when they have already been loaded, check out the documentation on [conditional relationships](https://laravel.com/docs/12.x/eloquent-resources#conditional-relationships).
#### [Resource Collections](https://laravel.com/docs/12.x/eloquent-resources#writing-resource-collections)
While resources transform a single model into an array, resource collections transform a collection of models into an array. However, it is not absolutely necessary to define a resource collection class for each one of your models since all Eloquent model collections provide a `toResourceCollection` method to generate an "ad-hoc" resource collection on the fly:
```


1use App\Models\User;




2 



3Route::get('/users', function () {




4    return User::all()->toResourceCollection();




5});




use App\Models\User;

Route::get('/users', function () {
    return User::all()->toResourceCollection();
});

```

However, if you need to customize the meta data returned with the collection, it is necessary to define your own resource collection:
```


 1<?php




 2 



 3namespace App\Http\Resources;




 4 



 5use Illuminate\Http\Request;




 6use Illuminate\Http\Resources\Json\ResourceCollection;




 7 



 8class UserCollection extends ResourceCollection




 9{




10    /**




11     * Transform the resource collection into an array.




12     *




13     * @return array<string, mixed>




14     */




15    public function toArray(Request $request): array




16    {




17        return [




18            'data' => $this->collection,




19            'links' => [




20                'self' => 'link-value',




21            ],




22        ];




23    }




24}




<?php

namespace App\Http\Resources;

use Illuminate\Http\Request;
use Illuminate\Http\Resources\Json\ResourceCollection;

class UserCollection extends ResourceCollection
{
    /**
     * Transform the resource collection into an array.
     *
     * @return array<string, mixed>
     */
    public function toArray(Request $request): array
    {
        return [
            'data' => $this->collection,
            'links' => [
                'self' => 'link-value',
            ],
        ];
    }
}

```

Like singular resources, resource collections may be returned directly from routes or controllers:
```


1use App\Http\Resources\UserCollection;




2use App\Models\User;




3 



4Route::get('/users', function () {




5    return new UserCollection(User::all());




6});




use App\Http\Resources\UserCollection;
use App\Models\User;

Route::get('/users', function () {
    return new UserCollection(User::all());
});

```

Or, for convenience, you may use the Eloquent collection's `toResourceCollection` method, which will use framework conventions to automatically discover the model's underlying resource collection:
```


1return User::all()->toResourceCollection();




return User::all()->toResourceCollection();

```

When invoking the `toResourceCollection` method, Laravel will attempt to locate a resource collection that matches the model's name and is suffixed with `Collection` within the `Http\Resources` namespace closest to the model's namespace.
### [Data Wrapping](https://laravel.com/docs/12.x/eloquent-resources#data-wrapping)
By default, your outermost resource is wrapped in a `data` key when the resource response is converted to JSON. So, for example, a typical resource collection response looks like the following:
```


 1{




 2    "data": [




 3        {




 4            "id": 1,




 5            "name": "Eladio Schroeder Sr.",




 6            "email": "therese28@example.com"




 7        },




 8        {




 9            "id": 2,




10            "name": "Liliana Mayert",




11            "email": "evandervort@example.com"




12        }




13    ]




14}




{
    "data": [
        {
            "id": 1,
            "name": "Eladio Schroeder Sr.",
            "email": "therese28@example.com"
        },
        {
            "id": 2,
            "name": "Liliana Mayert",
            "email": "evandervort@example.com"
        }
    ]
}

```

If you would like to disable the wrapping of the outermost resource, you should invoke the `withoutWrapping` method on the base `Illuminate\Http\Resources\Json\JsonResource` class. Typically, you should call this method from your `AppServiceProvider` or another [service provider](https://laravel.com/docs/12.x/providers) that is loaded on every request to your application:
```


 1<?php




 2 



 3namespace App\Providers;




 4 



 5use Illuminate\Http\Resources\Json\JsonResource;




 6use Illuminate\Support\ServiceProvider;




 7 



 8class AppServiceProvider extends ServiceProvider




 9{




10    /**




11     * Register any application services.




12     */




13    public function register(): void




14    {




15        // ...




16    }




17 



18    /**




19     * Bootstrap any application services.




20     */




21    public function boot(): void




22    {




23        JsonResource::withoutWrapping();




24    }




25}




<?php

namespace App\Providers;

use Illuminate\Http\Resources\Json\JsonResource;
use Illuminate\Support\ServiceProvider;

class AppServiceProvider extends ServiceProvider
{
    /**
     * Register any application services.
     */
    public function register(): void
    {
        // ...
    }

    /**
     * Bootstrap any application services.
     */
    public function boot(): void
    {
        JsonResource::withoutWrapping();
    }
}

```

The `withoutWrapping` method only affects the outermost response and will not remove `data` keys that you manually add to your own resource collections.
#### [Wrapping Nested Resources](https://laravel.com/docs/12.x/eloquent-resources#wrapping-nested-resources)
You have total freedom to determine how your resource's relationships are wrapped. If you would like all resource collections to be wrapped in a `data` key, regardless of their nesting, you should define a resource collection class for each resource and return the collection within a `data` key.
You may be wondering if this will cause your outermost resource to be wrapped in two `data` keys. Don't worry, Laravel will never let your resources be accidentally double-wrapped, so you don't have to be concerned about the nesting level of the resource collection you are transforming:
```


 1<?php




 2 



 3namespace App\Http\Resources;




 4 



 5use Illuminate\Http\Resources\Json\ResourceCollection;




 6 



 7class CommentsCollection extends ResourceCollection




 8{




 9    /**




10     * Transform the resource collection into an array.




11     *




12     * @return array<string, mixed>




13     */




14    public function toArray(Request $request): array




15    {




16        return ['data' => $this->collection];




17    }




18}




<?php

namespace App\Http\Resources;

use Illuminate\Http\Resources\Json\ResourceCollection;

class CommentsCollection extends ResourceCollection
{
    /**
     * Transform the resource collection into an array.
     *
     * @return array<string, mixed>
     */
    public function toArray(Request $request): array
    {
        return ['data' => $this->collection];
    }
}

```

#### [Data Wrapping and Pagination](https://laravel.com/docs/12.x/eloquent-resources#data-wrapping-and-pagination)
When returning paginated collections via a resource response, Laravel will wrap your resource data in a `data` key even if the `withoutWrapping` method has been called. This is because paginated responses always contain `meta` and `links` keys with information about the paginator's state:
```


 1{




 2    "data": [




 3        {




 4            "id": 1,




 5            "name": "Eladio Schroeder Sr.",




 6            "email": "therese28@example.com"




 7        },




 8        {




 9            "id": 2,




10            "name": "Liliana Mayert",




11            "email": "evandervort@example.com"




12        }




13    ],




14    "links":{




15        "first": "http://example.com/users?page=1",




16        "last": "http://example.com/users?page=1",




17        "prev": null,




18        "next": null




19    },




20    "meta":{




21        "current_page": 1,




22        "from": 1,




23        "last_page": 1,




24        "path": "http://example.com/users",




25        "per_page": 15,




26        "to": 10,




27        "total": 10




28    }




29}




{
    "data": [
        {
            "id": 1,
            "name": "Eladio Schroeder Sr.",
            "email": "therese28@example.com"
        },
        {
            "id": 2,
            "name": "Liliana Mayert",
            "email": "evandervort@example.com"
        }
    ],
    "links":{
        "first": "http://example.com/users?page=1",
        "last": "http://example.com/users?page=1",
        "prev": null,
        "next": null
    },
    "meta":{
        "current_page": 1,
        "from": 1,
        "last_page": 1,
        "path": "http://example.com/users",
        "per_page": 15,
        "to": 10,
        "total": 10
    }
}

```

### [Pagination](https://laravel.com/docs/12.x/eloquent-resources#pagination)
You may pass a Laravel paginator instance to the `collection` method of a resource or to a custom resource collection:
```


1use App\Http\Resources\UserCollection;




2use App\Models\User;




3 



4Route::get('/users', function () {




5    return new UserCollection(User::paginate());




6});




use App\Http\Resources\UserCollection;
use App\Models\User;

Route::get('/users', function () {
    return new UserCollection(User::paginate());
});

```

Or, for convenience, you may use the paginator's `toResourceCollection` method, which will use framework conventions to automatically discover the paginated model's underlying resource collection:
```


1return User::paginate()->toResourceCollection();




return User::paginate()->toResourceCollection();

```

Paginated responses always contain `meta` and `links` keys with information about the paginator's state:
```


 1{




 2    "data": [




 3        {




 4            "id": 1,




 5            "name": "Eladio Schroeder Sr.",




 6            "email": "therese28@example.com"




 7        },




 8        {




 9            "id": 2,




10            "name": "Liliana Mayert",




11            "email": "evandervort@example.com"




12        }




13    ],




14    "links":{




15        "first": "http://example.com/users?page=1",




16        "last": "http://example.com/users?page=1",




17        "prev": null,




18        "next": null




19    },




20    "meta":{




21        "current_page": 1,




22        "from": 1,




23        "last_page": 1,




24        "path": "http://example.com/users",




25        "per_page": 15,




26        "to": 10,




27        "total": 10




28    }




29}




{
    "data": [
        {
            "id": 1,
            "name": "Eladio Schroeder Sr.",
            "email": "therese28@example.com"
        },
        {
            "id": 2,
            "name": "Liliana Mayert",
            "email": "evandervort@example.com"
        }
    ],
    "links":{
        "first": "http://example.com/users?page=1",
        "last": "http://example.com/users?page=1",
        "prev": null,
        "next": null
    },
    "meta":{
        "current_page": 1,
        "from": 1,
        "last_page": 1,
        "path": "http://example.com/users",
        "per_page": 15,
        "to": 10,
        "total": 10
    }
}

```

#### [Customizing the Pagination Information](https://laravel.com/docs/12.x/eloquent-resources#customizing-the-pagination-information)
If you would like to customize the information included in the `links` or `meta` keys of the pagination response, you may define a `paginationInformation` method on the resource. This method will receive the `$paginated` data and the array of `$default` information, which is an array containing the `links` and `meta` keys:
```


 1/**




 2 * Customize the pagination information for the resource.




 3 *




 4 * @param  \Illuminate\Http\Request  $request




 5 * @param  array  $paginated




 6 * @param  array  $default




 7 * @return array




 8 */




 9public function paginationInformation($request, $paginated, $default)




10{




11    $default['links']['custom'] = 'https://example.com';




12 



13    return $default;




14}




/**
 * Customize the pagination information for the resource.
 *
 * @param  \Illuminate\Http\Request  $request
 * @param  array  $paginated
 * @param  array  $default
 * @return array
 */
public function paginationInformation($request, $paginated, $default)
{
    $default['links']['custom'] = 'https://example.com';

    return $default;
}

```

### [Conditional Attributes](https://laravel.com/docs/12.x/eloquent-resources#conditional-attributes)
Sometimes you may wish to only include an attribute in a resource response if a given condition is met. For example, you may wish to only include a value if the current user is an "administrator". Laravel provides a variety of helper methods to assist you in this situation. The `when` method may be used to conditionally add an attribute to a resource response:
```


 1/**




 2 * Transform the resource into an array.




 3 *




 4 * @return array<string, mixed>




 5 */




 6public function toArray(Request $request): array




 7{




 8    return [




 9        'id' => $this->id,




10        'name' => $this->name,




11        'email' => $this->email,




12        'secret' => $this->when($request->user()->isAdmin(), 'secret-value'),




13        'created_at' => $this->created_at,




14        'updated_at' => $this->updated_at,




15    ];




16}




/**
 * Transform the resource into an array.
 *
 * @return array<string, mixed>
 */
public function toArray(Request $request): array
{
    return [
        'id' => $this->id,
        'name' => $this->name,
        'email' => $this->email,
        'secret' => $this->when($request->user()->isAdmin(), 'secret-value'),
        'created_at' => $this->created_at,
        'updated_at' => $this->updated_at,
    ];
}

```

In this example, the `secret` key will only be returned in the final resource response if the authenticated user's `isAdmin` method returns `true`. If the method returns `false`, the `secret` key will be removed from the resource response before it is sent to the client. The `when` method allows you to expressively define your resources without resorting to conditional statements when building the array.
The `when` method also accepts a closure as its second argument, allowing you to calculate the resulting value only if the given condition is `true`:
```


1'secret' => $this->when($request->user()->isAdmin(), function () {




2    return 'secret-value';




3}),




'secret' => $this->when($request->user()->isAdmin(), function () {
    return 'secret-value';
}),

```

The `whenHas` method may be used to include an attribute if it is actually present on the underlying model:
```


1'name' => $this->whenHas('name'),




'name' => $this->whenHas('name'),

```

Additionally, the `whenNotNull` method may be used to include an attribute in the resource response if the attribute is not null:
```


1'name' => $this->whenNotNull($this->name),




'name' => $this->whenNotNull($this->name),

```

#### [Merging Conditional Attributes](https://laravel.com/docs/12.x/eloquent-resources#merging-conditional-attributes)
Sometimes you may have several attributes that should only be included in the resource response based on the same condition. In this case, you may use the `mergeWhen` method to include the attributes in the response only when the given condition is `true`:
```


 1/**




 2 * Transform the resource into an array.




 3 *




 4 * @return array<string, mixed>




 5 */




 6public function toArray(Request $request): array




 7{




 8    return [




 9        'id' => $this->id,




10        'name' => $this->name,




11        'email' => $this->email,




12        $this->mergeWhen($request->user()->isAdmin(), [




13            'first-secret' => 'value',




14            'second-secret' => 'value',




15        ]),




16        'created_at' => $this->created_at,




17        'updated_at' => $this->updated_at,




18    ];




19}




/**
 * Transform the resource into an array.
 *
 * @return array<string, mixed>
 */
public function toArray(Request $request): array
{
    return [
        'id' => $this->id,
        'name' => $this->name,
        'email' => $this->email,
        $this->mergeWhen($request->user()->isAdmin(), [
            'first-secret' => 'value',
            'second-secret' => 'value',
        ]),
        'created_at' => $this->created_at,
        'updated_at' => $this->updated_at,
    ];
}

```

Again, if the given condition is `false`, these attributes will be removed from the resource response before it is sent to the client.
The `mergeWhen` method should not be used within arrays that mix string and numeric keys. Furthermore, it should not be used within arrays with numeric keys that are not ordered sequentially.
### [Conditional Relationships](https://laravel.com/docs/12.x/eloquent-resources#conditional-relationships)
In addition to conditionally loading attributes, you may conditionally include relationships on your resource responses based on if the relationship has already been loaded on the model. This allows your controller to decide which relationships should be loaded on the model and your resource can easily include them only when they have actually been loaded. Ultimately, this makes it easier to avoid "N+1" query problems within your resources.
The `whenLoaded` method may be used to conditionally load a relationship. In order to avoid unnecessarily loading relationships, this method accepts the name of the relationship instead of the relationship itself:
```


 1use App\Http\Resources\PostResource;




 2 



 3/**




 4 * Transform the resource into an array.




 5 *




 6 * @return array<string, mixed>




 7 */




 8public function toArray(Request $request): array




 9{




10    return [




11        'id' => $this->id,




12        'name' => $this->name,




13        'email' => $this->email,




14        'posts' => PostResource::collection($this->whenLoaded('posts')),




15        'created_at' => $this->created_at,




16        'updated_at' => $this->updated_at,




17    ];




18}




use App\Http\Resources\PostResource;

/**
 * Transform the resource into an array.
 *
 * @return array<string, mixed>
 */
public function toArray(Request $request): array
{
    return [
        'id' => $this->id,
        'name' => $this->name,
        'email' => $this->email,
        'posts' => PostResource::collection($this->whenLoaded('posts')),
        'created_at' => $this->created_at,
        'updated_at' => $this->updated_at,
    ];
}

```

In this example, if the relationship has not been loaded, the `posts` key will be removed from the resource response before it is sent to the client.
#### [Conditional Relationship Counts](https://laravel.com/docs/12.x/eloquent-resources#conditional-relationship-counts)
In addition to conditionally including relationships, you may conditionally include relationship "counts" on your resource responses based on if the relationship's count has been loaded on the model:
```


1new UserResource($user->loadCount('posts'));




new UserResource($user->loadCount('posts'));

```

The `whenCounted` method may be used to conditionally include a relationship's count in your resource response. This method avoids unnecessarily including the attribute if the relationships' count is not present:
```


 1/**




 2 * Transform the resource into an array.




 3 *




 4 * @return array<string, mixed>




 5 */




 6public function toArray(Request $request): array




 7{




 8    return [




 9        'id' => $this->id,




10        'name' => $this->name,




11        'email' => $this->email,




12        'posts_count' => $this->whenCounted('posts'),




13        'created_at' => $this->created_at,




14        'updated_at' => $this->updated_at,




15    ];




16}




/**
 * Transform the resource into an array.
 *
 * @return array<string, mixed>
 */
public function toArray(Request $request): array
{
    return [
        'id' => $this->id,
        'name' => $this->name,
        'email' => $this->email,
        'posts_count' => $this->whenCounted('posts'),
        'created_at' => $this->created_at,
        'updated_at' => $this->updated_at,
    ];
}

```

In this example, if the `posts` relationship's count has not been loaded, the `posts_count` key will be removed from the resource response before it is sent to the client.
Other types of aggregates, such as `avg`, `sum`, `min`, and `max` may also be conditionally loaded using the `whenAggregated` method:
```


1'words_avg' => $this->whenAggregated('posts', 'words', 'avg'),




2'words_sum' => $this->whenAggregated('posts', 'words', 'sum'),




3'words_min' => $this->whenAggregated('posts', 'words', 'min'),




4'words_max' => $this->whenAggregated('posts', 'words', 'max'),




'words_avg' => $this->whenAggregated('posts', 'words', 'avg'),
'words_sum' => $this->whenAggregated('posts', 'words', 'sum'),
'words_min' => $this->whenAggregated('posts', 'words', 'min'),
'words_max' => $this->whenAggregated('posts', 'words', 'max'),

```

#### [Conditional Pivot Information](https://laravel.com/docs/12.x/eloquent-resources#conditional-pivot-information)
In addition to conditionally including relationship information in your resource responses, you may conditionally include data from the intermediate tables of many-to-many relationships using the `whenPivotLoaded` method. The `whenPivotLoaded` method accepts the name of the pivot table as its first argument. The second argument should be a closure that returns the value to be returned if the pivot information is available on the model:
```


 1/**




 2 * Transform the resource into an array.




 3 *




 4 * @return array<string, mixed>




 5 */




 6public function toArray(Request $request): array




 7{




 8    return [




 9        'id' => $this->id,




10        'name' => $this->name,




11        'expires_at' => $this->whenPivotLoaded('role_user', function () {




12            return $this->pivot->expires_at;




13        }),




14    ];




15}




/**
 * Transform the resource into an array.
 *
 * @return array<string, mixed>
 */
public function toArray(Request $request): array
{
    return [
        'id' => $this->id,
        'name' => $this->name,
        'expires_at' => $this->whenPivotLoaded('role_user', function () {
            return $this->pivot->expires_at;
        }),
    ];
}

```

If your relationship is using a [custom intermediate table model](https://laravel.com/docs/12.x/eloquent-relationships#defining-custom-intermediate-table-models), you may pass an instance of the intermediate table model as the first argument to the `whenPivotLoaded` method:
```


1'expires_at' => $this->whenPivotLoaded(new Membership, function () {




2    return $this->pivot->expires_at;




3}),




'expires_at' => $this->whenPivotLoaded(new Membership, function () {
    return $this->pivot->expires_at;
}),

```

If your intermediate table is using an accessor other than `pivot`, you may use the `whenPivotLoadedAs` method:
```


 1/**




 2 * Transform the resource into an array.




 3 *




 4 * @return array<string, mixed>




 5 */




 6public function toArray(Request $request): array




 7{




 8    return [




 9        'id' => $this->id,




10        'name' => $this->name,




11        'expires_at' => $this->whenPivotLoadedAs('subscription', 'role_user', function () {




12            return $this->subscription->expires_at;




13        }),




14    ];




15}




/**
 * Transform the resource into an array.
 *
 * @return array<string, mixed>
 */
public function toArray(Request $request): array
{
    return [
        'id' => $this->id,
        'name' => $this->name,
        'expires_at' => $this->whenPivotLoadedAs('subscription', 'role_user', function () {
            return $this->subscription->expires_at;
        }),
    ];
}

```

### [Adding Meta Data](https://laravel.com/docs/12.x/eloquent-resources#adding-meta-data)
Some JSON API standards require the addition of meta data to your resource and resource collections responses. This often includes things like `links` to the resource or related resources, or meta data about the resource itself. If you need to return additional meta data about a resource, include it in your `toArray` method. For example, you might include `links` information when transforming a resource collection:
```


 1/**




 2 * Transform the resource into an array.




 3 *




 4 * @return array<string, mixed>




 5 */




 6public function toArray(Request $request): array




 7{




 8    return [




 9        'data' => $this->collection,




10        'links' => [




11            'self' => 'link-value',




12        ],




13    ];




14}




/**
 * Transform the resource into an array.
 *
 * @return array<string, mixed>
 */
public function toArray(Request $request): array
{
    return [
        'data' => $this->collection,
        'links' => [
            'self' => 'link-value',
        ],
    ];
}

```

When returning additional meta data from your resources, you never have to worry about accidentally overriding the `links` or `meta` keys that are automatically added by Laravel when returning paginated responses. Any additional `links` you define will be merged with the links provided by the paginator.
#### [Top Level Meta Data](https://laravel.com/docs/12.x/eloquent-resources#top-level-meta-data)
Sometimes you may wish to only include certain meta data with a resource response if the resource is the outermost resource being returned. Typically, this includes meta information about the response as a whole. To define this meta data, add a `with` method to your resource class. This method should return an array of meta data to be included with the resource response only when the resource is the outermost resource being transformed:
```


 1<?php




 2 



 3namespace App\Http\Resources;




 4 



 5use Illuminate\Http\Resources\Json\ResourceCollection;




 6 



 7class UserCollection extends ResourceCollection




 8{




 9    /**




10     * Transform the resource collection into an array.




11     *




12     * @return array<string, mixed>




13     */




14    public function toArray(Request $request): array




15    {




16        return parent::toArray($request);




17    }




18 



19    /**




20     * Get additional data that should be returned with the resource array.




21     *




22     * @return array<string, mixed>




23     */




24    public function with(Request $request): array




25    {




26        return [




27            'meta' => [




28                'key' => 'value',




29            ],




30        ];




31    }




32}




<?php

namespace App\Http\Resources;

use Illuminate\Http\Resources\Json\ResourceCollection;

class UserCollection extends ResourceCollection
{
    /**
     * Transform the resource collection into an array.
     *
     * @return array<string, mixed>
     */
    public function toArray(Request $request): array
    {
        return parent::toArray($request);
    }

    /**
     * Get additional data that should be returned with the resource array.
     *
     * @return array<string, mixed>
     */
    public function with(Request $request): array
    {
        return [
            'meta' => [
                'key' => 'value',
            ],
        ];
    }
}

```

#### [Adding Meta Data When Constructing Resources](https://laravel.com/docs/12.x/eloquent-resources#adding-meta-data-when-constructing-resources)
You may also add top-level data when constructing resource instances in your route or controller. The `additional` method, which is available on all resources, accepts an array of data that should be added to the resource response:
```


1return User::all()




2    ->load('roles')




3    ->toResourceCollection()




4    ->additional(['meta' => [




5        'key' => 'value',




6    ]]);




return User::all()
    ->load('roles')
    ->toResourceCollection()
    ->additional(['meta' => [
        'key' => 'value',
    ]]);

```
