# collection(name="my_collection", metadata={})
```

<ParamField type="str" />

<ParamField type="Optional[Schema]" />

<ParamField type="Optional[CreateCollectionConfiguration]" />

<ParamField type="Optional[Dict[str, Any]]" />

<ParamField type="Optional[EmbeddingFunction[Optional[Embeddings]]]" />

<ParamField type="Optional[DataLoader[Optional[Embeddings]]]" />

### delete\_collection

Delete a collection with the given name.

<ParamField type="str">
  The name of the collection to delete.
</ParamField>

**Raises:**

* ValueError: If the collection does not exist.

### reset

Resets the database. This will delete all collections and entries.

**Returns:** True if the database was reset successfully.

### get\_version

Get the version of Chroma.

**Returns:** The version of Chroma

### get\_settings

Get the settings used to initialize.

**Returns:** The settings used to initialize.

### get\_max\_batch\_size

Return the maximum number of records that can be created or mutated in a single call.

***

## Admin Client Methods

### create\_tenant

Create a new tenant. Raises an error if the tenant already exists.

<ParamField type="str" />

### get\_tenant

Get a tenant. Raises an error if the tenant does not exist.

<ParamField type="str" />

### create\_database

Create a new database. Raises an error if the database already exists.

<ParamField type="str" />

<ParamField type="str" />

### get\_database

Get a database. Raises an error if the database does not exist.

<ParamField type="str" />

<ParamField type="str">
  The tenant of the database to get.
</ParamField>

### delete\_database

Delete a database. Raises an error if the database does not exist.

<ParamField type="str" />

<ParamField type="str">
  The tenant of the database to delete.
</ParamField>

### list\_databases

List all databases for a tenant. Raises an error if the tenant does not exist.

<ParamField type="Optional[int]" />

<ParamField type="Optional[int]" />

<ParamField type="str">
  The tenant to list databases for.
</ParamField>
