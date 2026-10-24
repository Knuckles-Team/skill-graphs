## Command-line options
The following table lists the command-line options available in **bcp** , and which operating systems they support.
Expand table
Command-line option | Supported on Windows | Supported on Linux and macOS
---|---|---
**[[_database_name_.]](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#database_name) [_schema_](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#schema).{[_table_name_](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#table_name) | [_view_name_](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#view_name) | ["_query_ "](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#query)}** | Yes | Yes
**{[in](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#in) [_data_file_](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#data_file) | [out](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#out) [_data_file_](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#data_file) | [queryout](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#queryout) [_data_file_](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#data_file) | [format](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#format) nul}** | Yes | Yes
[**-a _packet_size_**](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-a-packet_size) | Yes | Yes
[**-b _batch_size_**](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-b-batch_size) | Yes | Yes
[**-c**](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-c) | Yes | Yes
[**-C { ACP | OEM | RAW |_code_page_ }**](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-c--acp--oem--raw--code_page-) | Yes | No
[**-d _database_name_**](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-d-database_name) | Yes | Yes
[**-D**](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-d) | Yes | Yes
[**-e _err_file_**](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-e-err_file) | Yes | Yes
[**-E**](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-e) | Yes | Yes
[**-f _format_file_**](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-f-format_file) | Yes | Yes
[**-F _first_row_**](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-f-first_row) | Yes | Yes
[**-G Microsoft Entra authentication**](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-g) | Yes | Yes
[**-h"_hint_ [,..._n_]"**](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-h-hints---n) | Yes | No
[**-i _input_file_**](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-i-input_file) | Yes | No
[**-k**](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-k) | Yes | Yes
[**-K _application_intent_**](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-k-application_intent) | Yes | Yes
[**-l _login_timeout_**](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-l-login_timeout) | Yes | Yes
[**-L _last_row_**](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-l-last_row) | Yes | Yes
[**-m _max_errors_**](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-m-max_errors) | Yes | Yes
[**-n**](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-n-native) | Yes | Yes
[**-N**](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-n-unicode) | Yes | No
[**-o _output_file_**](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-o-output_file) | Yes | No
[**-P _password_**](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-p-password) | Yes | Yes
[**-q**](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-q) | Yes | Yes
[**-r _row_term_**](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-r-row_term) | Yes | Yes
[**-R**](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-r) | Yes | Yes
[**-S [_server_name_[\_instance_name_]]**](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-s-server_nameinstance_name) | Yes | Yes
[**-t _field_term_**](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-t-field_term) | Yes | Yes
[**-T**](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-t) | Yes | Yes
[**-U _login_id_**](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-u-login_id) | Yes | Yes
[**-u**](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-u) | Yes 1 | Yes
[**-v**](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-v) | Yes | Yes
[**-V (80 | 90 | 100 | 110 | 120 | 130 | 140 | 150 | 160 | 170 )**](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-v--80--90--100--110--120--130--140--150--160--170-) | Yes | No
[**-w**](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-w) | Yes | Yes
[**-x**](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-x) | Yes | No
[**-Y[s|m|o]**](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-ysmo) | Yes 1 | Yes
[**-z**](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-z) | No | Yes 2
1 SQL Server 2025 (17.x) and later versions.
2 ODBC 18.6.1.1 and later versions.
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#database_name)
#### _database_name_
The name of the database in which the specified table or view resides. If not specified, this is the default database for the user.
You can also explicitly specify the database name with `-d`.
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#schema)
#### _schema_
The name of the owner of the table or view. _schema_ is optional if the user performing the operation owns the specified table or view. If _schema_ isn't specified, and the user performing the operation doesn't own the specified table or view, SQL Server returns an error message, and the operation is canceled.
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#table_name)
#### _table_name_
The name of the destination table when importing data into SQL Server (`in`), and the source table when exporting data from SQL Server (`out`).
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#view_name)
#### _view_name_
The name of the destination view when copying data into SQL Server (`in`), and the source view when copying data from SQL Server (`out`). Only views in which all columns refer to the same table can be used as destination views. For more information on the restrictions for copying data into views, see [INSERT](https://learn.microsoft.com/en-us/sql/t-sql/statements/insert-transact-sql?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#query)
#### "_query_ "
A Transact-SQL query that returns a result set. If the query returns multiple result sets, only the first result set is copied to the data file; subsequent result sets are ignored. Use double quotation marks around the query and single quotation marks around anything embedded in the query. `queryout` must also be specified when bulk copying data from a query.
The query can reference a stored procedure as long as all tables referenced inside the stored procedure exist before executing the **bcp** statement. For example, if the stored procedure generates a temp table, the **bcp** statement fails because the temp table is available only at run time and not at statement execution time. In this case, consider inserting the results of the stored procedure into a table and then use **bcp** to copy the data from the table into a data file.
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#in)
#### in
Copies from a file into the database table or view. Specifies the direction of the bulk copy.
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#out)
#### out
Copies from the database table or view to a file. Specifies the direction of the bulk copy.
If you specify an existing file, the file is overwritten. When the **bcp** utility extracts data, it represents an empty string as a null, and a null string as an empty string.
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#data_file)
#### _data_file_
The full path of the data file. When data is bulk imported into SQL Server, the data file contains the data to be copied into the specified table or view. When data is bulk exported from SQL Server, the data file contains the data copied from the table or view. The path can have from 1 through 255 characters. The data file can contain a maximum of 2^63 - 1 rows.
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#queryout)
#### queryout
Copies from a query and must be specified only when bulk copying data from a query.
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#format)
#### format
Creates a format file based on the option specified (`-n`, `-c`, `-w`, or `-N`) and the table or view delimiters. When bulk copying data, the **bcp** command can refer to a format file, which saves you from reentering format information interactively. The `format` option requires the `-f` option; creating an XML format file, also requires the `-x` option. For more information, see [Create a format file with bcp (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/create-a-format-file-sql-server?view=sql-server-ver17). You must specify `nul` as the value (`format nul`).
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-a-packet_size)
#### -a _packet_size_
Specifies the number of bytes, per network packet, sent to and from the server. A server configuration option can be set by using SQL Server Management Studio (or the `sp_configure` system stored procedure). However, the server configuration option can be overridden on an individual basis by using this option. _packet_size_ can be from 4,096 bytes to 65,535 bytes; the default is `4096`.
Increased packet size can enhance performance of bulk-copy operations. If a larger packet is requested but can't be granted, the default is used. The performance statistics generated by the **bcp** utility show the packet size used.
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-b-batch_size)
#### -b _batch_size_
Specifies the number of rows per batch of imported data. Each batch is imported and logged as a separate transaction that imports the whole batch before being committed. By default, all the rows in the data file are imported as one batch. To distribute the rows among multiple batches, specify a _batch_size_ that is smaller than the number of rows in the data file. If the transaction for any batch fails, only insertions from the current batch are rolled back. Batches already imported by committed transactions are unaffected by a later failure.
Don't use this option with the `-h "ROWS_PER_BATCH=<bb>"` option.
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-c)
#### -c
Performs the operation using a character data type. This option doesn't prompt for each field; it uses **char** as the storage type, without prefixes and with `\t` (tab character) as the field separator and `\r\n` (newline character) as the row terminator. `-c` isn't compatible with `-w`.
For more information, see [Use character format to import or export data (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/use-character-format-to-import-or-export-data-sql-server?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-c--acp--oem--raw--code_page-)
#### -C { ACP | OEM | RAW | _code_page_ }
**Applies to** : Windows only. Not supported on Linux and macOS.
Specifies the code page of the data in the data file. _code_page_ is relevant only if the data contains **char** , **varchar** , or **text** columns with character values greater than 127 or less than 32.
You should specify a collation name for each column in a format file, except when you want the 65001 option to have priority over the collation/code page specification.
Expand table
Code page value | Description
---|---
`ACP` | ANSI/Microsoft Windows (ISO 1252).
`OEM` | Default code page used by the client. This is the default code page used if `-C` isn't specified.
`RAW` | No conversion from one code page to another occurs. This is the fastest option because no conversion occurs.
`<code_page>` | Specific code page number; for example, 850.

Versions before version 13 (SQL Server 2016 (13.x)) don't support code page 65001 (UTF-8 encoding). Versions beginning with 13 can import UTF-8 encoding to earlier versions of SQL Server.
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-d-database_name)
#### -d _database_name_
Specifies the database to connect to. By default, **bcp** connects to the user's default database. If `-d <database_name>` and a three part name (database_name.schema.table, passed as the first parameter to **bcp**) are specified, an error occurs because you can't specify the database name twice. If _database_name_ begins with a hyphen (`-`) or a forward slash (`/`), don't add a space between `-d` and the database name.
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-d)
#### -D
Causes the value passed to the `bcp -S` option to be interpreted as a data source name (DSN).
A DSN can be used to:
  * embed driver options to simplify command lines,
  * enforce driver options that aren't otherwise accessible from the command line such as MultiSubnetFailover,
  * or to help protect sensitive credentials from being discoverable as command line arguments.


For more information, see [DSN support in sqlcmd and bcp](https://learn.microsoft.com/en-us/sql/tools/sqlcmd/sqlcmd-utility?view=sql-server-ver17#dsn-support-in-sqlcmd-and-bcp).
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-e-err_file)
#### -e _err_file_
Specifies the full path of an error file used to store any rows that the **bcp** utility can't transfer from the file to the database. Error messages from the **bcp** command go to the workstation of the user. If this option isn't used, an error file isn't created.
If _err_file_ begins with a hyphen (`-`) or a forward slash (`/`), don't include a space between `-e` and the _err_file_ value.
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-e)
#### -E
Specifies that identity value or values in the imported data file are to be used for the identity column. If `-E` isn't given, the identity values for this column in the data file being imported are ignored, and SQL Server automatically assigns unique values based on the seed and increment values specified during table creation. For more information, see [DBCC CHECKIDENT](https://learn.microsoft.com/en-us/sql/t-sql/database-console-commands/dbcc-checkident-transact-sql?view=sql-server-ver17).
If the data file doesn't contain values for the identity column in the table or view, use a format file to specify that the identity column in the table or view should be skipped when importing data. SQL Server automatically assigns unique values for the column.
The `-E` option has a special permissions requirement. For more information, see "[Remarks](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#remarks)" later in this article.
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-f-format_file)
#### -f _format_file_
Specifies the full path of a format file. The meaning of this option depends on the environment in which it's used, as follows:
  * If `-f` is used with the `format` option, the specified _format_file_ is created for the specified table or view. To create an XML format file, also specify the `-x` option. For more information, see [Create a format file with bcp (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/create-a-format-file-sql-server?view=sql-server-ver17).
  * If used with the `in` or `out` option, `-f` requires an existing format file.
Using a format file in with the `in` or `out` option is optional. In the absence of the `-f` option, if `-n`, `-c`, `-w`, or `-N` isn't specified, the command prompts for format information and lets you save your responses in a format file (whose default file name is `bcp.fmt`).


If _format_file_ begins with a hyphen (`-`) or a forward slash (`/`), don't include a space between `-f` and the _format_file_ value.
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-f-first_row)
#### -F _first_row_
Specifies the number of the first row to export from a table or import from a data file. This parameter requires a value greater than (`>`) 0 but less than (`<`) or equal to (`=`) the total number rows. In the absence of this parameter, the default is the first row of the file.
_first_row_ can be a positive integer with a value up to 2^63-1. `-F` _first_row_ is 1-based.
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-g)
#### -G
**Applies to** : Azure SQL Database, SQL database in Microsoft Fabric, and Azure Synapse Analytics only.
This switch is used by the client to specify that the user is authenticated with Microsoft Entra ID. The `-G` switch requires [version 14.0.3008.27](https://go.microsoft.com/fwlink/?LinkID=825643) or later versions. To determine your version, execute `bcp -v`. For more information, see [Use Microsoft Entra authentication with SQL Database or Azure Synapse Analytics](https://learn.microsoft.com/en-us/azure/sql-database/sql-database-aad-authentication) or [Authentication in SQL database in Microsoft Fabric](https://learn.microsoft.com/en-us/fabric/database/sql/authentication).
On Linux and macOS, Microsoft Entra interactive authentication isn't currently supported. Microsoft Entra integrated authentication requires [Microsoft ODBC Driver 17 for SQL Server](https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver17) version 17.6.1 and later versions, and a properly [configured Kerberos environment](https://learn.microsoft.com/en-us/sql/connect/odbc/linux-mac/using-integrated-authentication?view=sql-server-ver17#configure-kerberos).
To check if your version of **bcp** includes support for Microsoft Entra authentication, type `bcp --help` and verify that you see `-G` in the list of available arguments.
  * **Microsoft Entra username and password**
When you want to use a Microsoft Entra username and password, you can provide the `-G` option and also use the username and password by providing the `-U` and `-P` options.
The following example exports data using Microsoft Entra username and password credentials. The example exports table `bcptest` from database `testdb` from Azure server `aadserver.database.windows.net` and stores the data in file `c:\last\data1.dat`:
Windows Command Prompt
Copy
```
bcp bcptest out "c:\last\data1.dat" -c -S aadserver.database.windows.net -d testdb -G -U alice@aadtest.onmicrosoft.com -P xxxxx

```

The following example imports data using the credentials of a Microsoft Entra user. The example imports data from file `c:\last\data1.dat` into table `bcptest` for database `testdb` on Azure server `aadserver.database.windows.net` using a Microsoft Entra username and password:
Windows Command Prompt
Copy
```
bcp bcptest in "c:\last\data1.dat" -c -S aadserver.database.windows.net -d testdb -G -U alice@aadtest.onmicrosoft.com -P xxxxx

```

  * **Microsoft Entra integrated**
For Microsoft Entra integrated authentication, provide the `-G` option without a username or password. This configuration requires that the current Windows user account (the account the **bcp** command is running under) is federated with Microsoft Entra ID:
The following example exports data using Microsoft Entra integrated authentication. The example exports table `bcptest` from database `testdb` on the logical server `aadserver.database.windows.net` and stores the data in file `c:\last\data2.dat`, using Windows credentials federated with Microsoft Entra ID:
Windows Command Prompt
Copy
```
bcp bcptest out "c:\last\data2.dat" -S aadserver.database.windows.net -d testdb -G -c

```

The following example imports data using Microsoft Entra integrated authentication. The example imports data from file table `c:\last\data2.dat` into table `bcptest` in the database `testdb` on the logical server `aadserver.database.windows.net`, using Windows credentials federated with Microsoft Entra ID:
Windows Command Prompt
Copy
```
bcp bcptest in "c:\last\data2.dat" -S aadserver.database.windows.net -d testdb -G -c

```

  * **Microsoft Entra Managed Service Identity**
**bcp** is tightly coupled with the driver. The major versions of both **bcp** and the driver a DSN is created with must be the same. To determine your version, execute `bcp -v`.
    * [Windows](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#tabpanel_3_windows)
    * [Linux and macOS](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#tabpanel_3_linux)
Exporting data via **bcp** using a Managed Service Identity on Windows requires a DSN be configured.
To configure a DSN on a machine running Windows:
    1. Press the Windows key on your keyboard
    2. Type `ODBC` and select the appropriate version of the **ODBC Data Source Administrator**
    3. Select either the **User DSN** or **System DSN** tab
    4. Select **Add** and follow the prompts
    5. When asked for an authentication type select **Azure Managed Service Identity authentication**
    6. If you have a User Assigned Managed Identity, paste the `Object (principal) ID` of the identity into the **Login ID** box at the bottom of the authentication tab
    7. To configure your DSN, continue following the prompts.
For a full walkthrough including screenshots, see [Creating and editing DSNs in the UI](https://learn.microsoft.com/en-us/sql/connect/odbc/using-azure-active-directory?view=sql-server-ver17#creating-and-editing-dsns-in-the-ui).
Once the DSN is configured, **bcp** can then be called using `-D` flag to indicate the value passed for `-S` is a DSN.
Windows Command Prompt
Copy
```
bcp bcptest out "c:\last\data1.dat" -c -D -S myDSN -d testdb

```

Exporting data via **bcp** using a Managed Service Identity on Linux can be configured using a DSN.
For this example, a user DSN was created by editing the user `.odbc.ini` file using the following command. `odbcinst -j` can be used to view where DSN files are located.
Bash
Copy
```
vi /home/<user>/.odbc.ini

```

Here's an example of the lines to add after any existing DSNs in the file. The line with `LastUser` should be removed when using System Assigned Managed Identities.
ini
Copy
```
[myDSN]
Driver = ODBC Driver 18 for SQL Server
Server = aadserver.database.windows.net
Database = testdb
Encrypt = yes
LastUser = <object_id_of_user_assigned_managed_identity>
Authentication = ActiveDirectoryMSI

```

Once the DSN is configured, **bcp** can then be called using `-D` flag to indicate the value passed for `-S` is a DSN.
Bash
Copy
```
bcp bcptest out data1.dat -c -D -S myDSN -d testdb

```



* * *
  * **Microsoft Entra ID access token**
**Applies to** : Linux and macOS only. Windows isn't supported.
Users of **bcp** 17.8 and later versions, on Linux and macOS, can also authenticate with a token. The following examples use [PowerShell on Linux](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-linux) to retrieve an access token.
This example retrieves an access token and places it into a file to export data using a system-assigned managed identity.
Bash
Copy
```
Connect-AzAccount -Identity
$access_token | cut -f 1 | tr -d '\n' | iconv -f ascii -t UTF-16LE > /tmp/tokenFile
bcp bcptest out data2.dat -S aadserver.database.windows.net -d testdb -G -P /tmp/tokenFile -c

```

This example passes a `Client ID` to the `-AccountId` parameter of `Connect-AzAccount` to retrieve an access token and place it into a token file. The token is then used to export data using the specified User Assigned Managed Identity.
Bash
Copy
```
Connect-AzAccount -Identity -AccountId 'client_id_of_user_assigned_managed_identity'
$access_token | cut -f 1 | tr -d '\n' | iconv -f ascii -t UTF-16LE > /tmp/tokenFile
bcp bcptest out data2.dat -S aadserver.database.windows.net -d testdb -G -P /tmp/tokenFile -c

```

  * **Microsoft Entra interactive**
**Applies to** : Windows only. Linux and macOS aren't supported.
Microsoft Entra interactive authentication, available for all Azure SQL, and SQL Server 2022 (16.x) and later versions, allows you to use an interactive dialog to authenticate, which also supports multifactor authentication.
Microsoft Entra interactive authentication requires **bcp** [version 15.0.1000.34](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#download-the-latest-version-of-the-bcp-utility) or later, and [ODBC version 17.2 or later](https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver17).
To enable interactive authentication, provide the `-G` option with user name (`-U`) only, and no password.
The following example exports data using Microsoft Entra interactive authentication, which includes specifying the username of a Microsoft Entra account.
Interactive mode requires a password to be manually entered, or for accounts with multifactor authentication enabled, complete your configured MFA authentication method.
Windows Command Prompt
Copy
```
bcp bcptest out "c:\last\data1.dat" -c -S aadserver.database.windows.net -d testdb -G -U alice@aadtest.onmicrosoft.com

```

If using a Microsoft Entra user that's a Windows account from a federated domain, the username entered in the command line must contain its domain (for example, `joe@contoso.com`):
Windows Command Prompt
Copy
```
bcp bcptest out "c:\last\data1.dat" -c -S aadserver.database.windows.net -d testdb -G -U joe@contoso.com

```

If guest users exist in a specific Microsoft Entra tenant and are part of a group that exists in Azure SQL Database that has database permissions to execute the **bcp** command, their guest user alias is used (for example, `keith0@adventure-works.com`).


[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-h-hints---n)
#### -h "_hints_ [, ... _n_]"
**Applies to** : Windows only. Not supported on Linux and macOS.
Specifies the hint or hints to be used during a bulk import of data into a table or view.
  * **ORDER (_column_ [ASC | DESC] [, ..._n_])**
The sort order of the data in the data file. Bulk import performance is improved if the data being imported is sorted according to the clustered index on the table, if any. If the data file is sorted in a different order, that is, other than the order of a clustered index key, or if there's no clustered index on the table, the `ORDER` clause is ignored. The column names supplied must be valid column names in the destination table. By default, **bcp** assumes the data file is unordered. For optimized bulk import, SQL Server also validates that the imported data is sorted.
  * **ROWS_PER_BATCH =_bb_**
Number of rows of data per batch (as _bb_). Used when `-b` isn't specified, resulting in the entire data file being sent to the server as a single transaction. The server optimizes the bulkload according to the value _bb_. By default, `ROWS_PER_BATCH` is unknown.
  * **KILOBYTES_PER_BATCH =_cc_**
Approximate number of kilobytes of data per batch (as _cc_). By default, `KILOBYTES_PER_BATCH` is unknown.
  * **TABLOCK**
Specifies that a bulk update table-level lock is acquired during the bulkload operation; otherwise, a row-level lock is acquired. This hint significantly improves performance because holding a lock during the bulk-copy operation reduces lock contention on the table. A table can be loaded concurrently from multiple clients if the table has no indexes and `TABLOCK` is specified. By default, locking behavior is determined by the table option `table lock on bulkload`. For more information, see [sp_tableoption](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-tableoption-transact-sql?view=sql-server-ver17).
If the target table is clustered columnstore index, `TABLOCK` hint isn't required for loading by multiple concurrent clients because each concurrent thread is assigned a separate rowgroup within the index and loads data into it. For more information, see [Columnstore indexes: overview](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/columnstore-indexes-overview?view=sql-server-ver17).
  * **CHECK_CONSTRAINTS**
Specifies that all constraints on the target table or view must be checked during the bulk-import operation. Without the `CHECK_CONSTRAINTS` hint, any `CHECK`, and `FOREIGN KEY` constraints are ignored, and after the operation the constraint on the table is marked as not-trusted.
`UNIQUE`, `PRIMARY KEY`, and `NOT NULL` constraints are always enforced.
At some point, you need to check the constraints on the entire table. If the table was nonempty before the bulk import operation, the cost of revalidating the constraint can exceed the cost of applying `CHECK` constraints to the incremental data. Therefore, we recommend that normally you enable constraint checking during an incremental bulk import.
A situation in which you might want constraints disabled (the default behavior) is if the input data contains rows that violate constraints. With `CHECK` constraints disabled, you can import the data and then use Transact-SQL statements to remove data that isn't valid.
**bcp** now enforces data validation and data checks that can cause scripts to fail if they're executed on invalid data in a data file.
The `-m` _max_errors_ switch doesn't apply to constraint checking.
  * **FIRE_TRIGGERS**
When you specify this option with the _in_ argument, any insert triggers defined on the destination table run during the bulk-copy operation. If `FIRE_TRIGGERS` isn't specified, no insert triggers run. `FIRE_TRIGGERS` is ignored for the `out`, `queryout`, and `format` arguments.


[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-i-input_file)
#### -i _input_file_
**Applies to** : Windows only. Not supported on Linux and macOS.
Specifies the name of a response file, containing the responses to the command prompt questions for each data field when a bulk copy is being performed using interactive mode (`-n`, `-c`, `-w`, or `-N` not specified).
If _input_file_ begins with a hyphen (`-`) or a forward slash (`/`), don't include a space between `-i` and the _input_file_ value.
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-k)
#### -k
Specifies that empty columns should retain a null value during the operation, rather than have any default values for the columns inserted. For more information, see [Keep nulls or default values during bulk import (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/keep-nulls-or-use-default-values-during-bulk-import-sql-server?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-k-application_intent)
#### -K _application_intent_
Declares the application workload type when connecting to a server. The only value that is possible is `ReadOnly`. If `-K` isn't specified, the **bcp** utility doesn't support connectivity to a secondary replica in an Always On availability group. For more information, see [Offload read-only workload to secondary replica of an Always On availability group](https://learn.microsoft.com/en-us/sql/database-engine/availability-groups/windows/active-secondaries-readable-secondary-replicas-always-on-availability-groups?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-l-login_timeout)
#### -l _login_timeout_
Specifies a login timeout. The `-l` option specifies the number of seconds before a login to SQL Server times out when you try to connect to a server. The default login timeout is 15 seconds. The login timeout must be a number between 0 and 65534. If the value supplied isn't numeric or doesn't fall into that range, **bcp** generates an error message. A value of 0 specifies an infinite timeout.
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-l-last_row)
#### -L _last_row_
Specifies the number of the last row to export from a table or import from a data file. This parameter requires a value greater than (`>`) 0 but less than (`<`) or equal to (`=`) the number of the last row. In the absence of this parameter, the default is the last row of the file.
_last_row_ can be a positive integer with a value up to 2^63-1.
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-m-max_errors)
#### -m _max_errors_
Specifies the maximum number of syntax errors that can occur before the **bcp** operation is canceled. A syntax error implies a data conversion error to the target data type. The _max_errors_ total excludes any errors that can be detected only at the server, such as constraint violations.
A row that can't be copied by the **bcp** utility is ignored and is counted as one error. If this option isn't included, the default is 10.
The `-m` option also doesn't apply to converting the **money** or **bigint** data types.
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-n)
#### -n
Performs the bulk-copy operation using the native (database) data types of the data. This option doesn't prompt for each field; it uses the native values.
For more information, see [Use native format to import or export data (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/use-native-format-to-import-or-export-data-sql-server?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-n-1)
#### -N
**Applies to** : Windows only. Not supported on Linux and macOS.
Performs the bulk-copy operation using the native (database) data types of the data for noncharacter data, and Unicode characters for character data. This option offers a higher performance alternative to the `-w` option, and is intended for transferring data from one instance of SQL Server to another using a data file. It doesn't prompt for each field. Use this option when you're transferring data that contains ANSI extended characters and you want to take advantage of the performance of native mode.
For more information, see [Use Unicode Native Format to Import or Export Data (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/use-unicode-native-format-to-import-or-export-data-sql-server?view=sql-server-ver17).
If you export and then import data to the same table schema by using **bcp** with `-N`, you might see a truncation warning if there's a fixed length, non-Unicode character column (for example, **char(10)**).
The warning can be ignored. One way to resolve this warning is to use `-n` instead of `-N`.
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-o-output_file)
#### -o _output_file_
**Applies to** : Windows only. Not supported on Linux and macOS.
Specifies the name of a file that receives output redirected from the command prompt.
If _output_file_ begins with a hyphen (`-`) or a forward slash (`/`), don't include a space between `-o` and the _output_file_ value.
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-p-password)
#### -P _password_
Specifies the password for the login ID. If this option isn't used, the **bcp** command prompts for a password. If this option is used at the end of the command prompt without a password, **bcp** uses the default password (`NULL`).
Do not use a blank password. Use a strong password.
  * [Windows](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#tabpanel_4_windows)
  * [Linux and macOS](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#tabpanel_4_linux)


To mask your password, don't specify the `-P` option along with the `-U` option. Instead, after specifying **bcp** along with the `-U` option and other switches (don't specify `-P`), press the **Enter** key, and the command prompts you for a password. This method ensures that your password is masked when it's entered.
If _password_ begins with a hyphen (`-`) or a forward slash (`/`), don't add a space between `-P` and the _password_ value.
To mask your password, don't specify the `-P` option along with the `-U` option. Instead, after specifying **bcp** along with the `-U` option and other switches (don't specify `-P`), press the **Enter** key, and the command prompts you for a password. This method ensures that your password is masked when it's entered.
If _password_ begins with a hyphen (`-`) or a forward slash (`/`), don't add a space between `-P` and the _password_ value.
When used with the `-G` option without `-U`, specifies a file that contains an access token (v17.8+). The token file should be in UTF-16LE (no BOM) format.
Access tokens can be obtained via various methods. It's important to ensure the access token is correct byte-for-byte, because it's sent as-is. Following is an example command that obtains an access token. The command uses the Azure CLI and Linux commands and saves it to a file in the proper format. If your system or terminal's default encoding isn't ASCII or UTF-8, you might need to adjust the `iconv` options. Be sure to carefully secure the resulting file and delete it when it's no longer required.
Azure CLI
Copy
```
az account get-access-token --resource https://database.windows.net --output tsv | cut -f 1 | tr -d '\n' | iconv -f ascii -t UTF-16LE > /tmp/tokenFile

```

[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-q)
#### -q
Executes the `SET QUOTED_IDENTIFIER ON` statement in the connection between the **bcp** utility and an instance of SQL Server. Use this option to specify a database, owner, table, or view name that contains a space or a single quotation mark. Enclose the entire three-part table or view name in quotation marks (`""`).
To specify a database name that contains a space or single quotation mark, you must use the `-q` option.
`-q` doesn't apply to values passed to `-d`.
For more information, see the [Remarks](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#remarks) section in this article.
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-r-row_term)
#### -r _row_term_
Specifies the row terminator. The default is `\n` (newline character). Use this parameter to override the default row terminator. For more information, see [Specify field and row terminators (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/specify-field-and-row-terminators-sql-server?view=sql-server-ver17).
If you specify the row terminator in hexadecimal notation in a **bcp** command, the value is truncated at `0x00`. For example, if you specify `0x410041`, `0x41` is used.
If _row_term_ begins with a hyphen (`-`) or a forward slash (`/`), don't include a space between `-r` and the _row_term_ value.
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-r)
#### -R
Specifies that currency, date, and time data is bulk copied into SQL Server using the regional format defined for the locale setting of the client computer. By default, regional settings are ignored.
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-s-server_nameinstance_name)
#### -S [_server_name_[\_instance_name_]]
Specifies the name of the SQL Server instance to connect to, or if `-D` is used, a DSN.
If no server is specified, the **bcp** utility connects to the default instance of SQL Server on the local computer. This option is required when a **bcp** command is run from a remote computer on the network or a local named instance. To connect to the default instance of SQL Server on a server, specify only _server_name_. To connect to a named instance of SQL Server, specify _server_name_ **\\**_instance_name_.
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-t-field_term)
#### -t _field_term_
Specifies the field terminator. The default is `\t` (tab character). Use this parameter to override the default field terminator. For more information, see [Specify field and row terminators (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/specify-field-and-row-terminators-sql-server?view=sql-server-ver17).
If you specify the field terminator in hexadecimal notation in a **bcp** command, the value is truncated at `0x00`. For example, if you specify `0x410041`, `0x41` is used.
If _field_term_ begins with a hyphen (`-`) or a forward slash (`/`), don't include a space between `-t` and the _field_term_ value.
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-t)
#### -T
Specifies that the **bcp** utility connects to SQL Server with a trusted connection using integrated security. The security credentials of the network user, _login_id_ , and _password_ aren't required. If `-T` isn't specified, you need to specify `-U` and `-P` to successfully connect.
When the **bcp** utility is connecting to SQL Server with a trusted connection using integrated security, use the `-T` option (trusted connection) instead of the _username_ and _password_ combination. When the **bcp** utility is connecting to SQL Database or Azure Synapse Analytics, using Windows authentication or Microsoft Entra authentication isn't supported. Use the `-U` and `-P` options.
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-u-login_id)
#### -U _login_id_
Specifies the login ID used to connect to SQL Server.
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-u)
#### -u
**Applies to** : **bcp** version 18 and later versions.
Trust server certificate. When used with the Encrypt option for the connection, enables encryption using a self-signed server certificate.
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-v)
#### -v
Reports the **bcp** utility version number and copyright.
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-v--80--90--100--110--120--130--140--150--160--170-)
#### -V { 80 | 90 | 100 | 110 | 120 | 130 | 140 | 150 | 160 | 170 }
**Applies to** : Windows only. Not supported on Linux and macOS.
Performs the bulk-copy operation using data types from an earlier version of SQL Server. This option doesn't prompt for each field; it uses the default values.
  * `80` = SQL Server 2000 (8.x)
  * `90` = SQL Server 2005 (9.x)
  * `100` = SQL Server 2008 (10.0.x) and SQL Server 2008 R2 (10.50.x)
  * `110` = SQL Server 2012 (11.x)
  * `120` = SQL Server 2014 (12.x)
  * `130` = SQL Server 2016 (13.x)
  * `140` = SQL Server 2017 (14.x)
  * `150` = SQL Server 2019 (15.x)
  * `160` = SQL Server 2022 (16.x)
  * `170` = SQL Server 2025 (17.x)


For example, to generate data for types not supported by SQL Server 2000 (8.x), but were introduced in later versions of SQL Server, use the `-V80` option.
For more information, see [Import native and character format data from earlier versions of SQL Server](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/import-native-and-character-format-data-from-earlier-versions-of-sql-server?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-w)
#### -w
Performs the bulk copy operation using Unicode characters. This option doesn't prompt for each field; it uses **nchar** as the storage type, no prefixes, `\t` (tab character) as the field separator, and `\n` (newline character) as the row terminator. `-w` isn't compatible with `-c`.
For more information, see [Use Unicode character format to import or export data (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/use-unicode-character-format-to-import-or-export-data-sql-server?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-x)
#### -x
**Applies to** : Windows only. Not supported on Linux and macOS.
This option is used with the `format` and `-f` _format_file_ options, and generates an XML-based format file instead of the default non-XML format file. The `-x` doesn't work when importing or exporting data. It generates an error if used without both `format` and `-f` _format_file_.
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-ysmo)
#### -Y[s|m|o]
**Applies to** : **bcp** version 18 and later versions.
Specifies whether connections use TLS encryption over the network. `-Y` can be `o` (for `optional`), `m` (for `mandatory`, the default), or `s` (for `strict`). If you don't include `-Y`, `-Ym` (for `mandatory`) is the default.
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#-z)
#### -z
**Applies to** : **bcp** (ODBC), Linux and macOS only. Windows isn't supported.
Enables **vector** data type support in the **bcp** utility. This is currently disabled by default. When disabled, vector data is imported/exported as JSON float array strings. When enabled, and when connecting to SQL Server 2025 (17.x) and later versions, vector data is imported/exported in native **vector** binary.
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#remarks)
