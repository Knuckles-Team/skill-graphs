## [Transcriptions](https://laravel.com/docs/12.x/ai-sdk#transcription)
The `Laravel\Ai\Transcription` class may be used to generate a transcript of the given audio:
```


1use Laravel\Ai\Transcription;




2 



3$transcript = Transcription::fromPath('/home/laravel/audio.mp3')->generate();




4$transcript = Transcription::fromStorage('audio.mp3')->generate();




5$transcript = Transcription::fromUpload($request->file('audio'))->generate();




6 



7return (string) $transcript;




use Laravel\Ai\Transcription;

$transcript = Transcription::fromPath('/home/laravel/audio.mp3')->generate();
$transcript = Transcription::fromStorage('audio.mp3')->generate();
$transcript = Transcription::fromUpload($request->file('audio'))->generate();

return (string) $transcript;

```

The `diarize` method may be used to indicate you would like the response to include the diarized transcript in addition to the raw text transcript, allowing you to access the segmented transcript by speaker:
```


1$transcript = Transcription::fromStorage('audio.mp3')




2    ->diarize()




3    ->generate();




$transcript = Transcription::fromStorage('audio.mp3')
    ->diarize()
    ->generate();

```

Transcription generation may also be queued:
```


1use Laravel\Ai\Transcription;




2use Laravel\Ai\Responses\TranscriptionResponse;




3 



4Transcription::fromStorage('audio.mp3')




5    ->queue()




6    ->then(function (TranscriptionResponse $transcript) {




7        // ...




8    });




use Laravel\Ai\Transcription;
use Laravel\Ai\Responses\TranscriptionResponse;

Transcription::fromStorage('audio.mp3')
    ->queue()
    ->then(function (TranscriptionResponse $transcript) {
        // ...
    });

```
