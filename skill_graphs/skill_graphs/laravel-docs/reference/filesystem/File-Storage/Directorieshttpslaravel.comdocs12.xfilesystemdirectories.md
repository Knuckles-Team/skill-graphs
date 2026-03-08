## [Directories](https://laravel.com/docs/12.x/filesystem#directories)
#### [Get All Files Within a Directory](https://laravel.com/docs/12.x/filesystem#get-all-files-within-a-directory)
The `files` method returns an array of all files within a given directory. If you would like to retrieve a list of all files within a given directory including subdirectories, you may use the `allFiles` method:
```


1use Illuminate\Support\Facades\Storage;




2 



3$files = Storage::files($directory);




4 



5$files = Storage::allFiles($directory);




use Illuminate\Support\Facades\Storage;

$files = Storage::files($directory);

$files = Storage::allFiles($directory);

```

#### [Get All Directories Within a Directory](https://laravel.com/docs/12.x/filesystem#get-all-directories-within-a-directory)
The `directories` method returns an array of all directories within a given directory. If you would like to retrieve a list of all directories within a given directory including subdirectories, you may use the `allDirectories` method:
```


1$directories = Storage::directories($directory);




2 



3$directories = Storage::allDirectories($directory);




$directories = Storage::directories($directory);

$directories = Storage::allDirectories($directory);

```

#### [Create a Directory](https://laravel.com/docs/12.x/filesystem#create-a-directory)
The `makeDirectory` method will create the given directory, including any needed subdirectories:
```


1Storage::makeDirectory($directory);




Storage::makeDirectory($directory);

```

#### [Delete a Directory](https://laravel.com/docs/12.x/filesystem#delete-a-directory)
Finally, the `deleteDirectory` method may be used to remove a directory and all of its files:
```


1Storage::deleteDirectory($directory);




Storage::deleteDirectory($directory);

```
