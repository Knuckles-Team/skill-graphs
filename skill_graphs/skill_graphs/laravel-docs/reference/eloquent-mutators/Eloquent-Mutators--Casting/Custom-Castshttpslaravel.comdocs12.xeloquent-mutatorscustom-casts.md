## [Custom Casts](https://laravel.com/docs/12.x/eloquent-mutators#custom-casts)
Laravel has a variety of built-in, helpful cast types; however, you may occasionally need to define your own cast types. To create a cast, execute the `make:cast` Artisan command. The new cast class will be placed in your `app/Casts` directory:
```


1php artisan make:cast AsJson




php artisan make:cast AsJson

```

All custom cast classes implement the `CastsAttributes` interface. Classes that implement this interface must define a `get` and `set` method. The `get` method is responsible for transforming a raw value from the database into a cast value, while the `set` method should transform a cast value into a raw value that can be stored in the database. As an example, we will re-implement the built-in `json` cast type as a custom cast type:
```


 1<?php




 2 



 3namespace App\Casts;




 4 



 5use Illuminate\Contracts\Database\Eloquent\CastsAttributes;




 6use Illuminate\Database\Eloquent\Model;




 7 



 8class AsJson implements CastsAttributes




 9{




10    /**




11     * Cast the given value.




12     *




13     * @param  array<string, mixed>  $attributes




14     * @return array<string, mixed>




15     */




16    public function get(




17        Model $model,




18        string $key,




19        mixed $value,




20        array $attributes,




21    ): array {




22        return json_decode($value, true);




23    }




24 



25    /**




26     * Prepare the given value for storage.




27     *




28     * @param  array<string, mixed>  $attributes




29     */




30    public function set(




31        Model $model,




32        string $key,




33        mixed $value,




34        array $attributes,




35    ): string {




36        return json_encode($value);




37    }




38}




<?php

namespace App\Casts;

use Illuminate\Contracts\Database\Eloquent\CastsAttributes;
use Illuminate\Database\Eloquent\Model;

class AsJson implements CastsAttributes
{
    /**
     * Cast the given value.
     *
     * @param  array<string, mixed>  $attributes
     * @return array<string, mixed>
     */
    public function get(
        Model $model,
        string $key,
        mixed $value,
        array $attributes,
    ): array {
        return json_decode($value, true);
    }

    /**
     * Prepare the given value for storage.
     *
     * @param  array<string, mixed>  $attributes
     */
    public function set(
        Model $model,
        string $key,
        mixed $value,
        array $attributes,
    ): string {
        return json_encode($value);
    }
}

```

Once you have defined a custom cast type, you may attach it to a model attribute using its class name:
```


 1<?php




 2 



 3namespace App\Models;




 4 



 5use App\Casts\AsJson;




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




18            'options' => AsJson::class,




19        ];




20    }




21}




<?php

namespace App\Models;

use App\Casts\AsJson;
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
            'options' => AsJson::class,
        ];
    }
}

```

### [Value Object Casting](https://laravel.com/docs/12.x/eloquent-mutators#value-object-casting)
You are not limited to casting values to primitive types. You may also cast values to objects. Defining custom casts that cast values to objects is very similar to casting to primitive types; however, if your value object encompasses more than one database column, the `set` method must return an array of key / value pairs that will be used to set raw, storable values on the model. If your value object only affects a single column, you should simply return the storable value.
As an example, we will define a custom cast class that casts multiple model values into a single `Address` value object. We will assume the `Address` value object has two public properties: `lineOne` and `lineTwo`:
```


 1<?php




 2 



 3namespace App\Casts;




 4 



 5use App\ValueObjects\Address;




 6use Illuminate\Contracts\Database\Eloquent\CastsAttributes;




 7use Illuminate\Database\Eloquent\Model;




 8use InvalidArgumentException;




 9 



10class AsAddress implements CastsAttributes




11{




12    /**




13     * Cast the given value.




14     *




15     * @param  array<string, mixed>  $attributes




16     */




17    public function get(




18        Model $model,




19        string $key,




20        mixed $value,




21        array $attributes,




22    ): Address {




23        return new Address(




24            $attributes['address_line_one'],




25            $attributes['address_line_two']




26        );




27    }




28 



29    /**




30     * Prepare the given value for storage.




31     *




32     * @param  array<string, mixed>  $attributes




33     * @return array<string, string>




34     */




35    public function set(




36        Model $model,




37        string $key,




38        mixed $value,




39        array $attributes,




40    ): array {




41        if (! $value instanceof Address) {




42            throw new InvalidArgumentException('The given value is not an Address instance.');




43        }




44 



45        return [




46            'address_line_one' => $value->lineOne,




47            'address_line_two' => $value->lineTwo,




48        ];




49    }




50}




<?php

namespace App\Casts;

use App\ValueObjects\Address;
use Illuminate\Contracts\Database\Eloquent\CastsAttributes;
use Illuminate\Database\Eloquent\Model;
use InvalidArgumentException;

class AsAddress implements CastsAttributes
{
    /**
     * Cast the given value.
     *
     * @param  array<string, mixed>  $attributes
     */
    public function get(
        Model $model,
        string $key,
        mixed $value,
        array $attributes,
    ): Address {
        return new Address(
            $attributes['address_line_one'],
            $attributes['address_line_two']
        );
    }

    /**
     * Prepare the given value for storage.
     *
     * @param  array<string, mixed>  $attributes
     * @return array<string, string>
     */
    public function set(
        Model $model,
        string $key,
        mixed $value,
        array $attributes,
    ): array {
        if (! $value instanceof Address) {
            throw new InvalidArgumentException('The given value is not an Address instance.');
        }

        return [
            'address_line_one' => $value->lineOne,
            'address_line_two' => $value->lineTwo,
        ];
    }
}

```

When casting to value objects, any changes made to the value object will automatically be synced back to the model before the model is saved:
```


1use App\Models\User;




2 



3$user = User::find(1);




4 



5$user->address->lineOne = 'Updated Address Value';




6 



7$user->save();




use App\Models\User;

$user = User::find(1);

$user->address->lineOne = 'Updated Address Value';

$user->save();

```

If you plan to serialize your Eloquent models containing value objects to JSON or arrays, you should implement the `Illuminate\Contracts\Support\Arrayable` and `JsonSerializable` interfaces on the value object.
#### [Value Object Caching](https://laravel.com/docs/12.x/eloquent-mutators#value-object-caching)
When attributes that are cast to value objects are resolved, they are cached by Eloquent. Therefore, the same object instance will be returned if the attribute is accessed again.
If you would like to disable the object caching behavior of custom cast classes, you may declare a public `withoutObjectCaching` property on your custom cast class:
```


1class AsAddress implements CastsAttributes




2{




3    public bool $withoutObjectCaching = true;




4 



5    // ...




6}




class AsAddress implements CastsAttributes
{
    public bool $withoutObjectCaching = true;

    // ...
}

```

### [Array / JSON Serialization](https://laravel.com/docs/12.x/eloquent-mutators#array-json-serialization)
When an Eloquent model is converted to an array or JSON using the `toArray` and `toJson` methods, your custom cast value objects will typically be serialized as well as long as they implement the `Illuminate\Contracts\Support\Arrayable` and `JsonSerializable` interfaces. However, when using value objects provided by third-party libraries, you may not have the ability to add these interfaces to the object.
Therefore, you may specify that your custom cast class will be responsible for serializing the value object. To do so, your custom cast class should implement the `Illuminate\Contracts\Database\Eloquent\SerializesCastableAttributes` interface. This interface states that your class should contain a `serialize` method which should return the serialized form of your value object:
```


 1/**




 2 * Get the serialized representation of the value.




 3 *




 4 * @param  array<string, mixed>  $attributes




 5 */




 6public function serialize(




 7    Model $model,




 8    string $key,




 9    mixed $value,




10    array $attributes,




11): string {




12    return (string) $value;




13}




/**
 * Get the serialized representation of the value.
 *
 * @param  array<string, mixed>  $attributes
 */
public function serialize(
    Model $model,
    string $key,
    mixed $value,
    array $attributes,
): string {
    return (string) $value;
}

```

### [Inbound Casting](https://laravel.com/docs/12.x/eloquent-mutators#inbound-casting)
Occasionally, you may need to write a custom cast class that only transforms values that are being set on the model and does not perform any operations when attributes are being retrieved from the model.
Inbound only custom casts should implement the `CastsInboundAttributes` interface, which only requires a `set` method to be defined. The `make:cast` Artisan command may be invoked with the `--inbound` option to generate an inbound only cast class:
```


1php artisan make:cast AsHash --inbound




php artisan make:cast AsHash --inbound

```

A classic example of an inbound only cast is a "hashing" cast. For example, we may define a cast that hashes inbound values via a given algorithm:
```


 1<?php




 2 



 3namespace App\Casts;




 4 



 5use Illuminate\Contracts\Database\Eloquent\CastsInboundAttributes;




 6use Illuminate\Database\Eloquent\Model;




 7 



 8class AsHash implements CastsInboundAttributes




 9{




10    /**




11     * Create a new cast class instance.




12     */




13    public function __construct(




14        protected string|null $algorithm = null,




15    ) {}




16 



17    /**




18     * Prepare the given value for storage.




19     *




20     * @param  array<string, mixed>  $attributes




21     */




22    public function set(




23        Model $model,




24        string $key,




25        mixed $value,




26        array $attributes,




27    ): string {




28        return is_null($this->algorithm)




29            ? bcrypt($value)




30            : hash($this->algorithm, $value);




31    }




32}




<?php

namespace App\Casts;

use Illuminate\Contracts\Database\Eloquent\CastsInboundAttributes;
use Illuminate\Database\Eloquent\Model;

class AsHash implements CastsInboundAttributes
{
    /**
     * Create a new cast class instance.
     */
    public function __construct(
        protected string|null $algorithm = null,
    ) {}

    /**
     * Prepare the given value for storage.
     *
     * @param  array<string, mixed>  $attributes
     */
    public function set(
        Model $model,
        string $key,
        mixed $value,
        array $attributes,
    ): string {
        return is_null($this->algorithm)
            ? bcrypt($value)
            : hash($this->algorithm, $value);
    }
}

```

### [Cast Parameters](https://laravel.com/docs/12.x/eloquent-mutators#cast-parameters)
When attaching a custom cast to a model, cast parameters may be specified by separating them from the class name using a `:` character and comma-delimiting multiple parameters. The parameters will be passed to the constructor of the cast class:
```


 1/**




 2 * Get the attributes that should be cast.




 3 *




 4 * @return array<string, string>




 5 */




 6protected function casts(): array




 7{




 8    return [




 9        'secret' => AsHash::class.':sha256',




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
        'secret' => AsHash::class.':sha256',
    ];
}

```

### [Comparing Cast Values](https://laravel.com/docs/12.x/eloquent-mutators#comparing-cast-values)
If you would like to define how two given cast values should be compared to determine if they have been changed, your custom cast class may implement the `Illuminate\Contracts\Database\Eloquent\ComparesCastableAttributes` interface. This allows you to have fine-grained control over which values Eloquent considers changed and thus saves to the database when a model is updated.
This interface states that your class should contain a `compare` method which should return `true` if the given values are considered equal:
```


 1/**




 2 * Determine if the given values are equal.




 3 *




 4 * @param  \Illuminate\Database\Eloquent\Model  $model




 5 * @param  string  $key




 6 * @param  mixed  $firstValue




 7 * @param  mixed  $secondValue




 8 * @return bool




 9 */




10public function compare(




11    Model $model,




12    string $key,




13    mixed $firstValue,




14    mixed $secondValue




15): bool {




16    return $firstValue === $secondValue;




17}




/**
 * Determine if the given values are equal.
 *
 * @param  \Illuminate\Database\Eloquent\Model  $model
 * @param  string  $key
 * @param  mixed  $firstValue
 * @param  mixed  $secondValue
 * @return bool
 */
public function compare(
    Model $model,
    string $key,
    mixed $firstValue,
    mixed $secondValue
): bool {
    return $firstValue === $secondValue;
}

```

### [Castables](https://laravel.com/docs/12.x/eloquent-mutators#castables)
You may want to allow your application's value objects to define their own custom cast classes. Instead of attaching the custom cast class to your model, you may alternatively attach a value object class that implements the `Illuminate\Contracts\Database\Eloquent\Castable` interface:
```


1use App\ValueObjects\Address;




2 



3protected function casts(): array




4{




5    return [




6        'address' => Address::class,




7    ];




8}




use App\ValueObjects\Address;

protected function casts(): array
{
    return [
        'address' => Address::class,
    ];
}

```

Objects that implement the `Castable` interface must define a `castUsing` method that returns the class name of the custom caster class that is responsible for casting to and from the `Castable` class:
```


 1<?php




 2 



 3namespace App\ValueObjects;




 4 



 5use Illuminate\Contracts\Database\Eloquent\Castable;




 6use App\Casts\AsAddress;




 7 



 8class Address implements Castable




 9{




10    /**




11     * Get the name of the caster class to use when casting from / to this cast target.




12     *




13     * @param  array<string, mixed>  $arguments




14     */




15    public static function castUsing(array $arguments): string




16    {




17        return AsAddress::class;




18    }




19}




<?php

namespace App\ValueObjects;

use Illuminate\Contracts\Database\Eloquent\Castable;
use App\Casts\AsAddress;

class Address implements Castable
{
    /**
     * Get the name of the caster class to use when casting from / to this cast target.
     *
     * @param  array<string, mixed>  $arguments
     */
    public static function castUsing(array $arguments): string
    {
        return AsAddress::class;
    }
}

```

When using `Castable` classes, you may still provide arguments in the `casts` method definition. The arguments will be passed to the `castUsing` method:
```


1use App\ValueObjects\Address;




2 



3protected function casts(): array




4{




5    return [




6        'address' => Address::class.':argument',




7    ];




8}




use App\ValueObjects\Address;

protected function casts(): array
{
    return [
        'address' => Address::class.':argument',
    ];
}

```

#### [Castables & Anonymous Cast Classes](https://laravel.com/docs/12.x/eloquent-mutators#anonymous-cast-classes)
By combining "castables" with PHP's `castUsing` method. The anonymous class should implement the `CastsAttributes` interface:
```


 1<?php




 2 



 3namespace App\ValueObjects;




 4 



 5use Illuminate\Contracts\Database\Eloquent\Castable;




 6use Illuminate\Contracts\Database\Eloquent\CastsAttributes;




 7 



 8class Address implements Castable




 9{




10    // ...




11 



12    /**




13     * Get the caster class to use when casting from / to this cast target.




14     *




15     * @param  array<string, mixed>  $arguments




16     */




17    public static function castUsing(array $arguments): CastsAttributes




18    {




19        return new class implements CastsAttributes




20        {




21            public function get(




22                Model $model,




23                string $key,




24                mixed $value,




25                array $attributes,




26            ): Address {




27                return new Address(




28                    $attributes['address_line_one'],




29                    $attributes['address_line_two']




30                );




31            }




32 



33            public function set(




34                Model $model,




35                string $key,




36                mixed $value,




37                array $attributes,




38            ): array {




39                return [




40                    'address_line_one' => $value->lineOne,




41                    'address_line_two' => $value->lineTwo,




42                ];




43            }




44        };




45    }




46}




<?php

namespace App\ValueObjects;

use Illuminate\Contracts\Database\Eloquent\Castable;
use Illuminate\Contracts\Database\Eloquent\CastsAttributes;

class Address implements Castable
{
    // ...

    /**
     * Get the caster class to use when casting from / to this cast target.
     *
     * @param  array<string, mixed>  $arguments
     */
    public static function castUsing(array $arguments): CastsAttributes
    {
        return new class implements CastsAttributes
        {
            public function get(
                Model $model,
                string $key,
                mixed $value,
                array $attributes,
            ): Address {
                return new Address(
                    $attributes['address_line_one'],
                    $attributes['address_line_two']
                );
            }

            public function set(
                Model $model,
                string $key,
                mixed $value,
                array $attributes,
            ): array {
                return [
                    'address_line_one' => $value->lineOne,
                    'address_line_two' => $value->lineTwo,
                ];
            }
        };
    }
}

```

Copy as markdown
  * [ Introduction ](https://laravel.com/docs/12.x/eloquent-mutators#introduction)
  * [ Accessors and Mutators ](https://laravel.com/docs/12.x/eloquent-mutators#accessors-and-mutators)
    * [ Defining an Accessor ](https://laravel.com/docs/12.x/eloquent-mutators#defining-an-accessor)
    * [ Defining a Mutator ](https://laravel.com/docs/12.x/eloquent-mutators#defining-a-mutator)
  * [ Attribute Casting ](https://laravel.com/docs/12.x/eloquent-mutators#attribute-casting)
    * [ Array and JSON Casting ](https://laravel.com/docs/12.x/eloquent-mutators#array-and-json-casting)
    * [ Binary Casting ](https://laravel.com/docs/12.x/eloquent-mutators#binary-casting)
    * [ Date Casting ](https://laravel.com/docs/12.x/eloquent-mutators#date-casting)
    * [ Enum Casting ](https://laravel.com/docs/12.x/eloquent-mutators#enum-casting)
    * [ Encrypted Casting ](https://laravel.com/docs/12.x/eloquent-mutators#encrypted-casting)
    * [ Query Time Casting ](https://laravel.com/docs/12.x/eloquent-mutators#query-time-casting)
  * [ Custom Casts ](https://laravel.com/docs/12.x/eloquent-mutators#custom-casts)
    * [ Value Object Casting ](https://laravel.com/docs/12.x/eloquent-mutators#value-object-casting)
    * [ Array / JSON Serialization ](https://laravel.com/docs/12.x/eloquent-mutators#array-json-serialization)
    * [ Inbound Casting ](https://laravel.com/docs/12.x/eloquent-mutators#inbound-casting)
    * [ Cast Parameters ](https://laravel.com/docs/12.x/eloquent-mutators#cast-parameters)
    * [ Comparing Cast Values ](https://laravel.com/docs/12.x/eloquent-mutators#comparing-cast-values)
    * [ Castables ](https://laravel.com/docs/12.x/eloquent-mutators#castables)


[ ![Laravel Boost](https://laravel.com/images/ads/boost-logo.svg) Supercharge your AI development with essential context Learn more  ](https://laravel.com/ai/boost)
[ ![Laravel Forge](https://laravel.com/images/ads/forge-logo.svg) Server management made simple for any PHP app Learn more  ](https://forge.laravel.com)
[ ![Laravel Cloud](https://laravel.com/images/ads/cloud-logo.svg) The fastest way to deploy and scale Laravel apps Learn more  ](https://cloud.laravel.com)
[ ![Laravel Nightwatch](https://laravel.com/images/ads/nightwatch-logo.svg) First-class monitoring and deep insights for Laravel apps Learn more  ](https://nightwatch.laravel.com)
Laravel is the most productive way to
build, deploy, and monitor software.
  * © 2026 Laravel
  * [ Legal ](https://laravel.com/legal)
  * [ Status ](https://status.laravel.com/)


####  Products
  * [ Cloud ](https://cloud.laravel.com)
  * [ Forge ](https://forge.laravel.com)
  * [ Nightwatch ](https://nightwatch.laravel.com)
  * [ Vapor ](https://vapor.laravel.com)
  * [ Nova ](https://nova.laravel.com)


####  Packages
  * [ Cashier ](https://laravel.com/docs/cashier)
  * [ Dusk ](https://laravel.com/docs/dusk)
  * [ Horizon ](https://laravel.com/docs/horizon)
  * [ Octane ](https://laravel.com/docs/octane)
  * [ Scout ](https://laravel.com/docs/scout)
  * [ Pennant ](https://laravel.com/docs/pennant)
  * [ Pint ](https://laravel.com/docs/pint)
  * [ Sail ](https://laravel.com/docs/sail)
  * [ Sanctum ](https://laravel.com/docs/sanctum)
  * [ Socialite ](https://laravel.com/docs/socialite)
  * [ Telescope ](https://laravel.com/docs/telescope)
  * [ Pulse ](https://laravel.com/docs/pulse)
  * [ Reverb ](https://laravel.com/docs/reverb)
  * [ Echo ](https://laravel.com/docs/broadcasting)


####  Resources
  * [ Documentation ](https://laravel.com/docs)
  * [ Starter Kits ](https://laravel.com/starter-kits)
  * [ Release Notes ](https://laravel.com/docs/releases)
  * [ Blog ](https://laravel.com/blog)
  * [ Community ](https://laravel.com/community)
  * [ Learn ](https://laravel.com/learn)
  * [ Careers ](https://laravel.com/careers)
  * [ Trust ](https://trust.laravel.com)


####  Partners
  *   * [byte5](https://partners.laravel.com/partners/byte5)
  * [Redberry](https://partners.laravel.com/partners/redberry)
  * [Vehikl](https://partners.laravel.com/partners/vehikl)
  * [Active Logic](https://partners.laravel.com/partners/active-logic)
  * [Tighten](https://partners.laravel.com/partners/tighten)
  * [Curotec](https://partners.laravel.com/partners/curotec)
  * [Kirschbaum](https://partners.laravel.com/partners/kirschbaum)
  * [Jump24](https://partners.laravel.com/partners/jump24)
  * [ More Partners ](https://partners.laravel.com)
