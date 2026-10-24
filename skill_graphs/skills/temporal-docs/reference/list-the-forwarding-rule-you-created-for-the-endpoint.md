# List the forwarding rule you created for the endpoint
gcloud compute forwarding-rules list \
  --filter="NAME:<endpoint-name>" \
  --format="value(IP_ADDRESS)"
