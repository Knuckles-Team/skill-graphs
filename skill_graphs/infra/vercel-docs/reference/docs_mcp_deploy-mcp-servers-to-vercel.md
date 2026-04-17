Getting Started
Getting Started
# Getting started with Vercel
Last updated September 24, 2025
Vercel is a platform for developers that provides the tools, workflows, and infrastructure you need to build and deploy your web apps faster, without the need for additional configuration.
Vercel supports [popular frontend frameworks](https://vercel.com/docs/frameworks) out-of-the-box, and its scalable, secure infrastructure is globally distributed to serve content from data centers near your users for optimal speeds.
During development, Vercel provides tools for real-time collaboration on your projects such as automatic preview and production environments, and comments on preview deployments.
##  [Before you begin](https://vercel.com/docs/getting-started-with-vercel#before-you-begin)[](https://vercel.com/docs/getting-started-with-vercel#before-you-begin)
To get started, create an account with Vercel. You can [select the plan](https://vercel.com/docs/plans) that's right for you.
  * [Sign up for a new Vercel account](https://vercel.com/signup)
  * [Log in to your existing Vercel account](https://vercel.com/login)


Once you create an account, you can choose to authenticate either with a Git provider or by using an email. When using email authentication, you may need to confirm both your email address and a phone number.
##  [Customizing your journey](https://vercel.com/docs/getting-started-with-vercel#customizing-your-journey)[](https://vercel.com/docs/getting-started-with-vercel#customizing-your-journey)
This tutorial is framework agnostic but Vercel supports many frontend [frameworks](https://vercel.com/docs/frameworks/more-frameworks). As you go through the docs, the quickstarts will provide specific instructions for your framework. If you don't find what you need, give us feedback and we'll update them!
While many of our instructions use the dashboard, you can also use [Vercel CLI](https://vercel.com/docs/cli) to carry out most tasks on Vercel. In this tutorial, look for the "Using CLI?" section for the CLI steps. To use the CLI, you'll need to install it:
Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm i -g vercel
```

```
yarn global add vercel
```

```
npm i -g vercel
```

```
bun add -g vercel
```

[Let's go](https://vercel.com/docs/getting-started-with-vercel/projects-deployments)
* * *
[ Previous Vercel Documentation ](https://vercel.com/docs)[ Next Projects and Deployments ](https://vercel.com/docs/getting-started-with-vercel/projects-deployments)
Was this helpful?
Send
Getting Started
# Deploy MCP servers to Vercel
Last updated January 29, 2026
Deploy your Model Context Protocol (MCP) servers on Vercel to [take advantage of features](https://vercel.com/docs/mcp/deploy-mcp-servers-to-vercel#deploy-mcp-servers-efficiently) like [Vercel Functions](https://vercel.com/docs/functions), [OAuth](https://vercel.com/docs/mcp/deploy-mcp-servers-to-vercel#enabling-authorization), and [efficient scaling](https://vercel.com/docs/fluid-compute) for AI applications.
  * Get started with [deploying MCP servers on Vercel](https://vercel.com/docs/getting-started-with-vercel#deploy-an-mcp-server-on-vercel)
  * Learn how to [enable authorization](https://vercel.com/docs/getting-started-with-vercel#enabling-authorization) to secure your MCP server


Get started in minutes
## Deploy a Template
[View All Templates](https://vercel.com/templates/)
[![ChatGPT app with Next.js ](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2F5PRJ9rK7DQfBKHB0QD6lq5%2F583aaaa7fd69c1e08c2197a5bc96a34d%2Fchatgpt__1_.png&w=3840&q=75) ChatGPT app with Next.js  Ship a ChatGPT app on Vercel with Next.js and Model Context Protocol (MCP).  ](https://vercel.com/templates/next.js/chatgpt-app-with-next-js)[![x402 AI Starter](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2FRySDRkLC7OpZaTg9gNXRg%2F6010713a043bc3eec14160e796f09acf%2Fscreenshot.png&w=3840&q=75) x402 AI Starter A fullstack template for using x402 with MCP and AI SDK. ](https://vercel.com/templates/next.js/x402-ai-starter)[![MCP with Next.js](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2F73N0dZEENNBHEK030NFGlR%2F643235f2fbd7c082c7333bb315fab891%2FMCP__6_.jpg&w=3840&q=75) MCP with Next.js Run an Model Context Protocol (MCP) server on Vercel with Next.js. ](https://vercel.com/templates/next.js/model-context-protocol-mcp-with-next-js)
[View All Templates](https://vercel.com/templates/)
##  [Deploy MCP servers efficiently](https://vercel.com/docs/getting-started-with-vercel#deploy-mcp-servers-efficiently)[](https://vercel.com/docs/getting-started-with-vercel#deploy-mcp-servers-efficiently)
Vercel provides the following features for production MCP deployments:
  * Optimized cost and performance: [Vercel Functions](https://vercel.com/docs/functions) with [Fluid compute](https://vercel.com/docs/fluid-compute) handle MCP servers' irregular usage patterns (long idle times, quick message bursts, heavy AI workloads) through [optimized concurrency](https://vercel.com/docs/getting-started-with-vercel/fundamental-concepts/what-is-compute#optimized-concurrency), [dynamic scaling](https://vercel.com/docs/getting-started-with-vercel/fundamental-concepts/what-is-compute#dynamic-scaling), and [instance sharing](https://vercel.com/docs/getting-started-with-vercel/fundamental-concepts/what-is-compute#compute-instance-sharing). You only pay for compute resources you actually use with minimal idle time.
  * [Instant Rollback](https://vercel.com/docs/instant-rollback): Quickly revert to previous production deployments if issues arise with your MCP server.
  * [Preview deployments with Deployment Protection](https://vercel.com/docs/deployment-protection): Secure your preview MCP servers and test changes safely before production
  * [Vercel Firewall](https://vercel.com/docs/vercel-firewall): Protect your MCP servers from malicious attacks and unauthorized access with multi-layered security
  * [Rolling Releases](https://vercel.com/docs/rolling-releases): Gradually roll out new MCP server deployments to a fraction of users before promoting to everyone


##  [Deploy an MCP server on Vercel](https://vercel.com/docs/getting-started-with-vercel#deploy-an-mcp-server-on-vercel)[](https://vercel.com/docs/getting-started-with-vercel#deploy-an-mcp-server-on-vercel)
Use the `mcp-handler` package and create the following API route to host an MCP server that provides a single tool that rolls a dice.
app/api/mcp/route.ts
```
import { z } from 'zod';
import { createMcpHandler } from 'mcp-handler';

const handler = createMcpHandler(
  (server) => {
    server.tool(
      'roll_dice',
      'Rolls an N-sided die',
      { sides: z.number().int().min(2) },
      async ({ sides }) => {
        const value = 1 + Math.floor(Math.random() * sides);
        return {
          content: [{ type: 'text', text: `🎲 You rolled a ${value}!` }],
        };
      },
    );
  },
  {},
  { basePath: '/api' },
);

export { handler as GET, handler as POST, handler as DELETE };
```

###  [Test the MCP server locally](https://vercel.com/docs/getting-started-with-vercel#test-the-mcp-server-locally)[](https://vercel.com/docs/getting-started-with-vercel#test-the-mcp-server-locally)
This assumes that your MCP server application, with the above-mentioned API route, runs locally at `http://localhost:3000`.
  1. Run the MCP inspector:


Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm dlx @modelcontextprotocol/inspector@latest http://localhost:3000 undefined
```

```
yarn dlx @modelcontextprotocol/inspector@latest http://localhost:3000 undefined
```

```
npx @modelcontextprotocol/inspector@latest http://localhost:3000 undefined
```

```
bunx @modelcontextprotocol/inspector@latest http://localhost:3000 undefined
```

  1. Open the inspector interface:
     * Browse to `http://127.0.0.1:6274` where the inspector runs by default
  2. Connect to your MCP server:
     * Select Streamable HTTP in the drop-down on the left
     * In the URL field, use `http://localhost:3000/api/mcp`
     * Expand Configuration
     * In the Proxy Session Token field, paste the token from the terminal where your MCP server is running
     * Click Connect
  3. Test the tools:
     * Click List Tools under Tools
     * Click on the `roll_dice` tool
     * Test it through the available options on the right of the tools section


When you deploy your application on Vercel, you will get a URL such as `https://my-mcp-server.vercel.app`.
###  [Configure an MCP host](https://vercel.com/docs/getting-started-with-vercel#configure-an-mcp-host)[](https://vercel.com/docs/getting-started-with-vercel#configure-an-mcp-host)
Using
.cursor/mcp.json
```
{
  "mcpServers": {
    "server-name": {
      "url": "https://my-mcp-server.vercel.app/api/mcp"
    }
  }
}
```

You can now use your MCP roll dice tool in
##  [Enabling authorization](https://vercel.com/docs/getting-started-with-vercel#enabling-authorization)[](https://vercel.com/docs/getting-started-with-vercel#enabling-authorization)
The `mcp-handler` provides built-in OAuth support to secure your MCP server. This ensures that only authorized clients with valid tokens can access your tools.
###  [Secure your server with OAuth](https://vercel.com/docs/getting-started-with-vercel#secure-your-server-with-oauth)[](https://vercel.com/docs/getting-started-with-vercel#secure-your-server-with-oauth)
To add OAuth authorization to [the MCP server you created in the previous section](https://vercel.com/docs/getting-started-with-vercel#deploy-an-mcp-server-on-vercel):
  1. Use the `withMcpAuth` function to wrap your MCP handler
  2. Implement token verification logic
  3. Configure required scopes and metadata path


app/api/[transport]/route.ts
```
import { withMcpAuth } from 'mcp-handler';
import { AuthInfo } from '@modelcontextprotocol/sdk/server/auth/types.js';

const handler = createMcpHandler(/* ... same configuration as above ... */);

const verifyToken = async (
  req: Request,
  bearerToken?: string,
): Promise<AuthInfo | undefined> => {
  if (!bearerToken) return undefined;

  const isValid = bearerToken === '123';
  if (!isValid) return undefined;

  return {
    token: bearerToken,
    scopes: ['read:stuff'],
    clientId: 'user123',
    extra: {
      userId: '123',
    },
  };
};

const authHandler = withMcpAuth(handler, verifyToken, {
  required: true,
  requiredScopes: ['read:stuff'],
  resourceMetadataPath: '/.well-known/oauth-protected-resource',
});

export { authHandler as GET, authHandler as POST };
```

###  [Expose OAuth metadata endpoint](https://vercel.com/docs/getting-started-with-vercel#expose-oauth-metadata-endpoint)[](https://vercel.com/docs/getting-started-with-vercel#expose-oauth-metadata-endpoint)
To comply with the MCP specification, your server must expose a
####  [How to add OAuth metadata endpoint](https://vercel.com/docs/getting-started-with-vercel#how-to-add-oauth-metadata-endpoint)[](https://vercel.com/docs/getting-started-with-vercel#how-to-add-oauth-metadata-endpoint)
  1. In your `app/` directory, create a `.well-known` folder.
  2. Inside this directory, create a subdirectory called `oauth-protected-resource`.
  3. In this subdirectory, create a `route.ts` file with the following code for that specific route.
  4. Replace the `https://example-authorization-server-issuer.com` URL with your own


app/.well-known/oauth-protected-resource/route.ts
```
import {
  protectedResourceHandler,
  metadataCorsOptionsRequestHandler,
} from 'mcp-handler';

const handler = protectedResourceHandler({
  authServerUrls: ['https://example-authorization-server-issuer.com'],
});

const corsHandler = metadataCorsOptionsRequestHandler();

export { handler as GET, corsHandler as OPTIONS };
```

To view the full list of values available to be returned in the OAuth Protected Resource Metadata JSON, see the protected resource metadata
MCP clients that are compliant with the latest version of the MCP spec can now securely connect and invoke tools defined in your MCP server, when provided with a valid OAuth token.
##  [More resources](https://vercel.com/docs/getting-started-with-vercel#more-resources)[](https://vercel.com/docs/getting-started-with-vercel#more-resources)
Learn how to deploy MCP servers on Vercel, connect to them using the AI SDK, and explore curated lists of public MCP servers.
  * [Deploy an MCP server with Next.js on Vercel](https://vercel.com/templates/ai/model-context-protocol-mcp-with-next-js)
  * [Deploy an MCP server with Vercel Functions](https://vercel.com/templates/other/model-context-protocol-mcp-with-vercel-functions)
  * [Deploy an xmcp server](https://vercel.com/templates/backend/xmcp-boilerplate)
  * [Learn about MCP server support on Vercel](https://vercel.com/changelog/mcp-server-support-on-vercel)


* * *
[ Previous Vercel Documentation ](https://vercel.com/docs)[ Next Projects and Deployments ](https://vercel.com/docs/getting-started-with-vercel/projects-deployments)
Was this helpful?
Send
