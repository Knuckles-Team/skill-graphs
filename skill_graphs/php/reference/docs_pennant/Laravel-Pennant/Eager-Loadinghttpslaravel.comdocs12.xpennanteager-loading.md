## [Eager Loading](https://laravel.com/docs/12.x/pennant#eager-loading)
Although Pennant keeps an in-memory cache of all resolved features for a single request, it is still possible to encounter performance issues. To alleviate this, Pennant offers the ability to eager load feature values.
To illustrate this, imagine that we are checking if a feature is active within a loop:
```


1use Laravel\Pennant\Feature;




2 



3foreach ($users as $user) {




4    if (Feature::for($user)->active('notifications-beta')) {




5        $user->notify(new RegistrationSuccess);




6    }




7}




use Laravel\Pennant\Feature;

foreach ($users as $user) {
    if (Feature::for($user)->active('notifications-beta')) {
        $user->notify(new RegistrationSuccess);
    }
}

```

Assuming we are using the database driver, this code will execute a database query for every user in the loop - executing potentially hundreds of queries. However, using Pennant's `load` method, we can remove this potential performance bottleneck by eager loading the feature values for a collection of users or scopes:
```


1Feature::for($users)->load(['notifications-beta']);




2 



3foreach ($users as $user) {




4    if (Feature::for($user)->active('notifications-beta')) {




5        $user->notify(new RegistrationSuccess);




6    }




7}




Feature::for($users)->load(['notifications-beta']);

foreach ($users as $user) {
    if (Feature::for($user)->active('notifications-beta')) {
        $user->notify(new RegistrationSuccess);
    }
}

```

To load feature values only when they have not already been loaded, you may use the `loadMissing` method:
```


1Feature::for($users)->loadMissing([




2    'new-api',




3    'purchase-button',




4    'notifications-beta',




5]);




Feature::for($users)->loadMissing([
    'new-api',
    'purchase-button',
    'notifications-beta',
]);

```

You may load all defined features using the `loadAll` method:
```


1Feature::for($users)->loadAll();




Feature::for($users)->loadAll();

```
