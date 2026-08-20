## [Pruning Models](https://laravel.com/docs/12.x/eloquent#pruning-models)
Sometimes you may want to periodically delete models that are no longer needed. To accomplish this, you may add the `Illuminate\Database\Eloquent\Prunable` or `Illuminate\Database\Eloquent\MassPrunable` trait to the models you would like to periodically prune. After adding one of the traits to the model, implement a `prunable` method which returns an Eloquent query builder that resolves the models that are no longer needed:
```


 1<?php




 2 



 3namespace App\Models;




 4 



 5use Illuminate\Database\Eloquent\Builder;




 6use Illuminate\Database\Eloquent\Model;




 7use Illuminate\Database\Eloquent\Prunable;




 8 



 9class Flight extends Model




10{




11    use Prunable;




12 



13    /**




14     * Get the prunable model query.




15     */




16    public function prunable(): Builder




17    {




18        return static::where('created_at', '<=', now()->minus(months: 1));




19    }




20}




<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Builder;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Prunable;

class Flight extends Model
{
    use Prunable;

    /**
     * Get the prunable model query.
     */
    public function prunable(): Builder
    {
        return static::where('created_at', '<=', now()->minus(months: 1));
    }
}

```

When marking models as `Prunable`, you may also define a `pruning` method on the model. This method will be called before the model is deleted. This method can be useful for deleting any additional resources associated with the model, such as stored files, before the model is permanently removed from the database:
```


1/**




2 * Prepare the model for pruning.




3 */




4protected function pruning(): void




5{




6    // ...




7}




/**
 * Prepare the model for pruning.
 */
protected function pruning(): void
{
    // ...
}

```

After configuring your prunable model, you should schedule the `model:prune` Artisan command in your application's `routes/console.php` file. You are free to choose the appropriate interval at which this command should be run:
```


1use Illuminate\Support\Facades\Schedule;




2 



3Schedule::command('model:prune')->daily();




use Illuminate\Support\Facades\Schedule;

Schedule::command('model:prune')->daily();

```

Behind the scenes, the `model:prune` command will automatically detect "Prunable" models within your application's `app/Models` directory. If your models are in a different location, you may use the `--model` option to specify the model class names:
```


1Schedule::command('model:prune', [




2    '--model' => [Address::class, Flight::class],




3])->daily();




Schedule::command('model:prune', [
    '--model' => [Address::class, Flight::class],
])->daily();

```

If you wish to exclude certain models from being pruned while pruning all other detected models, you may use the `--except` option:
```


1Schedule::command('model:prune', [




2    '--except' => [Address::class, Flight::class],




3])->daily();




Schedule::command('model:prune', [
    '--except' => [Address::class, Flight::class],
])->daily();

```

You may test your `prunable` query by executing the `model:prune` command with the `--pretend` option. When pretending, the `model:prune` command will simply report how many records would be pruned if the command were to actually run:
```


1php artisan model:prune --pretend




php artisan model:prune --pretend

```

Soft deleting models will be permanently deleted (`forceDelete`) if they match the prunable query.
#### [Mass Pruning](https://laravel.com/docs/12.x/eloquent#mass-pruning)
When models are marked with the `Illuminate\Database\Eloquent\MassPrunable` trait, models are deleted from the database using mass-deletion queries. Therefore, the `pruning` method will not be invoked, nor will the `deleting` and `deleted` model events be dispatched. This is because the models are never actually retrieved before deletion, thus making the pruning process much more efficient:
```


 1<?php




 2 



 3namespace App\Models;




 4 



 5use Illuminate\Database\Eloquent\Builder;




 6use Illuminate\Database\Eloquent\Model;




 7use Illuminate\Database\Eloquent\MassPrunable;




 8 



 9class Flight extends Model




10{




11    use MassPrunable;




12 



13    /**




14     * Get the prunable model query.




15     */




16    public function prunable(): Builder




17    {




18        return static::where('created_at', '<=', now()->minus(months: 1));




19    }




20}




<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Builder;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\MassPrunable;

class Flight extends Model
{
    use MassPrunable;

    /**
     * Get the prunable model query.
     */
    public function prunable(): Builder
    {
        return static::where('created_at', '<=', now()->minus(months: 1));
    }
}

```
