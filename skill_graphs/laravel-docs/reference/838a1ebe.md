## [Components](https://laravel.com/docs/12.x/dusk#components)
Components are similar to Dusk's "page objects", but are intended for pieces of UI and functionality that are reused throughout your application, such as a navigation bar or notification window. As such, components are not bound to specific URLs.
### [Generating Components](https://laravel.com/docs/12.x/dusk#generating-components)
To generate a component, execute the `dusk:component` Artisan command. New components are placed in the `tests/Browser/Components` directory:
```


1php artisan dusk:component DatePicker




php artisan dusk:component DatePicker

```

As shown above, a "date picker" is an example of a component that might exist throughout your application on a variety of pages. It can become cumbersome to manually write the browser automation logic to select a date in dozens of tests throughout your test suite. Instead, we can define a Dusk component to represent the date picker, allowing us to encapsulate that logic within the component:
```


 1<?php




 2 



 3namespace Tests\Browser\Components;




 4 



 5use Laravel\Dusk\Browser;




 6use Laravel\Dusk\Component as BaseComponent;




 7 



 8class DatePicker extends BaseComponent




 9{




10    /**




11     * Get the root selector for the component.




12     */




13    public function selector(): string




14    {




15        return '.date-picker';




16    }




17 



18    /**




19     * Assert that the browser page contains the component.




20     */




21    public function assert(Browser $browser): void




22    {




23        $browser->assertVisible($this->selector());




24    }




25 



26    /**




27     * Get the element shortcuts for the component.




28     *




29     * @return array<string, string>




30     */




31    public function elements(): array




32    {




33        return [




34            '@date-field' => 'input.datepicker-input',




35            '@year-list' => 'div > div.datepicker-years',




36            '@month-list' => 'div > div.datepicker-months',




37            '@day-list' => 'div > div.datepicker-days',




38        ];




39    }




40 



41    /**




42     * Select the given date.




43     */




44    public function selectDate(Browser $browser, int $year, int $month, int $day): void




45    {




46        $browser->click('@date-field')




47            ->within('@year-list', function (Browser $browser) use ($year) {




48                $browser->click($year);




49            })




50            ->within('@month-list', function (Browser $browser) use ($month) {




51                $browser->click($month);




52            })




53            ->within('@day-list', function (Browser $browser) use ($day) {




54                $browser->click($day);




55            });




56    }




57}




<?php

namespace Tests\Browser\Components;

use Laravel\Dusk\Browser;
use Laravel\Dusk\Component as BaseComponent;

class DatePicker extends BaseComponent
{
    /**
     * Get the root selector for the component.
     */
    public function selector(): string
    {
        return '.date-picker';
    }

    /**
     * Assert that the browser page contains the component.
     */
    public function assert(Browser $browser): void
    {
        $browser->assertVisible($this->selector());
    }

    /**
     * Get the element shortcuts for the component.
     *
     * @return array<string, string>
     */
    public function elements(): array
    {
        return [
            '@date-field' => 'input.datepicker-input',
            '@year-list' => 'div > div.datepicker-years',
            '@month-list' => 'div > div.datepicker-months',
            '@day-list' => 'div > div.datepicker-days',
        ];
    }

    /**
     * Select the given date.
     */
    public function selectDate(Browser $browser, int $year, int $month, int $day): void
    {
        $browser->click('@date-field')
            ->within('@year-list', function (Browser $browser) use ($year) {
                $browser->click($year);
            })
            ->within('@month-list', function (Browser $browser) use ($month) {
                $browser->click($month);
            })
            ->within('@day-list', function (Browser $browser) use ($day) {
                $browser->click($day);
            });
    }
}

```

### [Using Components](https://laravel.com/docs/12.x/dusk#using-components)
Once the component has been defined, we can easily select a date within the date picker from any test. And, if the logic necessary to select a date changes, we only need to update the component:
Pest PHPUnit
```


 1<?php




 2 



 3use Illuminate\Foundation\Testing\DatabaseMigrations;




 4use Laravel\Dusk\Browser;




 5use Tests\Browser\Components\DatePicker;




 6 



 7pest()->use(DatabaseMigrations::class);




 8 



 9test('basic example', function () {




10    $this->browse(function (Browser $browser) {




11        $browser->visit('/')




12            ->within(new DatePicker, function (Browser $browser) {




13                $browser->selectDate(2019, 1, 30);




14            })




15            ->assertSee('January');




16    });




17});




<?php

use Illuminate\Foundation\Testing\DatabaseMigrations;
use Laravel\Dusk\Browser;
use Tests\Browser\Components\DatePicker;

pest()->use(DatabaseMigrations::class);

test('basic example', function () {
    $this->browse(function (Browser $browser) {
        $browser->visit('/')
            ->within(new DatePicker, function (Browser $browser) {
                $browser->selectDate(2019, 1, 30);
            })
            ->assertSee('January');
    });
});

```

```


 1<?php




 2 



 3namespace Tests\Browser;




 4 



 5use Illuminate\Foundation\Testing\DatabaseMigrations;




 6use Laravel\Dusk\Browser;




 7use Tests\Browser\Components\DatePicker;




 8use Tests\DuskTestCase;




 9 



10class ExampleTest extends DuskTestCase




11{




12    /**




13     * A basic component test example.




14     */




15    public function test_basic_example(): void




16    {




17        $this->browse(function (Browser $browser) {




18            $browser->visit('/')




19                ->within(new DatePicker, function (Browser $browser) {




20                    $browser->selectDate(2019, 1, 30);




21                })




22                ->assertSee('January');




23        });




24    }




25}




<?php

namespace Tests\Browser;

use Illuminate\Foundation\Testing\DatabaseMigrations;
use Laravel\Dusk\Browser;
use Tests\Browser\Components\DatePicker;
use Tests\DuskTestCase;

class ExampleTest extends DuskTestCase
{
    /**
     * A basic component test example.
     */
    public function test_basic_example(): void
    {
        $this->browse(function (Browser $browser) {
            $browser->visit('/')
                ->within(new DatePicker, function (Browser $browser) {
                    $browser->selectDate(2019, 1, 30);
                })
                ->assertSee('January');
        });
    }
}

```

The `component` method may be used to retrieve a browser instance scoped to the given component:
```


1$datePicker = $browser->component(new DatePickerComponent);




2 



3$datePicker->selectDate(2019, 1, 30);




4 



5$datePicker->assertSee('January');




$datePicker = $browser->component(new DatePickerComponent);

$datePicker->selectDate(2019, 1, 30);

$datePicker->assertSee('January');

```
