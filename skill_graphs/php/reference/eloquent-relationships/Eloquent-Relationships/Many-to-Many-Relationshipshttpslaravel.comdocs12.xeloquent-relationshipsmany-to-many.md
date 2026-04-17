## [Many to Many Relationships](https://laravel.com/docs/12.x/eloquent-relationships#many-to-many)
Many-to-many relations are slightly more complicated than `hasOne` and `hasMany` relationships. An example of a many-to-many relationship is a user that has many roles and those roles are also shared by other users in the application. For example, a user may be assigned the role of "Author" and "Editor"; however, those roles may also be assigned to other users as well. So, a user has many roles and a role has many users.
#### [Table Structure](https://laravel.com/docs/12.x/eloquent-relationships#many-to-many-table-structure)
To define this relationship, three database tables are needed: `users`, `roles`, and `role_user`. The `role_user` table is derived from the alphabetical order of the related model names and contains `user_id` and `role_id` columns. This table is used as an intermediate table linking the users and roles.
Remember, since a role can belong to many users, we cannot simply place a `user_id` column on the `roles` table. This would mean that a role could only belong to a single user. In order to provide support for roles being assigned to multiple users, the `role_user` table is needed. We can summarize the relationship's table structure like so:
```


 1users




 2    id - integer




 3    name - string



 4



 5roles




 6    id - integer




 7    name - string



 8



 9role_user




10    user_id - integer




11    role_id - integer




users
    id - integer
    name - string

roles
    id - integer
    name - string

role_user
    user_id - integer
    role_id - integer

```

#### [Model Structure](https://laravel.com/docs/12.x/eloquent-relationships#many-to-many-model-structure)
Many-to-many relationships are defined by writing a method that returns the result of the `belongsToMany` method. The `belongsToMany` method is provided by the `Illuminate\Database\Eloquent\Model` base class that is used by all of your application's Eloquent models. For example, let's define a `roles` method on our `User` model. The first argument passed to this method is the name of the related model class:
```


 1<?php




 2 



 3namespace App\Models;




 4 



 5use Illuminate\Database\Eloquent\Model;




 6use Illuminate\Database\Eloquent\Relations\BelongsToMany;




 7 



 8class User extends Model




 9{




10    /**




11     * The roles that belong to the user.




12     */




13    public function roles(): BelongsToMany




14    {




15        return $this->belongsToMany(Role::class);




16    }




17}




<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsToMany;

class User extends Model
{
    /**
     * The roles that belong to the user.
     */
    public function roles(): BelongsToMany
    {
        return $this->belongsToMany(Role::class);
    }
}

```

Once the relationship is defined, you may access the user's roles using the `roles` dynamic relationship property:
```


1use App\Models\User;




2 



3$user = User::find(1);




4 



5foreach ($user->roles as $role) {




6    // ...




7}




use App\Models\User;

$user = User::find(1);

foreach ($user->roles as $role) {
    // ...
}

```

Since all relationships also serve as query builders, you may add further constraints to the relationship query by calling the `roles` method and continuing to chain conditions onto the query:
```


1$roles = User::find(1)->roles()->orderBy('name')->get();




$roles = User::find(1)->roles()->orderBy('name')->get();

```

To determine the table name of the relationship's intermediate table, Eloquent will join the two related model names in alphabetical order. However, you are free to override this convention. You may do so by passing a second argument to the `belongsToMany` method:
```


1return $this->belongsToMany(Role::class, 'role_user');




return $this->belongsToMany(Role::class, 'role_user');

```

In addition to customizing the name of the intermediate table, you may also customize the column names of the keys on the table by passing additional arguments to the `belongsToMany` method. The third argument is the foreign key name of the model on which you are defining the relationship, while the fourth argument is the foreign key name of the model that you are joining to:
```


1return $this->belongsToMany(Role::class, 'role_user', 'user_id', 'role_id');




return $this->belongsToMany(Role::class, 'role_user', 'user_id', 'role_id');

```

#### [Defining the Inverse of the Relationship](https://laravel.com/docs/12.x/eloquent-relationships#many-to-many-defining-the-inverse-of-the-relationship)
To define the "inverse" of a many-to-many relationship, you should define a method on the related model which also returns the result of the `belongsToMany` method. To complete our user / role example, let's define the `users` method on the `Role` model:
```


 1<?php




 2 



 3namespace App\Models;




 4 



 5use Illuminate\Database\Eloquent\Model;




 6use Illuminate\Database\Eloquent\Relations\BelongsToMany;




 7 



 8class Role extends Model




 9{




10    /**




11     * The users that belong to the role.




12     */




13    public function users(): BelongsToMany




14    {




15        return $this->belongsToMany(User::class);




16    }




17}




<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsToMany;

class Role extends Model
{
    /**
     * The users that belong to the role.
     */
    public function users(): BelongsToMany
    {
        return $this->belongsToMany(User::class);
    }
}

```

As you can see, the relationship is defined exactly the same as its `User` model counterpart with the exception of referencing the `App\Models\User` model. Since we're reusing the `belongsToMany` method, all of the usual table and key customization options are available when defining the "inverse" of many-to-many relationships.
### [Retrieving Intermediate Table Columns](https://laravel.com/docs/12.x/eloquent-relationships#retrieving-intermediate-table-columns)
As you have already learned, working with many-to-many relations requires the presence of an intermediate table. Eloquent provides some very helpful ways of interacting with this table. For example, let's assume our `User` model has many `Role` models that it is related to. After accessing this relationship, we may access the intermediate table using the `pivot` attribute on the models:
```


1use App\Models\User;




2 



3$user = User::find(1);




4 



5foreach ($user->roles as $role) {




6    echo $role->pivot->created_at;




7}




use App\Models\User;

$user = User::find(1);

foreach ($user->roles as $role) {
    echo $role->pivot->created_at;
}

```

Notice that each `Role` model we retrieve is automatically assigned a `pivot` attribute. This attribute contains a model representing the intermediate table.
By default, only the model keys will be present on the `pivot` model. If your intermediate table contains extra attributes, you must specify them when defining the relationship:
```


1return $this->belongsToMany(Role::class)->withPivot('active', 'created_by');




return $this->belongsToMany(Role::class)->withPivot('active', 'created_by');

```

If you would like your intermediate table to have `created_at` and `updated_at` timestamps that are automatically maintained by Eloquent, call the `withTimestamps` method when defining the relationship:
```


1return $this->belongsToMany(Role::class)->withTimestamps();




return $this->belongsToMany(Role::class)->withTimestamps();

```

Intermediate tables that utilize Eloquent's automatically maintained timestamps are required to have both `created_at` and `updated_at` timestamp columns.
#### [Customizing the `pivot` Attribute Name](https://laravel.com/docs/12.x/eloquent-relationships#customizing-the-pivot-attribute-name)
As noted previously, attributes from the intermediate table may be accessed on models via the `pivot` attribute. However, you are free to customize the name of this attribute to better reflect its purpose within your application.
For example, if your application contains users that may subscribe to podcasts, you likely have a many-to-many relationship between users and podcasts. If this is the case, you may wish to rename your intermediate table attribute to `subscription` instead of `pivot`. This can be done using the `as` method when defining the relationship:
```


1return $this->belongsToMany(Podcast::class)




2    ->as('subscription')




3    ->withTimestamps();




return $this->belongsToMany(Podcast::class)
    ->as('subscription')
    ->withTimestamps();

```

Once the custom intermediate table attribute has been specified, you may access the intermediate table data using the customized name:
```


1$users = User::with('podcasts')->get();




2 



3foreach ($users->flatMap->podcasts as $podcast) {




4    echo $podcast->subscription->created_at;




5}




$users = User::with('podcasts')->get();

foreach ($users->flatMap->podcasts as $podcast) {
    echo $podcast->subscription->created_at;
}

```

### [Filtering Queries via Intermediate Table Columns](https://laravel.com/docs/12.x/eloquent-relationships#filtering-queries-via-intermediate-table-columns)
You can also filter the results returned by `belongsToMany` relationship queries using the `wherePivot`, `wherePivotIn`, `wherePivotNotIn`, `wherePivotBetween`, `wherePivotNotBetween`, `wherePivotNull`, and `wherePivotNotNull` methods when defining the relationship:
```


 1return $this->belongsToMany(Role::class)




 2    ->wherePivot('approved', 1);




 3 



 4return $this->belongsToMany(Role::class)




 5    ->wherePivotIn('priority', [1, 2]);




 6 



 7return $this->belongsToMany(Role::class)




 8    ->wherePivotNotIn('priority', [1, 2]);




 9 



10return $this->belongsToMany(Podcast::class)




11    ->as('subscriptions')




12    ->wherePivotBetween('created_at', ['2020-01-01 00:00:00', '2020-12-31 00:00:00']);




13 



14return $this->belongsToMany(Podcast::class)




15    ->as('subscriptions')




16    ->wherePivotNotBetween('created_at', ['2020-01-01 00:00:00', '2020-12-31 00:00:00']);




17 



18return $this->belongsToMany(Podcast::class)




19    ->as('subscriptions')




20    ->wherePivotNull('expired_at');




21 



22return $this->belongsToMany(Podcast::class)




23    ->as('subscriptions')




24    ->wherePivotNotNull('expired_at');




return $this->belongsToMany(Role::class)
    ->wherePivot('approved', 1);

return $this->belongsToMany(Role::class)
    ->wherePivotIn('priority', [1, 2]);

return $this->belongsToMany(Role::class)
    ->wherePivotNotIn('priority', [1, 2]);

return $this->belongsToMany(Podcast::class)
    ->as('subscriptions')
    ->wherePivotBetween('created_at', ['2020-01-01 00:00:00', '2020-12-31 00:00:00']);

return $this->belongsToMany(Podcast::class)
    ->as('subscriptions')
    ->wherePivotNotBetween('created_at', ['2020-01-01 00:00:00', '2020-12-31 00:00:00']);

return $this->belongsToMany(Podcast::class)
    ->as('subscriptions')
    ->wherePivotNull('expired_at');

return $this->belongsToMany(Podcast::class)
    ->as('subscriptions')
    ->wherePivotNotNull('expired_at');

```

The `wherePivot` adds a where clause constraint to the query, but does not add the specified value when creating new models via the defined relationship. If you need to both query and create relationships with a particular pivot value, you may use the `withPivotValue` method:
```


1return $this->belongsToMany(Role::class)




2    ->withPivotValue('approved', 1);




return $this->belongsToMany(Role::class)
    ->withPivotValue('approved', 1);

```

### [Ordering Queries via Intermediate Table Columns](https://laravel.com/docs/12.x/eloquent-relationships#ordering-queries-via-intermediate-table-columns)
You can order the results returned by `belongsToMany` relationship queries using the `orderByPivot` and `orderByPivotDesc` methods. In the following example, we will retrieve all of the latest badges for the user:
```


1return $this->belongsToMany(Badge::class)




2    ->where('rank', 'gold')




3    ->orderByPivotDesc('created_at');




return $this->belongsToMany(Badge::class)
    ->where('rank', 'gold')
    ->orderByPivotDesc('created_at');

```

### [Defining Custom Intermediate Table Models](https://laravel.com/docs/12.x/eloquent-relationships#defining-custom-intermediate-table-models)
If you would like to define a custom model to represent the intermediate table of your many-to-many relationship, you may call the `using` method when defining the relationship. Custom pivot models give you the opportunity to define additional behavior on the pivot model, such as methods and casts.
Custom many-to-many pivot models should extend the `Illuminate\Database\Eloquent\Relations\Pivot` class while custom polymorphic many-to-many pivot models should extend the `Illuminate\Database\Eloquent\Relations\MorphPivot` class. For example, we may define a `Role` model which uses a custom `RoleUser` pivot model:
```


 1<?php




 2 



 3namespace App\Models;




 4 



 5use Illuminate\Database\Eloquent\Model;




 6use Illuminate\Database\Eloquent\Relations\BelongsToMany;




 7 



 8class Role extends Model




 9{




10    /**




11     * The users that belong to the role.




12     */




13    public function users(): BelongsToMany




14    {




15        return $this->belongsToMany(User::class)->using(RoleUser::class);




16    }




17}




<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsToMany;

class Role extends Model
{
    /**
     * The users that belong to the role.
     */
    public function users(): BelongsToMany
    {
        return $this->belongsToMany(User::class)->using(RoleUser::class);
    }
}

```

When defining the `RoleUser` model, you should extend the `Illuminate\Database\Eloquent\Relations\Pivot` class:
```


 1<?php




 2 



 3namespace App\Models;




 4 



 5use Illuminate\Database\Eloquent\Relations\Pivot;




 6 



 7class RoleUser extends Pivot




 8{




 9    // ...




10}




<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Relations\Pivot;

class RoleUser extends Pivot
{
    // ...
}

```

Pivot models may not use the `SoftDeletes` trait. If you need to soft delete pivot records consider converting your pivot model to an actual Eloquent model.
#### [Custom Pivot Models and Incrementing IDs](https://laravel.com/docs/12.x/eloquent-relationships#custom-pivot-models-and-incrementing-ids)
If you have defined a many-to-many relationship that uses a custom pivot model, and that pivot model has an auto-incrementing primary key, you should ensure your custom pivot model class defines an `incrementing` property that is set to `true`.
```


1/**




2 * Indicates if the IDs are auto-incrementing.




3 *




4 * @var bool




5 */




6public $incrementing = true;




/**
 * Indicates if the IDs are auto-incrementing.
 *
 * @var bool
 */
public $incrementing = true;

```
