[Skip to main content](https://docs.falkordb.com/algorithms/bfs.html#main-content) Link Menu Expand (external link) Document Search Copy Copied
  * [Home](https://docs.falkordb.com/)
  * [Getting Started](https://docs.falkordb.com/getting-started/)
    * [Configuration](https://docs.falkordb.com/getting-started/configuration.html)
    * [Client Libraries](https://docs.falkordb.com/getting-started/clients.html)
  * [Commands](https://docs.falkordb.com/commands/)
    * [GRAPH.QUERY](https://docs.falkordb.com/commands/graph.query.html)
    * [GRAPH.RO_QUERY](https://docs.falkordb.com/commands/graph.ro-query.html)
    * [GRAPH.DELETE](https://docs.falkordb.com/commands/graph.delete.html)
    * [GRAPH.EXPLAIN](https://docs.falkordb.com/commands/graph.explain.html)
    * [GRAPH.LIST](https://docs.falkordb.com/commands/graph.list.html)
    * [GRAPH.PROFILE](https://docs.falkordb.com/commands/graph.profile.html)
    * [GRAPH.CONFIG-SET](https://docs.falkordb.com/commands/graph.config-set.html)
    * [GRAPH.CONSTRAINT DROP](https://docs.falkordb.com/commands/graph.constraint-drop.html)
    * [GRAPH.COPY](https://docs.falkordb.com/commands/graph.copy.html)
    * [GRAPH.INFO](https://docs.falkordb.com/commands/graph.info.html)
    * [GRAPH.MEMORY](https://docs.falkordb.com/commands/graph.memory.html)
    * [ACL](https://docs.falkordb.com/commands/acl.html)
    * [GRAPH.CONFIG-GET](https://docs.falkordb.com/commands/graph.config-get.html)
    * [GRAPH.CONSTRAINT CREATE](https://docs.falkordb.com/commands/graph.constraint-create.html)
    * [GRAPH.SLOWLOG](https://docs.falkordb.com/commands/graph.slowlog.html)
  * [Algorithms](https://docs.falkordb.com/algorithms/)
    * BFS
    * [Betweenness Centrality](https://docs.falkordb.com/algorithms/betweenness-centrality.html)
    * [Community Detection using Label Propagation (CDLP)](https://docs.falkordb.com/algorithms/cdlp.html)
    * [PageRank](https://docs.falkordb.com/algorithms/pagerank.html)
    * [algo.SPpaths](https://docs.falkordb.com/algorithms/sppath.html)
    * [algo.SSpaths](https://docs.falkordb.com/algorithms/sspath.html)
    * [Weakly Connected Components (WCC)](https://docs.falkordb.com/algorithms/wcc.html)
    * [MSF](https://docs.falkordb.com/algorithms/msf.html)
  * [Data types](https://docs.falkordb.com/datatypes.html)
  * [Integration](https://docs.falkordb.com/integration/)
    * [Rest API](https://docs.falkordb.com/integration/rest.html)
    * [Kafka Connect Sink](https://docs.falkordb.com/integration/kafka-connect.html)
    * [Apache Jena](https://docs.falkordb.com/integration/jena.html)
    * [BOLT protocol support](https://docs.falkordb.com/integration/bolt-support.html)
    * [Spring Data FalkorDB](https://docs.falkordb.com/integration/spring-data-falkordb.html)
    * [Snowflake Integration](https://docs.falkordb.com/integration/snowflake.html)
  * [UDFs](https://docs.falkordb.com/udfs/)
    * [FLEX Function Reference](https://docs.falkordb.com/udfs/flex/)
      * [Bitwise Functions](https://docs.falkordb.com/udfs/flex/bitwise/)
        * [bitwise.and](https://docs.falkordb.com/udfs/flex/bitwise/and.html)
        * [bitwise.not](https://docs.falkordb.com/udfs/flex/bitwise/not.html)
        * [bitwise.or](https://docs.falkordb.com/udfs/flex/bitwise/or.html)
        * [bitwise.shiftLeft](https://docs.falkordb.com/udfs/flex/bitwise/shiftLeft.html)
        * [bitwise.shiftRight](https://docs.falkordb.com/udfs/flex/bitwise/shiftRight.html)
        * [bitwise.xor](https://docs.falkordb.com/udfs/flex/bitwise/xor.html)
      * [Collection Functions](https://docs.falkordb.com/udfs/flex/collections/)
        * [coll.frequencies](https://docs.falkordb.com/udfs/flex/collections/frequencies.html)
        * [coll.intersection](https://docs.falkordb.com/udfs/flex/collections/intersection.html)
        * [coll.shuffle](https://docs.falkordb.com/udfs/flex/collections/shuffle.html)
        * [coll.union](https://docs.falkordb.com/udfs/flex/collections/union.html)
        * [coll.zip](https://docs.falkordb.com/udfs/flex/collections/zip.html)
      * [Date Functions](https://docs.falkordb.com/udfs/flex/date/)
        * [date.format](https://docs.falkordb.com/udfs/flex/date/format.html)
        * [date.parse](https://docs.falkordb.com/udfs/flex/date/parse.html)
        * [date.toTimeZone](https://docs.falkordb.com/udfs/flex/date/toTimeZone.html)
        * [date.truncate](https://docs.falkordb.com/udfs/flex/date/truncate.html)
      * [JSON Functions](https://docs.falkordb.com/udfs/flex/json/)
        * [json.fromJsonList](https://docs.falkordb.com/udfs/flex/json/fromJsonList.html)
        * [json.fromJsonMap](https://docs.falkordb.com/udfs/flex/json/fromJsonMap.html)
        * [json.toJson](https://docs.falkordb.com/udfs/flex/json/toJson.html)
      * [Map Functions](https://docs.falkordb.com/udfs/flex/map/)
        * [map.fromPairs](https://docs.falkordb.com/udfs/flex/map/fromPairs.html)
        * [map.merge](https://docs.falkordb.com/udfs/flex/map/merge.html)
        * [map.removeKey](https://docs.falkordb.com/udfs/flex/map/removeKey.html)
        * [map.removeKeys](https://docs.falkordb.com/udfs/flex/map/removeKeys.html)
        * [map.submap](https://docs.falkordb.com/udfs/flex/map/submap.html)
      * [Similarity Functions](https://docs.falkordb.com/udfs/flex/similarity/)
        * [sim.jaccard](https://docs.falkordb.com/udfs/flex/similarity/jaccard.html)
      * [Text Functions](https://docs.falkordb.com/udfs/flex/text/)
        * [text.camelCase](https://docs.falkordb.com/udfs/flex/text/camelCase.html)
        * [text.capitalize](https://docs.falkordb.com/udfs/flex/text/capitalize.html)
        * [text.decapitalize](https://docs.falkordb.com/udfs/flex/text/decapitalize.html)
        * [text.format](https://docs.falkordb.com/udfs/flex/text/format.html)
        * [text.indexOf](https://docs.falkordb.com/udfs/flex/text/indexOf.html)
        * [text.indexesOf](https://docs.falkordb.com/udfs/flex/text/indexesOf.html)
        * [text.jaroWinkler](https://docs.falkordb.com/udfs/flex/text/jaroWinkler.html)
        * [text.join](https://docs.falkordb.com/udfs/flex/text/join.html)
        * [text.levenshtein](https://docs.falkordb.com/udfs/flex/text/levenshtein.html)
        * [text.lpad](https://docs.falkordb.com/udfs/flex/text/lpad.html)
        * [text.regexGroups](https://docs.falkordb.com/udfs/flex/text/regexGroups.html)
        * [text.repeat](https://docs.falkordb.com/udfs/flex/text/repeat.html)
        * [text.replace](https://docs.falkordb.com/udfs/flex/text/replace.html)
        * [text.rpad](https://docs.falkordb.com/udfs/flex/text/rpad.html)
        * [text.snakeCase](https://docs.falkordb.com/udfs/flex/text/snakeCase.html)
        * [text.swapCase](https://docs.falkordb.com/udfs/flex/text/swapCase.html)
        * [text.upperCamelCase](https://docs.falkordb.com/udfs/flex/text/upperCamelCase.html)
  * [Cypher Language](https://docs.falkordb.com/cypher/)
    * [MATCH](https://docs.falkordb.com/cypher/match.html)
    * [OPTIONAL MATCH](https://docs.falkordb.com/cypher/optional-match.html)
    * [WHERE](https://docs.falkordb.com/cypher/where.html)
    * [RETURN](https://docs.falkordb.com/cypher/return.html)
    * [ORDER BY](https://docs.falkordb.com/cypher/order-by.html)
    * [SKIP](https://docs.falkordb.com/cypher/skip.html)
    * [LIMIT](https://docs.falkordb.com/cypher/limit.html)
    * [CREATE](https://docs.falkordb.com/cypher/create.html)
    * [DELETE](https://docs.falkordb.com/cypher/delete.html)
    * [SET](https://docs.falkordb.com/cypher/set.html)
    * [MERGE](https://docs.falkordb.com/cypher/merge.html)
    * [WITH](https://docs.falkordb.com/cypher/with.html)
    * [UNION](https://docs.falkordb.com/cypher/union.html)
    * [UNWIND](https://docs.falkordb.com/cypher/unwind.html)
    * [FOREACH](https://docs.falkordb.com/cypher/foreach.html)
    * [CALL](https://docs.falkordb.com/cypher/call.html)
    * [LOAD CSV](https://docs.falkordb.com/cypher/load-csv.html)
    * [Functions](https://docs.falkordb.com/cypher/functions.html)
    * [Procedures](https://docs.falkordb.com/cypher/procedures.html)
    * [Indexing](https://docs.falkordb.com/cypher/indexing/)
      * [Range Index](https://docs.falkordb.com/cypher/indexing/range-index.html)
      * [Full-text Index](https://docs.falkordb.com/cypher/indexing/fulltext-index.html)
      * [Vector Index](https://docs.falkordb.com/cypher/indexing/vector-index.html)
    * [Cypher coverage](https://docs.falkordb.com/cypher/cypher-support.html)
    * [REMOVE](https://docs.falkordb.com/cypher/remove.html)
    * [Known limitations](https://docs.falkordb.com/cypher/known-limitations.html)
  * [GenAI Tools](https://docs.falkordb.com/genai-tools/)
    * [GraphRAG-SDK](https://docs.falkordb.com/genai-tools/graphrag-sdk.html)
    * [AG2](https://docs.falkordb.com/genai-tools/ag2.html)
    * [LangChain](https://docs.falkordb.com/genai-tools/langchain.html)
    * [LangGraph](https://docs.falkordb.com/genai-tools/langgraph.html)
    * [LlamaIndex](https://docs.falkordb.com/genai-tools/llamaindex.html)
    * [GraphRAG Toolkit](https://docs.falkordb.com/genai-tools/graphrag-toolkit.html)
    * [MCP Server](https://docs.falkordb.com/genai-tools/mcpserver/)
      * [Quick Start](https://docs.falkordb.com/genai-tools/mcpserver/quickstart.html)
      * [Configuration](https://docs.falkordb.com/genai-tools/mcpserver/configuration.html)
      * [Docker Deployment](https://docs.falkordb.com/genai-tools/mcpserver/docker.html)
  * [Browser](https://docs.falkordb.com/browser/)
    * [UI Elements](https://docs.falkordb.com/browser/ui/)
      * [Login Screen](https://docs.falkordb.com/browser/ui/login.html)
      * [Navigation & Header](https://docs.falkordb.com/browser/ui/navigation.html)
      * [Settings Page](https://docs.falkordb.com/browser/ui/settings.html)
      * [Graph Page (Layout)](https://docs.falkordb.com/browser/ui/graph-page.html)
      * [Main Graph Canvas](https://docs.falkordb.com/browser/ui/graph-canvas.html)
      * [Graph Info Panel](https://docs.falkordb.com/browser/ui/graph-info-panel.html)
      * [Style Panel](https://docs.falkordb.com/browser/ui/style-panel.html)
      * [Data / Property Panel](https://docs.falkordb.com/browser/ui/data-panel.html)
      * [Query Editor](https://docs.falkordb.com/browser/ui/query-editor.html)
      * [Query History](https://docs.falkordb.com/browser/ui/query-history.html)
      * [Table View](https://docs.falkordb.com/browser/ui/table-view.html)
      * [Metadata View](https://docs.falkordb.com/browser/ui/metadata-view.html)
      * [Graph Toolbar & Element Actions](https://docs.falkordb.com/browser/ui/toolbar-actions.html)
      * [Chat Panel](https://docs.falkordb.com/browser/ui/chat-panel.html)
  * [Cloud DBaaS](https://docs.falkordb.com/cloud/)
    * [Free Tier](https://docs.falkordb.com/cloud/free-tier.html)
    * [Startup Tier](https://docs.falkordb.com/cloud/startup-tier.html)
    * [Pro Tier](https://docs.falkordb.com/cloud/pro-tier.html)
    * [Enterprise Tier](https://docs.falkordb.com/cloud/enterprise-tier.html)
    * [Features](https://docs.falkordb.com/cloud/features.html)
  * [Operations](https://docs.falkordb.com/operations/)
    * [Migration](https://docs.falkordb.com/operations/migration/)
      * [RedisGraph to FalkorDB](https://docs.falkordb.com/operations/migration/redisgraph-to-falkordb.html)
      * [Neo4j to FalkorDB](https://docs.falkordb.com/operations/migration/neo4j-to-falkordb.html)
      * [Kuzu to FalkorDB](https://docs.falkordb.com/operations/migration/kuzu-to-falkordb.html)
      * [RDF to FalkorDB](https://docs.falkordb.com/operations/migration/rdf-to-falkordb.html)
      * [SQL Sources to FalkorDB (Online Migration)](https://docs.falkordb.com/operations/migration/sql-to-falkordb.html)
    * [Durability](https://docs.falkordb.com/operations/durability.html)
      * [Persistence on Docker](https://docs.falkordb.com/operations/persistence.html)
    * [Replication](https://docs.falkordb.com/operations/replication.html)
    * [Cluster](https://docs.falkordb.com/operations/cluster.html)
    * [Kubernetes support](https://docs.falkordb.com/operations/k8s-support.html)
    * [OpenTelemetry Integration](https://docs.falkordb.com/operations/opentelemetry.html)
    * [Railway](https://docs.falkordb.com/operations/railway.html)
    * [FalkorDBLite](https://docs.falkordb.com/operations/falkordblite/)
      * [FalkorDBLite (Python)](https://docs.falkordb.com/operations/falkordblite/falkordblite-py.html)
      * [FalkorDBLite (TypeScript)](https://docs.falkordb.com/operations/falkordblite/falkordblite-ts.html)
    * [Lightning.AI](https://docs.falkordb.com/operations/lightning-ai.html)
    * [Building Docker](https://docs.falkordb.com/operations/building-docker.html)
    * [KubeBlocks](https://docs.falkordb.com/operations/kubeblocks.html)
    * [Docker and Docker Compose](https://docs.falkordb.com/operations/docker.html)
  * [Agentic Memory](https://docs.falkordb.com/agentic-memory/)
    * [Graphiti](https://docs.falkordb.com/agentic-memory/graphiti.html)
    * [Cognee](https://docs.falkordb.com/agentic-memory/cognee.html)
    * [Graphiti MCP Server](https://docs.falkordb.com/agentic-memory/graphiti-mcp-server.html)
    * [Mem0](https://docs.falkordb.com/agentic-memory/mem0.html)
  * [The FalkorDB Design](https://docs.falkordb.com/design/)
    * [Client Specification](https://docs.falkordb.com/design/client-spec.html)
    * [Result Set Structure](https://docs.falkordb.com/design/result-structure.html)
    * [GRAPH.BULK endpoint specification](https://docs.falkordb.com/design/bulk-spec.html)
    * [Third Party](https://docs.falkordb.com/design/third-party.html)
  * [References](https://docs.falkordb.com/References/)
    * [FalkorDB License](https://docs.falkordb.com/References/license.html)


Search FalkorDB Docs
  1. [Algorithms](https://docs.falkordb.com/algorithms/)
  2. BFS


#  [](https://docs.falkordb.com/algorithms/bfs.html#bfs) BFS
##  [](https://docs.falkordb.com/algorithms/bfs.html#overview) Overview
The Breadth-First Search (BFS) procedure allows you to perform a breadth-first traversal of a graph starting from a specific node. BFS explores all the nodes at the present depth before moving on to nodes at the next depth level. This is particularly useful for finding the shortest path between two nodes or exploring a graph layer by layer.
##  [](https://docs.falkordb.com/algorithms/bfs.html#syntax) Syntax
```
CALL algo.bfs(start_node, max_depth, relationship)
YIELD nodes, edges

```

##  [](https://docs.falkordb.com/algorithms/bfs.html#arguments) Arguments
Name | Type | Description | Default
---|---|---|---
start_node | Node | Starting node for the BFS traversal | (Required)
max_depth | Integer | Maximum depth to traverse | (Required)
relationship | String or null | The relationship type to traverse. If null, all relationship types are used | null
##  [](https://docs.falkordb.com/algorithms/bfs.html#returns) Returns
Name | Type | Description
---|---|---
nodes | List | List of visited nodes in breadth-first order
edges | List | List of edges traversed during the BFS
##  [](https://docs.falkordb.com/algorithms/bfs.html#examples) Examples
###  [](https://docs.falkordb.com/algorithms/bfs.html#social-network-friend-recommendations) Social Network Friend Recommendations
This example demonstrates how to use BFS to find potential friend recommendations in a social network. By exploring friends of friends, BFS uncovers second-degree connections—people you may know through mutual friends—which are often strong candidates for relevant and meaningful recommendations.
####  [](https://docs.falkordb.com/algorithms/bfs.html#create-the-graph) Create the Graph
```
CREATE
  (alice:Person {name: 'Alice', age: 28, city: 'New York'}),
  (bob:Person {name: 'Bob', age: 32, city: 'Boston'}),
  (charlie:Person {name: 'Charlie', age: 35, city: 'Chicago'}),
  (david:Person {name: 'David', age: 29, city: 'Denver'}),
  (eve:Person {name: 'Eve', age: 31, city: 'San Francisco'}),
  (frank:Person {name: 'Frank', age: 27, city: 'Miami'}),

  (alice)-[:FRIEND]->(bob),
  (alice)-[:FRIEND]->(charlie),
  (bob)-[:FRIEND]->(david),
  (charlie)-[:FRIEND]->(eve),
  (david)-[:FRIEND]->(frank),
  (eve)-[:FRIEND]->(frank)

```

![Graph BFS](https://docs.falkordb.com/images/graph_bfs.png)
####  [](https://docs.falkordb.com/algorithms/bfs.html#find-friends-of-friends-potential-recommendations) Find Friends of Friends (Potential Recommendations)
```
// Find Alice's friends-of-friends (potential recommendations)
MATCH (alice:Person {name: 'Alice'})
CALL algo.bfs(alice, 2, 'FRIEND')
YIELD nodes

// Process results to get only depth 2 connections (friends of friends)
WHERE size(nodes) >= 3
WITH alice, nodes[2] AS potential_friend
WHERE NOT (alice)-[:FRIEND]->(potential_friend)
RETURN potential_friend

```

In this social network example, the BFS algorithm helps find potential friend recommendations by identifying people who are connected to Alice’s existing friends but not directly connected to Alice yet.
##  [](https://docs.falkordb.com/algorithms/bfs.html#performance-considerations) Performance Considerations
  * **Indexing:** Ensure properties used for finding your starting node are indexed for optimal performance
  * **Maximum Depth:** Choose an appropriate max_depth value based on your graph’s connectivity; large depths in highly connected graphs can result in exponential growth of traversed nodes
  * **Relationship Filtering:** When applicable, specify the relationship type to limit the traversal scope
  * **Memory Management:** Be aware that the procedure stores visited nodes in memory to avoid cycles, which may require significant resources in large, densely connected graphs


##  [](https://docs.falkordb.com/algorithms/bfs.html#error-handling) Error Handling
Common errors that may occur:
  * **Null Starting Node:** If the start_node parameter is null, the procedure will raise an error; ensure your MATCH clause successfully finds the starting node
  * **Invalid Relationship Type:** If you specify a relationship type that doesn’t exist in your graph, the traversal will only include the starting node
  * **Memory Limitations:** For large graphs with high connectivity, an out-of-memory error may occur if too many nodes are visited
  * **Result Size:** If the BFS traversal returns too many nodes, query execution may be slow or time out; in such cases, try reducing the max_depth or filtering by relationship types


* * *
Hi. Need any help?
