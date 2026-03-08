## [Testing](https://laravel.com/docs/12.x/queues#testing)
When testing code that dispatches jobs, you may wish to instruct Laravel to not actually execute the job itself, since the job's code can be tested directly and separately of the code that dispatches it. Of course, to test the job itself, you may instantiate a job instance and invoke the `handle` method directly in your test.
You may use the `Queue` facade's `fake` method to prevent queued jobs from actually being pushed to the queue. After calling the `Queue` facade's `fake` method, you may then assert that the application attempted to push jobs to the queue:
Pest PHPUnit
```


 1<?php




 2 



 3use App\Jobs\AnotherJob;




 4use App\Jobs\ShipOrder;




 5use Illuminate\Support\Facades\Queue;




 6 



 7test('orders can be shipped', function () {




 8    Queue::fake();




 9 



10    // Perform order shipping...




11 



12    // Assert that no jobs were pushed...




13    Queue::assertNothingPushed();




14 



15    // Assert a job was pushed to a given queue...




16    Queue::assertPushedOn('queue-name', ShipOrder::class);




17 



18    // Assert a job was pushed




19    Queue::assertPushed(ShipOrder::class);




20 



21    // Assert a job was pushed twice...




22    Queue::assertPushedTimes(ShipOrder::class, 2);




23 



24    // Assert a job was not pushed...




25    Queue::assertNotPushed(AnotherJob::class);




26 



27    // Assert that a closure was pushed to the queue...




28    Queue::assertClosurePushed();




29 



30    // Assert that a closure was not pushed...




31    Queue::assertClosureNotPushed();




32 



33    // Assert the total number of jobs that were pushed...




34    Queue::assertCount(3);




35});




<?php

use App\Jobs\AnotherJob;
use App\Jobs\ShipOrder;
use Illuminate\Support\Facades\Queue;

test('orders can be shipped', function () {
    Queue::fake();

    // Perform order shipping...

    // Assert that no jobs were pushed...
    Queue::assertNothingPushed();

    // Assert a job was pushed to a given queue...
    Queue::assertPushedOn('queue-name', ShipOrder::class);

    // Assert a job was pushed
    Queue::assertPushed(ShipOrder::class);

    // Assert a job was pushed twice...
    Queue::assertPushedTimes(ShipOrder::class, 2);

    // Assert a job was not pushed...
    Queue::assertNotPushed(AnotherJob::class);

    // Assert that a closure was pushed to the queue...
    Queue::assertClosurePushed();

    // Assert that a closure was not pushed...
    Queue::assertClosureNotPushed();

    // Assert the total number of jobs that were pushed...
    Queue::assertCount(3);
});

```

```


 1<?php




 2 



 3namespace Tests\Feature;




 4 



 5use App\Jobs\AnotherJob;




 6use App\Jobs\ShipOrder;




 7use Illuminate\Support\Facades\Queue;




 8use Tests\TestCase;




 9 



10class ExampleTest extends TestCase




11{




12    public function test_orders_can_be_shipped(): void




13    {




14        Queue::fake();




15 



16        // Perform order shipping...




17 



18        // Assert that no jobs were pushed...




19        Queue::assertNothingPushed();




20 



21        // Assert a job was pushed to a given queue...




22        Queue::assertPushedOn('queue-name', ShipOrder::class);




23 



24        // Assert a job was pushed




25        Queue::assertPushed(ShipOrder::class);




26 



27        // Assert a job was pushed twice...




28        Queue::assertPushedTimes(ShipOrder::class, 2);




29 



30        // Assert a job was not pushed...




31        Queue::assertNotPushed(AnotherJob::class);




32 



33        // Assert that a closure was pushed to the queue...




34        Queue::assertClosurePushed();




35 



36        // Assert that a closure was not pushed...




37        Queue::assertClosureNotPushed();




38 



39        // Assert the total number of jobs that were pushed...




40        Queue::assertCount(3);




41    }




42}




<?php

namespace Tests\Feature;

use App\Jobs\AnotherJob;
use App\Jobs\ShipOrder;
use Illuminate\Support\Facades\Queue;
use Tests\TestCase;

class ExampleTest extends TestCase
{
    public function test_orders_can_be_shipped(): void
    {
        Queue::fake();

        // Perform order shipping...

        // Assert that no jobs were pushed...
        Queue::assertNothingPushed();

        // Assert a job was pushed to a given queue...
        Queue::assertPushedOn('queue-name', ShipOrder::class);

        // Assert a job was pushed
        Queue::assertPushed(ShipOrder::class);

        // Assert a job was pushed twice...
        Queue::assertPushedTimes(ShipOrder::class, 2);

        // Assert a job was not pushed...
        Queue::assertNotPushed(AnotherJob::class);

        // Assert that a closure was pushed to the queue...
        Queue::assertClosurePushed();

        // Assert that a closure was not pushed...
        Queue::assertClosureNotPushed();

        // Assert the total number of jobs that were pushed...
        Queue::assertCount(3);
    }
}

```

You may pass a closure to the `assertPushed`, `assertNotPushed`, `assertClosurePushed`, or `assertClosureNotPushed` methods in order to assert that a job was pushed that passes a given "truth test". If at least one job was pushed that passes the given truth test then the assertion will be successful:
```


1use Illuminate\Queue\CallQueuedClosure;




2 



3Queue::assertPushed(function (ShipOrder $job) use ($order) {




4    return $job->order->id === $order->id;




5});




6 



7Queue::assertClosurePushed(function (CallQueuedClosure $job) {




8    return $job->name === 'validate-order';




9});




use Illuminate\Queue\CallQueuedClosure;

Queue::assertPushed(function (ShipOrder $job) use ($order) {
    return $job->order->id === $order->id;
});

Queue::assertClosurePushed(function (CallQueuedClosure $job) {
    return $job->name === 'validate-order';
});

```

### [Faking a Subset of Jobs](https://laravel.com/docs/12.x/queues#faking-a-subset-of-jobs)
If you only need to fake specific jobs while allowing your other jobs to execute normally, you may pass the class names of the jobs that should be faked to the `fake` method:
Pest PHPUnit
```


 1test('orders can be shipped', function () {




 2    Queue::fake([




 3        ShipOrder::class,




 4    ]);




 5 



 6    // Perform order shipping...




 7 



 8    // Assert a job was pushed twice...




 9    Queue::assertPushedTimes(ShipOrder::class, 2);




10});




test('orders can be shipped', function () {
    Queue::fake([
        ShipOrder::class,
    ]);

    // Perform order shipping...

    // Assert a job was pushed twice...
    Queue::assertPushedTimes(ShipOrder::class, 2);
});

```

```


 1public function test_orders_can_be_shipped(): void




 2{




 3    Queue::fake([




 4        ShipOrder::class,




 5    ]);




 6 



 7    // Perform order shipping...




 8 



 9    // Assert a job was pushed twice...




10    Queue::assertPushedTimes(ShipOrder::class, 2);




11}




public function test_orders_can_be_shipped(): void
{
    Queue::fake([
        ShipOrder::class,
    ]);

    // Perform order shipping...

    // Assert a job was pushed twice...
    Queue::assertPushedTimes(ShipOrder::class, 2);
}

```

You may fake all jobs except for a set of specified jobs using the `except` method:
```


1Queue::fake()->except([




2    ShipOrder::class,




3]);




Queue::fake()->except([
    ShipOrder::class,
]);

```

### [Testing Job Chains](https://laravel.com/docs/12.x/queues#testing-job-chains)
To test job chains, you will need to utilize the `Bus` facade's faking capabilities. The `Bus` facade's `assertChained` method may be used to assert that a [chain of jobs](https://laravel.com/docs/12.x/queues#job-chaining) was dispatched. The `assertChained` method accepts an array of chained jobs as its first argument:
```


 1use App\Jobs\RecordShipment;




 2use App\Jobs\ShipOrder;




 3use App\Jobs\UpdateInventory;




 4use Illuminate\Support\Facades\Bus;




 5 



 6Bus::fake();




 7 



 8// ...




 9 



10Bus::assertChained([




11    ShipOrder::class,




12    RecordShipment::class,




13    UpdateInventory::class




14]);




use App\Jobs\RecordShipment;
use App\Jobs\ShipOrder;
use App\Jobs\UpdateInventory;
use Illuminate\Support\Facades\Bus;

Bus::fake();

// ...

Bus::assertChained([
    ShipOrder::class,
    RecordShipment::class,
    UpdateInventory::class
]);

```

As you can see in the example above, the array of chained jobs may be an array of the job's class names. However, you may also provide an array of actual job instances. When doing so, Laravel will ensure that the job instances are of the same class and have the same property values of the chained jobs dispatched by your application:
```


1Bus::assertChained([




2    new ShipOrder,




3    new RecordShipment,




4    new UpdateInventory,




5]);




Bus::assertChained([
    new ShipOrder,
    new RecordShipment,
    new UpdateInventory,
]);

```

You may use the `assertDispatchedWithoutChain` method to assert that a job was pushed without a chain of jobs:
```


1Bus::assertDispatchedWithoutChain(ShipOrder::class);




Bus::assertDispatchedWithoutChain(ShipOrder::class);

```

#### [Testing Chain Modifications](https://laravel.com/docs/12.x/queues#testing-chain-modifications)
If a chained job [prepends or appends jobs to an existing chain](https://laravel.com/docs/12.x/queues#adding-jobs-to-the-chain), you may use the job's `assertHasChain` method to assert that the job has the expected chain of remaining jobs:
```


1$job = new ProcessPodcast;




2 



3$job->handle();




4 



5$job->assertHasChain([




6    new TranscribePodcast,




7    new OptimizePodcast,




8    new ReleasePodcast,




9]);




$job = new ProcessPodcast;

$job->handle();

$job->assertHasChain([
    new TranscribePodcast,
    new OptimizePodcast,
    new ReleasePodcast,
]);

```

The `assertDoesntHaveChain` method may be used to assert that the job's remaining chain is empty:
```


1$job->assertDoesntHaveChain();




$job->assertDoesntHaveChain();

```

#### [Testing Chained Batches](https://laravel.com/docs/12.x/queues#testing-chained-batches)
If your job chain [contains a batch of jobs](https://laravel.com/docs/12.x/queues#chains-and-batches), you may assert that the chained batch matches your expectations by inserting a `Bus::chainedBatch` definition within your chain assertion:
```


 1use App\Jobs\ShipOrder;




 2use App\Jobs\UpdateInventory;




 3use Illuminate\Bus\PendingBatch;




 4use Illuminate\Support\Facades\Bus;




 5 



 6Bus::assertChained([




 7    new ShipOrder,




 8    Bus::chainedBatch(function (PendingBatch $batch) {




 9        return $batch->jobs->count() === 3;




10    }),




11    new UpdateInventory,




12]);




use App\Jobs\ShipOrder;
use App\Jobs\UpdateInventory;
use Illuminate\Bus\PendingBatch;
use Illuminate\Support\Facades\Bus;

Bus::assertChained([
    new ShipOrder,
    Bus::chainedBatch(function (PendingBatch $batch) {
        return $batch->jobs->count() === 3;
    }),
    new UpdateInventory,
]);

```

### [Testing Job Batches](https://laravel.com/docs/12.x/queues#testing-job-batches)
The `Bus` facade's `assertBatched` method may be used to assert that a [batch of jobs](https://laravel.com/docs/12.x/queues#job-batching) was dispatched. The closure given to the `assertBatched` method receives an instance of `Illuminate\Bus\PendingBatch`, which may be used to inspect the jobs within the batch:
```


 1use Illuminate\Bus\PendingBatch;




 2use Illuminate\Support\Facades\Bus;




 3 



 4Bus::fake();




 5 



 6// ...




 7 



 8Bus::assertBatched(function (PendingBatch $batch) {




 9    return $batch->name == 'Import CSV' &&




10           $batch->jobs->count() === 10;




11});




use Illuminate\Bus\PendingBatch;
use Illuminate\Support\Facades\Bus;

Bus::fake();

// ...

Bus::assertBatched(function (PendingBatch $batch) {
    return $batch->name == 'Import CSV' &&
           $batch->jobs->count() === 10;
});

```

The `hasJobs` method may be used on the pending batch to verify that the batch contains the expected jobs. The method accepts an array of job instances, class names, or closures:
```


1Bus::assertBatched(function (PendingBatch $batch) {




2    return $batch->hasJobs([




3        new ProcessCsvRow(row: 1),




4        new ProcessCsvRow(row: 2),




5        new ProcessCsvRow(row: 3),




6    ]);




7});




Bus::assertBatched(function (PendingBatch $batch) {
    return $batch->hasJobs([
        new ProcessCsvRow(row: 1),
        new ProcessCsvRow(row: 2),
        new ProcessCsvRow(row: 3),
    ]);
});

```

When using closures, the closure will receive the job instance. The expected job type will be inferred from the closure's type hint:
```


1Bus::assertBatched(function (PendingBatch $batch) {




2    return $batch->hasJobs([




3        fn (ProcessCsvRow $job) => $job->row === 1,




4        fn (ProcessCsvRow $job) => $job->row === 2,




5        fn (ProcessCsvRow $job) => $job->row === 3,




6    ]);




7});




Bus::assertBatched(function (PendingBatch $batch) {
    return $batch->hasJobs([
        fn (ProcessCsvRow $job) => $job->row === 1,
        fn (ProcessCsvRow $job) => $job->row === 2,
        fn (ProcessCsvRow $job) => $job->row === 3,
    ]);
});

```

You may use the `assertBatchCount` method to assert that a given number of batches were dispatched:
```


1Bus::assertBatchCount(3);




Bus::assertBatchCount(3);

```

You may use `assertNothingBatched` to assert that no batches were dispatched:
```


1Bus::assertNothingBatched();




Bus::assertNothingBatched();

```

#### [Testing Job / Batch Interaction](https://laravel.com/docs/12.x/queues#testing-job-batch-interaction)
In addition, you may occasionally need to test an individual job's interaction with its underlying batch. For example, you may need to test if a job cancelled further processing for its batch. To accomplish this, you need to assign a fake batch to the job via the `withFakeBatch` method. The `withFakeBatch` method returns a tuple containing the job instance and the fake batch:
```


1[$job, $batch] = (new ShipOrder)->withFakeBatch();




2 



3$job->handle();




4 



5$this->assertTrue($batch->cancelled());




6$this->assertEmpty($batch->added);




[$job, $batch] = (new ShipOrder)->withFakeBatch();

$job->handle();

$this->assertTrue($batch->cancelled());
$this->assertEmpty($batch->added);

```

### [Testing Job / Queue Interactions](https://laravel.com/docs/12.x/queues#testing-job-queue-interactions)
Sometimes, you may need to test that a queued job [releases itself back onto the queue](https://laravel.com/docs/12.x/queues#manually-releasing-a-job). Or, you may need to test that the job deleted itself. You may test these queue interactions by instantiating the job and invoking the `withFakeQueueInteractions` method.
Once the job's queue interactions have been faked, you may invoke the `handle` method on the job. After invoking the job, various assertion methods are available to verify the job's queue interactions:
```


 1use App\Exceptions\CorruptedAudioException;




 2use App\Jobs\ProcessPodcast;




 3 



 4$job = (new ProcessPodcast)->withFakeQueueInteractions();




 5 



 6$job->handle();




 7 



 8$job->assertReleased(delay: 30);




 9$job->assertDeleted();




10$job->assertNotDeleted();




11$job->assertFailed();




12$job->assertFailedWith(CorruptedAudioException::class);




13$job->assertNotFailed();




use App\Exceptions\CorruptedAudioException;
use App\Jobs\ProcessPodcast;

$job = (new ProcessPodcast)->withFakeQueueInteractions();

$job->handle();

$job->assertReleased(delay: 30);
$job->assertDeleted();
$job->assertNotDeleted();
$job->assertFailed();
$job->assertFailedWith(CorruptedAudioException::class);
$job->assertNotFailed();

```
