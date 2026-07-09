## AI
Expand table
New feature or update | Details
---|---
[GitHub Copilot in SQL Server Management Studio](https://learn.microsoft.com/en-us/ssms/github-copilot/overview) | Ask questions. Get answers from your data.
[Vector data type](https://learn.microsoft.com/en-us/sql/t-sql/data-types/vector-data-type?view=sql-server-ver17) | Store vector data optimized for operations such as similarity search and machine learning applications. Vectors are stored in an optimized binary format but are exposed as JSON arrays for convenience. Each element of the vector can be stored either using a single-precision (4-byte) or half-precision (2-byte) floating-point value.
[Vector functions](https://learn.microsoft.com/en-us/sql/t-sql/functions/vector-functions-transact-sql?view=sql-server-ver17) | New scalar functions perform operations on vectors in binary format, allowing applications to store and manipulate vectors in the SQL Database Engine.
[Vector index](https://learn.microsoft.com/en-us/sql/sql-server/ai/vectors?view=sql-server-ver17#vector-search) | Create and manage approximate vector indexes to quickly and efficiently find similar vectors to a given reference vector.

Query vector indexes from [sys.vector_indexes](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-vector-indexes-transact-sql?view=sql-server-ver17). Requires [PREVIEW_FEATURES database scoped configuration](https://learn.microsoft.com/en-us/sql/t-sql/statements/alter-database-scoped-configuration-transact-sql?view=sql-server-ver17#preview-features).
[Manage external AI models](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-external-model-transact-sql?view=sql-server-ver17) | Manage external AI model objects for embedding tasks (creating vector arrays) accessing REST AI inference endpoints.
[](https://learn.microsoft.com/en-us/sql/sql-server/what-s-new-in-sql-server-2025?view=sql-server-ver17#developer)
