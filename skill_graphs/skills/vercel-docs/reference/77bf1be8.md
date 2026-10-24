# Troubleshooting domains
Last updated February 9, 2026
There are many common reasons why your domain configuration may not be working. Check the following:
  * Is your domain [added](https://vercel.com/docs/domains/add-a-domain#add-and-configure-domain) to your Vercel project?
  * Is your custom domain pointed to the provided Vercel `CNAME`/`A` record correctly? You can check it by using `dig [example.com]` in your Terminal.
  * If you use the [nameservers method](https://vercel.com/docs/domains/troubleshooting#configuring-nameservers-for-wildcard-domains) on your apex domain, please refer to your DNS provider's documentation for the exact instructions on how to change authoritative nameservers.
  * Is the issue only local to you? Try to clear your browser cache, and flush DNS caches on your machine/network if possible.
