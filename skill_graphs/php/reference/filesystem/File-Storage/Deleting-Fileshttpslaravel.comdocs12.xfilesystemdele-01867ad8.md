## [Deleting Files](https://laravel.com/docs/12.x/filesystem#deleting-files)
The `delete` method accepts a single filename or an array of files to delete:
```


1use Illuminate\Support\Facades\Storage;




2 



3Storage::delete('file.jpg');




4 



5Storage::delete(['file.jpg', 'file2.jpg']);




use Illuminate\Support\Facades\Storage;

Storage::delete('file.jpg');

Storage::delete(['file.jpg', 'file2.jpg']);

```

If necessary, you may specify the disk that the file should be deleted from:
```


1use Illuminate\Support\Facades\Storage;




2 



3Storage::disk('s3')->delete('path/file.jpg');




use Illuminate\Support\Facades\Storage;

Storage::disk('s3')->delete('path/file.jpg');

```
