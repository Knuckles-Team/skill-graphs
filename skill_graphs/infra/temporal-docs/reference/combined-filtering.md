# Combined filtering
/v1/metrics?namespaces=prod-*&metrics=temporal_cloud_v1_approximate_backlog_count
```

:::info

In Prometheus, the `params` config can be set to match the same behavior as above.

```yaml
scrape_configs:
- job_name: 'temporal-cloud'
  ...
  static_configs:
    - targets: ['metrics.temporal.io']
  metrics_path: '/v1/metrics'
  params:
    namespaces: ['prod-*']
    metrics: ['temporal_cloud_v1_approximate_backlog_count']

```

:::

### Label Management

#### Prometheus

If using Prometheus, you can configure it to drop metrics with a specific label or even rename specific label values to reduce the cardinality.

```yaml
metric_relabel_configs:
