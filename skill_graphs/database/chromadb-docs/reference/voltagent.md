# VoltAgent
Source: https://docs.trychroma.com/integrations/frameworks/voltagent

[VoltAgent](https://github.com/VoltAgent/voltagent) is an open-source TypeScript framework for building AI agents with modular tools, LLM orchestration, and flexible multi-agent systems. It features a built-in, n8n-style observability console that lets you visually inspect agent behavior, trace actions, and debug with ease.

<Callout>
  You can find the complete example code at: [VoltAgent with Chroma Example](https://github.com/VoltAgent/voltagent/tree/main/examples/with-chroma)
</Callout>

## Installation

Create a new VoltAgent project with Chroma integration:

<CodeGroup>
  ```bash npm theme={null}
  npm create voltagent-app@latest -- --example with-chroma
  ```

  ```bash pnpm theme={null}
  pnpm create voltagent-app --example=with-chroma
  ```

  ```bash yarn theme={null}
  yarn create voltagent-app --example=with-chroma
  ```
</CodeGroup>

This creates a complete VoltAgent + Chroma setup with sample data and two different agent configurations.

Install the dependencies:

<CodeGroup>
  ```bash npm theme={null}
  npm install
  ```

  ```bash pnpm theme={null}
  pnpm install
  ```

  ```bash yarn theme={null}
  yarn install
  ```
</CodeGroup>

Next, you'll need to launch a Chroma server instance.

```bash theme={null}
npm run chroma run
```

The server will be available at `http://localhost:8000`.

**Note**: For production deployments, you might prefer [Chroma Cloud](https://www.trychroma.com/), a fully managed hosted service. See the Environment Setup section below for cloud configuration.

## Environment Setup

Create a `.env` file with your configuration:

### Option 1: Local Chroma Server

```env theme={null}
