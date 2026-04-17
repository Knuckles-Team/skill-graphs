## Query Store and intelligent query processing
The [intelligent query processing (IQP)](https://learn.microsoft.com/en-us/sql/relational-databases/performance/intelligent-query-processing?view=sql-server-ver17) feature family includes features that improve the performance of existing workloads with minimal implementation effort.
[ ![Diagram representing the features in the intelligent query processing family and when they were introduced in SQL Server.](https://learn.microsoft.com/en-us/sql/sql-server/media/what-s-new-in-sql-server-2025/intelligent-query-processing-features.png?view=sql-server-ver17) ](https://learn.microsoft.com/en-us/sql/sql-server/media/what-s-new-in-sql-server-2025/intelligent-query-processing-features.png?view=sql-server-ver17#lightbox)
Expand table
New feature or update | Details
---|---
[Cardinality estimation feedback for expressions](https://learn.microsoft.com/en-us/sql/relational-databases/performance/intelligent-query-processing-ce-feedback-for-expressions?view=sql-server-ver17) | Learns from previous executions of expressions across queries. Finds appropriate cardinality estimation (CE) model choices and applies to future executions of those expressions.
[Optional parameter plan optimization (OPPO)](https://learn.microsoft.com/en-us/sql/relational-databases/performance/optional-parameter-optimization?view=sql-server-ver17) | Leverages the adaptive plan optimization (Multiplan) infrastructure that was introduced with the Parameter Sensitive Plan Optimization (PSPO) improvement, which generates multiple plans from a single statement. This allows the feature to make different assumptions depending on the parameter values used in the query.
Degree of parallelism (DOP) feedback | Now on by default.
[Query Store for readable secondaries](https://learn.microsoft.com/en-us/sql/relational-databases/performance/query-store-for-secondary-replicas?view=sql-server-ver17) | Now on by default.
[ABORT_QUERY_EXECUTION query hint](https://learn.microsoft.com/en-us/sql/relational-databases/performance/query-store-hints-best-practices?view=sql-server-ver17#block-future-execution-of-problematic-queries) | Blocks future execution of known problematic queries, for example nonessential queries affecting application workloads.
[](https://learn.microsoft.com/en-us/sql/sql-server/what-s-new-in-sql-server-2025?view=sql-server-ver17#language)
