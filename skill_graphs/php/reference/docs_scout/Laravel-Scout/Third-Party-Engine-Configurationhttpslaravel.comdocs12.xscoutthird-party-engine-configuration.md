## [Third-Party Engine Configuration](https://laravel.com/docs/12.x/scout#third-party-engine-configuration)
The following configuration options are only relevant when using a third-party search engine such as Algolia, Meilisearch, or Typesense. If you are using the [database engine](https://laravel.com/docs/12.x/scout#database-engine), you may skip this section.
### [Configuring Model Indexes](https://laravel.com/docs/12.x/scout#configuring-model-indexes)
When using a third-party engine, each Eloquent model is synced with a given search "index", which contains all of the searchable records for that model. By default, each model will be persisted to an index matching the model's typical "table" name. Typically, this is the plural form of the model name; however, you are free to customize the model's index by overriding the `searchableAs` method on the model:
```


 1<?php




 2 



 3namespace App\Models;




 4 



 5use Illuminate\Database\Eloquent\Model;




 6use Laravel\Scout\Searchable;




 7 



 8class Post extends Model




 9{




10    use Searchable;




11 



12    /**




13     * Get the name of the index associated with the model.




14     */




15    public function searchableAs(): string




16    {




17        return 'posts_index';




18    }




19}




<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Laravel\Scout\Searchable;

class Post extends Model
{
    use Searchable;

    /**
     * Get the name of the index associated with the model.
     */
    public function searchableAs(): string
    {
        return 'posts_index';
    }
}

```

The `searchableAs` method has no effect when using the database engine, which always searches the model's database table directly.
#### [Configuring the Model ID](https://laravel.com/docs/12.x/scout#configuring-the-model-id)
By default, Scout will use the primary key of the model as the model's unique ID / key that is stored in the search index. If you need to customize this behavior when using a third-party engine, you may override the `getScoutKey` and the `getScoutKeyName` methods on the model:
```


 1<?php




 2 



 3namespace App\Models;




 4 



 5use Illuminate\Database\Eloquent\Model;




 6use Laravel\Scout\Searchable;




 7 



 8class User extends Model




 9{




10    use Searchable;




11 



12    /**




13     * Get the value used to index the model.




14     */




15    public function getScoutKey(): mixed




16    {




17        return $this->email;




18    }




19 



20    /**




21     * Get the key name used to index the model.




22     */




23    public function getScoutKeyName(): mixed




24    {




25        return 'email';




26    }




27}




<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Laravel\Scout\Searchable;

class User extends Model
{
    use Searchable;

    /**
     * Get the value used to index the model.
     */
    public function getScoutKey(): mixed
    {
        return $this->email;
    }

    /**
     * Get the key name used to index the model.
     */
    public function getScoutKeyName(): mixed
    {
        return 'email';
    }
}

```

The `getScoutKey` and `getScoutKeyName` methods have no effect when using the database engine, which always uses the model's primary key.
### [Algolia](https://laravel.com/docs/12.x/scout#algolia-configuration)
#### [Index Settings](https://laravel.com/docs/12.x/scout#algolia-index-settings)
Sometimes you may want to configure additional settings on your Algolia indexes. While you can manage these settings via the Algolia UI, it is sometimes more efficient to manage the desired state of your index configuration directly from your application's `config/scout.php` configuration file.
This approach allows you to deploy these settings through your application's automated deployment pipeline, avoiding manual configuration and ensuring consistency across multiple environments. You may configure filterable attributes, ranking, faceting, or
To get started, add settings for each index in your application's `config/scout.php` configuration file:
```


 1use App\Models\User;




 2use App\Models\Flight;




 3 



 4'algolia' => [




 5    'id' => env('ALGOLIA_APP_ID', ''),




 6    'secret' => env('ALGOLIA_SECRET', ''),




 7    'index-settings' => [




 8        User::class => [




 9            'searchableAttributes' => ['id', 'name', 'email'],




10            'attributesForFaceting'=> ['filterOnly(email)'],




11            // Other settings fields...




12        ],




13        Flight::class => [




14            'searchableAttributes'=> ['id', 'destination'],




15        ],




16    ],




17],




use App\Models\User;
use App\Models\Flight;

'algolia' => [
    'id' => env('ALGOLIA_APP_ID', ''),
    'secret' => env('ALGOLIA_SECRET', ''),
    'index-settings' => [
        User::class => [
            'searchableAttributes' => ['id', 'name', 'email'],
            'attributesForFaceting'=> ['filterOnly(email)'],
            // Other settings fields...
        ],
        Flight::class => [
            'searchableAttributes'=> ['id', 'destination'],
        ],
    ],
],

```

If the model underlying a given index is soft deletable and is included in the `index-settings` array, Scout will automatically include support for faceting on soft deleted models on that index. If you have no other faceting attributes to define for a soft deletable model index, you may simply add an empty entry to the `index-settings` array for that model:
```


1'index-settings' => [




2    Flight::class => []




3],




'index-settings' => [
    Flight::class => []
],

```

After configuring your application's index settings, you must invoke the `scout:sync-index-settings` Artisan command. This command will inform Algolia of your currently configured index settings. For convenience, you may wish to make this command part of your deployment process:
```


1php artisan scout:sync-index-settings




php artisan scout:sync-index-settings

```

#### [Identifying Users](https://laravel.com/docs/12.x/scout#algolia-identifying-users)
Scout allows you to auto identify users when using Algolia. Associating the authenticated user with search operations may be helpful when viewing your search analytics within Algolia's dashboard. You can enable user identification by defining a `SCOUT_IDENTIFY` environment variable as `true` in your application's `.env` file:
```


1SCOUT_IDENTIFY=true




SCOUT_IDENTIFY=true

```

Enabling this feature will also pass the request's IP address and your authenticated user's primary identifier to Algolia so this data is associated with any search request that is made by the user.
### [Meilisearch](https://laravel.com/docs/12.x/scout#meilisearch-configuration)
#### [Index Settings](https://laravel.com/docs/12.x/scout#meilisearch-index-settings)
Meilisearch requires you to pre-define index search settings such as filterable attributes, sortable attributes, and
Filterable attributes are any attributes you plan to filter on when invoking Scout's `where` method, while sortable attributes are any attributes you plan to sort by when invoking Scout's `orderBy` method. To define your index settings, adjust the `index-settings` portion of your `meilisearch` configuration entry in your application's `scout` configuration file:
```


 1use App\Models\User;




 2use App\Models\Flight;




 3 



 4'meilisearch' => [




 5    'host' => env('MEILISEARCH_HOST', 'http://localhost:7700'),




 6    'key' => env('MEILISEARCH_KEY', null),




 7    'index-settings' => [




 8        User::class => [




 9            'filterableAttributes'=> ['id', 'name', 'email'],




10            'sortableAttributes' => ['created_at'],




11            // Other settings fields...




12        ],




13        Flight::class => [




14            'filterableAttributes'=> ['id', 'destination'],




15            'sortableAttributes' => ['updated_at'],




16        ],




17    ],




18],




use App\Models\User;
use App\Models\Flight;

'meilisearch' => [
    'host' => env('MEILISEARCH_HOST', 'http://localhost:7700'),
    'key' => env('MEILISEARCH_KEY', null),
    'index-settings' => [
        User::class => [
            'filterableAttributes'=> ['id', 'name', 'email'],
            'sortableAttributes' => ['created_at'],
            // Other settings fields...
        ],
        Flight::class => [
            'filterableAttributes'=> ['id', 'destination'],
            'sortableAttributes' => ['updated_at'],
        ],
    ],
],

```

If the model underlying a given index is soft deletable and is included in the `index-settings` array, Scout will automatically include support for filtering on soft deleted models on that index. If you have no other filterable or sortable attributes to define for a soft deletable model index, you may simply add an empty entry to the `index-settings` array for that model:
```


1'index-settings' => [




2    Flight::class => []




3],




'index-settings' => [
    Flight::class => []
],

```

After configuring your application's index settings, you must invoke the `scout:sync-index-settings` Artisan command. This command will inform Meilisearch of your currently configured index settings. For convenience, you may wish to make this command part of your deployment process:
```


1php artisan scout:sync-index-settings




php artisan scout:sync-index-settings

```

#### [Searchable Data Types](https://laravel.com/docs/12.x/scout#meilisearch-data-types)
Meilisearch will only perform filter operations (`>`, `<`, etc.) on data of the correct type. When customizing your searchable data, you should ensure that numeric values are cast to their correct type:
```


1public function toSearchableArray()




2{




3    return [




4        'id' => (int) $this->id,




5        'name' => $this->name,




6        'price' => (float) $this->price,




7    ];




8}




public function toSearchableArray()
{
    return [
        'id' => (int) $this->id,
        'name' => $this->name,
        'price' => (float) $this->price,
    ];
}

```

### [Typesense](https://laravel.com/docs/12.x/scout#typesense-configuration)
#### [Preparing Searchable Data](https://laravel.com/docs/12.x/scout#typesense-searchable-data)
When utilizing Typesense, your searchable models must define a `toSearchableArray` method that casts your model's primary key to a string and creation date to a UNIX timestamp:
```


 1/**




 2 * Get the indexable data array for the model.




 3 *




 4 * @return array<string, mixed>




 5 */




 6public function toSearchableArray(): array




 7{




 8    return array_merge($this->toArray(),[




 9        'id' => (string) $this->id,




10        'created_at' => $this->created_at->timestamp,




11    ]);




12}




/**
 * Get the indexable data array for the model.
 *
 * @return array<string, mixed>
 */
public function toSearchableArray(): array
{
    return array_merge($this->toArray(),[
        'id' => (string) $this->id,
        'created_at' => $this->created_at->timestamp,
    ]);
}

```

You should also define your Typesense collection schemas in your application's `config/scout.php` file. A collection schema describes the data types of each field that is searchable via Typesense. For more information on all available schema options, please consult the
If you need to change your Typesense collection's schema after it has been defined, you may either run `scout:flush` and `scout:import`, which will delete all existing indexed data and recreate the schema. Or, you may use Typesense's API to modify the collection's schema without removing any indexed data.
If your searchable model is soft deletable, you should define a `__soft_deleted` field in the model's corresponding Typesense schema within your application's `config/scout.php` configuration file:
```


 1User::class => [




 2    'collection-schema' => [




 3        'fields' => [




 4            // ...




 5            [




 6                'name' => '__soft_deleted',




 7                'type' => 'int32',




 8                'optional' => true,




 9            ],




10        ],




11    ],




12],




User::class => [
    'collection-schema' => [
        'fields' => [
            // ...
            [
                'name' => '__soft_deleted',
                'type' => 'int32',
                'optional' => true,
            ],
        ],
    ],
],

```

#### [Dynamic Search Parameters](https://laravel.com/docs/12.x/scout#typesense-dynamic-search-parameters)
Typesense allows you to modify your `options` method:
```


1use App\Models\Todo;




2 



3Todo::search('Groceries')->options([




4    'query_by' => 'title, description'




5])->get();




use App\Models\Todo;

Todo::search('Groceries')->options([
    'query_by' => 'title, description'
])->get();

```
