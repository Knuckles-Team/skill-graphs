## [Retrieving Files](https://laravel.com/docs/12.x/filesystem#retrieving-files)
The `get` method may be used to retrieve the contents of a file. The raw string contents of the file will be returned by the method. Remember, all file paths should be specified relative to the disk's "root" location:
```


1$contents = Storage::get('file.jpg');




$contents = Storage::get('file.jpg');

```

If the file you are retrieving contains JSON, you may use the `json` method to retrieve the file and decode its contents:
```


1$orders = Storage::json('orders.json');




$orders = Storage::json('orders.json');

```

The `exists` method may be used to determine if a file exists on the disk:
```


1if (Storage::disk('s3')->exists('file.jpg')) {




2    // ...




3}




if (Storage::disk('s3')->exists('file.jpg')) {
    // ...
}

```

The `missing` method may be used to determine if a file is missing from the disk:
```


1if (Storage::disk('s3')->missing('file.jpg')) {




2    // ...




3}




if (Storage::disk('s3')->missing('file.jpg')) {
    // ...
}

```

### [Downloading Files](https://laravel.com/docs/12.x/filesystem#downloading-files)
The `download` method may be used to generate a response that forces the user's browser to download the file at the given path. The `download` method accepts a filename as the second argument to the method, which will determine the filename that is seen by the user downloading the file. Finally, you may pass an array of HTTP headers as the third argument to the method:
```


1return Storage::download('file.jpg');




2 



3return Storage::download('file.jpg', $name, $headers);




return Storage::download('file.jpg');

return Storage::download('file.jpg', $name, $headers);

```

### [File URLs](https://laravel.com/docs/12.x/filesystem#file-urls)
You may use the `url` method to get the URL for a given file. If you are using the `local` driver, this will typically just prepend `/storage` to the given path and return a relative URL to the file. If you are using the `s3` driver, the fully qualified remote URL will be returned:
```


1use Illuminate\Support\Facades\Storage;




2 



3$url = Storage::url('file.jpg');




use Illuminate\Support\Facades\Storage;

$url = Storage::url('file.jpg');

```

When using the `local` driver, all files that should be publicly accessible should be placed in the `storage/app/public` directory. Furthermore, you should [create a symbolic link](https://laravel.com/docs/12.x/filesystem#the-public-disk) at `public/storage` which points to the `storage/app/public` directory.
When using the `local` driver, the return value of `url` is not URL encoded. For this reason, we recommend always storing your files using names that will create valid URLs.
#### [URL Host Customization](https://laravel.com/docs/12.x/filesystem#url-host-customization)
If you would like to modify the host for URLs generated using the `Storage` facade, you may add or change the `url` option in the disk's configuration array:
```


1'public' => [




2    'driver' => 'local',




3    'root' => storage_path('app/public'),




4    'url' => env('APP_URL').'/storage',




5    'visibility' => 'public',




6    'throw' => false,




7],




'public' => [
    'driver' => 'local',
    'root' => storage_path('app/public'),
    'url' => env('APP_URL').'/storage',
    'visibility' => 'public',
    'throw' => false,
],

```

### [Temporary URLs](https://laravel.com/docs/12.x/filesystem#temporary-urls)
Using the `temporaryUrl` method, you may create temporary URLs to files stored using the `local` and `s3` drivers. This method accepts a path and a `DateTime` instance specifying when the URL should expire:
```


1use Illuminate\Support\Facades\Storage;




2 



3$url = Storage::temporaryUrl(




4    'file.jpg', now()->plus(minutes: 5)




5);




use Illuminate\Support\Facades\Storage;

$url = Storage::temporaryUrl(
    'file.jpg', now()->plus(minutes: 5)
);

```

#### [Enabling Local Temporary URLs](https://laravel.com/docs/12.x/filesystem#enabling-local-temporary-urls)
If you started developing your application before support for temporary URLs was introduced to the `local` driver, you may need to enable local temporary URLs. To do so, add the `serve` option to your `local` disk's configuration array within the `config/filesystems.php` configuration file:
```


1'local' => [




2    'driver' => 'local',




3    'root' => storage_path('app/private'),




4    'serve' => true,




5    'throw' => false,




6],




'local' => [
    'driver' => 'local',
    'root' => storage_path('app/private'),
    'serve' => true,
    'throw' => false,
],

```

#### [S3 Request Parameters](https://laravel.com/docs/12.x/filesystem#s3-request-parameters)
If you need to specify additional `temporaryUrl` method:
```


1$url = Storage::temporaryUrl(




2    'file.jpg',




3    now()->plus(minutes: 5),




4    [




5        'ResponseContentType' => 'application/octet-stream',




6        'ResponseContentDisposition' => 'attachment; filename=file2.jpg',




7    ]




8);




$url = Storage::temporaryUrl(
    'file.jpg',
    now()->plus(minutes: 5),
    [
        'ResponseContentType' => 'application/octet-stream',
        'ResponseContentDisposition' => 'attachment; filename=file2.jpg',
    ]
);

```

#### [Customizing Temporary URLs](https://laravel.com/docs/12.x/filesystem#customizing-temporary-urls)
If you need to customize how temporary URLs are created for a specific storage disk, you can use the `buildTemporaryUrlsUsing` method. For example, this can be useful if you have a controller that allows you to download files stored via a disk that doesn't typically support temporary URLs. Usually, this method should be called from the `boot` method of a service provider:
```


 1<?php




 2 



 3namespace App\Providers;




 4 



 5use DateTime;




 6use Illuminate\Support\Facades\Storage;




 7use Illuminate\Support\Facades\URL;




 8use Illuminate\Support\ServiceProvider;




 9 



10class AppServiceProvider extends ServiceProvider




11{




12    /**




13     * Bootstrap any application services.




14     */




15    public function boot(): void




16    {




17        Storage::disk('local')->buildTemporaryUrlsUsing(




18            function (string $path, DateTime $expiration, array $options) {




19                return URL::temporarySignedRoute(




20                    'files.download',




21                    $expiration,




22                    array_merge($options, ['path' => $path])




23                );




24            }




25        );




26    }




27}




<?php

namespace App\Providers;

use DateTime;
use Illuminate\Support\Facades\Storage;
use Illuminate\Support\Facades\URL;
use Illuminate\Support\ServiceProvider;

class AppServiceProvider extends ServiceProvider
{
    /**
     * Bootstrap any application services.
     */
    public function boot(): void
    {
        Storage::disk('local')->buildTemporaryUrlsUsing(
            function (string $path, DateTime $expiration, array $options) {
                return URL::temporarySignedRoute(
                    'files.download',
                    $expiration,
                    array_merge($options, ['path' => $path])
                );
            }
        );
    }
}

```

#### [Temporary Upload URLs](https://laravel.com/docs/12.x/filesystem#temporary-upload-urls)
The ability to generate temporary upload URLs is only supported by the `s3` and `local` drivers.
If you need to generate a temporary URL that can be used to upload a file directly from your client-side application, you may use the `temporaryUploadUrl` method. This method accepts a path and a `DateTime` instance specifying when the URL should expire. The `temporaryUploadUrl` method returns an associative array which may be destructured into the upload URL and the headers that should be included with the upload request:
```


1use Illuminate\Support\Facades\Storage;




2 



3['url' => $url, 'headers' => $headers] = Storage::temporaryUploadUrl(




4    'file.jpg', now()->plus(minutes: 5)




5);




use Illuminate\Support\Facades\Storage;

['url' => $url, 'headers' => $headers] = Storage::temporaryUploadUrl(
    'file.jpg', now()->plus(minutes: 5)
);

```

This method is primarily useful in serverless environments that require the client-side application to directly upload files to a cloud storage system such as Amazon S3.
### [File Metadata](https://laravel.com/docs/12.x/filesystem#file-metadata)
In addition to reading and writing files, Laravel can also provide information about the files themselves. For example, the `size` method may be used to get the size of a file in bytes:
```


1use Illuminate\Support\Facades\Storage;




2 



3$size = Storage::size('file.jpg');




use Illuminate\Support\Facades\Storage;

$size = Storage::size('file.jpg');

```

The `lastModified` method returns the UNIX timestamp of the last time the file was modified:
```


1$time = Storage::lastModified('file.jpg');




$time = Storage::lastModified('file.jpg');

```

The MIME type of a given file may be obtained via the `mimeType` method:
```


1$mime = Storage::mimeType('file.jpg');




$mime = Storage::mimeType('file.jpg');

```

#### [File Paths](https://laravel.com/docs/12.x/filesystem#file-paths)
You may use the `path` method to get the path for a given file. If you are using the `local` driver, this will return the absolute path to the file. If you are using the `s3` driver, this method will return the relative path to the file in the S3 bucket:
```


1use Illuminate\Support\Facades\Storage;




2 



3$path = Storage::path('file.jpg');




use Illuminate\Support\Facades\Storage;

$path = Storage::path('file.jpg');

```
