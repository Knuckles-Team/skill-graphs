# Amazon Bedrock Reasoning
Last updated March 8, 2026
Amazon Bedrock supports model creator-specific reasoning features for Anthropic models. Configuration depends on the model:
  * Claude 4.6 (e.g., `anthropic/claude-opus-4.6`): Use adaptive reasoning with `type: 'adaptive'` and `maxReasoningEffort`
  * Older models (e.g., `anthropic/claude-sonnet-4.5`): Use manual reasoning with `type: 'enabled'` and `budgetTokens` (minimum: 1,024, maximum: 64,000)
