## [Checking Features](https://laravel.com/docs/12.x/pennant#checking-features)
To determine if a feature is active, you may use the `active` method on the `Feature` facade. By default, features are checked against the currently authenticated user:
```


 1<?php




 2 



 3namespace App\Http\Controllers;




 4 



 5use Illuminate\Http\Request;




 6use Illuminate\Http\Response;




 7use Laravel\Pennant\Feature;




 8 



 9class PodcastController




10{




11    /**




12     * Display a listing of the resource.




13     */




14    public function index(Request $request): Response




15    {




16        return Feature::active('new-api')




17            ? $this->resolveNewApiResponse($request)




18            : $this->resolveLegacyApiResponse($request);




19    }




20 



21    // ...




22}




<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Http\Response;
use Laravel\Pennant\Feature;

class PodcastController
{
    /**
     * Display a listing of the resource.
     */
    public function index(Request $request): Response
    {
        return Feature::active('new-api')
            ? $this->resolveNewApiResponse($request)
            : $this->resolveLegacyApiResponse($request);
    }

    // ...
}

```

Although features are checked against the currently authenticated user by default, you may easily check the feature against another user or [scope](https://laravel.com/docs/12.x/pennant#scope). To accomplish this, use the `for` method offered by the `Feature` facade:
```


1return Feature::for($user)->active('new-api')




2    ? $this->resolveNewApiResponse($request)




3    : $this->resolveLegacyApiResponse($request);




return Feature::for($user)->active('new-api')
    ? $this->resolveNewApiResponse($request)
    : $this->resolveLegacyApiResponse($request);

```

Pennant also offers some additional convenience methods that may prove useful when determining if a feature is active or not:
```


 1// Determine if all of the given features are active...




 2Feature::allAreActive(['new-api', 'site-redesign']);




 3 



 4// Determine if any of the given features are active...




 5Feature::someAreActive(['new-api', 'site-redesign']);




 6 



 7// Determine if a feature is inactive...




 8Feature::inactive('new-api');




 9 



10// Determine if all of the given features are inactive...




11Feature::allAreInactive(['new-api', 'site-redesign']);




12 



13// Determine if any of the given features are inactive...




14Feature::someAreInactive(['new-api', 'site-redesign']);




// Determine if all of the given features are active...
Feature::allAreActive(['new-api', 'site-redesign']);

// Determine if any of the given features are active...
Feature::someAreActive(['new-api', 'site-redesign']);

// Determine if a feature is inactive...
Feature::inactive('new-api');

// Determine if all of the given features are inactive...
Feature::allAreInactive(['new-api', 'site-redesign']);

// Determine if any of the given features are inactive...
Feature::someAreInactive(['new-api', 'site-redesign']);

```

When using Pennant outside of an HTTP context, such as in an Artisan command or a queued job, you should typically [explicitly specify the feature's scope](https://laravel.com/docs/12.x/pennant#specifying-the-scope). Alternatively, you may define a [default scope](https://laravel.com/docs/12.x/pennant#default-scope) that accounts for both authenticated HTTP contexts and unauthenticated contexts.
#### [Checking Class Based Features](https://laravel.com/docs/12.x/pennant#checking-class-based-features)
For class-based features, you should provide the class name when checking the feature:
```


 1<?php




 2 



 3namespace App\Http\Controllers;




 4 



 5use App\Features\NewApi;




 6use Illuminate\Http\Request;




 7use Illuminate\Http\Response;




 8use Laravel\Pennant\Feature;




 9 



10class PodcastController




11{




12    /**




13     * Display a listing of the resource.




14     */




15    public function index(Request $request): Response




16    {




17        return Feature::active(NewApi::class)




18            ? $this->resolveNewApiResponse($request)




19            : $this->resolveLegacyApiResponse($request);




20    }




21 



22    // ...




23}




<?php

namespace App\Http\Controllers;

use App\Features\NewApi;
use Illuminate\Http\Request;
use Illuminate\Http\Response;
use Laravel\Pennant\Feature;

class PodcastController
{
    /**
     * Display a listing of the resource.
     */
    public function index(Request $request): Response
    {
        return Feature::active(NewApi::class)
            ? $this->resolveNewApiResponse($request)
            : $this->resolveLegacyApiResponse($request);
    }

    // ...
}

```

### [Conditional Execution](https://laravel.com/docs/12.x/pennant#conditional-execution)
The `when` method may be used to fluently execute a given closure if a feature is active. Additionally, a second closure may be provided and will be executed if the feature is inactive:
```


 1<?php




 2 



 3namespace App\Http\Controllers;




 4 



 5use App\Features\NewApi;




 6use Illuminate\Http\Request;




 7use Illuminate\Http\Response;




 8use Laravel\Pennant\Feature;




 9 



10class PodcastController




11{




12    /**




13     * Display a listing of the resource.




14     */




15    public function index(Request $request): Response




16    {




17        return Feature::when(NewApi::class,




18            fn () => $this->resolveNewApiResponse($request),




19            fn () => $this->resolveLegacyApiResponse($request),




20        );




21    }




22 



23    // ...




24}




<?php

namespace App\Http\Controllers;

use App\Features\NewApi;
use Illuminate\Http\Request;
use Illuminate\Http\Response;
use Laravel\Pennant\Feature;

class PodcastController
{
    /**
     * Display a listing of the resource.
     */
    public function index(Request $request): Response
    {
        return Feature::when(NewApi::class,
            fn () => $this->resolveNewApiResponse($request),
            fn () => $this->resolveLegacyApiResponse($request),
        );
    }

    // ...
}

```

The `unless` method serves as the inverse of the `when` method, executing the first closure if the feature is inactive:
```


1return Feature::unless(NewApi::class,




2    fn () => $this->resolveLegacyApiResponse($request),




3    fn () => $this->resolveNewApiResponse($request),




4);




return Feature::unless(NewApi::class,
    fn () => $this->resolveLegacyApiResponse($request),
    fn () => $this->resolveNewApiResponse($request),
);

```

### [The `HasFeatures` Trait](https://laravel.com/docs/12.x/pennant#the-has-features-trait)
Pennant's `HasFeatures` trait may be added to your application's `User` model (or any other model that has features) to provide a fluent, convenient way to check features directly from the model:
```


 1<?php




 2 



 3namespace App\Models;




 4 



 5use Illuminate\Foundation\Auth\User as Authenticatable;




 6use Laravel\Pennant\Concerns\HasFeatures;




 7 



 8class User extends Authenticatable




 9{




10    use HasFeatures;




11 



12    // ...




13}




<?php

namespace App\Models;

use Illuminate\Foundation\Auth\User as Authenticatable;
use Laravel\Pennant\Concerns\HasFeatures;

class User extends Authenticatable
{
    use HasFeatures;

    // ...
}

```

Once the trait has been added to your model, you may easily check features by invoking the `features` method:
```


1if ($user->features()->active('new-api')) {




2    // ...




3}




if ($user->features()->active('new-api')) {
    // ...
}

```

Of course, the `features` method provides access to many other convenient methods for interacting with features:
```


 1// Values...




 2$value = $user->features()->value('purchase-button')




 3$values = $user->features()->values(['new-api', 'purchase-button']);




 4 



 5// State...




 6$user->features()->active('new-api');




 7$user->features()->allAreActive(['new-api', 'server-api']);




 8$user->features()->someAreActive(['new-api', 'server-api']);




 9 



10$user->features()->inactive('new-api');




11$user->features()->allAreInactive(['new-api', 'server-api']);




12$user->features()->someAreInactive(['new-api', 'server-api']);




13 



14// Conditional execution...




15$user->features()->when('new-api',




16    fn () => /* ... */,




17    fn () => /* ... */,




18);




19 



20$user->features()->unless('new-api',




21    fn () => /* ... */,




22    fn () => /* ... */,




23);




// Values...
$value = $user->features()->value('purchase-button')
$values = $user->features()->values(['new-api', 'purchase-button']);

// State...
$user->features()->active('new-api');
$user->features()->allAreActive(['new-api', 'server-api']);
$user->features()->someAreActive(['new-api', 'server-api']);

$user->features()->inactive('new-api');
$user->features()->allAreInactive(['new-api', 'server-api']);
$user->features()->someAreInactive(['new-api', 'server-api']);

// Conditional execution...
$user->features()->when('new-api',
    fn () => /* ... */,
    fn () => /* ... */,
);

$user->features()->unless('new-api',
    fn () => /* ... */,
    fn () => /* ... */,
);

```

### [Blade Directive](https://laravel.com/docs/12.x/pennant#blade-directive)
To make checking features in Blade a seamless experience, Pennant offers the `@feature` and `@featureany` directive:
```


1@feature('site-redesign')




2    <!-- 'site-redesign' is active -->




3@else




4    <!-- 'site-redesign' is inactive -->




5@endfeature




6 



7@featureany(['site-redesign', 'beta'])




8    <!-- 'site-redesign' or `beta` is active -->




9@endfeatureany




@feature('site-redesign')
    <!-- 'site-redesign' is active -->
@else
    <!-- 'site-redesign' is inactive -->
@endfeature

@featureany(['site-redesign', 'beta'])
    <!-- 'site-redesign' or `beta` is active -->
@endfeatureany

```

### [Middleware](https://laravel.com/docs/12.x/pennant#middleware)
Pennant also includes a [middleware](https://laravel.com/docs/12.x/middleware) that may be used to verify the currently authenticated user has access to a feature before a route is even invoked. You may assign the middleware to a route and specify the features that are required to access the route. If any of the specified features are inactive for the currently authenticated user, a `400 Bad Request` HTTP response will be returned by the route. Multiple features may be passed to the static `using` method.
```


1use Illuminate\Support\Facades\Route;




2use Laravel\Pennant\Middleware\EnsureFeaturesAreActive;




3 



4Route::get('/api/servers', function () {




5    // ...




6})->middleware(EnsureFeaturesAreActive::using('new-api', 'servers-api'));




use Illuminate\Support\Facades\Route;
use Laravel\Pennant\Middleware\EnsureFeaturesAreActive;

Route::get('/api/servers', function () {
    // ...
})->middleware(EnsureFeaturesAreActive::using('new-api', 'servers-api'));

```

#### [Customizing the Response](https://laravel.com/docs/12.x/pennant#customizing-the-response)
If you would like to customize the response that is returned by the middleware when one of the listed features is inactive, you may use the `whenInactive` method provided by the `EnsureFeaturesAreActive` middleware. Typically, this method should be invoked within the `boot` method of one of your application's service providers:
```


 1use Illuminate\Http\Request;




 2use Illuminate\Http\Response;




 3use Laravel\Pennant\Middleware\EnsureFeaturesAreActive;




 4 



 5/**




 6 * Bootstrap any application services.




 7 */




 8public function boot(): void




 9{




10    EnsureFeaturesAreActive::whenInactive(




11        function (Request $request, array $features) {




12            return new Response(status: 403);




13        }




14    );




15 



16    // ...




17}




use Illuminate\Http\Request;
use Illuminate\Http\Response;
use Laravel\Pennant\Middleware\EnsureFeaturesAreActive;

/**
 * Bootstrap any application services.
 */
public function boot(): void
{
    EnsureFeaturesAreActive::whenInactive(
        function (Request $request, array $features) {
            return new Response(status: 403);
        }
    );

    // ...
}

```

### [Intercepting Feature Checks](https://laravel.com/docs/12.x/pennant#intercepting-feature-checks)
Sometimes it can be useful to perform some in-memory checks before retrieving the stored value of a given feature. Imagine you are developing a new API behind a feature flag and want the ability to disable the new API without losing any of the resolved feature values in storage. If you notice a bug in the new API, you could easily disable it for everyone except internal team members, fix the bug, and then re-enable the new API for the users that previously had access to the feature.
You can achieve this with a [class-based feature's](https://laravel.com/docs/12.x/pennant#class-based-features) `before` method. When present, the `before` method is always run in-memory before retrieving the value from storage. If a non-`null` value is returned from the method, it will be used in place of the feature's stored value for the duration of the request:
```


 1<?php




 2 



 3namespace App\Features;




 4 



 5use App\Models\User;




 6use Illuminate\Support\Facades\Config;




 7use Illuminate\Support\Lottery;




 8 



 9class NewApi




10{




11    /**




12     * Run an always-in-memory check before the stored value is retrieved.




13     */




14    public function before(User $user): mixed




15    {




16        if (Config::get('features.new-api.disabled')) {




17            return $user->isInternalTeamMember();




18        }




19    }




20 



21    /**




22     * Resolve the feature's initial value.




23     */




24    public function resolve(User $user): mixed




25    {




26        return match (true) {




27            $user->isInternalTeamMember() => true,




28            $user->isHighTrafficCustomer() => false,




29            default => Lottery::odds(1 / 100),




30        };




31    }




32}




<?php

namespace App\Features;

use App\Models\User;
use Illuminate\Support\Facades\Config;
use Illuminate\Support\Lottery;

class NewApi
{
    /**
     * Run an always-in-memory check before the stored value is retrieved.
     */
    public function before(User $user): mixed
    {
        if (Config::get('features.new-api.disabled')) {
            return $user->isInternalTeamMember();
        }
    }

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

You could also use this feature to schedule the global rollout of a feature that was previously behind a feature flag:
```


 1<?php




 2 



 3namespace App\Features;




 4 



 5use Illuminate\Support\Carbon;




 6use Illuminate\Support\Facades\Config;




 7 



 8class NewApi




 9{




10    /**




11     * Run an always-in-memory check before the stored value is retrieved.




12     */




13    public function before(User $user): mixed




14    {




15        if (Config::get('features.new-api.disabled')) {




16            return $user->isInternalTeamMember();




17        }




18 



19        if (Carbon::parse(Config::get('features.new-api.rollout-date'))->isPast()) {




20            return true;




21        }




22    }




23 



24    // ...




25}




<?php

namespace App\Features;

use Illuminate\Support\Carbon;
use Illuminate\Support\Facades\Config;

class NewApi
{
    /**
     * Run an always-in-memory check before the stored value is retrieved.
     */
    public function before(User $user): mixed
    {
        if (Config::get('features.new-api.disabled')) {
            return $user->isInternalTeamMember();
        }

        if (Carbon::parse(Config::get('features.new-api.rollout-date'))->isPast()) {
            return true;
        }
    }

    // ...
}

```

### [In-Memory Cache](https://laravel.com/docs/12.x/pennant#in-memory-cache)
When checking a feature, Pennant will create an in-memory cache of the result. If you are using the `database` driver, this means that re-checking the same feature flag within a single request will not trigger additional database queries. This also ensures that the feature has a consistent result for the duration of the request.
If you need to manually flush the in-memory cache, you may use the `flushCache` method offered by the `Feature` facade:
```


1Feature::flushCache();




Feature::flushCache();

```
