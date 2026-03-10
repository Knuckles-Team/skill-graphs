# Skill Graphs - Indexed Agent Knowledge

![PyPI - Version](https://img.shields.io/pypi/v/skill-graphs)
![MCP Server](https://badge.mcpx.dev?type=server 'MCP Server')

*Version: 0.1.17*

## Overview

Skill Graphs is a dedicated repository for structured, documentation-based skills. It is designed to host "knowledge graphs" transformed from technical documentation, APIs, and web crawls, specifically for use with Pydantic AI Agents.

## Enabling Skill Graphs

By default, all skill-graphs included in this package are **disabled**. You can enable specific skill-graphs by setting their corresponding environment variables to `True`.

| Skill Directory | Description | Enable Flag |
|:----------------|:------------|:-------------|
| `aws-docs` | AWS Documentation | `AWS_DOCS_ENABLE=True` |
| `azure-docs` | Azure Documentation | `AZURE_DOCS_ENABLE=True` |
| `c-docs` | C Language Documentation | `C_DOCS_ENABLE=True` |
| `chakra-ui-docs` | Chakra UI Documentation | `CHAKRA_UI_DOCS_ENABLE=True` |
| `chromadb-docs` | ChromaDB Documentation | `CHROMADB_DOCS_ENABLE=True` |
| `couchbase-docs` | Couchbase Documentation | `COUCHBASE_DOCS_ENABLE=True` |
| `django-docs` | Django Documentation | `DJANGO_DOCS_ENABLE=True` |
| `docker-docs` | Docker Documentation | `DOCKER_DOCS_ENABLE=True` |
| `falkordb-docs` | FalkorDB Documentation | `FALKORDB_DOCS_ENABLE=True` |
| `fastapi-docs` | FastAPI Documentation | `FASTAPI_DOCS_ENABLE=True` |
| `fastmcp-docs` | FastMCP Documentation | `FASTMCP_DOCS_ENABLE=True` |
| `flask-docs` | Flask Documentation | `FLASK_DOCS_ENABLE=True` |
| `framer-docs` | Framer Motion Documentation | `FRAMER_DOCS_ENABLE=True` |
| `gcp-docs` | GCP Documentation | `GCP_DOCS_ENABLE=True` |
| `go-docs` | Go Documentation | `GO_DOCS_ENABLE=True` |
| `huggingface-docs` | Hugging Face Documentation | `HUGGINGFACE_DOCS_ENABLE=True` |
| `java-docs` | Java Documentation | `JAVA_DOCS_ENABLE=True` |
| `langchain-docs` | LangChain Documentation | `LANGCHAIN_DOCS_ENABLE=True` |
| `laravel-docs` | Laravel Documentation | `LARAVEL_DOCS_ENABLE=True` |
| `linux-docs` | Linux Documentation | `LINUX_DOCS_ENABLE=True` |
| `mariadb-docs` | MariaDB Documentation | `MARIADB_DOCS_ENABLE=True` |
| `material-ui-docs` | Material UI Documentation | `MATERIAL_UI_DOCS_ENABLE=True` |
| `matplotlib-docs` | Matplotlib Documentation | `MATPLOTLIB_DOCS_ENABLE=True` |
| `minio-docs` | MinIO Documentation | `MINIO_DOCS_ENABLE=True` |
| `mongodb-docs` | MongoDB Documentation | `MONGODB_DOCS_ENABLE=True` |
| `mssql-docs` | MS SQL Server Documentation | `MSSQL_DOCS_ENABLE=True` |
| `neo4j-docs` | Neo4j Documentation | `NEO4J_DOCS_ENABLE=True` |
| `nestjs-docs` | NestJS Documentation | `NESTJS_DOCS_ENABLE=True` |
| `nextjs-docs` | Next.js Documentation | `NEXTJS_DOCS_ENABLE=True` |
| `nodejs-docs` | Node.js Documentation | `NODEJS_DOCS_ENABLE=True` |
| `numpy-docs` | NumPy Documentation | `NUMPY_DOCS_ENABLE=True` |
| `pandas-docs` | Pandas Documentation | `PANDAS_DOCS_ENABLE=True` |
| `postgres-docs` | PostgreSQL Documentation | `POSTGRES_DOCS_ENABLE=True` |
| `pydantic-ai-docs` | Pydantic AI Documentation | `PYDANTIC_AI_DOCS_ENABLE=True` |
| `pydantic-docs` | Pydantic Documentation | `PYDANTIC_DOCS_ENABLE=True` |
| `python-docs` | Python Documentation | `PYTHON_DOCS_ENABLE=True` |
| `pytorch-docs` | PyTorch Documentation | `PYTORCH_DOCS_ENABLE=True` |
| `qdrant-docs` | Qdrant Documentation | `QDRANT_DOCS_ENABLE=True` |
| `radix-ui-docs` | Radix UI Documentation | `RADIX_UI_DOCS_ENABLE=True` |
| `react-docs` | React Documentation | `REACT_DOCS_ENABLE=True` |
| `reactrouter-docs` | React Router Documentation | `REACTROUTER_DOCS_ENABLE=True` |
| `redis-docs` | Redis Documentation | `REDIS_DOCS_ENABLE=True` |
| `redux-docs` | Redux Documentation | `REDUX_DOCS_ENABLE=True` |
| `remix-docs` | Remix Documentation | `REMIX_DOCS_ENABLE=True` |
| `rust-docs` | Rust Documentation | `RUST_DOCS_ENABLE=True` |
| `scikit-learn-docs` | Scikit-learn Documentation | `SCIKIT_LEARN_DOCS_ENABLE=True` |
| `scipy-docs` | SciPy Documentation | `SCIPY_DOCS_ENABLE=True` |
| `shadcn-docs` | shadcn/ui Documentation | `SHADCN_DOCS_ENABLE=True` |
| `svelte-docs` | Svelte Documentation | `SVELTE_DOCS_ENABLE=True` |
| `tanstack-docs` | TanStack Documentation | `TANSTACK_DOCS_ENABLE=True` |
| `temporal-docs` | Temporal Documentation | `TEMPORAL_DOCS_ENABLE=True` |
| `tensorflow-docs` | TensorFlow Documentation | `TENSORFLOW_DOCS_ENABLE=True` |
| `terraform-docs` | Terraform Documentation | `TERRAFORM_DOCS_ENABLE=True` |
| `testing-library-docs` | Testing Library Documentation | `TESTING_LIBRARY_DOCS_ENABLE=True` |
| `vercel-docs` | Vercel Documentation | `VERCEL_DOCS_ENABLE=True` |
| `vitejs-docs` | Vite Documentation | `VITEJS_DOCS_ENABLE=True` |
| `vuejs-docs` | Vue.js Documentation | `VUEJS_DOCS_ENABLE=True` |

## Installation

```bash
pip install skill-graphs
```

## Usage

Skill graphs are typically loaded using the `get_skill_graphs_path()` utility from `skill_graphs.skill_graph_utilities`.

```python
from skill_graphs.skill_graph_utilities import get_skill_graphs_path
from agent_utilities.agent_utilities import SkillsToolset

# Load enabled skill graphs
skills_directories = get_skill_graphs_path()
skills = SkillsToolset(directories=skills_directories)
```

## Building New Skill Graphs

Use the `skill-graph-builder` from the `universal-skills` package to generate new graphs:

```bash
python scripts/generate_skill.py https://ai.pydantic.dev pydantic-ai
```

By default, the builder will now target this repository if it is present in your workspace.
