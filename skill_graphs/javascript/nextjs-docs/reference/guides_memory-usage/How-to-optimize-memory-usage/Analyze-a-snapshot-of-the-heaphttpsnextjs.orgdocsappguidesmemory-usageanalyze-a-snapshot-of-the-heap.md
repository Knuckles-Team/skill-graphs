## Analyze a snapshot of the heap[](https://nextjs.org/docs/app/guides/memory-usage#analyze-a-snapshot-of-the-heap)
You can use an inspector tool to analyze the memory usage of the application.
When running the `next build` or `next dev` command, add `NODE_OPTIONS=--inspect` to the beginning of the command. This will expose the inspector agent on the default port. If you wish to break before any user code starts, you can pass `--inspect-brk` instead. While the process is running, you can use a tool such as Chrome DevTools to connect to the debugging port to record and analyze a snapshot of the heap to see what memory is being retained.
Starting in `14.2.0`, you can also run `next build` with the `--experimental-debug-memory-usage` flag to make it easier to take heap snapshots.
While running in this mode, you can send a `SIGUSR2` signal to the process at any point, and the process will take a heap snapshot.
The heap snapshot will be saved to the project root of the Next.js application and can be loaded in any heap analyzer, such as Chrome DevTools, to see what memory is retained. This mode is not yet compatible with Webpack build workers.
See
