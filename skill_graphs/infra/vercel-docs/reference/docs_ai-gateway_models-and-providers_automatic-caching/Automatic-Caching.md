# Automatic Caching
Last updated March 8, 2026
Some providers like Anthropic and MiniMax require explicit cache control markers to enable prompt caching, while others like OpenAI, Google, and DeepSeek cache automatically (sometimes called "implicit caching"). Use `caching: 'auto'` to let AI Gateway handle this for you. It applies the appropriate caching strategy based on the provider.
