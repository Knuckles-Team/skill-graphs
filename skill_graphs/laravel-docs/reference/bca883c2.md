## [Generating Events and Listeners](https://laravel.com/docs/12.x/events#generating-events-and-listeners)
To quickly generate events and listeners, you may use the `make:event` and `make:listener` Artisan commands:
```


1php artisan make:event PodcastProcessed




2 



3php artisan make:listener SendPodcastNotification --event=PodcastProcessed




php artisan make:event PodcastProcessed

php artisan make:listener SendPodcastNotification --event=PodcastProcessed

```

For convenience, you may also invoke the `make:event` and `make:listener` Artisan commands without additional arguments. When you do so, Laravel will automatically prompt you for the class name and, when creating a listener, the event it should listen to:
```


1php artisan make:event




2 



3php artisan make:listener




php artisan make:event

php artisan make:listener

```
