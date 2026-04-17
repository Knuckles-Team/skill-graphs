## [Querying Relations](https://laravel.com/docs/12.x/eloquent-relationships#querying-relations)
Since all Eloquent relationships are defined via methods, you may call those methods to obtain an instance of the relationship without actually executing a query to load the related models. In addition, all types of Eloquent relationships also serve as [query builders](https://laravel.com/docs/12.x/queries), allowing you to continue to chain constraints onto the relationship query before finally executing the SQL query against your database.
For example, imagine a blog application in which a `User` model has many associated `Post` models:
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




11     * Get all of the posts for the user.




12     */




13    public function posts(): HasMany




14    {




15        return $this->hasMany(Post::class);




16    }




17}




<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\HasMany;

class User extends Model
{
    /**
     * Get all of the posts for the user.
     */
    public function posts(): HasMany
    {
        return $this->hasMany(Post::class);
    }
}

```

You may query the `posts` relationship and add additional constraints to the relationship like so:
```


1use App\Models\User;




2 



3$user = User::find(1);




4 



5$user->posts()->where('active', 1)->get();




use App\Models\User;

$user = User::find(1);

$user->posts()->where('active', 1)->get();

```

You are able to use any of the Laravel [query builder's](https://laravel.com/docs/12.x/queries) methods on the relationship, so be sure to explore the query builder documentation to learn about all of the methods that are available to you.
#### [Chaining `orWhere` Clauses After Relationships](https://laravel.com/docs/12.x/eloquent-relationships#chaining-orwhere-clauses-after-relationships)
As demonstrated in the example above, you are free to add additional constraints to relationships when querying them. However, use caution when chaining `orWhere` clauses onto a relationship, as the `orWhere` clauses will be logically grouped at the same level as the relationship constraint:
```


1$user->posts()




2    ->where('active', 1)




3    ->orWhere('votes', '>=', 100)




4    ->get();




$user->posts()
    ->where('active', 1)
    ->orWhere('votes', '>=', 100)
    ->get();

```

The example above will generate the following SQL. As you can see, the `or` clause instructs the query to return _any_ post with greater than 100 votes. The query is no longer constrained to a specific user:
```


1select *




2from posts




3where user_id = ? and active = 1 or votes >= 100




select *
from posts
where user_id = ? and active = 1 or votes >= 100

```

In most situations, you should use [logical groups](https://laravel.com/docs/12.x/queries#logical-grouping) to group the conditional checks between parentheses:
```


1use Illuminate\Database\Eloquent\Builder;




2 



3$user->posts()




4    ->where(function (Builder $query) {




5        return $query->where('active', 1)




6            ->orWhere('votes', '>=', 100);




7    })




8    ->get();




use Illuminate\Database\Eloquent\Builder;

$user->posts()
    ->where(function (Builder $query) {
        return $query->where('active', 1)
            ->orWhere('votes', '>=', 100);
    })
    ->get();

```

The example above will produce the following SQL. Note that the logical grouping has properly grouped the constraints and the query remains constrained to a specific user:
```


1select *




2from posts




3where user_id = ? and (active = 1 or votes >= 100)




select *
from posts
where user_id = ? and (active = 1 or votes >= 100)

```

### [Relationship Methods vs. Dynamic Properties](https://laravel.com/docs/12.x/eloquent-relationships#relationship-methods-vs-dynamic-properties)
If you do not need to add additional constraints to an Eloquent relationship query, you may access the relationship as if it were a property. For example, continuing to use our `User` and `Post` example models, we may access all of a user's posts like so:
```


1use App\Models\User;




2 



3$user = User::find(1);




4 



5foreach ($user->posts as $post) {




6    // ...




7}




use App\Models\User;

$user = User::find(1);

foreach ($user->posts as $post) {
    // ...
}

```

Dynamic relationship properties perform "lazy loading", meaning they will only load their relationship data when you actually access them. Because of this, developers often use [eager loading](https://laravel.com/docs/12.x/eloquent-relationships#eager-loading) to pre-load relationships they know will be accessed after loading the model. Eager loading provides a significant reduction in SQL queries that must be executed to load a model's relations.
### [Querying Relationship Existence](https://laravel.com/docs/12.x/eloquent-relationships#querying-relationship-existence)
When retrieving model records, you may wish to limit your results based on the existence of a relationship. For example, imagine you want to retrieve all blog posts that have at least one comment. To do so, you may pass the name of the relationship to the `has` and `orHas` methods:
```


1use App\Models\Post;




2 



3// Retrieve all posts that have at least one comment...




4$posts = Post::has('comments')->get();




use App\Models\Post;

// Retrieve all posts that have at least one comment...
$posts = Post::has('comments')->get();

```

You may also specify an operator and count value to further customize the query:
```


1// Retrieve all posts that have three or more comments...




2$posts = Post::has('comments', '>=', 3)->get();




// Retrieve all posts that have three or more comments...
$posts = Post::has('comments', '>=', 3)->get();

```

Nested `has` statements may be constructed using "dot" notation. For example, you may retrieve all posts that have at least one comment that has at least one image:
```


1// Retrieve posts that have at least one comment with images...




2$posts = Post::has('comments.images')->get();




// Retrieve posts that have at least one comment with images...
$posts = Post::has('comments.images')->get();

```

If you need even more power, you may use the `whereHas` and `orWhereHas` methods to define additional query constraints on your `has` queries, such as inspecting the content of a comment:
```


 1use Illuminate\Database\Eloquent\Builder;




 2 



 3// Retrieve posts with at least one comment containing words like code%...




 4$posts = Post::whereHas('comments', function (Builder $query) {




 5    $query->where('content', 'like', 'code%');




 6})->get();




 7 



 8// Retrieve posts with at least ten comments containing words like code%...




 9$posts = Post::whereHas('comments', function (Builder $query) {




10    $query->where('content', 'like', 'code%');




11}, '>=', 10)->get();




use Illuminate\Database\Eloquent\Builder;

// Retrieve posts with at least one comment containing words like code%...
$posts = Post::whereHas('comments', function (Builder $query) {
    $query->where('content', 'like', 'code%');
})->get();

// Retrieve posts with at least ten comments containing words like code%...
$posts = Post::whereHas('comments', function (Builder $query) {
    $query->where('content', 'like', 'code%');
}, '>=', 10)->get();

```

Eloquent does not currently support querying for relationship existence across databases. The relationships must exist within the same database.
#### [Many to Many Relationship Existence Queries](https://laravel.com/docs/12.x/eloquent-relationships#many-to-many-relationship-existence-queries)
The `whereAttachedTo` method may be used to query for models that have a many to many attachment to a model or collection of models:
```


1$users = User::whereAttachedTo($role)->get();




$users = User::whereAttachedTo($role)->get();

```

You may also provide a [collection](https://laravel.com/docs/12.x/eloquent-collections) instance to the `whereAttachedTo` method. When doing so, Laravel will retrieve models that are attached to any of the models within the collection:
```


1$tags = Tag::whereLike('name', '%laravel%')->get();




2 



3$posts = Post::whereAttachedTo($tags)->get();




$tags = Tag::whereLike('name', '%laravel%')->get();

$posts = Post::whereAttachedTo($tags)->get();

```

#### [Inline Relationship Existence Queries](https://laravel.com/docs/12.x/eloquent-relationships#inline-relationship-existence-queries)
If you would like to query for a relationship's existence with a single, simple where condition attached to the relationship query, you may find it more convenient to use the `whereRelation`, `orWhereRelation`, `whereMorphRelation`, and `orWhereMorphRelation` methods. For example, we may query for all posts that have unapproved comments:
```


1use App\Models\Post;




2 



3$posts = Post::whereRelation('comments', 'is_approved', false)->get();




use App\Models\Post;

$posts = Post::whereRelation('comments', 'is_approved', false)->get();

```

Of course, like calls to the query builder's `where` method, you may also specify an operator:
```


1$posts = Post::whereRelation(




2    'comments', 'created_at', '>=', now()->minus(hours: 1)




3)->get();




$posts = Post::whereRelation(
    'comments', 'created_at', '>=', now()->minus(hours: 1)
)->get();

```

### [Querying Relationship Absence](https://laravel.com/docs/12.x/eloquent-relationships#querying-relationship-absence)
When retrieving model records, you may wish to limit your results based on the absence of a relationship. For example, imagine you want to retrieve all blog posts that **don't** have any comments. To do so, you may pass the name of the relationship to the `doesntHave` and `orDoesntHave` methods:
```


1use App\Models\Post;




2 



3$posts = Post::doesntHave('comments')->get();




use App\Models\Post;

$posts = Post::doesntHave('comments')->get();

```

If you need even more power, you may use the `whereDoesntHave` and `orWhereDoesntHave` methods to add additional query constraints to your `doesntHave` queries, such as inspecting the content of a comment:
```


1use Illuminate\Database\Eloquent\Builder;




2 



3$posts = Post::whereDoesntHave('comments', function (Builder $query) {




4    $query->where('content', 'like', 'code%');




5})->get();




use Illuminate\Database\Eloquent\Builder;

$posts = Post::whereDoesntHave('comments', function (Builder $query) {
    $query->where('content', 'like', 'code%');
})->get();

```

You may use "dot" notation to execute a query against a nested relationship. For example, the following query will retrieve all posts that do not have comments as well as posts that have comments where none of the comments are from banned users:
```


1use Illuminate\Database\Eloquent\Builder;




2 



3$posts = Post::whereDoesntHave('comments.author', function (Builder $query) {




4    $query->where('banned', 1);




5})->get();




use Illuminate\Database\Eloquent\Builder;

$posts = Post::whereDoesntHave('comments.author', function (Builder $query) {
    $query->where('banned', 1);
})->get();

```

### [Querying Morph To Relationships](https://laravel.com/docs/12.x/eloquent-relationships#querying-morph-to-relationships)
To query the existence of "morph to" relationships, you may use the `whereHasMorph` and `whereDoesntHaveMorph` methods. These methods accept the name of the relationship as their first argument. Next, the methods accept the names of the related models that you wish to include in the query. Finally, you may provide a closure which customizes the relationship query:
```


 1use App\Models\Comment;




 2use App\Models\Post;




 3use App\Models\Video;




 4use Illuminate\Database\Eloquent\Builder;




 5 



 6// Retrieve comments associated to posts or videos with a title like code%...




 7$comments = Comment::whereHasMorph(




 8    'commentable',




 9    [Post::class, Video::class],




10    function (Builder $query) {




11        $query->where('title', 'like', 'code%');




12    }




13)->get();




14 



15// Retrieve comments associated to posts with a title not like code%...




16$comments = Comment::whereDoesntHaveMorph(




17    'commentable',




18    Post::class,




19    function (Builder $query) {




20        $query->where('title', 'like', 'code%');




21    }




22)->get();




use App\Models\Comment;
use App\Models\Post;
use App\Models\Video;
use Illuminate\Database\Eloquent\Builder;

// Retrieve comments associated to posts or videos with a title like code%...
$comments = Comment::whereHasMorph(
    'commentable',
    [Post::class, Video::class],
    function (Builder $query) {
        $query->where('title', 'like', 'code%');
    }
)->get();

// Retrieve comments associated to posts with a title not like code%...
$comments = Comment::whereDoesntHaveMorph(
    'commentable',
    Post::class,
    function (Builder $query) {
        $query->where('title', 'like', 'code%');
    }
)->get();

```

You may occasionally need to add query constraints based on the "type" of the related polymorphic model. The closure passed to the `whereHasMorph` method may receive a `$type` value as its second argument. This argument allows you to inspect the "type" of the query that is being built:
```


 1use Illuminate\Database\Eloquent\Builder;




 2 



 3$comments = Comment::whereHasMorph(




 4    'commentable',




 5    [Post::class, Video::class],




 6    function (Builder $query, string $type) {




 7        $column = $type === Post::class ? 'content' : 'title';




 8 



 9        $query->where($column, 'like', 'code%');




10    }




11)->get();




use Illuminate\Database\Eloquent\Builder;

$comments = Comment::whereHasMorph(
    'commentable',
    [Post::class, Video::class],
    function (Builder $query, string $type) {
        $column = $type === Post::class ? 'content' : 'title';

        $query->where($column, 'like', 'code%');
    }
)->get();

```

Sometimes you may want to query for the children of a "morph to" relationship's parent. You may accomplish this using the `whereMorphedTo` and `whereNotMorphedTo` methods, which will automatically determine the proper morph type mapping for the given model. These methods accept the name of the `morphTo` relationship as their first argument and the related parent model as their second argument:
```


1$comments = Comment::whereMorphedTo('commentable', $post)




2    ->orWhereMorphedTo('commentable', $video)




3    ->get();




$comments = Comment::whereMorphedTo('commentable', $post)
    ->orWhereMorphedTo('commentable', $video)
    ->get();

```

#### [Querying All Related Models](https://laravel.com/docs/12.x/eloquent-relationships#querying-all-morph-to-related-models)
Instead of passing an array of possible polymorphic models, you may provide `*` as a wildcard value. This will instruct Laravel to retrieve all of the possible polymorphic types from the database. Laravel will execute an additional query in order to perform this operation:
```


1use Illuminate\Database\Eloquent\Builder;




2 



3$comments = Comment::whereHasMorph('commentable', '*', function (Builder $query) {




4    $query->where('title', 'like', 'foo%');




5})->get();




use Illuminate\Database\Eloquent\Builder;

$comments = Comment::whereHasMorph('commentable', '*', function (Builder $query) {
    $query->where('title', 'like', 'foo%');
})->get();

```
