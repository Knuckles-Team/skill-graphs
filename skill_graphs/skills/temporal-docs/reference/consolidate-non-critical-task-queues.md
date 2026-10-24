# Consolidate non-critical task queues
- source_labels: [temporal_task_queue]
  regex: '(critical-queue|payment-queue)'
  target_label: __tmp_keep_original
  replacement: 'true'

- source_labels: [__tmp_keep_original]
  regex: ''
  target_label: temporal_task_queue
  replacement: 'other'

- regex: '__tmp_keep_original'
  action: labeldrop
```

#### OpenTelemetry Collector

To accomplish the same as Prometheus, a filter can be used in the collector along with any other processors.

```
processors:
  filter:
    metrics:
      include:
        match_type: regexp
        expressions:
          # Only keep metrics with critical-queue or payment-queue
          - Label("temporal_task_queue") == nil or IsMatch(Label("temporal_task_queue"), "^(critical-queue|payment-queue)$")
```

### Monitoring Cardinality

Cardinality can be monitored using this PromQL query.

```shell
