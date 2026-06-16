# Mem0
Source: https://docs.trychroma.com/integrations/frameworks/mem0

Mem0 is an AI memory layer that transforms stateless AI agents into stateful systems with persistent, intelligent memory across interactions. It enables AI applications to remember, learn, and evolve by providing different types of memory including working memory, factual memory, episodic memory, and semantic memory.

## Installation

```bash theme={null}
pip install mem0ai chromadb
```

## Configuration

Mem0 can be configured to use Chroma as its vector database backend. Here are the available configuration options:

| Parameter         | Description                   | Default Value |
| ----------------- | ----------------------------- | ------------- |
| `collection_name` | Name of the Chroma collection | `mem0`        |
| `client`          | Custom Chroma client          | `None`        |
| `path`            | Path for the Chroma database  | `db`          |
| `host`            | Chroma server host            | `None`        |
| `port`            | Chroma server port            | `None`        |

## Basic Usage

### Using Mem0 with Local Chroma

```python theme={null}
import os
from mem0 import Memory
