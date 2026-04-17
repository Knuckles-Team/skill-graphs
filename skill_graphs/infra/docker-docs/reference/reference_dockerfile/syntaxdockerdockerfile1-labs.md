# syntax=docker/dockerfile:1-labs

[FROM](https://docs.docker.com/reference/dockerfile/#from "Learn more about the FROM instruction") scratch AS model
[ADD](https://docs.docker.com/reference/dockerfile/#add "Learn more about the ADD instruction") https://huggingface.co/bartowski/Llama-3.2-1B-Instruct-GGUF/resolve/main/Llama-3.2-1B-Instruct-Q4_K_M.gguf /model.gguf

[FROM](https://docs.docker.com/reference/dockerfile/#from "Learn more about the FROM instruction") scratch AS prompt
[COPY](https://docs.docker.com/reference/dockerfile/#copy "Learn more about the COPY instruction") <<EOF prompt.txt
Q: Generate  a list of 10 unique biggest countries by population in JSON with their estimated poulation in 1900 and 2024. Answer only newline formatted JSON with keys "country", "population_1900", "population_2024" with 10 items.
A:
[
    {

EOF

[FROM](https://docs.docker.com/reference/dockerfile/#from "Learn more about the FROM instruction") ghcr.io/ggml-org/llama.cpp:full-cuda-b5124
[RUN](https://docs.docker.com/reference/dockerfile/#run "Learn more about the RUN instruction") --device=nvidia.com/gpu=all \
    --mount=from=model,target=/models \
    --mount=from=prompt,target=/tmp \
    ./llama-cli -m /models/model.gguf -no-cnv -ngl 99 -f /tmp/prompt.txt
```

### [RUN --mount](https://docs.docker.com/reference/dockerfile#run---mount)
```
[RUN](https://docs.docker.com/reference/dockerfile/#run "Learn more about the RUN instruction") --mount=[type=TYPE][,option=<value>[,option=<value>]...]
```

`RUN --mount` allows you to create filesystem mounts that the build can access. This can be used to:
  * Create bind mount to the host filesystem or other build stages
  * Access build secrets or ssh-agent sockets
  * Use a persistent package management cache to speed up your build


The supported mount types are:
Type | Description
---|---
[`bind`](https://docs.docker.com/reference/dockerfile#run---mounttypebind) (default) | Bind-mount context directories (read-only).
[`cache`](https://docs.docker.com/reference/dockerfile#run---mounttypecache) | Mount a temporary directory to cache directories for compilers and package managers.
[`tmpfs`](https://docs.docker.com/reference/dockerfile#run---mounttypetmpfs) | Mount a `tmpfs` in the build container.
[`secret`](https://docs.docker.com/reference/dockerfile#run---mounttypesecret) | Allow the build container to access secure files such as private keys without baking them into the image or build cache.
[`ssh`](https://docs.docker.com/reference/dockerfile#run---mounttypessh) | Allow the build container to access SSH keys via SSH agents, with support for passphrases.
### [RUN --mount=type=bind](https://docs.docker.com/reference/dockerfile#run---mounttypebind)
This mount type allows binding files or directories to the build container. A bind mount is read-only by default.
Option | Description
---|---
`target`, `dst`, `destination`[1](https://docs.docker.com/reference/dockerfile#fn:1) | Mount path.
`source` | Source path in the `from`. Defaults to the root of the `from`.
`from` | Build stage, context, or image name for the root of the source. Defaults to the build context.
`rw`,`readwrite` | Allow writes on the mount. Written data will be discarded.
### [RUN --mount=type=cache](https://docs.docker.com/reference/dockerfile#run---mounttypecache)
This mount type allows the build container to cache directories for compilers and package managers.
Option | Description
---|---
`id` | Optional ID to identify separate/different caches. Defaults to value of `target`.
`target`, `dst`, `destination`[1](https://docs.docker.com/reference/dockerfile#fn:1) | Mount path.
`ro`,`readonly` | Read-only if set.
`sharing` | One of `shared`, `private`, or `locked`. Defaults to `shared`. A `shared` cache mount can be used concurrently by multiple writers. `private` creates a new mount if there are multiple writers. `locked` pauses the second writer until the first one releases the mount.
`from` | Build stage, context, or image name to use as a base of the cache mount. Defaults to empty directory.
`source` | Subpath in the `from` to mount. Defaults to the root of the `from`.
`mode` | File mode for new cache directory in octal. Default `0755`.
`uid` | User ID for new cache directory. Default `0`.
`gid` | Group ID for new cache directory. Default `0`.
Contents of the cache directories persists between builder invocations without invalidating the instruction cache. Cache mounts should only be used for better performance. Your build should work with any contents of the cache directory as another build may overwrite the files or GC may clean it if more storage space is needed.
#### [Example: cache Go packages](https://docs.docker.com/reference/dockerfile#example-cache-go-packages)
```
