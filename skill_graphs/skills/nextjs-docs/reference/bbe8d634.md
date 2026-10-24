## Tips[](https://nextjs.org/docs/architecture/fast-refresh#tips)
  * Fast Refresh preserves React local state in function components (and Hooks) by default.
  * Sometimes you might want to _force_ the state to be reset, and a component to be remounted. For example, this can be handy if you're tweaking an animation that only happens on mount. To do this, you can add `// @refresh reset` anywhere in the file you're editing. This directive is local to the file, and instructs Fast Refresh to remount components defined in that file on every edit.
  * You can put `console.log` or `debugger;` into the components you edit during development.
  * Remember that imports are case sensitive. Both fast and full refresh can fail, when your import doesn't match the actual filename. For example, `'./header'` vs `'./Header'`.
