# Subqueries (SQL Server)
Feedback
Summarize this article for me
##  In this article
  1. [Subquery fundamentals](https://learn.microsoft.com/en-us/sql/relational-databases/performance/subqueries?view=sql-server-ver17#subquery-fundamentals)
  2. [Subquery rules](https://learn.microsoft.com/en-us/sql/relational-databases/performance/subqueries?view=sql-server-ver17#subquery-rules)
  3. [Qualify column names in subqueries](https://learn.microsoft.com/en-us/sql/relational-databases/performance/subqueries?view=sql-server-ver17#qualify-column-names-in-subqueries)
  4. [Multiple levels of nesting](https://learn.microsoft.com/en-us/sql/relational-databases/performance/subqueries?view=sql-server-ver17#multiple-levels-of-nesting)
  5. [Correlated subqueries](https://learn.microsoft.com/en-us/sql/relational-databases/performance/subqueries?view=sql-server-ver17#correlated-subqueries)
  6. [Subquery types](https://learn.microsoft.com/en-us/sql/relational-databases/performance/subqueries?view=sql-server-ver17#subquery-types)
  7. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/performance/subqueries?view=sql-server-ver17#related-content)

Show 3 more
**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Database](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure Synapse Analytics](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Analytics Platform System (PDW)](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL database in Microsoft Fabric](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to)
A subquery is a query that is nested inside a `SELECT`, `INSERT`, `UPDATE`, or `DELETE` statement, or inside another subquery.
The code samples in this article use the `AdventureWorks2025` or `AdventureWorksDW2025` sample database, which you can download from the [Microsoft SQL Server Samples and Community Projects](https://go.microsoft.com/fwlink/?LinkID=85384) home page.
A subquery can be used anywhere an expression is allowed. In this example, a subquery is used as a column expression named MaxUnitPrice in a `SELECT` statement.
SQL
Copy
```
USE AdventureWorks2022;
GO
SELECT Ord.SalesOrderID, Ord.OrderDate,
    (SELECT MAX(OrdDet.UnitPrice)
     FROM Sales.SalesOrderDetail AS OrdDet
     WHERE Ord.SalesOrderID = OrdDet.SalesOrderID) AS MaxUnitPrice
FROM Sales.SalesOrderHeader AS Ord;
GO

```

[](https://learn.microsoft.com/en-us/sql/relational-databases/performance/subqueries?view=sql-server-ver17#subquery-fundamentals)
## Subquery fundamentals
A subquery is also called an inner query or inner select, while the statement containing a subquery is also called an outer query or outer select.
Many Transact-SQL statements that include subqueries can be alternatively formulated as joins. Other questions can be posed only with subqueries. In Transact-SQL, there's usually no performance difference between a statement that includes a subquery and a semantically equivalent version that doesn't. For architectural information on how SQL Server processes queries, see [SQL statement processing](https://learn.microsoft.com/en-us/sql/relational-databases/query-processing-architecture-guide?view=sql-server-ver17#sql-statement-processing). However, in some cases where existence must be checked, a join yields better performance. Otherwise, the nested query must be processed for each result of the outer query to ensure elimination of duplicates. In such cases, a join approach would yield better results.
The following example shows both a subquery `SELECT` and a join `SELECT` that return the same result set and execution plan:
SQL
Copy
```
USE AdventureWorks2022;
GO

/* SELECT statement built using a subquery. */
SELECT [Name]
FROM Production.Product
WHERE ListPrice =
    (SELECT ListPrice
     FROM Production.Product
     WHERE [Name] = 'Chainring Bolts' );
GO

/* SELECT statement built using a join that returns
   the same result set. */
SELECT Prd1.[Name]
FROM Production.Product AS Prd1
     JOIN Production.Product AS Prd2
       ON (Prd1.ListPrice = Prd2.ListPrice)
WHERE Prd2.[Name] = 'Chainring Bolts';
GO

```

A subquery nested in the outer `SELECT` statement has the following components:
  * A regular `SELECT` query including the regular select list components.
  * A regular `FROM` clause including one or more table or view names.
  * An optional `WHERE` clause.
  * An optional `GROUP BY` clause.
  * An optional `HAVING` clause.


The `SELECT` query of a subquery is always enclosed in parentheses. It can't include a `COMPUTE` or `FOR BROWSE` clause, and can only include an `ORDER BY` clause when a `TOP` clause is also specified.
A subquery can be nested inside the `WHERE` or `HAVING` clause of an outer `SELECT`, `INSERT`, `UPDATE`, or `DELETE` statement, or inside another subquery. Up to 32 levels of nesting is possible, although the limit varies based on available memory and the complexity of other expressions in the query. Individual queries don't support nesting up to 32 levels. A subquery can appear anywhere an expression can be used, if it returns a single value.
If a table appears only in a subquery and not in the outer query, then columns from that table can't be included in the output (the select list of the outer query).
Statements that include a subquery usually take one of these formats:
  * `WHERE expression [NOT] IN (subquery)`
  * `WHERE expression comparison_operator [ANY | ALL] (subquery)`
  * `WHERE [NOT] EXISTS (subquery)`


In some Transact-SQL statements, the subquery can be evaluated as if it were an independent query. Conceptually, the subquery results are substituted into the outer query (although this isn't necessarily how SQL Server actually processes Transact-SQL statements with subqueries).
There are three basic types of subqueries. Those that:
  * Operate on lists introduced with `IN`, or those that a comparison operator modified by `ANY` or `ALL`.
  * Are introduced with an unmodified comparison operator and must return a single value.
  * Are existence tests introduced with `EXISTS`.


[](https://learn.microsoft.com/en-us/sql/relational-databases/performance/subqueries?view=sql-server-ver17#subquery-rules)
## Subquery rules
A subquery is subject to the following restrictions:
  * The select list of a subquery introduced with a comparison operator can include only one expression or column name (except that `EXISTS` and `IN` operate on `SELECT *` or a list, respectively).
  * If the `WHERE` clause of an outer query includes a column name, it must be join-compatible with the column in the subquery select list.
  * The **ntext** , **text** , and **image** data types can't be used in the select list of subqueries.
  * Because they must return a single value, subqueries introduced by an unmodified comparison operator (one not followed by the keyword `ANY` or `ALL`) can't include `GROUP BY` and `HAVING` clauses.
  * The `DISTINCT` keyword can't be used with subqueries that include `GROUP BY`.
  * The `COMPUTE` and `INTO` clauses can't be specified.
  * `ORDER BY` can only be specified when `TOP` is also specified.
  * A view created by using a subquery can't be updated.
  * The select list of a subquery introduced with `EXISTS`, by convention, has an asterisk (`*`) instead of a single column name. The rules for a subquery introduced with `EXISTS` are the same as those for a standard select list, because a subquery introduced with `EXISTS` creates an existence test and returns TRUE or FALSE, instead of data.


[](https://learn.microsoft.com/en-us/sql/relational-databases/performance/subqueries?view=sql-server-ver17#qualify-column-names-in-subqueries)
## Qualify column names in subqueries
In the following example, the `BusinessEntityID` column in the `WHERE` clause of the outer query is implicitly qualified by the table name in the outer query `FROM` clause (`Sales.Store`). The reference to `CustomerID` in the select list of the subquery is qualified by the subquery `FROM` clause, that is, by the `Sales.Customer` table.
SQL
Copy
```
USE AdventureWorks2022;
GO
SELECT [Name]
FROM Sales.Store
WHERE BusinessEntityID NOT IN
    (SELECT CustomerID
     FROM Sales.Customer
     WHERE TerritoryID = 5);
GO

```

The general rule is that column names in a statement are implicitly qualified by the table referenced in the `FROM` clause at the same level. If a column doesn't exist in the table referenced in the `FROM` clause of a subquery, it's implicitly qualified by the table referenced in the `FROM` clause of the outer query.
Here's what the query looks like with these implicit assumptions specified:
SQL
Copy
```
USE AdventureWorks2022;
GO
SELECT [Name]
FROM Sales.Store
WHERE Sales.Store.BusinessEntityID NOT IN
    (SELECT Sales.Customer.CustomerID
     FROM Sales.Customer
     WHERE TerritoryID = 5);
GO

```

It's never wrong to state the table name explicitly, and it's always possible to override implicit assumptions about table names with explicit qualifications.
If a column is referenced in a subquery that doesn't exist in the table referenced by the subquery's `FROM` clause, but exists in a table referenced by the outer query's `FROM` clause, the query executes without error. SQL Server implicitly qualifies the column in the subquery with the table name in the outer query.
[](https://learn.microsoft.com/en-us/sql/relational-databases/performance/subqueries?view=sql-server-ver17#multiple-levels-of-nesting)
## Multiple levels of nesting
A subquery can itself include one or more subqueries. Any number of subqueries can be nested in a statement.
The following query finds the names of employees who are also sales persons.
SQL
Copy
```
USE AdventureWorks2022;
GO
SELECT LastName, FirstName
FROM Person.Person
WHERE BusinessEntityID IN
    (SELECT BusinessEntityID
     FROM HumanResources.Employee
     WHERE BusinessEntityID IN
        (SELECT BusinessEntityID
         FROM Sales.SalesPerson)
    );
GO

```

Here's the result set.
Output
Copy
```
LastName                                           FirstName
-------------------------------------------------- -----------------------
Jiang                                              Stephen
Abbas                                              Syed
Alberts                                            Amy
Ansman-Wolfe                                       Pamela
Campbell                                           David
Carson                                             Jillian
Ito                                                Shu
Mitchell                                           Linda
Reiter                                             Tsvi
Saraiva                                            Jos
Vargas                                             Garrett
Varkey Chudukatil                                  Ranjit
Valdez                                             Rachel
Tsoflias                                           Lynn
Pak                                                Jae
Blythe                                             Michael
Mensa-Annan                                        Tete

(17 row(s) affected)

```

The innermost query returns the sales person IDs. The query at the next higher level is evaluated with these sales person IDs and returns the contact ID numbers of the employees. Finally, the outer query uses the contact IDs to find the names of the employees.
You can also express this query as a join:
SQL
Copy
```
USE AdventureWorks2022;
GO
SELECT LastName, FirstName
FROM Person.Person c
INNER JOIN HumanResources.Employee e
ON c.BusinessEntityID = e.BusinessEntityID
JOIN Sales.SalesPerson s
ON e.BusinessEntityID = s.BusinessEntityID;
GO

```

[](https://learn.microsoft.com/en-us/sql/relational-databases/performance/subqueries?view=sql-server-ver17#correlated-subqueries)
## Correlated subqueries
Many queries can be evaluated by executing the subquery once and substituting the resulting value or values into the `WHERE` clause of the outer query. In queries that include a correlated subquery (also known as a repeating subquery), the subquery depends on the outer query for its values. This means that the subquery is executed repeatedly, once for each row that might be selected by the outer query.
This query retrieves one instance of each employee's first and last name for which the bonus in the `SalesPerson` table is 5000 and for which the employee identification numbers match in the `Employee` and `SalesPerson` tables.
SQL
Copy
```
USE AdventureWorks2022;
GO
SELECT DISTINCT c.LastName, c.FirstName, e.BusinessEntityID
FROM Person.Person AS c JOIN HumanResources.Employee AS e
ON e.BusinessEntityID = c.BusinessEntityID
WHERE 5000.00 IN
    (SELECT Bonus
    FROM Sales.SalesPerson sp
    WHERE e.BusinessEntityID = sp.BusinessEntityID) ;
GO

```

Here's the result set.
Output
Copy
```
LastName FirstName BusinessEntityID
-------------------------- ---------- ------------
Ansman-Wolfe Pamela 280
Saraiva José 282

(2 row(s) affected)

```

The previous subquery in this statement can't be evaluated independently of the outer query. It needs a value for `Employee.BusinessEntityID`, but this value changes as SQL Server examines different rows in `Employee`. That is exactly how this query is evaluated: SQL Server considers each row of the `Employee` table for inclusion in the results by substituting the value in each row into the inner query. For example, if SQL Server first examines the row for `Syed Abbas`, the variable `Employee.BusinessEntityID` takes the value `285`, which SQL Server substitutes into the inner query. These two query samples represent a decomposition of the previous sample with the correlated subquery.
SQL
Copy
```
USE AdventureWorks2022;
GO
SELECT Bonus
FROM Sales.SalesPerson
WHERE BusinessEntityID = 285;
GO

```

The result is 0.00 (`Syed Abbas` didn't receive a bonus because they aren't a salesperson), so the outer query evaluates to:
SQL
Copy
```
USE AdventureWorks2022;
GO
SELECT LastName, FirstName
FROM Person.Person AS c JOIN HumanResources.Employee AS e
ON e.BusinessEntityID = c.BusinessEntityID
WHERE 5000 IN (0.00);
GO

```

Because this is false, the row for `Syed Abbas` isn't included in the results of the previous sample query with the correlated subquery. Go through the same procedure with the row for `Pamela Ansman-Wolfe`. You see that this row is included in the results, because `WHERE 5000 IN (5000)` includes results.
Correlated subqueries can also include table-valued functions in the `FROM` clause by referencing columns from a table in the outer query as an argument of the table-valued function. In this case, for each row of the outer query, the table-valued function is evaluated according to the subquery.
[](https://learn.microsoft.com/en-us/sql/relational-databases/performance/subqueries?view=sql-server-ver17#subquery-types)
## Subquery types
Subqueries can be specified in many places:
  * With aliases. For more information, see [Subqueries with table aliases](https://learn.microsoft.com/en-us/sql/relational-databases/performance/subqueries?view=sql-server-ver17#aliases).
  * With `IN` or `NOT IN`. For more information, see [Subqueries with IN](https://learn.microsoft.com/en-us/sql/relational-databases/performance/subqueries?view=sql-server-ver17#in) and [Subqueries with NOT IN](https://learn.microsoft.com/en-us/sql/relational-databases/performance/subqueries?view=sql-server-ver17#notin).
  * In `UPDATE`, `DELETE`, and `INSERT` statements. For more information, see [Subqueries in UPDATE, DELETE, and INSERT Statements](https://learn.microsoft.com/en-us/sql/relational-databases/performance/subqueries?view=sql-server-ver17#upsert).
  * With comparison operators. For more information, see [Subqueries with comparison operators](https://learn.microsoft.com/en-us/sql/relational-databases/performance/subqueries?view=sql-server-ver17#comparison).
  * With `ANY`, `SOME`, or `ALL`. For more information, see [Comparison operators modified by ANY, SOME, or ALL](https://learn.microsoft.com/en-us/sql/relational-databases/performance/subqueries?view=sql-server-ver17#comparison_modified).
  * With `IS [NOT] DISTINCT FROM`. For more information, see [IS [NOT] DISTINCT FROM (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/queries/is-distinct-from-transact-sql?view=sql-server-ver17).
  * With `EXISTS` or `NOT EXISTS`. For more information, see [Subqueries with EXISTS](https://learn.microsoft.com/en-us/sql/relational-databases/performance/subqueries?view=sql-server-ver17#exists) and [Subqueries with NOT EXISTS](https://learn.microsoft.com/en-us/sql/relational-databases/performance/subqueries?view=sql-server-ver17#notexists).
  * In place of an expression. For more information, see [Subqueries used in place of an expression](https://learn.microsoft.com/en-us/sql/relational-databases/performance/subqueries?view=sql-server-ver17#expression).


[](https://learn.microsoft.com/en-us/sql/relational-databases/performance/subqueries?view=sql-server-ver17#subqueries-with-table-aliases)
### Subqueries with table aliases
Many statements in which the subquery and the outer query refer to the same table can be stated as self-joins (joining a table to itself). For example, you can find addresses of employees from a particular state using a subquery:
SQL
Copy
```
USE AdventureWorks2022;
GO
SELECT StateProvinceID, AddressID
FROM Person.Address
WHERE AddressID IN
    (SELECT AddressID
     FROM Person.Address
     WHERE StateProvinceID = 39);
GO

```

Here's the result set.
Output
Copy
```
StateProvinceID AddressID
----------- -----------
39 942
39 955
39 972
39 22660

(4 row(s) affected)

```

Or you can use a self-join:
SQL
Copy
```
USE AdventureWorks2022;
GO
SELECT e1.StateProvinceID, e1.AddressID
FROM Person.Address AS e1
INNER JOIN Person.Address AS e2
ON e1.AddressID = e2.AddressID
AND e2.StateProvinceID = 39;
GO

```

Table aliases `e1` and `e2` are required because the table being joined to itself appears in two different roles. Aliases can also be used in nested queries that refer to the same table in an inner and outer query.
SQL
Copy
```
USE AdventureWorks2022;
GO
SELECT e1.StateProvinceID, e1.AddressID
FROM Person.Address AS e1
WHERE e1.AddressID IN
    (SELECT e2.AddressID
     FROM Person.Address AS e2
     WHERE e2.StateProvinceID = 39);
GO

```

Explicit table aliases make it clear that a reference to `Person.Address` in the subquery doesn't mean the same thing as the reference in the outer query.
[](https://learn.microsoft.com/en-us/sql/relational-databases/performance/subqueries?view=sql-server-ver17#subqueries-with-in)
### Subqueries with IN
The result of a subquery introduced with `IN` (or with `NOT IN`) is a list of zero or more values. After the subquery returns results, the outer query makes use of them. The following query finds the names of all the wheel products that Adventure Works Cycles makes.
SQL
Copy
```
USE AdventureWorks2022;
GO
SELECT [Name]
FROM Production.Product
WHERE ProductSubcategoryID IN
    (SELECT ProductSubcategoryID
     FROM Production.ProductSubcategory
     WHERE [Name] = 'Wheels');
GO

```

Here's the result set.
Output
Copy
```
Name
----------------------------
LL Mountain Front Wheel
ML Mountain Front Wheel
HL Mountain Front Wheel
LL Road Front Wheel
ML Road Front Wheel
HL Road Front Wheel
Touring Front Wheel
LL Mountain Rear Wheel
ML Mountain Rear Wheel
HL Mountain Rear Wheel
LL Road Rear Wheel
ML Road Rear Wheel
HL Road Rear Wheel
Touring Rear Wheel

(14 row(s) affected)

```

This statement is evaluated in two steps. First, the inner query returns the subcategory identification number that matches the name `Wheel` (`17`). Second, this value is substituted into the outer query, which finds the product names that go with the subcategory identification numbers in `Production.Product`.
SQL
Copy
```
USE AdventureWorks2022;
GO
SELECT [Name]
FROM Production.Product
WHERE ProductSubcategoryID IN ('17');
GO

```

One difference in using a join rather than a subquery for this and similar problems is that the join lets you show columns from more than one table in the result. For example, if you want to include the name of the product subcategory in the result, you must use a join version.
SQL
Copy
```
USE AdventureWorks2022;
GO
SELECT p.[Name], s.[Name]
FROM Production.Product p
INNER JOIN Production.ProductSubcategory s
ON p.ProductSubcategoryID = s.ProductSubcategoryID
AND s.[Name] = 'Wheels';
GO

```

Here's the result set.
Output
Copy
```
Name
LL Mountain Front Wheel Wheels
ML Mountain Front Wheel Wheels
HL Mountain Front Wheel Wheels
LL Road Front Wheel Wheels
ML Road Front Wheel Wheels
HL Road Front Wheel Wheels
Touring Front Wheel Wheels
LL Mountain Rear Wheel Wheels
ML Mountain Rear Wheel Wheels
HL Mountain Rear Wheel Wheels
LL Road Rear Wheel Wheels
ML Road Rear Wheel Wheels
HL Road Rear Wheel Wheels
Touring Rear Wheel Wheels

(14 row(s) affected)

```

The following query finds the name of all vendors whose credit rating is good, from whom Adventure Works Cycles orders at least 20 items, and whose average lead time to deliver is less than 16 days.
SQL
Copy
```
USE AdventureWorks2022;
GO
SELECT [Name]
FROM Purchasing.Vendor
WHERE CreditRating = 1
AND BusinessEntityID IN
    (SELECT BusinessEntityID
     FROM Purchasing.ProductVendor
     WHERE MinOrderQty >= 20
     AND AverageLeadTime < 16);
GO

```

Here's the result set.
Output
Copy
```
Name
--------------------------------------------------
Compete Enterprises, Inc
International Trek Center
First National Sport Co.
Comfort Road Bicycles
Circuit Cycles
First Rate Bicycles
Jeff's Sporting Goods
Competition Bike Training Systems
Electronic Bike Repair & Supplies
Crowley Sport
Expert Bike Co
Team Athletic Co.
Compete, Inc.

(13 row(s) affected)

```

The inner query is evaluated, producing the ID numbers of the vendors who meet the subquery qualifications. The outer query is then evaluated. You can include more than one condition in the `WHERE` clause of both the inner and the outer query.
Using a join, the same query is expressed like this:
SQL
Copy
```
USE AdventureWorks2022;
GO
SELECT DISTINCT [Name]
FROM Purchasing.Vendor v
INNER JOIN Purchasing.ProductVendor p
ON v.BusinessEntityID = p.BusinessEntityID
WHERE CreditRating = 1
  AND MinOrderQty >= 20
  AND AverageLeadTime < 16;
GO

```

A join can always be expressed as a subquery. A subquery can often, but not always, be expressed as a join. This is because joins are symmetric: you can join table `A` to `B` in either order and get the same answer. The same isn't true if a subquery is involved.
[](https://learn.microsoft.com/en-us/sql/relational-databases/performance/subqueries?view=sql-server-ver17#subqueries-with-not-in)
### Subqueries with NOT IN
Subqueries introduced with the keyword `NOT IN` also return a list of zero or more values. The following query finds the names of the products that aren't finished bicycles.
SQL
Copy
```
USE AdventureWorks2022;
GO
SELECT [Name]
FROM Production.Product
WHERE ProductSubcategoryID NOT IN
    (SELECT ProductSubcategoryID
     FROM Production.ProductSubcategory
     WHERE [Name] = 'Mountain Bikes'
        OR [Name] = 'Road Bikes'
        OR [Name] = 'Touring Bikes');
GO

```

This statement can't be converted to a join. The analogous not-equal join has a different meaning: It finds the names of products that are in some subcategory that isn't a finished bicycle.
[](https://learn.microsoft.com/en-us/sql/relational-databases/performance/subqueries?view=sql-server-ver17#subqueries-in-update-delete-and-insert-statements)
### Subqueries in UPDATE, DELETE, and INSERT statements
Subqueries can be nested in the `UPDATE`, `DELETE`, `INSERT`, and `SELECT` data manipulation (DML) statements.
The following example doubles the value in the `ListPrice` column in the `Production.Product` table. The subquery in the `WHERE` clause references the `Purchasing.ProductVendor` table to restrict the rows updated in the _Product_ table to just those supplied by `BusinessEntity` `1540`.
SQL
Copy
```
USE AdventureWorks2022;
GO
UPDATE Production.Product
SET ListPrice = ListPrice * 2
WHERE ProductID IN
    (SELECT ProductID
     FROM Purchasing.ProductVendor
     WHERE BusinessEntityID = 1540);
GO

```

Here's an equivalent `UPDATE` statement using a join:
SQL
Copy
```
USE AdventureWorks2022;
GO
UPDATE Production.Product
SET ListPrice = ListPrice * 2
FROM Production.Product AS p
INNER JOIN Purchasing.ProductVendor AS pv
    ON p.ProductID = pv.ProductID AND BusinessEntityID = 1540;
GO

```

For clarity in case the same table is itself referenced in other subqueries, use the target table's alias:
SQL
Copy
```
USE AdventureWorks2022;
GO
UPDATE p
SET ListPrice = ListPrice * 2
FROM Production.Product AS p
INNER JOIN Purchasing.ProductVendor AS pv
    ON p.ProductID = pv.ProductID AND BusinessEntityID = 1540;
GO

```

[](https://learn.microsoft.com/en-us/sql/relational-databases/performance/subqueries?view=sql-server-ver17#subqueries-with-comparison-operators)
### Subqueries with comparison operators
Subqueries can be introduced with one of the comparison operators (`=`, `< >`, `>`, `> =`, `<`, `! >`, `! <`, or `< =`).
A subquery introduced with an unmodified comparison operator (a comparison operator not followed by `ANY` or `ALL`) must return a single value rather than a list of values, like subqueries introduced with `IN`. If such a subquery returns more than one value, SQL Server displays an error message.
To use a subquery introduced with an unmodified comparison operator, you must be familiar enough with your data and with the nature of the problem to know that the subquery will return exactly one value.
For example, if you assume each sales person only covers one sales territory, and you want to find the customers located in the territory covered by `Linda Mitchell`, you can write a statement with a subquery introduced with the simple `=` comparison operator.
SQL
Copy
```
USE AdventureWorks2022;
GO
SELECT CustomerID
FROM Sales.Customer
WHERE TerritoryID =
    (SELECT TerritoryID
     FROM Sales.SalesPerson
     WHERE BusinessEntityID = 276);
GO

```

If, however, `Linda Mitchell` covered more than one sales territory, then an error message would result. Instead of the `=` comparison operator, an `IN` formulation could be used (`=ANY` also works).
Subqueries introduced with unmodified comparison operators often include aggregate functions, because these return a single value. For example, the following statement finds the names of all products whose list price is greater than the average list price.
SQL
Copy
```
USE AdventureWorks2022;
GO
SELECT [Name]
FROM Production.Product
WHERE ListPrice >
    (SELECT AVG (ListPrice)
     FROM Production.Product);
GO

```

Because subqueries introduced with unmodified comparison operators must return a single value, they can't include `GROUP BY` or `HAVING` clauses unless you know the `GROUP BY` or `HAVING` clause itself returns a single value. For example, the following query finds the products priced higher than the lowest-priced product that is in `ProductSubcategoryID` `14`.
SQL
Copy
```
USE AdventureWorks2022;
GO
SELECT [Name]
FROM Production.Product
WHERE ListPrice >
    (SELECT MIN (ListPrice)
     FROM Production.Product
     GROUP BY ProductSubcategoryID
     HAVING ProductSubcategoryID = 14);
GO

```

[](https://learn.microsoft.com/en-us/sql/relational-databases/performance/subqueries?view=sql-server-ver17#comparison-operators-modified-by-any-some-or-all)
### Comparison operators modified by `ANY`, `SOME`, or `ALL`
Comparison operators that introduce a subquery can be modified by the keywords `ALL` or `ANY`. `SOME` is an ISO standard equivalent for `ANY`. For more information on these comparison operators, see [SOME | ANY](https://learn.microsoft.com/en-us/sql/t-sql/language-elements/some-any-transact-sql?view=sql-server-ver17).
Subqueries introduced with a modified comparison operator return a list of zero or more values and can include a `GROUP BY` or `HAVING` clause. These subqueries can be restated with `EXISTS`.
Using the > comparison operator as an example, `> ALL` means greater than every value. In other words, it means greater than the maximum value. For example, `> ALL (1, 2, 3)` means greater than 3. `> ANY` means greater than at least one value, that is, greater than the minimum. So `> ANY (1, 2, 3)` means greater than 1.
For a row in a subquery with `> ALL` to satisfy the condition specified in the outer query, the value in the column introducing the subquery must be greater than each value in the list of values returned by the subquery.
Similarly, `> ANY` means that for a row to satisfy the condition specified in the outer query, the value in the column that introduces the subquery must be greater than at least one of the values in the list of values returned by the subquery.
The following query provides an example of a subquery introduced with a comparison operator modified by `ANY`. It finds the products whose list prices are greater than or equal to the maximum list price of any product subcategory.
SQL
Copy
```
USE AdventureWorks2022;
GO
SELECT [Name]
FROM Production.Product
WHERE ListPrice >= ANY
    (SELECT MAX (ListPrice)
     FROM Production.Product
     GROUP BY ProductSubcategoryID);
GO

```

For each Product subcategory, the inner query finds the maximum list price. The outer query looks at all of these values and determines which individual product's list prices are greater than or equal to any product subcategory's maximum list price. If `ANY` is changed to `ALL`, the query returns only those products whose list price is greater than or equal to all the list prices returned in the inner query.
If the subquery doesn't return any values, the entire query fails to return any values.
The `= ANY` operator is equivalent to `IN`. For example, to find the names of all the wheel products that Adventure Works Cycles makes, you can use either `IN` or `= ANY`.
SQL
Copy
```
--Using = ANY
USE AdventureWorks2022;
GO
SELECT [Name]
FROM Production.Product
WHERE ProductSubcategoryID = ANY
    (SELECT ProductSubcategoryID
     FROM Production.ProductSubcategory
     WHERE Name = 'Wheels');
GO

--Using IN
USE AdventureWorks2022;
GO
SELECT [Name]
FROM Production.Product
WHERE ProductSubcategoryID IN
    (SELECT ProductSubcategoryID
     FROM Production.ProductSubcategory
     WHERE Name = 'Wheels');
GO

```

Here's the result set for either query:
Output
Copy
```
Name
--------------------------------------------------
LL Mountain Front Wheel
ML Mountain Front Wheel
HL Mountain Front Wheel
LL Road Front Wheel
ML Road Front Wheel
HL Road Front Wheel
Touring Front Wheel
LL Mountain Rear Wheel
ML Mountain Rear Wheel
HL Mountain Rear Wheel
LL Road Rear Wheel
ML Road Rear Wheel
HL Road Rear Wheel
Touring Rear Wheel

(14 row(s) affected)

```

The `<> ANY` operator, however, differs from `NOT IN`:
  * `<> ANY` means not = a, or not = b, or not = c
  * `NOT IN` means not = a, and not = b, and not = c
  * `<> ALL` means the same as `NOT IN`


For example, the following query finds customers located in a territory not covered by any sales persons.
SQL
Copy
```
USE AdventureWorks2022;
GO
SELECT CustomerID
FROM Sales.Customer
WHERE TerritoryID <> ANY
    (SELECT TerritoryID
     FROM Sales.SalesPerson);
GO

```

The results include all customers, except those whose sales territories are `NULL`, because every territory that is assigned to a customer is covered by a sales person. The inner query finds all the sales territories covered by sales persons, and then, for each territory, the outer query finds the customers who aren't in one.
For the same reason, when you use `NOT IN` in this query, the results include none of the customers.
You can get the same results with the `<> ALL` operator, which is equivalent to `NOT IN`.
[](https://learn.microsoft.com/en-us/sql/relational-databases/performance/subqueries?view=sql-server-ver17#subqueries-with-exists)
### Subqueries with `EXISTS`
When a subquery is introduced with the keyword `EXISTS`, the subquery functions as an existence test. The `WHERE` clause of the outer query tests whether the rows that are returned by the subquery exist. The subquery doesn't actually produce any data; it returns a value of `TRUE` or `FALSE`.
A subquery introduced with `EXISTS` has the following syntax: `WHERE [NOT] EXISTS (subquery)`
The following query finds the names of all products that are in the Wheels subcategory:
SQL
Copy
```
USE AdventureWorks2022;
GO
SELECT [Name]
FROM Production.Product
WHERE EXISTS
    (SELECT *
     FROM Production.ProductSubcategory
     WHERE ProductSubcategoryID =
            Production.Product.ProductSubcategoryID
        AND [Name] = 'Wheels');
GO

```

Here's the result set.
Output
Copy
```
Name
--------------------------------------------------
LL Mountain Front Wheel
ML Mountain Front Wheel
HL Mountain Front Wheel
LL Road Front Wheel
ML Road Front Wheel
HL Road Front Wheel
Touring Front Wheel
LL Mountain Rear Wheel
ML Mountain Rear Wheel
HL Mountain Rear Wheel
LL Road Rear Wheel
ML Road Rear Wheel
HL Road Rear Wheel
Touring Rear Wheel

(14 row(s) affected)

```

To understand the results of this query, consider the name of each product in turn. Does this value cause the subquery to return at least one row? In other words, does the query cause the existence test to evaluate to `TRUE`?
Subqueries that are introduced with `EXISTS` are a bit different from other subqueries in the following ways:
  * The keyword `EXISTS` isn't preceded by a column name, constant, or other expression.
  * The select list of a subquery introduced by `EXISTS` almost always consists of an asterisk (*). There's no reason to list column names because you're just testing whether rows that meet the conditions specified in the subquery exist.


The `EXISTS` keyword is important because frequently there's no alternative formulation without subqueries. Although some queries that are created with `EXISTS` can't be expressed any other way, many queries can use `IN` or a comparison operator modified by `ANY` or `ALL` to achieve similar results.
For example, the preceding query can be expressed by using `IN`:
SQL
Copy
```
USE AdventureWorks2022;
GO
SELECT [Name]
FROM Production.Product
WHERE ProductSubcategoryID IN
    (SELECT ProductSubcategoryID
     FROM Production.ProductSubcategory
     WHERE [Name] = 'Wheels');
GO

```

[](https://learn.microsoft.com/en-us/sql/relational-databases/performance/subqueries?view=sql-server-ver17#subqueries-with-not-exists)
### Subqueries with `NOT EXISTS`
`NOT EXISTS` works like `EXISTS`, except the `WHERE` clause is satisfied if no rows are returned by the subquery.
For example, to find the names of products that aren't in the wheels subcategory:
SQL
Copy
```
USE AdventureWorks2022;
GO
SELECT [Name]
FROM Production.Product
WHERE NOT EXISTS
    (SELECT *
     FROM Production.ProductSubcategory
     WHERE ProductSubcategoryID =
            Production.Product.ProductSubcategoryID
        AND [Name] = 'Wheels');
GO

```

[](https://learn.microsoft.com/en-us/sql/relational-databases/performance/subqueries?view=sql-server-ver17#subqueries-used-in-place-of-an-expression)
### Subqueries used in place of an expression
In Transact-SQL, a subquery can be substituted anywhere an expression can be used in `SELECT`, `UPDATE`, `INSERT`, and `DELETE` statements, except in an `ORDER BY` list.
The following example illustrates how you might use this enhancement. This query finds the prices of all mountain bike products, their average price, and the difference between the price of each mountain bike and the average price.
SQL
Copy
```
USE AdventureWorks2022;
GO
SELECT [Name], ListPrice,
(SELECT AVG(ListPrice) FROM Production.Product) AS Average,
    ListPrice - (SELECT AVG(ListPrice) FROM Production.Product)
    AS Difference
FROM Production.Product
WHERE ProductSubcategoryID = 1;
GO

```

[](https://learn.microsoft.com/en-us/sql/relational-databases/performance/subqueries?view=sql-server-ver17#related-content)
## Related content
  * [IN (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/language-elements/in-transact-sql?view=sql-server-ver17)
  * [EXISTS (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/language-elements/exists-transact-sql?view=sql-server-ver17)
  * [ALL (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/language-elements/all-transact-sql?view=sql-server-ver17)
  * [SOME | ANY (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/language-elements/some-any-transact-sql?view=sql-server-ver17)
  * [Joins (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/performance/joins?view=sql-server-ver17)
  * [Comparison Operators (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/language-elements/comparison-operators-transact-sql?view=sql-server-ver17)
  * [Query processing architecture guide](https://learn.microsoft.com/en-us/sql/relational-databases/query-processing-architecture-guide?view=sql-server-ver17)
  * [Best practices for monitoring workloads with Query Store](https://learn.microsoft.com/en-us/sql/relational-databases/performance/best-practice-with-the-query-store?view=sql-server-ver17)
  * [Intelligent query processing in SQL databases](https://learn.microsoft.com/en-us/sql/relational-databases/performance/intelligent-query-processing?view=sql-server-ver17)
  * [Cardinality Estimation (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/performance/cardinality-estimation-sql-server?view=sql-server-ver17)


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
  * [ Joins (SQL Server) - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/performance/joins?source=recommendations)
Learn about the types of join operations that SQL Server employs. SQL Server supports vertical table partitioning, or columnar storage, using join operations.
  * [ UNION (Transact-SQL) - SQL Server ](https://learn.microsoft.com/en-us/sql/t-sql/language-elements/set-operators-union-transact-sql?source=recommendations)
Set Operators - UNION (Transact-SQL)
  * [ INSERT (Transact-SQL) - SQL Server ](https://learn.microsoft.com/en-us/sql/t-sql/statements/insert-transact-sql?source=recommendations)
INSERT (Transact-SQL)
  * [ EXISTS (Transact-SQL) - SQL Server ](https://learn.microsoft.com/en-us/sql/t-sql/language-elements/exists-transact-sql?source=recommendations)
EXISTS specifies a subquery to test for the existence of rows.
  * [ INTO Clause (Transact-SQL) - SQL Server ](https://learn.microsoft.com/en-us/sql/t-sql/queries/select-into-clause-transact-sql?source=recommendations)
SELECT - INTO Clause (Transact-SQL)
  * [ TOP (Transact-SQL) - SQL Server ](https://learn.microsoft.com/en-us/sql/t-sql/queries/top-transact-sql?source=recommendations)
Limits the rows returned in a query result set to a specified number of rows or percentage of rows in the SQL Server Database Engine.
  * [ CASE (Transact-SQL) - SQL Server ](https://learn.microsoft.com/en-us/sql/t-sql/language-elements/case-transact-sql?source=recommendations)
Transact-SQL reference for the CASE expression. CASE evaluates a list of conditions to return specific results.
  * [ UPDATE (Transact-SQL) - SQL Server ](https://learn.microsoft.com/en-us/sql/t-sql/queries/update-transact-sql?source=recommendations)
UPDATE (Transact-SQL)


Show 5 more
Module
[ Write Subqueries in T-SQL - Training ](https://learn.microsoft.com/en-us/training/modules/write-subqueries/?source=recommendations)
Write Subqueries in T-SQL
Mar 8, 4 PM - Mar 8, 4 PM
Experiment with what's next in AI-driven apps and agent design
* * *
  * Last updated on 11/18/2025


##  In this article
  1. [Subquery fundamentals](https://learn.microsoft.com/en-us/sql/relational-databases/performance/subqueries?view=sql-server-ver17#subquery-fundamentals)
  2. [Subquery rules](https://learn.microsoft.com/en-us/sql/relational-databases/performance/subqueries?view=sql-server-ver17#subquery-rules)
  3. [Qualify column names in subqueries](https://learn.microsoft.com/en-us/sql/relational-databases/performance/subqueries?view=sql-server-ver17#qualify-column-names-in-subqueries)
  4. [Multiple levels of nesting](https://learn.microsoft.com/en-us/sql/relational-databases/performance/subqueries?view=sql-server-ver17#multiple-levels-of-nesting)
  5. [Correlated subqueries](https://learn.microsoft.com/en-us/sql/relational-databases/performance/subqueries?view=sql-server-ver17#correlated-subqueries)
  6. [Subquery types](https://learn.microsoft.com/en-us/sql/relational-databases/performance/subqueries?view=sql-server-ver17#subquery-types)
  7. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/performance/subqueries?view=sql-server-ver17#related-content)


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
[ Sign in ](https://learn.microsoft.com/en-us/sql/relational-databases/performance/subqueries?view=sql-server-ver17)
[English (United States)](https://learn.microsoft.com/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fsql%2Frelational-databases%2Fperformance%2Fsubqueries%3Fview%3Dsql-server-ver17)
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
