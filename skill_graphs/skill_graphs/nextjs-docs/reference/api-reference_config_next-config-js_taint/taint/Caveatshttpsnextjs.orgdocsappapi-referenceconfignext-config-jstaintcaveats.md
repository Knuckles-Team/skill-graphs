## Caveats[](https://nextjs.org/docs/app/api-reference/config/next-config-js/taint#caveats)
  * Tainting can only keep track of objects by reference. Copying an object creates an untainted version, which loses all guarantees given by the API. You'll need to taint the copy.
  * Tainting cannot keep track of data derived from a tainted value. You also need to taint the derived value.
  * Values are tainted for as long as their lifetime reference is within scope. See the
