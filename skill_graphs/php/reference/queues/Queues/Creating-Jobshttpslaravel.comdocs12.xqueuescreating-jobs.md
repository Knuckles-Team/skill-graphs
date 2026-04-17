## [Creating Jobs](https://laravel.com/docs/12.x/queues#creating-jobs)
### [Generating Job Classes](https://laravel.com/docs/12.x/queues#generating-job-classes)
By default, all of the queueable jobs for your application are stored in the `app/Jobs` directory. If the `app/Jobs` directory doesn't exist, it will be created when you run the `make:job` Artisan command:
```


1php artisan make:job ProcessPodcast




php artisan make:job ProcessPodcast

```

The generated class will implement the `Illuminate\Contracts\Queue\ShouldQueue` interface, indicating to Laravel that the job should be pushed onto the queue to run asynchronously.
Job stubs may be customized using [stub publishing](https://laravel.com/docs/12.x/artisan#stub-customization).
### [Class Structure](https://laravel.com/docs/12.x/queues#class-structure)
Job classes are very simple, normally containing only a `handle` method that is invoked when the job is processed by the queue. To get started, let's take a look at an example job class. In this example, we'll pretend we manage a podcast publishing service and need to process the uploaded podcast files before they are published:
```


 1<?php




 2 



 3namespace App\Jobs;




 4 



 5use App\Models\Podcast;




 6use App\Services\AudioProcessor;




 7use Illuminate\Contracts\Queue\ShouldQueue;




 8use Illuminate\Foundation\Queue\Queueable;




 9 



10class ProcessPodcast implements ShouldQueue




11{




12    use Queueable;




13 



14    /**




15     * Create a new job instance.




16     */




17    public function __construct(




18        public Podcast $podcast,




19    ) {}




20 



21    /**




22     * Execute the job.




23     */




24    public function handle(AudioProcessor $processor): void




25    {




26        // Process uploaded podcast...




27    }




28}




<?php

namespace App\Jobs;

use App\Models\Podcast;
use App\Services\AudioProcessor;
use Illuminate\Contracts\Queue\ShouldQueue;
use Illuminate\Foundation\Queue\Queueable;

class ProcessPodcast implements ShouldQueue
{
    use Queueable;

    /**
     * Create a new job instance.
     */
    public function __construct(
        public Podcast $podcast,
    ) {}

    /**
     * Execute the job.
     */
    public function handle(AudioProcessor $processor): void
    {
        // Process uploaded podcast...
    }
}

```

In this example, note that we were able to pass an [Eloquent model](https://laravel.com/docs/12.x/eloquent) directly into the queued job's constructor. Because of the `Queueable` trait that the job is using, Eloquent models and their loaded relationships will be gracefully serialized and unserialized when the job is processing.
If your queued job accepts an Eloquent model in its constructor, only the identifier for the model will be serialized onto the queue. When the job is actually handled, the queue system will automatically re-retrieve the full model instance and its loaded relationships from the database. This approach to model serialization allows for much smaller job payloads to be sent to your queue driver.
#### [`handle` Method Dependency Injection](https://laravel.com/docs/12.x/queues#handle-method-dependency-injection)
The `handle` method is invoked when the job is processed by the queue. Note that we are able to type-hint dependencies on the `handle` method of the job. The Laravel [service container](https://laravel.com/docs/12.x/container) automatically injects these dependencies.
If you would like to take total control over how the container injects dependencies into the `handle` method, you may use the container's `bindMethod` method. The `bindMethod` method accepts a callback which receives the job and the container. Within the callback, you are free to invoke the `handle` method however you wish. Typically, you should call this method from the `boot` method of your `App\Providers\AppServiceProvider` [service provider](https://laravel.com/docs/12.x/providers):
```


1use App\Jobs\ProcessPodcast;




2use App\Services\AudioProcessor;




3use Illuminate\Contracts\Foundation\Application;




4 



5$this->app->bindMethod([ProcessPodcast::class, 'handle'], function (ProcessPodcast $job, Application $app) {




6    return $job->handle($app->make(AudioProcessor::class));




7});




use App\Jobs\ProcessPodcast;
use App\Services\AudioProcessor;
use Illuminate\Contracts\Foundation\Application;

$this->app->bindMethod([ProcessPodcast::class, 'handle'], function (ProcessPodcast $job, Application $app) {
    return $job->handle($app->make(AudioProcessor::class));
});

```

Binary data, such as raw image contents, should be passed through the `base64_encode` function before being passed to a queued job. Otherwise, the job may not properly serialize to JSON when being placed on the queue.
#### [Queued Relationships](https://laravel.com/docs/12.x/queues#handling-relationships)
Because all loaded Eloquent model relationships also get serialized when a job is queued, the serialized job string can sometimes become quite large. Furthermore, when a job is deserialized and model relationships are re-retrieved from the database, they will be retrieved in their entirety. Any previous relationship constraints that were applied before the model was serialized during the job queueing process will not be applied when the job is deserialized. Therefore, if you wish to work with a subset of a given relationship, you should re-constrain that relationship within your queued job.
Or, to prevent relations from being serialized, you can call the `withoutRelations` method on the model when setting a property value. This method will return an instance of the model without its loaded relationships:
```


1/**




2 * Create a new job instance.




3 */




4public function __construct(




5    Podcast $podcast,




6) {




7    $this->podcast = $podcast->withoutRelations();




8}




/**
 * Create a new job instance.
 */
public function __construct(
    Podcast $podcast,
) {
    $this->podcast = $podcast->withoutRelations();
}

```

If you are using `WithoutRelations` attribute:
```


1use Illuminate\Queue\Attributes\WithoutRelations;




2 



3/**




4 * Create a new job instance.




5 */




6public function __construct(




7    #[WithoutRelations]




8    public Podcast $podcast,




9) {}




use Illuminate\Queue\Attributes\WithoutRelations;

/**
 * Create a new job instance.
 */
public function __construct(
    #[WithoutRelations]
    public Podcast $podcast,
) {}

```

For convenience, if you wish to serialize all models without relationships, you may apply the `WithoutRelations` attribute to the entire class instead of applying the attribute to each model:
```


 1<?php




 2 



 3namespace App\Jobs;




 4 



 5use App\Models\DistributionPlatform;




 6use App\Models\Podcast;




 7use Illuminate\Contracts\Queue\ShouldQueue;




 8use Illuminate\Foundation\Queue\Queueable;




 9use Illuminate\Queue\Attributes\WithoutRelations;




10 



11#[WithoutRelations]




12class ProcessPodcast implements ShouldQueue




13{




14    use Queueable;




15 



16    /**




17     * Create a new job instance.




18     */




19    public function __construct(




20        public Podcast $podcast,




21        public DistributionPlatform $platform,




22    ) {}




23}




<?php

namespace App\Jobs;

use App\Models\DistributionPlatform;
use App\Models\Podcast;
use Illuminate\Contracts\Queue\ShouldQueue;
use Illuminate\Foundation\Queue\Queueable;
use Illuminate\Queue\Attributes\WithoutRelations;

#[WithoutRelations]
class ProcessPodcast implements ShouldQueue
{
    use Queueable;

    /**
     * Create a new job instance.
     */
    public function __construct(
        public Podcast $podcast,
        public DistributionPlatform $platform,
    ) {}
}

```

If a job receives a collection or array of Eloquent models instead of a single model, the models within that collection will not have their relationships restored when the job is deserialized and executed. This is to prevent excessive resource usage on jobs that deal with large numbers of models.
### [Unique Jobs](https://laravel.com/docs/12.x/queues#unique-jobs)
Unique jobs require a cache driver that supports [locks](https://laravel.com/docs/12.x/cache#atomic-locks). Currently, the `memcached`, `redis`, `dynamodb`, `database`, `file`, and `array` cache drivers support atomic locks.
Unique job constraints do not apply to jobs within batches.
Sometimes, you may want to ensure that only one instance of a specific job is on the queue at any point in time. You may do so by implementing the `ShouldBeUnique` interface on your job class. This interface does not require you to define any additional methods on your class:
```


1<?php




2 



3use Illuminate\Contracts\Queue\ShouldQueue;




4use Illuminate\Contracts\Queue\ShouldBeUnique;




5 



6class UpdateSearchIndex implements ShouldQueue, ShouldBeUnique




7{




8    // ...




9}




<?php

use Illuminate\Contracts\Queue\ShouldQueue;
use Illuminate\Contracts\Queue\ShouldBeUnique;

class UpdateSearchIndex implements ShouldQueue, ShouldBeUnique
{
    // ...
}

```

In the example above, the `UpdateSearchIndex` job is unique. So, the job will not be dispatched if another instance of the job is already on the queue and has not finished processing.
In certain cases, you may want to define a specific "key" that makes the job unique or you may want to specify a timeout beyond which the job no longer stays unique. To accomplish this, you may define `uniqueId` and `uniqueFor` properties or methods on your job class:
```


 1<?php




 2 



 3namespace App\Jobs;




 4 



 5use Illuminate\Contracts\Queue\ShouldQueue;




 6use Illuminate\Contracts\Queue\ShouldBeUnique;




 7 



 8class UpdateSearchIndex implements ShouldQueue, ShouldBeUnique




 9{




10    /**




11     * The product instance.




12     *




13     * @var \App\Models\Product




14     */




15    public $product;




16 



17    /**




18     * The number of seconds after which the job's unique lock will be released.




19     *




20     * @var int




21     */




22    public $uniqueFor = 3600;




23 



24    /**




25     * Get the unique ID for the job.




26     */




27    public function uniqueId(): string




28    {




29        return $this->product->id;




30    }




31}




<?php

namespace App\Jobs;

use Illuminate\Contracts\Queue\ShouldQueue;
use Illuminate\Contracts\Queue\ShouldBeUnique;

class UpdateSearchIndex implements ShouldQueue, ShouldBeUnique
{
    /**
     * The product instance.
     *
     * @var \App\Models\Product
     */
    public $product;

    /**
     * The number of seconds after which the job's unique lock will be released.
     *
     * @var int
     */
    public $uniqueFor = 3600;

    /**
     * Get the unique ID for the job.
     */
    public function uniqueId(): string
    {
        return $this->product->id;
    }
}

```

In the example above, the `UpdateSearchIndex` job is unique by a product ID. So, any new dispatches of the job with the same product ID will be ignored until the existing job has completed processing. In addition, if the existing job is not processed within one hour, the unique lock will be released and another job with the same unique key can be dispatched to the queue.
If your application dispatches jobs from multiple web servers or containers, you should ensure that all of your servers are communicating with the same central cache server so that Laravel can accurately determine if a job is unique.
#### [Keeping Jobs Unique Until Processing Begins](https://laravel.com/docs/12.x/queues#keeping-jobs-unique-until-processing-begins)
By default, unique jobs are "unlocked" after a job completes processing or fails all of its retry attempts. However, there may be situations where you would like your job to unlock immediately before it is processed. To accomplish this, your job should implement the `ShouldBeUniqueUntilProcessing` contract instead of the `ShouldBeUnique` contract:
```


1<?php




2 



3use Illuminate\Contracts\Queue\ShouldQueue;




4use Illuminate\Contracts\Queue\ShouldBeUniqueUntilProcessing;




5 



6class UpdateSearchIndex implements ShouldQueue, ShouldBeUniqueUntilProcessing




7{




8    // ...




9}




<?php

use Illuminate\Contracts\Queue\ShouldQueue;
use Illuminate\Contracts\Queue\ShouldBeUniqueUntilProcessing;

class UpdateSearchIndex implements ShouldQueue, ShouldBeUniqueUntilProcessing
{
    // ...
}

```

#### [Unique Job Locks](https://laravel.com/docs/12.x/queues#unique-job-locks)
Behind the scenes, when a `ShouldBeUnique` job is dispatched, Laravel attempts to acquire a [lock](https://laravel.com/docs/12.x/cache#atomic-locks) with the `uniqueId` key. If the lock is already held, the job is not dispatched. This lock is released when the job completes processing or fails all of its retry attempts. By default, Laravel will use the default cache driver to obtain this lock. However, if you wish to use another driver for acquiring the lock, you may define a `uniqueVia` method that returns the cache driver that should be used:
```


 1use Illuminate\Contracts\Cache\Repository;




 2use Illuminate\Support\Facades\Cache;




 3 



 4class UpdateSearchIndex implements ShouldQueue, ShouldBeUnique




 5{




 6    // ...




 7 



 8    /**




 9     * Get the cache driver for the unique job lock.




10     */




11    public function uniqueVia(): Repository




12    {




13        return Cache::driver('redis');




14    }




15}




use Illuminate\Contracts\Cache\Repository;
use Illuminate\Support\Facades\Cache;

class UpdateSearchIndex implements ShouldQueue, ShouldBeUnique
{
    // ...

    /**
     * Get the cache driver for the unique job lock.
     */
    public function uniqueVia(): Repository
    {
        return Cache::driver('redis');
    }
}

```

If you only need to limit the concurrent processing of a job, use the [WithoutOverlapping](https://laravel.com/docs/12.x/queues#preventing-job-overlaps) job middleware instead.
### [Encrypted Jobs](https://laravel.com/docs/12.x/queues#encrypted-jobs)
Laravel allows you to ensure the privacy and integrity of a job's data via [encryption](https://laravel.com/docs/12.x/encryption). To get started, simply add the `ShouldBeEncrypted` interface to the job class. Once this interface has been added to the class, Laravel will automatically encrypt your job before pushing it onto a queue:
```


1<?php




2 



3use Illuminate\Contracts\Queue\ShouldBeEncrypted;




4use Illuminate\Contracts\Queue\ShouldQueue;




5 



6class UpdateSearchIndex implements ShouldQueue, ShouldBeEncrypted




7{




8    // ...




9}




<?php

use Illuminate\Contracts\Queue\ShouldBeEncrypted;
use Illuminate\Contracts\Queue\ShouldQueue;

class UpdateSearchIndex implements ShouldQueue, ShouldBeEncrypted
{
    // ...
}

```
