## [Invoices](https://laravel.com/docs/12.x/billing#invoices)
### [Retrieving Invoices](https://laravel.com/docs/12.x/billing#retrieving-invoices)
You may easily retrieve an array of a billable model's invoices using the `invoices` method. The `invoices` method returns a collection of `Laravel\Cashier\Invoice` instances:
```


1$invoices = $user->invoices();




$invoices = $user->invoices();

```

If you would like to include pending invoices in the results, you may use the `invoicesIncludingPending` method:
```


1$invoices = $user->invoicesIncludingPending();




$invoices = $user->invoicesIncludingPending();

```

You may use the `findInvoice` method to retrieve a specific invoice by its ID:
```


1$invoice = $user->findInvoice($invoiceId);




$invoice = $user->findInvoice($invoiceId);

```

#### [Displaying Invoice Information](https://laravel.com/docs/12.x/billing#displaying-invoice-information)
When listing the invoices for the customer, you may use the invoice's methods to display the relevant invoice information. For example, you may wish to list every invoice in a table, allowing the user to easily download any of them:
```


1<table>




2    @foreach ($invoices as $invoice)




3        <tr>




4            <td>{{ $invoice->date()->toFormattedDateString() }}</td>




5            <td>{{ $invoice->total() }}</td>




6            <td><a href="/user/invoice/{{ $invoice->id }}">Download</a></td>




7        </tr>




8    @endforeach




9</table>




<table>
    @foreach ($invoices as $invoice)
        <tr>
            <td>{{ $invoice->date()->toFormattedDateString() }}</td>
            <td>{{ $invoice->total() }}</td>
            <td><a href="/user/invoice/{{ $invoice->id }}">Download</a></td>
        </tr>
    @endforeach
</table>

```

### [Upcoming Invoices](https://laravel.com/docs/12.x/billing#upcoming-invoices)
To retrieve the upcoming invoice for a customer, you may use the `upcomingInvoice` method:
```


1$invoice = $user->upcomingInvoice();




$invoice = $user->upcomingInvoice();

```

Similarly, if the customer has multiple subscriptions, you can also retrieve the upcoming invoice for a specific subscription:
```


1$invoice = $user->subscription('default')->upcomingInvoice();




$invoice = $user->subscription('default')->upcomingInvoice();

```

### [Previewing Subscription Invoices](https://laravel.com/docs/12.x/billing#previewing-subscription-invoices)
Using the `previewInvoice` method, you can preview an invoice before making price changes. This will allow you to determine what your customer's invoice will look like when a given price change is made:
```


1$invoice = $user->subscription('default')->previewInvoice('price_yearly');




$invoice = $user->subscription('default')->previewInvoice('price_yearly');

```

You may pass an array of prices to the `previewInvoice` method in order to preview invoices with multiple new prices:
```


1$invoice = $user->subscription('default')->previewInvoice(['price_yearly', 'price_metered']);




$invoice = $user->subscription('default')->previewInvoice(['price_yearly', 'price_metered']);

```

### [Generating Invoice PDFs](https://laravel.com/docs/12.x/billing#generating-invoice-pdfs)
Before generating invoice PDFs, you should use Composer to install the Dompdf library, which is the default invoice renderer for Cashier:
```


1composer require dompdf/dompdf




composer require dompdf/dompdf

```

From within a route or controller, you may use the `downloadInvoice` method to generate a PDF download of a given invoice. This method will automatically generate the proper HTTP response needed to download the invoice:
```


1use Illuminate\Http\Request;




2 



3Route::get('/user/invoice/{invoice}', function (Request $request, string $invoiceId) {




4    return $request->user()->downloadInvoice($invoiceId);




5});




use Illuminate\Http\Request;

Route::get('/user/invoice/{invoice}', function (Request $request, string $invoiceId) {
    return $request->user()->downloadInvoice($invoiceId);
});

```

By default, all data on the invoice is derived from the customer and invoice data stored in Stripe. The filename is based on your `app.name` config value. However, you can customize some of this data by providing an array as the second argument to the `downloadInvoice` method. This array allows you to customize information such as your company and product details:
```


 1return $request->user()->downloadInvoice($invoiceId, [




 2    'vendor' => 'Your Company',




 3    'product' => 'Your Product',




 4    'street' => 'Main Str. 1',




 5    'location' => '2000 Antwerp, Belgium',




 6    'phone' => '+32 499 00 00 00',




 7    'email' => 'info@example.com',




 8    'url' => 'https://example.com',




 9    'vendorVat' => 'BE123456789',




10]);




return $request->user()->downloadInvoice($invoiceId, [
    'vendor' => 'Your Company',
    'product' => 'Your Product',
    'street' => 'Main Str. 1',
    'location' => '2000 Antwerp, Belgium',
    'phone' => '+32 499 00 00 00',
    'email' => 'info@example.com',
    'url' => 'https://example.com',
    'vendorVat' => 'BE123456789',
]);

```

The `downloadInvoice` method also allows for a custom filename via its third argument. This filename will automatically be suffixed with `.pdf`:
```


1return $request->user()->downloadInvoice($invoiceId, [], 'my-invoice');




return $request->user()->downloadInvoice($invoiceId, [], 'my-invoice');

```

#### [Custom Invoice Renderer](https://laravel.com/docs/12.x/billing#custom-invoice-render)
Cashier also makes it possible to use a custom invoice renderer. By default, Cashier uses the `DompdfInvoiceRenderer` implementation, which utilizes the `Laravel\Cashier\Contracts\InvoiceRenderer` interface. For example, you may wish to render an invoice PDF using an API call to a third-party PDF rendering service:
```


 1use Illuminate\Support\Facades\Http;




 2use Laravel\Cashier\Contracts\InvoiceRenderer;




 3use Laravel\Cashier\Invoice;




 4 



 5class ApiInvoiceRenderer implements InvoiceRenderer




 6{




 7    /**




 8     * Render the given invoice and return the raw PDF bytes.




 9     */




10    public function render(Invoice $invoice, array $data = [], array $options = []): string




11    {




12        $html = $invoice->view($data)->render();




13 



14        return Http::get('https://example.com/html-to-pdf', ['html' => $html])->get()->body();




15    }




16}




use Illuminate\Support\Facades\Http;
use Laravel\Cashier\Contracts\InvoiceRenderer;
use Laravel\Cashier\Invoice;

class ApiInvoiceRenderer implements InvoiceRenderer
{
    /**
     * Render the given invoice and return the raw PDF bytes.
     */
    public function render(Invoice $invoice, array $data = [], array $options = []): string
    {
        $html = $invoice->view($data)->render();

        return Http::get('https://example.com/html-to-pdf', ['html' => $html])->get()->body();
    }
}

```

Once you have implemented the invoice renderer contract, you should update the `cashier.invoices.renderer` configuration value in your application's `config/cashier.php` configuration file. This configuration value should be set to the class name of your custom renderer implementation.
