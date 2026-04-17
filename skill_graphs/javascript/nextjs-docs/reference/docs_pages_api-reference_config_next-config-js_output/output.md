# output
Last updated February 27, 2026
During a build, Next.js will automatically trace each page and its dependencies to determine all of the files that are needed for deploying a production version of your application.
This feature helps reduce the size of deployments drastically. Previously, when deploying with Docker you would need to have all files from your package's `dependencies` installed to run `next start`. Starting with Next.js 12, you can leverage Output File Tracing in the `.next/` directory to only include the necessary files.
Furthermore, this removes the need for the deprecated `serverless` target which can cause various issues and also creates unnecessary duplication.
