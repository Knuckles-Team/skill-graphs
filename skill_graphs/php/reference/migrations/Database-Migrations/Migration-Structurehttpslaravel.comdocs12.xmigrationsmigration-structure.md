## [Migration Structure](https://laravel.com/docs/12.x/migrations#migration-structure)
A migration class contains two methods: `up` and `down`. The `up` method is used to add new tables, columns, or indexes to your database, while the `down` method should reverse the operations performed by the `up` method.
Within both of these methods, you may use the Laravel schema builder to expressively create and modify tables. To learn about all of the methods available on the `Schema` builder, [check out its documentation](https://laravel.com/docs/12.x/migrations#creating-tables). For example, the following migration creates a `flights` table:
```


 1<?php




 2 



 3use Illuminate\Database\Migrations\Migration;




 4use Illuminate\Database\Schema\Blueprint;




 5use Illuminate\Support\Facades\Schema;




 6 



 7return new class extends Migration




 8{




 9    /**




10     * Run the migrations.




11     */




12    public function up(): void




13    {




14        Schema::create('flights', function (Blueprint $table) {




15            $table->id();




16            $table->string('name');




17            $table->string('airline');




18            $table->timestamps();




19        });




20    }




21 



22    /**




23     * Reverse the migrations.




24     */




25    public function down(): void




26    {




27        Schema::drop('flights');




28    }




29};




<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('flights', function (Blueprint $table) {
            $table->id();
            $table->string('name');
            $table->string('airline');
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::drop('flights');
    }
};

```

#### [Setting the Migration Connection](https://laravel.com/docs/12.x/migrations#setting-the-migration-connection)
If your migration will be interacting with a database connection other than your application's default database connection, you should set the `$connection` property of your migration:
```


 1/**




 2 * The database connection that should be used by the migration.




 3 *




 4 * @var string




 5 */




 6protected $connection = 'pgsql';




 7 



 8/**




 9 * Run the migrations.




10 */




11public function up(): void




12{




13    // ...




14}




/**
 * The database connection that should be used by the migration.
 *
 * @var string
 */
protected $connection = 'pgsql';

/**
 * Run the migrations.
 */
public function up(): void
{
    // ...
}

```

#### [Skipping Migrations](https://laravel.com/docs/12.x/migrations#skipping-migrations)
Sometimes a migration might be meant to support a feature that is not yet active and you do not want it to run yet. In this case you may define a `shouldRun` method on the migration. If the `shouldRun` method returns `false`, the migration will be skipped:
```


 1use App\Models\Flight;




 2use Laravel\Pennant\Feature;




 3 



 4/**




 5 * Determine if this migration should run.




 6 */




 7public function shouldRun(): bool




 8{




 9    return Feature::active(Flight::class);




10}




use App\Models\Flight;
use Laravel\Pennant\Feature;

/**
 * Determine if this migration should run.
 */
public function shouldRun(): bool
{
    return Feature::active(Flight::class);
}

```
