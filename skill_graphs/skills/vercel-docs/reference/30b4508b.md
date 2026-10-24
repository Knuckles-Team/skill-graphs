##  [Example](https://vercel.com/docs/getting-started-with-vercel#example)[](https://vercel.com/docs/getting-started-with-vercel#example)
A workspace contains a `package.json` file that looks like:
package.json
```
{
  "name": "test-workspace",
  "scripts": {
    "build": "tsc -b"
  }
}
```

It does not contain a `conformance` script, so this check will fail.
