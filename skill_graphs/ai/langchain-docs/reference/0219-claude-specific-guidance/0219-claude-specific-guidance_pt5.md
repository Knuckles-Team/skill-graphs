              ],
          },
          config={"configurable": {"thread_id": "12345"}},
      )
      ```
    </CodeGroup>
  </Tab>
</Tabs>

## Profiles

A [harness profile](/oss/python/deepagents/profiles#harness-profiles) is a reusable bundle of per-model configuration that `create_deep_agent` applies automatically when the matching model is selected. Profiles are the right tool when you want behaviour that follows the model—not the call site—such as a system prompt suffix tuned for Claude's instruction style, tool descriptions rewritten for GPT, or extra middleware that only makes sense with a specific provider.

A single profile can carry: a custom base system prompt (`base_system_prompt`), an appended suffix (`system_prompt_suffix`), tool description overrides, tools or middleware to exclude, additional middleware to inject, and edits to the auto-added general-purpose subagent.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from deepagents import HarnessProfile, register_harness_profile
