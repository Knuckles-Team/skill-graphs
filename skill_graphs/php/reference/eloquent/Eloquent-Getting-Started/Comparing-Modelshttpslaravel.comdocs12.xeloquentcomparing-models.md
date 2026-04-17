## [Comparing Models](https://laravel.com/docs/12.x/eloquent#comparing-models)
Sometimes you may need to determine if two models are the "same" or not. The `is` and `isNot` methods may be used to quickly verify two models have the same primary key, table, and database connection or not:
```


1if ($post->is($anotherPost)) {




2    // ...




3}




4 



5if ($post->isNot($anotherPost)) {




6    // ...




7}




if ($post->is($anotherPost)) {
    // ...
}

if ($post->isNot($anotherPost)) {
    // ...
}

```

The `is` and `isNot` methods are also available when using the `belongsTo`, `hasOne`, `morphTo`, and `morphOne` [relationships](https://laravel.com/docs/12.x/eloquent-relationships). This method is particularly helpful when you would like to compare a related model without issuing a query to retrieve that model:
```


1if ($post->author()->is($user)) {




2    // ...




3}




if ($post->author()->is($user)) {
    // ...
}

```
