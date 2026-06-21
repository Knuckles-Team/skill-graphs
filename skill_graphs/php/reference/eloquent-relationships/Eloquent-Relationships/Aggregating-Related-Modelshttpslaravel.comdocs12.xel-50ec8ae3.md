## [Aggregating Related Models](https://laravel.com/docs/12.x/eloquent-relationships#aggregating-related-models)
### [Counting Related Models](https://laravel.com/docs/12.x/eloquent-relationships#counting-related-models)
Sometimes you may want to count the number of related models for a given relationship without actually loading the models. To accomplish this, you may use the `withCount` method. The `withCount` method will place a `{relation}_count` attribute on the resulting models:
```


1use App\Models\Post;




2 



3$posts = Post::withCount('comments')->get();




4 



5foreach ($posts as $post) {




6    echo $post->comments_count;




7}




use App\Models\Post;

$posts = Post::withCount('comments')->get();

foreach ($posts as $post) {
    echo $post->comments_count;
}

```

By passing an array to the `withCount` method, you may add the "counts" for multiple relations as well as add additional constraints to the queries:
```


1use Illuminate\Database\Eloquent\Builder;




2 



3$posts = Post::withCount(['votes', 'comments' => function (Builder $query) {




4    $query->where('content', 'like', 'code%');




5}])->get();




6 



7echo $posts[0]->votes_count;




8echo $posts[0]->comments_count;




use Illuminate\Database\Eloquent\Builder;

$posts = Post::withCount(['votes', 'comments' => function (Builder $query) {
    $query->where('content', 'like', 'code%');
}])->get();

echo $posts[0]->votes_count;
echo $posts[0]->comments_count;

```

You may also alias the relationship count result, allowing multiple counts on the same relationship:
```


 1use Illuminate\Database\Eloquent\Builder;




 2 



 3$posts = Post::withCount([




 4    'comments',




 5    'comments as pending_comments_count' => function (Builder $query) {




 6        $query->where('approved', false);




 7    },




 8])->get();




 9 



10echo $posts[0]->comments_count;




11echo $posts[0]->pending_comments_count;




use Illuminate\Database\Eloquent\Builder;

$posts = Post::withCount([
    'comments',
    'comments as pending_comments_count' => function (Builder $query) {
        $query->where('approved', false);
    },
])->get();

echo $posts[0]->comments_count;
echo $posts[0]->pending_comments_count;

```

#### [Deferred Count Loading](https://laravel.com/docs/12.x/eloquent-relationships#deferred-count-loading)
Using the `loadCount` method, you may load a relationship count after the parent model has already been retrieved:
```


1$book = Book::first();




2 



3$book->loadCount('genres');




$book = Book::first();

$book->loadCount('genres');

```

If you need to set additional query constraints on the count query, you may pass an array keyed by the relationships you wish to count. The array values should be closures which receive the query builder instance:
```


1$book->loadCount(['reviews' => function (Builder $query) {




2    $query->where('rating', 5);




3}])




$book->loadCount(['reviews' => function (Builder $query) {
    $query->where('rating', 5);
}])

```

#### [Relationship Counting and Custom Select Statements](https://laravel.com/docs/12.x/eloquent-relationships#relationship-counting-and-custom-select-statements)
If you're combining `withCount` with a `select` statement, ensure that you call `withCount` after the `select` method:
```


1$posts = Post::select(['title', 'body'])




2    ->withCount('comments')




3    ->get();




$posts = Post::select(['title', 'body'])
    ->withCount('comments')
    ->get();

```

### [Other Aggregate Functions](https://laravel.com/docs/12.x/eloquent-relationships#other-aggregate-functions)
In addition to the `withCount` method, Eloquent provides `withMin`, `withMax`, `withAvg`, `withSum`, and `withExists` methods. These methods will place a `{relation}_{function}_{column}` attribute on your resulting models:
```


1use App\Models\Post;




2 



3$posts = Post::withSum('comments', 'votes')->get();




4 



5foreach ($posts as $post) {




6    echo $post->comments_sum_votes;




7}




use App\Models\Post;

$posts = Post::withSum('comments', 'votes')->get();

foreach ($posts as $post) {
    echo $post->comments_sum_votes;
}

```

If you wish to access the result of the aggregate function using another name, you may specify your own alias:
```


1$posts = Post::withSum('comments as total_comments', 'votes')->get();




2 



3foreach ($posts as $post) {




4    echo $post->total_comments;




5}




$posts = Post::withSum('comments as total_comments', 'votes')->get();

foreach ($posts as $post) {
    echo $post->total_comments;
}

```

Like the `loadCount` method, deferred versions of these methods are also available. These additional aggregate operations may be performed on Eloquent models that have already been retrieved:
```


1$post = Post::first();




2 



3$post->loadSum('comments', 'votes');




$post = Post::first();

$post->loadSum('comments', 'votes');

```

If you're combining these aggregate methods with a `select` statement, ensure that you call the aggregate methods after the `select` method:
```


1$posts = Post::select(['title', 'body'])




2    ->withExists('comments')




3    ->get();




$posts = Post::select(['title', 'body'])
    ->withExists('comments')
    ->get();

```

### [Counting Related Models on Morph To Relationships](https://laravel.com/docs/12.x/eloquent-relationships#counting-related-models-on-morph-to-relationships)
If you would like to eager load a "morph to" relationship, as well as related model counts for the various entities that may be returned by that relationship, you may utilize the `with` method in combination with the `morphTo` relationship's `morphWithCount` method.
In this example, let's assume that `Photo` and `Post` models may create `ActivityFeed` models. We will assume the `ActivityFeed` model defines a "morph to" relationship named `parentable` that allows us to retrieve the parent `Photo` or `Post` model for a given `ActivityFeed` instance. Additionally, let's assume that `Photo` models "have many" `Tag` models and `Post` models "have many" `Comment` models.
Now, let's imagine we want to retrieve `ActivityFeed` instances and eager load the `parentable` parent models for each `ActivityFeed` instance. In addition, we want to retrieve the number of tags that are associated with each parent photo and the number of comments that are associated with each parent post:
```


1use Illuminate\Database\Eloquent\Relations\MorphTo;




2 



3$activities = ActivityFeed::with([




4    'parentable' => function (MorphTo $morphTo) {




5        $morphTo->morphWithCount([




6            Photo::class => ['tags'],




7            Post::class => ['comments'],




8        ]);




9    }])->get();




use Illuminate\Database\Eloquent\Relations\MorphTo;

$activities = ActivityFeed::with([
    'parentable' => function (MorphTo $morphTo) {
        $morphTo->morphWithCount([
            Photo::class => ['tags'],
            Post::class => ['comments'],
        ]);
    }])->get();

```

#### [Deferred Count Loading](https://laravel.com/docs/12.x/eloquent-relationships#morph-to-deferred-count-loading)
Let's assume we have already retrieved a set of `ActivityFeed` models and now we would like to load the nested relationship counts for the various `parentable` models associated with the activity feeds. You may use the `loadMorphCount` method to accomplish this:
```


1$activities = ActivityFeed::with('parentable')->get();




2 



3$activities->loadMorphCount('parentable', [




4    Photo::class => ['tags'],




5    Post::class => ['comments'],




6]);




$activities = ActivityFeed::with('parentable')->get();

$activities->loadMorphCount('parentable', [
    Photo::class => ['tags'],
    Post::class => ['comments'],
]);

```
