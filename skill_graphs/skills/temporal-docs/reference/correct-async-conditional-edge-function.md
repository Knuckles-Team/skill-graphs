# ✅ Correct: async conditional edge function
async def should_continue(state: AgentState) -> str:
    if state["messages"][-1].startswith("[Agent]") and "Calling" in state["messages"][-1]:
        return "tools"
    return END

g.add_conditional_edges("agent", should_continue)
```

:::

### Syntax

```python
