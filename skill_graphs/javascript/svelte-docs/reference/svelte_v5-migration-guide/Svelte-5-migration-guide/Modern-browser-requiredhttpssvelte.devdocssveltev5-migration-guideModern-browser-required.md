##  Modern browser required[](https://svelte.dev/docs/svelte/v5-migration-guide#Modern-browser-required)
Svelte 5 requires a modern browser (in other words, not Internet Explorer) for various reasons:
  * it uses
  * elements with `clientWidth` / `clientHeight`/`offsetWidth`/`offsetHeight` bindings use a `<iframe>` hack
  * `<input type="range" bind:value={...} />` only uses an `input` event listener, rather than also listening for `change` events as a fallback


The `legacy` compiler option, which generated bulkier but IE-friendly code, no longer exists.
