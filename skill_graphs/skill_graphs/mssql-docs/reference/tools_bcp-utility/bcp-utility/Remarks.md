## Remarks
  * The **bcp** 13.0 client is installed when you install SQL Server 2019 (15.x) tools. If tools are installed for multiple versions of SQL Server, depending on the order of values of the `PATH` environment variable, you might be using the earlier **bcp** client instead of the **bcp** 13.0 client. This environment variable defines the set of directories used by Windows to search for executable files. To discover which version you're using, run the `bcp -v` command at the Windows Command Prompt. For information about how to set the command path in the `PATH` environment variable, see [Environment Variables](https://learn.microsoft.com/en-us/windows/win32/shell/user-environment-variables) or search for Environment Variables in Windows Help.
To make sure the newest version of the **bcp** utility is running, you need to remove any older versions of the **bcp** utility.
To determine where all versions of the **bcp** utility are installed, type in the command prompt:
Console
Copy
```
where bcp.exe

```

  * The **bcp** utility can also be downloaded separately from the [Microsoft SQL Server 2016 Feature Pack](https://www.microsoft.com/download/details.aspx?id=56833). Select either `ENU\x64\MsSqlCmdLnUtils.msi` or `ENU\x86\MsSqlCmdLnUtils.msi`.
  * XML format files are only supported when SQL Server tools are installed together with SQL Server Native Client.
  * For information about where to find or how to run the **bcp** utility and about the command prompt utilities syntax conventions, see [SQL command-line utilities (Database Engine)](https://learn.microsoft.com/en-us/sql/tools/command-prompt-utility-reference-database-engine?view=sql-server-ver17).
  * For information on preparing data for bulk import or export operations, see [Prepare data for bulk export or import](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/prepare-data-for-bulk-export-or-import-sql-server?view=sql-server-ver17).
  * For information about when row-insert operations that are performed by bulk import are logged in the transaction log, see [Prerequisites for minimal logging in bulk import](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/prerequisites-for-minimal-logging-in-bulk-import?view=sql-server-ver17).
  * [Using additional special characters](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/set_1#remarks)
The characters `<`, `>`, `|`, `&`, and `^` are special command shell characters, and they must be preceded by the escape character (`^`), or enclosed in quotation marks when used in String (for example, `"StringContaining&Symbol"`). If you use quotation marks to enclose a string that contains one of the special characters, the quotation marks are set as part of the environment variable value.


[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#native-data-file-support)
