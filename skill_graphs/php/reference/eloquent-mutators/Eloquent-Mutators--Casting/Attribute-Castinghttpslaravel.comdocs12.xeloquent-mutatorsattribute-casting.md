## [Attribute Casting](https://laravel.com/docs/12.x/eloquent-mutators#attribute-casting)
Attribute casting provides functionality similar to accessors and mutators without requiring you to define any additional methods on your model. Instead, your model's `casts` method provides a convenient way of converting attributes to common data types.
The `casts` method should return an array where the key is the name of the attribute being cast and the value is the type you wish to cast the column to. The supported cast types are:
  * `array`
  * `AsFluent::class`
  * `AsStringable::class`
  * `AsUri::class`
  * `boolean`
  * `collection`
  * `date`
  * `datetime`
  * `immutable_date`
  * `immutable_datetime`
  * `decimal:<precision>`
  * `double`
  * `encrypted`
  * `encrypted:array`
  * `encrypted:collection`
  * `encrypted:object`
  * `float`
  * `hashed`
  * `integer`
  * `object`
  * `real`
  * `string`
  * `timestamp`


To demonstrate attribute casting, let's cast the `is_admin` attribute, which is stored in our database as an integer (`0` or `1`) to a boolean value:
```


 1<?php




 2 



 3namespace App\Models;




 4 



 5use Illuminate\Database\Eloquent\Model;




 6 



 7class User extends Model




 8{




 9    /**




10     * Get the attributes that should be cast.




11     *




12     * @return array<string, string>




13     */




14    protected function casts(): array




15    {




16        return [




17            'is_admin' => 'boolean',




18        ];




19    }




20}




<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class User extends Model
{
    /**
     * Get the attributes that should be cast.
     *
     * @return array<string, string>
     */
    protected function casts(): array
    {
        return [
            'is_admin' => 'boolean',
        ];
    }
}

```

After defining the cast, the `is_admin` attribute will always be cast to a boolean when you access it, even if the underlying value is stored in the database as an integer:
```


1$user = App\Models\User::find(1);




2 



3if ($user->is_admin) {




4    // ...




5}




$user = App\Models\User::find(1);

if ($user->is_admin) {
    // ...
}

```

If you need to add a new, temporary cast at runtime, you may use the `mergeCasts` method. These cast definitions will be added to any of the casts already defined on the model:
```


1$user->mergeCasts([




2    'is_admin' => 'integer',




3    'options' => 'object',




4]);




$user->mergeCasts([
    'is_admin' => 'integer',
    'options' => 'object',
]);

```

Attributes that are `null` will not be cast. In addition, you should never define a cast (or an attribute) that has the same name as a relationship or assign a cast to the model's primary key.
#### [Stringable Casting](https://laravel.com/docs/12.x/eloquent-mutators#stringable-casting)
You may use the `Illuminate\Database\Eloquent\Casts\AsStringable` cast class to cast a model attribute to a [fluent Illuminate\Support\Stringable object](https://laravel.com/docs/12.x/strings#fluent-strings-method-list):
```


 1<?php




 2 



 3namespace App\Models;




 4 



 5use Illuminate\Database\Eloquent\Casts\AsStringable;




 6use Illuminate\Database\Eloquent\Model;




 7 



 8class User extends Model




 9{




10    /**




11     * Get the attributes that should be cast.




12     *




13     * @return array<string, string>




14     */




15    protected function casts(): array




16    {




17        return [




18            'directory' => AsStringable::class,




19        ];




20    }




21}




<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Casts\AsStringable;
use Illuminate\Database\Eloquent\Model;

class User extends Model
{
    /**
     * Get the attributes that should be cast.
     *
     * @return array<string, string>
     */
    protected function casts(): array
    {
        return [
            'directory' => AsStringable::class,
        ];
    }
}

```

### [Array and JSON Casting](https://laravel.com/docs/12.x/eloquent-mutators#array-and-json-casting)
The `array` cast is particularly useful when working with columns that are stored as serialized JSON. For example, if your database has a `JSON` or `TEXT` field type that contains serialized JSON, adding the `array` cast to that attribute will automatically deserialize the attribute to a PHP array when you access it on your Eloquent model:
```


 1<?php




 2 



 3namespace App\Models;




 4 



 5use Illuminate\Database\Eloquent\Model;




 6 



 7class User extends Model




 8{




 9    /**




10     * Get the attributes that should be cast.




11     *




12     * @return array<string, string>




13     */




14    protected function casts(): array




15    {




16        return [




17            'options' => 'array',




18        ];




19    }




20}




<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class User extends Model
{
    /**
     * Get the attributes that should be cast.
     *
     * @return array<string, string>
     */
    protected function casts(): array
    {
        return [
            'options' => 'array',
        ];
    }
}

```

Once the cast is defined, you may access the `options` attribute and it will automatically be deserialized from JSON into a PHP array. When you set the value of the `options` attribute, the given array will automatically be serialized back into JSON for storage:
```


 1use App\Models\User;




 2 



 3$user = User::find(1);




 4 



 5$options = $user->options;




 6 



 7$options['key'] = 'value';




 8 



 9$user->options = $options;




10 



11$user->save();




use App\Models\User;

$user = User::find(1);

$options = $user->options;

$options['key'] = 'value';

$user->options = $options;

$user->save();

```

To update a single field of a JSON attribute with a more terse syntax, you may [make the attribute mass assignable](https://laravel.com/docs/12.x/eloquent#mass-assignment-json-columns) and use the `->` operator when calling the `update` method:
```


1$user = User::find(1);




2 



3$user->update(['options->key' => 'value']);




$user = User::find(1);

$user->update(['options->key' => 'value']);

```

#### [JSON and Unicode](https://laravel.com/docs/12.x/eloquent-mutators#json-and-unicode)
If you would like to store an array attribute as JSON with unescaped Unicode characters, you may use the `json:unicode` cast:
```


 1/**




 2 * Get the attributes that should be cast.




 3 *




 4 * @return array<string, string>




 5 */




 6protected function casts(): array




 7{




 8    return [




 9        'options' => 'json:unicode',




10    ];




11}




/**
 * Get the attributes that should be cast.
 *
 * @return array<string, string>
 */
protected function casts(): array
{
    return [
        'options' => 'json:unicode',
    ];
}

```

#### [Array Object and Collection Casting](https://laravel.com/docs/12.x/eloquent-mutators#array-object-and-collection-casting)
Although the standard `array` cast is sufficient for many applications, it does have some disadvantages. Since the `array` cast returns a primitive type, it is not possible to mutate an offset of the array directly. For example, the following code will trigger a PHP error:
```


1$user = User::find(1);




2 



3$user->options['key'] = $value;




$user = User::find(1);

$user->options['key'] = $value;

```

To solve this, Laravel offers an `AsArrayObject` cast that casts your JSON attribute to an [custom cast](https://laravel.com/docs/12.x/eloquent-mutators#custom-casts) implementation, which allows Laravel to intelligently cache and transform the mutated object such that individual offsets may be modified without triggering a PHP error. To use the `AsArrayObject` cast, simply assign it to an attribute:
```


 1use Illuminate\Database\Eloquent\Casts\AsArrayObject;




 2 



 3/**




 4 * Get the attributes that should be cast.




 5 *




 6 * @return array<string, string>




 7 */




 8protected function casts(): array




 9{




10    return [




11        'options' => AsArrayObject::class,




12    ];




13}




use Illuminate\Database\Eloquent\Casts\AsArrayObject;

/**
 * Get the attributes that should be cast.
 *
 * @return array<string, string>
 */
protected function casts(): array
{
    return [
        'options' => AsArrayObject::class,
    ];
}

```

Similarly, Laravel offers an `AsCollection` cast that casts your JSON attribute to a Laravel [Collection](https://laravel.com/docs/12.x/collections) instance:
```


 1use Illuminate\Database\Eloquent\Casts\AsCollection;




 2 



 3/**




 4 * Get the attributes that should be cast.




 5 *




 6 * @return array<string, string>




 7 */




 8protected function casts(): array




 9{




10    return [




11        'options' => AsCollection::class,




12    ];




13}




use Illuminate\Database\Eloquent\Casts\AsCollection;

/**
 * Get the attributes that should be cast.
 *
 * @return array<string, string>
 */
protected function casts(): array
{
    return [
        'options' => AsCollection::class,
    ];
}

```

If you would like the `AsCollection` cast to instantiate a custom collection class instead of Laravel's base collection class, you may provide the collection class name as a cast argument:
```


 1use App\Collections\OptionCollection;




 2use Illuminate\Database\Eloquent\Casts\AsCollection;




 3 



 4/**




 5 * Get the attributes that should be cast.




 6 *




 7 * @return array<string, string>




 8 */




 9protected function casts(): array




10{




11    return [




12        'options' => AsCollection::using(OptionCollection::class),




13    ];




14}




use App\Collections\OptionCollection;
use Illuminate\Database\Eloquent\Casts\AsCollection;

/**
 * Get the attributes that should be cast.
 *
 * @return array<string, string>
 */
protected function casts(): array
{
    return [
        'options' => AsCollection::using(OptionCollection::class),
    ];
}

```

The `of` method may be used to indicate collection items should be mapped into a given class via the collection's [mapInto method](https://laravel.com/docs/12.x/collections#method-mapinto):
```


 1use App\ValueObjects\Option;




 2use Illuminate\Database\Eloquent\Casts\AsCollection;




 3 



 4/**




 5 * Get the attributes that should be cast.




 6 *




 7 * @return array<string, string>




 8 */




 9protected function casts(): array




10{




11    return [




12        'options' => AsCollection::of(Option::class)




13    ];




14}




use App\ValueObjects\Option;
use Illuminate\Database\Eloquent\Casts\AsCollection;

/**
 * Get the attributes that should be cast.
 *
 * @return array<string, string>
 */
protected function casts(): array
{
    return [
        'options' => AsCollection::of(Option::class)
    ];
}

```

When mapping collections to objects, the object should implement the `Illuminate\Contracts\Support\Arrayable` and `JsonSerializable` interfaces to define how their instances should be serialized into the database as JSON:
```


 1<?php




 2 



 3namespace App\ValueObjects;




 4 



 5use Illuminate\Contracts\Support\Arrayable;




 6use JsonSerializable;




 7 



 8class Option implements Arrayable, JsonSerializable




 9{




10    public string $name;




11    public mixed $value;




12    public bool $isLocked;




13 



14    /**




15     * Create a new Option instance.




16     */




17    public function __construct(array $data)




18    {




19        $this->name = $data['name'];




20        $this->value = $data['value'];




21        $this->isLocked = $data['is_locked'];




22    }




23 



24    /**




25     * Get the instance as an array.




26     *




27     * @return array{name: string, data: string, is_locked: bool}




28     */




29    public function toArray(): array




30    {




31        return [




32            'name' => $this->name,




33            'value' => $this->value,




34            'is_locked' => $this->isLocked,




35        ];




36    }




37 



38    /**




39     * Specify the data which should be serialized to JSON.




40     *




41     * @return array{name: string, data: string, is_locked: bool}




42     */




43    public function jsonSerialize(): array




44    {




45        return $this->toArray();




46    }




47}




<?php

namespace App\ValueObjects;

use Illuminate\Contracts\Support\Arrayable;
use JsonSerializable;

class Option implements Arrayable, JsonSerializable
{
    public string $name;
    public mixed $value;
    public bool $isLocked;

    /**
     * Create a new Option instance.
     */
    public function __construct(array $data)
    {
        $this->name = $data['name'];
        $this->value = $data['value'];
        $this->isLocked = $data['is_locked'];
    }

    /**
     * Get the instance as an array.
     *
     * @return array{name: string, data: string, is_locked: bool}
     */
    public function toArray(): array
    {
        return [
            'name' => $this->name,
            'value' => $this->value,
            'is_locked' => $this->isLocked,
        ];
    }

    /**
     * Specify the data which should be serialized to JSON.
     *
     * @return array{name: string, data: string, is_locked: bool}
     */
    public function jsonSerialize(): array
    {
        return $this->toArray();
    }
}

```

### [Binary Casting](https://laravel.com/docs/12.x/eloquent-mutators#binary-casting)
If your Eloquent model has a [binary type](https://laravel.com/docs/12.x/migrations#column-method-binary) `uuid` or `ulid` column in addition to your model's auto-incrementing ID column, you may use the `AsBinary` cast to automatically cast the value to and from its binary representation:
```


 1use Illuminate\Database\Eloquent\Casts\AsBinary;




 2 



 3/**




 4 * Get the attributes that should be cast.




 5 *




 6 * @return array<string, string>




 7 */




 8protected function casts(): array




 9{




10    return [




11        'uuid' => AsBinary::uuid(),




12        'ulid' => AsBinary::ulid(),




13    ];




14}




use Illuminate\Database\Eloquent\Casts\AsBinary;

/**
 * Get the attributes that should be cast.
 *
 * @return array<string, string>
 */
protected function casts(): array
{
    return [
        'uuid' => AsBinary::uuid(),
        'ulid' => AsBinary::ulid(),
    ];
}

```

Once the cast has been defined on the model, you may set the UUID / ULID attribute value to an object instance or a string. Eloquent will automatically cast the value to its binary representation. When retrieving the attribute's value, you will always receive a plain-text string value:
```


1use Illuminate\Support\Str;




2 



3$user->uuid = Str::uuid();




4 



5return $user->uuid;




6 



7// "6e8cdeed-2f32-40bd-b109-1e4405be2140"




use Illuminate\Support\Str;

$user->uuid = Str::uuid();

return $user->uuid;

// "6e8cdeed-2f32-40bd-b109-1e4405be2140"

```

### [Date Casting](https://laravel.com/docs/12.x/eloquent-mutators#date-casting)
By default, Eloquent will cast the `created_at` and `updated_at` columns to instances of `DateTime` class and provides an assortment of helpful methods. You may cast additional date attributes by defining additional date casts within your model's `casts` method. Typically, dates should be cast using the `datetime` or `immutable_datetime` cast types.
When defining a `date` or `datetime` cast, you may also specify the date's format. This format will be used when the [model is serialized to an array or JSON](https://laravel.com/docs/12.x/eloquent-serialization):
```


 1/**




 2 * Get the attributes that should be cast.




 3 *




 4 * @return array<string, string>




 5 */




 6protected function casts(): array




 7{




 8    return [




 9        'created_at' => 'datetime:Y-m-d',




10    ];




11}




/**
 * Get the attributes that should be cast.
 *
 * @return array<string, string>
 */
protected function casts(): array
{
    return [
        'created_at' => 'datetime:Y-m-d',
    ];
}

```

When a column is cast as a date, you may set the corresponding model attribute value to a UNIX timestamp, date string (`Y-m-d`), date-time string, or a `DateTime` / `Carbon` instance. The date's value will be correctly converted and stored in your database.
You may customize the default serialization format for all of your model's dates by defining a `serializeDate` method on your model. This method does not affect how your dates are formatted for storage in the database:
```


1/**




2 * Prepare a date for array / JSON serialization.




3 */




4protected function serializeDate(DateTimeInterface $date): string




5{




6    return $date->format('Y-m-d');




7}




/**
 * Prepare a date for array / JSON serialization.
 */
protected function serializeDate(DateTimeInterface $date): string
{
    return $date->format('Y-m-d');
}

```

To specify the format that should be used when actually storing a model's dates within your database, you should define a `$dateFormat` property on your model:
```


1/**




2 * The storage format of the model's date columns.




3 *




4 * @var string




5 */




6protected $dateFormat = 'U';




/**
 * The storage format of the model's date columns.
 *
 * @var string
 */
protected $dateFormat = 'U';

```

#### [Date Casting, Serialization, and Timezones](https://laravel.com/docs/12.x/eloquent-mutators#date-casting-and-timezones)
By default, the `date` and `datetime` casts will serialize dates to a UTC ISO-8601 date string (`YYYY-MM-DDTHH:MM:SS.uuuuuuZ`), regardless of the timezone specified in your application's `timezone` configuration option. You are strongly encouraged to always use this serialization format, as well as to store your application's dates in the UTC timezone by not changing your application's `timezone` configuration option from its default `UTC` value. Consistently using the UTC timezone throughout your application will provide the maximum level of interoperability with other date manipulation libraries written in PHP and JavaScript.
If a custom format is applied to the `date` or `datetime` cast, such as `datetime:Y-m-d H:i:s`, the inner timezone of the Carbon instance will be used during date serialization. Typically, this will be the timezone specified in your application's `timezone` configuration option. However, it's important to note that `timestamp` columns such as `created_at` and `updated_at` are exempt from this behavior and are always formatted in UTC, regardless of the application's timezone setting.
### [Enum Casting](https://laravel.com/docs/12.x/eloquent-mutators#enum-casting)
Eloquent also allows you to cast your attribute values to PHP `casts` method:
```


 1use App\Enums\ServerStatus;




 2 



 3/**




 4 * Get the attributes that should be cast.




 5 *




 6 * @return array<string, string>




 7 */




 8protected function casts(): array




 9{




10    return [




11        'status' => ServerStatus::class,




12    ];




13}




use App\Enums\ServerStatus;

/**
 * Get the attributes that should be cast.
 *
 * @return array<string, string>
 */
protected function casts(): array
{
    return [
        'status' => ServerStatus::class,
    ];
}

```

Once you have defined the cast on your model, the specified attribute will be automatically cast to and from an enum when you interact with the attribute:
```


1if ($server->status == ServerStatus::Provisioned) {




2    $server->status = ServerStatus::Ready;




3 



4    $server->save();




5}




if ($server->status == ServerStatus::Provisioned) {
    $server->status = ServerStatus::Ready;

    $server->save();
}

```

#### [Casting Arrays of Enums](https://laravel.com/docs/12.x/eloquent-mutators#casting-arrays-of-enums)
Sometimes you may need your model to store an array of enum values within a single column. To accomplish this, you may utilize the `AsEnumArrayObject` or `AsEnumCollection` casts provided by Laravel:
```


 1use App\Enums\ServerStatus;




 2use Illuminate\Database\Eloquent\Casts\AsEnumCollection;




 3 



 4/**




 5 * Get the attributes that should be cast.




 6 *




 7 * @return array<string, string>




 8 */




 9protected function casts(): array




10{




11    return [




12        'statuses' => AsEnumCollection::of(ServerStatus::class),




13    ];




14}




use App\Enums\ServerStatus;
use Illuminate\Database\Eloquent\Casts\AsEnumCollection;

/**
 * Get the attributes that should be cast.
 *
 * @return array<string, string>
 */
protected function casts(): array
{
    return [
        'statuses' => AsEnumCollection::of(ServerStatus::class),
    ];
}

```

### [Encrypted Casting](https://laravel.com/docs/12.x/eloquent-mutators#encrypted-casting)
The `encrypted` cast will encrypt a model's attribute value using Laravel's built-in [encryption](https://laravel.com/docs/12.x/encryption) features. In addition, the `encrypted:array`, `encrypted:collection`, `encrypted:object`, `AsEncryptedArrayObject`, and `AsEncryptedCollection` casts work like their unencrypted counterparts; however, as you might expect, the underlying value is encrypted when stored in your database.
As the final length of the encrypted text is not predictable and is longer than its plain text counterpart, make sure the associated database column is of `TEXT` type or larger. In addition, since the values are encrypted in the database, you will not be able to query or search encrypted attribute values.
#### [Key Rotation](https://laravel.com/docs/12.x/eloquent-mutators#key-rotation)
As you may know, Laravel encrypts strings using the `key` configuration value specified in your application's `app` configuration file. Typically, this value corresponds to the value of the `APP_KEY` environment variable. If you need to rotate your application's encryption key, you may [gracefully do so](https://laravel.com/docs/12.x/encryption#gracefully-rotating-encryption-keys).
### [Query Time Casting](https://laravel.com/docs/12.x/eloquent-mutators#query-time-casting)
Sometimes you may need to apply casts while executing a query, such as when selecting a raw value from a table. For example, consider the following query:
```


1use App\Models\Post;




2use App\Models\User;




3 



4$users = User::select([




5    'users.*',




6    'last_posted_at' => Post::selectRaw('MAX(created_at)')




7        ->whereColumn('user_id', 'users.id')




8])->get();




use App\Models\Post;
use App\Models\User;

$users = User::select([
    'users.*',
    'last_posted_at' => Post::selectRaw('MAX(created_at)')
        ->whereColumn('user_id', 'users.id')
])->get();

```

The `last_posted_at` attribute on the results of this query will be a simple string. It would be wonderful if we could apply a `datetime` cast to this attribute when executing the query. Thankfully, we may accomplish this using the `withCasts` method:
```


1$users = User::select([




2    'users.*',




3    'last_posted_at' => Post::selectRaw('MAX(created_at)')




4        ->whereColumn('user_id', 'users.id')




5])->withCasts([




6    'last_posted_at' => 'datetime'




7])->get();




$users = User::select([
    'users.*',
    'last_posted_at' => Post::selectRaw('MAX(created_at)')
        ->whereColumn('user_id', 'users.id')
])->withCasts([
    'last_posted_at' => 'datetime'
])->get();

```
