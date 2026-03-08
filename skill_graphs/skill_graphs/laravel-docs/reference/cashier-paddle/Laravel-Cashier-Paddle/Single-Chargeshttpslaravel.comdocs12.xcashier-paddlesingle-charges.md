## [Single Charges](https://laravel.com/docs/12.x/cashier-paddle#single-charges)
### [Charging for Products](https://laravel.com/docs/12.x/cashier-paddle#charging-for-products)
If you would like to initiate a product purchase for a customer, you may use the `checkout` method on a billable model instance to generate a checkout session for the purchase. The `checkout` method accepts one or multiple price ID's. If necessary, an associative array may be used to provide the quantity of the product that is being purchased:
```


1use Illuminate\Http\Request;




2 



3Route::get('/buy', function (Request $request) {




4    $checkout = $request->user()->checkout(['pri_tshirt', 'pri_socks' => 5]);




5 



6    return view('buy', ['checkout' => $checkout]);




7});




use Illuminate\Http\Request;

Route::get('/buy', function (Request $request) {
    $checkout = $request->user()->checkout(['pri_tshirt', 'pri_socks' => 5]);

    return view('buy', ['checkout' => $checkout]);
});

```

After generating the checkout session, you may use Cashier's provided `paddle-button` [Blade component](https://laravel.com/docs/12.x/cashier-paddle#overlay-checkout) to allow the user to view the Paddle checkout widget and complete the purchase:
```


1<x-paddle-button :checkout="$checkout" class="px-8 py-4">




2    Buy




3</x-paddle-button>




<x-paddle-button :checkout="$checkout" class="px-8 py-4">
    Buy
</x-paddle-button>

```

A checkout session has a `customData` method, allowing you to pass any custom data you wish to the underlying transaction creation. Please consult
```


1$checkout = $user->checkout('pri_tshirt')




2    ->customData([




3        'custom_option' => $value,




4    ]);




$checkout = $user->checkout('pri_tshirt')
    ->customData([
        'custom_option' => $value,
    ]);

```

### [Refunding Transactions](https://laravel.com/docs/12.x/cashier-paddle#refunding-transactions)
Refunding transactions will return the refunded amount to your customer's payment method that was used at the time of purchase. If you need to refund a Paddle purchase, you may use the `refund` method on a `Cashier\Paddle\Transaction` model. This method accepts a reason as the first argument, one or more price ID's to refund with optional amounts as an associative array. You may retrieve the transactions for a given billable model using the `transactions` method.
For example, imagine we want to refund a specific transaction for prices `pri_123` and `pri_456`. We want to fully refund `pri_123`, but only refund two dollars for `pri_456`:
```


 1use App\Models\User;




 2 



 3$user = User::find(1);




 4 



 5$transaction = $user->transactions()->first();




 6 



 7$response = $transaction->refund('Accidental charge', [




 8    'pri_123', // Fully refund this price...




 9    'pri_456' => 200, // Only partially refund this price...




10]);




use App\Models\User;

$user = User::find(1);

$transaction = $user->transactions()->first();

$response = $transaction->refund('Accidental charge', [
    'pri_123', // Fully refund this price...
    'pri_456' => 200, // Only partially refund this price...
]);

```

The example above refunds specific line items in a transaction. If you want to refund the entire transaction, simply provide a reason:
```


1$response = $transaction->refund('Accidental charge');




$response = $transaction->refund('Accidental charge');

```

For more information on refunds, please consult
Refunds must always be approved by Paddle before fully processing.
### [Crediting Transactions](https://laravel.com/docs/12.x/cashier-paddle#crediting-transactions)
Just like refunding, you can also credit transactions. Crediting transactions will add the funds to the customer's balance so it may be used for future purchases. Crediting transactions can only be done for manually-collected transactions and not for automatically-collected transactions (like subscriptions) since Paddle handles subscription credits automatically:
```


1$transaction = $user->transactions()->first();




2 



3// Credit a specific line item fully...




4$response = $transaction->credit('Compensation', 'pri_123');




$transaction = $user->transactions()->first();

// Credit a specific line item fully...
$response = $transaction->credit('Compensation', 'pri_123');

```

For more info,
Credits can only be applied for manually-collected transactions. Automatically-collected transactions are credited by Paddle themselves.
