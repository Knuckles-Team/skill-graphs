## [Lazy Collections](https://laravel.com/docs/12.x/collections#lazy-collections)
### [Introduction](https://laravel.com/docs/12.x/collections#lazy-collection-introduction)
Before learning more about Laravel's lazy collections, take some time to familiarize yourself with
To supplement the already powerful `Collection` class, the `LazyCollection` class leverages PHP's
For example, imagine your application needs to process a multi-gigabyte log file while taking advantage of Laravel's collection methods to parse the logs. Instead of reading the entire file into memory at once, lazy collections may be used to keep only a small part of the file in memory at a given time:
```


 1use App\Models\LogEntry;




 2use Illuminate\Support\LazyCollection;




 3 



 4LazyCollection::make(function () {




 5    $handle = fopen('log.txt', 'r');




 6 



 7    while (($line = fgets($handle)) !== false) {




 8        yield $line;




 9    }




10 



11    fclose($handle);




12})->chunk(4)->map(function (array $lines) {




13    return LogEntry::fromLines($lines);




14})->each(function (LogEntry $logEntry) {




15    // Process the log entry...




16});




use App\Models\LogEntry;
use Illuminate\Support\LazyCollection;

LazyCollection::make(function () {
    $handle = fopen('log.txt', 'r');

    while (($line = fgets($handle)) !== false) {
        yield $line;
    }

    fclose($handle);
})->chunk(4)->map(function (array $lines) {
    return LogEntry::fromLines($lines);
})->each(function (LogEntry $logEntry) {
    // Process the log entry...
});

```

Or, imagine you need to iterate through 10,000 Eloquent models. When using traditional Laravel collections, all 10,000 Eloquent models must be loaded into memory at the same time:
```


1use App\Models\User;




2 



3$users = User::all()->filter(function (User $user) {




4    return $user->id > 500;




5});




use App\Models\User;

$users = User::all()->filter(function (User $user) {
    return $user->id > 500;
});

```

However, the query builder's `cursor` method returns a `LazyCollection` instance. This allows you to still only run a single query against the database but also only keep one Eloquent model loaded in memory at a time. In this example, the `filter` callback is not executed until we actually iterate over each user individually, allowing for a drastic reduction in memory usage:
```


1use App\Models\User;




2 



3$users = User::cursor()->filter(function (User $user) {




4    return $user->id > 500;




5});




6 



7foreach ($users as $user) {




8    echo $user->id;




9}




use App\Models\User;

$users = User::cursor()->filter(function (User $user) {
    return $user->id > 500;
});

foreach ($users as $user) {
    echo $user->id;
}

```

### [Creating Lazy Collections](https://laravel.com/docs/12.x/collections#creating-lazy-collections)
To create a lazy collection instance, you should pass a PHP generator function to the collection's `make` method:
```


 1use Illuminate\Support\LazyCollection;




 2 



 3LazyCollection::make(function () {




 4    $handle = fopen('log.txt', 'r');




 5 



 6    while (($line = fgets($handle)) !== false) {




 7        yield $line;




 8    }




 9 



10    fclose($handle);




11});




use Illuminate\Support\LazyCollection;

LazyCollection::make(function () {
    $handle = fopen('log.txt', 'r');

    while (($line = fgets($handle)) !== false) {
        yield $line;
    }

    fclose($handle);
});

```

### [The Enumerable Contract](https://laravel.com/docs/12.x/collections#the-enumerable-contract)
Almost all methods available on the `Collection` class are also available on the `LazyCollection` class. Both of these classes implement the `Illuminate\Support\Enumerable` contract, which defines the following methods:
[all](https://laravel.com/docs/12.x/collections#method-all) [average](https://laravel.com/docs/12.x/collections#method-average) [avg](https://laravel.com/docs/12.x/collections#method-avg) [chunk](https://laravel.com/docs/12.x/collections#method-chunk) [chunkWhile](https://laravel.com/docs/12.x/collections#method-chunkwhile) [collapse](https://laravel.com/docs/12.x/collections#method-collapse) [collect](https://laravel.com/docs/12.x/collections#method-collect) [combine](https://laravel.com/docs/12.x/collections#method-combine) [concat](https://laravel.com/docs/12.x/collections#method-concat) [contains](https://laravel.com/docs/12.x/collections#method-contains) [containsStrict](https://laravel.com/docs/12.x/collections#method-containsstrict) [count](https://laravel.com/docs/12.x/collections#method-count) [countBy](https://laravel.com/docs/12.x/collections#method-countBy) [crossJoin](https://laravel.com/docs/12.x/collections#method-crossjoin) [dd](https://laravel.com/docs/12.x/collections#method-dd) [diff](https://laravel.com/docs/12.x/collections#method-diff) [diffAssoc](https://laravel.com/docs/12.x/collections#method-diffassoc) [diffKeys](https://laravel.com/docs/12.x/collections#method-diffkeys) [dump](https://laravel.com/docs/12.x/collections#method-dump) [duplicates](https://laravel.com/docs/12.x/collections#method-duplicates) [duplicatesStrict](https://laravel.com/docs/12.x/collections#method-duplicatesstrict) [each](https://laravel.com/docs/12.x/collections#method-each) [eachSpread](https://laravel.com/docs/12.x/collections#method-eachspread) [every](https://laravel.com/docs/12.x/collections#method-every) [except](https://laravel.com/docs/12.x/collections#method-except) [filter](https://laravel.com/docs/12.x/collections#method-filter) [first](https://laravel.com/docs/12.x/collections#method-first) [firstOrFail](https://laravel.com/docs/12.x/collections#method-first-or-fail) [firstWhere](https://laravel.com/docs/12.x/collections#method-first-where) [flatMap](https://laravel.com/docs/12.x/collections#method-flatmap) [flatten](https://laravel.com/docs/12.x/collections#method-flatten) [flip](https://laravel.com/docs/12.x/collections#method-flip) [forPage](https://laravel.com/docs/12.x/collections#method-forpage) [get](https://laravel.com/docs/12.x/collections#method-get) [groupBy](https://laravel.com/docs/12.x/collections#method-groupby) [has](https://laravel.com/docs/12.x/collections#method-has) [implode](https://laravel.com/docs/12.x/collections#method-implode) [intersect](https://laravel.com/docs/12.x/collections#method-intersect) [intersectAssoc](https://laravel.com/docs/12.x/collections#method-intersectAssoc) [intersectByKeys](https://laravel.com/docs/12.x/collections#method-intersectbykeys) [isEmpty](https://laravel.com/docs/12.x/collections#method-isempty) [isNotEmpty](https://laravel.com/docs/12.x/collections#method-isnotempty) [join](https://laravel.com/docs/12.x/collections#method-join) [keyBy](https://laravel.com/docs/12.x/collections#method-keyby) [keys](https://laravel.com/docs/12.x/collections#method-keys) [last](https://laravel.com/docs/12.x/collections#method-last) [macro](https://laravel.com/docs/12.x/collections#method-macro) [make](https://laravel.com/docs/12.x/collections#method-make) [map](https://laravel.com/docs/12.x/collections#method-map) [mapInto](https://laravel.com/docs/12.x/collections#method-mapinto) [mapSpread](https://laravel.com/docs/12.x/collections#method-mapspread) [mapToGroups](https://laravel.com/docs/12.x/collections#method-maptogroups) [mapWithKeys](https://laravel.com/docs/12.x/collections#method-mapwithkeys) [max](https://laravel.com/docs/12.x/collections#method-max) [median](https://laravel.com/docs/12.x/collections#method-median) [merge](https://laravel.com/docs/12.x/collections#method-merge) [mergeRecursive](https://laravel.com/docs/12.x/collections#method-mergerecursive) [min](https://laravel.com/docs/12.x/collections#method-min) [mode](https://laravel.com/docs/12.x/collections#method-mode) [nth](https://laravel.com/docs/12.x/collections#method-nth) [only](https://laravel.com/docs/12.x/collections#method-only) [pad](https://laravel.com/docs/12.x/collections#method-pad) [partition](https://laravel.com/docs/12.x/collections#method-partition) [pipe](https://laravel.com/docs/12.x/collections#method-pipe) [pluck](https://laravel.com/docs/12.x/collections#method-pluck) [random](https://laravel.com/docs/12.x/collections#method-random) [reduce](https://laravel.com/docs/12.x/collections#method-reduce) [reject](https://laravel.com/docs/12.x/collections#method-reject) [replace](https://laravel.com/docs/12.x/collections#method-replace) [replaceRecursive](https://laravel.com/docs/12.x/collections#method-replacerecursive) [reverse](https://laravel.com/docs/12.x/collections#method-reverse) [search](https://laravel.com/docs/12.x/collections#method-search) [shuffle](https://laravel.com/docs/12.x/collections#method-shuffle) [skip](https://laravel.com/docs/12.x/collections#method-skip) [slice](https://laravel.com/docs/12.x/collections#method-slice) [sole](https://laravel.com/docs/12.x/collections#method-sole) [some](https://laravel.com/docs/12.x/collections#method-some) [sort](https://laravel.com/docs/12.x/collections#method-sort) [sortBy](https://laravel.com/docs/12.x/collections#method-sortby) [sortByDesc](https://laravel.com/docs/12.x/collections#method-sortbydesc) [sortKeys](https://laravel.com/docs/12.x/collections#method-sortkeys) [sortKeysDesc](https://laravel.com/docs/12.x/collections#method-sortkeysdesc) [split](https://laravel.com/docs/12.x/collections#method-split) [sum](https://laravel.com/docs/12.x/collections#method-sum) [take](https://laravel.com/docs/12.x/collections#method-take) [tap](https://laravel.com/docs/12.x/collections#method-tap) [times](https://laravel.com/docs/12.x/collections#method-times) [toArray](https://laravel.com/docs/12.x/collections#method-toarray) [toJson](https://laravel.com/docs/12.x/collections#method-tojson) [union](https://laravel.com/docs/12.x/collections#method-union) [unique](https://laravel.com/docs/12.x/collections#method-unique) [uniqueStrict](https://laravel.com/docs/12.x/collections#method-uniquestrict) [unless](https://laravel.com/docs/12.x/collections#method-unless) [unlessEmpty](https://laravel.com/docs/12.x/collections#method-unlessempty) [unlessNotEmpty](https://laravel.com/docs/12.x/collections#method-unlessnotempty) [unwrap](https://laravel.com/docs/12.x/collections#method-unwrap) [values](https://laravel.com/docs/12.x/collections#method-values) [when](https://laravel.com/docs/12.x/collections#method-when) [whenEmpty](https://laravel.com/docs/12.x/collections#method-whenempty) [whenNotEmpty](https://laravel.com/docs/12.x/collections#method-whennotempty) [where](https://laravel.com/docs/12.x/collections#method-where) [whereStrict](https://laravel.com/docs/12.x/collections#method-wherestrict) [whereBetween](https://laravel.com/docs/12.x/collections#method-wherebetween) [whereIn](https://laravel.com/docs/12.x/collections#method-wherein) [whereInStrict](https://laravel.com/docs/12.x/collections#method-whereinstrict) [whereInstanceOf](https://laravel.com/docs/12.x/collections#method-whereinstanceof) [whereNotBetween](https://laravel.com/docs/12.x/collections#method-wherenotbetween) [whereNotIn](https://laravel.com/docs/12.x/collections#method-wherenotin) [whereNotInStrict](https://laravel.com/docs/12.x/collections#method-wherenotinstrict) [wrap](https://laravel.com/docs/12.x/collections#method-wrap) [zip](https://laravel.com/docs/12.x/collections#method-zip)
Methods that mutate the collection (such as `shift`, `pop`, `prepend` etc.) are **not** available on the `LazyCollection` class.
### [Lazy Collection Methods](https://laravel.com/docs/12.x/collections#lazy-collection-methods)
In addition to the methods defined in the `Enumerable` contract, the `LazyCollection` class contains the following methods:
#### [`takeUntilTimeout()`](https://laravel.com/docs/12.x/collections#method-takeUntilTimeout)
The `takeUntilTimeout` method returns a new lazy collection that will enumerate values until the specified time. After that time, the collection will then stop enumerating:
```


 1$lazyCollection = LazyCollection::times(INF)




 2    ->takeUntilTimeout(now()->plus(minutes: 1));




 3 



 4$lazyCollection->each(function (int $number) {




 5    dump($number);




 6 



 7    sleep(1);




 8});




 9 



10// 1




11// 2




12// ...




13// 58




14// 59




$lazyCollection = LazyCollection::times(INF)
    ->takeUntilTimeout(now()->plus(minutes: 1));

$lazyCollection->each(function (int $number) {
    dump($number);

    sleep(1);
});

// 1
// 2
// ...
// 58
// 59

```

To illustrate the usage of this method, imagine an application that submits invoices from the database using a cursor. You could define a [scheduled task](https://laravel.com/docs/12.x/scheduling) that runs every 15 minutes and only processes invoices for a maximum of 14 minutes:
```


1use App\Models\Invoice;




2use Illuminate\Support\Carbon;




3 



4Invoice::pending()->cursor()




5    ->takeUntilTimeout(




6        Carbon::createFromTimestamp(LARAVEL_START)->add(14, 'minutes')




7    )




8    ->each(fn (Invoice $invoice) => $invoice->submit());




use App\Models\Invoice;
use Illuminate\Support\Carbon;

Invoice::pending()->cursor()
    ->takeUntilTimeout(
        Carbon::createFromTimestamp(LARAVEL_START)->add(14, 'minutes')
    )
    ->each(fn (Invoice $invoice) => $invoice->submit());

```

#### [`tapEach()`](https://laravel.com/docs/12.x/collections#method-tapEach)
While the `each` method calls the given callback for each item in the collection right away, the `tapEach` method only calls the given callback as the items are being pulled out of the list one by one:
```


 1// Nothing has been dumped so far...




 2$lazyCollection = LazyCollection::times(INF)->tapEach(function (int $value) {




 3    dump($value);




 4});




 5 



 6// Three items are dumped...




 7$array = $lazyCollection->take(3)->all();




 8 



 9// 1




10// 2




11// 3




// Nothing has been dumped so far...
$lazyCollection = LazyCollection::times(INF)->tapEach(function (int $value) {
    dump($value);
});

// Three items are dumped...
$array = $lazyCollection->take(3)->all();

// 1
// 2
// 3

```

#### [`throttle()`](https://laravel.com/docs/12.x/collections#method-throttle)
The `throttle` method will throttle the lazy collection such that each value is returned after the specified number of seconds. This method is especially useful for situations where you may be interacting with external APIs that rate limit incoming requests:
```


1use App\Models\User;




2 



3User::where('vip', true)




4    ->cursor()




5    ->throttle(seconds: 1)




6    ->each(function (User $user) {




7        // Call external API...




8    });




use App\Models\User;

User::where('vip', true)
    ->cursor()
    ->throttle(seconds: 1)
    ->each(function (User $user) {
        // Call external API...
    });

```

#### [`remember()`](https://laravel.com/docs/12.x/collections#method-remember)
The `remember` method returns a new lazy collection that will remember any values that have already been enumerated and will not retrieve them again on subsequent collection enumerations:
```


 1// No query has been executed yet...




 2$users = User::cursor()->remember();




 3 



 4// The query is executed...




 5// The first 5 users are hydrated from the database...




 6$users->take(5)->all();




 7 



 8// First 5 users come from the collection's cache...




 9// The rest are hydrated from the database...




10$users->take(20)->all();




// No query has been executed yet...
$users = User::cursor()->remember();

// The query is executed...
// The first 5 users are hydrated from the database...
$users->take(5)->all();

// First 5 users come from the collection's cache...
// The rest are hydrated from the database...
$users->take(20)->all();

```

#### [`withHeartbeat()`](https://laravel.com/docs/12.x/collections#method-with-heartbeat)
The `withHeartbeat` method allows you to execute a callback at regular time intervals while a lazy collection is being enumerated. This is particularly useful for long-running operations that require periodic maintenance tasks, such as extending locks or sending progress updates:
```


 1use Carbon\CarbonInterval;




 2use Illuminate\Support\Facades\Cache;




 3 



 4$lock = Cache::lock('generate-reports', seconds: 60 * 5);




 5 



 6if ($lock->get()) {




 7    try {




 8        Report::where('status', 'pending')




 9            ->lazy()




10            ->withHeartbeat(




11                CarbonInterval::minutes(4),




12                fn () => $lock->extend(CarbonInterval::minutes(5))




13            )




14            ->each(fn ($report) => $report->process());




15    } finally {




16        $lock->release();




17    }




18}




use Carbon\CarbonInterval;
use Illuminate\Support\Facades\Cache;

$lock = Cache::lock('generate-reports', seconds: 60 * 5);

if ($lock->get()) {
    try {
        Report::where('status', 'pending')
            ->lazy()
            ->withHeartbeat(
                CarbonInterval::minutes(4),
                fn () => $lock->extend(CarbonInterval::minutes(5))
            )
            ->each(fn ($report) => $report->process());
    } finally {
        $lock->release();
    }
}

```

Copy as markdown
  * [ Introduction ](https://laravel.com/docs/12.x/collections#introduction)
    * [ Creating Collections ](https://laravel.com/docs/12.x/collections#creating-collections)
    * [ Extending Collections ](https://laravel.com/docs/12.x/collections#extending-collections)
  * [ Available Methods ](https://laravel.com/docs/12.x/collections#available-methods)
  * [ Higher Order Messages ](https://laravel.com/docs/12.x/collections#higher-order-messages)
  * [ Lazy Collections ](https://laravel.com/docs/12.x/collections#lazy-collections)
    * [ Introduction ](https://laravel.com/docs/12.x/collections#lazy-collection-introduction)
    * [ Creating Lazy Collections ](https://laravel.com/docs/12.x/collections#creating-lazy-collections)
    * [ The Enumerable Contract ](https://laravel.com/docs/12.x/collections#the-enumerable-contract)
    * [ Lazy Collection Methods ](https://laravel.com/docs/12.x/collections#lazy-collection-methods)


[ ![Laravel Nightwatch](https://laravel.com/images/ads/nightwatch-logo.svg) First-class monitoring and deep insights for Laravel apps Learn more  ](https://nightwatch.laravel.com)
[ ![Laravel Forge](https://laravel.com/images/ads/forge-logo.svg) Server management made simple for any PHP app Learn more  ](https://forge.laravel.com)
[ ![Laravel Cloud](https://laravel.com/images/ads/cloud-logo.svg) The fastest way to deploy and scale Laravel apps Learn more  ](https://cloud.laravel.com)
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
  *   * [Kirschbaum](https://partners.laravel.com/partners/kirschbaum)
  * [Active Logic](https://partners.laravel.com/partners/active-logic)
  * [Redberry](https://partners.laravel.com/partners/redberry)
  * [byte5](https://partners.laravel.com/partners/byte5)
  * [Tighten](https://partners.laravel.com/partners/tighten)
  * [Curotec](https://partners.laravel.com/partners/curotec)
  * [Jump24](https://partners.laravel.com/partners/jump24)
  * [Vehikl](https://partners.laravel.com/partners/vehikl)
  * [ More Partners ](https://partners.laravel.com)
