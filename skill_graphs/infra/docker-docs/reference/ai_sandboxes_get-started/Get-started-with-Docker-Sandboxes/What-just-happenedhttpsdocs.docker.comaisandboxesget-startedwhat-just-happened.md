## [What just happened?](https://docs.docker.com/ai/sandboxes/get-started#what-just-happened)
When you ran `docker sandbox run`:
  * Docker created a lightweight microVM with a private Docker daemon
  * The sandbox was assigned a name based on the workspace path
  * Your workspace synced into the VM
  * Docker started the Claude Code agent as a container inside the sandbox VM


The sandbox persists until you remove it. Installed packages and configuration remain available. Run `docker sandbox run <sandbox-name>` again to reconnect.
> Note
> Agents can modify files in your workspace. Review changes before executing code or performing actions that auto-run scripts. See [Security considerations](https://docs.docker.com/ai/sandboxes/workflows/#security-considerations) for details.
