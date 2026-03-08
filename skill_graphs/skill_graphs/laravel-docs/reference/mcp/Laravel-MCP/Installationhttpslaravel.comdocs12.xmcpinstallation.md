## [Installation](https://laravel.com/docs/12.x/mcp#installation)
To get started, install Laravel MCP into your project using the Composer package manager:
```


1composer require laravel/mcp




composer require laravel/mcp

```

### [Publishing Routes](https://laravel.com/docs/12.x/mcp#publishing-routes)
After installing Laravel MCP, execute the `vendor:publish` Artisan command to publish the `routes/ai.php` file where you will define your MCP servers:
```


1php artisan vendor:publish --tag=ai-routes




php artisan vendor:publish --tag=ai-routes

```

This command creates the `routes/ai.php` file in your application's `routes` directory, which you will use to register your MCP servers.
