# Always Encrypted
Feedback
Summarize this article for me
##  In this article
  1. [Configure Always Encrypted](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-database-engine?view=sql-server-ver17#configure-always-encrypted)
  2. [Limitations](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-database-engine?view=sql-server-ver17#limitations)
  3. [Always Encrypted Transact-SQL reference](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-database-engine?view=sql-server-ver17#always-encrypted-transact-sql-reference)
  4. [Next step](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-database-engine?view=sql-server-ver17#next-step)
  5. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-database-engine?view=sql-server-ver17#related-content)


**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Database](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to)
![Diagram of Always Encrypted.](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/media/always-encrypted-database-engine/always-encrypted.png?view=sql-server-ver17)
Always Encrypted and [Always Encrypted with secure enclaves](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-enclaves?view=sql-server-ver17) are features designed to safeguard sensitive information, including credit card numbers and national or regional identification numbers (such as U.S. social security numbers), in Azure SQL Database, Azure SQL Managed Instance, and SQL Server databases. You can encrypt sensitive data within client applications, ensuring that encryption keys are never exposed to the Database Engine. This approach provides a separation between those who own the data and can view it, and those who manage the data but should have no access: on-premises database administrators, cloud database operators, or other high-privileged unauthorized users. As a result, Always Encrypted allows customers to securely store their sensitive data in the cloud, reducing the risk of data theft by malicious insiders.
Always Encrypted has certain restrictions, such as the inability to perform operations on encrypted data, including sorting and filtering (except for point-lookups using deterministic encryption). This limitation means that some queries and applications might not be compatible with Always Encrypted or might require significant changes to the application logic.
To address these limitations, [Always Encrypted with secure enclaves](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-enclaves?view=sql-server-ver17) enables the database engine to process encrypted data within a protected memory area called a secure enclave. Secure enclaves enhance the confidential computing capabilities of Always Encrypted by supporting pattern matching, various comparison operators, and in-place encryption.
Always Encrypted ensures that encryption is seamless for applications. On the client, the Always Encrypted-enabled driver encrypts sensitive data before sending it to the Database Engine and automatically rewrites queries to maintain application semantics. It also automatically decrypts query results from encrypted database columns.
[](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-database-engine?view=sql-server-ver17#configure-always-encrypted)
## Configure Always Encrypted
For applications that need to perform pattern matching, use comparison operators, sort, and index on encrypted columns, implement [Always Encrypted with secure enclaves](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-enclaves?view=sql-server-ver17).
This section provides an overview of setting up Always Encrypted. For details and to get started, see [Tutorial: Getting started with Always Encrypted](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-tutorial-getting-started?view=sql-server-ver17).
To configure Always Encrypted in your database, follow these steps:
  1. **Provision cryptographic keys to protect your data**. Always Encrypted uses two types of keys:
     * Column encryption keys.
     * Column master keys.
A column encryption key encrypts the data within an encrypted column. A column master key is a key-protecting key that encrypts one or more column encryption keys.
Store column master keys in a trusted key store outside of the database system, such as [Azure Key Vault](https://learn.microsoft.com/en-us/azure/key-vault/general/basic-concepts), [Windows certificate store](https://learn.microsoft.com/en-us/windows-hardware/drivers/install/local-machine-and-current-user-certificate-stores), or a hardware security module. After this step, provision column encryption keys and encrypt each key with a column master key.
Finally, save the metadata about the keys in your database. The column master key metadata includes the location of the column master key. The column encryption key metadata contains the encrypted value of the column encryption key. The Database Engine doesn't store or use any keys in plaintext.
For more information on managing Always Encrypted keys, see [Overview of key management for Always Encrypted](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/overview-of-key-management-for-always-encrypted?view=sql-server-ver17).
  2. **Set up encryption for specific database columns** that include sensitive information to ensure protection. This step might require creating new tables with encrypted columns or encrypting the existing columns and data. When configuring encryption for a column, specify details about the encryption algorithm, the column encryption key to safeguard the data, and the type of encryption. Always Encrypted supports two types of encryption:
     * **Deterministic encryption** always generates the same encrypted value for a given plaintext value. By using deterministic encryption, you can perform point lookups, equality joins, grouping, and indexing on encrypted columns. However, unauthorized users might guess information about encrypted values by examining patterns in the encrypted column, especially if there's a small set of possible encrypted values, such as True/False, or North/South/East/West region.
     * **Randomized encryption** uses a method that encrypts data unpredictably. Each identical plaintext input results in a distinct encrypted output. This method improves the security of randomized encryption.


To perform pattern matching by using comparison operators, sorting, and indexing on encrypted columns, adopt [Always Encrypted with secure enclaves](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-enclaves?view=sql-server-ver17) and apply randomized encryption. Always Encrypted (_without secure enclaves_) randomized encryption doesn't support searching, grouping, indexing, or joining on encrypted columns. Instead, for columns intended for search or grouping purposes, you must use deterministic encryption. This encryption type allows operations such as point lookups, equality joins, grouping, and indexing on encrypted columns.
Since the database system by design has no access to cryptographic keys, any column encryption requires moving and encrypting data outside of the database. The encryption process can take a long time and is vulnerable to network interruptions. Additionally, if you need to re-encrypt a column later, such as when rotating the encryption key or changing encryption types, you encounter the same difficulties again. Using [Always Encrypted with secure enclaves](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-enclaves?view=sql-server-ver17) eliminates the necessity of moving data out of the database. Because the enclave is trusted, a client driver within your application or a tool like SQL Server Management Studio (SSMS) can safely share the keys with the enclave during cryptographic operations. The enclave can then encrypt or re-encrypt columns in place, significantly decreasing the time required for these actions.
For details on Always Encrypted cryptographic algorithms, see [Always Encrypted cryptography](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-cryptography?view=sql-server-ver17).
You can perform the preceding steps by using [SQL tools](https://learn.microsoft.com/en-us/sql/tools/overview-sql-tools?view=sql-server-ver17):
  * [Provision Always Encrypted keys using SQL Server Management Studio](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/configure-always-encrypted-keys-using-ssms?view=sql-server-ver17)
  * [Configure Always Encrypted using PowerShell](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/configure-always-encrypted-using-powershell?view=sql-server-ver17)
  * [sqlpackage](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/configure-always-encrypted-using-dacpac?view=sql-server-ver17) - which automate the setup process


To ensure Always Encrypted keys and protected sensitive data are never revealed in plaintext to the database environment, the Database Engine can't be involved in key provisioning and data encryption or decryption operations. Therefore, Transact-SQL (T-SQL) doesn't support key provisioning or cryptographic operations. For the same reason, encrypting existing data or re-encrypting it (with a different encryption type or a column encryption key) needs to be performed outside of the database (SQL tools can automate that).
After changing the definition of an encrypted column, execute [sp_refresh_parameter_encryption](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-refresh-parameter-encryption-transact-sql?view=sql-server-ver17) to update the Always Encrypted metadata for the object.
[](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-database-engine?view=sql-server-ver17#limitations)
## Limitations
The following limitations apply to queries on encrypted columns:
  * You can't perform computations on columns encrypted with randomized encryption. Deterministic encryption supports the following operations that involve equality comparisons. No other operations are allowed:
    * [= (Equals) (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/language-elements/equals-transact-sql?view=sql-server-ver17) in point lookup searches.
    * [IN (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/language-elements/in-transact-sql?view=sql-server-ver17).
    * [SELECT - GROUP BY- Transact-SQL](https://learn.microsoft.com/en-us/sql/t-sql/queries/select-group-by-transact-sql?view=sql-server-ver17).
    * [DISTINCT](https://learn.microsoft.com/en-us/sql/t-sql/queries/select-transact-sql?view=sql-server-ver17#c-using-distinct-with-select).
For applications that need to perform pattern matching, use comparison operators, sort, and index on encrypted columns, implement [Always Encrypted with secure enclaves](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-enclaves?view=sql-server-ver17).
  * You can't use query statements that trigger computations involving both plaintext and encrypted data. For example:
    * Comparing an encrypted column to a plaintext column or a literal.
    * Copying data from a plaintext column to an encrypted column (or the other way around) `UPDATE`, `BULK INSERT`, `SELECT INTO`, or `INSERT..SELECT`.
    * Inserting literals to encrypted columns.
Such statements result in operand clash errors like this:
Output
Copy
```
Msg 206, Level 16, State 2, Line 89
    Operand type clash: char(11) encrypted with (encryption_type = 'DETERMINISTIC', encryption_algorithm_name = 'AEAD_AES_256_CBC_HMAC_SHA_256', column_encryption_key_name = 'CEK_1', column_encryption_key_database_name = 'ssn') collation_name = 'Latin1_General_BIN2' is incompatible with char

```

Applications need to use query parameters to provide values for encrypted columns. For example, when you're inserting data into encrypted columns or filtering them by using deterministic encryption, use query parameters. Passing literals or T-SQL variables that correspond to encrypted columns isn't supported. For more information specific to a client driver you're using, see [Develop applications using Always Encrypted](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-client-development?view=sql-server-ver17).
In [SSMS](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-query-columns-ssms?view=sql-server-ver17#param), it's essential to apply parameterization for Always Encrypted variables to execute queries that handle values associated with encrypted columns. This requirement includes scenarios such as inserting data into encrypted columns or applying filters on them (in cases where deterministic encryption is used).
  * [Table-valued parameters](https://learn.microsoft.com/en-us/sql/relational-databases/tables/use-table-valued-parameters-database-engine?view=sql-server-ver17) targeting encrypted columns aren't supported.
  * Queries that use the following clauses aren't supported:
    * [FOR XML (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/xml/for-xml-sql-server?view=sql-server-ver17)
    * [Format query results as JSON with FOR JSON](https://learn.microsoft.com/en-us/sql/relational-databases/json/format-query-results-as-json-with-for-json-sql-server?view=sql-server-ver17)
  * Always Encrypted isn't supported for the columns with the following characteristics:
    * Columns using one of the following data types: **xml** , **timestamp** , **rowversion** , **image** , **ntext** , **text** , **sql_variant** , **hierarchyid** , **geography** , **geometry** , **vector** , alias, user-defined types.
    * [FILESTREAM](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-table-transact-sql?view=sql-server-ver17#filestream) columns.
    * Columns with the [IDENTITY](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-table-transact-sql?view=sql-server-ver17#identity) property.
    * Columns with [ROWGUIDCOL](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-table-transact-sql?view=sql-server-ver17#rowguidcol) property.
    * String (**varchar** , **char** , and other) columns with collations other than [binary-code point (`_BIN2`) collations](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17). Collation must not differ from the database's default collation.
    * Columns that are keys for clustered and nonclustered indices when using randomized encryption (indices on columns using deterministic encryption are supported).
    * Columns included in full-text indexes (Always Encrypted doesn't support [Full-Text Search](https://learn.microsoft.com/en-us/sql/relational-databases/search/full-text-search?view=sql-server-ver17)).
    * [Specify computed columns in a table](https://learn.microsoft.com/en-us/sql/relational-databases/tables/specify-computed-columns-in-a-table?view=sql-server-ver17).
    * Columns referenced by computed columns when the expression does unsupported operations for Always Encrypted.
    * [Use sparse columns](https://learn.microsoft.com/en-us/sql/relational-databases/tables/use-sparse-columns?view=sql-server-ver17).
    * Columns that are referenced by [statistics](https://learn.microsoft.com/en-us/sql/relational-databases/statistics/statistics?view=sql-server-ver17) when using randomized encryption (deterministic encryption is supported).
    * [Partitioning columns](https://learn.microsoft.com/en-us/sql/relational-databases/partitions/partitioned-tables-and-indexes?view=sql-server-ver17#partitioning-column).
    * Columns with [default constraints](https://learn.microsoft.com/en-us/sql/relational-databases/tables/specify-default-values-for-columns?view=sql-server-ver17).
    * Columns referenced by [unique constraints](https://learn.microsoft.com/en-us/sql/relational-databases/tables/create-unique-constraints?view=sql-server-ver17) when using randomized encryption (deterministic encryption is supported).
    * Primary key columns when using randomized encryption (deterministic encryption is supported).
    * Referencing columns in [foreign key constraints](https://learn.microsoft.com/en-us/sql/relational-databases/tables/create-foreign-key-relationships?view=sql-server-ver17) when using randomized encryption or when using deterministic encryption, if the referenced and referencing columns use different keys or algorithms.
    * Columns referenced by [check constraints](https://learn.microsoft.com/en-us/sql/relational-databases/system-information-schema-views/check-constraints-transact-sql?view=sql-server-ver17).
      * Columns captured or tracked using [change data capture](https://learn.microsoft.com/en-us/sql/relational-databases/track-changes/about-change-data-capture-sql-server?view=sql-server-ver17).
    * Primary key columns on tables that have [change tracking](https://learn.microsoft.com/en-us/sql/relational-databases/track-changes/about-change-tracking-sql-server?view=sql-server-ver17).
      * Columns that are masked using [Dynamic data masking](https://learn.microsoft.com/en-us/sql/relational-databases/security/dynamic-data-masking?view=sql-server-ver17).
    * When a column in a [memory-optimized table](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/introduction-to-memory-optimized-tables?view=sql-server-ver17) is referenced in a [natively compiled module](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/creating-natively-compiled-stored-procedures?view=sql-server-ver17), encryption can't be applied to any of the columns in that table.
      * Columns in [stretch database tables](https://learn.microsoft.com/en-us/previous-versions/sql/sql-server/stretch-database/stretch-database). (Tables with columns encrypted with Always Encrypted can be enabled for Stretch.)
Stretch Database is deprecated in SQL Server 2022 (16.x) and Azure SQL Database. This feature will be removed in a future version of the Database Engine. Avoid using this feature in new development work, and plan to modify applications that currently use this feature.
    * Columns in external (PolyBase) tables (note: using external tables and tables with encrypted columns in the same query is supported).
  * The following features don't work on encrypted columns:
    * [SQL Server Replication](https://learn.microsoft.com/en-us/sql/relational-databases/replication/sql-server-replication?view=sql-server-ver17) (transactional, merge, or snapshot replication). Physical replication features, including [Always On availability groups](https://learn.microsoft.com/en-us/sql/database-engine/availability-groups/windows/overview-of-always-on-availability-groups-sql-server?view=sql-server-ver17), are supported.
    * Distributed queries ([linked servers](https://learn.microsoft.com/en-us/sql/relational-databases/linked-servers/linked-servers-database-engine?view=sql-server-ver17), [OPENROWSET (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/functions/openrowset-transact-sql?view=sql-server-ver17), [OPENDATASOURCE (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/functions/opendatasource-transact-sql?view=sql-server-ver17)).
    * [Cross-Database Queries](https://learn.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/cross-database-queries?view=sql-server-ver17) that perform joins on columns that are encrypted from different databases.


[](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-database-engine?view=sql-server-ver17#always-encrypted-transact-sql-reference)
## Always Encrypted Transact-SQL reference
Always Encrypted uses the following Transact-SQL statements, system catalog views, system stored procedures, and permissions.
[](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-database-engine?view=sql-server-ver17#statements)
### Statements
Expand table
DDL statement | Description
---|---
[CREATE COLUMN MASTER KEY](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-column-master-key-transact-sql?view=sql-server-ver17) | Creates a column master key metadata object in a database
[DROP COLUMN MASTER KEY](https://learn.microsoft.com/en-us/sql/t-sql/statements/drop-column-master-key-transact-sql?view=sql-server-ver17) | Drops a column master key from a database.
[CREATE COLUMN ENCRYPTION KEY](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-column-encryption-key-transact-sql?view=sql-server-ver17) | Creates a column encryption key metadata object.
[ALTER COLUMN ENCRYPTION KEY](https://learn.microsoft.com/en-us/sql/t-sql/statements/alter-column-encryption-key-transact-sql?view=sql-server-ver17) | Alters a column encryption key in a database, adding or dropping an encrypted value.
[DROP COLUMN ENCRYPTION KEY](https://learn.microsoft.com/en-us/sql/t-sql/statements/drop-column-encryption-key-transact-sql?view=sql-server-ver17) | Drops a column encryption key from a database.
[CREATE TABLE (ENCRYPTED WITH)](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-table-transact-sql?view=sql-server-ver17#encrypted-with) | Specifies encrypting columns
[](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-database-engine?view=sql-server-ver17#system-catalog-views-and-stored-procedures)
### System catalog views and stored procedures
Expand table
System catalog views and stored procedures | Description
---|---
[sys.column_encryption_keys](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-column-encryption-keys-transact-sql?view=sql-server-ver17) | Returns information about column encryption keys (CEKs)
[sys.column_encryption_key_values](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-column-encryption-key-values-transact-sql?view=sql-server-ver17) | Returns information about encrypted values of column encryption keys (CEKs)
[sys.column_master_keys](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-column-master-keys-transact-sql?view=sql-server-ver17) | Returns a row for each database master key
[sp_refresh_parameter_encryption](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-refresh-parameter-encryption-transact-sql?view=sql-server-ver17) | Updates the Always Encrypted metadata for the parameters of the specified non-schema-bound stored procedure, user-defined function, view, DML trigger, database-level DDL trigger, or server-level DDL trigger
[sp_describe_parameter_encryption](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-describe-parameter-encryption-transact-sql?view=sql-server-ver17) | Analyses the specified Transact-SQL statement and its parameters, to determine which parameters correspond to database columns that are protected by using the Always Encrypted feature.
For information on encryption metadata stored for each column, see [sys.columns](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-columns-transact-sql?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-database-engine?view=sql-server-ver17#database-permissions)
### Database permissions
Always Encrypted uses four database permissions.
Expand table
System catalog views and stored procedures | Description
---|---
`ALTER ANY COLUMN MASTER KEY` | Required to create and delete column master key metadata.
`ALTER ANY COLUMN ENCRYPTION KEY` | Required to create and delete column encryption key metadata.
`VIEW ANY COLUMN MASTER KEY DEFINITION` | Required to access and read the column master key metadata, which is needed to query encrypted columns.
`VIEW ANY COLUMN ENCRYPTION KEY DEFINITION` | Required to access and read the column encryption key metadata, which is needed to query encrypted columns.
The following table summarizes the permissions required for common actions.
Expand table
Scenario | `ALTER ANY COLUMN MASTER KEY` | `ALTER ANY COLUMN ENCRYPTION KEY` | `VIEW ANY COLUMN MASTER KEY DEFINITION` | `VIEW ANY COLUMN ENCRYPTION KEY DEFINITION`
---|---|---|---|---
Key management (creating, changing, or reviewing key metadata in the database) | X | X | X | X
Querying encrypted columns |  |  | X | X
[](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-database-engine?view=sql-server-ver17#important-considerations)
#### Important considerations
  * The `VIEW ANY COLUMN MASTER KEY DEFINITION` and `VIEW ANY COLUMN ENCRYPTION KEY DEFINITION` permissions are required when selecting encrypted columns. These permissions protect the columns even if the user doesn't have permission to the column master keys in their key stores, and they prevent access to plaintext.
  * In SQL Server, the **public** fixed database role grants both `VIEW ANY COLUMN MASTER KEY DEFINITION` and `VIEW ANY COLUMN ENCRYPTION KEY DEFINITION` permissions by default. A database administrator might choose to revoke or deny these permissions to the **public** role and grant them to specific roles or users to implement more restricted control.
  * In SQL Database, the **public** fixed database role doesn't grant the `VIEW ANY COLUMN MASTER KEY DEFINITION` and `VIEW ANY COLUMN ENCRYPTION KEY DEFINITION` permissions by default. This change enables certain existing legacy tools that use older versions of DacFx to work properly. To work with encrypted columns (even if not decrypting them), a database administrator must explicitly grant the `VIEW ANY COLUMN MASTER KEY DEFINITION` and `VIEW ANY COLUMN ENCRYPTION KEY DEFINITION` permissions.


[](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-database-engine?view=sql-server-ver17#next-step)
## Next step
[Tutorial: Getting started with Always Encrypted](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-tutorial-getting-started?view=sql-server-ver17)
[](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-database-engine?view=sql-server-ver17#related-content)
## Related content
  * [Always Encrypted documentation](https://learn.microsoft.com/en-us/azure/azure-sql/database/always-encrypted-landing)


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
  * [ Always Encrypted cryptography - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-cryptography?source=recommendations)
Learn about encryption algorithms and mechanisms that derive cryptographic material in the Always Encrypted feature in SQL Server and Azure SQL Database.
  * [ Tutorial: Getting started with Always Encrypted - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-tutorial-getting-started?source=recommendations)
This tutorial teaches you how to encrypt columns using Always Encrypted and how to query encrypted columns in SQL Server, Azure SQL Database, and Azure SQL Managed Instance.
  * [ Overview of key management for Always Encrypted - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/overview-of-key-management-for-always-encrypted?source=recommendations)
Learn how to manage the two types of cryptographic keys Always Encrypted uses to protect your data in SQL Server: column encryption key and column master key.
  * [ Always Encrypted - How queries against encrypted columns work - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-how-queries-against-encrypted-columns-work?source=recommendations)
Learn about how queries against encrypted columns work in the Always Encrypted feature in SQL Server and Azure SQL.
  * [ Query columns using Always Encrypted with SQL Server Management Studio - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-query-columns-ssms?source=recommendations)
Learn how to query columns in Always Encrypted using SQL Server Management Studio. Retrieve ciphertext or text values stored in encrypted columns.
  * [ Always Encrypted with secure enclaves - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-enclaves?source=recommendations)
Learn about the Always Encrypted with secure enclaves feature for SQL Server.
  * [ CREATE COLUMN MASTER KEY (Transact-SQL) - SQL Server ](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-column-master-key-transact-sql?source=recommendations)
CREATE COLUMN MASTER KEY (Transact-SQL)
  * [ Configure Column Encryption Using Always Encrypted Wizard - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-wizard?source=recommendations)
Learn how to set the Always Encrypted configuration for database columns by using the Always Encrypted Wizard in SQL Server.


Show 5 more
Module
[ Protect data in-transit and at rest - Training ](https://learn.microsoft.com/en-us/training/modules/protect-data-transit-rest/?source=recommendations)
Protect data in-transit and at rest
Certification
[ Microsoft Certified: Azure Database Administrator Associate - Certifications ](https://learn.microsoft.com/en-us/credentials/certifications/azure-database-administrator-associate/?source=recommendations)
Administer an SQL Server database infrastructure for cloud, on-premises and hybrid relational databases using the Microsoft PaaS relational database offerings.
Mar 8, 4 PM - Mar 8, 4 PM
Experiment with what's next in AI-driven apps and agent design
* * *
  * Last updated on 01/29/2026


##  In this article
  1. [Configure Always Encrypted](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-database-engine?view=sql-server-ver17#configure-always-encrypted)
  2. [Limitations](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-database-engine?view=sql-server-ver17#limitations)
  3. [Always Encrypted Transact-SQL reference](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-database-engine?view=sql-server-ver17#always-encrypted-transact-sql-reference)
  4. [Next step](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-database-engine?view=sql-server-ver17#next-step)
  5. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-database-engine?view=sql-server-ver17#related-content)


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
[ Sign in ](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-database-engine?view=sql-server-ver17)
[English (United States)](https://learn.microsoft.com/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fsql%2Frelational-databases%2Fsecurity%2Fencryption%2Falways-encrypted-database-engine%3Fview%3Dsql-server-ver17)
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
