## [Run your first sandbox](https://docs.docker.com/ai/sandboxes/get-started#run-your-first-sandbox)
Follow these steps to run a sandbox with Claude Code:
  1. (Optional but recommended) Set your Anthropic API key as an environment variable.
Add the API key to your shell configuration file:
~/.bashrc or ~/.zshrc
```
export ANTHROPIC_API_KEY=sk-ant-api03-xxxxx
```

Docker Sandboxes use a daemon process that runs independently of your current shell session. This means setting the environment variable inline or in your current session will not work. You must set it globally in your shell configuration file to ensure the daemon can access it.
Apply the changes:
    1. Source your shell configuration.
    2. Restart Docker Desktop so the daemon picks up the new environment variable.
Alternatively, you can skip this step and authenticate interactively when Claude Code starts. Interactive authentication is less secure and requires you to re-authenticate for each workspace. See [Credential security](https://docs.docker.com/ai/sandboxes/workflows/#credential-security) for details.
  2. Create and run a sandbox for Claude Code for your workspace:
```
$ docker sandbox run claude [PATH]

```

This creates a microVM sandbox. Docker assigns it a name automatically based on the agent and workspace directory (`claude-somedir`). If that name is already in use, Docker appends a number.
The workspace parameter is optional and defaults to your current directory if omitted:
```
$ cd ~/my-project
$ docker sandbox run claude

```

You can also mount multiple workspaces. Append `:ro` for read-only access:
```
$ docker sandbox run claude ~/my-project ~/docs:ro

```

  3. Claude Code starts and you can begin working. The first run takes longer while Docker initializes the microVM and pulls the template image.
