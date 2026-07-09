## [Polymorphic Relationships](https://laravel.com/docs/12.x/eloquent-relationships#polymorphic-relationships)
A polymorphic relationship allows the child model to belong to more than one type of model using a single association. For example, imagine you are building an application that allows users to share blog posts and videos. In such an application, a `Comment` model might belong to both the `Post` and `Video` models.
### [One to One (Polymorphic)](https://laravel.com/docs/12.x/eloquent-relationships#one-to-one-polymorphic-relations)
#### [Table Structure](https://laravel.com/docs/12.x/eloquent-relationships#one-to-one-polymorphic-table-structure)
A one-to-one polymorphic relation is similar to a typical one-to-one relation; however, the child model can belong to more than one type of model using a single association. For example, a blog `Post` and a `User` may share a polymorphic relation to an `Image` model. Using a one-to-one polymorphic relation allows you to have a single table of unique images that may be associated with posts and users. First, let's examine the table structure:
```


 1posts




 2    id - integer




 3    name - string



 4



 5users




 6    id - integer




 7    name - string



 8



 9images




10    id - integer




11    url - string




12    imageable_id - integer




13    imageable_type - string




posts
    id - integer
    name - string

users
    id - integer
    name - string

images
    id - integer
    url - string
    imageable_id - integer
    imageable_type - string

```

Note the `imageable_id` and `imageable_type` columns on the `images` table. The `imageable_id` column will contain the ID value of the post or user, while the `imageable_type` column will contain the class name of the parent model. The `imageable_type` column is used by Eloquent to determine which "type" of parent model to return when accessing the `imageable` relation. In this case, the column would contain either `App\Models\Post` or `App\Models\User`.
#### [Model Structure](https://laravel.com/docs/12.x/eloquent-relationships#one-to-one-polymorphic-model-structure)
Next, let's examine the model definitions needed to build this relationship:
```


 1<?php




 2 



 3namespace App\Models;




 4 



 5use Illuminate\Database\Eloquent\Model;




 6use Illuminate\Database\Eloquent\Relations\MorphTo;




 7 



 8class Image extends Model




 9{




10    /**




11     * Get the parent imageable model (user or post).




12     */




13    public function imageable(): MorphTo




14    {




15        return $this->morphTo();




16    }




17}




18 



19use Illuminate\Database\Eloquent\Model;




20use Illuminate\Database\Eloquent\Relations\MorphOne;




21 



22class Post extends Model




23{




24    /**




25     * Get the post's image.




26     */




27    public function image(): MorphOne




28    {




29        return $this->morphOne(Image::class, 'imageable');




30    }




31}




32 



33use Illuminate\Database\Eloquent\Model;




34use Illuminate\Database\Eloquent\Relations\MorphOne;




35 



36class User extends Model




37{




38    /**




39     * Get the user's image.




40     */




41    public function image(): MorphOne




42    {




43        return $this->morphOne(Image::class, 'imageable');




44    }




45}




<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\MorphTo;

class Image extends Model
{
    /**
     * Get the parent imageable model (user or post).
     */
    public function imageable(): MorphTo
    {
        return $this->morphTo();
    }
}

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\MorphOne;

class Post extends Model
{
    /**
     * Get the post's image.
     */
    public function image(): MorphOne
    {
        return $this->morphOne(Image::class, 'imageable');
    }
}

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\MorphOne;

class User extends Model
{
    /**
     * Get the user's image.
     */
    public function image(): MorphOne
    {
        return $this->morphOne(Image::class, 'imageable');
    }
}

```

#### [Retrieving the Relationship](https://laravel.com/docs/12.x/eloquent-relationships#one-to-one-polymorphic-retrieving-the-relationship)
Once your database table and models are defined, you may access the relationships via your models. For example, to retrieve the image for a post, we can access the `image` dynamic relationship property:
```


1use App\Models\Post;




2 



3$post = Post::find(1);




4 



5$image = $post->image;




use App\Models\Post;

$post = Post::find(1);

$image = $post->image;

```

You may retrieve the parent of the polymorphic model by accessing the name of the method that performs the call to `morphTo`. In this case, that is the `imageable` method on the `Image` model. So, we will access that method as a dynamic relationship property:
```


1use App\Models\Image;




2 



3$image = Image::find(1);




4 



5$imageable = $image->imageable;




use App\Models\Image;

$image = Image::find(1);

$imageable = $image->imageable;

```

The `imageable` relation on the `Image` model will return either a `Post` or `User` instance, depending on which type of model owns the image.
#### [Key Conventions](https://laravel.com/docs/12.x/eloquent-relationships#morph-one-to-one-key-conventions)
If necessary, you may specify the name of the "id" and "type" columns utilized by your polymorphic child model. If you do so, ensure that you always pass the name of the relationship as the first argument to the `morphTo` method. Typically, this value should match the method name, so you may use PHP's `__FUNCTION__` constant:
```


1/**




2 * Get the model that the image belongs to.




3 */




4public function imageable(): MorphTo




5{




6    return $this->morphTo(__FUNCTION__, 'imageable_type', 'imageable_id');




7}




/**
 * Get the model that the image belongs to.
 */
public function imageable(): MorphTo
{
    return $this->morphTo(__FUNCTION__, 'imageable_type', 'imageable_id');
}

```

### [One to Many (Polymorphic)](https://laravel.com/docs/12.x/eloquent-relationships#one-to-many-polymorphic-relations)
#### [Table Structure](https://laravel.com/docs/12.x/eloquent-relationships#one-to-many-polymorphic-table-structure)
A one-to-many polymorphic relation is similar to a typical one-to-many relation; however, the child model can belong to more than one type of model using a single association. For example, imagine users of your application can "comment" on posts and videos. Using polymorphic relationships, you may use a single `comments` table to contain comments for both posts and videos. First, let's examine the table structure required to build this relationship:
```


 1posts




 2    id - integer




 3    title - string




 4    body - text



 5



 6videos




 7    id - integer




 8    title - string




 9    url - string



10



11comments




12    id - integer




13    body - text




14    commentable_id - integer




15    commentable_type - string




posts
    id - integer
    title - string
    body - text

videos
    id - integer
    title - string
    url - string

comments
    id - integer
    body - text
    commentable_id - integer
    commentable_type - string

```

#### [Model Structure](https://laravel.com/docs/12.x/eloquent-relationships#one-to-many-polymorphic-model-structure)
Next, let's examine the model definitions needed to build this relationship:
```


 1<?php




 2 



 3namespace App\Models;




 4 



 5use Illuminate\Database\Eloquent\Model;




 6use Illuminate\Database\Eloquent\Relations\MorphTo;




 7 



 8class Comment extends Model




 9{




10    /**




11     * Get the parent commentable model (post or video).




12     */




13    public function commentable(): MorphTo




14    {




15        return $this->morphTo();




16    }




17}




18 



19use Illuminate\Database\Eloquent\Model;




20use Illuminate\Database\Eloquent\Relations\MorphMany;




21 



22class Post extends Model




23{




24    /**




25     * Get all of the post's comments.




26     */




27    public function comments(): MorphMany




28    {




29        return $this->morphMany(Comment::class, 'commentable');




30    }




31}




32 



33use Illuminate\Database\Eloquent\Model;




34use Illuminate\Database\Eloquent\Relations\MorphMany;




35 



36class Video extends Model




37{




38    /**




39     * Get all of the video's comments.




40     */




41    public function comments(): MorphMany




42    {




43        return $this->morphMany(Comment::class, 'commentable');




44    }




45}




<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\MorphTo;

class Comment extends Model
{
    /**
     * Get the parent commentable model (post or video).
     */
    public function commentable(): MorphTo
    {
        return $this->morphTo();
    }
}

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\MorphMany;

class Post extends Model
{
    /**
     * Get all of the post's comments.
     */
    public function comments(): MorphMany
    {
        return $this->morphMany(Comment::class, 'commentable');
    }
}

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\MorphMany;

class Video extends Model
{
    /**
     * Get all of the video's comments.
     */
    public function comments(): MorphMany
    {
        return $this->morphMany(Comment::class, 'commentable');
    }
}

```

#### [Retrieving the Relationship](https://laravel.com/docs/12.x/eloquent-relationships#one-to-many-polymorphic-retrieving-the-relationship)
Once your database table and models are defined, you may access the relationships via your model's dynamic relationship properties. For example, to access all of the comments for a post, we can use the `comments` dynamic property:
```


1use App\Models\Post;




2 



3$post = Post::find(1);




4 



5foreach ($post->comments as $comment) {




6    // ...




7}




use App\Models\Post;

$post = Post::find(1);

foreach ($post->comments as $comment) {
    // ...
}

```

You may also retrieve the parent of a polymorphic child model by accessing the name of the method that performs the call to `morphTo`. In this case, that is the `commentable` method on the `Comment` model. So, we will access that method as a dynamic relationship property in order to access the comment's parent model:
```


1use App\Models\Comment;




2 



3$comment = Comment::find(1);




4 



5$commentable = $comment->commentable;




use App\Models\Comment;

$comment = Comment::find(1);

$commentable = $comment->commentable;

```

The `commentable` relation on the `Comment` model will return either a `Post` or `Video` instance, depending on which type of model is the comment's parent.
#### [Automatically Hydrating Parent Models on Children](https://laravel.com/docs/12.x/eloquent-relationships#polymorphic-automatically-hydrating-parent-models-on-children)
Even when utilizing Eloquent eager loading, "N + 1" query problems can arise if you try to access the parent model from a child model while looping through the child models:
```


1$posts = Post::with('comments')->get();




2 



3foreach ($posts as $post) {




4    foreach ($post->comments as $comment) {




5        echo $comment->commentable->title;




6    }




7}




$posts = Post::with('comments')->get();

foreach ($posts as $post) {
    foreach ($post->comments as $comment) {
        echo $comment->commentable->title;
    }
}

```

In the example above, an "N + 1" query problem has been introduced because, even though comments were eager loaded for every `Post` model, Eloquent does not automatically hydrate the parent `Post` on each child `Comment` model.
If you would like Eloquent to automatically hydrate parent models onto their children, you may invoke the `chaperone` method when defining a `morphMany` relationship:
```


 1class Post extends Model




 2{




 3    /**




 4     * Get all of the post's comments.




 5     */




 6    public function comments(): MorphMany




 7    {




 8        return $this->morphMany(Comment::class, 'commentable')->chaperone();




 9    }




10}




class Post extends Model
{
    /**
     * Get all of the post's comments.
     */
    public function comments(): MorphMany
    {
        return $this->morphMany(Comment::class, 'commentable')->chaperone();
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

### [One of Many (Polymorphic)](https://laravel.com/docs/12.x/eloquent-relationships#one-of-many-polymorphic-relations)
Sometimes a model may have many related models, yet you want to easily retrieve the "latest" or "oldest" related model of the relationship. For example, a `User` model may be related to many `Image` models, but you want to define a convenient way to interact with the most recent image the user has uploaded. You may accomplish this using the `morphOne` relationship type combined with the `ofMany` methods:
```


1/**




2 * Get the user's most recent image.




3 */




4public function latestImage(): MorphOne




5{




6    return $this->morphOne(Image::class, 'imageable')->latestOfMany();




7}




/**
 * Get the user's most recent image.
 */
public function latestImage(): MorphOne
{
    return $this->morphOne(Image::class, 'imageable')->latestOfMany();
}

```

Likewise, you may define a method to retrieve the "oldest", or first, related model of a relationship:
```


1/**




2 * Get the user's oldest image.




3 */




4public function oldestImage(): MorphOne




5{




6    return $this->morphOne(Image::class, 'imageable')->oldestOfMany();




7}




/**
 * Get the user's oldest image.
 */
public function oldestImage(): MorphOne
{
    return $this->morphOne(Image::class, 'imageable')->oldestOfMany();
}

```

By default, the `latestOfMany` and `oldestOfMany` methods will retrieve the latest or oldest related model based on the model's primary key, which must be sortable. However, sometimes you may wish to retrieve a single model from a larger relationship using a different sorting criteria.
For example, using the `ofMany` method, you may retrieve the user's most "liked" image. The `ofMany` method accepts the sortable column as its first argument and which aggregate function (`min` or `max`) to apply when querying for the related model:
```


1/**




2 * Get the user's most popular image.




3 */




4public function bestImage(): MorphOne




5{




6    return $this->morphOne(Image::class, 'imageable')->ofMany('likes', 'max');




7}




/**
 * Get the user's most popular image.
 */
public function bestImage(): MorphOne
{
    return $this->morphOne(Image::class, 'imageable')->ofMany('likes', 'max');
}

```

It is possible to construct more advanced "one of many" relationships. For more information, please consult the [has one of many documentation](https://laravel.com/docs/12.x/eloquent-relationships#advanced-has-one-of-many-relationships).
### [Many to Many (Polymorphic)](https://laravel.com/docs/12.x/eloquent-relationships#many-to-many-polymorphic-relations)
#### [Table Structure](https://laravel.com/docs/12.x/eloquent-relationships#many-to-many-polymorphic-table-structure)
Many-to-many polymorphic relations are slightly more complicated than "morph one" and "morph many" relationships. For example, a `Post` model and `Video` model could share a polymorphic relation to a `Tag` model. Using a many-to-many polymorphic relation in this situation would allow your application to have a single table of unique tags that may be associated with posts or videos. First, let's examine the table structure required to build this relationship:
```


 1posts




 2    id - integer




 3    name - string



 4



 5videos




 6    id - integer




 7    name - string



 8



 9tags




10    id - integer




11    name - string



12



13taggables




14    tag_id - integer




15    taggable_id - integer




16    taggable_type - string




posts
    id - integer
    name - string

videos
    id - integer
    name - string

tags
    id - integer
    name - string

taggables
    tag_id - integer
    taggable_id - integer
    taggable_type - string

```

Before diving into polymorphic many-to-many relationships, you may benefit from reading the documentation on typical [many-to-many relationships](https://laravel.com/docs/12.x/eloquent-relationships#many-to-many).
#### [Model Structure](https://laravel.com/docs/12.x/eloquent-relationships#many-to-many-polymorphic-model-structure)
Next, we're ready to define the relationships on the models. The `Post` and `Video` models will both contain a `tags` method that calls the `morphToMany` method provided by the base Eloquent model class.
The `morphToMany` method accepts the name of the related model as well as the "relationship name". Based on the name we assigned to our intermediate table name and the keys it contains, we will refer to the relationship as "taggable":
```


 1<?php




 2 



 3namespace App\Models;




 4 



 5use Illuminate\Database\Eloquent\Model;




 6use Illuminate\Database\Eloquent\Relations\MorphToMany;




 7 



 8class Post extends Model




 9{




10    /**




11     * Get all of the tags for the post.




12     */




13    public function tags(): MorphToMany




14    {




15        return $this->morphToMany(Tag::class, 'taggable');




16    }




17}




<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\MorphToMany;

class Post extends Model
{
    /**
     * Get all of the tags for the post.
     */
    public function tags(): MorphToMany
    {
        return $this->morphToMany(Tag::class, 'taggable');
    }
}

```

#### [Defining the Inverse of the Relationship](https://laravel.com/docs/12.x/eloquent-relationships#many-to-many-polymorphic-defining-the-inverse-of-the-relationship)
Next, on the `Tag` model, you should define a method for each of its possible parent models. So, in this example, we will define a `posts` method and a `videos` method. Both of these methods should return the result of the `morphedByMany` method.
The `morphedByMany` method accepts the name of the related model as well as the "relationship name". Based on the name we assigned to our intermediate table name and the keys it contains, we will refer to the relationship as "taggable":
```


 1<?php




 2 



 3namespace App\Models;




 4 



 5use Illuminate\Database\Eloquent\Model;




 6use Illuminate\Database\Eloquent\Relations\MorphToMany;




 7 



 8class Tag extends Model




 9{




10    /**




11     * Get all of the posts that are assigned this tag.




12     */




13    public function posts(): MorphToMany




14    {




15        return $this->morphedByMany(Post::class, 'taggable');




16    }




17 



18    /**




19     * Get all of the videos that are assigned this tag.




20     */




21    public function videos(): MorphToMany




22    {




23        return $this->morphedByMany(Video::class, 'taggable');




24    }




25}




<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\MorphToMany;

class Tag extends Model
{
    /**
     * Get all of the posts that are assigned this tag.
     */
    public function posts(): MorphToMany
    {
        return $this->morphedByMany(Post::class, 'taggable');
    }

    /**
     * Get all of the videos that are assigned this tag.
     */
    public function videos(): MorphToMany
    {
        return $this->morphedByMany(Video::class, 'taggable');
    }
}

```

#### [Retrieving the Relationship](https://laravel.com/docs/12.x/eloquent-relationships#many-to-many-polymorphic-retrieving-the-relationship)
Once your database table and models are defined, you may access the relationships via your models. For example, to access all of the tags for a post, you may use the `tags` dynamic relationship property:
```


1use App\Models\Post;




2 



3$post = Post::find(1);




4 



5foreach ($post->tags as $tag) {




6    // ...




7}




use App\Models\Post;

$post = Post::find(1);

foreach ($post->tags as $tag) {
    // ...
}

```

You may retrieve the parent of a polymorphic relation from the polymorphic child model by accessing the name of the method that performs the call to `morphedByMany`. In this case, that is the `posts` or `videos` methods on the `Tag` model:
```


 1use App\Models\Tag;




 2 



 3$tag = Tag::find(1);




 4 



 5foreach ($tag->posts as $post) {




 6    // ...




 7}




 8 



 9foreach ($tag->videos as $video) {




10    // ...




11}




use App\Models\Tag;

$tag = Tag::find(1);

foreach ($tag->posts as $post) {
    // ...
}

foreach ($tag->videos as $video) {
    // ...
}

```

### [Custom Polymorphic Types](https://laravel.com/docs/12.x/eloquent-relationships#custom-polymorphic-types)
By default, Laravel will use the fully qualified class name to store the "type" of the related model. For instance, given the one-to-many relationship example above where a `Comment` model may belong to a `Post` or a `Video` model, the default `commentable_type` would be either `App\Models\Post` or `App\Models\Video`, respectively. However, you may wish to decouple these values from your application's internal structure.
For example, instead of using the model names as the "type", we may use simple strings such as `post` and `video`. By doing so, the polymorphic "type" column values in our database will remain valid even if the models are renamed:
```


1use Illuminate\Database\Eloquent\Relations\Relation;




2 



3Relation::enforceMorphMap([




4    'post' => 'App\Models\Post',




5    'video' => 'App\Models\Video',




6]);




use Illuminate\Database\Eloquent\Relations\Relation;

Relation::enforceMorphMap([
    'post' => 'App\Models\Post',
    'video' => 'App\Models\Video',
]);

```

You may call the `enforceMorphMap` method in the `boot` method of your `App\Providers\AppServiceProvider` class or create a separate service provider if you wish.
You may determine the morph alias of a given model at runtime using the model's `getMorphClass` method. Conversely, you may determine the fully-qualified class name associated with a morph alias using the `Relation::getMorphedModel` method:
```


1use Illuminate\Database\Eloquent\Relations\Relation;




2 



3$alias = $post->getMorphClass();




4 



5$class = Relation::getMorphedModel($alias);




use Illuminate\Database\Eloquent\Relations\Relation;

$alias = $post->getMorphClass();

$class = Relation::getMorphedModel($alias);

```

When adding a "morph map" to your existing application, every morphable `*_type` column value in your database that still contains a fully-qualified class will need to be converted to its "map" name.
### [Dynamic Relationships](https://laravel.com/docs/12.x/eloquent-relationships#dynamic-relationships)
You may use the `resolveRelationUsing` method to define relations between Eloquent models at runtime. While not typically recommended for normal application development, this may occasionally be useful when developing Laravel packages.
The `resolveRelationUsing` method accepts the desired relationship name as its first argument. The second argument passed to the method should be a closure that accepts the model instance and returns a valid Eloquent relationship definition. Typically, you should configure dynamic relationships within the boot method of a [service provider](https://laravel.com/docs/12.x/providers):
```


1use App\Models\Order;




2use App\Models\Customer;




3 



4Order::resolveRelationUsing('customer', function (Order $orderModel) {




5    return $orderModel->belongsTo(Customer::class, 'customer_id');




6});




use App\Models\Order;
use App\Models\Customer;

Order::resolveRelationUsing('customer', function (Order $orderModel) {
    return $orderModel->belongsTo(Customer::class, 'customer_id');
});

```

When defining dynamic relationships, always provide explicit key name arguments to the Eloquent relationship methods.
