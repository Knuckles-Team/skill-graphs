# Alternatively, run npm ci, which installs only dependencies specified in the lock file and is generally faster.
RUN npm install --only=production \
    && npm run build

CMD ["npm", "start"]
```

For smaller images and/or more secure deployments, it is also possible to use `-slim` Docker image variants (like
`node:20-bullseye-slim`) or `distroless/nodejs` Docker images (like `gcr.io/distroless/nodejs20-debian11`) with the
following caveats.

### Using `node:slim` images

`node:slim` images do not contain some of the common packages found in regular images. This results in significantly
smaller images.

However, TypeScript SDK requires the presence of root TLS certificates (the `ca-certificates` package), which are not
included in `slim` images. The `ca-certificates` package is required even when connecting to a local Temporal Server or
when using a server connection config that doesn't explicitly use TLS.

For this reason, the `ca-certificates` package must be installed during the construction of the Docker image. For
example:

```dockerfile
FROM node:20-bullseye-slim

RUN apt-get update \
    && apt-get install -y ca-certificates \
    && rm -rf /var/lib/apt/lists/*
