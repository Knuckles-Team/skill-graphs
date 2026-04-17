## [Concept Overview](https://laravel.com/docs/12.x/eloquent-resources#concept-overview)
This is a high-level overview of resources and resource collections. You are highly encouraged to read the other sections of this documentation to gain a deeper understanding of the customization and power offered to you by resources.
Before diving into all of the options available to you when writing resources, let's first take a high-level look at how resources are used within Laravel. A resource class represents a single model that needs to be transformed into a JSON structure. For example, here is a simple `UserResource` resource class:
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

Every resource class defines a `toArray` method which returns the array of attributes that should be converted to JSON when the resource is returned as a response from a route or controller method.
Note that we can access model properties directly from the `$this` variable. This is because a resource class will automatically proxy property and method access down to the underlying model for convenient access. Once the resource is defined, it may be returned from a route or controller. The resource accepts the underlying model instance via its constructor:
```


1use App\Http\Resources\UserResource;




2use App\Models\User;




3 



4Route::get('/user/{id}', function (string $id) {




5    return new UserResource(User::findOrFail($id));




6});




use App\Http\Resources\UserResource;
use App\Models\User;

Route::get('/user/{id}', function (string $id) {
    return new UserResource(User::findOrFail($id));
});

```

For convenience, you may use the model's `toResource` method, which will use framework conventions to automatically discover the model's underlying resource:
```


1return User::findOrFail($id)->toResource();




return User::findOrFail($id)->toResource();

```

When invoking the `toResource` method, Laravel will attempt to locate a resource that matches the model's name and is optionally suffixed with `Resource` within the `Http\Resources` namespace closest to the model's namespace.
If your resource class doesn't follow this naming convention or is located in a different namespace, you may specify the default resource for the model using the `UseResource` attribute:
```


 1<?php




 2 



 3namespace App\Models;




 4 



 5use App\Http\Resources\CustomUserResource;




 6use Illuminate\Database\Eloquent\Model;




 7use Illuminate\Database\Eloquent\Attributes\UseResource;




 8 



 9#[UseResource(CustomUserResource::class)]




10class User extends Model




11{




12    // ...




13}




<?php

namespace App\Models;

use App\Http\Resources\CustomUserResource;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Attributes\UseResource;

#[UseResource(CustomUserResource::class)]
class User extends Model
{
    // ...
}

```

Alternatively, you may specify resource class by passing it to the `toResource` method:
```


1return User::findOrFail($id)->toResource(CustomUserResource::class);




return User::findOrFail($id)->toResource(CustomUserResource::class);

```

### [Resource Collections](https://laravel.com/docs/12.x/eloquent-resources#resource-collections)
If you are returning a collection of resources or a paginated response, you should use the `collection` method provided by your resource class when creating the resource instance in your route or controller:
```


1use App\Http\Resources\UserResource;




2use App\Models\User;




3 



4Route::get('/users', function () {




5    return UserResource::collection(User::all());




6});




use App\Http\Resources\UserResource;
use App\Models\User;

Route::get('/users', function () {
    return UserResource::collection(User::all());
});

```

Or, for convenience, you may use the Eloquent collection's `toResourceCollection` method, which will use framework conventions to automatically discover the model's underlying resource collection:
```


1return User::all()->toResourceCollection();




return User::all()->toResourceCollection();

```

When invoking the `toResourceCollection` method, Laravel will attempt to locate a resource collection that matches the model's name and is suffixed with `Collection` within the `Http\Resources` namespace closest to the model's namespace.
If your resource collection class doesn't follow this naming convention or is located in a different namespace, you may specify the default resource collection for the model using the `UseResourceCollection` attribute:
```


 1<?php




 2 



 3namespace App\Models;




 4 



 5use App\Http\Resources\CustomUserCollection;




 6use Illuminate\Database\Eloquent\Model;




 7use Illuminate\Database\Eloquent\Attributes\UseResourceCollection;




 8 



 9#[UseResourceCollection(CustomUserCollection::class)]




10class User extends Model




11{




12    // ...




13}




<?php

namespace App\Models;

use App\Http\Resources\CustomUserCollection;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Attributes\UseResourceCollection;

#[UseResourceCollection(CustomUserCollection::class)]
class User extends Model
{
    // ...
}

```

Alternatively, you may specify the resource collection class by passing it to the `toResourceCollection` method:
```


1return User::all()->toResourceCollection(CustomUserCollection::class);




return User::all()->toResourceCollection(CustomUserCollection::class);

```

#### [Custom Resource Collections](https://laravel.com/docs/12.x/eloquent-resources#custom-resource-collections)
By default, resource collections do not allow any addition of custom meta data that may need to be returned with your collection. If you would like to customize the resource collection response, you may create a dedicated resource to represent the collection:
```


1php artisan make:resource UserCollection




php artisan make:resource UserCollection

```

Once the resource collection class has been generated, you may easily define any meta data that should be included with the response:
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




13     * @return array<int|string, mixed>




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
     * @return array<int|string, mixed>
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

After defining your resource collection, it may be returned from a route or controller:
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
#### [Preserving Collection Keys](https://laravel.com/docs/12.x/eloquent-resources#preserving-collection-keys)
When returning a resource collection from a route, Laravel resets the collection's keys so that they are in numerical order. However, you may add a `preserveKeys` property to your resource class indicating whether a collection's original keys should be preserved:
```


 1<?php




 2 



 3namespace App\Http\Resources;




 4 



 5use Illuminate\Http\Resources\Json\JsonResource;




 6 



 7class UserResource extends JsonResource




 8{




 9    /**




10     * Indicates if the resource's collection keys should be preserved.




11     *




12     * @var bool




13     */




14    public $preserveKeys = true;




15}




<?php

namespace App\Http\Resources;

use Illuminate\Http\Resources\Json\JsonResource;

class UserResource extends JsonResource
{
    /**
     * Indicates if the resource's collection keys should be preserved.
     *
     * @var bool
     */
    public $preserveKeys = true;
}

```

When the `preserveKeys` property is set to `true`, collection keys will be preserved when the collection is returned from a route or controller:
```


1use App\Http\Resources\UserResource;




2use App\Models\User;




3 



4Route::get('/users', function () {




5    return UserResource::collection(User::all()->keyBy->id);




6});




use App\Http\Resources\UserResource;
use App\Models\User;

Route::get('/users', function () {
    return UserResource::collection(User::all()->keyBy->id);
});

```

#### [Customizing the Underlying Resource Class](https://laravel.com/docs/12.x/eloquent-resources#customizing-the-underlying-resource-class)
Typically, the `$this->collection` property of a resource collection is automatically populated with the result of mapping each item of the collection to its singular resource class. The singular resource class is assumed to be the collection's class name without the trailing `Collection` portion of the class name. In addition, depending on your personal preference, the singular resource class may or may not be suffixed with `Resource`.
For example, `UserCollection` will attempt to map the given user instances into the `UserResource` resource. To customize this behavior, you may override the `$collects` property of your resource collection:
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




10     * The resource that this resource collects.




11     *




12     * @var string




13     */




14    public $collects = Member::class;




15}




<?php

namespace App\Http\Resources;

use Illuminate\Http\Resources\Json\ResourceCollection;

class UserCollection extends ResourceCollection
{
    /**
     * The resource that this resource collects.
     *
     * @var string
     */
    public $collects = Member::class;
}

```
