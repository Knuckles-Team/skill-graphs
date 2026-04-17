## [Subscriptions](https://laravel.com/docs/12.x/billing#subscriptions)
Subscriptions provide a way to set up recurring payments for your customers. Stripe subscriptions managed by Cashier provide support for multiple subscription prices, subscription quantities, trials, and more.
### [Creating Subscriptions](https://laravel.com/docs/12.x/billing#creating-subscriptions)
To create a subscription, first retrieve an instance of your billable model, which typically will be an instance of `App\Models\User`. Once you have retrieved the model instance, you may use the `newSubscription` method to create the model's subscription:
```


1use Illuminate\Http\Request;




2 



3Route::post('/user/subscribe', function (Request $request) {




4    $request->user()->newSubscription(




5        'default', 'price_monthly'




6    )->create($request->paymentMethodId);




7 



8    // ...




9});




use Illuminate\Http\Request;

Route::post('/user/subscribe', function (Request $request) {
    $request->user()->newSubscription(
        'default', 'price_monthly'
    )->create($request->paymentMethodId);

    // ...
});

```

The first argument passed to the `newSubscription` method should be the internal type of the subscription. If your application only offers a single subscription, you might call this `default` or `primary`. This subscription type is only for internal application usage and is not meant to be shown to users. In addition, it should not contain spaces and it should never be changed after creating the subscription. The second argument is the specific price the user is subscribing to. This value should correspond to the price's identifier in Stripe.
The `create` method, which accepts [a Stripe payment method identifier](https://laravel.com/docs/12.x/billing#storing-payment-methods) or Stripe `PaymentMethod` object, will begin the subscription as well as update your database with the billable model's Stripe customer ID and other relevant billing information.
Passing a payment method identifier directly to the `create` subscription method will also automatically add it to the user's stored payment methods.
#### [Collecting Recurring Payments via Invoice Emails](https://laravel.com/docs/12.x/billing#collecting-recurring-payments-via-invoice-emails)
Instead of collecting a customer's recurring payments automatically, you may instruct Stripe to email an invoice to the customer each time their recurring payment is due. Then, the customer may manually pay the invoice once they receive it. The customer does not need to provide a payment method up front when collecting recurring payments via invoices:
```


1$user->newSubscription('default', 'price_monthly')->createAndSendInvoice();




$user->newSubscription('default', 'price_monthly')->createAndSendInvoice();

```

The amount of time a customer has to pay their invoice before their subscription is canceled is determined by the `days_until_due` option. By default, this is 30 days; however, you may provide a specific value for this option if you wish:
```


1$user->newSubscription('default', 'price_monthly')->createAndSendInvoice([], [




2    'days_until_due' => 30




3]);




$user->newSubscription('default', 'price_monthly')->createAndSendInvoice([], [
    'days_until_due' => 30
]);

```

#### [Quantities](https://laravel.com/docs/12.x/billing#subscription-quantities)
If you would like to set a specific `quantity` method on the subscription builder before creating the subscription:
```


1$user->newSubscription('default', 'price_monthly')




2    ->quantity(5)




3    ->create($paymentMethod);




$user->newSubscription('default', 'price_monthly')
    ->quantity(5)
    ->create($paymentMethod);

```

#### [Additional Details](https://laravel.com/docs/12.x/billing#additional-details)
If you would like to specify additional `create` method:
```


1$user->newSubscription('default', 'price_monthly')->create($paymentMethod, [




2    'email' => $email,




3], [




4    'metadata' => ['note' => 'Some extra information.'],




5]);




$user->newSubscription('default', 'price_monthly')->create($paymentMethod, [
    'email' => $email,
], [
    'metadata' => ['note' => 'Some extra information.'],
]);

```

#### [Coupons](https://laravel.com/docs/12.x/billing#coupons)
If you would like to apply a coupon when creating the subscription, you may use the `withCoupon` method:
```


1$user->newSubscription('default', 'price_monthly')




2    ->withCoupon('code')




3    ->create($paymentMethod);




$user->newSubscription('default', 'price_monthly')
    ->withCoupon('code')
    ->create($paymentMethod);

```

Or, if you would like to apply a `withPromotionCode` method:
```


1$user->newSubscription('default', 'price_monthly')




2    ->withPromotionCode('promo_code_id')




3    ->create($paymentMethod);




$user->newSubscription('default', 'price_monthly')
    ->withPromotionCode('promo_code_id')
    ->create($paymentMethod);

```

The given promotion code ID should be the Stripe API ID assigned to the promotion code and not the customer facing promotion code. If you need to find a promotion code ID based on a given customer facing promotion code, you may use the `findPromotionCode` method:
```


1// Find a promotion code ID by its customer facing code...




2$promotionCode = $user->findPromotionCode('SUMMERSALE');




3 



4// Find an active promotion code ID by its customer facing code...




5$promotionCode = $user->findActivePromotionCode('SUMMERSALE');




// Find a promotion code ID by its customer facing code...
$promotionCode = $user->findPromotionCode('SUMMERSALE');

// Find an active promotion code ID by its customer facing code...
$promotionCode = $user->findActivePromotionCode('SUMMERSALE');

```

In the example above, the returned `$promotionCode` object is an instance of `Laravel\Cashier\PromotionCode`. This class decorates an underlying `Stripe\PromotionCode` object. You can retrieve the coupon related to the promotion code by invoking the `coupon` method:
```


1$coupon = $user->findPromotionCode('SUMMERSALE')->coupon();




$coupon = $user->findPromotionCode('SUMMERSALE')->coupon();

```

The coupon instance allows you to determine the discount amount and whether the coupon represents a fixed discount or percentage based discount:
```


1if ($coupon->isPercentage()) {




2    return $coupon->percentOff().'%'; // 21.5%




3} else {




4    return $coupon->amountOff(); // $5.99




5}




if ($coupon->isPercentage()) {
    return $coupon->percentOff().'%'; // 21.5%
} else {
    return $coupon->amountOff(); // $5.99
}

```

You can also retrieve the discounts that are currently applied to a customer or subscription:
```


1$discount = $billable->discount();




2 



3$discount = $subscription->discount();




$discount = $billable->discount();

$discount = $subscription->discount();

```

The returned `Laravel\Cashier\Discount` instances decorate an underlying `Stripe\Discount` object instance. You may retrieve the coupon related to this discount by invoking the `coupon` method:
```


1$coupon = $subscription->discount()->coupon();




$coupon = $subscription->discount()->coupon();

```

If you would like to apply a new coupon or promotion code to a customer or subscription, you may do so via the `applyCoupon` or `applyPromotionCode` methods:
```


1$billable->applyCoupon('coupon_id');




2$billable->applyPromotionCode('promotion_code_id');




3 



4$subscription->applyCoupon('coupon_id');




5$subscription->applyPromotionCode('promotion_code_id');




$billable->applyCoupon('coupon_id');
$billable->applyPromotionCode('promotion_code_id');

$subscription->applyCoupon('coupon_id');
$subscription->applyPromotionCode('promotion_code_id');

```

Remember, you should use the Stripe API ID assigned to the promotion code and not the customer facing promotion code. Only one coupon or promotion code can be applied to a customer or subscription at a given time.
For more info on this subject, please consult the Stripe documentation regarding
#### [Adding Subscriptions](https://laravel.com/docs/12.x/billing#adding-subscriptions)
If you would like to add a subscription to a customer who already has a default payment method you may invoke the `add` method on the subscription builder:
```


1use App\Models\User;




2 



3$user = User::find(1);




4 



5$user->newSubscription('default', 'price_monthly')->add();




use App\Models\User;

$user = User::find(1);

$user->newSubscription('default', 'price_monthly')->add();

```

#### [Creating Subscriptions From the Stripe Dashboard](https://laravel.com/docs/12.x/billing#creating-subscriptions-from-the-stripe-dashboard)
You may also create subscriptions from the Stripe dashboard itself. When doing so, Cashier will sync newly added subscriptions and assign them a type of `default`. To customize the subscription type that is assigned to dashboard created subscriptions, [define webhook event handlers](https://laravel.com/docs/12.x/billing#defining-webhook-event-handlers).
In addition, you may only create one type of subscription via the Stripe dashboard. If your application offers multiple subscriptions that use different types, only one type of subscription may be added through the Stripe dashboard.
Finally, you should always make sure to only add one active subscription per type of subscription offered by your application. If a customer has two `default` subscriptions, only the most recently added subscription will be used by Cashier even though both would be synced with your application's database.
### [Checking Subscription Status](https://laravel.com/docs/12.x/billing#checking-subscription-status)
Once a customer is subscribed to your application, you may easily check their subscription status using a variety of convenient methods. First, the `subscribed` method returns `true` if the customer has an active subscription, even if the subscription is currently within its trial period. The `subscribed` method accepts the type of the subscription as its first argument:
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




18        if ($request->user() && ! $request->user()->subscribed('default')) {




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
        if ($request->user() && ! $request->user()->subscribed('default')) {
            // This user is not a paying customer...
            return redirect('/billing');
        }

        return $next($request);
    }
}

```

If you would like to determine if a user is still within their trial period, you may use the `onTrial` method. This method can be useful for determining if you should display a warning to the user that they are still on their trial period:
```


1if ($user->subscription('default')->onTrial()) {




2    // ...




3}




if ($user->subscription('default')->onTrial()) {
    // ...
}

```

The `subscribedToProduct` method may be used to determine if the user is subscribed to a given product based on a given Stripe product's identifier. In Stripe, products are collections of prices. In this example, we will determine if the user's `default` subscription is actively subscribed to the application's "premium" product. The given Stripe product identifier should correspond to one of your product's identifiers in the Stripe dashboard:
```


1if ($user->subscribedToProduct('prod_premium', 'default')) {




2    // ...




3}




if ($user->subscribedToProduct('prod_premium', 'default')) {
    // ...
}

```

By passing an array to the `subscribedToProduct` method, you may determine if the user's `default` subscription is actively subscribed to the application's "basic" or "premium" product:
```


1if ($user->subscribedToProduct(['prod_basic', 'prod_premium'], 'default')) {




2    // ...




3}




if ($user->subscribedToProduct(['prod_basic', 'prod_premium'], 'default')) {
    // ...
}

```

The `subscribedToPrice` method may be used to determine if a customer's subscription corresponds to a given price ID:
```


1if ($user->subscribedToPrice('price_basic_monthly', 'default')) {




2    // ...




3}




if ($user->subscribedToPrice('price_basic_monthly', 'default')) {
    // ...
}

```

The `recurring` method may be used to determine if the user is currently subscribed and is no longer within their trial period:
```


1if ($user->subscription('default')->recurring()) {




2    // ...




3}




if ($user->subscription('default')->recurring()) {
    // ...
}

```

If a user has two subscriptions with the same type, the most recent subscription will always be returned by the `subscription` method. For example, a user might have two subscription records with the type of `default`; however, one of the subscriptions may be an old, expired subscription, while the other is the current, active subscription. The most recent subscription will always be returned while older subscriptions are kept in the database for historical review.
#### [Canceled Subscription Status](https://laravel.com/docs/12.x/billing#cancelled-subscription-status)
To determine if the user was once an active subscriber but has canceled their subscription, you may use the `canceled` method:
```


1if ($user->subscription('default')->canceled()) {




2    // ...




3}




if ($user->subscription('default')->canceled()) {
    // ...
}

```

You may also determine if a user has canceled their subscription but are still on their "grace period" until the subscription fully expires. For example, if a user cancels a subscription on March 5th that was originally scheduled to expire on March 10th, the user is on their "grace period" until March 10th. Note that the `subscribed` method still returns `true` during this time:
```


1if ($user->subscription('default')->onGracePeriod()) {




2    // ...




3}




if ($user->subscription('default')->onGracePeriod()) {
    // ...
}

```

To determine if the user has canceled their subscription and is no longer within their "grace period", you may use the `ended` method:
```


1if ($user->subscription('default')->ended()) {




2    // ...




3}




if ($user->subscription('default')->ended()) {
    // ...
}

```

#### [Incomplete and Past Due Status](https://laravel.com/docs/12.x/billing#incomplete-and-past-due-status)
If a subscription requires a secondary payment action after creation the subscription will be marked as `incomplete`. Subscription statuses are stored in the `stripe_status` column of Cashier's `subscriptions` database table.
Similarly, if a secondary payment action is required when swapping prices the subscription will be marked as `past_due`. When your subscription is in either of these states it will not be active until the customer has confirmed their payment. Determining if a subscription has an incomplete payment may be accomplished using the `hasIncompletePayment` method on the billable model or a subscription instance:
```


1if ($user->hasIncompletePayment('default')) {




2    // ...




3}




4 



5if ($user->subscription('default')->hasIncompletePayment()) {




6    // ...




7}




if ($user->hasIncompletePayment('default')) {
    // ...
}

if ($user->subscription('default')->hasIncompletePayment()) {
    // ...
}

```

When a subscription has an incomplete payment, you should direct the user to Cashier's payment confirmation page, passing the `latestPayment` identifier. You may use the `latestPayment` method available on subscription instance to retrieve this identifier:
```


1<a href="{{ route('cashier.payment', $subscription->latestPayment()->id) }}">




2    Please confirm your payment.




3</a>




<a href="{{ route('cashier.payment', $subscription->latestPayment()->id) }}">
    Please confirm your payment.
</a>

```

If you would like the subscription to still be considered active when it's in a `past_due` or `incomplete` state, you may use the `keepPastDueSubscriptionsActive` and `keepIncompleteSubscriptionsActive` methods provided by Cashier. Typically, these methods should be called in the `register` method of your `App\Providers\AppServiceProvider`:
```


 1use Laravel\Cashier\Cashier;




 2 



 3/**




 4 * Register any application services.




 5 */




 6public function register(): void




 7{




 8    Cashier::keepPastDueSubscriptionsActive();




 9    Cashier::keepIncompleteSubscriptionsActive();




10}




use Laravel\Cashier\Cashier;

/**
 * Register any application services.
 */
public function register(): void
{
    Cashier::keepPastDueSubscriptionsActive();
    Cashier::keepIncompleteSubscriptionsActive();
}

```

When a subscription is in an `incomplete` state it cannot be changed until the payment is confirmed. Therefore, the `swap` and `updateQuantity` methods will throw an exception when the subscription is in an `incomplete` state.
#### [Subscription Scopes](https://laravel.com/docs/12.x/billing#subscription-scopes)
Most subscription states are also available as query scopes so that you may easily query your database for subscriptions that are in a given state:
```


1// Get all active subscriptions...




2$subscriptions = Subscription::query()->active()->get();




3 



4// Get all of the canceled subscriptions for a user...




5$subscriptions = $user->subscriptions()->canceled()->get();




// Get all active subscriptions...
$subscriptions = Subscription::query()->active()->get();

// Get all of the canceled subscriptions for a user...
$subscriptions = $user->subscriptions()->canceled()->get();

```

A complete list of available scopes is available below:
```


 1Subscription::query()->active();




 2Subscription::query()->canceled();




 3Subscription::query()->ended();




 4Subscription::query()->incomplete();




 5Subscription::query()->notCanceled();




 6Subscription::query()->notOnGracePeriod();




 7Subscription::query()->notOnTrial();




 8Subscription::query()->onGracePeriod();




 9Subscription::query()->onTrial();




10Subscription::query()->pastDue();




11Subscription::query()->recurring();




Subscription::query()->active();
Subscription::query()->canceled();
Subscription::query()->ended();
Subscription::query()->incomplete();
Subscription::query()->notCanceled();
Subscription::query()->notOnGracePeriod();
Subscription::query()->notOnTrial();
Subscription::query()->onGracePeriod();
Subscription::query()->onTrial();
Subscription::query()->pastDue();
Subscription::query()->recurring();

```

### [Changing Prices](https://laravel.com/docs/12.x/billing#changing-prices)
After a customer is subscribed to your application, they may occasionally want to change to a new subscription price. To swap a customer to a new price, pass the Stripe price's identifier to the `swap` method. When swapping prices, it is assumed that the user would like to re-activate their subscription if it was previously canceled. The given price identifier should correspond to a Stripe price identifier available in the Stripe dashboard:
```


1use App\Models\User;




2 



3$user = App\Models\User::find(1);




4 



5$user->subscription('default')->swap('price_yearly');




use App\Models\User;

$user = App\Models\User::find(1);

$user->subscription('default')->swap('price_yearly');

```

If the customer is on trial, the trial period will be maintained. Additionally, if a "quantity" exists for the subscription, that quantity will also be maintained.
If you would like to swap prices and cancel any trial period the customer is currently on, you may invoke the `skipTrial` method:
```


1$user->subscription('default')




2    ->skipTrial()




3    ->swap('price_yearly');




$user->subscription('default')
    ->skipTrial()
    ->swap('price_yearly');

```

If you would like to swap prices and immediately invoice the customer instead of waiting for their next billing cycle, you may use the `swapAndInvoice` method:
```


1$user = User::find(1);




2 



3$user->subscription('default')->swapAndInvoice('price_yearly');




$user = User::find(1);

$user->subscription('default')->swapAndInvoice('price_yearly');

```

#### [Prorations](https://laravel.com/docs/12.x/billing#prorations)
By default, Stripe prorates charges when swapping between prices. The `noProrate` method may be used to update the subscription's price without prorating the charges:
```


1$user->subscription('default')->noProrate()->swap('price_yearly');




$user->subscription('default')->noProrate()->swap('price_yearly');

```

For more information on subscription proration, consult the
Executing the `noProrate` method before the `swapAndInvoice` method will have no effect on proration. An invoice will always be issued.
### [Subscription Quantity](https://laravel.com/docs/12.x/billing#subscription-quantity)
Sometimes subscriptions are affected by "quantity". For example, a project management application might charge $10 per month per project. You may use the `incrementQuantity` and `decrementQuantity` methods to easily increment or decrement your subscription quantity:
```


 1use App\Models\User;




 2 



 3$user = User::find(1);




 4 



 5$user->subscription('default')->incrementQuantity();




 6 



 7// Add five to the subscription's current quantity...




 8$user->subscription('default')->incrementQuantity(5);




 9 



10$user->subscription('default')->decrementQuantity();




11 



12// Subtract five from the subscription's current quantity...




13$user->subscription('default')->decrementQuantity(5);




use App\Models\User;

$user = User::find(1);

$user->subscription('default')->incrementQuantity();

// Add five to the subscription's current quantity...
$user->subscription('default')->incrementQuantity(5);

$user->subscription('default')->decrementQuantity();

// Subtract five from the subscription's current quantity...
$user->subscription('default')->decrementQuantity(5);

```

Alternatively, you may set a specific quantity using the `updateQuantity` method:
```


1$user->subscription('default')->updateQuantity(10);




$user->subscription('default')->updateQuantity(10);

```

The `noProrate` method may be used to update the subscription's quantity without prorating the charges:
```


1$user->subscription('default')->noProrate()->updateQuantity(10);




$user->subscription('default')->noProrate()->updateQuantity(10);

```

For more information on subscription quantities, consult the
#### [Quantities for Subscriptions With Multiple Products](https://laravel.com/docs/12.x/billing#quantities-for-subscription-with-multiple-products)
If your subscription is a [subscription with multiple products](https://laravel.com/docs/12.x/billing#subscriptions-with-multiple-products), you should pass the ID of the price whose quantity you wish to increment or decrement as the second argument to the increment / decrement methods:
```


1$user->subscription('default')->incrementQuantity(1, 'price_chat');




$user->subscription('default')->incrementQuantity(1, 'price_chat');

```

### [Subscriptions With Multiple Products](https://laravel.com/docs/12.x/billing#subscriptions-with-multiple-products)
`subscription_items` database table.
You may specify multiple products for a given subscription by passing an array of prices as the second argument to the `newSubscription` method:
```


 1use Illuminate\Http\Request;




 2 



 3Route::post('/user/subscribe', function (Request $request) {




 4    $request->user()->newSubscription('default', [




 5        'price_monthly',




 6        'price_chat',




 7    ])->create($request->paymentMethodId);




 8 



 9    // ...




10});




use Illuminate\Http\Request;

Route::post('/user/subscribe', function (Request $request) {
    $request->user()->newSubscription('default', [
        'price_monthly',
        'price_chat',
    ])->create($request->paymentMethodId);

    // ...
});

```

In the example above, the customer will have two prices attached to their `default` subscription. Both prices will be charged on their respective billing intervals. If necessary, you may use the `quantity` method to indicate a specific quantity for each price:
```


1$user = User::find(1);




2 



3$user->newSubscription('default', ['price_monthly', 'price_chat'])




4    ->quantity(5, 'price_chat')




5    ->create($paymentMethod);




$user = User::find(1);

$user->newSubscription('default', ['price_monthly', 'price_chat'])
    ->quantity(5, 'price_chat')
    ->create($paymentMethod);

```

If you would like to add another price to an existing subscription, you may invoke the subscription's `addPrice` method:
```


1$user = User::find(1);




2 



3$user->subscription('default')->addPrice('price_chat');




$user = User::find(1);

$user->subscription('default')->addPrice('price_chat');

```

The example above will add the new price and the customer will be billed for it on their next billing cycle. If you would like to bill the customer immediately you may use the `addPriceAndInvoice` method:
```


1$user->subscription('default')->addPriceAndInvoice('price_chat');




$user->subscription('default')->addPriceAndInvoice('price_chat');

```

If you would like to add a price with a specific quantity, you can pass the quantity as the second argument of the `addPrice` or `addPriceAndInvoice` methods:
```


1$user = User::find(1);




2 



3$user->subscription('default')->addPrice('price_chat', 5);




$user = User::find(1);

$user->subscription('default')->addPrice('price_chat', 5);

```

You may remove prices from subscriptions using the `removePrice` method:
```


1$user->subscription('default')->removePrice('price_chat');




$user->subscription('default')->removePrice('price_chat');

```

You may not remove the last price on a subscription. Instead, you should simply cancel the subscription.
#### [Swapping Prices](https://laravel.com/docs/12.x/billing#swapping-prices)
You may also change the prices attached to a subscription with multiple products. For example, imagine a customer has a `price_basic` subscription with a `price_chat` add-on product and you want to upgrade the customer from the `price_basic` to the `price_pro` price:
```


1use App\Models\User;




2 



3$user = User::find(1);




4 



5$user->subscription('default')->swap(['price_pro', 'price_chat']);




use App\Models\User;

$user = User::find(1);

$user->subscription('default')->swap(['price_pro', 'price_chat']);

```

When executing the example above, the underlying subscription item with the `price_basic` is deleted and the one with the `price_chat` is preserved. Additionally, a new subscription item for the `price_pro` is created.
You can also specify subscription item options by passing an array of key / value pairs to the `swap` method. For example, you may need to specify the subscription price quantities:
```


1$user = User::find(1);




2 



3$user->subscription('default')->swap([




4    'price_pro' => ['quantity' => 5],




5    'price_chat'




6]);




$user = User::find(1);

$user->subscription('default')->swap([
    'price_pro' => ['quantity' => 5],
    'price_chat'
]);

```

If you want to swap a single price on a subscription, you may do so using the `swap` method on the subscription item itself. This approach is particularly useful if you would like to preserve all of the existing metadata on the subscription's other prices:
```


1$user = User::find(1);




2 



3$user->subscription('default')




4    ->findItemOrFail('price_basic')




5    ->swap('price_pro');




$user = User::find(1);

$user->subscription('default')
    ->findItemOrFail('price_basic')
    ->swap('price_pro');

```

#### [Proration](https://laravel.com/docs/12.x/billing#proration)
By default, Stripe will prorate charges when adding or removing prices from a subscription with multiple products. If you would like to make a price adjustment without proration, you should chain the `noProrate` method onto your price operation:
```


1$user->subscription('default')->noProrate()->removePrice('price_chat');




$user->subscription('default')->noProrate()->removePrice('price_chat');

```

#### [Quantities](https://laravel.com/docs/12.x/billing#swapping-quantities)
If you would like to update quantities on individual subscription prices, you may do so using the [existing quantity methods](https://laravel.com/docs/12.x/billing#subscription-quantity) by passing the ID of the price as an additional argument to the method:
```


1$user = User::find(1);




2 



3$user->subscription('default')->incrementQuantity(5, 'price_chat');




4 



5$user->subscription('default')->decrementQuantity(3, 'price_chat');




6 



7$user->subscription('default')->updateQuantity(10, 'price_chat');




$user = User::find(1);

$user->subscription('default')->incrementQuantity(5, 'price_chat');

$user->subscription('default')->decrementQuantity(3, 'price_chat');

$user->subscription('default')->updateQuantity(10, 'price_chat');

```

When a subscription has multiple prices the `stripe_price` and `quantity` attributes on the `Subscription` model will be `null`. To access the individual price attributes, you should use the `items` relationship available on the `Subscription` model.
#### [Subscription Items](https://laravel.com/docs/12.x/billing#subscription-items)
When a subscription has multiple prices, it will have multiple subscription "items" stored in your database's `subscription_items` table. You may access these via the `items` relationship on the subscription:
```


1use App\Models\User;




2 



3$user = User::find(1);




4 



5$subscriptionItem = $user->subscription('default')->items->first();




6 



7// Retrieve the Stripe price and quantity for a specific item...




8$stripePrice = $subscriptionItem->stripe_price;




9$quantity = $subscriptionItem->quantity;




use App\Models\User;

$user = User::find(1);

$subscriptionItem = $user->subscription('default')->items->first();

// Retrieve the Stripe price and quantity for a specific item...
$stripePrice = $subscriptionItem->stripe_price;
$quantity = $subscriptionItem->quantity;

```

You can also retrieve a specific price using the `findItemOrFail` method:
```


1$user = User::find(1);




2 



3$subscriptionItem = $user->subscription('default')->findItemOrFail('price_chat');




$user = User::find(1);

$subscriptionItem = $user->subscription('default')->findItemOrFail('price_chat');

```

### [Multiple Subscriptions](https://laravel.com/docs/12.x/billing#multiple-subscriptions)
Stripe allows your customers to have multiple subscriptions simultaneously. For example, you may run a gym that offers a swimming subscription and a weight-lifting subscription, and each subscription may have different pricing. Of course, customers should be able to subscribe to either or both plans.
When your application creates subscriptions, you may provide the type of the subscription to the `newSubscription` method. The type may be any string that represents the type of subscription the user is initiating:
```


1use Illuminate\Http\Request;




2 



3Route::post('/swimming/subscribe', function (Request $request) {




4    $request->user()->newSubscription('swimming')




5        ->price('price_swimming_monthly')




6        ->create($request->paymentMethodId);




7 



8    // ...




9});




use Illuminate\Http\Request;

Route::post('/swimming/subscribe', function (Request $request) {
    $request->user()->newSubscription('swimming')
        ->price('price_swimming_monthly')
        ->create($request->paymentMethodId);

    // ...
});

```

In this example, we initiated a monthly swimming subscription for the customer. However, they may want to swap to a yearly subscription at a later time. When adjusting the customer's subscription, we can simply swap the price on the `swimming` subscription:
```


1$user->subscription('swimming')->swap('price_swimming_yearly');




$user->subscription('swimming')->swap('price_swimming_yearly');

```

Of course, you may also cancel the subscription entirely:
```


1$user->subscription('swimming')->cancel();




$user->subscription('swimming')->cancel();

```

### [Usage Based Billing](https://laravel.com/docs/12.x/billing#usage-based-billing)
To start using usage billing, you will first need to create a new product in your Stripe dashboard with a `meteredPrice` method to add the metered price ID to a customer subscription:
```


1use Illuminate\Http\Request;




2 



3Route::post('/user/subscribe', function (Request $request) {




4    $request->user()->newSubscription('default')




5        ->meteredPrice('price_metered')




6        ->create($request->paymentMethodId);




7 



8    // ...




9});




use Illuminate\Http\Request;

Route::post('/user/subscribe', function (Request $request) {
    $request->user()->newSubscription('default')
        ->meteredPrice('price_metered')
        ->create($request->paymentMethodId);

    // ...
});

```

You may also start a metered subscription via [Stripe Checkout](https://laravel.com/docs/12.x/billing#checkout):
```


1$checkout = Auth::user()




2    ->newSubscription('default', [])




3    ->meteredPrice('price_metered')




4    ->checkout();




5 



6return view('your-checkout-view', [




7    'checkout' => $checkout,




8]);




$checkout = Auth::user()
    ->newSubscription('default', [])
    ->meteredPrice('price_metered')
    ->checkout();

return view('your-checkout-view', [
    'checkout' => $checkout,
]);

```

#### [Reporting Usage](https://laravel.com/docs/12.x/billing#reporting-usage)
As your customer uses your application, you will report their usage to Stripe so that they can be billed accurately. To report the usage of a metered event, you may use the `reportMeterEvent` method on your `Billable` model:
```


1$user = User::find(1);




2 



3$user->reportMeterEvent('emails-sent');




$user = User::find(1);

$user->reportMeterEvent('emails-sent');

```

By default, a "usage quantity" of 1 is added to the billing period. Alternatively, you may pass a specific amount of "usage" to add to the customer's usage for the billing period:
```


1$user = User::find(1);




2 



3$user->reportMeterEvent('emails-sent', quantity: 15);




$user = User::find(1);

$user->reportMeterEvent('emails-sent', quantity: 15);

```

To retrieve a customer's event summary for a meter, you may use a `Billable` instance's `meterEventSummaries` method:
```


1$user = User::find(1);




2 



3$meterUsage = $user->meterEventSummaries($meterId);




4 



5$meterUsage->first()->aggregated_value // 10




$user = User::find(1);

$meterUsage = $user->meterEventSummaries($meterId);

$meterUsage->first()->aggregated_value // 10

```

Please refer to Stripe's
To `Billable` instance's `meters` method:
```


1$user = User::find(1);




2 



3$user->meters();




$user = User::find(1);

$user->meters();

```

### [Subscription Taxes](https://laravel.com/docs/12.x/billing#subscription-taxes)
Instead of calculating Tax Rates manually, you can [automatically calculate taxes using Stripe Tax](https://laravel.com/docs/12.x/billing#tax-configuration)
To specify the tax rates a user pays on a subscription, you should implement the `taxRates` method on your billable model and return an array containing the Stripe tax rate IDs. You can define these tax rates in
```


1/**




2 * The tax rates that should apply to the customer's subscriptions.




3 *




4 * @return array<int, string>




5 */




6public function taxRates(): array




7{




8    return ['txr_id'];




9}




/**
 * The tax rates that should apply to the customer's subscriptions.
 *
 * @return array<int, string>
 */
public function taxRates(): array
{
    return ['txr_id'];
}

```

The `taxRates` method enables you to apply a tax rate on a customer-by-customer basis, which may be helpful for a user base that spans multiple countries and tax rates.
If you're offering subscriptions with multiple products, you may define different tax rates for each price by implementing a `priceTaxRates` method on your billable model:
```


 1/**




 2 * The tax rates that should apply to the customer's subscriptions.




 3 *




 4 * @return array<string, array<int, string>>




 5 */




 6public function priceTaxRates(): array




 7{




 8    return [




 9        'price_monthly' => ['txr_id'],




10    ];




11}




/**
 * The tax rates that should apply to the customer's subscriptions.
 *
 * @return array<string, array<int, string>>
 */
public function priceTaxRates(): array
{
    return [
        'price_monthly' => ['txr_id'],
    ];
}

```

The `taxRates` method only applies to subscription charges. If you use Cashier to make "one-off" charges, you will need to manually specify the tax rate at that time.
#### [Syncing Tax Rates](https://laravel.com/docs/12.x/billing#syncing-tax-rates)
When changing the hard-coded tax rate IDs returned by the `taxRates` method, the tax settings on any existing subscriptions for the user will remain the same. If you wish to update the tax value for existing subscriptions with the new `taxRates` values, you should call the `syncTaxRates` method on the user's subscription instance:
```


1$user->subscription('default')->syncTaxRates();




$user->subscription('default')->syncTaxRates();

```

This will also sync any item tax rates for a subscription with multiple products. If your application is offering subscriptions with multiple products, you should ensure that your billable model implements the `priceTaxRates` method [discussed above](https://laravel.com/docs/12.x/billing#subscription-taxes).
#### [Tax Exemption](https://laravel.com/docs/12.x/billing#tax-exemption)
Cashier also offers the `isNotTaxExempt`, `isTaxExempt`, and `reverseChargeApplies` methods to determine if the customer is tax exempt. These methods will call the Stripe API to determine a customer's tax exemption status:
```


1use App\Models\User;




2 



3$user = User::find(1);




4 



5$user->isTaxExempt();




6$user->isNotTaxExempt();




7$user->reverseChargeApplies();




use App\Models\User;

$user = User::find(1);

$user->isTaxExempt();
$user->isNotTaxExempt();
$user->reverseChargeApplies();

```

These methods are also available on any `Laravel\Cashier\Invoice` object. However, when invoked on an `Invoice` object, the methods will determine the exemption status at the time the invoice was created.
### [Subscription Anchor Date](https://laravel.com/docs/12.x/billing#subscription-anchor-date)
By default, the billing cycle anchor is the date the subscription was created or, if a trial period is used, the date that the trial ends. If you would like to modify the billing anchor date, you may use the `anchorBillingCycleOn` method:
```


 1use Illuminate\Http\Request;




 2 



 3Route::post('/user/subscribe', function (Request $request) {




 4    $anchor = Carbon::parse('first day of next month');




 5 



 6    $request->user()->newSubscription('default', 'price_monthly')




 7        ->anchorBillingCycleOn($anchor->startOfDay())




 8        ->create($request->paymentMethodId);




 9 



10    // ...




11});




use Illuminate\Http\Request;

Route::post('/user/subscribe', function (Request $request) {
    $anchor = Carbon::parse('first day of next month');

    $request->user()->newSubscription('default', 'price_monthly')
        ->anchorBillingCycleOn($anchor->startOfDay())
        ->create($request->paymentMethodId);

    // ...
});

```

For more information on managing subscription billing cycles, consult the
### [Cancelling Subscriptions](https://laravel.com/docs/12.x/billing#cancelling-subscriptions)
To cancel a subscription, call the `cancel` method on the user's subscription:
```


1$user->subscription('default')->cancel();




$user->subscription('default')->cancel();

```

When a subscription is canceled, Cashier will automatically set the `ends_at` column in your `subscriptions` database table. This column is used to know when the `subscribed` method should begin returning `false`.
For example, if a customer cancels a subscription on March 1st, but the subscription was not scheduled to end until March 5th, the `subscribed` method will continue to return `true` until March 5th. This is done because a user is typically allowed to continue using an application until the end of their billing cycle.
You may determine if a user has canceled their subscription but are still on their "grace period" using the `onGracePeriod` method:
```


1if ($user->subscription('default')->onGracePeriod()) {




2    // ...




3}




if ($user->subscription('default')->onGracePeriod()) {
    // ...
}

```

If you wish to cancel a subscription immediately, call the `cancelNow` method on the user's subscription:
```


1$user->subscription('default')->cancelNow();




$user->subscription('default')->cancelNow();

```

If you wish to cancel a subscription immediately and invoice any remaining un-invoiced metered usage or new / pending proration invoice items, call the `cancelNowAndInvoice` method on the user's subscription:
```


1$user->subscription('default')->cancelNowAndInvoice();




$user->subscription('default')->cancelNowAndInvoice();

```

You may also choose to cancel the subscription at a specific moment in time:
```


1$user->subscription('default')->cancelAt(




2    now()->plus(days: 10)




3);




$user->subscription('default')->cancelAt(
    now()->plus(days: 10)
);

```

Finally, you should always cancel user subscriptions before deleting the associated user model:
```


1$user->subscription('default')->cancelNow();




2 



3$user->delete();




$user->subscription('default')->cancelNow();

$user->delete();

```

### [Resuming Subscriptions](https://laravel.com/docs/12.x/billing#resuming-subscriptions)
If a customer has canceled their subscription and you wish to resume it, you may invoke the `resume` method on the subscription. The customer must still be within their "grace period" in order to resume a subscription:
```


1$user->subscription('default')->resume();




$user->subscription('default')->resume();

```

If the customer cancels a subscription and then resumes that subscription before the subscription has fully expired the customer will not be billed immediately. Instead, their subscription will be re-activated and they will be billed on the original billing cycle.
