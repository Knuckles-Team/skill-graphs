## [Columns](https://laravel.com/docs/12.x/migrations#columns)
### [Creating Columns](https://laravel.com/docs/12.x/migrations#creating-columns)
The `table` method on the `Schema` facade may be used to update existing tables. Like the `create` method, the `table` method accepts two arguments: the name of the table and a closure that receives an `Illuminate\Database\Schema\Blueprint` instance you may use to add columns to the table:
```


1use Illuminate\Database\Schema\Blueprint;




2use Illuminate\Support\Facades\Schema;




3 



4Schema::table('users', function (Blueprint $table) {




5    $table->integer('votes');




6});




use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

Schema::table('users', function (Blueprint $table) {
    $table->integer('votes');
});

```

### [Available Column Types](https://laravel.com/docs/12.x/migrations#available-column-types)
The schema builder blueprint offers a variety of methods that correspond to the different types of columns you can add to your database tables. Each of the available methods are listed in the table below:
#### [Boolean Types](https://laravel.com/docs/12.x/migrations#booleans-method-list)
[boolean](https://laravel.com/docs/12.x/migrations#column-method-boolean)
#### [String & Text Types](https://laravel.com/docs/12.x/migrations#strings-and-texts-method-list)
[char](https://laravel.com/docs/12.x/migrations#column-method-char) [longText](https://laravel.com/docs/12.x/migrations#column-method-longText) [mediumText](https://laravel.com/docs/12.x/migrations#column-method-mediumText) [string](https://laravel.com/docs/12.x/migrations#column-method-string) [text](https://laravel.com/docs/12.x/migrations#column-method-text) [tinyText](https://laravel.com/docs/12.x/migrations#column-method-tinyText)
#### [Numeric Types](https://laravel.com/docs/12.x/migrations#numbers--method-list)
[bigIncrements](https://laravel.com/docs/12.x/migrations#column-method-bigIncrements) [bigInteger](https://laravel.com/docs/12.x/migrations#column-method-bigInteger) [decimal](https://laravel.com/docs/12.x/migrations#column-method-decimal) [double](https://laravel.com/docs/12.x/migrations#column-method-double) [float](https://laravel.com/docs/12.x/migrations#column-method-float) [id](https://laravel.com/docs/12.x/migrations#column-method-id) [increments](https://laravel.com/docs/12.x/migrations#column-method-increments) [integer](https://laravel.com/docs/12.x/migrations#column-method-integer) [mediumIncrements](https://laravel.com/docs/12.x/migrations#column-method-mediumIncrements) [mediumInteger](https://laravel.com/docs/12.x/migrations#column-method-mediumInteger) [smallIncrements](https://laravel.com/docs/12.x/migrations#column-method-smallIncrements) [smallInteger](https://laravel.com/docs/12.x/migrations#column-method-smallInteger) [tinyIncrements](https://laravel.com/docs/12.x/migrations#column-method-tinyIncrements) [tinyInteger](https://laravel.com/docs/12.x/migrations#column-method-tinyInteger) [unsignedBigInteger](https://laravel.com/docs/12.x/migrations#column-method-unsignedBigInteger) [unsignedInteger](https://laravel.com/docs/12.x/migrations#column-method-unsignedInteger) [unsignedMediumInteger](https://laravel.com/docs/12.x/migrations#column-method-unsignedMediumInteger) [unsignedSmallInteger](https://laravel.com/docs/12.x/migrations#column-method-unsignedSmallInteger) [unsignedTinyInteger](https://laravel.com/docs/12.x/migrations#column-method-unsignedTinyInteger)
#### [Date & Time Types](https://laravel.com/docs/12.x/migrations#dates-and-times-method-list)
[dateTime](https://laravel.com/docs/12.x/migrations#column-method-dateTime) [dateTimeTz](https://laravel.com/docs/12.x/migrations#column-method-dateTimeTz) [date](https://laravel.com/docs/12.x/migrations#column-method-date) [time](https://laravel.com/docs/12.x/migrations#column-method-time) [timeTz](https://laravel.com/docs/12.x/migrations#column-method-timeTz) [timestamp](https://laravel.com/docs/12.x/migrations#column-method-timestamp) [timestamps](https://laravel.com/docs/12.x/migrations#column-method-timestamps) [timestampsTz](https://laravel.com/docs/12.x/migrations#column-method-timestampsTz) [softDeletes](https://laravel.com/docs/12.x/migrations#column-method-softDeletes) [softDeletesTz](https://laravel.com/docs/12.x/migrations#column-method-softDeletesTz) [year](https://laravel.com/docs/12.x/migrations#column-method-year)
#### [Binary Types](https://laravel.com/docs/12.x/migrations#binaries-method-list)
[binary](https://laravel.com/docs/12.x/migrations#column-method-binary)
#### [Object & Json Types](https://laravel.com/docs/12.x/migrations#object-and-jsons-method-list)
[json](https://laravel.com/docs/12.x/migrations#column-method-json) [jsonb](https://laravel.com/docs/12.x/migrations#column-method-jsonb)
#### [UUID & ULID Types](https://laravel.com/docs/12.x/migrations#uuids-and-ulids-method-list)
[ulid](https://laravel.com/docs/12.x/migrations#column-method-ulid) [ulidMorphs](https://laravel.com/docs/12.x/migrations#column-method-ulidMorphs) [uuid](https://laravel.com/docs/12.x/migrations#column-method-uuid) [uuidMorphs](https://laravel.com/docs/12.x/migrations#column-method-uuidMorphs) [nullableUlidMorphs](https://laravel.com/docs/12.x/migrations#column-method-nullableUlidMorphs) [nullableUuidMorphs](https://laravel.com/docs/12.x/migrations#column-method-nullableUuidMorphs)
#### [Spatial Types](https://laravel.com/docs/12.x/migrations#spatials-method-list)
[geography](https://laravel.com/docs/12.x/migrations#column-method-geography) [geometry](https://laravel.com/docs/12.x/migrations#column-method-geometry)
#### [Relationship Types](https://laravel.com/docs/12.x/migrations#relationship-method-list)
[foreignId](https://laravel.com/docs/12.x/migrations#column-method-foreignId) [foreignIdFor](https://laravel.com/docs/12.x/migrations#column-method-foreignIdFor) [foreignUlid](https://laravel.com/docs/12.x/migrations#column-method-foreignUlid) [foreignUuid](https://laravel.com/docs/12.x/migrations#column-method-foreignUuid) [morphs](https://laravel.com/docs/12.x/migrations#column-method-morphs) [nullableMorphs](https://laravel.com/docs/12.x/migrations#column-method-nullableMorphs)
#### [Specialty Types](https://laravel.com/docs/12.x/migrations#spacifics-method-list)
[enum](https://laravel.com/docs/12.x/migrations#column-method-enum) [set](https://laravel.com/docs/12.x/migrations#column-method-set) [macAddress](https://laravel.com/docs/12.x/migrations#column-method-macAddress) [ipAddress](https://laravel.com/docs/12.x/migrations#column-method-ipAddress) [rememberToken](https://laravel.com/docs/12.x/migrations#column-method-rememberToken) [vector](https://laravel.com/docs/12.x/migrations#column-method-vector)
#### [`bigIncrements()`](https://laravel.com/docs/12.x/migrations#column-method-bigIncrements)
The `bigIncrements` method creates an auto-incrementing `UNSIGNED BIGINT` (primary key) equivalent column:
```


1$table->bigIncrements('id');




$table->bigIncrements('id');

```

#### [`bigInteger()`](https://laravel.com/docs/12.x/migrations#column-method-bigInteger)
The `bigInteger` method creates a `BIGINT` equivalent column:
```


1$table->bigInteger('votes');




$table->bigInteger('votes');

```

#### [`binary()`](https://laravel.com/docs/12.x/migrations#column-method-binary)
The `binary` method creates a `BLOB` equivalent column:
```


1$table->binary('photo');




$table->binary('photo');

```

When utilizing MySQL, MariaDB, or SQL Server, you may pass `length` and `fixed` arguments to create `VARBINARY` or `BINARY` equivalent column:
```


1$table->binary('data', length: 16); // VARBINARY(16)




2 



3$table->binary('data', length: 16, fixed: true); // BINARY(16)




$table->binary('data', length: 16); // VARBINARY(16)

$table->binary('data', length: 16, fixed: true); // BINARY(16)

```

#### [`boolean()`](https://laravel.com/docs/12.x/migrations#column-method-boolean)
The `boolean` method creates a `BOOLEAN` equivalent column:
```


1$table->boolean('confirmed');




$table->boolean('confirmed');

```

#### [`char()`](https://laravel.com/docs/12.x/migrations#column-method-char)
The `char` method creates a `CHAR` equivalent column with of a given length:
```


1$table->char('name', length: 100);




$table->char('name', length: 100);

```

#### [`dateTimeTz()`](https://laravel.com/docs/12.x/migrations#column-method-dateTimeTz)
The `dateTimeTz` method creates a `DATETIME` (with timezone) equivalent column with an optional fractional seconds precision:
```


1$table->dateTimeTz('created_at', precision: 0);




$table->dateTimeTz('created_at', precision: 0);

```

#### [`dateTime()`](https://laravel.com/docs/12.x/migrations#column-method-dateTime)
The `dateTime` method creates a `DATETIME` equivalent column with an optional fractional seconds precision:
```


1$table->dateTime('created_at', precision: 0);




$table->dateTime('created_at', precision: 0);

```

#### [`date()`](https://laravel.com/docs/12.x/migrations#column-method-date)
The `date` method creates a `DATE` equivalent column:
```


1$table->date('created_at');




$table->date('created_at');

```

#### [`decimal()`](https://laravel.com/docs/12.x/migrations#column-method-decimal)
The `decimal` method creates a `DECIMAL` equivalent column with the given precision (total digits) and scale (decimal digits):
```


1$table->decimal('amount', total: 8, places: 2);




$table->decimal('amount', total: 8, places: 2);

```

#### [`double()`](https://laravel.com/docs/12.x/migrations#column-method-double)
The `double` method creates a `DOUBLE` equivalent column:
```


1$table->double('amount');




$table->double('amount');

```

#### [`enum()`](https://laravel.com/docs/12.x/migrations#column-method-enum)
The `enum` method creates a `ENUM` equivalent column with the given valid values:
```


1$table->enum('difficulty', ['easy', 'hard']);




$table->enum('difficulty', ['easy', 'hard']);

```

Of course, you may use the `Enum::cases()` method instead of manually defining an array of allowed values:
```


1use App\Enums\Difficulty;




2 



3$table->enum('difficulty', Difficulty::cases());




use App\Enums\Difficulty;

$table->enum('difficulty', Difficulty::cases());

```

#### [`float()`](https://laravel.com/docs/12.x/migrations#column-method-float)
The `float` method creates a `FLOAT` equivalent column with the given precision:
```


1$table->float('amount', precision: 53);




$table->float('amount', precision: 53);

```

#### [`foreignId()`](https://laravel.com/docs/12.x/migrations#column-method-foreignId)
The `foreignId` method creates an `UNSIGNED BIGINT` equivalent column:
```


1$table->foreignId('user_id');




$table->foreignId('user_id');

```

#### [`foreignIdFor()`](https://laravel.com/docs/12.x/migrations#column-method-foreignIdFor)
The `foreignIdFor` method adds a `{column}_id` equivalent column for a given model class. The column type will be `UNSIGNED BIGINT`, `CHAR(36)`, or `CHAR(26)` depending on the model key type:
```


1$table->foreignIdFor(User::class);




$table->foreignIdFor(User::class);

```

#### [`foreignUlid()`](https://laravel.com/docs/12.x/migrations#column-method-foreignUlid)
The `foreignUlid` method creates a `ULID` equivalent column:
```


1$table->foreignUlid('user_id');




$table->foreignUlid('user_id');

```

#### [`foreignUuid()`](https://laravel.com/docs/12.x/migrations#column-method-foreignUuid)
The `foreignUuid` method creates a `UUID` equivalent column:
```


1$table->foreignUuid('user_id');




$table->foreignUuid('user_id');

```

#### [`geography()`](https://laravel.com/docs/12.x/migrations#column-method-geography)
The `geography` method creates a `GEOGRAPHY` equivalent column with the given spatial type and SRID (Spatial Reference System Identifier):
```


1$table->geography('coordinates', subtype: 'point', srid: 4326);




$table->geography('coordinates', subtype: 'point', srid: 4326);

```

Support for spatial types depends on your database driver. Please refer to your database's documentation. If your application is utilizing a PostgreSQL database, you must install the `geography` method may be used.
#### [`geometry()`](https://laravel.com/docs/12.x/migrations#column-method-geometry)
The `geometry` method creates a `GEOMETRY` equivalent column with the given spatial type and SRID (Spatial Reference System Identifier):
```


1$table->geometry('positions', subtype: 'point', srid: 0);




$table->geometry('positions', subtype: 'point', srid: 0);

```

Support for spatial types depends on your database driver. Please refer to your database's documentation. If your application is utilizing a PostgreSQL database, you must install the `geometry` method may be used.
#### [`id()`](https://laravel.com/docs/12.x/migrations#column-method-id)
The `id` method is an alias of the `bigIncrements` method. By default, the method will create an `id` column; however, you may pass a column name if you would like to assign a different name to the column:
```


1$table->id();




$table->id();

```

#### [`increments()`](https://laravel.com/docs/12.x/migrations#column-method-increments)
The `increments` method creates an auto-incrementing `UNSIGNED INTEGER` equivalent column as a primary key:
```


1$table->increments('id');




$table->increments('id');

```

#### [`integer()`](https://laravel.com/docs/12.x/migrations#column-method-integer)
The `integer` method creates an `INTEGER` equivalent column:
```


1$table->integer('votes');




$table->integer('votes');

```

#### [`ipAddress()`](https://laravel.com/docs/12.x/migrations#column-method-ipAddress)
The `ipAddress` method creates a `VARCHAR` equivalent column:
```


1$table->ipAddress('visitor');




$table->ipAddress('visitor');

```

When using PostgreSQL, an `INET` column will be created.
#### [`json()`](https://laravel.com/docs/12.x/migrations#column-method-json)
The `json` method creates a `JSON` equivalent column:
```


1$table->json('options');




$table->json('options');

```

When using SQLite, a `TEXT` column will be created.
#### [`jsonb()`](https://laravel.com/docs/12.x/migrations#column-method-jsonb)
The `jsonb` method creates a `JSONB` equivalent column:
```


1$table->jsonb('options');




$table->jsonb('options');

```

When using SQLite, a `TEXT` column will be created.
#### [`longText()`](https://laravel.com/docs/12.x/migrations#column-method-longText)
The `longText` method creates a `LONGTEXT` equivalent column:
```


1$table->longText('description');




$table->longText('description');

```

When utilizing MySQL or MariaDB, you may apply a `binary` character set to the column in order to create a `LONGBLOB` equivalent column:
```


1$table->longText('data')->charset('binary'); // LONGBLOB




$table->longText('data')->charset('binary'); // LONGBLOB

```

#### [`macAddress()`](https://laravel.com/docs/12.x/migrations#column-method-macAddress)
The `macAddress` method creates a column that is intended to hold a MAC address. Some database systems, such as PostgreSQL, have a dedicated column type for this type of data. Other database systems will use a string equivalent column:
```


1$table->macAddress('device');




$table->macAddress('device');

```

#### [`mediumIncrements()`](https://laravel.com/docs/12.x/migrations#column-method-mediumIncrements)
The `mediumIncrements` method creates an auto-incrementing `UNSIGNED MEDIUMINT` equivalent column as a primary key:
```


1$table->mediumIncrements('id');




$table->mediumIncrements('id');

```

#### [`mediumInteger()`](https://laravel.com/docs/12.x/migrations#column-method-mediumInteger)
The `mediumInteger` method creates a `MEDIUMINT` equivalent column:
```


1$table->mediumInteger('votes');




$table->mediumInteger('votes');

```

#### [`mediumText()`](https://laravel.com/docs/12.x/migrations#column-method-mediumText)
The `mediumText` method creates a `MEDIUMTEXT` equivalent column:
```


1$table->mediumText('description');




$table->mediumText('description');

```

When utilizing MySQL or MariaDB, you may apply a `binary` character set to the column in order to create a `MEDIUMBLOB` equivalent column:
```


1$table->mediumText('data')->charset('binary'); // MEDIUMBLOB




$table->mediumText('data')->charset('binary'); // MEDIUMBLOB

```

#### [`morphs()`](https://laravel.com/docs/12.x/migrations#column-method-morphs)
The `morphs` method is a convenience method that adds a `{column}_id` equivalent column and a `{column}_type` `VARCHAR` equivalent column. The column type for the `{column}_id` will be `UNSIGNED BIGINT`, `CHAR(36)`, or `CHAR(26)` depending on the model key type.
This method is intended to be used when defining the columns necessary for a polymorphic [Eloquent relationship](https://laravel.com/docs/12.x/eloquent-relationships). In the following example, `taggable_id` and `taggable_type` columns would be created:
```


1$table->morphs('taggable');




$table->morphs('taggable');

```

#### [`nullableMorphs()`](https://laravel.com/docs/12.x/migrations#column-method-nullableMorphs)
The method is similar to the [morphs](https://laravel.com/docs/12.x/migrations#column-method-morphs) method; however, the columns that are created will be "nullable":
```


1$table->nullableMorphs('taggable');




$table->nullableMorphs('taggable');

```

#### [`nullableUlidMorphs()`](https://laravel.com/docs/12.x/migrations#column-method-nullableUlidMorphs)
The method is similar to the [ulidMorphs](https://laravel.com/docs/12.x/migrations#column-method-ulidMorphs) method; however, the columns that are created will be "nullable":
```


1$table->nullableUlidMorphs('taggable');




$table->nullableUlidMorphs('taggable');

```

#### [`nullableUuidMorphs()`](https://laravel.com/docs/12.x/migrations#column-method-nullableUuidMorphs)
The method is similar to the [uuidMorphs](https://laravel.com/docs/12.x/migrations#column-method-uuidMorphs) method; however, the columns that are created will be "nullable":
```


1$table->nullableUuidMorphs('taggable');




$table->nullableUuidMorphs('taggable');

```

#### [`rememberToken()`](https://laravel.com/docs/12.x/migrations#column-method-rememberToken)
The `rememberToken` method creates a nullable, `VARCHAR(100)` equivalent column that is intended to store the current "remember me" [authentication token](https://laravel.com/docs/12.x/authentication#remembering-users):
```


1$table->rememberToken();




$table->rememberToken();

```

#### [`set()`](https://laravel.com/docs/12.x/migrations#column-method-set)
The `set` method creates a `SET` equivalent column with the given list of valid values:
```


1$table->set('flavors', ['strawberry', 'vanilla']);




$table->set('flavors', ['strawberry', 'vanilla']);

```

#### [`smallIncrements()`](https://laravel.com/docs/12.x/migrations#column-method-smallIncrements)
The `smallIncrements` method creates an auto-incrementing `UNSIGNED SMALLINT` equivalent column as a primary key:
```


1$table->smallIncrements('id');




$table->smallIncrements('id');

```

#### [`smallInteger()`](https://laravel.com/docs/12.x/migrations#column-method-smallInteger)
The `smallInteger` method creates a `SMALLINT` equivalent column:
```


1$table->smallInteger('votes');




$table->smallInteger('votes');

```

#### [`softDeletesTz()`](https://laravel.com/docs/12.x/migrations#column-method-softDeletesTz)
The `softDeletesTz` method adds a nullable `deleted_at` `TIMESTAMP` (with timezone) equivalent column with an optional fractional seconds precision. This column is intended to store the `deleted_at` timestamp needed for Eloquent's "soft delete" functionality:
```


1$table->softDeletesTz('deleted_at', precision: 0);




$table->softDeletesTz('deleted_at', precision: 0);

```

#### [`softDeletes()`](https://laravel.com/docs/12.x/migrations#column-method-softDeletes)
The `softDeletes` method adds a nullable `deleted_at` `TIMESTAMP` equivalent column with an optional fractional seconds precision. This column is intended to store the `deleted_at` timestamp needed for Eloquent's "soft delete" functionality:
```


1$table->softDeletes('deleted_at', precision: 0);




$table->softDeletes('deleted_at', precision: 0);

```

#### [`string()`](https://laravel.com/docs/12.x/migrations#column-method-string)
The `string` method creates a `VARCHAR` equivalent column of the given length:
```


1$table->string('name', length: 100);




$table->string('name', length: 100);

```

#### [`text()`](https://laravel.com/docs/12.x/migrations#column-method-text)
The `text` method creates a `TEXT` equivalent column:
```


1$table->text('description');




$table->text('description');

```

When utilizing MySQL or MariaDB, you may apply a `binary` character set to the column in order to create a `BLOB` equivalent column:
```


1$table->text('data')->charset('binary'); // BLOB




$table->text('data')->charset('binary'); // BLOB

```

#### [`timeTz()`](https://laravel.com/docs/12.x/migrations#column-method-timeTz)
The `timeTz` method creates a `TIME` (with timezone) equivalent column with an optional fractional seconds precision:
```


1$table->timeTz('sunrise', precision: 0);




$table->timeTz('sunrise', precision: 0);

```

#### [`time()`](https://laravel.com/docs/12.x/migrations#column-method-time)
The `time` method creates a `TIME` equivalent column with an optional fractional seconds precision:
```


1$table->time('sunrise', precision: 0);




$table->time('sunrise', precision: 0);

```

#### [`timestampTz()`](https://laravel.com/docs/12.x/migrations#column-method-timestampTz)
The `timestampTz` method creates a `TIMESTAMP` (with timezone) equivalent column with an optional fractional seconds precision:
```


1$table->timestampTz('added_at', precision: 0);




$table->timestampTz('added_at', precision: 0);

```

#### [`timestamp()`](https://laravel.com/docs/12.x/migrations#column-method-timestamp)
The `timestamp` method creates a `TIMESTAMP` equivalent column with an optional fractional seconds precision:
```


1$table->timestamp('added_at', precision: 0);




$table->timestamp('added_at', precision: 0);

```

#### [`timestampsTz()`](https://laravel.com/docs/12.x/migrations#column-method-timestampsTz)
The `timestampsTz` method creates `created_at` and `updated_at` `TIMESTAMP` (with timezone) equivalent columns with an optional fractional seconds precision:
```


1$table->timestampsTz(precision: 0);




$table->timestampsTz(precision: 0);

```

#### [`timestamps()`](https://laravel.com/docs/12.x/migrations#column-method-timestamps)
The `timestamps` method creates `created_at` and `updated_at` `TIMESTAMP` equivalent columns with an optional fractional seconds precision:
```


1$table->timestamps(precision: 0);




$table->timestamps(precision: 0);

```

#### [`tinyIncrements()`](https://laravel.com/docs/12.x/migrations#column-method-tinyIncrements)
The `tinyIncrements` method creates an auto-incrementing `UNSIGNED TINYINT` equivalent column as a primary key:
```


1$table->tinyIncrements('id');




$table->tinyIncrements('id');

```

#### [`tinyInteger()`](https://laravel.com/docs/12.x/migrations#column-method-tinyInteger)
The `tinyInteger` method creates a `TINYINT` equivalent column:
```


1$table->tinyInteger('votes');




$table->tinyInteger('votes');

```

#### [`tinyText()`](https://laravel.com/docs/12.x/migrations#column-method-tinyText)
The `tinyText` method creates a `TINYTEXT` equivalent column:
```


1$table->tinyText('notes');




$table->tinyText('notes');

```

When utilizing MySQL or MariaDB, you may apply a `binary` character set to the column in order to create a `TINYBLOB` equivalent column:
```


1$table->tinyText('data')->charset('binary'); // TINYBLOB




$table->tinyText('data')->charset('binary'); // TINYBLOB

```

#### [`unsignedBigInteger()`](https://laravel.com/docs/12.x/migrations#column-method-unsignedBigInteger)
The `unsignedBigInteger` method creates an `UNSIGNED BIGINT` equivalent column:
```


1$table->unsignedBigInteger('votes');




$table->unsignedBigInteger('votes');

```

#### [`unsignedInteger()`](https://laravel.com/docs/12.x/migrations#column-method-unsignedInteger)
The `unsignedInteger` method creates an `UNSIGNED INTEGER` equivalent column:
```


1$table->unsignedInteger('votes');




$table->unsignedInteger('votes');

```

#### [`unsignedMediumInteger()`](https://laravel.com/docs/12.x/migrations#column-method-unsignedMediumInteger)
The `unsignedMediumInteger` method creates an `UNSIGNED MEDIUMINT` equivalent column:
```


1$table->unsignedMediumInteger('votes');




$table->unsignedMediumInteger('votes');

```

#### [`unsignedSmallInteger()`](https://laravel.com/docs/12.x/migrations#column-method-unsignedSmallInteger)
The `unsignedSmallInteger` method creates an `UNSIGNED SMALLINT` equivalent column:
```


1$table->unsignedSmallInteger('votes');




$table->unsignedSmallInteger('votes');

```

#### [`unsignedTinyInteger()`](https://laravel.com/docs/12.x/migrations#column-method-unsignedTinyInteger)
The `unsignedTinyInteger` method creates an `UNSIGNED TINYINT` equivalent column:
```


1$table->unsignedTinyInteger('votes');




$table->unsignedTinyInteger('votes');

```

#### [`ulidMorphs()`](https://laravel.com/docs/12.x/migrations#column-method-ulidMorphs)
The `ulidMorphs` method is a convenience method that adds a `{column}_id` `CHAR(26)` equivalent column and a `{column}_type` `VARCHAR` equivalent column.
This method is intended to be used when defining the columns necessary for a polymorphic [Eloquent relationship](https://laravel.com/docs/12.x/eloquent-relationships) that use ULID identifiers. In the following example, `taggable_id` and `taggable_type` columns would be created:
```


1$table->ulidMorphs('taggable');




$table->ulidMorphs('taggable');

```

#### [`uuidMorphs()`](https://laravel.com/docs/12.x/migrations#column-method-uuidMorphs)
The `uuidMorphs` method is a convenience method that adds a `{column}_id` `CHAR(36)` equivalent column and a `{column}_type` `VARCHAR` equivalent column.
This method is intended to be used when defining the columns necessary for a [polymorphic Eloquent relationship](https://laravel.com/docs/12.x/eloquent-relationships#polymorphic-relationships) that use UUID identifiers. In the following example, `taggable_id` and `taggable_type` columns would be created:
```


1$table->uuidMorphs('taggable');




$table->uuidMorphs('taggable');

```

#### [`ulid()`](https://laravel.com/docs/12.x/migrations#column-method-ulid)
The `ulid` method creates a `ULID` equivalent column:
```


1$table->ulid('id');




$table->ulid('id');

```

#### [`uuid()`](https://laravel.com/docs/12.x/migrations#column-method-uuid)
The `uuid` method creates a `UUID` equivalent column:
```


1$table->uuid('id');




$table->uuid('id');

```

#### [`vector()`](https://laravel.com/docs/12.x/migrations#column-method-vector)
The `vector` method creates a `vector` equivalent column:
```


1$table->vector('embedding', dimensions: 100);




$table->vector('embedding', dimensions: 100);

```

When utilizing PostgreSQL, the `pgvector` extension must be loaded before `vector` columns can be created:
```


1Schema::ensureVectorExtensionExists();




Schema::ensureVectorExtensionExists();

```

#### [`year()`](https://laravel.com/docs/12.x/migrations#column-method-year)
The `year` method creates a `YEAR` equivalent column:
```


1$table->year('birth_year');




$table->year('birth_year');

```

### [Column Modifiers](https://laravel.com/docs/12.x/migrations#column-modifiers)
In addition to the column types listed above, there are several column "modifiers" you may use when adding a column to a database table. For example, to make the column "nullable", you may use the `nullable` method:
```


1use Illuminate\Database\Schema\Blueprint;




2use Illuminate\Support\Facades\Schema;




3 



4Schema::table('users', function (Blueprint $table) {




5    $table->string('email')->nullable();




6});




use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

Schema::table('users', function (Blueprint $table) {
    $table->string('email')->nullable();
});

```

The following table contains all of the available column modifiers. This list does not include [index modifiers](https://laravel.com/docs/12.x/migrations#creating-indexes):
Modifier | Description
---|---
`->after('column')` | Place the column "after" another column (MariaDB / MySQL).
`->autoIncrement()` | Set `INTEGER` columns as auto-incrementing (primary key).
`->charset('utf8mb4')` | Specify a character set for the column (MariaDB / MySQL).
`->collation('utf8mb4_unicode_ci')` | Specify a collation for the column.
`->comment('my comment')` | Add a comment to a column (MariaDB / MySQL / PostgreSQL).
`->default($value)` | Specify a "default" value for the column.
`->first()` | Place the column "first" in the table (MariaDB / MySQL).
`->from($integer)` | Set the starting value of an auto-incrementing field (MariaDB / MySQL / PostgreSQL).
`->instant()` | Add or modify the column using an instant operation (MySQL).
`->invisible()` | Make the column "invisible" to `SELECT *` queries (MariaDB / MySQL).
`->lock($mode)` | Specify a lock mode for the column operation (MySQL).
`->nullable($value = true)` | Allow `NULL` values to be inserted into the column.
`->storedAs($expression)` | Create a stored generated column (MariaDB / MySQL / PostgreSQL / SQLite).
`->unsigned()` | Set `INTEGER` columns as `UNSIGNED` (MariaDB / MySQL).
`->useCurrent()` | Set `TIMESTAMP` columns to use `CURRENT_TIMESTAMP` as default value.
`->useCurrentOnUpdate()` | Set `TIMESTAMP` columns to use `CURRENT_TIMESTAMP` when a record is updated (MariaDB / MySQL).
`->virtualAs($expression)` | Create a virtual generated column (MariaDB / MySQL / SQLite).
`->generatedAs($expression)` | Create an identity column with specified sequence options (PostgreSQL).
`->always()` | Defines the precedence of sequence values over input for an identity column (PostgreSQL).
#### [Default Expressions](https://laravel.com/docs/12.x/migrations#default-expressions)
The `default` modifier accepts a value or an `Illuminate\Database\Query\Expression` instance. Using an `Expression` instance will prevent Laravel from wrapping the value in quotes and allow you to use database specific functions. One situation where this is particularly useful is when you need to assign default values to JSON columns:
```


 1<?php




 2 



 3use Illuminate\Support\Facades\Schema;




 4use Illuminate\Database\Schema\Blueprint;




 5use Illuminate\Database\Query\Expression;




 6use Illuminate\Database\Migrations\Migration;




 7 



 8return new class extends Migration




 9{




10    /**




11     * Run the migrations.




12     */




13    public function up(): void




14    {




15        Schema::create('flights', function (Blueprint $table) {




16            $table->id();




17            $table->json('movies')->default(new Expression('(JSON_ARRAY())'));




18            $table->timestamps();




19        });




20    }




21};




<?php

use Illuminate\Support\Facades\Schema;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Query\Expression;
use Illuminate\Database\Migrations\Migration;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('flights', function (Blueprint $table) {
            $table->id();
            $table->json('movies')->default(new Expression('(JSON_ARRAY())'));
            $table->timestamps();
        });
    }
};

```

Support for default expressions depends on your database driver, database version, and the field type. Please refer to your database's documentation.
#### [Column Order](https://laravel.com/docs/12.x/migrations#column-order)
When using the MariaDB or MySQL database, the `after` method may be used to add columns after an existing column in the schema:
```


1$table->after('password', function (Blueprint $table) {




2    $table->string('address_line1');




3    $table->string('address_line2');




4    $table->string('city');




5});




$table->after('password', function (Blueprint $table) {
    $table->string('address_line1');
    $table->string('address_line2');
    $table->string('city');
});

```

#### [Instant Column Operations](https://laravel.com/docs/12.x/migrations#instant-column-operations)
When using MySQL, you may chain the `instant` modifier onto a column definition to indicate that the column should be added or modified using MySQL's "instant" algorithm. This algorithm allows certain schema changes to be performed without a full table rebuild, making them nearly instantaneous regardless of table size:
```


1$table->string('name')->nullable()->instant();




$table->string('name')->nullable()->instant();

```

Instant column additions can only append columns to the end of the table, so the `instant` modifier cannot be combined with the `after` or `first` modifiers. In addition, the algorithm does not support all column types or operations. If the requested operation is incompatible, MySQL will raise an error.
Please refer to
#### [DDL Locking](https://laravel.com/docs/12.x/migrations#ddl-locking)
When using MySQL, you may chain the `lock` modifier onto column, index, or foreign key definitions to control table locking during schema operations. MySQL supports several lock modes: `none` allows concurrent reads and writes, `shared` allows concurrent reads but blocks writes, `exclusive` blocks all concurrent access, and `default` lets MySQL choose the most appropriate mode:
```


1$table->string('name')->lock('none');




2 



3$table->index('email')->lock('shared');




$table->string('name')->lock('none');

$table->index('email')->lock('shared');

```

If the requested lock mode is incompatible with the operation, MySQL will raise an error. The `lock` modifier may be combined with the `instant` modifier to further optimize schema changes:
```


1$table->string('name')->instant()->lock('none');




$table->string('name')->instant()->lock('none');

```

### [Modifying Columns](https://laravel.com/docs/12.x/migrations#modifying-columns)
The `change` method allows you to modify the type and attributes of existing columns. For example, you may wish to increase the size of a `string` column. To see the `change` method in action, let's increase the size of the `name` column from 25 to 50. To accomplish this, we simply define the new state of the column and then call the `change` method:
```


1Schema::table('users', function (Blueprint $table) {




2    $table->string('name', 50)->change();




3});




Schema::table('users', function (Blueprint $table) {
    $table->string('name', 50)->change();
});

```

When modifying a column, you must explicitly include all the modifiers you want to keep on the column definition - any missing attribute will be dropped. For example, to retain the `unsigned`, `default`, and `comment` attributes, you must call each modifier explicitly when changing the column:
```


1Schema::table('users', function (Blueprint $table) {




2    $table->integer('votes')->unsigned()->default(1)->comment('my comment')->change();




3});




Schema::table('users', function (Blueprint $table) {
    $table->integer('votes')->unsigned()->default(1)->comment('my comment')->change();
});

```

The `change` method does not change the indexes of the column. Therefore, you may use index modifiers to explicitly add or drop an index when modifying the column:
```


1// Add an index...




2$table->bigIncrements('id')->primary()->change();




3 



4// Drop an index...




5$table->char('postal_code', 10)->unique(false)->change();




// Add an index...
$table->bigIncrements('id')->primary()->change();

// Drop an index...
$table->char('postal_code', 10)->unique(false)->change();

```

### [Renaming Columns](https://laravel.com/docs/12.x/migrations#renaming-columns)
To rename a column, you may use the `renameColumn` method provided by the schema builder:
```


1Schema::table('users', function (Blueprint $table) {




2    $table->renameColumn('from', 'to');




3});




Schema::table('users', function (Blueprint $table) {
    $table->renameColumn('from', 'to');
});

```

### [Dropping Columns](https://laravel.com/docs/12.x/migrations#dropping-columns)
To drop a column, you may use the `dropColumn` method on the schema builder:
```


1Schema::table('users', function (Blueprint $table) {




2    $table->dropColumn('votes');




3});




Schema::table('users', function (Blueprint $table) {
    $table->dropColumn('votes');
});

```

You may drop multiple columns from a table by passing an array of column names to the `dropColumn` method:
```


1Schema::table('users', function (Blueprint $table) {




2    $table->dropColumn(['votes', 'avatar', 'location']);




3});




Schema::table('users', function (Blueprint $table) {
    $table->dropColumn(['votes', 'avatar', 'location']);
});

```

#### [Available Command Aliases](https://laravel.com/docs/12.x/migrations#available-command-aliases)
Laravel provides several convenient methods related to dropping common types of columns. Each of these methods is described in the table below:
Command | Description
---|---
`$table->dropMorphs('morphable');` | Drop the `morphable_id` and `morphable_type` columns.
`$table->dropRememberToken();` | Drop the `remember_token` column.
`$table->dropSoftDeletes();` | Drop the `deleted_at` column.
`$table->dropSoftDeletesTz();` | Alias of `dropSoftDeletes()` method.
`$table->dropTimestamps();` | Drop the `created_at` and `updated_at` columns.
`$table->dropTimestampsTz();` | Alias of `dropTimestamps()` method.
