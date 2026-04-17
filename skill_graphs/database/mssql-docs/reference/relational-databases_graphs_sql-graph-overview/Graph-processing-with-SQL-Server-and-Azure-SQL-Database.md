# Graph processing with SQL Server and Azure SQL Database
Feedback
Summarize this article for me
##  In this article
  1. [What is a graph database?](https://learn.microsoft.com/en-us/sql/relational-databases/graphs/sql-graph-overview?view=sql-server-ver17#what-is-a-graph-database)
  2. [When to use a graph database](https://learn.microsoft.com/en-us/sql/relational-databases/graphs/sql-graph-overview?view=sql-server-ver17#when-to-use-a-graph-database)
  3. [Graph features introduced in SQL Server 2017](https://learn.microsoft.com/en-us/sql/relational-databases/graphs/sql-graph-overview?view=sql-server-ver17#graph-features-introduced-in-sql-server-2017)
  4. [Edge constraints](https://learn.microsoft.com/en-us/sql/relational-databases/graphs/sql-graph-overview?view=sql-server-ver17#edge-constraints)
  5. [Merge DML](https://learn.microsoft.com/en-us/sql/relational-databases/graphs/sql-graph-overview?view=sql-server-ver17#merge-dml)
  6. [Shortest path](https://learn.microsoft.com/en-us/sql/relational-databases/graphs/sql-graph-overview?view=sql-server-ver17#shortest-path)
  7. [Fabric SQL database](https://learn.microsoft.com/en-us/sql/relational-databases/graphs/sql-graph-overview?view=sql-server-ver17#fabric-sql-database)
  8. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/graphs/sql-graph-overview?view=sql-server-ver17#related-content)

Show 4 more
**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) SQL Server 2017 (14.x) and later versions ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Database](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL database in Microsoft Fabric](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to)
SQL Server offers graph database capabilities to model many-to-many relationships. The graph relationships are integrated into Transact-SQL and receive the benefits of using SQL Server as the foundational database management system.
[](https://learn.microsoft.com/en-us/sql/relational-databases/graphs/sql-graph-overview?view=sql-server-ver17#what-is-a-graph-database)
## What is a graph database?
A [graph database](https://learn.microsoft.com/en-us/fabric/graph/graph-database) is a collection of nodes (or vertices) and edges (or relationships). A node represents an entity (for example, a person or an organization) and an edge represents a relationship between the two nodes that it connects (for example, likes or friends). Both nodes and edges might have properties associated with them. Here are some features that make a graph database unique:
  * Edges or relationships are first class entities in a Graph Database and can have attributes or properties associated with them.
  * A single edge can flexibly connect multiple nodes in a Graph Database.
  * You can express pattern matching and multi-hop navigation queries easily.
  * You can express transitive closure and polymorphic queries easily.


[](https://learn.microsoft.com/en-us/sql/relational-databases/graphs/sql-graph-overview?view=sql-server-ver17#when-to-use-a-graph-database)
## When to use a graph database
A relational database can achieve anything a graph database can. However, a graph database makes it easier to express certain kinds of queries. Also, with specific optimizations, certain queries might perform better. Your decision to choose either a relational or graph database is based on following factors:
  * Your application has hierarchical data. The **HierarchyID** data type can be used to implement hierarchies, but it has some limitations. For example, it doesn't allow you to store multiple parents for a node.
  * Your application has complex many-to-many relationships; as application evolves, new relationships are added.
  * You need to analyze interconnected data and relationships.


[](https://learn.microsoft.com/en-us/sql/relational-databases/graphs/sql-graph-overview?view=sql-server-ver17#graph-features-introduced-in-sql-server-2017)
## Graph features introduced in SQL Server 2017
The following features were introduced in SQL Server 2017 (14.x).
[](https://learn.microsoft.com/en-us/sql/relational-databases/graphs/sql-graph-overview?view=sql-server-ver17#create-graph-objects)
### Create graph objects
Transact-SQL extensions allow users to create node or edge tables. Both nodes and edges can have properties associated to them. Since, nodes and edges are stored as tables, all the operations that are supported on relational tables are supported on node or edge table. Here's an example:
SQL
Copy
```
CREATE TABLE Person
(
    ID INT PRIMARY KEY,
    Name VARCHAR (100),
    Age INT
) AS NODE;
CREATE TABLE friends
(
    StartDate DATE
) AS EDGE;

```

The following diagram shows how Nodes and Edges are stored as tables.
[ ![Diagram showing the Nodes and Edges are stored as tables.](https://learn.microsoft.com/en-us/sql/relational-databases/graphs/media/sql-graph-overview/person-friends-tables.png?view=sql-server-ver17) ](https://learn.microsoft.com/en-us/sql/relational-databases/graphs/media/sql-graph-overview/person-friends-tables.png?view=sql-server-ver17#lightbox)
[](https://learn.microsoft.com/en-us/sql/relational-databases/graphs/sql-graph-overview?view=sql-server-ver17#query-language-extensions)
### Query language extensions
New `MATCH` clause is introduced to support pattern matching and multi-hop navigation through the graph. The `MATCH` function uses ASCII-art style syntax for pattern matching. For example, to find friends of "John":
SQL
Copy
```
-- Find friends of John
SELECT Person2.Name
FROM Person AS Person1, Friends, Person AS Person2
WHERE MATCH(Person1-(Friends)->Person2)
      AND Person1.Name = 'John';

```

[](https://learn.microsoft.com/en-us/sql/relational-databases/graphs/sql-graph-overview?view=sql-server-ver17#fully-integrated-in-sql-server-database-engine)
### Fully integrated in SQL Server Database Engine
Graph extensions are fully integrated in SQL Server engine. Use the same storage engine, metadata, query processor, etc. to store and query graph data. Query across graph and relational data in a single query. Combining graph capabilities with other SQL Server technologies like columnstore indexes, HA, R services, etc. SQL graph also supports all the security and compliance features available with SQL Server.
[](https://learn.microsoft.com/en-us/sql/relational-databases/graphs/sql-graph-overview?view=sql-server-ver17#tooling-and-ecosystem)
### Tooling and ecosystem
Benefit from existing tools and ecosystem that SQL Server offers. Tools like backup and restore, import and export, and **bcp** just work out of the box. Other tools or services like SQL Server Integration Services, SQL Server Reporting Services, or Power BI work with graph tables, just the way they work with relational tables.
[](https://learn.microsoft.com/en-us/sql/relational-databases/graphs/sql-graph-overview?view=sql-server-ver17#edge-constraints)
## Edge constraints
An edge constraint is defined on a graph edge table and is a pair of node tables that a given edge type can connect. Edge constraints help developers restrict the type of nodes that a given edge can connect.
To learn more about how to create and use edge constraints, refer to [Edge constraints](https://learn.microsoft.com/en-us/sql/relational-databases/tables/graph-edge-constraints?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/relational-databases/graphs/sql-graph-overview?view=sql-server-ver17#merge-dml)
## Merge DML
The [MERGE](https://learn.microsoft.com/en-us/sql/t-sql/statements/merge-transact-sql?view=sql-server-ver17) statement performs insert, update, or delete operations on a target table based on the results of a join with a source table. For example, you can synchronize two tables by inserting, updating, or deleting rows in a target table based on differences between the target table and the source table. Using `MATCH` predicates in a `MERGE` statement is now supported on Azure SQL Database and SQL Server vNext. That is, it's now possible to merge your current graph data (node or edge tables) with new data using the `MATCH` predicates to specify graph relationships in a single statement, instead of separate `INSERT`, `UPDATE`, and `DELETE` statements.
To learn more about how match can be used in merge DML, refer to [MERGE](https://learn.microsoft.com/en-us/sql/t-sql/statements/merge-transact-sql?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/relational-databases/graphs/sql-graph-overview?view=sql-server-ver17#shortest-path)
## Shortest path
The [SHORTEST_PATH](https://learn.microsoft.com/en-us/sql/relational-databases/graphs/sql-graph-shortest-path?view=sql-server-ver17) function finds shortest path between any two nodes in a graph or starting from a given node to all the other nodes in the graph. `SHORTEST PATH` can also be used to find a transitive closure or for arbitrary length traversals in the graph.
[](https://learn.microsoft.com/en-us/sql/relational-databases/graphs/sql-graph-overview?view=sql-server-ver17#fabric-sql-database)
## Fabric SQL database
In Fabric SQL database, SQL Graph is allowed, but Node and Edge tables don't mirror to Fabric OneLake.
[](https://learn.microsoft.com/en-us/sql/relational-databases/graphs/sql-graph-overview?view=sql-server-ver17#related-content)
## Related content
  * [SQL Graph Architecture](https://learn.microsoft.com/en-us/sql/relational-databases/graphs/sql-graph-architecture?view=sql-server-ver17)
  * [Create a graph database and run some pattern matching queries using T-SQL](https://learn.microsoft.com/en-us/sql/relational-databases/graphs/sql-graph-sample?view=sql-server-ver17)


* * *
## Feedback
Was this page helpful?
Yes No No
Need help with this topic?
Want to try using Ask Learn to clarify or guide you through this topic?
Ask Learn Ask Learn
Suggest a fix?
* * *
##  Additional resources
Mar 8, 4 PM - Mar 8, 4 PM
Experiment with what's next in AI-driven apps and agent design
* * *
  * Last updated on 10/14/2025


##  In this article
  1. [What is a graph database?](https://learn.microsoft.com/en-us/sql/relational-databases/graphs/sql-graph-overview?view=sql-server-ver17#what-is-a-graph-database)
  2. [When to use a graph database](https://learn.microsoft.com/en-us/sql/relational-databases/graphs/sql-graph-overview?view=sql-server-ver17#when-to-use-a-graph-database)
  3. [Graph features introduced in SQL Server 2017](https://learn.microsoft.com/en-us/sql/relational-databases/graphs/sql-graph-overview?view=sql-server-ver17#graph-features-introduced-in-sql-server-2017)
  4. [Edge constraints](https://learn.microsoft.com/en-us/sql/relational-databases/graphs/sql-graph-overview?view=sql-server-ver17#edge-constraints)
  5. [Merge DML](https://learn.microsoft.com/en-us/sql/relational-databases/graphs/sql-graph-overview?view=sql-server-ver17#merge-dml)
  6. [Shortest path](https://learn.microsoft.com/en-us/sql/relational-databases/graphs/sql-graph-overview?view=sql-server-ver17#shortest-path)
  7. [Fabric SQL database](https://learn.microsoft.com/en-us/sql/relational-databases/graphs/sql-graph-overview?view=sql-server-ver17#fabric-sql-database)
  8. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/graphs/sql-graph-overview?view=sql-server-ver17#related-content)


Was this page helpful?
Yes No No
Need help with this topic?
Want to try using Ask Learn to clarify or guide you through this topic?
Ask Learn Ask Learn
Suggest a fix?
##
Ask Learn
Preview
Ask Learn is an AI assistant that can answer questions, clarify concepts, and define terms using trusted Microsoft documentation.
Please sign in to use Ask Learn.
[ Sign in ](https://learn.microsoft.com/en-us/sql/relational-databases/graphs/sql-graph-overview?view=sql-server-ver17)
[English (United States)](https://learn.microsoft.com/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fsql%2Frelational-databases%2Fgraphs%2Fsql-graph-overview%3Fview%3Dsql-server-ver17)
Theme
  * Light
  * Dark
  * High contrast


  * [AI Disclaimer](https://learn.microsoft.com/en-us/principles-for-ai-generated-content)
  * [Previous Versions](https://learn.microsoft.com/en-us/previous-versions/)
  * [Blog](https://techcommunity.microsoft.com/t5/microsoft-learn-blog/bg-p/MicrosoftLearnBlog)
  * [Contribute](https://learn.microsoft.com/en-us/contribute)
  * [Privacy](https://go.microsoft.com/fwlink/?LinkId=521839)
  * [Consumer Health Privacy](https://go.microsoft.com/fwlink/?linkid=2259814)
  * [Terms of Use](https://learn.microsoft.com/en-us/legal/termsofuse)
  * [Trademarks](https://www.microsoft.com/legal/intellectualproperty/Trademarks/)
  * © Microsoft 2026
