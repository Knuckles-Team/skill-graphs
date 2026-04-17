# How to set up instrumentation with OpenTelemetry
Last updated February 27, 2026
Observability is crucial for understanding and optimizing the behavior and performance of your Next.js app.
As applications become more complex, it becomes increasingly difficult to identify and diagnose issues that may arise. By leveraging observability tools, such as logging and metrics, developers can gain insights into their application's behavior and identify areas for optimization. With observability, developers can proactively address issues before they become major problems and provide a better user experience. Therefore, it is highly recommended to use observability in your Next.js applications to improve performance, optimize resources, and enhance user experience.
We recommend using OpenTelemetry for instrumenting your apps. It's a platform-agnostic way to instrument apps that allows you to change your observability provider without changing your code. Read
This documentation uses terms like _Span_ , _Trace_ or _Exporter_ throughout this doc, all of which can be found in
Next.js supports OpenTelemetry instrumentation out of the box, which means that we already instrumented Next.js itself.
