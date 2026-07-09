# Exec form:
[RUN](https://docs.docker.com/reference/dockerfile/#run "Learn more about the RUN instruction") [OPTIONS] [ "<command>", ... ]
```

For more information about the differences between these two forms, see [shell or exec forms](https://docs.docker.com/reference/dockerfile#shell-and-exec-form).
The shell form is most commonly used, and lets you break up longer instructions into multiple lines, either using newline [escapes](https://docs.docker.com/reference/dockerfile#escape), or with [heredocs](https://docs.docker.com/reference/dockerfile#here-documents):
```
[RUN](https://docs.docker.com/reference/dockerfile/#run "Learn more about the RUN instruction") <<EOF
apt-get update
apt-get install -y curl
EOF
```

The available `[OPTIONS]` for the `RUN` instruction are:
Option | Minimum Dockerfile version
---|---
[`--device`](https://docs.docker.com/reference/dockerfile#run---device) | 1.14-labs
[`--mount`](https://docs.docker.com/reference/dockerfile#run---mount) | 1.2
[`--network`](https://docs.docker.com/reference/dockerfile#run---network) | 1.3
[`--security`](https://docs.docker.com/reference/dockerfile#run---security) | 1.20
### [Cache invalidation for RUN instructions](https://docs.docker.com/reference/dockerfile#cache-invalidation-for-run-instructions)
The cache for `RUN` instructions isn't invalidated automatically during the next build. The cache for an instruction like `RUN apt-get dist-upgrade -y` will be reused during the next build. The cache for `RUN` instructions can be invalidated by using the `--no-cache` flag, for example `docker build --no-cache`.
See the [Dockerfile Best Practices guide](https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/) for more information.
The cache for `RUN` instructions can be invalidated by [`ADD`](https://docs.docker.com/reference/dockerfile#add) and [`COPY`](https://docs.docker.com/reference/dockerfile#copy) instructions.
### [RUN --device](https://docs.docker.com/reference/dockerfile#run---device)
> Note
> Not yet available in stable syntax, use [`docker/dockerfile:1-labs`](https://docs.docker.com/reference/dockerfile#syntax) version. It also needs BuildKit 0.20.0 or later.
```
[RUN](https://docs.docker.com/reference/dockerfile/#run "Learn more about the RUN instruction") --device=name,[required]
```

`RUN --device` allows build to request
> Warning
> The use of `--device` is protected by the `device` entitlement, which needs to be enabled when starting the buildkitd daemon with `--allow-insecure-entitlement device` flag or in [`--allow device` flag](https://docs.docker.com/engine/reference/commandline/buildx_build/#allow).
The device `name` is provided by the CDI specification registered in BuildKit.
In the following example, multiple devices are registered in the CDI specification for the `vendor1.com/device` vendor.
```
cdiVersion: "0.6.0"
kind: "vendor1.com/device"
devices:
  - name: foo
    containerEdits:
      env:
        - FOO=injected
  - name: bar
    annotations:
      org.mobyproject.buildkit.device.class: class1
    containerEdits:
      env:
        - BAR=injected
  - name: baz
    annotations:
      org.mobyproject.buildkit.device.class: class1
    containerEdits:
      env:
        - BAZ=injected
  - name: qux
    annotations:
      org.mobyproject.buildkit.device.class: class2
    containerEdits:
      env:
        - QUX=injected
annotations:
  org.mobyproject.buildkit.device.autoallow: true
```

The device name format is flexible and accepts various patterns to support multiple device configurations:
  * `vendor1.com/device`: request the first device found for this vendor
  * `vendor1.com/device=foo`: request a specific device
  * `vendor1.com/device=*`: request all devices for this vendor
  * `class1`: request devices by `org.mobyproject.buildkit.device.class` annotation


> Note
> Annotations are supported by the CDI specification since 0.6.0.
> Note
> To automatically allow all devices registered in the CDI specification, you can set the `org.mobyproject.buildkit.device.autoallow` annotation. You can also set this annotation for a specific device.
#### [Example: CUDA-Powered LLaMA Inference](https://docs.docker.com/reference/dockerfile#example-cuda-powered-llama-inference)
In this example we use the `--device` flag to run `llama.cpp` inference using an NVIDIA GPU device through CDI:
```
