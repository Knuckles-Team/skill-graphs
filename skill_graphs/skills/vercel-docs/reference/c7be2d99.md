##  [When not to use Static IPs](https://vercel.com/docs/security#when-not-to-use-static-ips)[](https://vercel.com/docs/security#when-not-to-use-static-ips)
Static IP is a service provided by Vercel that assigns a set of fixed outbound IP addresses used for egress traffic from your deployments. It does not assign a fixed public IP that external users or services can use to directly access or initiate inbound (ingress) traffic to your app. Therefore, Static IPs should not be used if you need your app to be reachable through a fixed inbound IP or require ingress traffic support, as inbound connections do not route through the Static IP service.
###  [Static IPs or Secure Compute](https://vercel.com/docs/security#static-ips-or-secure-compute)[](https://vercel.com/docs/security#static-ips-or-secure-compute)
Feature | Static IPs (Pro & Enterprise) | Secure Compute (Enterprise only)
---|---|---
IP type | Static in shared Virtual Private Cloud (VPC) | Static in dedicated VPC
Network isolation | Shared VPC for a small group of customers with subnet-level isolation | Dedicated VPC and subnet per customer
Use cases | IP allowlisting, database access | IP allowlisting, VPC Peering, full isolation
Pricing | $100/month per project, plus [Private Data Transfer](https://vercel.com/docs/pricing/regional-pricing) at regional rates | Custom pricing
###  [Static IPs with Secure Compute](https://vercel.com/docs/security#static-ips-with-secure-compute)[](https://vercel.com/docs/security#static-ips-with-secure-compute)
If your project uses [Secure Compute](https://vercel.com/docs/connectivity/secure-compute) and you have enabled Static IPs, Static IPs will be ignored.
