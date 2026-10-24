  console.log(`Path: ${metadata?.langgraph_path}`);
  console.log(`Checkpoint NS: ${metadata?.langgraph_checkpoint_ns}`);

  return state;
}
```

## Visualization

It's often nice to be able to visualize graphs, especially as they get more complex. LangGraph comes with several built-in ways to visualize graphs. See [Visualize your graph](/oss/javascript/langgraph/use-graph-api#visualize-your-graph) for more info.

## Observability and Tracing

To trace, debug and evaluate your agents, use [LangSmith](/langsmith/observability).

## Learn more

* [How to use the Graph API](/oss/javascript/langgraph/use-graph-api)
* [Functional API conceptual overview](/oss/javascript/langgraph/functional-api)
* [Choosing between Graph API and Functional API](/oss/javascript/langgraph/choosing-apis)

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/graph-api.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
