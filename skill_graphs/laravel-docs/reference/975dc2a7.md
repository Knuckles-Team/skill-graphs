## [Testing](https://laravel.com/docs/12.x/filesystem#testing)
The `Storage` facade's `fake` method allows you to easily generate a fake disk that, combined with the file generation utilities of the `Illuminate\Http\UploadedFile` class, greatly simplifies the testing of file uploads. For example:
Pest PHPUnit
```


 1<?php




 2 



 3use Illuminate\Http\UploadedFile;




 4use Illuminate\Support\Facades\Storage;




 5 



 6test('albums can be uploaded', function () {




 7    Storage::fake('photos');




 8 



 9    $response = $this->json('POST', '/photos', [




10        UploadedFile::fake()->image('photo1.jpg'),




11        UploadedFile::fake()->image('photo2.jpg')




12    ]);




13 



14    // Assert one or more files were stored...




15    Storage::disk('photos')->assertExists('photo1.jpg');




16    Storage::disk('photos')->assertExists(['photo1.jpg', 'photo2.jpg']);




17 



18    // Assert one or more files were not stored...




19    Storage::disk('photos')->assertMissing('missing.jpg');




20    Storage::disk('photos')->assertMissing(['missing.jpg', 'non-existing.jpg']);




21 



22    // Assert that the number of files in a given directory matches the expected count...




23    Storage::disk('photos')->assertCount('/wallpapers', 2);




24 



25    // Assert that a given directory is empty...




26    Storage::disk('photos')->assertDirectoryEmpty('/wallpapers');




27});




<?php

use Illuminate\Http\UploadedFile;
use Illuminate\Support\Facades\Storage;

test('albums can be uploaded', function () {
    Storage::fake('photos');

    $response = $this->json('POST', '/photos', [
        UploadedFile::fake()->image('photo1.jpg'),
        UploadedFile::fake()->image('photo2.jpg')
    ]);

    // Assert one or more files were stored...
    Storage::disk('photos')->assertExists('photo1.jpg');
    Storage::disk('photos')->assertExists(['photo1.jpg', 'photo2.jpg']);

    // Assert one or more files were not stored...
    Storage::disk('photos')->assertMissing('missing.jpg');
    Storage::disk('photos')->assertMissing(['missing.jpg', 'non-existing.jpg']);

    // Assert that the number of files in a given directory matches the expected count...
    Storage::disk('photos')->assertCount('/wallpapers', 2);

    // Assert that a given directory is empty...
    Storage::disk('photos')->assertDirectoryEmpty('/wallpapers');
});

```

```


 1<?php




 2 



 3namespace Tests\Feature;




 4 



 5use Illuminate\Http\UploadedFile;




 6use Illuminate\Support\Facades\Storage;




 7use Tests\TestCase;




 8 



 9class ExampleTest extends TestCase




10{




11    public function test_albums_can_be_uploaded(): void




12    {




13        Storage::fake('photos');




14 



15        $response = $this->json('POST', '/photos', [




16            UploadedFile::fake()->image('photo1.jpg'),




17            UploadedFile::fake()->image('photo2.jpg')




18        ]);




19 



20        // Assert one or more files were stored...




21        Storage::disk('photos')->assertExists('photo1.jpg');




22        Storage::disk('photos')->assertExists(['photo1.jpg', 'photo2.jpg']);




23 



24        // Assert one or more files were not stored...




25        Storage::disk('photos')->assertMissing('missing.jpg');




26        Storage::disk('photos')->assertMissing(['missing.jpg', 'non-existing.jpg']);




27 



28        // Assert that the number of files in a given directory matches the expected count...




29        Storage::disk('photos')->assertCount('/wallpapers', 2);




30 



31        // Assert that a given directory is empty...




32        Storage::disk('photos')->assertDirectoryEmpty('/wallpapers');




33    }




34}




<?php

namespace Tests\Feature;

use Illuminate\Http\UploadedFile;
use Illuminate\Support\Facades\Storage;
use Tests\TestCase;

class ExampleTest extends TestCase
{
    public function test_albums_can_be_uploaded(): void
    {
        Storage::fake('photos');

        $response = $this->json('POST', '/photos', [
            UploadedFile::fake()->image('photo1.jpg'),
            UploadedFile::fake()->image('photo2.jpg')
        ]);

        // Assert one or more files were stored...
        Storage::disk('photos')->assertExists('photo1.jpg');
        Storage::disk('photos')->assertExists(['photo1.jpg', 'photo2.jpg']);

        // Assert one or more files were not stored...
        Storage::disk('photos')->assertMissing('missing.jpg');
        Storage::disk('photos')->assertMissing(['missing.jpg', 'non-existing.jpg']);

        // Assert that the number of files in a given directory matches the expected count...
        Storage::disk('photos')->assertCount('/wallpapers', 2);

        // Assert that a given directory is empty...
        Storage::disk('photos')->assertDirectoryEmpty('/wallpapers');
    }
}

```

By default, the `fake` method will delete all files in its temporary directory. If you would like to keep these files, you may use the "persistentFake" method instead. For more information on testing file uploads, you may consult the [HTTP testing documentation's information on file uploads](https://laravel.com/docs/12.x/http-tests#testing-file-uploads).
The `image` method requires the
