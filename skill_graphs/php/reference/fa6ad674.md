## [Reusable Query Components](https://laravel.com/docs/12.x/queries#reusable-query-components)
If you have repeated query logic throughout your application, you may extract the logic into reusable objects using the query builder's `tap` and `pipe` methods. Imagine you have these two different queries in your application:
```


 1use Illuminate\Database\Query\Builder;




 2use Illuminate\Support\Facades\DB;




 3 



 4$destination = $request->query('destination');




 5 



 6DB::table('flights')




 7    ->when($destination, function (Builder $query, string $destination) {




 8        $query->where('destination', $destination);




 9    })




10    ->orderByDesc('price')




11    ->get();




12 



13// ...




14 



15$destination = $request->query('destination');




16 



17DB::table('flights')




18    ->when($destination, function (Builder $query, string $destination) {




19        $query->where('destination', $destination);




20    })




21    ->where('user', $request->user()->id)




22    ->orderBy('destination')




23    ->get();




use Illuminate\Database\Query\Builder;
use Illuminate\Support\Facades\DB;

$destination = $request->query('destination');

DB::table('flights')
    ->when($destination, function (Builder $query, string $destination) {
        $query->where('destination', $destination);
    })
    ->orderByDesc('price')
    ->get();

// ...

$destination = $request->query('destination');

DB::table('flights')
    ->when($destination, function (Builder $query, string $destination) {
        $query->where('destination', $destination);
    })
    ->where('user', $request->user()->id)
    ->orderBy('destination')
    ->get();

```

You may like to extract the destination filtering that is common between the queries into a reusable object:
```


 1<?php




 2 



 3namespace App\Scopes;




 4 



 5use Illuminate\Database\Query\Builder;




 6 



 7class DestinationFilter




 8{




 9    public function __construct(




10        private ?string $destination,




11    ) {




12        //




13    }




14 



15    public function __invoke(Builder $query): void




16    {




17        $query->when($this->destination, function (Builder $query) {




18            $query->where('destination', $this->destination);




19        });




20    }




21}




<?php

namespace App\Scopes;

use Illuminate\Database\Query\Builder;

class DestinationFilter
{
    public function __construct(
        private ?string $destination,
    ) {
        //
    }

    public function __invoke(Builder $query): void
    {
        $query->when($this->destination, function (Builder $query) {
            $query->where('destination', $this->destination);
        });
    }
}

```

Then, you can use the query builder's `tap` method to apply the object's logic to the query:
```


 1use App\Scopes\DestinationFilter;




 2use Illuminate\Database\Query\Builder;




 3use Illuminate\Support\Facades\DB;




 4 



 5DB::table('flights')




 6    ->when($destination, function (Builder $query, string $destination) {




 7        $query->where('destination', $destination);




 8    })




 9    ->tap(new DestinationFilter($destination))




10    ->orderByDesc('price')




11    ->get();




12 



13// ...




14 



15DB::table('flights')




16    ->when($destination, function (Builder $query, string $destination) {




17        $query->where('destination', $destination);




18    })




19    ->tap(new DestinationFilter($destination))




20    ->where('user', $request->user()->id)




21    ->orderBy('destination')




22    ->get();




use App\Scopes\DestinationFilter;
use Illuminate\Database\Query\Builder;
use Illuminate\Support\Facades\DB;

DB::table('flights')
    ->when($destination, function (Builder $query, string $destination) {
        $query->where('destination', $destination);
    })
    ->tap(new DestinationFilter($destination))
    ->orderByDesc('price')
    ->get();

// ...

DB::table('flights')
    ->when($destination, function (Builder $query, string $destination) {
        $query->where('destination', $destination);
    })
    ->tap(new DestinationFilter($destination))
    ->where('user', $request->user()->id)
    ->orderBy('destination')
    ->get();

```

#### [Query Pipes](https://laravel.com/docs/12.x/queries#query-pipes)
The `tap` method will always return the query builder. If you would like to extract an object that executes the query and returns another value, you may use the `pipe` method instead.
Consider the following query object that contains shared [pagination](https://laravel.com/docs/12.x/pagination) logic used throughout an application. Unlike the `DestinationFilter`, which applies query conditions to the query, the `Paginate` object executes the query and returns a paginator instance:
```


 1<?php




 2 



 3namespace App\Scopes;




 4 



 5use Illuminate\Contracts\Pagination\LengthAwarePaginator;




 6use Illuminate\Database\Query\Builder;




 7 



 8class Paginate




 9{




10    public function __construct(




11        private string $sortBy = 'timestamp',




12        private string $sortDirection = 'desc',




13        private int $perPage = 25,




14    ) {




15        //




16    }




17 



18    public function __invoke(Builder $query): LengthAwarePaginator




19    {




20        return $query->orderBy($this->sortBy, $this->sortDirection)




21            ->paginate($this->perPage, pageName: 'p');




22    }




23}




<?php

namespace App\Scopes;

use Illuminate\Contracts\Pagination\LengthAwarePaginator;
use Illuminate\Database\Query\Builder;

class Paginate
{
    public function __construct(
        private string $sortBy = 'timestamp',
        private string $sortDirection = 'desc',
        private int $perPage = 25,
    ) {
        //
    }

    public function __invoke(Builder $query): LengthAwarePaginator
    {
        return $query->orderBy($this->sortBy, $this->sortDirection)
            ->paginate($this->perPage, pageName: 'p');
    }
}

```

Using the query builder's `pipe` method, we can leverage this object to apply our shared pagination logic:
```


1$flights = DB::table('flights')




2    ->tap(new DestinationFilter($destination))




3    ->pipe(new Paginate);




$flights = DB::table('flights')
    ->tap(new DestinationFilter($destination))
    ->pipe(new Paginate);

```
