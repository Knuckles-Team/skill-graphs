## [Numbers](https://laravel.com/docs/12.x/helpers#numbers)
#### [`Number::abbreviate()`](https://laravel.com/docs/12.x/helpers#method-number-abbreviate)
The `Number::abbreviate` method returns the human-readable format of the provided numerical value, with an abbreviation for the units:
```


 1use Illuminate\Support\Number;




 2 



 3$number = Number::abbreviate(1000);




 4 



 5// 1K




 6 



 7$number = Number::abbreviate(489939);




 8 



 9// 490K




10 



11$number = Number::abbreviate(1230000, precision: 2);




12 



13// 1.23M




use Illuminate\Support\Number;

$number = Number::abbreviate(1000);

// 1K

$number = Number::abbreviate(489939);

// 490K

$number = Number::abbreviate(1230000, precision: 2);

// 1.23M

```

#### [`Number::clamp()`](https://laravel.com/docs/12.x/helpers#method-number-clamp)
The `Number::clamp` method ensures a given number stays within a specified range. If the number is lower than the minimum, the minimum value is returned. If the number is higher than the maximum, the maximum value is returned:
```


 1use Illuminate\Support\Number;




 2 



 3$number = Number::clamp(105, min: 10, max: 100);




 4 



 5// 100




 6 



 7$number = Number::clamp(5, min: 10, max: 100);




 8 



 9// 10




10 



11$number = Number::clamp(10, min: 10, max: 100);




12 



13// 10




14 



15$number = Number::clamp(20, min: 10, max: 100);




16 



17// 20




use Illuminate\Support\Number;

$number = Number::clamp(105, min: 10, max: 100);

// 100

$number = Number::clamp(5, min: 10, max: 100);

// 10

$number = Number::clamp(10, min: 10, max: 100);

// 10

$number = Number::clamp(20, min: 10, max: 100);

// 20

```

#### [`Number::currency()`](https://laravel.com/docs/12.x/helpers#method-number-currency)
The `Number::currency` method returns the currency representation of the given value as a string:
```


 1use Illuminate\Support\Number;




 2 



 3$currency = Number::currency(1000);




 4 



 5// $1,000.00




 6 



 7$currency = Number::currency(1000, in: 'EUR');




 8 



 9// €1,000.00




10 



11$currency = Number::currency(1000, in: 'EUR', locale: 'de');




12 



13// 1.000,00 €




14 



15$currency = Number::currency(1000, in: 'EUR', locale: 'de', precision: 0);




16 



17// 1.000 €




use Illuminate\Support\Number;

$currency = Number::currency(1000);

// $1,000.00

$currency = Number::currency(1000, in: 'EUR');

// €1,000.00

$currency = Number::currency(1000, in: 'EUR', locale: 'de');

// 1.000,00 €

$currency = Number::currency(1000, in: 'EUR', locale: 'de', precision: 0);

// 1.000 €

```

#### [`Number::defaultCurrency()`](https://laravel.com/docs/12.x/helpers#method-default-currency)
The `Number::defaultCurrency` method returns the default currency being used by the `Number` class:
```


1use Illuminate\Support\Number;




2 



3$currency = Number::defaultCurrency();




4 



5// USD




use Illuminate\Support\Number;

$currency = Number::defaultCurrency();

// USD

```

#### [`Number::defaultLocale()`](https://laravel.com/docs/12.x/helpers#method-default-locale)
The `Number::defaultLocale` method returns the default locale being used by the `Number` class:
```


1use Illuminate\Support\Number;




2 



3$locale = Number::defaultLocale();




4 



5// en




use Illuminate\Support\Number;

$locale = Number::defaultLocale();

// en

```

#### [`Number::fileSize()`](https://laravel.com/docs/12.x/helpers#method-number-file-size)
The `Number::fileSize` method returns the file size representation of the given byte value as a string:
```


 1use Illuminate\Support\Number;




 2 



 3$size = Number::fileSize(1024);




 4 



 5// 1 KB




 6 



 7$size = Number::fileSize(1024 * 1024);




 8 



 9// 1 MB




10 



11$size = Number::fileSize(1024, precision: 2);




12 



13// 1.00 KB




use Illuminate\Support\Number;

$size = Number::fileSize(1024);

// 1 KB

$size = Number::fileSize(1024 * 1024);

// 1 MB

$size = Number::fileSize(1024, precision: 2);

// 1.00 KB

```

#### [`Number::forHumans()`](https://laravel.com/docs/12.x/helpers#method-number-for-humans)
The `Number::forHumans` method returns the human-readable format of the provided numerical value:
```


 1use Illuminate\Support\Number;




 2 



 3$number = Number::forHumans(1000);




 4 



 5// 1 thousand




 6 



 7$number = Number::forHumans(489939);




 8 



 9// 490 thousand




10 



11$number = Number::forHumans(1230000, precision: 2);




12 



13// 1.23 million




use Illuminate\Support\Number;

$number = Number::forHumans(1000);

// 1 thousand

$number = Number::forHumans(489939);

// 490 thousand

$number = Number::forHumans(1230000, precision: 2);

// 1.23 million

```

#### [`Number::format()`](https://laravel.com/docs/12.x/helpers#method-number-format)
The `Number::format` method formats the given number into a locale specific string:
```


 1use Illuminate\Support\Number;




 2 



 3$number = Number::format(100000);




 4 



 5// 100,000




 6 



 7$number = Number::format(100000, precision: 2);




 8 



 9// 100,000.00




10 



11$number = Number::format(100000.123, maxPrecision: 2);




12 



13// 100,000.12




14 



15$number = Number::format(100000, locale: 'de');




16 



17// 100.000




use Illuminate\Support\Number;

$number = Number::format(100000);

// 100,000

$number = Number::format(100000, precision: 2);

// 100,000.00

$number = Number::format(100000.123, maxPrecision: 2);

// 100,000.12

$number = Number::format(100000, locale: 'de');

// 100.000

```

#### [`Number::ordinal()`](https://laravel.com/docs/12.x/helpers#method-number-ordinal)
The `Number::ordinal` method returns a number's ordinal representation:
```


 1use Illuminate\Support\Number;




 2 



 3$number = Number::ordinal(1);




 4 



 5// 1st




 6 



 7$number = Number::ordinal(2);




 8 



 9// 2nd




10 



11$number = Number::ordinal(21);




12 



13// 21st




use Illuminate\Support\Number;

$number = Number::ordinal(1);

// 1st

$number = Number::ordinal(2);

// 2nd

$number = Number::ordinal(21);

// 21st

```

#### [`Number::pairs()`](https://laravel.com/docs/12.x/helpers#method-number-pairs)
The `Number::pairs` method generates an array of number pairs (sub-ranges) based on a specified range and step value. This method can be useful for dividing a larger range of numbers into smaller, manageable sub-ranges for things like pagination or batching tasks. The `pairs` method returns an array of arrays, where each inner array represents a pair (sub-range) of numbers:
```


1use Illuminate\Support\Number;




2 



3$result = Number::pairs(25, 10);




4 



5// [[0, 9], [10, 19], [20, 25]]




6 



7$result = Number::pairs(25, 10, offset: 0);




8 



9// [[0, 10], [10, 20], [20, 25]]




use Illuminate\Support\Number;

$result = Number::pairs(25, 10);

// [[0, 9], [10, 19], [20, 25]]

$result = Number::pairs(25, 10, offset: 0);

// [[0, 10], [10, 20], [20, 25]]

```

#### [`Number::parseInt()`](https://laravel.com/docs/12.x/helpers#method-number-parse-int)
The `Number::parseInt` method parse a string into an integer according to the specified locale:
```


1use Illuminate\Support\Number;




2 



3$result = Number::parseInt('10.123');




4 



5// (int) 10




6 



7$result = Number::parseInt('10,123', locale: 'fr');




8 



9// (int) 10




use Illuminate\Support\Number;

$result = Number::parseInt('10.123');

// (int) 10

$result = Number::parseInt('10,123', locale: 'fr');

// (int) 10

```

#### [`Number::parseFloat()`](https://laravel.com/docs/12.x/helpers#method-number-parse-float)
The `Number::parseFloat` method parse a string into a float according to the specified locale:
```


1use Illuminate\Support\Number;




2 



3$result = Number::parseFloat('10');




4 



5// (float) 10.0




6 



7$result = Number::parseFloat('10', locale: 'fr');




8 



9// (float) 10.0




use Illuminate\Support\Number;

$result = Number::parseFloat('10');

// (float) 10.0

$result = Number::parseFloat('10', locale: 'fr');

// (float) 10.0

```

#### [`Number::percentage()`](https://laravel.com/docs/12.x/helpers#method-number-percentage)
The `Number::percentage` method returns the percentage representation of the given value as a string:
```


 1use Illuminate\Support\Number;




 2 



 3$percentage = Number::percentage(10);




 4 



 5// 10%




 6 



 7$percentage = Number::percentage(10, precision: 2);




 8 



 9// 10.00%




10 



11$percentage = Number::percentage(10.123, maxPrecision: 2);




12 



13// 10.12%




14 



15$percentage = Number::percentage(10, precision: 2, locale: 'de');




16 



17// 10,00%




use Illuminate\Support\Number;

$percentage = Number::percentage(10);

// 10%

$percentage = Number::percentage(10, precision: 2);

// 10.00%

$percentage = Number::percentage(10.123, maxPrecision: 2);

// 10.12%

$percentage = Number::percentage(10, precision: 2, locale: 'de');

// 10,00%

```

#### [`Number::spell()`](https://laravel.com/docs/12.x/helpers#method-number-spell)
The `Number::spell` method transforms the given number into a string of words:
```


1use Illuminate\Support\Number;




2 



3$number = Number::spell(102);




4 



5// one hundred and two




6 



7$number = Number::spell(88, locale: 'fr');




8 



9// quatre-vingt-huit




use Illuminate\Support\Number;

$number = Number::spell(102);

// one hundred and two

$number = Number::spell(88, locale: 'fr');

// quatre-vingt-huit

```

The `after` argument allows you to specify a value after which all numbers should be spelled out:
```


1$number = Number::spell(10, after: 10);




2 



3// 10




4 



5$number = Number::spell(11, after: 10);




6 



7// eleven




$number = Number::spell(10, after: 10);

// 10

$number = Number::spell(11, after: 10);

// eleven

```

The `until` argument allows you to specify a value before which all numbers should be spelled out:
```


1$number = Number::spell(5, until: 10);




2 



3// five




4 



5$number = Number::spell(10, until: 10);




6 



7// 10




$number = Number::spell(5, until: 10);

// five

$number = Number::spell(10, until: 10);

// 10

```

#### [`Number::spellOrdinal()`](https://laravel.com/docs/12.x/helpers#method-number-spell-ordinal)
The `Number::spellOrdinal` method returns the number's ordinal representation as a string of words:
```


 1use Illuminate\Support\Number;




 2 



 3$number = Number::spellOrdinal(1);




 4 



 5// first




 6 



 7$number = Number::spellOrdinal(2);




 8 



 9// second




10 



11$number = Number::spellOrdinal(21);




12 



13// twenty-first




use Illuminate\Support\Number;

$number = Number::spellOrdinal(1);

// first

$number = Number::spellOrdinal(2);

// second

$number = Number::spellOrdinal(21);

// twenty-first

```

#### [`Number::trim()`](https://laravel.com/docs/12.x/helpers#method-number-trim)
The `Number::trim` method removes any trailing zero digits after the decimal point of the given number:
```


1use Illuminate\Support\Number;




2 



3$number = Number::trim(12.0);




4 



5// 12




6 



7$number = Number::trim(12.30);




8 



9// 12.3




use Illuminate\Support\Number;

$number = Number::trim(12.0);

// 12

$number = Number::trim(12.30);

// 12.3

```

#### [`Number::useLocale()`](https://laravel.com/docs/12.x/helpers#method-number-use-locale)
The `Number::useLocale` method sets the default number locale globally, which affects how numbers and currency are formatted by subsequent invocations to the `Number` class's methods:
```


1use Illuminate\Support\Number;




2 



3/**




4 * Bootstrap any application services.




5 */




6public function boot(): void




7{




8    Number::useLocale('de');




9}




use Illuminate\Support\Number;

/**
 * Bootstrap any application services.
 */
public function boot(): void
{
    Number::useLocale('de');
}

```

#### [`Number::withLocale()`](https://laravel.com/docs/12.x/helpers#method-number-with-locale)
The `Number::withLocale` method executes the given closure using the specified locale and then restores the original locale after the callback has executed:
```


1use Illuminate\Support\Number;




2 



3$number = Number::withLocale('de', function () {




4    return Number::format(1500);




5});




use Illuminate\Support\Number;

$number = Number::withLocale('de', function () {
    return Number::format(1500);
});

```

#### [`Number::useCurrency()`](https://laravel.com/docs/12.x/helpers#method-number-use-currency)
The `Number::useCurrency` method sets the default number currency globally, which affects how the currency is formatted by subsequent invocations to the `Number` class's methods:
```


1use Illuminate\Support\Number;




2 



3/**




4 * Bootstrap any application services.




5 */




6public function boot(): void




7{




8    Number::useCurrency('GBP');




9}




use Illuminate\Support\Number;

/**
 * Bootstrap any application services.
 */
public function boot(): void
{
    Number::useCurrency('GBP');
}

```

#### [`Number::withCurrency()`](https://laravel.com/docs/12.x/helpers#method-number-with-currency)
The `Number::withCurrency` method executes the given closure using the specified currency and then restores the original currency after the callback has executed:
```


1use Illuminate\Support\Number;




2 



3$number = Number::withCurrency('GBP', function () {




4    // ...




5});




use Illuminate\Support\Number;

$number = Number::withCurrency('GBP', function () {
    // ...
});

```
