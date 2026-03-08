## [Third-Party Engine Indexing](https://laravel.com/docs/12.x/scout#indexing)
The indexing features described in this section are primarily relevant when using a third-party engine (Algolia, Meilisearch, or Typesense). The database engine searches your database tables directly, so it does not require manual index management.
### [Batch Import](https://laravel.com/docs/12.x/scout#batch-import)
If you are installing Scout into an existing project, you may already have database records you need to import into your indexes. Scout provides a `scout:import` Artisan command that you may use to import all of your existing records into your search indexes:
```


1php artisan scout:import "App\Models\Post"




php artisan scout:import "App\Models\Post"

```

The `scout:queue-import` command may be used to import all of your existing records using [queued jobs](https://laravel.com/docs/12.x/queues):
```


1php artisan scout:queue-import "App\Models\Post" --chunk=500




php artisan scout:queue-import "App\Models\Post" --chunk=500

```

The `flush` command may be used to remove all of a model's records from your search indexes:
```


1php artisan scout:flush "App\Models\Post"




php artisan scout:flush "App\Models\Post"

```

#### [Modifying the Import Query](https://laravel.com/docs/12.x/scout#modifying-the-import-query)
If you would like to modify the query that is used to retrieve all of your models for batch importing, you may define a `makeAllSearchableUsing` method on your model. This is a great place to add any eager relationship loading that may be necessary before importing your models:
```


1use Illuminate\Database\Eloquent\Builder;




2 



3/**




4 * Modify the query used to retrieve models when making all of the models searchable.




5 */




6protected function makeAllSearchableUsing(Builder $query): Builder




7{




8    return $query->with('author');




9}




use Illuminate\Database\Eloquent\Builder;

/**
 * Modify the query used to retrieve models when making all of the models searchable.
 */
protected function makeAllSearchableUsing(Builder $query): Builder
{
    return $query->with('author');
}

```

The `makeAllSearchableUsing` method may not be applicable when using a queue to batch import models. Relationships are [not restored](https://laravel.com/docs/12.x/queues#handling-relationships) when model collections are processed by jobs.
### [Adding Records](https://laravel.com/docs/12.x/scout#adding-records)
Once you have added the `Laravel\Scout\Searchable` trait to a model, all you need to do is `save` or `create` a model instance and it will automatically be added to your search index. If you have configured Scout to [use queues](https://laravel.com/docs/12.x/scout#queueing) this operation will be performed in the background by your queue worker:
```


1use App\Models\Order;




2 



3$order = new Order;




4 



5// ...




6 



7$order->save();




use App\Models\Order;

$order = new Order;

// ...

$order->save();

```

#### [Adding Records via Query](https://laravel.com/docs/12.x/scout#adding-records-via-query)
If you would like to add a collection of models to your search index via an Eloquent query, you may chain the `searchable` method onto the Eloquent query. The `searchable` method will [chunk the results](https://laravel.com/docs/12.x/eloquent#chunking-results) of the query and add the records to your search index. Again, if you have configured Scout to use queues, all of the chunks will be imported in the background by your queue workers:
```


1use App\Models\Order;




2 



3Order::where('price', '>', 100)->searchable();




use App\Models\Order;

Order::where('price', '>', 100)->searchable();

```

You may also call the `searchable` method on an Eloquent relationship instance:
```


1$user->orders()->searchable();




$user->orders()->searchable();

```

Or, if you already have a collection of Eloquent models in memory, you may call the `searchable` method on the collection instance to add the model instances to their corresponding index:
```


1$orders->searchable();




$orders->searchable();

```

The `searchable` method can be considered an "upsert" operation. In other words, if the model record is already in your index, it will be updated. If it does not exist in the search index, it will be added to the index.
### [Updating Records](https://laravel.com/docs/12.x/scout#updating-records)
To update a searchable model, you only need to update the model instance's properties and `save` the model to your database. Scout will automatically persist the changes to your search index:
```


1use App\Models\Order;




2 



3$order = Order::find(1);




4 



5// Update the order...




6 



7$order->save();




use App\Models\Order;

$order = Order::find(1);

// Update the order...

$order->save();

```

You may also invoke the `searchable` method on an Eloquent query instance to update a collection of models. If the models do not exist in your search index, they will be created:
```


1Order::where('price', '>', 100)->searchable();




Order::where('price', '>', 100)->searchable();

```

If you would like to update the search index records for all of the models in a relationship, you may invoke the `searchable` on the relationship instance:
```


1$user->orders()->searchable();




$user->orders()->searchable();

```

Or, if you already have a collection of Eloquent models in memory, you may call the `searchable` method on the collection instance to update the model instances in their corresponding index:
```


1$orders->searchable();




$orders->searchable();

```

#### [Modifying Records Before Importing](https://laravel.com/docs/12.x/scout#modifying-records-before-importing)
Sometimes you may need to prepare the collection of models before they are made searchable. For instance, you may want to eager load a relationship so that the relationship data can be efficiently added to your search index. To accomplish this, define a `makeSearchableUsing` method on the corresponding model:
```


1use Illuminate\Database\Eloquent\Collection;




2 



3/**




4 * Modify the collection of models being made searchable.




5 */




6public function makeSearchableUsing(Collection $models): Collection




7{




8    return $models->load('author');




9}




use Illuminate\Database\Eloquent\Collection;

/**
 * Modify the collection of models being made searchable.
 */
public function makeSearchableUsing(Collection $models): Collection
{
    return $models->load('author');
}

```

#### [Conditionally Updating the Search Index](https://laravel.com/docs/12.x/scout#conditionally-updating-the-search-index)
By default, Scout will reindex an updated model regardless of which attributes were modified. If you would like to customize this behavior, you may define a `searchIndexShouldBeUpdated` method on your model:
```


1/**




2 * Determine if the search index should be updated.




3 */




4public function searchIndexShouldBeUpdated(): bool




5{




6    return $this->wasRecentlyCreated || $this->wasChanged(['title', 'body']);




7}




/**
 * Determine if the search index should be updated.
 */
public function searchIndexShouldBeUpdated(): bool
{
    return $this->wasRecentlyCreated || $this->wasChanged(['title', 'body']);
}

```

### [Removing Records](https://laravel.com/docs/12.x/scout#removing-records)
To remove a record from your index you may simply `delete` the model from the database. This may be done even if you are using [soft deleted](https://laravel.com/docs/12.x/eloquent#soft-deleting) models:
```


1use App\Models\Order;




2 



3$order = Order::find(1);




4 



5$order->delete();




use App\Models\Order;

$order = Order::find(1);

$order->delete();

```

If you do not want to retrieve the model before deleting the record, you may use the `unsearchable` method on an Eloquent query instance:
```


1Order::where('price', '>', 100)->unsearchable();




Order::where('price', '>', 100)->unsearchable();

```

If you would like to remove the search index records for all of the models in a relationship, you may invoke the `unsearchable` on the relationship instance:
```


1$user->orders()->unsearchable();




$user->orders()->unsearchable();

```

Or, if you already have a collection of Eloquent models in memory, you may call the `unsearchable` method on the collection instance to remove the model instances from their corresponding index:
```


1$orders->unsearchable();




$orders->unsearchable();

```

To remove all of the model records from their corresponding index, you may invoke the `removeAllFromSearch` method:
```


1Order::removeAllFromSearch();




Order::removeAllFromSearch();

```

### [Pausing Indexing](https://laravel.com/docs/12.x/scout#pausing-indexing)
Sometimes you may need to perform a batch of Eloquent operations on a model without syncing the model data to your search index. You may do this using the `withoutSyncingToSearch` method. This method accepts a single closure which will be immediately executed. Any model operations that occur within the closure will not be synced to the model's index:
```


1use App\Models\Order;




2 



3Order::withoutSyncingToSearch(function () {




4    // Perform model actions...




5});




use App\Models\Order;

Order::withoutSyncingToSearch(function () {
    // Perform model actions...
});

```

### [Conditionally Searchable Model Instances](https://laravel.com/docs/12.x/scout#conditionally-searchable-model-instances)
Sometimes you may need to only make a model searchable under certain conditions. For example, imagine you have `App\Models\Post` model that may be in one of two states: "draft" and "published". You may only want to allow "published" posts to be searchable. To accomplish this, you may define a `shouldBeSearchable` method on your model:
```


1/**




2 * Determine if the model should be searchable.




3 */




4public function shouldBeSearchable(): bool




5{




6    return $this->isPublished();




7}




/**
 * Determine if the model should be searchable.
 */
public function shouldBeSearchable(): bool
{
    return $this->isPublished();
}

```

The `shouldBeSearchable` method is only applied when manipulating models through the `save` and `create` methods, queries, or relationships. Directly making models or collections searchable using the `searchable` method will override the result of the `shouldBeSearchable` method.
The `shouldBeSearchable` method is not applicable when using Scout's "database" engine, as all searchable data is always stored in the database. To achieve similar behavior when using the database engine, you should use [where clauses](https://laravel.com/docs/12.x/scout#where-clauses) instead.
