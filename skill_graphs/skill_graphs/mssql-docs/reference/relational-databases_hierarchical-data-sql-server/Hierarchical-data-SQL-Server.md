# Hierarchical data (SQL Server)
Feedback
Summarize this article for me
##  In this article
  1. [Key properties](https://learn.microsoft.com/en-us/sql/relational-databases/hierarchical-data-sql-server?view=sql-server-ver17#key-properties)
  2. [Limitations](https://learn.microsoft.com/en-us/sql/relational-databases/hierarchical-data-sql-server?view=sql-server-ver17#limitations)
  3. [When to use alternatives to hierarchyid](https://learn.microsoft.com/en-us/sql/relational-databases/hierarchical-data-sql-server?view=sql-server-ver17#when-to-use-alternatives-to-hierarchyid)
  4. [Index strategies for hierarchical data](https://learn.microsoft.com/en-us/sql/relational-databases/hierarchical-data-sql-server?view=sql-server-ver17#index-strategies-for-hierarchical-data)
  5. [Examples](https://learn.microsoft.com/en-us/sql/relational-databases/hierarchical-data-sql-server?view=sql-server-ver17#examples)
  6. [Related tasks](https://learn.microsoft.com/en-us/sql/relational-databases/hierarchical-data-sql-server?view=sql-server-ver17#related-tasks)
  7. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/hierarchical-data-sql-server?view=sql-server-ver17#related-content)

Show 3 more
**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Database](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL database in Microsoft Fabric](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to)
The built-in **hierarchyid** data type makes it easier to store and query hierarchical data. **hierarchyid** is optimized for representing trees, which are the most common type of hierarchical data.
Hierarchical data is defined as a set of data items that are related to each other by hierarchical relationships. Hierarchical relationships exist where one item of data is the parent of another item. Examples of the hierarchical data that is commonly stored in databases include the following items:
  * An organizational structure
  * A file system
  * A set of tasks in a project
  * A taxonomy of language terms
  * A graph of links between Web pages


Use [hierarchyid](https://learn.microsoft.com/en-us/sql/t-sql/data-types/hierarchyid-data-type-method-reference?view=sql-server-ver17) as a data type to create tables with a hierarchical structure, or to describe the hierarchical structure of data that is stored in another location. Use the [hierarchyid functions](https://learn.microsoft.com/en-us/sql/t-sql/data-types/hierarchyid-data-type-method-reference?view=sql-server-ver17) in Transact-SQL to query and manage hierarchical data.
[](https://learn.microsoft.com/en-us/sql/relational-databases/hierarchical-data-sql-server?view=sql-server-ver17#key-properties)
## Key properties
A value of the **hierarchyid** data type represents a position in a tree hierarchy. Values for **hierarchyid** have the following properties:
  * Extremely compact
The average number of bits that are required to represent a node in a tree with _n_ nodes depends on the average fanout (the average number of children of a node). For small fanouts (0-7), the size is about $6log{A}{n}$ bits, where A is the average fanout. A node in an organizational hierarchy of 100,000 people with an average fanout of six levels takes about 38 bits. This is rounded up to 40 bits, or 5 bytes, for storage.
  * Comparison is in depth-first order
Given two **hierarchyid** values `a` and `b`, `a < b` means `a` comes before `b` in a depth-first traversal of the tree. Indexes on **hierarchyid** data types are in depth-first order, and nodes close to each other in a depth-first traversal are stored near each other. For example, the children of a record are stored next to that record.
  * Support for arbitrary insertions and deletions
By using the [GetDescendant (Database Engine)](https://learn.microsoft.com/en-us/sql/t-sql/data-types/getdescendant-database-engine?view=sql-server-ver17) method, it's always possible to generate a sibling to the right of any given node, to the left of any given node, or between any two siblings. The comparison property is maintained when an arbitrary number of nodes is inserted or deleted from the hierarchy. Most insertions and deletions preserve the compactness property. However, insertions between two nodes produce **hierarchyid** values with a slightly less compact representation.


[](https://learn.microsoft.com/en-us/sql/relational-databases/hierarchical-data-sql-server?view=sql-server-ver17#limitations)
## Limitations
The **hierarchyid** data type has the following limitations:
  * A column of type **hierarchyid** doesn't automatically represent a tree. It's up to the application to generate and assign **hierarchyid** values in such a way that the desired relationship between rows is reflected in the values. Some applications might have a column of type **hierarchyid** that indicates the location in a hierarchy defined in another table.
  * It's up to the application to manage concurrency in generating and assigning **hierarchyid** values. There's no guarantee that **hierarchyid** values in a column are unique unless the application uses a unique key constraint or enforces uniqueness itself through its own logic.
  * Hierarchical relationships represented by **hierarchyid** values aren't enforced like a foreign key relationship. It's possible, and sometimes appropriate, to have a hierarchical relationship where `A` has a child `B`, and then `A` is deleted leaving `B` with a relationship to a nonexistent record. If this behavior is unacceptable, the application must query for descendants before deleting parents.


[](https://learn.microsoft.com/en-us/sql/relational-databases/hierarchical-data-sql-server?view=sql-server-ver17#when-to-use-alternatives-to-hierarchyid)
## When to use alternatives to hierarchyid
Two alternatives to **hierarchyid** for representing hierarchical data are:
  * Parent/child
  * XML


**hierarchyid** is generally superior to these alternatives. However, there are specific situations, detailed in this article, where the alternatives are likely superior.
[](https://learn.microsoft.com/en-us/sql/relational-databases/hierarchical-data-sql-server?view=sql-server-ver17#parentchild)
### Parent/child
When you use the parent/child approach, each row contains a reference to the parent. The following table defines a typical table used to contain the parent and the child rows in a parent/child relationship:
SQL
Copy
```
USE AdventureWorks2022;
GO

CREATE TABLE ParentChildOrg (
    BusinessEntityID INT PRIMARY KEY,
    ManagerId INT FOREIGN KEY REFERENCES ParentChildOrg(BusinessEntityID),
    EmployeeName NVARCHAR(50)
);
GO

```

Comparing parent/child and **hierarchyid** for common operations:
  * Subtree queries are significantly faster with **hierarchyid**.
  * Direct descendant queries are slightly slower with **hierarchyid**.
  * Moving nonleaf nodes is slower with **hierarchyid**.
  * Inserting nonleaf nodes and inserting or moving leaf nodes has the same complexity with **hierarchyid**.


Parent/child might be superior when the following conditions exist:
  * The size of the key is critical. For the same number of nodes, a **hierarchyid** value is equal to or larger than an integer-family (**smallint** , **int** , **bigint**) value. This is only a reason to use parent/child in rare cases, because **hierarchyid** has significantly better locality of I/O and CPU complexity than the common table expressions required when you're using a parent/child structure.
  * Queries rarely query across sections of the hierarchy. In other words, queries usually address only a single point in the hierarchy. In these cases, colocation isn't important. For example, parent/child is superior when the organization table is only used to process payroll for individual employees.
  * Nonleaf subtrees move frequently and performance is very important. In a parent/child representation, changing the location of a row in a hierarchy affects a single row. Changing the location of a row in a **hierarchyid** usage affects _n_ rows, where _n_ is number of nodes in the subtree being moved.
If the nonleaf subtrees move frequently and performance is important, but most of the moves are at a well-defined level of the hierarchy, consider splitting the higher and lower levels into two hierarchies. This makes all moves into leaf-levels of the higher hierarchy. For instance, consider a hierarchy of Web sites hosted by a service. Sites contain many pages arranged in a hierarchical manner. Hosted sites might be moved to other locations in the site hierarchy, but the subordinate pages are rarely rearranged. This could be represented via:
SQL
Copy
```
CREATE TABLE HostedSites (
    SiteId HIERARCHYID,
    PageId HIERARCHYID
);
GO

```



[](https://learn.microsoft.com/en-us/sql/relational-databases/hierarchical-data-sql-server?view=sql-server-ver17#xml)
### XML
An XML document is a tree, and therefore a single XML data type instance can represent a complete hierarchy. In SQL Server when an XML index is created, **hierarchyid** values are used internally to represent the position in the hierarchy.
Using XML data type can be superior when all the following are true:
  * The complete hierarchy is always stored and retrieved.
  * The data is consumed in XML format by the application.
  * Predicate searches are extremely limited and not performance critical.


For example, if an application tracks multiple organizations, always stores and retrieves the complete organizational hierarchy, and doesn't query into a single organization, a table of the following form might make sense:
SQL
Copy
```
CREATE TABLE XMLOrg (
    Orgid INT,
    Orgdata XML
);
GO

```

[](https://learn.microsoft.com/en-us/sql/relational-databases/hierarchical-data-sql-server?view=sql-server-ver17#index-strategies-for-hierarchical-data)
## Index strategies for hierarchical data
There are two strategies for indexing hierarchical data:
  * **Depth-first**
A depth-first index stores the rows in a subtree near each other. For example, all employees that report through a manager are stored near their managers' record.
In a depth-first index, all nodes in the subtree of a node are colocated. Depth-first indexes are therefore efficient for answering queries about subtrees, such as: "Find all files in this folder and its subfolders"
  * **Breadth-first**
A breadth-first index stores the rows each level of the hierarchy together. For example, the records of employees who directly report to the same manager are stored near each other.
In a breadth-first index, all direct children of a node are colocated. Breadth-first indexes are therefore efficient for answering queries about immediate children, such as: "Find all employees who report directly to this manager"


Whether to have depth-first, breadth-first, or both, and which to make the clustering key (if any), depends on the relative importance of the above types of queries, and the relative importance of `SELECT` vs. DML operations. For a detailed example of indexing strategies, see [Tutorial: Using the hierarchyid Data Type](https://learn.microsoft.com/en-us/sql/relational-databases/tables/tutorial-using-the-hierarchyid-data-type?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/relational-databases/hierarchical-data-sql-server?view=sql-server-ver17#create-indexes)
### Create indexes
The GetLevel() method can be used to create a breadth first ordering. In the following example, both breadth-first and depth-first indexes are created:
SQL
Copy
```
USE AdventureWorks2022;
GO

CREATE TABLE Organization (
    BusinessEntityID HIERARCHYID,
    OrgLevel AS BusinessEntityID.GetLevel(),
    EmployeeName NVARCHAR(50) NOT NULL
);
GO

CREATE CLUSTERED INDEX Org_Breadth_First
ON Organization (OrgLevel, BusinessEntityID);
GO

CREATE UNIQUE INDEX Org_Depth_First
ON Organization (BusinessEntityID);
GO

```

[](https://learn.microsoft.com/en-us/sql/relational-databases/hierarchical-data-sql-server?view=sql-server-ver17#examples)
## Examples
The code samples in this article use the `AdventureWorks2025` or `AdventureWorksDW2025` sample database, which you can download from the [Microsoft SQL Server Samples and Community Projects](https://go.microsoft.com/fwlink/?LinkID=85384) home page.
[](https://learn.microsoft.com/en-us/sql/relational-databases/hierarchical-data-sql-server?view=sql-server-ver17#basic-example)
### Basic example
The following example is intentionally simplistic to help you get started. First create a table to hold some geography data.
SQL
Copy
```
CREATE TABLE BasicDemo (
    [Level] HIERARCHYID NOT NULL,
    Location NVARCHAR(30) NOT NULL,
    LocationType NVARCHAR(9) NULL
);

```

Now insert data for some continents, countries/regions, states, and cities.
SQL
Copy
```
INSERT BasicDemo
VALUES ('/1/', 'Europe', 'Continent'),
    ('/2/', 'South America', 'Continent'),
    ('/1/1/', 'France', 'Country'),
    ('/1/1/1/', 'Paris', 'City'),
    ('/1/2/1/', 'Madrid', 'City'),
    ('/1/2/', 'Spain', 'Country'),
    ('/3/', 'Antarctica', 'Continent'),
    ('/2/1/', 'Brazil', 'Country'),
    ('/2/1/1/', 'Brasilia', 'City'),
    ('/2/1/2/', 'Bahia', 'State'),
    ('/2/1/2/1/', 'Salvador', 'City'),
    ('/3/1/', 'McMurdo Station', 'City');

```

Select the data, adding a column that converts the Level data into a text value that is easy to understand. This query also orders the result by the **hierarchyid** data type.
SQL
Copy
```
SELECT CAST([Level] AS NVARCHAR(100)) AS [Converted Level],
    *
FROM BasicDemo
ORDER BY [Level];

```

Here's the result set.
Output
Copy
```
Converted Level  Level     Location         LocationType
---------------  --------  ---------------  ---------------
/1/              0x58      Europe           Continent
/1/1/            0x5AC0    France           Country
/1/1/1/          0x5AD6    Paris            City
/1/2/            0x5B40    Spain            Country
/1/2/1/          0x5B56    Madrid           City
/2/              0x68      South America    Continent
/2/1/            0x6AC0    Brazil           Country
/2/1/1/          0x6AD6    Brasilia         City
/2/1/2/          0x6ADA    Bahia            State
/2/1/2/1/        0x6ADAB0  Salvador         City
/3/              0x78      Antarctica       Continent
/3/1/            0x7AC0    McMurdo Station  City

```

The hierarchy has a valid structure, even though it isn't internally consistent. Bahia is the only state. It appears in the hierarchy as a peer of the city Brasilia. Similarly, McMurdo Station doesn't have a parent country/region. Users must decide if this type of hierarchy is appropriate for their use.
Add another row and select the results.
SQL
Copy
```
INSERT BasicDemo
VALUES ('/1/3/1/', 'Kyoto', 'City'),
    ('/1/3/1/', 'London', 'City');

SELECT CAST([Level] AS NVARCHAR(100)) AS [Converted Level],
    *
FROM BasicDemo
ORDER BY [Level];

```

This demonstrates more possible problems. Kyoto can be inserted as level `/1/3/1/` even though there's no parent level `/1/3/`. And both London and Kyoto have the same value for the **hierarchyid**. Again, users must decide if this type of hierarchy is appropriate for their use, and block values that are invalid for their usage.
Also, this table didn't use the top of the hierarchy `'/'`. It was omitted because there's no common parent of all the continents. You can add one by adding the whole planet.
SQL
Copy
```
INSERT BasicDemo
VALUES ('/', 'Earth', 'Planet');

```

[](https://learn.microsoft.com/en-us/sql/relational-databases/hierarchical-data-sql-server?view=sql-server-ver17#related-tasks)
## Related tasks
[](https://learn.microsoft.com/en-us/sql/relational-databases/hierarchical-data-sql-server?view=sql-server-ver17#migrate-from-parentchild-to-hierarchyid)
### Migrate from parent/child to hierarchyid
Most trees are represented using parent/child. The easiest way to migrate from a parent/child structure to a table using **hierarchyid** is to use a temporary column or a temporary table to keep track of the number of nodes at each level of the hierarchy. For an example of migrating a parent/child table, see lesson 1 of [Tutorial: Using the hierarchyid Data Type](https://learn.microsoft.com/en-us/sql/relational-databases/tables/tutorial-using-the-hierarchyid-data-type?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/relational-databases/hierarchical-data-sql-server?view=sql-server-ver17#manage-a-tree-using-hierarchyid)
### Manage a tree using hierarchyid
Although a **hierarchyid** column doesn't necessarily represent a tree, an application can easily ensure that it does.
  * When generating new values, do one of the following steps:
    * Keep track of the last child number in the parent row.
    * Compute the last child. Doing this efficiently requires a breadth-first index.
  * Enforce uniqueness by creating a unique index on the column, perhaps as part of a clustering key. To ensure that unique values are inserted, do one of the following steps:
    * Detect unique key violation failures and retry.
    * Determine the uniqueness of each new child node, and insert it as part of a serializable transaction.


[](https://learn.microsoft.com/en-us/sql/relational-databases/hierarchical-data-sql-server?view=sql-server-ver17#example-using-error-detection)
#### Example using error detection
In the following example, the sample code computes the new child `EmployeeId` value, and then detects any key violation and returns to `INS_EMP` marker to recompute the `EmployeeId` value for the new row:
SQL
Copy
```
USE AdventureWorks;
GO

CREATE TABLE Org_T1 (
    EmployeeId HIERARCHYID PRIMARY KEY,
    OrgLevel AS EmployeeId.GetLevel(),
    EmployeeName NVARCHAR(50)
);
GO

CREATE INDEX Org_BreadthFirst ON Org_T1 (
    OrgLevel,
    EmployeeId
);
GO

CREATE PROCEDURE AddEmp (
    @mgrid HIERARCHYID,
    @EmpName NVARCHAR(50)
)
AS
BEGIN
    DECLARE @last_child HIERARCHYID;

    INS_EMP:

    SELECT @last_child = MAX(EmployeeId)
    FROM Org_T1
    WHERE EmployeeId.GetAncestor(1) = @mgrid;

    INSERT INTO Org_T1 (EmployeeId, EmployeeName)
    SELECT @mgrid.GetDescendant(@last_child, NULL), @EmpName;

    -- On error, return to INS_EMP to recompute @last_child
    IF @@error <> 0
        GOTO INS_EMP
END;
GO

```

[](https://learn.microsoft.com/en-us/sql/relational-databases/hierarchical-data-sql-server?view=sql-server-ver17#example-using-a-serializable-transaction)
#### Example using a serializable transaction
The `Org_BreadthFirst` index ensures that determining `@last_child` uses a range seek. In addition to other error cases an application might want to check, a duplicate key violation after the insert indicates an attempt to add multiple employees with the same ID, and therefore `@last_child` must be recomputed. The following code computes the new node value within a serializable transaction:
SQL
Copy
```
CREATE TABLE Org_T2 (
    EmployeeId HIERARCHYID PRIMARY KEY,
    LastChild HIERARCHYID,
    EmployeeName NVARCHAR(50)
);
GO

CREATE PROCEDURE AddEmp (
    @mgrid HIERARCHYID,
    @EmpName NVARCHAR(50)
)
AS
BEGIN
    DECLARE @last_child HIERARCHYID;

    SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;

    BEGIN TRANSACTION;

    SELECT @last_child = EmployeeId.GetDescendant(LastChild, NULL)
    FROM Org_T2
    WHERE EmployeeId = @mgrid;

    UPDATE Org_T2
    SET LastChild = @last_child
    WHERE EmployeeId = @mgrid;

    INSERT Org_T2 (EmployeeId, EmployeeName)
    VALUES (@last_child, @EmpName);

    COMMIT;
END;

```

The following code populates the table with three rows and returns the results:
SQL
Copy
```
INSERT Org_T2 (EmployeeId, EmployeeName)
VALUES (HIERARCHYID::GetRoot(), 'David');
GO

EXECUTE AddEmp 0x, 'Sariya';
GO

EXECUTE AddEmp 0x58, 'Mary';
GO

SELECT * FROM Org_T2

```

Here's the result set.
Output
Copy
```
EmployeeId LastChild EmployeeName
---------- --------- ------------
0x        0x58       David
0x58      0x5AC0     Sariya
0x5AC0    NULL       Mary

```

[](https://learn.microsoft.com/en-us/sql/relational-databases/hierarchical-data-sql-server?view=sql-server-ver17#enforce-a-tree)
### Enforce a tree
The previous examples illustrate how an application can ensure that a tree is maintained. To enforce a tree by using constraints, a computed column that defines the parent of each node can be created with a foreign key constraint back to the primary key ID.
SQL
Copy
```
CREATE TABLE Org_T3 (
    EmployeeId HIERARCHYID PRIMARY KEY,
    ParentId AS EmployeeId.GetAncestor(1) PERSISTED FOREIGN KEY REFERENCES Org_T3(EmployeeId),
    LastChild HIERARCHYID,
    EmployeeName NVARCHAR(50)
);
GO

```

This method of enforcing a relationship is preferred when code that isn't trusted to maintain the hierarchical tree has direct DML access to the table. However this method might reduce performance because the constraint must be checked on every DML operation.
[](https://learn.microsoft.com/en-us/sql/relational-databases/hierarchical-data-sql-server?view=sql-server-ver17#find-ancestors-by-using-the-clr)
### Find ancestors by using the CLR
A common operation involving two nodes in a hierarchy is to find the lowest common ancestor. This task can be written in either Transact-SQL or CLR, because the **hierarchyid** type is available in both. CLR is recommended because performance is faster.
Use the following CLR code to list ancestors and to find the lowest common ancestor:
C#
Copy
```
using System;
using System.Collections;
using System.Text;
using Microsoft.SqlServer.Server; // SqlFunction Attribute
using Microsoft.SqlServer.Types;  // SqlHierarchyId

public partial class HierarchyId_Operations
{
    [SqlFunction(FillRowMethodName = "FillRow_ListAncestors")]
    public static IEnumerable ListAncestors(SqlHierarchyId h)
    {
        while (!h.IsNull)
        {
            yield return (h);
            h = h.GetAncestor(1);
        }
    }

    public static void FillRow_ListAncestors(
        Object obj,
        out SqlHierarchyId ancestor
    )
    {
        ancestor = (SqlHierarchyId)obj;
    }

    public static HierarchyId CommonAncestor(
        SqlHierarchyId h1,
        HierarchyId h2
    )
    {
        while (!h1.IsDescendantOf(h2))
        {
            h1 = h1.GetAncestor(1);
        }

        return h1;
    }
}

```

To use the `ListAncestor` and `CommonAncestor` methods in the following Transact-SQL examples, build the DLL and create the `HierarchyId_Operations` assembly in SQL Server by executing code similar to the following example:
SQL
Copy
```
CREATE ASSEMBLY HierarchyId_Operations
    FROM '<path to DLL>\ListAncestors.dll';
GO

```

[](https://learn.microsoft.com/en-us/sql/relational-databases/hierarchical-data-sql-server?view=sql-server-ver17#list-ancestors)
### List ancestors
Creating a list of ancestors of a node is a common operation, for instance to show position in an organization. One way of doing this is by using a table-valued-function using the `HierarchyId_Operations` class defined previously:
Using Transact-SQL:
SQL
Copy
```
CREATE FUNCTION ListAncestors (@node HIERARCHYID)
RETURNS TABLE (node HIERARCHYID)
AS
EXTERNAL NAME HierarchyId_Operations.HierarchyId_Operations.ListAncestors;
GO

```

Example of usage:
SQL
Copy
```
DECLARE @h AS HIERARCHYID;

SELECT @h = OrgNode
FROM HumanResources.EmployeeDemo
WHERE LoginID = 'adventure-works\janice0' -- /1/1/5/2/

SELECT LoginID,
    OrgNode.ToString() AS LogicalNode
FROM HumanResources.EmployeeDemo AS ED
INNER JOIN ListAncestors(@h) AS A
    ON ED.OrgNode = A.Node
GO

```

[](https://learn.microsoft.com/en-us/sql/relational-databases/hierarchical-data-sql-server?view=sql-server-ver17#find-the-lowest-common-ancestor)
### Find the lowest common ancestor
Using the `HierarchyId_Operations` class defined previously, create the following Transact-SQL function to find the lowest common ancestor involving two nodes in a hierarchy:
SQL
Copy
```
CREATE FUNCTION CommonAncestor (
    @node1 HIERARCHYID,
    @node2 HIERARCHYID
)
RETURNS HIERARCHYID
AS
EXTERNAL NAME HierarchyId_Operations.HierarchyId_Operations.CommonAncestor;
GO

```

Example of usage:
SQL
Copy
```
DECLARE @h1 AS HIERARCHYID, @h2 AS HIERARCHYID;

SELECT @h1 = OrgNode
FROM HumanResources.EmployeeDemo
WHERE LoginID = 'adventure-works\jossef0';-- Node is /1/1/3/

SELECT @h2 = OrgNode
FROM HumanResources.EmployeeDemo
WHERE LoginID = 'adventure-works\janice0';-- Node is /1/1/5/2/

SELECT OrgNode.ToString() AS LogicalNode, LoginID
FROM HumanResources.EmployeeDemo
WHERE OrgNode = dbo.CommonAncestor(@h1, @h2);

```

The resultant node is /1/1/
[](https://learn.microsoft.com/en-us/sql/relational-databases/hierarchical-data-sql-server?view=sql-server-ver17#move-subtrees)
### Move subtrees
Another common operation is moving subtrees. The following procedure takes the subtree of `@oldMgr` and makes it (including `@oldMgr`) a subtree of `@newMgr`.
SQL
Copy
```
CREATE PROCEDURE MoveOrg (
    @oldMgr NVARCHAR(256),
    @newMgr NVARCHAR(256)
)
AS
BEGIN
    DECLARE @nold HIERARCHYID, @nnew HIERARCHYID;

    SELECT @nold = OrgNode
    FROM HumanResources.EmployeeDemo
    WHERE LoginID = @oldMgr;

    SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;

    BEGIN TRANSACTION;

    SELECT @nnew = OrgNode
    FROM HumanResources.EmployeeDemo
    WHERE LoginID = @newMgr;

    SELECT @nnew = @nnew.GetDescendant(max(OrgNode), NULL)
    FROM HumanResources.EmployeeDemo
    WHERE OrgNode.GetAncestor(1) = @nnew;

    UPDATE HumanResources.EmployeeDemo
    SET OrgNode = OrgNode.GetReparentedValue(@nold, @nnew)
    WHERE OrgNode.IsDescendantOf(@nold) = 1;

    COMMIT TRANSACTION;
END;
GO

```

[](https://learn.microsoft.com/en-us/sql/relational-databases/hierarchical-data-sql-server?view=sql-server-ver17#related-content)
## Related content
  * [hierarchyid Data Type Method Reference](https://learn.microsoft.com/en-us/sql/t-sql/data-types/hierarchyid-data-type-method-reference?view=sql-server-ver17)
  * [Tutorial: Using the hierarchyid Data Type](https://learn.microsoft.com/en-us/sql/relational-databases/tables/tutorial-using-the-hierarchyid-data-type?view=sql-server-ver17)
  * [hierarchyid (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/data-types/hierarchyid-data-type-method-reference?view=sql-server-ver17)


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
  * [ Tables - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/tables/tables?source=recommendations)
Learn more about tables in the SQL Database Engine.
  * [ Databases - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/databases/databases?source=recommendations)
Learn about database schemas, tables, filegroups, logins, and roles. See how you can use the SQL Server Management Studio tool to work with databases.
  * [ Graph Processing - SQL Server and Azure SQL Database ](https://learn.microsoft.com/en-us/sql/relational-databases/graphs/sql-graph-overview?source=recommendations)
Graph processing with SQL Server and Azure SQL Database
  * [ Tutorials for SQL Server - SQL Server ](https://learn.microsoft.com/en-us/sql/sql-server/tutorials-for-sql-server-2016?source=recommendations)
Use these SQL Server tutorials to learn new technologies and features. Tutorials for earlier versions of SQL Server usually work with more recent versions.
  * [ Data type method reference for hierarchyid (Transact-SQL) - SQL Server ](https://learn.microsoft.com/en-us/sql/t-sql/data-types/hierarchyid-data-type-method-reference?source=recommendations)
hierarchyid data type method reference
  * [ Cursors (SQL Server) - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/cursors?source=recommendations)
Cursors extend result processing by manipulating result sets in small blocks at a time.
  * [ Database Engine Scripting ](https://learn.microsoft.com/en-us/ssms/scripting/database-engine-scripting?source=recommendations)
Learn how you can use the Microsoft PowerShell scripting environment to manage instances of the SQL Server Database Engine, and how you can build and run Database Engine queries that contain Transact-SQL and XQuery.


Show 4 more
Learning path
[ Use advance techniques in canvas apps to perform custom updates and optimization - Training ](https://learn.microsoft.com/en-us/training/paths/use-advance-techniques-canvas-apps-custom-updates-optimization/?source=recommendations)
Use advance techniques in canvas apps to perform custom updates and optimization
Mar 8, 4 PM - Mar 8, 4 PM
Experiment with what's next in AI-driven apps and agent design
* * *
  * Last updated on 11/18/2025


##  In this article
  1. [Key properties](https://learn.microsoft.com/en-us/sql/relational-databases/hierarchical-data-sql-server?view=sql-server-ver17#key-properties)
  2. [Limitations](https://learn.microsoft.com/en-us/sql/relational-databases/hierarchical-data-sql-server?view=sql-server-ver17#limitations)
  3. [When to use alternatives to hierarchyid](https://learn.microsoft.com/en-us/sql/relational-databases/hierarchical-data-sql-server?view=sql-server-ver17#when-to-use-alternatives-to-hierarchyid)
  4. [Index strategies for hierarchical data](https://learn.microsoft.com/en-us/sql/relational-databases/hierarchical-data-sql-server?view=sql-server-ver17#index-strategies-for-hierarchical-data)
  5. [Examples](https://learn.microsoft.com/en-us/sql/relational-databases/hierarchical-data-sql-server?view=sql-server-ver17#examples)
  6. [Related tasks](https://learn.microsoft.com/en-us/sql/relational-databases/hierarchical-data-sql-server?view=sql-server-ver17#related-tasks)
  7. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/hierarchical-data-sql-server?view=sql-server-ver17#related-content)


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
[ Sign in ](https://learn.microsoft.com/en-us/sql/relational-databases/hierarchical-data-sql-server?view=sql-server-ver17)
[English (United States)](https://learn.microsoft.com/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fsql%2Frelational-databases%2Fhierarchical-data-sql-server%3Fview%3Dsql-server-ver17)
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
