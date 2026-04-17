## [Price Previews](https://laravel.com/docs/12.x/cashier-paddle#price-previews)
Paddle allows you to customize prices per currency, essentially allowing you to configure different prices for different countries. Cashier Paddle allows you to retrieve all of these prices using the `previewPrices` method. This method accepts the price IDs you wish to retrieve prices for:
```


1use Laravel\Paddle\Cashier;




2 



3$prices = Cashier::previewPrices(['pri_123', 'pri_456']);




use Laravel\Paddle\Cashier;

$prices = Cashier::previewPrices(['pri_123', 'pri_456']);

```

The currency will be determined based on the IP address of the request; however, you may optionally provide a specific country to retrieve prices for:
```


1use Laravel\Paddle\Cashier;




2 



3$prices = Cashier::previewPrices(['pri_123', 'pri_456'], ['address' => [




4    'country_code' => 'BE',




5    'postal_code' => '1234',




6]]);




use Laravel\Paddle\Cashier;

$prices = Cashier::previewPrices(['pri_123', 'pri_456'], ['address' => [
    'country_code' => 'BE',
    'postal_code' => '1234',
]]);

```

After retrieving the prices you may display them however you wish:
```


1<ul>




2    @foreach ($prices as $price)




3        <li>{{ $price->product['name'] }} - {{ $price->total() }}</li>




4    @endforeach




5</ul>




<ul>
    @foreach ($prices as $price)
        <li>{{ $price->product['name'] }} - {{ $price->total() }}</li>
    @endforeach
</ul>

```

You may also display the subtotal price and tax amount separately:
```


1<ul>




2    @foreach ($prices as $price)




3        <li>{{ $price->product['name'] }} - {{ $price->subtotal() }} (+ {{ $price->tax() }} tax)</li>




4    @endforeach




5</ul>




<ul>
    @foreach ($prices as $price)
        <li>{{ $price->product['name'] }} - {{ $price->subtotal() }} (+ {{ $price->tax() }} tax)</li>
    @endforeach
</ul>

```

For more information,
### [Customer Price Previews](https://laravel.com/docs/12.x/cashier-paddle#customer-price-previews)
If a user is already a customer and you would like to display the prices that apply to that customer, you may do so by retrieving the prices directly from the customer instance:
```


1use App\Models\User;




2 



3$prices = User::find(1)->previewPrices(['pri_123', 'pri_456']);




use App\Models\User;

$prices = User::find(1)->previewPrices(['pri_123', 'pri_456']);

```

Internally, Cashier will use the user's customer ID to retrieve the prices in their currency. So, for example, a user living in the United States will see prices in US dollars while a user in Belgium will see prices in Euros. If no matching currency can be found, the default currency of the product will be used. You can customize all prices of a product or subscription plan in the Paddle control panel.
### [Discounts](https://laravel.com/docs/12.x/cashier-paddle#price-discounts)
You may also choose to display prices after a discount. When calling the `previewPrices` method, you provide the discount ID via the `discount_id` option:
```


1use Laravel\Paddle\Cashier;




2 



3$prices = Cashier::previewPrices(['pri_123', 'pri_456'], [




4    'discount_id' => 'dsc_123'




5]);




use Laravel\Paddle\Cashier;

$prices = Cashier::previewPrices(['pri_123', 'pri_456'], [
    'discount_id' => 'dsc_123'
]);

```

Then, display the calculated prices:
```


1<ul>




2    @foreach ($prices as $price)




3        <li>{{ $price->product['name'] }} - {{ $price->total() }}</li>




4    @endforeach




5</ul>




<ul>
    @foreach ($prices as $price)
        <li>{{ $price->product['name'] }} - {{ $price->total() }}</li>
    @endforeach
</ul>

```
