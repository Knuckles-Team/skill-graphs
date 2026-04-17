## [Creating Policies](https://laravel.com/docs/12.x/authorization#creating-policies)
### [Generating Policies](https://laravel.com/docs/12.x/authorization#generating-policies)
Policies are classes that organize authorization logic around a particular model or resource. For example, if your application is a blog, you may have an `App\Models\Post` model and a corresponding `App\Policies\PostPolicy` to authorize user actions such as creating or updating posts.
You may generate a policy using the `make:policy` Artisan command. The generated policy will be placed in the `app/Policies` directory. If this directory does not exist in your application, Laravel will create it for you:
```


1php artisan make:policy PostPolicy




php artisan make:policy PostPolicy

```

The `make:policy` command will generate an empty policy class. If you would like to generate a class with example policy methods related to viewing, creating, updating, and deleting the resource, you may provide a `--model` option when executing the command:
```


1php artisan make:policy PostPolicy --model=Post




php artisan make:policy PostPolicy --model=Post

```

### [Registering Policies](https://laravel.com/docs/12.x/authorization#registering-policies)
#### [Policy Discovery](https://laravel.com/docs/12.x/authorization#policy-discovery)
By default, Laravel automatically discover policies as long as the model and policy follow standard Laravel naming conventions. Specifically, the policies must be in a `Policies` directory at or above the directory that contains your models. So, for example, the models may be placed in the `app/Models` directory while the policies may be placed in the `app/Policies` directory. In this situation, Laravel will check for policies in `app/Models/Policies` then `app/Policies`. In addition, the policy name must match the model name and have a `Policy` suffix. So, a `User` model would correspond to a `UserPolicy` policy class.
If you would like to define your own policy discovery logic, you may register a custom policy discovery callback using the `Gate::guessPolicyNamesUsing` method. Typically, this method should be called from the `boot` method of your application's `AppServiceProvider`:
```


1use Illuminate\Support\Facades\Gate;




2 



3Gate::guessPolicyNamesUsing(function (string $modelClass) {




4    // Return the name of the policy class for the given model...




5});




use Illuminate\Support\Facades\Gate;

Gate::guessPolicyNamesUsing(function (string $modelClass) {
    // Return the name of the policy class for the given model...
});

```

#### [Manually Registering Policies](https://laravel.com/docs/12.x/authorization#manually-registering-policies)
Using the `Gate` facade, you may manually register policies and their corresponding models within the `boot` method of your application's `AppServiceProvider`:
```


 1use App\Models\Order;




 2use App\Policies\OrderPolicy;




 3use Illuminate\Support\Facades\Gate;




 4 



 5/**




 6 * Bootstrap any application services.




 7 */




 8public function boot(): void




 9{




10    Gate::policy(Order::class, OrderPolicy::class);




11}




use App\Models\Order;
use App\Policies\OrderPolicy;
use Illuminate\Support\Facades\Gate;

/**
 * Bootstrap any application services.
 */
public function boot(): void
{
    Gate::policy(Order::class, OrderPolicy::class);
}

```

Alternatively, you may place the `UsePolicy` attribute on a model class to inform Laravel of the model's corresponding policy:
```


 1<?php




 2 



 3namespace App\Models;




 4 



 5use App\Policies\OrderPolicy;




 6use Illuminate\Database\Eloquent\Attributes\UsePolicy;




 7use Illuminate\Database\Eloquent\Model;




 8 



 9#[UsePolicy(OrderPolicy::class)]




10class Order extends Model




11{




12    //




13}




<?php

namespace App\Models;

use App\Policies\OrderPolicy;
use Illuminate\Database\Eloquent\Attributes\UsePolicy;
use Illuminate\Database\Eloquent\Model;

#[UsePolicy(OrderPolicy::class)]
class Order extends Model
{
    //
}

```
