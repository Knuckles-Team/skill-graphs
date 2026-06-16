# Quickstart

This guide walks you through setting up the Temporal Ruby SDK and running your first Workflow. In just a few steps,
you'll install the SDK and start a local development server. To validate that your local environment is correctly
installed, we will execute a Workflow that will output "Hello, Temporal".

<SetupSteps>
<SetupStep code={
  <>
    1. Check your Ruby version:
    <CodeSnippet language="bash">
    ruby -v
    </CodeSnippet>
    You should see output like <code>ruby 3.4.3</code>. Ruby 3.2+ is required. We recommend Ruby 3.4.3.

    2. Create your project folder:
    <CodeSnippet language="bash">
    mkdir temporal-project
    cd temporal-project
    </CodeSnippet>

    3. Initialize with Bundler:
    <CodeSnippet language="bash">
    bundle init
    </CodeSnippet>

    4. Add the Temporal Ruby SDK:
    <CodeSnippet language="bash">
    bundle add temporalio
    </CodeSnippet>

    You should see output like:
    <CodeSnippet language="bash">
    Fetching gem metadata from https://rubygems.org/...
    Resolving dependencies...
    Installing temporalio 0.4.0 (arm64-darwin)
    Bundle complete! 1 Gemfile dependency, 6 gems now installed.
    </CodeSnippet>

    5. Install dependencies:
    <CodeSnippet language="bash">
    bundle install
    </CodeSnippet>

</>
}>

## Installation

This step sets up a new Ruby project using Bundler and installs the Temporal Ruby SDK.

We recommend using [Bundler](https://bundler.io/) to manage your Ruby project dependencies, including the Temporal SDK.
These tutorials assume Ruby 3.4.3 or higher.

Follow the steps to create a directory, initialize the project with a `Gemfile`, and add the Temporal SDK.

**Note:**

- Only macOS ARM/x64 and Linux ARM/x64 are supported.
- Source gem is published but **cannot be built directly**.
- Windows (MinGW) is not supported.
- `fibers`/`async` are only supported on Ruby **3.3+**.
- See [Platform Support](#) for full details.

</SetupStep>

<SetupStep code={
<>
<Tabs>
<TabItem value="macos" label="macOS" default>

        Install the Temporal CLI using Homebrew:
        <CodeSnippet language="bash">
        brew install temporal
        </CodeSnippet>
      </TabItem>

      <TabItem value="windows" label="Windows">
        Download the Temporal CLI archive for your architecture:

          Windows amd64
          Windows arm64

        Extract it and add <code>temporal.exe</code> to your PATH.
      </TabItem>

      <TabItem value="linux" label="Linux">
        Download the Temporal CLI for your architecture:

          Linux amd64
          Linux arm64

        Extract the archive and move the <code>temporal</code> binary into your PATH, for example:
        <CodeSnippet language="bash">
        sudo mv temporal /usr/local/bin
        </CodeSnippet>
      </TabItem>
    </Tabs>

</>
}>

## Install Temporal CLI

The fastest way to get a development version of the Temporal Service running on your local machine is to use
[Temporal CLI](https://docs.temporal.io/cli).

Choose your operating system to install Temporal CLI.

</SetupStep>

<SetupStep code={
<>

After installing, open a new Terminal window and start the development server:

<CodeSnippet language="bash">temporal server start-dev</CodeSnippet>

Change the Web UI port
The Temporal Web UI may be on a different port in some examples or tutorials. To change the port for the Web UI, use the <code>--ui-port</code> option when starting the server:
<CodeSnippet language="bash">
temporal server start-dev --ui-port 8080
</CodeSnippet>
The Temporal Web UI will now be available at http://localhost:8080.

</>
}>

## Start the development server

Once you've installed Temporal CLI and added it to your PATH, open a new Terminal window and run the following command.

This command starts a local Temporal Service. It starts the Web UI, creates the default Namespace, and uses an in-memory
database.

The Temporal Service will be available on localhost:7233. The Temporal Web UI will be available at
http://localhost:8233.

Leave the local Temporal Service running as you work through tutorials and other projects. You can stop the Temporal
Service at any time by pressing CTRL+C.

Once you have everything installed, you're ready to build apps with Temporal on your local machine.

</SetupStep>
</SetupSteps>

## Run Hello World: Test Your Installation

Now let's verify your setup is working by creating and running a complete Temporal application with both a Workflow and
Activity.

This test will confirm that:

- The Temporal Ruby SDK is properly installed
- Your local Temporal Service is running
- You can successfully create and execute Workflows and Activities
- The communication between components is functioning correctly

### 1. Create the Activity

Create an Activity file (say_hello_activity.rb):

```ruby
require 'temporalio/activity'
