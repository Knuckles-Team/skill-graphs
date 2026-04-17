##  [Example](https://vercel.com/docs/conformance/rules/BFCACHE_INTEGRITY_NO_UNLOAD_LISTENERS#example)[](https://vercel.com/docs/conformance/rules/BFCACHE_INTEGRITY_NO_UNLOAD_LISTENERS#example)
Two examples of when this check would fail:
src/utils/handle-user-navigation.ts
```
export function handleUserNavigatingAway() {
  window.onunload = (event) => {
    console.log('Page has unloaded.');
  };
}

export function handleUserAboutToNavigateAway() {
  window.onbeforeunload = (event) => {
    console.log('Page is about to be unloaded.');
  };
}
```

src/utils/handle-user-navigation.ts
```
export function handleUserNavigatingAway() {
  window.addEventListener('unload', (event) => {
    console.log('Page has unloaded.');
  });
}

export function handleUserAboutToNavigateAway() {
  window.addEventListener('beforeunload', (event) => {
    console.log('Page is about to be unloaded.');
  });
}
```
