## [Inserting and Updating Related Models](https://laravel.com/docs/12.x/eloquent-relationships#inserting-and-updating-related-models)
### [The `save` Method](https://laravel.com/docs/12.x/eloquent-relationships#the-save-method)
Eloquent provides convenient methods for adding new models to relationships. For example, perhaps you need to add a new comment to a post. Instead of manually setting the `post_id` attribute on the `Comment` model you may insert the comment using the relationship's `save` method:
```


1use App\Models\Comment;




2use App\Models\Post;




3 



4$comment = new Comment(['message' => 'A new comment.']);




5 



6$post = Post::find(1);




7 



8$post->comments()->save($comment);




use App\Models\Comment;
use App\Models\Post;

$comment = new Comment(['message' => 'A new comment.']);

$post = Post::find(1);

$post->comments()->save($comment);

```

Note that we did not access the `comments` relationship as a dynamic property. Instead, we called the `comments` method to obtain an instance of the relationship. The `save` method will automatically add the appropriate `post_id` value to the new `Comment` model.
If you need to save multiple related models, you may use the `saveMany` method:
```


1$post = Post::find(1);




2 



3$post->comments()->saveMany([




4    new Comment(['message' => 'A new comment.']),




5    new Comment(['message' => 'Another new comment.']),




6]);




$post = Post::find(1);

$post->comments()->saveMany([
    new Comment(['message' => 'A new comment.']),
    new Comment(['message' => 'Another new comment.']),
]);

```

The `save` and `saveMany` methods will persist the given model instances, but will not add the newly persisted models to any in-memory relationships that are already loaded onto the parent model. If you plan on accessing the relationship after using the `save` or `saveMany` methods, you may wish to use the `refresh` method to reload the model and its relationships:
```


1$post->comments()->save($comment);




2 



3$post->refresh();




4 



5// All comments, including the newly saved comment...




6$post->comments;




$post->comments()->save($comment);

$post->refresh();

// All comments, including the newly saved comment...
$post->comments;

```

#### [Recursively Saving Models and Relationships](https://laravel.com/docs/12.x/eloquent-relationships#the-push-method)
If you would like to `save` your model and all of its associated relationships, you may use the `push` method. In this example, the `Post` model will be saved as well as its comments and the comment's authors:
```


1$post = Post::find(1);




2 



3$post->comments[0]->message = 'Message';




4$post->comments[0]->author->name = 'Author Name';




5 



6$post->push();




$post = Post::find(1);

$post->comments[0]->message = 'Message';
$post->comments[0]->author->name = 'Author Name';

$post->push();

```

The `pushQuietly` method may be used to save a model and its associated relationships without raising any events:
```


1$post->pushQuietly();




$post->pushQuietly();

```

### [The `create` Method](https://laravel.com/docs/12.x/eloquent-relationships#the-create-method)
In addition to the `save` and `saveMany` methods, you may also use the `create` method, which accepts an array of attributes, creates a model, and inserts it into the database. The difference between `save` and `create` is that `save` accepts a full Eloquent model instance while `create` accepts a plain PHP `array`. The newly created model will be returned by the `create` method:
```


1use App\Models\Post;




2 



3$post = Post::find(1);




4 



5$comment = $post->comments()->create([




6    'message' => 'A new comment.',




7]);




use App\Models\Post;

$post = Post::find(1);

$comment = $post->comments()->create([
    'message' => 'A new comment.',
]);

```

You may use the `createMany` method to create multiple related models:
```


1$post = Post::find(1);




2 



3$post->comments()->createMany([




4    ['message' => 'A new comment.'],




5    ['message' => 'Another new comment.'],




6]);




$post = Post::find(1);

$post->comments()->createMany([
    ['message' => 'A new comment.'],
    ['message' => 'Another new comment.'],
]);

```

The `createQuietly` and `createManyQuietly` methods may be used to create a model(s) without dispatching any events:
```


 1$user = User::find(1);




 2 



 3$user->posts()->createQuietly([




 4    'title' => 'Post title.',




 5]);




 6 



 7$user->posts()->createManyQuietly([




 8    ['title' => 'First post.'],




 9    ['title' => 'Second post.'],




10]);




$user = User::find(1);

$user->posts()->createQuietly([
    'title' => 'Post title.',
]);

$user->posts()->createManyQuietly([
    ['title' => 'First post.'],
    ['title' => 'Second post.'],
]);

```

You may also use the `findOrNew`, `firstOrNew`, `firstOrCreate`, and `updateOrCreate` methods to [create and update models on relationships](https://laravel.com/docs/12.x/eloquent#upserts).
Before using the `create` method, be sure to review the [mass assignment](https://laravel.com/docs/12.x/eloquent#mass-assignment) documentation.
### [Belongs To Relationships](https://laravel.com/docs/12.x/eloquent-relationships#updating-belongs-to-relationships)
If you would like to assign a child model to a new parent model, you may use the `associate` method. In this example, the `User` model defines a `belongsTo` relationship to the `Account` model. This `associate` method will set the foreign key on the child model:
```


1use App\Models\Account;




2 



3$account = Account::find(10);




4 



5$user->account()->associate($account);




6 



7$user->save();




use App\Models\Account;

$account = Account::find(10);

$user->account()->associate($account);

$user->save();

```

To remove a parent model from a child model, you may use the `dissociate` method. This method will set the relationship's foreign key to `null`:
```


1$user->account()->dissociate();




2 



3$user->save();




$user->account()->dissociate();

$user->save();

```

### [Many to Many Relationships](https://laravel.com/docs/12.x/eloquent-relationships#updating-many-to-many-relationships)
#### [Attaching / Detaching](https://laravel.com/docs/12.x/eloquent-relationships#attaching-detaching)
Eloquent also provides methods to make working with many-to-many relationships more convenient. For example, let's imagine a user can have many roles and a role can have many users. You may use the `attach` method to attach a role to a user by inserting a record in the relationship's intermediate table:
```


1use App\Models\User;




2 



3$user = User::find(1);




4 



5$user->roles()->attach($roleId);




use App\Models\User;

$user = User::find(1);

$user->roles()->attach($roleId);

```

When attaching a relationship to a model, you may also pass an array of additional data to be inserted into the intermediate table:
```


1$user->roles()->attach($roleId, ['expires' => $expires]);




$user->roles()->attach($roleId, ['expires' => $expires]);

```

Sometimes it may be necessary to remove a role from a user. To remove a many-to-many relationship record, use the `detach` method. The `detach` method will delete the appropriate record out of the intermediate table; however, both models will remain in the database:
```


1// Detach a single role from the user...




2$user->roles()->detach($roleId);




3 



4// Detach all roles from the user...




5$user->roles()->detach();




// Detach a single role from the user...
$user->roles()->detach($roleId);

// Detach all roles from the user...
$user->roles()->detach();

```

For convenience, `attach` and `detach` also accept arrays of IDs as input:
```


1$user = User::find(1);




2 



3$user->roles()->detach([1, 2, 3]);




4 



5$user->roles()->attach([




6    1 => ['expires' => $expires],




7    2 => ['expires' => $expires],




8]);




$user = User::find(1);

$user->roles()->detach([1, 2, 3]);

$user->roles()->attach([
    1 => ['expires' => $expires],
    2 => ['expires' => $expires],
]);

```

#### [Syncing Associations](https://laravel.com/docs/12.x/eloquent-relationships#syncing-associations)
You may also use the `sync` method to construct many-to-many associations. The `sync` method accepts an array of IDs to place on the intermediate table. Any IDs that are not in the given array will be removed from the intermediate table. So, after this operation is complete, only the IDs in the given array will exist in the intermediate table:
```


1$user->roles()->sync([1, 2, 3]);




$user->roles()->sync([1, 2, 3]);

```

You may also pass additional intermediate table values with the IDs:
```


1$user->roles()->sync([1 => ['expires' => true], 2, 3]);




$user->roles()->sync([1 => ['expires' => true], 2, 3]);

```

If you would like to insert the same intermediate table values with each of the synced model IDs, you may use the `syncWithPivotValues` method:
```


1$user->roles()->syncWithPivotValues([1, 2, 3], ['active' => true]);




$user->roles()->syncWithPivotValues([1, 2, 3], ['active' => true]);

```

If you do not want to detach existing IDs that are missing from the given array, you may use the `syncWithoutDetaching` method:
```


1$user->roles()->syncWithoutDetaching([1, 2, 3]);




$user->roles()->syncWithoutDetaching([1, 2, 3]);

```

#### [Toggling Associations](https://laravel.com/docs/12.x/eloquent-relationships#toggling-associations)
The many-to-many relationship also provides a `toggle` method which "toggles" the attachment status of the given related model IDs. If the given ID is currently attached, it will be detached. Likewise, if it is currently detached, it will be attached:
```


1$user->roles()->toggle([1, 2, 3]);




$user->roles()->toggle([1, 2, 3]);

```

You may also pass additional intermediate table values with the IDs:
```


1$user->roles()->toggle([




2    1 => ['expires' => true],




3    2 => ['expires' => true],




4]);




$user->roles()->toggle([
    1 => ['expires' => true],
    2 => ['expires' => true],
]);

```

#### [Updating a Record on the Intermediate Table](https://laravel.com/docs/12.x/eloquent-relationships#updating-a-record-on-the-intermediate-table)
If you need to update an existing row in your relationship's intermediate table, you may use the `updateExistingPivot` method. This method accepts the intermediate record foreign key and an array of attributes to update:
```


1$user = User::find(1);




2 



3$user->roles()->updateExistingPivot($roleId, [




4    'active' => false,




5]);




$user = User::find(1);

$user->roles()->updateExistingPivot($roleId, [
    'active' => false,
]);

```
