## [Vector Stores](https://laravel.com/docs/12.x/ai-sdk#vector-stores)
Vector stores allow you to create searchable collections of files that can be used for retrieval-augmented generation (RAG). The `Laravel\Ai\Stores` class provides methods for creating, retrieving, and deleting vector stores:
```


 1use Laravel\Ai\Stores;




 2 



 3// Create a new vector store...




 4$store = Stores::create('Knowledge Base');




 5 



 6// Create a store with additional options...




 7$store = Stores::create(




 8    name: 'Knowledge Base',




 9    description: 'Documentation and reference materials.',




10    expiresWhenIdleFor: days(30),




11);




12 



13return $store->id;




use Laravel\Ai\Stores;

// Create a new vector store...
$store = Stores::create('Knowledge Base');

// Create a store with additional options...
$store = Stores::create(
    name: 'Knowledge Base',
    description: 'Documentation and reference materials.',
    expiresWhenIdleFor: days(30),
);

return $store->id;

```

To retrieve an existing vector store by its ID, use the `get` method:
```


1use Laravel\Ai\Stores;




2 



3$store = Stores::get('store_id');




4 



5$store->id;




6$store->name;




7$store->fileCounts;




8$store->ready;




use Laravel\Ai\Stores;

$store = Stores::get('store_id');

$store->id;
$store->name;
$store->fileCounts;
$store->ready;

```

To delete a vector store, use the `delete` method on the `Stores` class or the store instance:
```


1use Laravel\Ai\Stores;




2 



3// Delete by ID...




4Stores::delete('store_id');




5 



6// Or delete via a store instance...




7$store = Stores::get('store_id');




8 



9$store->delete();




use Laravel\Ai\Stores;

// Delete by ID...
Stores::delete('store_id');

// Or delete via a store instance...
$store = Stores::get('store_id');

$store->delete();

```

### [Adding Files to Stores](https://laravel.com/docs/12.x/ai-sdk#adding-files-to-stores)
Once you have a vector store, you may add [files](https://laravel.com/docs/12.x/ai-sdk#files) to it using the `add` method. Files added to a store are automatically indexed for semantic searching using the [file search provider tool](https://laravel.com/docs/12.x/ai-sdk#file-search):
```


 1use Laravel\Ai\Files\Document;




 2use Laravel\Ai\Stores;




 3 



 4$store = Stores::get('store_id');




 5 



 6// Add a file that has already been stored with the provider...




 7$document = $store->add('file_id');




 8$document = $store->add(Document::fromId('file_id'));




 9 



10// Or, store and add a file in one step...




11$document = $store->add(Document::fromPath('/path/to/document.pdf'));




12$document = $store->add(Document::fromStorage('manual.pdf'));




13$document = $store->add($request->file('document'));




14 



15$document->id;




16$document->fileId;




use Laravel\Ai\Files\Document;
use Laravel\Ai\Stores;

$store = Stores::get('store_id');

// Add a file that has already been stored with the provider...
$document = $store->add('file_id');
$document = $store->add(Document::fromId('file_id'));

// Or, store and add a file in one step...
$document = $store->add(Document::fromPath('/path/to/document.pdf'));
$document = $store->add(Document::fromStorage('manual.pdf'));
$document = $store->add($request->file('document'));

$document->id;
$document->fileId;

```

Typically, when adding previously stored files to vector stores, the returned document ID will match the file's previously assigned ID; however, some vector storage providers may return a new, different "document ID". Therefore, it's recommended that you always store both IDs in your database for future reference.
You may attach metadata to files when adding them to a store. This metadata can later be used to filter search results when using the [file search provider tool](https://laravel.com/docs/12.x/ai-sdk#file-search):
```


1$store->add(Document::fromPath('/path/to/document.pdf'), metadata: [




2    'author' => 'Taylor Otwell',




3    'department' => 'Engineering',




4    'year' => 2026,




5]);




$store->add(Document::fromPath('/path/to/document.pdf'), metadata: [
    'author' => 'Taylor Otwell',
    'department' => 'Engineering',
    'year' => 2026,
]);

```

To remove a file from a store, use the `remove` method:
```


1$store->remove('file_id');




$store->remove('file_id');

```

Removing a file from a vector store does not remove it from the provider's [file storage](https://laravel.com/docs/12.x/ai-sdk#files). To remove a file from the vector store and delete it permanently from file storage, use the `deleteFile` argument:
```


1$store->remove('file_abc123', deleteFile: true);




$store->remove('file_abc123', deleteFile: true);

```
