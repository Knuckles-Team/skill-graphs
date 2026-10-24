# Introduction
Source: https://docs.postiz.com/cli/introduction

Automate social media posting from the command line with the Postiz CLI

<Note>
  Create AI-powered UGC videos for your social media with [Agent Media](https://agent-media.ai) — generate engaging video content and schedule it directly with Postiz. Perfect for OpenClaw 🦞
</Note>

<Warning>
  For your AI agent to work best with Postiz, install the skill by running:

  ```bash theme={null}
  npx skills add gitroomhq/postiz-agent
  ```

  Or load the SKILL md file from [github.com/gitroomhq/postiz-agent](https://github.com/gitroomhq/postiz-agent).
</Warning>

The Postiz CLI is a command-line tool for automating social media posting across 28+ platforms. It wraps the [Public API](/public-api/introduction) so you can schedule posts, manage integrations, and upload media directly from your terminal or shell scripts.

## Installation

<Tabs>
  <Tab title="npm">
    ```bash theme={null}
    npm install -g postiz
    ```
  </Tab>

  <Tab title="pnpm">
    ```bash theme={null}
    pnpm install -g postiz
    ```
  </Tab>
</Tabs>

Verify the installation:

```bash theme={null}
postiz --help
```

## Authentication

### Option 1: OAuth2 (Recommended)

Authenticate using the device flow — no client ID or secret needed:

```bash theme={null}
postiz auth:login
```

This will:

1. Display a one-time code in your terminal
2. Open your browser to authorize
3. Automatically save credentials to `~/.postiz/credentials.json`

```bash theme={null}
