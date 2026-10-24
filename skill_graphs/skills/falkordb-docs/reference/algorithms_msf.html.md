[Skip to main content](https://docs.falkordb.com/algorithms/cdlp.html#main-content) Link Menu Expand (external link) Document Search Copy Copied
[ ](https://www.falkordb.com)
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
    * [BFS](https://docs.falkordb.com/algorithms/bfs.html)
    * [Betweenness Centrality](https://docs.falkordb.com/algorithms/betweenness-centrality.html)
    * Community Detection using Label Propagation (CDLP)
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

This site uses
Search FalkorDB Docs
  1. [Algorithms](https://docs.falkordb.com/algorithms/)
  2. Community Detection using Label Propagation (CDLP)


#  [](https://docs.falkordb.com/algorithms/cdlp.html#community-detection-using-label-propagation-cdlp) Community Detection using Label Propagation (CDLP)
##  [](https://docs.falkordb.com/algorithms/cdlp.html#overview) Overview
The Community Detection using Label Propagation (CDLP) algorithm identifies communities in networks by propagating labels through the graph structure. Each node starts with a unique label, and through iterative propagation, nodes adopt the most frequent label among their neighbors, naturally forming communities where densely connected nodes share the same label.
CDLP serves as a powerful algorithm in scenarios such as:
  * Social network community detection
  * Biological network module identification
  * Web page clustering and topic detection
  * Market segmentation analysis
  * Fraud detection networks


##  [](https://docs.falkordb.com/algorithms/cdlp.html#algorithm-details) Algorithm Details
CDLP initializes by assigning each node a unique label (typically its node ID). The algorithm then iteratively updates each node’s label to the most frequent label among its neighbors. During each iteration, nodes are processed in random order to avoid deterministic bias. The algorithm continues until labels stabilize (no changes occur) or a maximum number of iterations is reached. The final labels represent community assignments, where nodes sharing the same label belong to the same community.
The algorithm’s strength lies in its ability to discover communities without requiring prior knowledge of the number of communities or their sizes. It runs in near-linear time and mimics epidemic contagion by spreading labels through the network.
###  [](https://docs.falkordb.com/algorithms/cdlp.html#performance) Performance
CDLP operates with a time complexity of **O(m + n)** per iteration, where:
  * **n** represents the total number of nodes
  * **m** represents the total number of edges


The algorithm typically converges within a few iterations, making it highly efficient for large-scale networks.
##  [](https://docs.falkordb.com/algorithms/cdlp.html#syntax) Syntax
```
CALL algo.labelPropagation([config])

```

###  [](https://docs.falkordb.com/algorithms/cdlp.html#parameters) Parameters
The procedure accepts an optional configuration `Map` with the following parameters:
Name | Type | Default | Description
---|---|---|---
`nodeLabels` | Array | All labels | Array of node labels to filter which nodes are included in the computation
`relationshipTypes` | Array | All relationship types | Array of relationship types to define which edges are traversed
`maxIterations` | Integer | 10 | Maximum number of iterations to run the algorithm
###  [](https://docs.falkordb.com/algorithms/cdlp.html#return-values) Return Values
The procedure returns a stream of records with the following fields:
Name | Type | Description
---|---|---
`node` | Node | The node entity included in the community
`communityId` | Integer | Identifier of the community the node belongs to
##  [](https://docs.falkordb.com/algorithms/cdlp.html#examples) Examples
Let’s take this Social Network as an example:
```
    (Alice)---(Bob)---(Charlie)  (Kate)
       |       |         |
    (Diana)    |      (Eve)---(Frank)
       |       |         |      |
    (Grace)--(Henry)   (Iris)--(Jack)

```

There are 3 different communities that should emerge from this network:
  * Alice, Bob, Charlie, Diana, Grace, Henry
  * Eve, Frank, Iris, Jack
  * Any isolated nodes


###  [](https://docs.falkordb.com/algorithms/cdlp.html#create-the-graph) Create the Graph
```
CREATE
  (alice:Person {name: 'Alice'}),
  (bob:Person {name: 'Bob'}),
  (charlie:Person {name: 'Charlie'}),
  (diana:Person {name: 'Diana'}),
  (eve:Person {name: 'Eve'}),
  (frank:Person {name: 'Frank'}),
  (grace:Person {name: 'Grace'}),
  (henry:Person {name: 'Henry'}),
  (iris:Person {name: 'Iris'}),
  (jack:Person {name: 'Jack'}),
  (kate:Person {name: 'Kate'}),

  (alice)-[:KNOWS]->(bob),
  (bob)-[:KNOWS]->(charlie),
  (alice)-[:KNOWS]->(diana),
  (bob)-[:KNOWS]->(henry),
  (diana)-[:KNOWS]->(grace),
  (grace)-[:KNOWS]->(henry),
  (charlie)-[:KNOWS]->(eve),
  (eve)-[:KNOWS]->(frank),
  (eve)-[:KNOWS]->(iris),
  (frank)-[:KNOWS]->(jack),
  (iris)-[:KNOWS]->(jack)

```

###  [](https://docs.falkordb.com/algorithms/cdlp.html#example-detect-all-communities-in-the-network) Example: Detect all communities in the network
```
CALL algo.labelPropagation() YIELD node, communityId RETURN node.name AS name, communityId ORDER BY communityId, name

```

####  [](https://docs.falkordb.com/algorithms/cdlp.html#expected-results) Expected Results
| name | communityId | |————|————-| | `Alice` | 0 | | `Bob` | 0 | | `Charlie` | 0 | | `Diana` | 0 | | `Grace` | 0 | | `Henry` | 0 | | `Eve` | 2 | | `Frank` | 2 | | `Iris` | 2 | | `Jack` | 2 | | `Kate` | 10 |
###  [](https://docs.falkordb.com/algorithms/cdlp.html#example-detect-communities-with-limited-iterations) Example: Detect communities with limited iterations
```
CALL algo.labelPropagation({maxIterations: 5}) YIELD node, communityId

```

###  [](https://docs.falkordb.com/algorithms/cdlp.html#example-focus-on-specific-node-types) Example: Focus on specific node types
```
CALL algo.labelPropagation({nodeLabels: ['Person']}) YIELD node, communityId

```

###  [](https://docs.falkordb.com/algorithms/cdlp.html#example-use-only-certain-relationship-types) Example: Use only certain relationship types
```
CALL algo.labelPropagation({relationshipTypes: ['KNOWS', 'FRIENDS_WITH']}) YIELD node, communityId

```

###  [](https://docs.falkordb.com/algorithms/cdlp.html#example-combine-node-and-relationship-filtering) Example: Combine node and relationship filtering
```
CALL algo.labelPropagation({
  nodeLabels: ['Person'],
  relationshipTypes: ['KNOWS']
}) YIELD node, communityId

```

###  [](https://docs.falkordb.com/algorithms/cdlp.html#example-group-communities-together) Example: Group communities together
```
CALL algo.labelPropagation() YIELD node, communityId
RETURN collect(node.name) AS community_members, communityId, count(*) AS community_size
ORDER BY community_size DESC

```

####  [](https://docs.falkordb.com/algorithms/cdlp.html#expected-results-1) Expected Results
| community_members | communityId | community_size | |———————————————————-|————-|—————-| | `["Alice", "Bob", "Charlie", "Diana", "Grace", "Henry"]` | 0 | 6 | | `["Eve", "Frank", "Iris", "Jack"]` | 2 | 4 | | `["Kate"]` | 10 | 1 |
###  [](https://docs.falkordb.com/algorithms/cdlp.html#example-find-the-largest-communities) Example: Find the largest communities
```
CALL algo.labelPropagation() YIELD node, communityId
RETURN communityId, collect(node) AS nodes, count(*) AS size
ORDER BY size DESC
LIMIT 1

```

* * *
This site uses
