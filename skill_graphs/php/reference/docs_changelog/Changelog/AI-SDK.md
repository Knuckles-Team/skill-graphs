## AI SDK
### Make Provider Default Models Configurable
Pull request by
The default models used for text, images, audio, transcription, and embeddings may are now configurable in your application's `config/ai.php` file. This gives you granular control over the exact models you'd like to use if you don't want to rely on the package defaults.
```


1return [




2    'models' => [




3        'text' => [




4            'default' => 'claude-sonnet-4-6',




5            'cheapest' => 'claude-haiku-4-5-20251001',




6            'smartest' => 'claude-opus-4-6',




7        ],




8    ],




9],




return [
    'models' => [
        'text' => [
            'default' => 'claude-sonnet-4-6',
            'cheapest' => 'claude-haiku-4-5-20251001',
            'smartest' => 'claude-opus-4-6',
        ],
    ],
],

```

### Add Support for Timeouts in Transcription
Pull request by
Transcription now supports timeouts, giving you better control in production workloads and preventing long-running requests from tying up workers.
```


1$transcript = Transcription::fromPath('./podcast.mp3')->timeout(240)->generate(Lab::ElevenLabs);




$transcript = Transcription::fromPath('./podcast.mp3')->timeout(240)->generate(Lab::ElevenLabs);

```

### New Providers Added
#### Azure OpenAI
Pull request by
#### Mistral AI
Pull request by
#### Voyage AI
Pull request by
#### DeepSeek
Pull request by
