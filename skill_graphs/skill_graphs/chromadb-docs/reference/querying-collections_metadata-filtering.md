[Skip to main content](https://docs.trychroma.com/docs/querying-collections/metadata-filtering#content-area)
[Chroma Docs home page![light logo](https://mintcdn.com/chroma-8943dec5/wr97NKZIObCJm0cR/images/light-logo.svg?fit=max&auto=format&n=wr97NKZIObCJm0cR&q=85&s=4d021170bd60f2e52fcb7bc0d3eb0552)![dark logo](https://mintcdn.com/chroma-8943dec5/wr97NKZIObCJm0cR/images/dark-logo.svg?fit=max&auto=format&n=wr97NKZIObCJm0cR&q=85&s=a6f162fa88876846a979771be29f2a13)](https://docs.trychroma.com/)
Search...
Ctrl KAsk AI
  * [Dashboard](https://trychroma.com/login)
  * [Dashboard](https://trychroma.com/login)


Search...
Navigation
Querying Collections
Metadata Filtering
[](https://docs.trychroma.com/docs/overview/introduction)[](https://docs.trychroma.com/cloud/getting-started)[](https://docs.trychroma.com/guides/build/building-with-ai)[](https://docs.trychroma.com/integrations/chroma-integrations)[](https://docs.trychroma.com/reference/overview)
##### Overview
  * [Introduction](https://docs.trychroma.com/docs/overview/introduction)
  * [Getting Started](https://docs.trychroma.com/docs/overview/getting-started)
  * [Architecture](https://docs.trychroma.com/docs/overview/architecture)
  * [Open Source](https://docs.trychroma.com/docs/overview/oss)
  * [Migration](https://docs.trychroma.com/docs/overview/migration)
  * [Troubleshooting](https://docs.trychroma.com/docs/overview/troubleshooting)


##### Run Chroma
  * [Chroma Clients](https://docs.trychroma.com/docs/run-chroma/clients)
  * [Client-Server Mode](https://docs.trychroma.com/docs/run-chroma/client-server)


##### Collections
  * [Manage Collections](https://docs.trychroma.com/docs/collections/manage-collections)
  * [Add Data](https://docs.trychroma.com/docs/collections/add-data)
  * [Update Data](https://docs.trychroma.com/docs/collections/update-data)
  * [Delete Data](https://docs.trychroma.com/docs/collections/delete-data)
  * [Configure Collections](https://docs.trychroma.com/docs/collections/configure)


##### Querying Collections
  * [Query and Get](https://docs.trychroma.com/docs/querying-collections/query-and-get)
  * [Metadata Filtering](https://docs.trychroma.com/docs/querying-collections/metadata-filtering)
  * [Full Text Search](https://docs.trychroma.com/docs/querying-collections/full-text-search)


##### Embeddings
  * [Embedding Functions](https://docs.trychroma.com/docs/embeddings/embedding-functions)
  * [Multimodal Embeddings](https://docs.trychroma.com/docs/embeddings/multimodal)


##### CLI
  * [Installing the CLI](https://docs.trychroma.com/docs/cli/install)
  * [Browse Collections](https://docs.trychroma.com/docs/cli/browse)
  * [Copy Collections](https://docs.trychroma.com/docs/cli/copy)
  * [DB Management](https://docs.trychroma.com/docs/cli/db)
  * [Sample Apps](https://docs.trychroma.com/docs/cli/sample-apps)
  * [Login](https://docs.trychroma.com/docs/cli/login)
  * [Profile Management](https://docs.trychroma.com/docs/cli/profile)
  * [Run a Chroma Server](https://docs.trychroma.com/docs/cli/run)
  * [Update](https://docs.trychroma.com/docs/cli/update)
  * [Vacuum](https://docs.trychroma.com/docs/cli/vacuum)


On this page
  * [Using Logical Operators](https://docs.trychroma.com/docs/querying-collections/metadata-filtering#using-logical-operators)
  * [Using Inclusion Operators](https://docs.trychroma.com/docs/querying-collections/metadata-filtering#using-inclusion-operators)
  * [Using Array Metadata](https://docs.trychroma.com/docs/querying-collections/metadata-filtering#using-array-metadata)
  * [Adding Array Metadata](https://docs.trychroma.com/docs/querying-collections/metadata-filtering#adding-array-metadata)
  * [Filtering with $contains and $not_contains](https://docs.trychroma.com/docs/querying-collections/metadata-filtering#filtering-with-%24contains-and-%24not_contains)
  * [Supported Array Types](https://docs.trychroma.com/docs/querying-collections/metadata-filtering#supported-array-types)
  * [Combining with Document Search](https://docs.trychroma.com/docs/querying-collections/metadata-filtering#combining-with-document-search)


Querying Collections
# Metadata Filtering
Copy page
Learn how to filter query results by metadata in Chroma collections.
Copy page
The `where` argument in `get` and `query` is used to filter records by their metadata. For example, in this `query` operation, Chroma will only query records that have the `page` metadata field with the value `10`:
Python
TypeScript
Rust
Report incorrect code
Copy
Ask AI
```
collection.query(
    query_texts=["first query", "second query"],
    where={"page": 10}
)

```

In order to filter on metadata, you must supply a `where` filter dictionary to the query. The dictionary must have the following structure:
Python
TypeScript
Rust
Report incorrect code
Copy
Ask AI
```
{
    "metadata_field": {
        <Operator>: <Value>
    }
}

```

Using the `$eq` operator is equivalent to using the metadata field directly in your `where` filter.
Python
TypeScript
Rust
Report incorrect code
Copy
Ask AI
```
{
    "metadata_field": "search_string"
}

# is equivalent to

{
    "metadata_field": {
        "$eq": "search_string"
    }
}

```

For example, here we query all records whose `page` metadata field is greater than 10:
Python
TypeScript
Rust
Report incorrect code
Copy
Ask AI
```
collection.query(
    query_texts=["first query", "second query"],
    where={"page": { "$gt": 10 }}
)

```

##
[​](https://docs.trychroma.com/docs/querying-collections/metadata-filtering#using-logical-operators)
Using Logical Operators
You can also use the logical operators `$and` and `$or` to combine multiple filters. An `$and` operator will return results that match all the filters in the list.
Python
TypeScript
Rust
Report incorrect code
Copy
Ask AI
```
{
    "$and": [
        {
            "metadata_field": {
                <Operator>: <Value>
            }
        },
        {
            "metadata_field": {
                <Operator>: <Value>
            }
        }
    ]
}

```

For example, here we query all records whose `page` metadata field is between 5 and 10:
Python
TypeScript
Rust
Report incorrect code
Copy
Ask AI
```
collection.query(
    query_texts=["first query", "second query"],
    where={
        "$and": [
            {"page": {"$gte": 5 }},
            {"page": {"$lte": 10 }},
        ]
    }
)

```

An `$or` operator will return results that match any of the filters in the list.
Python
TypeScript
Rust
Report incorrect code
Copy
Ask AI
```
{
    "$or": [
        {
            "metadata_field": {
                <Operator>: <Value>
            }
        },
        {
            "metadata_field": {
                <Operator>: <Value>
            }
        }
    ]
}

```

For example, here we get all records whose `color` metadata field is `red` or `blue`:
Python
TypeScript
Rust
Report incorrect code
Copy
Ask AI
```
collection.get(
    where={
        "$or": [
            {"color": "red"},
            {"color": "blue"},
        ]
    }
)

```

##
[​](https://docs.trychroma.com/docs/querying-collections/metadata-filtering#using-inclusion-operators)
Using Inclusion Operators
The following inclusion operators are supported:
  * `$in` - a value is in predefined list (string, int, float, bool)
  * `$nin` - a value is not in predefined list (string, int, float, bool)

An `$in` operator will return results where the metadata attribute is part of a provided list:
Python
TypeScript
Rust
Report incorrect code
Copy
Ask AI
```
{
  "metadata_field": {
    "$in": ["value1", "value2", "value3"]
  }
}

```

An `$nin` operator will return results where the metadata attribute is not part of a provided list (or the attribute’s key is not present):
Python
TypeScript
Rust
Report incorrect code
Copy
Ask AI
```
{
  "metadata_field": {
    "$nin": ["value1", "value2", "value3"]
  }
}

```

For example, here we get all records whose `author` metadata field is in a list of possible values:
Python
TypeScript
Rust
Report incorrect code
Copy
Ask AI
```
collection.get(
    where={
       "author": {"$in": ["Rowling", "Fitzgerald", "Herbert"]}
    }
)

```

##
[​](https://docs.trychroma.com/docs/querying-collections/metadata-filtering#using-array-metadata)
Using Array Metadata
Chroma supports storing arrays of values in metadata fields. You can use the `$contains` and `$not_contains` operators to filter records based on whether an array field includes a specific value.
###
[​](https://docs.trychroma.com/docs/querying-collections/metadata-filtering#adding-array-metadata)
Adding Array Metadata
Metadata arrays can contain strings, integers, floats, or booleans. All elements in an array must be the same type.
Python
TypeScript
Rust
Report incorrect code
Copy
Ask AI
```
collection.add(
    ids=["m1", "m2", "m3"],
    embeddings=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
    metadatas=[
        {"genres": ["action", "comedy"], "year": 2020},
        {"genres": ["drama"], "year": 2021},
        {"genres": ["action", "thriller"], "year": 2022},
    ],
)

```

###
[​](https://docs.trychroma.com/docs/querying-collections/metadata-filtering#filtering-with-$contains-and-$not_contains)
Filtering with `$contains` and `$not_contains`
Use `$contains` to check if a metadata array includes a specific scalar value, and `$not_contains` to check that it does not.
Python
TypeScript
Rust
Report incorrect code
Copy
Ask AI
```
# Get all records where genres contains "action"
collection.get(
    where={"genres": {"$contains": "action"}}
)

# Get all records where genres does NOT contain "action"
collection.get(
    where={"genres": {"$not_contains": "action"}}
)

# Works with integer arrays too
collection.get(
    where={"scores": {"$contains": 20}}
)

# Combine with other filters
collection.get(
    where={
        "$and": [
            {"genres": {"$contains": "action"}},
            {"year": {"$gte": 2021}},
        ]
    }
)

```

###
[​](https://docs.trychroma.com/docs/querying-collections/metadata-filtering#supported-array-types)
Supported Array Types
Type | Python | TypeScript | Rust
---|---|---|---
String | `["a", "b"]` | `["a", "b"]` | `MetadataValue::StringArray(...)`
Integer | `[1, 2, 3]` | `[1, 2, 3]` | `MetadataValue::IntArray(...)`
Float | `[1.5, 2.5]` | `[1.5, 2.5]` | `MetadataValue::FloatArray(...)`
Boolean | `[true, false]` | `[true, false]` | `MetadataValue::BoolArray(...)`
**Constraints:**
  * All elements in an array must be the same type.
  * Empty arrays are not allowed.
  * Nested arrays (arrays of arrays) are not supported.
  * The `$contains` value must be a scalar that matches the array’s element type.


##
[​](https://docs.trychroma.com/docs/querying-collections/metadata-filtering#combining-with-document-search)
Combining with Document Search
`.get` and `.query` can handle metadata filtering combined with [document search](https://docs.trychroma.com/docs/querying-collections/full-text-search):
Python
TypeScript
Rust
Report incorrect code
Copy
Ask AI
```
collection.query(
    query_texts=["doc10", "thus spake zarathustra", ...],
    n_results=10,
    where={"metadata_field": "is_equal_to_this"},
    where_document={"$contains":"search_string"}
)

```

Was this page helpful?
YesNo
[ Query and Get Previous ](https://docs.trychroma.com/docs/querying-collections/query-and-get)[ Full Text Search Next ](https://docs.trychroma.com/docs/querying-collections/full-text-search)
Ctrl+I
[Chroma Docs home page![light logo](https://mintcdn.com/chroma-8943dec5/wr97NKZIObCJm0cR/images/light-logo.svg?fit=max&auto=format&n=wr97NKZIObCJm0cR&q=85&s=4d021170bd60f2e52fcb7bc0d3eb0552)![dark logo](https://mintcdn.com/chroma-8943dec5/wr97NKZIObCJm0cR/images/dark-logo.svg?fit=max&auto=format&n=wr97NKZIObCJm0cR&q=85&s=a6f162fa88876846a979771be29f2a13)](https://docs.trychroma.com/)
[Enterprise](https://trychroma.com/enterprise)[Pricing](https://trychroma.com/pricing)[Changelog](https://trychroma.com/changelog)
Assistant
Responses are generated using AI and may contain mistakes.
