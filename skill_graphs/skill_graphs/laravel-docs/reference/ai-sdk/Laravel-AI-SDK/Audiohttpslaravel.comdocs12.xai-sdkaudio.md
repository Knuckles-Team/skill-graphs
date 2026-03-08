## [Audio](https://laravel.com/docs/12.x/ai-sdk#audio)
The `Laravel\Ai\Audio` class may be used to generate audio from the given text:
```


1use Laravel\Ai\Audio;




2 



3$audio = Audio::of('I love coding with Laravel.')->generate();




4 



5$rawContent = (string) $audio;




use Laravel\Ai\Audio;

$audio = Audio::of('I love coding with Laravel.')->generate();

$rawContent = (string) $audio;

```

The `male`, `female`, and `voice` methods may be used to determine the voice of the generated audio:
```


1$audio = Audio::of('I love coding with Laravel.')




2    ->female()




3    ->generate();




4 



5$audio = Audio::of('I love coding with Laravel.')




6    ->voice('voice-id-or-name')




7    ->generate();




$audio = Audio::of('I love coding with Laravel.')
    ->female()
    ->generate();

$audio = Audio::of('I love coding with Laravel.')
    ->voice('voice-id-or-name')
    ->generate();

```

Similarly, the `instructions` method may be used to dynamically coach the model on how the generated audio should sound:
```


1$audio = Audio::of('I love coding with Laravel.')




2    ->female()




3    ->instructions('Said like a pirate')




4    ->generate();




$audio = Audio::of('I love coding with Laravel.')
    ->female()
    ->instructions('Said like a pirate')
    ->generate();

```

Generated audio may be easily stored on the default disk configured in your application's `config/filesystems.php` configuration file:
```


1$audio = Audio::of('I love coding with Laravel.')->generate();




2 



3$path = $audio->store();




4$path = $audio->storeAs('audio.mp3');




5$path = $audio->storePublicly();




6$path = $audio->storePubliclyAs('audio.mp3');




$audio = Audio::of('I love coding with Laravel.')->generate();

$path = $audio->store();
$path = $audio->storeAs('audio.mp3');
$path = $audio->storePublicly();
$path = $audio->storePubliclyAs('audio.mp3');

```

Audio generation may also be queued:
```


 1use Laravel\Ai\Audio;




 2use Laravel\Ai\Responses\AudioResponse;




 3 



 4Audio::of('I love coding with Laravel.')




 5    ->queue()




 6    ->then(function (AudioResponse $audio) {




 7        $path = $audio->store();




 8 



 9        // ...




10    });




use Laravel\Ai\Audio;
use Laravel\Ai\Responses\AudioResponse;

Audio::of('I love coding with Laravel.')
    ->queue()
    ->then(function (AudioResponse $audio) {
        $path = $audio->store();

        // ...
    });

```
