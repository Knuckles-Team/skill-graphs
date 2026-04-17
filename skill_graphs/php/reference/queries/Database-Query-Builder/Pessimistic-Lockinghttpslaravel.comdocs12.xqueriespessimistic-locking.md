## [Pessimistic Locking](https://laravel.com/docs/12.x/queries#pessimistic-locking)
The query builder also includes a few functions to help you achieve "pessimistic locking" when executing your `select` statements. To execute a statement with a "shared lock", you may call the `sharedLock` method. A shared lock prevents the selected rows from being modified until your transaction is committed:
```


1DB::table('users')




2    ->where('votes', '>', 100)




3    ->sharedLock()




4    ->get();




DB::table('users')
    ->where('votes', '>', 100)
    ->sharedLock()
    ->get();

```

Alternatively, you may use the `lockForUpdate` method. A "for update" lock prevents the selected records from being modified or from being selected with another shared lock:
```


1DB::table('users')




2    ->where('votes', '>', 100)




3    ->lockForUpdate()




4    ->get();




DB::table('users')
    ->where('votes', '>', 100)
    ->lockForUpdate()
    ->get();

```

While not obligatory, it is recommended to wrap pessimistic locks within a [transaction](https://laravel.com/docs/12.x/database#database-transactions). This ensures that the data retrieved remains unaltered in the database until the entire operation completes. In case of a failure, the transaction will roll back any changes and release the locks automatically:
```


 1DB::transaction(function () {




 2    $sender = DB::table('users')




 3        ->lockForUpdate()




 4        ->find(1);




 5 



 6    $receiver = DB::table('users')




 7        ->lockForUpdate()




 8        ->find(2);




 9 



10    if ($sender->balance < 100) {




11        throw new RuntimeException('Balance too low.');




12    }




13 



14    DB::table('users')




15        ->where('id', $sender->id)




16        ->update([




17            'balance' => $sender->balance - 100




18        ]);




19 



20    DB::table('users')




21        ->where('id', $receiver->id)




22        ->update([




23            'balance' => $receiver->balance + 100




24        ]);




25});




DB::transaction(function () {
    $sender = DB::table('users')
        ->lockForUpdate()
        ->find(1);

    $receiver = DB::table('users')
        ->lockForUpdate()
        ->find(2);

    if ($sender->balance < 100) {
        throw new RuntimeException('Balance too low.');
    }

    DB::table('users')
        ->where('id', $sender->id)
        ->update([
            'balance' => $sender->balance - 100
        ]);

    DB::table('users')
        ->where('id', $receiver->id)
        ->update([
            'balance' => $receiver->balance + 100
        ]);
});

```
