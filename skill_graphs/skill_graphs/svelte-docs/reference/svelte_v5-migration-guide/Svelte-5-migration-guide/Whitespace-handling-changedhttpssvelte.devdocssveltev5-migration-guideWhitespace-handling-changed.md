##  Whitespace handling changed[](https://svelte.dev/docs/svelte/v5-migration-guide#Whitespace-handling-changed)
Previously, Svelte employed a very complicated algorithm to determine if whitespace should be kept or not. Svelte 5 simplifies this which makes it easier to reason about as a developer. The rules are:
  * Whitespace between nodes is collapsed to one whitespace
  * Whitespace at the start and end of a tag is removed completely
This new behavior is slightly different from native HTML rendering. For example, `<p>foo<span> - bar</span></p>` will render:
    * `foo - bar` in HTML
    * `foo- bar` in Svelte 5
You can reintroduce the missing space by moving it outside the `<span>`...
```
<p>foo <span>- bar</span></p>
```

...or, if necessary for styling reasons, including it as an expression:
```
<p>foo<span>{' '}- bar</span></p>
```

  * Certain exceptions apply such as keeping whitespace inside `pre` tags


As before, you can disable whitespace trimming by setting the `preserveWhitespace` option in your compiler settings or on a per-component basis in `<svelte:options>`.
