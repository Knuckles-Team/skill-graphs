## [Storing Files](https://laravel.com/docs/12.x/filesystem#storing-files)
The `put` method may be used to store file contents on a disk. You may also pass a PHP `resource` to the `put` method, which will use Flysystem's underlying stream support. Remember, all file paths should be specified relative to the "root" location configured for the disk:
```


1use Illuminate\Support\Facades\Storage;




2 



3Storage::put('file.jpg', $contents);




4 



5Storage::put('file.jpg', $resource);




use Illuminate\Support\Facades\Storage;

Storage::put('file.jpg', $contents);

Storage::put('file.jpg', $resource);

```

#### [Failed Writes](https://laravel.com/docs/12.x/filesystem#failed-writes)
If the `put` method (or other "write" operations) is unable to write the file to disk, `false` will be returned:
```


1if (! Storage::put('file.jpg', $contents)) {




2    // The file could not be written to disk...




3}




if (! Storage::put('file.jpg', $contents)) {
    // The file could not be written to disk...
}

```

If you wish, you may define the `throw` option within your filesystem disk's configuration array. When this option is defined as `true`, "write" methods such as `put` will throw an instance of `League\Flysystem\UnableToWriteFile` when write operations fail:
```


1'public' => [




2    'driver' => 'local',




3    // ...




4    'throw' => true,




5],




'public' => [
    'driver' => 'local',
    // ...
    'throw' => true,
],

```

### [Prepending and Appending To Files](https://laravel.com/docs/12.x/filesystem#prepending-appending-to-files)
The `prepend` and `append` methods allow you to write to the beginning or end of a file:
```


1Storage::prepend('file.log', 'Prepended Text');




2 



3Storage::append('file.log', 'Appended Text');




Storage::prepend('file.log', 'Prepended Text');

Storage::append('file.log', 'Appended Text');

```

### [Copying and Moving Files](https://laravel.com/docs/12.x/filesystem#copying-moving-files)
The `copy` method may be used to copy an existing file to a new location on the disk, while the `move` method may be used to rename or move an existing file to a new location:
```


1Storage::copy('old/file.jpg', 'new/file.jpg');




2 



3Storage::move('old/file.jpg', 'new/file.jpg');




Storage::copy('old/file.jpg', 'new/file.jpg');

Storage::move('old/file.jpg', 'new/file.jpg');

```

### [Automatic Streaming](https://laravel.com/docs/12.x/filesystem#automatic-streaming)
Streaming files to storage offers significantly reduced memory usage. If you would like Laravel to automatically manage streaming a given file to your storage location, you may use the `putFile` or `putFileAs` method. This method accepts either an `Illuminate\Http\File` or `Illuminate\Http\UploadedFile` instance and will automatically stream the file to your desired location:
```


1use Illuminate\Http\File;




2use Illuminate\Support\Facades\Storage;




3 



4// Automatically generate a unique ID for filename...




5$path = Storage::putFile('photos', new File('/path/to/photo'));




6 



7// Manually specify a filename...




8$path = Storage::putFileAs('photos', new File('/path/to/photo'), 'photo.jpg');




use Illuminate\Http\File;
use Illuminate\Support\Facades\Storage;

// Automatically generate a unique ID for filename...
$path = Storage::putFile('photos', new File('/path/to/photo'));

// Manually specify a filename...
$path = Storage::putFileAs('photos', new File('/path/to/photo'), 'photo.jpg');

```

There are a few important things to note about the `putFile` method. Note that we only specified a directory name and not a filename. By default, the `putFile` method will generate a unique ID to serve as the filename. The file's extension will be determined by examining the file's MIME type. The path to the file will be returned by the `putFile` method so you can store the path, including the generated filename, in your database.
The `putFile` and `putFileAs` methods also accept an argument to specify the "visibility" of the stored file. This is particularly useful if you are storing the file on a cloud disk such as Amazon S3 and would like the file to be publicly accessible via generated URLs:
```


1Storage::putFile('photos', new File('/path/to/photo'), 'public');




Storage::putFile('photos', new File('/path/to/photo'), 'public');

```

### [File Uploads](https://laravel.com/docs/12.x/filesystem#file-uploads)
In web applications, one of the most common use-cases for storing files is storing user uploaded files such as photos and documents. Laravel makes it very easy to store uploaded files using the `store` method on an uploaded file instance. Call the `store` method with the path at which you wish to store the uploaded file:
```


 1<?php




 2 



 3namespace App\Http\Controllers;




 4 



 5use Illuminate\Http\Request;




 6 



 7class UserAvatarController extends Controller




 8{




 9    /**




10     * Update the avatar for the user.




11     */




12    public function update(Request $request): string




13    {




14        $path = $request->file('avatar')->store('avatars');




15 



16        return $path;




17    }




18}




<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class UserAvatarController extends Controller
{
    /**
     * Update the avatar for the user.
     */
    public function update(Request $request): string
    {
        $path = $request->file('avatar')->store('avatars');

        return $path;
    }
}

```

There are a few important things to note about this example. Note that we only specified a directory name, not a filename. By default, the `store` method will generate a unique ID to serve as the filename. The file's extension will be determined by examining the file's MIME type. The path to the file will be returned by the `store` method so you can store the path, including the generated filename, in your database.
You may also call the `putFile` method on the `Storage` facade to perform the same file storage operation as the example above:
```


1$path = Storage::putFile('avatars', $request->file('avatar'));




$path = Storage::putFile('avatars', $request->file('avatar'));

```

#### [Specifying a File Name](https://laravel.com/docs/12.x/filesystem#specifying-a-file-name)
If you do not want a filename to be automatically assigned to your stored file, you may use the `storeAs` method, which receives the path, the filename, and the (optional) disk as its arguments:
```


1$path = $request->file('avatar')->storeAs(




2    'avatars', $request->user()->id




3);




$path = $request->file('avatar')->storeAs(
    'avatars', $request->user()->id
);

```

You may also use the `putFileAs` method on the `Storage` facade, which will perform the same file storage operation as the example above:
```


1$path = Storage::putFileAs(




2    'avatars', $request->file('avatar'), $request->user()->id




3);




$path = Storage::putFileAs(
    'avatars', $request->file('avatar'), $request->user()->id
);

```

Unprintable and invalid unicode characters will automatically be removed from file paths. Therefore, you may wish to sanitize your file paths before passing them to Laravel's file storage methods. File paths are normalized using the `League\Flysystem\WhitespacePathNormalizer::normalizePath` method.
#### [Specifying a Disk](https://laravel.com/docs/12.x/filesystem#specifying-a-disk)
By default, this uploaded file's `store` method will use your default disk. If you would like to specify another disk, pass the disk name as the second argument to the `store` method:
```


1$path = $request->file('avatar')->store(




2    'avatars/'.$request->user()->id, 's3'




3);




$path = $request->file('avatar')->store(
    'avatars/'.$request->user()->id, 's3'
);

```

If you are using the `storeAs` method, you may pass the disk name as the third argument to the method:
```


1$path = $request->file('avatar')->storeAs(




2    'avatars',




3    $request->user()->id,




4    's3'




5);




$path = $request->file('avatar')->storeAs(
    'avatars',
    $request->user()->id,
    's3'
);

```

#### [Other Uploaded File Information](https://laravel.com/docs/12.x/filesystem#other-uploaded-file-information)
If you would like to get the original name and extension of the uploaded file, you may do so using the `getClientOriginalName` and `getClientOriginalExtension` methods:
```


1$file = $request->file('avatar');




2 



3$name = $file->getClientOriginalName();




4$extension = $file->getClientOriginalExtension();




$file = $request->file('avatar');

$name = $file->getClientOriginalName();
$extension = $file->getClientOriginalExtension();

```

However, keep in mind that the `getClientOriginalName` and `getClientOriginalExtension` methods are considered unsafe, as the file name and extension may be tampered with by a malicious user. For this reason, you should typically prefer the `hashName` and `extension` methods to get a name and an extension for the given file upload:
```


1$file = $request->file('avatar');




2 



3$name = $file->hashName(); // Generate a unique, random name...




4$extension = $file->extension(); // Determine the file's extension based on the file's MIME type...




$file = $request->file('avatar');

$name = $file->hashName(); // Generate a unique, random name...
$extension = $file->extension(); // Determine the file's extension based on the file's MIME type...

```

### [File Visibility](https://laravel.com/docs/12.x/filesystem#file-visibility)
In Laravel's Flysystem integration, "visibility" is an abstraction of file permissions across multiple platforms. Files may either be declared `public` or `private`. When a file is declared `public`, you are indicating that the file should generally be accessible to others. For example, when using the S3 driver, you may retrieve URLs for `public` files.
You can set the visibility when writing the file via the `put` method:
```


1use Illuminate\Support\Facades\Storage;




2 



3Storage::put('file.jpg', $contents, 'public');




use Illuminate\Support\Facades\Storage;

Storage::put('file.jpg', $contents, 'public');

```

If the file has already been stored, its visibility can be retrieved and set via the `getVisibility` and `setVisibility` methods:
```


1$visibility = Storage::getVisibility('file.jpg');




2 



3Storage::setVisibility('file.jpg', 'public');




$visibility = Storage::getVisibility('file.jpg');

Storage::setVisibility('file.jpg', 'public');

```

When interacting with uploaded files, you may use the `storePublicly` and `storePubliclyAs` methods to store the uploaded file with `public` visibility:
```


1$path = $request->file('avatar')->storePublicly('avatars', 's3');




2 



3$path = $request->file('avatar')->storePubliclyAs(




4    'avatars',




5    $request->user()->id,




6    's3'




7);




$path = $request->file('avatar')->storePublicly('avatars', 's3');

$path = $request->file('avatar')->storePubliclyAs(
    'avatars',
    $request->user()->id,
    's3'
);

```

#### [Local Files and Visibility](https://laravel.com/docs/12.x/filesystem#local-files-and-visibility)
When using the `local` driver, `public` [visibility](https://laravel.com/docs/12.x/filesystem#file-visibility) translates to `0755` permissions for directories and `0644` permissions for files. You can modify the permissions mappings in your application's `filesystems` configuration file:
```


 1'local' => [




 2    'driver' => 'local',




 3    'root' => storage_path('app'),




 4    'permissions' => [




 5        'file' => [




 6            'public' => 0644,




 7            'private' => 0600,




 8        ],




 9        'dir' => [




10            'public' => 0755,




11            'private' => 0700,




12        ],




13    ],




14    'throw' => false,




15],




'local' => [
    'driver' => 'local',
    'root' => storage_path('app'),
    'permissions' => [
        'file' => [
            'public' => 0644,
            'private' => 0600,
        ],
        'dir' => [
            'public' => 0755,
            'private' => 0700,
        ],
    ],
    'throw' => false,
],

```
