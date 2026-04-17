## [Installation](https://laravel.com/docs/12.x/ai-sdk#installation)
You can install the Laravel AI SDK via Composer:
```


1composer require laravel/ai




composer require laravel/ai

```

Next, you should publish the AI SDK configuration and migration files using the `vendor:publish` Artisan command:
```


1php artisan vendor:publish --provider="Laravel\Ai\AiServiceProvider"




php artisan vendor:publish --provider="Laravel\Ai\AiServiceProvider"

```

Finally, you should run your application's database migrations. This will create a `agent_conversations` and `agent_conversation_messages` table that the AI SDK uses to power its conversation storage:
```


1php artisan migrate




php artisan migrate

```

### [Configuration](https://laravel.com/docs/12.x/ai-sdk#configuration)
You may define your AI provider credentials in your application's `config/ai.php` configuration file or as environment variables in your application's `.env` file:
```


 1ANTHROPIC_API_KEY=




 2COHERE_API_KEY=




 3ELEVENLABS_API_KEY=




 4GEMINI_API_KEY=




 5MISTRAL_API_KEY=




 6OLLAMA_API_KEY=




 7OPENAI_API_KEY=




 8JINA_API_KEY=




 9VOYAGEAI_API_KEY=




10XAI_API_KEY=




ANTHROPIC_API_KEY=
COHERE_API_KEY=
ELEVENLABS_API_KEY=
GEMINI_API_KEY=
MISTRAL_API_KEY=
OLLAMA_API_KEY=
OPENAI_API_KEY=
JINA_API_KEY=
VOYAGEAI_API_KEY=
XAI_API_KEY=

```

The default models used for text, images, audio, transcription, and embeddings may also be configured in your application's `config/ai.php` configuration file.
### [Custom Base URLs](https://laravel.com/docs/12.x/ai-sdk#custom-base-urls)
By default, the Laravel AI SDK connects directly to each provider's public API endpoint. However, you may need to route requests through a different endpoint - for example, when using a proxy service to centralize API key management, implement rate limiting, or route traffic through a corporate gateway.
You may configure custom base URLs by adding a `url` parameter to your provider configuration:
```


 1'providers' => [




 2    'openai' => [




 3        'driver' => 'openai',




 4        'key' => env('OPENAI_API_KEY'),




 5        'url' => env('OPENAI_BASE_URL'),




 6    ],




 7 



 8    'anthropic' => [




 9        'driver' => 'anthropic',




10        'key' => env('ANTHROPIC_API_KEY'),




11        'url' => env('ANTHROPIC_BASE_URL'),




12    ],




13],




'providers' => [
    'openai' => [
        'driver' => 'openai',
        'key' => env('OPENAI_API_KEY'),
        'url' => env('OPENAI_BASE_URL'),
    ],

    'anthropic' => [
        'driver' => 'anthropic',
        'key' => env('ANTHROPIC_API_KEY'),
        'url' => env('ANTHROPIC_BASE_URL'),
    ],
],

```

This is useful when routing requests through a proxy service (such as LiteLLM or Azure OpenAI Gateway) or using alternative endpoints.
Custom base URLs are supported for the following providers: OpenAI, Anthropic, Gemini, Groq, Cohere, DeepSeek, xAI, and OpenRouter.
### [Provider Support](https://laravel.com/docs/12.x/ai-sdk#provider-support)
The AI SDK supports a variety of providers across its features. The following table summarizes which providers are available for each feature:
Feature | Providers
---|---
Text | OpenAI, Anthropic, Gemini, Azure, Groq, xAI, DeepSeek, Mistral, Ollama
Images | OpenAI, Gemini, xAI
TTS | OpenAI, ElevenLabs
STT | OpenAI, ElevenLabs, Mistral
Embeddings | OpenAI, Gemini, Azure, Cohere, Mistral, Jina, VoyageAI
Reranking | Cohere, Jina
Files | OpenAI, Anthropic, Gemini
The `Laravel\Ai\Enums\Lab` enum may be used to reference providers throughout your code instead of using plain strings:
```


1use Laravel\Ai\Enums\Lab;




2 



3Lab::Anthropic;




4Lab::OpenAI;




5Lab::Gemini;




6// ...




use Laravel\Ai\Enums\Lab;

Lab::Anthropic;
Lab::OpenAI;
Lab::Gemini;
// ...

```
