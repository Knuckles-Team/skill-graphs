## [Eager Loading](https://laravel.com/docs/12.x/eloquent-relationships#eager-loading)
When accessing Eloquent relationships as properties, the related models are "lazy loaded". This means the relationship data is not actually loaded until you first access the property. However, Eloquent can "eager load" relationships at the time you query the parent model. Eager loading alleviates the "N + 1" query problem. To illustrate the N + 1 query problem, consider a `Book` model that "belongs to" to an `Author` model:
```


 1<?php




 2 



 3namespace App\Models;




 4 



 5use Illuminate\Database\Eloquent\Model;




 6use Illuminate\Database\Eloquent\Relations\BelongsTo;




 7 



 8class Book extends Model




 9{




10    /**




11     * Get the author that wrote the book.




12     */




13    public function author(): BelongsTo




14    {




15        return $this->belongsTo(Author::class);




16    }




17}




<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

class Book extends Model
{
    /**
     * Get the author that wrote the book.
     */
    public function author(): BelongsTo
    {
        return $this->belongsTo(Author::class);
    }
}

```

Now, let's retrieve all books and their authors:
```


1use App\Models\Book;




2 



3$books = Book::all();




4 



5foreach ($books as $book) {




6    echo $book->author->name;




7}




use App\Models\Book;

$books = Book::all();

foreach ($books as $book) {
    echo $book->author->name;
}

```

This loop will execute one query to retrieve all of the books within the database table, then another query for each book in order to retrieve the book's author. So, if we have 25 books, the code above would run 26 queries: one for the original book, and 25 additional queries to retrieve the author of each book.
Thankfully, we can use eager loading to reduce this operation to just two queries. When building a query, you may specify which relationships should be eager loaded using the `with` method:
```


1$books = Book::with('author')->get();




2 



3foreach ($books as $book) {




4    echo $book->author->name;




5}




$books = Book::with('author')->get();

foreach ($books as $book) {
    echo $book->author->name;
}

```

For this operation, only two queries will be executed - one query to retrieve all of the books and one query to retrieve all of the authors for all of the books:
```


1select * from books




2 



3select * from authors where id in (1, 2, 3, 4, 5, ...)




select * from books

select * from authors where id in (1, 2, 3, 4, 5, ...)

```

#### [Eager Loading Multiple Relationships](https://laravel.com/docs/12.x/eloquent-relationships#eager-loading-multiple-relationships)
Sometimes you may need to eager load several different relationships. To do so, just pass an array of relationships to the `with` method:
```


1$books = Book::with(['author', 'publisher'])->get();




$books = Book::with(['author', 'publisher'])->get();

```

#### [Nested Eager Loading](https://laravel.com/docs/12.x/eloquent-relationships#nested-eager-loading)
To eager load a relationship's relationships, you may use "dot" syntax. For example, let's eager load all of the book's authors and all of the author's personal contacts:
```


1$books = Book::with('author.contacts')->get();




$books = Book::with('author.contacts')->get();

```

Alternatively, you may specify nested eager loaded relationships by providing a nested array to the `with` method, which can be convenient when eager loading multiple nested relationships:
```


1$books = Book::with([




2    'author' => [




3        'contacts',




4        'publisher',




5    ],




6])->get();




$books = Book::with([
    'author' => [
        'contacts',
        'publisher',
    ],
])->get();

```

#### [Nested Eager Loading `morphTo` Relationships](https://laravel.com/docs/12.x/eloquent-relationships#nested-eager-loading-morphto-relationships)
If you would like to eager load a `morphTo` relationship, as well as nested relationships on the various entities that may be returned by that relationship, you may use the `with` method in combination with the `morphTo` relationship's `morphWith` method. To help illustrate this method, let's consider the following model:
```


 1<?php




 2 



 3use Illuminate\Database\Eloquent\Model;




 4use Illuminate\Database\Eloquent\Relations\MorphTo;




 5 



 6class ActivityFeed extends Model




 7{




 8    /**




 9     * Get the parent of the activity feed record.




10     */




11    public function parentable(): MorphTo




12    {




13        return $this->morphTo();




14    }




15}




<?php

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\MorphTo;

class ActivityFeed extends Model
{
    /**
     * Get the parent of the activity feed record.
     */
    public function parentable(): MorphTo
    {
        return $this->morphTo();
    }
}

```

In this example, let's assume `Event`, `Photo`, and `Post` models may create `ActivityFeed` models. Additionally, let's assume that `Event` models belong to a `Calendar` model, `Photo` models are associated with `Tag` models, and `Post` models belong to an `Author` model.
Using these model definitions and relationships, we may retrieve `ActivityFeed` model instances and eager load all `parentable` models and their respective nested relationships:
```


 1use Illuminate\Database\Eloquent\Relations\MorphTo;




 2 



 3$activities = ActivityFeed::query()




 4    ->with(['parentable' => function (MorphTo $morphTo) {




 5        $morphTo->morphWith([




 6            Event::class => ['calendar'],




 7            Photo::class => ['tags'],




 8            Post::class => ['author'],




 9        ]);




10    }])->get();




use Illuminate\Database\Eloquent\Relations\MorphTo;

$activities = ActivityFeed::query()
    ->with(['parentable' => function (MorphTo $morphTo) {
        $morphTo->morphWith([
            Event::class => ['calendar'],
            Photo::class => ['tags'],
            Post::class => ['author'],
        ]);
    }])->get();

```

#### [Eager Loading Specific Columns](https://laravel.com/docs/12.x/eloquent-relationships#eager-loading-specific-columns)
You may not always need every column from the relationships you are retrieving. For this reason, Eloquent allows you to specify which columns of the relationship you would like to retrieve:
```


1$books = Book::with('author:id,name,book_id')->get();




$books = Book::with('author:id,name,book_id')->get();

```

When using this feature, you should always include the `id` column and any relevant foreign key columns in the list of columns you wish to retrieve.
#### [Eager Loading by Default](https://laravel.com/docs/12.x/eloquent-relationships#eager-loading-by-default)
Sometimes you might want to always load some relationships when retrieving a model. To accomplish this, you may define a `$with` property on the model:
```


 1<?php




 2 



 3namespace App\Models;




 4 



 5use Illuminate\Database\Eloquent\Model;




 6use Illuminate\Database\Eloquent\Relations\BelongsTo;




 7 



 8class Book extends Model




 9{




10    /**




11     * The relationships that should always be loaded.




12     *




13     * @var array




14     */




15    protected $with = ['author'];




16 



17    /**




18     * Get the author that wrote the book.




19     */




20    public function author(): BelongsTo




21    {




22        return $this->belongsTo(Author::class);




23    }




24 



25    /**




26     * Get the genre of the book.




27     */




28    public function genre(): BelongsTo




29    {




30        return $this->belongsTo(Genre::class);




31    }




32}




<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

class Book extends Model
{
    /**
     * The relationships that should always be loaded.
     *
     * @var array
     */
    protected $with = ['author'];

    /**
     * Get the author that wrote the book.
     */
    public function author(): BelongsTo
    {
        return $this->belongsTo(Author::class);
    }

    /**
     * Get the genre of the book.
     */
    public function genre(): BelongsTo
    {
        return $this->belongsTo(Genre::class);
    }
}

```

If you would like to remove an item from the `$with` property for a single query, you may use the `without` method:
```


1$books = Book::without('author')->get();




$books = Book::without('author')->get();

```

If you would like to override all items within the `$with` property for a single query, you may use the `withOnly` method:
```


1$books = Book::withOnly('genre')->get();




$books = Book::withOnly('genre')->get();

```

### [Constraining Eager Loads](https://laravel.com/docs/12.x/eloquent-relationships#constraining-eager-loads)
Sometimes you may wish to eager load a relationship but also specify additional query conditions for the eager loading query. You can accomplish this by passing an array of relationships to the `with` method where the array key is a relationship name and the array value is a closure that adds additional constraints to the eager loading query:
```


1use App\Models\User;




2 



3$users = User::with(['posts' => function ($query) {




4    $query->where('title', 'like', '%code%');




5}])->get();




use App\Models\User;

$users = User::with(['posts' => function ($query) {
    $query->where('title', 'like', '%code%');
}])->get();

```

In this example, Eloquent will only eager load posts where the post's `title` column contains the word `code`. You may call other [query builder](https://laravel.com/docs/12.x/queries) methods to further customize the eager loading operation:
```


1$users = User::with(['posts' => function ($query) {




2    $query->orderBy('created_at', 'desc');




3}])->get();




$users = User::with(['posts' => function ($query) {
    $query->orderBy('created_at', 'desc');
}])->get();

```

#### [Constraining Eager Loading of `morphTo` Relationships](https://laravel.com/docs/12.x/eloquent-relationships#constraining-eager-loading-of-morph-to-relationships)
If you are eager loading a `morphTo` relationship, Eloquent will run multiple queries to fetch each type of related model. You may add additional constraints to each of these queries using the `MorphTo` relation's `constrain` method:
```


 1use Illuminate\Database\Eloquent\Relations\MorphTo;




 2 



 3$comments = Comment::with(['commentable' => function (MorphTo $morphTo) {




 4    $morphTo->constrain([




 5        Post::class => function ($query) {




 6            $query->whereNull('hidden_at');




 7        },




 8        Video::class => function ($query) {




 9            $query->where('type', 'educational');




10        },




11    ]);




12}])->get();




use Illuminate\Database\Eloquent\Relations\MorphTo;

$comments = Comment::with(['commentable' => function (MorphTo $morphTo) {
    $morphTo->constrain([
        Post::class => function ($query) {
            $query->whereNull('hidden_at');
        },
        Video::class => function ($query) {
            $query->where('type', 'educational');
        },
    ]);
}])->get();

```

In this example, Eloquent will only eager load posts that have not been hidden and videos that have a `type` value of "educational".
#### [Constraining Eager Loads With Relationship Existence](https://laravel.com/docs/12.x/eloquent-relationships#constraining-eager-loads-with-relationship-existence)
You may sometimes find yourself needing to check for the existence of a relationship while simultaneously loading the relationship based on the same conditions. For example, you may wish to only retrieve `User` models that have child `Post` models matching a given query condition while also eager loading the matching posts. You may accomplish this using the `withWhereHas` method:
```


1use App\Models\User;




2 



3$users = User::withWhereHas('posts', function ($query) {




4    $query->where('featured', true);




5})->get();




use App\Models\User;

$users = User::withWhereHas('posts', function ($query) {
    $query->where('featured', true);
})->get();

```

### [Lazy Eager Loading](https://laravel.com/docs/12.x/eloquent-relationships#lazy-eager-loading)
Sometimes you may need to eager load a relationship after the parent model has already been retrieved. For example, this may be useful if you need to dynamically decide whether to load related models:
```


1use App\Models\Book;




2 



3$books = Book::all();




4 



5if ($condition) {




6    $books->load('author', 'publisher');




7}




use App\Models\Book;

$books = Book::all();

if ($condition) {
    $books->load('author', 'publisher');
}

```

If you need to set additional query constraints on the eager loading query, you may pass an array keyed by the relationships you wish to load. The array values should be closure instances which receive the query instance:
```


1$author->load(['books' => function ($query) {




2    $query->orderBy('published_date', 'asc');




3}]);




$author->load(['books' => function ($query) {
    $query->orderBy('published_date', 'asc');
}]);

```

To load a relationship only when it has not already been loaded, use the `loadMissing` method:
```


1$book->loadMissing('author');




$book->loadMissing('author');

```

#### [Nested Lazy Eager Loading and `morphTo`](https://laravel.com/docs/12.x/eloquent-relationships#nested-lazy-eager-loading-morphto)
If you would like to eager load a `morphTo` relationship, as well as nested relationships on the various entities that may be returned by that relationship, you may use the `loadMorph` method.
This method accepts the name of the `morphTo` relationship as its first argument, and an array of model / relationship pairs as its second argument. To help illustrate this method, let's consider the following model:
```


 1<?php




 2 



 3use Illuminate\Database\Eloquent\Model;




 4use Illuminate\Database\Eloquent\Relations\MorphTo;




 5 



 6class ActivityFeed extends Model




 7{




 8    /**




 9     * Get the parent of the activity feed record.




10     */




11    public function parentable(): MorphTo




12    {




13        return $this->morphTo();




14    }




15}




<?php

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\MorphTo;

class ActivityFeed extends Model
{
    /**
     * Get the parent of the activity feed record.
     */
    public function parentable(): MorphTo
    {
        return $this->morphTo();
    }
}

```

In this example, let's assume `Event`, `Photo`, and `Post` models may create `ActivityFeed` models. Additionally, let's assume that `Event` models belong to a `Calendar` model, `Photo` models are associated with `Tag` models, and `Post` models belong to an `Author` model.
Using these model definitions and relationships, we may retrieve `ActivityFeed` model instances and eager load all `parentable` models and their respective nested relationships:
```


1$activities = ActivityFeed::with('parentable')




2    ->get()




3    ->loadMorph('parentable', [




4        Event::class => ['calendar'],




5        Photo::class => ['tags'],




6        Post::class => ['author'],




7    ]);




$activities = ActivityFeed::with('parentable')
    ->get()
    ->loadMorph('parentable', [
        Event::class => ['calendar'],
        Photo::class => ['tags'],
        Post::class => ['author'],
    ]);

```

### [Automatic Eager Loading](https://laravel.com/docs/12.x/eloquent-relationships#automatic-eager-loading)
This feature is currently in beta in order to gather community feedback. The behavior and functionality of this feature may change even on patch releases.
In many cases, Laravel can automatically eager load the relationships you access. To enable automatic eager loading, you should invoke the `Model::automaticallyEagerLoadRelationships` method within the `boot` method of your application's `AppServiceProvider`:
```


1use Illuminate\Database\Eloquent\Model;




2 



3/**




4 * Bootstrap any application services.




5 */




6public function boot(): void




7{




8    Model::automaticallyEagerLoadRelationships();




9}




use Illuminate\Database\Eloquent\Model;

/**
 * Bootstrap any application services.
 */
public function boot(): void
{
    Model::automaticallyEagerLoadRelationships();
}

```

When this feature is enabled, Laravel will attempt to automatically load any relationships you access that have not been previously loaded. For example, consider the following scenario:
```


 1use App\Models\User;




 2 



 3$users = User::all();




 4 



 5foreach ($users as $user) {




 6    foreach ($user->posts as $post) {




 7        foreach ($post->comments as $comment) {




 8            echo $comment->content;




 9        }




10    }




11}




use App\Models\User;

$users = User::all();

foreach ($users as $user) {
    foreach ($user->posts as $post) {
        foreach ($post->comments as $comment) {
            echo $comment->content;
        }
    }
}

```

Typically, the code above would execute a query for each user in order to retrieve their posts, as well as a query for each post to retrieve its comments. However, when the `automaticallyEagerLoadRelationships` feature has been enabled, Laravel will automatically [lazy eager load](https://laravel.com/docs/12.x/eloquent-relationships#lazy-eager-loading) the posts for all users in the user collection when you attempt to access the posts on any of the retrieved users. Likewise, when you attempt to access the comments for any retrieved post, all comments will be lazy eager loaded for all posts that were originally retrieved.
If you do not want to globally enable automatic eager loading, you can still enable this feature for a single Eloquent collection instance by invoking the `withRelationshipAutoloading` method on the collection:
```


1$users = User::where('vip', true)->get();




2 



3return $users->withRelationshipAutoloading();




$users = User::where('vip', true)->get();

return $users->withRelationshipAutoloading();

```

### [Preventing Lazy Loading](https://laravel.com/docs/12.x/eloquent-relationships#preventing-lazy-loading)
As previously discussed, eager loading relationships can often provide significant performance benefits to your application. Therefore, if you would like, you may instruct Laravel to always prevent the lazy loading of relationships. To accomplish this, you may invoke the `preventLazyLoading` method offered by the base Eloquent model class. Typically, you should call this method within the `boot` method of your application's `AppServiceProvider` class.
The `preventLazyLoading` method accepts an optional boolean argument that indicates if lazy loading should be prevented. For example, you may wish to only disable lazy loading in non-production environments so that your production environment will continue to function normally even if a lazy loaded relationship is accidentally present in production code:
```


1use Illuminate\Database\Eloquent\Model;




2 



3/**




4 * Bootstrap any application services.




5 */




6public function boot(): void




7{




8    Model::preventLazyLoading(! $this->app->isProduction());




9}




use Illuminate\Database\Eloquent\Model;

/**
 * Bootstrap any application services.
 */
public function boot(): void
{
    Model::preventLazyLoading(! $this->app->isProduction());
}

```

After preventing lazy loading, Eloquent will throw a `Illuminate\Database\LazyLoadingViolationException` exception when your application attempts to lazy load any Eloquent relationship.
You may customize the behavior of lazy loading violations using the `handleLazyLoadingViolationsUsing` method. For example, using this method, you may instruct lazy loading violations to only be logged instead of interrupting the application's execution with exceptions:
```


1Model::handleLazyLoadingViolationUsing(function (Model $model, string $relation) {




2    $class = $model::class;




3 



4    info("Attempted to lazy load [{$relation}] on model [{$class}].");




5});




Model::handleLazyLoadingViolationUsing(function (Model $model, string $relation) {
    $class = $model::class;

    info("Attempted to lazy load [{$relation}] on model [{$class}].");
});

```
