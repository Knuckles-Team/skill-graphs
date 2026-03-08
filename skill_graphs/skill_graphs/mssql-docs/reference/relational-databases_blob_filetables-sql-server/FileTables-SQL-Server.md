# FileTables (SQL Server)
Feedback
Summarize this article for me
##  In this article
  1. [Benefits of the FileTable feature](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filetables-sql-server?view=sql-server-ver17#Goals)
  2. [What is a FileTable?](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filetables-sql-server?view=sql-server-ver17#Description)
  3. [Additional considerations for using FileTables](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filetables-sql-server?view=sql-server-ver17#additional)
  4. [Related tasks](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filetables-sql-server?view=sql-server-ver17#related-tasks)
  5. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filetables-sql-server?view=sql-server-ver17#related-content)


**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to)
The FileTable feature brings support for the Windows file namespace and compatibility with Windows applications to the file data stored in SQL Server. FileTable lets an application integrate its storage and data management components, and provides integrated SQL Server services - including full-text search and semantic search - over unstructured data and metadata.
In other words, you can store files and documents in special tables in SQL Server called FileTables, but access them from Windows applications as if they were stored in the file system, without making any changes to your client applications.
The FileTable feature builds on top of SQL Server FILESTREAM technology. To learn more about FILESTREAM, see [FILESTREAM (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filestream-sql-server?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filetables-sql-server?view=sql-server-ver17#Goals)
##  Benefits of the FileTable feature
The goals of the FileTable feature include the following:
  * Windows API compatibility for file data stored within a SQL Server database. Windows API compatibility includes the following:
    * Non-transactional streaming access and in-place updates to FILESTREAM data.
    * A hierarchical namespace of directories and files.
    * Storage of file attributes, such as created date and modified date.
    * Support for Windows file and directory management APIs.
  * Compatibility with other SQL Server features including management tools, services, and relational query capabilities over FILESTREAM and file attribute data.


Thus FileTables remove a significant barrier to the use of SQL Server for the storage and management of unstructured data that is currently residing as files on file servers. Enterprises can move this data from file servers into FileTables to take advantage of integrated administration and services provided by SQL Server. At the same time, they can maintain Windows application compatibility for their existing Windows applications that see this data as files in the file system.
[](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filetables-sql-server?view=sql-server-ver17#Description)
##  What is a FileTable?
SQL Server provides a special _table of files_ , also referred to as a _FileTable_ , for applications that require file and directory storage in the database, with Windows API compatibility and non-transactional access. A FileTable is a specialized user table with a predefined schema that stores FILESTREAM data, as well as file and directory hierarchy information and file attributes.
A FileTable provides the following functionality:
  * A FileTable represents a hierarchy of directories and files. It stores data related to all the nodes in that hierarchy, for both directories and the files they contain. This hierarchy starts from a root directory that you specify when you create the FileTable.
  * Every row in a FileTable represents a file or a directory.
  * Every row contains the following items. For more information about the schema of a FileTable, see [FileTable Schema](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filetable-schema?view=sql-server-ver17).
    * A `file_stream` column for stream data and a `stream_id` (GUID) identifier. (The `file_stream` column is NULL for a directory.)
    * Both `path_locator` and `parent_path_locator` columns for representing and maintaining the current item (file or directory) and directory hierarchy.
    * 10 file attributes such as created date and modified date that are useful with file I/O APIs.
    * A type column that supports full-text search and semantic search over files and documents.
  * A FileTable enforces certain system-defined constraints and triggers to maintain file namespace semantics.
  * When the database is configured for non-transactional access, the file and directory hierarchy represented in the FileTable is exposed under the FILESTREAM share configured for the SQL Server instance. This provides file system access for Windows applications.


[](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filetables-sql-server?view=sql-server-ver17#some-additional-characteristics-of-filetables)
### Some additional characteristics of FileTables
  * The file and directory data stored in a FileTable is exposed through a Windows share for non-transactional file access for Windows API based applications. For a Windows application, this looks like a normal share with its files and directories. Applications can use a rich set of Windows APIs to manage the files and directories under this share.
  * The directory hierarchy surfaced through the share is a purely logical directory structure that is maintained within the FileTable.
  * Calls to create or change a file or directory through the Windows share are intercepted by a SQL Server component and reflected in the corresponding relational data in the FileTable.
  * Windows API operations are non-transactional in nature, and aren't associated with user transactions. However, transactional access to FILESTREAM data stored in a FileTable is fully supported, as is the case for any FILESTREAM column in a regular table. If you need to modify files frequently from multiple connections and ensure proper file protection, use transactional FILESTREAM access via [OpenSqlFilestream()](https://learn.microsoft.com/en-us/sql/relational-databases/blob/access-filestream-data-with-opensqlfilestream?view=sql-server-ver17), rather than exclusive file locks at the Windows API level.
  * FileTables can also be queried and updated through normal Transact-SQL access. They are also integrated with SQL Server management tools, and features such as backup.
  * You can't send an email request through Database Mail and attach a file located in a FILESTREAM directory (and therefore FileTable). The filesystem filter driver RsFx0420 inspects incoming I/O requests going in and out of the FILESTREAM folder. If the request isn't both from the SQLServer executable and FILESTREAM code, they are explicitly disallowed.


[](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filetables-sql-server?view=sql-server-ver17#additional)
##  Additional considerations for using FileTables
[](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filetables-sql-server?view=sql-server-ver17#DBA)
###  Administrative considerations
[](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filetables-sql-server?view=sql-server-ver17#about-filestream-and-filetables)
#### About FILESTREAM and FileTables
You configure FileTables separately from FILESTREAM. Therefore you can continue to use the FILESTREAM feature without enabling non-transactional access or creating FileTables.
There is no non-transactional access to FILESTREAM data except through FileTables. Therefore, when you enable non-transactional access, the behavior of existing FILESTREAM columns and applications isn't affected.
[](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filetables-sql-server?view=sql-server-ver17#about-filetables-and-non-transactional-access)
#### About FileTables and non-transactional access
You can enable or disable non-transactional access at the database level.
You can configure or fine-tune non-transactional access at the database level by turning it off, or by enabling read only or full read/write access.
[](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filetables-sql-server?view=sql-server-ver17#memory)
###  FileTables don't support memory-mapped files
FileTables don't support memory-mapped files. Notepad and Paint are two common examples of applications that use memory-mapped files. You can't use these applications on the same computer as SQL Server to open files that are stored in a FileTable. However you can use these applications from a remote computer to open files that are stored in a FileTable, because in these circumstances the memory-mapping feature isn't used.
[](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filetables-sql-server?view=sql-server-ver17#related-tasks)
## Related tasks
  * [Enable the prerequisites for FileTable](https://learn.microsoft.com/en-us/sql/relational-databases/blob/enable-the-prerequisites-for-filetable?view=sql-server-ver17)
  * [Create, Alter, and Drop FileTables](https://learn.microsoft.com/en-us/sql/relational-databases/blob/create-alter-and-drop-filetables?view=sql-server-ver17)
  * [Load Files into FileTables](https://learn.microsoft.com/en-us/sql/relational-databases/blob/load-files-into-filetables?view=sql-server-ver17)
  * [Work with Directories and Paths in FileTables](https://learn.microsoft.com/en-us/sql/relational-databases/blob/work-with-directories-and-paths-in-filetables?view=sql-server-ver17)
  * [Access FileTables with Transact-SQL](https://learn.microsoft.com/en-us/sql/relational-databases/blob/access-filetables-with-transact-sql?view=sql-server-ver17)
  * [Access FileTables with File Input-Output APIs](https://learn.microsoft.com/en-us/sql/relational-databases/blob/access-filetables-with-file-input-output-apis?view=sql-server-ver17)
  * [Manage FileTables](https://learn.microsoft.com/en-us/sql/relational-databases/blob/manage-filetables?view=sql-server-ver17)


[](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filetables-sql-server?view=sql-server-ver17#related-content)
## Related content
  * [FileTable Schema](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filetable-schema?view=sql-server-ver17)
  * [FileTable compatibility with other SQL Server features](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filetable-compatibility-with-other-sql-server-features?view=sql-server-ver17)
  * [FileTable DDL, functions, stored procedures, and views](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filetable-ddl-functions-stored-procedures-and-views?view=sql-server-ver17)
  * [FILESTREAM and FileTable Dynamic Management Views (Transact-SQL)](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/filestream-and-filetable-dynamic-management-views-transact-sql?view=sql-server-ver17)
  * [FILESTREAM and FileTable Catalog Views (Transact-SQL)](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/filestream-and-filetable-catalog-views-transact-sql?view=sql-server-ver17)
  * [FILESTREAM and FileTable system stored procedures (Transact-SQL)](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/filestream-and-filetable-system-stored-procedures?view=sql-server-ver17)


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
  * [ Create, Alter, or Drop a FileTable - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/blob/create-alter-and-drop-filetables?source=recommendations)
In SQL Server, the FileTables feature uses a directory structure to store files. Learn how to create a new FileTable or alter or drop an existing FileTable.
  * [ Enable the prerequisites for FileTable - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/blob/enable-the-prerequisites-for-filetable?source=recommendations)
To use FileTables, first turn on FILESTREAM, specify a directory, and set certain options and access levels. Learn how to meet all prerequisites.
  * [ Binary Large Object (Blob) Data (SQL Server) - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/blob/binary-large-object-blob-data-sql-server?source=recommendations)
With FILESTREAM, FileTables, and Remote Blob Store (RBS), SQL Server can store blobs in the database or in remote storage. Compare options for storing blobs.
  * [ FILESTREAM (SQL Server) - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filestream-sql-server?source=recommendations)
Learn about FILESTREAM, a SQL Server feature that stores data in the file system. Read about how it stores, secures, and provides access to data.
  * [ FileTable Schema - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filetable-schema?source=recommendations)
Learn about the pre-defined and fixed schema of FileTables, a SQL Server feature that uses a directory structure to store files.
  * [ Load files into FileTables - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/blob/load-files-into-filetables?source=recommendations)
Discover how to load and migrate files into FileTables in SQL Server when the files are stored in various ways. Read about bulk loading operations.
  * [ Compare Options for Storing Blobs (SQL Server) - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/blob/compare-options-for-storing-blobs-sql-server?source=recommendations)
SQL Server can store binary large object (blob) data used by Windows applications. Compare options in this relational database for storing unstructured data.
  * [ Access FILESTREAM data with Transact-SQL - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/blob/access-filestream-data-with-transact-sql?source=recommendations)
Learn how to use the Transact-SQL INSERT, UPDATE, and DELETE statements to access and manage FILESTREAM data.


Show 5 more
Module
[ Explore Windows client file systems - Training ](https://learn.microsoft.com/en-us/training/modules/explore-windows-client-file-systems/?source=recommendations)
In this module, you will learn about the differences and benefits of the file systems that Windows client supports.
Certification
[ Microsoft Certified: Azure Data Fundamentals - Certifications ](https://learn.microsoft.com/en-us/credentials/certifications/azure-data-fundamentals/?source=recommendations)
Demonstrate foundational knowledge of core data concepts related to Microsoft Azure data services.
Mar 8, 4 PM - Mar 8, 4 PM
Experiment with what's next in AI-driven apps and agent design
* * *
  * Last updated on 10/03/2023


##  In this article
  1. [Benefits of the FileTable feature](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filetables-sql-server?view=sql-server-ver17#Goals)
  2. [What is a FileTable?](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filetables-sql-server?view=sql-server-ver17#Description)
  3. [Additional considerations for using FileTables](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filetables-sql-server?view=sql-server-ver17#additional)
  4. [Related tasks](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filetables-sql-server?view=sql-server-ver17#related-tasks)
  5. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filetables-sql-server?view=sql-server-ver17#related-content)


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
[ Sign in ](https://learn.microsoft.com/en-us/sql/relational-databases/blob/filetables-sql-server?view=sql-server-ver17)
[English (United States)](https://learn.microsoft.com/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fsql%2Frelational-databases%2Fblob%2Ffiletables-sql-server%3Fview%3Dsql-server-ver17)
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
