##  [Concurrency and queues](https://vercel.com/docs/builds#concurrency-and-queues)[](https://vercel.com/docs/builds#concurrency-and-queues)
When multiple builds are requested, Vercel manages concurrency and queues for you:
  1. Concurrency Slots: Each plan has a limit on how many builds can run at once. If all slots are busy, new builds wait until a slot is free.
  2. Branch-Based Queue: If new commits land on the same branch, Vercel skips older queued builds and prioritizes only the most recent commit. This ensures that the latest changes are always deployed first.
  3. On-Demand Concurrency: If you need more concurrent build slots or want certain production builds to jump the queue, consider enabling [On-Demand Concurrent Builds](https://vercel.com/docs/deployments/managing-builds#on-demand-concurrent-builds).
