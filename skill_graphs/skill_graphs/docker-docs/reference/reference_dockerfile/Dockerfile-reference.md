# Dockerfile reference
Copy as Markdown
Open Markdown Ask Docs AI Claude Open in Claude
Table of contents
  * [Overview](https://docs.docker.com/reference/dockerfile#overview)
  * [Format](https://docs.docker.com/reference/dockerfile#format)
  * [Parser directives](https://docs.docker.com/reference/dockerfile#parser-directives)
    * [syntax](https://docs.docker.com/reference/dockerfile#syntax)
    * [escape](https://docs.docker.com/reference/dockerfile#escape)
    * [check](https://docs.docker.com/reference/dockerfile#check)
  * [Environment replacement](https://docs.docker.com/reference/dockerfile#environment-replacement)
  * [.dockerignore file](https://docs.docker.com/reference/dockerfile#dockerignore-file)
  * [Shell and exec form](https://docs.docker.com/reference/dockerfile#shell-and-exec-form)
    * [Exec form](https://docs.docker.com/reference/dockerfile#exec-form)
    * [Shell form](https://docs.docker.com/reference/dockerfile#shell-form)
    * [Use a different shell](https://docs.docker.com/reference/dockerfile#use-a-different-shell)
  * [FROM](https://docs.docker.com/reference/dockerfile#from)
    * [Understand how ARG and FROM interact](https://docs.docker.com/reference/dockerfile#understand-how-arg-and-from-interact)
  * [RUN](https://docs.docker.com/reference/dockerfile#run)
    * [Cache invalidation for RUN instructions](https://docs.docker.com/reference/dockerfile#cache-invalidation-for-run-instructions)
    * [RUN --device](https://docs.docker.com/reference/dockerfile#run---device)
    * [RUN --mount](https://docs.docker.com/reference/dockerfile#run---mount)
    * [RUN --mount=type=bind](https://docs.docker.com/reference/dockerfile#run---mounttypebind)
    * [RUN --mount=type=cache](https://docs.docker.com/reference/dockerfile#run---mounttypecache)
    * [RUN --mount=type=tmpfs](https://docs.docker.com/reference/dockerfile#run---mounttypetmpfs)
    * [RUN --mount=type=secret](https://docs.docker.com/reference/dockerfile#run---mounttypesecret)
    * [RUN --mount=type=ssh](https://docs.docker.com/reference/dockerfile#run---mounttypessh)
    * [RUN --network](https://docs.docker.com/reference/dockerfile#run---network)
    * [RUN --network=default](https://docs.docker.com/reference/dockerfile#run---networkdefault)
    * [RUN --network=none](https://docs.docker.com/reference/dockerfile#run---networknone)
    * [RUN --network=host](https://docs.docker.com/reference/dockerfile#run---networkhost)
    * [RUN --security](https://docs.docker.com/reference/dockerfile#run---security)
  * [CMD](https://docs.docker.com/reference/dockerfile#cmd)
  * [LABEL](https://docs.docker.com/reference/dockerfile#label)
  * [MAINTAINER (deprecated)](https://docs.docker.com/reference/dockerfile#maintainer-deprecated)
  * [EXPOSE](https://docs.docker.com/reference/dockerfile#expose)
  * [ENV](https://docs.docker.com/reference/dockerfile#env)
  * [ADD](https://docs.docker.com/reference/dockerfile#add)
    * [Source](https://docs.docker.com/reference/dockerfile#source)
    * [Destination](https://docs.docker.com/reference/dockerfile#destination)
    * [ADD --keep-git-dir](https://docs.docker.com/reference/dockerfile#add---keep-git-dir)
    * [ADD --checksum](https://docs.docker.com/reference/dockerfile#add---checksum)
    * [ADD --chmod](https://docs.docker.com/reference/dockerfile#add---chmod)
    * [ADD --chown](https://docs.docker.com/reference/dockerfile#add---chown)
    * [ADD --link](https://docs.docker.com/reference/dockerfile#add---link)
    * [ADD --unpack](https://docs.docker.com/reference/dockerfile#add---unpack)
    * [ADD --exclude](https://docs.docker.com/reference/dockerfile#add---exclude)
  * [COPY](https://docs.docker.com/reference/dockerfile#copy)
    * [Source](https://docs.docker.com/reference/dockerfile#source-1)
    * [Destination](https://docs.docker.com/reference/dockerfile#destination-1)
    * [COPY --from](https://docs.docker.com/reference/dockerfile#copy---from)
    * [COPY --chmod](https://docs.docker.com/reference/dockerfile#copy---chmod)
    * [COPY --chown](https://docs.docker.com/reference/dockerfile#copy---chown)
    * [COPY --link](https://docs.docker.com/reference/dockerfile#copy---link)
    * [COPY --parents](https://docs.docker.com/reference/dockerfile#copy---parents)
    * [COPY --exclude](https://docs.docker.com/reference/dockerfile#copy---exclude)
  * [ENTRYPOINT](https://docs.docker.com/reference/dockerfile#entrypoint)
    * [Exec form ENTRYPOINT example](https://docs.docker.com/reference/dockerfile#exec-form-entrypoint-example)
    * [Shell form ENTRYPOINT example](https://docs.docker.com/reference/dockerfile#shell-form-entrypoint-example)
    * [Understand how CMD and ENTRYPOINT interact](https://docs.docker.com/reference/dockerfile#understand-how-cmd-and-entrypoint-interact)
  * [VOLUME](https://docs.docker.com/reference/dockerfile#volume)
    * [Notes about specifying volumes](https://docs.docker.com/reference/dockerfile#notes-about-specifying-volumes)
  * [USER](https://docs.docker.com/reference/dockerfile#user)
  * [WORKDIR](https://docs.docker.com/reference/dockerfile#workdir)
  * [ARG](https://docs.docker.com/reference/dockerfile#arg)
    * [Default values](https://docs.docker.com/reference/dockerfile#default-values)
    * [Scope](https://docs.docker.com/reference/dockerfile#scope)
    * [Using ARG variables](https://docs.docker.com/reference/dockerfile#using-arg-variables)
    * [Predefined ARGs](https://docs.docker.com/reference/dockerfile#predefined-args)
    * [Automatic platform ARGs in the global scope](https://docs.docker.com/reference/dockerfile#automatic-platform-args-in-the-global-scope)
    * [BuildKit built-in build args](https://docs.docker.com/reference/dockerfile#buildkit-built-in-build-args)
    * [Impact on build caching](https://docs.docker.com/reference/dockerfile#impact-on-build-caching)
  * [ONBUILD](https://docs.docker.com/reference/dockerfile#onbuild)
    * [Copy or mount from stage, image, or context](https://docs.docker.com/reference/dockerfile#copy-or-mount-from-stage-image-or-context)
    * [ONBUILD limitations](https://docs.docker.com/reference/dockerfile#onbuild-limitations)
  * [STOPSIGNAL](https://docs.docker.com/reference/dockerfile#stopsignal)
  * [HEALTHCHECK](https://docs.docker.com/reference/dockerfile#healthcheck)
  * [SHELL](https://docs.docker.com/reference/dockerfile#shell)
  * [Here-Documents](https://docs.docker.com/reference/dockerfile#here-documents)
    * [Example: Running a multi-line script](https://docs.docker.com/reference/dockerfile#example-running-a-multi-line-script)
    * [Example: Creating inline files](https://docs.docker.com/reference/dockerfile#example-creating-inline-files)
  * [Dockerfile examples](https://docs.docker.com/reference/dockerfile#dockerfile-examples)


* * *
Docker can build images automatically by reading the instructions from a Dockerfile. A Dockerfile is a text document that contains all the commands a user could call on the command line to assemble an image. This page describes the commands you can use in a Dockerfile.
## [Overview](https://docs.docker.com/reference/dockerfile#overview)
The Dockerfile supports the following instructions:
Instruction | Description
---|---
[`ADD`](https://docs.docker.com/reference/dockerfile#add) | Add local or remote files and directories.
[`ARG`](https://docs.docker.com/reference/dockerfile#arg) | Use build-time variables.
[`CMD`](https://docs.docker.com/reference/dockerfile#cmd) | Specify default commands.
[`COPY`](https://docs.docker.com/reference/dockerfile#copy) | Copy files and directories.
[`ENTRYPOINT`](https://docs.docker.com/reference/dockerfile#entrypoint) | Specify default executable.
[`ENV`](https://docs.docker.com/reference/dockerfile#env) | Set environment variables.
[`EXPOSE`](https://docs.docker.com/reference/dockerfile#expose) | Describe which ports your application is listening on.
[`FROM`](https://docs.docker.com/reference/dockerfile#from) | Create a new build stage from a base image.
[`HEALTHCHECK`](https://docs.docker.com/reference/dockerfile#healthcheck) | Check a container's health on startup.
[`LABEL`](https://docs.docker.com/reference/dockerfile#label) | Add metadata to an image.
[`MAINTAINER`](https://docs.docker.com/reference/dockerfile#maintainer-deprecated) | Specify the author of an image.
[`ONBUILD`](https://docs.docker.com/reference/dockerfile#onbuild) | Specify instructions for when the image is used in a build.
[`RUN`](https://docs.docker.com/reference/dockerfile#run) | Execute build commands.
[`SHELL`](https://docs.docker.com/reference/dockerfile#shell) | Set the default shell of an image.
[`STOPSIGNAL`](https://docs.docker.com/reference/dockerfile#stopsignal) | Specify the system call signal for exiting a container.
[`USER`](https://docs.docker.com/reference/dockerfile#user) | Set user and group ID.
[`VOLUME`](https://docs.docker.com/reference/dockerfile#volume) | Create volume mounts.
[`WORKDIR`](https://docs.docker.com/reference/dockerfile#workdir) | Change working directory.
## [Format](https://docs.docker.com/reference/dockerfile#format)
Here is the format of the Dockerfile:
```
# Comment
INSTRUCTION arguments
```

The instruction is not case-sensitive. However, convention is for them to be UPPERCASE to distinguish them from arguments more easily.
Docker runs instructions in a Dockerfile in order. A Dockerfile **must begin with a`FROM` instruction**. This may be after [parser directives](https://docs.docker.com/reference/dockerfile#parser-directives), [comments](https://docs.docker.com/reference/dockerfile#format), and globally scoped [ARGs](https://docs.docker.com/reference/dockerfile#arg). The `FROM` instruction specifies the [base image](https://docs.docker.com/glossary/#base-image) from which you are building. `FROM` may only be preceded by one or more `ARG` instructions, which declare arguments that are used in `FROM` lines in the Dockerfile.
BuildKit treats lines that begin with `#` as a comment, unless the line is a valid [parser directive](https://docs.docker.com/reference/dockerfile#parser-directives). A `#` marker anywhere else in a line is treated as an argument. This allows statements like:
```
# Comment
[RUN](https://docs.docker.com/reference/dockerfile/#run "Learn more about the RUN instruction") echo 'we are running some # of cool things'
```

Comment lines are removed before the Dockerfile instructions are executed. The comment in the following example is removed before the shell executes the `echo` command.
```
[RUN](https://docs.docker.com/reference/dockerfile/#run "Learn more about the RUN instruction") echo hello \
# comment
world
```

The following examples is equivalent.
```
[RUN](https://docs.docker.com/reference/dockerfile/#run "Learn more about the RUN instruction") echo hello \
world
```

Comments don't support line continuation characters.
> Note
> **Note on whitespace**
> For backward compatibility, leading whitespace before comments (`#`) and instructions (such as `RUN`) are ignored, but discouraged. Leading whitespace is not preserved in these cases, and the following examples are therefore equivalent:
> ```
        # this is a comment-line
    RUN echo hello
[RUN](https://docs.docker.com/reference/dockerfile/#run "Learn more about the RUN instruction") echo world
```

> ```
# this is a comment-line
[RUN](https://docs.docker.com/reference/dockerfile/#run "Learn more about the RUN instruction") echo hello
[RUN](https://docs.docker.com/reference/dockerfile/#run "Learn more about the RUN instruction") echo world
```

> Whitespace in instruction arguments, however, isn't ignored. The following example prints `hello world` with leading whitespace as specified:
> ```
[RUN](https://docs.docker.com/reference/dockerfile/#run "Learn more about the RUN instruction") echo "\
     hello\
     world"
```

## [Parser directives](https://docs.docker.com/reference/dockerfile#parser-directives)
Parser directives are optional, and affect the way in which subsequent lines in a Dockerfile are handled. Parser directives don't add layers to the build, and don't show up as build steps. Parser directives are written as a special type of comment in the form `# directive=value`. A single directive may only be used once.
The following parser directives are supported:
  * [`syntax`](https://docs.docker.com/reference/dockerfile#syntax)
  * [`escape`](https://docs.docker.com/reference/dockerfile#escape)
  * [`check`](https://docs.docker.com/reference/dockerfile#check) (since Dockerfile v1.8.0)


Once a comment, empty line or builder instruction has been processed, BuildKit no longer looks for parser directives. Instead it treats anything formatted as a parser directive as a comment and doesn't attempt to validate if it might be a parser directive. Therefore, all parser directives must be at the top of a Dockerfile.
Parser directive keys, such as `syntax` or `check`, aren't case-sensitive, but they're lowercase by convention. Values for a directive are case-sensitive and must be written in the appropriate case for the directive. For example, `#check=skip=jsonargsrecommended` is invalid because the check name must use Pascal case, not lowercase. It's also conventional to include a blank line following any parser directives. Line continuation characters aren't supported in parser directives.
Due to these rules, the following examples are all invalid:
Invalid due to line continuation:
```
