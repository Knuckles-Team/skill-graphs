## [Testing](https://laravel.com/docs/12.x/pennant#testing)
When testing code that interacts with feature flags, the easiest way to control the feature flag's returned value in your tests is to simply re-define the feature. For example, imagine you have the following feature defined in one of your application's service provider:
```


1use Illuminate\Support\Arr;




2use Laravel\Pennant\Feature;




3 



4Feature::define('purchase-button', fn () => Arr::random([




5    'blue-sapphire',




6    'seafoam-green',




7    'tart-orange',




8]));




use Illuminate\Support\Arr;
use Laravel\Pennant\Feature;

Feature::define('purchase-button', fn () => Arr::random([
    'blue-sapphire',
    'seafoam-green',
    'tart-orange',
]));

```

To modify the feature's returned value in your tests, you may re-define the feature at the beginning of the test. The following test will always pass, even though the `Arr::random()` implementation is still present in the service provider:
Pest PHPUnit
```


1use Laravel\Pennant\Feature;




2 



3test('it can control feature values', function () {




4    Feature::define('purchase-button', 'seafoam-green');




5 



6    expect(Feature::value('purchase-button'))->toBe('seafoam-green');




7});




use Laravel\Pennant\Feature;

test('it can control feature values', function () {
    Feature::define('purchase-button', 'seafoam-green');

    expect(Feature::value('purchase-button'))->toBe('seafoam-green');
});

```

```


1use Laravel\Pennant\Feature;




2 



3public function test_it_can_control_feature_values()




4{




5    Feature::define('purchase-button', 'seafoam-green');




6 



7    $this->assertSame('seafoam-green', Feature::value('purchase-button'));




8}




use Laravel\Pennant\Feature;

public function test_it_can_control_feature_values()
{
    Feature::define('purchase-button', 'seafoam-green');

    $this->assertSame('seafoam-green', Feature::value('purchase-button'));
}

```

The same approach may be used for class-based features:
Pest PHPUnit
```


1use Laravel\Pennant\Feature;




2 



3test('it can control feature values', function () {




4    Feature::define(NewApi::class, true);




5 



6    expect(Feature::value(NewApi::class))->toBeTrue();




7});




use Laravel\Pennant\Feature;

test('it can control feature values', function () {
    Feature::define(NewApi::class, true);

    expect(Feature::value(NewApi::class))->toBeTrue();
});

```

```


1use App\Features\NewApi;




2use Laravel\Pennant\Feature;




3 



4public function test_it_can_control_feature_values()




5{




6    Feature::define(NewApi::class, true);




7 



8    $this->assertTrue(Feature::value(NewApi::class));




9}




use App\Features\NewApi;
use Laravel\Pennant\Feature;

public function test_it_can_control_feature_values()
{
    Feature::define(NewApi::class, true);

    $this->assertTrue(Feature::value(NewApi::class));
}

```

If your feature is returning a `Lottery` instance, there are a handful of useful [testing helpers available](https://laravel.com/docs/12.x/helpers#testing-lotteries).
#### [Store Configuration](https://laravel.com/docs/12.x/pennant#store-configuration)
You may configure the store that Pennant will use during testing by defining the `PENNANT_STORE` environment variable in your application's `phpunit.xml` file:
```


1<?xml version="1.0" encoding="UTF-8"?>




2<phpunit colors="true">




3    <!-- ... -->




4    <php>




5        <env name="PENNANT_STORE" value="array"/>




6        <!-- ... -->




7    </php>




8</phpunit>




<?xml version="1.0" encoding="UTF-8"?>
<phpunit colors="true">
    <!-- ... -->
    <php>
        <env name="PENNANT_STORE" value="array"/>
        <!-- ... -->
    </php>
</phpunit>

```
