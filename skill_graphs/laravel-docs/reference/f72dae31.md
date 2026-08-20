## [Quickstart](https://laravel.com/docs/12.x/billing#quickstart)
### [Selling Products](https://laravel.com/docs/12.x/billing#quickstart-selling-products)
Before utilizing Stripe Checkout, you should define Products with fixed prices in your Stripe dashboard. In addition, you should [configure Cashier's webhook handling](https://laravel.com/docs/12.x/billing#handling-stripe-webhooks).
Offering product and subscription billing via your application can be intimidating. However, thanks to Cashier and
To charge customers for non-recurring, single-charge products, we'll utilize Cashier to direct customers to Stripe Checkout, where they will provide their payment details and confirm their purchase. Once the payment has been made via Checkout, the customer will be redirected to a success URL of your choosing within your application:
```


 1use Illuminate\Http\Request;




 2 



 3Route::get('/checkout', function (Request $request) {




 4    $stripePriceId = 'price_deluxe_album';




 5 



 6    $quantity = 1;




 7 



 8    return $request->user()->checkout([$stripePriceId => $quantity], [




 9        'success_url' => route('checkout-success'),




10        'cancel_url' => route('checkout-cancel'),




11    ]);




12})->name('checkout');




13 



14Route::view('/checkout/success', 'checkout.success')->name('checkout-success');




15Route::view('/checkout/cancel', 'checkout.cancel')->name('checkout-cancel');




use Illuminate\Http\Request;

Route::get('/checkout', function (Request $request) {
    $stripePriceId = 'price_deluxe_album';

    $quantity = 1;

    return $request->user()->checkout([$stripePriceId => $quantity], [
        'success_url' => route('checkout-success'),
        'cancel_url' => route('checkout-cancel'),
    ]);
})->name('checkout');

Route::view('/checkout/success', 'checkout.success')->name('checkout-success');
Route::view('/checkout/cancel', 'checkout.cancel')->name('checkout-cancel');

```

As you can see in the example above, we will utilize Cashier's provided `checkout` method to redirect the customer to Stripe Checkout for a given "price identifier". When using Stripe, "prices" refer to
If necessary, the `checkout` method will automatically create a customer in Stripe and connect that Stripe customer record to the corresponding user in your application's database. After completing the checkout session, the customer will be redirected to a dedicated success or cancellation page where you can display an informational message to the customer.
#### [Providing Meta Data to Stripe Checkout](https://laravel.com/docs/12.x/billing#providing-meta-data-to-stripe-checkout)
When selling products, it's common to keep track of completed orders and purchased products via `Cart` and `Order` models defined by your own application. When redirecting customers to Stripe Checkout to complete a purchase, you may need to provide an existing order identifier so that you can associate the completed purchase with the corresponding order when the customer is redirected back to your application.
To accomplish this, you may provide an array of `metadata` to the `checkout` method. Let's imagine that a pending `Order` is created within our application when a user begins the checkout process. Remember, the `Cart` and `Order` models in this example are illustrative and not provided by Cashier. You are free to implement these concepts based on the needs of your own application:
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



12    return $request->user()->checkout($order->price_ids, [




13        'success_url' => route('checkout-success').'?session_id={CHECKOUT_SESSION_ID}',




14        'cancel_url' => route('checkout-cancel'),




15        'metadata' => ['order_id' => $order->id],




16    ]);




17})->name('checkout');




use App\Models\Cart;
use App\Models\Order;
use Illuminate\Http\Request;

Route::get('/cart/{cart}/checkout', function (Request $request, Cart $cart) {
    $order = Order::create([
        'cart_id' => $cart->id,
        'price_ids' => $cart->price_ids,
        'status' => 'incomplete',
    ]);

    return $request->user()->checkout($order->price_ids, [
        'success_url' => route('checkout-success').'?session_id={CHECKOUT_SESSION_ID}',
        'cancel_url' => route('checkout-cancel'),
        'metadata' => ['order_id' => $order->id],
    ]);
})->name('checkout');

```

As you can see in the example above, when a user begins the checkout process, we will provide all of the cart / order's associated Stripe price identifiers to the `checkout` method. Of course, your application is responsible for associating these items with the "shopping cart" or order as a customer adds them. We also provide the order's ID to the Stripe Checkout session via the `metadata` array. Finally, we have added the `CHECKOUT_SESSION_ID` template variable to the Checkout success route. When Stripe redirects customers back to your application, this template variable will automatically be populated with the Checkout session ID.
Next, let's build the Checkout success route. This is the route that users will be redirected to after their purchase has been completed via Stripe Checkout. Within this route, we can retrieve the Stripe Checkout session ID and the associated Stripe Checkout instance in order to access our provided meta data and update our customer's order accordingly:
```


 1use App\Models\Order;




 2use Illuminate\Http\Request;




 3use Laravel\Cashier\Cashier;




 4 



 5Route::get('/checkout/success', function (Request $request) {




 6    $sessionId = $request->get('session_id');




 7 



 8    if ($sessionId === null) {




 9        return;




10    }




11 



12    $session = Cashier::stripe()->checkout->sessions->retrieve($sessionId);




13 



14    if ($session->payment_status !== 'paid') {




15        return;




16    }




17 



18    $orderId = $session['metadata']['order_id'] ?? null;




19 



20    $order = Order::findOrFail($orderId);




21 



22    $order->update(['status' => 'completed']);




23 



24    return view('checkout-success', ['order' => $order]);




25})->name('checkout-success');




use App\Models\Order;
use Illuminate\Http\Request;
use Laravel\Cashier\Cashier;

Route::get('/checkout/success', function (Request $request) {
    $sessionId = $request->get('session_id');

    if ($sessionId === null) {
        return;
    }

    $session = Cashier::stripe()->checkout->sessions->retrieve($sessionId);

    if ($session->payment_status !== 'paid') {
        return;
    }

    $orderId = $session['metadata']['order_id'] ?? null;

    $order = Order::findOrFail($orderId);

    $order->update(['status' => 'completed']);

    return view('checkout-success', ['order' => $order]);
})->name('checkout-success');

```

Please refer to Stripe's documentation for more information on the
### [Selling Subscriptions](https://laravel.com/docs/12.x/billing#quickstart-selling-subscriptions)
Before utilizing Stripe Checkout, you should define Products with fixed prices in your Stripe dashboard. In addition, you should [configure Cashier's webhook handling](https://laravel.com/docs/12.x/billing#handling-stripe-webhooks).
Offering product and subscription billing via your application can be intimidating. However, thanks to Cashier and
To learn how to sell subscriptions using Cashier and Stripe Checkout, let's consider the simple scenario of a subscription service with a basic monthly (`price_basic_monthly`) and yearly (`price_basic_yearly`) plan. These two prices could be grouped under a "Basic" product (`pro_basic`) in our Stripe dashboard. In addition, our subscription service might offer an Expert plan as `pro_expert`.
First, let's discover how a customer can subscribe to our services. Of course, you can imagine the customer might click a "subscribe" button for the Basic plan on our application's pricing page. This button or link should direct the user to a Laravel route which creates the Stripe Checkout session for their chosen plan:
```


 1use Illuminate\Http\Request;




 2 



 3Route::get('/subscription-checkout', function (Request $request) {




 4    return $request->user()




 5        ->newSubscription('default', 'price_basic_monthly')




 6        ->trialDays(5)




 7        ->allowPromotionCodes()




 8        ->checkout([




 9            'success_url' => route('your-success-route'),




10            'cancel_url' => route('your-cancel-route'),




11        ]);




12});




use Illuminate\Http\Request;

Route::get('/subscription-checkout', function (Request $request) {
    return $request->user()
        ->newSubscription('default', 'price_basic_monthly')
        ->trialDays(5)
        ->allowPromotionCodes()
        ->checkout([
            'success_url' => route('your-success-route'),
            'cancel_url' => route('your-cancel-route'),
        ]);
});

```

As you can see in the example above, we will redirect the customer to a Stripe Checkout session which will allow them to subscribe to our Basic plan. After a successful checkout or cancellation, the customer will be redirected back to the URL we provided to the `checkout` method. To know when their subscription has actually started (since some payment methods require a few seconds to process), we'll also need to [configure Cashier's webhook handling](https://laravel.com/docs/12.x/billing#handling-stripe-webhooks).
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

#### [Building a Subscribed Middleware](https://laravel.com/docs/12.x/billing#quickstart-building-a-subscribed-middleware)
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




18            return redirect('/billing');




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
            return redirect('/billing');
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

#### [Allowing Customers to Manage Their Billing Plan](https://laravel.com/docs/12.x/billing#quickstart-allowing-customers-to-manage-their-billing-plan)
Of course, customers may want to change their subscription plan to another product or "tier". The easiest way to allow this is by directing customers to Stripe's
First, define a link or button within your application that directs users to a Laravel route which we will utilize to initiate a Billing Portal session:
```


1<a href="{{ route('billing') }}">




2    Billing




3</a>




<a href="{{ route('billing') }}">
    Billing
</a>

```

Next, let's define the route that initiates a Stripe Customer Billing Portal session and redirects the user to the Portal. The `redirectToBillingPortal` method accepts the URL that users should be returned to when exiting the Portal:
```


1use Illuminate\Http\Request;




2 



3Route::get('/billing', function (Request $request) {




4    return $request->user()->redirectToBillingPortal(route('dashboard'));




5})->middleware(['auth'])->name('billing');




use Illuminate\Http\Request;

Route::get('/billing', function (Request $request) {
    return $request->user()->redirectToBillingPortal(route('dashboard'));
})->middleware(['auth'])->name('billing');

```

As long as you have configured Cashier's webhook handling, Cashier will automatically keep your application's Cashier-related database tables in sync by inspecting the incoming webhooks from Stripe. So, for example, when a user cancels their subscription via Stripe's Customer Billing Portal, Cashier will receive the corresponding webhook and mark the subscription as "canceled" in your application's database.
