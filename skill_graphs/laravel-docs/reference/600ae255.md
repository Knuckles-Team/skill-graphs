## [Tables](https://laravel.com/docs/12.x/prompts#tables)
The `table` function makes it easy to display multiple rows and columns of data. All you need to do is provide the column names and the data for the table:
```


1use function Laravel\Prompts\table;




2 



3table(




4    headers: ['Name', 'Email'],




5    rows: User::all(['name', 'email'])->toArray()




6);




use function Laravel\Prompts\table;

table(
    headers: ['Name', 'Email'],
    rows: User::all(['name', 'email'])->toArray()
);

```
