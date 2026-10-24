# Add documents to collection
collection.add(
    documents=[case["case"] + "\n" + case["resolution"] for case in support_cases],
    metadatas=[{
        "category": case["category"],
        "date": case["date"]
    } for case in support_cases],
    ids=[f"case_{i}" for i in range(len(support_cases))]
)
```

Now team members can use Claude to access this knowledge.

In your claude config, add the following:

```json theme={null}
{
  "mcpServers": {
    "chroma": {
      "command": "uvx",
      "args": [
        "chroma-mcp",
        "--client-type",
        "cloud",
        "--tenant",
        "your-tenant-id",
        "--database",
        "support-kb",
        "--api-key",
        "YOUR_API_KEY"
      ]
    }
  }
}
```

Now you can use the knowledge base in your chats:

```
Claude, I'm having trouble helping a customer with IoT device connectivity.
Can you check our support knowledge base for similar cases and suggest a solution?
```

Claude will:

1. Search the shared knowledge base for relevant cases
2. Consider the context and solutions from similar past issues
3. Provide recommendations based on previous successful resolutions

This setup is particularly powerful because:

* All support team members have access to the same knowledge base
* Claude can learn from the entire team's experience
* Solutions are standardized across the organization
* New team members can quickly get up to speed on common issues

### Project Memory Example

Claude's context window has limits - long conversations eventually get truncated, and chats don't persist between sessions. Using Chroma as an external memory store solves these limitations, allowing Claude to reference past conversations and maintain context across multiple sessions.

First, tell Claude to use Chroma for memory as part of the project setup:

```
Remember, you have access to Chroma tools.
At any point if the user references previous chats or memory, check chroma for similar conversations.
Try to use retrieved information where possible.
```

<img alt="mcp-instructions" />

This prompt instructs Claude to:

* Proactively check Chroma when memory-related topics come up
* Search for semantically similar past conversations
* Incorporate relevant historical context into responses

To store the current conversation:

```
Please chunk our conversation into small chunks and store it in Chroma for future reference.
```

Claude will:

1. Break the conversation into smaller chunks (typically 512-1024 tokens)
   * Chunking is necessary because:
   * Large texts are harder to search semantically
   * Smaller chunks help retrieve more precise context
   * It prevents token limits in future retrievals
2. Generate embeddings for each chunk
3. Add metadata like timestamps and detected topics
4. Store everything in your Chroma collection

<img alt="mcp-store" />

Later, you can access past conversations naturally:

```
What did we discuss previously about the authentication system?
```

Claude will:

1. Search Chroma for chunks semantically related to authentication
2. Filter by timestamp metadata for last week's discussions
3. Incorporate the relevant historical context into its response

<img alt="mcp-search" />

This setup is particularly useful for:

* Long-running projects where context gets lost
* Teams where multiple people interact with Claude
* Complex discussions that reference past decisions
* Maintaining consistent context across multiple chat sessions

### Advanced Features

The Chroma MCP server supports:

* **Collection Management**: Create and organize separate collections for different projects
* **Document Operations**: Add, update, or delete documents
* **Search Capabilities**:
  * Vector similarity search
  * Keyword-based search
  * Metadata filtering
* **Batch Processing**: Efficient handling of multiple operations

## Troubleshooting

If you encounter issues:

1. Verify your configuration file syntax
2. Ensure all paths are absolute and valid
3. Try using full paths for `uvx` with `which uvx` and using that path in the config
4. Check the Claude logs (paths listed above)

## Resources

* [Model Context Protocol Documentation](https://modelcontextprotocol.io/introduction)
* [Chroma MCP Server Documentation](https://github.com/chroma-core/chroma-mcp)
* [Claude Desktop Guide](https://docs.anthropic.com/claude/docs/claude-desktop)
