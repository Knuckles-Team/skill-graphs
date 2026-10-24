##  In this article
  1. [Download the latest version of the bcp utility](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#download-the-latest-version-of-the-bcp-utility)
  2. [TDS 8.0 support](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#tds-80-support)
  3. [Syntax](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#syntax)
  4. [Considerations and limitations](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#considerations-and-limitations)
  5. [Command-line options](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#command-line-options)
  6. [Remarks](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#remarks)
  7. [Native data file support](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#native-data-file-support)
  8. [Computed columns and timestamp columns](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#computed-columns-and-timestamp-columns)
  9. [Specify identifiers that contain spaces or quotation marks](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#specify-identifiers-that-contain-spaces-or-quotation-marks)
  10. [Data validation](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#data-validation)
  11. [Bulk exporting or importing SQLXML documents](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#bulk-exporting-or-importing-sqlxml-documents)
  12. [Permissions](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#permissions)
  13. [Character mode (-c) and native mode (-n) best practices](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#character-mode--c-and-native-mode--n-best-practices)
  14. [Examples](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#examples)
  15. [Additional examples](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#additional-examples)
  16. [Related content](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#related-content)
  17. [Get help](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-get-help)
  18. [Contribute to SQL documentation](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-contribute-to-sql-documentation)

Show 14 more
**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Database](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure Synapse Analytics](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Analytics Platform System (PDW)](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL database in Microsoft Fabric](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to)
The bulk copy program utility (**bcp**) bulk copies data between an instance of SQL Server and a data file in a user-specified format.
For using **bcp** on Linux, see [Install the sqlcmd and bcp SQL Server command-line tools on Linux](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-setup-tools?view=sql-server-ver17). For detailed information about using **bcp** with Azure Synapse Analytics, see [Load data with bcp](https://learn.microsoft.com/en-us/azure/sql-data-warehouse/sql-data-warehouse-load-with-bcp).
The **bcp** utility can be used to import large numbers of new rows into SQL Server tables or to export data out of tables into data files. Except when used with the `queryout` option, the utility requires no knowledge of Transact-SQL. To import data into a table, you must either use a format file created for that table, or understand the structure of the table and the types of data that are valid for its columns.
If you use **bcp** to back up your data, create a format file to record the data format. **bcp** data files **don't include** any schema or format information, so if a table or view is dropped and you don't have a format file, you might be unable to import the data.
![](https://learn.microsoft.com/en-us/sql/includes/media/topic-link-icon.svg?view=sql-server-ver17) For the syntax conventions that are used for the **bcp** syntax, see [Transact-SQL syntax conventions](https://learn.microsoft.com/en-us/sql/t-sql/language-elements/transact-sql-syntax-conventions-transact-sql?view=sql-server-ver17).
For **bcp** on Linux and macOS, see [Considerations for bcp on Linux and macOS](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#considerations-for-bcp-on-linux-and-macos).
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#download-the-latest-version-of-the-bcp-utility)
##  In this article
  1. [Download the latest version of the bcp utility](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#download-the-latest-version-of-the-bcp-utility)
  2. [TDS 8.0 support](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#tds-80-support)
  3. [Syntax](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#syntax)
  4. [Considerations and limitations](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#considerations-and-limitations)
  5. [Command-line options](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#command-line-options)
  6. [Remarks](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#remarks)
  7. [Native data file support](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#native-data-file-support)
  8. [Computed columns and timestamp columns](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#computed-columns-and-timestamp-columns)
  9. [Specify identifiers that contain spaces or quotation marks](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#specify-identifiers-that-contain-spaces-or-quotation-marks)
  10. [Data validation](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#data-validation)
  11. [Bulk exporting or importing SQLXML documents](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#bulk-exporting-or-importing-sqlxml-documents)
  12. [Permissions](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#permissions)
  13. [Character mode (-c) and native mode (-n) best practices](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#character-mode--c-and-native-mode--n-best-practices)
  14. [Examples](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#examples)
  15. [Additional examples](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#additional-examples)
  16. [Related content](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#related-content)
  17. [Get help](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-get-help)
  18. [Contribute to SQL documentation](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-contribute-to-sql-documentation)

Show 9 more
Was this page helpful?
Yes No No
Need help with this topic?
Want to try using Ask Learn to clarify or guide you through this topic?
Ask Learn Ask Learn
Suggest a fix?
