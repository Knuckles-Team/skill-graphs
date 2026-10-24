# Simple limit: allow up to 10 concurrent runs
agent = Agent('gateway/openai:gpt-5', max_concurrency=10)
