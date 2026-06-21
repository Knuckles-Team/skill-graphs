##  [Storage calculation](https://vercel.com/docs/vercel-blob#storage-calculation)[](https://vercel.com/docs/vercel-blob#storage-calculation)
Vercel Blob measures your storage usage by taking snapshots of your blob store size every 15 minutes and averages these measurements over the entire month to calculate your GB-month usage. This approach accounts for fluctuations in storage as blobs are added and removed, ensuring you're only billed for your actual usage over time, not peak usage.
The Vercel dashboard displays two metrics:
  * Latest value: The most recent measurement of your blob store size
  * Monthly average: The average of all measurements throughout the billing period (this is what you're billed for)


Example:
  1. Day 1: Upload a 2GB file → Store size: 2GB
  2. Day 15: Add 1GB file → Store size: 3GB
  3. Day 25: Delete 2GB file → Store size: 1GB


Month end billing:
  * Latest value: 1GB
  * Monthly average: ~2GB (billed amount)


If no changes occur in the following month (no new uploads or deletions), each 15-minute measurement would consistently show 1 GB. In this case, your next month's billing would be exactly 1 GB/month, as your monthly average would equal your latest value.
