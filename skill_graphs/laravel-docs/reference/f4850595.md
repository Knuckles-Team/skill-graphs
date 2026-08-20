## [Testing File Uploads](https://laravel.com/docs/12.x/http-tests#testing-file-uploads)
The `Illuminate\Http\UploadedFile` class provides a `fake` method which may be used to generate dummy files or images for testing. This, combined with the `Storage` facade's `fake` method, greatly simplifies the testing of file uploads. For example, you may combine these two features to easily test an avatar upload form:
Pest PHPUnit
```


 1<?php




 2 



 3use Illuminate\Http\UploadedFile;




 4use Illuminate\Support\Facades\Storage;




 5 



 6test('avatars can be uploaded', function () {




 7    Storage::fake('avatars');




 8 



 9    $file = UploadedFile::fake()->image('avatar.jpg');




10 



11    $response = $this->post('/avatar', [




12        'avatar' => $file,




13    ]);




14 



15    Storage::disk('avatars')->assertExists($file->hashName());




16});




<?php

use Illuminate\Http\UploadedFile;
use Illuminate\Support\Facades\Storage;

test('avatars can be uploaded', function () {
    Storage::fake('avatars');

    $file = UploadedFile::fake()->image('avatar.jpg');

    $response = $this->post('/avatar', [
        'avatar' => $file,
    ]);

    Storage::disk('avatars')->assertExists($file->hashName());
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




11    public function test_avatars_can_be_uploaded(): void




12    {




13        Storage::fake('avatars');




14 



15        $file = UploadedFile::fake()->image('avatar.jpg');




16 



17        $response = $this->post('/avatar', [




18            'avatar' => $file,




19        ]);




20 



21        Storage::disk('avatars')->assertExists($file->hashName());




22    }




23}




<?php

namespace Tests\Feature;

use Illuminate\Http\UploadedFile;
use Illuminate\Support\Facades\Storage;
use Tests\TestCase;

class ExampleTest extends TestCase
{
    public function test_avatars_can_be_uploaded(): void
    {
        Storage::fake('avatars');

        $file = UploadedFile::fake()->image('avatar.jpg');

        $response = $this->post('/avatar', [
            'avatar' => $file,
        ]);

        Storage::disk('avatars')->assertExists($file->hashName());
    }
}

```

If you would like to assert that a given file does not exist, you may use the `assertMissing` method provided by the `Storage` facade:
```


1Storage::fake('avatars');




2 



3// ...




4 



5Storage::disk('avatars')->assertMissing('missing.jpg');




Storage::fake('avatars');

// ...

Storage::disk('avatars')->assertMissing('missing.jpg');

```

#### [Fake File Customization](https://laravel.com/docs/12.x/http-tests#fake-file-customization)
When creating files using the `fake` method provided by the `UploadedFile` class, you may specify the width, height, and size of the image (in kilobytes) in order to better test your application's validation rules:
```


1UploadedFile::fake()->image('avatar.jpg', $width, $height)->size(100);




UploadedFile::fake()->image('avatar.jpg', $width, $height)->size(100);

```

In addition to creating images, you may create files of any other type using the `create` method:
```


1UploadedFile::fake()->create('document.pdf', $sizeInKilobytes);




UploadedFile::fake()->create('document.pdf', $sizeInKilobytes);

```

If needed, you may pass a `$mimeType` argument to the method to explicitly define the MIME type that should be returned by the file:
```


1UploadedFile::fake()->create(




2    'document.pdf', $sizeInKilobytes, 'application/pdf'




3);




UploadedFile::fake()->create(
    'document.pdf', $sizeInKilobytes, 'application/pdf'
);

```
