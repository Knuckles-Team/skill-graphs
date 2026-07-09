## [Custom Engines](https://laravel.com/docs/12.x/scout#custom-engines)
#### [Writing the Engine](https://laravel.com/docs/12.x/scout#writing-the-engine)
If one of the built-in Scout search engines doesn't fit your needs, you may write your own custom engine and register it with Scout. Your engine should extend the `Laravel\Scout\Engines\Engine` abstract class. This abstract class contains eight methods your custom engine must implement:
```


 1use Laravel\Scout\Builder;




 2 



 3abstract public function update($models);




 4abstract public function delete($models);




 5abstract public function search(Builder $builder);




 6abstract public function paginate(Builder $builder, $perPage, $page);




 7abstract public function mapIds($results);




 8abstract public function map(Builder $builder, $results, $model);




 9abstract public function getTotalCount($results);




10abstract public function flush($model);




use Laravel\Scout\Builder;

abstract public function update($models);
abstract public function delete($models);
abstract public function search(Builder $builder);
abstract public function paginate(Builder $builder, $perPage, $page);
abstract public function mapIds($results);
abstract public function map(Builder $builder, $results, $model);
abstract public function getTotalCount($results);
abstract public function flush($model);

```

You may find it helpful to review the implementations of these methods on the `Laravel\Scout\Engines\AlgoliaEngine` class. This class will provide you with a good starting point for learning how to implement each of these methods in your own engine.
#### [Registering the Engine](https://laravel.com/docs/12.x/scout#registering-the-engine)
Once you have written your custom engine, you may register it with Scout using the `extend` method of the Scout engine manager. Scout's engine manager may be resolved from the Laravel service container. You should call the `extend` method from the `boot` method of your `App\Providers\AppServiceProvider` class or any other service provider used by your application:
```


 1use App\ScoutExtensions\MySqlSearchEngine;




 2use Laravel\Scout\EngineManager;




 3 



 4/**




 5 * Bootstrap any application services.




 6 */




 7public function boot(): void




 8{




 9    resolve(EngineManager::class)->extend('mysql', function () {




10        return new MySqlSearchEngine;




11    });




12}




use App\ScoutExtensions\MySqlSearchEngine;
use Laravel\Scout\EngineManager;

/**
 * Bootstrap any application services.
 */
public function boot(): void
{
    resolve(EngineManager::class)->extend('mysql', function () {
        return new MySqlSearchEngine;
    });
}

```

Once your engine has been registered, you may specify it as your default Scout `driver` in your application's `config/scout.php` configuration file:
```


1'driver' => 'mysql',




'driver' => 'mysql',

```

Copy as markdown
  * [ Introduction ](https://laravel.com/docs/12.x/scout#introduction)
  * [ Installation ](https://laravel.com/docs/12.x/scout#installation)
    * [ Queueing ](https://laravel.com/docs/12.x/scout#queueing)
  * [ Driver Prerequisites ](https://laravel.com/docs/12.x/scout#driver-prerequisites)
  * [ Configuration ](https://laravel.com/docs/12.x/scout#configuration)
    * [ Configuring Searchable Data ](https://laravel.com/docs/12.x/scout#configuring-searchable-data)
  * [ Database / Collection Engines ](https://laravel.com/docs/12.x/scout#database-and-collection-engines)
    * [ Database Engine ](https://laravel.com/docs/12.x/scout#database-engine)
    * [ Collection Engine ](https://laravel.com/docs/12.x/scout#collection-engine)
  * [ Third-Party Engine Configuration ](https://laravel.com/docs/12.x/scout#third-party-engine-configuration)
    * [ Configuring Model Indexes ](https://laravel.com/docs/12.x/scout#configuring-model-indexes)
    * [ Algolia ](https://laravel.com/docs/12.x/scout#algolia-configuration)
    * [ Meilisearch ](https://laravel.com/docs/12.x/scout#meilisearch-configuration)
    * [ Typesense ](https://laravel.com/docs/12.x/scout#typesense-configuration)
  * [ Third-Party Engine Indexing ](https://laravel.com/docs/12.x/scout#indexing)
    * [ Batch Import ](https://laravel.com/docs/12.x/scout#batch-import)
    * [ Adding Records ](https://laravel.com/docs/12.x/scout#adding-records)
    * [ Updating Records ](https://laravel.com/docs/12.x/scout#updating-records)
    * [ Removing Records ](https://laravel.com/docs/12.x/scout#removing-records)
    * [ Pausing Indexing ](https://laravel.com/docs/12.x/scout#pausing-indexing)
    * [ Conditionally Searchable Model Instances ](https://laravel.com/docs/12.x/scout#conditionally-searchable-model-instances)
  * [ Searching ](https://laravel.com/docs/12.x/scout#searching)
    * [ Where Clauses ](https://laravel.com/docs/12.x/scout#where-clauses)
    * [ Pagination ](https://laravel.com/docs/12.x/scout#pagination)
    * [ Soft Deleting ](https://laravel.com/docs/12.x/scout#soft-deleting)
    * [ Customizing Engine Searches ](https://laravel.com/docs/12.x/scout#customizing-engine-searches)
  * [ Custom Engines ](https://laravel.com/docs/12.x/scout#custom-engines)


[ ![Laravel Boost](https://laravel.com/images/ads/boost-logo.svg) Supercharge your AI development with essential context Learn more  ](https://laravel.com/ai/boost)
[ ![Laravel Forge](https://laravel.com/images/ads/forge-logo.svg) Server management made simple for any PHP app Learn more  ](https://forge.laravel.com)
[ ![Laravel Cloud](https://laravel.com/images/ads/cloud-logo.svg) The fastest way to deploy and scale Laravel apps Learn more  ](https://cloud.laravel.com)
[ ![Laravel Nightwatch](https://laravel.com/images/ads/nightwatch-logo.svg) First-class monitoring and deep insights for Laravel apps Learn more  ](https://nightwatch.laravel.com)
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
  * [Active Logic](https://partners.laravel.com/partners/active-logic)
  * [Tighten](https://partners.laravel.com/partners/tighten)
  * [byte5](https://partners.laravel.com/partners/byte5)
  * [Redberry](https://partners.laravel.com/partners/redberry)
  * [Kirschbaum](https://partners.laravel.com/partners/kirschbaum)
  * [Vehikl](https://partners.laravel.com/partners/vehikl)
  * [ More Partners ](https://partners.laravel.com)
