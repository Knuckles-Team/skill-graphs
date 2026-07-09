## Getting Started[](https://nextjs.org/docs/app/guides/open-telemetry#getting-started)
OpenTelemetry is extensible but setting it up properly can be quite verbose. That's why we prepared a package `@vercel/otel` that helps you get started quickly.
### Using `@vercel/otel`[](https://nextjs.org/docs/app/guides/open-telemetry#using-vercelotel)
To get started, install the following packages:
pnpmnpmyarnbun
Terminal
```
pnpm add @vercel/otel @opentelemetry/sdk-logs @opentelemetry/api-logs @opentelemetry/instrumentation
```

Next, create a custom [`instrumentation.ts`](https://nextjs.org/docs/app/guides/instrumentation) (or `.js`) file in the **root directory** of the project (or inside `src` folder if using one):
your-project/instrumentation.ts
TypeScript
JavaScript TypeScript
```
import { registerOTel } from '@vercel/otel'

export function register() {
  registerOTel({ serviceName: 'next-app' })
}
```

See the
> **Good to know** :
>   * The `instrumentation` file should be in the root of your project and not inside the `app` or `pages` directory. If you're using the `src` folder, then place the file inside `src` alongside `pages` and `app`.
>   * If you use the [`pageExtensions` config option](https://nextjs.org/docs/app/api-reference/config/next-config-js/pageExtensions) to add a suffix, you will also need to update the `instrumentation` filename to match.
>   * We have created a basic
>

### Manual OpenTelemetry configuration[](https://nextjs.org/docs/app/guides/open-telemetry#manual-opentelemetry-configuration)
The `@vercel/otel` package provides many configuration options and should serve most of common use cases. But if it doesn't suit your needs, you can configure OpenTelemetry manually.
Firstly you need to install OpenTelemetry packages:
pnpmnpmyarnbun
Terminal
```
pnpm add @opentelemetry/sdk-node @opentelemetry/resources @opentelemetry/semantic-conventions @opentelemetry/sdk-trace-node @opentelemetry/exporter-trace-otlp-http
```

Now you can initialize `NodeSDK` in your `instrumentation.ts`. Unlike `@vercel/otel`, `NodeSDK` is not compatible with edge runtime, so you need to make sure that you are importing them only when `process.env.NEXT_RUNTIME === 'nodejs'`. We recommend creating a new file `instrumentation.node.ts` which you conditionally import only when using node:
instrumentation.ts
TypeScript
JavaScript TypeScript
```
export async function register() {
  if (process.env.NEXT_RUNTIME === 'nodejs') {
    await import('./instrumentation.node.ts')
  }
}
```

instrumentation.node.ts
TypeScript
JavaScript TypeScript
```
import { OTLPTraceExporter } from '@opentelemetry/exporter-trace-otlp-http'
import { resourceFromAttributes } from '@opentelemetry/resources'
import { NodeSDK } from '@opentelemetry/sdk-node'
import { SimpleSpanProcessor } from '@opentelemetry/sdk-trace-node'
import { ATTR_SERVICE_NAME } from '@opentelemetry/semantic-conventions'

const sdk = new NodeSDK({
  resource: resourceFromAttributes({
    [ATTR_SERVICE_NAME]: 'next-app',
  }),
  spanProcessor: new SimpleSpanProcessor(new OTLPTraceExporter()),
})
sdk.start()
```

Doing this is equivalent to using `@vercel/otel`, but it's possible to modify and extend some features that are not exposed by the `@vercel/otel`. If edge runtime support is necessary, you will have to use `@vercel/otel`.
