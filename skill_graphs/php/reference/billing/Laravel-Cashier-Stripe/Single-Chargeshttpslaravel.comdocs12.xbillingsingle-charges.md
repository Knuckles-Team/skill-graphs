## [Single Charges](https://laravel.com/docs/12.x/billing#single-charges)
### [Simple Charge](https://laravel.com/docs/12.x/billing#simple-charge)
If you would like to make a one-time charge against a customer, you may use the `charge` method on a billable model instance. You will need to [provide a payment method identifier](https://laravel.com/docs/12.x/billing#payment-methods-for-single-charges) as the second argument to the `charge` method:
```


1use Illuminate\Http\Request;




2 



3Route::post('/purchase', function (Request $request) {




4    $stripeCharge = $request->user()->charge(




5        100, $request->paymentMethodId




6    );




7 



8    // ...




9});




use Illuminate\Http\Request;

Route::post('/purchase', function (Request $request) {
    $stripeCharge = $request->user()->charge(
        100, $request->paymentMethodId
    );

    // ...
});

```

The `charge` method accepts an array as its third argument, allowing you to pass any options you wish to the underlying Stripe charge creation. More information regarding the options available to you when creating charges may be found in the
```


1$user->charge(100, $paymentMethod, [




2    'custom_option' => $value,




3]);




$user->charge(100, $paymentMethod, [
    'custom_option' => $value,
]);

```

You may also use the `charge` method without an underlying customer or user. To accomplish this, invoke the `charge` method on a new instance of your application's billable model:
```


1use App\Models\User;




2 



3$stripeCharge = (new User)->charge(100, $paymentMethod);




use App\Models\User;

$stripeCharge = (new User)->charge(100, $paymentMethod);

```

The `charge` method will throw an exception if the charge fails. If the charge is successful, an instance of `Laravel\Cashier\Payment` will be returned from the method:
```


1try {




2    $payment = $user->charge(100, $paymentMethod);




3} catch (Exception $e) {




4    // ...




5}




try {
    $payment = $user->charge(100, $paymentMethod);
} catch (Exception $e) {
    // ...
}

```

The `charge` method accepts the payment amount in the lowest denominator of the currency used by your application. For example, if customers are paying in United States Dollars, amounts should be specified in pennies.
### [Charge With Invoice](https://laravel.com/docs/12.x/billing#charge-with-invoice)
Sometimes you may need to make a one-time charge and offer a PDF invoice to your customer. The `invoicePrice` method lets you do just that. For example, let's invoice a customer for five new shirts:
```


1$user->invoicePrice('price_tshirt', 5);




$user->invoicePrice('price_tshirt', 5);

```

The invoice will be immediately charged against the user's default payment method. The `invoicePrice` method also accepts an array as its third argument. This array contains the billing options for the invoice item. The fourth argument accepted by the method is also an array which should contain the billing options for the invoice itself:
```


1$user->invoicePrice('price_tshirt', 5, [




2    'discounts' => [




3        ['coupon' => 'SUMMER21SALE']




4    ],




5], [




6    'default_tax_rates' => ['txr_id'],




7]);




$user->invoicePrice('price_tshirt', 5, [
    'discounts' => [
        ['coupon' => 'SUMMER21SALE']
    ],
], [
    'default_tax_rates' => ['txr_id'],
]);

```

Similarly to `invoicePrice`, you may use the `tabPrice` method to create a one-time charge for multiple items (up to 250 items per invoice) by adding them to the customer's "tab" and then invoicing the customer. For example, we may invoice a customer for five shirts and two mugs:
```


1$user->tabPrice('price_tshirt', 5);




2$user->tabPrice('price_mug', 2);




3$user->invoice();




$user->tabPrice('price_tshirt', 5);
$user->tabPrice('price_mug', 2);
$user->invoice();

```

Alternatively, you may use the `invoiceFor` method to make a "one-off" charge against the customer's default payment method:
```


1$user->invoiceFor('One Time Fee', 500);




$user->invoiceFor('One Time Fee', 500);

```

Although the `invoiceFor` method is available for you to use, it is recommended that you use the `invoicePrice` and `tabPrice` methods with pre-defined prices. By doing so, you will have access to better analytics and data within your Stripe dashboard regarding your sales on a per-product basis.
The `invoice`, `invoicePrice`, and `invoiceFor` methods will create a Stripe invoice which will retry failed billing attempts. If you do not want invoices to retry failed charges, you will need to close them using the Stripe API after the first failed charge.
### [Creating Payment Intents](https://laravel.com/docs/12.x/billing#creating-payment-intents)
You can create a new Stripe payment intent by invoking the `pay` method on a billable model instance. Calling this method will create a payment intent that is wrapped in a `Laravel\Cashier\Payment` instance:
```


1use Illuminate\Http\Request;




2 



3Route::post('/pay', function (Request $request) {




4    $payment = $request->user()->pay(




5        $request->get('amount')




6    );




7 



8    return $payment->client_secret;




9});




use Illuminate\Http\Request;

Route::post('/pay', function (Request $request) {
    $payment = $request->user()->pay(
        $request->get('amount')
    );

    return $payment->client_secret;
});

```

After creating the payment intent, you can return the client secret to your application's frontend so that the user can complete the payment in their browser. To read more about building entire payment flows using Stripe payment intents, please consult the
When using the `pay` method, the default payment methods that are enabled within your Stripe dashboard will be available to the customer. Alternatively, if you only want to allow for some specific payment methods to be used, you may use the `payWith` method:
```


1use Illuminate\Http\Request;




2 



3Route::post('/pay', function (Request $request) {




4    $payment = $request->user()->payWith(




5        $request->get('amount'), ['card', 'bancontact']




6    );




7 



8    return $payment->client_secret;




9});




use Illuminate\Http\Request;

Route::post('/pay', function (Request $request) {
    $payment = $request->user()->payWith(
        $request->get('amount'), ['card', 'bancontact']
    );

    return $payment->client_secret;
});

```

The `pay` and `payWith` methods accept the payment amount in the lowest denominator of the currency used by your application. For example, if customers are paying in United States Dollars, amounts should be specified in pennies.
### [Refunding Charges](https://laravel.com/docs/12.x/billing#refunding-charges)
If you need to refund a Stripe charge, you may use the `refund` method. This method accepts the Stripe [payment intent ID](https://laravel.com/docs/12.x/billing#payment-methods-for-single-charges) as its first argument:
```


1$payment = $user->charge(100, $paymentMethodId);




2 



3$user->refund($payment->id);




$payment = $user->charge(100, $paymentMethodId);

$user->refund($payment->id);

```
