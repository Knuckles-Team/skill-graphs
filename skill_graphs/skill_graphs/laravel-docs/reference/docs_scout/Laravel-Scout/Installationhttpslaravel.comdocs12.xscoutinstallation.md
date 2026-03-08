## [Installation](https://laravel.com/docs/12.x/scout#installation)
First, install Scout via the Composer package manager:
```


1composer require laravel/scout




composer require laravel/scout

```

After installing Scout, you should publish the Scout configuration file using the `vendor:publish` Artisan command. This command will publish the `scout.php` configuration file to your application's `config` directory:
```


1php artisan vendor:publish --provider="Laravel\Scout\ScoutServiceProvider"




php artisan vendor:publish --provider="Laravel\Scout\ScoutServiceProvider"

```

Finally, add the `Laravel\Scout\Searchable` trait to the model you would like to make searchable. This trait will register a model observer that will automatically keep the model in sync with your search driver:
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




11}




<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Laravel\Scout\Searchable;

class Post extends Model
{
    use Searchable;
}

```

### [Queueing](https://laravel.com/docs/12.x/scout#queueing)
When using an engine that is not the `database` or `collection` engine, you should strongly consider configuring a [queue driver](https://laravel.com/docs/12.x/queues) before using the library. Running a queue worker will allow Scout to queue all operations that sync your model information to your search indexes, providing much better response times for your application's web interface.
Once you have configured a queue driver, set the value of the `queue` option in your `config/scout.php` configuration file to `true`:
```


1'queue' => true,




'queue' => true,

```

Even when the `queue` option is set to `false`, it's important to remember that some Scout drivers like Algolia and Meilisearch always index records asynchronously. In other words, even though the index operation has completed within your Laravel application, the search engine itself may not reflect the new and updated records immediately.
To specify the connection and queue that your Scout jobs utilize, you may define the `queue` configuration option as an array:
```


1'queue' => [




2    'connection' => 'redis',




3    'queue' => 'scout'




4],




'queue' => [
    'connection' => 'redis',
    'queue' => 'scout'
],

```

Of course, if you customize the connection and queue that Scout jobs utilize, you should run a queue worker to process jobs on that connection and queue:
```


1php artisan queue:work redis --queue=scout




php artisan queue:work redis --queue=scout

```
