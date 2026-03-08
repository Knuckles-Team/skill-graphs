##  [Configuring specific workspaces](https://vercel.com/docs/conformance/customize#configuring-specific-workspaces)[](https://vercel.com/docs/conformance/customize#configuring-specific-workspaces)
Each Conformance override accepts a `restrictTo` parameter which controls what workspaces the configuration will apply to. If no `restrictTo` is specified, then the configuration will apply globally to every workspace.
conformance.config.jsonc
```
{
  "overrides": [
    {
      // NOTE: No `restrictTo` is specified here so this applies globally.
      "rules": {},
    },
  ],
}
```

Conformance configuration can be applied to specific workspaces using either the name of the workspace or the directory of the workspace on the `restrictTo` field:
  * Use the `workspaces` field, which accepts a list of workspace names:
conformance.config.jsonc
```
{
  "overrides": [
    {
      "restrictTo": {
        "workspaces": ["eslint-config-custom"],
      },
      "rules": {},
    },
  ],
}
```

  * Use the `directories` field to specify a directory. All workspaces that live under that directory will be matched:
conformance.config.json
```
{
  "overrides": [
    {
      "restrictTo": {
        "directories": ["configs/"],
      },
      "rules": {},
    },
  ],
}
```

This will match `configs/tsconfig` and `configs/eslint-config-custom`.
  * Set the `root` field to true to match the root of the repository:
conformance.config.jsonc
```
{
  "overrides": [
    {
      "restrictTo": {
        "root": true,
      },
      "rules": {},
    },
  ],
}
```



###  [Configuration cascade](https://vercel.com/docs/conformance/customize#configuration-cascade)[](https://vercel.com/docs/conformance/customize#configuration-cascade)
If multiple overrides are specified that affect the same workspace, the configurations will be unioned together. If there are conflicts between the overrides, the last specified value will be used.
