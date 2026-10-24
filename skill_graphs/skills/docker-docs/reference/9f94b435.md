#	  dIrEcTiVe=value
```

### [syntax](https://docs.docker.com/reference/dockerfile#syntax)
Use the `syntax` parser directive to declare the Dockerfile syntax version to use for the build. If unspecified, BuildKit uses a bundled version of the Dockerfile frontend. Declaring a syntax version lets you automatically use the latest Dockerfile version without having to upgrade BuildKit or Docker Engine, or even use a custom Dockerfile implementation.
Most users will want to set this parser directive to `docker/dockerfile:1`, which causes BuildKit to pull the latest stable version of the Dockerfile syntax before the build.
```
