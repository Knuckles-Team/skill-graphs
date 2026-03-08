## Testing your instrumentation[](https://nextjs.org/docs/app/guides/open-telemetry#testing-your-instrumentation)
You need an OpenTelemetry collector with a compatible backend to test OpenTelemetry traces locally. We recommend using our
If everything works well you should be able to see the root server span labeled as `GET /requested/pathname`. All other spans from that particular trace will be nested under it.
Next.js traces more spans than are emitted by default. To see more spans, you must set `NEXT_OTEL_VERBOSE=1`.
