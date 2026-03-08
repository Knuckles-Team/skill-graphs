```


1use Illuminate\Support\Str;




2 



3$string = Str::trim(' foo bar ');




4 



5// 'foo bar'




use Illuminate\Support\Str;

$string = Str::trim(' foo bar ');

// 'foo bar'

```

#### [`Str::ltrim()`](https://laravel.com/docs/12.x/strings#method-str-ltrim)
The `Str::ltrim` method strips whitespace (or other characters) from the beginning of the given string. Unlike PHP's native `ltrim` function, the `Str::ltrim` method also removes unicode whitespace characters:
```


1use Illuminate\Support\Str;




2 



3$string = Str::ltrim('  foo bar  ');




4 



5// 'foo bar  '




use Illuminate\Support\Str;

$string = Str::ltrim('  foo bar  ');

// 'foo bar  '

```

#### [`Str::rtrim()`](https://laravel.com/docs/12.x/strings#method-str-rtrim)
The `Str::rtrim` method strips whitespace (or other characters) from the end of the given string. Unlike PHP's native `rtrim` function, the `Str::rtrim` method also removes unicode whitespace characters:
```


1use Illuminate\Support\Str;




2 



3$string = Str::rtrim('  foo bar  ');




4 



5// '  foo bar'




use Illuminate\Support\Str;

$string = Str::rtrim('  foo bar  ');

// '  foo bar'

```

#### [`Str::ucfirst()`](https://laravel.com/docs/12.x/strings#method-str-ucfirst)
The `Str::ucfirst` method returns the given string with the first character capitalized:
```


1use Illuminate\Support\Str;




2 



3$string = Str::ucfirst('foo bar');




4 



5// Foo bar




use Illuminate\Support\Str;

$string = Str::ucfirst('foo bar');

// Foo bar

```

#### [`Str::ucsplit()`](https://laravel.com/docs/12.x/strings#method-str-ucsplit)
The `Str::ucsplit` method splits the given string into an array by uppercase characters:
```


1use Illuminate\Support\Str;




2 



3$segments = Str::ucsplit('FooBar');




4 



5// [0 => 'Foo', 1 => 'Bar']




use Illuminate\Support\Str;

$segments = Str::ucsplit('FooBar');

// [0 => 'Foo', 1 => 'Bar']

```

#### [`Str::ucwords()`](https://laravel.com/docs/12.x/strings#method-str-ucwords)
The `Str::ucwords` method converts the first character of each word in the given string to uppercase:
```


1use Illuminate\Support\Str;




2 



3$string = Str::ucwords('laravel framework');




4 



5// Laravel Framework




use Illuminate\Support\Str;

$string = Str::ucwords('laravel framework');

// Laravel Framework

```

#### [`Str::upper()`](https://laravel.com/docs/12.x/strings#method-str-upper)
The `Str::upper` method converts the given string to uppercase:
```


1use Illuminate\Support\Str;




2 



3$string = Str::upper('laravel');




4 



5// LARAVEL




use Illuminate\Support\Str;

$string = Str::upper('laravel');

// LARAVEL

```

#### [`Str::ulid()`](https://laravel.com/docs/12.x/strings#method-str-ulid)
The `Str::ulid` method generates a ULID, which is a compact, time-ordered unique identifier:
```


1use Illuminate\Support\Str;




2 



3return (string) Str::ulid();




4 



5// 01gd6r360bp37zj17nxb55yv40




use Illuminate\Support\Str;

return (string) Str::ulid();

// 01gd6r360bp37zj17nxb55yv40

```

If you would like to retrieve a `Illuminate\Support\Carbon` date instance representing the date and time that a given ULID was created, you may use the `createFromId` method provided by Laravel's Carbon integration:
```


1use Illuminate\Support\Carbon;




2use Illuminate\Support\Str;




3 



4$date = Carbon::createFromId((string) Str::ulid());




use Illuminate\Support\Carbon;
use Illuminate\Support\Str;

$date = Carbon::createFromId((string) Str::ulid());

```

During testing, it may be useful to "fake" the value that is returned by the `Str::ulid` method. To accomplish this, you may use the `createUlidsUsing` method:
```


1use Symfony\Component\Uid\Ulid;




2 



3Str::createUlidsUsing(function () {




4    return new Ulid('01HRDBNHHCKNW2AK4Z29SN82T9');




5});




use Symfony\Component\Uid\Ulid;

Str::createUlidsUsing(function () {
    return new Ulid('01HRDBNHHCKNW2AK4Z29SN82T9');
});

```

To instruct the `ulid` method to return to generating ULIDs normally, you may invoke the `createUlidsNormally` method:
```


1Str::createUlidsNormally();




Str::createUlidsNormally();

```

#### [`Str::unwrap()`](https://laravel.com/docs/12.x/strings#method-str-unwrap)
The `Str::unwrap` method removes the specified strings from the beginning and end of a given string:
```


1use Illuminate\Support\Str;




2 



3Str::unwrap('-Laravel-', '-');




4 



5// Laravel




6 



7Str::unwrap('{framework: "Laravel"}', '{', '}');




8 



9// framework: "Laravel"




use Illuminate\Support\Str;

Str::unwrap('-Laravel-', '-');

// Laravel

Str::unwrap('{framework: "Laravel"}', '{', '}');

// framework: "Laravel"

```

#### [`Str::uuid()`](https://laravel.com/docs/12.x/strings#method-str-uuid)
The `Str::uuid` method generates a UUID (version 4):
```


1use Illuminate\Support\Str;




2 



3return (string) Str::uuid();




use Illuminate\Support\Str;

return (string) Str::uuid();

```

During testing, it may be useful to "fake" the value that is returned by the `Str::uuid` method. To accomplish this, you may use the `createUuidsUsing` method:
```


1use Ramsey\Uuid\Uuid;




2 



3Str::createUuidsUsing(function () {




4    return Uuid::fromString('eadbfeac-5258-45c2-bab7-ccb9b5ef74f9');




5});




use Ramsey\Uuid\Uuid;

Str::createUuidsUsing(function () {
    return Uuid::fromString('eadbfeac-5258-45c2-bab7-ccb9b5ef74f9');
});

```

To instruct the `uuid` method to return to generating UUIDs normally, you may invoke the `createUuidsNormally` method:
```


1Str::createUuidsNormally();




Str::createUuidsNormally();

```

#### [`Str::uuid7()`](https://laravel.com/docs/12.x/strings#method-str-uuid7)
The `Str::uuid7` method generates a UUID (version 7):
```


1use Illuminate\Support\Str;




2 



3return (string) Str::uuid7();




use Illuminate\Support\Str;

return (string) Str::uuid7();

```

A `DateTimeInterface` may be passed as an optional parameter which will be used to generate the ordered UUID:
```


1return (string) Str::uuid7(time: now());




return (string) Str::uuid7(time: now());

```

#### [`Str::wordCount()`](https://laravel.com/docs/12.x/strings#method-str-word-count)
The `Str::wordCount` method returns the number of words that a string contains:
```


1use Illuminate\Support\Str;




2 



3Str::wordCount('Hello, world!'); // 2




use Illuminate\Support\Str;

Str::wordCount('Hello, world!'); // 2

```

#### [`Str::wordWrap()`](https://laravel.com/docs/12.x/strings#method-str-word-wrap)
The `Str::wordWrap` method wraps a string to a given number of characters:
```


 1use Illuminate\Support\Str;




 2 



 3$text = "The quick brown fox jumped over the lazy dog."




 4 



 5Str::wordWrap($text, characters: 20, break: "<br />\n");




 6 



 7/*




 8The quick brown fox<br />




 9jumped over the lazy<br />




10dog.




11*/




use Illuminate\Support\Str;

$text = "The quick brown fox jumped over the lazy dog."

Str::wordWrap($text, characters: 20, break: "<br />\n");

/*
The quick brown fox<br />
jumped over the lazy<br />
dog.
*/

```

#### [`Str::words()`](https://laravel.com/docs/12.x/strings#method-str-words)
The `Str::words` method limits the number of words in a string. An additional string may be passed to this method via its third argument to specify which string should be appended to the end of the truncated string:
```


1use Illuminate\Support\Str;




2 



3return Str::words('Perfectly balanced, as all things should be.', 3, ' >>>');




4 



5// Perfectly balanced, as >>>




use Illuminate\Support\Str;

return Str::words('Perfectly balanced, as all things should be.', 3, ' >>>');

// Perfectly balanced, as >>>

```

#### [`Str::wrap()`](https://laravel.com/docs/12.x/strings#method-str-wrap)
The `Str::wrap` method wraps the given string with an additional string or pair of strings:
```


1use Illuminate\Support\Str;




2 



3Str::wrap('Laravel', '"');




4 



5// "Laravel"




6 



7Str::wrap('is', before: 'This ', after: ' Laravel!');




8 



9// This is Laravel!




use Illuminate\Support\Str;

Str::wrap('Laravel', '"');

// "Laravel"

Str::wrap('is', before: 'This ', after: ' Laravel!');

// This is Laravel!

```

#### [`str()`](https://laravel.com/docs/12.x/strings#method-str)
The `str` function returns a new `Illuminate\Support\Stringable` instance of the given string. This function is equivalent to the `Str::of` method:
```


1$string = str('Taylor')->append(' Otwell');




2 



3// 'Taylor Otwell'




$string = str('Taylor')->append(' Otwell');

// 'Taylor Otwell'

```

If no argument is provided to the `str` function, the function returns an instance of `Illuminate\Support\Str`:
```


1$snake = str()->snake('FooBar');




2 



3// 'foo_bar'




$snake = str()->snake('FooBar');

// 'foo_bar'

```

#### [`trans()`](https://laravel.com/docs/12.x/strings#method-trans)
The `trans` function translates the given translation key using your [language files](https://laravel.com/docs/12.x/localization):
```


1echo trans('messages.welcome');




echo trans('messages.welcome');

```

If the specified translation key does not exist, the `trans` function will return the given key. So, using the example above, the `trans` function would return `messages.welcome` if the translation key does not exist.
#### [`trans_choice()`](https://laravel.com/docs/12.x/strings#method-trans-choice)
The `trans_choice` function translates the given translation key with inflection:
```


1echo trans_choice('messages.notifications', $unreadCount);




echo trans_choice('messages.notifications', $unreadCount);

```

If the specified translation key does not exist, the `trans_choice` function will return the given key. So, using the example above, the `trans_choice` function would return `messages.notifications` if the translation key does not exist.
