## [Subscription Trials](https://laravel.com/docs/12.x/cashier-paddle#subscription-trials)
### [With Payment Method Up Front](https://laravel.com/docs/12.x/cashier-paddle#with-payment-method-up-front)
If you would like to offer trial periods to your customers while still collecting payment method information up front, you should use set a trial time in the Paddle dashboard on the price your customer is subscribing to. Then, initiate the checkout session as normal:
```


1use Illuminate\Http\Request;




2 



3Route::get('/user/subscribe', function (Request $request) {




4    $checkout = $request->user()




5        ->subscribe('pri_monthly')




6        ->returnTo(route('home'));




7 



8    return view('billing', ['checkout' => $checkout]);




9});




use Illuminate\Http\Request;

Route::get('/user/subscribe', function (Request $request) {
    $checkout = $request->user()
        ->subscribe('pri_monthly')
        ->returnTo(route('home'));

    return view('billing', ['checkout' => $checkout]);
});

```

When your application receives the `subscription_created` event, Cashier will set the trial period ending date on the subscription record within your application's database as well as instruct Paddle to not begin billing the customer until after this date.
If the customer's subscription is not canceled before the trial ending date they will be charged as soon as the trial expires, so you should be sure to notify your users of their trial ending date.
You may determine if the user is within their trial period using either the `onTrial` method of the user instance:
```


1if ($user->onTrial()) {




2    // ...




3}




if ($user->onTrial()) {
    // ...
}

```

To determine if an existing trial has expired, you may use the `hasExpiredTrial` methods:
```


1if ($user->hasExpiredTrial()) {




2    // ...




3}




if ($user->hasExpiredTrial()) {
    // ...
}

```

To determine if a user is on trial for a specific subscription type, you may provide the type to the `onTrial` or `hasExpiredTrial` methods:
```


1if ($user->onTrial('default')) {




2    // ...




3}




4 



5if ($user->hasExpiredTrial('default')) {




6    // ...




7}




if ($user->onTrial('default')) {
    // ...
}

if ($user->hasExpiredTrial('default')) {
    // ...
}

```

### [Without Payment Method Up Front](https://laravel.com/docs/12.x/cashier-paddle#without-payment-method-up-front)
If you would like to offer trial periods without collecting the user's payment method information up front, you may set the `trial_ends_at` column on the customer record attached to your user to your desired trial ending date. This is typically done during user registration:
```


1use App\Models\User;




2 



3$user = User::create([




4    // ...




5]);




6 



7$user->createAsCustomer([




8    'trial_ends_at' => now()->plus(days: 10)




9]);




use App\Models\User;

$user = User::create([
    // ...
]);

$user->createAsCustomer([
    'trial_ends_at' => now()->plus(days: 10)
]);

```

Cashier refers to this type of trial as a "generic trial", since it is not attached to any existing subscription. The `onTrial` method on the `User` instance will return `true` if the current date is not past the value of `trial_ends_at`:
```


1if ($user->onTrial()) {




2    // User is within their trial period...




3}




if ($user->onTrial()) {
    // User is within their trial period...
}

```

Once you are ready to create an actual subscription for the user, you may use the `subscribe` method as usual:
```


1use Illuminate\Http\Request;




2 



3Route::get('/user/subscribe', function (Request $request) {




4    $checkout = $request->user()




5        ->subscribe('pri_monthly')




6        ->returnTo(route('home'));




7 



8    return view('billing', ['checkout' => $checkout]);




9});




use Illuminate\Http\Request;

Route::get('/user/subscribe', function (Request $request) {
    $checkout = $request->user()
        ->subscribe('pri_monthly')
        ->returnTo(route('home'));

    return view('billing', ['checkout' => $checkout]);
});

```

To retrieve the user's trial ending date, you may use the `trialEndsAt` method. This method will return a Carbon date instance if a user is on a trial or `null` if they aren't. You may also pass an optional subscription type parameter if you would like to get the trial ending date for a specific subscription other than the default one:
```


1if ($user->onTrial('default')) {




2    $trialEndsAt = $user->trialEndsAt();




3}




if ($user->onTrial('default')) {
    $trialEndsAt = $user->trialEndsAt();
}

```

You may use the `onGenericTrial` method if you wish to know specifically that the user is within their "generic" trial period and has not created an actual subscription yet:
```


1if ($user->onGenericTrial()) {




2    // User is within their "generic" trial period...




3}




if ($user->onGenericTrial()) {
    // User is within their "generic" trial period...
}

```

### [Extend or Activate a Trial](https://laravel.com/docs/12.x/cashier-paddle#extend-or-activate-a-trial)
You can extend an existing trial period on a subscription by invoking the `extendTrial` method and specifying the moment in time that the trial should end:
```


1$user->subscription()->extendTrial(now()->plus(days: 5));




$user->subscription()->extendTrial(now()->plus(days: 5));

```

Or, you may immediately activate a subscription by ending its trial by calling the `activate` method on the subscription:
```


1$user->subscription()->activate();




$user->subscription()->activate();

```
