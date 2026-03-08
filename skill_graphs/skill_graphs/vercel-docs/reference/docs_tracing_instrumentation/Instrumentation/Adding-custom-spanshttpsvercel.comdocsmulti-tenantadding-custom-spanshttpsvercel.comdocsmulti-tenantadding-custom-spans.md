##  [Adding custom spans](https://vercel.com/docs/multi-tenant#adding-custom-spans)[](https://vercel.com/docs/multi-tenant#adding-custom-spans)
After installing `@vercel/otel`, you can add custom spans to your traces to capture additional visibility into your application. Custom spans let you track specific operations that matter to your business logic, such as processing payments, generating reports, or transforming data, so you can measure their performance and debug issues more effectively.
Use the `@opentelemetry/api` package to instrument specific operations:
custom-span.ts
```
import { trace } from '@opentelemetry/api';

const tracer = trace.getTracer('custom-tracer');

async function performOperation() {
  const span = tracer.startSpan('operation-name');
  try {
    // Your operation logic here
    span.setAttributes({
      'custom.attribute': 'value',
    });
  } finally {
    span.end();
  }
}
```

Custom spans from functions using the [Edge runtime](https://vercel.com/docs/functions/runtimes/edge) are not supported.
