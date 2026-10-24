##  [Outage resiliency](https://vercel.com/docs/regions#outage-resiliency)[](https://vercel.com/docs/regions#outage-resiliency)
Vercel's CDN is designed with high availability and fault tolerance in mind:
  * In the event of regional downtime, application traffic is automatically rerouted to the next closest region. This ensures that your application remains available to users even during localized outages.
  * Traffic will be rerouted to the next closest region in the following order:
