## [Adding Custom Pennant Drivers](https://laravel.com/docs/12.x/pennant#adding-custom-pennant-drivers)
#### [Implementing the Driver](https://laravel.com/docs/12.x/pennant#implementing-the-driver)
If none of Pennant's existing storage drivers fit your application's needs, you may write your own storage driver. Your custom driver should implement the `Laravel\Pennant\Contracts\Driver` interface:
```


 1<?php




 2 



 3namespace App\Extensions;




 4 



 5use Laravel\Pennant\Contracts\Driver;




 6 



 7class RedisFeatureDriver implements Driver




 8{




 9    public function define(string $feature, callable $resolver): void {}




10    public function defined(): array {}




11    public function getAll(array $features): array {}




12    public function get(string $feature, mixed $scope): mixed {}




13    public function set(string $feature, mixed $scope, mixed $value): void {}




14    public function setForAllScopes(string $feature, mixed $value): void {}




15    public function delete(string $feature, mixed $scope): void {}




16    public function purge(array|null $features): void {}




17}




<?php

namespace App\Extensions;

use Laravel\Pennant\Contracts\Driver;

class RedisFeatureDriver implements Driver
{
    public function define(string $feature, callable $resolver): void {}
    public function defined(): array {}
    public function getAll(array $features): array {}
    public function get(string $feature, mixed $scope): mixed {}
    public function set(string $feature, mixed $scope, mixed $value): void {}
    public function setForAllScopes(string $feature, mixed $value): void {}
    public function delete(string $feature, mixed $scope): void {}
    public function purge(array|null $features): void {}
}

```

Now, we just need to implement each of these methods using a Redis connection. For an example of how to implement each of these methods, take a look at the `Laravel\Pennant\Drivers\DatabaseDriver` in the
Laravel does not ship with a directory to contain your extensions. You are free to place them anywhere you like. In this example, we have created an `Extensions` directory to house the `RedisFeatureDriver`.
#### [Registering the Driver](https://laravel.com/docs/12.x/pennant#registering-the-driver)
Once your driver has been implemented, you are ready to register it with Laravel. To add additional drivers to Pennant, you may use the `extend` method provided by the `Feature` facade. You should call the `extend` method from the `boot` method of one of your application's [service provider](https://laravel.com/docs/12.x/providers):
```


 1<?php




 2 



 3namespace App\Providers;




 4 



 5use App\Extensions\RedisFeatureDriver;




 6use Illuminate\Contracts\Foundation\Application;




 7use Illuminate\Support\ServiceProvider;




 8use Laravel\Pennant\Feature;




 9 



10class AppServiceProvider extends ServiceProvider




11{




12    /**




13     * Register any application services.




14     */




15    public function register(): void




16    {




17        // ...




18    }




19 



20    /**




21     * Bootstrap any application services.




22     */




23    public function boot(): void




24    {




25        Feature::extend('redis', function (Application $app) {




26            return new RedisFeatureDriver($app->make('redis'), $app->make('events'), []);




27        });




28    }




29}




<?php

namespace App\Providers;

use App\Extensions\RedisFeatureDriver;
use Illuminate\Contracts\Foundation\Application;
use Illuminate\Support\ServiceProvider;
use Laravel\Pennant\Feature;

class AppServiceProvider extends ServiceProvider
{
    /**
     * Register any application services.
     */
    public function register(): void
    {
        // ...
    }

    /**
     * Bootstrap any application services.
     */
    public function boot(): void
    {
        Feature::extend('redis', function (Application $app) {
            return new RedisFeatureDriver($app->make('redis'), $app->make('events'), []);
        });
    }
}

```

Once the driver has been registered, you may use the `redis` driver in your application's `config/pennant.php` configuration file:
```


 1'stores' => [




 2 



 3    'redis' => [




 4        'driver' => 'redis',




 5        'connection' => null,




 6    ],




 7 



 8    // ...




 9 



10],




'stores' => [

    'redis' => [
        'driver' => 'redis',
        'connection' => null,
    ],

    // ...

],

```

### [Defining Features Externally](https://laravel.com/docs/12.x/pennant#defining-features-externally)
If your driver is a wrapper around a third-party feature flag platform, you will likely define features on the platform rather than using Pennant's `Feature::define` method. If that is the case, your custom driver should also implement the `Laravel\Pennant\Contracts\DefinesFeaturesExternally` interface:
```


 1<?php




 2 



 3namespace App\Extensions;




 4 



 5use Laravel\Pennant\Contracts\Driver;




 6use Laravel\Pennant\Contracts\DefinesFeaturesExternally;




 7 



 8class FeatureFlagServiceDriver implements Driver, DefinesFeaturesExternally




 9{




10    /**




11     * Get the features defined for the given scope.




12     */




13    public function definedFeaturesForScope(mixed $scope): array {}




14 



15    /* ... */




16}




<?php

namespace App\Extensions;

use Laravel\Pennant\Contracts\Driver;
use Laravel\Pennant\Contracts\DefinesFeaturesExternally;

class FeatureFlagServiceDriver implements Driver, DefinesFeaturesExternally
{
    /**
     * Get the features defined for the given scope.
     */
    public function definedFeaturesForScope(mixed $scope): array {}

    /* ... */
}

```

The `definedFeaturesForScope` method should return a list of feature names defined for the provided scope.
