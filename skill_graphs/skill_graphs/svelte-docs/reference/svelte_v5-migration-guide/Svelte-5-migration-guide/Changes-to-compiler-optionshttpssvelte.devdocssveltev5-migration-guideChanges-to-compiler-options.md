##  Changes to compiler options[](https://svelte.dev/docs/svelte/v5-migration-guide#Changes-to-compiler-options)
  * The `false` / `true` (already deprecated previously) and the `"none"` values were removed as valid values from the `css` option
  * The `legacy` option was repurposed
  * The `hydratable` option has been removed. Svelte components are always hydratable now
  * The `enableSourcemap` option has been removed. Source maps are always generated now, tooling can choose to ignore it
  * The `tag` option was removed. Use `<svelte:options customElement="tag-name" />` inside the component instead
  * The `loopGuardTimeout`, `format`, `sveltePath`, `errorMode` and `varsReport` options were removed
