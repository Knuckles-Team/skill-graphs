## Download the latest version of the bcp utility
The command-line tools are General Availability (GA), however they're being released with the installer package for SQL Server 2019 (15.x) and later versions.
  * [Windows](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#tabpanel_1_windows)
  * [Linux and macOS](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#tabpanel_1_linux)


![](https://learn.microsoft.com/en-us/sql/includes/media/download.svg?view=sql-server-ver17) [Download ODBC Driver for SQL Server](https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver17)
![](https://learn.microsoft.com/en-us/sql/includes/media/download.svg?view=sql-server-ver17) [Download Microsoft Command Line Utilities 15 for SQL Server (x64)](https://go.microsoft.com/fwlink/?linkid=2230791)
![](https://learn.microsoft.com/en-us/sql/includes/media/download.svg?view=sql-server-ver17) [Download Microsoft Command Line Utilities 15 for SQL Server (x86)](https://go.microsoft.com/fwlink/?linkid=2231320)
For instructions on installing **sqlcmd** and **bcp** on Linux and macOS, see [Install the sqlcmd and bcp SQL Server command-line tools on Linux](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-setup-tools?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#version-information)
### Version information
  * Release number: 15.0.4298.1
  * Build number: 15.0.4298.1
  * Release date: April 7, 2023


**bcp** supports Microsoft Entra authentication, including multifactor authentication (MFA) support for Azure SQL Database, SQL database in Microsoft Fabric, and Azure Synapse Analytics.
[Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/fundamentals/new-name) was previously known as Azure Active Directory (Azure AD).
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#system-requirements)
### System requirements
  * [Windows](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#tabpanel_2_windows)
  * [Linux and macOS](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#tabpanel_2_linux)


  * Windows 10 and later versions
  * Windows Server 2016 and later versions


This component requires the latest [Microsoft ODBC Driver 17 for SQL Server](https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver17#version-17).
To check the **bcp** version, execute `bcp -v` command, and confirm that 15.0.4298.1 or later is in use.
**sqlcmd** and **bcp** are available on Linux. For more information, see [Install the sqlcmd and bcp SQL Server command-line tools on Linux](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-setup-tools?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver17&tabs=linux#tds-80-support)
