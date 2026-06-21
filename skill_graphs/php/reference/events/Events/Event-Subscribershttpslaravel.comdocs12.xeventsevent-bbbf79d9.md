## [Event Subscribers](https://laravel.com/docs/12.x/events#event-subscribers)
### [Writing Event Subscribers](https://laravel.com/docs/12.x/events#writing-event-subscribers)
Event subscribers are classes that may subscribe to multiple events from within the subscriber class itself, allowing you to define several event handlers within a single class. Subscribers should define a `subscribe` method, which receives an event dispatcher instance. You may call the `listen` method on the given dispatcher to register event listeners:
```


 1<?php




 2 



 3namespace App\Listeners;




 4 



 5use Illuminate\Auth\Events\Login;




 6use Illuminate\Auth\Events\Logout;




 7use Illuminate\Events\Dispatcher;




 8 



 9class UserEventSubscriber




10{




11    /**




12     * Handle user login events.




13     */




14    public function handleUserLogin(Login $event): void {}




15 



16    /**




17     * Handle user logout events.




18     */




19    public function handleUserLogout(Logout $event): void {}




20 



21    /**




22     * Register the listeners for the subscriber.




23     */




24    public function subscribe(Dispatcher $events): void




25    {




26        $events->listen(




27            Login::class,




28            [UserEventSubscriber::class, 'handleUserLogin']




29        );




30 



31        $events->listen(




32            Logout::class,




33            [UserEventSubscriber::class, 'handleUserLogout']




34        );




35    }




36}




<?php

namespace App\Listeners;

use Illuminate\Auth\Events\Login;
use Illuminate\Auth\Events\Logout;
use Illuminate\Events\Dispatcher;

class UserEventSubscriber
{
    /**
     * Handle user login events.
     */
    public function handleUserLogin(Login $event): void {}

    /**
     * Handle user logout events.
     */
    public function handleUserLogout(Logout $event): void {}

    /**
     * Register the listeners for the subscriber.
     */
    public function subscribe(Dispatcher $events): void
    {
        $events->listen(
            Login::class,
            [UserEventSubscriber::class, 'handleUserLogin']
        );

        $events->listen(
            Logout::class,
            [UserEventSubscriber::class, 'handleUserLogout']
        );
    }
}

```

If your event listener methods are defined within the subscriber itself, you may find it more convenient to return an array of events and method names from the subscriber's `subscribe` method. Laravel will automatically determine the subscriber's class name when registering the event listeners:
```


 1<?php




 2 



 3namespace App\Listeners;




 4 



 5use Illuminate\Auth\Events\Login;




 6use Illuminate\Auth\Events\Logout;




 7use Illuminate\Events\Dispatcher;




 8 



 9class UserEventSubscriber




10{




11    /**




12     * Handle user login events.




13     */




14    public function handleUserLogin(Login $event): void {}




15 



16    /**




17     * Handle user logout events.




18     */




19    public function handleUserLogout(Logout $event): void {}




20 



21    /**




22     * Register the listeners for the subscriber.




23     *




24     * @return array<string, string>




25     */




26    public function subscribe(Dispatcher $events): array




27    {




28        return [




29            Login::class => 'handleUserLogin',




30            Logout::class => 'handleUserLogout',




31        ];




32    }




33}




<?php

namespace App\Listeners;

use Illuminate\Auth\Events\Login;
use Illuminate\Auth\Events\Logout;
use Illuminate\Events\Dispatcher;

class UserEventSubscriber
{
    /**
     * Handle user login events.
     */
    public function handleUserLogin(Login $event): void {}

    /**
     * Handle user logout events.
     */
    public function handleUserLogout(Logout $event): void {}

    /**
     * Register the listeners for the subscriber.
     *
     * @return array<string, string>
     */
    public function subscribe(Dispatcher $events): array
    {
        return [
            Login::class => 'handleUserLogin',
            Logout::class => 'handleUserLogout',
        ];
    }
}

```

### [Registering Event Subscribers](https://laravel.com/docs/12.x/events#registering-event-subscribers)
After writing the subscriber, Laravel will automatically register handler methods within the subscriber if they follow Laravel's [event discovery conventions](https://laravel.com/docs/12.x/events#event-discovery). Otherwise, you may manually register your subscriber using the `subscribe` method of the `Event` facade. Typically, this should be done within the `boot` method of your application's `AppServiceProvider`:
```


 1<?php




 2 



 3namespace App\Providers;




 4 



 5use App\Listeners\UserEventSubscriber;




 6use Illuminate\Support\Facades\Event;




 7use Illuminate\Support\ServiceProvider;




 8 



 9class AppServiceProvider extends ServiceProvider




10{




11    /**




12     * Bootstrap any application services.




13     */




14    public function boot(): void




15    {




16        Event::subscribe(UserEventSubscriber::class);




17    }




18}




<?php

namespace App\Providers;

use App\Listeners\UserEventSubscriber;
use Illuminate\Support\Facades\Event;
use Illuminate\Support\ServiceProvider;

class AppServiceProvider extends ServiceProvider
{
    /**
     * Bootstrap any application services.
     */
    public function boot(): void
    {
        Event::subscribe(UserEventSubscriber::class);
    }
}

```
