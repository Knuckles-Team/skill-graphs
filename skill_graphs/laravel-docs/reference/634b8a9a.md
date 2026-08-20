## [Running Database Queries](https://laravel.com/docs/12.x/queries#running-database-queries)
#### [Retrieving All Rows From a Table](https://laravel.com/docs/12.x/queries#retrieving-all-rows-from-a-table)
You may use the `table` method provided by the `DB` facade to begin a query. The `table` method returns a fluent query builder instance for the given table, allowing you to chain more constraints onto the query and then finally retrieve the results of the query using the `get` method:
```


 1<?php




 2 



 3namespace App\Http\Controllers;




 4 



 5use Illuminate\Support\Facades\DB;




 6use Illuminate\View\View;




 7 



 8class UserController extends Controller




 9{




10    /**




11     * Show a list of all of the application's users.




12     */




13    public function index(): View




14    {




15        $users = DB::table('users')->get();




16 



17        return view('user.index', ['users' => $users]);




18    }




19}




<?php

namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;
use Illuminate\View\View;

class UserController extends Controller
{
    /**
     * Show a list of all of the application's users.
     */
    public function index(): View
    {
        $users = DB::table('users')->get();

        return view('user.index', ['users' => $users]);
    }
}

```

The `get` method returns an `Illuminate\Support\Collection` instance containing the results of the query where each result is an instance of the PHP `stdClass` object. You may access each column's value by accessing the column as a property of the object:
```


1use Illuminate\Support\Facades\DB;




2 



3$users = DB::table('users')->get();




4 



5foreach ($users as $user) {




6    echo $user->name;




7}




use Illuminate\Support\Facades\DB;

$users = DB::table('users')->get();

foreach ($users as $user) {
    echo $user->name;
}

```

Laravel collections provide a variety of extremely powerful methods for mapping and reducing data. For more information on Laravel collections, check out the [collection documentation](https://laravel.com/docs/12.x/collections).
#### [Retrieving a Single Row / Column From a Table](https://laravel.com/docs/12.x/queries#retrieving-a-single-row-column-from-a-table)
If you just need to retrieve a single row from a database table, you may use the `DB` facade's `first` method. This method will return a single `stdClass` object:
```


1$user = DB::table('users')->where('name', 'John')->first();




2 



3return $user->email;




$user = DB::table('users')->where('name', 'John')->first();

return $user->email;

```

If you would like to retrieve a single row from a database table, but throw an `Illuminate\Database\RecordNotFoundException` if no matching row is found, you may use the `firstOrFail` method. If the `RecordNotFoundException` is not caught, a 404 HTTP response is automatically sent back to the client:
```


1$user = DB::table('users')->where('name', 'John')->firstOrFail();




$user = DB::table('users')->where('name', 'John')->firstOrFail();

```

If you don't need an entire row, you may extract a single value from a record using the `value` method. This method will return the value of the column directly:
```


1$email = DB::table('users')->where('name', 'John')->value('email');




$email = DB::table('users')->where('name', 'John')->value('email');

```

To retrieve a single row by its `id` column value, use the `find` method:
```


1$user = DB::table('users')->find(3);




$user = DB::table('users')->find(3);

```

#### [Retrieving a List of Column Values](https://laravel.com/docs/12.x/queries#retrieving-a-list-of-column-values)
If you would like to retrieve an `Illuminate\Support\Collection` instance containing the values of a single column, you may use the `pluck` method. In this example, we'll retrieve a collection of user titles:
```


1use Illuminate\Support\Facades\DB;




2 



3$titles = DB::table('users')->pluck('title');




4 



5foreach ($titles as $title) {




6    echo $title;




7}




use Illuminate\Support\Facades\DB;

$titles = DB::table('users')->pluck('title');

foreach ($titles as $title) {
    echo $title;
}

```

You may specify the column that the resulting collection should use as its keys by providing a second argument to the `pluck` method:
```


1$titles = DB::table('users')->pluck('title', 'name');




2 



3foreach ($titles as $name => $title) {




4    echo $title;




5}




$titles = DB::table('users')->pluck('title', 'name');

foreach ($titles as $name => $title) {
    echo $title;
}

```

### [Chunking Results](https://laravel.com/docs/12.x/queries#chunking-results)
If you need to work with thousands of database records, consider using the `chunk` method provided by the `DB` facade. This method retrieves a small chunk of results at a time and feeds each chunk into a closure for processing. For example, let's retrieve the entire `users` table in chunks of 100 records at a time:
```


1use Illuminate\Support\Collection;




2use Illuminate\Support\Facades\DB;




3 



4DB::table('users')->orderBy('id')->chunk(100, function (Collection $users) {




5    foreach ($users as $user) {




6        // ...




7    }




8});




use Illuminate\Support\Collection;
use Illuminate\Support\Facades\DB;

DB::table('users')->orderBy('id')->chunk(100, function (Collection $users) {
    foreach ($users as $user) {
        // ...
    }
});

```

You may stop further chunks from being processed by returning `false` from the closure:
```


1DB::table('users')->orderBy('id')->chunk(100, function (Collection $users) {




2    // Process the records...




3 



4    return false;




5});




DB::table('users')->orderBy('id')->chunk(100, function (Collection $users) {
    // Process the records...

    return false;
});

```

If you are updating database records while chunking results, your chunk results could change in unexpected ways. If you plan to update the retrieved records while chunking, it is always best to use the `chunkById` method instead. This method will automatically paginate the results based on the record's primary key:
```


1DB::table('users')->where('active', false)




2    ->chunkById(100, function (Collection $users) {




3        foreach ($users as $user) {




4            DB::table('users')




5                ->where('id', $user->id)




6                ->update(['active' => true]);




7        }




8    });




DB::table('users')->where('active', false)
    ->chunkById(100, function (Collection $users) {
        foreach ($users as $user) {
            DB::table('users')
                ->where('id', $user->id)
                ->update(['active' => true]);
        }
    });

```

Since the `chunkById` and `lazyById` methods add their own "where" conditions to the query being executed, you should typically [logically group](https://laravel.com/docs/12.x/queries#logical-grouping) your own conditions within a closure:
```


1DB::table('users')->where(function ($query) {




2    $query->where('credits', 1)->orWhere('credits', 2);




3})->chunkById(100, function (Collection $users) {




4    foreach ($users as $user) {




5        DB::table('users')




6            ->where('id', $user->id)




7            ->update(['credits' => 3]);




8    }




9});




DB::table('users')->where(function ($query) {
    $query->where('credits', 1)->orWhere('credits', 2);
})->chunkById(100, function (Collection $users) {
    foreach ($users as $user) {
        DB::table('users')
            ->where('id', $user->id)
            ->update(['credits' => 3]);
    }
});

```

When updating or deleting records inside the chunk callback, any changes to the primary key or foreign keys could affect the chunk query. This could potentially result in records not being included in the chunked results.
### [Streaming Results Lazily](https://laravel.com/docs/12.x/queries#streaming-results-lazily)
The `lazy` method works similarly to [the chunk method](https://laravel.com/docs/12.x/queries#chunking-results) in the sense that it executes the query in chunks. However, instead of passing each chunk into a callback, the `lazy()` method returns a [LazyCollection](https://laravel.com/docs/12.x/collections#lazy-collections), which lets you interact with the results as a single stream:
```


1use Illuminate\Support\Facades\DB;




2 



3DB::table('users')->orderBy('id')->lazy()->each(function (object $user) {




4    // ...




5});




use Illuminate\Support\Facades\DB;

DB::table('users')->orderBy('id')->lazy()->each(function (object $user) {
    // ...
});

```

Once again, if you plan to update the retrieved records while iterating over them, it is best to use the `lazyById` or `lazyByIdDesc` methods instead. These methods will automatically paginate the results based on the record's primary key:
```


1DB::table('users')->where('active', false)




2    ->lazyById()->each(function (object $user) {




3        DB::table('users')




4            ->where('id', $user->id)




5            ->update(['active' => true]);




6    });




DB::table('users')->where('active', false)
    ->lazyById()->each(function (object $user) {
        DB::table('users')
            ->where('id', $user->id)
            ->update(['active' => true]);
    });

```

When updating or deleting records while iterating over them, any changes to the primary key or foreign keys could affect the chunk query. This could potentially result in records not being included in the results.
### [Aggregates](https://laravel.com/docs/12.x/queries#aggregates)
The query builder also provides a variety of methods for retrieving aggregate values like `count`, `max`, `min`, `avg`, and `sum`. You may call any of these methods after constructing your query:
```


1use Illuminate\Support\Facades\DB;




2 



3$users = DB::table('users')->count();




4 



5$price = DB::table('orders')->max('price');




use Illuminate\Support\Facades\DB;

$users = DB::table('users')->count();

$price = DB::table('orders')->max('price');

```

Of course, you may combine these methods with other clauses to fine-tune how your aggregate value is calculated:
```


1$price = DB::table('orders')




2    ->where('finalized', 1)




3    ->avg('price');




$price = DB::table('orders')
    ->where('finalized', 1)
    ->avg('price');

```

#### [Determining if Records Exist](https://laravel.com/docs/12.x/queries#determining-if-records-exist)
Instead of using the `count` method to determine if any records exist that match your query's constraints, you may use the `exists` and `doesntExist` methods:
```


1if (DB::table('orders')->where('finalized', 1)->exists()) {




2    // ...




3}




4 



5if (DB::table('orders')->where('finalized', 1)->doesntExist()) {




6    // ...




7}




if (DB::table('orders')->where('finalized', 1)->exists()) {
    // ...
}

if (DB::table('orders')->where('finalized', 1)->doesntExist()) {
    // ...
}

```
