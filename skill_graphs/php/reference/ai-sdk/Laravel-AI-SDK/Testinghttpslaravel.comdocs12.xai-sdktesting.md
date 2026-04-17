## [Testing](https://laravel.com/docs/12.x/ai-sdk#testing)
### [Agents](https://laravel.com/docs/12.x/ai-sdk#testing-agents)
To fake an agent's responses during tests, call the `fake` method on the agent class. You may optionally provide an array of responses or a closure:
```


 1use App\Ai\Agents\SalesCoach;




 2use Laravel\Ai\Prompts\AgentPrompt;




 3 



 4// Automatically generate a fixed response for every prompt...




 5SalesCoach::fake();




 6 



 7// Provide a list of prompt responses...




 8SalesCoach::fake([




 9    'First response',




10    'Second response',




11]);




12 



13// Dynamically handle prompt responses based on the incoming prompt...




14SalesCoach::fake(function (AgentPrompt $prompt) {




15    return 'Response for: '.$prompt->prompt;




16});




use App\Ai\Agents\SalesCoach;
use Laravel\Ai\Prompts\AgentPrompt;

// Automatically generate a fixed response for every prompt...
SalesCoach::fake();

// Provide a list of prompt responses...
SalesCoach::fake([
    'First response',
    'Second response',
]);

// Dynamically handle prompt responses based on the incoming prompt...
SalesCoach::fake(function (AgentPrompt $prompt) {
    return 'Response for: '.$prompt->prompt;
});

```

When `Agent::fake()` is invoked on an agent that returns structured output, Laravel will automatically generate fake data that matches your agent's defined output schema.
After prompting the agent, you may make assertions about the prompts that were received:
```


 1use Laravel\Ai\Prompts\AgentPrompt;




 2 



 3SalesCoach::assertPrompted('Analyze this...');




 4 



 5SalesCoach::assertPrompted(function (AgentPrompt $prompt) {




 6    return $prompt->contains('Analyze');




 7});




 8 



 9SalesCoach::assertNotPrompted('Missing prompt');




10 



11SalesCoach::assertNeverPrompted();




use Laravel\Ai\Prompts\AgentPrompt;

SalesCoach::assertPrompted('Analyze this...');

SalesCoach::assertPrompted(function (AgentPrompt $prompt) {
    return $prompt->contains('Analyze');
});

SalesCoach::assertNotPrompted('Missing prompt');

SalesCoach::assertNeverPrompted();

```

For queued agent invocations, use the queued assertion methods:
```


 1use Laravel\Ai\QueuedAgentPrompt;




 2 



 3SalesCoach::assertQueued('Analyze this...');




 4 



 5SalesCoach::assertQueued(function (QueuedAgentPrompt $prompt) {




 6    return $prompt->contains('Analyze');




 7});




 8 



 9SalesCoach::assertNotQueued('Missing prompt');




10 



11SalesCoach::assertNeverQueued();




use Laravel\Ai\QueuedAgentPrompt;

SalesCoach::assertQueued('Analyze this...');

SalesCoach::assertQueued(function (QueuedAgentPrompt $prompt) {
    return $prompt->contains('Analyze');
});

SalesCoach::assertNotQueued('Missing prompt');

SalesCoach::assertNeverQueued();

```

To ensure all agent invocations have a corresponding fake response, you may use `preventStrayPrompts`. If an agent is invoked without a defined fake response, an exception will be thrown:
```


1SalesCoach::fake()->preventStrayPrompts();




SalesCoach::fake()->preventStrayPrompts();

```

### [Images](https://laravel.com/docs/12.x/ai-sdk#testing-images)
Image generations may be faked by invoking the `fake` method on the `Image` class. Once image has been faked, various assertions may be performed against the recorded image generation prompts:
```


 1use Laravel\Ai\Image;




 2use Laravel\Ai\Prompts\ImagePrompt;




 3use Laravel\Ai\Prompts\QueuedImagePrompt;




 4 



 5// Automatically generate a fixed response for every prompt...




 6Image::fake();




 7 



 8// Provide a list of prompt responses...




 9Image::fake([




10    base64_encode($firstImage),




11    base64_encode($secondImage),




12]);




13 



14// Dynamically handle prompt responses based on the incoming prompt...




15Image::fake(function (ImagePrompt $prompt) {




16    return base64_encode('...');




17});




use Laravel\Ai\Image;
use Laravel\Ai\Prompts\ImagePrompt;
use Laravel\Ai\Prompts\QueuedImagePrompt;

// Automatically generate a fixed response for every prompt...
Image::fake();

// Provide a list of prompt responses...
Image::fake([
    base64_encode($firstImage),
    base64_encode($secondImage),
]);

// Dynamically handle prompt responses based on the incoming prompt...
Image::fake(function (ImagePrompt $prompt) {
    return base64_encode('...');
});

```

After generating images, you may make assertions about the prompts that were received:
```


1Image::assertGenerated(function (ImagePrompt $prompt) {




2    return $prompt->contains('sunset') && $prompt->isLandscape();




3});




4 



5Image::assertNotGenerated('Missing prompt');




6 



7Image::assertNothingGenerated();




Image::assertGenerated(function (ImagePrompt $prompt) {
    return $prompt->contains('sunset') && $prompt->isLandscape();
});

Image::assertNotGenerated('Missing prompt');

Image::assertNothingGenerated();

```

For queued image generations, use the queued assertion methods:
```


1Image::assertQueued(




2    fn (QueuedImagePrompt $prompt) => $prompt->contains('sunset')




3);




4 



5Image::assertNotQueued('Missing prompt');




6 



7Image::assertNothingQueued();




Image::assertQueued(
    fn (QueuedImagePrompt $prompt) => $prompt->contains('sunset')
);

Image::assertNotQueued('Missing prompt');

Image::assertNothingQueued();

```

To ensure all image generations have a corresponding fake response, you may use `preventStrayImages`. If an image is generated without a defined fake response, an exception will be thrown:
```


1Image::fake()->preventStrayImages();




Image::fake()->preventStrayImages();

```

### [Audio](https://laravel.com/docs/12.x/ai-sdk#testing-audio)
Audio generations may be faked by invoking the `fake` method on the `Audio` class. Once audio has been faked, various assertions may be performed against the recorded audio generation prompts:
```


 1use Laravel\Ai\Audio;




 2use Laravel\Ai\Prompts\AudioPrompt;




 3use Laravel\Ai\Prompts\QueuedAudioPrompt;




 4 



 5// Automatically generate a fixed response for every prompt...




 6Audio::fake();




 7 



 8// Provide a list of prompt responses...




 9Audio::fake([




10    base64_encode($firstAudio),




11    base64_encode($secondAudio),




12]);




13 



14// Dynamically handle prompt responses based on the incoming prompt...




15Audio::fake(function (AudioPrompt $prompt) {




16    return base64_encode('...');




17});




use Laravel\Ai\Audio;
use Laravel\Ai\Prompts\AudioPrompt;
use Laravel\Ai\Prompts\QueuedAudioPrompt;

// Automatically generate a fixed response for every prompt...
Audio::fake();

// Provide a list of prompt responses...
Audio::fake([
    base64_encode($firstAudio),
    base64_encode($secondAudio),
]);

// Dynamically handle prompt responses based on the incoming prompt...
Audio::fake(function (AudioPrompt $prompt) {
    return base64_encode('...');
});

```

After generating audio, you may make assertions about the prompts that were received:
```


1Audio::assertGenerated(function (AudioPrompt $prompt) {




2    return $prompt->contains('Hello') && $prompt->isFemale();




3});




4 



5Audio::assertNotGenerated('Missing prompt');




6 



7Audio::assertNothingGenerated();




Audio::assertGenerated(function (AudioPrompt $prompt) {
    return $prompt->contains('Hello') && $prompt->isFemale();
});

Audio::assertNotGenerated('Missing prompt');

Audio::assertNothingGenerated();

```

For queued audio generations, use the queued assertion methods:
```


1Audio::assertQueued(




2    fn (QueuedAudioPrompt $prompt) => $prompt->contains('Hello')




3);




4 



5Audio::assertNotQueued('Missing prompt');




6 



7Audio::assertNothingQueued();




Audio::assertQueued(
    fn (QueuedAudioPrompt $prompt) => $prompt->contains('Hello')
);

Audio::assertNotQueued('Missing prompt');

Audio::assertNothingQueued();

```

To ensure all audio generations have a corresponding fake response, you may use `preventStrayAudio`. If audio is generated without a defined fake response, an exception will be thrown:
```


1Audio::fake()->preventStrayAudio();




Audio::fake()->preventStrayAudio();

```

### [Transcriptions](https://laravel.com/docs/12.x/ai-sdk#testing-transcriptions)
Transcription generations may be faked by invoking the `fake` method on the `Transcription` class. Once transcription has been faked, various assertions may be performed against the recorded transcription generation prompts:
```


 1use Laravel\Ai\Transcription;




 2use Laravel\Ai\Prompts\TranscriptionPrompt;




 3use Laravel\Ai\Prompts\QueuedTranscriptionPrompt;




 4 



 5// Automatically generate a fixed response for every prompt...




 6Transcription::fake();




 7 



 8// Provide a list of prompt responses...




 9Transcription::fake([




10    'First transcription text.',




11    'Second transcription text.',




12]);




13 



14// Dynamically handle prompt responses based on the incoming prompt...




15Transcription::fake(function (TranscriptionPrompt $prompt) {




16    return 'Transcribed text...';




17});




use Laravel\Ai\Transcription;
use Laravel\Ai\Prompts\TranscriptionPrompt;
use Laravel\Ai\Prompts\QueuedTranscriptionPrompt;

// Automatically generate a fixed response for every prompt...
Transcription::fake();

// Provide a list of prompt responses...
Transcription::fake([
    'First transcription text.',
    'Second transcription text.',
]);

// Dynamically handle prompt responses based on the incoming prompt...
Transcription::fake(function (TranscriptionPrompt $prompt) {
    return 'Transcribed text...';
});

```

After generating transcriptions, you may make assertions about the prompts that were received:
```


1Transcription::assertGenerated(function (TranscriptionPrompt $prompt) {




2    return $prompt->language === 'en' && $prompt->isDiarized();




3});




4 



5Transcription::assertNotGenerated(




6    fn (TranscriptionPrompt $prompt) => $prompt->language === 'fr'




7);




8 



9Transcription::assertNothingGenerated();




Transcription::assertGenerated(function (TranscriptionPrompt $prompt) {
    return $prompt->language === 'en' && $prompt->isDiarized();
});

Transcription::assertNotGenerated(
    fn (TranscriptionPrompt $prompt) => $prompt->language === 'fr'
);

Transcription::assertNothingGenerated();

```

For queued transcription generations, use the queued assertion methods:
```


1Transcription::assertQueued(




2    fn (QueuedTranscriptionPrompt $prompt) => $prompt->isDiarized()




3);




4 



5Transcription::assertNotQueued(




6    fn (QueuedTranscriptionPrompt $prompt) => $prompt->language === 'fr'




7);




8 



9Transcription::assertNothingQueued();




Transcription::assertQueued(
    fn (QueuedTranscriptionPrompt $prompt) => $prompt->isDiarized()
);

Transcription::assertNotQueued(
    fn (QueuedTranscriptionPrompt $prompt) => $prompt->language === 'fr'
);

Transcription::assertNothingQueued();

```

To ensure all transcription generations have a corresponding fake response, you may use `preventStrayTranscriptions`. If a transcription is generated without a defined fake response, an exception will be thrown:
```


1Transcription::fake()->preventStrayTranscriptions();




Transcription::fake()->preventStrayTranscriptions();

```

### [Embeddings](https://laravel.com/docs/12.x/ai-sdk#testing-embeddings)
Embeddings generations may be faked by invoking the `fake` method on the `Embeddings` class. Once embeddings has been faked, various assertions may be performed against the recorded embeddings generation prompts:
```


 1use Laravel\Ai\Embeddings;




 2use Laravel\Ai\Prompts\EmbeddingsPrompt;




 3use Laravel\Ai\Prompts\QueuedEmbeddingsPrompt;




 4 



 5// Automatically generate fake embeddings of the proper dimensions for every prompt...




 6Embeddings::fake();




 7 



 8// Provide a list of prompt responses...




 9Embeddings::fake([




10    [$firstEmbeddingVector],




11    [$secondEmbeddingVector],




12]);




13 



14// Dynamically handle prompt responses based on the incoming prompt...




15Embeddings::fake(function (EmbeddingsPrompt $prompt) {




16    return array_map(




17        fn () => Embeddings::fakeEmbedding($prompt->dimensions),




18        $prompt->inputs




19    );




20});




use Laravel\Ai\Embeddings;
use Laravel\Ai\Prompts\EmbeddingsPrompt;
use Laravel\Ai\Prompts\QueuedEmbeddingsPrompt;

// Automatically generate fake embeddings of the proper dimensions for every prompt...
Embeddings::fake();

// Provide a list of prompt responses...
Embeddings::fake([
    [$firstEmbeddingVector],
    [$secondEmbeddingVector],
]);

// Dynamically handle prompt responses based on the incoming prompt...
Embeddings::fake(function (EmbeddingsPrompt $prompt) {
    return array_map(
        fn () => Embeddings::fakeEmbedding($prompt->dimensions),
        $prompt->inputs
    );
});

```

After generating embeddings, you may make assertions about the prompts that were received:
```


1Embeddings::assertGenerated(function (EmbeddingsPrompt $prompt) {




2    return $prompt->contains('Laravel') && $prompt->dimensions === 1536;




3});




4 



5Embeddings::assertNotGenerated(




6    fn (EmbeddingsPrompt $prompt) => $prompt->contains('Other')




7);




8 



9Embeddings::assertNothingGenerated();




Embeddings::assertGenerated(function (EmbeddingsPrompt $prompt) {
    return $prompt->contains('Laravel') && $prompt->dimensions === 1536;
});

Embeddings::assertNotGenerated(
    fn (EmbeddingsPrompt $prompt) => $prompt->contains('Other')
);

Embeddings::assertNothingGenerated();

```

For queued embeddings generations, use the queued assertion methods:
```


1Embeddings::assertQueued(




2    fn (QueuedEmbeddingsPrompt $prompt) => $prompt->contains('Laravel')




3);




4 



5Embeddings::assertNotQueued(




6    fn (QueuedEmbeddingsPrompt $prompt) => $prompt->contains('Other')




7);




8 



9Embeddings::assertNothingQueued();




Embeddings::assertQueued(
    fn (QueuedEmbeddingsPrompt $prompt) => $prompt->contains('Laravel')
);

Embeddings::assertNotQueued(
    fn (QueuedEmbeddingsPrompt $prompt) => $prompt->contains('Other')
);

Embeddings::assertNothingQueued();

```

To ensure all embeddings generations have a corresponding fake response, you may use `preventStrayEmbeddings`. If embeddings are generated without a defined fake response, an exception will be thrown:
```


1Embeddings::fake()->preventStrayEmbeddings();




Embeddings::fake()->preventStrayEmbeddings();

```

### [Reranking](https://laravel.com/docs/12.x/ai-sdk#testing-reranking)
Reranking operations may be faked by invoking the `fake` method on the `Reranking` class:
```


 1use Laravel\Ai\Reranking;




 2use Laravel\Ai\Prompts\RerankingPrompt;




 3use Laravel\Ai\Responses\Data\RankedDocument;




 4 



 5// Automatically generate a fake reranked responses...




 6Reranking::fake();




 7 



 8// Provide custom responses...




 9Reranking::fake([




10    [




11        new RankedDocument(index: 0, document: 'First', score: 0.95),




12        new RankedDocument(index: 1, document: 'Second', score: 0.80),




13    ],




14]);




use Laravel\Ai\Reranking;
use Laravel\Ai\Prompts\RerankingPrompt;
use Laravel\Ai\Responses\Data\RankedDocument;

// Automatically generate a fake reranked responses...
Reranking::fake();

// Provide custom responses...
Reranking::fake([
    [
        new RankedDocument(index: 0, document: 'First', score: 0.95),
        new RankedDocument(index: 1, document: 'Second', score: 0.80),
    ],
]);

```

After reranking, you may make assertions about the operations that were performed:
```


1Reranking::assertReranked(function (RerankingPrompt $prompt) {




2    return $prompt->contains('Laravel') && $prompt->limit === 5;




3});




4 



5Reranking::assertNotReranked(




6    fn (RerankingPrompt $prompt) => $prompt->contains('Django')




7);




8 



9Reranking::assertNothingReranked();




Reranking::assertReranked(function (RerankingPrompt $prompt) {
    return $prompt->contains('Laravel') && $prompt->limit === 5;
});

Reranking::assertNotReranked(
    fn (RerankingPrompt $prompt) => $prompt->contains('Django')
);

Reranking::assertNothingReranked();

```

### [Files](https://laravel.com/docs/12.x/ai-sdk#testing-files)
File operations may be faked by invoking the `fake` method on the `Files` class:
```


1use Laravel\Ai\Files;




2 



3Files::fake();




use Laravel\Ai\Files;

Files::fake();

```

Once file operations have been faked, you may make assertions about the uploads and deletions that occurred:
```


 1use Laravel\Ai\Contracts\Files\StorableFile;




 2use Laravel\Ai\Files\Document;




 3 



 4// Store files...




 5Document::fromString('Hello, Laravel!', mimeType: 'text/plain')




 6    ->as('hello.txt')




 7    ->put();




 8 



 9// Make assertions...




10Files::assertStored(fn (StorableFile $file) =>




11    (string) $file === 'Hello, Laravel!' &&




12        $file->mimeType() === 'text/plain';




13);




14 



15Files::assertNotStored(fn (StorableFile $file) =>




16    (string) $file === 'Hello, World!'




17);




18 



19Files::assertNothingStored();




use Laravel\Ai\Contracts\Files\StorableFile;
use Laravel\Ai\Files\Document;

// Store files...
Document::fromString('Hello, Laravel!', mimeType: 'text/plain')
    ->as('hello.txt')
    ->put();

// Make assertions...
Files::assertStored(fn (StorableFile $file) =>
    (string) $file === 'Hello, Laravel!' &&
        $file->mimeType() === 'text/plain';
);

Files::assertNotStored(fn (StorableFile $file) =>
    (string) $file === 'Hello, World!'
);

Files::assertNothingStored();

```

For asserting against file deletions, you may pass a file ID:
```


1Files::assertDeleted('file-id');




2Files::assertNotDeleted('file-id');




3Files::assertNothingDeleted();




Files::assertDeleted('file-id');
Files::assertNotDeleted('file-id');
Files::assertNothingDeleted();

```

### [Vector Stores](https://laravel.com/docs/12.x/ai-sdk#testing-vector-stores)
Vector store operations may be faked by invoking the `fake` method on the `Stores` class. Faking stores will also fake [file operations](https://laravel.com/docs/12.x/ai-sdk#files) automatically:
```


1use Laravel\Ai\Stores;




2 



3Stores::fake();




use Laravel\Ai\Stores;

Stores::fake();

```

Once store operations have been faked, you may make assertions about the stores that were created or deleted:
```


 1use Laravel\Ai\Stores;




 2 



 3// Create store...




 4$store = Stores::create('Knowledge Base');




 5 



 6// Make assertions...




 7Stores::assertCreated('Knowledge Base');




 8 



 9Stores::assertCreated(fn (string $name, ?string $description) =>




10    $name === 'Knowledge Base'




11);




12 



13Stores::assertNotCreated('Other Store');




14 



15Stores::assertNothingCreated();




use Laravel\Ai\Stores;

// Create store...
$store = Stores::create('Knowledge Base');

// Make assertions...
Stores::assertCreated('Knowledge Base');

Stores::assertCreated(fn (string $name, ?string $description) =>
    $name === 'Knowledge Base'
);

Stores::assertNotCreated('Other Store');

Stores::assertNothingCreated();

```

For asserting against store deletions, you may provide the store ID:
```


1Stores::assertDeleted('store_id');




2Stores::assertNotDeleted('other_store_id');




3Stores::assertNothingDeleted();




Stores::assertDeleted('store_id');
Stores::assertNotDeleted('other_store_id');
Stores::assertNothingDeleted();

```

To assert files were added or removed from a store, use the assertion methods on a given `Store` instance:
```


 1Stores::fake();




 2 



 3$store = Stores::get('store_id');




 4 



 5// Add / remove files...




 6$store->add('added_id');




 7$store->remove('removed_id');




 8 



 9// Make assertions...




10$store->assertAdded('added_id');




11$store->assertRemoved('removed_id');




12 



13$store->assertNotAdded('other_file_id');




14$store->assertNotRemoved('other_file_id');




Stores::fake();

$store = Stores::get('store_id');

// Add / remove files...
$store->add('added_id');
$store->remove('removed_id');

// Make assertions...
$store->assertAdded('added_id');
$store->assertRemoved('removed_id');

$store->assertNotAdded('other_file_id');
$store->assertNotRemoved('other_file_id');

```

If a file is stored in the provider's [file storage](https://laravel.com/docs/12.x/ai-sdk#files) and added to a vector store in the same request, you may not know the file's provider ID. In this case, you can pass a closure to the `assertAdded` method to assert against the content of the added file:
```


1use Laravel\Ai\Contracts\Files\StorableFile;




2use Laravel\Ai\Files\Document;




3 



4$store->add(Document::fromString('Hello, World!', 'text/plain')->as('hello.txt'));




5 



6$store->assertAdded(fn (StorableFile $file) => $file->name() === 'hello.txt');




7$store->assertAdded(fn (StorableFile $file) => $file->content() === 'Hello, World!');




use Laravel\Ai\Contracts\Files\StorableFile;
use Laravel\Ai\Files\Document;

$store->add(Document::fromString('Hello, World!', 'text/plain')->as('hello.txt'));

$store->assertAdded(fn (StorableFile $file) => $file->name() === 'hello.txt');
$store->assertAdded(fn (StorableFile $file) => $file->content() === 'Hello, World!');

```
