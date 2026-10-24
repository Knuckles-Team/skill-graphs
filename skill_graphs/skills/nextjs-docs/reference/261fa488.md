## Bundler Compatibility[](https://nextjs.org/docs/pages/guides/migrating/from-create-react-app#bundler-compatibility)
Create React App uses webpack for bundling. Next.js now defaults to [Turbopack](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopack) for faster local development:
```
next dev  # Uses Turbopack by default
```

To use Webpack instead (similar to CRA):
```
next dev --webpack
```

You can still provide a [custom webpack configuration](https://nextjs.org/docs/app/api-reference/config/next-config-js/webpack) if you need to migrate advanced webpack settings from CRA.
