##  [Use cases](https://vercel.com/docs/routing/redirects#use-cases)[](https://vercel.com/docs/routing/redirects#use-cases)
  * Moving to a new domain: Redirects help maintain a seamless user experience when moving a website to a new domain by ensuring that visitors and search engines are aware of the new location.
  * Replacing a removed page: If a page has been moved, temporarily or permanently, you can use redirects to send users to a relevant new page, thus avoiding any negative impact on user experience.
  * Canonicalization of multiple URLs: If your website can be accessed through several URLs (e.g., `acme.com/home`, `home.acme.com`, or `www.acme.com`), you can choose a canonical URL and use redirects to guide traffic from the other URLs to the chosen one.
  * Geolocation-based redirects: Redirects can be configured to consider the source country of requests, enabling tailored experiences for users based on their geographic location.


We recommend using status code `307` or `308` to avoid the ambiguity of non `GET` methods, which is necessary when your application needs to redirect a public API.
