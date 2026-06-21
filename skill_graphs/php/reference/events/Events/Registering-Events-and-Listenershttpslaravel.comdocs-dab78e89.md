## [Registering Events and Listeners](https://laravel.com/docs/12.x/events#registering-events-and-listeners)
### [Event Discovery](https://laravel.com/docs/12.x/events#event-discovery)
By default, Laravel will automatically find and register your event listeners by scanning your application's `Listeners` directory. When Laravel finds any listener class method that begins with `handle` or `__invoke`, Laravel will register those methods as event listeners for the event that is type-hinted in the method's signature:
```


 1use App\Events\PodcastProcessed;




 2 



 3class SendPodcastNotification




 4{




 5    /**




 6     * Handle the event.




 7     */




 8    public function handle(PodcastProcessed $event): void




 9    {




10        // ...




11    }




12}




use App\Events\PodcastProcessed;

class SendPodcastNotification
{
    /**
     * Handle the event.
     */
    public function handle(PodcastProcessed $event): void
    {
        // ...
    }
}

```

You may listen to multiple events using PHP's union types:
```


1/**




2 * Handle the event.




3 */




4public function handle(PodcastProcessed|PodcastPublished $event): void




5{




6    // ...




7}




/**
 * Handle the event.
 */
public function handle(PodcastProcessed|PodcastPublished $event): void
{
    // ...
}

```

If you plan to store your listeners in a different directory or within multiple directories, you may instruct Laravel to scan those directories using the `withEvents` method in your application's `bootstrap/app.php` file:
```


1->withEvents(discover: [




2    __DIR__.'/../app/Domain/Orders/Listeners',




3])




->withEvents(discover: [
    __DIR__.'/../app/Domain/Orders/Listeners',
])

```

You may scan for listeners in multiple similar directories using the `*` character as a wildcard:
```


1->withEvents(discover: [




2    __DIR__.'/../app/Domain/*/Listeners',




3])




->withEvents(discover: [
    __DIR__.'/../app/Domain/*/Listeners',
])

```

The `event:list` command may be used to list all of the listeners registered within your application:
```


1php artisan event:list




php artisan event:list

```

#### [Event Discovery in Production](https://laravel.com/docs/12.x/events#event-discovery-in-production)
To give your application a speed boost, you should cache a manifest of all of your application's listeners using the `optimize` or `event:cache` Artisan commands. Typically, this command should be run as part of your application's [deployment process](https://laravel.com/docs/12.x/deployment#optimization). This manifest will be used by the framework to speed up the event registration process. The `event:clear` command may be used to destroy the event cache.
### [Manually Registering Events](https://laravel.com/docs/12.x/events#manually-registering-events)
Using the `Event` facade, you may manually register events and their corresponding listeners within the `boot` method of your application's `AppServiceProvider`:
```


 1use App\Domain\Orders\Events\PodcastProcessed;




 2use App\Domain\Orders\Listeners\SendPodcastNotification;




 3use Illuminate\Support\Facades\Event;




 4 



 5/**




 6 * Bootstrap any application services.




 7 */




 8public function boot(): void




 9{




10    Event::listen(




11        PodcastProcessed::class,




12        SendPodcastNotification::class,




13    );




14}




use App\Domain\Orders\Events\PodcastProcessed;
use App\Domain\Orders\Listeners\SendPodcastNotification;
use Illuminate\Support\Facades\Event;

/**
 * Bootstrap any application services.
 */
public function boot(): void
{
    Event::listen(
        PodcastProcessed::class,
        SendPodcastNotification::class,
    );
}

```

The `event:list` command may be used to list all of the listeners registered within your application:
```


1php artisan event:list




php artisan event:list

```

### [Closure Listeners](https://laravel.com/docs/12.x/events#closure-listeners)
Typically, listeners are defined as classes; however, you may also manually register closure-based event listeners in the `boot` method of your application's `AppServiceProvider`:
```


 1use App\Events\PodcastProcessed;




 2use Illuminate\Support\Facades\Event;




 3 



 4/**




 5 * Bootstrap any application services.




 6 */




 7public function boot(): void




 8{




 9    Event::listen(function (PodcastProcessed $event) {




10        // ...




11    });




12}




use App\Events\PodcastProcessed;
use Illuminate\Support\Facades\Event;

/**
 * Bootstrap any application services.
 */
public function boot(): void
{
    Event::listen(function (PodcastProcessed $event) {
        // ...
    });
}

```

#### [Queueable Anonymous Event Listeners](https://laravel.com/docs/12.x/events#queuable-anonymous-event-listeners)
When registering closure-based event listeners, you may wrap the listener closure within the `Illuminate\Events\queueable` function to instruct Laravel to execute the listener using the [queue](https://laravel.com/docs/12.x/queues):
```


 1use App\Events\PodcastProcessed;




 2use function Illuminate\Events\queueable;




 3use Illuminate\Support\Facades\Event;




 4 



 5/**




 6 * Bootstrap any application services.




 7 */




 8public function boot(): void




 9{




10    Event::listen(queueable(function (PodcastProcessed $event) {




11        // ...




12    }));




13}




use App\Events\PodcastProcessed;
use function Illuminate\Events\queueable;
use Illuminate\Support\Facades\Event;

/**
 * Bootstrap any application services.
 */
public function boot(): void
{
    Event::listen(queueable(function (PodcastProcessed $event) {
        // ...
    }));
}

```

Like queued jobs, you may use the `onConnection`, `onQueue`, and `delay` methods to customize the execution of the queued listener:
```


1Event::listen(queueable(function (PodcastProcessed $event) {




2    // ...




3})->onConnection('redis')->onQueue('podcasts')->delay(now()->plus(seconds: 10)));




Event::listen(queueable(function (PodcastProcessed $event) {
    // ...
})->onConnection('redis')->onQueue('podcasts')->delay(now()->plus(seconds: 10)));

```

If you would like to handle anonymous queued listener failures, you may provide a closure to the `catch` method while defining the `queueable` listener. This closure will receive the event instance and the `Throwable` instance that caused the listener's failure:
```


 1use App\Events\PodcastProcessed;




 2use function Illuminate\Events\queueable;




 3use Illuminate\Support\Facades\Event;




 4use Throwable;




 5 



 6Event::listen(queueable(function (PodcastProcessed $event) {




 7    // ...




 8})->catch(function (PodcastProcessed $event, Throwable $e) {




 9    // The queued listener failed...




10}));




use App\Events\PodcastProcessed;
use function Illuminate\Events\queueable;
use Illuminate\Support\Facades\Event;
use Throwable;

Event::listen(queueable(function (PodcastProcessed $event) {
    // ...
})->catch(function (PodcastProcessed $event, Throwable $e) {
    // The queued listener failed...
}));

```

#### [Wildcard Event Listeners](https://laravel.com/docs/12.x/events#wildcard-event-listeners)
You may also register listeners using the `*` character as a wildcard parameter, allowing you to catch multiple events on the same listener. Wildcard listeners receive the event name as their first argument and the entire event data array as their second argument:
```


1Event::listen('event.*', function (string $eventName, array $data) {




2    // ...




3});




Event::listen('event.*', function (string $eventName, array $data) {
    // ...
});

```
