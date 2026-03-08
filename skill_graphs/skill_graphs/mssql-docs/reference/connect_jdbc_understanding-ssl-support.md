Version SQL Server 2025
  * Analytics Platform System (PDW)
    * [2016-AU7](https://learn.microsoft.com/en-us/sql/connect/jdbc/understanding-ssl-support?view=aps-pdw-2016-au7)
    * [2016-AU6](https://learn.microsoft.com/en-us/sql/connect/jdbc/understanding-ssl-support?view=aps-pdw-2016)
  * [Azure SQL Database](https://learn.microsoft.com/en-us/sql/connect/jdbc/understanding-ssl-support?view=azuresqldb-current)
  * [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/sql/connect/jdbc/understanding-ssl-support?view=azuresqldb-mi-current)
  * [Azure Synapse Analytics](https://learn.microsoft.com/en-us/sql/connect/jdbc/understanding-ssl-support?view=azure-sqldw-latest)
  * [Fabric Data Warehouse](https://learn.microsoft.com/en-us/sql/connect/jdbc/understanding-ssl-support?view=fabric)
  * [Fabric SQL database](https://learn.microsoft.com/en-us/sql/connect/jdbc/understanding-ssl-support?view=fabric-sqldb)
  * SQL Server
    * [2025](https://learn.microsoft.com/en-us/sql/connect/jdbc/understanding-ssl-support?view=sql-server-ver17)
    * [2022](https://learn.microsoft.com/en-us/sql/connect/jdbc/understanding-ssl-support?view=sql-server-ver16)
    * [2019](https://learn.microsoft.com/en-us/sql/connect/jdbc/understanding-ssl-support?view=sql-server-ver15)
    * [2017](https://learn.microsoft.com/en-us/sql/connect/jdbc/understanding-ssl-support?view=sql-server-2017)
    * [2016](https://learn.microsoft.com/en-us/sql/connect/jdbc/understanding-ssl-support?view=sql-server-2016)
  * SQL Server on Linux
    * [2025](https://learn.microsoft.com/en-us/sql/connect/jdbc/understanding-ssl-support?view=sql-server-linux-ver17)
    * [2022](https://learn.microsoft.com/en-us/sql/connect/jdbc/understanding-ssl-support?view=sql-server-linux-ver16)
    * [2019](https://learn.microsoft.com/en-us/sql/connect/jdbc/understanding-ssl-support?view=sql-server-linux-ver15)
    * [2017](https://learn.microsoft.com/en-us/sql/connect/jdbc/understanding-ssl-support?view=sql-server-linux-2017)


Search
Suggestions will filter as you type
  * [Programming to interact with SQL Server](https://learn.microsoft.com/en-us/sql/connect/?view=sql-server-ver17)
  * [Welcome to SQL Server >](https://learn.microsoft.com/en-us/sql/sql-server/?view=sql-server-ver17)
  * [SQL Server drivers](https://learn.microsoft.com/en-us/sql/connect/sql-connection-libraries?view=sql-server-ver17)
  * [Driver feature support matrix](https://learn.microsoft.com/en-us/sql/connect/driver-feature-matrix?view=sql-server-ver17)
  * [SQL Server driver history](https://learn.microsoft.com/en-us/sql/connect/connect-history?view=sql-server-ver17)
  * [SQL data developer](https://learn.microsoft.com/en-us/sql/connect/sql-data-developer?view=sql-server-ver17)
  * NET
  *     * [Microsoft JDBC Driver for SQL Server](https://learn.microsoft.com/en-us/sql/connect/jdbc/microsoft-jdbc-driver-for-sql-server?view=sql-server-ver17)
    *       * [Securing applications](https://learn.microsoft.com/en-us/sql/connect/jdbc/securing-jdbc-driver-applications?view=sql-server-ver17)
      * [Securing connection strings](https://learn.microsoft.com/en-us/sql/connect/jdbc/securing-connection-strings?view=sql-server-ver17)
      * [Validating user input](https://learn.microsoft.com/en-us/sql/connect/jdbc/validating-user-input?view=sql-server-ver17)
      * [Application security](https://learn.microsoft.com/en-us/sql/connect/jdbc/application-security?view=sql-server-ver17)
      *         * [Using encryption](https://learn.microsoft.com/en-us/sql/connect/jdbc/using-ssl-encryption?view=sql-server-ver17)
        * [Understanding encryption support](https://learn.microsoft.com/en-us/sql/connect/jdbc/understanding-ssl-support?view=sql-server-ver17)
        * [Connecting with encryption](https://learn.microsoft.com/en-us/sql/connect/jdbc/connecting-with-ssl-encryption?view=sql-server-ver17)
        * [Configuring the client for encryption](https://learn.microsoft.com/en-us/sql/connect/jdbc/configuring-the-client-for-ssl-encryption?view=sql-server-ver17)
      * [FIPS mode](https://learn.microsoft.com/en-us/sql/connect/jdbc/fips-mode?view=sql-server-ver17)
  * js


Download PDF
Table of contents  Exit editor mode
  1. [ Learn ](https://learn.microsoft.com/en-us/?view=sql-server-ver17)
  2. [ SQL ](https://learn.microsoft.com/en-us/sql/?view=sql-server-ver17)
  3. [ SQL Server ](https://learn.microsoft.com/en-us/sql/sql-server/?view=sql-server-ver17)


  1. [Learn](https://learn.microsoft.com/en-us/?view=sql-server-ver17)
  2. [SQL](https://learn.microsoft.com/en-us/sql/?view=sql-server-ver17)
  3. [SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/?view=sql-server-ver17)


Ask Learn Ask Learn Focus mode
Table of contents [ Read in English ](https://learn.microsoft.com/en-us/sql/connect/jdbc/understanding-ssl-support?view=sql-server-ver17) Add to Collections Add to plan
* * *
#### Share via
* * *
Copy Markdown Print
* * *
Note
Access to this page requires authorization. You can try [signing in](https://learn.microsoft.com/en-us/sql/connect/jdbc/understanding-ssl-support?view=sql-server-ver17) or changing directories.
Access to this page requires authorization. You can try changing directories.
# Understanding encryption support
Feedback
Summarize this article for me
##  In this article
  1. [Remarks](https://learn.microsoft.com/en-us/sql/connect/jdbc/understanding-ssl-support?view=sql-server-ver17#remarks)
  2. [Validating server TLS certificate](https://learn.microsoft.com/en-us/sql/connect/jdbc/understanding-ssl-support?view=sql-server-ver17#validating-server-tls-certificate)
  3. [See also](https://learn.microsoft.com/en-us/sql/connect/jdbc/understanding-ssl-support?view=sql-server-ver17#see-also)


![](https://learn.microsoft.com/en-us/sql/includes/media/download.svg?view=sql-server-ver17) **[Download JDBC driver](https://learn.microsoft.com/en-us/sql/connect/jdbc/download-microsoft-jdbc-driver-for-sql-server?view=sql-server-ver17)**
When connecting to SQL Server, if the application requests encryption and the instance of SQL Server is configured to support TLS encryption, the Microsoft JDBC Driver for SQL Server initiates the TLS handshake. The handshake allows the server and client to negotiate the encryption and cryptographic algorithms to be used to protect data. After the TLS handshake is complete, the client and server can send the encrypted data securely. During the TLS handshake, the server sends its public key certificate to the client. The issuer of a public key certificate is known as a Certificate Authority (CA). The client is responsible for validating that the certificate authority is one the client trusts.
If the application doesn't request encryption, the Microsoft JDBC Driver for SQL Server won't force SQL Server to support TLS encryption. If the SQL Server instance isn't configured to force the TLS encryption, a connection is established without encryption. If the SQL Server instance is configured to force the TLS encryption, the driver will automatically enable TLS encryption when running on properly configured Java Virtual Machine (JVM), or else the connection is terminated and the driver will raise an error.
Make sure the value passed to **serverName** exactly matches the Common Name (CN) or DNS name in the Subject Alternate Name (SAN) in the server certificate for a TLS connection to succeed.
For more information about how to configure TLS for SQL Server, see [Enable encrypted connections to the Database Engine](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/configure-sql-server-encryption?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/connect/jdbc/understanding-ssl-support?view=sql-server-ver17#remarks)
## Remarks
To allow applications to use TLS encryption, the Microsoft JDBC Driver for SQL Server has introduced the following connection properties starting with the version 1.2 release: **encrypt** , **trustServerCertificate** , **trustStore** , **trustStorePassword** , and **hostNameInCertificate**. To allow the driver to use TDS 8.0 with TLS encryption, the connection property **serverCertificate** has been introduced starting with the version 11.2 release. For more information, see [Setting the connection properties](https://learn.microsoft.com/en-us/sql/connect/jdbc/setting-the-connection-properties?view=sql-server-ver17).
The following table summarizes how the Microsoft JDBC Driver for SQL Server version behaves for possible TLS connection scenarios. Each scenario uses a different set of TLS connection properties. The table includes:
  * **blank** : "The property doesn't exist in the connection string"
  * **value** : "The property exists in the connection string and its value is valid"
  * **any** : "It doesn't matter whether the property exists in the connection string or its value is valid"


The same behavior applies for SQL Server user authentication and Windows integrated authentication.
Expand table
Property settings  | Behavior
---|---
**encrypt** = false or blank
**trustServerCertificate** = any
**hostNameInCertificate** = any
**trustStore** = any
**trustStorePassword** = any
| The driver won't force the server to support TLS encryption. If the server has a self-signed certificate, the driver initiates the TLS certificate exchange. The TLS certificate won't be validated and only the credentials (in the login packet) are encrypted.

If the server requires the client to support TLS encryption, the driver will initiate the TLS certificate exchange. The TLS certificate won't be validated, but the entire communication will be encrypted.
**encrypt** = true
**trustServerCertificate** = true
**hostNameInCertificate** = any
**trustStore** = any
**trustStorePassword** = any
| The driver requests to use TLS encryption with the server.

If the server requires the client to support TLS encryption or if the server supports encryption, the driver will initiate the TLS certificate exchange. If the **trustServerCertificate** property is set to "true", the driver won't validate the TLS certificate.

If the server isn't configured to support encryption, the driver will raise an error and terminate the connection.
**encrypt** = true
**trustServerCertificate** = false or blank
**hostNameInCertificate** = blank
**trustStore** = blank
**trustStorePassword** = blank
| The driver requests to use TLS encryption with the server.

If the server requires the client to support TLS encryption or if the server supports encryption, the driver will initiate the TLS certificate exchange.

The driver will use the **serverName** property specified on the connection URL to validate the server TLS certificate and rely on the trust manager factory's look-up rules to determine which certificate store to use.

If the server isn't configured to support encryption, the driver will raise an error and terminate the connection.
**encrypt** = true
**trustServerCertificate** = false or blank
**hostNameInCertificate** = value
**trustStore** = blank
**trustStorePassword** = blank
| The driver requests to use TLS encryption with the server.

If the server requires the client to support TLS encryption or if the server supports encryption, the driver will initiate the TLS certificate exchange.

The driver will validate the TLS certificate's subject value by using the value specified for the **hostNameInCertificate** property.

If the server isn't configured to support encryption, the driver will raise an error and terminate the connection.
**encrypt** = true
**trustServerCertificate** = false or blank
**hostNameInCertificate** = blank
**trustStore** = value
**trustStorePassword** = value
| The driver requests to use TLS encryption with the server.

If the server requires the client to support TLS encryption or if the server supports encryption, the driver will initiate the TLS certificate exchange.

The driver will use the **trustStore** property value to find the certificate trustStore file and **trustStorePassword** property value to check the integrity of the trustStore file.

If the server isn't configured to support encryption, the driver will raise an error and terminate the connection.
**encrypt** = true
**trustServerCertificate** = false or blank
**hostNameInCertificate** = blank
**trustStore** = blank
**trustStorePassword** = value
| The driver requests to use TLS encryption with the server.

If the server requires the client to support TLS encryption or if the server supports encryption, the driver will initiate the TLS certificate exchange.

The driver will use the **trustStorePassword** property value to check the integrity of the default trustStore file.

If the server isn't configured to support encryption, the driver will raise an error and terminate the connection.
**encrypt** = true
**trustServerCertificate** = false or blank
**hostNameInCertificate** = blank
**trustStore** = value
**trustStorePassword** = blank
| The driver requests to use TLS encryption with the server.

If the server requires the client to support TLS encryption or if the server supports encryption, the driver will initiate the TLS certificate exchange.

The driver will use the **trustStore** property value to look up the location of the trustStore file.

If the server isn't configured to support encryption, the driver will raise an error and terminate the connection.
**encrypt** = true
**trustServerCertificate** = false or blank
**hostNameInCertificate** = value
**trustStore** = blank
**trustStorePassword** = value
| The driver requests to use TLS encryption with the server.

If the server requires the client to support TLS encryption or if the server supports encryption, the driver will initiate the TLS certificate exchange.

The driver will use the **trustStorePassword** property value to check the integrity of the default trustStore file. Also, the driver will use the **hostNameInCertificate** property value to validate the TLS certificate.

If the server isn't configured to support encryption, the driver will raise an error and terminate the connection.
**encrypt** = true
**trustServerCertificate** = false or blank
**hostNameInCertificate** = value
**trustStore** = value
**trustStorePassword** = blank
| The driver requests to use TLS encryption with the server.

If the server requires the client to support TLS encryption or if the server supports encryption, the driver will initiate the TLS certificate exchange.

The driver will use the **trustStore** property value to look up the location of the trustStore file. Also, the driver will use the **hostNameInCertificate** property value to validate the TLS certificate.

If the server isn't configured to support encryption, the driver will raise an error and terminate the connection.
**encrypt** = true
**trustServerCertificate** = false or blank
**hostNameInCertificate** = value
**trustStore** = value
**trustStorePassword** = value
| The driver requests to use TLS encryption with the server.

If the server requires the client to support TLS encryption or if the server supports encryption, the driver will initiate the TLS certificate exchange.

The driver will use the **trustStore** property value to find the certificate trustStore file and **trustStorePassword** property value to check the integrity of the trustStore file. Also, the driver will use the **hostNameInCertificate** property value to validate the TLS certificate.

If the server isn't configured to support encryption, the driver will raise an error and terminate the connection.
**encrypt** = strict
**hostNameInCertificate** = value
**trustStore** = blank
**trustStorePassword** = blank
**serverCertificate** = value
| The driver requests to use TDS 8.0 `strict` TLS encryption with the server.

The driver will initiate the TLS handshake and certificate exchange with the server as the first action.

The **trustServerCertificate** setting is ignored and treated as false in `strict` mode.

The driver will use the optional **hostNameInCertificate** or **serverCertificate** properties to validate the server TLS certificate.

If the server isn't configured to support TDS 8.0 connections, the driver will raise an error and terminate the connection.
If the encrypt property is set to **true** , the Microsoft JDBC Driver for SQL Server uses the JVM's default JSSE security provider to negotiate TLS encryption with SQL Server. The default security provider may not support all of the features required to negotiate TLS encryption successfully. For example, the default security provider may not support the size of the RSA public key used in the SQL Server TLS certificate. In this case, the default security provider might raise an error that will cause the JDBC driver to terminate the connection. To resolve this issue, one of the following options can be used:
  * Configure the SQL Server with a server certificate that has a smaller RSA public key
  * Configure the JVM to use a different JSSE security provider in the "<java-home>/lib/security/java.security" security properties file
  * Use a different JVM


[](https://learn.microsoft.com/en-us/sql/connect/jdbc/understanding-ssl-support?view=sql-server-ver17#validating-server-tls-certificate)
## Validating server TLS certificate
During the TLS handshake, the server sends its public key certificate to the client. The JDBC driver or client has to validate that the server certificate is issued by a certificate authority the client trusts. The driver requires the server certificate to meet the following conditions:
  * The certificate was issued by a trusted certificate authority.
  * The certificate must be issued for server authentication.
  * The certificate isn't expired.
  * The Common Name (CN) in the Subject or a DNS name in the Subject Alternate Name (SAN) of the certificate exactly matches the **serverName** value specified in the connection string or, if specified, the **hostNameInCertificate** property value.
  * A DNS name can include wild-card characters. Prior version 7.2, the Microsoft JDBC Driver for SQL Server doesn't support wild-card matching. That is, abc.com won't match *.com but *.com will match *.com. With version 7.2 and up, standard certificate wild-card matching is supported.


For use of TDS 8.0 with `strict` encryption, the **serverCertificate** property value provides the path to a server certificate to be used for server certificate validation. This file must use the PEM file format. The certificate received from the server must match this certificate exactly.
[](https://learn.microsoft.com/en-us/sql/connect/jdbc/understanding-ssl-support?view=sql-server-ver17#see-also)
## See also
[Using encryption](https://learn.microsoft.com/en-us/sql/connect/jdbc/using-ssl-encryption?view=sql-server-ver17)
[Securing JDBC driver applications](https://learn.microsoft.com/en-us/sql/connect/jdbc/securing-jdbc-driver-applications?view=sql-server-ver17)
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
  * [ Configuring the client for encryption - JDBC Driver for SQL Server ](https://learn.microsoft.com/en-us/sql/connect/jdbc/configuring-the-client-for-ssl-encryption?source=recommendations)
Learn about client-side encryption and certificate trust to ensure the security of clients using the Microsoft JDBC Driver for SQL Server.
  * [ Connecting with encryption - JDBC Driver for SQL Server ](https://learn.microsoft.com/en-us/sql/connect/jdbc/connecting-with-ssl-encryption?source=recommendations)
Find examples of how to connect using TLS encryption in your Java application by using the JDBC driver for SQL Server.
  * [ Using encryption - JDBC Driver for SQL Server ](https://learn.microsoft.com/en-us/sql/connect/jdbc/using-ssl-encryption?source=recommendations)
Learn how to establish secure communication channels using TLS encryption with your SQL database connections.
  * [ Securing connection strings - JDBC Driver for SQL Server ](https://learn.microsoft.com/en-us/sql/connect/jdbc/securing-connection-strings?source=recommendations)
Learn how to secure connection string information when using the JDBC Driver for SQL Server.
  * [ Setting the connection properties - JDBC Driver for SQL Server ](https://learn.microsoft.com/en-us/sql/connect/jdbc/setting-the-connection-properties?source=recommendations)
The connection string properties for the Microsoft JDBC Driver for SQL Server can be specified in various ways.
  * [ Client Certificate Authentication for loopback scenarios - JDBC Driver for SQL Server ](https://learn.microsoft.com/en-us/sql/connect/jdbc/client-certification-authentication-for-loopback-scenarios?source=recommendations)
Learn how to use client certificates for authentication in loopback scenarios on SQL Server.
  * [ Building the connection URL with the Microsoft JDBC Driver for SQL Server - JDBC Driver for SQL Server ](https://learn.microsoft.com/en-us/sql/connect/jdbc/building-the-connection-url?source=recommendations)
Learn about formatting the connection string used by the Microsoft JDBC Driver for SQL Server. Samples of connection strings are included in the examples section.


Show 4 more
Module
[ Protect data in-transit and at rest - Training ](https://learn.microsoft.com/en-us/training/modules/protect-data-transit-rest/?source=recommendations)
Protect data in-transit and at rest
Certification
[ Microsoft Certified: Azure Database Administrator Associate - Certifications ](https://learn.microsoft.com/en-us/credentials/certifications/azure-database-administrator-associate/?source=recommendations)
Administer an SQL Server database infrastructure for cloud, on-premises and hybrid relational databases using the Microsoft PaaS relational database offerings.
Mar 8, 4 PM - Mar 8, 4 PM
Experiment with what's next in AI-driven apps and agent design
* * *
  * Last updated on 06/25/2024


Ask Learn is an AI assistant that can answer questions, clarify concepts, and define terms using trusted Microsoft documentation.
Please sign in to use Ask Learn.
[ Sign in ](https://learn.microsoft.com/en-us/sql/connect/jdbc/understanding-ssl-support?view=sql-server-ver17)
