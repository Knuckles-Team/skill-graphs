## [Inserting and Updating Models](https://laravel.com/docs/12.x/eloquent#inserting-and-updating-models)
### [Inserts](https://laravel.com/docs/12.x/eloquent#inserts)
Of course, when using Eloquent, we don't only need to retrieve models from the database. We also need to insert new records. Thankfully, Eloquent makes it simple. To insert a new record into the database, you should instantiate a new model instance and set attributes on the model. Then, call the `save` method on the model instance:
```


 1<?php




 2 



 3namespace App\Http\Controllers;




 4 



 5use App\Models\Flight;




 6use Illuminate\Http\RedirectResponse;




 7use Illuminate\Http\Request;




 8 



 9class FlightController extends Controller




10{




11    /**




12     * Store a new flight in the database.




13     */




14    public function store(Request $request): RedirectResponse




15    {




16        // Validate the request...




17 



18        $flight = new Flight;




19 



20        $flight->name = $request->name;




21 



22        $flight->save();




23 



24        return redirect('/flights');




25    }




26}




<?php

namespace App\Http\Controllers;

use App\Models\Flight;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;

class FlightController extends Controller
{
    /**
     * Store a new flight in the database.
     */
    public function store(Request $request): RedirectResponse
    {
        // Validate the request...

        $flight = new Flight;

        $flight->name = $request->name;

        $flight->save();

        return redirect('/flights');
    }
}

```

In this example, we assign the `name` field from the incoming HTTP request to the `name` attribute of the `App\Models\Flight` model instance. When we call the `save` method, a record will be inserted into the database. The model's `created_at` and `updated_at` timestamps will automatically be set when the `save` method is called, so there is no need to set them manually.
Alternatively, you may use the `create` method to "save" a new model using a single PHP statement. The inserted model instance will be returned to you by the `create` method:
```


1use App\Models\Flight;




2 



3$flight = Flight::create([




4    'name' => 'London to Paris',




5]);




use App\Models\Flight;

$flight = Flight::create([
    'name' => 'London to Paris',
]);

```

However, before using the `create` method, you will need to specify either a `fillable` or `guarded` property on your model class. These properties are required because all Eloquent models are protected against mass assignment vulnerabilities by default. To learn more about mass assignment, please consult the [mass assignment documentation](https://laravel.com/docs/12.x/eloquent#mass-assignment).
### [Updates](https://laravel.com/docs/12.x/eloquent#updates)
The `save` method may also be used to update models that already exist in the database. To update a model, you should retrieve it and set any attributes you wish to update. Then, you should call the model's `save` method. Again, the `updated_at` timestamp will automatically be updated, so there is no need to manually set its value:
```


1use App\Models\Flight;




2 



3$flight = Flight::find(1);




4 



5$flight->name = 'Paris to London';




6 



7$flight->save();




use App\Models\Flight;

$flight = Flight::find(1);

$flight->name = 'Paris to London';

$flight->save();

```

Occasionally, you may need to update an existing model or create a new model if no matching model exists. Like the `firstOrCreate` method, the `updateOrCreate` method persists the model, so there's no need to manually call the `save` method.
In the example below, if a flight exists with a `departure` location of `Oakland` and a `destination` location of `San Diego`, its `price` and `discounted` columns will be updated. If no such flight exists, a new flight will be created which has the attributes resulting from merging the first argument array with the second argument array:
```


1$flight = Flight::updateOrCreate(




2    ['departure' => 'Oakland', 'destination' => 'San Diego'],




3    ['price' => 99, 'discounted' => 1]




4);




$flight = Flight::updateOrCreate(
    ['departure' => 'Oakland', 'destination' => 'San Diego'],
    ['price' => 99, 'discounted' => 1]
);

```

When using methods such as `firstOrCreate` or `updateOrCreate`, you may not know whether a new model has been created or an existing one has been updated. The `wasRecentlyCreated` property indicates if the model was created during its current lifecycle:
```


1$flight = Flight::updateOrCreate(




2    // ...




3);




4 



5if ($flight->wasRecentlyCreated) {




6    // New flight record was inserted...




7}




$flight = Flight::updateOrCreate(
    // ...
);

if ($flight->wasRecentlyCreated) {
    // New flight record was inserted...
}

```

#### [Mass Updates](https://laravel.com/docs/12.x/eloquent#mass-updates)
Updates can also be performed against models that match a given query. In this example, all flights that are `active` and have a `destination` of `San Diego` will be marked as delayed:
```


1Flight::where('active', 1)




2    ->where('destination', 'San Diego')




3    ->update(['delayed' => 1]);




Flight::where('active', 1)
    ->where('destination', 'San Diego')
    ->update(['delayed' => 1]);

```

The `update` method expects an array of column and value pairs representing the columns that should be updated. The `update` method returns the number of affected rows.
When issuing a mass update via Eloquent, the `saving`, `saved`, `updating`, and `updated` model events will not be fired for the updated models. This is because the models are never actually retrieved when issuing a mass update.
#### [Examining Attribute Changes](https://laravel.com/docs/12.x/eloquent#examining-attribute-changes)
Eloquent provides the `isDirty`, `isClean`, and `wasChanged` methods to examine the internal state of your model and determine how its attributes have changed from when the model was originally retrieved.
The `isDirty` method determines if any of the model's attributes have been changed since the model was retrieved. You may pass a specific attribute name or an array of attributes to the `isDirty` method to determine if any of the attributes are "dirty". The `isClean` method will determine if an attribute has remained unchanged since the model was retrieved. This method also accepts an optional attribute argument:
```


 1use App\Models\User;




 2 



 3$user = User::create([




 4    'first_name' => 'Taylor',




 5    'last_name' => 'Otwell',




 6    'title' => 'Developer',




 7]);




 8 



 9$user->title = 'Painter';




10 



11$user->isDirty(); // true




12$user->isDirty('title'); // true




13$user->isDirty('first_name'); // false




14$user->isDirty(['first_name', 'title']); // true




15 



16$user->isClean(); // false




17$user->isClean('title'); // false




18$user->isClean('first_name'); // true




19$user->isClean(['first_name', 'title']); // false




20 



21$user->save();




22 



23$user->isDirty(); // false




24$user->isClean(); // true




use App\Models\User;

$user = User::create([
    'first_name' => 'Taylor',
    'last_name' => 'Otwell',
    'title' => 'Developer',
]);

$user->title = 'Painter';

$user->isDirty(); // true
$user->isDirty('title'); // true
$user->isDirty('first_name'); // false
$user->isDirty(['first_name', 'title']); // true

$user->isClean(); // false
$user->isClean('title'); // false
$user->isClean('first_name'); // true
$user->isClean(['first_name', 'title']); // false

$user->save();

$user->isDirty(); // false
$user->isClean(); // true

```

The `wasChanged` method determines if any attributes were changed when the model was last saved within the current request cycle. If needed, you may pass an attribute name to see if a particular attribute was changed:
```


 1$user = User::create([




 2    'first_name' => 'Taylor',




 3    'last_name' => 'Otwell',




 4    'title' => 'Developer',




 5]);




 6 



 7$user->title = 'Painter';




 8 



 9$user->save();




10 



11$user->wasChanged(); // true




12$user->wasChanged('title'); // true




13$user->wasChanged(['title', 'slug']); // true




14$user->wasChanged('first_name'); // false




15$user->wasChanged(['first_name', 'title']); // true




$user = User::create([
    'first_name' => 'Taylor',
    'last_name' => 'Otwell',
    'title' => 'Developer',
]);

$user->title = 'Painter';

$user->save();

$user->wasChanged(); // true
$user->wasChanged('title'); // true
$user->wasChanged(['title', 'slug']); // true
$user->wasChanged('first_name'); // false
$user->wasChanged(['first_name', 'title']); // true

```

The `getOriginal` method returns an array containing the original attributes of the model regardless of any changes to the model since it was retrieved. If needed, you may pass a specific attribute name to get the original value of a particular attribute:
```


 1$user = User::find(1);




 2 



 3$user->name; // John




 4$user->email; // john@example.com




 5 



 6$user->name = 'Jack';




 7$user->name; // Jack




 8 



 9$user->getOriginal('name'); // John




10$user->getOriginal(); // Array of original attributes...




$user = User::find(1);

$user->name; // John
$user->email; // john@example.com

$user->name = 'Jack';
$user->name; // Jack

$user->getOriginal('name'); // John
$user->getOriginal(); // Array of original attributes...

```

The `getChanges` method returns an array containing the attributes that changed when the model was last saved, while the `getPrevious` method returns an array containing the original attribute values before the model was last saved:
```


 1$user = User::find(1);




 2 



 3$user->name; // John




 4$user->email; // john@example.com




 5 



 6$user->update([




 7    'name' => 'Jack',




 8    'email' => 'jack@example.com',




 9]);




10 



11$user->getChanges();




12 



13/*




14    [




15        'name' => 'Jack',




16        'email' => 'jack@example.com',




17    ]




18*/




19 



20$user->getPrevious();




21 



22/*




23    [




24        'name' => 'John',




25        'email' => 'john@example.com',




26    ]




27*/




$user = User::find(1);

$user->name; // John
$user->email; // john@example.com

$user->update([
    'name' => 'Jack',
    'email' => 'jack@example.com',
]);

$user->getChanges();

/*
    [
        'name' => 'Jack',
        'email' => 'jack@example.com',
    ]
*/

$user->getPrevious();

/*
    [
        'name' => 'John',
        'email' => 'john@example.com',
    ]
*/

```

### [Mass Assignment](https://laravel.com/docs/12.x/eloquent#mass-assignment)
You may use the `create` method to "save" a new model using a single PHP statement. The inserted model instance will be returned to you by the method:
```


1use App\Models\Flight;




2 



3$flight = Flight::create([




4    'name' => 'London to Paris',




5]);




use App\Models\Flight;

$flight = Flight::create([
    'name' => 'London to Paris',
]);

```

However, before using the `create` method, you will need to specify either a `fillable` or `guarded` property on your model class. These properties are required because all Eloquent models are protected against mass assignment vulnerabilities by default.
A mass assignment vulnerability occurs when a user passes an unexpected HTTP request field and that field changes a column in your database that you did not expect. For example, a malicious user might send an `is_admin` parameter through an HTTP request, which is then passed to your model's `create` method, allowing the user to escalate themselves to an administrator.
So, to get started, you should define which model attributes you want to make mass assignable. You may do this using the `$fillable` property on the model. For example, let's make the `name` attribute of our `Flight` model mass assignable:
```


 1<?php




 2 



 3namespace App\Models;




 4 



 5use Illuminate\Database\Eloquent\Model;




 6 



 7class Flight extends Model




 8{




 9    /**




10     * The attributes that are mass assignable.




11     *




12     * @var array<int, string>




13     */




14    protected $fillable = ['name'];




15}




<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Flight extends Model
{
    /**
     * The attributes that are mass assignable.
     *
     * @var array<int, string>
     */
    protected $fillable = ['name'];
}

```

Once you have specified which attributes are mass assignable, you may use the `create` method to insert a new record in the database. The `create` method returns the newly created model instance:
```


1$flight = Flight::create(['name' => 'London to Paris']);




$flight = Flight::create(['name' => 'London to Paris']);

```

If you already have a model instance, you may use the `fill` method to populate it with an array of attributes:
```


1$flight->fill(['name' => 'Amsterdam to Frankfurt']);




$flight->fill(['name' => 'Amsterdam to Frankfurt']);

```

#### [Mass Assignment and JSON Columns](https://laravel.com/docs/12.x/eloquent#mass-assignment-json-columns)
When assigning JSON columns, each column's mass assignable key must be specified in your model's `$fillable` array. For security, Laravel does not support updating nested JSON attributes when using the `guarded` property:
```


1/**




2 * The attributes that are mass assignable.




3 *




4 * @var array<int, string>




5 */




6protected $fillable = [




7    'options->enabled',




8];




/**
 * The attributes that are mass assignable.
 *
 * @var array<int, string>
 */
protected $fillable = [
    'options->enabled',
];

```

#### [Allowing Mass Assignment](https://laravel.com/docs/12.x/eloquent#allowing-mass-assignment)
If you would like to make all of your attributes mass assignable, you may define your model's `$guarded` property as an empty array. If you choose to unguard your model, you should take special care to always hand-craft the arrays passed to Eloquent's `fill`, `create`, and `update` methods:
```


1/**




2 * The attributes that aren't mass assignable.




3 *




4 * @var array<string>|bool




5 */




6protected $guarded = [];




/**
 * The attributes that aren't mass assignable.
 *
 * @var array<string>|bool
 */
protected $guarded = [];

```

#### [Mass Assignment Exceptions](https://laravel.com/docs/12.x/eloquent#mass-assignment-exceptions)
By default, attributes that are not included in the `$fillable` array are silently discarded when performing mass-assignment operations. In production, this is expected behavior; however, during local development it can lead to confusion as to why model changes are not taking effect.
If you wish, you may instruct Laravel to throw an exception when attempting to fill an unfillable attribute by invoking the `preventSilentlyDiscardingAttributes` method. Typically, this method should be invoked in the `boot` method of your application's `AppServiceProvider` class:
```


1use Illuminate\Database\Eloquent\Model;




2 



3/**




4 * Bootstrap any application services.




5 */




6public function boot(): void




7{




8    Model::preventSilentlyDiscardingAttributes($this->app->isLocal());




9}




use Illuminate\Database\Eloquent\Model;

/**
 * Bootstrap any application services.
 */
public function boot(): void
{
    Model::preventSilentlyDiscardingAttributes($this->app->isLocal());
}

```

### [Upserts](https://laravel.com/docs/12.x/eloquent#upserts)
Eloquent's `upsert` method may be used to update or create records in a single, atomic operation. The method's first argument consists of the values to insert or update, while the second argument lists the column(s) that uniquely identify records within the associated table. The method's third and final argument is an array of the columns that should be updated if a matching record already exists in the database. The `upsert` method will automatically set the `created_at` and `updated_at` timestamps if timestamps are enabled on the model:
```


1Flight::upsert([




2    ['departure' => 'Oakland', 'destination' => 'San Diego', 'price' => 99],




3    ['departure' => 'Chicago', 'destination' => 'New York', 'price' => 150]




4], uniqueBy: ['departure', 'destination'], update: ['price']);




Flight::upsert([
    ['departure' => 'Oakland', 'destination' => 'San Diego', 'price' => 99],
    ['departure' => 'Chicago', 'destination' => 'New York', 'price' => 150]
], uniqueBy: ['departure', 'destination'], update: ['price']);

```

All databases except SQL Server require the columns in the second argument of the `upsert` method to have a "primary" or "unique" index. In addition, the MariaDB and MySQL database drivers ignore the second argument of the `upsert` method and always use the "primary" and "unique" indexes of the table to detect existing records.
