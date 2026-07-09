##  [Configuring context propagation](https://vercel.com/docs/multi-tenant#configuring-context-propagation)[](https://vercel.com/docs/multi-tenant#configuring-context-propagation)
Context propagation connects operations across service boundaries so you can trace a request through your entire system. When your app calls another service, context propagation passes trace metadata (for example,trace IDs, span IDs) along with the request, typically through HTTP headers like `traceparent`. This lets OpenTelemetry link all the spans together into a single, complete trace.
Without context propagation, each service generates isolated spans you can't connect. With it, you see exactly how a request flows through your infrastructure—from the initial API call through databases, queues, and external services.
For more details on how context propagation works, see the
###  [For outgoing requests](https://vercel.com/docs/multi-tenant#for-outgoing-requests)[](https://vercel.com/docs/multi-tenant#for-outgoing-requests)
You can configure context propagation by configuring the `fetch` option in the `instrumentationConfig` option.
instrumentation.ts
TypeScript
TypeScript JavaScript Bash
```
import { registerOTel } from '@vercel/otel';

export function register() {
  registerOTel({
    serviceName: `your-project-name`,
    instrumentationConfig: {
      fetch: {
        // This URLs will have the tracing context propagated to them.
        propagateContextUrls: [
          'your-service-domain.com',
          'your-database-domain.com',
        ],
        // This URLs will not have the tracing context propagated to them.
        dontPropagateContextUrls: [
          'some-third-party-service-domain.com',
        ],
        // This URLs will be ignored and will not be traced.
        ignoreUrls: ['my-internal-private-tool.com'],
      },
    },
  });
}
// NOTE: You can replace `your-project-name` with the actual name of your project
```

###  [From incoming requests](https://vercel.com/docs/multi-tenant#from-incoming-requests)[](https://vercel.com/docs/multi-tenant#from-incoming-requests)
Next.js 13.4+ supports automatic OpenTelemetry context propagation for incoming requests. For other frameworks, that do not support automatic OpenTelemetry context propagation, you can refer to the following code example to manually inject the inbound context into a request handler.
api-handler.ts
```
import { propagation, context, trace } from "@opentelemetry/api";

const tracer = trace.getTracer('custom-tracer');

// This function injects the inbound context into the request handler
function injectInboundContext(f: (request: Request) => Promise<Response>): (request: Request) => Promise<Response> {
  return (req) => {
    const c = propagation.extract(context.active(), Object.fromEntries(req.headers))
    return context.with(c, async () => {
      return await f(req);
    })
  }
}

export const GET = injectInboundContext(async (req: Request) => {
  const span = tracer.startSpan('your-operation-name');
  // The above ^ span will be automatically attached to incoming tracing context (if any)
  try {
    // Your operation logic here
    span.setAttributes({
      'custom.attribute': 'value',
    });
    return new Response('Hello, world!');
  } finally {
    span.end();
  }
});
```

###  [Sampling behavior](https://vercel.com/docs/multi-tenant#sampling-behavior)[](https://vercel.com/docs/multi-tenant#sampling-behavior)
When requests arrive with a `traceparent` header, Vercel's infrastructure considers the inbound sampling decision alongside its own sampling rules. Both must agree to sample for spans to be emitted.
For a span to be emitted, both the inbound decision (if present) and Vercel's sampling rules must agree to sample:
Inbound decision | Vercel sampled | Result
---|---|---
Sampled | Yes | Emitted
Sampled | No | Dropped
Not sampled | Any | Dropped
No decision | Yes | Emitted
No decision | No | Dropped
This ensures consistency in distributed systems: if an upstream service marks a trace as not sampled, Vercel respects that decision. When an upstream marks a trace as sampled, Vercel still applies its own sampling rules to control span volume.
