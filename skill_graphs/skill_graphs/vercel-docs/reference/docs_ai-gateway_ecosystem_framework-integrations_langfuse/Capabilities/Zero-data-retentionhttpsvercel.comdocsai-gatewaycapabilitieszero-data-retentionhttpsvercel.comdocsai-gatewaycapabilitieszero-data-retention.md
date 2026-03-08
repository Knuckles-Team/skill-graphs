##  [Zero data retention](https://vercel.com/docs/ai-gateway/capabilities#zero-data-retention)[](https://vercel.com/docs/ai-gateway/capabilities#zero-data-retention)
AI Gateway uses zero data retention by default—it permanently deletes your prompts and responses after requests complete. For applications with strict compliance requirements, you can also enforce ZDR at the provider level:
```
const result = await streamText({
  model: 'anthropic/claude-sonnet-4.6',
  prompt: 'Analyze this sensitive data...',
  providerOptions: {
    gateway: { zeroDataRetention: true },
  },
});
```

When `zeroDataRetention` is enabled, requests only route to providers with verified ZDR agreements. See the [ZDR documentation](https://vercel.com/docs/ai-gateway/capabilities/zdr) for the list of compliant providers.
