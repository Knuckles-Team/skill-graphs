## [Basic commands](https://docs.docker.com/ai/sandboxes/get-started#basic-commands)
Here are essential commands to manage your sandboxes:
### [List sandboxes](https://docs.docker.com/ai/sandboxes/get-started#list-sandboxes)
```
$ docker sandbox ls

```

Shows all your sandboxes with their IDs, names, status, workspace paths, and creation time. Workspace paths are shown for both running and stopped sandboxes.
> Note
> Sandboxes don't appear in `docker ps` because they're microVMs, not containers. Use `docker sandbox ls` to see them.
### [Access a running sandbox](https://docs.docker.com/ai/sandboxes/get-started#access-a-running-sandbox)
```
$ docker sandbox exec -it <sandbox-name> bash

```

Executes a command inside the container in the sandbox. Use `-it` to open an interactive shell for debugging or installing additional tools.
### [Remove a sandbox](https://docs.docker.com/ai/sandboxes/get-started#remove-a-sandbox)
```
$ docker sandbox rm <sandbox-name>

```

Deletes the sandbox VM and all installed packages inside it. You can remove multiple sandboxes at once by specifying multiple names:
```
$ docker sandbox rm <sandbox-1> <sandbox-2>

```

### [Recreate a sandbox](https://docs.docker.com/ai/sandboxes/get-started#recreate-a-sandbox)
To start fresh with a clean environment, remove and recreate the sandbox:
```
$ docker sandbox rm <sandbox-name>
$ docker sandbox run claude [PATH]

```

Configuration like custom templates and workspace paths are set when you create the sandbox. To change these settings, remove and recreate.
For a complete list of commands and options, see the [CLI reference](https://docs.docker.com/reference/cli/docker/sandbox/).
