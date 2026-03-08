##  [Provider timeouts](https://vercel.com/docs/ai-gateway/sdks-and-apis/ai-sdk#provider-timeouts)[](https://vercel.com/docs/ai-gateway/sdks-and-apis/ai-sdk#provider-timeouts)
You can set per-provider timeouts for BYOK credentials to trigger fast failover when a provider is slow to respond. Pass `providerTimeouts` in `providerOptions.gateway`:
```
"providerOptions": {
  "gateway": {
    "providerTimeouts": {
      "byok": { "anthropic": 3000, "bedrock": 5000 }
    }
  }
}
```

For full details, limits, and response metadata, see [Provider Timeouts](https://vercel.com/docs/ai-gateway/models-and-providers/provider-timeouts).
