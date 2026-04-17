## [Events](https://laravel.com/docs/12.x/migrations#events)
For convenience, each migration operation will dispatch an [event](https://laravel.com/docs/12.x/events). All of the following events extend the base `Illuminate\Database\Events\MigrationEvent` class:
Class | Description
---|---
`Illuminate\Database\Events\MigrationsStarted` | A batch of migrations is about to be executed.
`Illuminate\Database\Events\MigrationsEnded` | A batch of migrations has finished executing.
`Illuminate\Database\Events\MigrationStarted` | A single migration is about to be executed.
`Illuminate\Database\Events\MigrationEnded` | A single migration has finished executing.
`Illuminate\Database\Events\NoPendingMigrations` | A migration command found no pending migrations.
`Illuminate\Database\Events\SchemaDumped` | A database schema dump has completed.
`Illuminate\Database\Events\SchemaLoaded` | An existing database schema dump has loaded.
Copy as markdown
  * [ Introduction ](https://laravel.com/docs/12.x/migrations#introduction)
  * [ Generating Migrations ](https://laravel.com/docs/12.x/migrations#generating-migrations)
    * [ Squashing Migrations ](https://laravel.com/docs/12.x/migrations#squashing-migrations)
  * [ Migration Structure ](https://laravel.com/docs/12.x/migrations#migration-structure)
  * [ Running Migrations ](https://laravel.com/docs/12.x/migrations#running-migrations)
    * [ Rolling Back Migrations ](https://laravel.com/docs/12.x/migrations#rolling-back-migrations)
  * [ Tables ](https://laravel.com/docs/12.x/migrations#tables)
    * [ Creating Tables ](https://laravel.com/docs/12.x/migrations#creating-tables)
    * [ Updating Tables ](https://laravel.com/docs/12.x/migrations#updating-tables)
    * [ Renaming / Dropping Tables ](https://laravel.com/docs/12.x/migrations#renaming-and-dropping-tables)
  * [ Columns ](https://laravel.com/docs/12.x/migrations#columns)
    * [ Creating Columns ](https://laravel.com/docs/12.x/migrations#creating-columns)
    * [ Available Column Types ](https://laravel.com/docs/12.x/migrations#available-column-types)
    * [ Column Modifiers ](https://laravel.com/docs/12.x/migrations#column-modifiers)
    * [ Modifying Columns ](https://laravel.com/docs/12.x/migrations#modifying-columns)
    * [ Renaming Columns ](https://laravel.com/docs/12.x/migrations#renaming-columns)
    * [ Dropping Columns ](https://laravel.com/docs/12.x/migrations#dropping-columns)
  * [ Indexes ](https://laravel.com/docs/12.x/migrations#indexes)
    * [ Creating Indexes ](https://laravel.com/docs/12.x/migrations#creating-indexes)
    * [ Renaming Indexes ](https://laravel.com/docs/12.x/migrations#renaming-indexes)
    * [ Dropping Indexes ](https://laravel.com/docs/12.x/migrations#dropping-indexes)
    * [ Foreign Key Constraints ](https://laravel.com/docs/12.x/migrations#foreign-key-constraints)
  * [ Events ](https://laravel.com/docs/12.x/migrations#events)


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
  *   * [Jump24](https://partners.laravel.com/partners/jump24)
  * [Active Logic](https://partners.laravel.com/partners/active-logic)
  * [Vehikl](https://partners.laravel.com/partners/vehikl)
  * [byte5](https://partners.laravel.com/partners/byte5)
  * [Redberry](https://partners.laravel.com/partners/redberry)
  * [Kirschbaum](https://partners.laravel.com/partners/kirschbaum)
  * [Tighten](https://partners.laravel.com/partners/tighten)
  * [Curotec](https://partners.laravel.com/partners/curotec)
  * [ More Partners ](https://partners.laravel.com)
