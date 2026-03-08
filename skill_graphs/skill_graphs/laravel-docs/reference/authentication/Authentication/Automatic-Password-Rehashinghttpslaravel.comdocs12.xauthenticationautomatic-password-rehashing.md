## [Automatic Password Rehashing](https://laravel.com/docs/12.x/authentication#automatic-password-rehashing)
Laravel's default password hashing algorithm is bcrypt. The "work factor" for bcrypt hashes can be adjusted via your application's `config/hashing.php` configuration file or the `BCRYPT_ROUNDS` environment variable.
Typically, the bcrypt work factor should be increased over time as CPU / GPU processing power increases. If you increase the bcrypt work factor for your application, Laravel will gracefully and automatically rehash user passwords as users authenticate with your application via Laravel's starter kits or when you [manually authenticate users](https://laravel.com/docs/12.x/authentication#authenticating-users) via the `attempt` method.
Typically, automatic password rehashing should not disrupt your application; however, you may disable this behavior by publishing the `hashing` configuration file:
```


1php artisan config:publish hashing




php artisan config:publish hashing

```

Once the configuration file has been published, you may set the `rehash_on_login` configuration value to `false`:
```


1'rehash_on_login' => false,




'rehash_on_login' => false,

```
