## [Generating Mailables](https://laravel.com/docs/12.x/mail#generating-mailables)
When building Laravel applications, each type of email sent by your application is represented as a "mailable" class. These classes are stored in the `app/Mail` directory. Don't worry if you don't see this directory in your application, since it will be generated for you when you create your first mailable class using the `make:mail` Artisan command:
```


1php artisan make:mail OrderShipped




php artisan make:mail OrderShipped

```
