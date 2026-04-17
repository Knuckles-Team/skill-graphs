# syntax=docker/dockerfile:1
```

For more information about how the parser directive works, see [Custom Dockerfile syntax](https://docs.docker.com/build/buildkit/dockerfile-frontend/).
### [escape](https://docs.docker.com/reference/dockerfile#escape)
```
# syntax=docker/dockerfile:1
[FROM](https://docs.docker.com/reference/dockerfile/#from "Learn more about the FROM instruction") golang
[RUN](https://docs.docker.com/reference/dockerfile/#run "Learn more about the RUN instruction") --mount=type=cache,target=/root/.cache/go-build \
  go build ...
```

#### [Example: cache apt packages](https://docs.docker.com/reference/dockerfile#example-cache-apt-packages)
```
# syntax=docker/dockerfile:1
[FROM](https://docs.docker.com/reference/dockerfile/#from "Learn more about the FROM instruction") ubuntu
[RUN](https://docs.docker.com/reference/dockerfile/#run "Learn more about the RUN instruction") rm -f /etc/apt/apt.conf.d/docker-clean; echo 'Binary::apt::APT::Keep-Downloaded-Packages "true";' > /etc/apt/apt.conf.d/keep-cache
[RUN](https://docs.docker.com/reference/dockerfile/#run "Learn more about the RUN instruction") --mount=type=cache,target=/var/cache/apt,sharing=locked \
  --mount=type=cache,target=/var/lib/apt,sharing=locked \
  apt-get update && apt-get --no-install-recommends install -y gcc
```

Apt needs exclusive access to its data, so the caches use the option `sharing=locked`, which will make sure multiple parallel builds using the same cache mount will wait for each other and not access the same cache files at the same time. You could also use `sharing=private` if you prefer to have each build create another cache directory in this case.
### [RUN --mount=type=tmpfs](https://docs.docker.com/reference/dockerfile#run---mounttypetmpfs)
This mount type allows mounting `tmpfs` in the build container.
Option | Description
---|---
`target`, `dst`, `destination`[1](https://docs.docker.com/reference/dockerfile#fn:1) | Mount path.
`size` | Specify an upper limit on the size of the filesystem.
### [RUN --mount=type=secret](https://docs.docker.com/reference/dockerfile#run---mounttypesecret)
This mount type allows the build container to access secret values, such as tokens or private keys, without baking them into the image.
By default, the secret is mounted as a file. You can also mount the secret as an environment variable by setting the `env` option.
Option | Description
---|---
`id` | ID of the secret. Defaults to basename of the target path.
`target`, `dst`, `destination` | Mount the secret to the specified path. Defaults to `/run/secrets/` + `id` if unset and if `env` is also unset.
`env` | Mount the secret to an environment variable instead of a file, or both. (since Dockerfile v1.10.0)
`required` | If set to `true`, the instruction errors out when the secret is unavailable. Defaults to `false`.
`mode` | File mode for secret file in octal. Default `0400`.
`uid` | User ID for secret file. Default `0`.
`gid` | Group ID for secret file. Default `0`.
#### [Example: access to S3](https://docs.docker.com/reference/dockerfile#example-access-to-s3)
```
# syntax=docker/dockerfile:1
[FROM](https://docs.docker.com/reference/dockerfile/#from "Learn more about the FROM instruction") python:3
[RUN](https://docs.docker.com/reference/dockerfile/#run "Learn more about the RUN instruction") pip install awscli
[RUN](https://docs.docker.com/reference/dockerfile/#run "Learn more about the RUN instruction") --mount=type=secret,id=aws,target=/root/.aws/credentials \
  aws s3 cp s3://... ...
```

```
$ docker buildx build --secret id=aws,src=$HOME/.aws/credentials .

```

#### [Example: Mount as environment variable](https://docs.docker.com/reference/dockerfile#example-mount-as-environment-variable)
The following example takes the secret `API_KEY` and mounts it as an environment variable with the same name.
```
# syntax=docker/dockerfile:1
[FROM](https://docs.docker.com/reference/dockerfile/#from "Learn more about the FROM instruction") alpine
[RUN](https://docs.docker.com/reference/dockerfile/#run "Learn more about the RUN instruction") --mount=type=secret,id=API_KEY,env=API_KEY \
    some-command --token-from-env $API_KEY
```

Assuming that the `API_KEY` environment variable is set in the build environment, you can build this with the following command:
```
$ docker buildx build --secret id=API_KEY .

```

### [RUN --mount=type=ssh](https://docs.docker.com/reference/dockerfile#run---mounttypessh)
This mount type allows the build container to access SSH keys via SSH agents, with support for passphrases.
Option | Description
---|---
`id` | ID of SSH agent socket or key. Defaults to "default".
`target`, `dst`, `destination` | SSH agent socket path. Defaults to `/run/buildkit/ssh_agent.${N}`.
`required` | If set to `true`, the instruction errors out when the key is unavailable. Defaults to `false`.
`mode` | File mode for socket in octal. Default `0600`.
`uid` | User ID for socket. Default `0`.
`gid` | Group ID for socket. Default `0`.
#### [Example: access to GitLab](https://docs.docker.com/reference/dockerfile#example-access-to-gitlab)
```
# syntax=docker/dockerfile:1
[FROM](https://docs.docker.com/reference/dockerfile/#from "Learn more about the FROM instruction") alpine
[RUN](https://docs.docker.com/reference/dockerfile/#run "Learn more about the RUN instruction") apk add --no-cache openssh-client
[RUN](https://docs.docker.com/reference/dockerfile/#run "Learn more about the RUN instruction") mkdir -p -m 0700 ~/.ssh && ssh-keyscan gitlab.com >> ~/.ssh/known_hosts
[RUN](https://docs.docker.com/reference/dockerfile/#run "Learn more about the RUN instruction") --mount=type=ssh \
  ssh -q -T git@gitlab.com 2>&1 | tee /hello
# syntax=docker/dockerfile:1
[FROM](https://docs.docker.com/reference/dockerfile/#from "Learn more about the FROM instruction") python:3.6
[ADD](https://docs.docker.com/reference/dockerfile/#add "Learn more about the ADD instruction") mypackage.tgz wheels/
[RUN](https://docs.docker.com/reference/dockerfile/#run "Learn more about the RUN instruction") --network=none pip install --find-links wheels mypackage
```

`pip` will only be able to install the packages provided in the tarfile, which can be controlled by an earlier build stage.
### [RUN --network=host](https://docs.docker.com/reference/dockerfile#run---networkhost)
The command is run in the host's network environment (similar to `docker build --network=host`, but on a per-instruction basis)
> Warning
> The use of `--network=host` is protected by the `network.host` entitlement, which needs to be enabled when starting the buildkitd daemon with `--allow-insecure-entitlement network.host` flag or in [`--allow network.host` flag](https://docs.docker.com/engine/reference/commandline/buildx_build/#allow).
### [RUN --security](https://docs.docker.com/reference/dockerfile#run---security)
```
[RUN](https://docs.docker.com/reference/dockerfile/#run "Learn more about the RUN instruction") --security=<sandbox|insecure>
```

The default security mode is `sandbox`. With `--security=insecure`, the builder runs the command without sandbox in insecure mode, which allows to run flows requiring elevated privileges (e.g. containerd). This is equivalent to running `docker run --privileged`.
> Warning
> In order to access this feature, entitlement `security.insecure` should be enabled when starting the buildkitd daemon with `--allow-insecure-entitlement security.insecure` flag or in [`--allow security.insecure` flag](https://docs.docker.com/engine/reference/commandline/buildx_build/#allow).
Default sandbox mode can be activated via `--security=sandbox`, but that is no-op.
#### [Example: check entitlements](https://docs.docker.com/reference/dockerfile#example-check-entitlements)
```
# syntax=docker/dockerfile:1
[FROM](https://docs.docker.com/reference/dockerfile/#from "Learn more about the FROM instruction") ubuntu
[RUN](https://docs.docker.com/reference/dockerfile/#run "Learn more about the RUN instruction") --security=insecure cat /proc/self/status | grep CapEff
```

```
#84 0.093 CapEff:	0000003fffffffff
```

## [CMD](https://docs.docker.com/reference/dockerfile#cmd)
The `CMD` instruction sets the command to be executed when running a container from an image.
You can specify `CMD` instructions using [shell or exec forms](https://docs.docker.com/reference/dockerfile#shell-and-exec-form):
  * `CMD ["executable","param1","param2"]` (exec form)
  * `CMD ["param1","param2"]` (exec form, as default parameters to `ENTRYPOINT`)
  * `CMD command param1 param2` (shell form)


There can only be one `CMD` instruction in a Dockerfile. If you list more than one `CMD`, only the last one takes effect.
The purpose of a `CMD` is to provide defaults for an executing container. These defaults can include an executable, or they can omit the executable, in which case you must specify an `ENTRYPOINT` instruction as well.
If you would like your container to run the same executable every time, then you should consider using `ENTRYPOINT` in combination with `CMD`. See [`ENTRYPOINT`](https://docs.docker.com/reference/dockerfile#entrypoint). If the user specifies arguments to `docker run` then they will override the default specified in `CMD`, but still use the default `ENTRYPOINT`.
If `CMD` is used to provide default arguments for the `ENTRYPOINT` instruction, both the `CMD` and `ENTRYPOINT` instructions should be specified in the [exec form](https://docs.docker.com/reference/dockerfile#exec-form).
> Note
> Don't confuse `RUN` with `CMD`. `RUN` actually runs a command and commits the result; `CMD` doesn't execute anything at build time, but specifies the intended command for the image.
## [LABEL](https://docs.docker.com/reference/dockerfile#label)
```
[LABEL](https://docs.docker.com/reference/dockerfile/#label "Learn more about the LABEL instruction") <key>=<value> [<key>=<value>...]
```

The `LABEL` instruction adds metadata to an image. A `LABEL` is a key-value pair. To include spaces within a `LABEL` value, use quotes and backslashes as you would in command-line parsing. A few usage examples:
```
[LABEL](https://docs.docker.com/reference/dockerfile/#label "Learn more about the LABEL instruction") "com.example.vendor"="ACME Incorporated"
[LABEL](https://docs.docker.com/reference/dockerfile/#label "Learn more about the LABEL instruction") com.example.label-with-value="foo"
[LABEL](https://docs.docker.com/reference/dockerfile/#label "Learn more about the LABEL instruction") version="1.0"
[LABEL](https://docs.docker.com/reference/dockerfile/#label "Learn more about the LABEL instruction") description="This text illustrates \
that label-values can span multiple lines."
```

An image can have more than one label. You can specify multiple labels on a single line. Prior to Docker 1.10, this decreased the size of the final image, but this is no longer the case. You may still choose to specify multiple labels in a single instruction, in one of the following two ways:
```
[LABEL](https://docs.docker.com/reference/dockerfile/#label "Learn more about the LABEL instruction") multi.label1="value1" multi.label2="value2" other="value3"
```

```
[LABEL](https://docs.docker.com/reference/dockerfile/#label "Learn more about the LABEL instruction") multi.label1="value1" \
      multi.label2="value2" \
      other="value3"
```

> Note
> Be sure to use double quotes and not single quotes. Particularly when you are using string interpolation (e.g. `LABEL example="foo-$ENV_VAR"`), single quotes will take the string as is without unpacking the variable's value.
Labels included in base images (images in the `FROM` line) are inherited by your image. If a label already exists but with a different value, the most-recently-applied value overrides any previously-set value.
To view an image's labels, use the `docker image inspect` command. You can use the `--format` option to show just the labels;
```
$ docker image inspect --format='{{json .Config.Labels}}' myimage

```

```
{
  "com.example.vendor": "ACME Incorporated",
  "com.example.label-with-value": "foo",
  "version": "1.0",
  "description": "This text illustrates that label-values can span multiple lines.",
  "multi.label1": "value1",
  "multi.label2": "value2",
  "other": "value3"
}
```

## [MAINTAINER (deprecated)](https://docs.docker.com/reference/dockerfile#maintainer-deprecated)
```
MAINTAINER <name>
```

The `MAINTAINER` instruction sets the _Author_ field of the generated images. The `LABEL` instruction is a much more flexible version of this and you should use it instead, as it enables setting any metadata you require, and can be viewed easily, for example with `docker inspect`. To set a label corresponding to the `MAINTAINER` field you could use:
```
[LABEL](https://docs.docker.com/reference/dockerfile/#label "Learn more about the LABEL instruction") org.opencontainers.image.authors="SvenDowideit@home.org.au"
```

This will then be visible from `docker inspect` with the other labels.
## [EXPOSE](https://docs.docker.com/reference/dockerfile#expose)
```
[EXPOSE](https://docs.docker.com/reference/dockerfile/#expose "Learn more about the EXPOSE instruction") <port> [<port>/<protocol>...]
```

The `EXPOSE` instruction informs Docker that the container listens on the specified network ports at runtime. You can specify whether the port listens on TCP or UDP, and the default is TCP if you don't specify a protocol.
The `EXPOSE` instruction doesn't actually publish the port. It functions as a type of documentation between the person who builds the image and the person who runs the container, about which ports are intended to be published. To publish the port when running the container, use the `-p` flag on `docker run` to publish and map one or more ports, or the `-P` flag to publish all exposed ports and map them to high-order ports.
By default, `EXPOSE` assumes TCP. You can also specify UDP:
```
[EXPOSE](https://docs.docker.com/reference/dockerfile/#expose "Learn more about the EXPOSE instruction") 80/udp
```

To expose on both TCP and UDP, include two lines:
```
[EXPOSE](https://docs.docker.com/reference/dockerfile/#expose "Learn more about the EXPOSE instruction") 80/tcp
[EXPOSE](https://docs.docker.com/reference/dockerfile/#expose "Learn more about the EXPOSE instruction") 80/udp
```

In this case, if you use `-P` with `docker run`, the port will be exposed once for TCP and once for UDP. Remember that `-P` uses an ephemeral high-ordered host port on the host, so TCP and UDP doesn't use the same port.
Regardless of the `EXPOSE` settings, you can override them at runtime by using the `-p` flag. For example
```
$ docker run -p 80:80/tcp -p 80:80/udp ...

```

To set up port redirection on the host system, see [using the -P flag](https://docs.docker.com/reference/cli/docker/container/run/#publish). The `docker network` command supports creating networks for communication among containers without the need to expose or publish specific ports, because the containers connected to the network can communicate with each other over any port. For detailed information, see the [overview of this feature](https://docs.docker.com/engine/userguide/networking/).
## [ENV](https://docs.docker.com/reference/dockerfile#env)
```
[ENV](https://docs.docker.com/reference/dockerfile/#env "Learn more about the ENV instruction") <key>=<value> [<key>=<value>...]
```

The `ENV` instruction sets the environment variable `<key>` to the value `<value>`. This value will be in the environment for all subsequent instructions in the build stage and can be [replaced inline](https://docs.docker.com/reference/dockerfile#environment-replacement) in many as well. The value will be interpreted for other environment variables, so quote characters will be removed if they are not escaped. Like command line parsing, quotes and backslashes can be used to include spaces within values.
Example:
```
[ENV](https://docs.docker.com/reference/dockerfile/#env "Learn more about the ENV instruction") MY_NAME="John Doe"
[ENV](https://docs.docker.com/reference/dockerfile/#env "Learn more about the ENV instruction") MY_DOG=Rex\ The\ Dog
[ENV](https://docs.docker.com/reference/dockerfile/#env "Learn more about the ENV instruction") MY_CAT=fluffy
```

The `ENV` instruction allows for multiple `<key>=<value> ...` variables to be set at one time, and the example below will yield the same net results in the final image:
```
[ENV](https://docs.docker.com/reference/dockerfile/#env "Learn more about the ENV instruction") MY_NAME="John Doe" MY_DOG=Rex\ The\ Dog \
    MY_CAT=fluffy
```

The environment variables set using `ENV` will persist when a container is run from the resulting image. You can view the values using `docker inspect`, and change them using `docker run --env <key>=<value>`.
A stage inherits any environment variables that were set using `ENV` by its parent stage or any ancestor. Refer to the [multi-stage builds section](https://docs.docker.com/build/building/multi-stage/) in the manual for more information.
Environment variable persistence can cause unexpected side effects. For example, setting `ENV DEBIAN_FRONTEND=noninteractive` changes the behavior of `apt-get`, and may confuse users of your image.
If an environment variable is only needed during build, and not in the final image, consider setting a value for a single command instead:
```
[RUN](https://docs.docker.com/reference/dockerfile/#run "Learn more about the RUN instruction") DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y ...
```

Or using [`ARG`](https://docs.docker.com/reference/dockerfile#arg), which is not persisted in the final image:
```
[ARG](https://docs.docker.com/reference/dockerfile/#arg "Learn more about the ARG instruction") DEBIAN_FRONTEND=noninteractive
[RUN](https://docs.docker.com/reference/dockerfile/#run "Learn more about the RUN instruction") apt-get update && apt-get install -y ...
```

> Note
> **Alternative syntax**
> The `ENV` instruction also allows an alternative syntax `ENV <key> <value>`, omitting the `=`. For example:
> ```
[ENV](https://docs.docker.com/reference/dockerfile/#env "Learn more about the ENV instruction") MY_VAR my-value
```

> This syntax does not allow for multiple environment-variables to be set in a single `ENV` instruction, and can be confusing. For example, the following sets a single environment variable (`ONE`) with value `"TWO= THREE=world"`:
> ```
[ENV](https://docs.docker.com/reference/dockerfile/#env "Learn more about the ENV instruction") ONE TWO= THREE=world
```

> The alternative syntax is supported for backward compatibility, but discouraged for the reasons outlined above, and may be removed in a future release.
## [ADD](https://docs.docker.com/reference/dockerfile#add)
ADD has two forms. The latter form is required for paths containing whitespace.
```
[ADD](https://docs.docker.com/reference/dockerfile/#add "Learn more about the ADD instruction") [OPTIONS] <src> ... <dest>
[ADD](https://docs.docker.com/reference/dockerfile/#add "Learn more about the ADD instruction") [OPTIONS] ["<src>", ... "<dest>"]
```

The available `[OPTIONS]` are:
Option | Minimum Dockerfile version
---|---
[`--keep-git-dir`](https://docs.docker.com/reference/dockerfile#add---keep-git-dir) | 1.1
[`--checksum`](https://docs.docker.com/reference/dockerfile#add---checksum) | 1.6
[`--chmod`](https://docs.docker.com/reference/dockerfile#add---chmod) | 1.2
[`--chown`](https://docs.docker.com/reference/dockerfile#add---chown) |
[`--link`](https://docs.docker.com/reference/dockerfile#add---link) | 1.4
[`--unpack`](https://docs.docker.com/reference/dockerfile#add---unpack) | 1.17
[`--exclude`](https://docs.docker.com/reference/dockerfile#add---exclude) | 1.19
The `ADD` instruction copies new files or directories from `<src>` and adds them to the filesystem of the image at the path `<dest>`. Files and directories can be copied from the build context, a remote URL, or a Git repository.
The `ADD` and `COPY` instructions are functionally similar, but serve slightly different purposes. Learn more about the [differences between `ADD` and `COPY`](https://docs.docker.com/build/building/best-practices/#add-or-copy).
### [Source](https://docs.docker.com/reference/dockerfile#source)
You can specify multiple source files or directories with `ADD`. The last argument must always be the destination. For example, to add two files, `file1.txt` and `file2.txt`, from the build context to `/usr/src/things/` in the build container:
```
[ADD](https://docs.docker.com/reference/dockerfile/#add "Learn more about the ADD instruction") file1.txt file2.txt /usr/src/things/
```

If you specify multiple source files, either directly or using a wildcard, then the destination must be a directory (must end with a slash `/`).
To add files from a remote location, you can specify a URL or the address of a Git repository as the source. For example:
```
[ADD](https://docs.docker.com/reference/dockerfile/#add "Learn more about the ADD instruction") https://example.com/archive.zip /usr/src/things/
[ADD](https://docs.docker.com/reference/dockerfile/#add "Learn more about the ADD instruction") git@github.com:user/repo.git /usr/src/things/
```

BuildKit detects the type of `<src>` and processes it accordingly.
  * If `<src>` is a local file or directory, the contents of the directory are copied to the specified destination. See [Adding files from the build context](https://docs.docker.com/reference/dockerfile#adding-files-from-the-build-context).
  * If `<src>` is a local tar archive, it is decompressed and extracted to the specified destination. See [Adding local tar archives](https://docs.docker.com/reference/dockerfile#adding-local-tar-archives).
  * If `<src>` is a URL, the contents of the URL are downloaded and placed at the specified destination. See [Adding files from a URL](https://docs.docker.com/reference/dockerfile#adding-files-from-a-url).
  * If `<src>` is a Git repository, the repository is cloned to the specified destination. See [Adding files from a Git repository](https://docs.docker.com/reference/dockerfile#adding-files-from-a-git-repository).


#### [Adding files from the build context](https://docs.docker.com/reference/dockerfile#adding-files-from-the-build-context)
Any relative or local path that doesn't begin with a `http://`, `https://`, or `git@` protocol prefix is considered a local file path. The local file path is relative to the build context. For example, if the build context is the current directory, `ADD file.txt /` adds the file at `./file.txt` to the root of the filesystem in the build container.
Specifying a source path with a leading slash or one that navigates outside the build context, such as `ADD ../something /something`, automatically removes any parent directory navigation (`../`). Trailing slashes in the source path are also disregarded, making `ADD something/ /something` equivalent to `ADD something /something`.
If the source is a directory, the contents of the directory are copied, including filesystem metadata. The directory itself isn't copied, only its contents. If it contains subdirectories, these are also copied, and merged with any existing directories at the destination. Any conflicts are resolved in favor of the content being added, on a file-by-file basis, except if you're trying to copy a directory onto an existing file, in which case an error is raised.
If the source is a file, the file and its metadata are copied to the destination. File permissions are preserved. If the source is a file and a directory with the same name exists at the destination, an error is raised.
If you pass a Dockerfile through stdin to the build (`docker build - < Dockerfile`), there is no build context. In this case, you can only use the `ADD` instruction to copy remote files. You can also pass a tar archive through stdin: (`docker build - < archive.tar`), the Dockerfile at the root of the archive and the rest of the archive will be used as the context of the build.
##### [Pattern matching](https://docs.docker.com/reference/dockerfile#pattern-matching)
For local files, each `<src>` may contain wildcards and matching will be done using Go's
For example, to add all files and directories in the root of the build context ending with `.png`:
```
[ADD](https://docs.docker.com/reference/dockerfile/#add "Learn more about the ADD instruction") *.png /dest/
```

In the following example, `?` is a single-character wildcard, matching e.g. `index.js` and `index.ts`.
```
[ADD](https://docs.docker.com/reference/dockerfile/#add "Learn more about the ADD instruction") index.?s /dest/
```

When adding files or directories that contain special characters (such as `[` and `]`), you need to escape those paths following the Golang rules to prevent them from being treated as a matching pattern. For example, to add a file named `arr[0].txt`, use the following;
```
[ADD](https://docs.docker.com/reference/dockerfile/#add "Learn more about the ADD instruction") arr[[]0].txt /dest/
```

#### [Adding local tar archives](https://docs.docker.com/reference/dockerfile#adding-local-tar-archives)
When using a local tar archive as the source for `ADD`, and the archive is in a recognized compression format (`gzip`, `bzip2` or `xz`, or uncompressed), the archive is decompressed and extracted into the specified destination. Local tar archives are extracted by default, see the [`ADD --unpack` flag].
When a directory is extracted, it has the same behavior as `tar -x`. The result is the union of:
  1. Whatever existed at the destination path, and
  2. The contents of the source tree, with conflicts resolved in favor of the content being added, on a file-by-file basis.


> Note
> Whether a file is identified as a recognized compression format or not is done solely based on the contents of the file, not the name of the file. For example, if an empty file happens to end with `.tar.gz` this isn't recognized as a compressed file and doesn't generate any kind of decompression error message, rather the file will simply be copied to the destination.
#### [Adding files from a URL](https://docs.docker.com/reference/dockerfile#adding-files-from-a-url)
In the case where source is a remote file URL, the destination will have permissions of 600. If the HTTP response contains a `Last-Modified` header, the timestamp from that header will be used to set the `mtime` on the destination file. However, like any other file processed during an `ADD`, `mtime` isn't included in the determination of whether or not the file has changed and the cache should be updated.
If remote file is a tar archive, the archive is not extracted by default. To download and extract the archive, use the [`ADD --unpack` flag].
If the destination ends with a trailing slash, then the filename is inferred from the URL path. For example, `ADD http://example.com/foobar /` would create the file `/foobar`. The URL must have a nontrivial path so that an appropriate filename can be discovered (`http://example.com` doesn't work).
If the destination doesn't end with a trailing slash, the destination path becomes the filename of the file downloaded from the URL. For example, `ADD http://example.com/foo /bar` creates the file `/bar`.
If your URL files are protected using authentication, you need to use `RUN wget`, `RUN curl` or use another tool from within the container as the `ADD` instruction doesn't support authentication.
#### [Adding files from a Git repository](https://docs.docker.com/reference/dockerfile#adding-files-from-a-git-repository)
To use a Git repository as the source for `ADD`, you can reference the repository's HTTP or SSH address as the source. The repository is cloned to the specified destination in the image.
```
[ADD](https://docs.docker.com/reference/dockerfile/#add "Learn more about the ADD instruction") https://github.com/user/repo.git /mydir/
```

You can use URL fragments to specify a specific branch, tag, commit, or subdirectory. For example, to add the `docs` directory of the `v0.14.1` tag of the `buildkit` repository:
```
[ADD](https://docs.docker.com/reference/dockerfile/#add "Learn more about the ADD instruction") git@github.com:moby/buildkit.git#v0.14.1:docs /buildkit-docs
```

For more information about Git URL fragments, see [URL fragments](https://docs.docker.com/build/building/context/#url-fragments).
When adding from a Git repository, the permissions bits for files are 644. If a file in the repository has the executable bit set, it will have permissions set to 755. Directories have permissions set to 755.
When using a Git repository as the source, the repository must be accessible from the build context. To add a repository via SSH, whether public or private, you must pass an SSH key for authentication. For example, given the following Dockerfile:
```
# syntax=docker/dockerfile:1
[FROM](https://docs.docker.com/reference/dockerfile/#from "Learn more about the FROM instruction") alpine
[ADD](https://docs.docker.com/reference/dockerfile/#add "Learn more about the ADD instruction") git@git.example.com:foo/bar.git /bar
```

To build this Dockerfile, pass the `--ssh` flag to the `docker build` to mount the SSH agent socket to the build. For example:
```
$ docker build --ssh default .

```

For more information about building with secrets, see [Build secrets](https://docs.docker.com/build/building/secrets/).
### [Destination](https://docs.docker.com/reference/dockerfile#destination)
If the destination path begins with a forward slash, it's interpreted as an absolute path, and the source files are copied into the specified destination relative to the root of the current build stage.
```
# syntax=docker/dockerfile:1
[FROM](https://docs.docker.com/reference/dockerfile/#from "Learn more about the FROM instruction") alpine
[ADD](https://docs.docker.com/reference/dockerfile/#add "Learn more about the ADD instruction") --keep-git-dir=true https://github.com/moby/buildkit.git#v0.10.1 /buildkit
```

### [ADD --checksum](https://docs.docker.com/reference/dockerfile#add---checksum)
```
[ADD](https://docs.docker.com/reference/dockerfile/#add "Learn more about the ADD instruction") [--checksum=<hash>] <src> ... <dir>
```

The `--checksum` flag lets you verify the checksum of a remote Git or HTTP resource:
  * For Git sources, the checksum is the commit SHA. It can be the full commit SHA or match on the prefix (1 or more characters).
  * For HTTP sources, the checksum is the SHA-256 content digest, formatted as `sha256:<hash>`. SHA-256 is the only supported hash algorithm.


```
[ADD](https://docs.docker.com/reference/dockerfile/#add "Learn more about the ADD instruction") --checksum=be1f38e https://github.com/moby/buildkit.git#v0.26.2 /
[ADD](https://docs.docker.com/reference/dockerfile/#add "Learn more about the ADD instruction") --checksum=sha256:24454f830cdb571e2c4ad15481119c43b3cafd48dd869a9b2945d1036d1dc68d https://mirrors.edge.kernel.org/pub/linux/kernel/Historic/linux-0.01.tar.gz /
```

### [ADD --chmod](https://docs.docker.com/reference/dockerfile#add---chmod)
See [`COPY --chmod`](https://docs.docker.com/reference/dockerfile#copy---chmod).
### [ADD --chown](https://docs.docker.com/reference/dockerfile#add---chown)
See [`COPY --chown`](https://docs.docker.com/reference/dockerfile#copy---chown).
### [ADD --link](https://docs.docker.com/reference/dockerfile#add---link)
See [`COPY --link`](https://docs.docker.com/reference/dockerfile#copy---link).
### [ADD --unpack](https://docs.docker.com/reference/dockerfile#add---unpack)
```
[ADD](https://docs.docker.com/reference/dockerfile/#add "Learn more about the ADD instruction") [--unpack=<bool>] <src> ... <dir>
```

The `--unpack` flag controls whether or not to automatically unpack tar archives (including compressed formats like `gzip` or `bzip2`) when adding them to the image. Local tar archives are unpacked by default, whereas remote tar archives (where `src` is a URL) are downloaded without unpacking.
```
# syntax=docker/dockerfile:1
[FROM](https://docs.docker.com/reference/dockerfile/#from "Learn more about the FROM instruction") alpine
# syntax=docker/dockerfile:1
[FROM](https://docs.docker.com/reference/dockerfile/#from "Learn more about the FROM instruction") alpine AS build
[COPY](https://docs.docker.com/reference/dockerfile/#copy "Learn more about the COPY instruction") . .
[RUN](https://docs.docker.com/reference/dockerfile/#run "Learn more about the RUN instruction") apk add clang
[RUN](https://docs.docker.com/reference/dockerfile/#run "Learn more about the RUN instruction") clang -o /hello hello.c

[FROM](https://docs.docker.com/reference/dockerfile/#from "Learn more about the FROM instruction") scratch
[COPY](https://docs.docker.com/reference/dockerfile/#copy "Learn more about the COPY instruction") --from=build /hello /
```

You can also copy files directly from named contexts (specified with `--build-context <name>=<source>`) or images. The following example copies an `nginx.conf` file from the official Nginx image.
```
[COPY](https://docs.docker.com/reference/dockerfile/#copy "Learn more about the COPY instruction") --from=nginx:latest /etc/nginx/nginx.conf /nginx.conf
```

The source path of `COPY --from` is always resolved from filesystem root of the image or stage that you specify.
### [COPY --chmod](https://docs.docker.com/reference/dockerfile#copy---chmod)
```
[COPY](https://docs.docker.com/reference/dockerfile/#copy "Learn more about the COPY instruction") [--chmod=<perms>] <src> ... <dest>
```

The `--chmod` flag supports octal notation (e.g., `755`, `644`) and symbolic notation (e.g., `+x`, `g=u`). Symbolic notation (added in Dockerfile version 1.14) is useful when octal isn't flexible enough. For example, `u=rwX,go=rX` sets directories to 755 and files to 644, while preserving the executable bit on files that already have it. (Capital `X` means "executable only if it's a directory or already executable.")
For more information about symbolic notation syntax, see the
Examples using octal notation:
```
[COPY](https://docs.docker.com/reference/dockerfile/#copy "Learn more about the COPY instruction") --chmod=755 app.sh /app/
[COPY](https://docs.docker.com/reference/dockerfile/#copy "Learn more about the COPY instruction") --chmod=644 file.txt /data/
[ARG](https://docs.docker.com/reference/dockerfile/#arg "Learn more about the ARG instruction") MODE=440
[COPY](https://docs.docker.com/reference/dockerfile/#copy "Learn more about the COPY instruction") --chmod=$MODE . .
```

Examples using symbolic notation:
```
[COPY](https://docs.docker.com/reference/dockerfile/#copy "Learn more about the COPY instruction") --chmod=+x script.sh /app/
[COPY](https://docs.docker.com/reference/dockerfile/#copy "Learn more about the COPY instruction") --chmod=u=rwX,go=rX . /app/
[COPY](https://docs.docker.com/reference/dockerfile/#copy "Learn more about the COPY instruction") --chmod=g=u config/ /config/
```

The `--chmod` flag is not supported when building Windows containers.
### [COPY --chown](https://docs.docker.com/reference/dockerfile#copy---chown)
```
[COPY](https://docs.docker.com/reference/dockerfile/#copy "Learn more about the COPY instruction") [--chown=<user>:<group>] <src> ... <dest>
```

Sets ownership of copied files. Without this flag, files are created with UID and GID of 0.
The flag accepts usernames, group names, UIDs, or GIDs in any combination. If you specify only a user, the GID is set to the same numeric value as the UID.
```
[COPY](https://docs.docker.com/reference/dockerfile/#copy "Learn more about the COPY instruction") --chown=55:mygroup files* /somedir/
[COPY](https://docs.docker.com/reference/dockerfile/#copy "Learn more about the COPY instruction") --chown=bin files* /somedir/
[COPY](https://docs.docker.com/reference/dockerfile/#copy "Learn more about the COPY instruction") --chown=1 files* /somedir/
[COPY](https://docs.docker.com/reference/dockerfile/#copy "Learn more about the COPY instruction") --chown=10:11 files* /somedir/
[COPY](https://docs.docker.com/reference/dockerfile/#copy "Learn more about the COPY instruction") --chown=myuser:mygroup --chmod=644 files* /somedir/
```

When using names instead of numeric IDs, BuildKit resolves them using `/etc/passwd` and `/etc/group` in the container's root filesystem. If these files are missing or don't contain the specified names, the build fails. Numeric IDs don't require this lookup.
The `--chown` flag is not supported when building Windows containers.
### [COPY --link](https://docs.docker.com/reference/dockerfile#copy---link)
```
[COPY](https://docs.docker.com/reference/dockerfile/#copy "Learn more about the COPY instruction") [--link[=<boolean>]] <src> ... <dest>
```

Enabling this flag in `COPY` or `ADD` commands allows you to copy files with enhanced semantics where your files remain independent on their own layer and don't get invalidated when commands on previous layers are changed.
When `--link` is used your source files are copied into an empty destination directory. That directory is turned into a layer that is linked on top of your previous state.
```
# syntax=docker/dockerfile:1
[FROM](https://docs.docker.com/reference/dockerfile/#from "Learn more about the FROM instruction") alpine
[COPY](https://docs.docker.com/reference/dockerfile/#copy "Learn more about the COPY instruction") --link /foo /bar
```

Is equivalent of doing two builds:
```
[FROM](https://docs.docker.com/reference/dockerfile/#from "Learn more about the FROM instruction") alpine
```

and
```
[FROM](https://docs.docker.com/reference/dockerfile/#from "Learn more about the FROM instruction") scratch
[COPY](https://docs.docker.com/reference/dockerfile/#copy "Learn more about the COPY instruction") /foo /bar
```

and merging all the layers of both images together.
#### [Benefits of using `--link`](https://docs.docker.com/reference/dockerfile#benefits-of-using---link)
Use `--link` to reuse already built layers in subsequent builds with `--cache-from` even if the previous layers have changed. This is especially important for multi-stage builds where a `COPY --from` statement would previously get invalidated if any previous commands in the same stage changed, causing the need to rebuild the intermediate stages again. With `--link` the layer the previous build generated is reused and merged on top of the new layers. This also means you can easily rebase your images when the base images receive updates, without having to execute the whole build again. In backends that support it, BuildKit can do this rebase action without the need to push or pull any layers between the client and the registry. BuildKit will detect this case and only create new image manifest that contains the new layers and old layers in correct order.
The same behavior where BuildKit can avoid pulling down the base image can also happen when using `--link` and no other commands that would require access to the files in the base image. In that case BuildKit will only build the layers for the `COPY` commands and push them to the registry directly on top of the layers of the base image.
#### [Incompatibilities with `--link=false`](https://docs.docker.com/reference/dockerfile#incompatibilities-with---linkfalse)
When using `--link` the `COPY/ADD` commands are not allowed to read any files from the previous state. This means that if in previous state the destination directory was a path that contained a symlink, `COPY/ADD` can not follow it. In the final image the destination path created with `--link` will always be a path containing only directories.
If you don't rely on the behavior of following symlinks in the destination path, using `--link` is always recommended. The performance of `--link` is equivalent or better than the default behavior and, it creates much better conditions for cache reuse.
### [COPY --parents](https://docs.docker.com/reference/dockerfile#copy---parents)
```
[COPY](https://docs.docker.com/reference/dockerfile/#copy "Learn more about the COPY instruction") [--parents[=<boolean>]] <src> ... <dest>
```

The `--parents` flag preserves parent directories for `src` entries. This flag defaults to `false`.
```
# syntax=docker/dockerfile:1
[FROM](https://docs.docker.com/reference/dockerfile/#from "Learn more about the FROM instruction") scratch

[COPY](https://docs.docker.com/reference/dockerfile/#copy "Learn more about the COPY instruction") ./x/a.txt ./y/a.txt /no_parents/
[COPY](https://docs.docker.com/reference/dockerfile/#copy "Learn more about the COPY instruction") --parents ./x/a.txt ./y/a.txt /parents/

# syntax=docker/dockerfile:1
[FROM](https://docs.docker.com/reference/dockerfile/#from "Learn more about the FROM instruction") scratch

[COPY](https://docs.docker.com/reference/dockerfile/#copy "Learn more about the COPY instruction") --parents ./x/./y/*.txt /parents/
