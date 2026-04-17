## [Updating Values](https://laravel.com/docs/12.x/pennant#updating-values)
When a feature's value is resolved for the first time, the underlying driver will store the result in storage. This is often necessary to ensure a consistent experience for your users across requests. However, at times, you may want to manually update the feature's stored value.
To accomplish this, you may use the `activate` and `deactivate` methods to toggle a feature "on" or "off":
```


1use Laravel\Pennant\Feature;




2 



3// Activate the feature for the default scope...




4Feature::activate('new-api');




5 



6// Deactivate the feature for the given scope...




7Feature::for($user->team)->deactivate('billing-v2');




use Laravel\Pennant\Feature;

// Activate the feature for the default scope...
Feature::activate('new-api');

// Deactivate the feature for the given scope...
Feature::for($user->team)->deactivate('billing-v2');

```

It is also possible to manually set a rich value for a feature by providing a second argument to the `activate` method:
```


1Feature::activate('purchase-button', 'seafoam-green');




Feature::activate('purchase-button', 'seafoam-green');

```

To instruct Pennant to forget the stored value for a feature, you may use the `forget` method. When the feature is checked again, Pennant will resolve the feature's value from its feature definition:
```


1Feature::forget('purchase-button');




Feature::forget('purchase-button');

```

### [Bulk Updates](https://laravel.com/docs/12.x/pennant#bulk-updates)
To update stored feature values in bulk, you may use the `activateForEveryone` and `deactivateForEveryone` methods.
For example, imagine you are now confident in the `new-api` feature's stability and have landed on the best `'purchase-button'` color for your checkout flow - you can update the stored value for all users accordingly:
```


1use Laravel\Pennant\Feature;




2 



3Feature::activateForEveryone('new-api');




4 



5Feature::activateForEveryone('purchase-button', 'seafoam-green');




use Laravel\Pennant\Feature;

Feature::activateForEveryone('new-api');

Feature::activateForEveryone('purchase-button', 'seafoam-green');

```

Alternatively, you may deactivate the feature for all users:
```


1Feature::deactivateForEveryone('new-api');




Feature::deactivateForEveryone('new-api');

```

This will only update the resolved feature values that have been stored by Pennant's storage driver. You will also need to update the feature definition in your application.
### [Purging Features](https://laravel.com/docs/12.x/pennant#purging-features)
Sometimes, it can be useful to purge an entire feature from storage. This is typically necessary if you have removed the feature from your application or you have made adjustments to the feature's definition that you would like to rollout to all users.
You may remove all stored values for a feature using the `purge` method:
```


1// Purging a single feature...




2Feature::purge('new-api');




3 



4// Purging multiple features...




5Feature::purge(['new-api', 'purchase-button']);




// Purging a single feature...
Feature::purge('new-api');

// Purging multiple features...
Feature::purge(['new-api', 'purchase-button']);

```

If you would like to purge _all_ features from storage, you may invoke the `purge` method without any arguments:
```


1Feature::purge();




Feature::purge();

```

As it can be useful to purge features as part of your application's deployment pipeline, Pennant includes a `pennant:purge` Artisan command which will purge the provided features from storage:
```


1php artisan pennant:purge new-api




2 



3php artisan pennant:purge new-api purchase-button




php artisan pennant:purge new-api

php artisan pennant:purge new-api purchase-button

```

It is also possible to purge all features _except_ those in a given feature list. For example, imagine you wanted to purge all features but keep the values for the "new-api" and "purchase-button" features in storage. To accomplish this, you can pass those feature names to the `--except` option:
```


1php artisan pennant:purge --except=new-api --except=purchase-button




php artisan pennant:purge --except=new-api --except=purchase-button

```

For convenience, the `pennant:purge` command also supports an `--except-registered` flag. This flag indicates that all features except those explicitly registered in a service provider should be purged:
```


1php artisan pennant:purge --except-registered




php artisan pennant:purge --except-registered

```
