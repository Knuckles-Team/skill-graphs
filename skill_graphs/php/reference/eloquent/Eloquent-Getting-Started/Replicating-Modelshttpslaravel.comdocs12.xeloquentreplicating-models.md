## [Replicating Models](https://laravel.com/docs/12.x/eloquent#replicating-models)
You may create an unsaved copy of an existing model instance using the `replicate` method. This method is particularly useful when you have model instances that share many of the same attributes:
```


 1use App\Models\Address;




 2 



 3$shipping = Address::create([




 4    'type' => 'shipping',




 5    'line_1' => '123 Example Street',




 6    'city' => 'Victorville',




 7    'state' => 'CA',




 8    'postcode' => '90001',




 9]);




10 



11$billing = $shipping->replicate()->fill([




12    'type' => 'billing'




13]);




14 



15$billing->save();




use App\Models\Address;

$shipping = Address::create([
    'type' => 'shipping',
    'line_1' => '123 Example Street',
    'city' => 'Victorville',
    'state' => 'CA',
    'postcode' => '90001',
]);

$billing = $shipping->replicate()->fill([
    'type' => 'billing'
]);

$billing->save();

```

To exclude one or more attributes from being replicated to the new model, you may pass an array to the `replicate` method:
```


 1$flight = Flight::create([




 2    'destination' => 'LAX',




 3    'origin' => 'LHR',




 4    'last_flown' => '2020-03-04 11:00:00',




 5    'last_pilot_id' => 747,




 6]);




 7 



 8$flight = $flight->replicate([




 9    'last_flown',




10    'last_pilot_id'




11]);




$flight = Flight::create([
    'destination' => 'LAX',
    'origin' => 'LHR',
    'last_flown' => '2020-03-04 11:00:00',
    'last_pilot_id' => 747,
]);

$flight = $flight->replicate([
    'last_flown',
    'last_pilot_id'
]);

```
