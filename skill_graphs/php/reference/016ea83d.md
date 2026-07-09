## [Rendering Mailables](https://laravel.com/docs/12.x/mail#rendering-mailables)
Sometimes you may wish to capture the HTML content of a mailable without sending it. To accomplish this, you may call the `render` method of the mailable. This method will return the evaluated HTML content of the mailable as a string:
```


1use App\Mail\InvoicePaid;




2use App\Models\Invoice;




3 



4$invoice = Invoice::find(1);




5 



6return (new InvoicePaid($invoice))->render();




use App\Mail\InvoicePaid;
use App\Models\Invoice;

$invoice = Invoice::find(1);

return (new InvoicePaid($invoice))->render();

```

### [Previewing Mailables in the Browser](https://laravel.com/docs/12.x/mail#previewing-mailables-in-the-browser)
When designing a mailable's template, it is convenient to quickly preview the rendered mailable in your browser like a typical Blade template. For this reason, Laravel allows you to return any mailable directly from a route closure or controller. When a mailable is returned, it will be rendered and displayed in the browser, allowing you to quickly preview its design without needing to send it to an actual email address:
```


1Route::get('/mailable', function () {




2    $invoice = App\Models\Invoice::find(1);




3 



4    return new App\Mail\InvoicePaid($invoice);




5});




Route::get('/mailable', function () {
    $invoice = App\Models\Invoice::find(1);

    return new App\Mail\InvoicePaid($invoice);
});

```
