## [Custom Validation Rules](https://laravel.com/docs/12.x/validation#custom-validation-rules)
### [Using Rule Objects](https://laravel.com/docs/12.x/validation#using-rule-objects)
Laravel provides a variety of helpful validation rules; however, you may wish to specify some of your own. One method of registering custom validation rules is using rule objects. To generate a new rule object, you may use the `make:rule` Artisan command. Let's use this command to generate a rule that verifies a string is uppercase. Laravel will place the new rule in the `app/Rules` directory. If this directory does not exist, Laravel will create it when you execute the Artisan command to create your rule:
```


1php artisan make:rule Uppercase




php artisan make:rule Uppercase

```

Once the rule has been created, we are ready to define its behavior. A rule object contains a single method: `validate`. This method receives the attribute name, its value, and a callback that should be invoked on failure with the validation error message:
```


 1<?php




 2 



 3namespace App\Rules;




 4 



 5use Closure;




 6use Illuminate\Contracts\Validation\ValidationRule;




 7 



 8class Uppercase implements ValidationRule




 9{




10    /**




11     * Run the validation rule.




12     */




13    public function validate(string $attribute, mixed $value, Closure $fail): void




14    {




15        if (strtoupper($value) !== $value) {




16            $fail('The :attribute must be uppercase.');




17        }




18    }




19}




<?php

namespace App\Rules;

use Closure;
use Illuminate\Contracts\Validation\ValidationRule;

class Uppercase implements ValidationRule
{
    /**
     * Run the validation rule.
     */
    public function validate(string $attribute, mixed $value, Closure $fail): void
    {
        if (strtoupper($value) !== $value) {
            $fail('The :attribute must be uppercase.');
        }
    }
}

```

Once the rule has been defined, you may attach it to a validator by passing an instance of the rule object with your other validation rules:
```


1use App\Rules\Uppercase;




2 



3$request->validate([




4    'name' => ['required', 'string', new Uppercase],




5]);




use App\Rules\Uppercase;

$request->validate([
    'name' => ['required', 'string', new Uppercase],
]);

```

#### Translating Validation Messages
Instead of providing a literal error message to the `$fail` closure, you may also provide a [translation string key](https://laravel.com/docs/12.x/localization) and instruct Laravel to translate the error message:
```


1if (strtoupper($value) !== $value) {




2    $fail('validation.uppercase')->translate();




3}




if (strtoupper($value) !== $value) {
    $fail('validation.uppercase')->translate();
}

```

If necessary, you may provide placeholder replacements and the preferred language as the first and second arguments to the `translate` method:
```


1$fail('validation.location')->translate([




2    'value' => $this->value,




3], 'fr');




$fail('validation.location')->translate([
    'value' => $this->value,
], 'fr');

```

#### Accessing Additional Data
If your custom validation rule class needs to access all of the other data undergoing validation, your rule class may implement the `Illuminate\Contracts\Validation\DataAwareRule` interface. This interface requires your class to define a `setData` method. This method will automatically be invoked by Laravel (before validation proceeds) with all of the data under validation:
```


 1<?php




 2 



 3namespace App\Rules;




 4 



 5use Illuminate\Contracts\Validation\DataAwareRule;




 6use Illuminate\Contracts\Validation\ValidationRule;




 7 



 8class Uppercase implements DataAwareRule, ValidationRule




 9{




10    /**




11     * All of the data under validation.




12     *




13     * @var array<string, mixed>




14     */




15    protected $data = [];




16 



17    // ...




18 



19    /**




20     * Set the data under validation.




21     *




22     * @param  array<string, mixed>  $data




23     */




24    public function setData(array $data): static




25    {




26        $this->data = $data;




27 



28        return $this;




29    }




30}




<?php

namespace App\Rules;

use Illuminate\Contracts\Validation\DataAwareRule;
use Illuminate\Contracts\Validation\ValidationRule;

class Uppercase implements DataAwareRule, ValidationRule
{
    /**
     * All of the data under validation.
     *
     * @var array<string, mixed>
     */
    protected $data = [];

    // ...

    /**
     * Set the data under validation.
     *
     * @param  array<string, mixed>  $data
     */
    public function setData(array $data): static
    {
        $this->data = $data;

        return $this;
    }
}

```

Or, if your validation rule requires access to the validator instance performing the validation, you may implement the `ValidatorAwareRule` interface:
```


 1<?php




 2 



 3namespace App\Rules;




 4 



 5use Illuminate\Contracts\Validation\ValidationRule;




 6use Illuminate\Contracts\Validation\ValidatorAwareRule;




 7use Illuminate\Validation\Validator;




 8 



 9class Uppercase implements ValidationRule, ValidatorAwareRule




10{




11    /**




12     * The validator instance.




13     *




14     * @var \Illuminate\Validation\Validator




15     */




16    protected $validator;




17 



18    // ...




19 



20    /**




21     * Set the current validator.




22     */




23    public function setValidator(Validator $validator): static




24    {




25        $this->validator = $validator;




26 



27        return $this;




28    }




29}




<?php

namespace App\Rules;

use Illuminate\Contracts\Validation\ValidationRule;
use Illuminate\Contracts\Validation\ValidatorAwareRule;
use Illuminate\Validation\Validator;

class Uppercase implements ValidationRule, ValidatorAwareRule
{
    /**
     * The validator instance.
     *
     * @var \Illuminate\Validation\Validator
     */
    protected $validator;

    // ...

    /**
     * Set the current validator.
     */
    public function setValidator(Validator $validator): static
    {
        $this->validator = $validator;

        return $this;
    }
}

```

### [Using Closures](https://laravel.com/docs/12.x/validation#using-closures)
If you only need the functionality of a custom rule once throughout your application, you may use a closure instead of a rule object. The closure receives the attribute's name, the attribute's value, and a `$fail` callback that should be called if validation fails:
```


 1use Illuminate\Support\Facades\Validator;




 2use Closure;




 3 



 4$validator = Validator::make($request->all(), [




 5    'title' => [




 6        'required',




 7        'max:255',




 8        function (string $attribute, mixed $value, Closure $fail) {




 9            if ($value === 'foo') {




10                $fail("The {$attribute} is invalid.");




11            }




12        },




13    ],




14]);




use Illuminate\Support\Facades\Validator;
use Closure;

$validator = Validator::make($request->all(), [
    'title' => [
        'required',
        'max:255',
        function (string $attribute, mixed $value, Closure $fail) {
            if ($value === 'foo') {
                $fail("The {$attribute} is invalid.");
            }
        },
    ],
]);

```

### [Implicit Rules](https://laravel.com/docs/12.x/validation#implicit-rules)
By default, when an attribute being validated is not present or contains an empty string, normal validation rules, including custom rules, are not run. For example, the [unique](https://laravel.com/docs/12.x/validation#rule-unique) rule will not be run against an empty string:
```


1use Illuminate\Support\Facades\Validator;




2 



3$rules = ['name' => 'unique:users,name'];




4 



5$input = ['name' => ''];




6 



7Validator::make($input, $rules)->passes(); // true




use Illuminate\Support\Facades\Validator;

$rules = ['name' => 'unique:users,name'];

$input = ['name' => ''];

Validator::make($input, $rules)->passes(); // true

```

For a custom rule to run even when an attribute is empty, the rule must imply that the attribute is required. To quickly generate a new implicit rule object, you may use the `make:rule` Artisan command with the `--implicit` option:
```


1php artisan make:rule Uppercase --implicit




php artisan make:rule Uppercase --implicit

```

An "implicit" rule only _implies_ that the attribute is required. Whether it actually invalidates a missing or empty attribute is up to you.
Copy as markdown
  * [ Introduction ](https://laravel.com/docs/12.x/validation#introduction)
  * [ Validation Quickstart ](https://laravel.com/docs/12.x/validation#validation-quickstart)
    * [ Defining the Routes ](https://laravel.com/docs/12.x/validation#quick-defining-the-routes)
    * [ Creating the Controller ](https://laravel.com/docs/12.x/validation#quick-creating-the-controller)
    * [ Writing the Validation Logic ](https://laravel.com/docs/12.x/validation#quick-writing-the-validation-logic)
    * [ Displaying the Validation Errors ](https://laravel.com/docs/12.x/validation#quick-displaying-the-validation-errors)
    * [ Repopulating Forms ](https://laravel.com/docs/12.x/validation#repopulating-forms)
    * [ A Note on Optional Fields ](https://laravel.com/docs/12.x/validation#a-note-on-optional-fields)
    * [ Validation Error Response Format ](https://laravel.com/docs/12.x/validation#validation-error-response-format)
  * [ Form Request Validation ](https://laravel.com/docs/12.x/validation#form-request-validation)
    * [ Creating Form Requests ](https://laravel.com/docs/12.x/validation#creating-form-requests)
    * [ Authorizing Form Requests ](https://laravel.com/docs/12.x/validation#authorizing-form-requests)
    * [ Customizing the Error Messages ](https://laravel.com/docs/12.x/validation#customizing-the-error-messages)
    * [ Preparing Input for Validation ](https://laravel.com/docs/12.x/validation#preparing-input-for-validation)
  * [ Manually Creating Validators ](https://laravel.com/docs/12.x/validation#manually-creating-validators)
    * [ Automatic Redirection ](https://laravel.com/docs/12.x/validation#automatic-redirection)
    * [ Named Error Bags ](https://laravel.com/docs/12.x/validation#named-error-bags)
    * [ Customizing the Error Messages ](https://laravel.com/docs/12.x/validation#manual-customizing-the-error-messages)
    * [ Performing Additional Validation ](https://laravel.com/docs/12.x/validation#performing-additional-validation)
  * [ Working With Validated Input ](https://laravel.com/docs/12.x/validation#working-with-validated-input)
  * [ Working With Error Messages ](https://laravel.com/docs/12.x/validation#working-with-error-messages)
    * [ Specifying Custom Messages in Language Files ](https://laravel.com/docs/12.x/validation#specifying-custom-messages-in-language-files)
    * [ Specifying Attributes in Language Files ](https://laravel.com/docs/12.x/validation#specifying-attribute-in-language-files)
    * [ Specifying Values in Language Files ](https://laravel.com/docs/12.x/validation#specifying-values-in-language-files)
  * [ Available Validation Rules ](https://laravel.com/docs/12.x/validation#available-validation-rules)
  * [ Conditionally Adding Rules ](https://laravel.com/docs/12.x/validation#conditionally-adding-rules)
  * [ Validating Arrays ](https://laravel.com/docs/12.x/validation#validating-arrays)
    * [ Validating Nested Array Input ](https://laravel.com/docs/12.x/validation#validating-nested-array-input)
    * [ Error Message Indexes and Positions ](https://laravel.com/docs/12.x/validation#error-message-indexes-and-positions)
  * [ Validating Files ](https://laravel.com/docs/12.x/validation#validating-files)
  * [ Validating Passwords ](https://laravel.com/docs/12.x/validation#validating-passwords)
  * [ Custom Validation Rules ](https://laravel.com/docs/12.x/validation#custom-validation-rules)
    * [ Using Rule Objects ](https://laravel.com/docs/12.x/validation#using-rule-objects)
    * [ Using Closures ](https://laravel.com/docs/12.x/validation#using-closures)
    * [ Implicit Rules ](https://laravel.com/docs/12.x/validation#implicit-rules)


[ ![Laravel Forge](https://laravel.com/images/ads/forge-logo.svg) Server management made simple for any PHP app Learn more  ](https://forge.laravel.com)
[ ![Laravel Cloud](https://laravel.com/images/ads/cloud-logo.svg) The fastest way to deploy and scale Laravel apps Learn more  ](https://cloud.laravel.com)
[ ![Laravel Nightwatch](https://laravel.com/images/ads/nightwatch-logo.svg) First-class monitoring and deep insights for Laravel apps Learn more  ](https://nightwatch.laravel.com)
[ ![Laravel Boost](https://laravel.com/images/ads/boost-logo.svg) Supercharge your AI development with essential context Learn more  ](https://laravel.com/ai/boost)
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
  *   * [Active Logic](https://partners.laravel.com/partners/active-logic)
  * [Curotec](https://partners.laravel.com/partners/curotec)
  * [Jump24](https://partners.laravel.com/partners/jump24)
  * [Vehikl](https://partners.laravel.com/partners/vehikl)
  * [Kirschbaum](https://partners.laravel.com/partners/kirschbaum)
  * [Tighten](https://partners.laravel.com/partners/tighten)
  * [Redberry](https://partners.laravel.com/partners/redberry)
  * [byte5](https://partners.laravel.com/partners/byte5)
  * [ More Partners ](https://partners.laravel.com)
