# Managing Nameservers
Last updated September 24, 2025
[Nameservers](https://vercel.com/docs/domains/working-with-nameservers) are used to resolve domain names to IP addresses. For domains with Vercel as the registrar, nameservers can be viewed, edited, and reset by selecting the domain from the [Domains section in your team dashboard sidebar](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fdomains&title=Go+to+team%27s+domains+page).
Sometimes, however, you may need to delegate nameserver management to another host. For domains registered with Vercel, you can [add custom nameservers](https://vercel.com/docs/project-configuration#add-custom-nameservers) to your Vercel-hosted domain, directly from the dashboard, allowing for delegation to other DNS providers. You can add up to four nameservers at once, and [revert to your previous settings](https://vercel.com/docs/project-configuration#restore-original-nameservers) if necessary.
For domains that are not registered with Vercel, you can change the nameservers directly from the domain registrar's dashboard.
Nameserver changes can take up to 48 hours to complete due to
