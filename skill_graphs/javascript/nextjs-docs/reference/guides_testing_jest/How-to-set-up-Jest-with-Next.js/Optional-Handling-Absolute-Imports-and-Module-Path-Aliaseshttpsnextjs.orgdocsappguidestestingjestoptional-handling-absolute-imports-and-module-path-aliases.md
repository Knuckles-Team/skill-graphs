## Optional: Handling Absolute Imports and Module Path Aliases[](https://nextjs.org/docs/app/guides/testing/jest#optional-handling-absolute-imports-and-module-path-aliases)
If your project is using [Module Path Aliases](https://nextjs.org/docs/app/getting-started/installation#set-up-absolute-imports-and-module-path-aliases), you will need to configure Jest to resolve the imports by matching the paths option in the `jsconfig.json` file with the `moduleNameMapper` option in the `jest.config.js` file. For example:
tsconfig.json or jsconfig.json
```
{
  "compilerOptions": {
    "module": "esnext",
    "moduleResolution": "bundler",
    "baseUrl": "./",
    "paths": {
      "@/components/*": ["components/*"]
    }
  }
}
```

jest.config.js
```
moduleNameMapper: {
  // ...
  '^@/components/(.*)$': '<rootDir>/components/$1',
}
```
