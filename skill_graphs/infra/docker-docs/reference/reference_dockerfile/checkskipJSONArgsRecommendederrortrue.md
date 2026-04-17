# check=skip=JSONArgsRecommended;error=true
```

To see all available checks, see the [build checks reference](https://docs.docker.com/reference/build-checks/). Note that the checks available depend on the Dockerfile syntax version. To make sure you're getting the most up-to-date checks, use the [`syntax`](https://docs.docker.com/reference/dockerfile#syntax) directive to specify the Dockerfile syntax version to the latest stable version.
## [Environment replacement](https://docs.docker.com/reference/dockerfile#environment-replacement)
Environment variables (declared with [the `ENV` statement](https://docs.docker.com/reference/dockerfile#env)) can also be used in certain instructions as variables to be interpreted by the Dockerfile. Escapes are also handled for including variable-like syntax into a statement literally.
Environment variables are notated in the Dockerfile either with `$variable_name` or `${variable_name}`. They are treated equivalently and the brace syntax is typically used to address issues with variable names with no whitespace, like `${foo}_bar`.
The `${variable_name}` syntax also supports a few of the standard `bash` modifiers as specified below:
  * `${variable:-word}` indicates that if `variable` is set then the result will be that value. If `variable` is not set then `word` will be the result.
  * `${variable:+word}` indicates that if `variable` is set then `word` will be the result, otherwise the result is the empty string.


The following variable replacements are supported in a pre-release version of Dockerfile syntax, when using the `# syntax=docker/dockerfile-upstream:master` syntax directive in your Dockerfile:
  * `${variable#pattern}` removes the shortest match of `pattern` from `variable`, seeking from the start of the string.
```
str=foobarbaz echo ${str#f*b}     # arbaz
```

  * `${variable##pattern}` removes the longest match of `pattern` from `variable`, seeking from the start of the string.
```
str=foobarbaz echo ${str##f*b}    # az
```

  * `${variable%pattern}` removes the shortest match of `pattern` from `variable`, seeking backwards from the end of the string.
```
string=foobarbaz echo ${string%b*}    # foobar
```

  * `${variable%%pattern}` removes the longest match of `pattern` from `variable`, seeking backwards from the end of the string.
```
string=foobarbaz echo ${string%%b*}   # foo
```

  * `${variable/pattern/replacement}` replace the first occurrence of `pattern` in `variable` with `replacement`
```
string=foobarbaz echo ${string/ba/fo}  # fooforbaz
```

  * `${variable//pattern/replacement}` replaces all occurrences of `pattern` in `variable` with `replacement`
```
string=foobarbaz echo ${string//ba/fo}  # fooforfoz
```



In all cases, `word` can be any string, including additional environment variables.
`pattern` is a glob pattern where `?` matches any single character and `*` any number of characters (including zero). To match literal `?` and `*`, use a backslash escape: `\?` and `\*`.
You can escape whole variable names by adding a `\` before the variable: `\$foo` or `\${foo}`, for example, will translate to `$foo` and `${foo}` literals respectively.
Example (parsed representation is displayed after the `#`):
```
[FROM](https://docs.docker.com/reference/dockerfile/#from "Learn more about the FROM instruction") busybox
[ENV](https://docs.docker.com/reference/dockerfile/#env "Learn more about the ENV instruction") FOO=/bar
[WORKDIR](https://docs.docker.com/reference/dockerfile/#workdir "Learn more about the WORKDIR instruction") ${FOO}   # WORKDIR /bar
[ADD](https://docs.docker.com/reference/dockerfile/#add "Learn more about the ADD instruction") . $FOO       # ADD . /bar
[COPY](https://docs.docker.com/reference/dockerfile/#copy "Learn more about the COPY instruction") \$FOO /quux # COPY $FOO /quux
```

Environment variables are supported by the following list of instructions in the Dockerfile:
  * `ADD`
  * `COPY`
  * `ENV`
  * `EXPOSE`
  * `FROM`
  * `LABEL`
  * `STOPSIGNAL`
  * `USER`
  * `VOLUME`
  * `WORKDIR`
  * `ONBUILD` (when combined with one of the supported instructions above)


You can also use environment variables with `RUN`, `CMD`, and `ENTRYPOINT` instructions, but in those cases the variable substitution is handled by the command shell, not the builder. Note that instructions using the exec form don't invoke a command shell automatically. See [Variable substitution](https://docs.docker.com/reference/dockerfile#variable-substitution).
Environment variable substitution use the same value for each variable throughout the entire instruction. Changing the value of a variable only takes effect in subsequent instructions. Consider the following example:
```
[ENV](https://docs.docker.com/reference/dockerfile/#env "Learn more about the ENV instruction") abc=hello
[ENV](https://docs.docker.com/reference/dockerfile/#env "Learn more about the ENV instruction") abc=bye def=$abc
[ENV](https://docs.docker.com/reference/dockerfile/#env "Learn more about the ENV instruction") ghi=$abc
```

  * The value of `def` becomes `hello`
  * The value of `ghi` becomes `bye`


## [.dockerignore file](https://docs.docker.com/reference/dockerfile#dockerignore-file)
You can use `.dockerignore` file to exclude files and directories from the build context. For more information, see [.dockerignore file](https://docs.docker.com/build/building/context/#dockerignore-files).
## [Shell and exec form](https://docs.docker.com/reference/dockerfile#shell-and-exec-form)
The `RUN`, `CMD`, and `ENTRYPOINT` instructions all have two possible forms:
  * `INSTRUCTION ["executable","param1","param2"]` (exec form)
  * `INSTRUCTION command param1 param2` (shell form)


The exec form makes it possible to avoid shell string munging, and to invoke commands using a specific command shell, or any other executable. It uses a JSON array syntax, where each element in the array is a command, flag, or argument.
The shell form is more relaxed, and emphasizes ease of use, flexibility, and readability. The shell form automatically uses a command shell, whereas the exec form does not.
### [Exec form](https://docs.docker.com/reference/dockerfile#exec-form)
The exec form is parsed as a JSON array, which means that you must use double-quotes (") around words, not single-quotes (').
```
[ENTRYPOINT](https://docs.docker.com/reference/dockerfile/#entrypoint "Learn more about the ENTRYPOINT instruction") ["/bin/bash", "-c", "echo hello"]
```

The exec form is best used to specify an `ENTRYPOINT` instruction, combined with `CMD` for setting default arguments that can be overridden at runtime. For more information, see [ENTRYPOINT](https://docs.docker.com/reference/dockerfile#entrypoint).
#### [Variable substitution](https://docs.docker.com/reference/dockerfile#variable-substitution)
Using the exec form doesn't automatically invoke a command shell. This means that normal shell processing, such as variable substitution, doesn't happen. For example, `RUN [ "echo", "$HOME" ]` won't handle variable substitution for `$HOME`.
If you want shell processing then either use the shell form or execute a shell directly with the exec form, for example: `RUN [ "sh", "-c", "echo $HOME" ]`. When using the exec form and executing a shell directly, as in the case for the shell form, it's the shell that's doing the environment variable substitution, not the builder.
#### [Backslashes](https://docs.docker.com/reference/dockerfile#backslashes)
In exec form, you must escape backslashes. This is particularly relevant on Windows where the backslash is the path separator. The following line would otherwise be treated as shell form due to not being valid JSON, and fail in an unexpected way:
```
[RUN](https://docs.docker.com/reference/dockerfile/#run "Learn more about the RUN instruction") ["c:\windows\system32\tasklist.exe"]
```

The correct syntax for this example is:
```
[RUN](https://docs.docker.com/reference/dockerfile/#run "Learn more about the RUN instruction") ["c:\\windows\\system32\\tasklist.exe"]
```

### [Shell form](https://docs.docker.com/reference/dockerfile#shell-form)
Unlike the exec form, instructions using the shell form always use a command shell. The shell form doesn't use the JSON array format, instead it's a regular string. The shell form string lets you escape newlines using the [escape character](https://docs.docker.com/reference/dockerfile#escape) (backslash by default) to continue a single instruction onto the next line. This makes it easier to use with longer commands, because it lets you split them up into multiple lines. For example, consider these two lines:
```
[RUN](https://docs.docker.com/reference/dockerfile/#run "Learn more about the RUN instruction") source $HOME/.bashrc && \
echo $HOME
```

They're equivalent to the following line:
```
[RUN](https://docs.docker.com/reference/dockerfile/#run "Learn more about the RUN instruction") source $HOME/.bashrc && echo $HOME
```

You can also use heredocs with the shell form to break up supported commands.
```
[RUN](https://docs.docker.com/reference/dockerfile/#run "Learn more about the RUN instruction") <<EOF
  source $HOME/.bashrc
  echo $HOME
EOF
```

For more information about heredocs, see [Here-documents](https://docs.docker.com/reference/dockerfile#here-documents).
### [Use a different shell](https://docs.docker.com/reference/dockerfile#use-a-different-shell)
You can change the default shell using the `SHELL` command. For example:
```
[SHELL](https://docs.docker.com/reference/dockerfile/#shell "Learn more about the SHELL instruction") ["/bin/bash", "-c"]
[RUN](https://docs.docker.com/reference/dockerfile/#run "Learn more about the RUN instruction") echo hello
```

For more information, see [SHELL](https://docs.docker.com/reference/dockerfile#shell).
## [FROM](https://docs.docker.com/reference/dockerfile#from)
```
[FROM](https://docs.docker.com/reference/dockerfile/#from "Learn more about the FROM instruction") [--platform=<platform>] <image> [AS <name>]
```

Or
```
[FROM](https://docs.docker.com/reference/dockerfile/#from "Learn more about the FROM instruction") [--platform=<platform>] <image>[:<tag>] [AS <name>]
```

Or
```
[FROM](https://docs.docker.com/reference/dockerfile/#from "Learn more about the FROM instruction") [--platform=<platform>] <image>[@<digest>] [AS <name>]
```

The `FROM` instruction initializes a new build stage and sets the [base image](https://docs.docker.com/glossary/#base-image) for subsequent instructions. As such, a valid Dockerfile must start with a `FROM` instruction. The image can be any valid image.
  * `ARG` is the only instruction that may precede `FROM` in the Dockerfile. See [Understand how ARG and FROM interact](https://docs.docker.com/reference/dockerfile#understand-how-arg-and-from-interact).
  * `FROM` can appear multiple times within a single Dockerfile to create multiple images or use one build stage as a dependency for another. Simply make a note of the last image ID output by the commit before each new `FROM` instruction. Each `FROM` instruction clears any state created by previous instructions.
  * Optionally a name can be given to a new build stage by adding `AS name` to the `FROM` instruction. The name can be used in subsequent `FROM <name>`, [`COPY --from=<name>`](https://docs.docker.com/reference/dockerfile#copy---from), and [`RUN --mount=type=bind,from=<name>`](https://docs.docker.com/reference/dockerfile#run---mounttypebind) instructions to refer to the image built in this stage.
  * The `tag` or `digest` values are optional. If you omit either of them, the builder assumes a `latest` tag by default. The builder returns an error if it can't find the `tag` value.


The optional `--platform` flag can be used to specify the platform of the image in case `FROM` references a multi-platform image. For example, `linux/amd64`, `linux/arm64`, or `windows/amd64`. By default, the target platform of the build request is used. Global build arguments can be used in the value of this flag, for example [automatic platform ARGs](https://docs.docker.com/reference/dockerfile#automatic-platform-args-in-the-global-scope) allow you to force a stage to native build platform (`--platform=$BUILDPLATFORM`), and use it to cross-compile to the target platform inside the stage.
### [Understand how ARG and FROM interact](https://docs.docker.com/reference/dockerfile#understand-how-arg-and-from-interact)
`FROM` instructions support variables that are declared by any `ARG` instructions that occur before the first `FROM`.
```
[ARG](https://docs.docker.com/reference/dockerfile/#arg "Learn more about the ARG instruction")  CODE_VERSION=latest
[FROM](https://docs.docker.com/reference/dockerfile/#from "Learn more about the FROM instruction") base:${CODE_VERSION}
[CMD](https://docs.docker.com/reference/dockerfile/#cmd "Learn more about the CMD instruction")  /code/run-app

[FROM](https://docs.docker.com/reference/dockerfile/#from "Learn more about the FROM instruction") extras:${CODE_VERSION}
[CMD](https://docs.docker.com/reference/dockerfile/#cmd "Learn more about the CMD instruction")  /code/run-extras
```

An `ARG` declared before a `FROM` is outside of a build stage, so it can't be used in any instruction after a `FROM`. To use the default value of an `ARG` declared before the first `FROM` use an `ARG` instruction without a value inside of a build stage:
```
[ARG](https://docs.docker.com/reference/dockerfile/#arg "Learn more about the ARG instruction") VERSION=latest
[FROM](https://docs.docker.com/reference/dockerfile/#from "Learn more about the FROM instruction") busybox:$VERSION
[ARG](https://docs.docker.com/reference/dockerfile/#arg "Learn more about the ARG instruction") VERSION
[RUN](https://docs.docker.com/reference/dockerfile/#run "Learn more about the RUN instruction") echo $VERSION > image_version
```

## [RUN](https://docs.docker.com/reference/dockerfile#run)
The `RUN` instruction will execute any commands to create a new layer on top of the current image. The added layer is used in the next step in the Dockerfile. `RUN` has two forms:
```
