
---

## Temporal CLI

The Temporal CLI (`temporal`) provides direct access to a Temporal Service via the terminal. Use it to manage, monitor,
and debug Temporal applications, plus run an embedded development service when you need fast local feedback.

In addition, we provide and maintain an official extension for the Temporal CLI you can use to interact with Temporal
Cloud. Use the extension to manage your Temporal Cloud control plane resources, including Namespaces, Users, Service
Accounts, API keys, and perform other operational and administrative tasks.

## Install and configure the CLI

Install the CLI and cloud extension, run a local development server, and configure your environment in
[Install and configure the CLI](/cli/setup-cli).

## Use with Temporal Cloud

Connect to Temporal Cloud with [environment configuration](/develop/environment-configuration) and use the Cloud
extension to manage your Temporal Cloud control plane resources in [Use with Temporal Cloud](/cli/cloud).

## Start a development server

The CLI includes a local Temporal development service for fast feedback while building or testing your application.

```bash
temporal server start-dev
```

## CLI basics

Get started with the basics of the CLI in [CLI basics](/cli/common-operations).

## Command reference

Refer to the [command reference](/cli/command-reference) for the complete list of commands.

---

## Install and configure the CLI

The Temporal CLI is a command-line tool for interacting with the Temporal Service. It helps you manage, monitor, and
debug Temporal applications.

## Install the CLI

The CLI is available for macOS, Linux, and Windows, or as a Docker image.

<Tabs>

<TabItem value="macosinstall" label="macOS">

Install with Homebrew:

```bash
brew install temporal
```

Or download from the CDN:

- [Darwin amd64](https://temporal.download/cli/archive/latest?platform=darwin&arch=amd64)
- [Darwin arm64](https://temporal.download/cli/archive/latest?platform=darwin&arch=arm64)

extract the archive and add the `temporal` binary to your `PATH`.

</TabItem>

<TabItem value="linuxinstall" label="Linux">

Install with Homebrew (if available):

```bash
brew install temporal
```

Or install with Snap:

```bash
snap install temporal
```

Or download from the CDN:

- [Linux amd64](https://temporal.download/cli/archive/latest?platform=linux&arch=amd64)
- [Linux arm64](https://temporal.download/cli/archive/latest?platform=linux&arch=arm64)

extract the archive and add the `temporal` binary to your `PATH`.

</TabItem>

<TabItem value="windowsinstall" label="Windows">

Download from the CDN:

- [Windows amd64](https://temporal.download/cli/archive/latest?platform=windows&arch=amd64)
- [Windows arm64](https://temporal.download/cli/archive/latest?platform=windows&arch=arm64)

extract the archive and add the `temporal.exe` binary to your `PATH`.

</TabItem>

<TabItem value="dockerinstall" label="Docker">

Temporal CLI container image is available on [DockerHub](https://hub.docker.com/r/temporalio/temporal) and can be run
directly:

```shell
docker run --rm temporalio/temporal --help
```

::::note

When running the Temporal CLI inside Docker, for the development server to be accessible from the host system, the
server needs to be configured to listen on external IP and the ports need to be forwarded:

```shell
docker run --rm -p 7233:7233 -p 8233:8233 temporalio/temporal server start-dev --ip 0.0.0.0
