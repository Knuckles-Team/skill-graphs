## [Resource Responses](https://laravel.com/docs/12.x/eloquent-resources#resource-responses)
As you have already read, resources may be returned directly from routes and controllers:
```


1use App\Models\User;




2 



3Route::get('/user/{id}', function (string $id) {




4    return User::findOrFail($id)->toResource();




5});




use App\Models\User;

Route::get('/user/{id}', function (string $id) {
    return User::findOrFail($id)->toResource();
});

```

However, sometimes you may need to customize the outgoing HTTP response before it is sent to the client. There are two ways to accomplish this. First, you may chain the `response` method onto the resource. This method will return an `Illuminate\Http\JsonResponse` instance, giving you full control over the response's headers:
```


1use App\Http\Resources\UserResource;




2use App\Models\User;




3 



4Route::get('/user', function () {




5    return User::find(1)




6        ->toResource()




7        ->response()




8        ->header('X-Value', 'True');




9});




use App\Http\Resources\UserResource;
use App\Models\User;

Route::get('/user', function () {
    return User::find(1)
        ->toResource()
        ->response()
        ->header('X-Value', 'True');
});

```

Alternatively, you may define a `withResponse` method within the resource itself. This method will be called when the resource is returned as the outermost resource in a response:
```


 1<?php




 2 



 3namespace App\Http\Resources;




 4 



 5use Illuminate\Http\JsonResponse;




 6use Illuminate\Http\Request;




 7use Illuminate\Http\Resources\Json\JsonResource;




 8 



 9class UserResource extends JsonResource




10{




11    /**




12     * Transform the resource into an array.




13     *




14     * @return array<string, mixed>




15     */




16    public function toArray(Request $request): array




17    {




18        return [




19            'id' => $this->id,




20        ];




21    }




22 



23    /**




24     * Customize the outgoing response for the resource.




25     */




26    public function withResponse(Request $request, JsonResponse $response): void




27    {




28        $response->header('X-Value', 'True');




29    }




30}




<?php

namespace App\Http\Resources;

use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;
use Illuminate\Http\Resources\Json\JsonResource;

class UserResource extends JsonResource
{
    /**
     * Transform the resource into an array.
     *
     * @return array<string, mixed>
     */
    public function toArray(Request $request): array
    {
        return [
            'id' => $this->id,
        ];
    }

    /**
     * Customize the outgoing response for the resource.
     */
    public function withResponse(Request $request, JsonResponse $response): void
    {
        $response->header('X-Value', 'True');
    }
}

```

Copy as markdown
  * [ Introduction ](https://laravel.com/docs/12.x/eloquent-resources#introduction)
  * [ Generating Resources ](https://laravel.com/docs/12.x/eloquent-resources#generating-resources)
  * [ Concept Overview ](https://laravel.com/docs/12.x/eloquent-resources#concept-overview)
    * [ Resource Collections ](https://laravel.com/docs/12.x/eloquent-resources#resource-collections)
  * [ Writing Resources ](https://laravel.com/docs/12.x/eloquent-resources#writing-resources)
    * [ Data Wrapping ](https://laravel.com/docs/12.x/eloquent-resources#data-wrapping)
    * [ Pagination ](https://laravel.com/docs/12.x/eloquent-resources#pagination)
    * [ Conditional Attributes ](https://laravel.com/docs/12.x/eloquent-resources#conditional-attributes)
    * [ Conditional Relationships ](https://laravel.com/docs/12.x/eloquent-resources#conditional-relationships)
    * [ Adding Meta Data ](https://laravel.com/docs/12.x/eloquent-resources#adding-meta-data)
  * [ Resource Responses ](https://laravel.com/docs/12.x/eloquent-resources#resource-responses)


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
  * [Kirschbaum](https://partners.laravel.com/partners/kirschbaum)
  * [Vehikl](https://partners.laravel.com/partners/vehikl)
  * [Tighten](https://partners.laravel.com/partners/tighten)
  * [byte5](https://partners.laravel.com/partners/byte5)
  * [Active Logic](https://partners.laravel.com/partners/active-logic)
  * [Redberry](https://partners.laravel.com/partners/redberry)
  * [ More Partners ](https://partners.laravel.com)
