## [Events](https://laravel.com/docs/12.x/http-client#events)
Laravel fires three events during the process of sending HTTP requests. The `RequestSending` event is fired prior to a request being sent, while the `ResponseReceived` event is fired after a response is received for a given request. The `ConnectionFailed` event is fired if no response is received for a given request.
The `RequestSending` and `ConnectionFailed` events both contain a public `$request` property that you may use to inspect the `Illuminate\Http\Client\Request` instance. Likewise, the `ResponseReceived` event contains a `$request` property as well as a `$response` property which may be used to inspect the `Illuminate\Http\Client\Response` instance. You may create [event listeners](https://laravel.com/docs/12.x/events) for these events within your application:
```


 1use Illuminate\Http\Client\Events\RequestSending;




 2 



 3class LogRequest




 4{




 5    /**




 6     * Handle the event.




 7     */




 8    public function handle(RequestSending $event): void




 9    {




10        // $event->request ...




11    }




12}




use Illuminate\Http\Client\Events\RequestSending;

class LogRequest
{
    /**
     * Handle the event.
     */
    public function handle(RequestSending $event): void
    {
        // $event->request ...
    }
}

```

Copy as markdown
  * [ Introduction ](https://laravel.com/docs/12.x/http-client#introduction)
  * [ Making Requests ](https://laravel.com/docs/12.x/http-client#making-requests)
    * [ Request Data ](https://laravel.com/docs/12.x/http-client#request-data)
    * [ Headers ](https://laravel.com/docs/12.x/http-client#headers)
    * [ Authentication ](https://laravel.com/docs/12.x/http-client#authentication)
    * [ Timeout ](https://laravel.com/docs/12.x/http-client#timeout)
    * [ Retries ](https://laravel.com/docs/12.x/http-client#retries)
    * [ Error Handling ](https://laravel.com/docs/12.x/http-client#error-handling)
    * [ Guzzle Middleware ](https://laravel.com/docs/12.x/http-client#guzzle-middleware)
    * [ Guzzle Options ](https://laravel.com/docs/12.x/http-client#guzzle-options)
  * [ Concurrent Requests ](https://laravel.com/docs/12.x/http-client#concurrent-requests)
    * [ Request Pooling ](https://laravel.com/docs/12.x/http-client#request-pooling)
    * [ Request Batching ](https://laravel.com/docs/12.x/http-client#request-batching)
  * [ Macros ](https://laravel.com/docs/12.x/http-client#macros)
  * [ Testing ](https://laravel.com/docs/12.x/http-client#testing)
    * [ Faking Responses ](https://laravel.com/docs/12.x/http-client#faking-responses)
    * [ Inspecting Requests ](https://laravel.com/docs/12.x/http-client#inspecting-requests)
    * [ Preventing Stray Requests ](https://laravel.com/docs/12.x/http-client#preventing-stray-requests)
  * [ Events ](https://laravel.com/docs/12.x/http-client#events)


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
  *   * [byte5](https://partners.laravel.com/partners/byte5)
  * [Curotec](https://partners.laravel.com/partners/curotec)
  * [Jump24](https://partners.laravel.com/partners/jump24)
  * [Vehikl](https://partners.laravel.com/partners/vehikl)
  * [Kirschbaum](https://partners.laravel.com/partners/kirschbaum)
  * [Active Logic](https://partners.laravel.com/partners/active-logic)
  * [Redberry](https://partners.laravel.com/partners/redberry)
  * [Tighten](https://partners.laravel.com/partners/tighten)
  * [ More Partners ](https://partners.laravel.com)
