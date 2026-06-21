## Record a heap profile[](https://nextjs.org/docs/app/guides/memory-usage#record-a-heap-profile)
To look for memory issues, you can record a heap profile from Node.js and load it in Chrome DevTools to identify potential sources of memory leaks.
In your terminal, pass the `--heap-prof` flag to Node.js when starting your Next.js build:
```
node --heap-prof node_modules/next/dist/bin/next build
```

At the end of the build, a `.heapprofile` file will be created by Node.js.
In Chrome DevTools, you can open the Memory tab and click on the "Load Profile" button to visualize the file.
