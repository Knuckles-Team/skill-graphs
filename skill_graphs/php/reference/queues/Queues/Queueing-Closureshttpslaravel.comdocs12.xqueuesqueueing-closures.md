## [Queueing Closures](https://laravel.com/docs/12.x/queues#queueing-closures)
Instead of dispatching a job class to the queue, you may also dispatch a closure. This is great for quick, simple tasks that need to be executed outside of the current request cycle. When dispatching closures to the queue, the closure's code content is cryptographically signed so that it cannot be modified in transit:
```


1use App\Models\Podcast;




2 



3$podcast = Podcast::find(1);




4 



5dispatch(function () use ($podcast) {




6    $podcast->publish();




7});




use App\Models\Podcast;

$podcast = Podcast::find(1);

dispatch(function () use ($podcast) {
    $podcast->publish();
});

```

To assign a name to the queued closure which may be used by queue reporting dashboards, as well as be displayed by the `queue:work` command, you may use the `name` method:
```


1dispatch(function () {




2    // ...




3})->name('Publish Podcast');




dispatch(function () {
    // ...
})->name('Publish Podcast');

```

Using the `catch` method, you may provide a closure that should be executed if the queued closure fails to complete successfully after exhausting all of your queue's [configured retry attempts](https://laravel.com/docs/12.x/queues#max-job-attempts-and-timeout):
```


1use Throwable;




2 



3dispatch(function () use ($podcast) {




4    $podcast->publish();




5})->catch(function (Throwable $e) {




6    // This job has failed...




7});




use Throwable;

dispatch(function () use ($podcast) {
    $podcast->publish();
})->catch(function (Throwable $e) {
    // This job has failed...
});

```

Since `catch` callbacks are serialized and executed at a later time by the Laravel queue, you should not use the `$this` variable within `catch` callbacks.
