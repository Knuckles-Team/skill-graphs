##  [How to fix](https://vercel.com/docs/getting-started-with-vercel#how-to-fix)[](https://vercel.com/docs/getting-started-with-vercel#how-to-fix)
To fix this, you can add a `modularizeImports` config to `next.config.js` for the package that uses barrel files. For example:
next.config.js
```
modularizeImports: {
  lodash: {
    transform: 'lodash/{{member}}';
  }
}
```

The exact format of the transform may differ by package, so double check how the package uses barrel files first.
See the
