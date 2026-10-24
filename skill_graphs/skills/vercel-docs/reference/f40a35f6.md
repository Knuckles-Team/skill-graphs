##  [Region list](https://vercel.com/docs/regions#region-list)[](https://vercel.com/docs/regions#region-list)
Regions table Region Code | Region Name | Reference Location
---|---|---
arn1 | eu-north-1 | Stockholm, Sweden
bom1 | ap-south-1 | Mumbai, India
cdg1 | eu-west-3 | Paris, France
cle1 | us-east-2 | Cleveland, USA
cpt1 | af-south-1 | Cape Town, South Africa
dub1 | eu-west-1 | Dublin, Ireland
dxb1 | me-central-1 | Dubai, United Arab Emirates
fra1 | eu-central-1 | Frankfurt, Germany
gru1 | sa-east-1 | São Paulo, Brazil
hkg1 | ap-east-1 | Hong Kong
hnd1 | ap-northeast-1 | Tokyo, Japan
iad1 | us-east-1 | Washington, D.C., USA
icn1 | ap-northeast-2 | Seoul, South Korea
kix1 | ap-northeast-3 | Osaka, Japan
lhr1 | eu-west-2 | London, United Kingdom
pdx1 | us-west-2 | Portland, USA
sfo1 | us-west-1 | San Francisco, USA
sin1 | ap-southeast-1 | Singapore
syd1 | ap-southeast-2 | Sydney, Australia
yul1 | ca-central-1 | Montréal, Canada
For information on different resource pricing based on region, see the [regional pricing](https://vercel.com/docs/pricing/regional-pricing) page.
###  [Points of Presence (PoPs)](https://vercel.com/docs/regions#points-of-presence-pops)[](https://vercel.com/docs/regions#points-of-presence-pops)
In addition to our 20 compute-capable regions, Vercel's CDN includes 126 PoPs distributed across the globe. These PoPs serve several crucial functions:
  1. TCP termination and routing: PoPs terminate TCP and route requests over a private network to the nearest Vercel region with single-digit millisecond latency.
  2. DDoS protection: They provide a first line of defense against distributed denial-of-service attacks.
  3. TLS termination: The Vercel region the request is routed to handles TLS encryption and decryption.


The extensive PoP network ensures that users worldwide can access your content with minimal latency, even if compute resources are concentrated in fewer regions.
