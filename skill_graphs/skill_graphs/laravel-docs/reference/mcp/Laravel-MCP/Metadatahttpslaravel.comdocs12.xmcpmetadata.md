## [Metadata](https://laravel.com/docs/12.x/mcp#metadata)
Laravel MCP also supports the `_meta` field as defined in the
You can attach metadata to individual response content using the `withMeta` method:
```


 1use Laravel\Mcp\Request;




 2use Laravel\Mcp\Response;




 3 



 4/**




 5 * Handle the tool request.




 6 */




 7public function handle(Request $request): Response




 8{




 9    return Response::text('The weather is sunny.')




10        ->withMeta(['source' => 'weather-api', 'cached' => true]);




11}




use Laravel\Mcp\Request;
use Laravel\Mcp\Response;

/**
 * Handle the tool request.
 */
public function handle(Request $request): Response
{
    return Response::text('The weather is sunny.')
        ->withMeta(['source' => 'weather-api', 'cached' => true]);
}

```

For result-level metadata that applies to the entire response envelope, wrap your responses with `Response::make` and call `withMeta` on the returned response factory instance:
```


 1use Laravel\Mcp\Request;




 2use Laravel\Mcp\Response;




 3use Laravel\Mcp\ResponseFactory;




 4 



 5/**




 6 * Handle the tool request.




 7 */




 8public function handle(Request $request): ResponseFactory




 9{




10    return Response::make(




11        Response::text('The weather is sunny.')




12    )->withMeta(['request_id' => '12345']);




13}




use Laravel\Mcp\Request;
use Laravel\Mcp\Response;
use Laravel\Mcp\ResponseFactory;

/**
 * Handle the tool request.
 */
public function handle(Request $request): ResponseFactory
{
    return Response::make(
        Response::text('The weather is sunny.')
    )->withMeta(['request_id' => '12345']);
}

```

To attach metadata to a tool, resource, or prompt itself, define a `$meta` property on the class:
```


 1use Laravel\Mcp\Server\Attributes\Description;




 2use Laravel\Mcp\Server\Tool;




 3 



 4#[Description('Fetches the current weather forecast.')]




 5class CurrentWeatherTool extends Tool




 6{




 7    protected ?array $meta = [




 8        'version' => '2.0',




 9        'author' => 'Weather Team',




10    ];




11 



12    // ...




13}




use Laravel\Mcp\Server\Attributes\Description;
use Laravel\Mcp\Server\Tool;

#[Description('Fetches the current weather forecast.')]
class CurrentWeatherTool extends Tool
{
    protected ?array $meta = [
        'version' => '2.0',
        'author' => 'Weather Team',
    ];

    // ...
}

```
