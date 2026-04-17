## Examples
The examples in this section make use of the `WideWorldImporters` sample database for SQL Server 2016 (13.x) and later versions, Azure SQL Database, and Azure SQL Managed Instance. `WideWorldImporters` can be downloaded from [RESTORE Statements](https://learn.microsoft.com/en-us/sql/t-sql/statements/restore-statements-transact-sql?view=sql-server-ver17) for the syntax to restore the sample database.
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#example-test-conditions)
### Example test conditions
Except where specified otherwise, the examples assume that you use Windows Authentication and have a trusted connection to the server instance on which you're running the **bcp** command. A directory named `D:\bcp` is used in many of the examples.
The following Transact-SQL script creates an empty copy of the `WideWorldImporters.Warehouse.StockItemTransactions` table and then adds a primary key constraint:
SQL
Copy
```
USE WideWorldImporters;
GO

SET NOCOUNT ON;

IF NOT EXISTS (SELECT *
               FROM sys.tables
               WHERE name = 'Warehouse.StockItemTransactions_bcp')
    BEGIN
        SELECT *
        INTO WideWorldImporters.Warehouse.StockItemTransactions_bcp
        FROM WideWorldImporters.Warehouse.StockItemTransactions
        WHERE 1 = 2;

        ALTER TABLE Warehouse.StockItemTransactions_bcp
        ADD CONSTRAINT PK_Warehouse_StockItemTransactions_bcp
            PRIMARY KEY NONCLUSTERED (StockItemTransactionID ASC);
    END

```

You can truncate the `StockItemTransactions_bcp` table as needed:
SQL
Copy
```
TRUNCATE TABLE WideWorldImporters.Warehouse.StockItemTransactions_bcp;

```

[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#a-identify-bcp-utility-version)
### A. Identify bcp utility version
At a command prompt, enter the following command:
Console
Copy
```
bcp -v

```

[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#b-copy-table-rows-into-a-data-file-with-a-trusted-connection)
### B. Copy table rows into a data file (with a trusted connection)
The following examples illustrate the `out` option on the `WideWorldImporters.Warehouse.StockItemTransactions` table.
  * **Basic**
This example creates a data file named `StockItemTransactions_character.bcp` and copies the table data into it using _character_ format.
At a command prompt, enter the following command:
Windows Command Prompt
Copy
```
bcp WideWorldImporters.Warehouse.StockItemTransactions out D:\bcp\StockItemTransactions_character.bcp -c -T

```

  * **Expanded**
This example creates a data file named `StockItemTransactions_native.bcp` and copies the table data into it using the _native_ format. The example also: specifies the maximum number of syntax errors, an error file, and an output file.
At a command prompt, enter the following command:
Windows Command Prompt
Copy
```
bcp WideWorldImporters.Warehouse.StockItemTransactions OUT D:\bcp\StockItemTransactions_native.bcp -m 1 -n -e D:\bcp\Error_out.log -o D:\bcp\Output_out.log -S -T

```



Review `Error_out.log` and `Output_out.log`. `Error_out.log` should be blank. Compare the file sizes between `StockItemTransactions_character.bcp` and `StockItemTransactions_native.bcp`.
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#c-copy-table-rows-into-a-data-file-with-mixed-mode-authentication)
### C. Copy table rows into a data file (with mixed-mode authentication)
The following example illustrates the `out` option on the `WideWorldImporters.Warehouse.StockItemTransactions` table. This example creates a data file named `StockItemTransactions_character.bcp` and copies the table data into it using **character** format.
The example assumes that you use mixed-mode authentication, and you must use the `-U` switch to specify your login ID. Also, unless you're connecting to the default instance of SQL Server on the local computer, use the `-S` switch to specify the system name and, optionally, an instance name.
At a command prompt, enter the following command: (The system prompts you for your password.)
Console
Copy
```
bcp WideWorldImporters.Warehouse.StockItemTransactions out D:\bcp\StockItemTransactions_character.bcp -c -U<login_id> -S<server_name\instance_name>

```

[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#d-copy-data-from-a-file-to-a-table)
### D. Copy data from a file to a table
The following examples illustrate the `in` option on the `WideWorldImporters.Warehouse.StockItemTransactions_bcp` table using files created previously.
  * **Basic**
This example uses the `StockItemTransactions_character.bcp` data file previously created.
At a command prompt, enter the following command:
Windows Command Prompt
Copy
```
bcp WideWorldImporters.Warehouse.StockItemTransactions_bcp IN D:\bcp\StockItemTransactions_character.bcp -c -T

```

  * **Expanded**
This example uses the `StockItemTransactions_native.bcp` data file previously created. The example also: use the hint `TABLOCK`, specifies the batch size, the maximum number of syntax errors, an error file, and an output file.
At a command prompt, enter the following command:
Windows Command Prompt
Copy
```
bcp WideWorldImporters.Warehouse.StockItemTransactions_bcp IN D:\bcp\StockItemTransactions_native.bcp -b 5000 -h "TABLOCK" -m 1 -n -e D:\bcp\Error_in.log -o D:\bcp\Output_in.log -S -T

```

Review `Error_in.log` and `Output_in.log`.


[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#e-copy-a-specific-column-into-a-data-file)
### E. Copy a specific column into a data file
To copy a specific column, you can use the `queryout` option. The following example copies only the `StockItemTransactionID` column of the `Warehouse.StockItemTransactions` table into a data file.
At a command prompt, enter the following command:
Console
Copy
```
bcp "SELECT StockItemTransactionID FROM WideWorldImporters.Warehouse.StockItemTransactions WITH (NOLOCK)" queryout D:\bcp\StockItemTransactionID_c.bcp -c -T

```

[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#f-copy-a-specific-row-into-a-data-file)
### F. Copy a specific row into a data file
To copy a specific row, you can use the `queryout` option. The following example copies only the row for the person named `Amy Trefl` from the `WideWorldImporters.Application.People` table into a data file `Amy_Trefl_c.bcp`.
The `-d` switch is used to identify the database.
At a command prompt, enter the following command:
Console
Copy
```
bcp "SELECT * from Application.People WHERE FullName = 'Amy Trefl'" queryout D:\bcp\Amy_Trefl_c.bcp -d WideWorldImporters -c -T

```

[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#g-copy-data-from-a-query-to-a-data-file)
### G. Copy data from a query to a data file
To copy the result set from a Transact-SQL statement to a data file, use the `queryout` option. The following example copies the names from the `WideWorldImporters.Application.People` table, ordered by full name, into the `People.txt` data file.
The `-t` switch is used to create a comma-delimited file.
At a command prompt, enter the following command:
Console
Copy
```
bcp "SELECT FullName, PreferredName FROM WideWorldImporters.Application.People ORDER BY FullName" queryout D:\bcp\People.txt -t, -c -T

```

[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#h-create-format-files)
### H. Create format files
The following example creates three different format files for the `Warehouse.StockItemTransactions` table in the `WideWorldImporters` database. Review the contents of each created file.
At a command prompt, enter the following commands:
Console
Copy
```
REM non-XML character format
bcp WideWorldImporters.Warehouse.StockItemTransactions format nul -f D:\bcp\StockItemTransactions_c.fmt -c -T

REM non-XML native format
bcp WideWorldImporters.Warehouse.StockItemTransactions format nul -f D:\bcp\StockItemTransactions_n.fmt -n -T

REM XML character format
bcp WideWorldImporters.Warehouse.StockItemTransactions format nul -f D:\bcp\StockItemTransactions_c.xml -x -c -T

```

To use the `-x` switch, you must be using a **bcp** 9.0 client. For information about how to use the **bcp** 9.0 client, see the [Remarks](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#remarks) section.
For more information, see [Use non-XML format files (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/non-xml-format-files-sql-server?view=sql-server-ver17) and [XML format files (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/xml-format-files-sql-server?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#i-use-a-format-file-to-bulk-import-with-bcp)
### I. Use a format file to bulk import with bcp
To use a previously created format file when importing data into an instance of SQL Server, use the `-f` switch with the `in` option. For example, the following command bulk copies the contents of a data file, `StockItemTransactions_character.bcp`, into a copy of the `Warehouse.StockItemTransactions_bcp` table by using the previously created format file, `StockItemTransactions_c.xml`.
The `-L` switch is used to import only the first 100 records.
At a command prompt, enter the following command:
Console
Copy
```
bcp WideWorldImporters.Warehouse.StockItemTransactions_bcp in D:\bcp\StockItemTransactions_character.bcp -L 100 -f D:\bcp\StockItemTransactions_c.xml -T

```

Format files are useful when the data file fields are different from the table columns; for example, in their number, ordering, or data types. For more information, see [Format files to import or export data (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/format-files-for-importing-or-exporting-data-sql-server?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#j-specify-a-code-page)
### J. Specify a code page
The following partial code example shows **bcp** import while specifying a code page 65001:
Console
Copy
```
bcp MyTable in "D:\data.csv" -T -c -C 65001 -t , ...

```

[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#k-example-output-file-using-a-custom-field-and-row-terminators)
### K. Example output file using a custom field and row terminators
This example shows two sample files, generated by **bcp** using custom field and row terminators.
  1. Create a table `dbo.T1` in the `tempdb` database, with two columns, `ID` and `Name`.
SQL
Copy
```
USE tempdb;
GO

CREATE TABLE dbo.T1 (ID INT, [Name] NVARCHAR (20));
GO

INSERT INTO dbo.T1 VALUES (1, N'Natalia');
INSERT INTO dbo.T1 VALUES (2, N'Mark');
INSERT INTO dbo.T1 VALUES (3, N'Randolph');
GO

```

  2. Generate an output file from the example table `dbo.T1`, using a custom field terminator.
In this example, the server name is `MYSERVER`, and `-t ,` specifies the custom field terminator.
Windows Command Prompt
Copy
```
bcp dbo.T1 out T1.txt -T -S MYSERVER -d tempdb -w -t ,

```

Here's the result set.
Output
Copy
```
1,Natalia
2,Mark
3,Randolph

```

  3. Generate an output file from the example table `dbo.T1`, using a custom field terminator and custom row terminator.
In this example, the server name is `MYSERVER`, `-t ,` specifies the custom field terminator, and `-r :` specifies the custom row terminator.
Windows Command Prompt
Copy
```
bcp dbo.T1 out T1.txt -T -S MYSERVER -d tempdb -w -t , -r :

```

Here's the result set.
Output
Copy
```
1,Natalia:2,Mark:3,Randolph:

```

The row terminator is always added, even to the last record. The field terminator, however, isn't added to the last field.


[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#additional-examples)
