Not sure when to use AI SDK, Boost, or MCP?[Read the breakdown](https://laravel.com/blog/laravel-ai-sdk-boost-or-mcp-which-tool-do-you-need)
Dismiss
[![Laravel](https://laravel.com/img/logotype.min.svg)](https://laravel.com/)
  * Framework
  * Products
  * Resources
  * Events
  * [Docs](https://laravel.com/docs)


Sign in
[![Laravel](https://laravel.com/img/logotype.min.svg)](https://laravel.com/)
  * Framework
  * Products
  * Resources
  * [Events](https://laravel.com/community)
  * [Docs](https://laravel.com/docs)


  * [Overview](https://laravel.com/)
  * [Starter Kits](https://laravel.com/starter-kits)
  * [Release Notes](https://laravel.com/docs/releases)
  * [Documentation](https://laravel.com/docs)
  * [Laravel Learn](https://laravel.com/learn)


  * [Laravel Cloud](https://cloud.laravel.com)
  * [Forge](https://forge.laravel.com)
  * [Nightwatch](https://nightwatch.laravel.com)
  * [Nova](https://nova.laravel.com)


  * [Blog](https://laravel.com/blog)
  * [Careers](https://laravel.com/careers)
  * [Trust](https://trust.laravel.com)
  * [Legal](https://laravel.com/legal)
  * [Status](https://status.laravel.com)


Search docs
Search`K`
`⌘K`
AI Tools
[ AI SDK  ](https://laravel.com/ai) [ Boost  ](https://laravel.com/ai/boost) [ MCP  ](https://laravel.com/ai/mcp)
#  Build powerful AI interactions with Laravel MCP
Laravel MCP provides a simple, expressive interface for creating servers, tools, and
resources that enable seamless AI interactions into your Laravel application.
$ composer require laravel/mcp
Copied
[ View documentation ](https://laravel.com/docs/12.x/mcp)
Laravel MCP By Numbers
v0.6.0
1 week ago
30
Contributors
696
GitHub Stars
2
Open PRs
### Incredibly simple
Create MCP servers with just a few lines of code. Our package handles the complexity while you focus on developing amazing AI experiences.
![Incredibly simple](https://laravel.com/images/ai/mcp/aimcp-simple-dark.webp) ![Incredibly simple](https://laravel.com/images/ai/mcp/aimcp-simple.webp)
### Built-in MCP Tools
Tools unlock your server's functionality to AI clients, enabling models to execute actions, run code, and integrate with your existing systems.
### Secure by default
Protect your MCP servers with familiar Laravel middleware patterns and built-in OAuth 2.1 and Sanctum support out of the box.
### Create smart prompts
Make reusable templates for AI clients to structure queries and interactions with your application.
### Dependency injection
Leverage Laravel's container for clean and testable code with automatic dependency resolution.
### Testing tools included
Use the included MCP Inspector and unit testing to ensure your AI works perfectly each commit.
### Real-time streaming
Automatically send intermediate updates to the client or stream progress and responses automatically to your AI clients with Laravel’s Server-Sent Events.
### Run web and local servers
Use Laravel MCP to easily remote MCP servers to pair with AI clients or create local servers that interact with agents like Claude Code.
##  Transform your Laravel
knowledge into AI solutions
Our MCP package is made for Laravel developers. If you're building applications with
Laravel, you're ready to start building AI solutions.
Servers  Tools  Prompts  Resources  Testing
```


 1<?php




 2 



 3namespace App\Mcp\Servers;




 4 



 5class Flightio extends Laravel\Mcp\Server




 6{




 7    public string $serverName = 'Flightio';




 8    public string $serverVersion = '0.0.1';




 9    public string $instructions = 'Use to help the user search, book, and manage flights.';




10 



11    public array $tools = [




12        \App\Mcp\Tools\Search::class,




13        \App\Mcp\Tools\Book::class,




14        \App\Mcp\Tools\Reschedule::class,




15        \App\Mcp\Tools\Cancel::class,




16    ];




17 



18    public array $resources = [




19        \App\Mcp\Resources\Itinerary::class,




20    ];




21 



22    public array $prompts = [




23        \App\Mcp\Prompts\Inspiration::class,




24    ];




25}




<?php

namespace App\Mcp\Servers;

class Flightio extends Laravel\Mcp\Server
{
    public string $serverName = 'Flightio';
    public string $serverVersion = '0.0.1';
    public string $instructions = 'Use to help the user search, book, and manage flights.';

    public array $tools = [
        \App\Mcp\Tools\Search::class,
        \App\Mcp\Tools\Book::class,
        \App\Mcp\Tools\Reschedule::class,
        \App\Mcp\Tools\Cancel::class,
    ];

    public array $resources = [
        \App\Mcp\Resources\Itinerary::class,
    ];

    public array $prompts = [
        \App\Mcp\Prompts\Inspiration::class,
    ];
}

```
```


1<?php




2 



3use App\Mcp\Servers\Flightio;




4use Laravel\Mcp\Facades\Mcp;




5 



6Mcp::oauthRoutes();




7 



8Mcp::web('/mcp', Flightio::class)




9    ->middleware('auth:api');




<?php

use App\Mcp\Servers\Flightio;
use Laravel\Mcp\Facades\Mcp;

Mcp::oauthRoutes();

Mcp::web('/mcp', Flightio::class)
    ->middleware('auth:api');

```

  * Flightio.php
  * routes/ai.php


```


 1<?php




 2 



 3namespace App\Mcp\Servers;




 4 



 5class Flightio extends Laravel\Mcp\Server




 6{




 7    public string $serverName = 'Flightio';




 8    public string $serverVersion = '0.0.1';




 9    public string $instructions = 'Use to help the user search, book, and manage flights.';




10 



11    public array $tools = [




12        \App\Mcp\Tools\Search::class,




13        \App\Mcp\Tools\Book::class,




14        \App\Mcp\Tools\Reschedule::class,




15        \App\Mcp\Tools\Cancel::class,




16    ];




17 



18    public array $resources = [




19        \App\Mcp\Resources\Itinerary::class,




20    ];




21 



22    public array $prompts = [




23        \App\Mcp\Prompts\Inspiration::class,




24    ];




25}




<?php

namespace App\Mcp\Servers;

class Flightio extends Laravel\Mcp\Server
{
    public string $serverName = 'Flightio';
    public string $serverVersion = '0.0.1';
    public string $instructions = 'Use to help the user search, book, and manage flights.';

    public array $tools = [
        \App\Mcp\Tools\Search::class,
        \App\Mcp\Tools\Book::class,
        \App\Mcp\Tools\Reschedule::class,
        \App\Mcp\Tools\Cancel::class,
    ];

    public array $resources = [
        \App\Mcp\Resources\Itinerary::class,
    ];

    public array $prompts = [
        \App\Mcp\Prompts\Inspiration::class,
    ];
}

```
```


1<?php




2 



3use App\Mcp\Servers\Flightio;




4use Laravel\Mcp\Facades\Mcp;




5 



6Mcp::oauthRoutes();




7 



8Mcp::web('/mcp', Flightio::class)




9    ->middleware('auth:api');




<?php

use App\Mcp\Servers\Flightio;
use Laravel\Mcp\Facades\Mcp;

Mcp::oauthRoutes();

Mcp::web('/mcp', Flightio::class)
    ->middleware('auth:api');

```

```


 1<?php




 2 



 3namespace App\Mcp\Tools;




 4 



 5use App\Actions\BookFlightForUser;




 6use Illuminate\JsonSchema\JsonSchema;




 7use Laravel\Mcp\Request;




 8use Laravel\Mcp\Response;




 9use Laravel\Mcp\Server\Tool;




10 



11class Book extends Tool




12{




13    protected string $description = 'Book flights for the user. Must be called with both departure and return flight details.';




14 



15    public function __construct(private BookFlightForUser $book) {}




16 



17    public function schema(JsonSchema $schema): array




18    {




19        return [




20            'departure' => $schema->array()




21                ->description('The deparature information')




22                ->required(),




23 



24            'return' => $schema->array()




25                ->description('The return information')




26                ->required(),




27        ];




28    }




29 



30    public function handle(Request $request): Response




31    {




32        if (! $request->user()) {




33            return Response::error('User must authenticate to book a flight.');




34        }




35 



36        $validated = $request->validate([




37            'departure.flight_code' => 'required|string|min:1',




38            'return.flight_code' => 'required|string|min:1',




39        ]);




40 



41        $booking = $this->book




42            ->forUser($request->user())




43            ->withDeparture($validated['departure'])




44            ->withReturn($validated['return']);




45 



46        return $booking->successful()




47            ? Response::text('Flight booked! Share all of these details with the user: '.$booking->itinerary())




48            : Response::error('Failed to book the flight. Work with the user to correct any errors and retry. Error details: '.$booking->error());




49    }




50}




<?php

namespace App\Mcp\Tools;

use App\Actions\BookFlightForUser;
use Illuminate\JsonSchema\JsonSchema;
use Laravel\Mcp\Request;
use Laravel\Mcp\Response;
use Laravel\Mcp\Server\Tool;

class Book extends Tool
{
    protected string $description = 'Book flights for the user. Must be called with both departure and return flight details.';

    public function __construct(private BookFlightForUser $book) {}

    public function schema(JsonSchema $schema): array
    {
        return [
            'departure' => $schema->array()
                ->description('The deparature information')
                ->required(),

            'return' => $schema->array()
                ->description('The return information')
                ->required(),
        ];
    }

    public function handle(Request $request): Response
    {
        if (! $request->user()) {
            return Response::error('User must authenticate to book a flight.');
        }

        $validated = $request->validate([
            'departure.flight_code' => 'required|string|min:1',
            'return.flight_code' => 'required|string|min:1',
        ]);

        $booking = $this->book
            ->forUser($request->user())
            ->withDeparture($validated['departure'])
            ->withReturn($validated['return']);

        return $booking->successful()
            ? Response::text('Flight booked! Share all of these details with the user: '.$booking->itinerary())
            : Response::error('Failed to book the flight. Work with the user to correct any errors and retry. Error details: '.$booking->error());
    }
}

```
```


 1<?php




 2 



 3namespace App\Mcp\Tools;




 4 



 5use App\Actions\SearchFlights;




 6use Illuminate\JsonSchema\JsonSchema;




 7use Laravel\Mcp\Request;




 8use Laravel\Mcp\Response;




 9use Laravel\Mcp\Server\Tool;




10 



11class Search extends Tool




12{




13    protected string $description = 'Search for available flights for the user between two dates.';




14 



15    public function schema(JsonSchema $schema): array




16    {




17        return [




18            'query' => $schema->string()




19                ->description('The query to search for flights')




20                ->required(),




21            'from' => $schema->string()




22                ->description('ISO 8601 formatted date string for the search start date')




23                ->required(),




24            'to' => $schema->string()




25                ->description('ISO 8601 formatted date string for the search end date')




26                ->required(),




27        ];




28    }




29 



30    public function handle(Request $request, SearchFlights $search): Response




31    {




32        // Validate will return an error if any input values are invalid




33        $validated = $request->validate([




34            'query' => 'required|string|min:1',




35            'from' => 'required|datetime',




36            'to' => 'required|datetime',




37        ]);




38 



39        $details = $this->search




40            ->query($validated['query'])




41            ->from($validated['from'])




42            ->to($validated['to']);




43 



44        if ($details->unsuccessful()) {




45            return Response::error('Failed to search for flights. Work with the user to correct any errors and retry. Error details: '.$details->error());




46        }




47 



48        return Response::text('All done! Share ALL of these details with the user: '.$details->results());




49    }




50}




<?php

namespace App\Mcp\Tools;

use App\Actions\SearchFlights;
use Illuminate\JsonSchema\JsonSchema;
use Laravel\Mcp\Request;
use Laravel\Mcp\Response;
use Laravel\Mcp\Server\Tool;

class Search extends Tool
{
    protected string $description = 'Search for available flights for the user between two dates.';

    public function schema(JsonSchema $schema): array
    {
        return [
            'query' => $schema->string()
                ->description('The query to search for flights')
                ->required(),
            'from' => $schema->string()
                ->description('ISO 8601 formatted date string for the search start date')
                ->required(),
            'to' => $schema->string()
                ->description('ISO 8601 formatted date string for the search end date')
                ->required(),
        ];
    }

    public function handle(Request $request, SearchFlights $search): Response
    {
        // Validate will return an error if any input values are invalid
        $validated = $request->validate([
            'query' => 'required|string|min:1',
            'from' => 'required|datetime',
            'to' => 'required|datetime',
        ]);

        $details = $this->search
            ->query($validated['query'])
            ->from($validated['from'])
            ->to($validated['to']);

        if ($details->unsuccessful()) {
            return Response::error('Failed to search for flights. Work with the user to correct any errors and retry. Error details: '.$details->error());
        }

        return Response::text('All done! Share ALL of these details with the user: '.$details->results());
    }
}

```

```


 1<?php




 2 



 3namespace App\Mcp\Prompts;




 4 



 5use Laravel\Mcp\Request;




 6use Laravel\Mcp\Response;




 7use Laravel\Mcp\Server\Prompt;




 8 



 9class Inspiration extends Prompt




10{




11    protected string $description = 'Help the user find inspiration for trips they could take.';




12 



13    public function handle(Request $request): Response




14    {




15        return Response::text(<<<'PROMPT'




16            Help me find places to visit, things to do, countries to explore.




17 



18            Inspire me!




19 



20            Ask me a few quick questions to narrow things down, then suggest 2-3 compelling options with brief explanations of why each might resonate.




21 



22            Start by asking about:




23            - Timeframe (weekend, week, longer?)




24            - Starting point/region




25            - Travel style (adventure, relaxation, culture, food, etc.)




26            - Any deal-breakers (budget limits, must-haves, can't-dos)




27 



28            Keep the back-and-forth tight - aim for 2-3 exchanges max before giving suggestions. For each trip idea, include: destination, rough cost estimate, what makes it special, and one practical tip.




29        PROMPT);




30    }




31}




<?php

namespace App\Mcp\Prompts;

use Laravel\Mcp\Request;
use Laravel\Mcp\Response;
use Laravel\Mcp\Server\Prompt;

class Inspiration extends Prompt
{
    protected string $description = 'Help the user find inspiration for trips they could take.';

    public function handle(Request $request): Response
    {
        return Response::text(<<<'PROMPT'
            Help me find places to visit, things to do, countries to explore.

            Inspire me!

            Ask me a few quick questions to narrow things down, then suggest 2-3 compelling options with brief explanations of why each might resonate.

            Start by asking about:
            - Timeframe (weekend, week, longer?)
            - Starting point/region
            - Travel style (adventure, relaxation, culture, food, etc.)
            - Any deal-breakers (budget limits, must-haves, can't-dos)

            Keep the back-and-forth tight - aim for 2-3 exchanges max before giving suggestions. For each trip idea, include: destination, rough cost estimate, what makes it special, and one practical tip.
        PROMPT);
    }
}

```

```


 1<?php




 2 



 3namespace App\Mcp\Resources;




 4 



 5use App\Actions\BuildItinerary;




 6use Laravel\Mcp\Request;




 7use Laravel\Mcp\Server\Resource;




 8 



 9class Itinerary extends Resource




10{




11    protected string $description = "The user's upcoming flights & trips.";




12 



13    public function handle(Request $request, BuildItinerary $buildItinerary): string




14    {




15        $user = $request->user();




16 



17        if (! $request->user()) {




18            return Response::error('User must login to view their itinerary.');




19        }




20 



21        $itinerary = $buildItinerary->for($user);




22 



23        if (! $itinerary) {




24            return Response::error('No flights found for this user. Maybe it is time they book a trip?');




25        }




26 



27        $output = '<trips>';




28 



29        foreach ($itinerary as $trip) {




30            $output .= <<<TRIP




31            <trip from="{$trip->leavingAt()}" to="{$trip->returningAt()}" name="{$trip->friendlyName}">




32                <departing




33                    from="{$trip->departure()->from()->airportCode}"




34                    to="{$trip->departure()->to()->airportCode}




35                >




36                    Baggage: {$trip->departure()->baggage()->allowanceText}




37                    Details: {$trip->departure()->details}




38                </departing>




39 



40                <returning




41                    from="{$trip->return()->from()->airportCode}"




42                    to="{$trip->return()->to()->airportCode}




43                >




44                    Baggage: {$trip->return()->baggage()->allowanceText}




45                    Details: {$trip->return()->details}




46                </returning>




47 



48                <costs>




49                    <out>{$trip->costs()->out}</out>




50                    <in>{$trip->costs()->in}</in>




51                    <total>{$trip->costs()->total}</total>




52                </costs>




53 



54                <notes>{$trip->usersNotes()}</notes>




55            </trip>




56            TRIP;




57        }




58 



59        $output .= '</trips>';




60 



61        return $output;




62    }




63}




<?php

namespace App\Mcp\Resources;

use App\Actions\BuildItinerary;
use Laravel\Mcp\Request;
use Laravel\Mcp\Server\Resource;

class Itinerary extends Resource
{
    protected string $description = "The user's upcoming flights & trips.";

    public function handle(Request $request, BuildItinerary $buildItinerary): string
    {
        $user = $request->user();

        if (! $request->user()) {
            return Response::error('User must login to view their itinerary.');
        }

        $itinerary = $buildItinerary->for($user);

        if (! $itinerary) {
            return Response::error('No flights found for this user. Maybe it is time they book a trip?');
        }

        $output = '<trips>';

        foreach ($itinerary as $trip) {
            $output .= <<<TRIP
            <trip from="{$trip->leavingAt()}" to="{$trip->returningAt()}" name="{$trip->friendlyName}">
                <departing
                    from="{$trip->departure()->from()->airportCode}"
                    to="{$trip->departure()->to()->airportCode}
                >
                    Baggage: {$trip->departure()->baggage()->allowanceText}
                    Details: {$trip->departure()->details}
                </departing>

                <returning
                    from="{$trip->return()->from()->airportCode}"
                    to="{$trip->return()->to()->airportCode}
                >
                    Baggage: {$trip->return()->baggage()->allowanceText}
                    Details: {$trip->return()->details}
                </returning>

                <costs>
                    <out>{$trip->costs()->out}</out>
                    <in>{$trip->costs()->in}</in>
                    <total>{$trip->costs()->total}</total>
                </costs>

                <notes>{$trip->usersNotes()}</notes>
            </trip>
            TRIP;
        }

        $output .= '</trips>';

        return $output;
    }
}

```

```


 1<?php




 2 



 3test('can book flight with valid details', function () {




 4    $response = Flightio::tool(Book::class, [




 5        'departure' => [




 6            'flight_code' => 'ABC123',




 7            'date' => '2025-10-23 10:10:10',




 8        ],




 9        'return' => [




10            'flight_code' => 'XYZ987',




11            'date' => '2025-11-04 11:11:11',




12        ],




13    ]);




14 



15    $response




16        ->assertOk()




17        ->assertSee('Flight booked successfully.');




18});




19 



20test('cannot book with invalid details', function () {




21    $response = Flightio::tool(Book::class, [




22        'departure' => [




23            'flight_code' => 'ZZZ455',




24            'date' => '2025-10-23 10:10:10',




25        ],




26        'return' => [




27            'flight_code' => 'OMG67',




28            'date' => '2025-11-04 11:11:11',




29        ],




30    ]);




31 



32    $response->assertHasErrors(['Flight codes ZZZ455 and OMG67 are invalid for these dates.']);




33});




<?php

test('can book flight with valid details', function () {
    $response = Flightio::tool(Book::class, [
        'departure' => [
            'flight_code' => 'ABC123',
            'date' => '2025-10-23 10:10:10',
        ],
        'return' => [
            'flight_code' => 'XYZ987',
            'date' => '2025-11-04 11:11:11',
        ],
    ]);

    $response
        ->assertOk()
        ->assertSee('Flight booked successfully.');
});

test('cannot book with invalid details', function () {
    $response = Flightio::tool(Book::class, [
        'departure' => [
            'flight_code' => 'ZZZ455',
            'date' => '2025-10-23 10:10:10',
        ],
        'return' => [
            'flight_code' => 'OMG67',
            'date' => '2025-11-04 11:11:11',
        ],
    ]);

    $response->assertHasErrors(['Flight codes ZZZ455 and OMG67 are invalid for these dates.']);
});

```

##  Learn about Laravel MCP directly
from the development team
Dive deeper into Laravel MCP with Ashley Hindle, Nuno Maduro and Josh Cirre. You'll
gain first hand experience and lessons direcly for the Laravel Team.
[ View documentation ](https://laravel.com/docs/12.x/mcp)
##  Start building your AI
experiences in Laravel MCP
Getting started is incredibly easy. View our documentation for more information, or
join us on GitHub and help contribute to the future of AI in Laravel.
[ View documentation ](https://laravel.com/docs/12.x/mcp)
$ composer require laravel/mcp
Copied
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
  * [Active Logic](https://partners.laravel.com/partners/active-logic)
  * [Kirschbaum](https://partners.laravel.com/partners/kirschbaum)
  * [Jump24](https://partners.laravel.com/partners/jump24)
  * [Curotec](https://partners.laravel.com/partners/curotec)
  * [byte5](https://partners.laravel.com/partners/byte5)
  * [Tighten](https://partners.laravel.com/partners/tighten)
  * [ More Partners ](https://partners.laravel.com)
