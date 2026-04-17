## [Debugging](https://laravel.com/docs/12.x/queries#debugging)
You may use the `dd` and `dump` methods while building a query to dump the current query bindings and SQL. The `dd` method will display the debug information and then stop executing the request. The `dump` method will display the debug information but allow the request to continue executing:
```


1DB::table('users')->where('votes', '>', 100)->dd();




2 



3DB::table('users')->where('votes', '>', 100)->dump();




DB::table('users')->where('votes', '>', 100)->dd();

DB::table('users')->where('votes', '>', 100)->dump();

```

The `dumpRawSql` and `ddRawSql` methods may be invoked on a query to dump the query's SQL with all parameter bindings properly substituted:
```


1DB::table('users')->where('votes', '>', 100)->dumpRawSql();




2 



3DB::table('users')->where('votes', '>', 100)->ddRawSql();




DB::table('users')->where('votes', '>', 100)->dumpRawSql();

DB::table('users')->where('votes', '>', 100)->ddRawSql();

```

Copy as markdown
  * [ Introduction ](https://laravel.com/docs/12.x/queries#introduction)
  * [ Running Database Queries ](https://laravel.com/docs/12.x/queries#running-database-queries)
    * [ Chunking Results ](https://laravel.com/docs/12.x/queries#chunking-results)
    * [ Streaming Results Lazily ](https://laravel.com/docs/12.x/queries#streaming-results-lazily)
    * [ Aggregates ](https://laravel.com/docs/12.x/queries#aggregates)
  * [ Select Statements ](https://laravel.com/docs/12.x/queries#select-statements)
  * [ Raw Expressions ](https://laravel.com/docs/12.x/queries#raw-expressions)
  * [ Joins ](https://laravel.com/docs/12.x/queries#joins)
  * [ Unions ](https://laravel.com/docs/12.x/queries#unions)
  * [ Basic Where Clauses ](https://laravel.com/docs/12.x/queries#basic-where-clauses)
    * [ Where Clauses ](https://laravel.com/docs/12.x/queries#where-clauses)
    * [ Or Where Clauses ](https://laravel.com/docs/12.x/queries#or-where-clauses)
    * [ Where Not Clauses ](https://laravel.com/docs/12.x/queries#where-not-clauses)
    * [ Where Any / All / None Clauses ](https://laravel.com/docs/12.x/queries#where-any-all-none-clauses)
    * [ JSON Where Clauses ](https://laravel.com/docs/12.x/queries#json-where-clauses)
    * [ Additional Where Clauses ](https://laravel.com/docs/12.x/queries#additional-where-clauses)
    * [ Logical Grouping ](https://laravel.com/docs/12.x/queries#logical-grouping)
  * [ Advanced Where Clauses ](https://laravel.com/docs/12.x/queries#advanced-where-clauses)
    * [ Where Exists Clauses ](https://laravel.com/docs/12.x/queries#where-exists-clauses)
    * [ Subquery Where Clauses ](https://laravel.com/docs/12.x/queries#subquery-where-clauses)
    * [ Full Text Where Clauses ](https://laravel.com/docs/12.x/queries#full-text-where-clauses)
    * [ Vector Similarity Clauses ](https://laravel.com/docs/12.x/queries#vector-similarity-clauses)
  * [ Ordering, Grouping, Limit and Offset ](https://laravel.com/docs/12.x/queries#ordering-grouping-limit-and-offset)
    * [ Ordering ](https://laravel.com/docs/12.x/queries#ordering)
    * [ Grouping ](https://laravel.com/docs/12.x/queries#grouping)
    * [ Limit and Offset ](https://laravel.com/docs/12.x/queries#limit-and-offset)
  * [ Conditional Clauses ](https://laravel.com/docs/12.x/queries#conditional-clauses)
  * [ Insert Statements ](https://laravel.com/docs/12.x/queries#insert-statements)
    * [ Upserts ](https://laravel.com/docs/12.x/queries#upserts)
  * [ Update Statements ](https://laravel.com/docs/12.x/queries#update-statements)
    * [ Updating JSON Columns ](https://laravel.com/docs/12.x/queries#updating-json-columns)
    * [ Increment and Decrement ](https://laravel.com/docs/12.x/queries#increment-and-decrement)
  * [ Delete Statements ](https://laravel.com/docs/12.x/queries#delete-statements)
  * [ Pessimistic Locking ](https://laravel.com/docs/12.x/queries#pessimistic-locking)
  * [ Reusable Query Components ](https://laravel.com/docs/12.x/queries#reusable-query-components)
  * [ Debugging ](https://laravel.com/docs/12.x/queries#debugging)


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
  *   * [byte5](https://partners.laravel.com/partners/byte5)
  * [Tighten](https://partners.laravel.com/partners/tighten)
  * [Redberry](https://partners.laravel.com/partners/redberry)
  * [Active Logic](https://partners.laravel.com/partners/active-logic)
  * [Kirschbaum](https://partners.laravel.com/partners/kirschbaum)
  * [Vehikl](https://partners.laravel.com/partners/vehikl)
  * [Curotec](https://partners.laravel.com/partners/curotec)
  * [Jump24](https://partners.laravel.com/partners/jump24)
  * [ More Partners ](https://partners.laravel.com)
