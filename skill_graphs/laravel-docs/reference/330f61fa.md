## [Agents](https://laravel.com/docs/12.x/ai-sdk#agents)
Agents are the fundamental building block for interacting with AI providers in the Laravel AI SDK. Each agent is a dedicated PHP class that encapsulates the instructions, conversation context, tools, and output schema needed to interact with a large language model. Think of an agent as a specialized assistant — a sales coach, a document analyzer, a support bot — that you configure once and prompt as needed throughout your application.
You can create an agent via the `make:agent` Artisan command:
```


1php artisan make:agent SalesCoach




2 



3php artisan make:agent SalesCoach --structured




php artisan make:agent SalesCoach

php artisan make:agent SalesCoach --structured

```

Within the generated agent class, you can define the system prompt / instructions, message context, available tools, and output schema (if applicable):
```


 1<?php




 2 



 3namespace App\Ai\Agents;




 4 



 5use App\Ai\Tools\RetrievePreviousTranscripts;




 6use App\Models\History;




 7use App\Models\User;




 8use Illuminate\Contracts\JsonSchema\JsonSchema;




 9use Laravel\Ai\Contracts\Agent;




10use Laravel\Ai\Contracts\Conversational;




11use Laravel\Ai\Contracts\HasStructuredOutput;




12use Laravel\Ai\Contracts\HasTools;




13use Laravel\Ai\Messages\Message;




14use Laravel\Ai\Promptable;




15use Stringable;




16 



17class SalesCoach implements Agent, Conversational, HasTools, HasStructuredOutput




18{




19    use Promptable;




20 



21    public function __construct(public User $user) {}




22 



23    /**




24     * Get the instructions that the agent should follow.




25     */




26    public function instructions(): Stringable|string




27    {




28        return 'You are a sales coach, analyzing transcripts and providing feedback and an overall sales strength score.';




29    }




30 



31    /**




32     * Get the list of messages comprising the conversation so far.




33     */




34    public function messages(): iterable




35    {




36        return History::where('user_id', $this->user->id)




37            ->latest()




38            ->limit(50)




39            ->get()




40            ->reverse()




41            ->map(function ($message) {




42                return new Message($message->role, $message->content);




43            })->all();




44    }




45 



46    /**




47     * Get the tools available to the agent.




48     *




49     * @return Tool[]




50     */




51    public function tools(): iterable




52    {




53        return [




54            new RetrievePreviousTranscripts,




55        ];




56    }




57 



58    /**




59     * Get the agent's structured output schema definition.




60     */




61    public function schema(JsonSchema $schema): array




62    {




63        return [




64            'feedback' => $schema->string()->required(),




65            'score' => $schema->integer()->min(1)->max(10)->required(),




66        ];




67    }




68}




<?php

namespace App\Ai\Agents;

use App\Ai\Tools\RetrievePreviousTranscripts;
use App\Models\History;
use App\Models\User;
use Illuminate\Contracts\JsonSchema\JsonSchema;
use Laravel\Ai\Contracts\Agent;
use Laravel\Ai\Contracts\Conversational;
use Laravel\Ai\Contracts\HasStructuredOutput;
use Laravel\Ai\Contracts\HasTools;
use Laravel\Ai\Messages\Message;
use Laravel\Ai\Promptable;
use Stringable;

class SalesCoach implements Agent, Conversational, HasTools, HasStructuredOutput
{
    use Promptable;

    public function __construct(public User $user) {}

    /**
     * Get the instructions that the agent should follow.
     */
    public function instructions(): Stringable|string
    {
        return 'You are a sales coach, analyzing transcripts and providing feedback and an overall sales strength score.';
    }

    /**
     * Get the list of messages comprising the conversation so far.
     */
    public function messages(): iterable
    {
        return History::where('user_id', $this->user->id)
            ->latest()
            ->limit(50)
            ->get()
            ->reverse()
            ->map(function ($message) {
                return new Message($message->role, $message->content);
            })->all();
    }

    /**
     * Get the tools available to the agent.
     *
     * @return Tool[]
     */
    public function tools(): iterable
    {
        return [
            new RetrievePreviousTranscripts,
        ];
    }

    /**
     * Get the agent's structured output schema definition.
     */
    public function schema(JsonSchema $schema): array
    {
        return [
            'feedback' => $schema->string()->required(),
            'score' => $schema->integer()->min(1)->max(10)->required(),
        ];
    }
}

```

### [Prompting](https://laravel.com/docs/12.x/ai-sdk#prompting)
To prompt an agent, first create an instance using the `make` method or standard instantiation, then call `prompt`:
```


1$response = (new SalesCoach)




2    ->prompt('Analyze this sales transcript...');




3 



4$response = SalesCoach::make()




5    ->prompt('Analyze this sales transcript...');




6 



7return (string) $response;




$response = (new SalesCoach)
    ->prompt('Analyze this sales transcript...');

$response = SalesCoach::make()
    ->prompt('Analyze this sales transcript...');

return (string) $response;

```

The `make` method resolves your agent from the container, allowing automatic dependency injection. You may also pass arguments to the agent's constructor:
```


1$agent = SalesCoach::make(user: $user);




$agent = SalesCoach::make(user: $user);

```

By passing additional arguments to the `prompt` method, you may override the default provider, model, or HTTP timeout when prompting:
```


1$response = (new SalesCoach)->prompt(




2    'Analyze this sales transcript...',




3    provider: Lab::Anthropic,




4    model: 'claude-haiku-4-5-20251001',




5    timeout: 120,




6);




$response = (new SalesCoach)->prompt(
    'Analyze this sales transcript...',
    provider: Lab::Anthropic,
    model: 'claude-haiku-4-5-20251001',
    timeout: 120,
);

```

### [Conversation Context](https://laravel.com/docs/12.x/ai-sdk#conversation-context)
If your agent implements the `Conversational` interface, you may use the `messages` method to return the previous conversation context, if applicable:
```


 1use App\Models\History;




 2use Laravel\Ai\Messages\Message;




 3 



 4/**




 5 * Get the list of messages comprising the conversation so far.




 6 */




 7public function messages(): iterable




 8{




 9    return History::where('user_id', $this->user->id)




10        ->latest()




11        ->limit(50)




12        ->get()




13        ->reverse()




14        ->map(function ($message) {




15            return new Message($message->role, $message->content);




16        })->all();




17}




use App\Models\History;
use Laravel\Ai\Messages\Message;

/**
 * Get the list of messages comprising the conversation so far.
 */
public function messages(): iterable
{
    return History::where('user_id', $this->user->id)
        ->latest()
        ->limit(50)
        ->get()
        ->reverse()
        ->map(function ($message) {
            return new Message($message->role, $message->content);
        })->all();
}

```

#### [Remembering Conversations](https://laravel.com/docs/12.x/ai-sdk#remembering-conversations)
Before using the `RemembersConversations` trait, you should publish and run the AI SDK migrations using the `vendor:publish` Artisan command. These migrations will create the necessary database tables to store conversations.
If you would like Laravel to automatically store and retrieve conversation history for your agent, you may use the `RemembersConversations` trait. This trait provides a simple way to persist conversation messages to the database without manually implementing the `Conversational` interface:
```


 1<?php




 2 



 3namespace App\Ai\Agents;




 4 



 5use Laravel\Ai\Concerns\RemembersConversations;




 6use Laravel\Ai\Contracts\Agent;




 7use Laravel\Ai\Contracts\Conversational;




 8use Laravel\Ai\Promptable;




 9 



10class SalesCoach implements Agent, Conversational




11{




12    use Promptable, RemembersConversations;




13 



14    /**




15     * Get the instructions that the agent should follow.




16     */




17    public function instructions(): string




18    {




19        return 'You are a sales coach...';




20    }




21}




<?php

namespace App\Ai\Agents;

use Laravel\Ai\Concerns\RemembersConversations;
use Laravel\Ai\Contracts\Agent;
use Laravel\Ai\Contracts\Conversational;
use Laravel\Ai\Promptable;

class SalesCoach implements Agent, Conversational
{
    use Promptable, RemembersConversations;

    /**
     * Get the instructions that the agent should follow.
     */
    public function instructions(): string
    {
        return 'You are a sales coach...';
    }
}

```

To start a new conversation for a user, call the `forUser` method before prompting:
```


1$response = (new SalesCoach)->forUser($user)->prompt('Hello!');




2 



3$conversationId = $response->conversationId;




$response = (new SalesCoach)->forUser($user)->prompt('Hello!');

$conversationId = $response->conversationId;

```

The conversation ID is returned on the response and can be stored for future reference, or you can retrieve all of a user's conversations from the `agent_conversations` table directly.
To continue an existing conversation, use the `continue` method:
```


1$response = (new SalesCoach)




2    ->continue($conversationId, as: $user)




3    ->prompt('Tell me more about that.');




$response = (new SalesCoach)
    ->continue($conversationId, as: $user)
    ->prompt('Tell me more about that.');

```

When using the `RemembersConversations` trait, previous messages are automatically loaded and included in the conversation context when prompting. New messages (both user and assistant) are automatically stored after each interaction.
### [Structured Output](https://laravel.com/docs/12.x/ai-sdk#structured-output)
If you would like your agent to return structured output, implement the `HasStructuredOutput` interface, which requires that your agent define a `schema` method:
```


 1<?php




 2 



 3namespace App\Ai\Agents;




 4 



 5use Illuminate\Contracts\JsonSchema\JsonSchema;




 6use Laravel\Ai\Contracts\Agent;




 7use Laravel\Ai\Contracts\HasStructuredOutput;




 8use Laravel\Ai\Promptable;




 9 



10class SalesCoach implements Agent, HasStructuredOutput




11{




12    use Promptable;




13 



14    // ...




15 



16    /**




17     * Get the agent's structured output schema definition.




18     */




19    public function schema(JsonSchema $schema): array




20    {




21        return [




22            'score' => $schema->integer()->required(),




23        ];




24    }




25}




<?php

namespace App\Ai\Agents;

use Illuminate\Contracts\JsonSchema\JsonSchema;
use Laravel\Ai\Contracts\Agent;
use Laravel\Ai\Contracts\HasStructuredOutput;
use Laravel\Ai\Promptable;

class SalesCoach implements Agent, HasStructuredOutput
{
    use Promptable;

    // ...

    /**
     * Get the agent's structured output schema definition.
     */
    public function schema(JsonSchema $schema): array
    {
        return [
            'score' => $schema->integer()->required(),
        ];
    }
}

```

When prompting an agent that returns structured output, you can access the returned `StructuredAgentResponse` like an array:
```


1$response = (new SalesCoach)->prompt('Analyze this sales transcript...');




2 



3return $response['score'];




$response = (new SalesCoach)->prompt('Analyze this sales transcript...');

return $response['score'];

```

### [Attachments](https://laravel.com/docs/12.x/ai-sdk#attachments)
When prompting, you may also pass attachments with the prompt to allow the model to inspect images and documents:
```


 1use App\Ai\Agents\SalesCoach;




 2use Laravel\Ai\Files;




 3 



 4$response = (new SalesCoach)->prompt(




 5    'Analyze the attached sales transcript...',




 6    attachments: [




 7        Files\Document::fromStorage('transcript.pdf') // Attach a document from a filesystem disk...




 8        Files\Document::fromPath('/home/laravel/transcript.md') // Attach a document from a local path...




 9        $request->file('transcript'), // Attach an uploaded file...




10    ]




11);




use App\Ai\Agents\SalesCoach;
use Laravel\Ai\Files;

$response = (new SalesCoach)->prompt(
    'Analyze the attached sales transcript...',
    attachments: [
        Files\Document::fromStorage('transcript.pdf') // Attach a document from a filesystem disk...
        Files\Document::fromPath('/home/laravel/transcript.md') // Attach a document from a local path...
        $request->file('transcript'), // Attach an uploaded file...
    ]
);

```

Likewise, the `Laravel\Ai\Files\Image` class may be used to attach images to a prompt:
```


 1use App\Ai\Agents\ImageAnalyzer;




 2use Laravel\Ai\Files;




 3 



 4$response = (new ImageAnalyzer)->prompt(




 5    'What is in this image?',




 6    attachments: [




 7        Files\Image::fromStorage('photo.jpg') // Attach an image from a filesystem disk...




 8        Files\Image::fromPath('/home/laravel/photo.jpg') // Attach an image from a local path...




 9        $request->file('photo'), // Attach an uploaded file...




10    ]




11);




use App\Ai\Agents\ImageAnalyzer;
use Laravel\Ai\Files;

$response = (new ImageAnalyzer)->prompt(
    'What is in this image?',
    attachments: [
        Files\Image::fromStorage('photo.jpg') // Attach an image from a filesystem disk...
        Files\Image::fromPath('/home/laravel/photo.jpg') // Attach an image from a local path...
        $request->file('photo'), // Attach an uploaded file...
    ]
);

```

### [Streaming](https://laravel.com/docs/12.x/ai-sdk#streaming)
You may stream an agent's response by invoking the `stream` method. The returned `StreamableAgentResponse` may be returned from a route to automatically send a streaming response (SSE) to the client:
```


1use App\Ai\Agents\SalesCoach;




2 



3Route::get('/coach', function () {




4    return (new SalesCoach)->stream('Analyze this sales transcript...');




5});




use App\Ai\Agents\SalesCoach;

Route::get('/coach', function () {
    return (new SalesCoach)->stream('Analyze this sales transcript...');
});

```

The `then` method may be used to provide a closure that will be invoked when the entire response has been streamed to the client:
```


 1use App\Ai\Agents\SalesCoach;




 2use Laravel\Ai\Responses\StreamedAgentResponse;




 3 



 4Route::get('/coach', function () {




 5    return (new SalesCoach)




 6        ->stream('Analyze this sales transcript...')




 7        ->then(function (StreamedAgentResponse $response) {




 8            // $response->text, $response->events, $response->usage...




 9        });




10});




use App\Ai\Agents\SalesCoach;
use Laravel\Ai\Responses\StreamedAgentResponse;

Route::get('/coach', function () {
    return (new SalesCoach)
        ->stream('Analyze this sales transcript...')
        ->then(function (StreamedAgentResponse $response) {
            // $response->text, $response->events, $response->usage...
        });
});

```

Alternatively, you may iterate through the streamed events manually:
```


1$stream = (new SalesCoach)->stream('Analyze this sales transcript...');




2 



3foreach ($stream as $event) {




4    // ...




5}




$stream = (new SalesCoach)->stream('Analyze this sales transcript...');

foreach ($stream as $event) {
    // ...
}

```

#### [Streaming Using the Vercel AI SDK Protocol](https://laravel.com/docs/12.x/ai-sdk#streaming-using-the-vercel-ai-sdk-protocol)
You may stream the events using the `usingVercelDataProtocol` method on the streamable response:
```


1use App\Ai\Agents\SalesCoach;




2 



3Route::get('/coach', function () {




4    return (new SalesCoach)




5        ->stream('Analyze this sales transcript...')




6        ->usingVercelDataProtocol();




7});




use App\Ai\Agents\SalesCoach;

Route::get('/coach', function () {
    return (new SalesCoach)
        ->stream('Analyze this sales transcript...')
        ->usingVercelDataProtocol();
});

```

### [Broadcasting](https://laravel.com/docs/12.x/ai-sdk#broadcasting)
You may broadcast streamed events in a few different ways. First, you can simply invoke the `broadcast` or `broadcastNow` method on a streamed event:
```


1use App\Ai\Agents\SalesCoach;




2use Illuminate\Broadcasting\Channel;




3 



4$stream = (new SalesCoach)->stream('Analyze this sales transcript...');




5 



6foreach ($stream as $event) {




7    $event->broadcast(new Channel('channel-name'));




8}




use App\Ai\Agents\SalesCoach;
use Illuminate\Broadcasting\Channel;

$stream = (new SalesCoach)->stream('Analyze this sales transcript...');

foreach ($stream as $event) {
    $event->broadcast(new Channel('channel-name'));
}

```

Or, you can invoke an agent's `broadcastOnQueue` method to queue the agent operation and broadcast the streamed events as they are available:
```


1(new SalesCoach)->broadcastOnQueue(




2    'Analyze this sales transcript...'




3    new Channel('channel-name'),




4);




(new SalesCoach)->broadcastOnQueue(
    'Analyze this sales transcript...'
    new Channel('channel-name'),
);

```

### [Queueing](https://laravel.com/docs/12.x/ai-sdk#queueing)
Using an agent's `queue` method, you may prompt the agent, but allow it to process the response in the background, keeping your application feeling fast and responsive. The `then` and `catch` methods may be used to register closures that will be invoked when a response is available or if an exception occurs:
```


 1use Illuminate\Http\Request;




 2use Laravel\Ai\Responses\AgentResponse;




 3use Throwable;




 4 



 5Route::post('/coach', function (Request $request) {




 6    return (new SalesCoach)




 7        ->queue($request->input('transcript'))




 8        ->then(function (AgentResponse $response) {




 9            // ...




10        })




11        ->catch(function (Throwable $e) {




12            // ...




13        });




14 



15    return back();




16});




use Illuminate\Http\Request;
use Laravel\Ai\Responses\AgentResponse;
use Throwable;

Route::post('/coach', function (Request $request) {
    return (new SalesCoach)
        ->queue($request->input('transcript'))
        ->then(function (AgentResponse $response) {
            // ...
        })
        ->catch(function (Throwable $e) {
            // ...
        });

    return back();
});

```

### [Tools](https://laravel.com/docs/12.x/ai-sdk#tools)
Tools may be used to give agents additional functionality that they can utilize while responding to prompts. Tools can be created using the `make:tool` Artisan command:
```


1php artisan make:tool RandomNumberGenerator




php artisan make:tool RandomNumberGenerator

```

The generated tool will be placed in your application's `app/Ai/Tools` directory. Each tool contains a `handle` method that will be invoked by the agent when it needs to utilize the tool:
```


 1<?php




 2 



 3namespace App\Ai\Tools;




 4 



 5use Illuminate\Contracts\JsonSchema\JsonSchema;




 6use Laravel\Ai\Contracts\Tool;




 7use Laravel\Ai\Tools\Request;




 8use Stringable;




 9 



10class RandomNumberGenerator implements Tool




11{




12    /**




13     * Get the description of the tool's purpose.




14     */




15    public function description(): Stringable|string




16    {




17        return 'This tool may be used to generate cryptographically secure random numbers.';




18    }




19 



20    /**




21     * Execute the tool.




22     */




23    public function handle(Request $request): Stringable|string




24    {




25        return (string) random_int($request['min'], $request['max']);




26    }




27 



28    /**




29     * Get the tool's schema definition.




30     */




31    public function schema(JsonSchema $schema): array




32    {




33        return [




34            'min' => $schema->integer()->min(0)->required(),




35            'max' => $schema->integer()->required(),




36        ];




37    }




38}




<?php

namespace App\Ai\Tools;

use Illuminate\Contracts\JsonSchema\JsonSchema;
use Laravel\Ai\Contracts\Tool;
use Laravel\Ai\Tools\Request;
use Stringable;

class RandomNumberGenerator implements Tool
{
    /**
     * Get the description of the tool's purpose.
     */
    public function description(): Stringable|string
    {
        return 'This tool may be used to generate cryptographically secure random numbers.';
    }

    /**
     * Execute the tool.
     */
    public function handle(Request $request): Stringable|string
    {
        return (string) random_int($request['min'], $request['max']);
    }

    /**
     * Get the tool's schema definition.
     */
    public function schema(JsonSchema $schema): array
    {
        return [
            'min' => $schema->integer()->min(0)->required(),
            'max' => $schema->integer()->required(),
        ];
    }
}

```

Once you have defined your tool, you may return it from the `tools` method of any of your agents:
```


 1use App\Ai\Tools\RandomNumberGenerator;




 2 



 3/**




 4 * Get the tools available to the agent.




 5 *




 6 * @return Tool[]




 7 */




 8public function tools(): iterable




 9{




10    return [




11        new RandomNumberGenerator,




12    ];




13}




use App\Ai\Tools\RandomNumberGenerator;

/**
 * Get the tools available to the agent.
 *
 * @return Tool[]
 */
public function tools(): iterable
{
    return [
        new RandomNumberGenerator,
    ];
}

```

#### [Similarity Search](https://laravel.com/docs/12.x/ai-sdk#similarity-search)
The `SimilaritySearch` tool allows agents to search for documents similar to a given query using vector embeddings stored in your database. This is useful for retrieval-augmented generation (RAG) when you want to give agents access to search your application's data.
The simplest way to create a similarity search tool is using the `usingModel` method with an Eloquent model that has vector embeddings:
```


1use App\Models\Document;




2use Laravel\Ai\Tools\SimilaritySearch;




3 



4public function tools(): iterable




5{




6    return [




7        SimilaritySearch::usingModel(Document::class, 'embedding'),




8    ];




9}




use App\Models\Document;
use Laravel\Ai\Tools\SimilaritySearch;

public function tools(): iterable
{
    return [
        SimilaritySearch::usingModel(Document::class, 'embedding'),
    ];
}

```

The first argument is the Eloquent model class, and the second argument is the column containing the vector embeddings.
You may also provide a minimum similarity threshold between `0.0` and `1.0` and a closure to customize the query:
```


1SimilaritySearch::usingModel(




2    model: Document::class,




3    column: 'embedding',




4    minSimilarity: 0.7,




5    limit: 10,




6    query: fn ($query) => $query->where('published', true),




7),




SimilaritySearch::usingModel(
    model: Document::class,
    column: 'embedding',
    minSimilarity: 0.7,
    limit: 10,
    query: fn ($query) => $query->where('published', true),
),

```

For more control, you may create a similarity search tool with a custom closure that returns the search results:
```


 1use App\Models\Document;




 2use Laravel\Ai\Tools\SimilaritySearch;




 3 



 4public function tools(): iterable




 5{




 6    return [




 7        new SimilaritySearch(using: function (string $query) {




 8            return Document::query()




 9                ->where('user_id', $this->user->id)




10                ->whereVectorSimilarTo('embedding', $query)




11                ->limit(10)




12                ->get();




13        }),




14    ];




15}




use App\Models\Document;
use Laravel\Ai\Tools\SimilaritySearch;

public function tools(): iterable
{
    return [
        new SimilaritySearch(using: function (string $query) {
            return Document::query()
                ->where('user_id', $this->user->id)
                ->whereVectorSimilarTo('embedding', $query)
                ->limit(10)
                ->get();
        }),
    ];
}

```

You may customize the tool's description using the `withDescription` method:
```


1SimilaritySearch::usingModel(Document::class, 'embedding')




2    ->withDescription('Search the knowledge base for relevant articles.'),




SimilaritySearch::usingModel(Document::class, 'embedding')
    ->withDescription('Search the knowledge base for relevant articles.'),

```

### [Provider Tools](https://laravel.com/docs/12.x/ai-sdk#provider-tools)
Provider tools are special tools implemented natively by AI providers, offering capabilities like web searching, URL fetching, and file searching. Unlike regular tools, provider tools are executed by the provider itself rather than your application.
Provider tools can be returned by your agent's `tools` method.
#### [Web Search](https://laravel.com/docs/12.x/ai-sdk#web-search)
The `WebSearch` provider tool allows agents to search the web for real-time information. This is useful for answering questions about current events, recent data, or topics that may have changed since the model's training cutoff.
**Supported Providers:** Anthropic, OpenAI, Gemini
```


1use Laravel\Ai\Providers\Tools\WebSearch;




2 



3public function tools(): iterable




4{




5    return [




6        new WebSearch,




7    ];




8}




use Laravel\Ai\Providers\Tools\WebSearch;

public function tools(): iterable
{
    return [
        new WebSearch,
    ];
}

```

You may configure the web search tool to limit the number of searches or restrict results to specific domains:
```


1(new WebSearch)->max(5)->allow(['laravel.com', 'php.net']),




(new WebSearch)->max(5)->allow(['laravel.com', 'php.net']),

```

To refine search results based on user location, use the `location` method:
```


1(new WebSearch)->location(




2    city: 'New York',




3    region: 'NY',




4    country: 'US'




5);




(new WebSearch)->location(
    city: 'New York',
    region: 'NY',
    country: 'US'
);

```

#### [Web Fetch](https://laravel.com/docs/12.x/ai-sdk#web-fetch)
The `WebFetch` provider tool allows agents to fetch and read the contents of web pages. This is useful when you need the agent to analyze specific URLs or retrieve detailed information from known web pages.
**Supported providers:** Anthropic, Gemini
```


1use Laravel\Ai\Providers\Tools\WebFetch;




2 



3public function tools(): iterable




4{




5    return [




6        new WebFetch,




7    ];




8}




use Laravel\Ai\Providers\Tools\WebFetch;

public function tools(): iterable
{
    return [
        new WebFetch,
    ];
}

```

You may configure the web fetch tool to limit the number of fetches or restrict to specific domains:
```


1(new WebFetch)->max(3)->allow(['docs.laravel.com']),




(new WebFetch)->max(3)->allow(['docs.laravel.com']),

```

#### [File Search](https://laravel.com/docs/12.x/ai-sdk#file-search)
The `FileSearch` provider tool allows agents to search through [files](https://laravel.com/docs/12.x/ai-sdk#files) stored in [vector stores](https://laravel.com/docs/12.x/ai-sdk#vector-stores). This enables retrieval-augmented generation (RAG) by allowing the agent to search your uploaded documents for relevant information.
**Supported providers:** OpenAI, Gemini
```


1use Laravel\Ai\Providers\Tools\FileSearch;




2 



3public function tools(): iterable




4{




5    return [




6        new FileSearch(stores: ['store_id']),




7    ];




8}




use Laravel\Ai\Providers\Tools\FileSearch;

public function tools(): iterable
{
    return [
        new FileSearch(stores: ['store_id']),
    ];
}

```

You may provide multiple vector store IDs to search across multiple stores:
```


1new FileSearch(stores: ['store_1', 'store_2']);




new FileSearch(stores: ['store_1', 'store_2']);

```

If your files have [metadata](https://laravel.com/docs/12.x/ai-sdk#adding-files-to-stores), you may filter the search results by providing a `where` argument. For simple equality filters, pass an array:
```


1new FileSearch(stores: ['store_id'], where: [




2    'author' => 'Taylor Otwell',




3    'year' => 2026,




4]);




new FileSearch(stores: ['store_id'], where: [
    'author' => 'Taylor Otwell',
    'year' => 2026,
]);

```

For more complex filters, you may pass a closure that receives a `FileSearchQuery` instance:
```


1use Laravel\Ai\Providers\Tools\FileSearchQuery;




2 



3new FileSearch(stores: ['store_id'], where: fn (FileSearchQuery $query) =>




4    $query->where('author', 'Taylor Otwell')




5        ->whereNot('status', 'draft')




6        ->whereIn('category', ['news', 'updates'])




7);




use Laravel\Ai\Providers\Tools\FileSearchQuery;

new FileSearch(stores: ['store_id'], where: fn (FileSearchQuery $query) =>
    $query->where('author', 'Taylor Otwell')
        ->whereNot('status', 'draft')
        ->whereIn('category', ['news', 'updates'])
);

```

### [Middleware](https://laravel.com/docs/12.x/ai-sdk#middleware)
Agents support middleware, allowing you to intercept and modify prompts before they are sent to the provider. Middleware can be created using the `make:agent-middleware` Artisan command:
```


1php artisan make:agent-middleware LogPrompts




php artisan make:agent-middleware LogPrompts

```

The generated middleware will be placed in your application's `app/Ai/Middleware` directory. To add middleware to an agent, implement the `HasMiddleware` interface and define a `middleware` method that returns an array of middleware classes:
```


 1<?php




 2 



 3namespace App\Ai\Agents;




 4 



 5use App\Ai\Middleware\LogPrompts;




 6use Laravel\Ai\Contracts\Agent;




 7use Laravel\Ai\Contracts\HasMiddleware;




 8use Laravel\Ai\Promptable;




 9 



10class SalesCoach implements Agent, HasMiddleware




11{




12    use Promptable;




13 



14    // ...




15 



16    /**




17     * Get the agent's middleware.




18     */




19    public function middleware(): array




20    {




21        return [




22            new LogPrompts,




23        ];




24    }




25}




<?php

namespace App\Ai\Agents;

use App\Ai\Middleware\LogPrompts;
use Laravel\Ai\Contracts\Agent;
use Laravel\Ai\Contracts\HasMiddleware;
use Laravel\Ai\Promptable;

class SalesCoach implements Agent, HasMiddleware
{
    use Promptable;

    // ...

    /**
     * Get the agent's middleware.
     */
    public function middleware(): array
    {
        return [
            new LogPrompts,
        ];
    }
}

```

Each middleware class should define a `handle` method that receives the `AgentPrompt` and a `Closure` to pass the prompt to the next middleware:
```


 1<?php




 2 



 3namespace App\Ai\Middleware;




 4 



 5use Closure;




 6use Laravel\Ai\Prompts\AgentPrompt;




 7 



 8class LogPrompts




 9{




10    /**




11     * Handle the incoming prompt.




12     */




13    public function handle(AgentPrompt $prompt, Closure $next)




14    {




15        Log::info('Prompting agent', ['prompt' => $prompt->prompt]);




16 



17        return $next($prompt);




18    }




19}




<?php

namespace App\Ai\Middleware;

use Closure;
use Laravel\Ai\Prompts\AgentPrompt;

class LogPrompts
{
    /**
     * Handle the incoming prompt.
     */
    public function handle(AgentPrompt $prompt, Closure $next)
    {
        Log::info('Prompting agent', ['prompt' => $prompt->prompt]);

        return $next($prompt);
    }
}

```

You may use the `then` method on the response to execute code after the agent has finished processing. This works for both synchronous and streaming responses:
```


1public function handle(AgentPrompt $prompt, Closure $next)




2{




3    return $next($prompt)->then(function (AgentResponse $response) {




4        Log::info('Agent responded', ['text' => $response->text]);




5    });




6}




public function handle(AgentPrompt $prompt, Closure $next)
{
    return $next($prompt)->then(function (AgentResponse $response) {
        Log::info('Agent responded', ['text' => $response->text]);
    });
}

```

### [Anonymous Agents](https://laravel.com/docs/12.x/ai-sdk#anonymous-agents)
Sometimes you may want to quickly interact with a model without creating a dedicated agent class. You can create an ad-hoc, anonymous agent using the `agent` function:
```


1use function Laravel\Ai\{agent};




2 



3$response = agent(




4    instructions: 'You are an expert at software development.',




5    messages: [],




6    tools: [],




7)->prompt('Tell me about Laravel')




use function Laravel\Ai\{agent};

$response = agent(
    instructions: 'You are an expert at software development.',
    messages: [],
    tools: [],
)->prompt('Tell me about Laravel')

```

Anonymous agents may also produce structured output:
```


1use Illuminate\Contracts\JsonSchema\JsonSchema;




2 



3use function Laravel\Ai\{agent};




4 



5$response = agent(




6    schema: fn (JsonSchema $schema) => [




7        'number' => $schema->integer()->required(),




8    ],




9)->prompt('Generate a random number less than 100')




use Illuminate\Contracts\JsonSchema\JsonSchema;

use function Laravel\Ai\{agent};

$response = agent(
    schema: fn (JsonSchema $schema) => [
        'number' => $schema->integer()->required(),
    ],
)->prompt('Generate a random number less than 100')

```

### [Agent Configuration](https://laravel.com/docs/12.x/ai-sdk#agent-configuration)
You may configure text generation options for an agent using PHP attributes. The following attributes are available:
  * `MaxSteps`: The maximum number of steps the agent may take when using tools.
  * `MaxTokens`: The maximum number of tokens the model may generate.
  * `Model`: The model the agent should use.
  * `Provider`: The AI provider (or providers for failover) to use for the agent.
  * `Temperature`: The sampling temperature to use for generation (0.0 to 1.0).
  * `Timeout`: The HTTP timeout in seconds for agent requests (default: 60).
  * `UseCheapestModel`: Use the provider's cheapest text model for cost optimization.
  * `UseSmartestModel`: Use the provider's most capable text model for complex tasks.


```


 1<?php




 2 



 3namespace App\Ai\Agents;




 4 



 5use Laravel\Ai\Attributes\MaxSteps;




 6use Laravel\Ai\Attributes\MaxTokens;




 7use Laravel\Ai\Attributes\Model;




 8use Laravel\Ai\Attributes\Provider;




 9use Laravel\Ai\Attributes\Temperature;




10use Laravel\Ai\Attributes\Timeout;




11use Laravel\Ai\Contracts\Agent;




12use Laravel\Ai\Enums\Lab;




13use Laravel\Ai\Promptable;




14 



15#[Provider(Lab::Anthropic)]




16#[Model('claude-haiku-4-5-20251001')]




17#[MaxSteps(10)]




18#[MaxTokens(4096)]




19#[Temperature(0.7)]




20#[Timeout(120)]




21class SalesCoach implements Agent




22{




23    use Promptable;




24 



25    // ...




26}




<?php

namespace App\Ai\Agents;

use Laravel\Ai\Attributes\MaxSteps;
use Laravel\Ai\Attributes\MaxTokens;
use Laravel\Ai\Attributes\Model;
use Laravel\Ai\Attributes\Provider;
use Laravel\Ai\Attributes\Temperature;
use Laravel\Ai\Attributes\Timeout;
use Laravel\Ai\Contracts\Agent;
use Laravel\Ai\Enums\Lab;
use Laravel\Ai\Promptable;

#[Provider(Lab::Anthropic)]
#[Model('claude-haiku-4-5-20251001')]
#[MaxSteps(10)]
#[MaxTokens(4096)]
#[Temperature(0.7)]
#[Timeout(120)]
class SalesCoach implements Agent
{
    use Promptable;

    // ...
}

```

The `UseCheapestModel` and `UseSmartestModel` attributes allow you to automatically select the most cost-effective or most capable model for a given provider without specifying a model name. This is useful when you want to optimize for cost or capability across different providers:
```


 1use Laravel\Ai\Attributes\UseCheapestModel;




 2use Laravel\Ai\Attributes\UseSmartestModel;




 3use Laravel\Ai\Contracts\Agent;




 4use Laravel\Ai\Promptable;




 5 



 6#[UseCheapestModel]




 7class SimpleSummarizer implements Agent




 8{




 9    use Promptable;




10 



11    // Will use the cheapest model (e.g., Haiku)...




12}




13 



14#[UseSmartestModel]




15class ComplexReasoner implements Agent




16{




17    use Promptable;




18 



19    // Will use the most capable model (e.g., Opus)...




20}




use Laravel\Ai\Attributes\UseCheapestModel;
use Laravel\Ai\Attributes\UseSmartestModel;
use Laravel\Ai\Contracts\Agent;
use Laravel\Ai\Promptable;

#[UseCheapestModel]
class SimpleSummarizer implements Agent
{
    use Promptable;

    // Will use the cheapest model (e.g., Haiku)...
}

#[UseSmartestModel]
class ComplexReasoner implements Agent
{
    use Promptable;

    // Will use the most capable model (e.g., Opus)...
}

```
