##  [Overwriting blobs](https://vercel.com/docs/vercel-blob#overwriting-blobs)[](https://vercel.com/docs/vercel-blob#overwriting-blobs)
By default, Vercel Blob prevents you from accidentally overwriting existing blobs by using the same pathname twice. When you attempt to upload a blob with a pathname that already exists, the operation will throw an error.
###  [Using `allowOverwrite`](https://vercel.com/docs/vercel-blob#using-allowoverwrite)[](https://vercel.com/docs/vercel-blob#using-allowoverwrite)
To explicitly allow overwriting existing blobs, you can use the `allowOverwrite` option:
```
const blob = await put('user-profile.jpg', imageFile, {
  access: 'private' /* or 'public' */,
  allowOverwrite: true, // Enable overwriting an existing blob with the same pathname
});
```

This option is available in these methods:
  * `put()`
  * In client uploads via the `onBeforeGenerateToken()` function


###  [When to use overwriting](https://vercel.com/docs/vercel-blob#when-to-use-overwriting)[](https://vercel.com/docs/vercel-blob#when-to-use-overwriting)
Overwriting blobs can be appropriate for certain use cases:
  1. Regularly updated files: For files that need to maintain the same URL but contain updated content (like JSON data files or configuration files)
  2. Content with predictable update patterns: For data that changes on a schedule and where consumers expect updates at the same URL


When overwriting blobs, be aware that due to [caching](https://vercel.com/docs/vercel-blob#caching), changes won't be immediately visible. The minimum time for changes to propagate is 60 seconds, and browser caches may need to be explicitly refreshed.
###  [Alternatives to overwriting](https://vercel.com/docs/vercel-blob#alternatives-to-overwriting)[](https://vercel.com/docs/vercel-blob#alternatives-to-overwriting)
If you want to avoid overwriting existing content (recommended for most use cases), you have two options:
  1. Use `addRandomSuffix: true`: This automatically adds a unique random suffix to your pathnames:


```
const blob = await put('avatar.jpg', imageFile, {
  access: 'private' /* or 'public' */,
  addRandomSuffix: true, // Creates a pathname like 'avatar-oYnXSVczoLa9yBYMFJOSNdaiiervF5.jpg'
});
```

  1. Generate unique pathnames programmatically: Create unique pathnames by adding timestamps, UUIDs, or other identifiers:


```
const timestamp = Date.now();
const blob = await put(`user-profile-${timestamp}.jpg`, imageFile, {
  access: 'private' /* or 'public' */
});
```
