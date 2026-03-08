## [Route Caching](https://laravel.com/docs/12.x/routing#route-caching)
When deploying your application to production, you should take advantage of Laravel's route cache. Using the route cache will drastically decrease the amount of time it takes to register all of your application's routes. To generate a route cache, execute the `route:cache` Artisan command:
```


1php artisan route:cache




php artisan route:cache

```

After running this command, your cached routes file will be loaded on every request. Remember, if you add any new routes you will need to generate a fresh route cache. Because of this, you should only run the `route:cache` command during your project's deployment.
You may use the `route:clear` command to clear the route cache:
```


1php artisan route:clear




php artisan route:clear

```

Copy as markdown
  * [ Basic Routing ](https://laravel.com/docs/12.x/routing#basic-routing)
    * [ The Default Route Files ](https://laravel.com/docs/12.x/routing#the-default-route-files)
    * [ Redirect Routes ](https://laravel.com/docs/12.x/routing#redirect-routes)
    * [ View Routes ](https://laravel.com/docs/12.x/routing#view-routes)
    * [ Listing Your Routes ](https://laravel.com/docs/12.x/routing#listing-your-routes)
    * [ Routing Customization ](https://laravel.com/docs/12.x/routing#routing-customization)
  * [ Route Parameters ](https://laravel.com/docs/12.x/routing#route-parameters)
    * [ Required Parameters ](https://laravel.com/docs/12.x/routing#required-parameters)
    * [ Optional Parameters ](https://laravel.com/docs/12.x/routing#parameters-optional-parameters)
    * [ Regular Expression Constraints ](https://laravel.com/docs/12.x/routing#parameters-regular-expression-constraints)
  * [ Named Routes ](https://laravel.com/docs/12.x/routing#named-routes)
  * [ Route Groups ](https://laravel.com/docs/12.x/routing#route-groups)
    * [ Middleware ](https://laravel.com/docs/12.x/routing#route-group-middleware)
    * [ Controllers ](https://laravel.com/docs/12.x/routing#route-group-controllers)
    * [ Subdomain Routing ](https://laravel.com/docs/12.x/routing#route-group-subdomain-routing)
    * [ Route Prefixes ](https://laravel.com/docs/12.x/routing#route-group-prefixes)
    * [ Route Name Prefixes ](https://laravel.com/docs/12.x/routing#route-group-name-prefixes)
  * [ Route Model Binding ](https://laravel.com/docs/12.x/routing#route-model-binding)
    * [ Implicit Binding ](https://laravel.com/docs/12.x/routing#implicit-binding)
    * [ Implicit Enum Binding ](https://laravel.com/docs/12.x/routing#implicit-enum-binding)
    * [ Explicit Binding ](https://laravel.com/docs/12.x/routing#explicit-binding)
  * [ Fallback Routes ](https://laravel.com/docs/12.x/routing#fallback-routes)
  * [ Rate Limiting ](https://laravel.com/docs/12.x/routing#rate-limiting)
    * [ Defining Rate Limiters ](https://laravel.com/docs/12.x/routing#defining-rate-limiters)
    * [ Attaching Rate Limiters to Routes ](https://laravel.com/docs/12.x/routing#attaching-rate-limiters-to-routes)
  * [ Form Method Spoofing ](https://laravel.com/docs/12.x/routing#form-method-spoofing)
  * [ Accessing the Current Route ](https://laravel.com/docs/12.x/routing#accessing-the-current-route)
  * [ Cross-Origin Resource Sharing (CORS) ](https://laravel.com/docs/12.x/routing#cors)
  * [ Route Caching ](https://laravel.com/docs/12.x/routing#route-caching)


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
  *   * [Tighten](https://partners.laravel.com/partners/tighten)
  * [Jump24](https://partners.laravel.com/partners/jump24)
  * [Kirschbaum](https://partners.laravel.com/partners/kirschbaum)
  * [Vehikl](https://partners.laravel.com/partners/vehikl)
  * [Active Logic](https://partners.laravel.com/partners/active-logic)
  * [byte5](https://partners.laravel.com/partners/byte5)
  * [Redberry](https://partners.laravel.com/partners/redberry)
  * [Curotec](https://partners.laravel.com/partners/curotec)
  * [ More Partners ](https://partners.laravel.com)
