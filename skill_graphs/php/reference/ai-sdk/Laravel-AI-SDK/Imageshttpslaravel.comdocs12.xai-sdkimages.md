## [Images](https://laravel.com/docs/12.x/ai-sdk#images)
The `Laravel\Ai\Image` class may be used to generate images using the `openai`, `gemini`, or `xai` providers:
```


1use Laravel\Ai\Image;




2 



3$image = Image::of('A donut sitting on the kitchen counter')->generate();




4 



5$rawContent = (string) $image;




use Laravel\Ai\Image;

$image = Image::of('A donut sitting on the kitchen counter')->generate();

$rawContent = (string) $image;

```

The `square`, `portrait`, and `landscape` methods may be used to control the aspect ratio of the image, while the `quality` method may be used to guide the model on final image quality (`high`, `medium`, `low`). The `timeout` method may be used to specify the HTTP timeout in seconds:
```


1use Laravel\Ai\Image;




2 



3$image = Image::of('A donut sitting on the kitchen counter')




4    ->quality('high')




5    ->landscape()




6    ->timeout(120)




7    ->generate();




use Laravel\Ai\Image;

$image = Image::of('A donut sitting on the kitchen counter')
    ->quality('high')
    ->landscape()
    ->timeout(120)
    ->generate();

```

You may attach reference images using the `attachments` method:
```


 1use Laravel\Ai\Files;




 2use Laravel\Ai\Image;




 3 



 4$image = Image::of('Update this photo of me to be in the style of an impressionist painting.')




 5    ->attachments([




 6        Files\Image::fromStorage('photo.jpg'),




 7        // Files\Image::fromPath('/home/laravel/photo.jpg'),




 8        // Files\Image::fromUrl('https://example.com/photo.jpg'),




 9        // $request->file('photo'),




10    ])




11    ->landscape()




12    ->generate();




use Laravel\Ai\Files;
use Laravel\Ai\Image;

$image = Image::of('Update this photo of me to be in the style of an impressionist painting.')
    ->attachments([
        Files\Image::fromStorage('photo.jpg'),
        // Files\Image::fromPath('/home/laravel/photo.jpg'),
        // Files\Image::fromUrl('https://example.com/photo.jpg'),
        // $request->file('photo'),
    ])
    ->landscape()
    ->generate();

```

Generated images may be easily stored on the default disk configured in your application's `config/filesystems.php` configuration file:
```


1$image = Image::of('A donut sitting on the kitchen counter');




2 



3$path = $image->store();




4$path = $image->storeAs('image.jpg');




5$path = $image->storePublicly();




6$path = $image->storePubliclyAs('image.jpg');




$image = Image::of('A donut sitting on the kitchen counter');

$path = $image->store();
$path = $image->storeAs('image.jpg');
$path = $image->storePublicly();
$path = $image->storePubliclyAs('image.jpg');

```

Image generation may also be queued:
```


 1use Laravel\Ai\Image;




 2use Laravel\Ai\Responses\ImageResponse;




 3 



 4Image::of('A donut sitting on the kitchen counter')




 5    ->portrait()




 6    ->queue()




 7    ->then(function (ImageResponse $image) {




 8        $path = $image->store();




 9 



10        // ...




11    });




use Laravel\Ai\Image;
use Laravel\Ai\Responses\ImageResponse;

Image::of('A donut sitting on the kitchen counter')
    ->portrait()
    ->queue()
    ->then(function (ImageResponse $image) {
        $path = $image->store();

        // ...
    });

```
