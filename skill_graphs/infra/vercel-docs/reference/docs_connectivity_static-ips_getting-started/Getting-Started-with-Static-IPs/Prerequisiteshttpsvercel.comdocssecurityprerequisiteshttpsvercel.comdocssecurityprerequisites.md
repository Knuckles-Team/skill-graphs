##  [Prerequisites](https://vercel.com/docs/security#prerequisites)[](https://vercel.com/docs/security#prerequisites)
Before you dive in, make sure you have:
  * A project deployed on Vercel
  * A backend service that supports IP allowlisting
  * [Pro](https://vercel.com/docs/plans/pro-plan) or [Enterprise](https://vercel.com/docs/plans/enterprise) plan


  1. ###  [Access the Connectivity settings](https://vercel.com/docs/security#access-the-connectivity-settings)[](https://vercel.com/docs/security#access-the-connectivity-settings)
    1. Go to your Project Dashboard
    2. Navigate to Project Settings
    3. Click the Connectivity section
  2. ###  [Configure your region](https://vercel.com/docs/security#configure-your-region)[](https://vercel.com/docs/security#configure-your-region)
    1. Click Manage Active Regions
    2. Pick a region close to your backend services to keep latency down. You can pick up to 3 regions
    3. Your project gets assigned static IPs within a shared VPC for each configured region
  3. ###  [Get your static IP addresses and configure your backend service](https://vercel.com/docs/security#get-your-static-ip-addresses-and-configure-your-backend-service)[](https://vercel.com/docs/security#get-your-static-ip-addresses-and-configure-your-backend-service)
    1. Copy the static IP addresses from the dashboard
    2. Add the static IPs to your backend service's allowlist so it knows which IP addresses are allowed to connect
  4. ###  [Verify your connection](https://vercel.com/docs/security#verify-your-connection)[](https://vercel.com/docs/security#verify-your-connection)
To test your connection, redeploy your project that connects to your backend service. All your outbound traffic will now go through those static IPs and be routed via the static IPs.
