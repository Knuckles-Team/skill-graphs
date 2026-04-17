## [Files](https://laravel.com/docs/12.x/ai-sdk#files)
The `Laravel\Ai\Files` class or the individual file classes may be used to store files with your AI provider for later use in conversations. This is useful for large documents or files you want to reference multiple times without re-uploading:
```


 1use Laravel\Ai\Files\Document;




 2use Laravel\Ai\Files\Image;




 3 



 4// Store a file from a local path...




 5$response = Document::fromPath('/home/laravel/document.pdf')->put();




 6$response = Image::fromPath('/home/laravel/photo.jpg')->put();




 7 



 8// Store a file that is stored on a filesystem disk...




 9$response = Document::fromStorage('document.pdf', disk: 'local')->put();




10$response = Image::fromStorage('photo.jpg', disk: 'local')->put();




11 



12// Store a file that is stored on a remote URL...




13$response = Document::fromUrl('https://example.com/document.pdf')->put();




14$response = Image::fromUrl('https://example.com/photo.jpg')->put();




15 



16return $response->id;




use Laravel\Ai\Files\Document;
use Laravel\Ai\Files\Image;

// Store a file from a local path...
$response = Document::fromPath('/home/laravel/document.pdf')->put();
$response = Image::fromPath('/home/laravel/photo.jpg')->put();

// Store a file that is stored on a filesystem disk...
$response = Document::fromStorage('document.pdf', disk: 'local')->put();
$response = Image::fromStorage('photo.jpg', disk: 'local')->put();

// Store a file that is stored on a remote URL...
$response = Document::fromUrl('https://example.com/document.pdf')->put();
$response = Image::fromUrl('https://example.com/photo.jpg')->put();

return $response->id;

```

You may also store raw content or uploaded files:
```


1use Laravel\Ai\Files;




2use Laravel\Ai\Files\Document;




3 



4// Store raw content...




5$stored = Document::fromString('Hello, World!', 'text/plain')->put();




6 



7// Store an uploaded file...




8$stored = Document::fromUpload($request->file('document'))->put();




use Laravel\Ai\Files;
use Laravel\Ai\Files\Document;

// Store raw content...
$stored = Document::fromString('Hello, World!', 'text/plain')->put();

// Store an uploaded file...
$stored = Document::fromUpload($request->file('document'))->put();

```

Once a file has been stored, you may reference the file when generating text via agents instead of re-uploading the file:
```


1use App\Ai\Agents\SalesCoach;




2use Laravel\Ai\Files;




3 



4$response = (new SalesCoach)->prompt(




5    'Analyze the attached sales transcript...'




6    attachments: [




7        Files\Document::fromId('file-id') // Attach a stored document...




8    ]




9);




use App\Ai\Agents\SalesCoach;
use Laravel\Ai\Files;

$response = (new SalesCoach)->prompt(
    'Analyze the attached sales transcript...'
    attachments: [
        Files\Document::fromId('file-id') // Attach a stored document...
    ]
);

```

To retrieve a previously stored file, use the `get` method on a file instance:
```


1use Laravel\Ai\Files\Document;




2 



3$file = Document::fromId('file-id')->get();




4 



5$file->id;




6$file->mimeType();




use Laravel\Ai\Files\Document;

$file = Document::fromId('file-id')->get();

$file->id;
$file->mimeType();

```

To delete a file from the provider, use the `delete` method:
```


1Document::fromId('file-id')->delete();




Document::fromId('file-id')->delete();

```

By default, the `Files` class uses the default AI provider configured in your application's `config/ai.php` configuration file. For most operations, you may specify a different provider using the `provider` argument:
```


1$response = Document::fromPath(




2    '/home/laravel/document.pdf'




3)->put(provider: Lab::Anthropic);




$response = Document::fromPath(
    '/home/laravel/document.pdf'
)->put(provider: Lab::Anthropic);

```

### [Using Stored Files in Conversations](https://laravel.com/docs/12.x/ai-sdk#using-stored-files-in-conversations)
Once a file has been stored with a provider, you may reference it in agent conversations using the `fromId` method on the `Document` or `Image` classes:
```


 1use App\Ai\Agents\DocumentAnalyzer;




 2use Laravel\Ai\Files;




 3use Laravel\Ai\Files\Document;




 4 



 5$stored = Document::fromPath('/path/to/report.pdf')->put();




 6 



 7$response = (new DocumentAnalyzer)->prompt(




 8    'Summarize this document.',




 9    attachments: [




10        Document::fromId($stored->id),




11    ],




12);




use App\Ai\Agents\DocumentAnalyzer;
use Laravel\Ai\Files;
use Laravel\Ai\Files\Document;

$stored = Document::fromPath('/path/to/report.pdf')->put();

$response = (new DocumentAnalyzer)->prompt(
    'Summarize this document.',
    attachments: [
        Document::fromId($stored->id),
    ],
);

```

Similarly, stored images may be referenced using the `Image` class:
```


 1use Laravel\Ai\Files;




 2use Laravel\Ai\Files\Image;




 3 



 4$stored = Image::fromPath('/path/to/photo.jpg')->put();




 5 



 6$response = (new ImageAnalyzer)->prompt(




 7    'What is in this image?',




 8    attachments: [




 9        Image::fromId($stored->id),




10    ],




11);




use Laravel\Ai\Files;
use Laravel\Ai\Files\Image;

$stored = Image::fromPath('/path/to/photo.jpg')->put();

$response = (new ImageAnalyzer)->prompt(
    'What is in this image?',
    attachments: [
        Image::fromId($stored->id),
    ],
);

```
