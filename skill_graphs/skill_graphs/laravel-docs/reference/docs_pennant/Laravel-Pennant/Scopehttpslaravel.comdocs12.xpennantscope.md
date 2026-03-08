## [Scope](https://laravel.com/docs/12.x/pennant#scope)
### [Specifying the Scope](https://laravel.com/docs/12.x/pennant#specifying-the-scope)
As discussed, features are typically checked against the currently authenticated user. However, this may not always suit your needs. Therefore, it is possible to specify the scope you would like to check a given feature against via the `Feature` facade's `for` method:
```


1return Feature::for($user)->active('new-api')




2    ? $this->resolveNewApiResponse($request)




3    : $this->resolveLegacyApiResponse($request);




return Feature::for($user)->active('new-api')
    ? $this->resolveNewApiResponse($request)
    : $this->resolveLegacyApiResponse($request);

```

Of course, feature scopes are not limited to "users". Imagine you have built a new billing experience that you are rolling out to entire teams rather than individual users. Perhaps you would like the oldest teams to have a slower rollout than the newer teams. Your feature resolution closure might look something like the following:
```


 1use App\Models\Team;




 2use Illuminate\Support\Carbon;




 3use Illuminate\Support\Lottery;




 4use Laravel\Pennant\Feature;




 5 



 6Feature::define('billing-v2', function (Team $team) {




 7    if ($team->created_at->isAfter(new Carbon('1st Jan, 2023'))) {




 8        return true;




 9    }




10 



11    if ($team->created_at->isAfter(new Carbon('1st Jan, 2019'))) {




12        return Lottery::odds(1 / 100);




13    }




14 



15    return Lottery::odds(1 / 1000);




16});




use App\Models\Team;
use Illuminate\Support\Carbon;
use Illuminate\Support\Lottery;
use Laravel\Pennant\Feature;

Feature::define('billing-v2', function (Team $team) {
    if ($team->created_at->isAfter(new Carbon('1st Jan, 2023'))) {
        return true;
    }

    if ($team->created_at->isAfter(new Carbon('1st Jan, 2019'))) {
        return Lottery::odds(1 / 100);
    }

    return Lottery::odds(1 / 1000);
});

```

You will notice that the closure we have defined is not expecting a `User`, but is instead expecting a `Team` model. To determine if this feature is active for a user's team, you should pass the team to the `for` method offered by the `Feature` facade:
```


1if (Feature::for($user->team)->active('billing-v2')) {




2    return redirect('/billing/v2');




3}




4 



5// ...




if (Feature::for($user->team)->active('billing-v2')) {
    return redirect('/billing/v2');
}

// ...

```

### [Default Scope](https://laravel.com/docs/12.x/pennant#default-scope)
It is also possible to customize the default scope Pennant uses to check features. For example, maybe all of your features are checked against the currently authenticated user's team instead of the user. Instead of having to call `Feature::for($user->team)` every time you check a feature, you may instead specify the team as the default scope. Typically, this should be done in one of your application's service providers:
```


 1<?php




 2 



 3namespace App\Providers;




 4 



 5use Illuminate\Support\Facades\Auth;




 6use Illuminate\Support\ServiceProvider;




 7use Laravel\Pennant\Feature;




 8 



 9class AppServiceProvider extends ServiceProvider




10{




11    /**




12     * Bootstrap any application services.




13     */




14    public function boot(): void




15    {




16        Feature::resolveScopeUsing(fn ($driver) => Auth::user()?->team);




17 



18        // ...




19    }




20}




<?php

namespace App\Providers;

use Illuminate\Support\Facades\Auth;
use Illuminate\Support\ServiceProvider;
use Laravel\Pennant\Feature;

class AppServiceProvider extends ServiceProvider
{
    /**
     * Bootstrap any application services.
     */
    public function boot(): void
    {
        Feature::resolveScopeUsing(fn ($driver) => Auth::user()?->team);

        // ...
    }
}

```

If no scope is explicitly provided via the `for` method, the feature check will now use the currently authenticated user's team as the default scope:
```


1Feature::active('billing-v2');




2 



3// Is now equivalent to...




4 



5Feature::for($user->team)->active('billing-v2');




Feature::active('billing-v2');

// Is now equivalent to...

Feature::for($user->team)->active('billing-v2');

```

### [Nullable Scope](https://laravel.com/docs/12.x/pennant#nullable-scope)
If the scope you provide when checking a feature is `null` and the feature's definition does not support `null` via a nullable type or by including `null` in a union type, Pennant will automatically return `false` as the feature's result value.
So, if the scope you are passing to a feature is potentially `null` and you want the feature's value resolver to be invoked, you should account for that in your feature's definition. A `null` scope may occur if you check a feature within an Artisan command, queued job, or unauthenticated route. Since there is usually not an authenticated user in these contexts, the default scope will be `null`.
If you do not always [explicitly specify your feature scope](https://laravel.com/docs/12.x/pennant#specifying-the-scope) then you should ensure the scope's type is "nullable" and handle the `null` scope value within your feature definition logic:
```


 1use App\Models\User;




 2use Illuminate\Support\Lottery;




 3use Laravel\Pennant\Feature;




 4 



 5Feature::define('new-api', fn (User $user) => match (true) {




 6Feature::define('new-api', fn (User|null $user) => match (true) {




 7    $user === null => true,




 8    $user->isInternalTeamMember() => true,




 9    $user->isHighTrafficCustomer() => false,




10    default => Lottery::odds(1 / 100),




11});




use App\Models\User;
use Illuminate\Support\Lottery;
use Laravel\Pennant\Feature;

Feature::define('new-api', fn (User $user) => match (true) {
Feature::define('new-api', fn (User|null $user) => match (true) {
    $user === null => true,
    $user->isInternalTeamMember() => true,
    $user->isHighTrafficCustomer() => false,
    default => Lottery::odds(1 / 100),
});

```

### [Identifying Scope](https://laravel.com/docs/12.x/pennant#identifying-scope)
Pennant's built-in `array` and `database` storage drivers know how to properly store scope identifiers for all PHP data types as well as Eloquent models. However, if your application utilizes a third-party Pennant driver, that driver may not know how to properly store an identifier for an Eloquent model or other custom types in your application.
In light of this, Pennant allows you to format scope values for storage by implementing the `FeatureScopeable` contract on the objects in your application that are used as Pennant scopes.
For example, imagine you are using two different feature drivers in a single application: the built-in `database` driver and a third-party "Flag Rocket" driver. The "Flag Rocket" driver does not know how to properly store an Eloquent model. Instead, it requires a `FlagRocketUser` instance. By implementing the `toFeatureIdentifier` defined by the `FeatureScopeable` contract, we can customize the storable scope value provided to each driver used by our application:
```


 1<?php




 2 



 3namespace App\Models;




 4 



 5use FlagRocket\FlagRocketUser;




 6use Illuminate\Database\Eloquent\Model;




 7use Laravel\Pennant\Contracts\FeatureScopeable;




 8 



 9class User extends Model implements FeatureScopeable




10{




11    /**




12     * Cast the object to a feature scope identifier for the given driver.




13     */




14    public function toFeatureIdentifier(string $driver): mixed




15    {




16        return match($driver) {




17            'database' => $this,




18            'flag-rocket' => FlagRocketUser::fromId($this->flag_rocket_id),




19        };




20    }




21}




<?php

namespace App\Models;

use FlagRocket\FlagRocketUser;
use Illuminate\Database\Eloquent\Model;
use Laravel\Pennant\Contracts\FeatureScopeable;

class User extends Model implements FeatureScopeable
{
    /**
     * Cast the object to a feature scope identifier for the given driver.
     */
    public function toFeatureIdentifier(string $driver): mixed
    {
        return match($driver) {
            'database' => $this,
            'flag-rocket' => FlagRocketUser::fromId($this->flag_rocket_id),
        };
    }
}

```

### [Serializing Scope](https://laravel.com/docs/12.x/pennant#serializing-scope)
By default, Pennant will use a fully qualified class name when storing a feature associated with an Eloquent model. If you are already using an [Eloquent morph map](https://laravel.com/docs/12.x/eloquent-relationships#custom-polymorphic-types), you may choose to have Pennant also use the morph map to decouple the stored feature from your application structure.
To achieve this, after defining your Eloquent morph map in a service provider, you may invoke the `Feature` facade's `useMorphMap` method:
```


1use Illuminate\Database\Eloquent\Relations\Relation;




2use Laravel\Pennant\Feature;




3 



4Relation::enforceMorphMap([




5    'post' => 'App\Models\Post',




6    'video' => 'App\Models\Video',




7]);




8 



9Feature::useMorphMap();




use Illuminate\Database\Eloquent\Relations\Relation;
use Laravel\Pennant\Feature;

Relation::enforceMorphMap([
    'post' => 'App\Models\Post',
    'video' => 'App\Models\Video',
]);

Feature::useMorphMap();

```
