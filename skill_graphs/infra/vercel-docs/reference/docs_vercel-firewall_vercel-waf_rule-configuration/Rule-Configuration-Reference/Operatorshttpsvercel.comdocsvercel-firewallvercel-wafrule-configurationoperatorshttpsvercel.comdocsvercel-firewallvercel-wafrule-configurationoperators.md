##  [Operators](https://vercel.com/docs/vercel-firewall/vercel-waf/rule-configuration#operators)[](https://vercel.com/docs/vercel-firewall/vercel-waf/rule-configuration#operators)
All operators are case insensitive.
Operators Rule Parameters Parameter | Value | Description
---|---|---
Equals | `eq` |
  * An exact string match


Does not equal | `neq` | Inverse of **Equals**
Is any of | `inc` |
  * An exact string match, matching any of the provided values
  * Acts like a `SQL IN` query


Is not any of | `ninc` |
  * Ensures the source is not a match with any of the provided values
  * Acts like a `SQL NOT IN` query


Contains | `sub` |
  * Includes the provided value


Does not contain | `sub` | Inverse of **Contains**. Set the `neg` parameter to `true`
Starts with | `pre` |
  * A string operator matching the start of the string
  * Optimized for performance. It's preferred to use this over a regex prefix expression


Ends with | `suf` |
  * A string operator matching the end of the string
  * Optimized for performance. It's preferred to use this over a regex suffix expression


Matches expression | `re` |
  * A PCRE (
  * Useful for negative matches like “does not contain” or similar strict matching criteria


Does not match expression | `re` | Inverse of **Matches expression**. Set the `neg` parameter to `true`
