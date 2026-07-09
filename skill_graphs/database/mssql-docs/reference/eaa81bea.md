# What is the MSSQL extension for Visual Studio Code?
Feedback
Summarize this article for me
##  In this article
  1. [Install the MSSQL Extension in Visual Studio Code](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/mssql-extension-visual-studio-code?view=sql-server-ver17#install-the-mssql-extension-in-visual-studio-code)
  2. [Modern UI](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/mssql-extension-visual-studio-code?view=sql-server-ver17#modern-ui)
  3. [Supported operating systems](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/mssql-extension-visual-studio-code?view=sql-server-ver17#supported-operating-systems)
  4. [Offline installation](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/mssql-extension-visual-studio-code?view=sql-server-ver17#offline-installation)
  5. [Feedback and support](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/mssql-extension-visual-studio-code?view=sql-server-ver17#feedback-and-support)
  6. [Related content](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/mssql-extension-visual-studio-code?view=sql-server-ver17#related-content)

Show 2 more
The
The extension includes advanced IntelliSense, Transact-SQL script execution, and customizable options to support SQL development for local and cloud-based databases.
[](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/mssql-extension-visual-studio-code?view=sql-server-ver17#install-the-mssql-extension-in-visual-studio-code)
## Install the MSSQL Extension in Visual Studio Code
To get started with SQL development in Visual Studio Code, install the **MSSQL extension** :
  1. Open **Visual Studio Code**.
  2. Select the **Extensions** icon in the Activity Bar (**Cmd** +**Shift** +**X** on macOS, or **Ctrl** +**Shift** +**X** on Windows and Linux).
  3. In the **search bar** , type `mssql`.
  4. Find **SQL Server (mssql)** in the results and select it.
  5. Select the **Install** button.


[ ![Screenshot of the MSSQL extension in Visual Studio Code.](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/media/mssql-extension-visual-studio-code/mssql-extension-vscode.png?view=sql-server-ver17) ](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/media/mssql-extension-visual-studio-code/mssql-extension-vscode.png?view=sql-server-ver17#lightbox)
You know the extension is installed correctly when the **MSSQL** icon appears in the Activity Bar and the **Connections** view becomes available.
[](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/mssql-extension-visual-studio-code?view=sql-server-ver17#modern-ui)
## Modern UI
The MSSQL extension for Visual Studio Code elevates the SQL development experience across SQL Server, Azure SQL, and SQL database on Fabric.
This experience delivers the following integrated features, which are enabled by default:
  * **Connection Dialog**
  * **Object Explorer (filtering)**
  * **Table Designer**
  * **Query Results Pane**
  * **Query Plan Visualizer**


[](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/mssql-extension-visual-studio-code?view=sql-server-ver17#connection-dialog)
### Connection dialog
The Connection dialog provides a simple and intuitive interface for connecting to databases hosted in Azure SQL (including Azure SQL Database, Azure SQL Managed Instance, and SQL Server on Azure VMs), SQL database in Fabric, or SQL Server. It offers multiple input options to cater to different scenarios:
  * **Parameters** : Enter individual connection details such as server name, database name, username, and password.
  * **Connection String** : Directly input a complete connection string for more advanced configurations.
  * **Browse Azure** : Browse available database instances and databases in your Azure account, with options to filter by subscription, resource group, and location.
  * **Connection Groups** : Organize environments by grouping connections into folders and assigning colors for quick visual identification. Easily assign or change a group when creating or editing a connection.


The connection dialog includes **Saved Connections** and **Recent Connections** panels to simplify reconnecting to previously used servers. The layout supports editing and saving connection details and makes it easy to switch between servers or databases.
[ ![Screenshot of the connection dialog feature.](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/media/mssql-extension-visual-studio-code/mssql-connection-dialog-parameters.png?view=sql-server-ver17) ](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/media/mssql-extension-visual-studio-code/mssql-connection-dialog-parameters.png?view=sql-server-ver17#lightbox)
[](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/mssql-extension-visual-studio-code?view=sql-server-ver17#database-operations)
### Database operations
The MSSQL extension provides built-in tools for common [database operations](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/mssql-database-operations?view=sql-server-ver17), including:
  * **Database management** : Create, rename, and drop databases directly from the **Object Explorer**.
  * **Database object search** : Find tables, views, functions, and stored procedures with type-aware search and contextual actions.
  * **Backup and restore** : Back up databases to disk or Azure Blob Storage, and restore from existing backups, backup files, or Azure Blob Storage.
  * **Import flat file** : Import `.csv` and `.txt` files into new SQL Server tables with a guided wizard.


[](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/mssql-extension-visual-studio-code?view=sql-server-ver17#object-explorer-filtering)
### Object Explorer (filtering)
The Object Explorer lets you explore your database objects, such as databases, tables, views, and programmability items. The enhanced filtering functionality makes it easier to find specific objects within large and complex database hierarchies:
  * **Apply Filters** : Filter database objects by properties like name, owner, or creation date. You can apply filters at multiple levels, including databases, tables, views, and programmability.
  * **Edit Filters** : Refine or update existing filters to further narrow the object list.
  * **Clear Filters** : Remove applied filters to view all objects within the hierarchy.


These filters give you flexibility and control, making it easier to manage large databases and find relevant objects.
[ ![Screenshot of the object explorer filter feature.](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/media/mssql-extension-visual-studio-code/object-explorer-filtering.png?view=sql-server-ver17) ](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/media/mssql-extension-visual-studio-code/object-explorer-filtering.png?view=sql-server-ver17#lightbox)
[](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/mssql-extension-visual-studio-code?view=sql-server-ver17#table-designer)
### Table Designer
The Table Designer provides a UI for creating and managing tables for your databases. It offers advanced capabilities to customize every aspect of the table's structure:
  * **Columns** : Add new columns, set data types, define nullability, and specify default values. You can also designate a column as a primary key or identity column directly within the interface.
  * **Primary Key** : Define one or more columns as the primary key for your table, ensuring each row is uniquely identifiable.
  * **Indexes** : Create and manage indexes to improve query performance by adding extra columns as indexes for faster data retrieval.
  * **Foreign Keys** : Define relationships between tables by adding foreign keys referencing primary keys in other tables, ensuring data integrity across tables.
  * **Check Constraints** : Set up rules to enforce specific conditions on the data being entered, such as value ranges or patterns.
  * **Advanced Options** : Configure more sophisticated properties and behaviors, such as system versioning and memory optimized tables.


Within the designer, the **Script As Create** panel provides an automatically generated T-SQL script that reflects your table design. You have the following options:
  * **Publish** : Apply your changes directly to the database by selecting **Publish**. This action is powered by DacFX (Data-tier Application Framework), which ensures the smooth and reliable deployment of your schema updates.
  * **Copy script** : Copy the generated T-SQL script from the preview panel for manual execution or open it directly in the editor for further adjustments and modifications as needed.


[ ![Screenshot of the table designer feature.](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/media/mssql-extension-visual-studio-code/table-designer.png?view=sql-server-ver17) ](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/media/mssql-extension-visual-studio-code/table-designer.png?view=sql-server-ver17#lightbox)
[](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/mssql-extension-visual-studio-code?view=sql-server-ver17#view--edit-data-preview)
### View & Edit Data (Preview)
View & Edit Data (Preview) provides an intuitive, interactive way to browse and modify table data directly within the editor without writing Transact-SQL data manipulation language (DML) statements. Developers can interact with their data in an intuitive interface, simplifying everything from quick edits to in-depth validation.
To use this feature, right-click a table in Object Explorer and select **View & Edit Data (Preview)**. The table data opens in a data grid within a new editor tab, displaying the contents in a familiar, spreadsheet-like layout with paging controls based on the configured rows per page.
Key capabilities include:
  * **Inline editing** : Update cell values directly within the grid. Edits are validated in real time and return an error message for incorrect inputs, such as invalid data types or violations of a constraint. The grid highlights the cell with the incorrect input in red.
  * **Add and delete rows** : Insert new rows or delete existing ones, so you can quickly adjust data during development and testing.
  * **Pagination** : Efficiently load and navigate large datasets using built-in paging controls for smooth scrolling and performance.
  * **Save Changes** : All edits remain in a pending state until you select **Save Changes** , giving you complete control over when updates are committed to the database.
  * **Show Script** : This pane displays a read-only DML script that reflects all actions performed in the data grid in real time. This allows you to review the underlying DML operations before saving changes


[ ![Screenshot of the Edit Data screen.](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/media/mssql-extension-visual-studio-code/edit-data.png?view=sql-server-ver17) ](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/media/mssql-extension-visual-studio-code/edit-data.png?view=sql-server-ver17#lightbox)
[](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/mssql-extension-visual-studio-code?view=sql-server-ver17#query-results-pane)
### Query Results pane
The MSSQL extension for Visual Studio Code provides an enhanced query results experience, helping you efficiently visualize and understand your data output. The query results display within the bottom panel of Visual Studio Code, which also hosts the integrated terminal, output, debug console, and other tools, creating a unified interface for easy access.
You can open query results in a new tab for an expanded view, similar to the previous experience.
Key features of the Query Results pane include:
  * **Grid View** : Displays query results in a familiar grid format, so you can easily inspect the data. You can display results in a new tab for a clearer, more organized view.
  * **Copy Options** : Right-click within the results grid to access options like _Select All, Copy, Copy with Headers, and Copy Headers_ , making it convenient to transfer data for other uses.
  * **Save Query Results** : Includes the ability to save query results to multiple formats such as JSON, Excel, and CSV, so you can work with the data outside of Visual Studio Code.
  * **Inline Sorting** : You can sort the data by selecting the column headers directly in the query results view. Sorting can be done in ascending or descending order to make it easier to analyze specific subsets of the data.
  * **Estimated Plan** : The Estimated Plan button is located in the query toolbar, next to the Run Query button. It appears as a flowchart icon and allows you to generate an estimated execution plan without executing the query itself. This feature provides valuable insight into query performance, helping identify potential bottlenecks and inefficiencies before running the actual query.
  * **Enable Actual Plan** : A button labeled **Enable Actual Plan** , located right after **Estimated Plan** button in the upper right corner of the results pane, lets you view the actual query plan for executed queries. This addition provides deeper insight into query performance and helps identify bottlenecks and inefficiencies.


This query results experience supports common workflows for viewing and working with result sets.
[ ![Screenshot of the query results feature.](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/media/mssql-extension-visual-studio-code/query-results-vscode.png?view=sql-server-ver17) ](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/media/mssql-extension-visual-studio-code/query-results-vscode.png?view=sql-server-ver17#lightbox)
You can customize the query results behavior using the `mssql.openQueryResultsInTabByDefault` setting. When set to `true`, query results open in a new tab by default, helping declutter your workspace.
[](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/mssql-extension-visual-studio-code?view=sql-server-ver17#query-plan-visualizer)
### Query Plan Visualizer
Use the Query Plan Visualizer in the MSSQL extension for Visual Studio Code to analyze SQL query performance by viewing detailed execution plans. This tool provides insights into how SQL queries run, so you can identify bottlenecks and optimize your queries.
Key features and capabilities include:
  * **Node Navigation** : Each step in the execution plan appears as a node. You can interact with the plan in different ways. Select nodes to view tooltips or detailed information about specific operations. Collapse or expand node trees to simplify the view and focus on key areas of the query plan.
  * **Zoom Controls** : The visualizer offers flexible zoom options to help you analyze the plan in detail. You can zoom in or out to adjust the level of detail. Use the "zoom to fit" feature to resize the view and fit the entire plan on your screen. Set custom zoom levels to examine specific elements precisely.
  * **Metrics and Highlighting** : The metrics toolbar helps you analyze key performance indicators and highlight expensive operations. Select metrics such as **Actual Elapsed Time** , **Cost** , **Subtree Cost** , or **Number of Rows Read** from the dropdown list to identify bottlenecks. Use these metrics to search for specific nodes within the query plan for deeper analysis.


The right-hand sidebar provides quick access to more actions:
  * **Save Plan** : Save the current execution plan for future reference.
  * **Open XML** : Open the XML representation of the query plan to inspect details at the code level.
  * **Open Query** : View the query that generated the execution plan directly from the toolbar.
  * **Toggle Tooltips** : Enable or disable tooltips for more details on each node.
  * **Properties** : View the properties of each node in the execution plan, with options to sort by importance or alphabetically.


[ ![Screenshot of the query plan visualizer feature.](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/media/mssql-extension-visual-studio-code/query-plan-visualizer-vscode.png?view=sql-server-ver17) ](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/media/mssql-extension-visual-studio-code/query-plan-visualizer-vscode.png?view=sql-server-ver17#lightbox)
[](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/mssql-extension-visual-studio-code?view=sql-server-ver17#supported-operating-systems)
## Supported operating systems
Currently, this extension supports the following operating systems:
  * Windows (x64, x86, Arm64)
  * macOS (x64, Arm64)
  * Linux Arm64
  * Ubuntu 18.04, 20.04, 22.04
  * Debian 10, 11, 12
  * CentOS 7, 8 / Oracle Linux 7, 8
  * Red Hat Enterprise Linux (RHEL) 8, 9
  * Fedora 35, 36
  * OpenSUSE Leap 15


[](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/mssql-extension-visual-studio-code?view=sql-server-ver17#offline-installation)
## Offline installation
The extension can download and install a required `SqlToolsService` package during activation. You can still use the extension for machines with no Internet access by choosing the **Install from VSIX...** option in the Extension view and installing a bundled release from the `.vsix` file with the required service included. Pick the file for your OS, download, and install it to get started. Choose a full release and ignore any alpha or beta releases, as these are daily builds used in testing.
[](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/mssql-extension-visual-studio-code?view=sql-server-ver17#feedback-and-support)
## Feedback and support
If you have ideas, feedback, or want to engage with the community, join the discussion at
[](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/mssql-extension-visual-studio-code?view=sql-server-ver17#related-content)
## Related content
  * [Quickstart: Connect to and query a database with the MSSQL extension for Visual Studio Code](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/connect-database-visual-studio-code?view=sql-server-ver17)
  * [GitHub Copilot for MSSQL extension for Visual Studio Code](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/github-copilot/overview?view=sql-server-ver17)
  * [Database operations (Preview)](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/mssql-database-operations?view=sql-server-ver17)
  * [Schema Designer](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/mssql-schema-designer?view=sql-server-ver17)
  * [Schema Compare](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/mssql-schema-compare?view=sql-server-ver17)


**Note:** The author created this article with assistance from AI. [Learn more](https://learn.microsoft.com/principles-for-ai-generated-content)
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
  * [ Quickstart: Connect to and Query a Database with the MSSQL Extension for Visual Studio Code - SQL Server ](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/connect-database-visual-studio-code?source=recommendations)
Learn how to connect to a database using the MSSQL extension for Visual Studio Code, and execute Transact-SQL (T-SQL) statements to interact with your database.
  * [ Use Visual Studio Code to connect and query - Azure SQL Database & SQL Managed Instance ](https://learn.microsoft.com/en-us/azure/azure-sql/database/connect-query-vscode?source=recommendations)
Learn how to connect to Azure SQL Database or Azure SQL Managed Instance by using Visual Studio Code. Then, run Transact-SQL (T-SQL) statements to query and edit data.


Module
[ Developing in the Windows Subsystem for Linux with Visual Studio Code - Training ](https://learn.microsoft.com/en-us/training/modules/developing-in-wsl/?source=recommendations)
In this module, you learn how to use the Windows Subsystem for Linux (WSL) with Visual Studio Code (VS Code). We explore the installation process and the basics of using WSL. Additionally, we install and utilize the Visual Studio Code WSL extension. Finally, we demonstrate how to debug and run Python code in VS Code within our WSL environment.
Certification
[ Microsoft Certified: Azure Database Administrator Associate - Certifications ](https://learn.microsoft.com/en-us/credentials/certifications/azure-database-administrator-associate/?source=recommendations)
Administer an SQL Server database infrastructure for cloud, on-premises and hybrid relational databases using the Microsoft PaaS relational database offerings.
Mar 8, 4 PM - Mar 8, 4 PM
Experiment with what's next in AI-driven apps and agent design
* * *
  * Last updated on 02/21/2026


##  In this article
  1. [Install the MSSQL Extension in Visual Studio Code](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/mssql-extension-visual-studio-code?view=sql-server-ver17#install-the-mssql-extension-in-visual-studio-code)
  2. [Modern UI](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/mssql-extension-visual-studio-code?view=sql-server-ver17#modern-ui)
  3. [Supported operating systems](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/mssql-extension-visual-studio-code?view=sql-server-ver17#supported-operating-systems)
  4. [Offline installation](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/mssql-extension-visual-studio-code?view=sql-server-ver17#offline-installation)
  5. [Feedback and support](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/mssql-extension-visual-studio-code?view=sql-server-ver17#feedback-and-support)
  6. [Related content](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/mssql-extension-visual-studio-code?view=sql-server-ver17#related-content)


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
[ Sign in ](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/mssql-extension-visual-studio-code?view=sql-server-ver17)
[English (United States)](https://learn.microsoft.com/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fsql%2Ftools%2Fvisual-studio-code-extensions%2Fmssql%2Fmssql-extension-visual-studio-code%3Fview%3Dsql-server-ver17)
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
