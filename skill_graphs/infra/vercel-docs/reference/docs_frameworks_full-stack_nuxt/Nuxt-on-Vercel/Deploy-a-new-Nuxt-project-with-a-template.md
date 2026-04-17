## Deploy a new Nuxt project with a template
[View All Templates](https://vercel.com/templates/nuxt)
[![Nuxt.js 3 Boilerplate](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2FleiZ1j6r8MPRgnugYyWf3%2F01c94495dd082a948af73e871347c93e%2FCleanShot_2022-11-18_at_13.58.42_2x.png&w=3840&q=75) Nuxt.js 3 Boilerplate A Nuxt.js 3 app, bootstrapped with create-nuxt-app. ](https://vercel.com/templates/nuxt/nuxtjs-boilerplate)[![Nuxt AI Chatbot](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2F2JYEQBdJFmMb9niUVb3tJb%2F06dcfed55deee856edf845cd7afa6af5%2FCleanShot_2025-10-19_at_20.17.03_2x.png&w=3840&q=75) Nuxt AI Chatbot An AI chatbot template to build your own chatbot powered by Nuxt MDC and Vercel AI SDK. ](https://vercel.com/templates/nuxt/nuxt-ai-chatbot)[![Onelink](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2FYff7IWoq8oBeZI4bun01X%2F238fda2122860223189377c61f699303%2Foneline.jpeg&w=3840&q=75) Onelink A link-in-bio SaaS built with Nuxt.js, where the data lives in the URL – no database required. ](https://vercel.com/templates/nuxt/onelink)
[View All Templates](https://vercel.com/templates/nuxt)


Vercel deployments can [integrate with your git provider](https://vercel.com/docs/git) to [generate preview URLs](https://vercel.com/docs/deployments/environments#preview-environment-pre-production) for each pull request you make to your Nuxt project.
###  [Choosing a build command](https://vercel.com/docs/getting-started-with-vercel#choosing-a-build-command)[](https://vercel.com/docs/getting-started-with-vercel#choosing-a-build-command)
The following table outlines the differences between `nuxt build` and `nuxt generate` on Vercel:
Feature | `nuxt build` | `nuxt generate`
---|---|---
Default build command | Yes | No
Supports all Vercel features out of the box | Yes | Yes
[Supports SSR](https://vercel.com/docs/getting-started-with-vercel#server-side-rendering-ssr) | Yes | No
[Supports SSG](https://vercel.com/docs/getting-started-with-vercel#static-rendering) | Yes, [with nuxt config](https://vercel.com/docs/getting-started-with-vercel#static-rendering) | Yes
[Supports ISR](https://vercel.com/docs/getting-started-with-vercel#incremental-static-regeneration-isr) | Yes | No
In general, `nuxt build` is likely best for most use cases. Consider using `nuxt generate` to build [fully static sites](https://vercel.com/docs/getting-started-with-vercel#static-rendering).
