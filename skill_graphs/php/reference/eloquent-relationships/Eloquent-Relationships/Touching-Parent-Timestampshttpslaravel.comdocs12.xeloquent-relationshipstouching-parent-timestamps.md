## [Touching Parent Timestamps](https://laravel.com/docs/12.x/eloquent-relationships#touching-parent-timestamps)
When a model defines a `belongsTo` or `belongsToMany` relationship to another model, such as a `Comment` which belongs to a `Post`, it is sometimes helpful to update the parent's timestamp when the child model is updated.
For example, when a `Comment` model is updated, you may want to automatically "touch" the `updated_at` timestamp of the owning `Post` so that it is set to the current date and time. To accomplish this, you may add a `touches` property to your child model containing the names of the relationships that should have their `updated_at` timestamps updated when the child model is updated:
```


 1<?php




 2 



 3namespace App\Models;




 4 



 5use Illuminate\Database\Eloquent\Model;




 6use Illuminate\Database\Eloquent\Relations\BelongsTo;




 7 



 8class Comment extends Model




 9{




10    /**




11     * All of the relationships to be touched.




12     *




13     * @var array




14     */




15    protected $touches = ['post'];




16 



17    /**




18     * Get the post that the comment belongs to.




19     */




20    public function post(): BelongsTo




21    {




22        return $this->belongsTo(Post::class);




23    }




24}




<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

class Comment extends Model
{
    /**
     * All of the relationships to be touched.
     *
     * @var array
     */
    protected $touches = ['post'];

    /**
     * Get the post that the comment belongs to.
     */
    public function post(): BelongsTo
    {
        return $this->belongsTo(Post::class);
    }
}

```

Parent model timestamps will only be updated if the child model is updated using Eloquent's `save` method.
Copy as markdown
  * [ Introduction ](https://laravel.com/docs/12.x/eloquent-relationships#introduction)
  * [ Defining Relationships ](https://laravel.com/docs/12.x/eloquent-relationships#defining-relationships)
    * [ One to One / Has One ](https://laravel.com/docs/12.x/eloquent-relationships#one-to-one)
    * [ One to Many / Has Many ](https://laravel.com/docs/12.x/eloquent-relationships#one-to-many)
    * [ One to Many (Inverse) / Belongs To ](https://laravel.com/docs/12.x/eloquent-relationships#one-to-many-inverse)
    * [ Has One of Many ](https://laravel.com/docs/12.x/eloquent-relationships#has-one-of-many)
    * [ Has One Through ](https://laravel.com/docs/12.x/eloquent-relationships#has-one-through)
    * [ Has Many Through ](https://laravel.com/docs/12.x/eloquent-relationships#has-many-through)
  * [ Scoped Relationships ](https://laravel.com/docs/12.x/eloquent-relationships#scoped-relationships)
  * [ Many to Many Relationships ](https://laravel.com/docs/12.x/eloquent-relationships#many-to-many)
    * [ Retrieving Intermediate Table Columns ](https://laravel.com/docs/12.x/eloquent-relationships#retrieving-intermediate-table-columns)
    * [ Filtering Queries via Intermediate Table Columns ](https://laravel.com/docs/12.x/eloquent-relationships#filtering-queries-via-intermediate-table-columns)
    * [ Ordering Queries via Intermediate Table Columns ](https://laravel.com/docs/12.x/eloquent-relationships#ordering-queries-via-intermediate-table-columns)
    * [ Defining Custom Intermediate Table Models ](https://laravel.com/docs/12.x/eloquent-relationships#defining-custom-intermediate-table-models)
  * [ Polymorphic Relationships ](https://laravel.com/docs/12.x/eloquent-relationships#polymorphic-relationships)
    * [ One to One ](https://laravel.com/docs/12.x/eloquent-relationships#one-to-one-polymorphic-relations)
    * [ One to Many ](https://laravel.com/docs/12.x/eloquent-relationships#one-to-many-polymorphic-relations)
    * [ One of Many ](https://laravel.com/docs/12.x/eloquent-relationships#one-of-many-polymorphic-relations)
    * [ Many to Many ](https://laravel.com/docs/12.x/eloquent-relationships#many-to-many-polymorphic-relations)
    * [ Custom Polymorphic Types ](https://laravel.com/docs/12.x/eloquent-relationships#custom-polymorphic-types)
  * [ Dynamic Relationships ](https://laravel.com/docs/12.x/eloquent-relationships#dynamic-relationships)
  * [ Querying Relations ](https://laravel.com/docs/12.x/eloquent-relationships#querying-relations)
    * [ Relationship Methods vs. Dynamic Properties ](https://laravel.com/docs/12.x/eloquent-relationships#relationship-methods-vs-dynamic-properties)
    * [ Querying Relationship Existence ](https://laravel.com/docs/12.x/eloquent-relationships#querying-relationship-existence)
    * [ Querying Relationship Absence ](https://laravel.com/docs/12.x/eloquent-relationships#querying-relationship-absence)
    * [ Querying Morph To Relationships ](https://laravel.com/docs/12.x/eloquent-relationships#querying-morph-to-relationships)
  * [ Aggregating Related Models ](https://laravel.com/docs/12.x/eloquent-relationships#aggregating-related-models)
    * [ Counting Related Models ](https://laravel.com/docs/12.x/eloquent-relationships#counting-related-models)
    * [ Other Aggregate Functions ](https://laravel.com/docs/12.x/eloquent-relationships#other-aggregate-functions)
    * [ Counting Related Models on Morph To Relationships ](https://laravel.com/docs/12.x/eloquent-relationships#counting-related-models-on-morph-to-relationships)
  * [ Eager Loading ](https://laravel.com/docs/12.x/eloquent-relationships#eager-loading)
    * [ Constraining Eager Loads ](https://laravel.com/docs/12.x/eloquent-relationships#constraining-eager-loads)
    * [ Lazy Eager Loading ](https://laravel.com/docs/12.x/eloquent-relationships#lazy-eager-loading)
    * [ Automatic Eager Loading ](https://laravel.com/docs/12.x/eloquent-relationships#automatic-eager-loading)
    * [ Preventing Lazy Loading ](https://laravel.com/docs/12.x/eloquent-relationships#preventing-lazy-loading)
  * [ Inserting and Updating Related Models ](https://laravel.com/docs/12.x/eloquent-relationships#inserting-and-updating-related-models)
    * [ The save Method ](https://laravel.com/docs/12.x/eloquent-relationships#the-save-method)
    * [ The create Method ](https://laravel.com/docs/12.x/eloquent-relationships#the-create-method)
    * [ Belongs To Relationships ](https://laravel.com/docs/12.x/eloquent-relationships#updating-belongs-to-relationships)
    * [ Many to Many Relationships ](https://laravel.com/docs/12.x/eloquent-relationships#updating-many-to-many-relationships)
  * [ Touching Parent Timestamps ](https://laravel.com/docs/12.x/eloquent-relationships#touching-parent-timestamps)


[ ![Laravel Nightwatch](https://laravel.com/images/ads/nightwatch-logo.svg) First-class monitoring and deep insights for Laravel apps Learn more  ](https://nightwatch.laravel.com)
[ ![Laravel Forge](https://laravel.com/images/ads/forge-logo.svg) Server management made simple for any PHP app Learn more  ](https://forge.laravel.com)
[ ![Laravel Cloud](https://laravel.com/images/ads/cloud-logo.svg) The fastest way to deploy and scale Laravel apps Learn more  ](https://cloud.laravel.com)
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
  *   * [byte5](https://partners.laravel.com/partners/byte5)
  * [Curotec](https://partners.laravel.com/partners/curotec)
  * [Redberry](https://partners.laravel.com/partners/redberry)
  * [Vehikl](https://partners.laravel.com/partners/vehikl)
  * [Tighten](https://partners.laravel.com/partners/tighten)
  * [Active Logic](https://partners.laravel.com/partners/active-logic)
  * [Jump24](https://partners.laravel.com/partners/jump24)
  * [Kirschbaum](https://partners.laravel.com/partners/kirschbaum)
  * [ More Partners ](https://partners.laravel.com)
