# Using the REST API with the Firewall
Last updated November 25, 2025
The security section of the [Vercel REST API](https://vercel.com/docs/rest-api) allows you to programmatically interact with some of the functionality of the Vercel Firewall such as [creating a system bypass rule](https://vercel.com/docs/rest-api/reference/endpoints/security/create-system-bypass-rule) and [updating your Vercel WAF rule configuration](https://vercel.com/docs/rest-api/reference/endpoints/security/update-firewall-configuration).
You can use the REST API programmatically as follows:
  * Install the [Vercel SDK](https://vercel.com/docs/rest-api/sdk) and use the
  * [Call the endpoints directly](https://vercel.com/docs/rest-api) and use the [security endpoints](https://vercel.com/docs/rest-api/reference/endpoints/security).


To define firewall rules in code that apply across multiple projects, you can use the
After [setting up Terraform](https://vercel.com/kb/guide/integrating-terraform-with-vercel), you can use the following rules:
