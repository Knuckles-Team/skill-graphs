## [Rich Feature Values](https://laravel.com/docs/12.x/pennant#rich-feature-values)
Until now, we have primarily shown features as being in a binary state, meaning they are either "active" or "inactive", but Pennant also allows you to store rich values as well.
For example, imagine you are testing three new colors for the "Buy now" button of your application. Instead of returning `true` or `false` from the feature definition, you may instead return a string:
```


1use Illuminate\Support\Arr;




2use Laravel\Pennant\Feature;




3 



4Feature::define('purchase-button', fn (User $user) => Arr::random([




5    'blue-sapphire',




6    'seafoam-green',




7    'tart-orange',




8]));




use Illuminate\Support\Arr;
use Laravel\Pennant\Feature;

Feature::define('purchase-button', fn (User $user) => Arr::random([
    'blue-sapphire',
    'seafoam-green',
    'tart-orange',
]));

```

You may retrieve the value of the `purchase-button` feature using the `value` method:
```


1$color = Feature::value('purchase-button');




$color = Feature::value('purchase-button');

```

Pennant's included Blade directive also makes it easy to conditionally render content based on the current value of the feature:
```


1@feature('purchase-button', 'blue-sapphire')




2    <!-- 'blue-sapphire' is active -->




3@elsefeature('purchase-button', 'seafoam-green')




4    <!-- 'seafoam-green' is active -->




5@elsefeature('purchase-button', 'tart-orange')




6    <!-- 'tart-orange' is active -->




7@endfeature




@feature('purchase-button', 'blue-sapphire')
    <!-- 'blue-sapphire' is active -->
@elsefeature('purchase-button', 'seafoam-green')
    <!-- 'seafoam-green' is active -->
@elsefeature('purchase-button', 'tart-orange')
    <!-- 'tart-orange' is active -->
@endfeature

```

When using rich values, it is important to know that a feature is considered "active" when it has any value other than `false`.
When calling the [conditional `when`](https://laravel.com/docs/12.x/pennant#conditional-execution) method, the feature's rich value will be provided to the first closure:
```


1Feature::when('purchase-button',




2    fn ($color) => /* ... */,




3    fn () => /* ... */,




4);




Feature::when('purchase-button',
    fn ($color) => /* ... */,
    fn () => /* ... */,
);

```

Likewise, when calling the conditional `unless` method, the feature's rich value will be provided to the optional second closure:
```


1Feature::unless('purchase-button',




2    fn () => /* ... */,




3    fn ($color) => /* ... */,




4);




Feature::unless('purchase-button',
    fn () => /* ... */,
    fn ($color) => /* ... */,
);

```
