## [Environment Variables](https://laravel.com/docs/12.x/vite#environment-variables)
You may inject environment variables into your JavaScript by prefixing them with `VITE_` in your application's `.env` file:
```


1VITE_SENTRY_DSN_PUBLIC=http://example.com




VITE_SENTRY_DSN_PUBLIC=http://example.com

```

You may access injected environment variables via the `import.meta.env` object:
```


1import.meta.env.VITE_SENTRY_DSN_PUBLIC




import.meta.env.VITE_SENTRY_DSN_PUBLIC

```
