# Import Flat File to SQL Wizard
Feedback
Summarize this article for me
##  In this article
  1. [Why would I use this wizard?](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/import-flat-file-wizard?view=sql-server-ver17#why-would-i-use-this-wizard)
  2. [Prerequisites](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/import-flat-file-wizard?view=sql-server-ver17#prerequisites)
  3. [Getting Started](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/import-flat-file-wizard?view=sql-server-ver17#started)
  4. [Tutorial](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/import-flat-file-wizard?view=sql-server-ver17#tutorial)
  5. [Troubleshooting](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/import-flat-file-wizard?view=sql-server-ver17#troubleshooting)
  6. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/import-flat-file-wizard?view=sql-server-ver17#related-content)

Show 2 more
**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Database](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to)
> For content related to the Import and Export Wizard, see [Import and Export Data with the SQL Server Import and Export Wizard](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/import-and-export-data-with-the-sql-server-import-and-export-wizard?view=sql-server-ver17).
Import Flat File Wizard is a simple way to copy data from a flat file (for example, .csv or .txt) to a new table in your database. The Import Flat File Wizard supports multiple delimiters, including commas, tabs, semicolons, and pipes, and also supports fixed width data. This overview describes the reasons for using this wizard, how to find this wizard, and a simple example to follow.
[](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/import-flat-file-wizard?view=sql-server-ver17#why-would-i-use-this-wizard)
## Why would I use this wizard?
This wizard was created to improve the current import experience leveraging an intelligent framework known as Program Synthesis using Examples (
PROSE analyzes data patterns in your input file to infer column names, types, delimiters, and more. This framework learns the structure of the file and does all of the hard work so users don't have to.
[](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/import-flat-file-wizard?view=sql-server-ver17#prerequisites)
## Prerequisites
Install the latest version of [SQL Server Management Studio (SSMS)](https://learn.microsoft.com/en-us/ssms/install/install).
[](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/import-flat-file-wizard?view=sql-server-ver17#started)
## Getting Started
To access the Import Flat File Wizard, follow these steps:
  1. Open **SQL Server Management Studio**.
  2. Connect to an instance of the SQL Server Database Engine or localhost.
  3. Expand **Databases** , right-click a database (test in the following example), point to **Tasks** , and select **Import Flat File** above Import Data.


![Screenshot of Import Flat File menu.](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/media/import-flat-file-wizard/import-flat-file-menu.png?view=sql-server-ver17)
To learn more about the different functions of the wizard, refer to the following tutorial:
[](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/import-flat-file-wizard?view=sql-server-ver17#tutorial)
## Tutorial
For the purposes of this tutorial, feel free to use your own flat file. Otherwise, this tutorial is using the following CSV from Excel, which you're free to copy. If you use this CSV, title it **example.csv** and make sure to save it as a csv in an easy location such as your desktop.
![Screenshot of Excel.](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/media/import-flat-file-wizard/import-flat-file-example.png?view=sql-server-ver17)
Overview:
  1. [Access Wizard](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/import-flat-file-wizard?view=sql-server-ver17#step-1-access-wizard-and-intro-page)
  2. [Specify Input File](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/import-flat-file-wizard?view=sql-server-ver17#step-2-specify-input-file)
  3. [Preview Data](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/import-flat-file-wizard?view=sql-server-ver17#step-3-preview-data)
  4. [Modify Columns](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/import-flat-file-wizard?view=sql-server-ver17#step-4-modify-columns)
  5. [Summary](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/import-flat-file-wizard?view=sql-server-ver17#step-5-summary)
  6. [Results](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/import-flat-file-wizard?view=sql-server-ver17#step-6-results)


[](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/import-flat-file-wizard?view=sql-server-ver17#step-1-access-wizard-and-intro-page)
### Step 1: Access Wizard and Intro Page
Access the wizard as described in [Getting Started](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/import-flat-file-wizard?view=sql-server-ver17#started).
The first page of the wizard is the welcome page. If you don't want to see this page again, feel free to select **Do not show this starting page again.**
[ ![Screenshot of Import Flat File Wizard Introduction menu.](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/media/import-flat-file-wizard/import-flat-file-intro.png?view=sql-server-ver17) ](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/media/import-flat-file-wizard/import-flat-file-intro.png?view=sql-server-ver17#lightbox)
[](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/import-flat-file-wizard?view=sql-server-ver17#step-2-specify-input-file)
### Step 2: Specify Input File
Select browse to select your input file. At default, the wizard searches for .csv and .txt files. PROSE detects if the file is comma-separated or fixed-width format regardless of file extension.
The new table name should be unique, and the wizard doesn't allow you to move further if not.
[ ![Screenshot of Import Flat File Wizard Specify Input File menu.](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/media/import-flat-file-wizard/import-flat-file-specify.png?view=sql-server-ver17) ](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/media/import-flat-file-wizard/import-flat-file-specify.png?view=sql-server-ver17#lightbox)
[](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/import-flat-file-wizard?view=sql-server-ver17#step-3-preview-data)
### Step 3: Preview Data
The wizard generates a preview that you can view for the first 50 rows. If there are any problems, select cancel, otherwise proceed to the next page.
[ ![Screenshot of Import Flat File Wizard Preview Data menu.](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/media/import-flat-file-wizard/import-flat-file-preview.png?view=sql-server-ver17) ](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/media/import-flat-file-wizard/import-flat-file-preview.png?view=sql-server-ver17#lightbox)
[](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/import-flat-file-wizard?view=sql-server-ver17#step-4-modify-columns)
### Step 4: Modify Columns
The wizard identifies what it believes are the correct column names, data types, etc. Here's where you can edit the fields if they're incorrect (for example, data type should be a float instead of an int).
Columns where empty values are detected will have "Allow Nulls" checked. However if you expect nulls in a column and "Allow Nulls" isn't checked, here's where you can update the table definition to allow nulls in one or all columns.
Proceed when ready.
[ ![Screenshot of Import Flat File Wizard Modify Columns menu.](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/media/import-flat-file-wizard/import-flat-file-modify.png?view=sql-server-ver17) ](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/media/import-flat-file-wizard/import-flat-file-modify.png?view=sql-server-ver17#lightbox)
[](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/import-flat-file-wizard?view=sql-server-ver17#step-5-summary)
### Step 5: Summary
This is simply a summary page displaying your current configuration. If there are issues, you can go back to previous sections. Otherwise, selecting finish attempts the import process.
[ ![Screenshot of Import Flat File Wizard Summary menu.](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/media/import-flat-file-wizard/import-flat-file-summary.png?view=sql-server-ver17) ](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/media/import-flat-file-wizard/import-flat-file-summary.png?view=sql-server-ver17#lightbox)
[](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/import-flat-file-wizard?view=sql-server-ver17#step-6-results)
### Step 6: Results
This page indicates whether the import was successful. If a green check mark appears, it was a success, otherwise you might need to review your configuration or input file for any errors.
[ ![Screenshot of Import Flat File Wizard Results menu.](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/media/import-flat-file-wizard/import-flat-file-results.png?view=sql-server-ver17) ](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/media/import-flat-file-wizard/import-flat-file-results.png?view=sql-server-ver17#lightbox)
[](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/import-flat-file-wizard?view=sql-server-ver17#troubleshooting)
## Troubleshooting
The Import Flat File Wizard detects the data types based on the first 200 rows. In scenarios where data further in the flat file doesn't conform to the automatically detected data types, an error occurs during import. The error message would be similar to the following:
Output
Copy
```
Error inserting data into table. (Microsoft.SqlServer.Prose.Import)
The given value of type String from the data source cannot be converted to type nvarchar of the specified target column. (System.Data)
String or binary data would be truncated. (System.Data)

```

Tactics to alleviate this error:
  * Expanding the data type sizes in the [Modify Columns step](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/import-flat-file-wizard?view=sql-server-ver17#step-4-modify-columns), such as the length of a nvarchar column, might compensate for variations in the data from the remainder of the flat file.
  * Enabling error reporting in the [Modify Columns step](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/import-flat-file-wizard?view=sql-server-ver17#step-4-modify-columns), especially by a smaller number, will reveal which rows in the flat file contain data that doesn't fit the selected data types. For example, in a flat file where the second row introduces an error, running the import with error reporting with a range of 1 provides a specific error message. Examining the file directly at the location can provide more targeted changes to the data types based on the data in the identified rows.


[ ![Screenshot of an error in the Import Flat File Wizard reporting results.](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/media/import-flat-file-wizard/import-flat-file-error.png?view=sql-server-ver17) ](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/media/import-flat-file-wizard/import-flat-file-error.png?view=sql-server-ver17#lightbox)
Output
Copy
```
Error inserting data into table occurred while inserting rows 1 - 2. (Microsoft.SqlServer.Prose.Import)
The given value of type String from the data source cannot be converted to type float of the specified target column. (System.Data)
Failed to convert parameter value from a String to a Double. (System.Data)

```

Currently, the importer uses encoding based on the system's active code page. On most machines this defaults to ANSI.
[](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/import-flat-file-wizard?view=sql-server-ver17#related-content)
## Related content
Learn more about the wizard.
  * **Learn more about importing other sources.** If you're looking to import more than flat files, see [Import and Export Data with the SQL Server Import and Export Wizard](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/import-and-export-data-with-the-sql-server-import-and-export-wizard?view=sql-server-ver17).
  * **Learn more about connecting to flat file sources.** If you're looking for more information about connecting to flat file sources, see [Connect to a Flat File Data Source (SQL Server Import and Export Wizard)](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/connect-to-a-flat-file-data-source-sql-server-import-and-export-wizard?view=sql-server-ver17).
  * **Learn more about PROSE.** If you're looking for an overview of the intelligent framework used by this wizard, see


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
  * [ Import Data from Excel to SQL Server or Azure SQL Database - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/import-data-from-excel-to-sql?source=recommendations)
This article describes methods to import data from Excel to SQL Server or Azure SQL Database. Some use a single step, others require an intermediate text file.
  * [ Bulk Import and Export of Data (SQL Server) - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/bulk-import-and-export-of-data-sql-server?source=recommendations)
SQL Server supports exporting data in bulk from a SQL Server table and importing bulk data into a SQL Server table or nonpartitioned view.
  * [ Start the SQL Server Import and Export Wizard - Integration Services (SSIS) ](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/start-the-sql-server-import-and-export-wizard?source=recommendations)
Start the SQL Server Import and Export Wizard
  * [ Connect to a Flat File Data Source (SQL Server Import and Export Wizard) - SQL Server Integration Services (SSIS) ](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/connect-to-a-flat-file-data-source-sql-server-import-and-export-wizard?source=recommendations)
Connect to a Flat File Data Source (SQL Server Import and Export Wizard)
  * [ Use BULK INSERT or OPENROWSET(BULK...) to import data to SQL Server - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/import-bulk-data-by-using-bulk-insert-or-openrowset-bulk-sql-server?source=recommendations)
Find out how to use Transact-SQL statements to bulk import data from a file to a SQL Server or Azure SQL Database table, including security considerations.
  * [ BULK INSERT (Transact-SQL) - SQL Server ](https://learn.microsoft.com/en-us/sql/t-sql/statements/bulk-insert-transact-sql?source=recommendations)
Transact-SQL reference for the BULK INSERT statement.
  * [ Column Mappings (SQL Server Import and Export Wizard) - SQL Server Integration Services (SSIS) ](https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/column-mappings-sql-server-import-and-export-wizard?source=recommendations)
Column Mappings (SQL Server Import and Export Wizard)
  * [ IServerVirtualDeviceSet2::ExecuteCompletionAgent - SQL Server VDI reference ](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/vdi-reference/iservervirtualdeviceset2-executecompletionagent?source=recommendations)
This article provides reference for the IServerVirtualDeviceSet2::ExecuteCompletionAgent command.


Show 5 more
Module
[ Use Power Query to load data in Dataverse - Training ](https://learn.microsoft.com/en-us/training/modules/use-power-query/?source=recommendations)
Learn how to synchronize data from different sources to a Microsoft Dataverse table using Power Query and create dataflows in Power Apps.
Mar 8, 4 PM - Mar 8, 4 PM
Experiment with what's next in AI-driven apps and agent design
* * *
  * Last updated on 11/25/2025


##  In this article
  1. [Why would I use this wizard?](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/import-flat-file-wizard?view=sql-server-ver17#why-would-i-use-this-wizard)
  2. [Prerequisites](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/import-flat-file-wizard?view=sql-server-ver17#prerequisites)
  3. [Getting Started](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/import-flat-file-wizard?view=sql-server-ver17#started)
  4. [Tutorial](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/import-flat-file-wizard?view=sql-server-ver17#tutorial)
  5. [Troubleshooting](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/import-flat-file-wizard?view=sql-server-ver17#troubleshooting)
  6. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/import-flat-file-wizard?view=sql-server-ver17#related-content)


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
[ Sign in ](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/import-flat-file-wizard?view=sql-server-ver17)
[English (United States)](https://learn.microsoft.com/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fsql%2Frelational-databases%2Fimport-export%2Fimport-flat-file-wizard%3Fview%3Dsql-server-ver17)
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
