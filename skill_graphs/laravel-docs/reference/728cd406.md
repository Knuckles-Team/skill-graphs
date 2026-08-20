## [Customers](https://laravel.com/docs/12.x/billing#customers)
### [Retrieving Customers](https://laravel.com/docs/12.x/billing#retrieving-customers)
You can retrieve a customer by their Stripe ID using the `Cashier::findBillable` method. This method will return an instance of the billable model:
```


1use Laravel\Cashier\Cashier;




2 



3$user = Cashier::findBillable($stripeId);




use Laravel\Cashier\Cashier;

$user = Cashier::findBillable($stripeId);

```

### [Creating Customers](https://laravel.com/docs/12.x/billing#creating-customers)
Occasionally, you may wish to create a Stripe customer without beginning a subscription. You may accomplish this using the `createAsStripeCustomer` method:
```


1$stripeCustomer = $user->createAsStripeCustomer();




$stripeCustomer = $user->createAsStripeCustomer();

```

Once the customer has been created in Stripe, you may begin a subscription at a later date. You may provide an optional `$options` array to pass in any additional
```


1$stripeCustomer = $user->createAsStripeCustomer($options);




$stripeCustomer = $user->createAsStripeCustomer($options);

```

You may use the `asStripeCustomer` method if you want to return the Stripe customer object for a billable model:
```


1$stripeCustomer = $user->asStripeCustomer();




$stripeCustomer = $user->asStripeCustomer();

```

The `createOrGetStripeCustomer` method may be used if you would like to retrieve the Stripe customer object for a given billable model but are not sure whether the billable model is already a customer within Stripe. This method will create a new customer in Stripe if one does not already exist:
```


1$stripeCustomer = $user->createOrGetStripeCustomer();




$stripeCustomer = $user->createOrGetStripeCustomer();

```

### [Updating Customers](https://laravel.com/docs/12.x/billing#updating-customers)
Occasionally, you may wish to update the Stripe customer directly with additional information. You may accomplish this using the `updateStripeCustomer` method. This method accepts an array of
```


1$stripeCustomer = $user->updateStripeCustomer($options);




$stripeCustomer = $user->updateStripeCustomer($options);

```

### [Balances](https://laravel.com/docs/12.x/billing#balances)
Stripe allows you to credit or debit a customer's "balance". Later, this balance will be credited or debited on new invoices. To check the customer's total balance you may use the `balance` method that is available on your billable model. The `balance` method will return a formatted string representation of the balance in the customer's currency:
```


1$balance = $user->balance();




$balance = $user->balance();

```

To credit a customer's balance, you may provide a value to the `creditBalance` method. If you wish, you may also provide a description:
```


1$user->creditBalance(500, 'Premium customer top-up.');




$user->creditBalance(500, 'Premium customer top-up.');

```

Providing a value to the `debitBalance` method will debit the customer's balance:
```


1$user->debitBalance(300, 'Bad usage penalty.');




$user->debitBalance(300, 'Bad usage penalty.');

```

The `applyBalance` method will create new customer balance transactions for the customer. You may retrieve these transaction records using the `balanceTransactions` method, which may be useful in order to provide a log of credits and debits for the customer to review:
```


 1// Retrieve all transactions...




 2$transactions = $user->balanceTransactions();




 3 



 4foreach ($transactions as $transaction) {




 5    // Transaction amount...




 6    $amount = $transaction->amount(); // $2.31




 7 



 8    // Retrieve the related invoice when available...




 9    $invoice = $transaction->invoice();




10}




// Retrieve all transactions...
$transactions = $user->balanceTransactions();

foreach ($transactions as $transaction) {
    // Transaction amount...
    $amount = $transaction->amount(); // $2.31

    // Retrieve the related invoice when available...
    $invoice = $transaction->invoice();
}

```

### [Tax IDs](https://laravel.com/docs/12.x/billing#tax-ids)
Cashier offers an easy way to manage a customer's tax IDs. For example, the `taxIds` method may be used to retrieve all of the
```


1$taxIds = $user->taxIds();




$taxIds = $user->taxIds();

```

You can also retrieve a specific tax ID for a customer by its identifier:
```


1$taxId = $user->findTaxId('txi_belgium');




$taxId = $user->findTaxId('txi_belgium');

```

You may create a new Tax ID by providing a valid `createTaxId` method:
```


1$taxId = $user->createTaxId('eu_vat', 'BE0123456789');




$taxId = $user->createTaxId('eu_vat', 'BE0123456789');

```

The `createTaxId` method will immediately add the VAT ID to the customer's account. `customer.tax_id.updated` webhook event and inspecting [documentation on defining webhook handlers](https://laravel.com/docs/12.x/billing#handling-stripe-webhooks).
You may delete a tax ID using the `deleteTaxId` method:
```


1$user->deleteTaxId('txi_belgium');




$user->deleteTaxId('txi_belgium');

```

### [Syncing Customer Data With Stripe](https://laravel.com/docs/12.x/billing#syncing-customer-data-with-stripe)
Typically, when your application's users update their name, email address, or other information that is also stored by Stripe, you should inform Stripe of the updates. By doing so, Stripe's copy of the information will be in sync with your application's.
To automate this, you may define an event listener on your billable model that reacts to the model's `updated` event. Then, within your event listener, you may invoke the `syncStripeCustomerDetails` method on the model:
```


 1use App\Models\User;




 2use function Illuminate\Events\queueable;




 3 



 4/**




 5 * The "booted" method of the model.




 6 */




 7protected static function booted(): void




 8{




 9    static::updated(queueable(function (User $customer) {




10        if ($customer->hasStripeId()) {




11            $customer->syncStripeCustomerDetails();




12        }




13    }));




14}




use App\Models\User;
use function Illuminate\Events\queueable;

/**
 * The "booted" method of the model.
 */
protected static function booted(): void
{
    static::updated(queueable(function (User $customer) {
        if ($customer->hasStripeId()) {
            $customer->syncStripeCustomerDetails();
        }
    }));
}

```

Now, every time your customer model is updated, its information will be synced with Stripe. For convenience, Cashier will automatically sync your customer's information with Stripe on the initial creation of the customer.
You may customize the columns used for syncing customer information to Stripe by overriding a variety of methods provided by Cashier. For example, you may override the `stripeName` method to customize the attribute that should be considered the customer's "name" when Cashier syncs customer information to Stripe:
```


1/**




2 * Get the customer name that should be synced to Stripe.




3 */




4public function stripeName(): string|null




5{




6    return $this->company_name;




7}




/**
 * Get the customer name that should be synced to Stripe.
 */
public function stripeName(): string|null
{
    return $this->company_name;
}

```

Similarly, you may override the `stripeEmail`, `stripePhone` (20 character maximum), `stripeAddress`, and `stripePreferredLocales` methods. These methods will sync information to their corresponding customer parameters when `syncStripeCustomerDetails` method.
### [Billing Portal](https://laravel.com/docs/12.x/billing#billing-portal)
Stripe offers `redirectToBillingPortal` method on the billable model from a controller or route:
```


1use Illuminate\Http\Request;




2 



3Route::get('/billing-portal', function (Request $request) {




4    return $request->user()->redirectToBillingPortal();




5});




use Illuminate\Http\Request;

Route::get('/billing-portal', function (Request $request) {
    return $request->user()->redirectToBillingPortal();
});

```

By default, when the user is finished managing their subscription, they will be able to return to the `home` route of your application via a link within the Stripe billing portal. You may provide a custom URL that the user should return to by passing the URL as an argument to the `redirectToBillingPortal` method:
```


1use Illuminate\Http\Request;




2 



3Route::get('/billing-portal', function (Request $request) {




4    return $request->user()->redirectToBillingPortal(route('billing'));




5});




use Illuminate\Http\Request;

Route::get('/billing-portal', function (Request $request) {
    return $request->user()->redirectToBillingPortal(route('billing'));
});

```

If you would like to generate the URL to the billing portal without generating an HTTP redirect response, you may invoke the `billingPortalUrl` method:
```


1$url = $request->user()->billingPortalUrl(route('billing'));




$url = $request->user()->billingPortalUrl(route('billing'));

```
