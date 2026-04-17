## [Quickstart](https://laravel.com/docs/12.x/cashier-paddle#quickstart)
### [Selling Products](https://laravel.com/docs/12.x/cashier-paddle#quickstart-selling-products)
Before utilizing Paddle Checkout, you should define Products with fixed prices in your Paddle dashboard. In addition, you should [configure Paddle's webhook handling](https://laravel.com/docs/12.x/cashier-paddle#handling-paddle-webhooks).
Offering product and subscription billing via your application can be intimidating. However, thanks to Cashier and
To charge customers for non-recurring, single-charge products, we'll utilize Cashier to charge customers with Paddle's Checkout Overlay, where they will provide their payment details and confirm their purchase. Once the payment has been made via the Checkout Overlay, the customer will be redirected to a success URL of your choosing within your application:
```


1use Illuminate\Http\Request;




2 



3Route::get('/buy', function (Request $request) {




4    $checkout = $request->user()->checkout('pri_deluxe_album')




5        ->returnTo(route('dashboard'));




6 



7    return view('buy', ['checkout' => $checkout]);




8})->name('checkout');




use Illuminate\Http\Request;

Route::get('/buy', function (Request $request) {
    $checkout = $request->user()->checkout('pri_deluxe_album')
        ->returnTo(route('dashboard'));

    return view('buy', ['checkout' => $checkout]);
})->name('checkout');

```

As you can see in the example above, we will utilize Cashier's provided `checkout` method to create a checkout object to present the customer the Paddle Checkout Overlay for a given "price identifier". When using Paddle, "prices" refer to
If necessary, the `checkout` method will automatically create a customer in Paddle and connect that Paddle customer record to the corresponding user in your application's database. After completing the checkout session, the customer will be redirected to a dedicated success page where you can display an informational message to the customer.
In the `buy` view, we will include a button to display the Checkout Overlay. The `paddle-button` Blade component is included with Cashier Paddle; however, you may also [manually render an overlay checkout](https://laravel.com/docs/12.x/cashier-paddle#manually-rendering-an-overlay-checkout):
```


1<x-paddle-button :checkout="$checkout" class="px-8 py-4">




2    Buy Product




3</x-paddle-button>




<x-paddle-button :checkout="$checkout" class="px-8 py-4">
    Buy Product
</x-paddle-button>

```

#### [Providing Meta Data to Paddle Checkout](https://laravel.com/docs/12.x/cashier-paddle#providing-meta-data-to-paddle-checkout)
When selling products, it's common to keep track of completed orders and purchased products via `Cart` and `Order` models defined by your own application. When redirecting customers to Paddle's Checkout Overlay to complete a purchase, you may need to provide an existing order identifier so that you can associate the completed purchase with the corresponding order when the customer is redirected back to your application.
To accomplish this, you may provide an array of custom data to the `checkout` method. Let's imagine that a pending `Order` is created within our application when a user begins the checkout process. Remember, the `Cart` and `Order` models in this example are illustrative and not provided by Cashier. You are free to implement these concepts based on the needs of your own application:
```


 1use App\Models\Cart;




 2use App\Models\Order;




 3use Illuminate\Http\Request;




 4 



 5Route::get('/cart/{cart}/checkout', function (Request $request, Cart $cart) {




 6    $order = Order::create([




 7        'cart_id' => $cart->id,




 8        'price_ids' => $cart->price_ids,




 9        'status' => 'incomplete',




10    ]);




11 



12    $checkout = $request->user()->checkout($order->price_ids)




13        ->customData(['order_id' => $order->id]);




14 



15    return view('billing', ['checkout' => $checkout]);




16})->name('checkout');




use App\Models\Cart;
use App\Models\Order;
use Illuminate\Http\Request;

Route::get('/cart/{cart}/checkout', function (Request $request, Cart $cart) {
    $order = Order::create([
        'cart_id' => $cart->id,
        'price_ids' => $cart->price_ids,
        'status' => 'incomplete',
    ]);

    $checkout = $request->user()->checkout($order->price_ids)
        ->customData(['order_id' => $order->id]);

    return view('billing', ['checkout' => $checkout]);
})->name('checkout');

```

As you can see in the example above, when a user begins the checkout process, we will provide all of the cart / order's associated Paddle price identifiers to the `checkout` method. Of course, your application is responsible for associating these items with the "shopping cart" or order as a customer adds them. We also provide the order's ID to the Paddle Checkout Overlay via the `customData` method.
Of course, you will likely want to mark the order as "complete" once the customer has finished the checkout process. To accomplish this, you may listen to the webhooks dispatched by Paddle and raised via events by Cashier to store order information in your database.
To get started, listen for the `TransactionCompleted` event dispatched by Cashier. Typically, you should register the event listener in the `boot` method of your application's `AppServiceProvider`:
```


 1use App\Listeners\CompleteOrder;




 2use Illuminate\Support\Facades\Event;




 3use Laravel\Paddle\Events\TransactionCompleted;




 4 



 5/**




 6 * Bootstrap any application services.




 7 */




 8public function boot(): void




 9{




10    Event::listen(TransactionCompleted::class, CompleteOrder::class);




11}




use App\Listeners\CompleteOrder;
use Illuminate\Support\Facades\Event;
use Laravel\Paddle\Events\TransactionCompleted;

/**
 * Bootstrap any application services.
 */
public function boot(): void
{
    Event::listen(TransactionCompleted::class, CompleteOrder::class);
}

```

In this example, the `CompleteOrder` listener might look like the following:
```


 1namespace App\Listeners;




 2 



 3use App\Models\Order;




 4use Laravel\Paddle\Cashier;




 5use Laravel\Paddle\Events\TransactionCompleted;




 6 



 7class CompleteOrder




 8{




 9    /**




10     * Handle the incoming Cashier webhook event.




11     */




12    public function handle(TransactionCompleted $event): void




13    {




14        $orderId = $event->payload['data']['custom_data']['order_id'] ?? null;




15 



16        $order = Order::findOrFail($orderId);




17 



18        $order->update(['status' => 'completed']);




19    }




20}




namespace App\Listeners;

use App\Models\Order;
use Laravel\Paddle\Cashier;
use Laravel\Paddle\Events\TransactionCompleted;

class CompleteOrder
{
    /**
     * Handle the incoming Cashier webhook event.
     */
    public function handle(TransactionCompleted $event): void
    {
        $orderId = $event->payload['data']['custom_data']['order_id'] ?? null;

        $order = Order::findOrFail($orderId);

        $order->update(['status' => 'completed']);
    }
}

```

Please refer to Paddle's documentation for more information on the
### [Selling Subscriptions](https://laravel.com/docs/12.x/cashier-paddle#quickstart-selling-subscriptions)
Before utilizing Paddle Checkout, you should define Products with fixed prices in your Paddle dashboard. In addition, you should [configure Paddle's webhook handling](https://laravel.com/docs/12.x/cashier-paddle#handling-paddle-webhooks).
Offering product and subscription billing via your application can be intimidating. However, thanks to Cashier and
To learn how to sell subscriptions using Cashier and Paddle's Checkout Overlay, let's consider the simple scenario of a subscription service with a basic monthly (`price_basic_monthly`) and yearly (`price_basic_yearly`) plan. These two prices could be grouped under a "Basic" product (`pro_basic`) in our Paddle dashboard. In addition, our subscription service might offer an "Expert" plan as `pro_expert`.
First, let's discover how a customer can subscribe to our services. Of course, you can imagine the customer might click a "subscribe" button for the Basic plan on our application's pricing page. This button will invoke a Paddle Checkout Overlay for their chosen plan. To get started, let's initiate a checkout session via the `checkout` method:
```


1use Illuminate\Http\Request;




2 



3Route::get('/subscribe', function (Request $request) {




4    $checkout = $request->user()->checkout('price_basic_monthly')




5        ->returnTo(route('dashboard'));




6 



7    return view('subscribe', ['checkout' => $checkout]);




8})->name('subscribe');




use Illuminate\Http\Request;

Route::get('/subscribe', function (Request $request) {
    $checkout = $request->user()->checkout('price_basic_monthly')
        ->returnTo(route('dashboard'));

    return view('subscribe', ['checkout' => $checkout]);
})->name('subscribe');

```

In the `subscribe` view, we will include a button to display the Checkout Overlay. The `paddle-button` Blade component is included with Cashier Paddle; however, you may also [manually render an overlay checkout](https://laravel.com/docs/12.x/cashier-paddle#manually-rendering-an-overlay-checkout):
```


1<x-paddle-button :checkout="$checkout" class="px-8 py-4">




2    Subscribe




3</x-paddle-button>




<x-paddle-button :checkout="$checkout" class="px-8 py-4">
    Subscribe
</x-paddle-button>

```

Now, when the Subscribe button is clicked, the customer will be able to enter their payment details and initiate their subscription. To know when their subscription has actually started (since some payment methods require a few seconds to process), you should also [configure Cashier's webhook handling](https://laravel.com/docs/12.x/cashier-paddle#handling-paddle-webhooks).
Now that customers can start subscriptions, we need to restrict certain portions of our application so that only subscribed users can access them. Of course, we can always determine a user's current subscription status via the `subscribed` method provided by Cashier's `Billable` trait:
```


1@if ($user->subscribed())




2    <p>You are subscribed.</p>




3@endif




@if ($user->subscribed())
    <p>You are subscribed.</p>
@endif

```

We can even easily determine if a user is subscribed to specific product or price:
```


1@if ($user->subscribedToProduct('pro_basic'))




2    <p>You are subscribed to our Basic product.</p>




3@endif




4 



5@if ($user->subscribedToPrice('price_basic_monthly'))




6    <p>You are subscribed to our monthly Basic plan.</p>




7@endif




@if ($user->subscribedToProduct('pro_basic'))
    <p>You are subscribed to our Basic product.</p>
@endif

@if ($user->subscribedToPrice('price_basic_monthly'))
    <p>You are subscribed to our monthly Basic plan.</p>
@endif

```

#### [Building a Subscribed Middleware](https://laravel.com/docs/12.x/cashier-paddle#quickstart-building-a-subscribed-middleware)
For convenience, you may wish to create a [middleware](https://laravel.com/docs/12.x/middleware) which determines if the incoming request is from a subscribed user. Once this middleware has been defined, you may easily assign it to a route to prevent users that are not subscribed from accessing the route:
```


 1<?php




 2 



 3namespace App\Http\Middleware;




 4 



 5use Closure;




 6use Illuminate\Http\Request;




 7use Symfony\Component\HttpFoundation\Response;




 8 



 9class Subscribed




10{




11    /**




12     * Handle an incoming request.




13     */




14    public function handle(Request $request, Closure $next): Response




15    {




16        if (! $request->user()?->subscribed()) {




17            // Redirect user to billing page and ask them to subscribe...




18            return redirect('/subscribe');




19        }




20 



21        return $next($request);




22    }




23}




<?php

namespace App\Http\Middleware;

use Closure;
use Illuminate\Http\Request;
use Symfony\Component\HttpFoundation\Response;

class Subscribed
{
    /**
     * Handle an incoming request.
     */
    public function handle(Request $request, Closure $next): Response
    {
        if (! $request->user()?->subscribed()) {
            // Redirect user to billing page and ask them to subscribe...
            return redirect('/subscribe');
        }

        return $next($request);
    }
}

```

Once the middleware has been defined, you may assign it to a route:
```


1use App\Http\Middleware\Subscribed;




2 



3Route::get('/dashboard', function () {




4    // ...




5})->middleware([Subscribed::class]);




use App\Http\Middleware\Subscribed;

Route::get('/dashboard', function () {
    // ...
})->middleware([Subscribed::class]);

```

#### [Allowing Customers to Manage Their Billing Plan](https://laravel.com/docs/12.x/cashier-paddle#quickstart-allowing-customers-to-manage-their-billing-plan)
Of course, customers may want to change their subscription plan to another product or "tier". In our example from above, we'd want to allow the customer to change their plan from a monthly subscription to a yearly subscription. For this you'll need to implement something like a button that leads to the below route:
```


1use Illuminate\Http\Request;




2 



3Route::put('/subscription/{price}/swap', function (Request $request, $price) {




4    $user->subscription()->swap($price); // With "$price" being "price_basic_yearly" for this example.




5 



6    return redirect()->route('dashboard');




7})->name('subscription.swap');




use Illuminate\Http\Request;

Route::put('/subscription/{price}/swap', function (Request $request, $price) {
    $user->subscription()->swap($price); // With "$price" being "price_basic_yearly" for this example.

    return redirect()->route('dashboard');
})->name('subscription.swap');

```

Besides swapping plans you'll also need to allow your customers to cancel their subscription. Like swapping plans, provide a button that leads to the following route:
```


1use Illuminate\Http\Request;




2 



3Route::put('/subscription/cancel', function (Request $request, $price) {




4    $user->subscription()->cancel();




5 



6    return redirect()->route('dashboard');




7})->name('subscription.cancel');




use Illuminate\Http\Request;

Route::put('/subscription/cancel', function (Request $request, $price) {
    $user->subscription()->cancel();

    return redirect()->route('dashboard');
})->name('subscription.cancel');

```

And now your subscription will get canceled at the end of its billing period.
As long as you have configured Cashier's webhook handling, Cashier will automatically keep your application's Cashier-related database tables in sync by inspecting the incoming webhooks from Paddle. So, for example, when you cancel a customer's subscription via Paddle's dashboard, Cashier will receive the corresponding webhook and mark the subscription as "canceled" in your application's database.
