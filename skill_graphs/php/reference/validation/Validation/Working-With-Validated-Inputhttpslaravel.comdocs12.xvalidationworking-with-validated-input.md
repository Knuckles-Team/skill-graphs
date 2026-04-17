## [Working With Validated Input](https://laravel.com/docs/12.x/validation#working-with-validated-input)
After validating incoming request data using a form request or a manually created validator instance, you may wish to retrieve the incoming request data that actually underwent validation. This can be accomplished in several ways. First, you may call the `validated` method on a form request or validator instance. This method returns an array of the data that was validated:
```


1$validated = $request->validated();




2 



3$validated = $validator->validated();




$validated = $request->validated();

$validated = $validator->validated();

```

Alternatively, you may call the `safe` method on a form request or validator instance. This method returns an instance of `Illuminate\Support\ValidatedInput`. This object exposes `only`, `except`, and `all` methods to retrieve a subset of the validated data or the entire array of validated data:
```


1$validated = $request->safe()->only(['name', 'email']);




2 



3$validated = $request->safe()->except(['name', 'email']);




4 



5$validated = $request->safe()->all();




$validated = $request->safe()->only(['name', 'email']);

$validated = $request->safe()->except(['name', 'email']);

$validated = $request->safe()->all();

```

In addition, the `Illuminate\Support\ValidatedInput` instance may be iterated over and accessed like an array:
```


1// Validated data may be iterated...




2foreach ($request->safe() as $key => $value) {




3    // ...




4}




5 



6// Validated data may be accessed as an array...




7$validated = $request->safe();




8 



9$email = $validated['email'];




// Validated data may be iterated...
foreach ($request->safe() as $key => $value) {
    // ...
}

// Validated data may be accessed as an array...
$validated = $request->safe();

$email = $validated['email'];

```

If you would like to add additional fields to the validated data, you may call the `merge` method:
```


1$validated = $request->safe()->merge(['name' => 'Taylor Otwell']);




$validated = $request->safe()->merge(['name' => 'Taylor Otwell']);

```

If you would like to retrieve the validated data as a [collection](https://laravel.com/docs/12.x/collections) instance, you may call the `collect` method:
```


1$collection = $request->safe()->collect();




$collection = $request->safe()->collect();

```
