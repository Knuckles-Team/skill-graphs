## [Introduction](https://laravel.com/docs/12.x/scout#introduction)
[Eloquent models](https://laravel.com/docs/12.x/eloquent). Using model observers, Scout will automatically keep your search indexes in sync with your Eloquent records.
Scout ships with a built-in `database` engine that uses MySQL / PostgreSQL full-text indexes and `LIKE` clauses to search your existing database — no external service required. For most applications, this is all you need. For an overview of all search options available in Laravel, consult the [search documentation](https://laravel.com/docs/12.x/search).
Scout also includes drivers for [custom engines](https://laravel.com/docs/12.x/scout#custom-engines) as well.
