## [Generating Model Classes](https://laravel.com/docs/12.x/eloquent#generating-model-classes)
To get started, let's create an Eloquent model. Models typically live in the `app\Models` directory and extend the `Illuminate\Database\Eloquent\Model` class. You may use the `make:model` [Artisan command](https://laravel.com/docs/12.x/artisan) to generate a new model:
```


1php artisan make:model Flight




php artisan make:model Flight

```

If you would like to generate a [database migration](https://laravel.com/docs/12.x/migrations) when you generate the model, you may use the `--migration` or `-m` option:
```


1php artisan make:model Flight --migration




php artisan make:model Flight --migration

```

You may generate various other types of classes when generating a model, such as factories, seeders, policies, controllers, and form requests. In addition, these options may be combined to create multiple classes at once:
```


 1# Generate a model and a FlightFactory class...




 2php artisan make:model Flight --factory




 3php artisan make:model Flight -f




 4 



 5# Generate a model and a FlightSeeder class...




 6php artisan make:model Flight --seed




 7php artisan make:model Flight -s




 8 



 9# Generate a model and a FlightController class...




10php artisan make:model Flight --controller




11php artisan make:model Flight -c




12 



13# Generate a model, FlightController resource class, and form request classes...




14php artisan make:model Flight --controller --resource --requests




15php artisan make:model Flight -crR




16 



17# Generate a model and a FlightPolicy class...




18php artisan make:model Flight --policy




19 



20# Generate a model and a migration, factory, seeder, and controller...




21php artisan make:model Flight -mfsc




22 



23# Shortcut to generate a model, migration, factory, seeder, policy, controller, and form requests...




24php artisan make:model Flight --all




25php artisan make:model Flight -a




26 



27# Generate a pivot model...




28php artisan make:model Member --pivot




29php artisan make:model Member -p




# Generate a model and a FlightFactory class...
php artisan make:model Flight --factory
php artisan make:model Flight -f

# Generate a model and a FlightSeeder class...
php artisan make:model Flight --seed
php artisan make:model Flight -s

# Generate a model and a FlightController class...
php artisan make:model Flight --controller
php artisan make:model Flight -c

# Generate a model, FlightController resource class, and form request classes...
php artisan make:model Flight --controller --resource --requests
php artisan make:model Flight -crR

# Generate a model and a FlightPolicy class...
php artisan make:model Flight --policy

# Generate a model and a migration, factory, seeder, and controller...
php artisan make:model Flight -mfsc

# Shortcut to generate a model, migration, factory, seeder, policy, controller, and form requests...
php artisan make:model Flight --all
php artisan make:model Flight -a

# Generate a pivot model...
php artisan make:model Member --pivot
php artisan make:model Member -p

```

#### [Inspecting Models](https://laravel.com/docs/12.x/eloquent#inspecting-models)
Sometimes it can be difficult to determine all of a model's available attributes and relationships just by skimming its code. Instead, try the `model:show` Artisan command, which provides a convenient overview of all the model's attributes and relations:
```


1php artisan model:show Flight




php artisan model:show Flight

```
