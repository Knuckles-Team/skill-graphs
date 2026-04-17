## [Testing](https://laravel.com/docs/12.x/passport#testing)
Passport's `actingAs` method may be used to specify the currently authenticated user as well as its scopes. The first argument given to the `actingAs` method is the user instance and the second is an array of scopes that should be granted to the user's token:
Pest PHPUnit
```


 1use App\Models\User;




 2use Laravel\Passport\Passport;




 3 



 4test('orders can be created', function () {




 5    Passport::actingAs(




 6        User::factory()->create(),




 7        ['orders:create']




 8    );




 9 



10    $response = $this->post('/api/orders');




11 



12    $response->assertStatus(201);




13});




use App\Models\User;
use Laravel\Passport\Passport;

test('orders can be created', function () {
    Passport::actingAs(
        User::factory()->create(),
        ['orders:create']
    );

    $response = $this->post('/api/orders');

    $response->assertStatus(201);
});

```

```


 1use App\Models\User;




 2use Laravel\Passport\Passport;




 3 



 4public function test_orders_can_be_created(): void




 5{




 6    Passport::actingAs(




 7        User::factory()->create(),




 8        ['orders:create']




 9    );




10 



11    $response = $this->post('/api/orders');




12 



13    $response->assertStatus(201);




14}




use App\Models\User;
use Laravel\Passport\Passport;

public function test_orders_can_be_created(): void
{
    Passport::actingAs(
        User::factory()->create(),
        ['orders:create']
    );

    $response = $this->post('/api/orders');

    $response->assertStatus(201);
}

```

Passport's `actingAsClient` method may be used to specify the currently authenticated client as well as its scopes. The first argument given to the `actingAsClient` method is the client instance and the second is an array of scopes that should be granted to the client's token:
Pest PHPUnit
```


 1use Laravel\Passport\Client;




 2use Laravel\Passport\Passport;




 3 



 4test('servers can be retrieved', function () {




 5    Passport::actingAsClient(




 6        Client::factory()->create(),




 7        ['servers:read']




 8    );




 9 



10    $response = $this->get('/api/servers');




11 



12    $response->assertStatus(200);




13});




use Laravel\Passport\Client;
use Laravel\Passport\Passport;

test('servers can be retrieved', function () {
    Passport::actingAsClient(
        Client::factory()->create(),
        ['servers:read']
    );

    $response = $this->get('/api/servers');

    $response->assertStatus(200);
});

```

```


 1use Laravel\Passport\Client;




 2use Laravel\Passport\Passport;




 3 



 4public function test_servers_can_be_retrieved(): void




 5{




 6    Passport::actingAsClient(




 7        Client::factory()->create(),




 8        ['servers:read']




 9    );




10 



11    $response = $this->get('/api/servers');




12 



13    $response->assertStatus(200);




14}




use Laravel\Passport\Client;
use Laravel\Passport\Passport;

public function test_servers_can_be_retrieved(): void
{
    Passport::actingAsClient(
        Client::factory()->create(),
        ['servers:read']
    );

    $response = $this->get('/api/servers');

    $response->assertStatus(200);
}

```

Copy as markdown
  * [ Introduction ](https://laravel.com/docs/12.x/passport#introduction)
    * [ Passport or Sanctum? ](https://laravel.com/docs/12.x/passport#passport-or-sanctum)
  * [ Installation ](https://laravel.com/docs/12.x/passport#installation)
    * [ Deploying Passport ](https://laravel.com/docs/12.x/passport#deploying-passport)
    * [ Upgrading Passport ](https://laravel.com/docs/12.x/passport#upgrading-passport)
  * [ Configuration ](https://laravel.com/docs/12.x/passport#configuration)
    * [ Token Lifetimes ](https://laravel.com/docs/12.x/passport#token-lifetimes)
    * [ Overriding Default Models ](https://laravel.com/docs/12.x/passport#overriding-default-models)
    * [ Overriding Routes ](https://laravel.com/docs/12.x/passport#overriding-routes)
  * [ Authorization Code Grant ](https://laravel.com/docs/12.x/passport#authorization-code-grant)
    * [ Managing Clients ](https://laravel.com/docs/12.x/passport#managing-clients)
    * [ Requesting Tokens ](https://laravel.com/docs/12.x/passport#requesting-tokens)
    * [ Managing Tokens ](https://laravel.com/docs/12.x/passport#managing-tokens)
    * [ Refreshing Tokens ](https://laravel.com/docs/12.x/passport#refreshing-tokens)
    * [ Revoking Tokens ](https://laravel.com/docs/12.x/passport#revoking-tokens)
    * [ Purging Tokens ](https://laravel.com/docs/12.x/passport#purging-tokens)
  * [ Authorization Code Grant With PKCE ](https://laravel.com/docs/12.x/passport#code-grant-pkce)
    * [ Creating the Client ](https://laravel.com/docs/12.x/passport#creating-a-auth-pkce-grant-client)
    * [ Requesting Tokens ](https://laravel.com/docs/12.x/passport#requesting-auth-pkce-grant-tokens)
  * [ Device Authorization Grant ](https://laravel.com/docs/12.x/passport#device-authorization-grant)
    * [ Creating a Device Code Grant Client ](https://laravel.com/docs/12.x/passport#creating-a-device-authorization-grant-client)
    * [ Requesting Tokens ](https://laravel.com/docs/12.x/passport#requesting-device-authorization-grant-tokens)
  * [ Password Grant ](https://laravel.com/docs/12.x/passport#password-grant)
    * [ Creating a Password Grant Client ](https://laravel.com/docs/12.x/passport#creating-a-password-grant-client)
    * [ Requesting Tokens ](https://laravel.com/docs/12.x/passport#requesting-password-grant-tokens)
    * [ Requesting All Scopes ](https://laravel.com/docs/12.x/passport#requesting-all-scopes)
    * [ Customizing the User Provider ](https://laravel.com/docs/12.x/passport#customizing-the-user-provider)
    * [ Customizing the Username Field ](https://laravel.com/docs/12.x/passport#customizing-the-username-field)
    * [ Customizing the Password Validation ](https://laravel.com/docs/12.x/passport#customizing-the-password-validation)
  * [ Implicit Grant ](https://laravel.com/docs/12.x/passport#implicit-grant)
  * [ Client Credentials Grant ](https://laravel.com/docs/12.x/passport#client-credentials-grant)
  * [ Personal Access Tokens ](https://laravel.com/docs/12.x/passport#personal-access-tokens)
    * [ Creating a Personal Access Client ](https://laravel.com/docs/12.x/passport#creating-a-personal-access-client)
    * [ Customizing the User Provider ](https://laravel.com/docs/12.x/passport#customizing-the-user-provider-for-pat)
    * [ Managing Personal Access Tokens ](https://laravel.com/docs/12.x/passport#managing-personal-access-tokens)
  * [ Protecting Routes ](https://laravel.com/docs/12.x/passport#protecting-routes)
    * [ Via Middleware ](https://laravel.com/docs/12.x/passport#via-middleware)
    * [ Passing the Access Token ](https://laravel.com/docs/12.x/passport#passing-the-access-token)
  * [ Token Scopes ](https://laravel.com/docs/12.x/passport#token-scopes)
    * [ Defining Scopes ](https://laravel.com/docs/12.x/passport#defining-scopes)
    * [ Default Scope ](https://laravel.com/docs/12.x/passport#default-scope)
    * [ Assigning Scopes to Tokens ](https://laravel.com/docs/12.x/passport#assigning-scopes-to-tokens)
    * [ Checking Scopes ](https://laravel.com/docs/12.x/passport#checking-scopes)
  * [ SPA Authentication ](https://laravel.com/docs/12.x/passport#spa-authentication)
  * [ Events ](https://laravel.com/docs/12.x/passport#events)
  * [ Testing ](https://laravel.com/docs/12.x/passport#testing)


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
  *   * [Active Logic](https://partners.laravel.com/partners/active-logic)
  * [Kirschbaum](https://partners.laravel.com/partners/kirschbaum)
  * [Curotec](https://partners.laravel.com/partners/curotec)
  * [Redberry](https://partners.laravel.com/partners/redberry)
  * [Jump24](https://partners.laravel.com/partners/jump24)
  * [byte5](https://partners.laravel.com/partners/byte5)
  * [Tighten](https://partners.laravel.com/partners/tighten)
  * [Vehikl](https://partners.laravel.com/partners/vehikl)
  * [ More Partners ](https://partners.laravel.com)
