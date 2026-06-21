## [Defining Relationships](https://laravel.com/docs/12.x/eloquent-relationships#defining-relationships)
Eloquent relationships are defined as methods on your Eloquent model classes. Since relationships also serve as powerful [query builders](https://laravel.com/docs/12.x/queries), defining relationships as methods provides powerful method chaining and querying capabilities. For example, we may chain additional query constraints on this `posts` relationship:
```


1$user->posts()->where('active', 1)->get();




$user->posts()->where('active', 1)->get();

```

But, before diving too deep into using relationships, let's learn how to define each type of relationship supported by Eloquent.
### [One to One / Has One](https://laravel.com/docs/12.x/eloquent-relationships#one-to-one)
A one-to-one relationship is a very basic type of database relationship. For example, a `User` model might be associated with one `Phone` model. To define this relationship, we will place a `phone` method on the `User` model. The `phone` method should call the `hasOne` method and return its result. The `hasOne` method is available to your model via the model's `Illuminate\Database\Eloquent\Model` base class:
```


 1<?php




 2 



 3namespace App\Models;




 4 



 5use Illuminate\Database\Eloquent\Model;




 6use Illuminate\Database\Eloquent\Relations\HasOne;




 7 



 8class User extends Model




 9{




10    /**




11     * Get the phone associated with the user.




12     */




13    public function phone(): HasOne




14    {




15        return $this->hasOne(Phone::class);




16    }




17}




<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\HasOne;

class User extends Model
{
    /**
     * Get the phone associated with the user.
     */
    public function phone(): HasOne
    {
        return $this->hasOne(Phone::class);
    }
}

```

The first argument passed to the `hasOne` method is the name of the related model class. Once the relationship is defined, we may retrieve the related record using Eloquent's dynamic properties. Dynamic properties allow you to access relationship methods as if they were properties defined on the model:
```


1$phone = User::find(1)->phone;




$phone = User::find(1)->phone;

```

Eloquent determines the foreign key of the relationship based on the parent model name. In this case, the `Phone` model is automatically assumed to have a `user_id` foreign key. If you wish to override this convention, you may pass a second argument to the `hasOne` method:
```


1return $this->hasOne(Phone::class, 'foreign_key');




return $this->hasOne(Phone::class, 'foreign_key');

```

Additionally, Eloquent assumes that the foreign key should have a value matching the primary key column of the parent. In other words, Eloquent will look for the value of the user's `id` column in the `user_id` column of the `Phone` record. If you would like the relationship to use a primary key value other than `id` or your model's `$primaryKey` property, you may pass a third argument to the `hasOne` method:
```


1return $this->hasOne(Phone::class, 'foreign_key', 'local_key');




return $this->hasOne(Phone::class, 'foreign_key', 'local_key');

```

#### [Defining the Inverse of the Relationship](https://laravel.com/docs/12.x/eloquent-relationships#one-to-one-defining-the-inverse-of-the-relationship)
So, we can access the `Phone` model from our `User` model. Next, let's define a relationship on the `Phone` model that will let us access the user that owns the phone. We can define the inverse of a `hasOne` relationship using the `belongsTo` method:
```


 1<?php




 2 



 3namespace App\Models;




 4 



 5use Illuminate\Database\Eloquent\Model;




 6use Illuminate\Database\Eloquent\Relations\BelongsTo;




 7 



 8class Phone extends Model




 9{




10    /**




11     * Get the user that owns the phone.




12     */




13    public function user(): BelongsTo




14    {




15        return $this->belongsTo(User::class);




16    }




17}




<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

class Phone extends Model
{
    /**
     * Get the user that owns the phone.
     */
    public function user(): BelongsTo
    {
        return $this->belongsTo(User::class);
    }
}

```

When invoking the `user` method, Eloquent will attempt to find a `User` model that has an `id` which matches the `user_id` column on the `Phone` model.
Eloquent determines the foreign key name by examining the name of the relationship method and suffixing the method name with `_id`. So, in this case, Eloquent assumes that the `Phone` model has a `user_id` column. However, if the foreign key on the `Phone` model is not `user_id`, you may pass a custom key name as the second argument to the `belongsTo` method:
```


1/**




2 * Get the user that owns the phone.




3 */




4public function user(): BelongsTo




5{




6    return $this->belongsTo(User::class, 'foreign_key');




7}




/**
 * Get the user that owns the phone.
 */
public function user(): BelongsTo
{
    return $this->belongsTo(User::class, 'foreign_key');
}

```

If the parent model does not use `id` as its primary key, or you wish to find the associated model using a different column, you may pass a third argument to the `belongsTo` method specifying the parent table's custom key:
```


1/**




2 * Get the user that owns the phone.




3 */




4public function user(): BelongsTo




5{




6    return $this->belongsTo(User::class, 'foreign_key', 'owner_key');




7}




/**
 * Get the user that owns the phone.
 */
public function user(): BelongsTo
{
    return $this->belongsTo(User::class, 'foreign_key', 'owner_key');
}

```

### [One to Many / Has Many](https://laravel.com/docs/12.x/eloquent-relationships#one-to-many)
A one-to-many relationship is used to define relationships where a single model is the parent to one or more child models. For example, a blog post may have an infinite number of comments. Like all other Eloquent relationships, one-to-many relationships are defined by defining a method on your Eloquent model:
```


 1<?php




 2 



 3namespace App\Models;




 4 



 5use Illuminate\Database\Eloquent\Model;




 6use Illuminate\Database\Eloquent\Relations\HasMany;




 7 



 8class Post extends Model




 9{




10    /**




11     * Get the comments for the blog post.




12     */




13    public function comments(): HasMany




14    {




15        return $this->hasMany(Comment::class);




16    }




17}




<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\HasMany;

class Post extends Model
{
    /**
     * Get the comments for the blog post.
     */
    public function comments(): HasMany
    {
        return $this->hasMany(Comment::class);
    }
}

```

Remember, Eloquent will automatically determine the proper foreign key column for the `Comment` model. By convention, Eloquent will take the "snake case" name of the parent model and suffix it with `_id`. So, in this example, Eloquent will assume the foreign key column on the `Comment` model is `post_id`.
Once the relationship method has been defined, we can access the [collection](https://laravel.com/docs/12.x/eloquent-collections) of related comments by accessing the `comments` property. Remember, since Eloquent provides "dynamic relationship properties", we can access relationship methods as if they were defined as properties on the model:
```


1use App\Models\Post;




2 



3$comments = Post::find(1)->comments;




4 



5foreach ($comments as $comment) {




6    // ...




7}




use App\Models\Post;

$comments = Post::find(1)->comments;

foreach ($comments as $comment) {
    // ...
}

```

Since all relationships also serve as query builders, you may add further constraints to the relationship query by calling the `comments` method and continuing to chain conditions onto the query:
```


1$comment = Post::find(1)->comments()




2    ->where('title', 'foo')




3    ->first();




$comment = Post::find(1)->comments()
    ->where('title', 'foo')
    ->first();

```

Like the `hasOne` method, you may also override the foreign and local keys by passing additional arguments to the `hasMany` method:
```


1return $this->hasMany(Comment::class, 'foreign_key');




2 



3return $this->hasMany(Comment::class, 'foreign_key', 'local_key');




return $this->hasMany(Comment::class, 'foreign_key');

return $this->hasMany(Comment::class, 'foreign_key', 'local_key');

```

#### [Automatically Hydrating Parent Models on Children](https://laravel.com/docs/12.x/eloquent-relationships#automatically-hydrating-parent-models-on-children)
Even when utilizing Eloquent eager loading, "N + 1" query problems can arise if you try to access the parent model from a child model while looping through the child models:
```


1$posts = Post::with('comments')->get();




2 



3foreach ($posts as $post) {




4    foreach ($post->comments as $comment) {




5        echo $comment->post->title;




6    }




7}




$posts = Post::with('comments')->get();

foreach ($posts as $post) {
    foreach ($post->comments as $comment) {
        echo $comment->post->title;
    }
}

```

In the example above, an "N + 1" query problem has been introduced because, even though comments were eager loaded for every `Post` model, Eloquent does not automatically hydrate the parent `Post` on each child `Comment` model.
If you would like Eloquent to automatically hydrate parent models onto their children, you may invoke the `chaperone` method when defining a `hasMany` relationship:
```


 1<?php




 2 



 3namespace App\Models;




 4 



 5use Illuminate\Database\Eloquent\Model;




 6use Illuminate\Database\Eloquent\Relations\HasMany;




 7 



 8class Post extends Model




 9{




10    /**




11     * Get the comments for the blog post.




12     */




13    public function comments(): HasMany




14    {




15        return $this->hasMany(Comment::class)->chaperone();




16    }




17}




<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\HasMany;

class Post extends Model
{
    /**
     * Get the comments for the blog post.
     */
    public function comments(): HasMany
    {
        return $this->hasMany(Comment::class)->chaperone();
    }
}

```

Or, if you would like to opt-in to automatic parent hydration at run time, you may invoke the `chaperone` model when eager loading the relationship:
```


1use App\Models\Post;




2 



3$posts = Post::with([




4    'comments' => fn ($comments) => $comments->chaperone(),




5])->get();




use App\Models\Post;

$posts = Post::with([
    'comments' => fn ($comments) => $comments->chaperone(),
])->get();

```

### [One to Many (Inverse) / Belongs To](https://laravel.com/docs/12.x/eloquent-relationships#one-to-many-inverse)
Now that we can access all of a post's comments, let's define a relationship to allow a comment to access its parent post. To define the inverse of a `hasMany` relationship, define a relationship method on the child model which calls the `belongsTo` method:
```


 1<?php




 2 



 3namespace App\Models;




 4 



 5use Illuminate\Database\Eloquent\Model;




 6use Illuminate\Database\Eloquent\Relations\BelongsTo;




 7 



 8class Comment extends Model




 9{




10    /**




11     * Get the post that owns the comment.




12     */




13    public function post(): BelongsTo




14    {




15        return $this->belongsTo(Post::class);




16    }




17}




<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

class Comment extends Model
{
    /**
     * Get the post that owns the comment.
     */
    public function post(): BelongsTo
    {
        return $this->belongsTo(Post::class);
    }
}

```

Once the relationship has been defined, we can retrieve a comment's parent post by accessing the `post` "dynamic relationship property":
```


1use App\Models\Comment;




2 



3$comment = Comment::find(1);




4 



5return $comment->post->title;




use App\Models\Comment;

$comment = Comment::find(1);

return $comment->post->title;

```

In the example above, Eloquent will attempt to find a `Post` model that has an `id` which matches the `post_id` column on the `Comment` model.
Eloquent determines the default foreign key name by examining the name of the relationship method and suffixing the method name with a `_` followed by the name of the parent model's primary key column. So, in this example, Eloquent will assume the `Post` model's foreign key on the `comments` table is `post_id`.
However, if the foreign key for your relationship does not follow these conventions, you may pass a custom foreign key name as the second argument to the `belongsTo` method:
```


1/**




2 * Get the post that owns the comment.




3 */




4public function post(): BelongsTo




5{




6    return $this->belongsTo(Post::class, 'foreign_key');




7}




/**
 * Get the post that owns the comment.
 */
public function post(): BelongsTo
{
    return $this->belongsTo(Post::class, 'foreign_key');
}

```

If your parent model does not use `id` as its primary key, or you wish to find the associated model using a different column, you may pass a third argument to the `belongsTo` method specifying your parent table's custom key:
```


1/**




2 * Get the post that owns the comment.




3 */




4public function post(): BelongsTo




5{




6    return $this->belongsTo(Post::class, 'foreign_key', 'owner_key');




7}




/**
 * Get the post that owns the comment.
 */
public function post(): BelongsTo
{
    return $this->belongsTo(Post::class, 'foreign_key', 'owner_key');
}

```

#### [Default Models](https://laravel.com/docs/12.x/eloquent-relationships#default-models)
The `belongsTo`, `hasOne`, `hasOneThrough`, and `morphOne` relationships allow you to define a default model that will be returned if the given relationship is `null`. This pattern is often referred to as the `user` relation will return an empty `App\Models\User` model if no user is attached to the `Post` model:
```


1/**




2 * Get the author of the post.




3 */




4public function user(): BelongsTo




5{




6    return $this->belongsTo(User::class)->withDefault();




7}




/**
 * Get the author of the post.
 */
public function user(): BelongsTo
{
    return $this->belongsTo(User::class)->withDefault();
}

```

To populate the default model with attributes, you may pass an array or closure to the `withDefault` method:
```


 1/**




 2 * Get the author of the post.




 3 */




 4public function user(): BelongsTo




 5{




 6    return $this->belongsTo(User::class)->withDefault([




 7        'name' => 'Guest Author',




 8    ]);




 9}




10 



11/**




12 * Get the author of the post.




13 */




14public function user(): BelongsTo




15{




16    return $this->belongsTo(User::class)->withDefault(function (User $user, Post $post) {




17        $user->name = 'Guest Author';




18    });




19}




/**
 * Get the author of the post.
 */
public function user(): BelongsTo
{
    return $this->belongsTo(User::class)->withDefault([
        'name' => 'Guest Author',
    ]);
}

/**
 * Get the author of the post.
 */
public function user(): BelongsTo
{
    return $this->belongsTo(User::class)->withDefault(function (User $user, Post $post) {
        $user->name = 'Guest Author';
    });
}

```

#### [Querying Belongs To Relationships](https://laravel.com/docs/12.x/eloquent-relationships#querying-belongs-to-relationships)
When querying for the children of a "belongs to" relationship, you may manually build the `where` clause to retrieve the corresponding Eloquent models:
```


1use App\Models\Post;




2 



3$posts = Post::where('user_id', $user->id)->get();




use App\Models\Post;

$posts = Post::where('user_id', $user->id)->get();

```

However, you may find it more convenient to use the `whereBelongsTo` method, which will automatically determine the proper relationship and foreign key for the given model:
```


1$posts = Post::whereBelongsTo($user)->get();




$posts = Post::whereBelongsTo($user)->get();

```

You may also provide a [collection](https://laravel.com/docs/12.x/eloquent-collections) instance to the `whereBelongsTo` method. When doing so, Laravel will retrieve models that belong to any of the parent models within the collection:
```


1$users = User::where('vip', true)->get();




2 



3$posts = Post::whereBelongsTo($users)->get();




$users = User::where('vip', true)->get();

$posts = Post::whereBelongsTo($users)->get();

```

By default, Laravel will determine the relationship associated with the given model based on the class name of the model; however, you may specify the relationship name manually by providing it as the second argument to the `whereBelongsTo` method:
```


1$posts = Post::whereBelongsTo($user, 'author')->get();




$posts = Post::whereBelongsTo($user, 'author')->get();

```

### [Has One of Many](https://laravel.com/docs/12.x/eloquent-relationships#has-one-of-many)
Sometimes a model may have many related models, yet you want to easily retrieve the "latest" or "oldest" related model of the relationship. For example, a `User` model may be related to many `Order` models, but you want to define a convenient way to interact with the most recent order the user has placed. You may accomplish this using the `hasOne` relationship type combined with the `ofMany` methods:
```


1/**




2 * Get the user's most recent order.




3 */




4public function latestOrder(): HasOne




5{




6    return $this->hasOne(Order::class)->latestOfMany();




7}




/**
 * Get the user's most recent order.
 */
public function latestOrder(): HasOne
{
    return $this->hasOne(Order::class)->latestOfMany();
}

```

Likewise, you may define a method to retrieve the "oldest", or first, related model of a relationship:
```


1/**




2 * Get the user's oldest order.




3 */




4public function oldestOrder(): HasOne




5{




6    return $this->hasOne(Order::class)->oldestOfMany();




7}




/**
 * Get the user's oldest order.
 */
public function oldestOrder(): HasOne
{
    return $this->hasOne(Order::class)->oldestOfMany();
}

```

By default, the `latestOfMany` and `oldestOfMany` methods will retrieve the latest or oldest related model based on the model's primary key, which must be sortable. However, sometimes you may wish to retrieve a single model from a larger relationship using a different sorting criteria.
For example, using the `ofMany` method, you may retrieve the user's most expensive order. The `ofMany` method accepts the sortable column as its first argument and which aggregate function (`min` or `max`) to apply when querying for the related model:
```


1/**




2 * Get the user's largest order.




3 */




4public function largestOrder(): HasOne




5{




6    return $this->hasOne(Order::class)->ofMany('price', 'max');




7}




/**
 * Get the user's largest order.
 */
public function largestOrder(): HasOne
{
    return $this->hasOne(Order::class)->ofMany('price', 'max');
}

```

Because PostgreSQL does not support executing the `MAX` function against UUID columns, it is not currently possible to use one-of-many relationships in combination with PostgreSQL UUID columns.
#### [Converting "Many" Relationships to Has One Relationships](https://laravel.com/docs/12.x/eloquent-relationships#converting-many-relationships-to-has-one-relationships)
Often, when retrieving a single model using the `latestOfMany`, `oldestOfMany`, or `ofMany` methods, you already have a "has many" relationship defined for the same model. For convenience, Laravel allows you to easily convert this relationship into a "has one" relationship by invoking the `one` method on the relationship:
```


 1/**




 2 * Get the user's orders.




 3 */




 4public function orders(): HasMany




 5{




 6    return $this->hasMany(Order::class);




 7}




 8 



 9/**




10 * Get the user's largest order.




11 */




12public function largestOrder(): HasOne




13{




14    return $this->orders()->one()->ofMany('price', 'max');




15}




/**
 * Get the user's orders.
 */
public function orders(): HasMany
{
    return $this->hasMany(Order::class);
}

/**
 * Get the user's largest order.
 */
public function largestOrder(): HasOne
{
    return $this->orders()->one()->ofMany('price', 'max');
}

```

You may also use the `one` method to convert `HasManyThrough` relationships to `HasOneThrough` relationships:
```


1public function latestDeployment(): HasOneThrough




2{




3    return $this->deployments()->one()->latestOfMany();




4}




public function latestDeployment(): HasOneThrough
{
    return $this->deployments()->one()->latestOfMany();
}

```

#### [Advanced Has One of Many Relationships](https://laravel.com/docs/12.x/eloquent-relationships#advanced-has-one-of-many-relationships)
It is possible to construct more advanced "has one of many" relationships. For example, a `Product` model may have many associated `Price` models that are retained in the system even after new pricing is published. In addition, new pricing data for the product may be able to be published in advance to take effect at a future date via a `published_at` column.
So, in summary, we need to retrieve the latest published pricing where the published date is not in the future. In addition, if two prices have the same published date, we will prefer the price with the greatest ID. To accomplish this, we must pass an array to the `ofMany` method that contains the sortable columns which determine the latest price. In addition, a closure will be provided as the second argument to the `ofMany` method. This closure will be responsible for adding additional publish date constraints to the relationship query:
```


 1/**




 2 * Get the current pricing for the product.




 3 */




 4public function currentPricing(): HasOne




 5{




 6    return $this->hasOne(Price::class)->ofMany([




 7        'published_at' => 'max',




 8        'id' => 'max',




 9    ], function (Builder $query) {




10        $query->where('published_at', '<', now());




11    });




12}




/**
 * Get the current pricing for the product.
 */
public function currentPricing(): HasOne
{
    return $this->hasOne(Price::class)->ofMany([
        'published_at' => 'max',
        'id' => 'max',
    ], function (Builder $query) {
        $query->where('published_at', '<', now());
    });
}

```

### [Has One Through](https://laravel.com/docs/12.x/eloquent-relationships#has-one-through)
The "has-one-through" relationship defines a one-to-one relationship with another model. However, this relationship indicates that the declaring model can be matched with one instance of another model by proceeding _through_ a third model.
For example, in a vehicle repair shop application, each `Mechanic` model may be associated with one `Car` model, and each `Car` model may be associated with one `Owner` model. While the mechanic and the owner have no direct relationship within the database, the mechanic can access the owner _through_ the `Car` model. Let's look at the tables necessary to define this relationship:
```


 1mechanics




 2    id - integer




 3    name - string



 4



 5cars




 6    id - integer




 7    model - string




 8    mechanic_id - integer



 9



10owners




11    id - integer




12    name - string




13    car_id - integer




mechanics
    id - integer
    name - string

cars
    id - integer
    model - string
    mechanic_id - integer

owners
    id - integer
    name - string
    car_id - integer

```

Now that we have examined the table structure for the relationship, let's define the relationship on the `Mechanic` model:
```


 1<?php




 2 



 3namespace App\Models;




 4 



 5use Illuminate\Database\Eloquent\Model;




 6use Illuminate\Database\Eloquent\Relations\HasOneThrough;




 7 



 8class Mechanic extends Model




 9{




10    /**




11     * Get the car's owner.




12     */




13    public function carOwner(): HasOneThrough




14    {




15        return $this->hasOneThrough(Owner::class, Car::class);




16    }




17}




<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\HasOneThrough;

class Mechanic extends Model
{
    /**
     * Get the car's owner.
     */
    public function carOwner(): HasOneThrough
    {
        return $this->hasOneThrough(Owner::class, Car::class);
    }
}

```

The first argument passed to the `hasOneThrough` method is the name of the final model we wish to access, while the second argument is the name of the intermediate model.
Or, if the relevant relationships have already been defined on all of the models involved in the relationship, you may fluently define a "has-one-through" relationship by invoking the `through` method and supplying the names of those relationships. For example, if the `Mechanic` model has a `cars` relationship and the `Car` model has an `owner` relationship, you may define a "has-one-through" relationship connecting the mechanic and the owner like so:
```


1// String based syntax...




2return $this->through('cars')->has('owner');




3 



4// Dynamic syntax...




5return $this->throughCars()->hasOwner();




// String based syntax...
return $this->through('cars')->has('owner');

// Dynamic syntax...
return $this->throughCars()->hasOwner();

```

#### [Key Conventions](https://laravel.com/docs/12.x/eloquent-relationships#has-one-through-key-conventions)
Typical Eloquent foreign key conventions will be used when performing the relationship's queries. If you would like to customize the keys of the relationship, you may pass them as the third and fourth arguments to the `hasOneThrough` method. The third argument is the name of the foreign key on the intermediate model. The fourth argument is the name of the foreign key on the final model. The fifth argument is the local key, while the sixth argument is the local key of the intermediate model:
```


 1class Mechanic extends Model




 2{




 3    /**




 4     * Get the car's owner.




 5     */




 6    public function carOwner(): HasOneThrough




 7    {




 8        return $this->hasOneThrough(




 9            Owner::class,




10            Car::class,




11            'mechanic_id', // Foreign key on the cars table...




12            'car_id', // Foreign key on the owners table...




13            'id', // Local key on the mechanics table...




14            'id' // Local key on the cars table...




15        );




16    }




17}




class Mechanic extends Model
{
    /**
     * Get the car's owner.
     */
    public function carOwner(): HasOneThrough
    {
        return $this->hasOneThrough(
            Owner::class,
            Car::class,
            'mechanic_id', // Foreign key on the cars table...
            'car_id', // Foreign key on the owners table...
            'id', // Local key on the mechanics table...
            'id' // Local key on the cars table...
        );
    }
}

```

Or, as discussed earlier, if the relevant relationships have already been defined on all of the models involved in the relationship, you may fluently define a "has-one-through" relationship by invoking the `through` method and supplying the names of those relationships. This approach offers the advantage of reusing the key conventions already defined on the existing relationships:
```


1// String based syntax...




2return $this->through('cars')->has('owner');




3 



4// Dynamic syntax...




5return $this->throughCars()->hasOwner();




// String based syntax...
return $this->through('cars')->has('owner');

// Dynamic syntax...
return $this->throughCars()->hasOwner();

```

### [Has Many Through](https://laravel.com/docs/12.x/eloquent-relationships#has-many-through)
The "has-many-through" relationship provides a convenient way to access distant relations via an intermediate relation. For example, let's assume we are building a deployment platform like [Laravel Cloud](https://cloud.laravel.com). An `Application` model might access many `Deployment` models through an intermediate `Environment` model. Using this example, you could easily gather all deployments for a given application. Let's look at the tables required to define this relationship:
```


 1applications




 2    id - integer




 3    name - string



 4



 5environments




 6    id - integer




 7    application_id - integer




 8    name - string



 9



10deployments




11    id - integer




12    environment_id - integer




13    commit_hash - string




applications
    id - integer
    name - string

environments
    id - integer
    application_id - integer
    name - string

deployments
    id - integer
    environment_id - integer
    commit_hash - string

```

Now that we have examined the table structure for the relationship, let's define the relationship on the `Application` model:
```


 1<?php




 2 



 3namespace App\Models;




 4 



 5use Illuminate\Database\Eloquent\Model;




 6use Illuminate\Database\Eloquent\Relations\HasManyThrough;




 7 



 8class Application extends Model




 9{




10    /**




11     * Get all of the deployments for the application.




12     */




13    public function deployments(): HasManyThrough




14    {




15        return $this->hasManyThrough(Deployment::class, Environment::class);




16    }




17}




<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\HasManyThrough;

class Application extends Model
{
    /**
     * Get all of the deployments for the application.
     */
    public function deployments(): HasManyThrough
    {
        return $this->hasManyThrough(Deployment::class, Environment::class);
    }
}

```

The first argument passed to the `hasManyThrough` method is the name of the final model we wish to access, while the second argument is the name of the intermediate model.
Or, if the relevant relationships have already been defined on all of the models involved in the relationship, you may fluently define a "has-many-through" relationship by invoking the `through` method and supplying the names of those relationships. For example, if the `Application` model has a `environments` relationship and the `Environment` model has a `deployments` relationship, you may define a "has-many-through" relationship connecting the application and the deployments like so:
```


1// String based syntax...




2return $this->through('environments')->has('deployments');




3 



4// Dynamic syntax...




5return $this->throughEnvironments()->hasDeployments();




// String based syntax...
return $this->through('environments')->has('deployments');

// Dynamic syntax...
return $this->throughEnvironments()->hasDeployments();

```

Though the `Deployment` model's table does not contain a `application_id` column, the `hasManyThrough` relation provides access to an application's deployments via `$application->deployments`. To retrieve these models, Eloquent inspects the `application_id` column on the intermediate `Environment` model's table. After finding the relevant environment IDs, they are used to query the `Deployment` model's table.
#### [Key Conventions](https://laravel.com/docs/12.x/eloquent-relationships#has-many-through-key-conventions)
Typical Eloquent foreign key conventions will be used when performing the relationship's queries. If you would like to customize the keys of the relationship, you may pass them as the third and fourth arguments to the `hasManyThrough` method. The third argument is the name of the foreign key on the intermediate model. The fourth argument is the name of the foreign key on the final model. The fifth argument is the local key, while the sixth argument is the local key of the intermediate model:
```


 1class Application extends Model




 2{




 3    public function deployments(): HasManyThrough




 4    {




 5        return $this->hasManyThrough(




 6            Deployment::class,




 7            Environment::class,




 8            'application_id', // Foreign key on the environments table...




 9            'environment_id', // Foreign key on the deployments table...




10            'id', // Local key on the applications table...




11            'id' // Local key on the environments table...




12        );




13    }




14}




class Application extends Model
{
    public function deployments(): HasManyThrough
    {
        return $this->hasManyThrough(
            Deployment::class,
            Environment::class,
            'application_id', // Foreign key on the environments table...
            'environment_id', // Foreign key on the deployments table...
            'id', // Local key on the applications table...
            'id' // Local key on the environments table...
        );
    }
}

```

Or, as discussed earlier, if the relevant relationships have already been defined on all of the models involved in the relationship, you may fluently define a "has-many-through" relationship by invoking the `through` method and supplying the names of those relationships. This approach offers the advantage of reusing the key conventions already defined on the existing relationships:
```


1// String based syntax...




2return $this->through('environments')->has('deployments');




3 



4// Dynamic syntax...




5return $this->throughEnvironments()->hasDeployments();




// String based syntax...
return $this->through('environments')->has('deployments');

// Dynamic syntax...
return $this->throughEnvironments()->hasDeployments();

```

### [Scoped Relationships](https://laravel.com/docs/12.x/eloquent-relationships#scoped-relationships)
It's common to add additional methods to models that constrain relationships. For example, you might add a `featuredPosts` method to a `User` model which constrains the broader `posts` relationship with an additional `where` constraint:
```


 1<?php




 2 



 3namespace App\Models;




 4 



 5use Illuminate\Database\Eloquent\Model;




 6use Illuminate\Database\Eloquent\Relations\HasMany;




 7 



 8class User extends Model




 9{




10    /**




11     * Get the user's posts.




12     */




13    public function posts(): HasMany




14    {




15        return $this->hasMany(Post::class)->latest();




16    }




17 



18    /**




19     * Get the user's featured posts.




20     */




21    public function featuredPosts(): HasMany




22    {




23        return $this->posts()->where('featured', true);




24    }




25}




<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\HasMany;

class User extends Model
{
    /**
     * Get the user's posts.
     */
    public function posts(): HasMany
    {
        return $this->hasMany(Post::class)->latest();
    }

    /**
     * Get the user's featured posts.
     */
    public function featuredPosts(): HasMany
    {
        return $this->posts()->where('featured', true);
    }
}

```

However, if you attempt to create a model via the `featuredPosts` method, its `featured` attribute would not be set to `true`. If you would like to create models via relationship methods and also specify attributes that should be added to all models created via that relationship, you may use the `withAttributes` method when building the relationship query:
```


1/**




2 * Get the user's featured posts.




3 */




4public function featuredPosts(): HasMany




5{




6    return $this->posts()->withAttributes(['featured' => true]);




7}




/**
 * Get the user's featured posts.
 */
public function featuredPosts(): HasMany
{
    return $this->posts()->withAttributes(['featured' => true]);
}

```

The `withAttributes` method will add `where` conditions to the query using the given attributes, and it will also add the given attributes to any models created via the relationship method:
```


1$post = $user->featuredPosts()->create(['title' => 'Featured Post']);




2 



3$post->featured; // true




$post = $user->featuredPosts()->create(['title' => 'Featured Post']);

$post->featured; // true

```

To instruct the `withAttributes` method to not add `where` conditions to the query, you may set the `asConditions` argument to `false`:
```


1return $this->posts()->withAttributes(['featured' => true], asConditions: false);




return $this->posts()->withAttributes(['featured' => true], asConditions: false);

```
