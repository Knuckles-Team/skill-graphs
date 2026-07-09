## [Customers](https://laravel.com/docs/12.x/cashier-paddle#customers)
### [Customer Defaults](https://laravel.com/docs/12.x/cashier-paddle#customer-defaults)
Cashier allows you to define some useful defaults for your customers when creating checkout sessions. Setting these defaults allow you to pre-fill a customer's email address and name so that they can immediately move on to the payment portion of the checkout widget. You can set these defaults by overriding the following methods on your billable model:
```


 1/**




 2 * Get the customer's name to associate with Paddle.




 3 */




 4public function paddleName(): string|null




 5{




 6    return $this->name;




 7}




 8 



 9/**




10 * Get the customer's email address to associate with Paddle.




11 */




12public function paddleEmail(): string|null




13{




14    return $this->email;




15}




/**
 * Get the customer's name to associate with Paddle.
 */
public function paddleName(): string|null
{
    return $this->name;
}

/**
 * Get the customer's email address to associate with Paddle.
 */
public function paddleEmail(): string|null
{
    return $this->email;
}

```

These defaults will be used for every action in Cashier that generates a [checkout session](https://laravel.com/docs/12.x/cashier-paddle#checkout-sessions).
### [Retrieving Customers](https://laravel.com/docs/12.x/cashier-paddle#retrieving-customers)
You can retrieve a customer by their Paddle Customer ID using the `Cashier::findBillable` method. This method will return an instance of the billable model:
```


1use Laravel\Paddle\Cashier;




2 



3$user = Cashier::findBillable($customerId);




use Laravel\Paddle\Cashier;

$user = Cashier::findBillable($customerId);

```

### [Creating Customers](https://laravel.com/docs/12.x/cashier-paddle#creating-customers)
Occasionally, you may wish to create a Paddle customer without beginning a subscription. You may accomplish this using the `createAsCustomer` method:
```


1$customer = $user->createAsCustomer();




$customer = $user->createAsCustomer();

```

An instance of `Laravel\Paddle\Customer` is returned. Once the customer has been created in Paddle, you may begin a subscription at a later date. You may provide an optional `$options` array to pass in any additional
```


1$customer = $user->createAsCustomer($options);




$customer = $user->createAsCustomer($options);

```
