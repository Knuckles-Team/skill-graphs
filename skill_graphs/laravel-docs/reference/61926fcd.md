## [Deleting Models](https://laravel.com/docs/12.x/eloquent#deleting-models)
To delete a model, you may call the `delete` method on the model instance:
```


1use App\Models\Flight;




2 



3$flight = Flight::find(1);




4 



5$flight->delete();




use App\Models\Flight;

$flight = Flight::find(1);

$flight->delete();

```

#### [Deleting an Existing Model by its Primary Key](https://laravel.com/docs/12.x/eloquent#deleting-an-existing-model-by-its-primary-key)
In the example above, we are retrieving the model from the database before calling the `delete` method. However, if you know the primary key of the model, you may delete the model without explicitly retrieving it by calling the `destroy` method. In addition to accepting the single primary key, the `destroy` method will accept multiple primary keys, an array of primary keys, or a [collection](https://laravel.com/docs/12.x/collections) of primary keys:
```


1Flight::destroy(1);




2 



3Flight::destroy(1, 2, 3);




4 



5Flight::destroy([1, 2, 3]);




6 



7Flight::destroy(collect([1, 2, 3]));




Flight::destroy(1);

Flight::destroy(1, 2, 3);

Flight::destroy([1, 2, 3]);

Flight::destroy(collect([1, 2, 3]));

```

If you are utilizing [soft deleting models](https://laravel.com/docs/12.x/eloquent#soft-deleting), you may permanently delete models via the `forceDestroy` method:
```


1Flight::forceDestroy(1);




Flight::forceDestroy(1);

```

The `destroy` method loads each model individually and calls the `delete` method so that the `deleting` and `deleted` events are properly dispatched for each model.
#### [Deleting Models Using Queries](https://laravel.com/docs/12.x/eloquent#deleting-models-using-queries)
Of course, you may build an Eloquent query to delete all models matching your query's criteria. In this example, we will delete all flights that are marked as inactive. Like mass updates, mass deletes will not dispatch model events for the models that are deleted:
```


1$deleted = Flight::where('active', 0)->delete();




$deleted = Flight::where('active', 0)->delete();

```

To delete all models in a table, you should execute a query without adding any conditions:
```


1$deleted = Flight::query()->delete();




$deleted = Flight::query()->delete();

```

When executing a mass delete statement via Eloquent, the `deleting` and `deleted` model events will not be dispatched for the deleted models. This is because the models are never actually retrieved when executing the delete statement.
### [Soft Deleting](https://laravel.com/docs/12.x/eloquent#soft-deleting)
In addition to actually removing records from your database, Eloquent can also "soft delete" models. When models are soft deleted, they are not actually removed from your database. Instead, a `deleted_at` attribute is set on the model indicating the date and time at which the model was "deleted". To enable soft deletes for a model, add the `Illuminate\Database\Eloquent\SoftDeletes` trait to the model:
```


 1<?php




 2 



 3namespace App\Models;




 4 



 5use Illuminate\Database\Eloquent\Model;




 6use Illuminate\Database\Eloquent\SoftDeletes;




 7 



 8class Flight extends Model




 9{




10    use SoftDeletes;




11}




<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\SoftDeletes;

class Flight extends Model
{
    use SoftDeletes;
}

```

The `SoftDeletes` trait will automatically cast the `deleted_at` attribute to a `DateTime` / `Carbon` instance for you.
You should also add the `deleted_at` column to your database table. The Laravel [schema builder](https://laravel.com/docs/12.x/migrations) contains a helper method to create this column:
```


 1use Illuminate\Database\Schema\Blueprint;




 2use Illuminate\Support\Facades\Schema;




 3 



 4Schema::table('flights', function (Blueprint $table) {




 5    $table->softDeletes();




 6});




 7 



 8Schema::table('flights', function (Blueprint $table) {




 9    $table->dropSoftDeletes();




10});




use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

Schema::table('flights', function (Blueprint $table) {
    $table->softDeletes();
});

Schema::table('flights', function (Blueprint $table) {
    $table->dropSoftDeletes();
});

```

Now, when you call the `delete` method on the model, the `deleted_at` column will be set to the current date and time. However, the model's database record will be left in the table. When querying a model that uses soft deletes, the soft deleted models will automatically be excluded from all query results.
To determine if a given model instance has been soft deleted, you may use the `trashed` method:
```


1if ($flight->trashed()) {




2    // ...




3}




if ($flight->trashed()) {
    // ...
}

```

#### [Restoring Soft Deleted Models](https://laravel.com/docs/12.x/eloquent#restoring-soft-deleted-models)
Sometimes you may wish to "un-delete" a soft deleted model. To restore a soft deleted model, you may call the `restore` method on a model instance. The `restore` method will set the model's `deleted_at` column to `null`:
```


1$flight->restore();




$flight->restore();

```

You may also use the `restore` method in a query to restore multiple models. Again, like other "mass" operations, this will not dispatch any model events for the models that are restored:
```


1Flight::withTrashed()




2    ->where('airline_id', 1)




3    ->restore();




Flight::withTrashed()
    ->where('airline_id', 1)
    ->restore();

```

The `restore` method may also be used when building [relationship](https://laravel.com/docs/12.x/eloquent-relationships) queries:
```


1$flight->history()->restore();




$flight->history()->restore();

```

#### [Permanently Deleting Models](https://laravel.com/docs/12.x/eloquent#permanently-deleting-models)
Sometimes you may need to truly remove a model from your database. You may use the `forceDelete` method to permanently remove a soft deleted model from the database table:
```


1$flight->forceDelete();




$flight->forceDelete();

```

You may also use the `forceDelete` method when building Eloquent relationship queries:
```


1$flight->history()->forceDelete();




$flight->history()->forceDelete();

```

### [Querying Soft Deleted Models](https://laravel.com/docs/12.x/eloquent#querying-soft-deleted-models)
#### [Including Soft Deleted Models](https://laravel.com/docs/12.x/eloquent#including-soft-deleted-models)
As noted above, soft deleted models will automatically be excluded from query results. However, you may force soft deleted models to be included in a query's results by calling the `withTrashed` method on the query:
```


1use App\Models\Flight;




2 



3$flights = Flight::withTrashed()




4    ->where('account_id', 1)




5    ->get();




use App\Models\Flight;

$flights = Flight::withTrashed()
    ->where('account_id', 1)
    ->get();

```

The `withTrashed` method may also be called when building a [relationship](https://laravel.com/docs/12.x/eloquent-relationships) query:
```


1$flight->history()->withTrashed()->get();




$flight->history()->withTrashed()->get();

```

#### [Retrieving Only Soft Deleted Models](https://laravel.com/docs/12.x/eloquent#retrieving-only-soft-deleted-models)
The `onlyTrashed` method will retrieve **only** soft deleted models:
```


1$flights = Flight::onlyTrashed()




2    ->where('airline_id', 1)




3    ->get();




$flights = Flight::onlyTrashed()
    ->where('airline_id', 1)
    ->get();

```
