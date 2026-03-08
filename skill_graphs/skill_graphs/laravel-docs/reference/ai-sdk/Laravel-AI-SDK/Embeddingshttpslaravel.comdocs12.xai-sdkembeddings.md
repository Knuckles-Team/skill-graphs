## [Embeddings](https://laravel.com/docs/12.x/ai-sdk#embeddings)
You may easily generate vector embeddings for any given string using the new `toEmbeddings` method available via Laravel's `Stringable` class:
```


1use Illuminate\Support\Str;




2 



3$embeddings = Str::of('Napa Valley has great wine.')->toEmbeddings();




use Illuminate\Support\Str;

$embeddings = Str::of('Napa Valley has great wine.')->toEmbeddings();

```

Alternatively, you may use the `Embeddings` class to generate embeddings for multiple inputs at once:
```


1use Laravel\Ai\Embeddings;




2 



3$response = Embeddings::for([




4    'Napa Valley has great wine.',




5    'Laravel is a PHP framework.',




6])->generate();




7 



8$response->embeddings; // [[0.123, 0.456, ...], [0.789, 0.012, ...]]




use Laravel\Ai\Embeddings;

$response = Embeddings::for([
    'Napa Valley has great wine.',
    'Laravel is a PHP framework.',
])->generate();

$response->embeddings; // [[0.123, 0.456, ...], [0.789, 0.012, ...]]

```

You may specify the dimensions and provider for the embeddings:
```


1$response = Embeddings::for(['Napa Valley has great wine.'])




2    ->dimensions(1536)




3    ->generate(Lab::OpenAI, 'text-embedding-3-small');




$response = Embeddings::for(['Napa Valley has great wine.'])
    ->dimensions(1536)
    ->generate(Lab::OpenAI, 'text-embedding-3-small');

```

### [Querying Embeddings](https://laravel.com/docs/12.x/ai-sdk#querying-embeddings)
Once you have generated embeddings, you will typically store them in a `vector` column in your database for later querying. Laravel provides native support for vector columns on PostgreSQL via the `pgvector` extension. To get started, define a `vector` column in your migration, specifying the number of dimensions:
```


1Schema::ensureVectorExtensionExists();




2 



3Schema::create('documents', function (Blueprint $table) {




4    $table->id();




5    $table->string('title');




6    $table->text('content');




7    $table->vector('embedding', dimensions: 1536);




8    $table->timestamps();




9});




Schema::ensureVectorExtensionExists();

Schema::create('documents', function (Blueprint $table) {
    $table->id();
    $table->string('title');
    $table->text('content');
    $table->vector('embedding', dimensions: 1536);
    $table->timestamps();
});

```

You may also add a vector index to speed up similarity searches. When calling `index` on a vector column, Laravel will automatically create an HNSW index with cosine distance:
```


1$table->vector('embedding', dimensions: 1536)->index();




$table->vector('embedding', dimensions: 1536)->index();

```

On your Eloquent model, you should cast the vector column to an `array`:
```


1protected function casts(): array




2{




3    return [




4        'embedding' => 'array',




5    ];




6}




protected function casts(): array
{
    return [
        'embedding' => 'array',
    ];
}

```

To query for similar records, use the `whereVectorSimilarTo` method. This method filters results by a minimum cosine similarity (between `0.0` and `1.0`, where `1.0` is identical) and orders the results by similarity:
```


1use App\Models\Document;




2 



3$documents = Document::query()




4    ->whereVectorSimilarTo('embedding', $queryEmbedding, minSimilarity: 0.4)




5    ->limit(10)




6    ->get();




use App\Models\Document;

$documents = Document::query()
    ->whereVectorSimilarTo('embedding', $queryEmbedding, minSimilarity: 0.4)
    ->limit(10)
    ->get();

```

The `$queryEmbedding` may be an array of floats or a plain string. When a string is given, Laravel will automatically generate embeddings for it:
```


1$documents = Document::query()




2    ->whereVectorSimilarTo('embedding', 'best wineries in Napa Valley')




3    ->limit(10)




4    ->get();




$documents = Document::query()
    ->whereVectorSimilarTo('embedding', 'best wineries in Napa Valley')
    ->limit(10)
    ->get();

```

If you need more control, you may use the lower-level `whereVectorDistanceLessThan`, `selectVectorDistance`, and `orderByVectorDistance` methods independently:
```


1$documents = Document::query()




2    ->select('*')




3    ->selectVectorDistance('embedding', $queryEmbedding, as: 'distance')




4    ->whereVectorDistanceLessThan('embedding', $queryEmbedding, maxDistance: 0.3)




5    ->orderByVectorDistance('embedding', $queryEmbedding)




6    ->limit(10)




7    ->get();




$documents = Document::query()
    ->select('*')
    ->selectVectorDistance('embedding', $queryEmbedding, as: 'distance')
    ->whereVectorDistanceLessThan('embedding', $queryEmbedding, maxDistance: 0.3)
    ->orderByVectorDistance('embedding', $queryEmbedding)
    ->limit(10)
    ->get();

```

If you would like to give an agent the ability to perform similarity searches as a tool, check out the [Similarity Search](https://laravel.com/docs/12.x/ai-sdk#similarity-search) tool documentation.
Vector queries are currently only supported on PostgreSQL connections using the `pgvector` extension.
### [Caching Embeddings](https://laravel.com/docs/12.x/ai-sdk#caching-embeddings)
Embedding generation can be cached to avoid redundant API calls for identical inputs. To enable caching, set the `ai.caching.embeddings.cache` configuration option to `true`:
```


1'caching' => [




2    'embeddings' => [




3        'cache' => true,




4        'store' => env('CACHE_STORE', 'database'),




5        // ...




6    ],




7],




'caching' => [
    'embeddings' => [
        'cache' => true,
        'store' => env('CACHE_STORE', 'database'),
        // ...
    ],
],

```

When caching is enabled, embeddings are cached for 30 days. The cache key is based on the provider, model, dimensions, and input content, ensuring that identical requests return cached results while different configurations generate fresh embeddings.
You may also enable caching for a specific request using the `cache` method, even when global caching is disabled:
```


1$response = Embeddings::for(['Napa Valley has great wine.'])




2    ->cache()




3    ->generate();




$response = Embeddings::for(['Napa Valley has great wine.'])
    ->cache()
    ->generate();

```

You may specify a custom cache duration in seconds:
```


1$response = Embeddings::for(['Napa Valley has great wine.'])




2    ->cache(seconds: 3600) // Cache for 1 hour




3    ->generate();




$response = Embeddings::for(['Napa Valley has great wine.'])
    ->cache(seconds: 3600) // Cache for 1 hour
    ->generate();

```

The `toEmbeddings` Stringable method also accepts a `cache` argument:
```


1// Cache with default duration...




2$embeddings = Str::of('Napa Valley has great wine.')->toEmbeddings(cache: true);




3 



4// Cache for a specific duration...




5$embeddings = Str::of('Napa Valley has great wine.')->toEmbeddings(cache: 3600);




// Cache with default duration...
$embeddings = Str::of('Napa Valley has great wine.')->toEmbeddings(cache: true);

// Cache for a specific duration...
$embeddings = Str::of('Napa Valley has great wine.')->toEmbeddings(cache: 3600);

```
