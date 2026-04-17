## [Defining Features](https://laravel.com/docs/12.x/pennant#defining-features)
To define a feature, you may use the `define` method offered by the `Feature` facade. You will need to provide a name for the feature, as well as a closure that will be invoked to resolve the feature's initial value.
Typically, features are defined in a service provider using the `Feature` facade. The closure will receive the "scope" for the feature check. Most commonly, the scope is the currently authenticated user. In this example, we will define a feature for incrementally rolling out a new API to our application's users:
```


 1<?php




 2 



 3namespace App\Providers;




 4 



 5use App\Models\User;




 6use Illuminate\Support\Lottery;




 7use Illuminate\Support\ServiceProvider;




 8use Laravel\Pennant\Feature;




 9 



10class AppServiceProvider extends ServiceProvider




11{




12    /**




13     * Bootstrap any application services.




14     */




15    public function boot(): void




16    {




17        Feature::define('new-api', fn (User $user) => match (true) {




18            $user->isInternalTeamMember() => true,




19            $user->isHighTrafficCustomer() => false,




20            default => Lottery::odds(1 / 100),




21        });




22    }




23}




<?php

namespace App\Providers;

use App\Models\User;
use Illuminate\Support\Lottery;
use Illuminate\Support\ServiceProvider;
use Laravel\Pennant\Feature;

class AppServiceProvider extends ServiceProvider
{
    /**
     * Bootstrap any application services.
     */
    public function boot(): void
    {
        Feature::define('new-api', fn (User $user) => match (true) {
            $user->isInternalTeamMember() => true,
            $user->isHighTrafficCustomer() => false,
            default => Lottery::odds(1 / 100),
        });
    }
}

```

As you can see, we have the following rules for our feature:
  * All internal team members should be using the new API.
  * Any high traffic customers should not be using the new API.
  * Otherwise, the feature should be randomly assigned to users with a 1 in 100 chance of being active.


The first time the `new-api` feature is checked for a given user, the result of the closure will be stored by the storage driver. The next time the feature is checked against the same user, the value will be retrieved from storage and the closure will not be invoked.
For convenience, if a feature definition only returns a lottery, you may omit the closure completely:
```


1Feature::define('site-redesign', Lottery::odds(1, 1000));




Feature::define('site-redesign', Lottery::odds(1, 1000));

```

### [Class Based Features](https://laravel.com/docs/12.x/pennant#class-based-features)
Pennant also allows you to define class-based features. Unlike closure-based feature definitions, there is no need to register a class-based feature in a service provider. To create a class-based feature, you may invoke the `pennant:feature` Artisan command. By default, the feature class will be placed in your application's `app/Features` directory:
```


1php artisan pennant:feature NewApi




php artisan pennant:feature NewApi

```

When writing a feature class, you only need to define a `resolve` method, which will be invoked to resolve the feature's initial value for a given scope. Again, the scope will typically be the currently authenticated user:
```


 1<?php




 2 



 3namespace App\Features;




 4 



 5use App\Models\User;




 6use Illuminate\Support\Lottery;




 7 



 8class NewApi




 9{




10    /**




11     * Resolve the feature's initial value.




12     */




13    public function resolve(User $user): mixed




14    {




15        return match (true) {




16            $user->isInternalTeamMember() => true,




17            $user->isHighTrafficCustomer() => false,




18            default => Lottery::odds(1 / 100),




19        };




20    }




21}




<?php

namespace App\Features;

use App\Models\User;
use Illuminate\Support\Lottery;

class NewApi
{
    /**
     * Resolve the feature's initial value.
     */
    public function resolve(User $user): mixed
    {
        return match (true) {
            $user->isInternalTeamMember() => true,
            $user->isHighTrafficCustomer() => false,
            default => Lottery::odds(1 / 100),
        };
    }
}

```

If you would like to manually resolve an instance of a class-based feature, you may invoke the `instance` method on the `Feature` facade:
```


1use Illuminate\Support\Facades\Feature;




2 



3$instance = Feature::instance(NewApi::class);




use Illuminate\Support\Facades\Feature;

$instance = Feature::instance(NewApi::class);

```

Feature classes are resolved via the [container](https://laravel.com/docs/12.x/container), so you may inject dependencies into the feature class's constructor when needed.
#### Customizing the Stored Feature Name
By default, Pennant will store the feature class's fully qualified class name. If you would like to decouple the stored feature name from the application's internal structure, you may add the `Name` attribute on the feature class. The value of this attribute will be stored in place of the class name:
```


 1<?php




 2 



 3namespace App\Features;




 4 



 5use Laravel\Pennant\Attributes\Name;




 6 



 7#[Name('new-api')]




 8class NewApi




 9{




10    // ...




11}




<?php

namespace App\Features;

use Laravel\Pennant\Attributes\Name;

#[Name('new-api')]
class NewApi
{
    // ...
}

```
