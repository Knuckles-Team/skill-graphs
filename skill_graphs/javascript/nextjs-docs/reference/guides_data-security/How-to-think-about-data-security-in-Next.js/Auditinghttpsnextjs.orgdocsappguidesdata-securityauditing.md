## Auditing[](https://nextjs.org/docs/app/guides/data-security#auditing)
If you're doing an audit of a Next.js project, here are a few things we recommend looking extra at:
  * **Data Access Layer:** Is there an established practice for an isolated Data Access Layer? Verify that database packages and environment variables are not imported outside the Data Access Layer.
  * **`"use client"`files:** Are the Component props expecting private data? Are the type signatures overly broad?
  * **`"use server"`files:** Are the Action arguments validated in the action or inside the Data Access Layer? Is the user re-authorized inside the action?
  * **`/[param]/.`**Folders with brackets are user input. Are params validated?
  * **`proxy.ts`and`route.ts` :** Have a lot of power. Spend extra time auditing these using traditional techniques. Perform Penetration Testing or Vulnerability Scanning regularly or in alignment with your team's software development lifecycle.
