## [Events](https://laravel.com/docs/12.x/pennant#events)
Pennant dispatches a variety of events that can be useful when tracking feature flags throughout your application.
### `Laravel\Pennant\Events\FeatureRetrieved`
This event is dispatched whenever a [feature is checked](https://laravel.com/docs/12.x/pennant#checking-features). This event may be useful for creating and tracking metrics against a feature flag's usage throughout your application.
### `Laravel\Pennant\Events\FeatureResolved`
This event is dispatched the first time a feature's value is resolved for a specific scope.
### `Laravel\Pennant\Events\UnknownFeatureResolved`
This event is dispatched the first time an unknown feature is resolved for a specific scope. Listening to this event may be useful if you have intended to remove a feature flag but have accidentally left stray references to it throughout your application:
```


 1<?php




 2 



 3namespace App\Providers;




 4 



 5use Illuminate\Support\ServiceProvider;




 6use Illuminate\Support\Facades\Event;




 7use Illuminate\Support\Facades\Log;




 8use Laravel\Pennant\Events\UnknownFeatureResolved;




 9 



10class AppServiceProvider extends ServiceProvider




11{




12    /**




13     * Bootstrap any application services.




14     */




15    public function boot(): void




16    {




17        Event::listen(function (UnknownFeatureResolved $event) {




18            Log::error("Resolving unknown feature [{$event->feature}].");




19        });




20    }




21}




<?php

namespace App\Providers;

use Illuminate\Support\ServiceProvider;
use Illuminate\Support\Facades\Event;
use Illuminate\Support\Facades\Log;
use Laravel\Pennant\Events\UnknownFeatureResolved;

class AppServiceProvider extends ServiceProvider
{
    /**
     * Bootstrap any application services.
     */
    public function boot(): void
    {
        Event::listen(function (UnknownFeatureResolved $event) {
            Log::error("Resolving unknown feature [{$event->feature}].");
        });
    }
}

```

### `Laravel\Pennant\Events\DynamicallyRegisteringFeatureClass`
This event is dispatched when a [class-based feature](https://laravel.com/docs/12.x/pennant#class-based-features) is dynamically checked for the first time during a request.
### `Laravel\Pennant\Events\UnexpectedNullScopeEncountered`
This event is dispatched when a `null` scope is passed to a feature definition that [doesn't support null](https://laravel.com/docs/12.x/pennant#nullable-scope).
This situation is handled gracefully and the feature will return `false`. However, if you would like to opt out of this feature's default graceful behavior, you may register a listener for this event in the `boot` method of your application's `AppServiceProvider`:
```


 1use Illuminate\Support\Facades\Log;




 2use Laravel\Pennant\Events\UnexpectedNullScopeEncountered;




 3 



 4/**




 5 * Bootstrap any application services.




 6 */




 7public function boot(): void




 8{




 9    Event::listen(UnexpectedNullScopeEncountered::class, fn () => abort(500));




10}




use Illuminate\Support\Facades\Log;
use Laravel\Pennant\Events\UnexpectedNullScopeEncountered;

/**
 * Bootstrap any application services.
 */
public function boot(): void
{
    Event::listen(UnexpectedNullScopeEncountered::class, fn () => abort(500));
}

```

### `Laravel\Pennant\Events\FeatureUpdated`
This event is dispatched when updating a feature for a scope, usually by calling `activate` or `deactivate`.
### `Laravel\Pennant\Events\FeatureUpdatedForAllScopes`
This event is dispatched when updating a feature for all scopes, usually by calling `activateForEveryone` or `deactivateForEveryone`.
### `Laravel\Pennant\Events\FeatureDeleted`
This event is dispatched when deleting a feature for a scope, usually by calling `forget`.
### `Laravel\Pennant\Events\FeaturesPurged`
This event is dispatched when purging specific features.
### `Laravel\Pennant\Events\AllFeaturesPurged`
This event is dispatched when purging all features.
Copy as markdown
  * [ Introduction ](https://laravel.com/docs/12.x/pennant#introduction)
  * [ Installation ](https://laravel.com/docs/12.x/pennant#installation)
  * [ Configuration ](https://laravel.com/docs/12.x/pennant#configuration)
  * [ Defining Features ](https://laravel.com/docs/12.x/pennant#defining-features)
    * [ Class Based Features ](https://laravel.com/docs/12.x/pennant#class-based-features)
  * [ Checking Features ](https://laravel.com/docs/12.x/pennant#checking-features)
    * [ Conditional Execution ](https://laravel.com/docs/12.x/pennant#conditional-execution)
    * [ The HasFeatures Trait ](https://laravel.com/docs/12.x/pennant#the-has-features-trait)
    * [ Blade Directive ](https://laravel.com/docs/12.x/pennant#blade-directive)
    * [ Middleware ](https://laravel.com/docs/12.x/pennant#middleware)
    * [ Intercepting Feature Checks ](https://laravel.com/docs/12.x/pennant#intercepting-feature-checks)
    * [ In-Memory Cache ](https://laravel.com/docs/12.x/pennant#in-memory-cache)
  * [ Scope ](https://laravel.com/docs/12.x/pennant#scope)
    * [ Specifying the Scope ](https://laravel.com/docs/12.x/pennant#specifying-the-scope)
    * [ Default Scope ](https://laravel.com/docs/12.x/pennant#default-scope)
    * [ Nullable Scope ](https://laravel.com/docs/12.x/pennant#nullable-scope)
    * [ Identifying Scope ](https://laravel.com/docs/12.x/pennant#identifying-scope)
    * [ Serializing Scope ](https://laravel.com/docs/12.x/pennant#serializing-scope)
  * [ Rich Feature Values ](https://laravel.com/docs/12.x/pennant#rich-feature-values)
  * [ Retrieving Multiple Features ](https://laravel.com/docs/12.x/pennant#retrieving-multiple-features)
  * [ Eager Loading ](https://laravel.com/docs/12.x/pennant#eager-loading)
  * [ Updating Values ](https://laravel.com/docs/12.x/pennant#updating-values)
    * [ Bulk Updates ](https://laravel.com/docs/12.x/pennant#bulk-updates)
    * [ Purging Features ](https://laravel.com/docs/12.x/pennant#purging-features)
  * [ Testing ](https://laravel.com/docs/12.x/pennant#testing)
  * [ Adding Custom Pennant Drivers ](https://laravel.com/docs/12.x/pennant#adding-custom-pennant-drivers)
    * [ Implementing the Driver ](https://laravel.com/docs/12.x/pennant#implementing-the-driver)
    * [ Registering the Driver ](https://laravel.com/docs/12.x/pennant#registering-the-driver)
    * [ Defining Features Externally ](https://laravel.com/docs/12.x/pennant#defining-features-externally)
  * [ Events ](https://laravel.com/docs/12.x/pennant#events)


[ ![Laravel Forge](https://laravel.com/images/ads/forge-logo.svg) Server management made simple for any PHP app Learn more  ](https://forge.laravel.com)
[ ![Laravel Cloud](https://laravel.com/images/ads/cloud-logo.svg) The fastest way to deploy and scale Laravel apps Learn more  ](https://cloud.laravel.com)
[ ![Laravel Nightwatch](https://laravel.com/images/ads/nightwatch-logo.svg) First-class monitoring and deep insights for Laravel apps Learn more  ](https://nightwatch.laravel.com)
[ ![Laravel Boost](https://laravel.com/images/ads/boost-logo.svg) Supercharge your AI development with essential context Learn more  ](https://laravel.com/ai/boost)
Laravel is the most productive way to
build, deploy, and monitor software.
  * © 2026 Laravel
  * [ Legal ](https://laravel.com/legal)
  * [ Status ](https://status.laravel.com/)


####  Products
  * [ Cloud ](https://cloud.laravel.com)
  * [ Forge ](https://forge.laravel.com)
  * [ Nightwatch ](https://nightwatch.laravel.com)
  * [ Vapor ](https://vapor.laravel.com)
  * [ Nova ](https://nova.laravel.com)


####  Packages
  * [ Cashier ](https://laravel.com/docs/cashier)
  * [ Dusk ](https://laravel.com/docs/dusk)
  * [ Horizon ](https://laravel.com/docs/horizon)
  * [ Octane ](https://laravel.com/docs/octane)
  * [ Scout ](https://laravel.com/docs/scout)
  * [ Pennant ](https://laravel.com/docs/pennant)
  * [ Pint ](https://laravel.com/docs/pint)
  * [ Sail ](https://laravel.com/docs/sail)
  * [ Sanctum ](https://laravel.com/docs/sanctum)
  * [ Socialite ](https://laravel.com/docs/socialite)
  * [ Telescope ](https://laravel.com/docs/telescope)
  * [ Pulse ](https://laravel.com/docs/pulse)
  * [ Reverb ](https://laravel.com/docs/reverb)
  * [ Echo ](https://laravel.com/docs/broadcasting)


####  Resources
  * [ Documentation ](https://laravel.com/docs)
  * [ Starter Kits ](https://laravel.com/starter-kits)
  * [ Release Notes ](https://laravel.com/docs/releases)
  * [ Blog ](https://laravel.com/blog)
  * [ Community ](https://laravel.com/community)
  * [ Learn ](https://laravel.com/learn)
  * [ Careers ](https://laravel.com/careers)
  * [ Trust ](https://trust.laravel.com)


####  Partners
  *   * [Curotec](https://partners.laravel.com/partners/curotec)
  * [Jump24](https://partners.laravel.com/partners/jump24)
  * [Vehikl](https://partners.laravel.com/partners/vehikl)
  * [Tighten](https://partners.laravel.com/partners/tighten)
  * [Redberry](https://partners.laravel.com/partners/redberry)
  * [byte5](https://partners.laravel.com/partners/byte5)
  * [Active Logic](https://partners.laravel.com/partners/active-logic)
  * [Kirschbaum](https://partners.laravel.com/partners/kirschbaum)
  * [ More Partners ](https://partners.laravel.com)
