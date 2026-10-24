## Upgrade[](https://nextjs.org/docs/app/guides/upgrading/codemods#upgrade)
Upgrades your Next.js application, automatically running codemods and updating Next.js, React, and React DOM.
Terminal
```
npx @next/codemod upgrade [revision]
```

### Options[](https://nextjs.org/docs/app/guides/upgrading/codemods#options)
  * `revision` (optional): Specify the upgrade type (`patch`, `minor`, `major`), an NPM dist tag (e.g. `latest`, `canary`, `rc`), or an exact version (e.g. `15.0.0`). Defaults to `minor` for stable versions.
  * `--verbose`: Show more detailed output during the upgrade process.


For example:
Terminal
```
# Upgrade to the latest patch (e.g. 16.0.7 -> 16.0.8)
npx @next/codemod upgrade patch

# Upgrade to the latest minor (e.g. 15.3.7 -> 15.4.8). This is the default.
npx @next/codemod upgrade minor

# Upgrade to the latest major (e.g. 15.5.7 -> 16.0.7)
npx @next/codemod upgrade major

# Upgrade to a specific version
npx @next/codemod upgrade 16

# Upgrade to the canary release
npx @next/codemod upgrade canary
```

> **Good to know** :
>   * If the target version is the same as or lower than your current version, the command exits without making changes.
>   * During the upgrade, you may be prompted to choose which Next.js codemods to apply and run React 19 codemods if upgrading React.
>
