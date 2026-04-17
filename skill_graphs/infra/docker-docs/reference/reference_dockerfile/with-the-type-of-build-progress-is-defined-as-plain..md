# with the type of build progress is defined as `plain`.
```

```
$ eval $(ssh-agent)
$ ssh-add ~/.ssh/id_rsa
(Input your passphrase here)
$ docker buildx build --ssh default=$SSH_AUTH_SOCK .

```

You can also specify a path to `*.pem` file on the host directly instead of `$SSH_AUTH_SOCK`. However, pem files with passphrases are not supported.
### [RUN --network](https://docs.docker.com/reference/dockerfile#run---network)
```
[RUN](https://docs.docker.com/reference/dockerfile/#run "Learn more about the RUN instruction") --network=TYPE
```

`RUN --network` allows control over which networking environment the command is run in.
The supported network types are:
Type | Description
---|---
[`default`](https://docs.docker.com/reference/dockerfile#run---networkdefault) (default) | Run in the default network.
[`none`](https://docs.docker.com/reference/dockerfile#run---networknone) | Run with no network access.
[`host`](https://docs.docker.com/reference/dockerfile#run---networkhost) | Run in the host's network environment.
### [RUN --network=default](https://docs.docker.com/reference/dockerfile#run---networkdefault)
Equivalent to not supplying a flag at all, the command is run in the default network for the build.
### [RUN --network=none](https://docs.docker.com/reference/dockerfile#run---networknone)
The command is run with no network access (`lo` is still available, but is isolated to this process)
#### [Example: isolating external effects](https://docs.docker.com/reference/dockerfile#example-isolating-external-effects)
```
