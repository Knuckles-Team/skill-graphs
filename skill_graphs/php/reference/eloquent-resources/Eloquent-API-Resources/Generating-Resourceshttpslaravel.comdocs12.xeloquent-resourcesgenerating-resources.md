## [Generating Resources](https://laravel.com/docs/12.x/eloquent-resources#generating-resources)
To generate a resource class, you may use the `make:resource` Artisan command. By default, resources will be placed in the `app/Http/Resources` directory of your application. Resources extend the `Illuminate\Http\Resources\Json\JsonResource` class:
```


1php artisan make:resource UserResource




php artisan make:resource UserResource

```

#### [Resource Collections](https://laravel.com/docs/12.x/eloquent-resources#generating-resource-collections)
In addition to generating resources that transform individual models, you may generate resources that are responsible for transforming collections of models. This allows your JSON responses to include links and other meta information that is relevant to an entire collection of a given resource.
To create a resource collection, you should use the `--collection` flag when creating the resource. Or, including the word `Collection` in the resource name will indicate to Laravel that it should create a collection resource. Collection resources extend the `Illuminate\Http\Resources\Json\ResourceCollection` class:
```


1php artisan make:resource User --collection




2 



3php artisan make:resource UserCollection




php artisan make:resource User --collection

php artisan make:resource UserCollection

```
