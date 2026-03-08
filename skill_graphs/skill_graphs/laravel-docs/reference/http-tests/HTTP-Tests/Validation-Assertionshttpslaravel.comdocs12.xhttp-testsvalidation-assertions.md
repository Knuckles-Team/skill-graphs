## [Validation Assertions](https://laravel.com/docs/12.x/http-tests#validation-assertions)
Laravel provides two primary validation related assertions that you may use to ensure the data provided in your request was either valid or invalid.
#### [assertValid](https://laravel.com/docs/12.x/http-tests#validation-assert-valid)
Assert that the response has no validation errors for the given keys. This method may be used for asserting against responses where the validation errors are returned as a JSON structure or where the validation errors have been flashed to the session:
```


1// Assert that no validation errors are present...




2$response->assertValid();




3 



4// Assert that the given keys do not have validation errors...




5$response->assertValid(['name', 'email']);




// Assert that no validation errors are present...
$response->assertValid();

// Assert that the given keys do not have validation errors...
$response->assertValid(['name', 'email']);

```

#### [assertInvalid](https://laravel.com/docs/12.x/http-tests#validation-assert-invalid)
Assert that the response has validation errors for the given keys. This method may be used for asserting against responses where the validation errors are returned as a JSON structure or where the validation errors have been flashed to the session:
```


1$response->assertInvalid(['name', 'email']);




$response->assertInvalid(['name', 'email']);

```

You may also assert that a given key has a particular validation error message. When doing so, you may provide the entire message or only a small portion of the message:
```


1$response->assertInvalid([




2    'name' => 'The name field is required.',




3    'email' => 'valid email address',




4]);




$response->assertInvalid([
    'name' => 'The name field is required.',
    'email' => 'valid email address',
]);

```

Copy as markdown
  * [ Introduction ](https://laravel.com/docs/12.x/http-tests#introduction)
  * [ Making Requests ](https://laravel.com/docs/12.x/http-tests#making-requests)
    * [ Customizing Request Headers ](https://laravel.com/docs/12.x/http-tests#customizing-request-headers)
    * [ Cookies ](https://laravel.com/docs/12.x/http-tests#cookies)
    * [ Session / Authentication ](https://laravel.com/docs/12.x/http-tests#session-and-authentication)
    * [ Debugging Responses ](https://laravel.com/docs/12.x/http-tests#debugging-responses)
    * [ Exception Handling ](https://laravel.com/docs/12.x/http-tests#exception-handling)
  * [ Testing JSON APIs ](https://laravel.com/docs/12.x/http-tests#testing-json-apis)
    * [ Fluent JSON Testing ](https://laravel.com/docs/12.x/http-tests#fluent-json-testing)
  * [ Testing File Uploads ](https://laravel.com/docs/12.x/http-tests#testing-file-uploads)
  * [ Testing Views ](https://laravel.com/docs/12.x/http-tests#testing-views)
    * [ Rendering Blade and Components ](https://laravel.com/docs/12.x/http-tests#rendering-blade-and-components)
  * [ Caching Routes ](https://laravel.com/docs/12.x/http-tests#caching-routes)
  * [ Available Assertions ](https://laravel.com/docs/12.x/http-tests#available-assertions)
    * [ Response Assertions ](https://laravel.com/docs/12.x/http-tests#response-assertions)
    * [ Authentication Assertions ](https://laravel.com/docs/12.x/http-tests#authentication-assertions)
    * [ Validation Assertions ](https://laravel.com/docs/12.x/http-tests#validation-assertions)


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
  *   * [Redberry](https://partners.laravel.com/partners/redberry)
  * [Active Logic](https://partners.laravel.com/partners/active-logic)
  * [Tighten](https://partners.laravel.com/partners/tighten)
  * [byte5](https://partners.laravel.com/partners/byte5)
  * [Jump24](https://partners.laravel.com/partners/jump24)
  * [Vehikl](https://partners.laravel.com/partners/vehikl)
  * [Kirschbaum](https://partners.laravel.com/partners/kirschbaum)
  * [Curotec](https://partners.laravel.com/partners/curotec)
  * [ More Partners ](https://partners.laravel.com)
