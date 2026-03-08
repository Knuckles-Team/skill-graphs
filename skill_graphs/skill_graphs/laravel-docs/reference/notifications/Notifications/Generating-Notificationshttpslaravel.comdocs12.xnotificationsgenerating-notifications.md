## [Generating Notifications](https://laravel.com/docs/12.x/notifications#generating-notifications)
In Laravel, each notification is represented by a single class that is typically stored in the `app/Notifications` directory. Don't worry if you don't see this directory in your application - it will be created for you when you run the `make:notification` Artisan command:
```


1php artisan make:notification InvoicePaid




php artisan make:notification InvoicePaid

```

This command will place a fresh notification class in your `app/Notifications` directory. Each notification class contains a `via` method and a variable number of message building methods, such as `toMail` or `toDatabase`, that convert the notification to a message tailored for that particular channel.
