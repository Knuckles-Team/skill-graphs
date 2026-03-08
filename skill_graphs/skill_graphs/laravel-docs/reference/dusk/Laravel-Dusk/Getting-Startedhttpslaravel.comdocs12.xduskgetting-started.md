## [Getting Started](https://laravel.com/docs/12.x/dusk#getting-started)
### [Generating Tests](https://laravel.com/docs/12.x/dusk#generating-tests)
To generate a Dusk test, use the `dusk:make` Artisan command. The generated test will be placed in the `tests/Browser` directory:
```


1php artisan dusk:make LoginTest




php artisan dusk:make LoginTest

```

### [Resetting the Database After Each Test](https://laravel.com/docs/12.x/dusk#resetting-the-database-after-each-test)
Most of the tests you write will interact with pages that retrieve data from your application's database; however, your Dusk tests should never use the `RefreshDatabase` trait. The `RefreshDatabase` trait leverages database transactions which will not be applicable or available across HTTP requests. Instead, you have two options: the `DatabaseMigrations` trait and the `DatabaseTruncation` trait.
#### [Using Database Migrations](https://laravel.com/docs/12.x/dusk#reset-migrations)
The `DatabaseMigrations` trait will run your database migrations before each test. However, dropping and re-creating your database tables for each test is typically slower than truncating the tables:
Pest PHPUnit
```


1<?php




2 



3use Illuminate\Foundation\Testing\DatabaseMigrations;




4use Laravel\Dusk\Browser;




5 



6pest()->use(DatabaseMigrations::class);




7 



8//




<?php

use Illuminate\Foundation\Testing\DatabaseMigrations;
use Laravel\Dusk\Browser;

pest()->use(DatabaseMigrations::class);

//

```

```


 1<?php




 2 



 3namespace Tests\Browser;




 4 



 5use Illuminate\Foundation\Testing\DatabaseMigrations;




 6use Laravel\Dusk\Browser;




 7use Tests\DuskTestCase;




 8 



 9class ExampleTest extends DuskTestCase




10{




11    use DatabaseMigrations;




12 



13    //




14}




<?php

namespace Tests\Browser;

use Illuminate\Foundation\Testing\DatabaseMigrations;
use Laravel\Dusk\Browser;
use Tests\DuskTestCase;

class ExampleTest extends DuskTestCase
{
    use DatabaseMigrations;

    //
}

```

SQLite in-memory databases may not be used when executing Dusk tests. Since the browser executes within its own process, it will not be able to access the in-memory databases of other processes.
#### [Using Database Truncation](https://laravel.com/docs/12.x/dusk#reset-truncation)
The `DatabaseTruncation` trait will migrate your database on the first test in order to ensure your database tables have been properly created. However, on subsequent tests, the database's tables will simply be truncated - providing a speed boost over re-running all of your database migrations:
Pest PHPUnit
```


1<?php




2 



3use Illuminate\Foundation\Testing\DatabaseTruncation;




4use Laravel\Dusk\Browser;




5 



6pest()->use(DatabaseTruncation::class);




7 



8//




<?php

use Illuminate\Foundation\Testing\DatabaseTruncation;
use Laravel\Dusk\Browser;

pest()->use(DatabaseTruncation::class);

//

```

```


 1<?php




 2 



 3namespace Tests\Browser;




 4 



 5use App\Models\User;




 6use Illuminate\Foundation\Testing\DatabaseTruncation;




 7use Laravel\Dusk\Browser;




 8use Tests\DuskTestCase;




 9 



10class ExampleTest extends DuskTestCase




11{




12    use DatabaseTruncation;




13 



14    //




15}




<?php

namespace Tests\Browser;

use App\Models\User;
use Illuminate\Foundation\Testing\DatabaseTruncation;
use Laravel\Dusk\Browser;
use Tests\DuskTestCase;

class ExampleTest extends DuskTestCase
{
    use DatabaseTruncation;

    //
}

```

By default, this trait will truncate all tables except the `migrations` table. If you would like to customize the tables that should be truncated, you may define a `$tablesToTruncate` property on your test class:
If you are using Pest, you should define properties or methods on the base `DuskTestCase` class or on any class your test file extends.
```


1/**




2 * Indicates which tables should be truncated.




3 *




4 * @var array




5 */




6protected $tablesToTruncate = ['users'];




/**
 * Indicates which tables should be truncated.
 *
 * @var array
 */
protected $tablesToTruncate = ['users'];

```

Alternatively, you may define an `$exceptTables` property on your test class to specify which tables should be excluded from truncation:
```


1/**




2 * Indicates which tables should be excluded from truncation.




3 *




4 * @var array




5 */




6protected $exceptTables = ['users'];




/**
 * Indicates which tables should be excluded from truncation.
 *
 * @var array
 */
protected $exceptTables = ['users'];

```

To specify the database connections that should have their tables truncated, you may define a `$connectionsToTruncate` property on your test class:
```


1/**




2 * Indicates which connections should have their tables truncated.




3 *




4 * @var array




5 */




6protected $connectionsToTruncate = ['mysql'];




/**
 * Indicates which connections should have their tables truncated.
 *
 * @var array
 */
protected $connectionsToTruncate = ['mysql'];

```

If you would like to execute code before or after database truncation is performed, you may define `beforeTruncatingDatabase` or `afterTruncatingDatabase` methods on your test class:
```


 1/**




 2 * Perform any work that should take place before the database has started truncating.




 3 */




 4protected function beforeTruncatingDatabase(): void




 5{




 6    //




 7}




 8 



 9/**




10 * Perform any work that should take place after the database has finished truncating.




11 */




12protected function afterTruncatingDatabase(): void




13{




14    //




15}




/**
 * Perform any work that should take place before the database has started truncating.
 */
protected function beforeTruncatingDatabase(): void
{
    //
}

/**
 * Perform any work that should take place after the database has finished truncating.
 */
protected function afterTruncatingDatabase(): void
{
    //
}

```

### [Running Tests](https://laravel.com/docs/12.x/dusk#running-tests)
To run your browser tests, execute the `dusk` Artisan command:
```


1php artisan dusk




php artisan dusk

```

If you had test failures the last time you ran the `dusk` command, you may save time by re-running the failing tests first using the `dusk:fails` command:
```


1php artisan dusk:fails




php artisan dusk:fails

```

The `dusk` command accepts any argument that is normally accepted by the Pest / PHPUnit test runner, such as allowing you to only run the tests for a given
```


1php artisan dusk --group=foo




php artisan dusk --group=foo

```

If you are using [Laravel Sail](https://laravel.com/docs/12.x/sail) to manage your local development environment, please consult the Sail documentation on [configuring and running Dusk tests](https://laravel.com/docs/12.x/sail#laravel-dusk).
#### [Manually Starting ChromeDriver](https://laravel.com/docs/12.x/dusk#manually-starting-chromedriver)
By default, Dusk will automatically attempt to start ChromeDriver. If this does not work for your particular system, you may manually start ChromeDriver before running the `dusk` command. If you choose to start ChromeDriver manually, you should comment out the following line of your `tests/DuskTestCase.php` file:
```


1/**




2 * Prepare for Dusk test execution.




3 *




4 * @beforeClass




5 */




6public static function prepare(): void




7{




8    // static::startChromeDriver();




9}




/**
 * Prepare for Dusk test execution.
 *
 * @beforeClass
 */
public static function prepare(): void
{
    // static::startChromeDriver();
}

```

In addition, if you start ChromeDriver on a port other than 9515, you should modify the `driver` method of the same class to reflect the correct port:
```


 1use Facebook\WebDriver\Remote\RemoteWebDriver;




 2 



 3/**




 4 * Create the RemoteWebDriver instance.




 5 */




 6protected function driver(): RemoteWebDriver




 7{




 8    return RemoteWebDriver::create(




 9        'http://localhost:9515', DesiredCapabilities::chrome()




10    );




11}




use Facebook\WebDriver\Remote\RemoteWebDriver;

/**
 * Create the RemoteWebDriver instance.
 */
protected function driver(): RemoteWebDriver
{
    return RemoteWebDriver::create(
        'http://localhost:9515', DesiredCapabilities::chrome()
    );
}

```

### [Environment Handling](https://laravel.com/docs/12.x/dusk#environment-handling)
To force Dusk to use its own environment file when running tests, create a `.env.dusk.{environment}` file in the root of your project. For example, if you will be initiating the `dusk` command from your `local` environment, you should create a `.env.dusk.local` file.
When running tests, Dusk will back-up your `.env` file and rename your Dusk environment to `.env`. Once the tests have completed, your `.env` file will be restored.
