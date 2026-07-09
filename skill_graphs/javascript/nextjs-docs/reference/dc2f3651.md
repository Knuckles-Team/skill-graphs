# typescript
Last updated February 27, 2026
Configure TypeScript behavior with the `typescript` option in `next.config.js`:
next.config.js
```
module.exports = {
  typescript: {
    ignoreBuildErrors: false,
    tsconfigPath: 'tsconfig.json',
  },
}
```
