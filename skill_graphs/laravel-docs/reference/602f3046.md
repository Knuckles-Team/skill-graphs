## [Transactions](https://laravel.com/docs/12.x/cashier-paddle#transactions)
You may easily retrieve an array of a billable model's transactions via the `transactions` property:
```


1use App\Models\User;




2 



3$user = User::find(1);




4 



5$transactions = $user->transactions;




use App\Models\User;

$user = User::find(1);

$transactions = $user->transactions;

```

Transactions represent payments for your products and purchases and are accompanied by invoices. Only completed transactions are stored in your application's database.
When listing the transactions for a customer, you may use the transaction instance's methods to display the relevant payment information. For example, you may wish to list every transaction in a table, allowing the user to easily download any of the invoices:
```


 1<table>




 2    @foreach ($transactions as $transaction)




 3        <tr>




 4            <td>{{ $transaction->billed_at->toFormattedDateString() }}</td>




 5            <td>{{ $transaction->total() }}</td>




 6            <td>{{ $transaction->tax() }}</td>




 7            <td><a href="{{ route('download-invoice', $transaction->id) }}" target="_blank">Download</a></td>




 8        </tr>




 9    @endforeach




10</table>




<table>
    @foreach ($transactions as $transaction)
        <tr>
            <td>{{ $transaction->billed_at->toFormattedDateString() }}</td>
            <td>{{ $transaction->total() }}</td>
            <td>{{ $transaction->tax() }}</td>
            <td><a href="{{ route('download-invoice', $transaction->id) }}" target="_blank">Download</a></td>
        </tr>
    @endforeach
</table>

```

The `download-invoice` route may look like the following:
```


1use Illuminate\Http\Request;




2use Laravel\Paddle\Transaction;




3 



4Route::get('/download-invoice/{transaction}', function (Request $request, Transaction $transaction) {




5    return $transaction->redirectToInvoicePdf();




6})->name('download-invoice');




use Illuminate\Http\Request;
use Laravel\Paddle\Transaction;

Route::get('/download-invoice/{transaction}', function (Request $request, Transaction $transaction) {
    return $transaction->redirectToInvoicePdf();
})->name('download-invoice');

```

### [Past and Upcoming Payments](https://laravel.com/docs/12.x/cashier-paddle#past-and-upcoming-payments)
You may use the `lastPayment` and `nextPayment` methods to retrieve and display a customer's past or upcoming payments for recurring subscriptions:
```


1use App\Models\User;




2 



3$user = User::find(1);




4 



5$subscription = $user->subscription();




6 



7$lastPayment = $subscription->lastPayment();




8$nextPayment = $subscription->nextPayment();




use App\Models\User;

$user = User::find(1);

$subscription = $user->subscription();

$lastPayment = $subscription->lastPayment();
$nextPayment = $subscription->nextPayment();

```

Both of these methods will return an instance of `Laravel\Paddle\Payment`; however, `lastPayment` will return `null` when transactions have not been synced by webhooks yet, while `nextPayment` will return `null` when the billing cycle has ended (such as when a subscription has been canceled):
```


1Next payment: {{ $nextPayment->amount() }} due on {{ $nextPayment->date()->format('d/m/Y') }}




Next payment: {{ $nextPayment->amount() }} due on {{ $nextPayment->date()->format('d/m/Y') }}

```
