## [Quickstart](https://laravel.com/docs/12.x/broadcasting#quickstart)
By default, broadcasting is not enabled in new Laravel applications. You may enable broadcasting using the `install:broadcasting` Artisan command:
```


1php artisan install:broadcasting




php artisan install:broadcasting

```

The `install:broadcasting` command will prompt you for which event broadcasting service you would like to use. In addition, it will create the `config/broadcasting.php` configuration file and the `routes/channels.php` file where you may register your application's broadcast authorization routes and callbacks.
Laravel supports several broadcast drivers out of the box: [Laravel Reverb](https://laravel.com/docs/12.x/reverb), `log` driver for local development and debugging. Additionally, a `null` driver is included which allows you to disable broadcasting during testing. A configuration example is included for each of these drivers in the `config/broadcasting.php` configuration file.
All of your application's event broadcasting configuration is stored in the `config/broadcasting.php` configuration file. Don't worry if this file does not exist in your application; it will be created when you run the `install:broadcasting` Artisan command.
#### [Next Steps](https://laravel.com/docs/12.x/broadcasting#quickstart-next-steps)
Once you have enabled event broadcasting, you're ready to learn more about [defining broadcast events](https://laravel.com/docs/12.x/broadcasting#defining-broadcast-events) and [listening for events](https://laravel.com/docs/12.x/broadcasting#listening-for-events). If you're using Laravel's React or Vue [starter kits](https://laravel.com/docs/12.x/starter-kits), you may listen for events using Echo's [useEcho hook](https://laravel.com/docs/12.x/broadcasting#using-react-or-vue).
Before broadcasting any events, you should first configure and run a [queue worker](https://laravel.com/docs/12.x/queues). All event broadcasting is done via queued jobs so that the response time of your application is not seriously affected by events being broadcast.
