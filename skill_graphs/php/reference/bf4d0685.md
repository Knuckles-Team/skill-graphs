## [Configuration](https://laravel.com/docs/12.x/scout#configuration)
### [Configuring Searchable Data](https://laravel.com/docs/12.x/scout#configuring-searchable-data)
By default, the entire `toArray` form of a given model will be persisted to its search index. If you would like to customize the data that is synchronized to the search index, you may override the `toSearchableArray` method on the model:
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




13     * Get the indexable data array for the model.




14     *




15     * @return array<string, mixed>




16     */




17    public function toSearchableArray(): array




18    {




19        $array = $this->toArray();




20 



21        // Customize the data array...




22 



23        return $array;




24    }




25}




<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Laravel\Scout\Searchable;

class Post extends Model
{
    use Searchable;

    /**
     * Get the indexable data array for the model.
     *
     * @return array<string, mixed>
     */
    public function toSearchableArray(): array
    {
        $array = $this->toArray();

        // Customize the data array...

        return $array;
    }
}

```

#### [Configuring Model Engines](https://laravel.com/docs/12.x/scout#configuring-search-engines-per-model)
When searching, Scout will typically use the default search engine specified in your application's `scout` configuration file. However, the search engine for a particular model can be changed by overriding the `searchableUsing` method on the model:
```


 1<?php




 2 



 3namespace App\Models;




 4 



 5use Illuminate\Database\Eloquent\Model;




 6use Laravel\Scout\Engines\Engine;




 7use Laravel\Scout\Scout;




 8use Laravel\Scout\Searchable;




 9 



10class User extends Model




11{




12    use Searchable;




13 



14    /**




15     * Get the engine used to index the model.




16     */




17    public function searchableUsing(): Engine




18    {




19        return Scout::engine('meilisearch');




20    }




21}




<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Laravel\Scout\Engines\Engine;
use Laravel\Scout\Scout;
use Laravel\Scout\Searchable;

class User extends Model
{
    use Searchable;

    /**
     * Get the engine used to index the model.
     */
    public function searchableUsing(): Engine
    {
        return Scout::engine('meilisearch');
    }
}

```
