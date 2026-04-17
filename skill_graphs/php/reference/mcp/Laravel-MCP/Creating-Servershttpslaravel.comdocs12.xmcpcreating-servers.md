## [Creating Servers](https://laravel.com/docs/12.x/mcp#creating-servers)
You can create an MCP server using the `make:mcp-server` Artisan command. Servers act as the central communication point that exposes MCP capabilities like tools, resources, and prompts to AI clients:
```


1php artisan make:mcp-server WeatherServer




php artisan make:mcp-server WeatherServer

```

This command will create a new server class in the `app/Mcp/Servers` directory. The generated server class extends Laravel MCP's base `Laravel\Mcp\Server` class and provides attributes and properties for configuring the server and registering tools, resources, and prompts:
```


 1<?php




 2 



 3namespace App\Mcp\Servers;




 4 



 5use Laravel\Mcp\Server\Attributes\Instructions;




 6use Laravel\Mcp\Server\Attributes\Name;




 7use Laravel\Mcp\Server\Attributes\Version;




 8use Laravel\Mcp\Server;




 9 



10#[Name('Weather Server')]




11#[Version('1.0.0')]




12#[Instructions('This server provides weather information and forecasts.')]




13class WeatherServer extends Server




14{




15    /**




16     * The tools registered with this MCP server.




17     *




18     * @var array<int, class-string<\Laravel\Mcp\Server\Tool>>




19     */




20    protected array $tools = [




21        // GetCurrentWeatherTool::class,




22    ];




23 



24    /**




25     * The resources registered with this MCP server.




26     *




27     * @var array<int, class-string<\Laravel\Mcp\Server\Resource>>




28     */




29    protected array $resources = [




30        // WeatherGuidelinesResource::class,




31    ];




32 



33    /**




34     * The prompts registered with this MCP server.




35     *




36     * @var array<int, class-string<\Laravel\Mcp\Server\Prompt>>




37     */




38    protected array $prompts = [




39        // DescribeWeatherPrompt::class,




40    ];




41}




<?php

namespace App\Mcp\Servers;

use Laravel\Mcp\Server\Attributes\Instructions;
use Laravel\Mcp\Server\Attributes\Name;
use Laravel\Mcp\Server\Attributes\Version;
use Laravel\Mcp\Server;

#[Name('Weather Server')]
#[Version('1.0.0')]
#[Instructions('This server provides weather information and forecasts.')]
class WeatherServer extends Server
{
    /**
     * The tools registered with this MCP server.
     *
     * @var array<int, class-string<\Laravel\Mcp\Server\Tool>>
     */
    protected array $tools = [
        // GetCurrentWeatherTool::class,
    ];

    /**
     * The resources registered with this MCP server.
     *
     * @var array<int, class-string<\Laravel\Mcp\Server\Resource>>
     */
    protected array $resources = [
        // WeatherGuidelinesResource::class,
    ];

    /**
     * The prompts registered with this MCP server.
     *
     * @var array<int, class-string<\Laravel\Mcp\Server\Prompt>>
     */
    protected array $prompts = [
        // DescribeWeatherPrompt::class,
    ];
}

```

### [Server Registration](https://laravel.com/docs/12.x/mcp#server-registration)
Once you've created a server, you must register it in your `routes/ai.php` file to make it accessible. Laravel MCP provides two methods for registering servers: `web` for HTTP-accessible servers and `local` for command-line servers.
### [Web Servers](https://laravel.com/docs/12.x/mcp#web-servers)
Web servers are the most common types of servers and are accessible via HTTP POST requests, making them ideal for remote AI clients or web-based integrations. Register a web server using the `web` method:
```


1use App\Mcp\Servers\WeatherServer;




2use Laravel\Mcp\Facades\Mcp;




3 



4Mcp::web('/mcp/weather', WeatherServer::class);




use App\Mcp\Servers\WeatherServer;
use Laravel\Mcp\Facades\Mcp;

Mcp::web('/mcp/weather', WeatherServer::class);

```

Just like normal routes, you may apply middleware to protect your web servers:
```


1Mcp::web('/mcp/weather', WeatherServer::class)




2    ->middleware(['throttle:mcp']);




Mcp::web('/mcp/weather', WeatherServer::class)
    ->middleware(['throttle:mcp']);

```

### [Local Servers](https://laravel.com/docs/12.x/mcp#local-servers)
Local servers run as Artisan commands, perfect for building local AI assistant integrations like [Laravel Boost](https://laravel.com/docs/12.x/installation#installing-laravel-boost). Register a local server using the `local` method:
```


1use App\Mcp\Servers\WeatherServer;




2use Laravel\Mcp\Facades\Mcp;




3 



4Mcp::local('weather', WeatherServer::class);




use App\Mcp\Servers\WeatherServer;
use Laravel\Mcp\Facades\Mcp;

Mcp::local('weather', WeatherServer::class);

```

Once registered, you should not typically need to manually run the `mcp:start` Artisan command yourself. Instead, configure your MCP client (AI agent) to start the server or use the [MCP Inspector](https://laravel.com/docs/12.x/mcp#mcp-inspector).
