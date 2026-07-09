## [Query Scopes](https://laravel.com/docs/12.x/eloquent#query-scopes)
### [Global Scopes](https://laravel.com/docs/12.x/eloquent#global-scopes)
Global scopes allow you to add constraints to all queries for a given model. Laravel's own [soft delete](https://laravel.com/docs/12.x/eloquent#soft-deleting) functionality utilizes global scopes to only retrieve "non-deleted" models from the database. Writing your own global scopes can provide a convenient, easy way to make sure every query for a given model receives certain constraints.
#### [Generating Scopes](https://laravel.com/docs/12.x/eloquent#generating-scopes)
To generate a new global scope, you may invoke the `make:scope` Artisan command, which will place the generated scope in your application's `app/Models/Scopes` directory:
```


1php artisan make:scope AncientScope




php artisan make:scope AncientScope

```

#### [Writing Global Scopes](https://laravel.com/docs/12.x/eloquent#writing-global-scopes)
Writing a global scope is simple. First, use the `make:scope` command to generate a class that implements the `Illuminate\Database\Eloquent\Scope` interface. The `Scope` interface requires you to implement one method: `apply`. The `apply` method may add `where` constraints or other types of clauses to the query as needed:
```


 1<?php




 2 



 3namespace App\Models\Scopes;




 4 



 5use Illuminate\Database\Eloquent\Builder;




 6use Illuminate\Database\Eloquent\Model;




 7use Illuminate\Database\Eloquent\Scope;




 8 



 9class AncientScope implements Scope




10{




11    /**




12     * Apply the scope to a given Eloquent query builder.




13     */




14    public function apply(Builder $builder, Model $model): void




15    {




16        $builder->where('created_at', '<', now()->minus(years: 2000));




17    }




18}




<?php

namespace App\Models\Scopes;

use Illuminate\Database\Eloquent\Builder;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Scope;

class AncientScope implements Scope
{
    /**
     * Apply the scope to a given Eloquent query builder.
     */
    public function apply(Builder $builder, Model $model): void
    {
        $builder->where('created_at', '<', now()->minus(years: 2000));
    }
}

```

If your global scope is adding columns to the select clause of the query, you should use the `addSelect` method instead of `select`. This will prevent the unintentional replacement of the query's existing select clause.
#### [Applying Global Scopes](https://laravel.com/docs/12.x/eloquent#applying-global-scopes)
To assign a global scope to a model, you may simply place the `ScopedBy` attribute on the model:
```


 1<?php




 2 



 3namespace App\Models;




 4 



 5use App\Models\Scopes\AncientScope;




 6use Illuminate\Database\Eloquent\Attributes\ScopedBy;




 7 



 8#[ScopedBy([AncientScope::class])]




 9class User extends Model




10{




11    //




12}




<?php

namespace App\Models;

use App\Models\Scopes\AncientScope;
use Illuminate\Database\Eloquent\Attributes\ScopedBy;

#[ScopedBy([AncientScope::class])]
class User extends Model
{
    //
}

```

Or, you may manually register the global scope by overriding the model's `booted` method and invoke the model's `addGlobalScope` method. The `addGlobalScope` method accepts an instance of your scope as its only argument:
```


 1<?php




 2 



 3namespace App\Models;




 4 



 5use App\Models\Scopes\AncientScope;




 6use Illuminate\Database\Eloquent\Model;




 7 



 8class User extends Model




 9{




10    /**




11     * The "booted" method of the model.




12     */




13    protected static function booted(): void




14    {




15        static::addGlobalScope(new AncientScope);




16    }




17}




<?php

namespace App\Models;

use App\Models\Scopes\AncientScope;
use Illuminate\Database\Eloquent\Model;

class User extends Model
{
    /**
     * The "booted" method of the model.
     */
    protected static function booted(): void
    {
        static::addGlobalScope(new AncientScope);
    }
}

```

After adding the scope in the example above to the `App\Models\User` model, a call to the `User::all()` method will execute the following SQL query:
```


1select * from `users` where `created_at` < 0021-02-18 00:00:00




select * from `users` where `created_at` < 0021-02-18 00:00:00

```

#### [Anonymous Global Scopes](https://laravel.com/docs/12.x/eloquent#anonymous-global-scopes)
Eloquent also allows you to define global scopes using closures, which is particularly useful for simple scopes that do not warrant a separate class of their own. When defining a global scope using a closure, you should provide a scope name of your own choosing as the first argument to the `addGlobalScope` method:
```


 1<?php




 2 



 3namespace App\Models;




 4 



 5use Illuminate\Database\Eloquent\Builder;




 6use Illuminate\Database\Eloquent\Model;




 7 



 8class User extends Model




 9{




10    /**




11     * The "booted" method of the model.




12     */




13    protected static function booted(): void




14    {




15        static::addGlobalScope('ancient', function (Builder $builder) {




16            $builder->where('created_at', '<', now()->minus(years: 2000));




17        });




18    }




19}




<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Builder;
use Illuminate\Database\Eloquent\Model;

class User extends Model
{
    /**
     * The "booted" method of the model.
     */
    protected static function booted(): void
    {
        static::addGlobalScope('ancient', function (Builder $builder) {
            $builder->where('created_at', '<', now()->minus(years: 2000));
        });
    }
}

```

#### [Removing Global Scopes](https://laravel.com/docs/12.x/eloquent#removing-global-scopes)
If you would like to remove a global scope for a given query, you may use the `withoutGlobalScope` method. This method accepts the class name of the global scope as its only argument:
```


1User::withoutGlobalScope(AncientScope::class)->get();




User::withoutGlobalScope(AncientScope::class)->get();

```

Or, if you defined the global scope using a closure, you should pass the string name that you assigned to the global scope:
```


1User::withoutGlobalScope('ancient')->get();




User::withoutGlobalScope('ancient')->get();

```

If you would like to remove several or even all of the query's global scopes, you may use the `withoutGlobalScopes` and `withoutGlobalScopesExcept` methods:
```


 1// Remove all of the global scopes...




 2User::withoutGlobalScopes()->get();




 3 



 4// Remove some of the global scopes...




 5User::withoutGlobalScopes([




 6    FirstScope::class, SecondScope::class




 7])->get();




 8 



 9// Remove all global scopes except the given ones...




10User::withoutGlobalScopesExcept([




11    SecondScope::class,




12])->get();




// Remove all of the global scopes...
User::withoutGlobalScopes()->get();

// Remove some of the global scopes...
User::withoutGlobalScopes([
    FirstScope::class, SecondScope::class
])->get();

// Remove all global scopes except the given ones...
User::withoutGlobalScopesExcept([
    SecondScope::class,
])->get();

```

### [Local Scopes](https://laravel.com/docs/12.x/eloquent#local-scopes)
Local scopes allow you to define common sets of query constraints that you may easily reuse throughout your application. For example, you may need to frequently retrieve all users that are considered "popular". To define a scope, add the `Scope` attribute to an Eloquent method.
Scopes should always return the same query builder instance or `void`:
```


 1<?php




 2 



 3namespace App\Models;




 4 



 5use Illuminate\Database\Eloquent\Attributes\Scope;




 6use Illuminate\Database\Eloquent\Builder;




 7use Illuminate\Database\Eloquent\Model;




 8 



 9class User extends Model




10{




11    /**




12     * Scope a query to only include popular users.




13     */




14    #[Scope]




15    protected function popular(Builder $query): void




16    {




17        $query->where('votes', '>', 100);




18    }




19 



20    /**




21     * Scope a query to only include active users.




22     */




23    #[Scope]




24    protected function active(Builder $query): void




25    {




26        $query->where('active', 1);




27    }




28}




<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Attributes\Scope;
use Illuminate\Database\Eloquent\Builder;
use Illuminate\Database\Eloquent\Model;

class User extends Model
{
    /**
     * Scope a query to only include popular users.
     */
    #[Scope]
    protected function popular(Builder $query): void
    {
        $query->where('votes', '>', 100);
    }

    /**
     * Scope a query to only include active users.
     */
    #[Scope]
    protected function active(Builder $query): void
    {
        $query->where('active', 1);
    }
}

```

#### [Utilizing a Local Scope](https://laravel.com/docs/12.x/eloquent#utilizing-a-local-scope)
Once the scope has been defined, you may call the scope methods when querying the model. You can even chain calls to various scopes:
```


1use App\Models\User;




2 



3$users = User::popular()->active()->orderBy('created_at')->get();




use App\Models\User;

$users = User::popular()->active()->orderBy('created_at')->get();

```

Combining multiple Eloquent model scopes via an `or` query operator may require the use of closures to achieve the correct [logical grouping](https://laravel.com/docs/12.x/queries#logical-grouping):
```


1$users = User::popular()->orWhere(function (Builder $query) {




2    $query->active();




3})->get();




$users = User::popular()->orWhere(function (Builder $query) {
    $query->active();
})->get();

```

However, since this can be cumbersome, Laravel provides a "higher order" `orWhere` method that allows you to fluently chain scopes together without the use of closures:
```


1$users = User::popular()->orWhere->active()->get();




$users = User::popular()->orWhere->active()->get();

```

#### [Dynamic Scopes](https://laravel.com/docs/12.x/eloquent#dynamic-scopes)
Sometimes you may wish to define a scope that accepts parameters. To get started, just add your additional parameters to your scope method's signature. Scope parameters should be defined after the `$query` parameter:
```


 1<?php




 2 



 3namespace App\Models;




 4 



 5use Illuminate\Database\Eloquent\Attributes\Scope;




 6use Illuminate\Database\Eloquent\Builder;




 7use Illuminate\Database\Eloquent\Model;




 8 



 9class User extends Model




10{




11    /**




12     * Scope a query to only include users of a given type.




13     */




14    #[Scope]




15    protected function ofType(Builder $query, string $type): void




16    {




17        $query->where('type', $type);




18    }




19}




<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Attributes\Scope;
use Illuminate\Database\Eloquent\Builder;
use Illuminate\Database\Eloquent\Model;

class User extends Model
{
    /**
     * Scope a query to only include users of a given type.
     */
    #[Scope]
    protected function ofType(Builder $query, string $type): void
    {
        $query->where('type', $type);
    }
}

```

Once the expected arguments have been added to your scope method's signature, you may pass the arguments when calling the scope:
```


1$users = User::ofType('admin')->get();




$users = User::ofType('admin')->get();

```

### [Pending Attributes](https://laravel.com/docs/12.x/eloquent#pending-attributes)
If you would like to use scopes to create models that have the same attributes as those used to constrain the scope, you may use the `withAttributes` method when building the scope query:
```


 1<?php




 2 



 3namespace App\Models;




 4 



 5use Illuminate\Database\Eloquent\Attributes\Scope;




 6use Illuminate\Database\Eloquent\Builder;




 7use Illuminate\Database\Eloquent\Model;




 8 



 9class Post extends Model




10{




11    /**




12     * Scope the query to only include drafts.




13     */




14    #[Scope]




15    protected function draft(Builder $query): void




16    {




17        $query->withAttributes([




18            'hidden' => true,




19        ]);




20    }




21}




<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Attributes\Scope;
use Illuminate\Database\Eloquent\Builder;
use Illuminate\Database\Eloquent\Model;

class Post extends Model
{
    /**
     * Scope the query to only include drafts.
     */
    #[Scope]
    protected function draft(Builder $query): void
    {
        $query->withAttributes([
            'hidden' => true,
        ]);
    }
}

```

The `withAttributes` method will add `where` conditions to the query using the given attributes, and it will also add the given attributes to any models created via the scope:
```


1$draft = Post::draft()->create(['title' => 'In Progress']);




2 



3$draft->hidden; // true




$draft = Post::draft()->create(['title' => 'In Progress']);

$draft->hidden; // true

```

To instruct the `withAttributes` method to not add `where` conditions to the query, you may set the `asConditions` argument to `false`:
```


1$query->withAttributes([




2    'hidden' => true,




3], asConditions: false);




$query->withAttributes([
    'hidden' => true,
], asConditions: false);

```
