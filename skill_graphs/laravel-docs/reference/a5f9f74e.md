## [Testing Servers](https://laravel.com/docs/12.x/mcp#testing-servers)
You may test your MCP servers using the built-in MCP Inspector or by writing unit tests.
### [MCP Inspector](https://laravel.com/docs/12.x/mcp#mcp-inspector)
The
You may run the inspector for any registered server:
```


1# Web server...




2php artisan mcp:inspector mcp/weather




3 



4# Local server named "weather"...




5php artisan mcp:inspector weather




# Web server...
php artisan mcp:inspector mcp/weather

# Local server named "weather"...
php artisan mcp:inspector weather

```

This command launches the MCP Inspector and provides the client settings that you may copy into your MCP client to ensure everything is configured correctly. If your web server is protected by an authentication middleware, make sure to include the required headers, such as an `Authorization` bearer token, when connecting.
### [Unit Tests](https://laravel.com/docs/12.x/mcp#unit-tests)
You may write unit tests for your MCP servers, tools, resources, and prompts.
To get started, create a new test case and invoke the desired primitive on the server that registers it. For example, to test a tool on the `WeatherServer`:
Pest PHPUnit
```


 1test('tool', function () {




 2    $response = WeatherServer::tool(CurrentWeatherTool::class, [




 3        'location' => 'New York City',




 4        'units' => 'fahrenheit',




 5    ]);




 6 



 7    $response




 8        ->assertOk()




 9        ->assertSee('The current weather in New York City is 72°F and sunny.');




10});




test('tool', function () {
    $response = WeatherServer::tool(CurrentWeatherTool::class, [
        'location' => 'New York City',
        'units' => 'fahrenheit',
    ]);

    $response
        ->assertOk()
        ->assertSee('The current weather in New York City is 72°F and sunny.');
});

```

```


 1/**




 2 * Test a tool.




 3 */




 4public function test_tool(): void




 5{




 6    $response = WeatherServer::tool(CurrentWeatherTool::class, [




 7        'location' => 'New York City',




 8        'units' => 'fahrenheit',




 9    ]);




10 



11    $response




12        ->assertOk()




13        ->assertSee('The current weather in New York City is 72°F and sunny.');




14}




/**
 * Test a tool.
 */
public function test_tool(): void
{
    $response = WeatherServer::tool(CurrentWeatherTool::class, [
        'location' => 'New York City',
        'units' => 'fahrenheit',
    ]);

    $response
        ->assertOk()
        ->assertSee('The current weather in New York City is 72°F and sunny.');
}

```

Similarly, you may test prompts and resources:
```


1$response = WeatherServer::prompt(...);




2$response = WeatherServer::resource(...);




$response = WeatherServer::prompt(...);
$response = WeatherServer::resource(...);

```

You may also act as an authenticated user by chaining the `actingAs` method before invoking the primitive:
```


1$response = WeatherServer::actingAs($user)->tool(...);




$response = WeatherServer::actingAs($user)->tool(...);

```

Once you receive the response, you may use various assertion methods to verify the content and status of the response.
You may assert that a response is successful using the `assertOk` method. This checks that the response does not have any errors:
```


1$response->assertOk();




$response->assertOk();

```

You may assert that a response contains specific text using the `assertSee` method:
```


1$response->assertSee('The current weather in New York City is 72°F and sunny.');




$response->assertSee('The current weather in New York City is 72°F and sunny.');

```

You may assert that a response contains an error using the `assertHasErrors` method:
```


1$response->assertHasErrors();




2 



3$response->assertHasErrors([




4    'Something went wrong.',




5]);




$response->assertHasErrors();

$response->assertHasErrors([
    'Something went wrong.',
]);

```

You may assert that a response does not contain an error using the `assertHasNoErrors` method:
```


1$response->assertHasNoErrors();




$response->assertHasNoErrors();

```

You may assert that a response contains specific metadata using the `assertName()`, `assertTitle()`, and `assertDescription()` methods:
```


1$response->assertName('current-weather');




2$response->assertTitle('Current Weather Tool');




3$response->assertDescription('Fetches the current weather forecast for a specified location.');




$response->assertName('current-weather');
$response->assertTitle('Current Weather Tool');
$response->assertDescription('Fetches the current weather forecast for a specified location.');

```

You may assert that notifications were sent using the `assertSentNotification` and `assertNotificationCount` methods:
```


 1$response->assertSentNotification('processing/progress', [




 2    'step' => 1,




 3    'total' => 5,




 4]);




 5 



 6$response->assertSentNotification('processing/progress', [




 7    'step' => 2,




 8    'total' => 5,




 9]);




10 



11$response->assertNotificationCount(5);




$response->assertSentNotification('processing/progress', [
    'step' => 1,
    'total' => 5,
]);

$response->assertSentNotification('processing/progress', [
    'step' => 2,
    'total' => 5,
]);

$response->assertNotificationCount(5);

```

Finally, if you wish to inspect the raw response content, you may use the `dd` or `dump` methods to output the response for debugging purposes:
```


1$response->dd();




2$response->dump();




$response->dd();
$response->dump();

```

Copy as markdown
  * [ Introduction ](https://laravel.com/docs/12.x/mcp#introduction)
  * [ Installation ](https://laravel.com/docs/12.x/mcp#installation)
    * [ Publishing Routes ](https://laravel.com/docs/12.x/mcp#publishing-routes)
  * [ Creating Servers ](https://laravel.com/docs/12.x/mcp#creating-servers)
    * [ Server Registration ](https://laravel.com/docs/12.x/mcp#server-registration)
    * [ Web Servers ](https://laravel.com/docs/12.x/mcp#web-servers)
    * [ Local Servers ](https://laravel.com/docs/12.x/mcp#local-servers)
  * [ Tools ](https://laravel.com/docs/12.x/mcp#tools)
    * [ Creating Tools ](https://laravel.com/docs/12.x/mcp#creating-tools)
    * [ Tool Input Schemas ](https://laravel.com/docs/12.x/mcp#tool-input-schemas)
    * [ Tool Output Schemas ](https://laravel.com/docs/12.x/mcp#tool-output-schemas)
    * [ Validating Tool Arguments ](https://laravel.com/docs/12.x/mcp#validating-tool-arguments)
    * [ Tool Dependency Injection ](https://laravel.com/docs/12.x/mcp#tool-dependency-injection)
    * [ Tool Annotations ](https://laravel.com/docs/12.x/mcp#tool-annotations)
    * [ Conditional Tool Registration ](https://laravel.com/docs/12.x/mcp#conditional-tool-registration)
    * [ Tool Responses ](https://laravel.com/docs/12.x/mcp#tool-responses)
  * [ Prompts ](https://laravel.com/docs/12.x/mcp#prompts)
    * [ Creating Prompts ](https://laravel.com/docs/12.x/mcp#creating-prompts)
    * [ Prompt Arguments ](https://laravel.com/docs/12.x/mcp#prompt-arguments)
    * [ Validating Prompt Arguments ](https://laravel.com/docs/12.x/mcp#validating-prompt-arguments)
    * [ Prompt Dependency Injection ](https://laravel.com/docs/12.x/mcp#prompt-dependency-injection)
    * [ Conditional Prompt Registration ](https://laravel.com/docs/12.x/mcp#conditional-prompt-registration)
    * [ Prompt Responses ](https://laravel.com/docs/12.x/mcp#prompt-responses)
  * [ Resources ](https://laravel.com/docs/12.x/mcp#resources)
    * [ Creating Resources ](https://laravel.com/docs/12.x/mcp#creating-resources)
    * [ Resource Templates ](https://laravel.com/docs/12.x/mcp#resource-templates)
    * [ Resource URI and MIME Type ](https://laravel.com/docs/12.x/mcp#resource-uri-and-mime-type)
    * [ Resource Request ](https://laravel.com/docs/12.x/mcp#resource-request)
    * [ Resource Dependency Injection ](https://laravel.com/docs/12.x/mcp#resource-dependency-injection)
    * [ Resource Annotations ](https://laravel.com/docs/12.x/mcp#resource-annotations)
    * [ Conditional Resource Registration ](https://laravel.com/docs/12.x/mcp#conditional-resource-registration)
    * [ Resource Responses ](https://laravel.com/docs/12.x/mcp#resource-responses)
  * [ Metadata ](https://laravel.com/docs/12.x/mcp#metadata)
  * [ Authentication ](https://laravel.com/docs/12.x/mcp#authentication)
    * [ OAuth 2.1 ](https://laravel.com/docs/12.x/mcp#oauth)
    * [ Sanctum ](https://laravel.com/docs/12.x/mcp#sanctum)
  * [ Authorization ](https://laravel.com/docs/12.x/mcp#authorization)
  * [ Testing Servers ](https://laravel.com/docs/12.x/mcp#testing-servers)
    * [ MCP Inspector ](https://laravel.com/docs/12.x/mcp#mcp-inspector)
    * [ Unit Tests ](https://laravel.com/docs/12.x/mcp#unit-tests)


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
  *   * [Vehikl](https://partners.laravel.com/partners/vehikl)
  * [Redberry](https://partners.laravel.com/partners/redberry)
  * [Curotec](https://partners.laravel.com/partners/curotec)
  * [Jump24](https://partners.laravel.com/partners/jump24)
  * [byte5](https://partners.laravel.com/partners/byte5)
  * [Active Logic](https://partners.laravel.com/partners/active-logic)
  * [Kirschbaum](https://partners.laravel.com/partners/kirschbaum)
  * [Tighten](https://partners.laravel.com/partners/tighten)
  * [ More Partners ](https://partners.laravel.com)
