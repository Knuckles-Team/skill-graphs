## [Clearing Jobs From Queues](https://laravel.com/docs/12.x/queues#clearing-jobs-from-queues)
When using [Horizon](https://laravel.com/docs/12.x/horizon), you should use the `horizon:clear` command to clear jobs from the queue instead of the `queue:clear` command.
If you would like to delete all jobs from the default queue of the default connection, you may do so using the `queue:clear` Artisan command:
```


1php artisan queue:clear




php artisan queue:clear

```

You may also provide the `connection` argument and `queue` option to delete jobs from a specific connection and queue:
```


1php artisan queue:clear redis --queue=emails




php artisan queue:clear redis --queue=emails

```

Clearing jobs from queues is only available for the SQS, Redis, and database queue drivers. In addition, the SQS message deletion process takes up to 60 seconds, so jobs sent to the SQS queue up to 60 seconds after you clear the queue might also be deleted.
