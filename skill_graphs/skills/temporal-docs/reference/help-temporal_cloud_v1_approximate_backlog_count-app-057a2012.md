# HELP temporal_cloud_v1_approximate_backlog_count Approximate number of tasks in a task queue
temporal_cloud_v1_approximate_backlog_count{temporal_namespace="production",temporal_task_queue="critical-queue",task_type="workflow", region="aws-us-west-2"} 15.0 1609459200000
```

:::

#### Summary of Best Practices

* *Honor timestamps*: Set `honor_timestamps: true` in Prometheus
* *Scrape interval*: Use 30s. Intervals longer than 60s may skip datapoints because metrics update once per minute.
* *Timeout*: Set scrape timeout to 10 seconds for large responses
* *Filtering*: Use query parameters to reduce response size

### List Metric Descriptors

`GET /v1/descriptors`

Lists all metric descriptors including metadata, data types, and available dimensions (a.k.a. labels).

#### Query Parameters

| Parameter | Type | Description |
| ----- | ----- | ----- |
| `limit` | integer | Page size (1-100, default: 100\) |
| `offset` | integer | Page offset |

:::info Example

Request:

```shell
curl -H "Authorization: Bearer <API_KEY>" \
  "https://metrics.temporal.io/v1/descriptors"
```

Response:

```json
{
  "meta": {
    "pagination": {
      "total": 35,
      "limit": 100,
      "offset": 0
    }
  },
  "descriptors": [
    {
      "name": "temporal_cloud_v1_workflow_success_count",
      "help": "The number of successful workflows per second",
      "dimensions": [
        "temporal_namespace",
        "temporal_workflow_type",
        "temporal_task_queue",
        "region"
      ]
    }
  ]
}
```

:::

## Managing High Cardinality

:::caution

High-cardinality labels like `temporal_task_queue` and `temporal_workflow_type` can significantly increase metric volume and impact performance of your monitoring system.

:::

### Cardinality Estimation

To estimate your metric cardinality and see if this is an issue:

```
Total series = Base metrics × Namespaces × Task queues × Workflow types
```

Example:

* 6 workflow metrics with both labels
* 10 namespaces
* 50 task queues
* 20 workflow types
* \= 6 × 10 × 50 × 20 \= 60,000 time series

:::note

60,000 time series in the above example results in exceeding the 30,000 data points per scrape limit.

:::

If the cardinality is too high or you are hitting API limits, consider the following strategies.

### Filtering at Scrape Time

You can isolate only the metrics/namespaces you need.  For example, the following shows examples of filtering by modifying the `metrics_path.`

```shell
