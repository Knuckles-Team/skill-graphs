##  [](https://qdrant.tech/documentation/concepts/points/#awaiting-result)Awaiting result
If the API is called with the `&wait=false` parameter, or if it is not explicitly specified, the client will receive an acknowledgment of receiving data:
```
{
  "result": {
    "operation_id": 123,
    "status": "acknowledged"
  },
  "status": "ok",
  "time": 0.000206061
}

```

This response does not mean that the data is available for retrieval yet. This uses a form of eventual consistency. It may take a short amount of time before it is actually processed as updating the collection happens in the background. In fact, it is possible that such request eventually fails. If inserting a lot of vectors, we also recommend using asynchronous requests to take advantage of pipelining.
If the logic of your application requires a guarantee that the vector will be available for searching immediately after the API responds, then use the flag `?wait=true`. In this case, the API will return the result only after the operation is finished:
```
{
  "result": {
    "operation_id": 0,
    "status": "completed"
  },
  "status": "ok",
  "time": 0.000206061
}

```

##### Was this page useful?
![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg) Yes  ![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg) No
Thank you for your feedback! 🙏
We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/concepts/points.md) this page on GitHub, or
On this page:
  * [Points](https://qdrant.tech/documentation/concepts/points/#points)
    * [Point IDs](https://qdrant.tech/documentation/concepts/points/#point-ids)
    * [Vectors](https://qdrant.tech/documentation/concepts/points/#vectors)
    * [Upload points](https://qdrant.tech/documentation/concepts/points/#upload-points)
      * [Python client optimizations](https://qdrant.tech/documentation/concepts/points/#python-client-optimizations)
      * [Idempotence](https://qdrant.tech/documentation/concepts/points/#idempotence)
      * [Update Mode](https://qdrant.tech/documentation/concepts/points/#update-mode)
      * [Named vectors](https://qdrant.tech/documentation/concepts/points/#named-vectors)
      * [Sparse vectors](https://qdrant.tech/documentation/concepts/points/#sparse-vectors)
      * [Inference](https://qdrant.tech/documentation/concepts/points/#inference)
    * [Modify points](https://qdrant.tech/documentation/concepts/points/#modify-points)
      * [Update vectors](https://qdrant.tech/documentation/concepts/points/#update-vectors)
      * [Delete vectors](https://qdrant.tech/documentation/concepts/points/#delete-vectors)
      * [Update payload](https://qdrant.tech/documentation/concepts/points/#update-payload)
    * [Delete points](https://qdrant.tech/documentation/concepts/points/#delete-points)
    * [Conditional updates](https://qdrant.tech/documentation/concepts/points/#conditional-updates)
    * [Retrieve points](https://qdrant.tech/documentation/concepts/points/#retrieve-points)
    * [Scroll points](https://qdrant.tech/documentation/concepts/points/#scroll-points)
      * [Order points by payload key](https://qdrant.tech/documentation/concepts/points/#order-points-by-payload-key)
    * [Counting points](https://qdrant.tech/documentation/concepts/points/#counting-points)
    * [Batch update](https://qdrant.tech/documentation/concepts/points/#batch-update)
    * [Awaiting result](https://qdrant.tech/documentation/concepts/points/#awaiting-result)


#### Ready to get started with Qdrant?
© 2025 Qdrant.
[Terms](https://qdrant.tech/legal/terms_and_conditions/) [Privacy Policy](https://qdrant.tech/legal/privacy-policy/) [Impressum](https://qdrant.tech/legal/impressum/)
×
[ Powered by ](https://qdrant.tech/)
