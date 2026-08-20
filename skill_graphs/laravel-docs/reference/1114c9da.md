## [Accessors and Mutators](https://laravel.com/docs/12.x/eloquent-mutators#accessors-and-mutators)
### [Defining an Accessor](https://laravel.com/docs/12.x/eloquent-mutators#defining-an-accessor)
An accessor transforms an Eloquent attribute value when it is accessed. To define an accessor, create a protected method on your model to represent the accessible attribute. This method name should correspond to the "camel case" representation of the true underlying model attribute / database column when applicable.
In this example, we'll define an accessor for the `first_name` attribute. The accessor will automatically be called by Eloquent when attempting to retrieve the value of the `first_name` attribute. All attribute accessor / mutator methods must declare a return type-hint of `Illuminate\Database\Eloquent\Casts\Attribute`:
```


 1<?php




 2 



 3namespace App\Models;




 4 



 5use Illuminate\Database\Eloquent\Casts\Attribute;




 6use Illuminate\Database\Eloquent\Model;




 7 



 8class User extends Model




 9{




10    /**




11     * Get the user's first name.




12     */




13    protected function firstName(): Attribute




14    {




15        return Attribute::make(




16            get: fn (string $value) => ucfirst($value),




17        );




18    }




19}




<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Casts\Attribute;
use Illuminate\Database\Eloquent\Model;

class User extends Model
{
    /**
     * Get the user's first name.
     */
    protected function firstName(): Attribute
    {
        return Attribute::make(
            get: fn (string $value) => ucfirst($value),
        );
    }
}

```

All accessor methods return an `Attribute` instance which defines how the attribute will be accessed and, optionally, mutated. In this example, we are only defining how the attribute will be accessed. To do so, we supply the `get` argument to the `Attribute` class constructor.
As you can see, the original value of the column is passed to the accessor, allowing you to manipulate and return the value. To access the value of the accessor, you may simply access the `first_name` attribute on a model instance:
```


1use App\Models\User;




2 



3$user = User::find(1);




4 



5$firstName = $user->first_name;




use App\Models\User;

$user = User::find(1);

$firstName = $user->first_name;

```

If you would like these computed values to be added to the array / JSON representations of your model, [you will need to append them](https://laravel.com/docs/12.x/eloquent-serialization#appending-values-to-json).
#### [Building Value Objects From Multiple Attributes](https://laravel.com/docs/12.x/eloquent-mutators#building-value-objects-from-multiple-attributes)
Sometimes your accessor may need to transform multiple model attributes into a single "value object". To do so, your `get` closure may accept a second argument of `$attributes`, which will be automatically supplied to the closure and will contain an array of all of the model's current attributes:
```


 1use App\Support\Address;




 2use Illuminate\Database\Eloquent\Casts\Attribute;




 3 



 4/**




 5 * Interact with the user's address.




 6 */




 7protected function address(): Attribute




 8{




 9    return Attribute::make(




10        get: fn (mixed $value, array $attributes) => new Address(




11            $attributes['address_line_one'],




12            $attributes['address_line_two'],




13        ),




14    );




15}




use App\Support\Address;
use Illuminate\Database\Eloquent\Casts\Attribute;

/**
 * Interact with the user's address.
 */
protected function address(): Attribute
{
    return Attribute::make(
        get: fn (mixed $value, array $attributes) => new Address(
            $attributes['address_line_one'],
            $attributes['address_line_two'],
        ),
    );
}

```

#### [Accessor Caching](https://laravel.com/docs/12.x/eloquent-mutators#accessor-caching)
When returning value objects from accessors, any changes made to the value object will automatically be synced back to the model before the model is saved. This is possible because Eloquent retains instances returned by accessors so it can return the same instance each time the accessor is invoked:
```


1use App\Models\User;




2 



3$user = User::find(1);




4 



5$user->address->lineOne = 'Updated Address Line 1 Value';




6$user->address->lineTwo = 'Updated Address Line 2 Value';




7 



8$user->save();




use App\Models\User;

$user = User::find(1);

$user->address->lineOne = 'Updated Address Line 1 Value';
$user->address->lineTwo = 'Updated Address Line 2 Value';

$user->save();

```

However, you may sometimes wish to enable caching for primitive values like strings and booleans, particularly if they are computationally intensive. To accomplish this, you may invoke the `shouldCache` method when defining your accessor:
```


1protected function hash(): Attribute




2{




3    return Attribute::make(




4        get: fn (string $value) => bcrypt(gzuncompress($value)),




5    )->shouldCache();




6}




protected function hash(): Attribute
{
    return Attribute::make(
        get: fn (string $value) => bcrypt(gzuncompress($value)),
    )->shouldCache();
}

```

If you would like to disable the object caching behavior of attributes, you may invoke the `withoutObjectCaching` method when defining the attribute:
```


 1/**




 2 * Interact with the user's address.




 3 */




 4protected function address(): Attribute




 5{




 6    return Attribute::make(




 7        get: fn (mixed $value, array $attributes) => new Address(




 8            $attributes['address_line_one'],




 9            $attributes['address_line_two'],




10        ),




11    )->withoutObjectCaching();




12}




/**
 * Interact with the user's address.
 */
protected function address(): Attribute
{
    return Attribute::make(
        get: fn (mixed $value, array $attributes) => new Address(
            $attributes['address_line_one'],
            $attributes['address_line_two'],
        ),
    )->withoutObjectCaching();
}

```

### [Defining a Mutator](https://laravel.com/docs/12.x/eloquent-mutators#defining-a-mutator)
A mutator transforms an Eloquent attribute value when it is set. To define a mutator, you may provide the `set` argument when defining your attribute. Let's define a mutator for the `first_name` attribute. This mutator will be automatically called when we attempt to set the value of the `first_name` attribute on the model:
```


 1<?php




 2 



 3namespace App\Models;




 4 



 5use Illuminate\Database\Eloquent\Casts\Attribute;




 6use Illuminate\Database\Eloquent\Model;




 7 



 8class User extends Model




 9{




10    /**




11     * Interact with the user's first name.




12     */




13    protected function firstName(): Attribute




14    {




15        return Attribute::make(




16            get: fn (string $value) => ucfirst($value),




17            set: fn (string $value) => strtolower($value),




18        );




19    }




20}




<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Casts\Attribute;
use Illuminate\Database\Eloquent\Model;

class User extends Model
{
    /**
     * Interact with the user's first name.
     */
    protected function firstName(): Attribute
    {
        return Attribute::make(
            get: fn (string $value) => ucfirst($value),
            set: fn (string $value) => strtolower($value),
        );
    }
}

```

The mutator closure will receive the value that is being set on the attribute, allowing you to manipulate the value and return the manipulated value. To use our mutator, we only need to set the `first_name` attribute on an Eloquent model:
```


1use App\Models\User;




2 



3$user = User::find(1);




4 



5$user->first_name = 'Sally';




use App\Models\User;

$user = User::find(1);

$user->first_name = 'Sally';

```

In this example, the `set` callback will be called with the value `Sally`. The mutator will then apply the `strtolower` function to the name and set its resulting value in the model's internal `$attributes` array.
#### [Mutating Multiple Attributes](https://laravel.com/docs/12.x/eloquent-mutators#mutating-multiple-attributes)
Sometimes your mutator may need to set multiple attributes on the underlying model. To do so, you may return an array from the `set` closure. Each key in the array should correspond with an underlying attribute / database column associated with the model:
```


 1use App\Support\Address;




 2use Illuminate\Database\Eloquent\Casts\Attribute;




 3 



 4/**




 5 * Interact with the user's address.




 6 */




 7protected function address(): Attribute




 8{




 9    return Attribute::make(




10        get: fn (mixed $value, array $attributes) => new Address(




11            $attributes['address_line_one'],




12            $attributes['address_line_two'],




13        ),




14        set: fn (Address $value) => [




15            'address_line_one' => $value->lineOne,




16            'address_line_two' => $value->lineTwo,




17        ],




18    );




19}




use App\Support\Address;
use Illuminate\Database\Eloquent\Casts\Attribute;

/**
 * Interact with the user's address.
 */
protected function address(): Attribute
{
    return Attribute::make(
        get: fn (mixed $value, array $attributes) => new Address(
            $attributes['address_line_one'],
            $attributes['address_line_two'],
        ),
        set: fn (Address $value) => [
            'address_line_one' => $value->lineOne,
            'address_line_two' => $value->lineTwo,
        ],
    );
}

```
