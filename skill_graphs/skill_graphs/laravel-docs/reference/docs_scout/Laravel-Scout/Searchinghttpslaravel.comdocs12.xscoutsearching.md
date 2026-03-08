## [Searching](https://laravel.com/docs/12.x/scout#searching)
You may begin searching a model using the `search` method. The search method accepts a single string that will be used to search your models. You should then chain the `get` method onto the search query to retrieve the Eloquent models that match the given search query:
```


1use App\Models\Order;




2 



3$orders = Order::search('Star Trek')->get();




use App\Models\Order;

$orders = Order::search('Star Trek')->get();

```

Since Scout searches return a collection of Eloquent models, you may even return the results directly from a route or controller and they will automatically be converted to JSON:
```


1use App\Models\Order;




2use Illuminate\Http\Request;




3 



4Route::get('/search', function (Request $request) {




5    return Order::search($request->search)->get();




6});




use App\Models\Order;
use Illuminate\Http\Request;

Route::get('/search', function (Request $request) {
    return Order::search($request->search)->get();
});

```

If you would like to get the raw search results before they are converted to Eloquent models, you may use the `raw` method:
```


1$orders = Order::search('Star Trek')->raw();




$orders = Order::search('Star Trek')->raw();

```

#### [Custom Indexes](https://laravel.com/docs/12.x/scout#custom-indexes)
When searching using third-party engines, search queries will typically be performed on the index specified by the model's [searchableAs](https://laravel.com/docs/12.x/scout#configuring-model-indexes) method. However, you may use the `within` method to specify a custom index that should be searched instead:
```


1$orders = Order::search('Star Trek')




2    ->within('tv_shows_popularity_desc')




3    ->get();




$orders = Order::search('Star Trek')
    ->within('tv_shows_popularity_desc')
    ->get();

```

### [Where Clauses](https://laravel.com/docs/12.x/scout#where-clauses)
Scout allows you to add simple "where" clauses to your search queries. Currently, these clauses only support basic equality checks and are primarily useful for scoping search queries by an owner ID:
```


1use App\Models\Order;




2 



3$orders = Order::search('Star Trek')->where('user_id', 1)->get();




use App\Models\Order;

$orders = Order::search('Star Trek')->where('user_id', 1)->get();

```

In addition, the `whereIn` method may be used to verify that a given column's value is contained within the given array:
```


1$orders = Order::search('Star Trek')->whereIn(




2    'status', ['open', 'paid']




3)->get();




$orders = Order::search('Star Trek')->whereIn(
    'status', ['open', 'paid']
)->get();

```

The `whereNotIn` method verifies that the given column's value is not contained in the given array:
```


1$orders = Order::search('Star Trek')->whereNotIn(




2    'status', ['closed']




3)->get();




$orders = Order::search('Star Trek')->whereNotIn(
    'status', ['closed']
)->get();

```

If your application is using Meilisearch, you must configure your application's [filterable attributes](https://laravel.com/docs/12.x/scout#meilisearch-index-settings) before utilizing Scout's "where" clauses.
#### [Customizing the Eloquent Results Query](https://laravel.com/docs/12.x/scout#customizing-the-eloquent-results-query)
After Scout retrieves a list of matching Eloquent models from your application's search engine, Eloquent is used to retrieve all of the matching models by their primary keys. You may customize this query by invoking the `query` method. The `query` method accepts a closure that will receive the Eloquent query builder instance as an argument:
```


1use App\Models\Order;




2use Illuminate\Database\Eloquent\Builder;




3 



4$orders = Order::search('Star Trek')




5    ->query(fn (Builder $query) => $query->with('invoices'))




6    ->get();




use App\Models\Order;
use Illuminate\Database\Eloquent\Builder;

$orders = Order::search('Star Trek')
    ->query(fn (Builder $query) => $query->with('invoices'))
    ->get();

```

When using a third-party engine, this callback is invoked after the relevant models have already been retrieved from the search engine, so it should not be used for "filtering" results — use [Scout where clauses](https://laravel.com/docs/12.x/scout#where-clauses) instead. However, when using the database engine, the `query` method's constraints are applied directly to the database query, so you may use it for filtering as well.
### [Pagination](https://laravel.com/docs/12.x/scout#pagination)
In addition to retrieving a collection of models, you may paginate your search results using the `paginate` method. This method will return an `Illuminate\Pagination\LengthAwarePaginator` instance just as if you had [paginated a traditional Eloquent query](https://laravel.com/docs/12.x/pagination):
```


1use App\Models\Order;




2 



3$orders = Order::search('Star Trek')->paginate();




use App\Models\Order;

$orders = Order::search('Star Trek')->paginate();

```

You may specify how many models to retrieve per page by passing the amount as the first argument to the `paginate` method:
```


1$orders = Order::search('Star Trek')->paginate(15);




$orders = Order::search('Star Trek')->paginate(15);

```

When using the database engine, you may also use the `simplePaginate` method. Unlike `paginate`, which retrieves the total number of matching records so it can display page numbers, `simplePaginate` only determines whether there are more results beyond the current page — making it more efficient for large datasets where you only need "previous" and "next" links:
```


1$orders = Order::search('Star Trek')->simplePaginate(15);




$orders = Order::search('Star Trek')->simplePaginate(15);

```

Once you have retrieved the results, you may display the results and render the page links using [Blade](https://laravel.com/docs/12.x/blade) just as if you had paginated a traditional Eloquent query:
```


1<div class="container">




2    @foreach ($orders as $order)




3        {{ $order->price }}




4    @endforeach




5</div>




6 



7{{ $orders->links() }}




<div class="container">
    @foreach ($orders as $order)
        {{ $order->price }}
    @endforeach
</div>

{{ $orders->links() }}

```

Of course, if you would like to retrieve the pagination results as JSON, you may return the paginator instance directly from a route or controller:
```


1use App\Models\Order;




2use Illuminate\Http\Request;




3 



4Route::get('/orders', function (Request $request) {




5    return Order::search($request->input('query'))->paginate(15);




6});




use App\Models\Order;
use Illuminate\Http\Request;

Route::get('/orders', function (Request $request) {
    return Order::search($request->input('query'))->paginate(15);
});

```

Since search engines are not aware of your Eloquent model's global scope definitions, you should not utilize global scopes in applications that utilize Scout pagination. Or, you should recreate the global scope's constraints when searching via Scout.
### [Soft Deleting](https://laravel.com/docs/12.x/scout#soft-deleting)
If your indexed models are [soft deleting](https://laravel.com/docs/12.x/eloquent#soft-deleting) and you need to search your soft deleted models, set the `soft_delete` option of the `config/scout.php` configuration file to `true`:
```


1'soft_delete' => true,




'soft_delete' => true,

```

When this configuration option is `true`, Scout will not remove soft deleted models from the search index. Instead, it will set a hidden `__soft_deleted` attribute on the indexed record. Then, you may use the `withTrashed` or `onlyTrashed` methods to retrieve the soft deleted records when searching:
```


1use App\Models\Order;




2 



3// Include trashed records when retrieving results...




4$orders = Order::search('Star Trek')->withTrashed()->get();




5 



6// Only include trashed records when retrieving results...




7$orders = Order::search('Star Trek')->onlyTrashed()->get();




use App\Models\Order;

// Include trashed records when retrieving results...
$orders = Order::search('Star Trek')->withTrashed()->get();

// Only include trashed records when retrieving results...
$orders = Order::search('Star Trek')->onlyTrashed()->get();

```

When a soft deleted model is permanently deleted using `forceDelete`, Scout will remove it from the search index automatically.
### [Customizing Engine Searches](https://laravel.com/docs/12.x/scout#customizing-engine-searches)
If you need to perform advanced customization of the search behavior of an engine you may pass a closure as the second argument to the `search` method. For example, you could use this callback to add geo-location data to your search options before the search query is passed to Algolia:
```


 1use Algolia\AlgoliaSearch\SearchIndex;




 2use App\Models\Order;




 3 



 4Order::search(




 5    'Star Trek',




 6    function (SearchIndex $algolia, string $query, array $options) {




 7        $options['body']['query']['bool']['filter']['geo_distance'] = [




 8            'distance' => '1000km',




 9            'location' => ['lat' => 36, 'lon' => 111],




10        ];




11 



12        return $algolia->search($query, $options);




13    }




14)->get();




use Algolia\AlgoliaSearch\SearchIndex;
use App\Models\Order;

Order::search(
    'Star Trek',
    function (SearchIndex $algolia, string $query, array $options) {
        $options['body']['query']['bool']['filter']['geo_distance'] = [
            'distance' => '1000km',
            'location' => ['lat' => 36, 'lon' => 111],
        ];

        return $algolia->search($query, $options);
    }
)->get();

```
