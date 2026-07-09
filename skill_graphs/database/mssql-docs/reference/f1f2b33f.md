# What is SQL Server 2016 R Services?
Feedback
Summarize this article for me
##  In this article
  1. [What is R Services?](https://learn.microsoft.com/en-us/sql/machine-learning/r/sql-server-r-services?view=sql-server-2016#what-is-r-services)
  2. [What can I do with R Services?](https://learn.microsoft.com/en-us/sql/machine-learning/r/sql-server-r-services?view=sql-server-2016#what-can-i-do-with-r-services)
  3. [R versions](https://learn.microsoft.com/en-us/sql/machine-learning/r/sql-server-r-services?view=sql-server-2016#r-versions)
  4. [R packages](https://learn.microsoft.com/en-us/sql/machine-learning/r/sql-server-r-services?view=sql-server-2016#r-packages)
  5. [How do I get started with R Services?](https://learn.microsoft.com/en-us/sql/machine-learning/r/sql-server-r-services?view=sql-server-2016#how-do-i-get-started-with-r-services)
  6. [Next steps](https://learn.microsoft.com/en-us/sql/machine-learning/r/sql-server-r-services?view=sql-server-2016#next-steps)

Show 2 more
**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-2016) SQL Server 2016 (13.x)
R Services is a feature in SQL Server 2016 that gives the ability to run R scripts with relational data. You can use open-source packages and frameworks, and the [Microsoft R packages](https://learn.microsoft.com/en-us/sql/machine-learning/r/sql-server-r-services?view=sql-server-2016#packages) for predictive analytics and machine learning. The scripts are executed in-database without moving data outside SQL Server or over the network. This article explains the basics of SQL Server R Services.
R Services was renamed to [Machine Learning Services](https://learn.microsoft.com/en-us/sql/machine-learning/sql-server-machine-learning-services?view=sql-server-2016) in SQL Server 2017 and later, and supports both Python and R.
[](https://learn.microsoft.com/en-us/sql/machine-learning/r/sql-server-r-services?view=sql-server-2016#what-is-r-services)
## What is R Services?
SQL Server R Services lets you execute R scripts in-database. You can use it to prepare and clean data, do feature engineering, and train, evaluate, and deploy machine learning models within a database. The feature runs your scripts where the data resides and eliminates transfer of the data across the network to another server.
Base distributions of R are included in R Services. You can use open-source packages and frameworks in addition to the Microsoft packages [RevoScaleR](https://learn.microsoft.com/en-us/sql/machine-learning/r/ref-r-revoscaler?view=sql-server-2016), [MicrosoftML](https://learn.microsoft.com/en-us/sql/machine-learning/r/ref-r-microsoftml?view=sql-server-2016), [olapR]../r/ref-r-olapr.md), and [sqlrutils](https://learn.microsoft.com/en-us/sql/machine-learning/r/ref-r-sqlrutils?view=sql-server-2016) for R.
R Services uses an extensibility framework to run R scripts in SQL Server. Learn more about how this works:
  * [Extensibility framework](https://learn.microsoft.com/en-us/sql/machine-learning/concepts/extensibility-framework?view=sql-server-2016)
  * [R extension](https://learn.microsoft.com/en-us/sql/machine-learning/concepts/extension-r?view=sql-server-2016)


[](https://learn.microsoft.com/en-us/sql/machine-learning/r/sql-server-r-services?view=sql-server-2016#what-can-i-do-with-r-services)
## What can I do with R Services?
You can use R Services to build and training machine learning and deep learning models within SQL Server. You can also deploy existing models to R Services and use relational data for predictions.
Examples of the type of predictions that you can use SQL Server R Services for, include:
Expand table
Prediction type | Example
---|---
Classification/Categorization | Automatically divide customer feedback into positive and negative categories
Regression/Predict continuous values | Predict the price of houses based on size and location
Anomaly Detection | Detect fraudulent banking transactions
Recommendations | Suggest products that online shoppers may want to buy, based on their previous purchases
[](https://learn.microsoft.com/en-us/sql/machine-learning/r/sql-server-r-services?view=sql-server-2016#how-to-execute-r-scripts)
### How to execute R scripts
There are two ways to execute R scripts in R Services:
  * The most common way is to use the T-SQL stored procedure [sp_execute_external_script](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-execute-external-script-transact-sql?view=sql-server-2016).
  * You can also use your preferred R client and write scripts that push the execution (referred to as a _remote compute context_) to a remote SQL Server. See how to [set up a data science client R development](https://learn.microsoft.com/en-us/sql/machine-learning/r/set-up-data-science-client?view=sql-server-2016) for more information.


[](https://learn.microsoft.com/en-us/sql/machine-learning/r/sql-server-r-services?view=sql-server-2016#r-versions)
## R versions
The following lists the versions of the R runtime that are included in SQL Server 2016 R Services.
Expand table
SQL Server version | Default R runtime versions
---|---
SQL Server 2016 RTM - SP2 CU13 | 3.2.2
SQL Server 2016 SP2 CU14 and later | 3.2.2 and 3.5.2
Cumulative Update (CU) 14 for SQL Server 2016 Service Pack (SP) 2 and later include newer R runtimes. For more information, see [Change the default language runtime version](https://learn.microsoft.com/en-us/sql/machine-learning/install/change-default-language-runtime-version?view=sql-server-2016).
For other versions of R, or to run Python, use [Machine Learning Services for SQL Server 2017 and later](https://learn.microsoft.com/en-us/sql/machine-learning/sql-server-machine-learning-services?view=sql-server-2016).
[](https://learn.microsoft.com/en-us/sql/machine-learning/r/sql-server-r-services?view=sql-server-2016#r-packages)
## R packages
You can use open-source packages and frameworks, in addition to Microsoft's enterprise packages. Most common open-source R packages are pre-installed in R Services. The following R packages from Microsoft are also included:
Expand table
Package | Description
---|---
[RevoScaleR](https://learn.microsoft.com/en-us/sql/machine-learning/r/ref-r-revoscaler?view=sql-server-2016) | The primary package for scalable R. Data transformations and manipulation, statistical summarization, visualization, and many forms of modeling. Additionally, functions in this package automatically distribute workloads across available cores for parallel processing.
[MicrosoftML (R)](https://learn.microsoft.com/en-us/sql/machine-learning/r/ref-r-microsoftml?view=sql-server-2016) | Adds machine learning algorithms to create custom models for text analysis, image analysis, and sentiment analysis.
[olapR](https://learn.microsoft.com/en-us/sql/machine-learning/r/ref-r-olapr?view=sql-server-2016) | R functions used for MDX queries against a SQL Server Analysis Services OLAP cube.
[sqlrutils](https://learn.microsoft.com/en-us/sql/machine-learning/r/ref-r-sqlrutils?view=sql-server-2016) | A mechanism to use R scripts in a T-SQL stored procedure, register that stored procedure with a database, and run the stored procedure from an [R development environment](https://learn.microsoft.com/en-us/sql/machine-learning/r/set-up-data-science-client?view=sql-server-2016).
Microsoft R Open ([retired](https://techcommunity.microsoft.com/t5/azure-sql-blog/microsoft-r-application-network-retirement/ba-p/3707161)) | Microsoft R Open (MRO) was the enhanced distribution of R from Microsoft.
[](https://learn.microsoft.com/en-us/sql/machine-learning/r/sql-server-r-services?view=sql-server-2016#how-do-i-get-started-with-r-services)
## How do I get started with R Services?
  1. [Install SQL Server 2016 R Services](https://learn.microsoft.com/en-us/sql/machine-learning/install/sql-r-services-windows-install?view=sql-server-2016)
  2. Configure your development tools. You can use:
     * The [MSSQL extension for Visual Studio Code](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/mssql-extension-visual-studio-code?view=sql-server-2016) or [SQL Server Management Studio (SSMS)](https://learn.microsoft.com/en-us/ssms/sql-server-management-studio-ssms), to use T-SQL and the stored procedure [sp_execute_external_script](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-execute-external-script-transact-sql?view=sql-server-2016) to execute your R script.
     * R on your own development laptop or workstation to execute scripts. You can either pull data down locally or push the execution remotely to SQL Server with [RevoScaleR](https://learn.microsoft.com/en-us/sql/machine-learning/r/ref-r-revoscaler?view=sql-server-2016). See how to [set up a data science client R development](https://learn.microsoft.com/en-us/sql/machine-learning/r/set-up-data-science-client?view=sql-server-2016) for more information.
  3. Write your first R script
     * Quickstart: [Create and run simple R scripts in SQL Server](https://learn.microsoft.com/en-us/sql/machine-learning/tutorials/quickstart-r-create-script?view=sql-server-2016)
     * Quickstart: [Create and train a predictive model in R](https://learn.microsoft.com/en-us/sql/machine-learning/tutorials/quickstart-r-train-score-model?view=sql-server-2016)
     * Tutorial: [Use R in T-SQL](https://learn.microsoft.com/en-us/sql/machine-learning/tutorials/r-taxi-classification-introduction?view=sql-server-2016): Explore data, perform feature engineering, train and deploy models, and make predictions (five-part series)
     * Tutorial: [Use R Services in R tools](https://learn.microsoft.com/en-us/sql/machine-learning/tutorials/walkthrough-data-science-end-to-end-walkthrough?view=sql-server-2016): Explore data, create graphs and plots, perform feature engineering, train and deploy models, and make predictions (six-part series)


[](https://learn.microsoft.com/en-us/sql/machine-learning/r/sql-server-r-services?view=sql-server-2016#next-steps)
## Next steps
  * [Install SQL Server 2016 R Services](https://learn.microsoft.com/en-us/sql/machine-learning/install/sql-r-services-windows-install?view=sql-server-2016)
  * [Set up a data science client for R development](https://learn.microsoft.com/en-us/sql/machine-learning/r/set-up-data-science-client?view=sql-server-2016)


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
  * [ Install R custom runtime - SQL Server Machine Learning Services ](https://learn.microsoft.com/en-us/sql/machine-learning/install/custom-runtime-r?source=recommendations)
Learn how to install an R custom runtime for SQL Server using Language Extensions. The Python custom runtime can run machine learning scripts.
  * [ Install SQL Server 2016 R Services - SQL Server Machine Learning Services ](https://learn.microsoft.com/en-us/sql/machine-learning/install/sql-r-services-windows-install?source=recommendations)
Learn how to install SQL Server 2016 R Services on Windows. You can use R Services to execute R scripts in-database.
  * [ Quickstart: Run R scripts - SQL machine learning ](https://learn.microsoft.com/en-us/sql/machine-learning/tutorials/quickstart-r-create-script?source=recommendations)
Run a set of simple R scripts with SQL machine learning. Learn how to use the stored procedure sp_execute_external_script to execute the script.
  * [ Get R package information - SQL Server Machine Learning Services ](https://learn.microsoft.com/en-us/sql/machine-learning/package-management/r-package-information?source=recommendations)
Learn how to get information about installed R packages on SQL Server Machine Learning Services and SQL Server R Services.
  * [ Install pretrained models - SQL Server Machine Learning Services ](https://learn.microsoft.com/en-us/sql/machine-learning/install/sql-pretrained-models-install?source=recommendations)
Add pretrained models for sentiment analysis and image featurization to SQL Server Machine Learning Services (R or Python) or SQL Server R Services.
  * [ Known issues for Python and R - SQL Server Machine Learning Services ](https://learn.microsoft.com/en-us/sql/machine-learning/troubleshooting/known-issues-for-sql-server-machine-learning-services?source=recommendations)
This article describes known problems or limitations with the Python and R components that are provided in SQL Server Machine Learning Services and SQL Server 2016 R Services.
  * [ Set up an R data science client - SQL Server Machine Learning Services ](https://learn.microsoft.com/en-us/sql/machine-learning/r/set-up-data-science-client?source=recommendations)
Install local R libraries and tools on a development workstation for remote connections to SQL Server.
  * [ Install R packages with sqlmlutils - SQL Server Machine Learning Services ](https://learn.microsoft.com/en-us/sql/machine-learning/package-management/install-additional-r-packages-on-sql-server?source=recommendations)
Learn how to use sqlmlutils to install new R packages to an instance of SQL Server Machine Learning Services.


Show 5 more
Module
[ Explore and analyze data with R - Training ](https://learn.microsoft.com/en-us/training/modules/explore-analyze-data-with-r/?source=recommendations)
In this module, you explore, analyze, and visualize data by using the R programming language.
Certification
[ Microsoft Certified: Azure Data Scientist Associate - Certifications ](https://learn.microsoft.com/en-us/credentials/certifications/azure-data-scientist/?source=recommendations)
Manage data ingestion and preparation, model training and deployment, and machine learning solution monitoring with Python, Azure Machine Learning and MLflow.
Mar 8, 4 PM - Mar 8, 4 PM
Experiment with what's next in AI-driven apps and agent design
* * *
  * Last updated on 02/18/2026


##  In this article
  1. [What is R Services?](https://learn.microsoft.com/en-us/sql/machine-learning/r/sql-server-r-services?view=sql-server-2016#what-is-r-services)
  2. [What can I do with R Services?](https://learn.microsoft.com/en-us/sql/machine-learning/r/sql-server-r-services?view=sql-server-2016#what-can-i-do-with-r-services)
  3. [R versions](https://learn.microsoft.com/en-us/sql/machine-learning/r/sql-server-r-services?view=sql-server-2016#r-versions)
  4. [R packages](https://learn.microsoft.com/en-us/sql/machine-learning/r/sql-server-r-services?view=sql-server-2016#r-packages)
  5. [How do I get started with R Services?](https://learn.microsoft.com/en-us/sql/machine-learning/r/sql-server-r-services?view=sql-server-2016#how-do-i-get-started-with-r-services)
  6. [Next steps](https://learn.microsoft.com/en-us/sql/machine-learning/r/sql-server-r-services?view=sql-server-2016#next-steps)


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
[ Sign in ](https://learn.microsoft.com/en-us/sql/machine-learning/r/sql-server-r-services?view=sql-server-2016)
[English (United States)](https://learn.microsoft.com/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fsql%2Fmachine-learning%2Fr%2Fsql-server-r-services%3Fview%3Dsql-server-2016)
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
