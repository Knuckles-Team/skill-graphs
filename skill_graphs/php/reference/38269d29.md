## [Delete Statements](https://laravel.com/docs/12.x/queries#delete-statements)
The query builder's `delete` method may be used to delete records from the table. The `delete` method returns the number of affected rows. You may constrain `delete` statements by adding "where" clauses before calling the `delete` method:
```


1$deleted = DB::table('users')->delete();




2 



3$deleted = DB::table('users')->where('votes', '>', 100)->delete();




$deleted = DB::table('users')->delete();

$deleted = DB::table('users')->where('votes', '>', 100)->delete();

```
