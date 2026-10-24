##  [Get started](https://vercel.com/docs/vercel-firewall/vercel-waf/system-bypass-rules#get-started)[](https://vercel.com/docs/vercel-firewall/vercel-waf/system-bypass-rules#get-started)
To add an IP address that should bypass system mitigations, open [Firewall](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Ffirewall&title=Go+to+Firewall) in the sidebar of your project and follow these steps:
  1. Select Configure on the top right of the Firewall overview page
  2. Scroll down to the System Bypass Rules section
  3. Select the + Add Rule button
  4. Complete the following fields in the Configure New System Bypass modal:
     * IP Address Or CIDR (required)
     * Domain (required): The domain connected to the project or use `*` to specify all domains connected to a project
     * Note: For future reference
  5. Select the Create System Bypass button
  6. Apply the changes:
     * When you make any change, you will see a Review Changes button appear or update on the top right with the number of changes requested
     * Select Review Changes and review the changes to be applied
     * Select Publish to apply the changes to your production deployment
