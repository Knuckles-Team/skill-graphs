# Quickstart

Configure your local development environment to get started developing with Temporal.

<SetupSteps>
  <SetupStep code={
    <>
      The .NET SDK requires .NET 6.0 or later.
      Install the latest version of .NET by following the official .NET instructions.
    </>
  }>
    ## Install .NET

    The .NET SDK requires .NET 6.0 or later.
    Install the latest version of .NET by following the [official .NET instructions](https://dotnet.microsoft.com/download).
  </SetupStep>

  <SetupStep code={
    <>
      <CodeSnippet language="bash">
{`# Create solution and projects
mkdir TemporalioHelloWorld
cd TemporalioHelloWorld

dotnet new sln -n TemporalioHelloWorld

dotnet new classlib -o Workflow
dotnet new console -o Worker
dotnet new console -o Client
