# Average latency
rate(temporal_cloud_v0_service_latency_sum[$__rate_interval])
/ rate(temporal_cloud_v0_service_latency_count[$__rate_interval])
