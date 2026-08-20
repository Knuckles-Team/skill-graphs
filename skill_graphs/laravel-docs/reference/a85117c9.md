## [Authorization & Inertia](https://laravel.com/docs/12.x/authorization#authorization-and-inertia)
Although authorization must always be handled on the server, it can often be convenient to provide your frontend application with authorization data in order to properly render your application's UI. Laravel does not define a required convention for exposing authorization information to an Inertia powered frontend.
However, if you are using one of Laravel's Inertia-based [starter kits](https://laravel.com/docs/12.x/starter-kits), your application already contains a `HandleInertiaRequests` middleware. Within this middleware's `share` method, you may return shared data that will be provided to all Inertia pages in your application. This shared data can serve as a convenient location to define authorization information for the user:
```


 1<?php




 2 



 3namespace App\Http\Middleware;




 4 



 5use App\Models\Post;




 6use Illuminate\Http\Request;




 7use Inertia\Middleware;




 8 



 9class HandleInertiaRequests extends Middleware




10{




11    // ...




12 



13    /**




14     * Define the props that are shared by default.




15     *




16     * @return array<string, mixed>




17     */




18    public function share(Request $request)




19    {




20        return [




21            ...parent::share($request),




22            'auth' => [




23                'user' => $request->user(),




24                'permissions' => [




25                    'post' => [




26                        'create' => $request->user()->can('create', Post::class),




27                    ],




28                ],




29            ],




30        ];




31    }




32}




<?php

namespace App\Http\Middleware;

use App\Models\Post;
use Illuminate\Http\Request;
use Inertia\Middleware;

class HandleInertiaRequests extends Middleware
{
    // ...

    /**
     * Define the props that are shared by default.
     *
     * @return array<string, mixed>
     */
    public function share(Request $request)
    {
        return [
            ...parent::share($request),
            'auth' => [
                'user' => $request->user(),
                'permissions' => [
                    'post' => [
                        'create' => $request->user()->can('create', Post::class),
                    ],
                ],
            ],
        ];
    }
}

```

Copy as markdown
  * [ Introduction ](https://laravel.com/docs/12.x/authorization#introduction)
  * [ Gates ](https://laravel.com/docs/12.x/authorization#gates)
    * [ Writing Gates ](https://laravel.com/docs/12.x/authorization#writing-gates)
    * [ Authorizing Actions ](https://laravel.com/docs/12.x/authorization#authorizing-actions-via-gates)
    * [ Gate Responses ](https://laravel.com/docs/12.x/authorization#gate-responses)
    * [ Intercepting Gate Checks ](https://laravel.com/docs/12.x/authorization#intercepting-gate-checks)
    * [ Inline Authorization ](https://laravel.com/docs/12.x/authorization#inline-authorization)
  * [ Creating Policies ](https://laravel.com/docs/12.x/authorization#creating-policies)
    * [ Generating Policies ](https://laravel.com/docs/12.x/authorization#generating-policies)
    * [ Registering Policies ](https://laravel.com/docs/12.x/authorization#registering-policies)
  * [ Writing Policies ](https://laravel.com/docs/12.x/authorization#writing-policies)
    * [ Policy Methods ](https://laravel.com/docs/12.x/authorization#policy-methods)
    * [ Policy Responses ](https://laravel.com/docs/12.x/authorization#policy-responses)
    * [ Methods Without Models ](https://laravel.com/docs/12.x/authorization#methods-without-models)
    * [ Guest Users ](https://laravel.com/docs/12.x/authorization#guest-users)
    * [ Policy Filters ](https://laravel.com/docs/12.x/authorization#policy-filters)
  * [ Authorizing Actions Using Policies ](https://laravel.com/docs/12.x/authorization#authorizing-actions-using-policies)
    * [ Via the User Model ](https://laravel.com/docs/12.x/authorization#via-the-user-model)
    * [ Via the Gate Facade ](https://laravel.com/docs/12.x/authorization#via-the-gate-facade)
    * [ Via Middleware ](https://laravel.com/docs/12.x/authorization#via-middleware)
    * [ Via Blade Templates ](https://laravel.com/docs/12.x/authorization#via-blade-templates)
    * [ Supplying Additional Context ](https://laravel.com/docs/12.x/authorization#supplying-additional-context)
  * [ Authorization & Inertia ](https://laravel.com/docs/12.x/authorization#authorization-and-inertia)


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
  * [Vehikl](https://partners.laravel.com/partners/vehikl)
  * [byte5](https://partners.laravel.com/partners/byte5)
  * [Curotec](https://partners.laravel.com/partners/curotec)
  * [Active Logic](https://partners.laravel.com/partners/active-logic)
  * [Jump24](https://partners.laravel.com/partners/jump24)
  * [Redberry](https://partners.laravel.com/partners/redberry)
  * [Kirschbaum](https://partners.laravel.com/partners/kirschbaum)
  * [ More Partners ](https://partners.laravel.com)
