## [Database / Collection Engines](https://laravel.com/docs/12.x/scout#database-and-collection-engines)
### [Database Engine](https://laravel.com/docs/12.x/scout#database-engine)
The database engine currently supports MySQL and PostgreSQL, both of which provide support for fast, full-text column indexing.
The `database` engine uses MySQL / PostgreSQL full-text indexes and `LIKE` clauses to search your existing database directly. For many applications, this is the simplest and most practical way to add search — no external service or additional infrastructure required.
To use the database engine, set the `SCOUT_DRIVER` environment variable to `database`:
```


1SCOUT_DRIVER=database




SCOUT_DRIVER=database

```

Once configured, you may [define your searchable data](https://laravel.com/docs/12.x/scout#configuring-searchable-data) and start [executing search queries](https://laravel.com/docs/12.x/scout#searching) against your models. Unlike third-party engines, the database engine requires no separate indexing step — it searches your database tables directly.
#### Customizing Database Searching Strategies
By default, the database engine will execute a `LIKE` query against every model attribute that you have [configured as searchable](https://laravel.com/docs/12.x/scout#configuring-searchable-data). However, you can assign more efficient search strategies to specific columns. The `SearchUsingFullText` attribute will use your database's full-text index for that column, while `SearchUsingPrefix` will only match the beginning of strings (`example%`) instead of searching within the entire string (`%example%`).
To define this behavior, assign PHP attributes to your model's `toSearchableArray` method. Any columns without an attribute will continue to use the default `LIKE` strategy:
```


 1use Laravel\Scout\Attributes\SearchUsingFullText;




 2use Laravel\Scout\Attributes\SearchUsingPrefix;




 3 



 4/**




 5 * Get the indexable data array for the model.




 6 *




 7 * @return array<string, mixed>




 8 */




 9#[SearchUsingPrefix(['id', 'email'])]




10#[SearchUsingFullText(['bio'])]




11public function toSearchableArray(): array




12{




13    return [




14        'id' => $this->id,




15        'name' => $this->name,




16        'email' => $this->email,




17        'bio' => $this->bio,




18    ];




19}




use Laravel\Scout\Attributes\SearchUsingFullText;
use Laravel\Scout\Attributes\SearchUsingPrefix;

/**
 * Get the indexable data array for the model.
 *
 * @return array<string, mixed>
 */
#[SearchUsingPrefix(['id', 'email'])]
#[SearchUsingFullText(['bio'])]
public function toSearchableArray(): array
{
    return [
        'id' => $this->id,
        'name' => $this->name,
        'email' => $this->email,
        'bio' => $this->bio,
    ];
}

```

Before specifying that a column should use full text query constraints, ensure that the column has been assigned a [full text index](https://laravel.com/docs/12.x/migrations#available-index-types).
### [Collection Engine](https://laravel.com/docs/12.x/scout#collection-engine)
The "collection" engine is intended for quick prototypes, extremely small datasets (a few hundred records), or running tests. It retrieves all possible records from your database and uses Laravel's `Str::is` helper to filter them in PHP, so it does not require any indexing or database-specific features. For anything beyond trivial use cases, you should use the [database engine](https://laravel.com/docs/12.x/scout#database-engine) instead.
To use the collection engine, you may simply set the value of the `SCOUT_DRIVER` environment variable to `collection`, or specify the `collection` driver directly in your application's `scout` configuration file:
```


1SCOUT_DRIVER=collection




SCOUT_DRIVER=collection

```

Once you have specified the collection driver as your preferred driver, you may start [executing search queries](https://laravel.com/docs/12.x/scout#searching) against your models. Search engine indexing, such as the indexing needed to seed Algolia, Meilisearch, or Typesense indexes, is unnecessary when using the collection engine.
#### Differences From Database Engine
While the database engine uses full-text indexes and `LIKE` clauses to find matching records efficiently, the collection engine pulls all records and filters them in PHP. The collection engine is the most portable option as it works across all relational databases supported by Laravel (including SQLite and SQL Server); however, it is significantly less efficient than the database engine and should not be used with large datasets.
