## Loading Environment Variables[](https://nextjs.org/docs/app/guides/environment-variables#loading-environment-variables)
Next.js has built-in support for loading environment variables from `.env*` files into `process.env`.
.env
```
DB_HOST=localhost
DB_USER=myuser
DB_PASS=mypassword
```

> **Note** : Next.js also supports multiline variables inside of your `.env*` files:
> ```
