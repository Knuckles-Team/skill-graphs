## [Prompts](https://laravel.com/docs/12.x/mcp#prompts)
### [Creating Prompts](https://laravel.com/docs/12.x/mcp#creating-prompts)
To create a prompt, run the `make:mcp-prompt` Artisan command:
```


1php artisan make:mcp-prompt DescribeWeatherPrompt




php artisan make:mcp-prompt DescribeWeatherPrompt

```

After creating a prompt, register it in your server's `$prompts` property:
```


 1<?php




 2 



 3namespace App\Mcp\Servers;




 4 



 5use App\Mcp\Prompts\DescribeWeatherPrompt;




 6use Laravel\Mcp\Server;




 7 



 8class WeatherServer extends Server




 9{




10    /**




11     * The prompts registered with this MCP server.




12     *




13     * @var array<int, class-string<\Laravel\Mcp\Server\Prompt>>




14     */




15    protected array $prompts = [




16        DescribeWeatherPrompt::class,




17    ];




18}




<?php

namespace App\Mcp\Servers;

use App\Mcp\Prompts\DescribeWeatherPrompt;
use Laravel\Mcp\Server;

class WeatherServer extends Server
{
    /**
     * The prompts registered with this MCP server.
     *
     * @var array<int, class-string<\Laravel\Mcp\Server\Prompt>>
     */
    protected array $prompts = [
        DescribeWeatherPrompt::class,
    ];
}

```

#### [Prompt Name, Title, and Description](https://laravel.com/docs/12.x/mcp#prompt-name-title-and-description)
By default, the prompt's name and title are derived from the class name. For example, `DescribeWeatherPrompt` will have a name of `describe-weather` and a title of `Describe Weather Prompt`. You may customize these values using the `Name` and `Title` attributes:
```


1use Laravel\Mcp\Server\Attributes\Name;




2use Laravel\Mcp\Server\Attributes\Title;




3 



4#[Name('weather-assistant')]




5#[Title('Weather Assistant Prompt')]




6class DescribeWeatherPrompt extends Prompt




7{




8    // ...




9}




use Laravel\Mcp\Server\Attributes\Name;
use Laravel\Mcp\Server\Attributes\Title;

#[Name('weather-assistant')]
#[Title('Weather Assistant Prompt')]
class DescribeWeatherPrompt extends Prompt
{
    // ...
}

```

Prompt descriptions are not automatically generated. You should always provide a meaningful description using the `Description` attribute:
```


1use Laravel\Mcp\Server\Attributes\Description;




2 



3#[Description('Generates a natural-language explanation of the weather for a given location.')]




4class DescribeWeatherPrompt extends Prompt




5{




6    //




7}




use Laravel\Mcp\Server\Attributes\Description;

#[Description('Generates a natural-language explanation of the weather for a given location.')]
class DescribeWeatherPrompt extends Prompt
{
    //
}

```

The description is a critical part of the prompt's metadata, as it helps AI models understand when and how to get the best use out of the prompt.
### [Prompt Arguments](https://laravel.com/docs/12.x/mcp#prompt-arguments)
Prompts can define arguments that allow AI clients to customize the prompt template with specific values. Use the `arguments` method to define what arguments your prompt accepts:
```


 1<?php




 2 



 3namespace App\Mcp\Prompts;




 4 



 5use Laravel\Mcp\Server\Prompt;




 6use Laravel\Mcp\Server\Prompts\Argument;




 7 



 8class DescribeWeatherPrompt extends Prompt




 9{




10    /**




11     * Get the prompt's arguments.




12     *




13     * @return array<int, \Laravel\Mcp\Server\Prompts\Argument>




14     */




15    public function arguments(): array




16    {




17        return [




18            new Argument(




19                name: 'tone',




20                description: 'The tone to use in the weather description (e.g., formal, casual, humorous).',




21                required: true,




22            ),




23        ];




24    }




25}




<?php

namespace App\Mcp\Prompts;

use Laravel\Mcp\Server\Prompt;
use Laravel\Mcp\Server\Prompts\Argument;

class DescribeWeatherPrompt extends Prompt
{
    /**
     * Get the prompt's arguments.
     *
     * @return array<int, \Laravel\Mcp\Server\Prompts\Argument>
     */
    public function arguments(): array
    {
        return [
            new Argument(
                name: 'tone',
                description: 'The tone to use in the weather description (e.g., formal, casual, humorous).',
                required: true,
            ),
        ];
    }
}

```

### [Validating Prompt Arguments](https://laravel.com/docs/12.x/mcp#validating-prompt-arguments)
Prompt arguments are automatically validated based on their definition, but you may also want to enforce more complex validation rules.
Laravel MCP integrates seamlessly with Laravel's [validation features](https://laravel.com/docs/12.x/validation). You may validate incoming prompt arguments within your prompt's `handle` method:
```


 1<?php




 2 



 3namespace App\Mcp\Prompts;




 4 



 5use Laravel\Mcp\Request;




 6use Laravel\Mcp\Response;




 7use Laravel\Mcp\Server\Prompt;




 8 



 9class DescribeWeatherPrompt extends Prompt




10{




11    /**




12     * Handle the prompt request.




13     */




14    public function handle(Request $request): Response




15    {




16        $validated = $request->validate([




17            'tone' => 'required|string|max:50',




18        ]);




19 



20        $tone = $validated['tone'];




21 



22        // Generate the prompt response using the given tone...




23    }




24}




<?php

namespace App\Mcp\Prompts;

use Laravel\Mcp\Request;
use Laravel\Mcp\Response;
use Laravel\Mcp\Server\Prompt;

class DescribeWeatherPrompt extends Prompt
{
    /**
     * Handle the prompt request.
     */
    public function handle(Request $request): Response
    {
        $validated = $request->validate([
            'tone' => 'required|string|max:50',
        ]);

        $tone = $validated['tone'];

        // Generate the prompt response using the given tone...
    }
}

```

On validation failure, AI clients will act based on the error messages you provide. As such, it is critical to provide clear and actionable error messages:
```


1$validated = $request->validate([




2    'tone' => ['required','string','max:50'],




3],[




4    'tone.*' => 'You must specify a tone for the weather description. Examples include "formal", "casual", or "humorous".',




5]);




$validated = $request->validate([
    'tone' => ['required','string','max:50'],
],[
    'tone.*' => 'You must specify a tone for the weather description. Examples include "formal", "casual", or "humorous".',
]);

```

### [Prompt Dependency Injection](https://laravel.com/docs/12.x/mcp#prompt-dependency-injection)
The Laravel [service container](https://laravel.com/docs/12.x/container) is used to resolve all prompts. As a result, you are able to type-hint any dependencies your prompt may need in its constructor. The declared dependencies will automatically be resolved and injected into the prompt instance:
```


 1<?php




 2 



 3namespace App\Mcp\Prompts;




 4 



 5use App\Repositories\WeatherRepository;




 6use Laravel\Mcp\Server\Prompt;




 7 



 8class DescribeWeatherPrompt extends Prompt




 9{




10    /**




11     * Create a new prompt instance.




12     */




13    public function __construct(




14        protected WeatherRepository $weather,




15    ) {}




16 



17    //




18}




<?php

namespace App\Mcp\Prompts;

use App\Repositories\WeatherRepository;
use Laravel\Mcp\Server\Prompt;

class DescribeWeatherPrompt extends Prompt
{
    /**
     * Create a new prompt instance.
     */
    public function __construct(
        protected WeatherRepository $weather,
    ) {}

    //
}

```

In addition to constructor injection, you may also type-hint dependencies in your prompt's `handle` method. The service container will automatically resolve and inject the dependencies when the method is called:
```


 1<?php




 2 



 3namespace App\Mcp\Prompts;




 4 



 5use App\Repositories\WeatherRepository;




 6use Laravel\Mcp\Request;




 7use Laravel\Mcp\Response;




 8use Laravel\Mcp\Server\Prompt;




 9 



10class DescribeWeatherPrompt extends Prompt




11{




12    /**




13     * Handle the prompt request.




14     */




15    public function handle(Request $request, WeatherRepository $weather): Response




16    {




17        $isAvailable = $weather->isServiceAvailable();




18 



19        // ...




20    }




21}




<?php

namespace App\Mcp\Prompts;

use App\Repositories\WeatherRepository;
use Laravel\Mcp\Request;
use Laravel\Mcp\Response;
use Laravel\Mcp\Server\Prompt;

class DescribeWeatherPrompt extends Prompt
{
    /**
     * Handle the prompt request.
     */
    public function handle(Request $request, WeatherRepository $weather): Response
    {
        $isAvailable = $weather->isServiceAvailable();

        // ...
    }
}

```

### [Conditional Prompt Registration](https://laravel.com/docs/12.x/mcp#conditional-prompt-registration)
You may conditionally register prompts at runtime by implementing the `shouldRegister` method in your prompt class. This method allows you to determine whether a prompt should be available based on application state, configuration, or request parameters:
```


 1<?php




 2 



 3namespace App\Mcp\Prompts;




 4 



 5use Laravel\Mcp\Request;




 6use Laravel\Mcp\Server\Prompt;




 7 



 8class CurrentWeatherPrompt extends Prompt




 9{




10    /**




11     * Determine if the prompt should be registered.




12     */




13    public function shouldRegister(Request $request): bool




14    {




15        return $request?->user()?->subscribed() ?? false;




16    }




17}




<?php

namespace App\Mcp\Prompts;

use Laravel\Mcp\Request;
use Laravel\Mcp\Server\Prompt;

class CurrentWeatherPrompt extends Prompt
{
    /**
     * Determine if the prompt should be registered.
     */
    public function shouldRegister(Request $request): bool
    {
        return $request?->user()?->subscribed() ?? false;
    }
}

```

When a prompt's `shouldRegister` method returns `false`, it will not appear in the list of available prompts and cannot be invoked by AI clients.
### [Prompt Responses](https://laravel.com/docs/12.x/mcp#prompt-responses)
Prompts may return a single `Laravel\Mcp\Response` or an iterable of `Laravel\Mcp\Response` instances. These responses encapsulate the content that will be sent to the AI client:
```


 1<?php




 2 



 3namespace App\Mcp\Prompts;




 4 



 5use Laravel\Mcp\Request;




 6use Laravel\Mcp\Response;




 7use Laravel\Mcp\Server\Prompt;




 8 



 9class DescribeWeatherPrompt extends Prompt




10{




11    /**




12     * Handle the prompt request.




13     *




14     * @return array<int, \Laravel\Mcp\Response>




15     */




16    public function handle(Request $request): array




17    {




18        $tone = $request->string('tone');




19 



20        $systemMessage = "You are a helpful weather assistant. Please provide a weather description in a {$tone} tone.";




21 



22        $userMessage = "What is the current weather like in New York City?";




23 



24        return [




25            Response::text($systemMessage)->asAssistant(),




26            Response::text($userMessage),




27        ];




28    }




29}




<?php

namespace App\Mcp\Prompts;

use Laravel\Mcp\Request;
use Laravel\Mcp\Response;
use Laravel\Mcp\Server\Prompt;

class DescribeWeatherPrompt extends Prompt
{
    /**
     * Handle the prompt request.
     *
     * @return array<int, \Laravel\Mcp\Response>
     */
    public function handle(Request $request): array
    {
        $tone = $request->string('tone');

        $systemMessage = "You are a helpful weather assistant. Please provide a weather description in a {$tone} tone.";

        $userMessage = "What is the current weather like in New York City?";

        return [
            Response::text($systemMessage)->asAssistant(),
            Response::text($userMessage),
        ];
    }
}

```

You can use the `asAssistant()` method to indicate that a response message should be treated as coming from the AI assistant, while regular messages are treated as user input.
