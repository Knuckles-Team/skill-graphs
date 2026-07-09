## [Tools](https://laravel.com/docs/12.x/mcp#tools)
Tools enable your server to expose functionality that AI clients can call. They allow language models to perform actions, run code, or interact with external systems:
```


 1<?php




 2 



 3namespace App\Mcp\Tools;




 4 



 5use Illuminate\Contracts\JsonSchema\JsonSchema;




 6use Laravel\Mcp\Request;




 7use Laravel\Mcp\Response;




 8use Laravel\Mcp\Server\Attributes\Description;




 9use Laravel\Mcp\Server\Tool;




10 



11#[Description('Fetches the current weather forecast for a specified location.')]




12class CurrentWeatherTool extends Tool




13{




14    /**




15     * Handle the tool request.




16     */




17    public function handle(Request $request): Response




18    {




19        $location = $request->get('location');




20 



21        // Get weather...




22 



23        return Response::text('The weather is...');




24    }




25 



26    /**




27     * Get the tool's input schema.




28     *




29     * @return array<string, \Illuminate\JsonSchema\Types\Type>




30     */




31    public function schema(JsonSchema $schema): array




32    {




33        return [




34            'location' => $schema->string()




35                ->description('The location to get the weather for.')




36                ->required(),




37        ];




38    }




39}




<?php

namespace App\Mcp\Tools;

use Illuminate\Contracts\JsonSchema\JsonSchema;
use Laravel\Mcp\Request;
use Laravel\Mcp\Response;
use Laravel\Mcp\Server\Attributes\Description;
use Laravel\Mcp\Server\Tool;

#[Description('Fetches the current weather forecast for a specified location.')]
class CurrentWeatherTool extends Tool
{
    /**
     * Handle the tool request.
     */
    public function handle(Request $request): Response
    {
        $location = $request->get('location');

        // Get weather...

        return Response::text('The weather is...');
    }

    /**
     * Get the tool's input schema.
     *
     * @return array<string, \Illuminate\JsonSchema\Types\Type>
     */
    public function schema(JsonSchema $schema): array
    {
        return [
            'location' => $schema->string()
                ->description('The location to get the weather for.')
                ->required(),
        ];
    }
}

```

### [Creating Tools](https://laravel.com/docs/12.x/mcp#creating-tools)
To create a tool, run the `make:mcp-tool` Artisan command:
```


1php artisan make:mcp-tool CurrentWeatherTool




php artisan make:mcp-tool CurrentWeatherTool

```

After creating a tool, register it in your server's `$tools` property:
```


 1<?php




 2 



 3namespace App\Mcp\Servers;




 4 



 5use App\Mcp\Tools\CurrentWeatherTool;




 6use Laravel\Mcp\Server;




 7 



 8class WeatherServer extends Server




 9{




10    /**




11     * The tools registered with this MCP server.




12     *




13     * @var array<int, class-string<\Laravel\Mcp\Server\Tool>>




14     */




15    protected array $tools = [




16        CurrentWeatherTool::class,




17    ];




18}




<?php

namespace App\Mcp\Servers;

use App\Mcp\Tools\CurrentWeatherTool;
use Laravel\Mcp\Server;

class WeatherServer extends Server
{
    /**
     * The tools registered with this MCP server.
     *
     * @var array<int, class-string<\Laravel\Mcp\Server\Tool>>
     */
    protected array $tools = [
        CurrentWeatherTool::class,
    ];
}

```

#### [Tool Name, Title, and Description](https://laravel.com/docs/12.x/mcp#tool-name-title-description)
By default, the tool's name and title are derived from the class name. For example, `CurrentWeatherTool` will have a name of `current-weather` and a title of `Current Weather Tool`. You may customize these values using the `Name` and `Title` attributes:
```


1use Laravel\Mcp\Server\Attributes\Name;




2use Laravel\Mcp\Server\Attributes\Title;




3 



4#[Name('get-optimistic-weather')]




5#[Title('Get Optimistic Weather Forecast')]




6class CurrentWeatherTool extends Tool




7{




8    // ...




9}




use Laravel\Mcp\Server\Attributes\Name;
use Laravel\Mcp\Server\Attributes\Title;

#[Name('get-optimistic-weather')]
#[Title('Get Optimistic Weather Forecast')]
class CurrentWeatherTool extends Tool
{
    // ...
}

```

Tool descriptions are not automatically generated. You should always provide a meaningful description using the `Description` attribute:
```


1use Laravel\Mcp\Server\Attributes\Description;




2 



3#[Description('Fetches the current weather forecast for a specified location.')]




4class CurrentWeatherTool extends Tool




5{




6    //




7}




use Laravel\Mcp\Server\Attributes\Description;

#[Description('Fetches the current weather forecast for a specified location.')]
class CurrentWeatherTool extends Tool
{
    //
}

```

The description is a critical part of the tool's metadata, as it helps AI models understand when and how to use the tool effectively.
### [Tool Input Schemas](https://laravel.com/docs/12.x/mcp#tool-input-schemas)
Tools can define input schemas to specify what arguments they accept from AI clients. Use Laravel's `Illuminate\Contracts\JsonSchema\JsonSchema` builder to define your tool's input requirements:
```


 1<?php




 2 



 3namespace App\Mcp\Tools;




 4 



 5use Illuminate\Contracts\JsonSchema\JsonSchema;




 6use Laravel\Mcp\Server\Tool;




 7 



 8class CurrentWeatherTool extends Tool




 9{




10    /**




11     * Get the tool's input schema.




12     *




13     * @return array<string, \Illuminate\JsonSchema\Types\Type>




14     */




15    public function schema(JsonSchema $schema): array




16    {




17        return [




18            'location' => $schema->string()




19                ->description('The location to get the weather for.')




20                ->required(),




21 



22            'units' => $schema->string()




23                ->enum(['celsius', 'fahrenheit'])




24                ->description('The temperature units to use.')




25                ->default('celsius'),




26        ];




27    }




28}




<?php

namespace App\Mcp\Tools;

use Illuminate\Contracts\JsonSchema\JsonSchema;
use Laravel\Mcp\Server\Tool;

class CurrentWeatherTool extends Tool
{
    /**
     * Get the tool's input schema.
     *
     * @return array<string, \Illuminate\JsonSchema\Types\Type>
     */
    public function schema(JsonSchema $schema): array
    {
        return [
            'location' => $schema->string()
                ->description('The location to get the weather for.')
                ->required(),

            'units' => $schema->string()
                ->enum(['celsius', 'fahrenheit'])
                ->description('The temperature units to use.')
                ->default('celsius'),
        ];
    }
}

```

### [Tool Output Schemas](https://laravel.com/docs/12.x/mcp#tool-output-schemas)
Tools can define `outputSchema` method to define your tool's output structure:
```


 1<?php




 2 



 3namespace App\Mcp\Tools;




 4 



 5use Illuminate\Contracts\JsonSchema\JsonSchema;




 6use Laravel\Mcp\Server\Tool;




 7 



 8class CurrentWeatherTool extends Tool




 9{




10    /**




11     * Get the tool's output schema.




12     *




13     * @return array<string, \Illuminate\JsonSchema\Types\Type>




14     */




15    public function outputSchema(JsonSchema $schema): array




16    {




17        return [




18            'temperature' => $schema->number()




19                ->description('Temperature in Celsius')




20                ->required(),




21 



22            'conditions' => $schema->string()




23                ->description('Weather conditions')




24                ->required(),




25 



26            'humidity' => $schema->integer()




27                ->description('Humidity percentage')




28                ->required(),




29        ];




30    }




31}




<?php

namespace App\Mcp\Tools;

use Illuminate\Contracts\JsonSchema\JsonSchema;
use Laravel\Mcp\Server\Tool;

class CurrentWeatherTool extends Tool
{
    /**
     * Get the tool's output schema.
     *
     * @return array<string, \Illuminate\JsonSchema\Types\Type>
     */
    public function outputSchema(JsonSchema $schema): array
    {
        return [
            'temperature' => $schema->number()
                ->description('Temperature in Celsius')
                ->required(),

            'conditions' => $schema->string()
                ->description('Weather conditions')
                ->required(),

            'humidity' => $schema->integer()
                ->description('Humidity percentage')
                ->required(),
        ];
    }
}

```

### [Validating Tool Arguments](https://laravel.com/docs/12.x/mcp#validating-tool-arguments)
JSON Schema definitions provide a basic structure for tool arguments, but you may also want to enforce more complex validation rules.
Laravel MCP integrates seamlessly with Laravel's [validation features](https://laravel.com/docs/12.x/validation). You may validate incoming tool arguments within your tool's `handle` method:
```


 1<?php




 2 



 3namespace App\Mcp\Tools;




 4 



 5use Laravel\Mcp\Request;




 6use Laravel\Mcp\Response;




 7use Laravel\Mcp\Server\Tool;




 8 



 9class CurrentWeatherTool extends Tool




10{




11    /**




12     * Handle the tool request.




13     */




14    public function handle(Request $request): Response




15    {




16        $validated = $request->validate([




17            'location' => 'required|string|max:100',




18            'units' => 'in:celsius,fahrenheit',




19        ]);




20 



21        // Fetch weather data using the validated arguments...




22    }




23}




<?php

namespace App\Mcp\Tools;

use Laravel\Mcp\Request;
use Laravel\Mcp\Response;
use Laravel\Mcp\Server\Tool;

class CurrentWeatherTool extends Tool
{
    /**
     * Handle the tool request.
     */
    public function handle(Request $request): Response
    {
        $validated = $request->validate([
            'location' => 'required|string|max:100',
            'units' => 'in:celsius,fahrenheit',
        ]);

        // Fetch weather data using the validated arguments...
    }
}

```

On validation failure, AI clients will act based on the error messages you provide. As such, it is critical to provide clear and actionable error messages:
```


1$validated = $request->validate([




2    'location' => ['required','string','max:100'],




3    'units' => 'in:celsius,fahrenheit',




4],[




5    'location.required' => 'You must specify a location to get the weather for. For example, "New York City" or "Tokyo".',




6    'units.in' => 'You must specify either "celsius" or "fahrenheit" for the units.',




7]);




$validated = $request->validate([
    'location' => ['required','string','max:100'],
    'units' => 'in:celsius,fahrenheit',
],[
    'location.required' => 'You must specify a location to get the weather for. For example, "New York City" or "Tokyo".',
    'units.in' => 'You must specify either "celsius" or "fahrenheit" for the units.',
]);

```

#### [Tool Dependency Injection](https://laravel.com/docs/12.x/mcp#tool-dependency-injection)
The Laravel [service container](https://laravel.com/docs/12.x/container) is used to resolve all tools. As a result, you are able to type-hint any dependencies your tool may need in its constructor. The declared dependencies will automatically be resolved and injected into the tool instance:
```


 1<?php




 2 



 3namespace App\Mcp\Tools;




 4 



 5use App\Repositories\WeatherRepository;




 6use Laravel\Mcp\Server\Tool;




 7 



 8class CurrentWeatherTool extends Tool




 9{




10    /**




11     * Create a new tool instance.




12     */




13    public function __construct(




14        protected WeatherRepository $weather,




15    ) {}




16 



17    // ...




18}




<?php

namespace App\Mcp\Tools;

use App\Repositories\WeatherRepository;
use Laravel\Mcp\Server\Tool;

class CurrentWeatherTool extends Tool
{
    /**
     * Create a new tool instance.
     */
    public function __construct(
        protected WeatherRepository $weather,
    ) {}

    // ...
}

```

In addition to constructor injection, you may also type-hint dependencies in your tool's `handle()` method. The service container will automatically resolve and inject the dependencies when the method is called:
```


 1<?php




 2 



 3namespace App\Mcp\Tools;




 4 



 5use App\Repositories\WeatherRepository;




 6use Laravel\Mcp\Request;




 7use Laravel\Mcp\Response;




 8use Laravel\Mcp\Server\Tool;




 9 



10class CurrentWeatherTool extends Tool




11{




12    /**




13     * Handle the tool request.




14     */




15    public function handle(Request $request, WeatherRepository $weather): Response




16    {




17        $location = $request->get('location');




18 



19        $forecast = $weather->getForecastFor($location);




20 



21        // ...




22    }




23}




<?php

namespace App\Mcp\Tools;

use App\Repositories\WeatherRepository;
use Laravel\Mcp\Request;
use Laravel\Mcp\Response;
use Laravel\Mcp\Server\Tool;

class CurrentWeatherTool extends Tool
{
    /**
     * Handle the tool request.
     */
    public function handle(Request $request, WeatherRepository $weather): Response
    {
        $location = $request->get('location');

        $forecast = $weather->getForecastFor($location);

        // ...
    }
}

```

### [Tool Annotations](https://laravel.com/docs/12.x/mcp#tool-annotations)
You may enhance your tools with
```


 1<?php




 2 



 3namespace App\Mcp\Tools;




 4 



 5use Laravel\Mcp\Server\Tools\Annotations\IsIdempotent;




 6use Laravel\Mcp\Server\Tools\Annotations\IsReadOnly;




 7use Laravel\Mcp\Server\Tool;




 8 



 9#[IsIdempotent]




10#[IsReadOnly]




11class CurrentWeatherTool extends Tool




12{




13    //




14}




<?php

namespace App\Mcp\Tools;

use Laravel\Mcp\Server\Tools\Annotations\IsIdempotent;
use Laravel\Mcp\Server\Tools\Annotations\IsReadOnly;
use Laravel\Mcp\Server\Tool;

#[IsIdempotent]
#[IsReadOnly]
class CurrentWeatherTool extends Tool
{
    //
}

```

Available annotations include:
Annotation | Type | Description
---|---|---
`#[IsReadOnly]` | boolean | Indicates the tool does not modify its environment.
`#[IsDestructive]` | boolean | Indicates the tool may perform destructive updates (only meaningful when not read-only).
`#[IsIdempotent]` | boolean | Indicates repeated calls with same arguments have no additional effect (when not read-only).
`#[IsOpenWorld]` | boolean | Indicates the tool may interact with external entities.
Annotation values can be explicitly set using boolean arguments:
```


 1use Laravel\Mcp\Server\Tools\Annotations\IsReadOnly;




 2use Laravel\Mcp\Server\Tools\Annotations\IsDestructive;




 3use Laravel\Mcp\Server\Tools\Annotations\IsOpenWorld;




 4use Laravel\Mcp\Server\Tools\Annotations\IsIdempotent;




 5use Laravel\Mcp\Server\Tool;




 6 



 7#[IsReadOnly(true)]




 8#[IsDestructive(false)]




 9#[IsOpenWorld(false)]




10#[IsIdempotent(true)]




11class CurrentWeatherTool extends Tool




12{




13    //




14}




use Laravel\Mcp\Server\Tools\Annotations\IsReadOnly;
use Laravel\Mcp\Server\Tools\Annotations\IsDestructive;
use Laravel\Mcp\Server\Tools\Annotations\IsOpenWorld;
use Laravel\Mcp\Server\Tools\Annotations\IsIdempotent;
use Laravel\Mcp\Server\Tool;

#[IsReadOnly(true)]
#[IsDestructive(false)]
#[IsOpenWorld(false)]
#[IsIdempotent(true)]
class CurrentWeatherTool extends Tool
{
    //
}

```

### [Conditional Tool Registration](https://laravel.com/docs/12.x/mcp#conditional-tool-registration)
You may conditionally register tools at runtime by implementing the `shouldRegister` method in your tool class. This method allows you to determine whether a tool should be available based on application state, configuration, or request parameters:
```


 1<?php




 2 



 3namespace App\Mcp\Tools;




 4 



 5use Laravel\Mcp\Request;




 6use Laravel\Mcp\Server\Tool;




 7 



 8class CurrentWeatherTool extends Tool




 9{




10    /**




11     * Determine if the tool should be registered.




12     */




13    public function shouldRegister(Request $request): bool




14    {




15        return $request?->user()?->subscribed() ?? false;




16    }




17}




<?php

namespace App\Mcp\Tools;

use Laravel\Mcp\Request;
use Laravel\Mcp\Server\Tool;

class CurrentWeatherTool extends Tool
{
    /**
     * Determine if the tool should be registered.
     */
    public function shouldRegister(Request $request): bool
    {
        return $request?->user()?->subscribed() ?? false;
    }
}

```

When a tool's `shouldRegister` method returns `false`, it will not appear in the list of available tools and cannot be invoked by AI clients.
### [Tool Responses](https://laravel.com/docs/12.x/mcp#tool-responses)
Tools must return an instance of `Laravel\Mcp\Response`. The Response class provides several convenient methods for creating different types of responses:
For simple text responses, use the `text` method:
```


 1use Laravel\Mcp\Request;




 2use Laravel\Mcp\Response;




 3 



 4/**




 5 * Handle the tool request.




 6 */




 7public function handle(Request $request): Response




 8{




 9    // ...




10 



11    return Response::text('Weather Summary: Sunny, 72°F');




12}




use Laravel\Mcp\Request;
use Laravel\Mcp\Response;

/**
 * Handle the tool request.
 */
public function handle(Request $request): Response
{
    // ...

    return Response::text('Weather Summary: Sunny, 72°F');
}

```

To indicate an error occurred during tool execution, use the `error` method:
```


1return Response::error('Unable to fetch weather data. Please try again.');




return Response::error('Unable to fetch weather data. Please try again.');

```

To return image or audio content, use the `image` and `audio` methods:
```


1return Response::image(file_get_contents(storage_path('weather/radar.png')), 'image/png');




2 



3return Response::audio(file_get_contents(storage_path('weather/alert.mp3')), 'audio/mp3');




return Response::image(file_get_contents(storage_path('weather/radar.png')), 'image/png');

return Response::audio(file_get_contents(storage_path('weather/alert.mp3')), 'audio/mp3');

```

You may also load image and audio content directly from a Laravel filesystem disk using the `fromStorage` method. The MIME type will be automatically detected from the file:
```


1return Response::fromStorage('weather/radar.png');




return Response::fromStorage('weather/radar.png');

```

If needed, you may specify a particular disk or override the MIME type:
```


1return Response::fromStorage('weather/radar.png', disk: 's3');




2 



3return Response::fromStorage('weather/radar.png', mimeType: 'image/webp');




return Response::fromStorage('weather/radar.png', disk: 's3');

return Response::fromStorage('weather/radar.png', mimeType: 'image/webp');

```

#### [Multiple Content Responses](https://laravel.com/docs/12.x/mcp#multiple-content-responses)
Tools can return multiple pieces of content by returning an array of `Response` instances:
```


 1use Laravel\Mcp\Request;




 2use Laravel\Mcp\Response;




 3 



 4/**




 5 * Handle the tool request.




 6 *




 7 * @return array<int, \Laravel\Mcp\Response>




 8 */




 9public function handle(Request $request): array




10{




11    // ...




12 



13    return [




14        Response::text('Weather Summary: Sunny, 72°F'),




15        Response::text('**Detailed Forecast**\n- Morning: 65°F\n- Afternoon: 78°F\n- Evening: 70°F')




16    ];




17}




use Laravel\Mcp\Request;
use Laravel\Mcp\Response;

/**
 * Handle the tool request.
 *
 * @return array<int, \Laravel\Mcp\Response>
 */
public function handle(Request $request): array
{
    // ...

    return [
        Response::text('Weather Summary: Sunny, 72°F'),
        Response::text('**Detailed Forecast**\n- Morning: 65°F\n- Afternoon: 78°F\n- Evening: 70°F')
    ];
}

```

#### [Structured Responses](https://laravel.com/docs/12.x/mcp#structured-responses)
Tools can return `structured` method. This provides parseable data for AI clients while maintaining backward compatibility with a JSON-encoded text representation:
```


1return Response::structured([




2    'temperature' => 22.5,




3    'conditions' => 'Partly cloudy',




4    'humidity' => 65,




5]);




return Response::structured([
    'temperature' => 22.5,
    'conditions' => 'Partly cloudy',
    'humidity' => 65,
]);

```

If you need to provide custom text alongside structured content, use the `withStructuredContent` method on the response factory:
```


1return Response::make(




2    Response::text('Weather is 22.5°C and sunny')




3)->withStructuredContent([




4    'temperature' => 22.5,




5    'conditions' => 'Sunny',




6]);




return Response::make(
    Response::text('Weather is 22.5°C and sunny')
)->withStructuredContent([
    'temperature' => 22.5,
    'conditions' => 'Sunny',
]);

```

#### [Streaming Responses](https://laravel.com/docs/12.x/mcp#streaming-responses)
For long-running operations or real-time data streaming, tools can return a `handle` method. This enables sending intermediate updates to the client before the final response:
```


 1<?php




 2 



 3namespace App\Mcp\Tools;




 4 



 5use Generator;




 6use Laravel\Mcp\Request;




 7use Laravel\Mcp\Response;




 8use Laravel\Mcp\Server\Tool;




 9 



10class CurrentWeatherTool extends Tool




11{




12    /**




13     * Handle the tool request.




14     *




15     * @return \Generator<int, \Laravel\Mcp\Response>




16     */




17    public function handle(Request $request): Generator




18    {




19        $locations = $request->array('locations');




20 



21        foreach ($locations as $index => $location) {




22            yield Response::notification('processing/progress', [




23                'current' => $index + 1,




24                'total' => count($locations),




25                'location' => $location,




26            ]);




27 



28            yield Response::text($this->forecastFor($location));




29        }




30    }




31}




<?php

namespace App\Mcp\Tools;

use Generator;
use Laravel\Mcp\Request;
use Laravel\Mcp\Response;
use Laravel\Mcp\Server\Tool;

class CurrentWeatherTool extends Tool
{
    /**
     * Handle the tool request.
     *
     * @return \Generator<int, \Laravel\Mcp\Response>
     */
    public function handle(Request $request): Generator
    {
        $locations = $request->array('locations');

        foreach ($locations as $index => $location) {
            yield Response::notification('processing/progress', [
                'current' => $index + 1,
                'total' => count($locations),
                'location' => $location,
            ]);

            yield Response::text($this->forecastFor($location));
        }
    }
}

```

When using web-based servers, streaming responses automatically open an SSE (Server-Sent Events) stream, sending each yielded message as an event to the client.
