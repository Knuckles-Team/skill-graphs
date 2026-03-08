## Getting started[](https://nextjs.org/docs/app/api-reference/turbopack#getting-started)
Turbopack is now the **default bundler** in Next.js. No configuration is needed to use Turbopack:
package.json
```
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start"
  }
}
```

### Using Webpack instead[](https://nextjs.org/docs/app/api-reference/turbopack#using-webpack-instead)
If you need to use Webpack instead of Turbopack, you can opt-in with the `--webpack` flag:
package.json
```
{
  "scripts": {
    "dev": "next dev --webpack",
    "build": "next build --webpack",
    "start": "next start"
  }
}
```
