# Build Output Configuration
Last updated August 15, 2025
`
.vercel/output/config.json
`


Schema (as TypeScript):
```
type Config = {
  version: 3;
  routes?: Route[];
  images?: ImagesConfig;
  wildcard?: WildcardConfig;
  overrides?: OverrideConfig;
  cache?: string[];
  crons?: CronsConfig;
};
```

Config Types:
  * [Route](https://vercel.com/docs/build-output-api/configuration#routes)
  * [ImagesConfig](https://vercel.com/docs/build-output-api/configuration#images)
  * [WildcardConfig](https://vercel.com/docs/build-output-api/configuration#wildcard)
  * [OverrideConfig](https://vercel.com/docs/build-output-api/configuration#overrides)
  * [CronsConfig](https://vercel.com/docs/build-output-api/configuration#crons)



The `config.json` file contains configuration information and metadata for a Deployment. The individual properties are described in greater detail in the sub-sections below.
At a minimum, a `config.json` file with a `"version"` property is _required_.
