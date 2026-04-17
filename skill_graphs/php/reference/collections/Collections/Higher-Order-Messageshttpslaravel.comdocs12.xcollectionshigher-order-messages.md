## [Higher Order Messages](https://laravel.com/docs/12.x/collections#higher-order-messages)
Collections also provide support for "higher order messages", which are short-cuts for performing common actions on collections. The collection methods that provide higher order messages are: [average](https://laravel.com/docs/12.x/collections#method-average), [avg](https://laravel.com/docs/12.x/collections#method-avg), [contains](https://laravel.com/docs/12.x/collections#method-contains), [each](https://laravel.com/docs/12.x/collections#method-each), [every](https://laravel.com/docs/12.x/collections#method-every), [filter](https://laravel.com/docs/12.x/collections#method-filter), [first](https://laravel.com/docs/12.x/collections#method-first), [flatMap](https://laravel.com/docs/12.x/collections#method-flatmap), [groupBy](https://laravel.com/docs/12.x/collections#method-groupby), [keyBy](https://laravel.com/docs/12.x/collections#method-keyby), [map](https://laravel.com/docs/12.x/collections#method-map), [max](https://laravel.com/docs/12.x/collections#method-max), [min](https://laravel.com/docs/12.x/collections#method-min), [partition](https://laravel.com/docs/12.x/collections#method-partition), [reject](https://laravel.com/docs/12.x/collections#method-reject), [skipUntil](https://laravel.com/docs/12.x/collections#method-skipuntil), [skipWhile](https://laravel.com/docs/12.x/collections#method-skipwhile), [some](https://laravel.com/docs/12.x/collections#method-some), [sortBy](https://laravel.com/docs/12.x/collections#method-sortby), [sortByDesc](https://laravel.com/docs/12.x/collections#method-sortbydesc), [sum](https://laravel.com/docs/12.x/collections#method-sum), [takeUntil](https://laravel.com/docs/12.x/collections#method-takeuntil), [takeWhile](https://laravel.com/docs/12.x/collections#method-takewhile), and [unique](https://laravel.com/docs/12.x/collections#method-unique).
Each higher order message can be accessed as a dynamic property on a collection instance. For instance, let's use the `each` higher order message to call a method on each object within a collection:
```


1use App\Models\User;




2 



3$users = User::where('votes', '>', 500)->get();




4 



5$users->each->markAsVip();




use App\Models\User;

$users = User::where('votes', '>', 500)->get();

$users->each->markAsVip();

```

Likewise, we can use the `sum` higher order message to gather the total number of "votes" for a collection of users:
```


1$users = User::where('group', 'Development')->get();




2 



3return $users->sum->votes;




$users = User::where('group', 'Development')->get();

return $users->sum->votes;

```
