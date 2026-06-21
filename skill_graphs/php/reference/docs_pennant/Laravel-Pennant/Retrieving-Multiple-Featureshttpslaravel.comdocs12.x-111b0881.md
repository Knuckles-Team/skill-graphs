## [Retrieving Multiple Features](https://laravel.com/docs/12.x/pennant#retrieving-multiple-features)
The `values` method allows the retrieval of multiple features for a given scope:
```


1Feature::values(['billing-v2', 'purchase-button']);




2 



3// [




4//     'billing-v2' => false,




5//     'purchase-button' => 'blue-sapphire',




6// ]




Feature::values(['billing-v2', 'purchase-button']);

// [
//     'billing-v2' => false,
//     'purchase-button' => 'blue-sapphire',
// ]

```

Or, you may use the `all` method to retrieve the values of all defined features for a given scope:
```


1Feature::all();




2 



3// [




4//     'billing-v2' => false,




5//     'purchase-button' => 'blue-sapphire',




6//     'site-redesign' => true,




7// ]




Feature::all();

// [
//     'billing-v2' => false,
//     'purchase-button' => 'blue-sapphire',
//     'site-redesign' => true,
// ]

```

However, class-based features are dynamically registered and are not known by Pennant until they are explicitly checked. This means your application's class-based features may not appear in the results returned by the `all` method if they have not already been checked during the current request.
If you would like to ensure that feature classes are always included when using the `all` method, you may use Pennant's feature discovery capabilities. To get started, invoke the `discover` method in one of your application's service providers:
```


 1<?php




 2 



 3namespace App\Providers;




 4 



 5use Illuminate\Support\ServiceProvider;




 6use Laravel\Pennant\Feature;




 7 



 8class AppServiceProvider extends ServiceProvider




 9{




10    /**




11     * Bootstrap any application services.




12     */




13    public function boot(): void




14    {




15        Feature::discover();




16 



17        // ...




18    }




19}




<?php

namespace App\Providers;

use Illuminate\Support\ServiceProvider;
use Laravel\Pennant\Feature;

class AppServiceProvider extends ServiceProvider
{
    /**
     * Bootstrap any application services.
     */
    public function boot(): void
    {
        Feature::discover();

        // ...
    }
}

```

The `discover` method will register all of the feature classes in your application's `app/Features` directory. The `all` method will now include these classes in its results, regardless of whether they have been checked during the current request:
```


1Feature::all();




2 



3// [




4//     'App\Features\NewApi' => true,




5//     'billing-v2' => false,




6//     'purchase-button' => 'blue-sapphire',




7//     'site-redesign' => true,




8// ]




Feature::all();

// [
//     'App\Features\NewApi' => true,
//     'billing-v2' => false,
//     'purchase-button' => 'blue-sapphire',
//     'site-redesign' => true,
// ]

```
