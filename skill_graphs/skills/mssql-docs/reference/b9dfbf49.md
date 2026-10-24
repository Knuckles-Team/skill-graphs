# Spatial Data
Feedback
Summarize this article for me
##  In this article
  1. [Limitations](https://learn.microsoft.com/en-us/sql/relational-databases/spatial/spatial-data-sql-server?view=sql-server-ver17#limitations)
  2. [Related Tasks](https://learn.microsoft.com/en-us/sql/relational-databases/spatial/spatial-data-sql-server?view=sql-server-ver17#related-tasks)
  3. [Spatial tools open-source project](https://learn.microsoft.com/en-us/sql/relational-databases/spatial/spatial-data-sql-server?view=sql-server-ver17#spatial-tools-open-source-project)
  4. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/spatial/spatial-data-sql-server?view=sql-server-ver17#related-content)


**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Database](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL analytics endpoint in Microsoft Fabric](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Warehouse in Microsoft Fabric](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL database in Microsoft Fabric](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to)
Spatial data represents information about the physical location and shape of geometric objects. These objects can be point locations or more complex objects such as countries/regions, roads, or lakes.
SQL Server supports two spatial data types: the **geometry** data type and the **geography** data type.
  * The **geometry** type represents data in a Euclidean (flat) coordinate system.
  * The **geography** type represents data in a round-earth coordinate system.


Both data types are implemented as .NET common language runtime (CLR) data types in SQL Server.
[](https://learn.microsoft.com/en-us/sql/relational-databases/spatial/spatial-data-sql-server?view=sql-server-ver17#limitations)
## Limitations
In SQL database in Microsoft Fabric, **geography** and **geometry** data types are supported but cannot be [mirrored to the Fabric OneLake](https://learn.microsoft.com/en-us/fabric/database/sql/mirroring-overview).
[](https://learn.microsoft.com/en-us/sql/relational-databases/spatial/spatial-data-sql-server?view=sql-server-ver17#related-tasks)
## Related Tasks
[Create, Construct, and Query geometry Instances](https://learn.microsoft.com/en-us/sql/relational-databases/spatial/create-construct-and-query-geometry-instances?view=sql-server-ver17)
Describes the methods that you can use with instances of the **geometry** data type.
[Create, Construct, and Query geography Instances](https://learn.microsoft.com/en-us/sql/relational-databases/spatial/create-construct-and-query-geography-instances?view=sql-server-ver17)
Describes the methods that you can use with instances of the **geography** data type.
[Query Spatial Data for Nearest Neighbor](https://learn.microsoft.com/en-us/sql/relational-databases/spatial/query-spatial-data-for-nearest-neighbor?view=sql-server-ver17)
Describes the common query pattern that is used to find the closest spatial objects to a specific spatial object.
[Create, Modify, and Drop Spatial Indexes](https://learn.microsoft.com/en-us/sql/relational-databases/spatial/create-modify-and-drop-spatial-indexes?view=sql-server-ver17)
Provides information about creating, altering, and dropping a spatial index.
[](https://learn.microsoft.com/en-us/sql/relational-databases/spatial/spatial-data-sql-server?view=sql-server-ver17#spatial-tools-open-source-project)
## Spatial tools open-source project
SQL Server spatial tools is a Microsoft sponsored open-source collection of tools for use with the spatial types in SQL Server. This project provides a set of reusable functions which applications can make use of. These functions may include data conversion routines, new transformations, aggregates, etc. See
[](https://learn.microsoft.com/en-us/sql/relational-databases/spatial/spatial-data-sql-server?view=sql-server-ver17#related-content)
## Related content
  * [Spatial Data Types Overview](https://learn.microsoft.com/en-us/sql/relational-databases/spatial/spatial-data-types-overview?view=sql-server-ver17)
  * [Point](https://learn.microsoft.com/en-us/sql/relational-databases/spatial/point?view=sql-server-ver17)
  * [LineString](https://learn.microsoft.com/en-us/sql/relational-databases/spatial/linestring?view=sql-server-ver17)
  * [CircularString](https://learn.microsoft.com/en-us/sql/relational-databases/spatial/circularstring?view=sql-server-ver17)
  * [CompoundCurve](https://learn.microsoft.com/en-us/sql/relational-databases/spatial/compoundcurve?view=sql-server-ver17)
  * [Polygon](https://learn.microsoft.com/en-us/sql/relational-databases/spatial/polygon?view=sql-server-ver17)
  * [CurvePolygon](https://learn.microsoft.com/en-us/sql/relational-databases/spatial/curvepolygon?view=sql-server-ver17)
  * [MultiPoint](https://learn.microsoft.com/en-us/sql/relational-databases/spatial/multipoint?view=sql-server-ver17)
  * [MultiLineString](https://learn.microsoft.com/en-us/sql/relational-databases/spatial/multilinestring?view=sql-server-ver17)
  * [MultiPolygon](https://learn.microsoft.com/en-us/sql/relational-databases/spatial/multipolygon?view=sql-server-ver17)
  * [GeometryCollection](https://learn.microsoft.com/en-us/sql/relational-databases/spatial/geometrycollection?view=sql-server-ver17)
  * [Spatial Indexes Overview](https://learn.microsoft.com/en-us/sql/relational-databases/spatial/spatial-indexes-overview?view=sql-server-ver17)


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
  * [ Spatial Data Types Overview - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/spatial/spatial-data-types-overview?source=recommendations)
Spatial Data Types represent information about the physical location and shape of geometric objects in the SQL Database Engine.
  * [ Query spatial data for nearest neighbor - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/spatial/query-spatial-data-for-nearest-neighbor?source=recommendations)
Query spatial data for nearest neighbor, used to find the closest spatial objects to a specific spatial object.
  * [ Create, construct, and query geometry instances - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/spatial/create-construct-and-query-geometry-instances?source=recommendations)
Geometry instances represent data in a Euclidean (flat) coordinate system. Learn how to create, construct, and query geometry data in SQL Database Engine spatial data.
  * [ Polygon - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/spatial/polygon?source=recommendations)
Polygon is a two-dimensional surface stored as a sequence of points defining an exterior bounding ring and zero or more interior rings, in SQL Server spatial data.
  * [ Point - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/spatial/point?source=recommendations)
Point is a 0-dimensional object representing a single location and can contain Z (elevation) and M (measure) values in SQL Server spatial data.
  * [ Create, Construct, and Query geography instances - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/spatial/create-construct-and-query-geography-instances?source=recommendations)
Create, Construct, and Query geography instances represents data in a round-earth coordinate system in SQL Database Engine spatial data.
  * [ GeometryCollection - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/spatial/geometrycollection?source=recommendations)
GeometryCollection is a collection of zero or more geometry or geography instances in SQL Database Engine spatial data.
  * [ geometry (Transact-SQL) - SQL Server ](https://learn.microsoft.com/en-us/sql/t-sql/spatial-geometry/spatial-types-geometry-transact-sql?source=recommendations)
Spatial Types - geometry (Transact-SQL)


Show 5 more
Learning path
[ Write advanced Transact-SQL queries - Training ](https://learn.microsoft.com/en-us/training/paths/write-advanced-transact-sql-queries/?source=recommendations)
Write advanced Transact-SQL queries
Mar 8, 4 PM - Mar 8, 4 PM
Experiment with what's next in AI-driven apps and agent design
* * *
  * Last updated on 11/18/2025


##  In this article
  1. [Limitations](https://learn.microsoft.com/en-us/sql/relational-databases/spatial/spatial-data-sql-server?view=sql-server-ver17#limitations)
  2. [Related Tasks](https://learn.microsoft.com/en-us/sql/relational-databases/spatial/spatial-data-sql-server?view=sql-server-ver17#related-tasks)
  3. [Spatial tools open-source project](https://learn.microsoft.com/en-us/sql/relational-databases/spatial/spatial-data-sql-server?view=sql-server-ver17#spatial-tools-open-source-project)
  4. [Related content](https://learn.microsoft.com/en-us/sql/relational-databases/spatial/spatial-data-sql-server?view=sql-server-ver17#related-content)


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
[ Sign in ](https://learn.microsoft.com/en-us/sql/relational-databases/spatial/spatial-data-sql-server?view=sql-server-ver17)
[English (United States)](https://learn.microsoft.com/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fsql%2Frelational-databases%2Fspatial%2Fspatial-data-sql-server%3Fview%3Dsql-server-ver17)
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
