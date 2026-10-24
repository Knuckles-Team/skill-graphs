##  [Best practices for applying rules](https://vercel.com/docs/vercel-firewall/vercel-waf/custom-rules#best-practices-for-applying-rules)[](https://vercel.com/docs/vercel-firewall/vercel-waf/custom-rules#best-practices-for-applying-rules)
To ensure your Custom Rule behaves as intended:
  1. Test a Custom Rule by setting it up with a log action
  2. Observe the 10-minute live traffic to check the behavior
  3. Update the Custom Rule condition if needed. Once you're happy with the behavior, update the rule with a challenge, deny, or bypass, or rate limit action
