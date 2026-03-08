## [Configuration](https://laravel.com/docs/12.x/filesystem#configuration)
Laravel's filesystem configuration file is located at `config/filesystems.php`. Within this file, you may configure all of your filesystem "disks". Each disk represents a particular storage driver and storage location. Example configurations for each supported driver are included in the configuration file so you can modify the configuration to reflect your storage preferences and credentials.
The `local` driver interacts with files stored locally on the server running the Laravel application, while the `sftp` storage driver is used for SSH key-based FTP. The `s3` driver is used to write to Amazon's S3 cloud storage service.
You may configure as many disks as you like and may even have multiple disks that use the same driver.
### [The Local Driver](https://laravel.com/docs/12.x/filesystem#the-local-driver)
When using the `local` driver, all file operations are relative to the `root` directory defined in your `filesystems` configuration file. By default, this value is set to the `storage/app/private` directory. Therefore, the following method would write to `storage/app/private/example.txt`:
```


1use Illuminate\Support\Facades\Storage;




2 



3Storage::disk('local')->put('example.txt', 'Contents');




use Illuminate\Support\Facades\Storage;

Storage::disk('local')->put('example.txt', 'Contents');

```

### [The Public Disk](https://laravel.com/docs/12.x/filesystem#the-public-disk)
The `public` disk included in your application's `filesystems` configuration file is intended for files that are going to be publicly accessible. By default, the `public` disk uses the `local` driver and stores its files in `storage/app/public`.
If your `public` disk uses the `local` driver and you want to make these files accessible from the web, you should create a symbolic link from source directory `storage/app/public` to target directory `public/storage`:
To create the symbolic link, you may use the `storage:link` Artisan command:
```


1php artisan storage:link




php artisan storage:link

```

Once a file has been stored and the symbolic link has been created, you can create a URL to the files using the `asset` helper:
```


1echo asset('storage/file.txt');




echo asset('storage/file.txt');

```

You may configure additional symbolic links in your `filesystems` configuration file. Each of the configured links will be created when you run the `storage:link` command:
```


1'links' => [




2    public_path('storage') => storage_path('app/public'),




3    public_path('images') => storage_path('app/images'),




4],




'links' => [
    public_path('storage') => storage_path('app/public'),
    public_path('images') => storage_path('app/images'),
],

```

The `storage:unlink` command may be used to destroy your configured symbolic links:
```


1php artisan storage:unlink




php artisan storage:unlink

```

### [Driver Prerequisites](https://laravel.com/docs/12.x/filesystem#driver-prerequisites)
#### [S3 Driver Configuration](https://laravel.com/docs/12.x/filesystem#s3-driver-configuration)
Before using the S3 driver, you will need to install the Flysystem S3 package via the Composer package manager:
```


1composer require league/flysystem-aws-s3-v3 "^3.0" --with-all-dependencies




composer require league/flysystem-aws-s3-v3 "^3.0" --with-all-dependencies

```

An S3 disk configuration array is located in your `config/filesystems.php` configuration file. Typically, you should configure your S3 information and credentials using the following environment variables which are referenced by the `config/filesystems.php` configuration file:
```


1AWS_ACCESS_KEY_ID=<your-key-id>




2AWS_SECRET_ACCESS_KEY=<your-secret-access-key>




3AWS_DEFAULT_REGION=us-east-1




4AWS_BUCKET=<your-bucket-name>




5AWS_USE_PATH_STYLE_ENDPOINT=false




AWS_ACCESS_KEY_ID=<your-key-id>
AWS_SECRET_ACCESS_KEY=<your-secret-access-key>
AWS_DEFAULT_REGION=us-east-1
AWS_BUCKET=<your-bucket-name>
AWS_USE_PATH_STYLE_ENDPOINT=false

```

For convenience, these environment variables match the naming convention used by the AWS CLI.
#### [FTP Driver Configuration](https://laravel.com/docs/12.x/filesystem#ftp-driver-configuration)
Before using the FTP driver, you will need to install the Flysystem FTP package via the Composer package manager:
```


1composer require league/flysystem-ftp "^3.0"




composer require league/flysystem-ftp "^3.0"

```

Laravel's Flysystem integrations work great with FTP; however, a sample configuration is not included with the framework's default `config/filesystems.php` configuration file. If you need to configure an FTP filesystem, you may use the configuration example below:
```


 1'ftp' => [




 2    'driver' => 'ftp',




 3    'host' => env('FTP_HOST'),




 4    'username' => env('FTP_USERNAME'),




 5    'password' => env('FTP_PASSWORD'),




 6 



 7    // Optional FTP Settings...




 8    // 'port' => env('FTP_PORT', 21),




 9    // 'root' => env('FTP_ROOT'),




10    // 'passive' => true,




11    // 'ssl' => true,




12    // 'timeout' => 30,




13],




'ftp' => [
    'driver' => 'ftp',
    'host' => env('FTP_HOST'),
    'username' => env('FTP_USERNAME'),
    'password' => env('FTP_PASSWORD'),

    // Optional FTP Settings...
    // 'port' => env('FTP_PORT', 21),
    // 'root' => env('FTP_ROOT'),
    // 'passive' => true,
    // 'ssl' => true,
    // 'timeout' => 30,
],

```

#### [SFTP Driver Configuration](https://laravel.com/docs/12.x/filesystem#sftp-driver-configuration)
Before using the SFTP driver, you will need to install the Flysystem SFTP package via the Composer package manager:
```


1composer require league/flysystem-sftp-v3 "^3.0"




composer require league/flysystem-sftp-v3 "^3.0"

```

Laravel's Flysystem integrations work great with SFTP; however, a sample configuration is not included with the framework's default `config/filesystems.php` configuration file. If you need to configure an SFTP filesystem, you may use the configuration example below:
```


 1'sftp' => [




 2    'driver' => 'sftp',




 3    'host' => env('SFTP_HOST'),




 4 



 5    // Settings for basic authentication...




 6    'username' => env('SFTP_USERNAME'),




 7    'password' => env('SFTP_PASSWORD'),




 8 



 9    // Settings for SSH key-based authentication with encryption password...




10    'privateKey' => env('SFTP_PRIVATE_KEY'),




11    'passphrase' => env('SFTP_PASSPHRASE'),




12 



13    // Settings for file / directory permissions...




14    'visibility' => 'private', // `private` = 0600, `public` = 0644




15    'directory_visibility' => 'private', // `private` = 0700, `public` = 0755




16 



17    // Optional SFTP Settings...




18    // 'hostFingerprint' => env('SFTP_HOST_FINGERPRINT'),




19    // 'maxTries' => 4,




20    // 'passphrase' => env('SFTP_PASSPHRASE'),




21    // 'port' => env('SFTP_PORT', 22),




22    // 'root' => env('SFTP_ROOT', ''),




23    // 'timeout' => 30,




24    // 'useAgent' => true,




25],




'sftp' => [
    'driver' => 'sftp',
    'host' => env('SFTP_HOST'),

    // Settings for basic authentication...
    'username' => env('SFTP_USERNAME'),
    'password' => env('SFTP_PASSWORD'),

    // Settings for SSH key-based authentication with encryption password...
    'privateKey' => env('SFTP_PRIVATE_KEY'),
    'passphrase' => env('SFTP_PASSPHRASE'),

    // Settings for file / directory permissions...
    'visibility' => 'private', // `private` = 0600, `public` = 0644
    'directory_visibility' => 'private', // `private` = 0700, `public` = 0755

    // Optional SFTP Settings...
    // 'hostFingerprint' => env('SFTP_HOST_FINGERPRINT'),
    // 'maxTries' => 4,
    // 'passphrase' => env('SFTP_PASSPHRASE'),
    // 'port' => env('SFTP_PORT', 22),
    // 'root' => env('SFTP_ROOT', ''),
    // 'timeout' => 30,
    // 'useAgent' => true,
],

```

### [Scoped and Read-Only Filesystems](https://laravel.com/docs/12.x/filesystem#scoped-and-read-only-filesystems)
Scoped disks allow you to define a filesystem where all paths are automatically prefixed with a given path prefix. Before creating a scoped filesystem disk, you will need to install an additional Flysystem package via the Composer package manager:
```


1composer require league/flysystem-path-prefixing "^3.0"




composer require league/flysystem-path-prefixing "^3.0"

```

You may create a path scoped instance of any existing filesystem disk by defining a disk that utilizes the `scoped` driver. For example, you may create a disk which scopes your existing `s3` disk to a specific path prefix, and then every file operation using your scoped disk will utilize the specified prefix:
```


1's3-videos' => [




2    'driver' => 'scoped',




3    'disk' => 's3',




4    'prefix' => 'path/to/videos',




5],




's3-videos' => [
    'driver' => 'scoped',
    'disk' => 's3',
    'prefix' => 'path/to/videos',
],

```

"Read-only" disks allow you to create filesystem disks that do not allow write operations. Before using the `read-only` configuration option, you will need to install an additional Flysystem package via the Composer package manager:
```


1composer require league/flysystem-read-only "^3.0"




composer require league/flysystem-read-only "^3.0"

```

Next, you may include the `read-only` configuration option in one or more of your disk's configuration arrays:
```


1's3-videos' => [




2    'driver' => 's3',




3    // ...




4    'read-only' => true,




5],




's3-videos' => [
    'driver' => 's3',
    // ...
    'read-only' => true,
],

```

### [Amazon S3 Compatible Filesystems](https://laravel.com/docs/12.x/filesystem#amazon-s3-compatible-filesystems)
By default, your application's `filesystems` configuration file contains a disk configuration for the `s3` disk. In addition to using this disk to interact with
Typically, after updating the disk's credentials to match the credentials of the service you are planning to use, you only need to update the value of the `endpoint` configuration option. This option's value is typically defined via the `AWS_ENDPOINT` environment variable:
```


1'endpoint' => env('AWS_ENDPOINT', 'https://rustfs:9000'),




'endpoint' => env('AWS_ENDPOINT', 'https://rustfs:9000'),

```
