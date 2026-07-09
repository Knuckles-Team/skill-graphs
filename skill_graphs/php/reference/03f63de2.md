## [Testing](https://laravel.com/docs/12.x/events#testing)
When testing code that dispatches events, you may wish to instruct Laravel to not actually execute the event's listeners, since the listener's code can be tested directly and separately of the code that dispatches the corresponding event. Of course, to test the listener itself, you may instantiate a listener instance and invoke the `handle` method directly in your test.
Using the `Event` facade's `fake` method, you may prevent listeners from executing, execute the code under test, and then assert which events were dispatched by your application using the `assertDispatched`, `assertNotDispatched`, and `assertNothingDispatched` methods:
Pest PHPUnit
```


 1<?php




 2 



 3use App\Events\OrderFailedToShip;




 4use App\Events\OrderShipped;




 5use Illuminate\Support\Facades\Event;




 6 



 7test('orders can be shipped', function () {




 8    Event::fake();




 9 



10    // Perform order shipping...




11 



12    // Assert that an event was dispatched...




13    Event::assertDispatched(OrderShipped::class);




14 



15    // Assert an event was dispatched twice...




16    Event::assertDispatched(OrderShipped::class, 2);




17 



18    // Assert an event was dispatched once...




19    Event::assertDispatchedOnce(OrderShipped::class);




20 



21    // Assert an event was not dispatched...




22    Event::assertNotDispatched(OrderFailedToShip::class);




23 



24    // Assert that no events were dispatched...




25    Event::assertNothingDispatched();




26});




<?php

use App\Events\OrderFailedToShip;
use App\Events\OrderShipped;
use Illuminate\Support\Facades\Event;

test('orders can be shipped', function () {
    Event::fake();

    // Perform order shipping...

    // Assert that an event was dispatched...
    Event::assertDispatched(OrderShipped::class);

    // Assert an event was dispatched twice...
    Event::assertDispatched(OrderShipped::class, 2);

    // Assert an event was dispatched once...
    Event::assertDispatchedOnce(OrderShipped::class);

    // Assert an event was not dispatched...
    Event::assertNotDispatched(OrderFailedToShip::class);

    // Assert that no events were dispatched...
    Event::assertNothingDispatched();
});

```

```


 1<?php




 2 



 3namespace Tests\Feature;




 4 



 5use App\Events\OrderFailedToShip;




 6use App\Events\OrderShipped;




 7use Illuminate\Support\Facades\Event;




 8use Tests\TestCase;




 9 



10class ExampleTest extends TestCase




11{




12    /**




13     * Test order shipping.




14     */




15    public function test_orders_can_be_shipped(): void




16    {




17        Event::fake();




18 



19        // Perform order shipping...




20 



21        // Assert that an event was dispatched...




22        Event::assertDispatched(OrderShipped::class);




23 



24        // Assert an event was dispatched twice...




25        Event::assertDispatched(OrderShipped::class, 2);




26 



27        // Assert an event was dispatched once...




28        Event::assertDispatchedOnce(OrderShipped::class);




29 



30        // Assert an event was not dispatched...




31        Event::assertNotDispatched(OrderFailedToShip::class);




32 



33        // Assert that no events were dispatched...




34        Event::assertNothingDispatched();




35    }




36}




<?php

namespace Tests\Feature;

use App\Events\OrderFailedToShip;
use App\Events\OrderShipped;
use Illuminate\Support\Facades\Event;
use Tests\TestCase;

class ExampleTest extends TestCase
{
    /**
     * Test order shipping.
     */
    public function test_orders_can_be_shipped(): void
    {
        Event::fake();

        // Perform order shipping...

        // Assert that an event was dispatched...
        Event::assertDispatched(OrderShipped::class);

        // Assert an event was dispatched twice...
        Event::assertDispatched(OrderShipped::class, 2);

        // Assert an event was dispatched once...
        Event::assertDispatchedOnce(OrderShipped::class);

        // Assert an event was not dispatched...
        Event::assertNotDispatched(OrderFailedToShip::class);

        // Assert that no events were dispatched...
        Event::assertNothingDispatched();
    }
}

```

You may pass a closure to the `assertDispatched` or `assertNotDispatched` methods in order to assert that an event was dispatched that passes a given "truth test". If at least one event was dispatched that passes the given truth test then the assertion will be successful:
```


1Event::assertDispatched(function (OrderShipped $event) use ($order) {




2    return $event->order->id === $order->id;




3});




Event::assertDispatched(function (OrderShipped $event) use ($order) {
    return $event->order->id === $order->id;
});

```

If you would simply like to assert that an event listener is listening to a given event, you may use the `assertListening` method:
```


1Event::assertListening(




2    OrderShipped::class,




3    SendShipmentNotification::class




4);




Event::assertListening(
    OrderShipped::class,
    SendShipmentNotification::class
);

```

After calling `Event::fake()`, no event listeners will be executed. So, if your tests use model factories that rely on events, such as creating a UUID during a model's `creating` event, you should call `Event::fake()` **after** using your factories.
### [Faking a Subset of Events](https://laravel.com/docs/12.x/events#faking-a-subset-of-events)
If you only want to fake event listeners for a specific set of events, you may pass them to the `fake` or `fakeFor` method:
Pest PHPUnit
```


 1test('orders can be processed', function () {




 2    Event::fake([




 3        OrderCreated::class,




 4    ]);




 5 



 6    $order = Order::factory()->create();




 7 



 8    Event::assertDispatched(OrderCreated::class);




 9 



10    // Other events are dispatched as normal...




11    $order->update([




12        // ...




13    ]);




14});




test('orders can be processed', function () {
    Event::fake([
        OrderCreated::class,
    ]);

    $order = Order::factory()->create();

    Event::assertDispatched(OrderCreated::class);

    // Other events are dispatched as normal...
    $order->update([
        // ...
    ]);
});

```

```


 1/**




 2 * Test order process.




 3 */




 4public function test_orders_can_be_processed(): void




 5{




 6    Event::fake([




 7        OrderCreated::class,




 8    ]);




 9 



10    $order = Order::factory()->create();




11 



12    Event::assertDispatched(OrderCreated::class);




13 



14    // Other events are dispatched as normal...




15    $order->update([




16        // ...




17    ]);




18}




/**
 * Test order process.
 */
public function test_orders_can_be_processed(): void
{
    Event::fake([
        OrderCreated::class,
    ]);

    $order = Order::factory()->create();

    Event::assertDispatched(OrderCreated::class);

    // Other events are dispatched as normal...
    $order->update([
        // ...
    ]);
}

```

You may fake all events except for a set of specified events using the `except` method:
```


1Event::fake()->except([




2    OrderCreated::class,




3]);




Event::fake()->except([
    OrderCreated::class,
]);

```

### [Scoped Event Fakes](https://laravel.com/docs/12.x/events#scoped-event-fakes)
If you only want to fake event listeners for a portion of your test, you may use the `fakeFor` method:
Pest PHPUnit
```


 1<?php




 2 



 3use App\Events\OrderCreated;




 4use App\Models\Order;




 5use Illuminate\Support\Facades\Event;




 6 



 7test('orders can be processed', function () {




 8    $order = Event::fakeFor(function () {




 9        $order = Order::factory()->create();




10 



11        Event::assertDispatched(OrderCreated::class);




12 



13        return $order;




14    });




15 



16    // Events are dispatched as normal and observers will run...




17    $order->update([




18        // ...




19    ]);




20});




<?php

use App\Events\OrderCreated;
use App\Models\Order;
use Illuminate\Support\Facades\Event;

test('orders can be processed', function () {
    $order = Event::fakeFor(function () {
        $order = Order::factory()->create();

        Event::assertDispatched(OrderCreated::class);

        return $order;
    });

    // Events are dispatched as normal and observers will run...
    $order->update([
        // ...
    ]);
});

```

```


 1<?php




 2 



 3namespace Tests\Feature;




 4 



 5use App\Events\OrderCreated;




 6use App\Models\Order;




 7use Illuminate\Support\Facades\Event;




 8use Tests\TestCase;




 9 



10class ExampleTest extends TestCase




11{




12    /**




13     * Test order process.




14     */




15    public function test_orders_can_be_processed(): void




16    {




17        $order = Event::fakeFor(function () {




18            $order = Order::factory()->create();




19 



20            Event::assertDispatched(OrderCreated::class);




21 



22            return $order;




23        });




24 



25        // Events are dispatched as normal and observers will run...




26        $order->update([




27            // ...




28        ]);




29    }




30}




<?php

namespace Tests\Feature;

use App\Events\OrderCreated;
use App\Models\Order;
use Illuminate\Support\Facades\Event;
use Tests\TestCase;

class ExampleTest extends TestCase
{
    /**
     * Test order process.
     */
    public function test_orders_can_be_processed(): void
    {
        $order = Event::fakeFor(function () {
            $order = Order::factory()->create();

            Event::assertDispatched(OrderCreated::class);

            return $order;
        });

        // Events are dispatched as normal and observers will run...
        $order->update([
            // ...
        ]);
    }
}

```

Copy as markdown
  * [ Introduction ](https://laravel.com/docs/12.x/events#introduction)
  * [ Generating Events and Listeners ](https://laravel.com/docs/12.x/events#generating-events-and-listeners)
  * [ Registering Events and Listeners ](https://laravel.com/docs/12.x/events#registering-events-and-listeners)
    * [ Event Discovery ](https://laravel.com/docs/12.x/events#event-discovery)
    * [ Manually Registering Events ](https://laravel.com/docs/12.x/events#manually-registering-events)
    * [ Closure Listeners ](https://laravel.com/docs/12.x/events#closure-listeners)
  * [ Defining Events ](https://laravel.com/docs/12.x/events#defining-events)
  * [ Defining Listeners ](https://laravel.com/docs/12.x/events#defining-listeners)
  * [ Queued Event Listeners ](https://laravel.com/docs/12.x/events#queued-event-listeners)
    * [ Manually Interacting With the Queue ](https://laravel.com/docs/12.x/events#manually-interacting-with-the-queue)
    * [ Queued Event Listeners and Database Transactions ](https://laravel.com/docs/12.x/events#queued-event-listeners-and-database-transactions)
    * [ Queued Listener Middleware ](https://laravel.com/docs/12.x/events#queued-listener-middleware)
    * [ Encrypted Queued Listeners ](https://laravel.com/docs/12.x/events#encrypted-queued-listeners)
    * [ Unique Event Listeners ](https://laravel.com/docs/12.x/events#unique-event-listeners)
    * [ Keeping Listeners Unique Until Processing Begins ](https://laravel.com/docs/12.x/events#keeping-listeners-unique-until-processing-begins)
    * [ Unique Listener Locks ](https://laravel.com/docs/12.x/events#unique-listener-locks)
    * [ Handling Failed Jobs ](https://laravel.com/docs/12.x/events#handling-failed-jobs)
  * [ Dispatching Events ](https://laravel.com/docs/12.x/events#dispatching-events)
    * [ Dispatching Events After Database Transactions ](https://laravel.com/docs/12.x/events#dispatching-events-after-database-transactions)
    * [ Deferring Events ](https://laravel.com/docs/12.x/events#deferring-events)
  * [ Event Subscribers ](https://laravel.com/docs/12.x/events#event-subscribers)
    * [ Writing Event Subscribers ](https://laravel.com/docs/12.x/events#writing-event-subscribers)
    * [ Registering Event Subscribers ](https://laravel.com/docs/12.x/events#registering-event-subscribers)
  * [ Testing ](https://laravel.com/docs/12.x/events#testing)
    * [ Faking a Subset of Events ](https://laravel.com/docs/12.x/events#faking-a-subset-of-events)
    * [ Scoped Events Fakes ](https://laravel.com/docs/12.x/events#scoped-event-fakes)


[ ![Laravel Forge](https://laravel.com/images/ads/forge-logo.svg) Server management made simple for any PHP app Learn more  ](https://forge.laravel.com)
[ ![Laravel Cloud](https://laravel.com/images/ads/cloud-logo.svg) The fastest way to deploy and scale Laravel apps Learn more  ](https://cloud.laravel.com)
[ ![Laravel Nightwatch](https://laravel.com/images/ads/nightwatch-logo.svg) First-class monitoring and deep insights for Laravel apps Learn more  ](https://nightwatch.laravel.com)
[ ![Laravel Boost](https://laravel.com/images/ads/boost-logo.svg) Supercharge your AI development with essential context Learn more  ](https://laravel.com/ai/boost)
Laravel is the most productive way to
build, deploy, and monitor software.
  * © 2026 Laravel
  * [ Legal ](https://laravel.com/legal)
  * [ Status ](https://status.laravel.com/)


####  Products
  * [ Cloud ](https://cloud.laravel.com)
  * [ Forge ](https://forge.laravel.com)
  * [ Nightwatch ](https://nightwatch.laravel.com)
  * [ Vapor ](https://vapor.laravel.com)
  * [ Nova ](https://nova.laravel.com)


####  Packages
  * [ Cashier ](https://laravel.com/docs/cashier)
  * [ Dusk ](https://laravel.com/docs/dusk)
  * [ Horizon ](https://laravel.com/docs/horizon)
  * [ Octane ](https://laravel.com/docs/octane)
  * [ Scout ](https://laravel.com/docs/scout)
  * [ Pennant ](https://laravel.com/docs/pennant)
  * [ Pint ](https://laravel.com/docs/pint)
  * [ Sail ](https://laravel.com/docs/sail)
  * [ Sanctum ](https://laravel.com/docs/sanctum)
  * [ Socialite ](https://laravel.com/docs/socialite)
  * [ Telescope ](https://laravel.com/docs/telescope)
  * [ Pulse ](https://laravel.com/docs/pulse)
  * [ Reverb ](https://laravel.com/docs/reverb)
  * [ Echo ](https://laravel.com/docs/broadcasting)


####  Resources
  * [ Documentation ](https://laravel.com/docs)
  * [ Starter Kits ](https://laravel.com/starter-kits)
  * [ Release Notes ](https://laravel.com/docs/releases)
  * [ Blog ](https://laravel.com/blog)
  * [ Community ](https://laravel.com/community)
  * [ Learn ](https://laravel.com/learn)
  * [ Careers ](https://laravel.com/careers)
  * [ Trust ](https://trust.laravel.com)


####  Partners
  *   * [Tighten](https://partners.laravel.com/partners/tighten)
  * [byte5](https://partners.laravel.com/partners/byte5)
  * [Jump24](https://partners.laravel.com/partners/jump24)
  * [Kirschbaum](https://partners.laravel.com/partners/kirschbaum)
  * [Active Logic](https://partners.laravel.com/partners/active-logic)
  * [Vehikl](https://partners.laravel.com/partners/vehikl)
  * [Redberry](https://partners.laravel.com/partners/redberry)
  * [Curotec](https://partners.laravel.com/partners/curotec)
  * [ More Partners ](https://partners.laravel.com)
