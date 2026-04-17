## [Subscriptions](https://laravel.com/docs/12.x/cashier-paddle#subscriptions)
### [Creating Subscriptions](https://laravel.com/docs/12.x/cashier-paddle#creating-subscriptions)
To create a subscription, first retrieve an instance of your billable model from your database, which will typically be an instance of `App\Models\User`. Once you have retrieved the model instance, you may use the `subscribe` method to create the model's checkout session:
```


1use Illuminate\Http\Request;




2 



3Route::get('/user/subscribe', function (Request $request) {




4    $checkout = $request->user()->subscribe($premium = 'pri_123', 'default')




5        ->returnTo(route('home'));




6 



7    return view('billing', ['checkout' => $checkout]);




8});




use Illuminate\Http\Request;

Route::get('/user/subscribe', function (Request $request) {
    $checkout = $request->user()->subscribe($premium = 'pri_123', 'default')
        ->returnTo(route('home'));

    return view('billing', ['checkout' => $checkout]);
});

```

The first argument given to the `subscribe` method is the specific price the user is subscribing to. This value should correspond to the price's identifier in Paddle. The `returnTo` method accepts a URL that your user will be redirected to after they successfully complete the checkout. The second argument passed to the `subscribe` method should be the internal "type" of the subscription. If your application only offers a single subscription, you might call this `default` or `primary`. This subscription type is only for internal application usage and is not meant to be displayed to users. In addition, it should not contain spaces and it should never be changed after creating the subscription.
You may also provide an array of custom metadata regarding the subscription using the `customData` method:
```


1$checkout = $request->user()->subscribe($premium = 'pri_123', 'default')




2    ->customData(['key' => 'value'])




3    ->returnTo(route('home'));




$checkout = $request->user()->subscribe($premium = 'pri_123', 'default')
    ->customData(['key' => 'value'])
    ->returnTo(route('home'));

```

Once a subscription checkout session has been created, the checkout session may be provided to the `paddle-button` [Blade component](https://laravel.com/docs/12.x/cashier-paddle#overlay-checkout) that is included with Cashier Paddle:
```


1<x-paddle-button :checkout="$checkout" class="px-8 py-4">




2    Subscribe




3</x-paddle-button>




<x-paddle-button :checkout="$checkout" class="px-8 py-4">
    Subscribe
</x-paddle-button>

```

After the user has finished their checkout, a `subscription_created` webhook will be dispatched from Paddle. Cashier will receive this webhook and setup the subscription for your customer. In order to make sure all webhooks are properly received and handled by your application, ensure you have properly [setup webhook handling](https://laravel.com/docs/12.x/cashier-paddle#handling-paddle-webhooks).
### [Checking Subscription Status](https://laravel.com/docs/12.x/cashier-paddle#checking-subscription-status)
Once a user is subscribed to your application, you may check their subscription status using a variety of convenient methods. First, the `subscribed` method returns `true` if the user has a valid subscription, even if the subscription is currently within its trial period:
```


1if ($user->subscribed()) {




2    // ...




3}




if ($user->subscribed()) {
    // ...
}

```

If your application offers multiple subscriptions, you may specify the subscription when invoking the `subscribed` method:
```


1if ($user->subscribed('default')) {




2    // ...




3}




if ($user->subscribed('default')) {
    // ...
}

```

The `subscribed` method also makes a great candidate for a [route middleware](https://laravel.com/docs/12.x/middleware), allowing you to filter access to routes and controllers based on the user's subscription status:
```


 1<?php




 2 



 3namespace App\Http\Middleware;




 4 



 5use Closure;




 6use Illuminate\Http\Request;




 7use Symfony\Component\HttpFoundation\Response;




 8 



 9class EnsureUserIsSubscribed




10{




11    /**




12     * Handle an incoming request.




13     *




14     * @param  \Closure(\Illuminate\Http\Request): (\Symfony\Component\HttpFoundation\Response)  $next




15     */




16    public function handle(Request $request, Closure $next): Response




17    {




18        if ($request->user() && ! $request->user()->subscribed()) {




19            // This user is not a paying customer...




20            return redirect('/billing');




21        }




22 



23        return $next($request);




24    }




25}




<?php

namespace App\Http\Middleware;

use Closure;
use Illuminate\Http\Request;
use Symfony\Component\HttpFoundation\Response;

class EnsureUserIsSubscribed
{
    /**
     * Handle an incoming request.
     *
     * @param  \Closure(\Illuminate\Http\Request): (\Symfony\Component\HttpFoundation\Response)  $next
     */
    public function handle(Request $request, Closure $next): Response
    {
        if ($request->user() && ! $request->user()->subscribed()) {
            // This user is not a paying customer...
            return redirect('/billing');
        }

        return $next($request);
    }
}

```

If you would like to determine if a user is still within their trial period, you may use the `onTrial` method. This method can be useful for determining if you should display a warning to the user that they are still on their trial period:
```


1if ($user->subscription()->onTrial()) {




2    // ...




3}




if ($user->subscription()->onTrial()) {
    // ...
}

```

The `subscribedToPrice` method may be used to determine if the user is subscribed to a given plan based on a given Paddle price ID. In this example, we will determine if the user's `default` subscription is actively subscribed to the monthly price:
```


1if ($user->subscribedToPrice($monthly = 'pri_123', 'default')) {




2    // ...




3}




if ($user->subscribedToPrice($monthly = 'pri_123', 'default')) {
    // ...
}

```

The `recurring` method may be used to determine if the user is currently on an active subscription and is no longer within their trial period or on a grace period:
```


1if ($user->subscription()->recurring()) {




2    // ...




3}




if ($user->subscription()->recurring()) {
    // ...
}

```

#### [Canceled Subscription Status](https://laravel.com/docs/12.x/cashier-paddle#canceled-subscription-status)
To determine if the user was once an active subscriber but has canceled their subscription, you may use the `canceled` method:
```


1if ($user->subscription()->canceled()) {




2    // ...




3}




if ($user->subscription()->canceled()) {
    // ...
}

```

You may also determine if a user has canceled their subscription, but are still on their "grace period" until the subscription fully expires. For example, if a user cancels a subscription on March 5th that was originally scheduled to expire on March 10th, the user is on their "grace period" until March 10th. In addition, the `subscribed` method will still return `true` during this time:
```


1if ($user->subscription()->onGracePeriod()) {




2    // ...




3}




if ($user->subscription()->onGracePeriod()) {
    // ...
}

```

#### [Past Due Status](https://laravel.com/docs/12.x/cashier-paddle#past-due-status)
If a payment fails for a subscription, it will be marked as `past_due`. When your subscription is in this state it will not be active until the customer has updated their payment information. You may determine if a subscription is past due using the `pastDue` method on the subscription instance:
```


1if ($user->subscription()->pastDue()) {




2    // ...




3}




if ($user->subscription()->pastDue()) {
    // ...
}

```

When a subscription is past due, you should instruct the user to [update their payment information](https://laravel.com/docs/12.x/cashier-paddle#updating-payment-information).
If you would like subscriptions to still be considered valid when they are `past_due`, you may use the `keepPastDueSubscriptionsActive` method provided by Cashier. Typically, this method should be called in the `register` method of your `AppServiceProvider`:
```


1use Laravel\Paddle\Cashier;




2 



3/**




4 * Register any application services.




5 */




6public function register(): void




7{




8    Cashier::keepPastDueSubscriptionsActive();




9}




use Laravel\Paddle\Cashier;

/**
 * Register any application services.
 */
public function register(): void
{
    Cashier::keepPastDueSubscriptionsActive();
}

```

When a subscription is in a `past_due` state it cannot be changed until payment information has been updated. Therefore, the `swap` and `updateQuantity` methods will throw an exception when the subscription is in a `past_due` state.
#### [Subscription Scopes](https://laravel.com/docs/12.x/cashier-paddle#subscription-scopes)
Most subscription states are also available as query scopes so that you may easily query your database for subscriptions that are in a given state:
```


1// Get all valid subscriptions...




2$subscriptions = Subscription::query()->valid()->get();




3 



4// Get all of the canceled subscriptions for a user...




5$subscriptions = $user->subscriptions()->canceled()->get();




// Get all valid subscriptions...
$subscriptions = Subscription::query()->valid()->get();

// Get all of the canceled subscriptions for a user...
$subscriptions = $user->subscriptions()->canceled()->get();

```

A complete list of available scopes is available below:
```


 1Subscription::query()->valid();




 2Subscription::query()->onTrial();




 3Subscription::query()->expiredTrial();




 4Subscription::query()->notOnTrial();




 5Subscription::query()->active();




 6Subscription::query()->recurring();




 7Subscription::query()->pastDue();




 8Subscription::query()->paused();




 9Subscription::query()->notPaused();




10Subscription::query()->onPausedGracePeriod();




11Subscription::query()->notOnPausedGracePeriod();




12Subscription::query()->canceled();




13Subscription::query()->notCanceled();




14Subscription::query()->onGracePeriod();




15Subscription::query()->notOnGracePeriod();




Subscription::query()->valid();
Subscription::query()->onTrial();
Subscription::query()->expiredTrial();
Subscription::query()->notOnTrial();
Subscription::query()->active();
Subscription::query()->recurring();
Subscription::query()->pastDue();
Subscription::query()->paused();
Subscription::query()->notPaused();
Subscription::query()->onPausedGracePeriod();
Subscription::query()->notOnPausedGracePeriod();
Subscription::query()->canceled();
Subscription::query()->notCanceled();
Subscription::query()->onGracePeriod();
Subscription::query()->notOnGracePeriod();

```

### [Subscription Single Charges](https://laravel.com/docs/12.x/cashier-paddle#subscription-single-charges)
Subscription single charges allow you to charge subscribers with a one-time charge on top of their subscriptions. You must provide one or multiple price ID's when invoking the `charge` method:
```


1// Charge a single price...




2$response = $user->subscription()->charge('pri_123');




3 



4// Charge multiple prices at once...




5$response = $user->subscription()->charge(['pri_123', 'pri_456']);




// Charge a single price...
$response = $user->subscription()->charge('pri_123');

// Charge multiple prices at once...
$response = $user->subscription()->charge(['pri_123', 'pri_456']);

```

The `charge` method will not actually charge the customer until the next billing interval of their subscription. If you would like to bill the customer immediately, you may use the `chargeAndInvoice` method instead:
```


1$response = $user->subscription()->chargeAndInvoice('pri_123');




$response = $user->subscription()->chargeAndInvoice('pri_123');

```

### [Updating Payment Information](https://laravel.com/docs/12.x/cashier-paddle#updating-payment-information)
Paddle always saves a payment method per subscription. If you want to update the default payment method for a subscription, you should redirect your customer to Paddle's hosted payment method update page using the `redirectToUpdatePaymentMethod` method on the subscription model:
```


1use Illuminate\Http\Request;




2 



3Route::get('/update-payment-method', function (Request $request) {




4    $user = $request->user();




5 



6    return $user->subscription()->redirectToUpdatePaymentMethod();




7});




use Illuminate\Http\Request;

Route::get('/update-payment-method', function (Request $request) {
    $user = $request->user();

    return $user->subscription()->redirectToUpdatePaymentMethod();
});

```

When a user has finished updating their information, a `subscription_updated` webhook will be dispatched by Paddle and the subscription details will be updated in your application's database.
### [Changing Plans](https://laravel.com/docs/12.x/cashier-paddle#changing-plans)
After a user has subscribed to your application, they may occasionally want to change to a new subscription plan. To update the subscription plan for a user, you should pass the Paddle price's identifier to the subscription's `swap` method:
```


1use App\Models\User;




2 



3$user = User::find(1);




4 



5$user->subscription()->swap($premium = 'pri_456');




use App\Models\User;

$user = User::find(1);

$user->subscription()->swap($premium = 'pri_456');

```

If you would like to swap plans and immediately invoice the user instead of waiting for their next billing cycle, you may use the `swapAndInvoice` method:
```


1$user = User::find(1);




2 



3$user->subscription()->swapAndInvoice($premium = 'pri_456');




$user = User::find(1);

$user->subscription()->swapAndInvoice($premium = 'pri_456');

```

#### [Prorations](https://laravel.com/docs/12.x/cashier-paddle#prorations)
By default, Paddle prorates charges when swapping between plans. The `noProrate` method may be used to update the subscriptions without prorating the charges:
```


1$user->subscription('default')->noProrate()->swap($premium = 'pri_456');




$user->subscription('default')->noProrate()->swap($premium = 'pri_456');

```

If you would like to disable proration and invoice customers immediately, you may use the `swapAndInvoice` method in combination with `noProrate`:
```


1$user->subscription('default')->noProrate()->swapAndInvoice($premium = 'pri_456');




$user->subscription('default')->noProrate()->swapAndInvoice($premium = 'pri_456');

```

Or, to not bill your customer for a subscription change, you may utilize the `doNotBill` method:
```


1$user->subscription('default')->doNotBill()->swap($premium = 'pri_456');




$user->subscription('default')->doNotBill()->swap($premium = 'pri_456');

```

For more information on Paddle's proration policies, please consult Paddle's
### [Subscription Quantity](https://laravel.com/docs/12.x/cashier-paddle#subscription-quantity)
Sometimes subscriptions are affected by "quantity". For example, a project management application might charge $10 per month per project. To easily increment or decrement your subscription's quantity, use the `incrementQuantity` and `decrementQuantity` methods:
```


 1$user = User::find(1);




 2 



 3$user->subscription()->incrementQuantity();




 4 



 5// Add five to the subscription's current quantity...




 6$user->subscription()->incrementQuantity(5);




 7 



 8$user->subscription()->decrementQuantity();




 9 



10// Subtract five from the subscription's current quantity...




11$user->subscription()->decrementQuantity(5);




$user = User::find(1);

$user->subscription()->incrementQuantity();

// Add five to the subscription's current quantity...
$user->subscription()->incrementQuantity(5);

$user->subscription()->decrementQuantity();

// Subtract five from the subscription's current quantity...
$user->subscription()->decrementQuantity(5);

```

Alternatively, you may set a specific quantity using the `updateQuantity` method:
```


1$user->subscription()->updateQuantity(10);




$user->subscription()->updateQuantity(10);

```

The `noProrate` method may be used to update the subscription's quantity without prorating the charges:
```


1$user->subscription()->noProrate()->updateQuantity(10);




$user->subscription()->noProrate()->updateQuantity(10);

```

#### [Quantities for Subscriptions With Multiple Products](https://laravel.com/docs/12.x/cashier-paddle#quantities-for-subscription-with-multiple-products)
If your subscription is a [subscription with multiple products](https://laravel.com/docs/12.x/cashier-paddle#subscriptions-with-multiple-products), you should pass the ID of the price whose quantity you wish to increment or decrement as the second argument to the increment / decrement methods:
```


1$user->subscription()->incrementQuantity(1, 'price_chat');




$user->subscription()->incrementQuantity(1, 'price_chat');

```

### [Subscriptions With Multiple Products](https://laravel.com/docs/12.x/cashier-paddle#subscriptions-with-multiple-products)
When creating subscription checkout sessions, you may specify multiple products for a given subscription by passing an array of prices as the first argument to the `subscribe` method:
```


 1use Illuminate\Http\Request;




 2 



 3Route::post('/user/subscribe', function (Request $request) {




 4    $checkout = $request->user()->subscribe([




 5        'price_monthly',




 6        'price_chat',




 7    ]);




 8 



 9    return view('billing', ['checkout' => $checkout]);




10});




use Illuminate\Http\Request;

Route::post('/user/subscribe', function (Request $request) {
    $checkout = $request->user()->subscribe([
        'price_monthly',
        'price_chat',
    ]);

    return view('billing', ['checkout' => $checkout]);
});

```

In the example above, the customer will have two prices attached to their `default` subscription. Both prices will be charged on their respective billing intervals. If necessary, you may pass an associative array of key / value pairs to indicate a specific quantity for each price:
```


1$user = User::find(1);




2 



3$checkout = $user->subscribe('default', ['price_monthly', 'price_chat' => 5]);




$user = User::find(1);

$checkout = $user->subscribe('default', ['price_monthly', 'price_chat' => 5]);

```

If you would like to add another price to an existing subscription, you must use the subscription's `swap` method. When invoking the `swap` method, you should also include the subscription's current prices and quantities as well:
```


1$user = User::find(1);




2 



3$user->subscription()->swap(['price_chat', 'price_original' => 2]);




$user = User::find(1);

$user->subscription()->swap(['price_chat', 'price_original' => 2]);

```

The example above will add the new price, but the customer will not be billed for it until their next billing cycle. If you would like to bill the customer immediately you may use the `swapAndInvoice` method:
```


1$user->subscription()->swapAndInvoice(['price_chat', 'price_original' => 2]);




$user->subscription()->swapAndInvoice(['price_chat', 'price_original' => 2]);

```

You may remove prices from subscriptions using the `swap` method and omitting the price you want to remove:
```


1$user->subscription()->swap(['price_original' => 2]);




$user->subscription()->swap(['price_original' => 2]);

```

You may not remove the last price on a subscription. Instead, you should simply cancel the subscription.
### [Multiple Subscriptions](https://laravel.com/docs/12.x/cashier-paddle#multiple-subscriptions)
Paddle allows your customers to have multiple subscriptions simultaneously. For example, you may run a gym that offers a swimming subscription and a weight-lifting subscription, and each subscription may have different pricing. Of course, customers should be able to subscribe to either or both plans.
When your application creates subscriptions, you may provide the type of the subscription to the `subscribe` method as the second argument. The type may be any string that represents the type of subscription the user is initiating:
```


1use Illuminate\Http\Request;




2 



3Route::post('/swimming/subscribe', function (Request $request) {




4    $checkout = $request->user()->subscribe($swimmingMonthly = 'pri_123', 'swimming');




5 



6    return view('billing', ['checkout' => $checkout]);




7});




use Illuminate\Http\Request;

Route::post('/swimming/subscribe', function (Request $request) {
    $checkout = $request->user()->subscribe($swimmingMonthly = 'pri_123', 'swimming');

    return view('billing', ['checkout' => $checkout]);
});

```

In this example, we initiated a monthly swimming subscription for the customer. However, they may want to swap to a yearly subscription at a later time. When adjusting the customer's subscription, we can simply swap the price on the `swimming` subscription:
```


1$user->subscription('swimming')->swap($swimmingYearly = 'pri_456');




$user->subscription('swimming')->swap($swimmingYearly = 'pri_456');

```

Of course, you may also cancel the subscription entirely:
```


1$user->subscription('swimming')->cancel();




$user->subscription('swimming')->cancel();

```

### [Pausing Subscriptions](https://laravel.com/docs/12.x/cashier-paddle#pausing-subscriptions)
To pause a subscription, call the `pause` method on the user's subscription:
```


1$user->subscription()->pause();




$user->subscription()->pause();

```

When a subscription is paused, Cashier will automatically set the `paused_at` column in your database. This column is used to determine when the `paused` method should begin returning `true`. For example, if a customer pauses a subscription on March 1st, but the subscription was not scheduled to recur until March 5th, the `paused` method will continue to return `false` until March 5th. This is because a user is typically allowed to continue using an application until the end of their billing cycle.
By default, pausing happens at the next billing interval so the customer can use the remainder of the period they paid for. If you want to pause a subscription immediately, you may use the `pauseNow` method:
```


1$user->subscription()->pauseNow();




$user->subscription()->pauseNow();

```

Using the `pauseUntil` method, you can pause the subscription until a specific moment in time:
```


1$user->subscription()->pauseUntil(now()->plus(months: 1));




$user->subscription()->pauseUntil(now()->plus(months: 1));

```

Or, you may use the `pauseNowUntil` method to immediately pause the subscription until a given point in time:
```


1$user->subscription()->pauseNowUntil(now()->plus(months: 1));




$user->subscription()->pauseNowUntil(now()->plus(months: 1));

```

You may determine if a user has paused their subscription but are still on their "grace period" using the `onPausedGracePeriod` method:
```


1if ($user->subscription()->onPausedGracePeriod()) {




2    // ...




3}




if ($user->subscription()->onPausedGracePeriod()) {
    // ...
}

```

To resume a paused subscription, you may invoke the `resume` method on the subscription:
```


1$user->subscription()->resume();




$user->subscription()->resume();

```

A subscription cannot be modified while it is paused. If you want to swap to a different plan or update quantities you must resume the subscription first.
### [Canceling Subscriptions](https://laravel.com/docs/12.x/cashier-paddle#canceling-subscriptions)
To cancel a subscription, call the `cancel` method on the user's subscription:
```


1$user->subscription()->cancel();




$user->subscription()->cancel();

```

When a subscription is canceled, Cashier will automatically set the `ends_at` column in your database. This column is used to determine when the `subscribed` method should begin returning `false`. For example, if a customer cancels a subscription on March 1st, but the subscription was not scheduled to end until March 5th, the `subscribed` method will continue to return `true` until March 5th. This is done because a user is typically allowed to continue using an application until the end of their billing cycle.
You may determine if a user has canceled their subscription but are still on their "grace period" using the `onGracePeriod` method:
```


1if ($user->subscription()->onGracePeriod()) {




2    // ...




3}




if ($user->subscription()->onGracePeriod()) {
    // ...
}

```

If you wish to cancel a subscription immediately, you may call the `cancelNow` method on the subscription:
```


1$user->subscription()->cancelNow();




$user->subscription()->cancelNow();

```

To stop a subscription on its grace period from canceling, you may invoke the `stopCancelation` method:
```


1$user->subscription()->stopCancelation();




$user->subscription()->stopCancelation();

```

Paddle's subscriptions cannot be resumed after cancellation. If your customer wishes to resume their subscription, they will have to create a new subscription.
