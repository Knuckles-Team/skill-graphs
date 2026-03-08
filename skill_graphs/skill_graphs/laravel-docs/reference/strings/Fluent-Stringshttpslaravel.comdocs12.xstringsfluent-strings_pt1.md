## [Fluent Strings](https://laravel.com/docs/12.x/strings#fluent-strings)
Fluent strings provide a more fluent, object-oriented interface for working with string values, allowing you to chain multiple string operations together using a more readable syntax compared to traditional string operations.
#### [`after`](https://laravel.com/docs/12.x/strings#method-fluent-str-after)
The `after` method returns everything after the given value in a string. The entire string will be returned if the value does not exist within the string:
```


1use Illuminate\Support\Str;




2 



3$slice = Str::of('This is my name')->after('This is');




4 



5// ' my name'




use Illuminate\Support\Str;

$slice = Str::of('This is my name')->after('This is');

// ' my name'

```

#### [`afterLast`](https://laravel.com/docs/12.x/strings#method-fluent-str-after-last)
The `afterLast` method returns everything after the last occurrence of the given value in a string. The entire string will be returned if the value does not exist within the string:
```


1use Illuminate\Support\Str;




2 



3$slice = Str::of('App\Http\Controllers\Controller')->afterLast('\\');




4 



5// 'Controller'




use Illuminate\Support\Str;

$slice = Str::of('App\Http\Controllers\Controller')->afterLast('\\');

// 'Controller'

```

#### [`apa`](https://laravel.com/docs/12.x/strings#method-fluent-str-apa)
The `apa` method converts the given string to title case following the
```


1use Illuminate\Support\Str;




2 



3$converted = Str::of('a nice title uses the correct case')->apa();




4 



5// A Nice Title Uses the Correct Case




use Illuminate\Support\Str;

$converted = Str::of('a nice title uses the correct case')->apa();

// A Nice Title Uses the Correct Case

```

#### [`append`](https://laravel.com/docs/12.x/strings#method-fluent-str-append)
The `append` method appends the given values to the string:
```


1use Illuminate\Support\Str;




2 



3$string = Str::of('Taylor')->append(' Otwell');




4 



5// 'Taylor Otwell'




use Illuminate\Support\Str;

$string = Str::of('Taylor')->append(' Otwell');

// 'Taylor Otwell'

```

#### [`ascii`](https://laravel.com/docs/12.x/strings#method-fluent-str-ascii)
The `ascii` method will attempt to transliterate the string into an ASCII value:
```


1use Illuminate\Support\Str;




2 



3$string = Str::of('ü')->ascii();




4 



5// 'u'




use Illuminate\Support\Str;

$string = Str::of('ü')->ascii();

// 'u'

```

#### [`basename`](https://laravel.com/docs/12.x/strings#method-fluent-str-basename)
The `basename` method will return the trailing name component of the given string:
```


1use Illuminate\Support\Str;




2 



3$string = Str::of('/foo/bar/baz')->basename();




4 



5// 'baz'




use Illuminate\Support\Str;

$string = Str::of('/foo/bar/baz')->basename();

// 'baz'

```

If needed, you may provide an "extension" that will be removed from the trailing component:
```


1use Illuminate\Support\Str;




2 



3$string = Str::of('/foo/bar/baz.jpg')->basename('.jpg');




4 



5// 'baz'




use Illuminate\Support\Str;

$string = Str::of('/foo/bar/baz.jpg')->basename('.jpg');

// 'baz'

```

#### [`before`](https://laravel.com/docs/12.x/strings#method-fluent-str-before)
The `before` method returns everything before the given value in a string:
```


1use Illuminate\Support\Str;




2 



3$slice = Str::of('This is my name')->before('my name');




4 



5// 'This is '




use Illuminate\Support\Str;

$slice = Str::of('This is my name')->before('my name');

// 'This is '

```

#### [`beforeLast`](https://laravel.com/docs/12.x/strings#method-fluent-str-before-last)
The `beforeLast` method returns everything before the last occurrence of the given value in a string:
```


1use Illuminate\Support\Str;




2 



3$slice = Str::of('This is my name')->beforeLast('is');




4 



5// 'This '




use Illuminate\Support\Str;

$slice = Str::of('This is my name')->beforeLast('is');

// 'This '

```

#### [`between`](https://laravel.com/docs/12.x/strings#method-fluent-str-between)
The `between` method returns the portion of a string between two values:
```


1use Illuminate\Support\Str;




2 



3$converted = Str::of('This is my name')->between('This', 'name');




4 



5// ' is my '




use Illuminate\Support\Str;

$converted = Str::of('This is my name')->between('This', 'name');

// ' is my '

```

#### [`betweenFirst`](https://laravel.com/docs/12.x/strings#method-fluent-str-between-first)
The `betweenFirst` method returns the smallest possible portion of a string between two values:
```


1use Illuminate\Support\Str;




2 



3$converted = Str::of('[a] bc [d]')->betweenFirst('[', ']');




4 



5// 'a'




use Illuminate\Support\Str;

$converted = Str::of('[a] bc [d]')->betweenFirst('[', ']');

// 'a'

```

#### [`camel`](https://laravel.com/docs/12.x/strings#method-fluent-str-camel)
The `camel` method converts the given string to `camelCase`:
```


1use Illuminate\Support\Str;




2 



3$converted = Str::of('foo_bar')->camel();




4 



5// 'fooBar'




use Illuminate\Support\Str;

$converted = Str::of('foo_bar')->camel();

// 'fooBar'

```

#### [`charAt`](https://laravel.com/docs/12.x/strings#method-fluent-str-char-at)
The `charAt` method returns the character at the specified index. If the index is out of bounds, `false` is returned:
```


1use Illuminate\Support\Str;




2 



3$character = Str::of('This is my name.')->charAt(6);




4 



5// 's'




use Illuminate\Support\Str;

$character = Str::of('This is my name.')->charAt(6);

// 's'

```

#### [`classBasename`](https://laravel.com/docs/12.x/strings#method-fluent-str-class-basename)
The `classBasename` method returns the class name of the given class with the class's namespace removed:
```


1use Illuminate\Support\Str;




2 



3$class = Str::of('Foo\Bar\Baz')->classBasename();




4 



5// 'Baz'




use Illuminate\Support\Str;

$class = Str::of('Foo\Bar\Baz')->classBasename();

// 'Baz'

```

#### [`chopStart`](https://laravel.com/docs/12.x/strings#method-fluent-str-chop-start)
The `chopStart` method removes the first occurrence of the given value only if the value appears at the start of the string:
```


1use Illuminate\Support\Str;




2 



3$url = Str::of('https://laravel.com')->chopStart('https://');




4 



5// 'laravel.com'




use Illuminate\Support\Str;

$url = Str::of('https://laravel.com')->chopStart('https://');

// 'laravel.com'

```

You may also pass an array. If the string starts with any of the values in the array then that value will be removed from string:
```


1use Illuminate\Support\Str;




2 



3$url = Str::of('http://laravel.com')->chopStart(['https://', 'http://']);




4 



5// 'laravel.com'




use Illuminate\Support\Str;

$url = Str::of('http://laravel.com')->chopStart(['https://', 'http://']);

// 'laravel.com'

```

#### [`chopEnd`](https://laravel.com/docs/12.x/strings#method-fluent-str-chop-end)
The `chopEnd` method removes the last occurrence of the given value only if the value appears at the end of the string:
```


1use Illuminate\Support\Str;




2 



3$url = Str::of('https://laravel.com')->chopEnd('.com');




4 



5// 'https://laravel'




use Illuminate\Support\Str;

$url = Str::of('https://laravel.com')->chopEnd('.com');

// 'https://laravel'

```

You may also pass an array. If the string ends with any of the values in the array then that value will be removed from string:
```


1use Illuminate\Support\Str;




2 



3$url = Str::of('http://laravel.com')->chopEnd(['.com', '.io']);




4 



5// 'http://laravel'




use Illuminate\Support\Str;

$url = Str::of('http://laravel.com')->chopEnd(['.com', '.io']);

// 'http://laravel'

```

#### [`contains`](https://laravel.com/docs/12.x/strings#method-fluent-str-contains)
The `contains` method determines if the given string contains the given value. By default, this method is case sensitive:
```


1use Illuminate\Support\Str;




2 



3$contains = Str::of('This is my name')->contains('my');




4 



5// true




use Illuminate\Support\Str;

$contains = Str::of('This is my name')->contains('my');

// true

```

You may also pass an array of values to determine if the given string contains any of the values in the array:
```


1use Illuminate\Support\Str;




2 



3$contains = Str::of('This is my name')->contains(['my', 'foo']);




4 



5// true




use Illuminate\Support\Str;

$contains = Str::of('This is my name')->contains(['my', 'foo']);

// true

```

You can disable case sensitivity by setting the `ignoreCase` argument to `true`:
```


1use Illuminate\Support\Str;




2 



3$contains = Str::of('This is my name')->contains('MY', ignoreCase: true);




4 



5// true




use Illuminate\Support\Str;

$contains = Str::of('This is my name')->contains('MY', ignoreCase: true);

// true

```

#### [`containsAll`](https://laravel.com/docs/12.x/strings#method-fluent-str-contains-all)
The `containsAll` method determines if the given string contains all of the values in the given array:
```


1use Illuminate\Support\Str;




2 



3$containsAll = Str::of('This is my name')->containsAll(['my', 'name']);




4 



5// true




use Illuminate\Support\Str;

$containsAll = Str::of('This is my name')->containsAll(['my', 'name']);

// true

```

You can disable case sensitivity by setting the `ignoreCase` argument to `true`:
```


1use Illuminate\Support\Str;




2 



3$containsAll = Str::of('This is my name')->containsAll(['MY', 'NAME'], ignoreCase: true);




4 



5// true




use Illuminate\Support\Str;

$containsAll = Str::of('This is my name')->containsAll(['MY', 'NAME'], ignoreCase: true);

// true

```

#### [`decrypt`](https://laravel.com/docs/12.x/strings#method-fluent-str-decrypt)
The `decrypt` method [decrypts](https://laravel.com/docs/12.x/encryption) the encrypted string:
```


1use Illuminate\Support\Str;




2 



3$decrypted = $encrypted->decrypt();




4 



5// 'secret'




use Illuminate\Support\Str;

$decrypted = $encrypted->decrypt();

// 'secret'

```

For the inverse of `decrypt`, see the [encrypt](https://laravel.com/docs/12.x/strings#method-fluent-str-encrypt) method.
#### [`deduplicate`](https://laravel.com/docs/12.x/strings#method-fluent-str-deduplicate)
The `deduplicate` method replaces consecutive instances of a character with a single instance of that character in the given string. By default, the method deduplicates spaces:
```


1use Illuminate\Support\Str;




2 



3$result = Str::of('The   Laravel   Framework')->deduplicate();




4 



5// The Laravel Framework




use Illuminate\Support\Str;

$result = Str::of('The   Laravel   Framework')->deduplicate();

// The Laravel Framework

```

You may specify a different character to deduplicate by passing it in as the second argument to the method:
```


1use Illuminate\Support\Str;




2 



3$result = Str::of('The---Laravel---Framework')->deduplicate('-');




4 



5// The-Laravel-Framework




use Illuminate\Support\Str;

$result = Str::of('The---Laravel---Framework')->deduplicate('-');

// The-Laravel-Framework

```

#### [`dirname`](https://laravel.com/docs/12.x/strings#method-fluent-str-dirname)
The `dirname` method returns the parent directory portion of the given string:
```


1use Illuminate\Support\Str;




2 



3$string = Str::of('/foo/bar/baz')->dirname();




4 



5// '/foo/bar'




use Illuminate\Support\Str;

$string = Str::of('/foo/bar/baz')->dirname();

// '/foo/bar'

```

If necessary, you may specify how many directory levels you wish to trim from the string:
```


1use Illuminate\Support\Str;




2 



3$string = Str::of('/foo/bar/baz')->dirname(2);




4 



5// '/foo'




use Illuminate\Support\Str;

$string = Str::of('/foo/bar/baz')->dirname(2);

// '/foo'

```

#### [`doesntContain()`](https://laravel.com/docs/12.x/strings#method-fluent-str-doesnt-contain)
The `doesntContain` method determines if the given string does not contain the given value. This method is the inverse of the [contains](https://laravel.com/docs/12.x/strings#method-fluent-str-contains) method. By default, this method is case sensitive:
```


1use Illuminate\Support\Str;




2 



3$doesntContain = Str::of('This is name')->doesntContain('my');




4 



5// true




use Illuminate\Support\Str;

$doesntContain = Str::of('This is name')->doesntContain('my');

// true

```

You may also pass an array of values to determine if the given string does not contain any of the values in the array:
```


1use Illuminate\Support\Str;




2 



3$doesntContain = Str::of('This is name')->doesntContain(['my', 'framework']);




4 



5// true




use Illuminate\Support\Str;

$doesntContain = Str::of('This is name')->doesntContain(['my', 'framework']);

// true

```

You may disable case sensitivity by setting the `ignoreCase` argument to `true`:
```


1use Illuminate\Support\Str;




2 



3$doesntContain = Str::of('This is my name')->doesntContain('MY', ignoreCase: true);




4 



5// false




use Illuminate\Support\Str;

$doesntContain = Str::of('This is my name')->doesntContain('MY', ignoreCase: true);

// false

```

#### [`doesntEndWith`](https://laravel.com/docs/12.x/strings#method-fluent-str-doesnt-end-with)
The `doesntEndWith` method determines if the given string doesn't end with the given value:
```


1use Illuminate\Support\Str;




2 



3$result = Str::of('This is my name')->doesntEndWith('dog');




4 



5// true




use Illuminate\Support\Str;

$result = Str::of('This is my name')->doesntEndWith('dog');

// true

```

You may also pass an array of values to determine if the given string doesn't end with any of the values in the array:
```


1use Illuminate\Support\Str;




2 



3$result = Str::of('This is my name')->doesntEndWith(['this', 'foo']);




4 



5// true




6 



7$result = Str::of('This is my name')->doesntEndWith(['name', 'foo']);




8 



9// false




use Illuminate\Support\Str;

$result = Str::of('This is my name')->doesntEndWith(['this', 'foo']);

// true

$result = Str::of('This is my name')->doesntEndWith(['name', 'foo']);

// false

```

#### [`doesntStartWith`](https://laravel.com/docs/12.x/strings#method-fluent-str-doesnt-start-with)
The `doesntStartWith` method determines if the given string doesn't begin with the given value:
```


1use Illuminate\Support\Str;




2 



3$result = Str::of('This is my name')->doesntStartWith('That');




4 



5// true




use Illuminate\Support\Str;

$result = Str::of('This is my name')->doesntStartWith('That');

// true

```

You may also pass an array of values to determine if the given string doesn't start with any of the values in the array:
```


1use Illuminate\Support\Str;




2 



3$result = Str::of('This is my name')->doesntStartWith(['What', 'That', 'There']);




4 



5// true




use Illuminate\Support\Str;

$result = Str::of('This is my name')->doesntStartWith(['What', 'That', 'There']);

// true

```

#### [`encrypt`](https://laravel.com/docs/12.x/strings#method-fluent-str-encrypt)
The `encrypt` method [encrypts](https://laravel.com/docs/12.x/encryption) the string:
```


1use Illuminate\Support\Str;




2 



3$encrypted = Str::of('secret')->encrypt();




use Illuminate\Support\Str;

$encrypted = Str::of('secret')->encrypt();

```

For the inverse of `encrypt`, see the [decrypt](https://laravel.com/docs/12.x/strings#method-fluent-str-decrypt) method.
#### [`endsWith`](https://laravel.com/docs/12.x/strings#method-fluent-str-ends-with)
The `endsWith` method determines if the given string ends with the given value:
```


1use Illuminate\Support\Str;




2 



3$result = Str::of('This is my name')->endsWith('name');




4 



5// true




use Illuminate\Support\Str;

$result = Str::of('This is my name')->endsWith('name');

// true

```

You may also pass an array of values to determine if the given string ends with any of the values in the array:
```


1use Illuminate\Support\Str;




2 



3$result = Str::of('This is my name')->endsWith(['name', 'foo']);




4 



5// true




6 



7$result = Str::of('This is my name')->endsWith(['this', 'foo']);




8 



9// false




use Illuminate\Support\Str;

$result = Str::of('This is my name')->endsWith(['name', 'foo']);

// true

$result = Str::of('This is my name')->endsWith(['this', 'foo']);

// false

```

#### [`exactly`](https://laravel.com/docs/12.x/strings#method-fluent-str-exactly)
The `exactly` method determines if the given string is an exact match with another string:
```


1use Illuminate\Support\Str;




2 



3$result = Str::of('Laravel')->exactly('Laravel');




4 



5// true




use Illuminate\Support\Str;

$result = Str::of('Laravel')->exactly('Laravel');

// true

```

#### [`excerpt`](https://laravel.com/docs/12.x/strings#method-fluent-str-excerpt)
The `excerpt` method extracts an excerpt from the string that matches the first instance of a phrase within that string:
```


1use Illuminate\Support\Str;




2 



3$excerpt = Str::of('This is my name')->excerpt('my', [




4    'radius' => 3




5]);




6 



7// '...is my na...'




use Illuminate\Support\Str;

$excerpt = Str::of('This is my name')->excerpt('my', [
    'radius' => 3
]);

// '...is my na...'

```

The `radius` option, which defaults to `100`, allows you to define the number of characters that should appear on each side of the truncated string.
In addition, you may use the `omission` option to change the string that will be prepended and appended to the truncated string:
```


1use Illuminate\Support\Str;




2 



3$excerpt = Str::of('This is my name')->excerpt('name', [




4    'radius' => 3,




5    'omission' => '(...) '




6]);




7 



8// '(...) my name'




use Illuminate\Support\Str;

$excerpt = Str::of('This is my name')->excerpt('name', [
    'radius' => 3,
    'omission' => '(...) '
]);

// '(...) my name'

```

#### [`explode`](https://laravel.com/docs/12.x/strings#method-fluent-str-explode)
The `explode` method splits the string by the given delimiter and returns a collection containing each section of the split string:
```


1use Illuminate\Support\Str;




2 



3$collection = Str::of('foo bar baz')->explode(' ');




4 



5// collect(['foo', 'bar', 'baz'])




use Illuminate\Support\Str;

$collection = Str::of('foo bar baz')->explode(' ');

// collect(['foo', 'bar', 'baz'])

```

#### [`finish`](https://laravel.com/docs/12.x/strings#method-fluent-str-finish)
The `finish` method adds a single instance of the given value to a string if it does not already end with that value:
```


1use Illuminate\Support\Str;




2 



3$adjusted = Str::of('this/string')->finish('/');




4 



5// this/string/




6 



7$adjusted = Str::of('this/string/')->finish('/');




8 



9// this/string/




use Illuminate\Support\Str;

$adjusted = Str::of('this/string')->finish('/');

// this/string/

$adjusted = Str::of('this/string/')->finish('/');

// this/string/

```

#### [`fromBase64`](https://laravel.com/docs/12.x/strings#method-fluent-str-from-base64)
The `fromBase64` method decodes the given Base64 string:
```


1use Illuminate\Support\Str;




2 



3$decoded = Str::of('TGFyYXZlbA==')->fromBase64();




4 



5// Laravel




use Illuminate\Support\Str;

$decoded = Str::of('TGFyYXZlbA==')->fromBase64();

// Laravel

```

#### [`hash`](https://laravel.com/docs/12.x/strings#method-fluent-str-hash)
The `hash` method hashes the string using the given
```


1use Illuminate\Support\Str;




2 



3$hashed = Str::of('secret')->hash(algorithm: 'sha256');




4 



5// '2bb80d537b1da3e38bd30361aa855686bde0eacd7162fef6a25fe97bf527a25b'




use Illuminate\Support\Str;

$hashed = Str::of('secret')->hash(algorithm: 'sha256');

// '2bb80d537b1da3e38bd30361aa855686bde0eacd7162fef6a25fe97bf527a25b'

```

#### [`headline`](https://laravel.com/docs/12.x/strings#method-fluent-str-headline)
The `headline` method will convert strings delimited by casing, hyphens, or underscores into a space delimited string with each word's first letter capitalized:
```


1use Illuminate\Support\Str;




2 



3$headline = Str::of('taylor_otwell')->headline();




4 



5// Taylor Otwell




6 



7$headline = Str::of('EmailNotificationSent')->headline();




8 



9// Email Notification Sent




use Illuminate\Support\Str;

$headline = Str::of('taylor_otwell')->headline();

// Taylor Otwell

$headline = Str::of('EmailNotificationSent')->headline();

// Email Notification Sent

```

#### [`inlineMarkdown`](https://laravel.com/docs/12.x/strings#method-fluent-str-inline-markdown)
The `inlineMarkdown` method converts GitHub flavored Markdown into inline HTML using `markdown` method, it does not wrap all generated HTML in a block-level element:
```


1use Illuminate\Support\Str;




2 



3$html = Str::of('**Laravel**')->inlineMarkdown();




4 



5// <strong>Laravel</strong>




use Illuminate\Support\Str;

$html = Str::of('**Laravel**')->inlineMarkdown();

// <strong>Laravel</strong>

```

#### Markdown Security
By default, Markdown supports raw HTML, which will expose Cross-Site Scripting (XSS) vulnerabilities when used with raw user input. As per the `html_input` option to either escape or strip raw HTML, and the `allow_unsafe_links` option to specify whether to allow unsafe links. If you need to allow some raw HTML, you should pass your compiled Markdown through an HTML Purifier:
```


1use Illuminate\Support\Str;




2 



3Str::of('Inject: <script>alert("Hello XSS!");</script>')->inlineMarkdown([




4    'html_input' => 'strip',




5    'allow_unsafe_links' => false,




6]);




7 



8// Inject: alert(&quot;Hello XSS!&quot;);




use Illuminate\Support\Str;

Str::of('Inject: <script>alert("Hello XSS!");</script>')->inlineMarkdown([
    'html_input' => 'strip',
    'allow_unsafe_links' => false,
]);

// Inject: alert(&quot;Hello XSS!&quot;);

```

#### [`is`](https://laravel.com/docs/12.x/strings#method-fluent-str-is)
The `is` method determines if a given string matches a given pattern. Asterisks may be used as wildcard values
```


1use Illuminate\Support\Str;




2 



3$matches = Str::of('foobar')->is('foo*');




4 



5// true




6 



7$matches = Str::of('foobar')->is('baz*');




8 



9// false




use Illuminate\Support\Str;

$matches = Str::of('foobar')->is('foo*');

// true

$matches = Str::of('foobar')->is('baz*');

// false

```

#### [`isAscii`](https://laravel.com/docs/12.x/strings#method-fluent-str-is-ascii)
The `isAscii` method determines if a given string is an ASCII string:
```


1use Illuminate\Support\Str;




2 



3$result = Str::of('Taylor')->isAscii();




4 



5// true




6 



7$result = Str::of('ü')->isAscii();




8 



9// false




use Illuminate\Support\Str;

$result = Str::of('Taylor')->isAscii();

// true

$result = Str::of('ü')->isAscii();

// false

```

#### [`isEmpty`](https://laravel.com/docs/12.x/strings#method-fluent-str-is-empty)
The `isEmpty` method determines if the given string is empty:
```


1use Illuminate\Support\Str;




2 



3$result = Str::of('  ')->trim()->isEmpty();




4 



5// true




6 



7$result = Str::of('Laravel')->trim()->isEmpty();




8 



9// false




use Illuminate\Support\Str;

$result = Str::of('  ')->trim()->isEmpty();

// true

$result = Str::of('Laravel')->trim()->isEmpty();

// false

```

#### [`isNotEmpty`](https://laravel.com/docs/12.x/strings#method-fluent-str-is-not-empty)
The `isNotEmpty` method determines if the given string is not empty:
```


1use Illuminate\Support\Str;




2 



3$result = Str::of('  ')->trim()->isNotEmpty();




4 



5// false




6 



7$result = Str::of('Laravel')->trim()->isNotEmpty();




8 



9// true




use Illuminate\Support\Str;

$result = Str::of('  ')->trim()->isNotEmpty();

// false

$result = Str::of('Laravel')->trim()->isNotEmpty();

// true

```

#### [`isJson`](https://laravel.com/docs/12.x/strings#method-fluent-str-is-json)
The `isJson` method determines if a given string is valid JSON:
```


 1use Illuminate\Support\Str;




 2 



 3$result = Str::of('[1,2,3]')->isJson();




 4 



 5// true




 6 



 7$result = Str::of('{"first": "John", "last": "Doe"}')->isJson();




 8 



 9// true




10 



11$result = Str::of('{first: "John", last: "Doe"}')->isJson();




12 



13// false




use Illuminate\Support\Str;

$result = Str::of('[1,2,3]')->isJson();

// true

$result = Str::of('{"first": "John", "last": "Doe"}')->isJson();

// true

$result = Str::of('{first: "John", last: "Doe"}')->isJson();

// false

```

#### [`isUlid`](https://laravel.com/docs/12.x/strings#method-fluent-str-is-ulid)
The `isUlid` method determines if a given string is a ULID:
```


1use Illuminate\Support\Str;




2 



3$result = Str::of('01gd6r360bp37zj17nxb55yv40')->isUlid();




4 



5// true




6 



7$result = Str::of('Taylor')->isUlid();




8 



9// false




use Illuminate\Support\Str;

$result = Str::of('01gd6r360bp37zj17nxb55yv40')->isUlid();

// true

$result = Str::of('Taylor')->isUlid();

// false

```

#### [`isUrl`](https://laravel.com/docs/12.x/strings#method-fluent-str-is-url)
The `isUrl` method determines if a given string is a URL:
```


1use Illuminate\Support\Str;




2 



3$result = Str::of('http://example.com')->isUrl();




4 



5// true




6 



7$result = Str::of('Taylor')->isUrl();




8 



9// false




use Illuminate\Support\Str;

$result = Str::of('http://example.com')->isUrl();

// true

$result = Str::of('Taylor')->isUrl();

// false

```

The `isUrl` method considers a wide range of protocols as valid. However, you may specify the protocols that should be considered valid by providing them to the `isUrl` method:
