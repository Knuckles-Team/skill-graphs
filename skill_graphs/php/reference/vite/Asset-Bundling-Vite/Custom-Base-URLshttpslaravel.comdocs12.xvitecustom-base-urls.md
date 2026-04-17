## [Custom Base URLs](https://laravel.com/docs/12.x/vite#custom-base-urls)
If your Vite compiled assets are deployed to a domain separate from your application, such as via a CDN, you must specify the `ASSET_URL` environment variable within your application's `.env` file:
```


1ASSET_URL=https://cdn.example.com




ASSET_URL=https://cdn.example.com

```

After configuring the asset URL, all re-written URLs to your assets will be prefixed with the configured value:
```


1https://cdn.example.com/build/assets/app.9dce8d17.js




https://cdn.example.com/build/assets/app.9dce8d17.js

```

Remember that [absolute URLs are not re-written by Vite](https://laravel.com/docs/12.x/vite#url-processing), so they will not be prefixed.
