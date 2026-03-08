## [Obtaining Disk Instances](https://laravel.com/docs/12.x/filesystem#obtaining-disk-instances)
The `Storage` facade may be used to interact with any of your configured disks. For example, you may use the `put` method on the facade to store an avatar on the default disk. If you call methods on the `Storage` facade without first calling the `disk` method, the method will automatically be passed to the default disk:
```


1use Illuminate\Support\Facades\Storage;




2 



3Storage::put('avatars/1', $content);




use Illuminate\Support\Facades\Storage;

Storage::put('avatars/1', $content);

```

If your application interacts with multiple disks, you may use the `disk` method on the `Storage` facade to work with files on a particular disk:
```


1Storage::disk('s3')->put('avatars/1', $content);




Storage::disk('s3')->put('avatars/1', $content);

```

### [On-Demand Disks](https://laravel.com/docs/12.x/filesystem#on-demand-disks)
Sometimes you may wish to create a disk at runtime using a given configuration without that configuration actually being present in your application's `filesystems` configuration file. To accomplish this, you may pass a configuration array to the `Storage` facade's `build` method:
```


1use Illuminate\Support\Facades\Storage;




2 



3$disk = Storage::build([




4    'driver' => 'local',




5    'root' => '/path/to/root',




6]);




7 



8$disk->put('image.jpg', $content);




use Illuminate\Support\Facades\Storage;

$disk = Storage::build([
    'driver' => 'local',
    'root' => '/path/to/root',
]);

$disk->put('image.jpg', $content);

```
