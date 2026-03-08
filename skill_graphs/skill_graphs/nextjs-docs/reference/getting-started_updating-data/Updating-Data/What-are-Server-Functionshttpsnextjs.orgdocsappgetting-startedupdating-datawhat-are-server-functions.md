## What are Server Functions?[](https://nextjs.org/docs/app/getting-started/updating-data#what-are-server-functions)
A **Server Function** is an asynchronous function that runs on the server. They can be called from the client through a network request, which is why they must be asynchronous.
In an `action` or mutation context, they are also called **Server Actions**.
> **Good to know:** A Server Action is a Server Function used in a specific way (for handling form submissions and mutations). Server Function is the broader term.
By convention, a Server Action is an async function used with
  * Passed to a `<form>` using the `action` prop.
  * Passed to a `<button>` using the `formAction` prop.


In Next.js, Server Actions integrate with the framework's [caching](https://nextjs.org/docs/app/guides/caching) architecture. When an action is invoked, Next.js can return both the updated UI and new data in a single server roundtrip.
Behind the scenes, actions use the `POST` method, and only this HTTP method can invoke them.
