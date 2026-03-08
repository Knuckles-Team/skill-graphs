## Deployment[](https://nextjs.org/docs/app/guides/open-telemetry#deployment)
### Using OpenTelemetry Collector[](https://nextjs.org/docs/app/guides/open-telemetry#using-opentelemetry-collector)
When you are deploying with OpenTelemetry Collector, you can use `@vercel/otel`. It will work both on Vercel and when self-hosted.
#### Deploying on Vercel[](https://nextjs.org/docs/app/guides/open-telemetry#deploying-on-vercel)
We made sure that OpenTelemetry works out of the box on Vercel.
Follow
#### Self-hosting[](https://nextjs.org/docs/app/guides/open-telemetry#self-hosting)
Deploying to other platforms is also straightforward. You will need to spin up your own OpenTelemetry Collector to receive and process the telemetry data from your Next.js app.
To do this, follow the
Once you have your collector up and running, you can deploy your Next.js app to your chosen platform following their respective deployment guides.
### Custom Exporters[](https://nextjs.org/docs/app/guides/open-telemetry#custom-exporters)
OpenTelemetry Collector is not necessary. You can use a custom OpenTelemetry exporter with [`@vercel/otel`](https://nextjs.org/docs/app/guides/open-telemetry#using-vercelotel) or [manual OpenTelemetry configuration](https://nextjs.org/docs/app/guides/open-telemetry#manual-opentelemetry-configuration).
