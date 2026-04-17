##  [How it works](https://vercel.com/docs/security#how-it-works)[](https://vercel.com/docs/security#how-it-works)
When you enable Static IPs, you get:
  * Shared infrastructure: Each VPC serves a small group of customers
  * Static egress: All outbound traffic routes through shared static IP pairs
  * Logical isolation: Subnet-level isolation maintains security between customers on the same VPC
  * NAT gateway: Traffic exits through a managed NAT gateway for consistent IPs
  * Build traffic: Traffic from both deployed functions and builds will route through the static IPs
