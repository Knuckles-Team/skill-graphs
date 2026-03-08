# Reverse Proxy Servers and Vercel
Last updated November 25, 2025
We do not recommend placing a reverse proxy server in front of your Vercel project as it affects Vercel's firewall in the following ways:
  * Vercel's CDN loses visibility into the traffic, which reduces the effectiveness of the firewall in identifying suspicious activity.
  * Real end-user IP addresses cannot be accurately identified.
  * If the reverse proxy undergoes a malicious attack, this traffic can be forwarded to the Vercel project and cause usage spikes.
  * If the reverse proxy is compromised, Vercel's firewall cannot automatically purge the cache.
