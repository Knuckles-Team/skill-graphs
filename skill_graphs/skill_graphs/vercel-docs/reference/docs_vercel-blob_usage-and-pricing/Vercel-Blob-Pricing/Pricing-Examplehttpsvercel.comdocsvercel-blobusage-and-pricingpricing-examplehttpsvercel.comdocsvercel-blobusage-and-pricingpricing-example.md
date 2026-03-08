##  [Pricing Example](https://vercel.com/docs/vercel-blob/usage-and-pricing#pricing-example)[](https://vercel.com/docs/vercel-blob/usage-and-pricing#pricing-example)
Let's say during one month of usage, you upload 120,000 blobs of which 30% (36,000 blobs) are uploaded using multipart uploads with 5 parts each. Your storage averages 50 GB and your blobs are downloaded 2.5 million times, with a 70% cache HIT ratio (meaning 30% or 750,000 downloads are cache MISSes), for a total of 350 GB of data transfer.
Here's the cost breakdown:
  * **Storage** : 50 GB total - 5 GB included = 45 GB extra at $0.023/GB = $1.04
  * **Simple Operations** : 750K (30% cache MISSes of 2.5M downloads + head calls) - 100K included = 650K extra at $0.40/1M = $0.26
  * **Advanced Operations** :
    * Single uploads: 84K (70% of 120K blobs)
    * Multipart uploads: 36K × (1 start + 5 parts + 1 completion) = 252K operations
    * Total: 336K - 10K included = 326K extra at $5.00/1M = $1.63
  * **Data Transfer** (iad1): 350 GB total - 100 GB included = 250 GB extra at $0.05/GB = $12.50
  * **Edge Requests** : 2.5M requests (all downloads) - 10M included = $0.00
  * **Fast Origin Transfer** (iad1): 105 GB (30% cache MISSes of 350 GB) - 100 GB included = 5 GB extra at $0.06/GB = $0.30


**Total** : $15.73/month
